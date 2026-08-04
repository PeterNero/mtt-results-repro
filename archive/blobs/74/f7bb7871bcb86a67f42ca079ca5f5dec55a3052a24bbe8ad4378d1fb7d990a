"""Gate the selected Qa/SU3 Route C source solve against current q79 evidence."""

from __future__ import annotations

import json
import sys
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
CERTS = ROOT / "certificates"
Q79_REPO = Path(r"C:\Users\nero_\Downloads\TEXPAPERS\mtt-q79-proof-repro")
Q79_CERTS = Q79_REPO / "certificates"

SPECTRAL_REDUCTION = CERTS / "selected_qa_su3_spectral_fallback_reduction_certificate.json"
SELECTED_DE = Q79_CERTS / "iwasawa_selected_de_construction_attempt_certificate.json"
PROMOTION_GATE = Q79_CERTS / "iwasawa_selected_source_promotion_gate_certificate.json"
HYM_ATTEMPT = Q79_CERTS / "selected_hym_operator_source_attempt_certificate.json"
HYM_VALIDATOR = Q79_CERTS / "selected_hym_operator_source_validator_certificate.json"
VISIBLE_BLOCKER = Q79_CERTS / "visible_operator_source_blocker_resolution_certificate.json"
VISIBLE_AFTER_S3 = Q79_CERTS / "visible_operator_source_after_s3_closure_certificate.json"
TYPED_MONAD = Q79_CERTS / "iwasawa_typed_monad_section_recovery_certificate.json"
TWISTED_PACKET = Q79_CERTS / "iwasawa_twisted_source_packet_fill_attempt_certificate.json"

OUTPUT_TEMPLATE = CERTS / "selected_qa_su3_routec_source_solve.template.json"
OUTPUT_CERT = CERTS / "selected_qa_su3_routec_source_solve_gate_certificate.json"


