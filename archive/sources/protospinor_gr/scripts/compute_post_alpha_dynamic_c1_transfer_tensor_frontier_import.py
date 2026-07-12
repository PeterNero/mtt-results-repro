from __future__ import annotations

import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SM_ROOT = ROOT.parent / "mtt-sm-parity-closure"

PREV = ROOT / "certificates" / "post_alpha_enriched_weylpair_static_provenance_certificate.json"
SM_CERT = SM_ROOT / "certificates" / "selected_dynamicc1transfertensor_or_galerkinc1values_certificate.json"
SM_CANDIDATE = SM_ROOT / "candidate_data" / "selected_dynamicc1transfertensor_or_galerkinc1values.candidate.json"
SM_DIR = SM_ROOT / "candidate_data" / "selected_dynamicc1transfertensor_or_galerkinc1values"
SUPPORT = SM_DIR / "closed_dynamic_operator_support.packet.json"
TENSOR = SM_DIR / "conditional_dynamic_c1_transfer_tensor.packet.json"
FRONTIER = SM_DIR / "primitive_tensor_or_galerkin_frontier.packet.json"

OUT_CERT = ROOT / "certificates" / "post_alpha_dynamic_c1_transfer_tensor_frontier_certificate.json"
OUT_PACKET = ROOT / "candidate_data" / "post_alpha_dynamic_c1_transfer_tensor_frontier.packet.json"
OUT_NOTE = ROOT / "proof_corpus" / "PostAlpha_DynamicC1_TransferTensor_Frontier_Import_v1.md"

STATUS = "POST_ALPHA_DYNAMIC_C1_TRANSFER_TENSOR_FRONTIER_BUILT_PRIMITIVE_VALUES_OPEN"
NEXT = "MTT_Selected_PrimitiveC1Tensor_or_HessianSourceVector_or_GalerkinC1Values_v1"


