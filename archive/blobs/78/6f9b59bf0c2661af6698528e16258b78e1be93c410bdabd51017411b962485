"""Audit selected Route-C hybrid matter-slot Galerkin source packet attempt."""

from __future__ import annotations

import json
import sys
from pathlib import Path


REPO = Path(__file__).resolve().parents[1]
DATA = REPO / "candidate_data" / "selected_routec_hybrid_matter_slot_galerkin_source_packet.candidate.json"
CERT = REPO / "certificates" / "selected_routec_hybrid_matter_slot_galerkin_source_packet_certificate.json"
NOTE = REPO / "proof_corpus" / "MTT_Selected_RouteC_Hybrid_MatterSlot_Galerkin_Source_Packet_v1.md"

STATUS = "MTT_SELECTED_ROUTEC_HYBRID_MATTERSLOT_GALERKIN_PACKET_ATTEMPT_BUILT_SELECTED_SOURCE_AND_OVERLAP_OPEN"
NEXT = "MTT_Selected_RouteC_Selected_OperatorSource_and_OverlapTensor_Packet_v1"


def check(name: str, condition: bool, detail: object) -> bool:
    print(("PASS" if condition else "FAIL") + f": {name} -- {detail}")
    return condition


def main() -> int:
    data = json.loads(DATA.read_text(encoding="utf-8"))
    cert = json.loads(CERT.read_text(encoding="utf-8"))
    note = NOTE.read_text(encoding="utf-8")
    goal = data["packet_goal"]
    honest = data["attempts"]["honest_routec_galerkin_fill"]
    fixture = data["attempts"]["conditional_su5_fixture_fill"]
    c1 = data["c1_overlap_boundary"]
    verdict = data["selection_verdict"]

    checks = [
        check("status", data["status"] == STATUS, data["status"]),
        check("certificate agreement", cert["status"] == data["status"], cert["status"]),
        check("packet not closed", goal["closed_now"] is False and verdict["hybrid_packet_selected"] is False, verdict),
        check(
            "honest shape present",
            honest["fields_present"]["three_dimensional_model_zero_cluster"] is True
            and honest["fields_present"]["positive_model_gap"] is True
            and honest["fields_present"]["Riesz_and_reduced_Green_model_emitted"] is True
            and honest["fields_present"]["sector_projectors_emitted"] is True
            and honest["fields_present"]["dotD_alpha1_matrix_emitted"] is True,
            honest["fields_present"],
        ),
        check(
            "honest source flags false",
            honest["source_flags"]["selected_dotD_source_verified"] is False
            and honest["source_flags"]["alpha1_driver_verified"] is False
            and honest["source_flags"]["matter_slot_source_verified"] is False,
            honest["source_flags"],
        ),
        check(
            "current transport identity no-go",
            honest["basis_transport"]["all_checked_family_bases_identical"] is True
            and honest["basis_transport"]["current_relative_transport"] == "I_3"
            and honest["basis_transport"]["current_payload_reaches_desired_transport"] is False,
            honest["basis_transport"],
        ),
        check(
            "fixture not promoted",
            fixture["has_10M_clock"] is True
            and fixture["has_bar5M_shift"] is True
            and fixture["selected_by_mtt"] is False
            and fixture["fixture_only"] is True
            and fixture["has_1M_singlet_neutrino_rule"] is False,
            fixture,
        ),
        check(
            "C1 overlap boundary retained",
            c1["route_c_smoke_dotD_alone_closes_ckm_heavy_link"] is False
            and c1["universal_tensor_case_gives_Delta_t_zero"] is True
            and c1["heavy_link_overlap_unknowns_per_sector"] == 5
            and "sector-resolved trilinear overlap tensors T_s" in c1["new_required_selected_data"],
            c1,
        ),
        check(
            "no closure or fitting",
            data["closure_claimed"] is False and data["target_fitting_used"] is False,
            {"closure_claimed": data["closure_claimed"], "target_fitting_used": data["target_fitting_used"]},
        ),
        check("next artifact", data["next_required_artifact"] == NEXT, data["next_required_artifact"]),
        check(
            "note records attempt",
            "Honest Route-C/Galerkin Fill" in note
            and "Conditional SU(5) Fixture Fill" in note
            and "C1 Boundary" in note
            and f"Next artifact: `{NEXT}`" in note,
            NOTE,
        ),
    ]
    print("\nMTT selected Route-C hybrid matter-slot Galerkin packet audit")
    return 0 if all(checks) else 1


if __name__ == "__main__":
    sys.exit(main())
