#!/usr/bin/env python3
"""Benchmark exact Singular saturations for pairs of finite-field coordinates."""

from __future__ import annotations

import argparse
import hashlib
import itertools
import json
import os
import re
import statistics
import subprocess
import tempfile
import time
from pathlib import Path


SINGULAR_ROOT = Path("/home/nerodes/.local/opt/singular-4.4.1/root")
SINGULAR = SINGULAR_ROOT / "usr/bin/Singular"
SINGULAR_LIBRARY = SINGULAR_ROOT / "usr/lib/x86_64-linux-gnu"
SINGULAR_MODULES = SINGULAR_LIBRARY / "singular/MOD"
SINGULAR_PATH = SINGULAR_ROOT / "usr/share/singular/LIB"


def parse_msolve_input(path: Path) -> tuple[list[str], int, list[str]]:
    lines = path.read_text(encoding="ascii").replace("\r\n", "\n").splitlines()
    if len(lines) < 4:
        raise ValueError("input must contain a ring, field, and at least two rows")
    variables = [name.strip() for name in lines[0].split(",")]
    characteristic = int(lines[1].strip())
    rows = [line.strip().removesuffix(",").strip() for line in lines[2:]]
    if any(not row for row in rows):
        raise ValueError("empty polynomial row")
    return variables, characteristic, rows


def substitute_coordinates(
    row: str,
    assignments: dict[str, int],
    characteristic: int,
) -> str:
    substituted = row
    for name, value in assignments.items():
        substituted = re.sub(
            rf"\b{re.escape(name)}\b",
            str(value % characteristic),
            substituted,
        )
    return substituted


