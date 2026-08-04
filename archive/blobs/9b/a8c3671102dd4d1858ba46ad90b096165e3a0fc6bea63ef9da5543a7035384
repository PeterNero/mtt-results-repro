from __future__ import annotations

import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]

PREV = ROOT / "certificates" / "post_alpha_independent_differentiated_residual_projector_source_rule_or_honest_galerkin_c1_execution_certificate.json"
SOURCE_CERT = ROOT / "certificates" / "post_alpha_weylpair_source_emission_or_honest_galerkin_c1_execution_valuerun_certificate.json"

OUT_CERT = ROOT / "certificates" / "post_alpha_independent_weylpair_source_emission_or_honest_galerkin_c1_execution_valuerun_certificate.json"
OUT_PACKET = ROOT / "candidate_data" / "post_alpha_independent_weylpair_source_emission_or_honest_galerkin_c1_execution_valuerun.packet.json"
OUT_NOTE = ROOT / "proof_corpus" / "PostAlpha_IndependentWeylPairSourceEmission_or_HonestGalerkinC1Execution_ValueRun_Import_v1.md"

STATUS = "POST_ALPHA_INDEPENDENT_WEYLPAIR_SOURCE_EMISSION_OR_HONEST_GALERKIN_C1_EXECUTION_VALUERUN_IMPORTED_PROMOTION_BLOCKED"
SOURCE_STATUS = "POST_ALPHA_WEYLPAIR_SOURCE_EMISSION_OR_HONEST_GALERKIN_C1_EXECUTION_VALUERUN_IMPORTED_PROMOTION_BLOCKED"
THIS_ARTIFACT = "MTT_Selected_WeylPairSourceEmission_or_HonestGalerkinC1Execution_ValueRun_v1"
NEXT = "MTT_Selected_EnrichedWeylPairSourceProvenance_or_GalerkinC1Values_v1"


