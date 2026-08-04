"""Import the constants-repo Qa/SU3 visible-source architecture into q79.

The constants/no-knob repo now ranks the viable architectures for the selected
visible SM bundle/operator source.  This script records how that ranking maps
onto the q79 same-source monad/GS/operator fusion packet.
"""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
CANDIDATES = ROOT / "candidate_data"
CERTS = ROOT / "certificates"

CONSTANTS_REPO = Path(r"C:\Users\nero_\Downloads\TEXPAPERS\mtt-nonsm-constants-no-knob")
GR_REPO = Path(r"C:\Users\nero_\Downloads\TEXPAPERS\mtt-protospinor-gr-response-proof")

CONSTANTS_ARCH = (
    CONSTANTS_REPO
    / "certificates"
    / "selected_qa_su3_visible_source_architecture_certificate.json"
)
CONSTANTS_TEMPLATE = (
    CONSTANTS_REPO
    / "certificates"
    / "selected_qa_su3_visible_sm_bundle_operator_source.template.json"
)
GR_STRESS = (
    GR_REPO / "certificates" / "physical_normalization_stress_response_gate_certificate.json"
)
Q79_FUSION_ATTEMPT = CERTS / "same_source_monad_gs_operator_fusion_attempt_certificate.json"

OUT_CANDIDATE = CANDIDATES / "selected_qa_su3_visible_source_architecture_import.candidate.json"
OUT_CERT = CERTS / "selected_qa_su3_visible_source_architecture_import_certificate.json"
OUT_TEMPLATE = CERTS / "selected_qa_su3_same_source_valpha_s3_operator_packet.template.json"


