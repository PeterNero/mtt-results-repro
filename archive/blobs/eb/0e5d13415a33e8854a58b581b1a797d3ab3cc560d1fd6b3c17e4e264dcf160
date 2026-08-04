#!/usr/bin/env python3
"""Close exact R-only line exceptions with the complete q79 R/y/D parent."""

from __future__ import annotations

import argparse
import concurrent.futures
import hashlib
import json
import re
import subprocess
import sys
from pathlib import Path


PRIME = 101
REPOSITORY = Path(__file__).resolve().parents[1]
SCRIPTS = REPOSITORY / "scripts"
PARENT_DIR = REPOSITORY / "candidate_data" / "q79_Ronly_classfree_representative_lines"
BENCHMARK = SCRIPTS / "benchmark_q79_msolve_inverse_root_triple_endpoint_fibers.py"
FULL_PARENT_ROWS = tuple(index for index in range(22) if index not in {0, 13})
PARENTS = {
    (space, scalar_class): PARENT_DIR
    / f"space_{space}_h0_g0_class{scalar_class}_inverse_root.msolve.in"
    for space in (5, 6)
    for scalar_class in (1, 2)
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


def parse_line_identity(path: Path) -> tuple[int, int, int, int]:
    match = re.fullmatch(
        r"space(5|6)_class(1|2)_u1_(\d{3})_a_(\d{3})\.packet\.json",
        path.name,
    )
    require(match is not None, f"canonical line packet name {path.name}")
    return tuple(int(match.group(index)) for index in range(1, 5))


def load_completed_line(path: Path) -> dict[str, object] | None:
    try:
        packet = json.loads(path.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError):
        return None
    if packet.get("schema") != "MTTQ79MsolveInverseRootTripleEndpointFiberBenchmark.v1":
        return None
    space, scalar_class, u1_value, a_value = parse_line_identity(path)
    outcomes = packet.get("outcomes", [])
    exact_statuses = {"EXACT_UNIT_GROEBNER_BASIS", "EXACT_REDUCED_GROEBNER_BASIS"}
    if not (
        packet.get("field_characteristic") == PRIME
        and packet.get("scalar_square_class_representative") == scalar_class
        and packet.get("selected_parent_row_indices") == list(range(1, 13))
        and packet.get("dropped_source_variables") == ["y1", "y2", "y3", "y4"]
        and len(outcomes) == PRIME - 1
        and [row.get("v") for row in outcomes] == list(range(1, PRIME))
        and all(
            row.get("u1") == u1_value
            and row.get("a_equals_v_times_u3") == a_value
            and row.get("returncode") == 0
            and row.get("status") in exact_statuses
            for row in outcomes
        )
    ):
        return None
    exceptions = [
        {
            "space": space,
            "scalar_class": scalar_class,
            "u1": u1_value,
            "a": a_value,
            "v": int(row["v"]),
            "R_status": row["status"],
            "R_output_sha256": row["output_sha256"],
        }
        for row in outcomes
        if row["status"] == "EXACT_REDUCED_GROEBNER_BASIS"
    ]
    require(
        packet.get("exact_unit_samples") == len(outcomes) - len(exceptions),
        "line exact-unit count",
    )
    return {
        "space": space,
        "scalar_class": scalar_class,
        "u1": u1_value,
        "a": a_value,
        "packet": checksum(path),
        "exact_R_unit_fibers": len(outcomes) - len(exceptions),
        "R_exceptions": exceptions,
    }


def index_full_parent_units(
    directory: Path,
) -> dict[tuple[int, int, int, int, int], dict[str, object]]:
    result: dict[tuple[int, int, int, int, int], dict[str, object]] = {}
    for path in sorted(directory.glob("*.full_RD.packet.json")):
        try:
            packet = json.loads(path.read_text(encoding="utf-8"))
        except (OSError, json.JSONDecodeError):
            continue
        if not (
            packet.get("schema") == "MTTQ79MsolveInverseRootTripleEndpointFiberBenchmark.v1"
            and packet.get("field_characteristic") == PRIME
            and packet.get("selected_parent_row_indices") == list(FULL_PARENT_ROWS)
            and packet.get("dropped_source_variables") == []
        ):
            continue
        input_name = Path(packet.get("input", {}).get("path", "")).name
        match = re.search(r"space_(5|6).*class(1|2)", input_name)
        if match is None:
            continue
        space, scalar_class = int(match.group(1)), int(match.group(2))
        for outcome_index, outcome in enumerate(packet.get("outcomes", [])):
            if not (
                outcome.get("status") == "EXACT_UNIT_GROEBNER_BASIS"
                and outcome.get("returncode") == 0
                and "[1]:" in outcome.get("output_text", "")
            ):
                continue
            key = (
                space,
                scalar_class,
                int(outcome["u1"]),
                int(outcome["a_equals_v_times_u3"]),
                int(outcome["v"]),
            )
            result[key] = {
                "packet": checksum(path),
                "outcome_index": outcome_index,
                "elapsed_seconds": outcome["elapsed_seconds"],
                "output_sha256": outcome["output_sha256"],
            }
    return result


def run_exception(task: dict[str, object]) -> dict[str, object]:
    space = int(task["space"])
    scalar_class = int(task["scalar_class"])
    u1_value = int(task["u1"])
    a_value = int(task["a"])
    v_value = int(task["v"])
    output = Path(str(task["output"]))
    command = [
        sys.executable,
        str(BENCHMARK),
        "--input",
        str(PARENTS[(space, scalar_class)]),
        "--scalar-class",
        str(scalar_class),
        "--samples",
        f"{u1_value}:{a_value}:{v_value}",
        "--timeout",
        str(task["timeout"]),
        "--output",
        str(output),
    ]
    completed = subprocess.run(
        command,
        cwd=REPOSITORY,
        text=True,
        stdout=subprocess.PIPE,
        stderr=subprocess.STDOUT,
        check=False,
    )
    log = output.with_suffix(".run.log")
    log.write_text(completed.stdout, encoding="utf-8")
    return {
        **task,
        "returncode": completed.returncode,
        "packet": checksum(output) if output.is_file() else None,
        "log": checksum(log),
    }


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--line-cover-dir", type=Path, required=True)
    parser.add_argument("--exception-dir", type=Path, required=True)
    parser.add_argument("--sign-certificate", type=Path, required=True)
    parser.add_argument("--manifest", type=Path, required=True)
    parser.add_argument("--jobs", type=int, default=2)
    parser.add_argument("--timeout", type=float, default=600.0)
    parser.add_argument(
        "--u1",
        type=int,
        default=1,
        help="Nonzero F_101 endpoint value whose line packets are augmented.",
    )
    args = parser.parse_args()
    require(1 <= args.jobs <= 4 and args.timeout > 0, "execution bounds")
    fixed_u1 = args.u1 % PRIME
    require(fixed_u1 != 0, "fixed u1 must be nonzero in F_101")
    for path in (BENCHMARK, args.sign_certificate, *PARENTS.values()):
        require(path.is_file(), f"required source {path}")
    sign = json.loads(args.sign_certificate.read_text(encoding="utf-8"))
    require(
        sign.get("status") == "EXACT_FULL_PARENT_SIGN_INVOLUTION_AND_CANONICAL_A_COVER"
        and all(sign.get("checks", {}).values()),
        "exact sign involution certificate",
    )
    args.exception_dir.mkdir(parents=True, exist_ok=True)

    line_paths = sorted(
        args.line_cover_dir.glob(
            f"space*_class*_u1_{fixed_u1:03d}_a_*.packet.json"
        )
    )
    completed_lines = []
    incomplete_paths = []
    for path in line_paths:
        row = load_completed_line(path)
        if row is None:
            incomplete_paths.append(str(path))
        else:
            completed_lines.append(row)

    units = index_full_parent_units(args.exception_dir)
    tasks = []
    for line in completed_lines:
        for exception in line["R_exceptions"]:
            key = (
                int(exception["space"]),
                int(exception["scalar_class"]),
                int(exception["u1"]),
                int(exception["a"]),
                int(exception["v"]),
            )
            if key in units:
                continue
            stem = (
                f"space{key[0]}_class{key[1]}_u1_{key[2]:03d}_"
                f"a_{key[3]:03d}_v_{key[4]:03d}.full_RD.packet.json"
            )
            tasks.append(
                {
                    **exception,
                    "timeout": args.timeout,
                    "output": str(args.exception_dir / stem),
                }
            )
    with concurrent.futures.ThreadPoolExecutor(max_workers=args.jobs) as executor:
        futures = [executor.submit(run_exception, task) for task in tasks]
        for future in concurrent.futures.as_completed(futures):
            result = future.result()
            print(
                f"space={result['space']} class={result['scalar_class']} "
                f"a={result['a']} v={result['v']}: exit={result['returncode']}",
                flush=True,
            )

    units = index_full_parent_units(args.exception_dir)
    closed_lines = []
    open_exceptions = []
    for line in completed_lines:
        witnesses = []
        for exception in line["R_exceptions"]:
            key = (
                int(exception["space"]),
                int(exception["scalar_class"]),
                int(exception["u1"]),
                int(exception["a"]),
                int(exception["v"]),
            )
            witness = units.get(key)
            if witness is None:
                open_exceptions.append(exception)
            else:
                witnesses.append(exception | {"full_RD_unit_witness": witness})
        line["full_RD_unit_exceptions"] = witnesses
        line["status"] = (
            "EXACT_F101_LINE_CLOSED_BY_R_OR_FULL_RD"
            if len(witnesses) == len(line["R_exceptions"])
            else "OPEN_R_EXCEPTION_WITHOUT_FULL_RD_UNIT"
        )
        if line["status"] == "EXACT_F101_LINE_CLOSED_BY_R_OR_FULL_RD":
            closed_lines.append(line)

    expected_lines = 4 * 50
    complete = (
        len(completed_lines) == expected_lines
        and len(closed_lines) == expected_lines
        and not open_exceptions
        and not incomplete_paths
    )
    chart_accounting = {}
    for space in (5, 6):
        for scalar_class in (1, 2):
            chart_lines = [
                line
                for line in completed_lines
                if line["space"] == space and line["scalar_class"] == scalar_class
            ]
            chart_closed = [
                line
                for line in chart_lines
                if line["status"] == "EXACT_F101_LINE_CLOSED_BY_R_OR_FULL_RD"
            ]
            chart_accounting[f"space{space}_class{scalar_class}"] = {
                "expected_canonical_lines": 50,
                "completed_exact_R_line_packets": len(chart_lines),
                "closed_canonical_lines_by_R_or_full_RD": len(chart_closed),
                "R_only_exceptional_fibers": sum(
                    len(line["R_exceptions"]) for line in chart_lines
                ),
                "full_RD_unit_exceptional_fibers": sum(
                    len(line["full_RD_unit_exceptions"]) for line in chart_lines
                ),
                "status": (
                    "EXACT_F101_FIXED_U1_CHART_CLOSED"
                    if len(chart_closed) == 50
                    else "CHECKPOINT"
                ),
            }
    space_accounting = {}
    for space in (5, 6):
        keys = [f"space{space}_class1", f"space{space}_class2"]
        completed_for_space = sum(
            chart_accounting[key]["completed_exact_R_line_packets"] for key in keys
        )
        closed_for_space = sum(
            chart_accounting[key]["closed_canonical_lines_by_R_or_full_RD"]
            for key in keys
        )
        space_accounting[f"space{space}"] = {
            "expected_canonical_lines": 100,
            "completed_exact_R_line_packets": completed_for_space,
            "closed_canonical_lines_by_R_or_full_RD": closed_for_space,
            "status": (
                "EXACT_F101_FIXED_U1_FULL_RD_SPACE_SLICE_CLOSED"
                if closed_for_space == 100
                else "CHECKPOINT"
            ),
        }
    completed_spaces = [
        key
        for key, row in space_accounting.items()
        if row["status"] == "EXACT_F101_FIXED_U1_FULL_RD_SPACE_SLICE_CLOSED"
    ]
    checks = {
        "sign_involution_covers_each_nonzero_a_pair_exactly": True,
        "only_complete_100_fiber_R_packets_are_admitted": True,
        "every_admitted_R_outcome_is_an_exact_reduced_Groebner_basis": True,
        "every_nonunit_R_exception_requires_a_literal_full_parent_unit_basis": not open_exceptions,
        "full_parent_witnesses_restore_all_y_and_D_rows": True,
        "no_timeout_or_incomplete_output_is_promoted": True,
        "no_continuous_fit_parameter_is_added": True,
    }
    manifest = {
        "schema": "MTTQ79RonlyFixedU1DAugmentedCanonicalLineCover.v2",
        "date": "2026-07-21",
        "status": (
            "EXACT_F101_FIXED_U1_FULL_RD_SLICE_CLOSED"
            if complete
            else "EXACT_F101_FIXED_U1_FULL_RD_SPACE_SLICE_CLOSED_CHECKPOINT"
            if completed_spaces
            else "EXACT_D_AUGMENTED_FIXED_U1_CHECKPOINT"
        ),
        "field": "F_101",
        "fixed_u1": fixed_u1,
        "sign_involution_certificate": checksum(args.sign_certificate),
        "parents": {
            f"space{space}_class{scalar_class}": checksum(path)
            for (space, scalar_class), path in PARENTS.items()
        },
        "accounting": {
            "expected_canonical_lines": expected_lines,
            "discovered_line_packets": len(line_paths),
            "completed_exact_R_line_packets": len(completed_lines),
            "closed_canonical_lines_by_R_or_full_RD": len(closed_lines),
            "nominal_signed_lines_closed": 2 * len(closed_lines),
            "R_only_exceptional_fibers": sum(
                len(line["R_exceptions"]) for line in completed_lines
            ),
            "full_RD_unit_exceptional_fibers": sum(
                len(line["full_RD_unit_exceptions"]) for line in completed_lines
            ),
            "open_exceptional_fibers": len(open_exceptions),
            "incomplete_or_invalid_line_packets": len(incomplete_paths),
            "complete_space_slices": completed_spaces,
        },
        "chart_accounting": chart_accounting,
        "space_accounting": space_accounting,
        "line_records": completed_lines,
        "open_exceptions": open_exceptions,
        "incomplete_or_invalid_line_packets": incomplete_paths,
        "checks": checks,
        "theorem_if_complete": (
            f"For u1={fixed_u1}, every F_101 point in all four inverse-root charts "
            "lies on one "
            "canonical a-line or its exact sign partner. Every R-only fiber is either "
            "unit or an exact nonunit exception whose complete R/y/D parent is unit. "
            f"Therefore the simultaneous full R/D u1={fixed_u1} finite slice is empty."
        ),
        "theorem_for_each_complete_space": (
            "For each space listed in complete_space_slices, both scalar classes and "
            "all 50 canonical a values are exact. The sign involution supplies their "
            "partners, v=1,...,100 exhausts every nonzero u3, and every R exception "
            "has a literal full-parent unit basis. Therefore that space's simultaneous "
            f"R/D u1={fixed_u1} finite slice is empty over F_101."
        ),
        "claim_boundary": (
            "A checkpoint closes only its displayed completed canonical lines. The "
            "full fixed-u1 theorem requires 200/200 closed canonical lines. Even that "
            "does not classify the other 99 nonzero u1 values, characteristic zero, "
            "or physical HYM/QG promotion."
        ),
        "new_continuous_fit_parameters": 0,
    }
    args.manifest.parent.mkdir(parents=True, exist_ok=True)
    args.manifest.write_text(json.dumps(manifest, indent=2) + "\n", encoding="utf-8")
    print(manifest["status"])
    print(
        f"closed_lines={len(closed_lines)}/{expected_lines}; "
        f"R_exceptions={manifest['accounting']['R_only_exceptional_fibers']}; "
        f"full_RD_units={manifest['accounting']['full_RD_unit_exceptional_fibers']}"
    )
    print(args.manifest)
    return 0 if not open_exceptions else 2


if __name__ == "__main__":
    raise SystemExit(main())
