from __future__ import annotations

import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
CERT = ROOT / "certificates" / "post_alpha_i10_payload_certificate_or_quadrature_values_fill_certificate.json"
STATUS = "POST_ALPHA_I10_PAYLOAD_CERTIFICATE_OR_QUADRATURE_VALUES_FILL_IMPORTED_CUTSET_OPEN"
NEXT = "MTT_Selected_StromingerTraceC1FirstVariation_or_QuadratureExecutionPlan_v1"


def require(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)


def main() -> None:
    cert = json.loads(CERT.read_text(encoding="utf-8"))
    packet = json.loads(Path(cert["packet_written"]).read_text(encoding="utf-8"))
    note = Path(cert["note_written"]).read_text(encoding="utf-8")

    require(cert["status"] == STATUS, "unexpected status")
    require(cert["closure_claimed"] is False, "must not claim closure")
    require(cert["unpatched_theorem_closure_claimed"] is False, "unpatched closure overclaimed")
    require(cert["theorem"]["proved"] is True, "I10 fill cutset theorem should be proved")
    require(all(cert["what_closes_now"].values()), "closed checks should pass")
    require(all(cert["what_remains_open"].values()), "open gates should remain open")
    require(all(cert["guardrails"].values()), "guardrails should hold")
    require(cert["frontier_decision"]["next_required_artifact"] == NEXT, "wrong next artifact")

    summary = packet["source_candidate_summary"]
    require(summary["promotion_decision"]["I10_proved"] is False, "I10 overclaimed")
    require(summary["promotion_decision"]["route_A_i10_payload_certificate_accepted"] is False, "route A overclaimed")
    require(summary["promotion_decision"]["route_B_independent_quadrature_values_accepted"] is False, "route B overclaimed")
    require(summary["promotion_decision"]["true_SM_equivalence_closed"] is False, "SM equivalence overclaimed")
    require(summary["replay_if_route_A_or_B_accepted"]["A_transpose_A"] == [[12.0, 0.0], [0.0, 12.0]], "wrong Gram")
    require(summary["replay_if_route_A_or_B_accepted"]["A_transpose_b"] == [12.0, 12.0], "wrong ATb")
    require(summary["replay_if_route_A_or_B_accepted"]["deltaTheta_C1"] == [1.0, 1.0], "wrong DeltaTheta")

    route_a = packet["route_A_i10_payload_certificate_fill_attempt"]
    require(route_a["accepted_now"] is False, "route A should not be accepted")
    require(route_a["payload_checks"]["no_observed_data_as_selector"]["value"] is True, "selector guardrail drift")
    require(route_a["payload_checks"]["selected_minimizer_trace_payload_verified"]["value"] is False, "minimizer payload overclaimed")
    require(route_a["payload_checks"]["selected_c1_response_payload_verified"]["value"] is False, "C1 response payload overclaimed")
    require(route_a["payload_checks"]["defect_functional_minimizer_payload_verified"]["value"] is False, "defect payload overclaimed")

    route_b = packet["route_B_independent_quadrature_values_fill_attempt"]
    require(route_b["accepted_now"] is False, "route B should not be accepted")
    require(route_b["acceptance_checks"]["no_patched_replay_copying"] is True, "replay-copying guardrail drift")
    require(route_b["table_counts"] == {
        "hessian_source_rows": 0,
        "primitive_contraction_rows": 0,
        "sector_matrix_rows": 0,
        "zero_mode_basis_rows": 0,
    }, "quadrature tables should remain empty")

    cutset = packet["minimal_next_cutset"]
    require(cutset["recommended_next"]["artifact"] == NEXT, "cutset next artifact drift")
    require(len(cutset["route_A_minimal_cutset"]) == 3, "route A cutset count drift")
    require(len(cutset["route_B_minimal_cutset"]) == 4, "route B cutset count drift")
    require(STATUS in note and NEXT in note and "does not close I10" in note, "note missing essentials")
    print("AUDIT_PASS: I10 payload/quadrature fill attempt imported; next cutset remains open")


if __name__ == "__main__":
    main()
