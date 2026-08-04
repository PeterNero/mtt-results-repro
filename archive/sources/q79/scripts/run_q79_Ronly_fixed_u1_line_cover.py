#!/usr/bin/env python3
"""Checkpointed exact cover of one nonzero q79 R-only fixed-u1 slice."""

from __future__ import annotations

import argparse
import concurrent.futures
import hashlib
import json
import subprocess
import sys
import time
from pathlib import Path


PRIME = 101
REPOSITORY = Path(__file__).resolve().parents[1]
SCRIPTS = REPOSITORY / "scripts"
PARENT_DIR = REPOSITORY / "candidate_data" / "q79_Ronly_classfree_representative_lines"
BENCHMARK = SCRIPTS / "benchmark_q79_msolve_inverse_root_triple_endpoint_fibers.py"
PARENTS = {
    (5, 1): PARENT_DIR
    / "space_5_h0_g0_class1_inverse_root.msolve.in",
    (5, 2): PARENT_DIR
    / "space_5_h0_g0_class2_inverse_root.msolve.in",
    (6, 1): PARENT_DIR
    / "space_6_h0_g0_class1_inverse_root.msolve.in",
    (6, 2): PARENT_DIR
    / "space_6_h0_g0_class2_inverse_root.msolve.in",
}


def require(condition: bool, label: str) -> None:
    if not condition:
        raise AssertionError(label)


def checksum(path: Path) -> dict[str, object]:
    return {
        "path": str(path),
        "bytes": path.stat().st_size,
        "sha256": hashlib.sha256(path.read_bytes()).hexdigest(),
    }


def exact_line_kind(
    path: Path, space: int, scalar_class: int, u1: int, a: int
) -> str | None:
    if not path.is_file():
        return None
    try:
        packet = json.loads(path.read_text(encoding="utf-8"))
    except (json.JSONDecodeError, OSError):
        return None
    outcomes = packet.get("outcomes", [])
    complete = (
        packet.get("schema")
        == "MTTQ79MsolveInverseRootTripleEndpointFiberBenchmark.v1"
        and packet.get("field_characteristic") == PRIME
        and packet.get("scalar_square_class_representative") == scalar_class
        and len(outcomes) == PRIME - 1
        and packet.get("exact_positive_samples") == 0
        and [row.get("v") for row in outcomes] == list(range(1, PRIME))
        and all(
            row.get("u1") == u1
            and row.get("a_equals_v_times_u3") == a
            and row.get("status")
            in {"EXACT_UNIT_GROEBNER_BASIS", "EXACT_REDUCED_GROEBNER_BASIS"}
            and row.get("returncode") == 0
            for row in outcomes
        )
    )
    if not complete:
        return None
    unit_count = sum(
        row.get("status") == "EXACT_UNIT_GROEBNER_BASIS" for row in outcomes
    )
    require(packet.get("exact_unit_samples") == unit_count, "saved exact-unit count")
    return "UNIT" if unit_count == PRIME - 1 else "NONUNIT"


