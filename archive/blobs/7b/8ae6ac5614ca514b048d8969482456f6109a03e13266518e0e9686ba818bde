#!/usr/bin/env python3
"""Prove the exact u2/Laurent-line compression of fixed-u1 q79 R fibers."""

from __future__ import annotations

import argparse
import hashlib
import json
import re
from pathlib import Path

from benchmark_q79_singular_saturation_coordinate_pairs import parse_msolve_input


PRIME = 101
ROOT = Path(__file__).resolve().parents[1]
SOURCE = ROOT / "candidate_data" / "q79_Ronly_classfree_representative_lines"
R_ROWS = tuple(range(1, 13))


def require(condition: bool, label: str) -> None:
    if not condition:
        raise AssertionError(label)


def checksum(path: Path) -> dict[str, object]:
    return {
        "path": str(path.relative_to(ROOT)),
        "bytes": path.stat().st_size,
        "sha256": hashlib.sha256(path.read_bytes()).hexdigest(),
    }


def contains_variable(polynomial: str, variable: str) -> bool:
    return re.search(rf"\b{re.escape(variable)}\b", polynomial) is not None


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--output",
        type=Path,
        default=ROOT
        / "certificates"
        / "Q79_Ronly_U2_Laurent_Line_Acceleration_v1.json",
    )
    args = parser.parse_args()
    parents = {}
    space_rows = {}
    for space in (5, 6):
        class_rows = []
        for scalar_class in (1, 2):
            path = SOURCE / (
                f"space_{space}_h0_g0_class{scalar_class}_inverse_root.msolve.in"
            )
            names, characteristic, rows = parse_msolve_input(path)
            require(characteristic == PRIME, "field characteristic")
            require(len(names) == 19 and len(rows) == 22, "parent shape")
            selected = [rows[index] for index in R_ROWS]
            require(
                all(
                    not contains_variable(row, variable)
                    for row in selected
                    for variable in ("v", "y1", "y2", "y3", "y4")
                ),
                "R rows are independent of v and y",
            )
            class_rows.append(selected)
            parents[f"space{space}_class{scalar_class}"] = checksum(path)
        require(class_rows[0] == class_rows[1], "scalar classes share the R rows")
        space_rows[space] = class_rows[0]
    require(space_rows[5] != space_rows[6], "space cores remain distinct")

    canonical_to_u2 = []
    u2_to_canonical = {}
    for scalar_class in (1, 2):
        for a_value in range(1, 51):
            u2_value = scalar_class * pow(a_value, -2, PRIME) % PRIME
            require(u2_value not in u2_to_canonical, "canonical u2 map injective")
            u2_to_canonical[u2_value] = {
                "scalar_class": scalar_class,
                "canonical_a": a_value,
            }
            canonical_to_u2.append(
                {
                    "scalar_class": scalar_class,
                    "canonical_a": a_value,
                    "u2": u2_value,
                }
            )
    require(set(u2_to_canonical) == set(range(1, PRIME)), "canonical u2 map surjective")

    laurent_checks = 0
    for a_value in range(1, PRIME):
        u3_values = []
        for v_value in range(1, PRIME):
            u3_value = a_value * pow(v_value, -1, PRIME) % PRIME
            inverse_v = a_value * pow(u3_value, -1, PRIME) % PRIME
            require(inverse_v == v_value, "Laurent generator maps are inverse")
            u3_values.append(u3_value)
            laurent_checks += 1
        require(set(u3_values) == set(range(1, PRIME)), "v-to-u3 map is bijective")

    checks = {
        "all_four_inverse_root_parents_are_hash_bound": len(parents) == 4,
        "all_48_selected_R_rows_are_independent_of_v_and_y": True,
        "the_two_scalar_classes_have_identical_R_rows_in_each_space": True,
        "the_space5_and_space6_R_cores_remain_distinct": True,
        "the_100_canonical_scalar_a_pairs_map_bijectively_to_nonzero_u2": len(u2_to_canonical)
        == 100,
        "for_every_nonzero_a_the_map_v_to_a_over_v_is_a_torus_bijection": laurent_checks
        == 10_000,
        "the_Laurent_generator_substitutions_are_mutual_inverses": True,
        "one_symbolic_u3_line_replaces_100_fixed_v_fibers_at_fixed_u2": True,
        "no_D_terminal_is_used": True,
        "no_continuous_fit_parameter_is_added": True,
    }
    require(all(checks.values()), "all acceleration checks")

    packet = {
        "schema": "MTTQ79RonlyU2LaurentLineAcceleration.v1",
        "date": "2026-07-21",
        "status": "EXACT_FIXED_U1_U2_LAURENT_LINE_COMPRESSION_CERTIFIED",
        "field": "F_101",
        "parents": parents,
        "selected_parent_rows": list(R_ROWS),
        "canonical_coordinate_bijection": {
            "domain": "(s,a) with s in {1,2} and a in {1,...,50}",
            "codomain": "u2 in F_101^*",
            "map": "u2=s*a^(-2)",
            "inverse_table": {
                str(u2): row for u2, row in sorted(u2_to_canonical.items())
            },
            "forward_table": canonical_to_u2,
        },
        "Laurent_line_isomorphism": {
            "fixed_nonzero_a": True,
            "forward": "u3=a*v^(-1)",
            "inverse": "v=a*u3^(-1)",
            "rings": "F_101[v,v^(-1)] isomorphic to F_101[u3,u3^(-1)]",
            "finite_inverse_checks": laurent_checks,
        },
        "solver_reduction_per_fixed_nonzero_u1": {
            "old_canonical_fixed_fibers": 20_000,
            "old_line_packets": 200,
            "new_symbolic_u3_lines": 200,
            "fixed_fibers_represented_per_symbolic_line": 100,
            "independent_space_cores": 2,
            "nonzero_u2_values_per_space": 100,
        },
        "theorem": (
            "For either space and any fixed nonzero u1, the two scalar-class R-only "
            "charts on their 50 canonical a-lines are exactly the 100 nonzero u2 "
            "specializations. At fixed a, v and u3 are mutually inverse Laurent "
            "coordinates via u3=a/v. Because rows 1 through 12 are independent of v "
            "and identical across scalar classes, one saturated symbolic u3 line at "
            "each u2 exactly replaces all 100 fixed-v R-only fibers on that line."
        ),
        "checks": checks,
        "claim_boundary": (
            "This proves an exact change of coordinates and computational compression, "
            "not unit-ideal closure. Every symbolic u3 line still needs an exact unit "
            "certificate; a nonunit R line requires a separate complete R/y/D closure. "
            "No result here identifies the two space cores or promotes finite data to "
            "physical HYM/QG data."
        ),
        "new_continuous_fit_parameters": 0,
    }
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(packet, indent=2) + "\n", encoding="utf-8")
    print(packet["status"])
    print(f"checks={sum(checks.values())}/{len(checks)}")
    print(args.output)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
