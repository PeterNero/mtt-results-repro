#!/usr/bin/env python3
"""Freeze the exact R-only q79 triple-fiber unit and degree lower bound."""

from __future__ import annotations

import argparse
import hashlib
import json
import re
from pathlib import Path


RECURRENCE_ROWS = [1, 2, 3, 4, 5, 6, 14, 15, 16, 17]
R_TERMINAL_ROWS = [7, 8, 9, 10, 11, 12]


def require(condition: bool, label: str) -> None:
    if not condition:
        raise AssertionError(label)


def checksum(path: Path) -> dict[str, object]:
    return {
        "path": str(path),
        "bytes": path.stat().st_size,
        "sha256": hashlib.sha256(path.read_bytes()).hexdigest(),
    }


def load_json(path: Path) -> dict[str, object]:
    return json.loads(path.read_text(encoding="utf-8"))


def exact_rank(path: Path) -> dict[str, int]:
    data = path.read_bytes()
    text = data.decode("utf-16") if data.startswith(b"\xff\xfe") else data.decode(
        "utf-8", errors="replace"
    )
    matches = re.findall(
        r"EXACT_SPARSE_ELIMINATION_RANK rows=(\d+) columns=(\d+) rank=(\d+)",
        text,
    )
    require(len(matches) == 1, f"one exact rank in {path.name}")
    rows, columns, rank = (int(value) for value in matches[0])
    require("Exit status: 0" in text, f"successful exact rank in {path.name}")
    return {"rows": rows, "columns": columns, "rank": rank}


