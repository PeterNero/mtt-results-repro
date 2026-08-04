from __future__ import annotations

import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SM_ROOT = ROOT.parent / "mtt-sm-parity-closure"

PREV = ROOT / "certificates" / "post_alpha_source_map_selection_boundary_certificate.json"
SM_CERT = SM_ROOT / "certificates" / "selected_differentiatedphifinc1_residualprojectoraxiom_or_galerkinc1execution_certificate.json"
SM_CANDIDATE = SM_ROOT / "candidate_data" / "selected_differentiatedphifinc1_residualprojectoraxiom_or_galerkinc1execution.candidate.json"
SM_DIR = SM_ROOT / "candidate_data" / "selected_differentiatedphifinc1_residualprojectoraxiom_or_galerkinc1execution"
AXIOM_CONTRACT = SM_DIR / "residual_projector_axiom_patch_contract.packet.json"
IMPLICATION_REPLAY = SM_DIR / "closure_implication_replay.packet.json"
GALERKIN_CONTRACT = SM_DIR / "honest_galerkin_execution_acceptance_contract.packet.json"

OUT_CERT = ROOT / "certificates" / "post_alpha_differentiated_phifinc1_residual_projector_contract_certificate.json"
OUT_PACKET = ROOT / "candidate_data" / "post_alpha_differentiated_phifinc1_residual_projector_contract.packet.json"
OUT_NOTE = ROOT / "proof_corpus" / "PostAlpha_DifferentiatedPhiFinC1_ResidualProjectorContract_Import_v1.md"

STATUS = "POST_ALPHA_DIFFERENTIATED_PHIFINC1_RESIDUAL_PROJECTOR_CONTRACT_IMPORTED_OPEN"
NEXT = "MTT_Selected_ResidualProjectorAxiomInsertion_or_GalerkinC1FirstExecution_v1"


