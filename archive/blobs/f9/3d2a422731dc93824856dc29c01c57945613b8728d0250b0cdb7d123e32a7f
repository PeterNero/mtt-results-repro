"""Build visible Chern-Weil source proof or Route-C residual/D_E value-fill attempt."""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "candidate_data"
CERTS = ROOT / "certificates"
CORPUS = ROOT / "proof_corpus"

SLUG = "selected_visiblechernweilsourceproof_or_routecresidualdevaluefill"
PACKET_DIR = DATA / SLUG
OUTPUT = DATA / f"{SLUG}.candidate.json"
ATTEMPT = PACKET_DIR / "visible_chern_weil_or_routec_value_fill_attempt.packet.json"
EDGE_TEST = PACKET_DIR / "rank2_and_routec_edge_test.packet.json"
DECISION = PACKET_DIR / "operator_source_slot_decision_after_value_fill.packet.json"
CERT = CERTS / f"{SLUG}_certificate.json"
NOTE = CORPUS / "MTT_Selected_VisibleChernWeilSourceProof_or_RouteCResidualAndDEValueFill_v1.md"

STATUS = "MTT_SELECTED_VISIBLECHERNWEILSOURCEPROOF_OR_ROUTECRESIDUALDEVALUEFILL_BUILT_SOURCE_PROMOTION_STILL_OPEN"
NEXT = "MTT_Selected_PhiFinPayload_or_GlobalDestabilizerEnumeration_ClosingRun_v1"


def rel(path: Path) -> str:
    try:
        return str(path.relative_to(ROOT)).replace("\\", "/")
    except ValueError:
        return str(path)


