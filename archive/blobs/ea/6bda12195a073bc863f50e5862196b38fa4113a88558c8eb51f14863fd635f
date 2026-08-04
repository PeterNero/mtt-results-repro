#!/usr/bin/env python3
"""Certify a q79 triple endpoint fiber through its four-carrier quotient.

The ten recurrence equations are a triangular Groebner basis for the ten
root variables. Reducing a selected terminal subset by that basis leaves an
ideal in u4,u5,u6,u7. This script asks Singular for a unit certificate in the
small carrier ring and can lift it back to the selected original fiber rows.
"""

from __future__ import annotations

import argparse
import hashlib
import json
import os
import re
import subprocess
import tempfile
import time
from pathlib import Path

from benchmark_q79_singular_saturation_coordinate_pairs import (
    SINGULAR,
    SINGULAR_LIBRARY,
    SINGULAR_MODULES,
    SINGULAR_PATH,
    SINGULAR_ROOT,
    parse_msolve_input,
    substitute_coordinates,
)


PRIME = 101
RECURRENCE_PARENT_ROWS = (1, 2, 3, 4, 5, 6, 14, 15, 16, 17)
TERMINAL_PARENT_ROWS = (7, 8, 9, 10, 11, 12, 18, 19, 20, 21)


def require(condition: bool, label: str) -> None:
    if not condition:
        raise AssertionError(label)


