#!/usr/bin/env python3
"""Checkpointed exact msolve cover of one q79 fixed-u1 symbolic-u2 family."""

from __future__ import annotations

import argparse
import concurrent.futures
import hashlib
import json
import os
import re
import subprocess
import time
from pathlib import Path


PRIME = 101
ROOT = Path(__file__).resolve().parents[1]
DEFAULT_MSOLVE = Path("/home/nerodes/.local/opt/msolve-0.10.1/msolve")
VARIABLES = (
    "h1",
    "h2",
    "h3",
    "h4",
    "h5",
    "h6",
    "u3",
    "u4",
    "u5",
    "u6",
    "u7",
    "t",
)


def require(condition: bool, label: str) -> None:
    if not condition:
        raise AssertionError(label)


def checksum(path: Path) -> dict[str, object]:
    return {
        "path": str(path),
        "bytes": path.stat().st_size,
        "sha256": hashlib.sha256(path.read_bytes()).hexdigest(),
    }


def resolve_artifact(path_text: str) -> Path:
    path = Path(path_text.replace("\\", "/"))
    return path if path.is_absolute() else ROOT / path


def validate_input(path: Path, expected: dict[str, object]) -> None:
    require(path.is_file(), f"symbolic input {path}")
    require(checksum(path)["sha256"] == expected["sha256"], "input checksum")
    lines = path.read_text(encoding="ascii").replace("\r\n", "\n").splitlines()
    require(tuple(lines[0].split(",")) == VARIABLES, "variable order")
    require(int(lines[1]) == PRIME, "field characteristic")
    rows = "\n".join(lines[2:]).rstrip().removesuffix(",").split(",\n")
    require(len(rows) == 13, "13 symbolic rows")
    require(rows[-1] in {"u3*t + 100", "t*u3 + 100"}, "nonzero-u3 saturation")


def classify_output(path: Path) -> str | None:
    if not path.is_file() or path.stat().st_size == 0:
        return None
    text = path.read_text(encoding="utf-8", errors="strict")
    if not (
        text.startswith("#Reduced Groebner basis data")
        and "#field characteristic: 101" in text
        and "#variable order:       " + ", ".join(VARIABLES) in text
        and text.rstrip().endswith("]:")
    ):
        return None
    length = re.search(r"#length of basis:\s+(\d+) element", text)
    require(length is not None and int(length.group(1)) >= 1, "basis length")
    return "UNIT" if re.search(r"\[1\]:\s*$", text) is not None else "NONUNIT"