def load(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def write(path: Path, data: dict[str, Any]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(data, indent=2, sort_keys=True) + "\n", encoding="utf-8")


def make_local_template(constants_template: dict[str, Any]) -> dict[str, Any]:
    must_bind = constants_template["must_bind_same_source"]
    return {
        "schema": "SelectedQaSU3SameSourceVAlphaS3OperatorPacket.v1",
        "status": "OPEN_SELECTED_QA_SU3_SAME_SOURCE_VALPHA_S3_OPERATOR_PACKET_REQUIRED",
        "purpose": (
            "Bind the rank-two V_alpha/terminal-monad source skeleton to the "
            "selected S3/Green-Schwarz visible support and emit validator-ready "
            "operator data for the q79/F branch."
        ),
        "source_skeleton": {
            "rank2_valpha_or_equivalent_visible_bundle_model": must_bind[
                "rank2_valpha_or_equivalent_visible_bundle_model"
            ],
            "terminal_monad_difference_L3_minus_K2_selector": must_bind[
                "terminal_monad_difference_L3_minus_K2_selector"
            ],
            "pic0_selection_or_physical_quotient": must_bind[
                "pic0_selection_or_physical_quotient"
            ],
        },
        "same_source_merge": {
            "selected_s3_green_schwarz_visible_support": must_bind[
                "selected_s3_green_schwarz_visible_support"
            ],
            "chern_weil_visible_row_derivation": must_bind[
                "chern_weil_visible_row_derivation"
            ],
            "coherent_projector_retention": must_bind["coherent_projector_retention"],
        },
        "operator_execution": {
            "typed_transition_or_rhoE_data": must_bind["typed_transition_or_rhoE_data"],
            "hym_strominger_or_routec_residual_solve": must_bind[
                "hym_strominger_or_routec_residual_solve"
            ],
            "sector_D_E_Riesz_Green_dotD_packets": must_bind[
                "sector_D_E_Riesz_Green_dotD_packets"
            ],
            "primitive_C1_or_Yukawa_overlap_contractions": must_bind[
                "primitive_C1_or_Yukawa_overlap_contractions"
            ],
        },
        "forbidden_shortcuts": constants_template["forbidden_shortcuts"],
    }


def build_report() -> dict[str, Any]:
    arch = load(CONSTANTS_ARCH)
    constants_template = load(CONSTANTS_TEMPLATE)
    fusion = load(Q79_FUSION_ATTEMPT)
    gr = load(GR_STRESS)

    local_template = make_local_template(constants_template)
    write(OUT_TEMPLATE, local_template)

    report = {
        "calculation": "SelectedQaSU3VisibleSourceArchitectureImport",
        "status": "SELECTED_QA_SU3_VISIBLE_ARCHITECTURE_IMPORTED_SAME_SOURCE_PACKET_OPEN",
        "inputs": {
            "constants_architecture": str(CONSTANTS_ARCH),
            "constants_visible_source_template": str(CONSTANTS_TEMPLATE),
            "q79_same_source_fusion_attempt": str(Q79_FUSION_ATTEMPT.relative_to(ROOT)),
            "gr_stress_response_gate": str(GR_STRESS),
        },
        "imported_statuses": {
            "constants_architecture": arch["status"],
            "q79_same_source_fusion_attempt": fusion["status"],
            "gr_stress_response_gate": gr["status"],
        },
        "recommended_construction": arch["recommended_construction"],
        "next_object": {
            "constants_name": arch["next_object"]["name"],
            "local_template": str(OUT_TEMPLATE.relative_to(ROOT)),
            "minimal_payload": arch["next_object"]["must_prove"],
        },
        "mapping_to_q79_fusion_packet": {
            "A_rank2_valpha_terminal_monad_primary": [
                "ordered_source.selected_L",
                "ordered_source.selected_L2",
                "ordered_source.source_lane_selector",
                "ordered_source.pic0_resolution",
            ],
            "B_s3_green_schwarz_visible_support": [
                "green_schwarz_and_gerbe.visible_green_schwarz_row_derived_from_same_source",
                "green_schwarz_and_gerbe.projector_retention_verified",
                "operator_response.primitive_C1_contractions",
            ],
            "C_direct_hym_routec_solve": [
                "operator_response.route_c_residuals_pass",
                "operator_response.de_action_pass",
                "operator_response.riesz_gap_pass",
                "operator_response.reduced_green_pass",
                "operator_response.dotd_response_pass",
                "operator_response.selected_dotD_source_verified",
            ],
        },
        "closed_now": {
            "constants_repo_ranked_best_architecture": arch["closed_now"][
                "ranked_architectures_built"
            ],
            "q79_fusion_validator_already_executable": fusion["what_this_closes"][
                "fusion_packet_validator_created"
            ],
            "local_same_source_valpha_s3_template_written": True,
            "gr_structural_stress_response_separated_from_sm_source": gr["stress_response"][
                "universal_variational_definition_closed"
            ]
            and not gr["physical_normalization"][
                "physical_absolute_dimensionful_anchor_closed"
            ],
            "no_target_fitting_used": arch["closed_now"]["no_target_fitting_used"],
        },
        "not_closed": {
            "same_source_valpha_s3_binding": arch["not_closed"][
                "same_source_binding_between_A_and_B"
            ],
            "selected_visible_sm_bundle_or_sheaf_model": arch["not_closed"][
                "selected_visible_sm_bundle_or_sheaf_model"
            ],
            "selected_L3_minus_K2_source": arch["not_closed"]["selected_L3_minus_K2_source"],
            "Pic0_selection_or_quotient": arch["not_closed"]["Pic0_selection_or_quotient"],
            "typed_transition_or_rhoE_data": arch["not_closed"][
                "typed_transition_or_rhoE_data"
            ],
            "selected_D_E_dotD_Riesz_Green": arch["not_closed"][
                "selected_D_E_dotD_Riesz_Green"
            ],
            "primitive_C1_or_Yukawa_contractions": arch["not_closed"][
                "primitive_C1_or_Yukawa_contractions"
            ],
            "same_source_fusion_packet": fusion["what_this_does_not_close"][
                "same_source_fusion_packet"
            ]
            is False,
            "full_SM_closure": True,
        },
        "guardrails": {
            "claims_same_source_binding_proved": False,
            "claims_selected_visible_bundle_constructed": False,
            "claims_selected_D_E_constructed": False,
            "claims_physical_GR_normalization_imported": False,
            "claims_full_SM_closure": False,
            "uses_observed_masses_or_mixings": False,
            "uses_observed_Newton_or_Planck_input": False,
        },
        "verdict": {
            "what_changed": (
                "The next q79 object is now sharpened from a generic selected "
                "operator source to a same-source V_alpha/S3 packet with Route C "
                "as execution engine."
            ),
            "hard_next_step": (
                "Prove or compute the same-source binding between terminal-monad "
                "V_alpha/L3-K2 data and selected S3/Green-Schwarz visible support."
            ),
        },
    }
    return report


def main() -> int:
    report = build_report()
    write(OUT_CANDIDATE, report)
    cert = {
        "certificate": "SelectedQaSU3VisibleSourceArchitectureImport",
        "status": report["status"],
        "analysis_script": "scripts/import_selected_qa_su3_visible_source_architecture.py",
        "candidate_data": str(OUT_CANDIDATE.relative_to(ROOT)),
        "local_template": report["next_object"]["local_template"],
        "imported_statuses": report["imported_statuses"],
        "recommended_construction": report["recommended_construction"],
        "mapping_to_q79_fusion_packet": report["mapping_to_q79_fusion_packet"],
        "closed_now": report["closed_now"],
        "not_closed": report["not_closed"],
        "guardrails": report["guardrails"],
        "verdict": report["verdict"],
    }
    write(OUT_CERT, cert)
    print(json.dumps(report, indent=2, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
