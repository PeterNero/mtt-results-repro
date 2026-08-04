"""Build the conditional prefix for Selected_Qa_SU3_M1_Chern_Weil_Operator_Source_v1.

The output deliberately separates the source prefix closed under the explicit
terminal admissible-section principle from the still-open dotD/C1/full theorem.
"""

from __future__ import annotations

import json
import sys
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
CERTS = ROOT / "certificates"
CANDIDATES = ROOT / "candidate_data"
CORPUS = ROOT / "proof_corpus"

RETARDED_SELECTOR = CERTS / "q79_retarded_source_boundary_selector_or_source_origin_certificate.json"
CW_ATTEMPT = CERTS / "selected_qa_su3_m1_cw_operator_source_attempt_certificate.json"
CW_PROOF_ATTEMPT = CERTS / "selected_qa_su3_m1_cw_operator_source_proof_attempt_certificate.json"
H1_FIXTURE = CERTS / "selected_qa_su3_m1_rank2_ext_h1_source_data_attempt_certificate.json"
L2_FIXTURE = CERTS / "q79_selected_l2_cochain_ext_or_direct_hym_value_packet_fill_certificate.json"
TERMINAL_SOURCE = CERTS / "q79_base_order_terminal_lane_or_direct_hym_selected_source_import_certificate.json"
AH_HYM_PROMOTION = CERTS / "q79_selected_ah_goodcover_hym_or_routec_residual_promotion_import_certificate.json"
ROUTEC_SYNTHESIS = CERTS / "q79_selected_ah_source_or_routec_residual_synthesis_certificate.json"
PHIFIN_SOURCE = CERTS / "q79_routec_phifin_source_identity_certificate.json"
PHIFIN_DOTD = CERTS / "q79_routec_phifin_dotd_alpha1_source_identity_attempt_certificate.json"

PACKET = CANDIDATES / "selected_qa_su3_m1_cw_operator_source_conditional_prefix.candidate.json"
CERT = CERTS / "selected_qa_su3_m1_cw_operator_source_conditional_prefix_certificate.json"
NOTE = CORPUS / "Selected_Qa_SU3_M1_Chern_Weil_Operator_Source_Conditional_Prefix_v1.md"