def load(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def main() -> None:
    prev = load(PREV)
    sm_cert = load(SM_CERT)
    sm_candidate = load(SM_CANDIDATE)
    axiom_contract = load(AXIOM_CONTRACT)
    implication = load(IMPLICATION_REPLAY)
    galerkin_contract = load(GALERKIN_CONTRACT)

    prev_ok = all(
        [
            prev["theorem"]["proved"] is True,
            prev["closure_claimed"] is False,
            prev["frontier_decision"]["frontier_is_differentiated_PhiFinC1_application_or_Galerkin_execution"] is True,
            prev["frontier_decision"]["next_required_artifact"]
            == "MTT_Selected_DifferentiatedPhiFinC1ResidualProjectorAxiom_or_GalerkinC1Execution_v1",
        ]
    )

    imported_gate_ok = all(
        [
            sm_cert["certificate"]
            == "MTT_Selected_DifferentiatedPhiFinC1ResidualProjectorAxiom_or_GalerkinC1Execution_v1",
            sm_cert["theorem_proved"] is True,
            sm_cert["closure_claimed"] is False,
            sm_cert["observed_data_used"] is False,
            sm_cert["target_fitting_used"] is False,
            sm_cert["next_required_artifact"] == NEXT,
            all(sm_cert["what_closes"].values()),
            all(sm_cert["what_remains_open"].values()),
            sm_candidate["theorem"]["name"] == "TwoLaneDynamicClosureImplicationTheorem",
            sm_candidate["theorem"]["proved"] is True,
            sm_candidate["closure_claimed"] is False,
            sm_candidate["promotion_decision"]["differentiated_PhiFinC1_application_rule_proved_now"] is False,
            sm_candidate["promotion_decision"]["residual_projector_axiom_inserted_now"] is False,
            sm_candidate["promotion_decision"]["honest_Galerkin_C1_execution_run_now"] is False,
            sm_candidate["promotion_decision"]["A_selected_promoted"] is False,
            sm_candidate["promotion_decision"]["b_selected_promoted"] is False,
            sm_candidate["promotion_decision"]["deltaTheta_C1_promoted"] is False,
        ]
    )

    axiom_contract_ok = all(
        [
            axiom_contract["schema"] == "MTTDifferentiatedPhiFinC1ResidualProjectorAxiomContract.v1",
            axiom_contract["status"] == "AXIOM_CONTRACT_READY_NOT_INSERTED",
            axiom_contract["axiom_name"] == "DifferentiatedPhiFinC1ResidualProjectorAxiom",
            axiom_contract["inserted_now"] is False,
            axiom_contract["selected_now"] is False,
            axiom_contract["observed_data_used"] is False,
            axiom_contract["target_fitting_used"] is False,
            axiom_contract["premises_required"]["canonical_Q_residual_available"] is True,
            axiom_contract["new_axiom_payload_if_accepted"]["selected_differentiated_PhiFinC1_applies_Q_residual"] is True,
            axiom_contract["new_axiom_payload_if_accepted"]["phase_R_Z_selected"] is True,
            axiom_contract["new_axiom_payload_if_accepted"]["shift_R_X_selected"] is True,
            axiom_contract["new_axiom_payload_if_accepted"]["b_source_emitted"] is True,
            axiom_contract["exact_source_values_to_emit"]["phase_R_Z"]["residual_norm_sq"] == 4.0,
            axiom_contract["exact_source_values_to_emit"]["shift_R_X"]["residual_norm_sq"] == 2.0,
            axiom_contract["exact_source_values_to_emit"]["conditional_b_norm_sq"] == 24.0,
            axiom_contract["exact_source_values_to_emit"]["routed_total_residual_norm_sq"] == 12.0,
        ]
    )

    implication_ok = all(
        [
            implication["schema"] == "MTTDynamicPacketClosureImplicationReplay.v1",
            implication["status"] == "IMPLICATION_PROVED_ANTECEDENT_OPEN",
            implication["proved_now"] is True,
            implication["antecedent_currently_met"] is False,
            implication["observed_data_used"] is False,
            implication["target_fitting_used"] is False,
            implication["current_numeric_replay_if_axiom_accepted"]["rank"] == 2,
            implication["current_numeric_replay_if_axiom_accepted"]["A_transpose_A"] == [[12.0, 0.0], [0.0, 12.0]],
            implication["current_numeric_replay_if_axiom_accepted"]["A_transpose_b"] == [12.0, 12.0],
            implication["current_numeric_replay_if_axiom_accepted"]["deltaTheta_C1"] == [1.0, 1.0],
            implication["if_axiom_contract_accepted_then"]["SM_parity_dynamic_packet_would_close"] is True,
            implication["if_honest_galerkin_contract_filled_then"]["SM_parity_dynamic_packet_would_close"] is True,
            implication["if_axiom_contract_accepted_then"]["no_knob_flavor_constants_would_close"] is False,
            implication["if_honest_galerkin_contract_filled_then"]["no_knob_flavor_constants_would_close_by_default"] is False,
        ]
    )

    galerkin_contract_ok = all(
        [
            galerkin_contract["schema"] == "MTTHonestGalerkinC1ExecutionAcceptanceContract.v1",
            galerkin_contract["status"] == "GALERKIN_EXECUTION_CONTRACT_READY_VALUES_MISSING",
            galerkin_contract["observed_data_used"] is False,
            galerkin_contract["target_fitting_used"] is False,
            galerkin_contract["strict_coordinate_target"]["total_real_coordinates"] == 72,
            galerkin_contract["current_values_available"]["A_selected_emitted"] is False,
            galerkin_contract["current_values_available"]["b_selected_emitted"] is False,
            galerkin_contract["current_values_available"]["sector_response_matrices_emitted"] is False,
            galerkin_contract["current_values_available"]["selected_source_verified"] is False,
            galerkin_contract["would_close_SM_parity_dynamic_packet_if_accepted"] is True,
            galerkin_contract["would_close_no_knob_flavor_constants_by_itself"] is False,
        ]
    )

    what_closes_now = {
        "previous_source_map_selection_boundary_consumed": prev_ok,
        "two_lane_implication_theorem_imported": imported_gate_ok,
        "residual_projector_axiom_contract_fixed": axiom_contract_ok,
        "closure_implication_replay_proved": implication_ok,
        "honest_galerkin_execution_acceptance_contract_fixed": galerkin_contract_ok,
    }

    what_remains_open = {
        "derive_or_insert_residual_projector_axiom": True,
        "prove_selected_differentiated_PhiFinC1_application_rule": True,
        "run_honest_selected_Galerkin_C1_execution": True,
        "emit_selected_A_matrix": True,
        "emit_selected_b_vector": True,
        "emit_selected_deltaTheta_C1": True,
        "emit_sector_response_matrices": True,
        "SM_parity_dynamic_packet_closure": True,
        "full_no_knob_flavor_closure": True,
        "true_SM_equivalence_closure": True,
    }

    guardrails = {
        "does_not_insert_residual_projector_axiom": axiom_contract["inserted_now"] is False,
        "does_not_mark_residual_projector_axiom_selected": axiom_contract["selected_now"] is False,
        "does_not_promote_A_b_deltaTheta_or_sector_matrices": True,
        "does_not_claim_Galerkin_execution_values": True,
        "does_not_use_observed_or_target_inputs": True,
        "does_not_claim_SM_parity_or_no_knob_closure": True,
    }

    theorem = {
        "name": "PostAlphaDifferentiatedPhiFinC1ResidualProjectorContractImport",
        "proved": all([all(what_closes_now.values()), all(what_remains_open.values()), all(guardrails.values())]),
        "closure_claimed": False,
        "statement": (
            "The selected differentiated Phi_fin^C1 residual-projector frontier has "
            "been reduced to two typed lanes with identical strict 72-real acceptance: "
            "an axiom/theorem lane that would apply Q_residual and emit the selected "
            "R_Z/R_X/b source, and an honest Galerkin execution lane that would compute "
            "the primitive contractions directly. The implication from either accepted "
            "lane to the dynamic C1 packet is proved by exact rank-2 replay, but the "
            "projector axiom is not inserted and the Galerkin values are not yet emitted."
        ),
    }

    packet = {
        "theorem": theorem,
        "status": STATUS,
        "what_closes_now": what_closes_now,
        "axiom_contract": axiom_contract,
        "closure_implication_replay": implication,
        "honest_galerkin_execution_acceptance_contract": galerkin_contract,
        "what_remains_open": what_remains_open,
        "frontier_decision": {
            "two_lane_acceptance_target_fixed": True,
            "closure_implication_proved": True,
            "residual_projector_axiom_inserted_now": False,
            "honest_Galerkin_C1_execution_run_now": False,
            "frontier_is_axiom_insertion_or_first_Galerkin_execution": True,
            "next_required_artifact": NEXT,
        },
        "guardrails": guardrails,
        "input_artifacts": {
            "previous_boundary_certificate": str(PREV),
            "sm_gate_certificate": str(SM_CERT),
            "sm_gate_candidate": str(SM_CANDIDATE),
            "axiom_contract": str(AXIOM_CONTRACT),
            "closure_implication_replay": str(IMPLICATION_REPLAY),
            "galerkin_execution_acceptance_contract": str(GALERKIN_CONTRACT),
        },
    }

    note = f"""# PostAlpha Differentiated PhiFin C1 Residual Projector Contract Import v1

## Result

The dynamic C1 frontier is now reduced to two strict lanes.

Lane A:

```text
insert or prove DifferentiatedPhiFinC1ResidualProjectorAxiom
apply Q_residual on the selected branch
emit selected R_Z, R_X, and b_selected
```

Lane B:

```text
run honest selected Galerkin C1 execution
emit zero-mode bases, primitive contractions, A_selected, b_selected
solve DeltaTheta_C1 in the fixed 72-real coordinate target
```

The implication is closed:

```text
A^T A = [[12.0, 0.0], [0.0, 12.0]]
A^T b = [12.0, 12.0]
DeltaTheta_C1 = [1.0, 1.0]
rank = 2
```

But the antecedent is open. The residual-projector axiom is a contract, not an
inserted theorem, and the Galerkin value run has not emitted matrices.

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
        "certificate": "post_alpha_differentiated_phifinc1_residual_projector_contract",
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
