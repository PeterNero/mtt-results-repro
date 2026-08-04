#!/usr/bin/env python3
"""Verify the exact (a,v) -> (-a,-v) involution of q79 inverse-root charts."""

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
    parser.add_argument("--input", type=Path, action="append", required=True)
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()
    require(len(args.input) == 4 and len(set(args.input)) == 4, "four distinct chart inputs")

    charts = []
    identified = set()
    for path in args.input:
        match = re.search(r"space_(5|6).*class(1|2)", path.name)
        require(match is not None, "space and scalar class in filename")
        key = (int(match.group(1)), int(match.group(2)))
        require(key not in identified, "one input per chart")
        identified.add(key)

        names, field, texts = parse_input(path)
        require(field == PRIME and len(names) == 19 and len(texts) == 22, "parent chart shape")
        context = nmod_mpoly_ctx.get(names, ordering="degrevlex", modulus=PRIME)
        rows = [parse_polynomial(text, context, names) for text in texts]
        positions = {name: index for index, name in enumerate(names)}
        v_position = positions["v"]
        even_rows = []
        for row_index, row in enumerate(rows):
            even = all(
                int(monomial[v_position]) % 2 == 0 for monomial in row.to_dict()
            )
            require(even, f"chart {key} row {row_index} is even in v")
            even_rows.append(row_index)

        generators = dict(zip(names, context.gens()))
        composition = [
            -generators[name] if name == "v" else generators[name] for name in names
        ]
        require(
            all(row.compose(*composition, ctx=context) == row for row in rows),
            f"chart {key} fixed by v sign",
        )
        scalar_class = key[1]
        require(
            rows[0] == generators["u0"] * generators["u1"] ** 2 - 1,
            f"chart {key} first endpoint",
        )
        require(
            rows[13]
            == generators["v"] ** 2
            * generators["u2"]
            * generators["u3"] ** 2
            - scalar_class,
            f"chart {key} scalar endpoint",
        )
        charts.append(
            {
                "space_index": key[0],
                "scalar_square_class_representative": scalar_class,
                "input": checksum(path),
                "row_count": len(rows),
                "even_in_v_parent_rows": even_rows,
            }
        )

    require(identified == {(5, 1), (5, 2), (6, 1), (6, 2)}, "complete chart set")

    line_context = nmod_mpoly_ctx.get(
        ("a", "u3", "v"), ordering="degrevlex", modulus=PRIME
    )
    a, u3, v = line_context.gens()
    line = v * u3 - a
    transformed_line = line.compose(-a, u3, -v, ctx=line_context)
    require(transformed_line == -line, "line equation transported up to a unit")

    scalar_selection_checks = 0
    line_point_checks = 0
    for scalar_class in (1, 2):
        for a_value in range(1, PRIME):
            minus_a = -a_value % PRIME
            selected_u2 = scalar_class * pow(a_value, -2, PRIME) % PRIME
            selected_minus_u2 = scalar_class * pow(minus_a, -2, PRIME) % PRIME
            require(selected_u2 == selected_minus_u2, "u2 sign invariance")
            scalar_selection_checks += 1
            for v_value in range(1, PRIME):
                u3_value = a_value * pow(v_value, -1, PRIME) % PRIME
                partner_u3 = minus_a * pow(-v_value % PRIME, -1, PRIME) % PRIME
                require(u3_value == partner_u3, "u3 fixed under paired signs")
                line_point_checks += 1

    checks = {
        "all_four_inverse_root_parent_charts_are_included": True,
        "all_88_parent_rows_are_even_in_v": True,
        "substitution_v_to_minus_v_fixes_every_parent_polynomial": True,
        "line_equation_vu3_minus_a_maps_to_its_negative": True,
        "selected_u2_equals_s_times_a_inverse_squared_and_is_sign_invariant": True,
        "u3_equals_a_over_v_is_fixed_under_the_paired_sign_change": True,
        "all_200_scalar_selection_cases_are_exhausted": scalar_selection_checks == 200,
        "all_20000_nonzero_line_point_cases_are_exhausted": line_point_checks == 20_000,
        "no_continuous_fit_parameter_is_added": True,
    }
    require(all(checks.values()), "sign involution checks")

    result = {
        "schema": "MTTQ79InverseRootVSignInvolution.v1",
        "date": "2026-07-20",
        "status": "EXACT_FULL_PARENT_SIGN_INVOLUTION_AND_CANONICAL_A_COVER",
        "field": "F_101",
        "charts": sorted(
            charts,
            key=lambda row: (
                row["space_index"], row["scalar_square_class_representative"]
            ),
        ),
        "involution": {
            "parameter_map": {"a": "-a", "v": "-v"},
            "fixed_coordinates": [
                "h1",
                "h2",
                "h3",
                "h4",
                "h5",
                "h6",
                "y1",
                "y2",
                "y3",
                "y4",
                "u0",
                "u1",
                "u2",
                "u3",
                "u4",
                "u5",
                "u6",
                "u7",
            ],
            "line_relation_transport": "v*u3-a maps to -(v*u3-a)",
            "order": 2,
        },
        "finite_exhaustion": {
            "nonzero_a_values": PRIME - 1,
            "canonical_representatives": list(range(1, 51)),
            "partner_rule": "a_partner=101-a",
            "scalar_selection_checks": scalar_selection_checks,
            "line_point_checks": line_point_checks,
        },
        "checks": checks,
        "theorem": (
            "For every selected inverse-root parent chart, all 22 parent rows are even "
            "in v. The simultaneous transformation (a,v)->(-a,-v) fixes every parent "
            "row and carries v*u3-a to its negative, while u2=s*a^(-2) and u3=a/v "
            "remain unchanged. Therefore each nonzero a-line and its sign partner are "
            "isomorphic as complete R/y/D schemes. The representatives a=1,...,50 "
            "form an exact canonical cover of all 100 nonzero a values."
        ),
        "claim_boundary": (
            "This is an algebraic orbit reduction inside the finite inverse-root charts. "
            "It does not select a physical chirality, causal branch, or arrow of time."
        ),
        "new_continuous_fit_parameters": 0,
    }
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
    print(result["status"])
    print("parent_rows=88/88; scalar_cases=200/200; line_points=20000/20000")
    print(args.output)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
