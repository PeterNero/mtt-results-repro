from __future__ import annotations

import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SM_ROOT = ROOT.parent / "mtt-sm-parity-closure"

PREV = ROOT / "certificates" / "post_alpha_primitive_rows_execution_or_dynamic_dotd_trace_binding_certificate.json"
SM_SLUG = "selected_residualcompletion_sourcepromotion_or_honestgalerkinc1_emission"
SM_CERT = SM_ROOT / "certificates" / f"{SM_SLUG}_certificate.json"
SM_CANDIDATE = SM_ROOT / "candidate_data" / f"{SM_SLUG}.candidate.json"
SM_NOTE = SM_ROOT / "proof_corpus" / "MTT_Selected_ResidualCompletion_SourcePromotion_or_HonestGalerkinC1_Emission_v1.md"
SM_DIR = SM_ROOT / "candidate_data" / SM_SLUG
SOURCE_PACKET = SM_DIR / "minimal_residual_source_packet.template.json"
PARITY_GATE = SM_DIR / "sm_parity_vs_no_knob_acceptance_gate.packet.json"

OUT_CERT = ROOT / "certificates" / "post_alpha_residual_completion_source_promotion_or_honest_galerkin_c1_emission_certificate.json"
OUT_PACKET = ROOT / "candidate_data" / "post_alpha_residual_completion_source_promotion_or_honest_galerkin_c1_emission.packet.json"
OUT_NOTE = ROOT / "proof_corpus" / "PostAlpha_ResidualCompletion_SourcePromotion_or_HonestGalerkinC1_Emission_Import_v1.md"

STATUS = "POST_ALPHA_RESIDUAL_COMPLETION_SOURCE_PROMOTION_OR_HONEST_GALERKIN_C1_EMISSION_GATE_OPEN"
NEXT = "MTT_Selected_ResidualSourceTheorem_or_GalerkinC1Run_ValueFill_v1"


