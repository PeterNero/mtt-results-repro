from __future__ import annotations

import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]

PREV = ROOT / "certificates" / "post_alpha_independent_dynamic_c1_transfer_tensor_or_galerkin_c1_values_certificate.json"
SOURCE_CERT = ROOT / "certificates" / "post_alpha_primitive_c1_tensor_hessian_source_map_or_honest_galerkin_c1_execution_certificate.json"

OUT_CERT = ROOT / "certificates" / "post_alpha_independent_primitive_c1_tensor_hessian_source_map_or_honest_galerkin_c1_execution_certificate.json"
OUT_PACKET = ROOT / "candidate_data" / "post_alpha_independent_primitive_c1_tensor_hessian_source_map_or_honest_galerkin_c1_execution.packet.json"
OUT_NOTE = ROOT / "proof_corpus" / "PostAlpha_IndependentPrimitiveC1Tensor_HessianSourceMap_or_HonestGalerkinC1Execution_Import_v1.md"

STATUS = "POST_ALPHA_INDEPENDENT_PRIMITIVE_C1_TENSOR_HESSIAN_SOURCE_MAP_OR_HONEST_GALERKIN_C1_EXECUTION_IMPORTED_CANDIDATE_VALUES_OPEN"
SOURCE_STATUS = "POST_ALPHA_PRIMITIVE_C1_TENSOR_HESSIAN_SOURCE_MAP_OR_HONEST_GALERKIN_C1_EXECUTION_IMPORTED_CANDIDATE_VALUES_OPEN"
THIS_ARTIFACT = "MTT_Selected_PrimitiveC1Tensor_or_HessianSourceVector_or_GalerkinC1Values_v1"
NEXT = "MTT_Selected_SourceMapSelectionTheorem_or_HonestGalerkinC1ValueRun_v1"


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
            prev["frontier_decision"]["operator_alpha1_support_closed_for_frontier"] is True,
            prev["frontier_decision"]["conditional_dynamic_C1_transfer_tensor_built_not_selected"] is True,
            prev["frontier_decision"]["frontier_is_primitive_C1_tensor_or_Hessian_source_vector_or_Galerkin_values"]
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
            source["frontier_decision"]["source_map_candidate_constructed"] is True,
            source["frontier_decision"]["source_map_selection_open"] is True,
            source["frontier_decision"]["frontier_is_source_map_selection_theorem_or_honest_galerkin_value_run"]
            is True,
            source["frontier_decision"]["next_required_artifact"] == NEXT,
            all(source["what_closes_now"].values()),
            all(source["what_remains_open"].values()),
            all(source["guardrails"].values()),
        ]
    )

    source_map = source_packet["primitive_tensor_hessian_source_map_candidate"]
    kernel = source_packet["source_map_selection_obligation_kernel"]
    galerkin = source_packet["honest_galerkin_execution_value_slots"]

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
            kernel["schema"] == "MTTSourceMapSelectionObligationKernel.v1",
            kernel["status"] == "SELECTION_OBLIGATION_KERNEL_BUILT_VALUES_OPEN",
            kernel["closed_numeric_facts"]["rank_2_condition_number_1"] is True,
            kernel["closed_numeric_facts"]["A_transpose_A_equals_12I2"] is True,
            kernel["closed_numeric_facts"]["A_transpose_b_equals_12_12"] is True,
            kernel["closed_numeric_facts"]["deltaTheta_equals_1_1"] is True,
            kernel["currently_emitted"]["selected_A_selected"] is False,
            kernel["currently_emitted"]["selected_b_selected"] is False,
            kernel["currently_emitted"]["selected_deltaTheta_C1"] is False,
            kernel["minimal_truth_table"]["current_case"]["phase_R_Z_selected"] is False,
            kernel["minimal_truth_table"]["current_case"]["shift_R_X_selected"] is False,
            kernel["minimal_truth_table"]["current_case"]["b_source_emitted"] is False,
            kernel["minimal_truth_table"]["if_phase_and_shift_residual_sources_selected_and_b_source_emitted"][
                "SM_parity_dynamic_packet_would_close"
            ]
            is True,
            kernel["minimal_truth_table"]["if_phase_and_shift_residual_sources_selected_and_b_source_emitted"][
                "no_knob_flavor_constants_would_close"
            ]
            is False,
            kernel["strict_acceptance_field_status"]["A_selected"] == "CONDITIONAL_REFERENCE_ONLY_NOT_SELECTED",
            kernel["strict_acceptance_field_status"]["sector_response_matrices"]
            == "NOT_EMITTED_BY_SELECTED_VALUE_SOURCE",
            kernel["observed_data_used"] is False,
            kernel["target_fitting_used"] is False,
        ]
    )

    galerkin_ok = all(
        [
            galerkin["schema"] == "MTTHonestGalerkinC1ExecutionValueSlots.v1",
            galerkin["status"] == "HONEST_GALERKIN_EXECUTION_SLOTS_RESTATED_VALUES_OPEN",
            galerkin["manifest_status"] == "OPEN_C1_PRIMITIVE_CONTRACTIONS_MISSING",
            galerkin["selected_source_verified"] is False,
            galerkin["can_replace_source_map_now"] is False,
            galerkin["strict_coordinate_target"]["total_real_coordinates"] == 72,
            "primitive_three_by_three_contraction_terms" in galerkin["required_outputs"],
            "linear_response_matrices" in galerkin["required_outputs"],
            galerkin["observed_data_used"] is False,
            galerkin["target_fitting_used"] is False,
        ]
    )

    what_closes_now = {
        "long_name_dynamic_C1_frontier_gate_consumed": prev_ok,
        "audited_primitive_Hessian_source_map_candidate_reanchored": source_ok,
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
        "name": "PostAlphaIndependentPrimitiveC1TensorHessianSourceMapCandidateImport",
        "proved": all([all(what_closes_now.values()), all(what_remains_open.values()), all(guardrails.values())]),
        "closure_claimed": False,
        "statement": (
            "The independent long-name branch imports the primitive/Hessian "
            "source-map candidate Q_residual-enriched Weyl pair. Phase R_Z and "
            "shift R_X residual operators are attached to the 72-real acceptance "
            "target and the selection-obligation kernel records the conditional "
            "rank-2 closure. The source map, b source, response matrices, "
            "A_selected, b_selected, and deltaTheta_C1 remain unselected."
        ),
    }

    packet = {
        "theorem": theorem,
        "status": STATUS,
        "what_closes_now": what_closes_now,
        "source_primitive_map_certificate": source,
        "primitive_tensor_hessian_source_map_candidate": source_map,
        "source_map_selection_obligation_kernel": kernel,
        "honest_galerkin_execution_value_slots": galerkin,
        "what_remains_open": what_remains_open,
        "frontier_decision": {
            "source_map_candidate_constructed": True,
            "source_map_selection_open": True,
            "frontier_is_source_map_selection_theorem_or_honest_galerkin_value_run": True,
            "next_required_artifact": NEXT,
        },
        "guardrails": guardrails,
        "input_artifacts": {
            "previous_long_name_certificate": str(PREV),
            "source_primitive_map_certificate": str(SOURCE_CERT),
            "source_primitive_map_packet": source["packet_written"],
        },
    }

    note = f"""# PostAlpha Independent PrimitiveC1Tensor HessianSourceMap or HonestGalerkinC1Execution Import v1

## Result

The independent long-name branch now carries the primitive/Hessian source-map candidate.

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

This constructs the candidate and selection-obligation kernel. It does not
select the source map or promote the response values.

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
        "certificate": "post_alpha_independent_primitive_c1_tensor_hessian_source_map_or_honest_galerkin_c1_execution",
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