def run_line(task: dict[str, object]) -> dict[str, object]:
    input_path = Path(str(task["input_path"]))
    output_path = input_path.with_suffix(".out")
    log_path = input_path.with_suffix(".log")
    saved = classify_output(output_path)
    if saved is not None:
        return {
            **task,
            "status": f"RESUMED_EXACT_{saved}_SYMBOLIC_LINE",
            "elapsed_seconds": 0.0,
            "output": checksum(output_path),
            "log": checksum(log_path) if log_path.is_file() else None,
        }

    command = [
        "prlimit",
        f"--as={int(task['memory_mib']) * 1024 * 1024}",
        "--",
        str(task["msolve"]),
        "-t",
        "1",
        "-l",
        "2",
        "-d",
        "0",
        "-c",
        "0",
        "-g",
        "2",
        "-f",
        str(input_path),
        "-o",
        str(output_path),
        "-v",
        "1",
        "-q",
        "0",
    ]
    environment = os.environ.copy()
    for name in ("OMP_NUM_THREADS", "OPENBLAS_NUM_THREADS", "MKL_NUM_THREADS"):
        environment[name] = "1"
    started = time.perf_counter()
    timed_out = False
    try:
        completed = subprocess.run(
            command,
            cwd=ROOT,
            env=environment,
            text=True,
            stdout=subprocess.PIPE,
            stderr=subprocess.STDOUT,
            timeout=float(task["timeout"]),
            check=False,
        )
        returncode = completed.returncode
        transcript = completed.stdout
    except subprocess.TimeoutExpired as error:
        timed_out = True
        returncode = None
        transcript = error.stdout or ""
        if isinstance(transcript, bytes):
            transcript = transcript.decode("utf-8", errors="replace")
        transcript += "\nQ79_SYMBOLIC_LINE_TIMEOUT\n"
    elapsed = time.perf_counter() - started
    log_path.write_text(transcript, encoding="utf-8", newline="\n")
    exact = classify_output(output_path) if returncode == 0 and not timed_out else None
    return {
        **task,
        "status": (
            f"EXACT_{exact}_SYMBOLIC_LINE"
            if exact is not None
            else "INCOMPLETE_TIMEOUT"
            if timed_out
            else f"INCOMPLETE_EXIT_{returncode}"
        ),
        "elapsed_seconds": elapsed,
        "returncode": returncode,
        "timed_out": timed_out,
        "output": checksum(output_path) if output_path.is_file() else None,
        "log": checksum(log_path),
    }


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--family-packet", type=Path, required=True)
    parser.add_argument("--manifest", type=Path, required=True)
    parser.add_argument("--msolve", type=Path, default=DEFAULT_MSOLVE)
    parser.add_argument("--jobs", type=int, default=2)
    parser.add_argument("--timeout", type=float, default=900.0)
    parser.add_argument("--memory-mib", type=int, default=4096)
    parser.add_argument("--max-lines", type=int)
    args = parser.parse_args()
    require(1 <= args.jobs <= 4, "worker count")
    require(args.timeout > 0 and args.memory_mib >= 512, "resource bounds")
    require(args.family_packet.is_file() and args.msolve.is_file(), "required inputs")

    family = json.loads(args.family_packet.read_text(encoding="utf-8"))
    require(
        family.get("schema") == "MTTQ79RonlyFixedU1U2SymbolicFamily.v1"
        and family.get("status") == "EXACT_100_NONZERO_U2_SYMBOLIC_INPUTS_EMITTED",
        "exact family packet",
    )
    records = family.get("records", [])
    require(
        len(records) == 100
        and [row.get("u2") for row in records] == list(range(1, PRIME)),
        "ordered nonzero u2 exhaustion",
    )
    tasks = []
    for record in records:
        input_path = resolve_artifact(str(record["input"]["path"]))
        validate_input(input_path, record["input"])
        tasks.append(
            {
                "space": int(family["space_index"]),
                "u1": int(family["fixed_u1"]),
                "u2": int(record["u2"]),
                "input_path": str(input_path),
                "input": checksum(input_path),
                "msolve": str(args.msolve),
                "timeout": args.timeout,
                "memory_mib": args.memory_mib,
            }
        )
    if args.max_lines is not None:
        require(args.max_lines > 0, "positive max-lines")
        tasks = tasks[: args.max_lines]

    results = []
    started = time.perf_counter()
    with concurrent.futures.ThreadPoolExecutor(max_workers=args.jobs) as executor:
        futures = [executor.submit(run_line, task) for task in tasks]
        for future in concurrent.futures.as_completed(futures):
            result = future.result()
            results.append(result)
            print(
                f"space={result['space']} u1={result['u1']} u2={result['u2']}: "
                f"{result['status']} elapsed={result['elapsed_seconds']:.1f}s",
                flush=True,
            )
    results.sort(key=lambda row: int(row["u2"]))
    exact = [
        row
        for row in results
        if row["status"]
        in {
            "EXACT_UNIT_SYMBOLIC_LINE",
            "RESUMED_EXACT_UNIT_SYMBOLIC_LINE",
            "EXACT_NONUNIT_SYMBOLIC_LINE",
            "RESUMED_EXACT_NONUNIT_SYMBOLIC_LINE",
        }
    ]
    units = [row for row in exact if "_UNIT_SYMBOLIC_LINE" in row["status"]]
    nonunits = [row for row in exact if "_NONUNIT_SYMBOLIC_LINE" in row["status"]]
    complete = len(tasks) == 100 and len(exact) == 100
    manifest = {
        "schema": "MTTQ79RonlyFixedU1U2SymbolicCover.v1",
        "date": "2026-07-21",
        "status": (
            "EXACT_100_U2_SYMBOLIC_LINES_CLASSIFIED"
            if complete
            else "PARTIAL_OR_INCOMPLETE_U2_SYMBOLIC_COVER"
        ),
        "field": "F_101",
        "space_index": int(family["space_index"]),
        "fixed_u1": int(family["fixed_u1"]),
        "family_packet": checksum(args.family_packet),
        "msolve": checksum(args.msolve),
        "jobs": args.jobs,
        "timeout_seconds": args.timeout,
        "memory_mib_per_worker": args.memory_mib,
        "wall_seconds": time.perf_counter() - started,
        "results": results,
        "accounting": {
            "requested_symbolic_lines": len(tasks),
            "exact_classified_symbolic_lines": len(exact),
            "exact_unit_symbolic_lines": len(units),
            "exact_nonunit_symbolic_lines": len(nonunits),
            "incomplete_symbolic_lines": len(tasks) - len(exact),
            "fixed_F101_fibers_represented_by_exact_lines": 100 * len(exact),
        },
        "nonunit_lines_requiring_full_R_y_D_closure": [
            {"space": row["space"], "u1": row["u1"], "u2": row["u2"]}
            for row in nonunits
        ],
        "checks": {
            "family_packet_hash_binds_all_inputs": True,
            "all_inputs_are_12_variable_13_row_saturated_cubic_lines": True,
            "only_literal_complete_reduced_Groebner_outputs_are_classified": True,
            "one_symbolic_line_represents_all_100_nonzero_u3_values": True,
            "nonunit_R_lines_are_not_promoted_to_full_parent_closure": True,
            "no_continuous_fit_parameter_is_added": True,
        },
        "claim_boundary": (
            "A unit line closes its full nonzero Laurent coordinate over every field "
            "extension. A nonunit R line remains open until a complete R/y/D unit "
            "witness is supplied. A partial manifest asserts only its exact outputs."
        ),
        "new_continuous_fit_parameters": 0,
    }
    args.manifest.parent.mkdir(parents=True, exist_ok=True)
    args.manifest.write_text(json.dumps(manifest, indent=2) + "\n", encoding="utf-8")
    print(manifest["status"])
    print(
        f"exact={len(exact)}/{len(tasks)}; units={len(units)}; "
        f"nonunits={len(nonunits)}"
    )
    print(args.manifest)
    return 0 if len(exact) == len(tasks) else 2


if __name__ == "__main__":
    raise SystemExit(main())