def load(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def main() -> None:
    prev = load(PREV)
    cert = load(SM_CERT)
    candidate = load(SM_CANDIDATE)
    source_packet = load(SOURCE_PACKET)
    parity_gate = load(PARITY_GATE)
    source_note = SM_NOTE.read_text(encoding="utf-8")

    prev_ok = all(
        [
            prev["theorem"]["proved"] is True,
            prev["closure_claimed"] is False,
            prev["frontier_decision"]["frontier_is_residual_completion_source_promotion_or_honest_galerkin_C1_emission"]
            is True,
            prev["frontier_decision"]["next_required_artifact"]
            == "MTT_Selected_ResidualCompletion_SourcePromotion_or_HonestGalerkinC1_Emission_v1",
        ]
    )

    imported_ok = all(
        [
            cert["certificate"] == "MTT_Selected_ResidualCompletion_SourcePromotion_or_HonestGalerkinC1_Emission_v1",
            cert["theorem_proved"] is True,
            cert["closure_claimed"] is False,
            cert["SM_parity_dynamic_packet_closure_claimed"] is False,
            cert["true_SM_equivalence_claimed"] is False,
            cert["no_knob_closure_claimed"] is False,
            cert["observed_data_used"] is False,
            cert["target_fitting_used"] is False,
            cert["next_required_artifact"] == NEXT,
            all(cert["what_closes"].values()),
            all(cert["what_remains_open"].values()),
            candidate["theorem"]["name"] == "ResidualSourcePromotionOrGalerkinC1EmissionGateTheorem",
            candidate["theorem"]["proved"] is True,
            candidate["closure_claimed"] is False,
            candidate["SM_parity_dynamic_packet_closure_claimed"] is False,
            candidate["true_SM_equivalence_claimed"] is False,
            candidate["no_knob_closure_claimed"] is False,
            candidate["promotion_decision"]["lane_A_promoted"] is False,
            candidate["promotion_decision"]["lane_B_promoted"] is False,
            candidate["promotion_decision"]["selected_residual_source_packet_promoted"] is False,
            candidate["promotion_decision"]["honest_Galerkin_C1_emission_promoted"] is False,
            candidate["promotion_decision"]["A_selected_promoted"] is False,
            candidate["promotion_decision"]["b_selected_promoted"] is False,
            candidate["promotion_decision"]["deltaTheta_C1_promoted"] is False,
            candidate["promotion_decision"]["SM_parity_dynamic_packet_closed"] is False,
            candidate["promotion_decision"]["no_knob_flavor_constants_closed"] is False,
            NEXT in source_note,
        ]
    )

    phase = source_packet["required_source_emissions"]["phase_residual_operator_R_Z"]
    shift = source_packet["required_source_emissions"]["shift_residual_operator_R_X"]
    implied = source_packet["if_emitted_then"]
    source_packet_ok = all(
        [
            source_packet["schema"] == "MTTSelectedResidualSourcePacketTemplate.v1",
            source_packet["status"] == "TEMPLATE_EMITTED_SOURCE_THEOREM_OPEN",
            source_packet["same_branch_source_required"] is True,
            source_packet["observed_data_forbidden"] is True,
            source_packet["target_fitting_forbidden"] is True,
            source_packet["selected_source_selector_attached"] is True,
            source_packet["absolute_fiber_origin_selected"] is False,
            source_packet["active_shift"] == [1, 1],
            source_packet["fixed_fiber_class"] == [0, 1, 2],
            source_packet["static_route_required"] == ["u", "e", "d", "nuD"],
            phase["selected_by_MTT_now"] is False,
            shift["selected_by_MTT_now"] is False,
            phase["shape"]["residual_norm_sq"] == 4.0,
            shift["shape"]["residual_norm_sq"] == 2.0,
            phase["shape"]["residual_rank"] == 2,
            shift["shape"]["residual_rank"] == 2,
            phase["shape"]["closure_error_norm_sq"] == 0.0,
            shift["shape"]["closure_error_norm_sq"] == 0.0,
            phase["shape"]["orthogonal_to_fixed_fiber_span"] is True,
            shift["shape"]["orthogonal_to_fixed_fiber_span"] is True,
            implied["projection_plus_residual_reconstructs_conditional_packet"] is True,
            implied["A_selected_columns_available"] is True,
            implied["A_transpose_A"] == [[12.0, 0.0], [0.0, 12.0]],
            implied["A_transpose_b"] == [12.0, 12.0],
            implied["deltaTheta_C1"] == [1.0, 1.0],
            implied["rank"] == 2,
        ]
    )

    parity_ok = all(
        [
            parity_gate["schema"] == "MTTSMParityVsNoKnobResidualGate.v1",
            parity_gate["status"] == "SM_PARITY_GATE_TYPED_PACKET_OPEN_NO_KNOB_STRONGER",
            parity_gate["this_repo_view"] == "SM_PARITY_FIRST",
            parity_gate["sibling_repo_default_view"] == "NO_KNOB_RESEARCH",
            parity_gate["current_decision"]
            == "OPEN_FOR_SM_PARITY_BECAUSE_NO_TYPED_SELECTED_DYNAMIC_PACKET_IS_EMITTED_YET",
            parity_gate["measured_constants_used_as_selector"] is False,
            "typed selected residual source packet R_Z/R_X from Lane A"
            in parity_gate["SM_parity_can_close_with"],
            "typed selected honest Galerkin C1 emission packet from Lane B"
            in parity_gate["SM_parity_can_close_with"],
            "deriving observed Yukawa magnitudes" in parity_gate["SM_parity_does_not_require_here"],
            "derive Yukawa/CKM/PMNS/mass values from the selected packet"
            in parity_gate["no_knob_research_would_still_require"],
        ]
    )

    lane_a, lane_b = candidate["lane_results"]
    lanes_ok = all(
        [
            lane_a["lane"] == "A_residual_source_promotion",
            lane_a["status"] == "OPEN_SOURCE_THEOREM_MISSING",
            lane_a["current_evidence"]["exact_residual_completion_computed"] is True,
            lane_a["current_evidence"]["selected_static_source_selector"] is True,
            lane_a["current_evidence"]["same_branch_residual_source_theorem"] is False,
            lane_a["closes_SM_parity_dynamic_packet_if_source_theorem_supplied"] is True,
            lane_a["closes_no_knob_flavor_constants_if_source_theorem_supplied"] is False,
            lane_b["lane"] == "B_honest_Galerkin_C1_emission",
            lane_b["status"] == "OPEN_RUN_VALUES_MISSING",
            lane_b["selected_source_verified"] is False,
            lane_b["closes_SM_parity_dynamic_packet_if_selected_run_emits_values"] is True,
            lane_b["closes_no_knob_flavor_constants_if_selected_run_emits_values"] is False,
            "linear_response_matrices" in lane_b["required_outputs"],
            "C33/nonzero-family-rank tests" in lane_b["required_outputs"],
        ]
    )

    what_closes_now = {
        "previous_dynamic_binding_gate_consumed": prev_ok,
        "residual_completion_promotion_gate_imported": imported_ok,
        "minimal_residual_source_packet_template_emitted": source_packet_ok,
        "SM_parity_vs_no_knob_acceptance_separated": parity_ok,
        "two_lane_source_promotion_gate_built": lanes_ok,
    }

    what_remains_open = {
        "same_branch_residual_source_theorem": True,
        "honest_selected_Galerkin_C1_value_run": True,
        "selected_residual_source_packet_promoted": True,
        "honest_Galerkin_C1_emission_promoted": True,
        "selected_A_selected": True,
        "selected_b_selected": True,
        "selected_deltaTheta_C1": True,
        "SM_parity_dynamic_packet_closure": True,
        "true_SM_equivalence_closure": True,
        "full_no_knob_flavor_closure": True,
    }

    guardrails = {
        "does_not_promote_lane_A": True,
        "does_not_promote_lane_B": True,
        "does_not_promote_minimal_residual_source_packet": True,
        "does_not_promote_A_b_deltaTheta": True,
        "does_not_claim_SM_parity_dynamic_packet_closure": True,
        "does_not_claim_true_SM_equivalence": True,
        "does_not_claim_no_knob_flavor_closure": True,
        "does_not_use_observed_or_target_inputs": True,
    }

    theorem = {
        "name": "PostAlphaResidualCompletionSourcePromotionOrHonestGalerkinC1EmissionImport",
        "proved": all([all(what_closes_now.values()), all(what_remains_open.values()), all(guardrails.values())]),
        "closure_claimed": False,
        "SM_parity_dynamic_packet_closure_claimed": False,
        "true_SM_equivalence_claimed": False,
        "no_knob_closure_claimed": False,
        "statement": (
            "The residual-completion obstruction is converted into a minimal typed "
            "source-packet template with phase residual R_Z and shift residual R_X. "
            "If a same-branch source theorem or honest selected Galerkin C1 emission "
            "emits those selected operators, the downstream SM-parity dynamic packet "
            "linear algebra is fixed. Neither lane is selected yet, and no no-knob "
            "flavor closure is claimed."
        ),
    }

    packet = {
        "theorem": theorem,
        "status": STATUS,
        "what_closes_now": what_closes_now,
        "source_candidate_summary": {
            "status": candidate["status"],
            "theorem": candidate["theorem"],
            "promotion_decision": candidate["promotion_decision"],
            "minimal_source_packet_summary": candidate["minimal_source_packet_summary"],
            "SM_parity_view": candidate["SM_parity_view"],
            "what_closes_now": candidate["what_closes_now"],
            "what_remains_open": candidate["what_remains_open"],
        },
        "lane_results": candidate["lane_results"],
        "minimal_residual_source_packet": source_packet,
        "sm_parity_vs_no_knob_acceptance_gate": parity_gate,
        "what_remains_open": what_remains_open,
        "frontier_decision": {
            "minimal_residual_source_packet_template_emitted": True,
            "SM_parity_view_separated_from_no_knob_view": True,
            "frontier_is_residual_source_theorem_or_galerkin_C1_run_value_fill": True,
            "next_required_artifact": NEXT,
        },
        "guardrails": guardrails,
        "input_artifacts": {
            "previous_gate_certificate": str(PREV),
            "sm_gate_certificate": str(SM_CERT),
            "sm_gate_candidate": str(SM_CANDIDATE),
            "minimal_residual_source_packet": str(SOURCE_PACKET),
            "sm_parity_vs_no_knob_acceptance_gate": str(PARITY_GATE),
        },
    }

    note = f"""# PostAlpha Residual Completion Source Promotion or Honest Galerkin C1 Emission Import v1

## Result

The residual completion is now a minimal typed source-packet template, but it is not promoted.

Residual source template:

```text
R_Z phase residual norm^2 per sector = 4
R_X shift residual norm^2 per sector = 2
phase residual rank                  = 2
shift residual rank                  = 2
closure error                        = 0
```

Two legal lanes remain:

```text
Lane A: same-branch residual source theorem for R_Z/R_X
Lane B: honest selected Galerkin C1 emission
```

SM-parity closure is separated from the stronger no-knob flavor program. A typed selected dynamic packet would be enough for SM parity here; deriving observed Yukawa, CKM, PMNS, and mass values remains a later no-knob task.

## Status

```text
{STATUS}
```

Next:

```text
{NEXT}
```
"""

    cert_out = {
        "program": "MTT protospinor GR response proof",
        "certificate": "post_alpha_residual_completion_source_promotion_or_honest_galerkin_c1_emission",
        "status": STATUS,
        "closure_claimed": False,
        "SM_parity_dynamic_packet_closure_claimed": False,
        "true_SM_equivalence_claimed": False,
        "no_knob_closure_claimed": False,
        "theorem": theorem,
        "what_closes_now": what_closes_now,
        "what_remains_open": what_remains_open,
        "frontier_decision": packet["frontier_decision"],
        "guardrails": guardrails,
        "packet_written": str(OUT_PACKET),
        "note_written": str(OUT_NOTE),
    }

    OUT_PACKET.write_text(json.dumps(packet, indent=2), encoding="utf-8")
    OUT_CERT.write_text(json.dumps(cert_out, indent=2), encoding="utf-8")
    OUT_NOTE.write_text(note, encoding="utf-8")
    print(f"WROTE: {OUT_CERT}")
    print(f"WROTE: {OUT_PACKET}")
    print(f"WROTE: {OUT_NOTE}")
    print(f"STATUS: {STATUS}")


if __name__ == "__main__":
    main()
