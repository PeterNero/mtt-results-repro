from __future__ import annotations

import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
CERT = ROOT / "certificates" / "post_alpha_primitive_rows_execution_or_dynamic_dotd_trace_binding_certificate.json"
STATUS = "POST_ALPHA_DYNAMIC_DOTD_TRACE_BOUND_PRIMITIVE_ROWS_BLOCKED_BY_RESIDUAL_COMPLETION"
NEXT = "MTT_Selected_ResidualCompletion_SourcePromotion_or_HonestGalerkinC1_Emission_v1"


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
    require(cert["theorem"]["proved"] is True, "dynamic binding theorem should be proved")
    require(all(cert["what_closes_now"].values()), "closed checks should pass")
    require(all(cert["what_remains_open"].values()), "open gates should remain open")
    require(all(cert["guardrails"].values()), "guardrails should hold")
    require(cert["frontier_decision"]["next_required_artifact"] == NEXT, "wrong next artifact")

    decision = packet["source_candidate_summary"]["promotion_decision"]
    require(decision["dynamic_dotD_trace_binding_accepted"] is True, "dynamic binding not promoted")
    for key in [
        "primitive_rows_executed",
        "residual_completion_promoted",
        "honest_Galerkin_C1_emission_promoted",
        "I10_proved",
        "unpatched_A_selected_promoted",
        "unpatched_b_selected_promoted",
        "unpatched_deltaTheta_C1_promoted",
        "unpatched_SM_parity_dynamic_packet_closed",
        "true_SM_equivalence_closed",
    ]:
        require(decision[key] is False, f"promotion overclaimed: {key}")

    binding = packet["dynamic_dotd_trace_binding"]
    flags = binding["binding_flags"]
    require(binding["status"] == "DYNAMIC_DOTD_TRACE_BINDING_ACCEPTED", "binding status drift")
    require(flags["dynamic_dotD_trace_binding_accepted"] is True, "binding flag missing")
    require(flags["selected_dotD_source_verified"] is True, "dotD source missing")
    require(flags["alpha1_driver_verified"] is True, "alpha1 driver missing")
    require("A_selected" in binding["not_accepted_scope"], "A guardrail missing")
    require("b_selected" in binding["not_accepted_scope"], "b guardrail missing")
    require("deltaTheta_C1" in binding["not_accepted_scope"], "deltaTheta guardrail missing")

    primitive = packet["primitive_rows_execution_attempt"]
    require(primitive["row_count"] == 72, "primitive row count drift")
    require(len(primitive["rows"]) == 72, "primitive rows missing")
    require(primitive["executed_row_count"] == 0, "primitive rows overexecuted")
    require(primitive["primitive_rows_executed"] is False, "primitive execution overclaimed")
    require(primitive["span_obstruction_summary"]["pure_fixed_fiber_span_can_close"] is False, "span obstruction missing")
    for row in primitive["rows"]:
        require(row["basis_stage_accepted"] is True, f"basis stage missing: {row['row_id']}")
        require(row["dynamic_trace_binding_accepted"] is True, f"dynamic binding missing: {row['row_id']}")
        require(row["executed_now"] is False, f"row overexecuted: {row['row_id']}")
    conditional = primitive["conditional_dynamic_values_retained"]
    require(conditional["Gram_A_transpose_A"] == [[12.0, 0.0], [0.0, 12.0]], "conditional Gram drift")
    require(conditional["A_transpose_b_conditional"] == [12.0, 12.0], "conditional b drift")
    require(conditional["deltaTheta_conditional_from_Gram_solve"] == [1.0, 1.0], "conditional deltaTheta drift")
    require(conditional["rank"] == 2, "conditional rank drift")

    cutset = packet["residual_completion_or_honest_galerkin_cutset"]
    require(cutset["recommended_next"]["artifact"] == NEXT, "cutset next artifact drift")
    require(cutset["recommended_next"]["locked_conditional_target"]["deltaTheta_C1"] == [1.0, 1.0], "cutset target drift")
    require("selected_residual_completion_source_theorem" in cutset["still_open"], "residual source gate missing")
    require("honest_Galerkin_C1_contractions" in cutset["still_open"], "honest Galerkin gate missing")
    require(STATUS in note and NEXT in note and "dynamic trace binding is now accepted" in note, "note missing essentials")
    print("AUDIT_PASS: dynamic dotD trace binding imported; primitive rows remain blocked by residual completion")


if __name__ == "__main__":
    main()
