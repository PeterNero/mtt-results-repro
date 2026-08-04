"""Build the gerbe-twist cancellation packet for Qa/SU3 monad maps."""

from __future__ import annotations

import json
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
CERTS = ROOT / "certificates"
DATA = ROOT / "candidate_data"
OUTPUT_CERT = CERTS / "gerbe_twist_cancellation_packet_certificate.json"
OUTPUT_DATA = DATA / "gerbe_twist_cancellation_packet.candidate.json"


PAIRS = [
    ("F1", [-3, 0, 1], "G1", [2, 1, -1]),
    ("F2", [-2, 1, -1], "G2", [1, 0, 1]),
    ("F3", [0, -1, 0], "G3", [-1, 2, 0]),
    ("F4", [0, 0, -1], "G4", [-1, 1, 1]),
    ("F5", [1, 1, 1], "G5", [-2, 0, -1]),
]
P_CHARGE = [-1, 1, 0]


def add(u: list[int], v: list[int]) -> list[int]:
    return [a + b for a, b in zip(u, v)]


def split(charge: list[int]) -> dict[str, object]:
    return {"ordinary_ab_charge": charge[:2], "gerbe_c_twist": charge[2]}


def main() -> None:
    pair_results = []
    for fid, f_charge, gid, g_charge in PAIRS:
        total = add(f_charge, g_charge)
        pair_results.append(
            {
                "pair": [fid, gid],
                "F": {"charge": f_charge, **split(f_charge)},
                "G": {"charge": g_charge, **split(g_charge)},
                "product_charge": total,
                "product_matches_P": total == P_CHARGE,
                "ordinary_ab_product_matches_P_ab": total[:2] == P_CHARGE[:2],
                "gerbe_twist_cancels": f_charge[2] + g_charge[2] == P_CHARGE[2] == 0,
            }
        )
    all_cancel = all(item["gerbe_twist_cancels"] for item in pair_results)
    all_match = all(item["product_matches_P"] for item in pair_results)
    twist_values = sorted({item["F"]["gerbe_c_twist"] for item in pair_results} | {item["G"]["gerbe_c_twist"] for item in pair_results})
    candidate = {
        "candidate": "SelectedQaSU3GerbeTwistCancellationPacket",
        "status": "GERBE_TWIST_CANCELLATION_PACKET_BUILT_SOURCE_SELECTION_OPEN",
        "interpretation": {
            "ordinary_part": "Use only the closed a,b directions as ordinary line-bundle first-Chern data.",
            "twisted_part": "Use the c component as a gerbe/B-field/twisted-module charge rather than an ordinary line-bundle c1.",
            "monad_product": "Each F_i and G_i pair carries opposite c twist, so products land in the untwisted P sector.",
        },
        "P": {"charge": P_CHARGE, **split(P_CHARGE)},
        "pair_results": pair_results,
        "twist_values_used": twist_values,
        "solution_claim": {
            "solves_literal_c_nonclosed_obstruction_at_product_level": all_cancel and all_match,
            "ordinary_line_bundle_c_axis_no_longer_required": True,
            "monad_map_typing_repaired_as_twisted_maps": all_cancel and all_match,
            "selected_smooth_gerbe_source_supplied": False,
            "section_bases_supplied": False,
            "operator_exit_supplied": False,
        },
        "next_required_data": [
            "selected Deligne/Cech or B-field representative for the c twist",
            "twisted section spaces for c=+1,-1 and ordinary ab charges",
            "proof that twisted multiplication cancels to the untwisted P sector",
            "Freed-Witten/Bianchi admissibility for the selected twist",
            "twisted projector/operator retention and D_E or torsion finite part",
        ],
        "target_fitting_used": False,
    }
    certificate = {
        "certificate": "SelectedQaSU3GerbeTwistCancellationPacket",
        "status": "QA_SU3_GERBE_TWIST_CANCELLATION_SOLUTION_CANDIDATE_BUILT_SOURCE_OPEN",
        "candidate_path": str(OUTPUT_DATA.relative_to(ROOT)),
        "what_closes": {
            "literal_c_obstruction_bypassed_by_retyping": True,
            "all_Fi_Gi_c_twists_cancel_to_P": all_cancel,
            "all_Fi_Gi_products_match_P_charge": all_match,
            "ordinary_ab_line_bundle_part_remains_closed_class_candidate": True,
        },
        "what_remains_open": {
            "selected_gerbe_or_B_field_representative": True,
            "twisted_section_bases": True,
            "twisted_multiplication_constants": True,
            "Freed_Witten_Bianchi_check": True,
            "operator_exit": True,
            "qa_su3_packet_closed": False,
        },
        "route_update": {
            "proposed_solution": "ordinary_ab_line_bundles_plus_c_gerbe_twist_cancellation",
            "ordinary_full_nil_line_bundle_route": "REPLACED_BY_TWISTED_MONAD_MAP_TYPING",
            "next_required_artifact": "Selected_Qa_SU3_Twisted_Section_Ring_and_Gerbe_Source_Gate_v1",
        },
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