def is_unit_msolve_output(path: Path) -> bool:
    text = path.read_text(encoding="ascii")
    return (
        "#field characteristic: 101" in text
        and "#length of basis:      1 element" in text
        and text.rstrip().endswith("[1]:")
    )


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--parent-input", type=Path, required=True)
    parser.add_argument("--direct-f4-packet", type=Path, required=True)
    parser.add_argument("--carrier-input-packet", type=Path, required=True)
    parser.add_argument("--carrier-input", type=Path, required=True)
    parser.add_argument("--carrier-linalg1-output", type=Path, required=True)
    parser.add_argument("--carrier-linalg2-output", type=Path, required=True)
    parser.add_argument("--D6-packet", type=Path, required=True)
    parser.add_argument("--D6-augmented-packet", type=Path, required=True)
    parser.add_argument("--D6-rank-log", type=Path, required=True)
    parser.add_argument("--D6-augmented-rank-log", type=Path, required=True)
    parser.add_argument("--D7-packet", type=Path, required=True)
    parser.add_argument("--D7-augmented-packet", type=Path, required=True)
    parser.add_argument("--D7-rank-log", type=Path, required=True)
    parser.add_argument("--D7-augmented-rank-log", type=Path, required=True)
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()

    parent = checksum(args.parent_input)
    direct = load_json(args.direct_f4_packet)
    require(direct["input"]["sha256"] == parent["sha256"], "direct input binding")
    require(
        direct["selected_parent_row_indices"] == RECURRENCE_ROWS + R_TERMINAL_ROWS,
        "direct R-only rows",
    )
    require(
        direct["exact_unit_samples"] == 1
        and direct["outcomes"][0]["status"] == "EXACT_UNIT_GROEBNER_BASIS"
        and direct["outcomes"][0]["output_text"].rstrip().endswith("[1]:"),
        "direct exact unit basis",
    )

    carrier_packet = load_json(args.carrier_input_packet)
    carrier = checksum(args.carrier_input)
    require(
        carrier_packet["status"] == "EXACT_REDUCED_CARRIER_INPUT_EMITTED"
        and carrier_packet["input"]["sha256"] == parent["sha256"]
        and carrier_packet["terminal_parent_rows"] == R_TERMINAL_ROWS
        and carrier_packet["carrier_input"]["sha256"] == carrier["sha256"],
        "carrier reduction binding",
    )
    require(
        is_unit_msolve_output(args.carrier_linalg1_output)
        and is_unit_msolve_output(args.carrier_linalg2_output),
        "two exact carrier unit outputs",
    )

    degree_packets = {
        6: (load_json(args.D6_packet), load_json(args.D6_augmented_packet)),
        7: (load_json(args.D7_packet), load_json(args.D7_augmented_packet)),
    }
    ranks = {
        6: {
            "operator": exact_rank(args.D6_rank_log),
            "augmented": exact_rank(args.D6_augmented_rank_log),
        },
        7: {
            "operator": exact_rank(args.D7_rank_log),
            "augmented": exact_rank(args.D7_augmented_rank_log),
        },
    }
    expected = {
        6: {"rows": 38760, "columns": 15640, "rank": 14831},
        7: {"rows": 116280, "columns": 66096, "rank": 58490},
    }
    for degree in (6, 7):
        operator_packet, augmented_packet = degree_packets[degree]
        operator = operator_packet["operator"]
        require(
            operator_packet["input"]["sha256"] == parent["sha256"]
            and operator_packet["row_partition"]["recurrence_parent_rows"]
            == RECURRENCE_ROWS
            and operator_packet["row_partition"]["terminal_parent_rows"]
            == R_TERMINAL_ROWS
            and operator_packet["maximum_product_total_degree"] == degree,
            f"degree {degree} operator binding",
        )
        require(
            ranks[degree]["operator"] == expected[degree]
            and ranks[degree]["augmented"]
            == {
                "rows": expected[degree]["rows"],
                "columns": expected[degree]["columns"] + 1,
                "rank": expected[degree]["rank"] + 1,
            },
            f"degree {degree} exact rank jump",
        )
        require(
            operator["rows"] == expected[degree]["rows"]
            and operator["columns"] == expected[degree]["columns"]
            and augmented_packet["dimensions"]["augmented_columns"]
            == expected[degree]["columns"] + 1,
            f"degree {degree} dimensions",
        )

    packet = {
        "schema": "MTTQ79RonlyTripleFiberUnitAndMinDegreeFrontier.v1",
        "date": "2026-07-20",
        "status": "EXACT_R_ONLY_TRIPLE_FIBER_UNIT_WITH_CERTIFICATE_DEGREE_AT_LEAST_8",
        "field": "F_101",
        "parent_input": parent,
        "fiber": {
            "space": 5,
            "scalar_square_class_representative": 1,
            "u1": 1,
            "a_equals_v_times_u3": 1,
            "v": 1,
            "forced_assignments": {"u0": 1, "u2": 1, "u3": 1},
        },
        "selected_rows": {
            "recurrence_parent_rows": RECURRENCE_ROWS,
            "R_terminal_parent_rows": R_TERMINAL_ROWS,
            "D_terminal_rows_used": [],
        },
        "unit_membership": {
            "direct_fourteen_variable_msolve": checksum(args.direct_f4_packet),
            "four_carrier_input": carrier,
            "four_carrier_msolve_exact_linalg1": checksum(args.carrier_linalg1_output),
            "four_carrier_msolve_exact_linalg2": checksum(args.carrier_linalg2_output),
            "quotient_implication": (
                "The six carrier remainders generate 1 modulo the ten recurrence "
                "rows; hence the original ten recurrence plus six R-terminal rows "
                "generate 1 on this fiber."
            ),
        },
        "ordinary_total_degree_obstructions": {
            "degree_6": ranks[6],
            "degree_7": ranks[7],
            "theorem": (
                "For D=6 and D=7, rank([A_D|e_1])=rank(A_D)+1. Therefore no "
                "Nullstellensatz multiplier identity exists with maximum product "
                "total degree at most 7 in this selected generating set."
            ),
            "first_unexcluded_degree": 8,
        },
        "open_provenance_layer": {
            "expanded_six_carrier_multipliers": False,
            "expanded_sixteen_original_row_multipliers": False,
            "mathematical_unit_membership": True,
            "reason": (
                "Eager change-matrix and target-only lift implementations timed out; "
                "this is a certificate-expansion problem, not an open unit-membership problem."
            ),
        },
        "checks": {
            "direct_R_only_unit_basis_is_exact": True,
            "carrier_reduction_is_hash_bound_to_the_same_parent_input": True,
            "two_exact_msolve_linear_algebra_modes_return_the_unit_basis": True,
            "degree_6_rank_jump_is_deterministic_sparse_elimination": True,
            "degree_7_rank_jump_is_deterministic_sparse_elimination": True,
            "D_terminal_rows_are_not_used": True,
            "no_continuous_fit_parameter_is_added": True,
        },
        "claim_boundary": (
            "This is an exact theorem for one displayed R-only triple fiber. It does "
            "not classify the one million triples in its scalar chart, the other "
            "mirror charts, or promote this finite-field obstruction to physical HYM/QG data."
        ),
        "new_continuous_fit_parameters": 0,
    }
    require(all(packet["checks"].values()), "all frontier checks")
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(packet, indent=2) + "\n", encoding="utf-8")
    print("Q79_RONLY_TRIPLE_FIBER_MIN_DEGREE_FRONTIER_PASS")
    print(args.output)


if __name__ == "__main__":
    main()