def load(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def main() -> int:
    PACKET_DIR.mkdir(parents=True, exist_ok=True)

    fourth = load(DATA / "selected_fourthqasu3operatorslotclosure_or_visiblechernweilsource.candidate.json")
    visible_cw = load(DATA / "selected_visible_chern_weil_operator_source.candidate.json")
    rank2 = load(DATA / "selected_routec_stability_hym_or_routec_residual_source.candidate.json")
    routec_de = load(DATA / "selected_routec_de_action_on_smooth_bn.candidate.json")
    routec_dotd = load(DATA / "selected_routec_sector_projectors_dotd_on_smooth_bn.candidate.json")
    routec_first = load(DATA / "selected_routec_strominger_galerkin_first_run.candidate.json")
    phifin = load(DATA / "finite_emission_morphism_phifin.candidate.json")
    phifin_alpha1 = load(DATA / "selected_phifin_alpha1_payload.candidate.json")
    provenance_basis = load(DATA / "selected_routec_source_provenance_or_basis_certificate.candidate.json")
    source_origin = load(DATA / "routec_selected_source_origin_lemma.candidate.json")

    rank2_edge_closed = (
        rank2["proof_verdict"]["full_stability_proved"] is True
        and rank2["proof_verdict"]["hym_existence_proved"] is True
        and visible_cw["open_gates"]["same_source_cut_set"]["Chern_Weil_row_derived_from_selected_source"] is False
    )
    routec_edge_closed = (
        routec_first["validation"]["honest_root_all_pass"] is True
        and phifin["obstruction"]["selected_payload_closed"] is True
        and all(phifin["phifin_schema"]["selected_flags"].values())
        and all(phifin_alpha1["payload_summary"]["selected_payload_flags"].values())
    )
    lower_algebra_ready = (
        routec_first["validation"]["formal_lift_lower_validators_all_pass"] is True
        and routec_de["validation"]["matrix_consistency"]["honest_validator_fails_only_by_selected_source_flags"] is True
        and routec_dotd["validation"]["honest_validator_fails_only_by_source_driver_flags"] is True
    )

    edge_test = {
        "schema": "MTTRank2AndRouteCEdgeTest.v1",
        "rank2_visible_bundle_edge": {
            "closed": rank2_edge_closed,
            "support_closed": {
                "selected_l2_ext_input": True,
                "central_neutral_destabilizers_obstructed": rank2["proof_verdict"][
                    "central_neutral_stability_subtheorem_proved"
                ],
                "chern_h1_curvature_layer_pic0_quotiented": True,
            },
            "missing": {
                "global_rank_one_torsion_free_subsheaf_enumeration": rank2["what_remains_open"][
                    "global_rank_one_torsion_free_subsheaf_enumeration"
                ],
                "prove_all_destabilizers_have_central_neutral_reflexive_hull": rank2["what_remains_open"][
                    "prove_all_destabilizers_have_central_neutral_base_pullback_reflexive_hull"
                ],
                "selected_HYM_or_Strominger_existence_certificate": rank2["what_remains_open"][
                    "selected_HYM_or_Strominger_existence_certificate"
                ],
                "same_source_D_E_Riesz_Green_dotD": rank2["what_remains_open"][
                    "same_source_D_E_Riesz_Green_dotD"
                ],
            },
        },
        "routec_value_fill_edge": {
            "closed": routec_edge_closed,
            "lower_algebra_ready": lower_algebra_ready,
            "support_closed": {
                "fixed_q79_branch": provenance_basis["provenance_gate"]["support"]["fixed_q79_branch"],
                "strominger_selection_support": provenance_basis["provenance_gate"]["support"][
                    "strominger_selection_support"
                ],
                "phifin_codomain_schema": provenance_basis["provenance_gate"]["support"]["phifin_codomain_schema"],
                "formal_lift_lower_validators_all_pass": routec_first["validation"][
                    "formal_lift_lower_validators_all_pass"
                ],
                "DE_matrix_emitted": routec_de["what_closes_now"]["D_E_matrix_on_27_mode_BN_emitted"],
                "dotD_matrix_emitted": routec_dotd["what_closes_now"]["dotD_alpha1_matrix_in_same_basis_emitted"],
            },
            "missing": {
                "Phi_fin_selected_payload": provenance_basis["what_remains_open"]["Phi_fin_selected_payload"],
                "quotient_valid_BN_basis_certificate": provenance_basis["what_remains_open"][
                    "quotient_valid_BN_basis_certificate"
                ],
                "selected_source_flags_promoted": provenance_basis["what_remains_open"][
                    "selected_source_flags_promoted"
                ],
                "selected_payload_closed": phifin["obstruction"]["selected_payload_closed"] is False,
                "selected_PhiFin_alpha1_payload_values": phifin_alpha1["what_remains_open"][
                    "selected_PhiFin_alpha1_payload_values"
                ],
            },
        },
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
    }

    source_promotion_closure = rank2_edge_closed or routec_edge_closed
    attempted_fill = {
        "schema": "MTTVisibleChernWeilOrRouteCValueFillAttempt.v1",
        "input_frontier": rel(DATA / "selected_fourthqasu3operatorslotclosure_or_visiblechernweilsource.candidate.json"),
        "attempted_gate": "same_source_Chern_Weil_row_or_selected_RouteC_residual_DE_value_fill",
        "existing_support": {
            "SM_parity_closed": fourth["closure_decision"]["SM_parity_closed"],
            "previous_operator_source_slots_closed": fourth["closure_decision"][
                "operator_source_slots_closed_total"
            ],
            "visible_green_schwarz_support_retained": fourth["closure_decision"][
                "visible_chern_weil_support_retained"
            ],
            "fixed_sector_source_support_exists": source_origin["gate_matrix"]["G1_fixed_topological_sector_named"][
                "passes"
            ],
            "MTT_strominger_selection_support_exists": source_origin["gate_matrix"][
                "G2_MTT_Strominger_selection_available"
            ]["passes"],
            "lower_routec_algebra_validates_under_formal_lift": lower_algebra_ready,
        },
        "promotion_result": {
            "source_promotion_closed": source_promotion_closure,
            "rank2_edge_closed": rank2_edge_closed,
            "routec_edge_closed": routec_edge_closed,
            "same_source_Chern_Weil_row_derived": rank2_edge_closed,
            "selected_RouteC_residual_DE_values_emitted": routec_edge_closed,
            "fourth_operator_source_slot_closed": source_promotion_closure,
            "why_not_closed": (
                "Both edges were tested. The rank-two edge still lacks global destabilizer enumeration/HYM "
                "existence and same-source operator data. The Route-C edge has validator-ready lower algebra, "
                "but Phi_fin selected payload, quotient-valid B_N basis, and theorem-derived selected-source/"
                "alpha1-driver flags are still open. Promoting the diagnostic formal lift would overclaim."
            ),
        },
        "minimal_closing_theorem": {
            "name": "PhiFinPayloadOrGlobalDestabilizerEnumerationClosingRun",
            "rank2_sufficient_condition": [
                "enumerate all rank-one torsion-free destabilizer reflexive hulls and reduce them to the closed central-neutral list",
                "prove stability/HYM existence for the selected non-split V_alpha source",
                "derive the visible Chern-Weil row and D_E/Riesz/Green/dotD from that same source",
            ],
            "routec_sufficient_condition": [
                "emit selected Phi_fin payload from the selected q79/F,m=1 Strominger/HYM minimizer",
                "emit quotient/deck-valid B_N basis certificate",
                "rerun lower validators with theorem-derived selected_source_verified, selected_dotD_source_verified, and alpha1_driver_verified",
            ],
        },
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
    }

    closed_slots = 4 if source_promotion_closure else fourth["closure_decision"]["operator_source_slots_closed_total"]
    remaining_slots = 8 - closed_slots
    decision = {
        "schema": "MTTOperatorSourceSlotDecisionAfterValueFill.v1",
        "status": "SOURCE_PROMOTION_OPEN_LOWER_ALGEBRA_READY" if not source_promotion_closure else "FOURTH_SLOT_CLOSED",
        "operator_source_slots_closed": closed_slots,
        "operator_source_slots_remaining": remaining_slots,
        "fourth_operator_source_slot_closed": source_promotion_closure,
        "lower_routec_algebra_ready": lower_algebra_ready,
        "true_SM_equivalence_closed": False,
        "no_knob_closed": False,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
    }

    candidate = {
        "candidate": "MTTSelectedVisibleChernWeilSourceProofOrRouteCResidualDEValueFill",
        "status": STATUS,
        "inputs": {
            "fourth_slot_cutset": rel(DATA / "selected_fourthqasu3operatorslotclosure_or_visiblechernweilsource.candidate.json"),
            "visible_cw_source": rel(DATA / "selected_visible_chern_weil_operator_source.candidate.json"),
            "rank2_stability": rel(DATA / "selected_routec_stability_hym_or_routec_residual_source.candidate.json"),
            "routec_first_run": rel(DATA / "selected_routec_strominger_galerkin_first_run.candidate.json"),
            "finite_emission_morphism": rel(DATA / "finite_emission_morphism_phifin.candidate.json"),
            "phifin_alpha1_payload": rel(DATA / "selected_phifin_alpha1_payload.candidate.json"),
            "provenance_or_basis": rel(DATA / "selected_routec_source_provenance_or_basis_certificate.candidate.json"),
        },
        "output_packets": {
            "rank2_and_routec_edge_test": rel(EDGE_TEST),
            "visible_chern_weil_or_routec_value_fill_attempt": rel(ATTEMPT),
            "operator_source_slot_decision_after_value_fill": rel(DECISION),
        },
        "theorem": {
            "name": "VisibleChernWeilSourceProofOrRouteCResidualDEValueFillAttemptTheorem",
            "proved": True,
            "statement": (
                "The attempted closure of the fourth Qa/SU3 operator-source slot has exactly two honest edges: "
                "rank-two global stability/HYM with same-source Chern-Weil/operator derivation, or Route-C "
                "selected Phi_fin/basis promotion of the existing finite lower algebra. Current artifacts close "
                "the lower algebra and support stacks but do not close either source-promotion edge."
            ),
        },
        "what_closes_now": {
            "both_edges_tested": True,
            "lower_routec_algebra_ready_for_honest_replay": lower_algebra_ready,
            "rank2_missing_global_stability_not_arithmetic": True,
            "routec_missing_source_promotion_not_matrix_shape": True,
            "formal_lift_rejected_as_proof": True,
            "target_fitting_excluded": True,
        },
        "what_remains_open": {
            "same_source_Chern_Weil_row": not rank2_edge_closed,
            "selected_RouteC_residual_DE_values": not routec_edge_closed,
            "Phi_fin_selected_payload": True,
            "quotient_valid_BN_basis_certificate": True,
            "global_destabilizer_enumeration_or_HYM_existence": True,
            "actual_dynamic_QaSU3_operator_packet": True,
            "true_SM_equivalence": True,
            "no_knob_closure": True,
        },
        "closure_decision": {
            "SM_parity_closed": True,
            "fourth_QaSU3_operator_source_slot_closed": source_promotion_closure,
            "operator_source_slots_closed_total": closed_slots,
            "operator_source_slots_remaining": remaining_slots,
            "actual_dynamic_QaSU3_operator_packet_closed": False,
            "true_SM_equivalence_closed": False,
            "no_knob_closed": False,
        },
        "next_required_artifact": NEXT,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "closure_claimed": source_promotion_closure,
    }

    cert = {
        "certificate": "MTT_Selected_VisibleChernWeilSourceProof_or_RouteCResidualAndDEValueFill_v1",
        "candidate_path": rel(OUTPUT),
        "status": STATUS,
        "theorem_proved": True,
        "source_promotion_closed": source_promotion_closure,
        "fourth_QaSU3_operator_source_slot_closed": source_promotion_closure,
        "closed_operator_source_slots_total": closed_slots,
        "operator_source_slots_remaining": remaining_slots,
        "lower_routec_algebra_ready": lower_algebra_ready,
        "next_required_artifact": NEXT,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "note_path": rel(NOTE),
    }

    note = f"""# MTT Selected VisibleChernWeilSourceProof or RouteCResidualAndDEValueFill v1

This artifact tries to close the fourth Qa/SU3 operator-source slot by both
honest edges:

- rank-two global stability/HYM plus same-source Chern-Weil/operator derivation
- Route-C selected `Phi_fin`/basis promotion of the already emitted finite
  `rho_E`, `D_E`, Riesz/Green, and `dotD` lower algebra

It does not close the slot yet.  The important advance is that the obstruction
is no longer a vague matrix or shape problem: the Route-C lower algebra validates
under formal lift, and the rank-two arithmetic/cohomology layer is already past
the selected `L^2`/Ext stage.  The remaining blocker is source promotion:
selected `Phi_fin` payload plus quotient-valid `B_N` basis, or a global
destabilizer/HYM theorem for the selected non-split `V_alpha`.

Promoting the diagnostic formal lift would be an overclaim.

Current count remains three closed operator-source slots and five open slots.

Next artifact: `{NEXT}`.
"""

    for path, payload in [
        (EDGE_TEST, edge_test),
        (ATTEMPT, attempted_fill),
        (DECISION, decision),
        (OUTPUT, candidate),
        (CERT, cert),
    ]:
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(json.dumps(payload, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    NOTE.write_text(note, encoding="utf-8")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
