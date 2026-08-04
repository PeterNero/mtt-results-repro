from __future__ import annotations

import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SM_ROOT = ROOT.parent / "mtt-sm-parity-closure"

PREV = ROOT / "certificates" / "post_alpha_enriched_weylpair_source_provenance_or_galerkin_c1_values_certificate.json"
SLUG = "selected_dynamicc1transfertensor_or_galerkinc1values"
SM_CERT = SM_ROOT / "certificates" / f"{SLUG}_certificate.json"
SM_CANDIDATE = SM_ROOT / "candidate_data" / f"{SLUG}.candidate.json"
SM_DIR = SM_ROOT / "candidate_data" / SLUG
SUPPORT = SM_DIR / "closed_dynamic_operator_support.packet.json"
TENSOR = SM_DIR / "conditional_dynamic_c1_transfer_tensor.packet.json"
FRONTIER = SM_DIR / "primitive_tensor_or_galerkin_frontier.packet.json"

OUT_CERT = ROOT / "certificates" / "post_alpha_dynamic_c1_transfer_tensor_or_galerkin_c1_values_certificate.json"
OUT_PACKET = ROOT / "candidate_data" / "post_alpha_dynamic_c1_transfer_tensor_or_galerkin_c1_values.packet.json"
OUT_NOTE = ROOT / "proof_corpus" / "PostAlpha_DynamicC1TransferTensor_or_GalerkinC1Values_Import_v1.md"

STATUS = "POST_ALPHA_DYNAMIC_C1_TRANSFER_TENSOR_OR_GALERKIN_C1_VALUES_IMPORTED_OPERATOR_ALPHA1_CLOSED_PRIMITIVE_OPEN"
NEXT = "MTT_Selected_PrimitiveC1Tensor_or_HessianSourceVector_or_GalerkinC1Values_v1"


def load(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def main() -> None:
    prev = load(PREV)
    cert = load(SM_CERT)
    candidate = load(SM_CANDIDATE)
    support = load(SUPPORT)
    tensor = load(TENSOR)
    frontier = load(FRONTIER)

    prev_ok = all(
        [
            prev["theorem"]["proved"] is True,
            prev["closure_claimed"] is False,
            prev["frontier_decision"]["frontier_is_dynamic_C1_transfer_tensor_or_galerkin_C1_values"] is True,
            prev["frontier_decision"]["next_required_artifact"]
            == "MTT_Selected_DynamicC1TransferTensor_or_GalerkinC1Values_v1",
        ]
    )

    imported_ok = all(
        [
            cert["certificate"] == "MTT_Selected_DynamicC1TransferTensor_or_GalerkinC1Values_v1",
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
            candidate["theorem"]["name"] == "DynamicC1FrontierReductionTheorem",
            candidate["theorem"]["proved"] is True,
            candidate["promotion_decision"]["operator_alpha1_support_closed_for_frontier"] is True,
            candidate["promotion_decision"]["conditional_dynamic_C1_transfer_tensor_selected"] is False,
            candidate["promotion_decision"]["selected_noninvariant_primitive_C1_tensor_promoted"] is False,
            candidate["promotion_decision"]["selected_Hessian_or_b_source_vector_promoted"] is False,
            candidate["promotion_decision"]["A_selected_promoted"] is False,
            candidate["promotion_decision"]["b_selected_promoted"] is False,
            candidate["promotion_decision"]["deltaTheta_C1_promoted"] is False,
            candidate["promotion_decision"]["SM_parity_dynamic_packet_closed"] is False,
        ]
    )

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
        "static_provenance_gate_consumed": prev_ok,
        "dynamic_frontier_reduction_imported": imported_ok,
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
        "name": "PostAlphaDynamicC1FrontierReductionImport",
        "proved": all([all(what_closes_now.values()), all(what_remains_open.values()), all(guardrails.values())]),
        "closure_claimed": False,
        "statement": (
            "After static Weyl-pair provenance and alpha1/dotD support are closed, "
            "the remaining obstruction is reduced to selected non-invariant primitive "
            "C1 tensor values, a selected Hessian/source vector b_selected, or honest "
            "Galerkin C1 values. The conditional dynamic C1 tensor normal form is built "
            "with rank 2 and A^T A=12 I_2, but is not selected physical data."
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
            "previous_gate_certificate": str(PREV),
            "sm_gate_certificate": str(SM_CERT),
            "sm_gate_candidate": str(SM_CANDIDATE),
            "closed_dynamic_operator_support": str(SUPPORT),
            "conditional_dynamic_c1_transfer_tensor": str(TENSOR),
            "primitive_tensor_or_galerkin_frontier": str(FRONTIER),
        },
    }

    note = f"""# PostAlpha DynamicC1TransferTensor or GalerkinC1Values Import v1

## Result

Dynamic operator support and alpha1/dotD support are closed for the frontier.
The conditional dynamic tensor normal form is built but not selected.

```text
tensor name   = T_dynamic_conditional_WeylPair
codomain      = 72 real dimensions
rank          = 2
A^T A         = [[12, 0], [0, 12]]
A^T b         = [12, 12]
deltaTheta    = [1, 1]
```

The remaining value routes are now exactly: non-invariant primitive C1 tensor,
Hessian/source vector `b_selected`, or honest selected Galerkin C1 values.

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
        "certificate": "post_alpha_dynamic_c1_transfer_tensor_or_galerkin_c1_values",
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
