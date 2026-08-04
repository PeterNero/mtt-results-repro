#!/usr/bin/env python3
"""Emit all exact nonzero-u2 symbolic saturation lines at one q79 u1 value."""

from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path

from flint import nmod_mpoly_ctx

from build_q79_D10_D6_h1_g1_pair_quotient_obstructions import (
    PRIME,
    parse_input,
    parse_polynomial,
)


SELECTED_ROWS = tuple(range(1, 13))


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
    parser.add_argument("--space", type=int, choices=(5, 6), required=True)
    parser.add_argument("--u1", type=int, default=1)
    parser.add_argument("--output-dir", type=Path, required=True)
    parser.add_argument("--packet", type=Path, required=True)
    args = parser.parse_args()

    names, field, texts = parse_input(args.input)
    require(field == PRIME and len(names) == 15 and len(texts) == 14, "core input")
    source_context = nmod_mpoly_ctx.get(names, ordering="degrevlex", modulus=PRIME)
    source_rows = [parse_polynomial(text, source_context, names) for text in texts]
    source_generators = dict(zip(names, source_context.gens()))
    require(
        source_rows[0] == source_generators["u0"] * source_generators["u1"] ** 2 - 1,
        "u endpoint",
    )
    require(
        source_rows[13]
        == source_generators["t"]
        * source_generators["u2"]
        * source_generators["u3"]
        - 1,
        "saturation row",
    )

    u1 = args.u1 % PRIME
    require(u1 != 0, "nonzero u1")
    u0 = pow(u1, -2, PRIME)
    target_names = tuple(name for name in names if name not in {"u0", "u1", "u2"})
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
            "t",
        ),
        "target variable order",
    )
    target_context = nmod_mpoly_ctx.get(
        target_names, ordering="degrevlex", modulus=PRIME
    )
    target_generators = dict(zip(target_names, target_context.gens()))
    expected_saturation = target_generators["t"] * target_generators["u3"] - 1
    args.output_dir.mkdir(parents=True, exist_ok=True)

    records = []
    supports_by_u2: dict[int, list[set[tuple[int, ...]]]] = {}
    for u2 in range(1, PRIME):
        composition = []
        for name in names:
            if name == "u0":
                composition.append(target_context.constant(u0))
            elif name == "u1":
                composition.append(target_context.constant(u1))
            elif name == "u2":
                composition.append(target_context.constant(u2))
            elif name == "t":
                composition.append(
                    target_generators["t"] * target_context.constant(pow(u2, -1, PRIME))
                )
            else:
                composition.append(target_generators[name])
        rows = [row.compose(*composition, ctx=target_context) for row in source_rows]
        require(rows[0] == target_context.constant(0), "endpoint vanishes")
        require(rows[13] == expected_saturation, "normalized saturation")
        output_rows = [rows[index] for index in SELECTED_ROWS] + [rows[13]]
        require(max(int(row.total_degree()) for row in output_rows) <= 3, "cubic rows")
        output_path = args.output_dir / f"space{args.space}_u1_{u1:03d}_u2_{u2:03d}.msolve.in"
        output_text = (
            ",".join(target_names)
            + f"\n{PRIME}\n"
            + ",\n".join(str(row) for row in output_rows)
            + "\n"
        )
        output_path.write_text(output_text, encoding="ascii", newline="\n")
        row_supports = [set(row.to_dict()) for row in output_rows]
        supports_by_u2[u2] = row_supports
        records.append(
            {
                "u2": u2,
                "input": checksum(output_path),
                "row_term_counts": [len(support) for support in row_supports],
            }
        )

    union_supports = []
    for row_index in range(13):
        union = set()
        for u2 in range(1, PRIME):
            union.update(supports_by_u2[u2][row_index])
        union_supports.append(union)
    full_support_values = [
        u2
        for u2 in range(1, PRIME)
        if all(
            supports_by_u2[u2][row_index] == union_supports[row_index]
            for row_index in range(13)
        )
    ]
    packet = {
        "schema": "MTTQ79RonlyFixedU1U2SymbolicFamily.v1",
        "date": "2026-07-20",
        "status": "EXACT_100_NONZERO_U2_SYMBOLIC_INPUTS_EMITTED",
        "field": "F_101",
        "space_index": args.space,
        "fixed_u1": u1,
        "endpoint_selected_u0": u0,
        "generic_line_relation": "t*u3=1",
        "parent_input": checksum(args.input),
        "variables": list(target_names),
        "selected_parent_rows": list(SELECTED_ROWS),
        "records": records,
        "union_row_term_counts": [len(support) for support in union_supports],
        "full_union_support_specializations": full_support_values,
        "checks": {
            "all_100_nonzero_u2_values_are_emitted": len(records) == 100,
            "u0_is_selected_exactly_by_the_endpoint": True,
            "saturation_is_normalized_by_an_invertible_t_rescaling": True,
            "all_inputs_have_12_variables_and_13_cubic_rows": True,
            "class_and_a_labels_are_replaced_by_the_class_free_u2_coordinate": True,
            "no_D_terminal_is_used": True,
            "no_continuous_fit_parameter_is_added": True,
        },
        "claim_boundary": (
            "This is an exact family emission and support atlas, not an emptiness result. "
            "Each input still requires an exact unit/nonunit certificate."
        ),
        "new_continuous_fit_parameters": 0,
    }
    args.packet.parent.mkdir(parents=True, exist_ok=True)
    args.packet.write_text(json.dumps(packet, indent=2) + "\n", encoding="utf-8")
    print(packet["status"])
    print(f"full_union_support_values={full_support_values}")
    print(args.packet)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