def load(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def main() -> None:
    prev = load(PREV)
    source = load(SOURCE_CERT)
    source_packet = load(Path(source["packet_written"]))

    prev_ok = all(
        [
            prev["theorem"]["proved"] is True,
            prev["closure_claimed"] is False,
            prev["frontier_decision"]["frontier_is_weylpair_source_emission_or_honest_galerkin_value_run"]
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
            source["frontier_decision"]["conditional_value_run_ready"] is True,
            source["frontier_decision"]["selected_value_promotion_blocked"] is True,
            source["frontier_decision"]["next_required_artifact"] == NEXT,
            all(source["what_closes_now"].values()),
            all(source["what_remains_open"].values()),
            all(source["guardrails"].values()),
        ]
    )

    conditional = source_packet["conditional_weylpair_value_run"]
    promotion = source_packet["weylpair_source_emission_promotion_attempt"]
    honest = source_packet["honest_galerkin_execution_value_run_gate"]

    conditional_ok = all(
        [
            conditional["schema"] == "MTTConditionalWeylPairValueRun.v1",
            conditional["status"] == "CONDITIONAL_VALUE_RUN_READY_NOT_PROMOTED",
            conditional["operator_is_A_selected"] is False,
            conditional["operator_shape"] == [72, 2],
            conditional["rank"] == 2,
            abs(conditional["condition_number"] - 1.0) < 1e-12,
            conditional["relative_residual"] < 1e-12,
            conditional["A_transpose_A_if_promoted"] == [[12.0, 0.0], [0.0, 12.0]],
            conditional["A_transpose_b_if_promoted"] == [12.0, 12.0],
            conditional["deltaTheta_C1_if_promoted"] == [1.0, 1.0],
            conditional["SM_parity_dynamic_packet_would_close_if_promoted"] is True,
            conditional["no_knob_flavor_constants_would_close_if_promoted"] is False,
            conditional["selected_value_promotion_allowed_now"] is False,
            conditional["observed_data_used"] is False,
            conditional["target_fitting_used"] is False,
        ]
    )

    promotion_ok = all(
        [
            promotion["status"] == "PROMOTION_BLOCKED_SOURCE_EMISSION_NOT_THEOREM_DERIVED",
            promotion["candidate_route"] == "B_enriched_weylpair_basis_transport_or_vertex_source",
            promotion["already_closed_support"]["target_in_weylpair_span"] is True,
            promotion["already_closed_support"]["conditional_A_rank"] == 2,
            promotion["already_closed_support"]["source_selector_promoted"] is True,
            promotion["promotion_inputs_missing"]["A_selected_currently_emitted"] is False,
            promotion["promotion_inputs_missing"]["b_selected_currently_emitted"] is False,
            promotion["promotion_inputs_missing"]["rank_test_now_computable_for_selected_A"] is False,
            promotion["promotion_inputs_missing"]["least_squares_now_computable_for_selected_A"] is False,
            promotion["promotion_decision"]["enriched_weylpair_source_emission_promoted"] is False,
            promotion["promotion_decision"]["A_selected_promoted"] is False,
            promotion["promotion_decision"]["b_selected_promoted"] is False,
            promotion["promotion_decision"]["deltaTheta_C1_promoted"] is False,
            promotion["promotion_decision"]["SM_parity_dynamic_packet_closed"] is False,
            promotion["observed_data_used"] is False,
            promotion["target_fitting_used"] is False,
        ]
    )

    honest_ok = all(
        [
            honest["status"] == "HONEST_GALERKIN_EXECUTION_VALUES_STILL_OPEN",
            honest["contract_status"] == "HONEST_GALERKIN_RUN_CONTRACT_EMITTED_VALUES_OPEN",
            honest["selected_source_verified"] is False,
            honest["target_fitting_forbidden"] is True,
            honest["observed_flavor_data_forbidden"] is True,
            honest["would_close_SM_parity_dynamic_packet_if_values_emitted"] is True,
            honest["would_close_no_knob_flavor_constants_if_values_emitted"] is False,
        ]
    )

    what_closes_now = {
        "long_name_differentiated_source_rule_gate_consumed": prev_ok,
        "audited_weylpair_value_run_reanchored": source_ok,
        "conditional_rank2_value_run_verified": conditional_ok,
        "promotion_blocker_preserved": promotion_ok,
        "honest_galerkin_value_gate_reemitted": honest_ok,
    }

    what_remains_open = {
        "same_branch_weyl_pair_source_provenance": True,
        "selected_phase_like_Z_or_basis_holonomy_source": True,
        "selected_shift_like_X_vertex_source": True,
        "theorem_derived_A_selected": True,
        "theorem_derived_b_selected": True,
        "selected_deltaTheta_C1": True,
        "honest_selected_Galerkin_C1_execution_values": True,
        "SM_parity_dynamic_packet_closure": True,
        "true_SM_equivalence_closure": True,
        "full_no_knob_flavor_closure": True,
    }

    guardrails = {
        "does_not_promote_conditional_A_as_A_selected": True,
        "does_not_promote_conditional_b_as_b_selected": True,
        "does_not_promote_conditional_deltaTheta": True,
        "does_not_promote_weylpair_source_emission": True,
        "does_not_promote_honest_galerkin_execution": True,
        "does_not_claim_SM_parity_dynamic_closure": True,
        "does_not_claim_true_SM_equivalence": True,
        "does_not_claim_no_knob_flavor_closure": True,
        "does_not_use_observed_or_target_inputs": True,
    }

    theorem = {
        "name": "PostAlphaIndependentWeylPairSourceEmissionAttemptAndValueRunImport",
        "proved": all([all(what_closes_now.values()), all(what_remains_open.values()), all(guardrails.values())]),
        "closure_claimed": False,
        "statement": (
            "The independent long-name branch imports the enriched Weyl-pair "
            "conditional value run. The conditional 72-by-2 operator is rank 2 "
            "with unit condition number and would yield deltaTheta_C1=(1,1), "
            "but A_selected, b_selected, deltaTheta_C1, and SM parity closure "
            "remain unpromoted until same-branch Weyl-pair source emission or "
            "honest Galerkin C1 execution supplies selected values."
        ),
    }

    packet = {
        "theorem": theorem,
        "status": STATUS,
        "what_closes_now": what_closes_now,
        "source_weylpair_valuerun_certificate": source,
        "conditional_weylpair_value_run": conditional,
        "weylpair_source_emission_promotion_attempt": promotion,
        "honest_galerkin_execution_value_run_gate": honest,
        "what_remains_open": what_remains_open,
        "frontier_decision": {
            "conditional_value_run_ready": True,
            "selected_value_promotion_blocked": True,
            "frontier_is_enriched_weylpair_source_provenance_or_galerkin_C1_values": True,
            "next_required_artifact": NEXT,
        },
        "guardrails": guardrails,
        "input_artifacts": {
            "previous_long_name_certificate": str(PREV),
            "source_weylpair_valuerun_certificate": str(SOURCE_CERT),
            "source_weylpair_valuerun_packet": source["packet_written"],
        },
    }

    note = f"""# PostAlpha Independent WeylPairSourceEmission or HonestGalerkinC1Execution ValueRun Import v1

## Result

The independent long-name branch now carries the Weyl-pair conditional value run.

```text
operator shape      = 72 x 2
rank                = 2
condition number    = {conditional["condition_number"]}
relative residual   = {conditional["relative_residual"]}
A^T A if promoted   = [[12, 0], [0, 12]]
A^T b if promoted   = [12, 12]
deltaTheta if proven = [1, 1]
```

This is a value-run readiness theorem, not a selected-value theorem. Promotion is
still blocked until enriched Weyl-pair source provenance or honest Galerkin C1
execution emits the selected matrices.

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
        "certificate": "post_alpha_independent_weylpair_source_emission_or_honest_galerkin_c1_execution_valuerun",
        "status": STATUS,
        "closure_claimed": False,
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
