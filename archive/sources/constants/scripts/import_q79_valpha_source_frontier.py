"""Import q79 VAlpha source-frontier update."""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
TEXPAPERS = ROOT.parent
CERTS = ROOT / "certificates"
Q79 = TEXPAPERS / "mtt-q79-proof-repro"

LOCAL_CROSS_REPO = CERTS / "cross_repo_update_chain_and_next_gate_certificate.json"
Q79_FRONTIER = Q79 / "certificates" / "valpha_repo_update_source_frontier_certificate.json"

OUTPUT = CERTS / "q79_valpha_source_frontier_import_certificate.json"


def load(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def main() -> None:
    cross = load(LOCAL_CROSS_REPO)
    q79 = load(Q79_FRONTIER)
    reduction = q79["repo_update_source_frontier"]["frontier_reduction"]
    statuses = q79["repo_update_source_frontier"]["imported_certificate_statuses"]

    output = {
        "certificate": "Q79VAlphaSourceFrontierImport",
        "status": "Q79_VALPHA_SOURCE_FRONTIER_IMPORTED_FINITE_EMISSION_BRIDGE_NEXT",
        "inputs": {
            "local_cross_repo_update": str(LOCAL_CROSS_REPO.relative_to(ROOT)),
            "q79_frontier": str(Q79_FRONTIER),
        },
        "closed_now": {
            "q79_frontier_imported": q79["closed_by_this_attempt"]["next_frontier_reduced_to_source_origin_finite_emission_bridge"],
            "q79_yoneda_promoted_to_AH_conditional": reduction["q79_yoneda_promoted_to_AH_conditional"],
            "q79_central_neutral_lane_obstructed_reduced_model": reduction[
                "q79_central_neutral_lane_obstructed_reduced_model"
            ],
            "direct_pic0_shortcut_not_available": reduction["direct_pic0_shortcut_not_available"],
            "same_source_blocker_identified": reduction["same_source_blocker_identified"],
            "local_cross_repo_frontier_agrees": cross["next_closing_object"]["name"]
            == "Selected_Source_Certificate_or_BN_Basis_PhiFin_Payload_Fill_v1",
        },
        "imported_statuses": {
            "q79_ah_promotion": statuses["q79_ah_promotion"]["status"],
            "q79_central_neutral": statuses["q79_central_neutral"]["status"],
            "sm_orientation_de_dotd": statuses["sm_orientation_de_dotd"]["status"],
            "sm_routec_origin": statuses["sm_routec_origin"]["status"],
            "qa_logdet_bridge": statuses["qa_logdet_bridge"]["status"],
        },
        "updated_next_gate": {
            "name": "Q79_VAlpha_Source_Origin_and_Finite_Emission_Bridge_v1",
            "relation_to_local_frontier": (
                "This is the q79/VAlpha-facing refinement of the local "
                "Selected_Source_Certificate_or_BN_Basis_PhiFin_Payload_Fill_v1 gate."
            ),
            "must_prove": [
                "bind q79 Appell-Humbert/Yoneda VAlpha data to source origin, not merely conditional multiplication",
                "respect the central-neutral/Pic0 obstruction instead of quotienting it globally",
                "connect the source origin to finite emission morphism Phi_fin or selected BN basis payload",
                "then promote D_E/dotD/C1 only through selected-source replay",
            ],
        },
        "not_closed": {
            "selected_visible_valpha_source": True,
            "selected_Pic0_rule": True,
            "selected_D_E_dotD_Riesz_Green": True,
            "selected_HYM_or_RouteC_values": True,
            "primitive_C1_contractions": True,
            "full_SM_closure": True,
        },
        "guardrails": {
            "claims_q79_dirty_frontier_is_final_proof": False,
            "claims_selected_visible_valpha_source": False,
            "claims_selected_Pic0_rule": False,
            "claims_selected_D_E_dotD": False,
            "claims_full_SM_closure": False,
            "uses_observed_flavor_data": False,
            "uses_benchmark_flavor_entries": False,
        },
        "honest_answer": (
            "The q79 VAlpha update agrees with the SM-parity reduction: the "
            "next bridge is source origin to finite emission/Phi_fin, with "
            "Appell-Humbert/Yoneda available only conditionally and Pic0 still "
            "an obstruction. This sharpens the next gate but does not promote "
            "selected source flags."
        ),
    }

    if "--write-certificate" in __import__("sys").argv:
        OUTPUT.write_text(json.dumps(output, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    print(json.dumps(output, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
