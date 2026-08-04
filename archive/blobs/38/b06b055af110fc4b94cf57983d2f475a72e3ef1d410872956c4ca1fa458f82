"""Rank candidate architectures for the selected Qa/SU3 visible operator source."""

from __future__ import annotations

import json
import sys
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
CERTS = ROOT / "certificates"
Q79_REPO = Path(r"C:\Users\nero_\Downloads\TEXPAPERS\mtt-q79-proof-repro")
Q79_CERTS = Q79_REPO / "certificates"

ROUTEC_GATE = CERTS / "selected_qa_su3_routec_source_solve_gate_certificate.json"
VISIBLE_PACKET = CERTS / "selected_qa_su3_visible_operator_source_packet_attempt_certificate.json"
VALPHA = CERTS / "selected_qa_su3_visible_rank2_valpha_source_attempt_certificate.json"
MONAD_DIFF = CERTS / "selected_qa_su3_monad_difference_l2_source_attempt_certificate.json"
TERMINAL_LANE = CERTS / "selected_qa_su3_terminal_monad_lane_selector_attempt_certificate.json"
SPECTRAL_REDUCTION = CERTS / "selected_qa_su3_spectral_fallback_reduction_certificate.json"

VISIBLE_AFTER_S3 = Q79_CERTS / "visible_operator_source_after_s3_closure_certificate.json"
TWISTED_PACKET = Q79_CERTS / "iwasawa_twisted_source_packet_fill_attempt_certificate.json"
SELECTED_DE = Q79_CERTS / "iwasawa_selected_de_construction_attempt_certificate.json"
HYM_ATTEMPT = Q79_CERTS / "selected_hym_operator_source_attempt_certificate.json"

OUTPUT_TEMPLATE = CERTS / "selected_qa_su3_visible_sm_bundle_operator_source.template.json"
OUTPUT_CERT = CERTS / "selected_qa_su3_visible_source_architecture_certificate.json"


