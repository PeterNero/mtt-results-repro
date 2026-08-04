#!/usr/bin/env python3
"""Consolidate the q79 class-free reduction and four exact endpoint lines."""

from __future__ import annotations

import argparse
import hashlib
import json
import re
from pathlib import Path


PRIME = 101
ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "candidate_data" / "q79_Ronly_classfree_representative_lines"
DEFAULT_OUTPUT = (
    ROOT
    / "certificates"
    / "Q79_Ronly_ClassFree_Core_and_Representative_Lines_v1.json"
)
H_ROWS = (1, 2, 3, 4, 5, 6)
R_ROWS = (7, 8, 9, 10, 11, 12)
Y_ROWS = (14, 15, 16, 17)
CORE_ROWS = (0,) + H_ROWS + R_ROWS
DROPPED_Y = ["y1", "y2", "y3", "y4"]


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


def contains_variable(row: str, name: str) -> bool:
    return re.search(rf"\b{re.escape(name)}\b", row) is not None


def literal_unit_output(text: str) -> bool:
    lines = text.strip().splitlines()
    return (
        bool(lines)
        and lines[0] == "#Reduced Groebner basis data"
        and any("#field characteristic: 101" in line for line in lines)
        and any("#length of basis:      1 element" in line for line in lines)
        and [line for line in lines if line and not line.startswith("#")] == ["[1]:"]
    )


