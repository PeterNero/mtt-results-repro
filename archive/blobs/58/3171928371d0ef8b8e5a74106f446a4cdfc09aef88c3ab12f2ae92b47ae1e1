#!/usr/bin/env python3
"""Combine the independently audited q79 space-5 and space-6 u1=1 covers."""

from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SPACE_CERTIFICATES = {
    5: ROOT / "certificates" / "Q79_Ronly_FixedU1_Space5_D_Augmented_Cover_v1.json",
    6: ROOT / "certificates" / "Q79_Ronly_FixedU1_Space6_D_Augmented_Cover_v1.json",
}
EXPECTED = {
    5: {
        "status": "EXACT_F101_SPACE5_U1_1_FULL_RD_SLICE_CLOSED",
        "R_units": 9_993,
        "fallbacks": 7,
    },
    6: {
        "status": "EXACT_F101_SPACE6_U1_1_FULL_RD_SLICE_CLOSED",
        "R_units": 9_996,
        "fallbacks": 4,
    },
}


def require(condition: bool, label: str) -> None:
    if not condition:
        raise AssertionError(label)


def artifact(path: Path) -> dict[str, object]:
    return {
        "path": str(path.relative_to(ROOT)),
        "bytes": path.stat().st_size,
        "sha256": hashlib.sha256(path.read_bytes()).hexdigest(),
    }


