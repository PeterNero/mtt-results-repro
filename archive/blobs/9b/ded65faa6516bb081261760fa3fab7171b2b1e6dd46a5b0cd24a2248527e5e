from __future__ import annotations

import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
CERT = ROOT / "certificates" / "post_alpha_independent_dynamic_c1_transfer_tensor_or_galerkin_c1_values_certificate.json"
STATUS = "POST_ALPHA_INDEPENDENT_DYNAMIC_C1_TRANSFER_TENSOR_OR_GALERKIN_C1_VALUES_IMPORTED_OPERATOR_ALPHA1_CLOSED_PRIMITIVE_OPEN"
NEXT = "MTT_Selected_PrimitiveC1Tensor_or_HessianSourceVector_or_GalerkinC1Values_v1"


def require(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)


def main() -> None:
    cert = json.loads(CERT.read_text(encoding="utf-8"))
    packet = json.loads(Path(cert["packet_written"]).read_text(encoding="utf-8"))
    note = Path(cert["note_written"]).read_text(encoding="utf-8")

    require(cert["status"] == STATUS, "unexpected status")
    require(cert["closure_claimed"] is False, "closure overclaimed")
    require(cert["theorem"]["proved"] is True, "independent dynamic C1 frontier import should be proved")
    require(all(cert["what_closes_now"].values()), "closed checks should pass")
    require(all(cert["what_remains_open"].values()), "open gates should remain open")
    require(all(cert["guardrails"].values()), "guardrails should hold")
    require(cert["frontier_decision"]["next_required_artifact"] == NEXT, "wrong next artifact")
    require(cert["frontier_decision"]["operator_alpha1_support_closed_for_frontier"] is True, "operator support not closed")
    require(cert["frontier_decision"]["conditional_dynamic_C1_transfer_tensor_built_not_selected"] is True, "conditional tensor boundary lost")

    support = packet["closed_dynamic_operator_support"]
    require(support["closed_for_frontier"] is True, "support frontier not closed")
    require(support["alpha1_dotD_support"]["honest_dotD_alpha1_replay"] is True, "alpha1 replay missing")
    require(support["alpha1_dotD_support"]["primitive_overlap_values_emitted_by_driver"] is False, "primitive values overemitted")
    require("selected A_selected" in support["does_not_emit"], "support guardrail missing")

    tensor = packet["conditional_dynamic_c1_transfer_tensor"]
    require(tensor["status"] == "CONDITIONAL_TENSOR_NORMAL_FORM_BUILT_NOT_SELECTED", "tensor status drift")
    require(tensor["selection_status"]["conditional_tensor_built"] is True, "conditional tensor not built")
    require(tensor["selection_status"]["selected_dynamic_C1_transfer_tensor_promoted"] is False, "tensor overpromoted")
    require(tensor["normal_form_replay"]["rank"] == 2, "rank drift")
    require(abs(tensor["normal_form_replay"]["condition_number"] - 1.0) < 1e-12, "condition number drift")
    require(tensor["normal_form_replay"]["A_transpose_A"] == [[12.0, 0.0], [0.0, 12.0]], "A^T A drift")
    require(tensor["normal_form_replay"]["A_transpose_b"] == [12.0, 12.0], "A^T b drift")
    require(tensor["normal_form_replay"]["deltaTheta_C1"] == [1.0, 1.0], "deltaTheta drift")
    require(tensor["domain_basis"][0]["routed_to"] == ["u", "e"], "phase route drift")
    require(tensor["domain_basis"][1]["routed_to"] == ["d", "nuD"], "shift route drift")

    frontier = packet["primitive_tensor_or_galerkin_frontier"]
    require(frontier["status"] == "PRIMITIVE_TENSOR_HESSIAN_OR_GALERKIN_VALUES_OPEN", "frontier status drift")
    require(frontier["canonical_tensor_selected_by_theorem"] is False, "canonical tensor overselected")
    require(frontier["transport_only_lane_rejected"] is True, "transport-only rejection missing")
    require(frontier["remaining_value_routes"]["route_A_selected_noninvariant_primitive_tensor"]["currently_emitted"] is False, "route A overemitted")
    require(frontier["remaining_value_routes"]["route_B_selected_Hessian_or_b_source_vector"]["currently_emitted"] is False, "route B overemitted")
    require(frontier["remaining_value_routes"]["route_C_honest_Galerkin_C1_values"]["currently_emitted"] is False, "route C overemitted")
    require("b_selected is emitted by the same primitive/Hessian source, not copied from a target vector" in frontier["required_acceptance_equations"], "b guardrail missing")

    require(STATUS in note and NEXT in note and "dynamic C1 frontier reduction" in note, "note missing essentials")
    print("AUDIT_PASS: long-chain dynamic C1 transfer frontier imported; primitive/Hessian/Galerkin values remain open")


if __name__ == "__main__":
    main()
