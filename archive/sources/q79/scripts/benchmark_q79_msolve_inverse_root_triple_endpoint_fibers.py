#!/usr/bin/env python3
"""Benchmark exact (u1, a=v*u3, v) fibers of an inverse-root mirror chart."""

from __future__ import annotations

import argparse
import hashlib
import json
import os
import re
import statistics
import subprocess
import tempfile
import time
from pathlib import Path

from flint import nmod_mpoly_ctx

from build_q79_D10_D6_h1_g1_pair_quotient_obstructions import (
    PRIME,
    parse_input,
    parse_polynomial,
)


DEFAULT_MSOLVE = Path("/home/nerodes/.local/opt/msolve-0.10.1/msolve")


def require(condition: bool, label: str) -> None:
    if not condition:
        raise AssertionError(label)


def serialize_input(names, rows) -> str:
    return ",".join(names) + "\n101\n" + ",\n".join(str(row) for row in rows) + "\n"


def classify(output: str, returncode: int | None, timed_out: bool) -> str:
    if timed_out:
        return "TIMEOUT"
    if returncode != 0:
        return f"SOLVER_EXIT_{returncode}"
    if output == "[-1]:":
        return "EXACT_UNIT_IDEAL"
    if output.startswith("#Reduced Groebner basis data") and output.endswith("]:"):
        body = output[output.index("[") + 1 : output.rindex("]:")]
        basis = [value.strip() for value in body.split(",\n") if value.strip()]
        return "EXACT_UNIT_GROEBNER_BASIS" if basis == ["1"] else "EXACT_REDUCED_GROEBNER_BASIS"
    if output.startswith("[0,") and output.endswith(":"):
        return "EXACT_FINITE_PARAMETRIZATION"
    if output.startswith("[1,") and output.endswith(":"):
        return "EXACT_POSITIVE_DIMENSIONAL_OUTPUT"
    return "UNCLASSIFIED_OUTPUT" if output else "EMPTY_OUTPUT"


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--input", type=Path, required=True)
    parser.add_argument("--scalar-class", type=int, choices=(1, 2), required=True)
    parser.add_argument("--samples", default="1:1:1")
    parser.add_argument(
        "--parent-row-indices",
        help="Comma-separated active parent rows; defaults to all rows except 0 and 13.",
    )
    parser.add_argument(
        "--drop-variables",
        default="",
        help="Comma-separated variables proved absent from every selected parent row.",
    )
    parser.add_argument("--timeout", type=float, default=30.0)
    parser.add_argument("--mode", choices=("groebner", "parametrization"), default="groebner")
    parser.add_argument("--linear-algebra", type=int, choices=(1, 2, 42, 44), default=2)
    parser.add_argument("--verbose", type=int, choices=(0, 1, 2), default=0)
    parser.add_argument("--signature", action="store_true")
    parser.add_argument("--msolve", type=Path, default=DEFAULT_MSOLVE)
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()

    names, field, texts = parse_input(args.input)
    require(field == PRIME and len(names) == 19 and len(texts) == 22, "inverse-root parent")
    context = nmod_mpoly_ctx.get(names, ordering="degrevlex", modulus=PRIME)
    rows = [parse_polynomial(text, context, names) for text in texts]
    generator = dict(zip(names, context.gens()))
    require(rows[0] == generator["u0"] * generator["u1"] ** 2 - 1, "r endpoint")
    require(
        rows[13]
        == generator["v"] ** 2 * generator["u2"] * generator["u3"] ** 2
        - args.scalar_class,
        "d endpoint",
    )
    samples = [
        tuple(int(value) % PRIME for value in sample.split(":"))
        for sample in args.samples.split(",")
    ]
    require(
        all(len(sample) == 3 and all(value != 0 for value in sample) for sample in samples),
        "nonzero triple samples",
    )
    all_active_parent_rows = tuple(index for index in range(len(rows)) if index not in {0, 13})
    selected_parent_rows = (
        tuple(int(value) for value in args.parent_row_indices.split(","))
        if args.parent_row_indices
        else all_active_parent_rows
    )
    require(
        bool(selected_parent_rows)
        and len(set(selected_parent_rows)) == len(selected_parent_rows)
        and set(selected_parent_rows).issubset(all_active_parent_rows),
        "selected active parent rows",
    )
    dropped_variables = tuple(
        value.strip() for value in args.drop_variables.split(",") if value.strip()
    )
    require(
        len(set(dropped_variables)) == len(dropped_variables)
        and all(value in names for value in dropped_variables),
        "dropped variables belong to the source ring",
    )
    for row_index in selected_parent_rows:
        require(
            not any(
                re.search(rf"\b{re.escape(name)}\b", texts[row_index])
                for name in dropped_variables
            ),
            f"dropped variable absent from selected row {row_index}",
        )

    environment = os.environ.copy()
    environment["OMP_NUM_THREADS"] = "1"
    environment["OPENBLAS_NUM_THREADS"] = "1"
    environment["MKL_NUM_THREADS"] = "1"
    outcomes = []
    with tempfile.TemporaryDirectory(prefix="q79-triple-endpoint-") as directory:
        temporary = Path(directory)
        for sample_index, (u1, a_value, v_value) in enumerate(samples):
            u0 = pow(u1, -2, PRIME)
            u2 = args.scalar_class * pow(a_value, -2, PRIME) % PRIME
            u3 = a_value * pow(v_value, -1, PRIME) % PRIME
            assignments = {
                "u0": u0,
                "u1": u1,
                "u2": u2,
                "u3": u3,
                "v": v_value,
            }
            omitted_names = set(assignments) | set(dropped_variables)
            target_names = tuple(name for name in names if name not in omitted_names)
            target_context = nmod_mpoly_ctx.get(
                target_names, ordering="degrevlex", modulus=PRIME
            )
            target_generator = dict(zip(target_names, target_context.gens()))
            composition = []
            for name in names:
                if name in assignments:
                    composition.append(target_context.constant(assignments[name]))
                elif name in target_generator:
                    composition.append(target_generator[name])
                else:
                    composition.append(target_context.constant(0))
            composed = [row.compose(*composition, ctx=target_context) for row in rows]
            require(composed[0] == target_context.constant(0), "r endpoint vanishes")
            require(composed[13] == target_context.constant(0), "d endpoint vanishes")
            reduced_rows = [composed[index] for index in selected_parent_rows]
            require(
                len(target_names) == 14 - len(dropped_variables)
                and len(reduced_rows) == len(selected_parent_rows),
                "triple fiber dimensions",
            )
            require(max(int(row.total_degree()) for row in reduced_rows) <= 3, "cubic bound")
            input_text = serialize_input(target_names, reduced_rows)
            input_path = temporary / f"fiber_{sample_index}.in"
            output_path = temporary / f"fiber_{sample_index}.out"
            input_path.write_text(input_text, encoding="ascii")
            if args.mode == "groebner":
                command = [
                    str(args.msolve),
                    "-t",
                    "1",
                    "-l",
                    str(args.linear_algebra),
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
                ]
            else:
                command = [
                    str(args.msolve),
                    "-t",
                    "1",
                    "-l",
                    str(args.linear_algebra),
                    "-d",
                    "4",
                    "-c",
                    "2",
                    "-f",
                    str(input_path),
                    "-o",
                    str(output_path),
                ]
            command.extend(["-v", str(args.verbose), "-q", "1" if args.signature else "0"])
            started = time.perf_counter()
            try:
                completed = subprocess.run(
                    command,
                    env=environment,
                    stdout=subprocess.PIPE,
                    stderr=subprocess.PIPE,
                    timeout=args.timeout,
                    check=False,
                    text=True,
                )
                timed_out = False
                returncode = completed.returncode
                stdout_tail = completed.stdout[-2000:]
                stderr_tail = completed.stderr[-2000:]
            except subprocess.TimeoutExpired as error:
                timed_out = True
                returncode = None
                stdout_tail = error.stdout or ""
                stderr_tail = error.stderr or ""
                if isinstance(stdout_tail, bytes):
                    stdout_tail = stdout_tail.decode("utf-8", errors="replace")
                if isinstance(stderr_tail, bytes):
                    stderr_tail = stderr_tail.decode("utf-8", errors="replace")
            elapsed = time.perf_counter() - started
            output_text = (
                output_path.read_text(encoding="ascii").strip()
                if output_path.exists() and output_path.stat().st_size
                else ""
            )
            status = classify(output_text, returncode, timed_out)
            outcomes.append(
                {
                    "u1": u1,
                    "a_equals_v_times_u3": a_value,
                    "v": v_value,
                    "forced_u0": u0,
                    "forced_u2": u2,
                    "forced_u3": u3,
                    "status": status,
                    "returncode": returncode,
                    "elapsed_seconds": elapsed,
                    "variables": len(target_names),
                    "equations": len(reduced_rows),
                    "maximum_total_degree": max(
                        int(row.total_degree()) for row in reduced_rows
                    ),
                    "row_term_counts": [len(row.to_dict()) for row in reduced_rows],
                    "input_sha256": hashlib.sha256(input_text.encode("ascii")).hexdigest(),
                    "output_sha256": hashlib.sha256(output_text.encode("ascii")).hexdigest(),
                    "output_text": output_text
                    if status.startswith(
                        (
                            "EXACT_UNIT",
                            "EXACT_REDUCED",
                            "EXACT_FINITE",
                            "EXACT_POSITIVE",
                        )
                    )
                    else "",
                    "stdout_tail": str(stdout_tail)[-2000:]
                    if status in {"TIMEOUT", "EMPTY_OUTPUT", "UNCLASSIFIED_OUTPUT"}
                    else str(stdout_tail)[-20_000:]
                    if args.verbose
                    else "",
                    "stderr_tail": str(stderr_tail)[-2000:]
                    if status.startswith("SOLVER_EXIT")
                    else str(stderr_tail)[-50_000:]
                    if args.verbose
                    else "",
                }
            )
            print(
                f"u1={u1},a={a_value},v={v_value}: {status}; {elapsed:.3f}s",
                flush=True,
            )

    packet = {
        "schema": "MTTQ79MsolveInverseRootTripleEndpointFiberBenchmark.v1",
        "date": "2026-07-20",
        "input": {
            "path": str(args.input),
            "sha256": hashlib.sha256(args.input.read_bytes()).hexdigest(),
        },
        "field_characteristic": PRIME,
        "scalar_square_class_representative": args.scalar_class,
        "exact_cover": (
            "For every u1,a,v in F101*, set u0=u1^(-2), u2=s*a^(-2), and "
            "u3=a*v^(-1). Every source solution lies on exactly one such triple fiber."
        ),
        "cover_size_per_scalar_class_chart": (PRIME - 1) ** 3,
        "fiber_dimensions": {
            "variables": 14 - len(dropped_variables),
            "equations": len(selected_parent_rows),
            "maximum_total_degree": 3,
        },
        "selected_parent_row_indices": list(selected_parent_rows),
        "dropped_source_variables": list(dropped_variables),
        "solver_mode": args.mode,
        "linear_algebra": args.linear_algebra,
        "verbose": args.verbose,
        "signature_algorithm": args.signature,
        "probabilistic_reconnaissance_only": args.linear_algebra in {42, 44},
        "timeout_seconds": args.timeout,
        "outcomes": outcomes,
        "exact_unit_samples": sum(
            row["status"].startswith("EXACT_UNIT") for row in outcomes
        ),
        "exact_positive_samples": sum(
            row["status"].startswith(("EXACT_FINITE", "EXACT_POSITIVE"))
            for row in outcomes
        ),
        "median_elapsed_seconds": statistics.median(
            row["elapsed_seconds"] for row in outcomes
        ),
        "claim_boundary": (
            "Each unit result excludes only its exact triple fiber. A complete chart "
            "classification requires all one million nonzero triples or a proved orbit "
            "reduction. Timeout is not a no-go."
        ),
        "new_continuous_fit_parameters": 0,
    }
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(packet, indent=2) + "\n", encoding="utf-8")
    print(args.output)


if __name__ == "__main__":
    main()
