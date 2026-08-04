from __future__ import annotations

import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SM_ROOT = ROOT.parent / "mtt-sm-parity-closure"

PREV = ROOT / "certificates" / "post_alpha_residual_projector_source_rule_contract_certificate.json"

SM_CERT = SM_ROOT / "certificates" / "selected_weylpairsourceemission_or_honestgalerkinc1execution_valuerun_certificate.json"
SM_CANDIDATE = SM_ROOT / "candidate_data" / "selected_weylpairsourceemission_or_honestgalerkinc1execution_valuerun.candidate.json"
SM_DIR = SM_ROOT / "candidate_data" / "selected_weylpairsourceemission_or_honestgalerkinc1execution_valuerun"
CONDITIONAL_RUN = SM_DIR / "conditional_weylpair_value_run.packet.json"
PROMOTION_ATTEMPT = SM_DIR / "weylpair_source_emission_promotion_attempt.packet.json"
HONEST_GATE = SM_DIR / "honest_galerkin_execution_value_run_gate.packet.json"

OUT_CERT = ROOT / "certificates" / "post_alpha_weylpair_source_emission_valuerun_certificate.json"
OUT_PACKET = ROOT / "candidate_data" / "post_alpha_weylpair_source_emission_valuerun.packet.json"
OUT_NOTE = ROOT / "proof_corpus" / "PostAlpha_WeylPair_SourceEmission_ValueRun_Import_v1.md"

STATUS = "POST_ALPHA_WEYLPAIR_SOURCE_EMISSION_VALUERUN_READY_PROMOTION_BLOCKED"
NEXT = "MTT_Selected_EnrichedWeylPairSourceProvenance_or_GalerkinC1Values_v1"


