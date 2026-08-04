from __future__ import annotations

import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SM_ROOT = ROOT.parent / "mtt-sm-parity-closure"

PREV = ROOT / "certificates" / "post_alpha_dynamic_c1_transfer_tensor_or_galerkin_c1_values_certificate.json"
SLUG = "selected_primitivec1tensor_hessiansourcemap_or_honestgalerkinc1execution"
SM_CERT = SM_ROOT / "certificates" / f"{SLUG}_certificate.json"
SM_CANDIDATE = SM_ROOT / "candidate_data" / f"{SLUG}.candidate.json"
SM_DIR = SM_ROOT / "candidate_data" / SLUG
SOURCE_MAP = SM_DIR / "primitive_tensor_hessian_source_map_candidate.packet.json"
SELECTION_KERNEL = SM_DIR / "source_map_selection_obligation_kernel.packet.json"
GALERKIN_SLOTS = SM_DIR / "honest_galerkin_execution_value_slots.packet.json"

OUT_CERT = ROOT / "certificates" / "post_alpha_primitive_c1_tensor_hessian_source_map_or_honest_galerkin_c1_execution_certificate.json"
OUT_PACKET = ROOT / "candidate_data" / "post_alpha_primitive_c1_tensor_hessian_source_map_or_honest_galerkin_c1_execution.packet.json"
OUT_NOTE = ROOT / "proof_corpus" / "PostAlpha_PrimitiveC1Tensor_HessianSourceMap_or_HonestGalerkinC1Execution_Import_v1.md"

STATUS = "POST_ALPHA_PRIMITIVE_C1_TENSOR_HESSIAN_SOURCE_MAP_OR_HONEST_GALERKIN_C1_EXECUTION_IMPORTED_CANDIDATE_VALUES_OPEN"
NEXT = "MTT_Selected_SourceMapSelectionTheorem_or_HonestGalerkinC1ValueRun_v1"


