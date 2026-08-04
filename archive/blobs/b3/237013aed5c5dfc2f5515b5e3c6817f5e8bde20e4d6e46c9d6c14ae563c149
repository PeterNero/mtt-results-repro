from __future__ import annotations

import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SM_ROOT = ROOT.parent / "mtt-sm-parity-closure"

PREV = ROOT / "certificates" / "post_alpha_differentiated_residual_projector_source_rule_or_honest_galerkin_c1_execution_certificate.json"
SLUG = "selected_weylpairsourceemission_or_honestgalerkinc1execution_valuerun"
SM_CERT = SM_ROOT / "certificates" / f"{SLUG}_certificate.json"
SM_CANDIDATE = SM_ROOT / "candidate_data" / f"{SLUG}.candidate.json"
SM_DIR = SM_ROOT / "candidate_data" / SLUG
CONDITIONAL_RUN = SM_DIR / "conditional_weylpair_value_run.packet.json"
PROMOTION_ATTEMPT = SM_DIR / "weylpair_source_emission_promotion_attempt.packet.json"
HONEST_GATE = SM_DIR / "honest_galerkin_execution_value_run_gate.packet.json"

OUT_CERT = ROOT / "certificates" / "post_alpha_weylpair_source_emission_or_honest_galerkin_c1_execution_valuerun_certificate.json"
OUT_PACKET = ROOT / "candidate_data" / "post_alpha_weylpair_source_emission_or_honest_galerkin_c1_execution_valuerun.packet.json"
OUT_NOTE = ROOT / "proof_corpus" / "PostAlpha_WeylPairSourceEmission_or_HonestGalerkinC1Execution_ValueRun_Import_v1.md"

STATUS = "POST_ALPHA_WEYLPAIR_SOURCE_EMISSION_OR_HONEST_GALERKIN_C1_EXECUTION_VALUERUN_IMPORTED_PROMOTION_BLOCKED"
NEXT = "MTT_Selected_EnrichedWeylPairSourceProvenance_or_GalerkinC1Values_v1"