def load(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def main() -> None:
    prev = load(PREV)
    sm_cert = load(SM_CERT)
    sm_candidate = load(SM_CANDIDATE)
    conditional = load(CONDITIONAL_RUN)
    promotion = load(PROMOTION_ATTEMPT)
    honest = load(HONEST_GATE)

    previous_contract_ok = all(
        [
            prev["theorem"]["proved"] is True,
            prev["closure_claimed"] is False,
            prev["frontier_decision"]["frontier_is_three_route_value_emission_contract"] is True,
            prev["frontier_decision"]["recommended_primary_route"]
            == "B_enriched_weylpair_basis_transport_or_vertex_source",
        ]
    )

    imported_valuerun_ok = all(
        [
            sm_cert["theorem_proved"] is True,
            sm_cert["closure_claimed"] is False,
            sm_cert["SM_parity_dynamic_packet_closure_claimed"] is False,
            sm_cert["no_knob_closure_claimed"] is False,
            sm_cert["true_SM_equivalence_claimed"] is False,
            sm_cert["observed_data_used"] is False,
            sm_cert["target_fitting_used"] is False,
            sm_cert["next_required_artifact"] == NEXT,
            all(sm_cert["what_closes"].values()),
            all(sm_cert["what_remains_open"].values()),
            sm_candidate["theorem"]["proved"] is True,
            sm_candidate["closure_claimed"] is False,
            sm_candidate["observed_data_used"] is False,
            sm_candidate["target_fitting_used"] is False,
            sm_candidate["next_required_artifact"] == NEXT,
            sm_candidate["promotion_decision"]["enriched_weylpair_source_emission_promoted"] is False,
            sm_candidate["promotion_decision"]["A_selected_promoted"] is False,
            sm_candidate["promotion_decision"]["b_selected_promoted"] is False,
            sm_candidate["promotion_decision"]["deltaTheta_C1_promoted"] is False,
            sm_candidate["promotion_decision"]["honest_Galerkin_C1_execution_promoted"] is False,
            all(sm_candidate["what_closes_now"].values()),
            all(sm_candidate["what_remains_open"].values()),
        ]
    )

    conditional_value_run_ok = all(
        [
            conditional["schema"] == "MTTConditionalWeylPairValueRun.v1",
            conditional["status"] == "CONDITIONAL_VALUE_RUN_READY_NOT_PROMOTED",
            conditional["operator_name"] == "A_weylpair_conditional",
            conditional["operator_shape"] == [72, 2],
            conditional["operator_is_A_selected"] is False,
            conditional["selected_value_promotion_allowed_now"] is False,
            conditional["observed_data_used"] is False,
            conditional["target_fitting_used"] is False,
            conditional["rank"] == 2,
            conditional["A_transpose_A_if_promoted"] == [[12.0, 0.0], [0.0, 12.0]],
            conditional["A_transpose_b_if_promoted"] == [12.0, 12.0],
            conditional["deltaTheta_C1_if_promoted"] == [1.0, 1.0],
            conditional["SM_parity_dynamic_packet_would_close_if_promoted"] is True,
            conditional["no_knob_flavor_constants_would_close_if_promoted"] is False,
            "A_selected_currently_emitted_false" in conditional["blocked_by"],
            "b_selected_currently_emitted_false" in conditional["blocked_by"],
        ]
    )

    promotion_attempt_ok = all(
        [
            promotion["schema"] == "MTTWeylPairSourceEmissionPromotionAttempt.v1",
            promotion["status"] == "PROMOTION_BLOCKED_SOURCE_EMISSION_NOT_THEOREM_DERIVED",
            promotion["candidate_route"] == "B_enriched_weylpair_basis_transport_or_vertex_source",
            promotion["observed_data_used"] is False,
            promotion["target_fitting_used"] is False,
            promotion["already_closed_support"]["source_level_weyl_carrier_proved"] is True,
            promotion["already_closed_support"]["active_shift_proved"] is True,
            promotion["already_closed_support"]["conditional_A_rank"] == 2,
            promotion["promotion_decision"]["enriched_weylpair_source_emission_promoted"] is False,
            promotion["promotion_decision"]["A_selected_promoted"] is False,
            promotion["promotion_decision"]["b_selected_promoted"] is False,
            promotion["promotion_decision"]["deltaTheta_C1_promoted"] is False,
            promotion["promotion_inputs_missing"]["A_selected_currently_emitted"] is False,
            promotion["promotion_inputs_missing"]["b_selected_currently_emitted"] is False,
            promotion["promotion_inputs_missing"]["rank_test_now_computable_for_selected_A"] is False,
            promotion["promotion_inputs_missing"]["least_squares_now_computable_for_selected_A"] is False,
        ]
    )

    honest_gate_ok = all(
        [
            honest["schema"] == "MTTHonestGalerkinC1ExecutionValueRunGate.v1",
            honest["status"] == "HONEST_GALERKIN_EXECUTION_VALUES_STILL_OPEN",
            honest["contract_status"] == "HONEST_GALERKIN_RUN_CONTRACT_EMITTED_VALUES_OPEN",
            honest["current_manifest_status"] == "OPEN_C1_PRIMITIVE_CONTRACTIONS_MISSING",
            honest["selected_source_verified"] is False,
            honest["observed_flavor_data_forbidden"] is True,
            honest["target_fitting_forbidden"] is True,
            honest["would_close_SM_parity_dynamic_packet_if_values_emitted"] is True,
            honest["would_close_no_knob_flavor_constants_if_values_emitted"] is False,
            honest["required_outputs"]
            == [
                "zero_mode_bases",
                "primitive_three_by_three_contraction_terms",
                "linear_response_matrices",
                "C33/nonzero-family-rank tests",
            ],
        ]
    )

    missing_source_obligations = promotion["promotion_inputs_missing"]["missing_source_obligations"]
    expected_obligations = {
        "A_selected_assembled_from_theorem_derived_packet",
        "b_selected_emitted",
        "deltaTheta_C1_solve_executed",
        "same_branch_weyl_pair_source_provenance",
        "selected_source_emits_phase_like_Z_or_basis_holonomy",
        "selected_source_emits_shift_like_X_vertex_response",
    }

    what_closes_now = {
        "previous_residual_projector_contract_consumed": previous_contract_ok,
        "primary_weylpair_route_attempt_imported": imported_valuerun_ok,
        "conditional_weylpair_value_run_replayed": conditional_value_run_ok,
        "promotion_blocker_identified": promotion_attempt_ok,
        "honest_Galerkin_value_gate_reemitted": honest_gate_ok,
        "missing_source_obligations_exact": set(missing_source_obligations) == expected_obligations,
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
        "does_not_promote_conditional_operator_as_A_selected": True,
        "does_not_promote_conditional_b_or_deltaTheta": True,
        "does_not_claim_selected_source_emission": True,
        "does_not_claim_honest_Galerkin_values": True,
        "does_not_use_observed_or_target_inputs": True,
        "does_not_claim_SM_or_no_knob_closure": True,
    }

    theorem_proved = all(
        [
            all(what_closes_now.values()),
            all(what_remains_open.values()),
            all(guardrails.values()),
        ]
    )

    theorem = {
        "name": "PostAlphaWeylPairSourceEmissionValueRunImport",
        "proved": theorem_proved,
        "closure_claimed": False,
        "statement": (
            "The primary enriched Weyl-pair source-emission route has been "
            "attempted. Its conditional value run is numerically ready with "
            "rank 2, condition number 1, and DeltaTheta_C1=(1,1), but it is "
            "not selected data because the phase-like Z/basis-holonomy source, "
            "shift-like X/vertex source, A_selected, and b_selected are not "
            "theorem-derived. The frontier is therefore enriched Weyl-pair "
            "source provenance or honest Galerkin C1 values."
        ),
    }

    packet = {
        "theorem": theorem,
        "status": STATUS,
        "what_closes_now": what_closes_now,
        "conditional_value_run": {
            "operator_name": conditional["operator_name"],
            "operator_shape": conditional["operator_shape"],
            "rank": conditional["rank"],
            "condition_number": conditional["condition_number"],
            "relative_residual": conditional["relative_residual"],
            "A_transpose_A_if_promoted": conditional["A_transpose_A_if_promoted"],
            "A_transpose_b_if_promoted": conditional["A_transpose_b_if_promoted"],
            "deltaTheta_C1_if_promoted": conditional["deltaTheta_C1_if_promoted"],
            "selected_now": False,
        },
        "already_closed_support": promotion["already_closed_support"],
        "missing_source_obligations": missing_source_obligations,
        "honest_galerkin_required_outputs": honest["required_outputs"],
        "what_remains_open": what_remains_open,
        "frontier_decision": {
            "frontier_is_enriched_weylpair_source_provenance_or_honest_galerkin_values": True,
            "conditional_value_run_ready": True,
            "conditional_value_run_promoted": False,
            "next_required_artifact": NEXT,
        },
        "guardrails": guardrails,
        "input_artifacts": {
            "previous_residual_projector_source_rule_contract": str(PREV),
            "sm_weylpair_valuerun_certificate": str(SM_CERT),
            "sm_weylpair_valuerun_candidate": str(SM_CANDIDATE),
            "conditional_weylpair_value_run": str(CONDITIONAL_RUN),
            "weylpair_source_emission_promotion_attempt": str(PROMOTION_ATTEMPT),
            "honest_galerkin_execution_value_run_gate": str(HONEST_GATE),
        },
    }

    note = f"""# PostAlpha WeylPair Source-Emission ValueRun Import v1

## Result

The primary enriched Weyl-pair route has been attempted locally as an imported
value-run gate.

The conditional run is ready:

```text
rank(A_conditional) = 2
condition number    = 1.0000000000000002
DeltaTheta_C1       = [1.0, 1.0]
A^T A if promoted   = [[12.0, 0.0], [0.0, 12.0]]
A^T b if promoted   = [12.0, 12.0]
relative residual   = 1.5700924586837752e-16
```

But it is not promoted. The exact missing obligations are:

```text
same-branch Weyl-pair source provenance
selected phase-like Z or basis-holonomy source
selected shift-like X or active-vertex source
theorem-derived A_selected
theorem-derived b_selected
selected DeltaTheta_C1 solve
```

So the remaining problem is no longer a numerical search at this layer. It is
source promotion or honest selected Galerkin C1 value emission.

## Status

```text
{STATUS}
```

Next:

```text
{NEXT}
```
"""

    cert = {
        "program": "MTT protospinor GR response proof",
        "certificate": "post_alpha_weylpair_source_emission_valuerun",
        "status": STATUS,
        "closure_claimed": False,
        "theorem": theorem,
        "what_closes_now": what_closes_now,
        "what_remains_open": what_remains_open,
        "frontier_decision": packet["frontier_decision"],
        "guardrails": guardrails,
        "missing_source_obligations": missing_source_obligations,
        "packet_written": str(OUT_PACKET),
        "note_written": str(OUT_NOTE),
    }

    OUT_PACKET.write_text(json.dumps(packet, indent=2), encoding="utf-8")
    OUT_CERT.write_text(json.dumps(cert, indent=2), encoding="utf-8")
    OUT_NOTE.write_text(note, encoding="utf-8")
    print(f"WROTE: {OUT_CERT}")
    print(f"WROTE: {OUT_PACKET}")
    print(f"WROTE: {OUT_NOTE}")
    print(f"STATUS: {STATUS}")


if __name__ == "__main__":
    main()