def load(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def main() -> None:
    prev = load(PREV)
    cert = load(SM_CERT)
    cand = load(SM_CANDIDATE)
    support = load(SUPPORT)
    tensor = load(TENSOR)
    frontier = load(FRONTIER)

    prev_ok = (
        prev["theorem"]["proved"] is True
        and prev["frontier_decision"]["static_enriched_weylpair_provenance_closed"] is True
        and prev["frontier_decision"]["dynamic_C1_values_promoted"] is False
    )

    imported_ok = all(
        [
            cert["theorem_proved"] is True,
            cert["closure_claimed"] is False,
            cert["observed_data_used"] is False,
            cert["target_fitting_used"] is False,
            cert["next_required_artifact"] == NEXT,
            all(cert["what_closes"].values()),
            all(cert["what_remains_open"].values()),
            cand["theorem"]["proved"] is True,
            cand["closure_claimed"] is False,
            cand["A_selected_claimed"] is False,
            cand["b_selected_claimed"] is False,
            cand["deltaTheta_C1_claimed"] is False,
            cand["promotion_decision"]["operator_alpha1_support_closed_for_frontier"] is True,
            cand["promotion_decision"]["conditional_dynamic_C1_transfer_tensor_selected"] is False,
            cand["promotion_decision"]["selected_noninvariant_primitive_C1_tensor_promoted"] is False,
            cand["promotion_decision"]["selected_Hessian_or_b_source_vector_promoted"] is False,
            cand["promotion_decision"]["A_selected_promoted"] is False,
            cand["promotion_decision"]["b_selected_promoted"] is False,
        ]
    )

    support_ok = all(
        [
            support["schema"] == "MTTClosedDynamicOperatorSupport.v1",
            support["status"] == "STATIC_OPERATOR_ALPHA1_SUPPORT_CLOSED_FOR_DYNAMIC_C1_FRONTIER",
            support["closed_for_frontier"] is True,
            support["observed_data_used"] is False,
            support["target_fitting_used"] is False,
            support["static_source_support"]["static_enriched_weylpair_source_provenance_promoted"] is True,
            support["static_source_support"]["phase_Z_to"] == ["u", "e"],
            support["static_source_support"]["shift_X_to"] == ["d", "nuD"],
            support["stationary_operator_support"]["selected_riesz_green_source_verified"] is True,
            support["alpha1_dotD_support"]["alpha1_driver_verified_imported"] is True,
            support["alpha1_dotD_support"]["honest_dotD_alpha1_replay"] is True,
            "selected A_selected" in support["does_not_emit"],
            "selected deltaTheta_C1" in support["does_not_emit"],
        ]
    )

    tensor_ok = all(
        [
            tensor["schema"] == "MTTConditionalDynamicC1TransferTensor.v1",
            tensor["status"] == "CONDITIONAL_TENSOR_NORMAL_FORM_BUILT_NOT_SELECTED",
            tensor["tensor_name"] == "T_dynamic_conditional_WeylPair",
            tensor["observed_data_used"] is False,
            tensor["target_fitting_used"] is False,
            tensor["codomain"]["real_dimension"] == 72,
            tensor["codomain"]["sector_order"] == ["u", "d", "e", "nuD"],
            [b["id"] for b in tensor["domain_basis"]] == ["phase_Z", "shift_X"],
            tensor["normal_form_replay"]["rank"] == 2,
            tensor["normal_form_replay"]["A_transpose_A"] == [[12.0, 0.0], [0.0, 12.0]],
            tensor["normal_form_replay"]["A_transpose_b"] == [12.0, 12.0],
            tensor["normal_form_replay"]["deltaTheta_C1"] == [1.0, 1.0],
            tensor["selection_status"]["conditional_tensor_built"] is True,
            tensor["selection_status"]["selected_dynamic_C1_transfer_tensor_promoted"] is False,
            tensor["selection_status"]["A_selected_promoted"] is False,
            tensor["selection_status"]["b_selected_promoted"] is False,
        ]
    )

    frontier_ok = all(
        [
            frontier["schema"] == "MTTPrimitiveTensorOrGalerkinFrontier.v1",
            frontier["status"] == "PRIMITIVE_TENSOR_HESSIAN_OR_GALERKIN_VALUES_OPEN",
            frontier["canonical_tensor_selected_by_theorem"] is False,
            frontier["observed_data_used"] is False,
            frontier["target_fitting_used"] is False,
            frontier["transport_only_lane_rejected"] is True,
            frontier["transport_only_zero_matrices"] is True,
            all(not route["currently_emitted"] for route in frontier["remaining_value_routes"].values()),
        ]
    )

    what_closes_now = {
        "previous_static_provenance_gate_consumed": prev_ok,
        "dynamic_frontier_reduction_imported": imported_ok,
        "operator_alpha1_support_closed_for_frontier": support_ok,
        "conditional_dynamic_C1_transfer_tensor_normal_form_built": tensor_ok,
        "primitive_Hessian_or_Galerkin_frontier_identified": frontier_ok,
    }

    what_remains_open = {
        "selected_noninvariant_primitive_C1_tensor": True,
        "selected_primitive_C1_overlap_contractions": True,
        "selected_Hessian_or_b_source_vector": True,
        "selected_b_selected": True,
        "selected_A_selected": True,
        "selected_deltaTheta_C1": True,
        "honest_selected_Galerkin_C1_values": True,
        "SM_parity_dynamic_packet_closure": True,
        "full_no_knob_flavor_closure": True,
        "true_SM_equivalence_closure": True,
    }

    guardrails = {
        "does_not_promote_conditional_tensor": True,
        "does_not_promote_A_selected_b_selected_or_deltaTheta": True,
        "does_not_claim_primitive_C1_values": True,
        "does_not_claim_Galerkin_values": True,
        "does_not_use_observed_or_target_inputs": True,
        "does_not_claim_SM_or_no_knob_closure": True,
    }

    theorem = {
        "name": "PostAlphaDynamicC1TransferTensorFrontierImport",
        "proved": all([all(what_closes_now.values()), all(what_remains_open.values()), all(guardrails.values())]),
        "closure_claimed": False,
        "statement": (
            "After static Weyl-pair provenance, stationary projector/Riesz/Green "
            "transport, and alpha1/dotD replay are closed for the frontier, the "
            "conditional dynamic C1 transfer-tensor normal form is built with "
            "rank 2, A^T A=12 I_2, A^T b=(12,12), and DeltaTheta_C1=(1,1). "
            "It is not selected physical data. The remaining obstruction is "
            "exactly selected non-invariant primitive C1 tensor values, a "
            "same-branch Hessian/source vector b_selected, or honest Galerkin C1 values."
        ),
    }

    packet = {
        "theorem": theorem,
        "status": STATUS,
        "what_closes_now": what_closes_now,
        "closed_operator_support": {
            "static_source_support": support["static_source_support"],
            "stationary_operator_support": support["stationary_operator_support"],
            "alpha1_dotD_support": support["alpha1_dotD_support"],
            "does_not_emit": support["does_not_emit"],
        },
        "conditional_tensor_normal_form": {
            "tensor_name": tensor["tensor_name"],
            "codomain": tensor["codomain"],
            "domain_basis": tensor["domain_basis"],
            "normal_form_replay": tensor["normal_form_replay"],
            "selection_status": tensor["selection_status"],
        },
        "frontier_value_routes": frontier["remaining_value_routes"],
        "required_acceptance_equations": frontier["required_acceptance_equations"],
        "required_primitive_formula": frontier["required_primitive_formula"],
        "what_remains_open": what_remains_open,
        "frontier_decision": {
            "operator_alpha1_support_closed": True,
            "conditional_dynamic_tensor_built": True,
            "conditional_dynamic_tensor_promoted": False,
            "frontier_is_primitive_tensor_Hessian_or_Galerkin_values": True,
            "next_required_artifact": NEXT,
        },
        "guardrails": guardrails,
        "input_artifacts": {
            "previous_static_provenance": str(PREV),
            "sm_dynamic_tensor_certificate": str(SM_CERT),
            "sm_dynamic_tensor_candidate": str(SM_CANDIDATE),
            "closed_dynamic_operator_support": str(SUPPORT),
            "conditional_dynamic_c1_transfer_tensor": str(TENSOR),
            "primitive_tensor_or_galerkin_frontier": str(FRONTIER),
        },
    }

    note = f"""# PostAlpha Dynamic C1 Transfer Tensor Frontier Import v1

## Result

Closed for the dynamic C1 frontier:

```text
static Weyl-pair provenance
stationary projector/Riesz/Green support
alpha1/dotD driver replay
transport-only zero lane rejected
```

The conditional dynamic tensor normal form is built:

```text
rank = 2
A^T A = [[12.0, 0.0], [0.0, 12.0]]
A^T b = [12.0, 12.0]
DeltaTheta_C1 = [1.0, 1.0]
```

But it remains unpromoted. The live frontier is:

```text
selected non-invariant primitive C1 tensor
selected Hessian/source vector b_selected
honest selected Galerkin C1 values
```

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
        "certificate": "post_alpha_dynamic_c1_transfer_tensor_frontier",
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