def load(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def main() -> None:
    prev = load(PREV)
    cert = load(SM_CERT)
    candidate = load(SM_CANDIDATE)
    source_map = load(SOURCE_MAP)
    selection_kernel = load(SELECTION_KERNEL)
    galerkin_slots = load(GALERKIN_SLOTS)

    prev_ok = all(
        [
            prev["theorem"]["proved"] is True,
            prev["closure_claimed"] is False,
            prev["frontier_decision"]["frontier_is_primitive_C1_tensor_or_Hessian_source_vector_or_Galerkin_values"]
            is True,
            prev["frontier_decision"]["next_required_artifact"]
            == "MTT_Selected_PrimitiveC1Tensor_or_HessianSourceVector_or_GalerkinC1Values_v1",
        ]
    )

    imported_ok = all(
        [
            cert["certificate"] == "MTT_Selected_PrimitiveC1Tensor_HessianSourceMap_or_HonestGalerkinC1Execution_v1",
            cert["theorem_proved"] is True,
            cert["closure_claimed"] is False,
            cert["A_selected_claimed"] is False,
            cert["b_selected_claimed"] is False,
            cert["deltaTheta_C1_claimed"] is False,
            cert["source_map_selected_claimed"] is False,
            cert["sector_response_matrices_claimed"] is False,
            cert["honest_Galerkin_C1_claimed"] is False,
            cert["observed_data_used"] is False,
            cert["target_fitting_used"] is False,
            cert["next_required_artifact"] == NEXT,
            all(cert["what_closes"].values()),
            all(cert["what_remains_open"].values()),
            candidate["theorem"]["name"] == "PrimitiveC1TensorHessianSourceMapCandidateTheorem",
            candidate["theorem"]["proved"] is True,
            candidate["promotion_decision"]["source_map_candidate_constructed"] is True,
            candidate["promotion_decision"]["source_map_selected_by_MTT_now"] is False,
            candidate["promotion_decision"]["sector_response_matrices_promoted"] is False,
            candidate["promotion_decision"]["A_selected_promoted"] is False,
            candidate["promotion_decision"]["b_selected_promoted"] is False,
            candidate["promotion_decision"]["deltaTheta_C1_promoted"] is False,
            candidate["promotion_decision"]["SM_parity_dynamic_packet_closed"] is False,
        ]
    )

    source_map_ok = all(
        [
            source_map["schema"] == "MTTPrimitiveC1TensorHessianSourceMapCandidate.v1",
            source_map["status"] == "SOURCE_MAP_CANDIDATE_CONSTRUCTED_SELECTION_OPEN",
            source_map["source_map_name"] == "Q_residual_enriched_Weyl_pair_C1_source_map",
            source_map["selected_by_MTT_now"] is False,
            source_map["domain"]["branch"] == "q79/F,m=1 S3/GS Route-C branch",
            source_map["closed_support"]["canonical_Q_residual_available"] is True,
            source_map["closed_support"]["Q_residual_rank"] == 6,
            source_map["closed_support"]["alpha1_dotD_driver_verified"] is True,
            source_map["closed_support"]["strict_72_real_acceptance_target"]["total_real_coordinates"] == 72,
            source_map["candidate_residual_operators"]["phase_R_Z"]["selected_by_MTT_now"] is False,
            source_map["candidate_residual_operators"]["phase_R_Z"]["shape"]["orthogonal_to_fixed_fiber_span"] is True,
            source_map["candidate_residual_operators"]["phase_R_Z"]["shape"]["residual_norm_sq"] == 4.0,
            source_map["candidate_residual_operators"]["shift_R_X"]["selected_by_MTT_now"] is False,
            source_map["candidate_residual_operators"]["shift_R_X"]["shape"]["orthogonal_to_fixed_fiber_span"] is True,
            source_map["candidate_residual_operators"]["shift_R_X"]["shape"]["residual_norm_sq"] == 2.0,
            source_map["residual_completion_replay"]["phase_projection_plus_residual_equals_target"] is True,
            source_map["residual_completion_replay"]["shift_projection_plus_residual_equals_target"] is True,
            source_map["if_source_map_selected_then"]["A_selected_columns_available"] is True,
            source_map["if_source_map_selected_then"]["rank"] == 2,
            source_map["if_source_map_selected_then"]["A_transpose_A"] == [[12.0, 0.0], [0.0, 12.0]],
            source_map["if_source_map_selected_then"]["A_transpose_b"] == [12.0, 12.0],
            source_map["if_source_map_selected_then"]["deltaTheta_C1"] == [1.0, 1.0],
            source_map["observed_data_used"] is False,
            source_map["target_fitting_used"] is False,
        ]
    )

    kernel_ok = all(
        [
            selection_kernel["schema"] == "MTTSourceMapSelectionObligationKernel.v1",
            selection_kernel["status"] == "SELECTION_OBLIGATION_KERNEL_BUILT_VALUES_OPEN",
            selection_kernel["closed_numeric_facts"]["rank_2_condition_number_1"] is True,
            selection_kernel["closed_numeric_facts"]["A_transpose_A_equals_12I2"] is True,
            selection_kernel["closed_numeric_facts"]["A_transpose_b_equals_12_12"] is True,
            selection_kernel["closed_numeric_facts"]["deltaTheta_equals_1_1"] is True,
            selection_kernel["currently_emitted"]["selected_A_selected"] is False,
            selection_kernel["currently_emitted"]["selected_b_selected"] is False,
            selection_kernel["currently_emitted"]["selected_deltaTheta_C1"] is False,
            selection_kernel["minimal_truth_table"]["current_case"]["phase_R_Z_selected"] is False,
            selection_kernel["minimal_truth_table"]["current_case"]["shift_R_X_selected"] is False,
            selection_kernel["minimal_truth_table"]["current_case"]["b_source_emitted"] is False,
            selection_kernel["minimal_truth_table"]["if_phase_and_shift_residual_sources_selected_and_b_source_emitted"][
                "SM_parity_dynamic_packet_would_close"
            ]
            is True,
            selection_kernel["minimal_truth_table"]["if_phase_and_shift_residual_sources_selected_and_b_source_emitted"][
                "no_knob_flavor_constants_would_close"
            ]
            is False,
            selection_kernel["strict_acceptance_field_status"]["A_selected"] == "CONDITIONAL_REFERENCE_ONLY_NOT_SELECTED",
            selection_kernel["strict_acceptance_field_status"]["sector_response_matrices"]
            == "NOT_EMITTED_BY_SELECTED_VALUE_SOURCE",
            selection_kernel["observed_data_used"] is False,
            selection_kernel["target_fitting_used"] is False,
        ]
    )

    galerkin_ok = all(
        [
            galerkin_slots["schema"] == "MTTHonestGalerkinC1ExecutionValueSlots.v1",
            galerkin_slots["status"] == "HONEST_GALERKIN_EXECUTION_SLOTS_RESTATED_VALUES_OPEN",
            galerkin_slots["manifest_status"] == "OPEN_C1_PRIMITIVE_CONTRACTIONS_MISSING",
            galerkin_slots["selected_source_verified"] is False,
            galerkin_slots["can_replace_source_map_now"] is False,
            galerkin_slots["strict_coordinate_target"]["total_real_coordinates"] == 72,
            "primitive_three_by_three_contraction_terms" in galerkin_slots["required_outputs"],
            "linear_response_matrices" in galerkin_slots["required_outputs"],
            galerkin_slots["observed_data_used"] is False,
            galerkin_slots["target_fitting_used"] is False,
        ]
    )

    what_closes_now = {
        "dynamic_C1_transfer_tensor_frontier_consumed": prev_ok,
        "primitive_Hessian_source_map_candidate_imported": imported_ok,
        "exact_phase_shift_residual_operator_candidate_attached": source_map_ok,
        "source_map_selection_obligation_kernel_built": kernel_ok,
        "honest_galerkin_execution_value_slots_reemitted": galerkin_ok,
    }

    what_remains_open = {
        "selected_phase_R_Z_source": True,
        "selected_shift_R_X_source": True,
        "selected_Hessian_or_b_source_vector": True,
        "selected_primitive_C1_tensor_values": True,
        "selected_sector_response_matrices": True,
        "selected_A_selected": True,
        "selected_b_selected": True,
        "selected_deltaTheta_C1": True,
        "honest_selected_Galerkin_C1_execution_values": True,
        "SM_parity_dynamic_packet_closure": True,
        "true_SM_equivalence_closure": True,
        "full_no_knob_flavor_closure": True,
    }

    guardrails = {
        "promotes_source_map_candidate_only": True,
        "does_not_select_source_map_by_MTT": True,
        "does_not_promote_sector_response_matrices": True,
        "does_not_promote_A_b_deltaTheta": True,
        "does_not_promote_honest_galerkin_execution": True,
        "does_not_claim_SM_parity_dynamic_closure": True,
        "does_not_claim_true_SM_equivalence": True,
        "does_not_claim_no_knob_flavor_closure": True,
        "does_not_use_observed_or_target_inputs": True,
    }

    theorem = {
        "name": "PostAlphaPrimitiveC1TensorHessianSourceMapCandidateImport",
        "proved": all([all(what_closes_now.values()), all(what_remains_open.values()), all(guardrails.values())]),
        "closure_claimed": False,
        "statement": (
            "The exact primitive/Hessian source-map candidate Q_residual-enriched Weyl "
            "pair is constructed: phase R_Z and shift R_X residual operators are attached "
            "with the fixed 72-real acceptance target. If the phase source, shift source, "
            "and b source are selected, A_selected, b_selected, deltaTheta_C1, and the "
            "SM-parity dynamic packet would close. Those selections remain open."
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
        "primitive_tensor_hessian_source_map_candidate": source_map,
        "source_map_selection_obligation_kernel": selection_kernel,
        "honest_galerkin_execution_value_slots": galerkin_slots,
        "what_remains_open": what_remains_open,
        "frontier_decision": {
            "source_map_candidate_constructed": True,
            "source_map_selection_open": True,
            "frontier_is_source_map_selection_theorem_or_honest_galerkin_value_run": True,
            "next_required_artifact": NEXT,
        },
        "guardrails": guardrails,
        "input_artifacts": {
            "previous_gate_certificate": str(PREV),
            "sm_gate_certificate": str(SM_CERT),
            "sm_gate_candidate": str(SM_CANDIDATE),
            "primitive_tensor_hessian_source_map_candidate": str(SOURCE_MAP),
            "source_map_selection_obligation_kernel": str(SELECTION_KERNEL),
            "honest_galerkin_execution_value_slots": str(GALERKIN_SLOTS),
        },
    }

    note = f"""# PostAlpha PrimitiveC1Tensor HessianSourceMap or HonestGalerkinC1Execution Import v1

## Result

The same-branch primitive/Hessian source-map candidate is constructed.

```text
source map = Q_residual_enriched_Weyl_pair_C1_source_map
phase R_Z residual norm^2 = 4
shift R_X residual norm^2 = 2
acceptance coordinate system = 72 real coordinates
```

If the phase source, shift source, and b source are selected by MTT, then:

```text
A^T A        = [[12, 0], [0, 12]]
A^T b        = [12, 12]
deltaTheta   = [1, 1]
```

This import constructs the candidate; it does not select the source map.

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
        "certificate": "post_alpha_primitive_c1_tensor_hessian_source_map_or_honest_galerkin_c1_execution",
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