def load(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def rel(path: Path) -> str:
    return str(path.relative_to(ROOT)).replace("\\", "/")


def build_packet() -> dict[str, Any]:
    retarded = load(RETARDED_SELECTOR)
    cw_attempt = load(CW_ATTEMPT)
    cw_proof = load(CW_PROOF_ATTEMPT)
    h1_fixture = load(H1_FIXTURE)
    l2_fixture = load(L2_FIXTURE)
    terminal = load(TERMINAL_SOURCE)
    ah_hym = load(AH_HYM_PROMOTION)
    routec = load(ROUTEC_SYNTHESIS)
    phifin = load(PHIFIN_SOURCE)
    phifin_dotd = load(PHIFIN_DOTD)

    selected = terminal["selected_terminal_source_under_principle"]
    derivation = selected["selection_derivation"]
    principle = selected["source_principle"]
    matrix_binding = terminal["sign_and_base_order"]["ordered_base_matrix_binding"]

    prefix_checks = {
        "P0_previous_gate_names_cw_operator_source": retarded["verdict"][
            "next_required_artifact"
        ]
        == "Selected_Qa_SU3_M1_Chern_Weil_Operator_Source_v1",
        "P1_terminal_principle_explicit": principle["status"]
        == "EXPLICIT_PRINCIPLE_SYNTHESIZED_FROM_MTT_CORPUS",
        "P2_terminal_principle_not_unconditional": terminal["verdict"][
            "selected_value_source_unconditional"
        ]
        is False
        and terminal["guardrails"]["claims_unconditional_terminal_selector"] is False,
        "P3_terminal_lane_selects_L3_K2": derivation["selected_source_label"] == "g3 / L3-K2"
        and derivation["selected_L"] == [1, -2, 0]
        and derivation["selected_L2"] == [2, -4, 0],
        "P4_visible_c2_and_shared_circle_match": derivation["selected_c2"] == [4, 0, 0]
        and matrix_binding["central_shared_circle_degree_zero"] is True,
        "P5_ordered_source_and_h1_promote_under_principle": selected["validator_results"][
            "ordered_source"
        ]["exit_code"]
        == 0
        and selected["validator_results"]["cohomology"]["exit_code"] == 0
        and selected["validator_results"]["cohomology"]["promotes_rank_two_route"] is True,
        "P6_old_fixture_was_unselected": h1_fixture["imported_h1_packet"][
            "source_selected_by_mtt"
        ]
        is False
        and l2_fixture["finite_value_packet"]["source_status"]["fixture_only"] is True,
        "P7_terminal_import_promotes_that_payload_conditionally": terminal["what_closes_now"][
            "selected_h1_8_nonzero_Ext_under_principle"
        ]
        is True
        and terminal["what_closes_now"]["selected_ordered_L2_source_under_principle"] is True,
        "P8_formal_cw_target_viable": cw_attempt["closed_now"][
            "formal_trace_free_CW_row_realizable"
        ]
        is True
        and cw_attempt["closed_now"]["rank2_extension_c2_arithmetic_viable"] is True,
        "P9_DE_gap_riesz_green_source_identity_closed": phifin["what_closes_now"][
            "Phi_fin_source_identity_for_D_E_gap_layer"
        ]
        is True
        and phifin["what_closes_now"]["Riesz_Green_layer_closed_from_selected_gap"] is True,
        "P10_dotD_first_variation_still_open": phifin_dotd["verdict"][
            "dotD_source_identity_closed"
        ]
        is False
        and phifin_dotd["what_remains_open"]["selected_alpha1_deformation_parameter"] is True,
        "P11_full_cw_proof_attempt_still_open": cw_proof["theorem_proved"] is False,
        "P12_ah_or_hym_full_promotion_still_open": ah_hym["verdict"][
            "selected_source_or_values_closed"
        ]
        is False
        and ah_hym["what_remains_open"]["same_source_DE_Riesz_Green_dotD"] is True,
        "P13_routec_synthesis_keeps_dotd_and_C1_open": routec["what_remains_open"][
            "same_source_D_E_Riesz_Green_dotD"
        ]
        is True
        and routec["what_remains_open"]["primitive_C1_overlap_tensors"] is True,
    }

    selected_source_prefix = {
        "status": "CONDITIONAL_ON_TERMINAL_ADMISSIBLE_SECTION_SOURCE_PRINCIPLE",
        "principle_name": principle["name"],
        "principle_status": principle["status"],
        "unconditional_selector_proved": False,
        "selected_source_label": derivation["selected_source_label"],
        "selected_L": derivation["selected_L"],
        "selected_L2": derivation["selected_L2"],
        "selected_c2": derivation["selected_c2"],
        "visible_extension_sequence": "0 -> L -> V_alpha -> L^{-1} -> 0",
        "ordered_base_matrix": matrix_binding["matrix_order_g1_to_g6"],
        "central_shared_circle_degree_zero": matrix_binding[
            "central_shared_circle_degree_zero"
        ],
        "validators": selected["validator_results"],
        "why_this_is_not_a_fit_knob": principle["why_not_a_fit_knob"],
        "credibility_boundary": principle["credibility_status"],
    }

    closed_now = {
        "selected_visible_source_prefix_under_explicit_principle": True,
        "rank2_nonzero_Ext_and_h1_promoted_under_explicit_principle": True,
        "visible_Chern_Weil_target_bound_to_L3_K2_conditionally": True,
        "Pic0_quotient_available_for_ordered_CW_H1_scope_only": True,
        "D_E_gap_Riesz_Green_source_identity_imported": True,
        "retarded_selector_reduced_to_CW_operator_source_with_conditional_prefix": True,
    }

    remains = {
        "promote_terminal_principle_to_unconditional_MTT_spine": True,
        "selected_literal_goodcover_or_HYM_stability_payload": True,
        "full_S1_rhoE_source_promotion": True,
        "selected_dotD_alpha1_first_variation": True,
        "retarded_overlap_derivative_formula": True,
        "sector_equality_to_dotD_matrices_without_lifted_flags": True,
        "selected_noninvariant_C1_primitive_or_vertex": True,
        "nonzero_C1_response_matrices": True,
        "selected_Yukawa_or_full_SM_closure": True,
    }

    theorem = {
        "name": "SelectedQaSU3M1ChernWeilOperatorSourceConditionalPrefixTheorem",
        "proved": all(prefix_checks.values()),
        "closure_claimed": False,
        "statement": (
            "Assuming the explicit TerminalAdmissibleSectionSourcePrinciple, "
            "the q79 terminal lane selects g3/L3-K2, hence L=(1,-2,0), "
            "L^2=(2,-4,0), c2(V_alpha)=(4,0,0), and the ordered-source plus "
            "H1/Ext validators promote the visible rank-two V_alpha source "
            "payload. The same branch imports the Phi_fin D_E gap/Riesz/Green "
            "source identity. This is a conditional prefix for "
            "Selected_Qa_SU3_M1_Chern_Weil_Operator_Source_v1, not the full "
            "operator theorem: dotD/alpha1, retarded derivative, C1 response, "
            "and full SM/Yukawa closure remain open."
        ),
    }

    return {
        "packet": "Selected_Qa_SU3_M1_Chern_Weil_Operator_Source_Conditional_Prefix_v1",
        "status": "QA_SU3_M1_CW_OPERATOR_SOURCE_CONDITIONAL_PREFIX_CLOSED_DOTD_C1_OPEN",
        "inputs": {
            "retarded_selector_reduction": rel(RETARDED_SELECTOR),
            "cw_attempt": rel(CW_ATTEMPT),
            "cw_proof_attempt": rel(CW_PROOF_ATTEMPT),
            "h1_fixture": rel(H1_FIXTURE),
            "l2_fixture": rel(L2_FIXTURE),
            "terminal_source_import": rel(TERMINAL_SOURCE),
            "ah_hym_promotion_import": rel(AH_HYM_PROMOTION),
            "routec_synthesis": rel(ROUTEC_SYNTHESIS),
            "phifin_source_identity": rel(PHIFIN_SOURCE),
            "phifin_dotd_attempt": rel(PHIFIN_DOTD),
        },
        "prefix_checks": prefix_checks,
        "selected_source_prefix": selected_source_prefix,
        "same_source_operator_layer": {
            "D_E_gap_Riesz_Green": phifin["selected_source_identity"],
            "dotD_alpha1_status": phifin_dotd["reduction"],
            "scope": (
                "source identity through D_E/gap/Riesz/Green is imported; "
                "first-variation and C1 layers are not promoted"
            ),
        },
        "what_closes_now": closed_now,
        "what_remains_open": remains,
        "theorem": theorem,
        "verdict": {
            "conditional_prefix_closed": theorem["proved"],
            "full_CW_operator_source_closed": False,
            "selected_source_unconditional": False,
            "next_required_artifact": "Selected_Qa_SU3_M1_CW_dotD_alpha1_and_C1_Primitive_Source_v1",
            "why_next": (
                "The selected-source prefix is now stable under the explicit "
                "terminal principle. The true remaining gate is to derive the "
                "same-branch dotD/alpha1 first variation and primitive C1 "
                "response from that source without lifted flags."
            ),
        },
        "guardrails": {
            "claims_unconditional_terminal_selector": False,
            "claims_full_CW_operator_source_theorem": False,
            "claims_selected_dotD_alpha1": False,
            "claims_nonzero_C1_response": False,
            "claims_Yukawa_or_full_SM_closure": False,
            "uses_observed_cp_or_masses": False,
            "uses_benchmark_flavor_entries": False,
            "uses_lifted_selected_flags": False,
        },
    }


def render_note(packet: dict[str, Any]) -> str:
    return "\n".join(
        [
            "# Selected Qa/SU3 M1 Chern-Weil Operator Source Conditional Prefix v1",
            "",
            "## Result",
            "",
            f"Status: `{packet['status']}`",
            "",
            "The source part of `Selected_Qa_SU3_M1_Chern_Weil_Operator_Source_v1`",
            "is now closed as a conditional prefix: assuming the explicit",
            "`TerminalAdmissibleSectionSourcePrinciple.v1`, the q79 terminal lane",
            "selects `g3 / L3-K2`, hence `L=(1,-2,0)`, `L^2=(2,-4,0)`,",
            "and `c2(V_alpha)=(4,0,0)`.  The ordered-source and `H^1/Ext`",
            "validators then promote the previously fixture-only rank-two payload.",
            "",
            "This is not the full Chern-Weil/operator source theorem.  The terminal",
            "principle still needs promotion to the unconditional MTT spine, and the",
            "same-source `dotD/alpha1`, retarded derivative, and primitive `C1`",
            "response layers remain open.",
            "",
            "## Conditional Source Prefix",
            "",
            "```json",
            json.dumps(packet["selected_source_prefix"], indent=2, sort_keys=True),
            "```",
            "",
            "## Same-Source Operator Layer",
            "",
            "```json",
            json.dumps(packet["same_source_operator_layer"], indent=2, sort_keys=True),
            "```",
            "",
            "## What Closes Now",
            "",
            "```json",
            json.dumps(packet["what_closes_now"], indent=2, sort_keys=True),
            "```",
            "",
            "## What Remains Open",
            "",
            "```json",
            json.dumps(packet["what_remains_open"], indent=2, sort_keys=True),
            "```",
            "",
            f"Next: `{packet['verdict']['next_required_artifact']}`.",
            "",
        ]
    )


def main() -> int:
    packet = build_packet()
    if "--write-certificate" in sys.argv:
        PACKET.write_text(json.dumps(packet, indent=2, sort_keys=True) + "\n", encoding="utf-8")
        CERT.write_text(json.dumps(packet, indent=2, sort_keys=True) + "\n", encoding="utf-8")
        NOTE.write_text(render_note(packet), encoding="utf-8")
    print(json.dumps(packet, indent=2, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