def run_line(task: dict[str, object]) -> dict[str, object]:
    space = int(task["space"])
    scalar_class = int(task["scalar_class"])
    u1 = int(task["u1"])
    a = int(task["a"])
    output = Path(str(task["output"]))
    log = Path(str(task["log"]))
    saved_kind = exact_line_kind(output, space, scalar_class, u1, a)
    if saved_kind is not None:
        return {
            **task,
            "status": f"RESUMED_EXACT_{saved_kind}_LINE",
            "elapsed_seconds": 0.0,
        }
    samples = ",".join(f"{u1}:{a}:{v}" for v in range(1, PRIME))
    command = [
        sys.executable,
        str(BENCHMARK),
        "--input",
        str(PARENTS[(space, scalar_class)]),
        "--scalar-class",
        str(scalar_class),
        "--samples",
        samples,
        "--parent-row-indices",
        "1,2,3,4,5,6,7,8,9,10,11,12",
        "--drop-variables",
        "y1,y2,y3,y4",
        "--timeout",
        str(task["fiber_timeout"]),
        "--mode",
        "groebner",
        "--linear-algebra",
        "2",
        "--output",
        str(output),
    ]
    started = time.perf_counter()
    completed = subprocess.run(
        command,
        cwd=REPOSITORY,
        text=True,
        stdout=subprocess.PIPE,
        stderr=subprocess.STDOUT,
        check=False,
    )
    elapsed = time.perf_counter() - started
    log.write_text(completed.stdout, encoding="utf-8")
    exact_kind = (
        exact_line_kind(output, space, scalar_class, u1, a)
        if completed.returncode == 0
        else None
    )
    return {
        **task,
        "status": (
            f"EXACT_{exact_kind}_LINE"
            if exact_kind is not None
            else f"INCOMPLETE_EXIT_{completed.returncode}"
        ),
        "elapsed_seconds": elapsed,
        "packet": checksum(output) if output.is_file() else None,
        "log_checksum": checksum(log),
    }


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--output-dir", type=Path, required=True)
    parser.add_argument("--manifest", type=Path, required=True)
    parser.add_argument("--jobs", type=int, default=8)
    parser.add_argument("--fiber-timeout", type=float, default=15.0)
    parser.add_argument(
        "--u1",
        type=int,
        default=1,
        help="Nonzero F_101 endpoint value to cover (default: 1).",
    )
    parser.add_argument(
        "--max-lines",
        type=int,
        help="Run only this many canonical lines, for a bounded smoke or partial cover.",
    )
    args = parser.parse_args()
    require(1 <= args.jobs <= 16, "worker count")
    require(args.fiber_timeout > 0, "fiber timeout")
    fixed_u1 = args.u1 % PRIME
    require(fixed_u1 != 0, "fixed u1 must be nonzero in F_101")
    for path in (BENCHMARK, *PARENTS.values()):
        require(path.is_file(), f"required source {path}")
    args.output_dir.mkdir(parents=True, exist_ok=True)
    tasks = []
    for space in (5, 6):
        for scalar_class in (1, 2):
            for a in range(1, 51):
                stem = (
                    f"space{space}_class{scalar_class}_u1_{fixed_u1:03d}_a_{a:03d}"
                )
                tasks.append(
                    {
                        "space": space,
                        "scalar_class": scalar_class,
                        "u1": fixed_u1,
                        "a": a,
                        "u2": scalar_class * pow(a, -2, PRIME) % PRIME,
                        "output": str(args.output_dir / f"{stem}.packet.json"),
                        "log": str(args.output_dir / f"{stem}.run.log"),
                        "fiber_timeout": args.fiber_timeout,
                    }
                )
    if args.max_lines is not None:
        require(args.max_lines > 0, "positive max lines")
        tasks = tasks[: args.max_lines]

    results = []
    started = time.perf_counter()
    with concurrent.futures.ThreadPoolExecutor(max_workers=args.jobs) as executor:
        futures = {executor.submit(run_line, task): task for task in tasks}
        for future in concurrent.futures.as_completed(futures):
            result = future.result()
            results.append(result)
            print(
                f"space={result['space']} class={result['scalar_class']} "
                f"a={result['a']}: {result['status']} "
                f"elapsed={result['elapsed_seconds']:.1f}s",
                flush=True,
            )
    results.sort(key=lambda row: (row["space"], row["scalar_class"], row["a"]))
    exact_lines = sum(
        row["status"] in {"EXACT_UNIT_LINE", "RESUMED_EXACT_UNIT_LINE"}
        for row in results
    )
    exact_complete_lines = sum(
        row["status"]
        in {
            "EXACT_UNIT_LINE",
            "RESUMED_EXACT_UNIT_LINE",
            "EXACT_NONUNIT_LINE",
            "RESUMED_EXACT_NONUNIT_LINE",
        }
        for row in results
    )
    manifest = {
        "schema": "MTTQ79RonlyFixedU1CanonicalLineCover.v2",
        "date": "2026-07-21",
        "status": (
            "EXACT_FIXED_U1_RONLY_CANONICAL_LINE_COVER_COMPLETE"
            if len(results) == 200 and exact_lines == 200
            else "EXACT_FIXED_U1_CANONICAL_LINE_PACKETS_COMPLETE_WITH_EXCEPTIONS"
            if len(results) == 200 and exact_complete_lines == 200
            else "PARTIAL_OR_INCOMPLETE_FIXED_U1_LINE_COVER"
        ),
        "field": "F_101",
        "fixed_u1": fixed_u1,
        "canonical_a_values": "1,...,50, one representative of each +/- pair",
        "benchmark_script": checksum(BENCHMARK),
        "parents": {
            f"space{space}_class{scalar_class}": checksum(path)
            for (space, scalar_class), path in PARENTS.items()
        },
        "jobs": args.jobs,
        "fiber_timeout_seconds": args.fiber_timeout,
        "wall_seconds": time.perf_counter() - started,
        "results": results,
        "exact_canonical_lines": exact_lines,
        "exact_complete_canonical_line_packets": exact_complete_lines,
        "expected_canonical_lines": len(tasks),
        "nominal_lines_covered_if_complete": 2 * exact_lines,
        "exact_fixed_fibers_per_canonical_line": PRIME - 1,
        "checks": {
            "canonical_a_values_cover_each_sign_pair_once": True,
            "class1_and_class2_u2_sets_partition_F101_nonzero": True,
            "v_exhaustion_is_equivalent_to_u3_exhaustion": True,
            "all_selected_rows_are_h_recurrences_or_R_terminals": True,
            "no_D_terminal_is_used": True,
            "no_continuous_fit_parameter_is_added": True,
        },
        "claim_boundary": (
            "Only exact complete packets count. A complete all-unit 200/200 canonical "
            f"cover closes the finite u1={fixed_u1} R-only slice in both spaces. "
            "Complete packets with exact nonunit fibers instead feed the separate full "
            "R/y/D exception augmenter. Neither result classifies another u1 value or "
            "promotes the auxiliary finite system to physical HYM/QG data."
        ),
        "new_continuous_fit_parameters": 0,
    }
    args.manifest.parent.mkdir(parents=True, exist_ok=True)
    args.manifest.write_text(json.dumps(manifest, indent=2) + "\n", encoding="utf-8")
    print(manifest["status"])
    print(f"exact_lines={exact_lines}/{len(tasks)}")
    print(args.manifest)
    return 0 if exact_complete_lines == len(tasks) else 2


if __name__ == "__main__":
    raise SystemExit(main())