def load(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def make_template() -> dict[str, Any]:
    return {
        "schema": "SelectedQaSU3RouteCSourceSolve.v1",
        "status": "OPEN_SELECTED_QA_SU3_ROUTEC_SOURCE_SOLVE_REQUIRED",
        "purpose": (
            "Supply the first genuinely new selected visible SM bundle/operator "
            "source on the q79/F branch, then emit validator-ready rho_E, D_E, "
            "Riesz/Green, dotD, and primitive-overlap data."
        ),
        "must_supply": {
            "selected_visible_sm_bundle_or_sheaf_model": None,
            "mtt_selection_certificate_for_q79_F_m1_branch": None,
            "chern_weil_visible_row_from_same_source": None,
            "finite_rhoE_transition_data_not_pure_gauge_smoke": None,
            "route_c_residual_packet_with_selected_source_verified": None,
            "sector_D_E_action_matrices": None,
            "riesz_projector_gap_and_reduced_green": None,
            "same_branch_dotD_alpha1_and_horizontal_responses": None,
            "coherent_projector_retention": None,
            "primitive_C1_or_Yukawa_overlap_contractions": None,
        },
        "accepted_source_routes": [
            "typed Cech/monad transition data",
            "finite HYM/Strominger solve",
            "corrected selected non-invariant Dolbeault operator with residual bounds",
        ],
        "forbidden_shortcuts": [
            "Do not promote route-c smoke residuals.",
            "Do not treat abstract Li-Yau/HYM existence as a matrix source.",
            "Do not treat typed monad labels as typed sections.",
            "Do not use observed masses, mixings, or benchmark flavor entries.",
        ],
    }


def main() -> None:
    spectral = load(SPECTRAL_REDUCTION)
    selected_de = load(SELECTED_DE)
    promotion = load(PROMOTION_GATE)
    hym_attempt = load(HYM_ATTEMPT)
    hym_validator = load(HYM_VALIDATOR)
    visible_blocker = load(VISIBLE_BLOCKER)
    visible_after_s3 = load(VISIBLE_AFTER_S3)
    typed_monad = load(TYPED_MONAD)
    twisted_packet = load(TWISTED_PACKET)

    route_evaluation = selected_de["route_evaluation"]
    all_current_routes_blocked = (
        route_evaluation["R1_corrected_non_invariant_Dolbeault_operator"]["status"] == "BLOCKED"
        and route_evaluation["R2_typed_monad_sections"]["status"] == "BLOCKED"
        and route_evaluation["R3_direct_selected_HYM_solve"]["status"] == "ABSTRACT_EXISTENCE_ONLY"
        and visible_blocker["calculation_results"]["all_current_routes_blocked"] is True
    )
    promotion_contract_ready = (
        promotion["verdict"]["promotion_gate_ready"] is True
        and "typed_Cech_monad_transition_data" in promotion["source_kinds_allowed"]
        and "finite_HYM_Strominger_solve" in promotion["source_kinds_allowed"]
    )
    no_existing_operator_source = (
        hym_attempt["calculation_results"]["selected_hym_operator_source_verified"] is False
        and hym_validator["verdict"]["selected_hym_operator_source_verified"] is False
        and visible_after_s3["calculation_results"]["operator_source_cut_set_still_open"] is True
        and visible_blocker["what_is_solved_once_and_for_all"][
            "current_corpus_has_no_closing_selected_operator_source"
        ]
        is True
    )
    typed_route_absent = (
        typed_monad["route_decision"]["typed_monad_cech_can_close_now"] is False
        and typed_monad["not_recovered_from_corpus"]["explicit_f_i_section_representatives"] is True
        and typed_monad["not_recovered_from_corpus"]["explicit_g_i_section_representatives"] is True
        and typed_monad["not_recovered_from_corpus"]["transition_functions_for_L_i_K1_K2"] is True
    )
    twisted_route_partial_only = (
        twisted_packet["verdict"]["promotion_packet_passes"] is False
        and twisted_packet["unfilled_fields"]["selected_visible_operator_source_packet"] is True
        and twisted_packet["unfilled_fields"]["selected_twisted_D_E_dotD"] is True
    )

    output = {
        "certificate": "SelectedQaSU3RouteCSourceSolveGate",
        "status": "QA_SU3_ROUTEC_SOURCE_SOLVE_GATE_CURRENT_SOURCE_EXHAUSTED_NEW_SOURCE_REQUIRED",
        "inputs": {
            "spectral_fallback_reduction": str(SPECTRAL_REDUCTION.relative_to(ROOT)),
            "q79_selected_de_construction_attempt": str(SELECTED_DE),
            "q79_selected_source_promotion_gate": str(PROMOTION_GATE),
            "q79_selected_hym_operator_attempt": str(HYM_ATTEMPT),
            "q79_selected_hym_operator_validator": str(HYM_VALIDATOR),
            "q79_visible_operator_source_blocker": str(VISIBLE_BLOCKER),
            "q79_visible_operator_after_s3": str(VISIBLE_AFTER_S3),
            "q79_typed_monad_recovery": str(TYPED_MONAD),
            "q79_twisted_source_packet_fill_attempt": str(TWISTED_PACKET),
        },
        "template_written": str(OUTPUT_TEMPLATE.relative_to(ROOT)),
        "closed_now": {
            "current_route_exhaustion_proved": all_current_routes_blocked,
            "promotion_contract_ready": promotion_contract_ready,
            "no_existing_selected_hym_operator_source": no_existing_operator_source,
            "typed_monad_route_absent_from_current_corpus": typed_route_absent,
            "twisted_or_s3_route_partial_but_not_operator_source": twisted_route_partial_only,
            "finite_validator_pipeline_ready_from_previous_gate": spectral["closed_now"][
                "current_q79_branch_finite_pipeline_conditionally_validates"
            ],
            "first_new_object_identified": visible_blocker["what_is_solved_once_and_for_all"][
                "first_required_new_object_identified"
            ]
            == "selected visible SM bundle/operator source",
        },
        "not_closed": {
            "selected_visible_sm_bundle_or_sheaf_model": True,
            "selected_D_E_source": True,
            "route_c_residual_solve": True,
            "selected_dotD_alpha1_source": True,
            "riesz_green_projector_retention": True,
            "primitive_C1_or_Yukawa_contractions": True,
            "full_SM_closure": True,
        },
        "route_status": {
            "R1_corrected_non_invariant_Dolbeault_operator": route_evaluation[
                "R1_corrected_non_invariant_Dolbeault_operator"
            ]["status"],
            "R2_typed_monad_sections": route_evaluation["R2_typed_monad_sections"]["status"],
            "R3_direct_selected_HYM_solve": route_evaluation["R3_direct_selected_HYM_solve"][
                "status"
            ],
            "twisted_S3_packet": "PARTIAL_PROMOTION_OPEN",
        },
        "minimal_new_data_that_would_close": visible_blocker[
            "minimal_new_data_that_would_close"
        ],
        "next_object": {
            "name": "Selected_Qa_SU3_Visible_SM_Bundle_Operator_Source_v1",
            "exact_role": (
                "First new source object; once supplied it should feed the "
                "existing q79 promotion gate and finite D_E/Riesz/Green/dotD validators."
            ),
            "then_run": [
                "validate_iwasawa_route_c_residuals.py",
                "validate_iwasawa_de_action.py",
                "validate_iwasawa_riesz_gap.py",
                "validate_iwasawa_reduced_green.py",
                "validate_iwasawa_dotd_response.py",
                "validate_selected_hym_operator_source.py",
            ],
        },
        "guardrails": {
            "claims_selected_visible_operator_source_constructed": False,
            "claims_selected_D_E_constructed": False,
            "claims_route_c_residual_solve": False,
            "promotes_route_c_smoke": False,
            "promotes_abstract_hym_existence_to_matrix": False,
            "uses_observed_masses_or_mixings": False,
            "claims_full_SM_closure": False,
        },
    }

    cert_text = json.dumps(output, indent=2, sort_keys=True)
    template_text = json.dumps(make_template(), indent=2, sort_keys=True)
    if "--write-certificate" in sys.argv:
        OUTPUT_CERT.write_text(cert_text + "\n", encoding="utf-8")
        OUTPUT_TEMPLATE.write_text(template_text + "\n", encoding="utf-8")
    print(cert_text)


if __name__ == "__main__":
    main()
