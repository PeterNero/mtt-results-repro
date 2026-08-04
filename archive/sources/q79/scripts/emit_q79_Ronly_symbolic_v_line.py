#!/usr/bin/env python3
"""Emit one exact symbolic-v line of a selected q79 R-only chart."""

from __future__ import annotations

import argparse
import hashlib
import json
import re
from pathlib import Path

from flint import nmod_mpoly_ctx

from build_q79_D10_D6_h1_g1_pair_quotient_obstructions import (
    PRIME,
    parse_input,
    parse_polynomial,
)


SELECTED_PARENT_ROWS = tuple(range(1, 13))
DROPPED_Y_VARIABLES = ("y1", "y2", "y3", "y4")


def require(condition: bool, label: str) -> None:
    if not condition:
        raise AssertionError(label)


def checksum(path: Path) -> dict[str, object]:
    return {
        "path": str(path),
        "bytes": path.stat().st_size,
        "sha256": hashlib.sha256(path.read_bytes()).hexdigest(),
    }


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--input", type=Path, required=True)
    parser.add_argument("--scalar-class", type=int, choices=(1, 2), required=True)
    parser.add_argument("--u1", type=int, required=True)
    parser.add_argument("--a", type=int, required=True)
    parser.add_argument("--output", type=Path, required=True)
    parser.add_argument("--packet", type=Path, required=True)
    args = parser.parse_args()

    names, field, texts = parse_input(args.input)
    require(field == PRIME and len(names) == 19 and len(texts) == 22, "parent input")
    source_context = nmod_mpoly_ctx.get(names, ordering="degrevlex", modulus=PRIME)
    source_rows = [parse_polynomial(text, source_context, names) for text in texts]
    source_generator = dict(zip(names, source_context.gens()))
    require(
        source_rows[0] == source_generator["u0"] * source_generator["u1"] ** 2 - 1,
        "u endpoint row",
    )
    require(
        source_rows[13]
        == source_generator["v"] ** 2
        * source_generator["u2"]
        * source_generator["u3"] ** 2
        - args.scalar_class,
        "scalar endpoint row",
    )
    for row_index in SELECTED_PARENT_ROWS:
        require(
            not any(
                re.search(rf"\b{re.escape(name)}\b", texts[row_index])
                for name in DROPPED_Y_VARIABLES
            ),
            f"reconstructible y variable absent from selected row {row_index}",
        )

    u1 = args.u1 % PRIME
    a_value = args.a % PRIME
    require(u1 != 0 and a_value != 0, "nonzero line coordinates")
    assignments = {
        "u0": pow(u1, -2, PRIME),
        "u1": u1,
        "u2": args.scalar_class * pow(a_value, -2, PRIME) % PRIME,
    }
    omitted_names = set(assignments) | set(DROPPED_Y_VARIABLES)
    target_names = tuple(name for name in names if name not in omitted_names)
    require(
        target_names
        == (
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
        ),
        "symbolic line variable order",
    )
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
    rows = [row.compose(*composition, ctx=target_context) for row in source_rows]
    require(rows[0] == target_context.constant(0), "u endpoint vanishes")

    vu3 = target_generator["v"] * target_generator["u3"]
    line_row = vu3 - a_value
    endpoint_factor = (
        target_context.constant(args.scalar_class * pow(a_value, -2, PRIME) % PRIME)
        * line_row
        * (vu3 + a_value)
    )
    require(rows[13] == endpoint_factor, "line relation exactly factors scalar endpoint")
    selected_rows = [rows[index] for index in SELECTED_PARENT_ROWS]
    output_rows = selected_rows + [line_row]
    require(len(target_names) == 12 and len(output_rows) == 13, "symbolic line shape")
    require(max(int(row.total_degree()) for row in output_rows) <= 3, "cubic bound")

    output_text = (
        ",".join(target_names)
        + "\n101\n"
        + ",\n".join(str(row) for row in output_rows)
        + "\n"
    )
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(output_text, encoding="ascii", newline="\n")
    packet = {
        "schema": "MTTQ79RonlySymbolicVLineInput.v1",
        "date": "2026-07-20",
        "status": "EXACT_SELECTED_SYMBOLIC_V_LINE_INPUT",
        "field": "F_101",
        "parent_input": checksum(args.input),
        "scalar_square_class_representative": args.scalar_class,
        "fixed_coordinates": {
            "u1": u1,
            "a_equals_v_times_u3": a_value,
            "selected_u0": assignments["u0"],
            "selected_u2": assignments["u2"],
        },
        "variables": list(target_names),
        "selected_parent_rows": list(SELECTED_PARENT_ROWS),
        "added_exact_line_relation": f"v*u3-{a_value}=0",
        "row_term_counts": [len(row.to_dict()) for row in output_rows],
        "maximum_total_degree": max(int(row.total_degree()) for row in output_rows),
        "output": checksum(args.output),
        "checks": {
            "u_endpoint_is_eliminated_by_unique_nonzero_u1_solution": True,
            "line_relation_exactly_factors_scalar_endpoint": True,
            "selected_hR_rows_are_independent_of_reconstructible_y_variables": True,
            "symbolic_line_has_12_variables_and_13_rows": True,
            "all_rows_have_total_degree_at_most_three": True,
            "no_continuous_fit_parameter_is_added": True,
        },
        "equivalence": (
            "This input is the exact selected h/R restriction to the line with fixed "
            "nonzero u1 and a=v*u3. On that line the omitted endpoint row is a multiple "
            "of v*u3-a and therefore vanishes identically. The four omitted y rows have "
            "constant pivots and are uniquely reconstructible after any h/R solution."
        ),
        "claim_boundary": (
            "Emission is not an emptiness result. A literal unit Groebner basis or an "
            "independent exact certificate is required to close the whole symbolic line."
        ),
        "new_continuous_fit_parameters": 0,
    }
    args.packet.parent.mkdir(parents=True, exist_ok=True)
    args.packet.write_text(json.dumps(packet, indent=2) + "\n", encoding="utf-8")
    print("Q79_RONLY_SYMBOLIC_V_LINE_EMIT_OK")
    print(args.output)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
