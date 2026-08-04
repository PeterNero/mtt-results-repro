"""Attempt the selected Qa/SU3 m=1 Chern-Weil/operator source construction."""

from __future__ import annotations

import json
import sys
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
CERTS = ROOT / "certificates"
Q79_CERTS = Path(r"C:\Users\nero_\Downloads\TEXPAPERS\mtt-q79-proof-repro\certificates")

OPERATOR_CUTSET = CERTS / "selected_qa_su3_m1_operator_cutset_certificate.json"
COMMON_PAYLOAD = CERTS / "common_de_dotd_riesz_green_payload_map_certificate.json"
FORMAL_CW = Q79_CERTS / "visible_chern_weil_formal_source_certificate.json"
QUANTIZATION = Q79_CERTS / "visible_chern_weil_quantization_gate_certificate.json"
INTEGRAL_CANDIDATE = Q79_CERTS / "visible_integral_chern_source_candidate_certificate.json"
RANK2_ROUTE = Q79_CERTS / "visible_rank2_extension_valpha_route_certificate.json"
RANK2_H1_GATE = Q79_CERTS / "visible_rank2_l2_ext_h1_gate_certificate.json"
MONAD_ROLE = Q79_CERTS / "iwasawa_monad_visible_source_role_certificate.json"
FUSION_ATTEMPT = Q79_CERTS / "same_source_monad_gs_operator_fusion_attempt_certificate.json"
BLOCKER = Q79_CERTS / "visible_operator_source_blocker_resolution_certificate.json"

OUTPUT_CERT = CERTS / "selected_qa_su3_m1_cw_operator_source_attempt_certificate.json"
OUTPUT_TEMPLATE = CERTS / "selected_qa_su3_m1_rank2_ext_h1_source_data.template.json"


