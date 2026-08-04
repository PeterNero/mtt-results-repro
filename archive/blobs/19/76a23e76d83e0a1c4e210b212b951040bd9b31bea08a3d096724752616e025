from __future__ import annotations

import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SM_ROOT = ROOT.parent / "mtt-sm-parity-closure"

PREV = ROOT / "certificates" / "post_alpha_dynamic_c1_transfer_tensor_frontier_certificate.json"
SM_CERT = SM_ROOT / "certificates" / "selected_primitivec1tensor_hessiansourcemap_or_honestgalerkinc1execution_certificate.json"
SM_CANDIDATE = SM_ROOT / "candidate_data" / "selected_primitivec1tensor_hessiansourcemap_or_honestgalerkinc1execution.candidate.json"
SM_DIR = SM_ROOT / "candidate_data" / "selected_primitivec1tensor_hessiansourcemap_or_honestgalerkinc1execution"
SOURCE_MAP = SM_DIR / "primitive_tensor_hessian_source_map_candidate.packet.json"
SELECTION_KERNEL = SM_DIR / "source_map_selection_obligation_kernel.packet.json"
GALERKIN_SLOTS = SM_DIR / "honest_galerkin_execution_value_slots.packet.json"

OUT_CERT = ROOT / "certificates" / "post_alpha_primitive_c1_hessian_source_map_candidate_certificate.json"
OUT_PACKET = ROOT / "candidate_data" / "post_alpha_primitive_c1_hessian_source_map_candidate.packet.json"
OUT_NOTE = ROOT / "proof_corpus" / "PostAlpha_PrimitiveC1_HessianSourceMap_Candidate_Import_v1.md"

STATUS = "POST_ALPHA_PRIMITIVE_C1_HESSIAN_SOURCE_MAP_CANDIDATE_BUILT_VALUES_OPEN"
NEXT = "MTT_Selected_SourceMapSelectionTheorem_or_HonestGalerkinC1ValueRun_v1"


