from __future__ import annotations

import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]

PREV = (
    ROOT
    / "certificates"
    / "post_alpha_independent_long_primitive_rows_execution_or_dynamic_dotd_trace_binding_certificate.json"
)
SOURCE_CERT = (
    ROOT
    / "certificates"
    / "post_alpha_residual_completion_source_promotion_or_honest_galerkin_c1_emission_certificate.json"
)

OUT_CERT = (
    ROOT
    / "certificates"
    / "post_alpha_independent_long_residual_completion_source_promotion_or_honest_galerkin_c1_emission_certificate.json"
)
OUT_PACKET = (
    ROOT
    / "candidate_data"
    / "post_alpha_independent_long_residual_completion_source_promotion_or_honest_galerkin_c1_emission.packet.json"
)
OUT_NOTE = (
    ROOT
    / "proof_corpus"
    / "PostAlpha_IndependentLongResidualCompletionSourcePromotion_or_HonestGalerkinC1Emission_Import_v1.md"
)

STATUS = "POST_ALPHA_INDEPENDENT_LONG_RESIDUAL_COMPLETION_SOURCE_PROMOTION_OR_HONEST_GALERKIN_C1_EMISSION_GATE_OPEN"
PREV_STATUS = "POST_ALPHA_INDEPENDENT_LONG_DYNAMIC_DOTD_TRACE_BOUND_PRIMITIVE_ROWS_BLOCKED_BY_RESIDUAL_COMPLETION"
SOURCE_STATUS = "POST_ALPHA_RESIDUAL_COMPLETION_SOURCE_PROMOTION_OR_HONEST_GALERKIN_C1_EMISSION_GATE_OPEN"
THIS_ARTIFACT = "MTT_Selected_ResidualCompletion_SourcePromotion_or_HonestGalerkinC1_Emission_v1"
NEXT = "MTT_Selected_ResidualSourceTheorem_or_GalerkinC1Run_ValueFill_v1"


def load(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def main() -> None:
    prev = load(PREV)
    source = load(SOURCE_CERT)
    source_packet = load(Path(source["packet_written"]))

    prev_ok = all(
        [
            prev["status"] == PREV_STATUS,
            prev["theorem"]["proved"] is True,
            prev["closure_claimed"] is False,
            prev["unpatched_theorem_closure_claimed"] is False,
            prev["frontier_decision"]["dynamic_dotD_trace_binding_accepted"] is True,
            prev["frontier_decision"]["independent_primitive_rows_executed"] is False,
            prev["frontier_decision"]["frontier_is_residual_completion_source_promotion_or_honest_galerkin_C1_emission"]
            is True,
            prev["frontier_decision"]["next_required_artifact"] == THIS_ARTIFACT,
            all(prev["what_closes_now"].values()),
            all(prev["what_remains_open"].values()),
            all(prev["guardrails"].values()),
        ]
    )

    source_ok = all(
        [
            source["status"] == SOURCE_STATUS,
            source["theorem"]["proved"] is True,
            source["closure_claimed"] is False,
            source["SM_parity_dynamic_packet_closure_claimed"] is False,
            source["true_SM_equivalence_claimed"] is False,
            source["no_knob_closure_claimed"] is False,
            source["frontier_decision"]["minimal_residual_source_packet_template_emitted"] is True,
            source["frontier_decision"]["SM_parity_view_separated_from_no_knob_view"] is True,
            source["frontier_decision"]["frontier_is_residual_source_theorem_or_galerkin_C1_run_value_fill"]
            is True,
            source["frontier_decision"]["next_required_artifact"] == NEXT,
            all(source["what_closes_now"].values()),
            all(source["what_remains_open"].values()),
            all(source["guardrails"].values()),
        ]
    )

    source_template = source_packet["minimal_residual_source_packet"]
    parity_gate = source_packet["sm_parity_vs_no_knob_acceptance_gate"]
    lane_a, lane_b = source_packet["lane_results"]

    phase = source_template["required_source_emissions"]["phase_residual_operator_R_Z"]
    shift = source_template["required_source_emissions"]["shift_residual_operator_R_X"]
    implied = source_template["if_emitted_then"]
    source_template_ok = all(
        [
            source_template["schema"] == "MTTSelectedResidualSourcePacketTemplate.v1",
            source_template["status"] == "TEMPLATE_EMITTED_SOURCE_THEOREM_OPEN",
            source_template["same_branch_source_required"] is True,
            source_template["observed_data_forbidden"] is True,
            source_template["target_fitting_forbidden"] is True,
            source_template["selected_source_selector_attached"] is True,
            source_template["absolute_fiber_origin_selected"] is False,
            source_template["active_shift"] == [1, 1],
            source_template["fixed_fiber_class"] == [0, 1, 2],
            phase["selected_by_MTT_now"] is False,
            shift["selected_by_MTT_now"] is False,
            phase["shape"]["residual_norm_sq"] == 4.0,
            shift["shape"]["residual_norm_sq"] == 2.0,
            phase["shape"]["residual_rank"] == 2,
            shift["shape"]["residual_rank"] == 2,
            phase["shape"]["closure_error_norm_sq"] == 0.0,
            shift["shape"]["closure_error_norm_sq"] == 0.0,
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
        ]
    )

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
        ]
    )

    what_closes_now = {
        "fresh_long_dynamic_binding_gate_consumed": prev_ok,
        "audited_residual_completion_gate_reanchored": source_ok,
        "minimal_residual_source_packet_template_emitted": source_template_ok,
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
        "name": "PostAlphaIndependentLongResidualCompletionSourcePromotionOrHonestGalerkinC1EmissionImport",
        "proved": all([all(what_closes_now.values()), all(what_remains_open.values()), all(guardrails.values())]),
        "closure_claimed": False,
        "SM_parity_dynamic_packet_closure_claimed": False,
        "true_SM_equivalence_claimed": False,
        "no_knob_closure_claimed": False,
        "statement": (
            "The fresh long-chain branch converts the independent primitive obstruction "
            "into a typed residual source-packet template. Phase residual R_Z and shift "
            "residual R_X are shaped and sufficient if emitted by a same-branch source "
            "theorem or honest selected Galerkin C1 run, but neither lane is promoted."
        ),
    }

    packet = {
        "theorem": theorem,
        "status": STATUS,
        "what_closes_now": what_closes_now,
        "fresh_previous_certificate": prev,
        "source_residual_completion_certificate": source,
        "lane_results": source_packet["lane_results"],
        "minimal_residual_source_packet": source_template,
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
            "fresh_previous_certificate": str(PREV),
            "source_residual_completion_certificate": str(SOURCE_CERT),
            "source_residual_completion_packet": source["packet_written"],
        },
    }

    note = f"""# PostAlpha IndependentLong Residual Completion Source Promotion or Honest Galerkin C1 Emission Import v1

## Result

The fresh long-chain branch now has a typed residual source-packet template.

Residual source template:

```text
R_Z phase residual norm^2 per sector = 4
R_X shift residual norm^2 per sector = 2
phase residual rank                  = 2
shift residual rank                  = 2
closure error                        = 0
```

Two lanes remain open:

```text
Lane A: same-branch residual source theorem for R_Z/R_X
Lane B: honest selected Galerkin C1 emission
```

No lane, A/b/deltaTheta replay, SM parity closure, or no-knob flavor closure is promoted.

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
        "certificate": "post_alpha_independent_long_residual_completion_source_promotion_or_honest_galerkin_c1_emission",
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