def singular_program(
    variables: list[str],
    characteristic: int,
    ideal_rows: list[str],
    saturation_row: str | None,
    algorithm: str,
    root_block_order: bool,
) -> str:
    if root_block_order:
        root_count = sum(name.startswith(("h", "g")) for name in variables)
        if not 0 < root_count < len(variables):
            raise ValueError("root block order requires root and carrier variables")
        ordering = f"(lp({root_count}),dp({len(variables) - root_count}))"
    else:
        ordering = "dp"
    setup = []
    if saturation_row is not None:
        setup.append('LIB "elim.lib";')
    setup.extend(
        [
            f"ring q79={characteristic},({','.join(variables)}),{ordering};",
            "option(redSB);",
            f"ideal I={','.join(ideal_rows)};",
        ]
    )
    if saturation_row is not None:
        setup.extend(
            [
                f"ideal S={saturation_row};",
                "list L=sat(I,S);",
                f"ideal G={algorithm}(L[1]);",
            ]
        )
    else:
        setup.append(f"ideal G={algorithm}(I);")
    return "\n".join(
        [
            *setup,
            'print("Q79_SATURATION_BEGIN");',
            "if (reduce(1,G)==0)",
            "{",
            '  print("EXACT_UNIT_IDEAL");',
            "}",
            "else",
            "{",
            '  print("EXACT_NONUNIT_IDEAL");',
            "  print(size(G));",
            "  print(G);",
            "}",
            'print("Q79_SATURATION_END");',
            "quit;",
            "",
        ]
    )


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--input", type=Path, required=True)
    parser.add_argument("--coordinates", default="u0,u2,u3,u4,u5,u6,u7")
    parser.add_argument("--samples", default="1:1,37:73")
    parser.add_argument("--timeout", type=float, default=15.0)
    parser.add_argument("--ordinary", action="store_true")
    parser.add_argument("--algorithm", choices=("std", "slimgb"), default="std")
    parser.add_argument("--root-block-order", action="store_true")
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()

    variables, characteristic, rows = parse_msolve_input(args.input)
    coordinates = args.coordinates.split(",")
    if len(set(coordinates)) != len(coordinates):
        raise ValueError("coordinates must be distinct")
    if any(name not in variables for name in coordinates):
        raise ValueError("benchmark coordinate is absent from the ring")
    samples = [
        tuple(int(value) % characteristic for value in sample.split(":"))
        for sample in args.samples.split(",")
    ]
    if any(len(sample) != 2 for sample in samples):
        raise ValueError("every sample must provide two values")

    saturation_row = None if args.ordinary else rows[-1]
    parent_rows = rows if args.ordinary else rows[:-1]
    environment = os.environ.copy()
    environment["LD_LIBRARY_PATH"] = os.pathsep.join(
        [str(SINGULAR_LIBRARY), str(SINGULAR_MODULES)]
    )
    environment["SINGULARPATH"] = os.pathsep.join(
        [str(SINGULAR_PATH), str(SINGULAR_MODULES)]
    )
    environment["SINGULAR_BIN_DIR"] = str(SINGULAR_ROOT / "usr/bin")
    environment["SINGULAR_DATA_DIR"] = str(SINGULAR_ROOT / "usr/share")
    environment["SINGULAR_PROCS_DIR"] = str(SINGULAR_MODULES)
    environment["SINGULAR_ROOT_DIR"] = str(SINGULAR_ROOT / "usr")
    environment["OMP_NUM_THREADS"] = "1"
    environment["OPENBLAS_NUM_THREADS"] = "1"
    environment["MKL_NUM_THREADS"] = "1"

    benchmark_rows = []
    with tempfile.TemporaryDirectory(prefix="q79-singular-saturation-") as directory:
        temporary = Path(directory)
        for first, second in itertools.combinations(coordinates, 2):
            outcomes = []
            for sample_index, (first_value, second_value) in enumerate(samples):
                assignments = {first: first_value, second: second_value}
                active_variables = [
                    name for name in variables if name not in assignments
                ]
                if args.root_block_order:
                    h_variables = sorted(
                        (name for name in active_variables if name.startswith("h")),
                        key=lambda name: int(name[1:]),
                        reverse=True,
                    )
                    g_variables = sorted(
                        (name for name in active_variables if name.startswith("g")),
                        key=lambda name: int(name[1:]),
                        reverse=True,
                    )
                    other_variables = [
                        name
                        for name in active_variables
                        if not name.startswith(("h", "g"))
                    ]
                    active_variables = [*h_variables, *g_variables, *other_variables]
                fiber_rows = [
                    substitute_coordinates(row, assignments, characteristic)
                    for row in parent_rows
                ]
                fiber_saturation_row = (
                    substitute_coordinates(
                        saturation_row, assignments, characteristic
                    )
                    if saturation_row is not None
                    else None
                )
                program = singular_program(
                    active_variables,
                    characteristic,
                    fiber_rows,
                    fiber_saturation_row,
                    args.algorithm,
                    args.root_block_order,
                )
                script_path = temporary / f"pair_{first}_{second}_{sample_index}.sing"
                script_path.write_text(program, encoding="ascii")
                started = time.perf_counter()
                try:
                    completed = subprocess.run(
                        [
                            str(SINGULAR),
                            "-q",
                            "-t",
                            "--threads=1",
                            "--flint-threads=1",
                            str(script_path),
                        ],
                        env=environment,
                        stdout=subprocess.PIPE,
                        stderr=subprocess.PIPE,
                        timeout=args.timeout,
                        check=False,
                        text=True,
                    )
                    stdout = completed.stdout
                    stderr = completed.stderr
                    if (
                        completed.returncode == 0
                        and "Q79_SATURATION_BEGIN" in stdout
                        and "Q79_SATURATION_END" in stdout
                        and "EXACT_UNIT_IDEAL" in stdout
                    ):
                        status = "EXACT_UNIT_IDEAL"
                    elif (
                        completed.returncode == 0
                        and "Q79_SATURATION_BEGIN" in stdout
                        and "Q79_SATURATION_END" in stdout
                        and "EXACT_NONUNIT_IDEAL" in stdout
                    ):
                        status = "EXACT_NONUNIT_IDEAL"
                    else:
                        status = "FAILED"
                    returncode = completed.returncode
                except subprocess.TimeoutExpired as error:
                    stdout = error.stdout or ""
                    stderr = error.stderr or ""
                    if isinstance(stdout, bytes):
                        stdout = stdout.decode("utf-8", errors="replace")
                    if isinstance(stderr, bytes):
                        stderr = stderr.decode("utf-8", errors="replace")
                    status = "TIMEOUT"
                    returncode = None
                elapsed = time.perf_counter() - started
                outcomes.append(
                    {
                        "values": [first_value, second_value],
                        "status": status,
                        "returncode": returncode,
                        "elapsed_seconds": elapsed,
                        "stdout_sha256": hashlib.sha256(
                            stdout.encode("utf-8")
                        ).hexdigest(),
                        "stdout_tail": stdout[-2000:],
                        "stderr_tail": stderr[-2000:],
                    }
                )
            exact_count = sum(
                row["status"].startswith("EXACT_") for row in outcomes
            )
            elapsed_values = [row["elapsed_seconds"] for row in outcomes]
            benchmark_rows.append(
                {
                    "coordinates": [first, second],
                    "exact_samples": exact_count,
                    "unit_samples": sum(
                        row["status"] == "EXACT_UNIT_IDEAL" for row in outcomes
                    ),
                    "median_elapsed_seconds": statistics.median(elapsed_values),
                    "max_elapsed_seconds": max(elapsed_values),
                    "outcomes": outcomes,
                }
            )
            print(
                f"{first},{second}: exact={exact_count}/{len(samples)}; "
                f"median={statistics.median(elapsed_values):.3f}s",
                flush=True,
            )

    benchmark_rows.sort(
        key=lambda row: (
            -row["exact_samples"],
            row["median_elapsed_seconds"],
            row["coordinates"],
        )
    )
    packet = {
        "schema": "MTTQ79SingularSaturationCoordinatePairBenchmark.v1",
        "date": "2026-07-19",
        "input": {
            "path": str(args.input),
            "sha256": hashlib.sha256(args.input.read_bytes()).hexdigest(),
        },
        "engine": {
            "name": "Singular",
            "version": "4.4.1",
            "binary": str(SINGULAR),
            "exact_operation": (
                "ordinary ideal Groebner basis"
                if args.ordinary
                else "ideal saturation by final input generator"
            ),
        },
        "field_characteristic": characteristic,
        "saturation_polynomial": saturation_row,
        "ordinary_ideal": args.ordinary,
        "singular_algorithm": args.algorithm,
        "root_block_order": args.root_block_order,
        "root_block_contract": (
            "reverse-index lexicographic h/g block before the carrier dp block"
            if args.root_block_order
            else None
        ),
        "fiber_construction": "exact coordinate substitution before saturation",
        "samples": [list(sample) for sample in samples],
        "timeout_seconds": args.timeout,
        "rows_ranked": benchmark_rows,
        "claim_boundary": (
            "Runtime benchmark only. Exact outcomes certify only the displayed "
            "sample fibers; a complete finite-field cover is still required."
        ),
    }
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(packet, indent=2) + "\n", encoding="utf-8")
    print(args.output)
    if benchmark_rows:
        print("best=" + ",".join(benchmark_rows[0]["coordinates"]))


if __name__ == "__main__":
    main()
