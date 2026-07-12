"""Build the first source-augmentation packet for the Iwasawa monad maps."""

from __future__ import annotations

import json
import sys
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
CERTS = ROOT / "certificates"
DATA = ROOT / "candidate_data"
OUTPUT_CERT = CERTS / "source_augmentation_packet_certificate.json"
OUTPUT_DATA = DATA / "source_augmentation_packet.candidate.json"


REQUIRED_SPACES = [
    ("F1", "f_1", [-3, 0, 1]),
    ("F2", "f_2", [-2, 1, -1]),
    ("F3", "f_3", [0, -1, 0]),
    ("F4", "f_4", [0, 0, -1]),
    ("F5", "f_5", [1, 1, 1]),
    ("G1", "g_1", [2, 1, -1]),
    ("G2", "g_2", [1, 0, 1]),
    ("G3", "g_3", [-1, 2, 0]),
    ("G4", "g_4", [-1, 1, 1]),
    ("G5", "g_5", [-2, 0, -1]),
    ("P", "product_target", [-1, 1, 0]),
]


def add(u: list[int], v: list[int]) -> list[int]:
    return [a + b for a, b in zip(u, v)]


def main() -> None:
    spaces = [{"id": sid, "role": role, "charge": charge} for sid, role, charge in REQUIRED_SPACES]
    charge_by_id = {sid: charge for sid, _, charge in REQUIRED_SPACES}
    product_tests = []
    for i in range(1, 6):
        fid = f"F{i}"
        gid = f"G{i}"
        product_tests.append(
            {
                "pair": [fid, gid],
                "charge_sum": add(charge_by_id[fid], charge_by_id[gid]),
                "target_charge": charge_by_id["P"],
                "lands_in_P": add(charge_by_id[fid], charge_by_id[gid]) == charge_by_id["P"],
                "multiplication_constant": None,
            }
        )
    standard_iwasawa_actions = [
        {
            "generator": "g1",
            "action": "(z1,z2,z3) -> (z1+1,z2,z3)",
            "status": "SCHEMA_ONLY_NEEDS_LATTICE_CONVENTION",
        },
        {
            "generator": "g2",
            "action": "(z1,z2,z3) -> (z1+i,z2,z3)",
            "status": "SCHEMA_ONLY_NEEDS_LATTICE_CONVENTION",
        },
        {
            "generator": "g3",
            "action": "(z1,z2,z3) -> (z1,z2+1,z3+z1)",
            "status": "SCHEMA_ONLY_NEEDS_LEFT_RIGHT_CHECK",
        },
        {
            "generator": "g4",
            "action": "(z1,z2,z3) -> (z1,z2+i,z3+i*z1)",
            "status": "SCHEMA_ONLY_NEEDS_LEFT_RIGHT_CHECK",
        },
        {
            "generator": "g5",
            "action": "(z1,z2,z3) -> (z1,z2,z3+1)",
            "status": "SCHEMA_ONLY_NEEDS_LATTICE_CONVENTION",
        },
        {
            "generator": "g6",
            "action": "(z1,z2,z3) -> (z1,z2,z3+i)",
            "status": "SCHEMA_ONLY_NEEDS_LATTICE_CONVENTION",
        },
    ]
    obstruction_tests = {
        "all_pair_charges_land_in_P": all(t["lands_in_P"] for t in product_tests),
        "flat_character_can_realize_nonzero_c1": False,
        "literal_constant_sections_have_correct_charge": False,
        "automorphy_data_supplied_now": False,
        "section_basis_supplied_now": False,
        "gf_zero_computable_now": False,
    }
    candidate = {
        "candidate": "SelectedQaSU3SourceAugmentationPacket",
        "status": "SOURCE_AUGMENTATION_PACKET_BUILT_SYMBOLIC_CHARGE_PRODUCTS_PASS_VALUES_OPEN",
        "ambient_group_law": "(z1,z2,z3)*(w1,w2,w3)=(z1+w1,z2+w2,z3+w3+z1*w2)",
        "coordinate_action_schema": standard_iwasawa_actions,
        "required_section_spaces": spaces,
        "product_tests": product_tests,
        "missing_values": [
            "left/right quotient convention",
            "actual Gamma lattice generator action in selected source convention",
            "charge-to-factor map q -> a_q(gamma,z)",
            "cocycle proof and c1(q) proof",
            "basis for each section space",
            "multiplication constants in P",
            "exact coefficients for f,g with g f = 0",
            "local-freeness/stability certificate for exact maps",
            "operator exit through Cech/Dolbeault, rho_E, or D_E",
        ],
        "obstruction_tests": obstruction_tests,
        "target_fitting_used": False,
    }
    certificate = {
        "certificate": "SelectedQaSU3SourceAugmentationPacket",
        "status": "QA_SU3_SOURCE_AUGMENTATION_PACKET_SYMBOLIC_PRODUCTS_PASS_VALUES_OPEN",
        "candidate_path": str(OUTPUT_DATA.relative_to(ROOT)),
        "what_closes": {
            "required_charge_list": True,
            "pairwise_Fi_Gi_to_P_charge_matching": obstruction_tests["all_pair_charges_land_in_P"],
            "standard_iwasawa_group_action_schema": True,
        },
        "what_remains_open": {
            "selected_automorphy_factors": True,
            "section_bases": True,
            "multiplication_constants": True,
            "exact_f_g_maps": True,
            "operator_exit": True,
            "qa_su3_packet_closed": False,
        },
        "route_update": {
            "primary_route_still_live": True,
            "reason": "All five symbolic products have the correct target charge P, so the monad map obstruction is not charge mismatch but missing section-ring values.",
            "next_required_artifact": "Selected_Qa_SU3_Automorphy_Factor_Ansatz_Constraint_Solver_v1",
        },
        "forbidden_shortcuts": [
            "do not fill multiplication constants by convenience",
            "do not use target residual",
            "do not treat group-action schema as selected factors of automorphy",
        ],
        "closure_claimed": False,
        "target_fitting_used": False,
    }
    text_data = json.dumps(candidate, indent=2, sort_keys=True)
    text_cert = json.dumps(certificate, indent=2, sort_keys=True)
    if "--write" in sys.argv:
        OUTPUT_DATA.write_text(text_data + "\n", encoding="utf-8")
        OUTPUT_CERT.write_text(text_cert + "\n", encoding="utf-8")
    print(text_cert)


if __name__ == "__main__":
    main()