def load(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def h1_source_template(preferred: dict[str, Any]) -> dict[str, Any]:
    return {
        "schema": "SelectedQaSU3M1Rank2ExtH1SourceData.v1",
        "status": "OPEN_SELECTED_QA_SU3_M1_RANK2_EXT_H1_SOURCE_DATA_REQUIRED",
        "purpose": (
            "Fill the finite Cech/Dolbeault data for the preferred non-split "
            "rank-two V_alpha route, prove a nonzero extension class, then use "
            "that selected source to feed HYM/Route-C and D_E/dotD/Riesz/Green."
        ),
        "preferred_first_target": preferred,
        "must_supply": {
            "selected_holomorphic_line_bundle_L_squared": None,
            "C0_basis": None,
            "C1_basis": None,
            "C2_basis": None,
            "d0_matrix": None,
            "d1_matrix": None,
            "proof_d1_d0_zero": None,
            "closed_non_exact_extension_vector_eta": None,
            "selected_chamber_or_Gauduchon_data": None,
            "non_split_stability_or_HYM_existence_certificate": None,
            "same_source_operator_payload_plan": None,
        },
        "acceptance_tests": [
            "d1*d0=0 and h1=dim ker(d1)-rank(d0)>0.",
            "eta is closed and not exact.",
            "The selected source realizes c1=0 and c2=4 alpha_1 without using the split abelian shortcut.",
            "The same source is the one later used for D_E/Riesz/Green/dotD.",
        ],
        "forbidden_shortcuts": [
            "Do not claim h1 from topology-only c1 data.",
            "Do not use the split line-pair candidate as an HYM source.",
            "Do not reuse the c2=0 printed monad as the c2=4 alpha_1 visible source.",
        ],
    }


def main() -> None:
    cutset = load(OPERATOR_CUTSET)
    common = load(COMMON_PAYLOAD)
    formal = load(FORMAL_CW)
    quant = load(QUANTIZATION)
    integral = load(INTEGRAL_CANDIDATE)
    rank2 = load(RANK2_ROUTE)
    h1_gate = load(RANK2_H1_GATE)
    monad = load(MONAD_ROLE)
    fusion = load(FUSION_ATTEMPT)
    blocker = load(BLOCKER)
    template = h1_source_template(h1_gate["preferred_first_target"])

    output = {
        "certificate": "SelectedQaSU3M1ChernWeilOperatorSourceAttempt",
        "status": "QA_SU3_M1_CW_OPERATOR_SOURCE_ATTEMPT_RANK2_EXT_H1_DATA_OPEN",
        "inputs": {
            "operator_cutset": str(OPERATOR_CUTSET.relative_to(ROOT)),
            "common_payload_map": str(COMMON_PAYLOAD.relative_to(ROOT)),
            "q79_visible_chern_weil_formal_source": str(FORMAL_CW),
            "q79_visible_chern_weil_quantization_gate": str(QUANTIZATION),
            "q79_visible_integral_chern_source_candidate": str(INTEGRAL_CANDIDATE),
            "q79_visible_rank2_extension_valpha_route": str(RANK2_ROUTE),
            "q79_visible_rank2_l2_ext_h1_gate": str(RANK2_H1_GATE),
            "q79_iwasawa_monad_visible_source_role": str(MONAD_ROLE),
            "q79_same_source_monad_gs_operator_fusion_attempt": str(FUSION_ATTEMPT),
            "q79_visible_operator_source_blocker_resolution": str(BLOCKER),
        },
        "closed_now": {
            "formal_trace_free_CW_row_realizable": formal["what_this_closes"][
                "formal_trace_free_Chern_Weil_row_realizability"
            ],
            "no_current_integrality_contradiction": quant["what_this_closes"][
                "no_current_integrality_contradiction"
            ],
            "standard_chern_character_label_for_candidate": integral[
                "what_this_closes"
            ]["standard_chern_character_label_for_candidate"],
            "split_abelian_shortcut_rejected_as_HYM_source": integral[
                "what_this_closes"
            ]["split_abelian_shortcut_rejected_as_HYM_source"],
            "rank2_extension_c2_arithmetic_viable": rank2["what_this_closes"][
                "minimal_rank2_extension_c2_arithmetic"
            ],
            "rank2_h1_finite_input_format_defined": h1_gate["what_this_closes"][
                "exact_finite_input_format_for_H1_X_L_squared"
            ],
            "printed_c2_zero_monad_not_visible_alpha1_source": monad[
                "what_this_closes"
            ]["do_not_reuse_c2_zero_monad_as_c2_4_alpha1_source"],
            "same_source_gap_confirmed_by_fusion_validator": fusion[
                "what_this_closes"
            ]["selected_source_gap_confirmed"],
        },
        "source_route_ranking": [
            {
                "rank": 1,
                "route": "non_split_rank2_V_alpha_extension",
                "status": "PRIMARY_LIVE_SOURCE_ROUTE",
                "why": [
                    "It has c1=0 and c2=4 alpha_1 arithmetic.",
                    "It avoids the split abelian HYM no-go.",
                    "Its next missing data are finite and explicit: H^1(X,L^2), nonzero Ext class, stability/HYM source.",
                ],
                "next_required_data": h1_gate["preferred_first_target"],
            },
            {
                "rank": 2,
                "route": "Route_C_or_direct_HYM_selected_solve",
                "status": "EXECUTION_ENGINE_AFTER_SOURCE_OR_FALLBACK_SOURCE",
                "why": [
                    "Validators and finite pipeline exist.",
                    "Current attempts fail only because selected source flags and same-branch derivative proof are absent.",
                ],
                "open_items": blocker["minimal_new_data_that_would_close"],
            },
            {
                "rank": 3,
                "route": "printed_three_family_monad",
                "status": "MATTER_ZERO_MODE_SEED_NOT_VISIBLE_CW_SOURCE",
                "why": [
                    "It has c2=0, while the visible source requires c2=4 alpha_1.",
                    "It may still supply matter zero modes only if typed maps and same-source operator data are supplied.",
                ],
            },
            {
                "rank": 4,
                "route": "split_abelian_line_pair",
                "status": "RETIRED_AS_HYM_SOURCE_BUT_USEFUL_AS_INTEGRAL_TARGET_WITNESS",
                "why": [
                    "It identifies the integral Chern-character label.",
                    "It fails individual primitivity/HYM for positive radii.",
                ],
            },
        ],
        "attempt_result": {
            "cw_operator_source_constructed": False,
            "selected_visible_bundle_or_sheaf_model": False,
            "chern_weil_row_derived_from_selected_source": False,
            "HYM_or_Route_C_residual_with_selected_source_verified": False,
            "coherent_spectral_zero_mode_projectors": False,
            "sector_D_E_action_matrices": False,
            "Riesz_projectors_and_gap_bounds": False,
            "reduced_Green_operators": False,
            "same_branch_dotD_alpha1_response": False,
            "primitive_C1_contractions": False,
        },
        "not_closed": {
            "compute_H1_X_L_squared_for_preferred_rank2_target": h1_gate[
                "still_open"
            ]["compute_actual_h1_for_L_squared"],
            "select_nonzero_extension_class": rank2["still_open"][
                "select_nonzero_extension_class"
            ],
            "prove_non_split_extension_stability": rank2["still_open"][
                "prove_non_split_extension_stability"
            ],
            "prove_HYM_or_Route_C_residual": rank2["still_open"][
                "prove_HYM_or_Route_C_residual"
            ],
            "derive_same_total_source_D_E_dotD_Riesz_Green": rank2[
                "still_open"
            ]["derive_same_total_source_D_E_dotD_Riesz_Green"],
            "primitive_C1_contractions": rank2["still_open"][
                "primitive_C1_contractions"
            ],
            "full_SM_closure": rank2["still_open"]["full_SM_closure"],
        },
        "relation_to_common_payload": {
            "current_frontier": common["memory_checkpoint"]["current_branch_frontier"],
            "payload_order": common["common_payload"],
            "this_attempt_closes_prefix_through": [
                "formal row target",
                "integral label witness",
                "primary source route selection",
            ],
            "first_unfilled_payload_item": "selected_source_certificate",
        },
        "next_object": {
            "name": "Selected_Qa_SU3_M1_Rank2_Ext_H1_Source_Data_v1",
            "template": str(OUTPUT_TEMPLATE.relative_to(ROOT)),
            "role": h1_gate["verdict"]["next_action"],
        },
        "guardrails": {
            "claims_selected_visible_operator_source_constructed": False,
            "claims_selected_D_E_dotD_constructed": False,
            "claims_h1_value_computed": False,
            "claims_full_SM_closure": False,
            "uses_observed_flavor_data": False,
            "uses_lifted_flags_as_proof": False,
        },
        "honest_answer": (
            "The Chern-Weil/operator-source construction is advanced but not "
            "closed. The row and integral target are viable, the split shortcut "
            "is rejected, and the primary live source is the non-split rank-two "
            "V_alpha extension. The next true computation is H^1(X,L^2) and a "
            "selected nonzero Ext class for the preferred L=(1,-2,0) target."
        ),
    }

    cert_text = json.dumps(output, indent=2, sort_keys=True)
    if "--write-certificate" in sys.argv:
        OUTPUT_CERT.write_text(cert_text + "\n", encoding="utf-8")
        OUTPUT_TEMPLATE.write_text(
            json.dumps(template, indent=2, sort_keys=True) + "\n",
            encoding="utf-8",
        )
    print(cert_text)


if __name__ == "__main__":
    main()
