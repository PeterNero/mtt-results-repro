#!/usr/bin/env python3
"""Certify four exact symbolic-v q79 R-only unit ideals."""

from __future__ import annotations

import argparse
import hashlib
import json
import re
from pathlib import Path


PRIME = 101
ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "candidate_data" / "q79_Ronly_symbolic_v_lines"
PARENT_DATA = ROOT / "candidate_data" / "q79_Ronly_classfree_representative_lines"
PREDECESSOR = (
    ROOT
    / "certificates"
    / "Q79_Ronly_ClassFree_Core_and_Representative_Lines_v1.json"
)
DEFAULT_OUTPUT = ROOT / "certificates" / "Q79_Ronly_Symbolic_V_Lines_v1.json"
TARGET_NAMES = (
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
    "v",
)
SELECTED_ROWS = tuple(range(1, 13))
DROPPED_Y = ("y1", "y2", "y3", "y4")


def require(condition: bool, label: str) -> None:
    if not condition:
        raise AssertionError(label)


def checksum(path: Path) -> dict[str, object]:
    return {
        "name": path.name,
        "bytes": path.stat().st_size,
        "sha256": hashlib.sha256(path.read_bytes()).hexdigest(),
    }


def parse_input(path: Path) -> tuple[tuple[str, ...], int, list[str]]:
    lines = path.read_text(encoding="ascii").replace("\r\n", "\n").splitlines()
    require(len(lines) >= 3, f"complete input {path.name}")
    return (
        tuple(lines[0].split(",")),
        int(lines[1]),
        [line.removesuffix(",") for line in lines[2:] if line],
    )


def polynomial_dict(
    text: str, names: tuple[str, ...]
) -> dict[tuple[int, ...], int]:
    positions = {name: index for index, name in enumerate(names)}
    coefficients: dict[tuple[int, ...], int] = {}
    for raw_term in text.replace("-", "+-").split("+"):
        raw_term = raw_term.strip()
        if not raw_term:
            continue
        sign = -1 if raw_term.startswith("-") else 1
        if sign < 0:
            raw_term = raw_term[1:]
        factors = raw_term.split("*")
        first_is_coefficient = factors[0].isdigit()
        coefficient = sign * (int(factors[0]) if first_is_coefficient else 1)
        exponents = [0] * len(names)
        for factor in factors[1 if first_is_coefficient else 0 :]:
            if "^" in factor:
                name, exponent_text = factor.split("^", 1)
                exponent = int(exponent_text)
            else:
                name, exponent = factor, 1
            require(name in positions, f"known variable {name}")
            exponents[positions[name]] += exponent
        monomial = tuple(exponents)
        coefficients[monomial] = (
            coefficients.get(monomial, 0) + coefficient
        ) % PRIME
    return {
        monomial: coefficient
        for monomial, coefficient in coefficients.items()
        if coefficient
    }


def substitute(
    polynomial: dict[tuple[int, ...], int],
    source_names: tuple[str, ...],
    assignments: dict[str, int],
) -> dict[tuple[int, ...], int]:
    target_positions = {name: index for index, name in enumerate(TARGET_NAMES)}
    result: dict[tuple[int, ...], int] = {}
    for monomial, raw_coefficient in polynomial.items():
        coefficient = raw_coefficient
        target_exponents = [0] * len(TARGET_NAMES)
        for name, exponent in zip(source_names, monomial):
            if exponent == 0:
                continue
            if name in assignments:
                coefficient = coefficient * pow(assignments[name], exponent, PRIME) % PRIME
            else:
                require(name in target_positions, f"unassigned source variable {name}")
                target_exponents[target_positions[name]] += exponent
        key = tuple(target_exponents)
        result[key] = (result.get(key, 0) + coefficient) % PRIME
    return {key: value for key, value in result.items() if value}


def maximum_degree(polynomial: dict[tuple[int, ...], int]) -> int:
    return max((sum(monomial) for monomial in polynomial), default=0)


def multiply(
    left: dict[tuple[int, ...], int],
    right: dict[tuple[int, ...], int],
) -> dict[tuple[int, ...], int]:
    result: dict[tuple[int, ...], int] = {}
    for left_monomial, left_coefficient in left.items():
        for right_monomial, right_coefficient in right.items():
            monomial = tuple(
                left_exponent + right_exponent
                for left_exponent, right_exponent in zip(
                    left_monomial, right_monomial
                )
            )
            result[monomial] = (
                result.get(monomial, 0)
                + left_coefficient * right_coefficient
            ) % PRIME
    return {
        monomial: coefficient
        for monomial, coefficient in result.items()
        if coefficient
    }


def literal_unit_output(text: str) -> bool:
    lines = text.strip().splitlines()
    return (
        bool(lines)
        and lines[0] == "#Reduced Groebner basis data"
        and any("#field characteristic: 101" in line for line in lines)
        and any("#length of basis:      1 element" in line for line in lines)
        and [line for line in lines if line and not line.startswith("#")] == ["[1]:"]
    )