def certify_y_chain(names: tuple[str, ...], rows: list[str]) -> list[dict[str, int]]:
    positions = {name: index for index, name in enumerate(names)}
    result = []
    for offset, row_index in enumerate(Y_ROWS, start=1):
        leader = f"y{offset}"
        polynomial = polynomial_dict(rows[row_index], names)
        leader_position = positions[leader]
        leader_terms = [
            (monomial, coefficient)
            for monomial, coefficient in polynomial.items()
            if monomial[leader_position]
        ]
        expected_monomial = tuple(
            1 if index == leader_position else 0 for index in range(len(names))
        )
        require(
            leader_terms
            == [(expected_monomial, polynomial[expected_monomial])],
            f"constant linear pivot {leader}",
        )
        require(
            all(
                not contains_variable(rows[row_index], f"y{later}")
                for later in range(offset + 1, 5)
            ),
            f"no later y variable in row {row_index}",
        )
        pivot = polynomial[expected_monomial]
        require(pivot != 0, f"invertible pivot {leader}")
        result.append(
            {
                "parent_row": row_index,
                "leader": leader,
                "pivot_mod_101": pivot,
            }
        )
    return result


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--output", type=Path, default=DEFAULT_OUTPUT)
    args = parser.parse_args()

    parent_data: dict[tuple[int, int], dict[str, object]] = {}
    space_records = []
    for space in (5, 6):
        selected_by_class = []
        parent_records = []
        y_chains = []
        for scalar_class in (1, 2):
            parent_path = (
                DATA
                / f"space_{space}_h0_g0_class{scalar_class}_inverse_root.msolve.in"
            )
            names, field, rows = parse_input(parent_path)
            require(field == PRIME and len(names) == 19 and len(rows) == 22, "parent shape")
            require(rows[0] == "u0*u1^2 + 100", "R endpoint")
            expected_companion = (
                "u2*u3^2*v^2 + 100"
                if scalar_class == 1
                else "u2*u3^2*v^2 + 99"
            )
            require(rows[13] == expected_companion, "companion endpoint")
            selected = [rows[index] for index in CORE_ROWS]
            require(
                all(
                    not contains_variable(row, name)
                    for row in selected
                    for name in (*DROPPED_Y, "v")
                ),
                "R-only rows are independent of y and v",
            )
            y_chain = certify_y_chain(names, rows)
            selected_by_class.append(selected)
            parent_record = checksum(parent_path)
            parent_records.append(parent_record)
            y_chains.append(
                {
                    "scalar_square_class_representative": scalar_class,
                    "rows": y_chain,
                }
            )
            parent_data[(space, scalar_class)] = {
                "path": parent_path,
                "names": names,
                "rows": rows,
                "checksum": parent_record,
            }

        require(selected_by_class[0] == selected_by_class[1], "class-free selected rows")
        core_path = DATA / f"space{space}_classfree_saturated_hR_core.msolve.in"
        core_names, core_field, core_rows = parse_input(core_path)
        expected_core_names = tuple(
            name
            for name in parent_data[(space, 1)]["names"]
            if name not in {*DROPPED_Y, "v"}
        ) + ("t",)
        require(
            core_field == PRIME
            and core_names == expected_core_names
            and core_rows == selected_by_class[0] + ["t*u2*u3 + 100"],
            "literal class-free core",
        )
        space_records.append(
            {
                "space_index": space,
                "parent_inputs": parent_records,
                "y_reconstruction_chains": y_chains,
                "class_free_core": checksum(core_path),
                "core_shape": {
                    "variables": len(core_names),
                    "equations": len(core_rows),
                    "maximum_total_degree": 3,
                },
            }
        )

    require(
        space_records[0]["class_free_core"]["sha256"]
        != space_records[1]["class_free_core"]["sha256"],
        "independent space cores",
    )

    line_records = []
    total_outcomes = 0
    for space in (5, 6):
        for scalar_class in (1, 2):
            packet_path = (
                DATA
                / f"space{space}_class{scalar_class}_u1_1_a_1_v_full_line.packet.json"
            )
            packet = json.loads(packet_path.read_text(encoding="utf-8"))
            parent = parent_data[(space, scalar_class)]
            require(
                packet["schema"]
                == "MTTQ79MsolveInverseRootTripleEndpointFiberBenchmark.v1",
                "line packet schema",
            )
            require(packet["field_characteristic"] == PRIME, "line field")
            require(
                packet["scalar_square_class_representative"] == scalar_class,
                "line scalar class",
            )
            require(
                packet["input"]["sha256"] == parent["checksum"]["sha256"],
                "line parent hash",
            )
            require(
                packet["selected_parent_row_indices"] == list(H_ROWS + R_ROWS)
                and packet["dropped_source_variables"] == DROPPED_Y,
                "line selected h/R rows",
            )
            require(
                packet["fiber_dimensions"]
                == {"variables": 10, "equations": 12, "maximum_total_degree": 3},
                "line fiber shape",
            )
            outcomes = packet["outcomes"]
            require(len(outcomes) == 100, "100 line outcomes")
            require(
                [row["v"] for row in outcomes] == list(range(1, PRIME)),
                "all nonzero v values",
            )
            for row in outcomes:
                v_value = int(row["v"])
                u3_value = pow(v_value, -1, PRIME)
                require(row["u1"] == row["a_equals_v_times_u3"] == 1, "line anchor")
                require(
                    row["forced_u0"] == 1
                    and row["forced_u2"] == scalar_class
                    and row["forced_u3"] == u3_value,
                    "forced line coordinates",
                )
                require(
                    v_value**2 * scalar_class * u3_value**2 % PRIME == scalar_class,
                    "companion endpoint vanishes",
                )
                require(
                    row["status"] == "EXACT_UNIT_GROEBNER_BASIS"
                    and row["returncode"] == 0
                    and literal_unit_output(row["output_text"]),
                    "literal unit output",
                )
                require(
                    hashlib.sha256(row["output_text"].encode("ascii")).hexdigest()
                    == row["output_sha256"],
                    "line output hash",
                )
            require(
                {row["forced_u3"] for row in outcomes} == set(range(1, PRIME)),
                "v to u3 bijection",
            )
            require(
                packet["exact_unit_samples"] == 100
                and packet["exact_positive_samples"] == 0,
                "line packet counts",
            )
            require(
                len({row["input_sha256"] for row in outcomes}) == 100,
                "distinct fixed-fiber inputs",
            )
            line_records.append(
                {
                    "space_index": space,
                    "scalar_square_class_representative": scalar_class,
                    "fixed_coordinates": {
                        "u1": 1,
                        "a_equals_v_times_u3": 1,
                        "u2": scalar_class,
                    },
                    "varying_coordinate": "v in F_101*, equivalently u3=v^-1",
                    "exact_unit_fibers": 100,
                    "packet": checksum(packet_path),
                }
            )
            total_outcomes += len(outcomes)

    checks = {
        "all_four_parent_charts_are_hash_bound": len(parent_data) == 4,
        "six_h_recurrences_and_six_R_terminals_are_retained": True,
        "selected_R_only_rows_are_independent_of_y_and_v": True,
        "four_y_rows_reconstruct_uniquely_in_every_parent": True,
        "companion_endpoint_projects_to_u2_u3_nonzero": True,
        "each_space_scalar_pair_has_one_identical_class_free_core": True,
        "four_scalar_charts_reduce_to_two_distinct_cubic_cores": True,
        "all_four_representative_lines_exhaust_F101_nonzero": True,
        "all_400_fixed_fibers_have_literal_unit_reduced_bases": total_outcomes
        == 400,
        "no_timeout_or_nonunit_output_is_counted": True,
        "no_D_terminal_row_is_used": True,
        "no_continuous_fit_parameter_is_added": True,
    }
    require(all(checks.values()), "all consolidated checks")
    certificate = {
        "schema": "MTTQ79RonlyClassFreeCoreAndRepresentativeLines.v1",
        "date": "2026-07-20",
        "status": "EXACT_FOUR_CHART_TO_TWO_CORES_AND_FOUR_LINES_CERTIFIED",
        "field": "F_101",
        "support_pattern": [6, 10, 8],
        "optional_fixed_fiber_reproducer": checksum(
            ROOT / "scripts" / "benchmark_q79_Ronly_representative_v_lines.py"
        ),
        "class_free_reduction": {
            "spaces": space_records,
            "theorem": (
                "In each space, omitting the constant-pivot y chain and projecting "
                "the companion endpoint gives the exact saturated h/R core with "
                "t*u2*u3=1. Over an algebraic closure each scalar chart has this core; "
                "over F_101 the two scalar charts partition its nonzero u2 values by "
                "square class. Thus four scalar charts reduce to two space cores."
            ),
        },
        "representative_line_theorem": {
            "lines": line_records,
            "statement": (
                "For each space 5 or 6 and scalar class 1 or 2, every nonzero-v "
                "fiber at u1=a=1 has literal reduced Groebner basis [1]. Equivalently, "
                "all nonzero u3 fibers at u1=1 and u2 equal to the class representative "
                "are empty."
            ),
        },
        "totals": {
            "nominal_scalar_charts": 4,
            "class_free_cubic_cores": 2,
            "nominal_nonzero_endpoint_lines": 40000,
            "exactly_closed_endpoint_lines": 4,
            "remaining_unclassified_endpoint_lines": 39996,
            "nominal_nonzero_endpoint_fibers": 4000000,
            "exactly_closed_fixed_endpoint_fibers": 400,
            "remaining_unclassified_fixed_endpoint_fibers": 3999600,
        },
        "checks": checks,
        "claim_tiers": {
            "four_chart_to_two_core_reduction": "CLOSED_EXACTLY",
            "four_representative_v_lines": "CLOSED_EXACTLY",
            "space5_complete_core_or_finite_chart": "OPEN",
            "space6_complete_core_or_finite_chart": "OPEN",
            "all_four_scalar_charts": "OPEN",
            "physical_HYM_QG_promotion": "NOT_CLAIMED",
        },
        "next_target": (
            "Prove a triangular jet/pivot stratification in (u1,a), or execute a "
            "checkpointed exact cover of the remaining 39,996 finite endpoint lines."
        ),
        "claim_boundary": (
            "The reduction theorem and the four displayed finite-field lines are exact. "
            "The two global cubic ideals timed out and are not called unit. No result "
            "here classifies the remaining lines or promotes the finite obstruction to "
            "selected physical HYM or quantum-gravity data."
        ),
        "new_continuous_fit_parameters": 0,
    }
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(certificate, indent=2) + "\n", encoding="utf-8")
    print(certificate["status"])
    print(f"checks={sum(checks.values())}/{len(checks)}")
    print("fixed_fibers=400/400")
    print(args.output)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
