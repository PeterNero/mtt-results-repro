from __future__ import annotations

import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]

PREV = ROOT / "certificates" / "post_alpha_independent_source_map_selection_theorem_or_honest_galerkin_c1_value_run_certificate.json"
SOURCE_CERT = ROOT / "certificates" / "post_alpha_differentiated_phifinc1_residual_projector_axiom_or_galerkin_c1_execution_certificate.json"

OUT_CERT = ROOT / "certificates" / "post_alpha_independent_differentiated_phifinc1_residual_projector_axiom_or_galerkin_c1_execution_certificate.json"
OUT_PACKET = ROOT / "candidate_data" / "post_alpha_independent_differentiated_phifinc1_residual_projector_axiom_or_galerkin_c1_execution.packet.json"
OUT_NOTE = ROOT / "proof_corpus" / "PostAlpha_IndependentDifferentiatedPhiFinC1ResidualProjectorAxiom_or_GalerkinC1Execution_Import_v1.md"

STATUS = "POST_ALPHA_INDEPENDENT_DIFFERENTIATED_PHIFINC1_RESIDUAL_PROJECTOR_AXIOM_OR_GALERKIN_C1_EXECUTION_IMPORTED_CONTRACT_OPEN"
SOURCE_STATUS = "POST_ALPHA_DIFFERENTIATED_PHIFINC1_RESIDUAL_PROJECTOR_AXIOM_OR_GALERKIN_C1_EXECUTION_IMPORTED_CONTRACT_OPEN"
THIS_ARTIFACT = "MTT_Selected_DifferentiatedPhiFinC1ResidualProjectorAxiom_or_GalerkinC1Execution_v1"
NEXT = "MTT_Selected_ResidualProjectorAxiomInsertion_or_GalerkinC1FirstExecution_v1"


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
            prev["frontier_decision"]["source_map_selection_test_built"] is True,
            prev["frontier_decision"]["if_selected_closure_exact"] is True,
            prev["frontier_decision"]["frontier_is_differentiated_PhiFinC1_residual_projector_axiom_or_Galerkin_execution"]
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
            source["frontier_decision"]["two_lane_closure_implication_proved"] is True,
            source["frontier_decision"]["residual_projector_axiom_contract_ready_not_inserted"] is True,
            source["frontier_decision"]["honest_galerkin_contract_ready_values_missing"] is True,
            source["frontier_decision"]["frontier_is_residual_projector_axiom_insertion_or_galerkin_first_execution"]
            is True,
            source["frontier_decision"]["next_required_artifact"] == NEXT,
            all(source["what_closes_now"].values()),
            all(source["what_remains_open"].values()),
            all(source["guardrails"].values()),
        ]
    )

    implication = source_packet["closure_implication_replay"]
    axiom = source_packet["residual_projector_axiom_patch_contract"]
    galerkin = source_packet["honest_galerkin_execution_acceptance_contract"]

    implication_ok = all(
        [
            implication["schema"] == "MTTDynamicPacketClosureImplicationReplay.v1",
            implication["status"] == "IMPLICATION_PROVED_ANTECEDENT_OPEN",
            implication["proved_now"] is True,
            implication["antecedent_currently_met"] is False,
            implication["current_numeric_replay_if_axiom_accepted"]["rank"] == 2,
            implication["current_numeric_replay_if_axiom_accepted"]["A_transpose_A"] == [[12.0, 0.0], [0.0, 12.0]],
            implication["current_numeric_replay_if_axiom_accepted"]["A_transpose_b"] == [12.0, 12.0],
            implication["current_numeric_replay_if_axiom_accepted"]["deltaTheta_C1"] == [1.0, 1.0],
            implication["if_axiom_contract_accepted_then"]["SM_parity_dynamic_packet_would_close"] is True,
            implication["if_axiom_contract_accepted_then"]["no_knob_flavor_constants_would_close"] is False,
            implication["if_honest_galerkin_contract_filled_then"]["SM_parity_dynamic_packet_would_close"] is True,
            implication["if_honest_galerkin_contract_filled_then"]["no_knob_flavor_constants_would_close_by_default"]
            is False,
            implication["observed_data_used"] is False,
            implication["target_fitting_used"] is False,
        ]
    )

    axiom_ok = all(
        [
            axiom["schema"] == "MTTDifferentiatedPhiFinC1ResidualProjectorAxiomContract.v1",
            axiom["status"] == "AXIOM_CONTRACT_READY_NOT_INSERTED",
            axiom["axiom_name"] == "DifferentiatedPhiFinC1ResidualProjectorAxiom",
            axiom["selected_now"] is False,
            axiom["inserted_now"] is False,
            axiom["premises_required"]["canonical_Q_residual_available"] is True,
            axiom["premises_required"]["alpha1_dotD_driver_verified"] is True,
            axiom["premises_required"]["selected_qutrit_weyl_carrier"] is True,
            axiom["premises_required"]["selected_static_route_Z_clock_to_u_e"] is True,
            axiom["premises_required"]["selected_static_route_X_shift_to_d_nuD"] is True,
            axiom["new_axiom_payload_if_accepted"]["selected_differentiated_PhiFinC1_applies_Q_residual"] is True,
            axiom["new_axiom_payload_if_accepted"]["phase_R_Z_selected"] is True,
            axiom["new_axiom_payload_if_accepted"]["shift_R_X_selected"] is True,
            axiom["new_axiom_payload_if_accepted"]["b_source_emitted"] is True,
            axiom["exact_source_values_to_emit"]["phase_R_Z"]["residual_norm_sq"] == 4.0,
            axiom["exact_source_values_to_emit"]["shift_R_X"]["residual_norm_sq"] == 2.0,
            axiom["exact_source_values_to_emit"]["routed_total_residual_norm_sq"] == 12.0,
            axiom["exact_source_values_to_emit"]["conditional_b_norm_sq"] == 24.0,
            "same-branch proof or explicit corpus axiom insertion exists" in axiom["acceptance_tests"],
            "b_selected is emitted by the same source rule or Hessian source vector" in axiom["acceptance_tests"],
            axiom["observed_data_used"] is False,
            axiom["target_fitting_used"] is False,
        ]
    )

    galerkin_ok = all(
        [
            galerkin["schema"] == "MTTHonestGalerkinC1ExecutionAcceptanceContract.v1",
            galerkin["status"] == "GALERKIN_EXECUTION_CONTRACT_READY_VALUES_MISSING",
            galerkin["would_close_SM_parity_dynamic_packet_if_accepted"] is True,
            galerkin["would_close_no_knob_flavor_constants_by_itself"] is False,
            galerkin["strict_coordinate_target"]["total_real_coordinates"] == 72,
            galerkin["current_values_available"]["selected_source_verified"] is False,
            galerkin["current_values_available"]["sector_response_matrices_emitted"] is False,
            galerkin["current_values_available"]["A_selected_emitted"] is False,
            galerkin["current_values_available"]["b_selected_emitted"] is False,
            galerkin["current_values_available"]["can_replace_source_map_now"] is False,
            galerkin["acceptance_tests"]["selected_source_verified"] is True,
            galerkin["acceptance_tests"]["primitive_contractions_are_computed_not_benchmarked"] is True,
            "deltaTheta_C1 solve certificate" in galerkin["minimal_required_outputs"],
            galerkin["observed_data_used"] is False,
            galerkin["target_fitting_used"] is False,
        ]
    )

    what_closes_now = {
        "long_name_source_map_selection_boundary_consumed": prev_ok,
        "audited_two_lane_dynamic_closure_implication_reanchored": source_ok,
        "closure_implication_replay_proved": implication_ok,
        "residual_projector_axiom_contract_built_not_inserted": axiom_ok,
        "honest_galerkin_execution_acceptance_contract_built": galerkin_ok,
    }

    what_remains_open = {
        "derive_or_insert_residual_projector_axiom": True,
        "prove_selected_differentiated_PhiFinC1_application_rule": True,
        "run_honest_selected_Galerkin_C1_execution": True,
        "emit_sector_response_matrices": True,
        "emit_selected_b_source_vector": True,
        "promote_A_selected": True,
        "promote_b_selected": True,
        "promote_deltaTheta_C1": True,
        "SM_parity_dynamic_packet_closure": True,
        "true_SM_equivalence_closure": True,
        "full_no_knob_flavor_closure": True,
    }

    guardrails = {
        "does_not_insert_residual_projector_axiom": True,
        "does_not_claim_differentiated_PhiFinC1_application_rule": True,
        "does_not_run_honest_galerkin_execution": True,
        "does_not_promote_sector_response_matrices": True,
        "does_not_promote_A_b_deltaTheta": True,
        "does_not_claim_SM_parity_dynamic_closure": True,
        "does_not_claim_true_SM_equivalence": True,
        "does_not_claim_no_knob_flavor_closure": True,
        "does_not_use_observed_or_target_inputs": True,
    }

    theorem = {
        "name": "PostAlphaIndependentTwoLaneDynamicClosureImplicationImport",
        "proved": all([all(what_closes_now.values()), all(what_remains_open.values()), all(guardrails.values())]),
        "closure_claimed": False,
        "statement": (
            "The independent long-name branch imports the two-lane dynamic closure "
            "implication. The residual-projector axiom contract and honest Galerkin "
            "execution contract share the strict 72-real target and would close the "
            "rank-2 C1 dynamic packet if accepted/filled. No axiom insertion, "
            "Galerkin execution, sector matrix promotion, or A/b/deltaTheta promotion "
            "is claimed."
        ),
    }

    packet = {
        "theorem": theorem,
        "status": STATUS,
        "what_closes_now": what_closes_now,
        "source_two_lane_certificate": source,
        "closure_implication_replay": implication,
        "residual_projector_axiom_patch_contract": axiom,
        "honest_galerkin_execution_acceptance_contract": galerkin,
        "what_remains_open": what_remains_open,
        "frontier_decision": {
            "two_lane_closure_implication_proved": True,
            "residual_projector_axiom_contract_ready_not_inserted": True,
            "honest_galerkin_contract_ready_values_missing": True,
            "frontier_is_residual_projector_axiom_insertion_or_galerkin_first_execution": True,
            "next_required_artifact": NEXT,
        },
        "guardrails": guardrails,
        "input_artifacts": {
            "previous_long_name_certificate": str(PREV),
            "source_two_lane_certificate": str(SOURCE_CERT),
            "source_two_lane_packet": source["packet_written"],
        },
    }

    note = f"""# PostAlpha Independent DifferentiatedPhiFinC1ResidualProjectorAxiom or GalerkinC1Execution Import v1

## Result

The independent long-name branch now carries the two-lane dynamic closure implication.

```text
Lane A = DifferentiatedPhiFinC1ResidualProjectorAxiom
Lane B = honest selected Galerkin C1 execution
target = fixed 72-real C1 coordinate system
```

If either lane emits selected `A_selected` and `b_selected`, then:

```text
A^T A       = [[12, 0], [0, 12]]
A^T b       = [12, 12]
deltaTheta  = [1, 1]
```

Current status: axiom not inserted, Galerkin values missing.

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
        "certificate": "post_alpha_independent_differentiated_phifinc1_residual_projector_axiom_or_galerkin_c1_execution",
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
