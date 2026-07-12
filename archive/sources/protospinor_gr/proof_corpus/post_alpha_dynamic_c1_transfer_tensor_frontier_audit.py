from __future__ import annotations

import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
CERT = ROOT / "certificates" / "post_alpha_dynamic_c1_transfer_tensor_frontier_certificate.json"
STATUS = "POST_ALPHA_DYNAMIC_C1_TRANSFER_TENSOR_FRONTIER_BUILT_PRIMITIVE_VALUES_OPEN"
NEXT = "MTT_Selected_PrimitiveC1Tensor_or_HessianSourceVector_or_GalerkinC1Values_v1"


def require(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)


def main() -> None:
    cert = json.loads(CERT.read_text(encoding="utf-8"))
    packet = json.loads(Path(cert["packet_written"]).read_text(encoding="utf-8"))
    note = Path(cert["note_written"]).read_text(encoding="utf-8")

    require(cert["status"] == STATUS, "unexpected status")
    require(cert["closure_claimed"] is False, "must not claim closure")
    require(cert["theorem"]["proved"] is True, "dynamic tensor frontier theorem should be proved")
    require(all(cert["what_closes_now"].values()), "closed checks should pass")
    require(all(cert["what_remains_open"].values()), "open gates should remain open")
    require(all(cert["guardrails"].values()), "guardrails should hold")

    decision = cert["frontier_decision"]
    require(decision["operator_alpha1_support_closed"] is True, "operator support not closed")
    require(decision["conditional_dynamic_tensor_built"] is True, "conditional tensor not built")
    require(decision["conditional_dynamic_tensor_promoted"] is False, "conditional tensor promoted")
    require(decision["frontier_is_primitive_tensor_Hessian_or_Galerkin_values"] is True, "wrong frontier")
    require(decision["next_required_artifact"] == NEXT, "wrong next artifact")

    normal = packet["conditional_tensor_normal_form"]["normal_form_replay"]
    require(normal["rank"] == 2, "rank drift")
    require(normal["A_transpose_A"] == [[12.0, 0.0], [0.0, 12.0]], "wrong A^T A")
    require(normal["A_transpose_b"] == [12.0, 12.0], "wrong A^T b")
    require(normal["deltaTheta_C1"] == [1.0, 1.0], "wrong DeltaTheta")
    require(packet["conditional_tensor_normal_form"]["selection_status"]["selected_dynamic_C1_transfer_tensor_promoted"] is False, "tensor selected")
    require(packet["conditional_tensor_normal_form"]["codomain"]["real_dimension"] == 72, "codomain drift")

    routes = packet["frontier_value_routes"]
    require(set(routes) == {
        "route_A_selected_noninvariant_primitive_tensor",
        "route_B_selected_Hessian_or_b_source_vector",
        "route_C_honest_Galerkin_C1_values",
    }, "route set drift")
    require(all(route["currently_emitted"] is False for route in routes.values()), "route emitted prematurely")
    require("selected A_selected" in packet["closed_operator_support"]["does_not_emit"], "A guard lost")
    require("selected deltaTheta_C1" in packet["closed_operator_support"]["does_not_emit"], "DeltaTheta guard lost")
    require(STATUS in note and NEXT in note and "conditional dynamic tensor normal form is built" in note, "note missing essentials")
    print("AUDIT_PASS: dynamic C1 transfer tensor frontier built; primitive/Hessian/Galerkin values remain open")


if __name__ == "__main__":
    main()
