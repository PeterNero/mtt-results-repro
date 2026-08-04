from __future__ import annotations

import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]

PREV = ROOT / "certificates" / "post_alpha_independent_enriched_weylpair_source_provenance_or_galerkin_c1_values_certificate.json"
SOURCE_CERT = ROOT / "certificates" / "post_alpha_dynamic_c1_transfer_tensor_or_galerkin_c1_values_certificate.json"

OUT_CERT = ROOT / "certificates" / "post_alpha_independent_dynamic_c1_transfer_tensor_or_galerkin_c1_values_certificate.json"
OUT_PACKET = ROOT / "candidate_data" / "post_alpha_independent_dynamic_c1_transfer_tensor_or_galerkin_c1_values.packet.json"
OUT_NOTE = ROOT / "proof_corpus" / "PostAlpha_IndependentDynamicC1TransferTensor_or_GalerkinC1Values_Import_v1.md"

STATUS = "POST_ALPHA_INDEPENDENT_DYNAMIC_C1_TRANSFER_TENSOR_OR_GALERKIN_C1_VALUES_IMPORTED_OPERATOR_ALPHA1_CLOSED_PRIMITIVE_OPEN"
SOURCE_STATUS = "POST_ALPHA_DYNAMIC_C1_TRANSFER_TENSOR_OR_GALERKIN_C1_VALUES_IMPORTED_OPERATOR_ALPHA1_CLOSED_PRIMITIVE_OPEN"
THIS_ARTIFACT = "MTT_Selected_DynamicC1TransferTensor_or_GalerkinC1Values_v1"
NEXT = "MTT_Selected_PrimitiveC1Tensor_or_HessianSourceVector_or_GalerkinC1Values_v1"


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
            prev["frontier_decision"]["static_enriched_weylpair_source_provenance_closed"] is True,
            prev["frontier_decision"]["dynamic_C1_values_open_after_static_closure"] is True,
            prev["frontier_decision"]["frontier_is_dynamic_C1_transfer_tensor_or_galerkin_C1_values"] is True,
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
            source["frontier_decision"]["operator_alpha1_support_closed_for_frontier"] is True,
            source["frontier_decision"]["conditional_dynamic_C1_transfer_tensor_built_not_selected"] is True,
            source["frontier_decision"]["frontier_is_primitive_C1_tensor_or_Hessian_source_vector_or_Galerkin_values"]
            is True,
            source["frontier_decision"]["next_required_artifact"] == NEXT,
            all(source["what_closes_now"].values()),
            all(source["what_remains_open"].values()),
            all(source["guardrails"].values()),
        ]
    )

    support = source_packet["closed_dynamic_operator_support"]
    tensor = source_packet["conditional_dynamic_c1_transfer_tensor"]
    frontier = source_packet["primitive_tensor_or_galerkin_frontier"]

    support_ok = all(
        [
            support["schema"] == "MTTClosedDynamicOperatorSupport.v1",
            support["status"] == "STATIC_OPERATOR_ALPHA1_SUPPORT_CLOSED_FOR_DYNAMIC_C1_FRONTIER",
            support["closed_for_frontier"] is True,
            support["static_source_support"]["static_enriched_weylpair_source_provenance_promoted"] is True,
            support["static_source_support"]["phase_Z_to"] == ["u", "e"],
            support["static_source_support"]["shift_X_to"] == ["d", "nuD"],
            support["static_source_support"]["trace_transfer_normalization_selected"] is True,
            support["stationary_operator_support"]["selected_source_verified"] is True,
            support["stationary_operator_support"]["selected_riesz_green_source_verified"] is True,
            support["alpha1_dotD_support"]["alpha1_driver_verified_imported"] is True,
            support["alpha1_dotD_support"]["honest_dotD_alpha1_replay"] is True,
            support["alpha1_dotD_support"]["primitive_overlap_values_emitted_by_driver"] is False,
            "selected non-invariant primitive C1 tensor" in support["does_not_emit"],
            "selected A_selected" in support["does_not_emit"],
            support["observed_data_used"] is False,
            support["target_fitting_used"] is False,
        ]
    )

    tensor_ok = all(
        [
            tensor["schema"] == "MTTConditionalDynamicC1TransferTensor.v1",
            tensor["status"] == "CONDITIONAL_TENSOR_NORMAL_FORM_BUILT_NOT_SELECTED",
            tensor["tensor_name"] == "T_dynamic_conditional_WeylPair",
            tensor["codomain"]["real_dimension"] == 72,
            tensor["codomain"]["sector_order"] == ["u", "d", "e", "nuD"],
            tensor["domain_basis"][0]["id"] == "phase_Z",
            tensor["domain_basis"][0]["routed_to"] == ["u", "e"],
            tensor["domain_basis"][1]["id"] == "shift_X",
            tensor["domain_basis"][1]["routed_to"] == ["d", "nuD"],
            tensor["normal_form_replay"]["rank"] == 2,
            abs(tensor["normal_form_replay"]["condition_number"] - 1.0) < 1e-12,
            tensor["normal_form_replay"]["A_transpose_A"] == [[12.0, 0.0], [0.0, 12.0]],
            tensor["normal_form_replay"]["A_transpose_b"] == [12.0, 12.0],
            tensor["normal_form_replay"]["deltaTheta_C1"] == [1.0, 1.0],
            tensor["normal_form_replay"]["SM_parity_dynamic_packet_would_close_if_promoted"] is True,
            tensor["normal_form_replay"]["no_knob_flavor_constants_would_close_if_promoted"] is False,
            tensor["selection_status"]["conditional_tensor_built"] is True,
            tensor["selection_status"]["selected_dynamic_C1_transfer_tensor_promoted"] is False,
            tensor["selection_status"]["A_selected_promoted"] is False,
            tensor["selection_status"]["b_selected_promoted"] is False,
            tensor["selection_status"]["deltaTheta_C1_promoted"] is False,
            tensor["observed_data_used"] is False,
            tensor["target_fitting_used"] is False,
        ]
    )

    frontier_ok = all(
        [
            frontier["schema"] == "MTTPrimitiveTensorOrGalerkinFrontier.v1",
            frontier["status"] == "PRIMITIVE_TENSOR_HESSIAN_OR_GALERKIN_VALUES_OPEN",
            frontier["canonical_tensor_selected_by_theorem"] is False,
            frontier["transport_only_lane_rejected"] is True,
            frontier["transport_only_zero_matrices"] is True,
            frontier["remaining_value_routes"]["route_A_selected_noninvariant_primitive_tensor"]["currently_emitted"] is False,
            frontier["remaining_value_routes"]["route_B_selected_Hessian_or_b_source_vector"]["currently_emitted"] is False,
            frontier["remaining_value_routes"]["route_C_honest_Galerkin_C1_values"]["currently_emitted"] is False,
            frontier["remaining_value_routes"]["route_C_honest_Galerkin_C1_values"]["selected_source_verified_now"] is False,
            "A_selected=[phase_column, shift_column]" in frontier["required_acceptance_equations"],
            "b_selected is emitted by the same primitive/Hessian source, not copied from a target vector"
            in frontier["required_acceptance_equations"],
            "HessianCounterterm_s^r[i,j]" in frontier["required_primitive_formula"],
            frontier["observed_data_used"] is False,
            frontier["target_fitting_used"] is False,
        ]
    )

    what_closes_now = {
        "long_name_static_provenance_gate_consumed": prev_ok,
        "audited_dynamic_frontier_reduction_reanchored": source_ok,
        "operator_alpha1_support_closed_for_frontier": support_ok,
        "conditional_dynamic_C1_transfer_tensor_normal_form_built": tensor_ok,
        "primitive_tensor_Hessian_or_Galerkin_frontier_identified": frontier_ok,
    }

    what_remains_open = {
        "selected_noninvariant_primitive_C1_tensor": True,
        "selected_primitive_C1_overlap_contractions": True,
        "selected_Hessian_or_b_source_vector": True,
        "selected_A_selected": True,
        "selected_b_selected": True,
        "selected_deltaTheta_C1": True,
        "honest_selected_Galerkin_C1_values": True,
        "SM_parity_dynamic_packet_closure": True,
        "true_SM_equivalence_closure": True,
        "full_no_knob_flavor_closure": True,
    }

    guardrails = {
        "promotes_operator_alpha1_support_only_for_frontier": True,
        "does_not_promote_conditional_dynamic_C1_tensor": True,
        "does_not_promote_primitive_tensor": True,
        "does_not_promote_Hessian_or_b_source_vector": True,
        "does_not_promote_A_b_deltaTheta": True,
        "does_not_claim_SM_parity_dynamic_closure": True,
        "does_not_claim_true_SM_equivalence": True,
        "does_not_claim_no_knob_flavor_closure": True,
        "does_not_use_observed_or_target_inputs": True,
    }

    theorem = {
        "name": "PostAlphaIndependentDynamicC1FrontierReductionImport",
        "proved": all([all(what_closes_now.values()), all(what_remains_open.values()), all(guardrails.values())]),
        "closure_claimed": False,
        "statement": (
            "The independent long-name branch imports the dynamic C1 frontier "
            "reduction. Operator alpha1 support is closed for the frontier and the "
            "conditional dynamic Weyl-pair tensor normal form is built, but selected "
            "primitive tensor values, Hessian/source-vector values, A_selected, "
            "b_selected, deltaTheta_C1, and honest Galerkin values remain open."
        ),
    }

    packet = {
        "theorem": theorem,
        "status": STATUS,
        "what_closes_now": what_closes_now,
        "source_dynamic_frontier_certificate": source,
        "closed_dynamic_operator_support": support,
        "conditional_dynamic_c1_transfer_tensor": tensor,
        "primitive_tensor_or_galerkin_frontier": frontier,
        "what_remains_open": what_remains_open,
        "frontier_decision": {
            "operator_alpha1_support_closed_for_frontier": True,
            "conditional_dynamic_C1_transfer_tensor_built_not_selected": True,
            "frontier_is_primitive_C1_tensor_or_Hessian_source_vector_or_Galerkin_values": True,
            "next_required_artifact": NEXT,
        },
        "guardrails": guardrails,
        "input_artifacts": {
            "previous_long_name_certificate": str(PREV),
            "source_dynamic_frontier_certificate": str(SOURCE_CERT),
            "source_dynamic_frontier_packet": source["packet_written"],
        },
    }

    note = f"""# PostAlpha Independent DynamicC1TransferTensor or GalerkinC1Values Import v1

## Result

The independent long-name branch now carries the dynamic C1 frontier reduction.

```text
tensor name   = T_dynamic_conditional_WeylPair
codomain      = 72 real dimensions
rank          = 2
A^T A         = [[12, 0], [0, 12]]
A^T b         = [12, 12]
deltaTheta    = [1, 1]
```

This closes operator/alpha1 support for the frontier only. The remaining value
routes are the selected non-invariant primitive C1 tensor, selected
Hessian/source vector, or honest selected Galerkin C1 values.

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
        "certificate": "post_alpha_independent_dynamic_c1_transfer_tensor_or_galerkin_c1_values",
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