def load(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def main() -> None:
    prev = load(PREV)
    cert = load(SM_CERT)
    candidate = load(SM_CANDIDATE)
    conditional_run = load(CONDITIONAL_RUN)
    promotion_attempt = load(PROMOTION_ATTEMPT)
    honest_gate = load(HONEST_GATE)

    prev_ok = all(
        [
            prev["theorem"]["proved"] is True,
            prev["closure_claimed"] is False,
            prev["frontier_decision"]["frontier_is_weylpair_source_emission_or_honest_galerkin_value_run"] is True,
            prev["frontier_decision"]["next_required_artifact"]
            == "MTT_Selected_WeylPairSourceEmission_or_HonestGalerkinC1Execution_ValueRun_v1",
        ]
    )

    imported_ok = all(
        [
            cert["certificate"] == "MTT_Selected_WeylPairSourceEmission_or_HonestGalerkinC1Execution_ValueRun_v1",
            cert["theorem_proved"] is True,
            cert["closure_claimed"] is False,
            cert["SM_parity_dynamic_packet_closure_claimed"] is False,
            cert["no_knob_closure_claimed"] is False,
            cert["true_SM_equivalence_claimed"] is False,
            cert["observed_data_used"] is False,
            cert["target_fitting_used"] is False,
            cert["next_required_artifact"] == NEXT,
            all(cert["what_closes"].values()),
            all(cert["what_remains_open"].values()),
            candidate["theorem"]["name"] == "WeylPairSourceEmissionAttemptAndValueRunTheorem",
            candidate["theorem"]["proved"] is True,
            candidate["promotion_decision"]["enriched_weylpair_source_emission_promoted"] is False,
            candidate["promotion_decision"]["honest_Galerkin_C1_execution_promoted"] is False,
            candidate["promotion_decision"]["A_selected_promoted"] is False,
            candidate["promotion_decision"]["b_selected_promoted"] is False,
            candidate["promotion_decision"]["deltaTheta_C1_promoted"] is False,
            candidate["promotion_decision"]["SM_parity_dynamic_packet_closed"] is False,
        ]
    )

    conditional_ok = all(
        [
            conditional_run["schema"] == "MTTConditionalWeylPairValueRun.v1",
            conditional_run["status"] == "CONDITIONAL_VALUE_RUN_READY_NOT_PROMOTED",
            conditional_run["operator_name"] == "A_weylpair_conditional",
            conditional_run["operator_is_A_selected"] is False,
            conditional_run["operator_shape"] == [72, 2],
            conditional_run["rank"] == 2,
            abs(conditional_run["condition_number"] - 1.0) < 1e-12,
            conditional_run["relative_residual"] < 1e-12,
            conditional_run["A_transpose_A_if_promoted"] == [[12.0, 0.0], [0.0, 12.0]],
            conditional_run["A_transpose_b_if_promoted"] == [12.0, 12.0],
            conditional_run["deltaTheta_C1_if_promoted"] == [1.0, 1.0],
            conditional_run["SM_parity_dynamic_packet_would_close_if_promoted"] is True,
            conditional_run["no_knob_flavor_constants_would_close_if_promoted"] is False,
            conditional_run["selected_value_promotion_allowed_now"] is False,
            conditional_run["observed_data_used"] is False,
            conditional_run["target_fitting_used"] is False,
        ]
    )

    promotion_ok = all(
        [
            promotion_attempt["schema"] == "MTTWeylPairSourceEmissionPromotionAttempt.v1",
            promotion_attempt["status"] == "PROMOTION_BLOCKED_SOURCE_EMISSION_NOT_THEOREM_DERIVED",
            promotion_attempt["candidate_route"] == "B_enriched_weylpair_basis_transport_or_vertex_source",
            promotion_attempt["already_closed_support"]["target_in_weylpair_span"] is True,
            promotion_attempt["already_closed_support"]["conditional_A_rank"] == 2,
            promotion_attempt["already_closed_support"]["source_selector_promoted"] is True,
            promotion_attempt["promotion_inputs_missing"]["A_selected_currently_emitted"] is False,
            promotion_attempt["promotion_inputs_missing"]["b_selected_currently_emitted"] is False,
            promotion_attempt["promotion_inputs_missing"]["rank_test_now_computable_for_selected_A"] is False,
            promotion_attempt["promotion_inputs_missing"]["least_squares_now_computable_for_selected_A"] is False,
            promotion_attempt["promotion_decision"]["enriched_weylpair_source_emission_promoted"] is False,
            promotion_attempt["promotion_decision"]["A_selected_promoted"] is False,
            promotion_attempt["promotion_decision"]["b_selected_promoted"] is False,
            promotion_attempt["promotion_decision"]["deltaTheta_C1_promoted"] is False,
            promotion_attempt["promotion_decision"]["SM_parity_dynamic_packet_closed"] is False,
            promotion_attempt["observed_data_used"] is False,
            promotion_attempt["target_fitting_used"] is False,
        ]
    )

    honest_ok = all(
        [
            honest_gate["schema"] == "MTTHonestGalerkinC1ExecutionValueRunGate.v1",
            honest_gate["status"] == "HONEST_GALERKIN_EXECUTION_VALUES_STILL_OPEN",
            honest_gate["contract_status"] == "HONEST_GALERKIN_RUN_CONTRACT_EMITTED_VALUES_OPEN",
            honest_gate["current_manifest_status"] == "OPEN_C1_PRIMITIVE_CONTRACTIONS_MISSING",
            honest_gate["selected_source_verified"] is False,
            honest_gate["target_fitting_forbidden"] is True,
            honest_gate["observed_flavor_data_forbidden"] is True,
            honest_gate["would_close_SM_parity_dynamic_packet_if_values_emitted"] is True,
            honest_gate["would_close_no_knob_flavor_constants_if_values_emitted"] is False,
            "sector response matrices M_u, M_d, M_e, M_nuD emitted" in honest_gate["acceptance_checks"],
            "CP-odd invariant test" in honest_gate["acceptance_checks"],
        ]
    )

    missing_obligations_ok = all(
        obligation in promotion_attempt["promotion_inputs_missing"]["missing_source_obligations"]
        for obligation in conditional_run["blocked_by"][:6]
    )

    what_closes_now = {
        "differentiated_source_rule_ladder_consumed": prev_ok,
        "weylpair_source_emission_attempt_imported": imported_ok,
        "conditional_weylpair_value_run_replayed": conditional_ok,
        "promotion_blocker_identified": promotion_ok,
        "honest_galerkin_value_run_gate_reemitted": honest_ok,
        "missing_source_obligations_match_conditional_blockers": missing_obligations_ok,
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
        "name": "PostAlphaWeylPairSourceEmissionAttemptAndValueRunImport",
        "proved": all([all(what_closes_now.values()), all(what_remains_open.values()), all(guardrails.values())]),
        "closure_claimed": False,
        "statement": (
            "The enriched Weyl-pair conditional value run is numerically ready: a "
            "72-by-2 rank-2 conditional operator has unit condition number and "
            "solves deltaTheta=(1,1) with negligible residual. This does not promote "
            "A_selected, b_selected, or deltaTheta_C1 because same-branch Weyl-pair "
            "source emission and b_selected remain theorem-open."
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
            "what_closes_now": candidate["what_closes_now"],
            "what_remains_open": candidate["what_remains_open"],
        },
        "conditional_weylpair_value_run": conditional_run,
        "weylpair_source_emission_promotion_attempt": promotion_attempt,
        "honest_galerkin_execution_value_run_gate": honest_gate,
        "what_remains_open": what_remains_open,
        "frontier_decision": {
            "conditional_value_run_ready": True,
            "selected_value_promotion_blocked": True,
            "frontier_is_enriched_weylpair_source_provenance_or_galerkin_C1_values": True,
            "next_required_artifact": NEXT,
        },
        "guardrails": guardrails,
        "input_artifacts": {
            "previous_gate_certificate": str(PREV),
            "sm_gate_certificate": str(SM_CERT),
            "sm_gate_candidate": str(SM_CANDIDATE),
            "conditional_weylpair_value_run": str(CONDITIONAL_RUN),
            "weylpair_source_emission_promotion_attempt": str(PROMOTION_ATTEMPT),
            "honest_galerkin_execution_value_run_gate": str(HONEST_GATE),
        },
    }

    note = f"""# PostAlpha WeylPairSourceEmission or HonestGalerkinC1Execution ValueRun Import v1

## Result

The enriched Weyl-pair conditional value run is numerically ready but not
selected.

```text
operator shape      = 72 x 2
rank                = 2
condition number    = {conditional_run["condition_number"]}
relative residual   = {conditional_run["relative_residual"]}
A^T A if promoted   = [[12, 0], [0, 12]]
A^T b if promoted   = [12, 12]
deltaTheta if proven = [1, 1]
```

Promotion is blocked because source emission, `A_selected`, and `b_selected`
remain theorem-derived-value obligations, not emitted selected values.

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
        "certificate": "post_alpha_weylpair_source_emission_or_honest_galerkin_c1_execution_valuerun",
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