def load(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def make_template() -> dict[str, Any]:
    return {
        "schema": "SelectedQaSU3VisibleSMBundleOperatorSource.v1",
        "status": "OPEN_SELECTED_QA_SU3_VISIBLE_SM_BUNDLE_OPERATOR_SOURCE_REQUIRED",
        "purpose": (
            "Supply a single same-source visible bundle/sheaf/operator packet on "
            "the q79/F branch, combining topological Chern source, S3/GS visible "
            "support, selected branch/Pic0 data, and validator-ready D_E/dotD."
        ),
        "must_bind_same_source": {
            "rank2_valpha_or_equivalent_visible_bundle_model": None,
            "terminal_monad_difference_L3_minus_K2_selector": None,
            "selected_s3_green_schwarz_visible_support": None,
            "chern_weil_visible_row_derivation": None,
            "pic0_selection_or_physical_quotient": None,
            "typed_transition_or_rhoE_data": None,
            "hym_strominger_or_routec_residual_solve": None,
            "sector_D_E_Riesz_Green_dotD_packets": None,
            "coherent_projector_retention": None,
            "primitive_C1_or_Yukawa_overlap_contractions": None,
        },
        "forbidden_shortcuts": [
            "Do not splice topological V_alpha data and S3/GS support unless they are proven same-source.",
            "Do not promote visible Green-Schwarz row insertion to a Chern-Weil derivation.",
            "Do not treat route-c smoke data as selected D_E/dotD.",
            "Do not use observed flavor data.",
        ],
    }


def main() -> None:
    routec = load(ROUTEC_GATE)
    visible_packet = load(VISIBLE_PACKET)
    valpha = load(VALPHA)
    monad = load(MONAD_DIFF)
    terminal = load(TERMINAL_LANE)
    spectral = load(SPECTRAL_REDUCTION)
    after_s3 = load(VISIBLE_AFTER_S3)
    twisted = load(TWISTED_PACKET)
    selected_de = load(SELECTED_DE)
    hym = load(HYM_ATTEMPT)

    architectures = {
        "A_rank2_valpha_terminal_monad_primary": {
            "description": (
                "Use V_alpha from L3-K2 as the visible bundle skeleton, then "
                "bind it to Appell-Humbert/Cech/rhoE data and selected D_E."
            ),
            "closed_support": {
                "rank2_topological_c1_c2": valpha["closed_now"]["topological_rank2_target_c1_c2"],
                "conditional_ext_math": valpha["closed_now"]["conditional_h1_equals_8_and_nonzero_ext"],
                "monad_difference_sufficiency": monad["closed_now"]["sufficiency_of_selected_monad_difference"],
                "terminal_lane_conditional_uniqueness": terminal["closed_now"][
                    "conditional_uniqueness_inside_terminal_lane"
                ],
            },
            "open_blockers": {
                "actual_MTT_selection_of_L3_minus_K2": monad["not_closed"][
                    "actual_MTT_selection_of_L3_minus_K2"
                ],
                "pic0_selection_or_quotient": monad["not_closed"]["Pic0_selection_or_quotient"],
                "typed_transition_or_rhoE_data": monad["not_closed"]["typed_monad_sections_for_source"],
                "same_source_D_E_dotD_Riesz_Green": valpha["not_closed"][
                    "same_source_D_E_dotD_Riesz_Green"
                ],
            },
        },
        "B_s3_green_schwarz_visible_support": {
            "description": (
                "Use selected S3/Green-Schwarz support to constrain the visible "
                "source and projector support, then attach a bundle/operator source."
            ),
            "closed_support": {
                "selected_s3_support": after_s3["calculation_results"]["selected_s3_support_now_closed"],
                "visible_gs_curvature_row": after_s3["calculation_results"][
                    "visible_gs_curvature_now_closed"
                ],
                "block_factorized_sector_maps": twisted["verdict"][
                    "finite_block_factorized_sector_maps_validated"
                ],
            },
            "open_blockers": {
                "selected_visible_operator_source_packet": twisted["unfilled_fields"][
                    "selected_visible_operator_source_packet"
                ],
                "selected_twisted_D_E_dotD": twisted["unfilled_fields"]["selected_twisted_D_E_dotD"],
                "chern_weil_row_from_selected_source": after_s3["still_open_cut_set"][
                    "Chern_Weil_row_derived_from_selected_source"
                ],
            },
        },
        "C_direct_hym_routec_solve": {
            "description": (
                "Solve the selected HYM/Strominger or Route C operator problem "
                "directly and use it as the visible operator source."
            ),
            "closed_support": {
                "finite_pipeline_ready": spectral["closed_now"][
                    "current_q79_branch_finite_pipeline_conditionally_validates"
                ],
                "diagnostic_pipeline_ready": selected_de["verdict"]["diagnostic_pipeline_ready"],
                "validator_instantiated": visible_packet["closed_now"][
                    "selected_hym_operator_validator_instantiated"
                ],
            },
            "open_blockers": {
                "selected_D_E_constructed": selected_de["verdict"]["selected_D_E_constructed"] is False,
                "selected_hym_operator_source_verified": hym["calculation_results"][
                    "selected_hym_operator_source_verified"
                ]
                is False,
                "route_c_residual_solve": routec["not_closed"]["route_c_residual_solve"],
            },
        },
    }

    recommended = {
        "primary": "A_rank2_valpha_terminal_monad_primary",
        "required_merge": "B_s3_green_schwarz_visible_support",
        "execution_engine": "C_direct_hym_routec_solve",
        "reason": (
            "A supplies the best topological visible-bundle skeleton, B supplies "
            "the already-closed visible S3/Green-Schwarz support, and C is the "
            "finite validator engine once A+B are promoted to same-source data."
        ),
    }

    output = {
        "certificate": "SelectedQaSU3VisibleSourceArchitecture",
        "status": "QA_SU3_VISIBLE_SOURCE_ARCHITECTURE_RANKED_SAME_SOURCE_BINDING_OPEN",
        "inputs": {
            "routec_source_solve_gate": str(ROUTEC_GATE.relative_to(ROOT)),
            "visible_operator_source_packet_attempt": str(VISIBLE_PACKET.relative_to(ROOT)),
            "rank2_valpha_source_attempt": str(VALPHA.relative_to(ROOT)),
            "monad_difference_l2_source_attempt": str(MONAD_DIFF.relative_to(ROOT)),
            "terminal_monad_lane_selector": str(TERMINAL_LANE.relative_to(ROOT)),
            "spectral_fallback_reduction": str(SPECTRAL_REDUCTION.relative_to(ROOT)),
            "q79_visible_after_s3": str(VISIBLE_AFTER_S3),
            "q79_twisted_packet": str(TWISTED_PACKET),
            "q79_selected_de_attempt": str(SELECTED_DE),
            "q79_hym_attempt": str(HYM_ATTEMPT),
        },
        "template_written": str(OUTPUT_TEMPLATE.relative_to(ROOT)),
        "architectures": architectures,
        "closed_now": {
            "ranked_architectures_built": True,
            "valpha_monad_primary_route_identified": True,
            "s3_gs_support_route_must_be_same_source_bound": True,
            "direct_hym_route_is_execution_engine_not_source_by_itself": True,
            "no_target_fitting_used": True,
        },
        "not_closed": {
            "same_source_binding_between_A_and_B": True,
            "selected_visible_sm_bundle_or_sheaf_model": True,
            "selected_L3_minus_K2_source": True,
            "Pic0_selection_or_quotient": True,
            "typed_transition_or_rhoE_data": True,
            "selected_D_E_dotD_Riesz_Green": True,
            "primitive_C1_or_Yukawa_contractions": True,
            "full_SM_closure": True,
        },
        "recommended_construction": recommended,
        "next_object": {
            "name": "Selected_Qa_SU3_Same_Source_VAlpha_S3_Operator_Packet_v1",
            "must_prove": [
                "V_alpha/L3-K2 and selected S3/GS visible support are the same selected source or are linked by a proved physical quotient",
                "neutral Pic0 is selected or quotient-irrelevant",
                "Chern-Weil row is derived from that source rather than inserted",
                "transition/rhoE data are emitted for the same source",
                "Route C or HYM residual passes honestly with selected_source_verified true",
                "D_E, Riesz/Green, dotD, and projector retention validators pass without smoke lifting",
            ],
        },
        "guardrails": {
            "claims_same_source_binding_proved": False,
            "claims_selected_visible_bundle_constructed": False,
            "claims_selected_D_E_constructed": False,
            "claims_full_SM_closure": False,
            "uses_observed_masses_or_mixings": False,
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