def load(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def main() -> None:
    prev = load(PREV)
    cert = load(SM_CERT)
    cand = load(SM_CANDIDATE)
    source_map = load(SOURCE_MAP)
    kernel = load(SELECTION_KERNEL)
    galerkin = load(GALERKIN_SLOTS)

    prev_ok = all(
        [
            prev["theorem"]["proved"] is True,
            prev["closure_claimed"] is False,
            prev["frontier_decision"]["operator_alpha1_support_closed"] is True,
            prev["frontier_decision"]["conditional_dynamic_tensor_built"] is True,
            prev["frontier_decision"]["conditional_dynamic_tensor_promoted"] is False,
            prev["frontier_decision"]["frontier_is_primitive_tensor_Hessian_or_Galerkin_values"] is True,
        ]
    )

    imported_ok = all(
        [
            cert["theorem_proved"] is True,
            cert["closure_claimed"] is False,
            cert["observed_data_used"] is False,
            cert["target_fitting_used"] is False,
            cert["source_map_selected_claimed"] is False,
            cert["A_selected_claimed"] is False,
            cert["b_selected_claimed"] is False,
            cert["deltaTheta_C1_claimed"] is False,
            cert["sector_response_matrices_claimed"] is False,
            cert["honest_Galerkin_C1_claimed"] is False,
            cert["next_required_artifact"] == NEXT,
            all(cert["what_closes"].values()),
            all(cert["what_remains_open"].values()),
            cand["theorem"]["proved"] is True,
            cand["promotion_decision"]["source_map_candidate_constructed"] is True,
            cand["promotion_decision"]["source_map_selected_by_MTT_now"] is False,
            cand["promotion_decision"]["A_selected_promoted"] is False,
            cand["promotion_decision"]["b_selected_promoted"] is False,
            cand["promotion_decision"]["deltaTheta_C1_promoted"] is False,
        ]
    )

    residuals = source_map["candidate_residual_operators"]
    source_map_ok = all(
        [
            source_map["schema"] == "MTTPrimitiveC1TensorHessianSourceMapCandidate.v1",
            source_map["status"] == "SOURCE_MAP_CANDIDATE_CONSTRUCTED_SELECTION_OPEN",
            source_map["selected_by_MTT_now"] is False,
            source_map["observed_data_used"] is False,
            source_map["target_fitting_used"] is False,
            source_map["closed_support"]["canonical_Q_residual_available"] is True,
            source_map["closed_support"]["Q_residual_rank"] == 6,
            source_map["closed_support"]["alpha1_dotD_driver_verified"] is True,
            source_map["closed_support"]["strict_72_real_acceptance_target"]["total_real_coordinates"] == 72,
            source_map["domain"]["active_shift"] == [1, 1],
            residuals["phase_R_Z"]["selected_by_MTT_now"] is False,
            residuals["shift_R_X"]["selected_by_MTT_now"] is False,
            residuals["phase_R_Z"]["shape"]["residual_norm_sq"] == 4.0,
            residuals["shift_R_X"]["shape"]["residual_norm_sq"] == 2.0,
            residuals["phase_R_Z"]["shape"]["closure_error_norm_sq"] == 0.0,
            residuals["shift_R_X"]["shape"]["closure_error_norm_sq"] == 0.0,
            source_map["residual_completion_replay"]["phase_projection_plus_residual_equals_target"] is True,
            source_map["residual_completion_replay"]["shift_projection_plus_residual_equals_target"] is True,
            source_map["residual_completion_replay"]["routed_72_real_completion"]["conditional_b_norm_sq"] == 24.0,
            source_map["if_source_map_selected_then"]["rank"] == 2,
            source_map["if_source_map_selected_then"]["A_transpose_A"] == [[12.0, 0.0], [0.0, 12.0]],
            source_map["if_source_map_selected_then"]["A_transpose_b"] == [12.0, 12.0],
            source_map["if_source_map_selected_then"]["deltaTheta_C1"] == [1.0, 1.0],
        ]
    )

    current = kernel["minimal_truth_table"]["current_case"]
    selected_case = kernel["minimal_truth_table"]["if_phase_and_shift_residual_sources_selected_and_b_source_emitted"]
    kernel_ok = all(
        [
            kernel["schema"] == "MTTSourceMapSelectionObligationKernel.v1",
            kernel["status"] == "SELECTION_OBLIGATION_KERNEL_BUILT_VALUES_OPEN",
            kernel["observed_data_used"] is False,
            kernel["target_fitting_used"] is False,
            kernel["closed_numeric_facts"]["rank_2_condition_number_1"] is True,
            current["phase_R_Z_selected"] is False,
            current["shift_R_X_selected"] is False,
            current["b_source_emitted"] is False,
            current["A_selected_promotes"] is False,
            current["b_selected_promotes"] is False,
            current["deltaTheta_C1_promotes"] is False,
            selected_case["A_selected_promotes"] is True,
            selected_case["b_selected_promotes"] is True,
            selected_case["deltaTheta_C1_promotes"] is True,
            selected_case["SM_parity_dynamic_packet_would_close"] is True,
            selected_case["no_knob_flavor_constants_would_close"] is False,
            kernel["strict_acceptance_field_status"]["A_selected"] == "CONDITIONAL_REFERENCE_ONLY_NOT_SELECTED",
            kernel["strict_acceptance_field_status"]["sector_response_matrices"] == "NOT_EMITTED_BY_SELECTED_VALUE_SOURCE",
        ]
    )

    galerkin_ok = all(
        [
            galerkin["schema"] == "MTTHonestGalerkinC1ExecutionValueSlots.v1",
            galerkin["status"] == "HONEST_GALERKIN_EXECUTION_SLOTS_RESTATED_VALUES_OPEN",
            galerkin["can_replace_source_map_now"] is False,
            galerkin["manifest_status"] == "OPEN_C1_PRIMITIVE_CONTRACTIONS_MISSING",
            galerkin["selected_source_verified"] is False,
            galerkin["observed_data_used"] is False,
            galerkin["target_fitting_used"] is False,
            galerkin["strict_coordinate_target"]["total_real_coordinates"] == 72,
            galerkin["required_outputs"]
            == [
                "zero_mode_bases",
                "primitive_three_by_three_contraction_terms",
                "linear_response_matrices",
                "C33/nonzero-family-rank tests",
            ],
        ]
    )

    what_closes_now = {
        "previous_dynamic_tensor_frontier_consumed": prev_ok,
        "primitive_Hessian_source_map_candidate_imported": imported_ok,
        "exact_phase_and_shift_residual_shapes_attached": source_map_ok,
        "selection_obligation_truth_table_built": kernel_ok,
        "honest_Galerkin_value_slots_reemitted": galerkin_ok,
    }

    what_remains_open = {
        "selected_phase_R_Z_source": True,
        "selected_shift_R_X_source": True,
        "selected_Hessian_or_b_source_vector": True,
        "selected_b_selected": True,
        "selected_A_selected": True,
        "selected_deltaTheta_C1": True,
        "selected_primitive_C1_tensor_values": True,
        "selected_sector_response_matrices": True,
        "honest_selected_Galerkin_C1_execution_values": True,
        "SM_parity_dynamic_packet_closure": True,
        "full_no_knob_flavor_closure": True,
        "true_SM_equivalence_closure": True,
    }

    guardrails = {
        "does_not_select_source_map": True,
        "does_not_promote_residual_operator_shapes_as_values": True,
        "does_not_promote_A_b_deltaTheta_or_sector_matrices": True,
        "does_not_claim_Galerkin_values": True,
        "does_not_use_observed_or_target_inputs": True,
        "does_not_claim_SM_or_no_knob_closure": True,
    }

    theorem = {
        "name": "PostAlphaPrimitiveC1HessianSourceMapCandidateImport",
        "proved": all([all(what_closes_now.values()), all(what_remains_open.values()), all(guardrails.values())]),
        "closure_claimed": False,
        "statement": (
            "The exact minimal same-branch primitive/Hessian source-map candidate "
            "is built: apply Q_residual to the selected enriched Weyl-pair phase "
            "and shift legs, yielding R_Z and R_X residual operators with exact "
            "residual norms 4 and 2. If MTT selects these residual sources and "
            "emits b_selected, the rank-2 A_selected, b_selected, and DeltaTheta_C1 "
            "normal form follows. The current packet constructs the candidate and "
            "truth table only; it does not select the source map or promote values."
        ),
    }

    packet = {
        "theorem": theorem,
        "status": STATUS,
        "what_closes_now": what_closes_now,
        "source_map_candidate": {
            "name": source_map["source_map_name"],
            "selected_by_MTT_now": False,
            "domain": source_map["domain"],
            "closed_support": source_map["closed_support"],
            "residual_completion_replay": source_map["residual_completion_replay"],
            "if_source_map_selected_then": source_map["if_source_map_selected_then"],
        },
        "candidate_residual_shapes": source_map["candidate_residual_operators"],
        "selection_obligation_kernel": {
            "formal_statement": kernel["formal_statement"],
            "currently_emitted": kernel["currently_emitted"],
            "minimal_truth_table": kernel["minimal_truth_table"],
            "required_emissions": kernel["required_emissions"],
            "why_not_selected_yet": kernel["why_not_selected_yet"],
        },
        "honest_galerkin_value_slots": {
            "required_outputs": galerkin["required_outputs"],
            "can_replace_source_map_now": galerkin["can_replace_source_map_now"],
            "manifest_status": galerkin["manifest_status"],
            "selected_source_verified": galerkin["selected_source_verified"],
        },
        "what_remains_open": what_remains_open,
        "frontier_decision": {
            "source_map_candidate_constructed": True,
            "source_map_selected_by_MTT_now": False,
            "frontier_is_source_map_selection_or_honest_galerkin_value_run": True,
            "next_required_artifact": NEXT,
        },
        "guardrails": guardrails,
        "input_artifacts": {
            "previous_dynamic_tensor_frontier": str(PREV),
            "sm_source_map_certificate": str(SM_CERT),
            "sm_source_map_candidate": str(SM_CANDIDATE),
            "source_map_packet": str(SOURCE_MAP),
            "selection_kernel": str(SELECTION_KERNEL),
            "galerkin_slots": str(GALERKIN_SLOTS),
        },
    }

    note = f"""# PostAlpha Primitive C1 Hessian Source-Map Candidate Import v1

## Result

The missing source map is now explicit as a candidate:

```text
Z/clock phase leg    -> R_Z residual/Hessian source
X/shift active leg   -> R_X residual/Hessian source
shared support       -> canonical Q_residual, rank 6
```

Exact residual facts:

```text
||R_Z||^2 = 4.0
||R_X||^2 = 2.0
closure errors = 0.0
conditional ||b||^2 = 24.0
```

If MTT selects both residual sources and emits `b_selected`, the conditional
rank-2 normal form would promote:

```text
A^T A = [[12.0, 0.0], [0.0, 12.0]]
A^T b = [12.0, 12.0]
DeltaTheta_C1 = [1.0, 1.0]
```

But this packet does not select the source map. It records the candidate and
the selection obligation.

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
        "certificate": "post_alpha_primitive_c1_hessian_source_map_candidate",
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