def parse_execution_log(text: str) -> dict[str, object]:
    elapsed = re.search(r"overall\(elapsed\)\s+([0-9.]+) sec", text)
    rss = re.search(r"Maximum resident set size \(kbytes\):\s+(\d+)", text)
    exit_status = re.search(r"Exit status:\s+(\d+)", text)
    require(elapsed is not None, "msolve elapsed time")
    require(rss is not None, "msolve maximum RSS")
    require(exit_status is not None and exit_status.group(1) == "0", "msolve exit zero")
    require("Grobner basis has a single element" in text, "single-element basis log")
    require("No solution" in text, "no-solution log")
    return {
        "solver": "msolve 0.10.1",
        "field_characteristic": PRIME,
        "threads": 1,
        "basis_mode": "reduced DRL Groebner basis",
        "elapsed_seconds": float(elapsed.group(1)),
        "maximum_resident_kbytes": int(rss.group(1)),
        "exit_status": 0,
    }


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--output", type=Path, default=DEFAULT_OUTPUT)
    args = parser.parse_args()

    predecessor = json.loads(PREDECESSOR.read_text(encoding="utf-8"))
    require(
        predecessor["status"]
        == "EXACT_FOUR_CHART_TO_TWO_CORES_AND_FOUR_LINES_CERTIFIED",
        "predecessor theorem status",
    )
    records = []
    for space in (5, 6):
        for scalar_class in (1, 2):
            stem = f"space{space}_class{scalar_class}_u1_001_a_001_symbolic_v"
            parent_path = (
                PARENT_DATA
                / f"space_{space}_h0_g0_class{scalar_class}_inverse_root.msolve.in"
            )
            input_path = DATA / f"{stem}.msolve.in"
            packet_path = DATA / f"{stem}.input.packet.json"
            output_path = DATA / f"{stem}.msolve.out"
            log_path = DATA / f"{stem}.msolve.log"
            packet = json.loads(packet_path.read_text(encoding="utf-8"))
            parent_names, parent_field, parent_rows = parse_input(parent_path)
            target_names, target_field, target_rows = parse_input(input_path)
            require(
                parent_field == target_field == PRIME
                and len(parent_names) == 19
                and len(parent_rows) == 22,
                "parent and target rings",
            )
            require(
                target_names == TARGET_NAMES and len(target_rows) == 13,
                "12-variable 13-row symbolic line",
            )
            require(
                packet["schema"] == "MTTQ79RonlySymbolicVLineInput.v1"
                and packet["status"] == "EXACT_SELECTED_SYMBOLIC_V_LINE_INPUT",
                "symbolic input packet status",
            )
            require(
                packet["parent_input"]["sha256"] == checksum(parent_path)["sha256"]
                and packet["output"]["sha256"] == checksum(input_path)["sha256"],
                "packet input hashes",
            )
            require(
                packet["scalar_square_class_representative"] == scalar_class
                and packet["fixed_coordinates"]
                == {
                    "u1": 1,
                    "a_equals_v_times_u3": 1,
                    "selected_u0": 1,
                    "selected_u2": scalar_class,
                },
                "selected line coordinates",
            )
            require(
                packet["selected_parent_rows"] == list(SELECTED_ROWS)
                and packet["variables"] == list(TARGET_NAMES),
                "selected rows and variables",
            )
            require(
                all(
                    not re.search(rf"\b{re.escape(name)}\b", parent_rows[row_index])
                    for row_index in SELECTED_ROWS
                    for name in DROPPED_Y
                ),
                "selected rows omit reconstructible y variables",
            )
            assignments = {"u0": 1, "u1": 1, "u2": scalar_class}
            transformed_u_endpoint = substitute(
                polynomial_dict(parent_rows[0], parent_names), parent_names, assignments
            )
            require(not transformed_u_endpoint, "u endpoint vanishes identically")
            for target_index, parent_index in enumerate(SELECTED_ROWS):
                expected = substitute(
                    polynomial_dict(parent_rows[parent_index], parent_names),
                    parent_names,
                    assignments,
                )
                actual = polynomial_dict(target_rows[target_index], TARGET_NAMES)
                require(actual == expected, f"exact transformed row {parent_index}")
            endpoint = substitute(
                polynomial_dict(parent_rows[13], parent_names),
                parent_names,
                assignments,
            )
            expected_endpoint = polynomial_dict(
                f"{scalar_class}*v^2*u3^2-{scalar_class}", TARGET_NAMES
            )
            line_relation = polynomial_dict("v*u3-1", TARGET_NAMES)
            complementary_factor = polynomial_dict(
                f"{scalar_class}*v*u3+{scalar_class}", TARGET_NAMES
            )
            require(
                endpoint == expected_endpoint
                and endpoint == multiply(line_relation, complementary_factor),
                "selected scalar endpoint factorization",
            )
            require(
                polynomial_dict(target_rows[-1], TARGET_NAMES) == line_relation,
                "exact symbolic line relation",
            )
            require(
                max(
                    maximum_degree(polynomial_dict(row, TARGET_NAMES))
                    for row in target_rows
                )
                <= 3,
                "cubic line input",
            )
            output_text = output_path.read_text(encoding="ascii")
            require(literal_unit_output(output_text), "literal reduced unit basis")
            execution = parse_execution_log(log_path.read_text(encoding="utf-8"))
            records.append(
                {
                    "space_index": space,
                    "scalar_square_class_representative": scalar_class,
                    "fixed_coordinates": {
                        "u1": 1,
                        "a_equals_v_times_u3": 1,
                        "u0": 1,
                        "u2": scalar_class,
                    },
                    "symbolic_relation": "v*u3=1",
                    "parent_input": checksum(parent_path),
                    "symbolic_input": checksum(input_path),
                    "input_packet": checksum(packet_path),
                    "reduced_basis_output": checksum(output_path),
                    "execution_log": checksum(log_path),
                    "execution": execution,
                    "result": "UNIT_IDEAL_OVER_F101",
                }
            )

    checks = {
        "predecessor_four_line_theorem_is_hash_bound": True,
        "all_four_parent_charts_are_hash_bound": len(records) == 4,
        "all_selected_inputs_are_exact_parent_restrictions": True,
        "u_endpoint_is_eliminated_exactly": True,
        "scalar_endpoint_factors_through_v_u3_minus_one": True,
        "reconstructible_y_rows_are_not_used": True,
        "all_four_inputs_have_12_variables_and_13_cubics": True,
        "all_four_msolve_runs_exit_zero": True,
        "all_four_outputs_are_literal_reduced_unit_bases": True,
        "unit_ideal_excludes_points_over_every_field_extension": True,
        "no_D_terminal_row_is_used": True,
        "no_continuous_fit_parameter_is_added": True,
    }
    require(all(checks.values()), "all symbolic-line checks")
    certificate = {
        "schema": "MTTQ79RonlySymbolicVLines.v1",
        "date": "2026-07-20",
        "status": "EXACT_FOUR_SYMBOLIC_V_LINES_UNIT_OVER_ALGEBRAIC_CLOSURE",
        "field": "F_101",
        "predecessor_certificate": checksum(PREDECESSOR),
        "support_pattern": [6, 10, 8],
        "line_records": records,
        "theorem": (
            "For each mirror space 5 or 6 and each scalar class representative 1 or 2, "
            "the selected R-only ideal restricted by u1=1, u2=s and v*u3=1 is the "
            "unit ideal in F_101[h1,...,h6,u3,...,u7,v]. Therefore the entire "
            "symbolic-v line is empty over F_101 and over every field extension, "
            "including the algebraic closure."
        ),
        "strengthening_over_predecessor": (
            "The predecessor enumerated 100 F_101 points on each of these four lines. "
            "This certificate proves the four line ideals themselves are unit, so it "
            "also excludes extension-field points. It does not add new parameter lines."
        ),
        "totals": {
            "exact_symbolic_lines": 4,
            "finite_F101_points_subsumed": 400,
            "nominal_nonzero_endpoint_lines": 40000,
            "remaining_unclassified_endpoint_lines": 39996,
        },
        "checks": checks,
        "claim_tiers": {
            "four_displayed_symbolic_v_line_ideals": "CLOSED_EXACTLY",
            "remaining_39996_finite_endpoint_lines": "OPEN",
            "generic_u2_exceptional_locus": "OPEN",
            "space5_complete_R_only_core": "OPEN",
            "space6_complete_R_only_core": "OPEN",
            "simultaneous_R_and_D_system": "OPEN",
            "physical_HYM_QG_promotion": "NOT_CLAIMED",
        },
        "next_target": (
            "Compute a generic-u2 unit certificate over F_101(u2) at fixed u1 and "
            "extract its denominator polynomial. Only roots of that denominator can "
            "support exceptional u2 lines; then test those lines and the simultaneous "
            "R/D locus exactly."
        ),
        "claim_boundary": (
            "This is an exact algebraic theorem for four displayed R-only restrictions. "
            "It neither classifies the other 39,996 finite parameter lines nor proves "
            "that the full R-only locus, the simultaneous R/D locus, or selected "
            "physical q79 quantum gravity is empty."
        ),
        "new_continuous_fit_parameters": 0,
    }
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(certificate, indent=2) + "\n", encoding="utf-8")
    print(certificate["status"])
    print(f"checks={sum(checks.values())}/{len(checks)}")
    print(args.output)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