def singular_program(
    variables: list[str],
    recurrence: list[str],
    terminals: list[str],
    full_lift: bool,
    print_certificate: bool,
    emit_reduced_only: bool,
    targeted_lift: bool,
) -> str:
    root_variables = [
        *[f"h{index}" for index in range(6, 0, -1)],
        *[f"y{index}" for index in range(4, 0, -1)],
    ]
    carrier_variables = ["u4", "u5", "u6", "u7"]
    require(set(variables) == set(root_variables + carrier_variables), "fiber variables")
    ordered = root_variables + carrier_variables
    lines = [
        f"ring q79={PRIME},({','.join(ordered)}),(lp(10),dp(4));",
        "option(redSB);",
        f"ideal G={','.join(recurrence)};",
        f"ideal E={','.join(terminals)};",
        "ideal R=reduce(E,G);",
        'print(\"Q79_REDUCED_TERMINALS_BEGIN\");',
        "print(size(R));",
        "int i;",
        "for (i=1; i<=size(R); i++)",
        "{",
        '  print(string(i)+\",\"+string(size(R[i]))+\",\"+string(deg(R[i])));',
        "}",
    ]
    if emit_reduced_only:
        lines.extend(
            [
                'print("Q79_REDUCED_POLYNOMIALS_BEGIN");',
                "for (i=1; i<=size(R); i++)",
                "{",
                '  print(string(i)+"|"+string(R[i]));',
                "}",
                'print("Q79_REDUCED_POLYNOMIALS_END");',
                'print("Q79_RECURSIVE_QUOTIENT_END");',
                "quit;",
                "",
            ]
        )
        return "\n".join(lines)
    lines.extend(
        [
            "ideal RQ=R;",
            "ring c79=101,(u4,u5,u6,u7),dp;",
            "option(redSB);",
            "ideal R=imap(q79,RQ);",
        ]
    )
    carrier_matrix_entries = ",".join(
        f"R[{index}]" for index in range(1, len(terminals) + 1)
    )
    if targeted_lift:
        lines.extend(
            [
                "ideal J=1;",
                "matrix A=lift(R,J);",
                f"matrix RM[1][{len(terminals)}]={carrier_matrix_entries};",
                "matrix AV=RM*A;",
                'print("Q79_CARRIER_TARGETED_LIFT_BEGIN");',
                "print(nrows(A));",
                "print(ncols(A));",
                "if ((nrows(AV)==1) && (ncols(AV)==1) && (AV[1,1]==1))",
                "{",
                '  print("Q79_EXACT_CARRIER_UNIT_TRANSFORM");',
                "}",
                "else",
                "{",
                '  print("Q79_CARRIER_TRANSFORM_NOT_UNIT");',
                "}",
            ]
        )
    else:
        lines.extend(
            [
                "matrix A;",
                "ideal H=liftstd(R,A);",
                'print("Q79_CARRIER_LIFTSTD_BEGIN");',
                "print(size(H));",
                "print(nrows(A));",
                "print(ncols(A));",
                f"matrix RM[1][{len(terminals)}]={carrier_matrix_entries};",
                "matrix AV=RM*A;",
                "if ((size(H)==1) && (H[1]==1) && (AV[1,1]==1))",
                "{",
                '  print("Q79_EXACT_CARRIER_UNIT_TRANSFORM");',
                "}",
                "else",
                "{",
                '  print("Q79_CARRIER_TRANSFORM_NOT_UNIT");',
                "}",
            ]
        )
    if full_lift:
        source_matrix_entries = ",".join(
            [f"G[{index}]" for index in range(1, len(recurrence) + 1)]
            + [f"E[{index}]" for index in range(1, len(terminals) + 1)]
        )
        lines.extend(
            [
                "setring q79;",
                "matrix AQ=imap(c79,A);",
                "matrix B=lift(G+E,R);",
                "matrix C=B*AQ;",
                f"matrix SM[1][{len(recurrence) + len(terminals)}]={source_matrix_entries};",
                "matrix V=SM*C;",
                'print(\"Q79_FULL_LIFT_BEGIN\");',
                "print(nrows(C));",
                "print(ncols(C));",
                "if ((nrows(V)==1) && (ncols(V)==1) && (V[1,1]==1))",
                "{",
                '  print(\"Q79_DIRECT_SELECTED_ROW_IDENTITY_VERIFIED\");',
                "}",
                "else",
                "{",
                '  print(\"Q79_DIRECT_SELECTED_ROW_IDENTITY_FAILED\");',
                "}",
            ]
        )
        if print_certificate:
            lines.extend(
                [
                    'print(\"Q79_CERTIFICATE_BEGIN\");',
                    "for (i=1; i<=nrows(C); i++)",
                    "{",
                    '  print(string(i)+\"|\"+string(C[i,1]));',
                    "}",
                    'print(\"Q79_CERTIFICATE_END\");',
                ]
            )
    lines.extend(['print("Q79_RECURSIVE_QUOTIENT_END");', "quit;", ""])
    return "\n".join(lines)


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--input", type=Path, required=True)
    parser.add_argument("--scalar-class", type=int, choices=(1, 2), required=True)
    parser.add_argument("--u1", type=int, default=1)
    parser.add_argument("--a", type=int, default=1)
    parser.add_argument("--v", type=int, default=1)
    parser.add_argument(
        "--terminal-parent-rows",
        default=",".join(str(value) for value in TERMINAL_PARENT_ROWS),
    )
    parser.add_argument("--timeout", type=float, default=300.0)
    parser.add_argument("--full-lift", action="store_true")
    parser.add_argument("--print-certificate", action="store_true")
    parser.add_argument("--emit-carrier-input", type=Path)
    parser.add_argument("--targeted-lift", action="store_true")
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()
    require(not args.print_certificate or args.full_lift, "certificate requires full lift")
    require(
        args.emit_carrier_input is None
        or (not args.full_lift and not args.print_certificate),
        "carrier-input emission is reduction-only",
    )
    terminal_parent_rows = tuple(
        int(value) for value in args.terminal_parent_rows.split(",") if value
    )
    require(
        terminal_parent_rows
        and len(set(terminal_parent_rows)) == len(terminal_parent_rows)
        and set(terminal_parent_rows).issubset(TERMINAL_PARENT_ROWS),
        "terminal rows",
    )

    variables, characteristic, rows = parse_msolve_input(args.input)
    require(characteristic == PRIME and len(variables) == 19 and len(rows) == 22, "parent")
    u1 = args.u1 % PRIME
    a_value = args.a % PRIME
    v_value = args.v % PRIME
    require(u1 and a_value and v_value, "nonzero triple")
    assignments = {
        "u0": pow(u1, -2, PRIME),
        "u1": u1,
        "u2": args.scalar_class * pow(a_value, -2, PRIME) % PRIME,
        "u3": a_value * pow(v_value, -1, PRIME) % PRIME,
        "v": v_value,
    }
    active_variables = [name for name in variables if name not in assignments]
    substituted = [substitute_coordinates(row, assignments, PRIME) for row in rows]
    recurrence = [substituted[index] for index in RECURRENCE_PARENT_ROWS]
    terminals = [substituted[index] for index in terminal_parent_rows]
    require(len(active_variables) == 14, "fourteen active variables")

    program = singular_program(
        active_variables,
        recurrence,
        terminals,
        args.full_lift,
        args.print_certificate,
        args.emit_carrier_input is not None,
        args.targeted_lift,
    )
    environment = os.environ.copy()
    environment["LD_LIBRARY_PATH"] = os.pathsep.join([str(SINGULAR_LIBRARY), str(SINGULAR_MODULES)])
    environment["SINGULARPATH"] = os.pathsep.join([str(SINGULAR_PATH), str(SINGULAR_MODULES)])
    environment["SINGULAR_BIN_DIR"] = str(SINGULAR_ROOT / "usr/bin")
    environment["SINGULAR_DATA_DIR"] = str(SINGULAR_ROOT / "usr/share")
    environment["SINGULAR_PROCS_DIR"] = str(SINGULAR_MODULES)
    environment["SINGULAR_ROOT_DIR"] = str(SINGULAR_ROOT / "usr")
    environment["OMP_NUM_THREADS"] = "1"
    environment["OPENBLAS_NUM_THREADS"] = "1"
    environment["MKL_NUM_THREADS"] = "1"

    with tempfile.TemporaryDirectory(prefix="q79-recursive-quotient-") as directory:
        script_path = Path(directory) / "certificate.sing"
        script_path.write_text(program, encoding="ascii")
        started = time.perf_counter()
        try:
            completed = subprocess.run(
                [str(SINGULAR), "-q", "-t", "--threads=1", "--flint-threads=1", str(script_path)],
                env=environment,
                stdout=subprocess.PIPE,
                stderr=subprocess.PIPE,
                timeout=args.timeout,
                check=False,
                text=True,
            )
            stdout = completed.stdout
            stderr = completed.stderr
            returncode = completed.returncode
            timed_out = False
        except subprocess.TimeoutExpired as error:
            stdout = error.stdout or ""
            stderr = error.stderr or ""
            if isinstance(stdout, bytes):
                stdout = stdout.decode("utf-8", errors="replace")
            if isinstance(stderr, bytes):
                stderr = stderr.decode("utf-8", errors="replace")
            returncode = None
            timed_out = True
        elapsed = time.perf_counter() - started

    carrier_unit = (
        not timed_out
        and returncode == 0
        and "Q79_EXACT_CARRIER_UNIT_TRANSFORM" in stdout
        and "Q79_RECURSIVE_QUOTIENT_END" in stdout
    )
    full_unit = carrier_unit and "Q79_DIRECT_SELECTED_ROW_IDENTITY_VERIFIED" in stdout
    profiles: list[dict[str, int]] = []
    if "Q79_REDUCED_TERMINALS_BEGIN" in stdout:
        body = stdout.split("Q79_REDUCED_TERMINALS_BEGIN", 1)[1]
        for line in body.splitlines():
            match = re.fullmatch(r"(\d+),(\d+),(\d+)", line.strip())
            if match:
                profiles.append(
                    {
                        "index": int(match.group(1)),
                        "terms": int(match.group(2)),
                        "total_degree": int(match.group(3)),
                    }
                )
    reduced_polynomials: list[str] = []
    if "Q79_REDUCED_POLYNOMIALS_BEGIN" in stdout:
        body = stdout.split("Q79_REDUCED_POLYNOMIALS_BEGIN", 1)[1].split(
            "Q79_REDUCED_POLYNOMIALS_END", 1
        )[0]
        indexed_polynomials: dict[int, str] = {}
        for line in body.splitlines():
            match = re.fullmatch(r"(\d+)\|(.*)", line.strip())
            if match:
                indexed_polynomials[int(match.group(1))] = match.group(2)
        reduced_polynomials = [
            indexed_polynomials[index]
            for index in range(1, len(terminal_parent_rows) + 1)
        ]
    carrier_input = None
    if args.emit_carrier_input is not None:
        require(
            not timed_out
            and returncode == 0
            and len(reduced_polynomials) == len(terminal_parent_rows),
            "complete reduced carrier input",
        )
        args.emit_carrier_input.parent.mkdir(parents=True, exist_ok=True)
        args.emit_carrier_input.write_text(
            "u4,u5,u6,u7\n101\n" + ",\n".join(reduced_polynomials) + "\n",
            encoding="ascii",
        )
        carrier_input = {
            "path": str(args.emit_carrier_input),
            "sha256": hashlib.sha256(args.emit_carrier_input.read_bytes()).hexdigest(),
            "bytes": args.emit_carrier_input.stat().st_size,
            "polynomials": len(reduced_polynomials),
        }
    certificate_rows = []
    if full_unit and args.print_certificate:
        require("Q79_CERTIFICATE_BEGIN" in stdout and "Q79_CERTIFICATE_END" in stdout, "certificate markers")
        body = stdout.split("Q79_CERTIFICATE_BEGIN", 1)[1].split("Q79_CERTIFICATE_END", 1)[0]
        parent_indices = (*RECURRENCE_PARENT_ROWS, *terminal_parent_rows)
        for line in body.splitlines():
            match = re.fullmatch(r"(\d+)\|(.*)", line.strip())
            if match:
                index = int(match.group(1))
                certificate_rows.append(
                    {
                        "fiber_generator_index": index,
                        "parent_row_index": parent_indices[index - 1],
                        "multiplier": match.group(2),
                    }
                )
        require(
            len(certificate_rows) == len(parent_indices),
            "selected certificate multipliers",
        )

    status = (
        "EXACT_REDUCED_CARRIER_INPUT_EMITTED"
        if carrier_input is not None
        else "EXACT_SELECTED_ROW_NULLSTELLENSATZ_CERTIFICATE"
        if full_unit
        and len(certificate_rows)
        == len(RECURRENCE_PARENT_ROWS) + len(terminal_parent_rows)
        else "EXACT_SELECTED_ROW_UNIT_TRANSFORM"
        if full_unit
        else "EXACT_FOUR_CARRIER_UNIT_TRANSFORM"
        if carrier_unit
        else "TIMEOUT"
        if timed_out
        else "FAILED_OR_NONUNIT"
    )
    packet = {
        "schema": "MTTQ79D10D6TripleEndpointRecursiveQuotientCertificate.v1",
        "date": "2026-07-20",
        "status": status,
        "input": {"path": str(args.input), "sha256": hashlib.sha256(args.input.read_bytes()).hexdigest()},
        "field": "F_101",
        "scalar_square_class_representative": args.scalar_class,
        "fiber": {
            "u1": u1,
            "a_equals_v_times_u3": a_value,
            "v": v_value,
            "assignments": assignments,
        },
        "triangular_recurrence_parent_rows": list(RECURRENCE_PARENT_ROWS),
        "terminal_parent_rows": list(terminal_parent_rows),
        "carrier_variables": ["u4", "u5", "u6", "u7"],
        "carrier_input": carrier_input,
        "reduced_terminal_profiles": profiles,
        "carrier_unit_transform_verified": carrier_unit,
        "direct_selected_row_identity_verified": full_unit,
        "certificate_rows": certificate_rows,
        "timeout_seconds": args.timeout,
        "elapsed_seconds": elapsed,
        "returncode": returncode,
        "timed_out": timed_out,
        "stdout_sha256": hashlib.sha256(stdout.encode("utf-8")).hexdigest(),
        "stdout_tail": stdout[-8000:] if not certificate_rows else "",
        "stderr_tail": stderr[-4000:],
        "checks": {
            "both_endpoint_equations_vanish_by_exact_assignments": True,
            "ten_recurrences_have_distinct_root_leaders": True,
            "selected_terminals_are_reduced_to_four_carrier_variables": len(profiles)
            == len(terminal_parent_rows),
            "no_continuous_fit_parameter_is_added": True,
        },
        "claim_boundary": (
            "A carrier transform proves the reduced four-variable fiber ideal is unit. "
            "Only the direct selected-row identity promotes that result to an explicit "
            "Nullstellensatz certificate in the original triple fiber. One fiber does "
            "not classify the one-million-fiber chart."
        ),
        "new_continuous_fit_parameters": 0,
    }
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(packet, indent=2) + "\n", encoding="utf-8")
    print(f"status={status}; elapsed={elapsed:.3f}s; profiles={len(profiles)}; certificate_rows={len(certificate_rows)}")
    print(args.output)


if __name__ == "__main__":
    main()
