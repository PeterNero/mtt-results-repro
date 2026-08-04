from __future__ import annotations

import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
CERT = (
    ROOT
    / "certificates"
    / "post_alpha_independent_long_primitive_rows_execution_or_dynamic_dotd_trace_binding_certificate.json"
)
STATUS = "POST_ALPHA_INDEPENDENT_LONG_DYNAMIC_DOTD_TRACE_BOUND_PRIMITIVE_ROWS_BLOCKED_BY_RESIDUAL_COMPLETION"
NEXT = "MTT_Selected_ResidualCompletion_SourcePromotion_or_HonestGalerkinC1_Emission_v1"


def require(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)


def main() -> None:
    cert = json.loads(CERT.read_text(encoding="utf-8"))
    packet = json.loads(Path(cert["packet_written"]).read_text(encoding="utf-8"))
    note = Path(cert["note_written"]).read_text(encoding="utf-8")

    require(cert["status"] == STATUS, "unexpected status")
    require(cert["closure_claimed"] is False, "closure overclaimed")
    require(cert["unpatched_theorem_closure_claimed"] is False, "unpatched closure overclaimed")
    require(cert["theorem"]["proved"] is True, "long-chain dynamic-binding bridge should be proved")
    require(all(cert["what_closes_now"].values()), "closed checks should pass")
    require(all(cert["what_remains_open"].values()), "open gates should remain open")
    require(all(cert["guardrails"].values()), "guardrails should hold")

    previous = packet["fresh_previous_certificate"]
    require(previous["theorem"]["proved"] is True, "previous theorem not proved")
    require(previous["frontier_decision"]["next_required_artifact"].endswith("DotDTraceBinding_v1"), "previous frontier drift")

    frontier = cert["frontier_decision"]
    require(frontier["dynamic_dotD_trace_binding_accepted"] is True, "dynamic binding not accepted")
    require(frontier["independent_primitive_rows_executed"] is False, "primitive rows overexecuted")
    require(frontier["conditional_replay_retained_without_promotion"] is True, "conditional guardrail missing")
    require(frontier["frontier_is_residual_completion_source_promotion_or_honest_galerkin_C1_emission"] is True, "wrong frontier")
    require(frontier["next_required_artifact"] == NEXT, "wrong next artifact")

    binding = packet["dynamic_dotd_trace_binding"]
    flags = binding["binding_flags"]
    require(binding["status"] == "DYNAMIC_DOTD_TRACE_BINDING_ACCEPTED", "binding status drift")
    require(flags["dynamic_dotD_trace_binding_accepted"] is True, "dynamic binding flag missing")
    require(flags["selected_dotD_source_verified"] is True, "dotD source missing")
    require(flags["alpha1_driver_verified"] is True, "alpha1 driver missing")
    require("A_selected" in binding["not_accepted_scope"], "A guardrail missing")
    require("b_selected" in binding["not_accepted_scope"], "b guardrail missing")
    require("deltaTheta_C1" in binding["not_accepted_scope"], "deltaTheta guardrail missing")

    primitive = packet["independent_primitive_rows_execution_attempt"]
    require(primitive["row_count"] == 72, "primitive row count drift")
    require(len(primitive["rows"]) == 72, "primitive rows missing")
    require(primitive["executed_row_count"] == 0, "primitive rows overexecuted")
    require(primitive["primitive_rows_executed"] is False, "primitive execution overclaimed")
    require(primitive["span_obstruction_summary"]["pure_fixed_fiber_span_can_close"] is False, "span obstruction missing")
    conditional = primitive["conditional_dynamic_values_retained"]
    require(conditional["Gram_A_transpose_A"] == [[12.0, 0.0], [0.0, 12.0]], "conditional Gram drift")
    require(conditional["A_transpose_b_conditional"] == [12.0, 12.0], "conditional b drift")
    require(conditional["deltaTheta_conditional_from_Gram_solve"] == [1.0, 1.0], "conditional deltaTheta drift")
    require(conditional["rank"] == 2, "conditional rank drift")

    cutset = packet["residual_completion_or_honest_galerkin_cutset"]
    require(cutset["recommended_next"]["artifact"] == NEXT, "cutset next drift")
    require("selected_residual_completion_source_theorem" in cutset["still_open"], "residual source gate missing")
    require("honest_Galerkin_C1_contractions" in cutset["still_open"], "honest Galerkin gate missing")

    require(STATUS in note and NEXT in note and "dynamic trace binding" in note, "note missing essentials")
    print(
        "AUDIT_PASS: reanchored long-chain dynamic dotD trace binding accepted; "
        "primitive rows remain blocked"
    )


if __name__ == "__main__":
    main()