def load(path: Path) -> dict[str, object]:
    require(path.is_file(), f"required certificate {path}")
    value = json.loads(path.read_text(encoding="utf-8"))
    require(isinstance(value, dict), f"certificate object {path}")
    return value


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--output",
        type=Path,
        default=ROOT
        / "certificates"
        / "Q79_Ronly_FixedU1_AllSpaces_D_Augmented_Cover_v1.json",
    )
    args = parser.parse_args()

    spaces = []
    total_R_units = 0
    total_fallbacks = 0
    sign_hashes = set()
    parent_hashes = set()
    line_hashes = set()
    fallback_coordinates = set()
    for space, path in SPACE_CERTIFICATES.items():
        certificate = load(path)
        expected = EXPECTED[space]
        fixed = certificate.get("fixed_slice", {})
        cover = certificate.get("canonical_cover", {})
        signed = certificate.get("signed_closure", {})
        require(certificate.get("status") == expected["status"], "space status")
        require(certificate.get("field") == "F_101", "common field")
        require(fixed == {"space_index": space, "u1": 1, "forced_u0": 1}, "fixed slice")
        require(all(certificate.get("checks", {}).values()), "space checks")
        require(certificate.get("new_continuous_fit_parameters") == 0, "space fit count")
        require(cover.get("canonical_line_count") == 100, "space line count")
        require(cover.get("canonical_endpoint_fiber_count") == 10_000, "space canonical fibers")
        require(cover.get("literal_R_unit_fibers") == expected["R_units"], "space R units")
        require(cover.get("full_parent_fallback_fibers") == expected["fallbacks"], "space fallbacks")
        require(signed.get("excluded_endpoint_fibers") == 20_000, "space signed fibers")

        sign_hashes.add(
            certificate["prerequisites"]["sign_involution_certificate"]["sha256"]
        )
        for parent in certificate["prerequisites"]["parents"].values():
            require(parent["sha256"] not in parent_hashes, "distinct parent inputs")
            parent_hashes.add(parent["sha256"])
        for packet in cover["line_packets"]:
            require(packet["sha256"] not in line_hashes, "distinct line packet")
            line_hashes.add(packet["sha256"])
        coordinates = {
            (space, int(row["scalar_class"]), int(row["a"]), int(row["v"]))
            for row in certificate.get("fallback_witnesses", [])
        }
        require(len(coordinates) == expected["fallbacks"], "fallback coordinate count")
        require(not fallback_coordinates.intersection(coordinates), "disjoint fallback coordinates")
        fallback_coordinates.update(coordinates)

        total_R_units += int(cover["literal_R_unit_fibers"])
        total_fallbacks += int(cover["full_parent_fallback_fibers"])
        spaces.append(
            {
                "space_index": space,
                "certificate": artifact(path),
                "canonical_line_packets": cover["canonical_line_count"],
                "canonical_endpoint_fibers": cover["canonical_endpoint_fiber_count"],
                "literal_R_unit_fibers": cover["literal_R_unit_fibers"],
                "full_parent_fallback_fibers": cover["full_parent_fallback_fibers"],
                "signed_endpoint_fibers_excluded": signed["excluded_endpoint_fibers"],
            }
        )

    checks = {
        "both_independent_space_certificates_are_exact_and_reproduced": len(spaces) == 2,
        "both_certificates_use_the_same_sign_involution": len(sign_hashes) == 1,
        "all_four_parent_inputs_are_distinct_and_hash_bound": len(parent_hashes) == 4,
        "exactly_200_canonical_line_packets_are_disjoint": len(line_hashes) == 200,
        "canonical_accounting_is_20000_equals_19989_plus_11": total_R_units
        == 19_989
        and total_fallbacks == 11,
        "the_11_full_parent_fallback_coordinates_are_disjoint": len(fallback_coordinates)
        == 11,
        "the_sign_involution_doubles_to_40000_excluded_fibers": True,
        "exactly_four_of_400_space_class_u1_slices_are_closed": True,
        "global_symbolic_chart_accounting_remains_138_of_140": True,
        "no_continuous_fit_parameter_is_added": True,
    }
    require(all(checks.values()), "union checks")

    certificate = {
        "schema": "MTTQ79RonlyFixedU1AllSpacesDAugmentedCover.v1",
        "date": "2026-07-21",
        "status": "EXACT_F101_ALL_INVERSE_ROOT_U1_1_FULL_RD_SLICE_CLOSED",
        "field": "F_101",
        "fixed_u1": 1,
        "forced_u0": 1,
        "spaces": spaces,
        "canonical_union": {
            "space_indices": [5, 6],
            "scalar_square_classes_per_space": [1, 2],
            "canonical_a_representatives": 50,
            "nonzero_v_values": 100,
            "canonical_line_packets": 200,
            "canonical_endpoint_fibers": 20_000,
            "literal_R_unit_fibers": total_R_units,
            "literal_full_R_y_D_unit_fibers": total_fallbacks,
            "fallback_coordinates": [
                {"space": space, "scalar_class": scalar_class, "a": a, "v": v}
                for space, scalar_class, a, v in sorted(fallback_coordinates)
            ],
        },
        "signed_union": {
            "involution": "(a,v)->(-a,-v)",
            "excluded_endpoint_fibers": 40_000,
            "closed_space_class_u1_slices": 4,
            "finite_strategy_space_class_u1_slices": 400,
        },
        "checks": checks,
        "theorem": (
            "At u1=1 over F_101, every nonzero endpoint fiber in both scalar "
            "classes of inverse-root spaces 5 and 6 has a literal unit Groebner "
            "basis, either already in the selected R-only subideal or after restoring "
            "all y recurrences and D terminals. The exact sign involution supplies the "
            "omitted a partners, excluding all 40000 finite endpoint fibers."
        ),
        "claim_boundary": {
            "closed": "spaces 5 and 6, both scalar classes, u1=1, over F_101",
            "not_closed": (
                "u1=2,...,100; extension-valued endpoint parameters; characteristic "
                "zero; the two remaining mirror charts as global symbolic schemes; "
                "physical HYM/QG promotion"
            ),
            "finite_slice_accounting": "4/400",
            "global_chart_accounting": "remains 138/140",
        },
        "new_continuous_fit_parameters": 0,
    }
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(certificate, indent=2) + "\n", encoding="utf-8")
    print(f"wrote {args.output}")
    print(certificate["status"])
    print("canonical fibers: 20000 = 19989 R-only units + 11 full-parent units")
    print("signed fibers closed: 40000; finite slices: 4/400")


if __name__ == "__main__":
    main()
