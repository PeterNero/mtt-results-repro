from __future__ import annotations

import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
CERT = ROOT / "certificates" / "post_alpha_weylpair_source_emission_or_honest_galerkin_c1_execution_valuerun_certificate.json"
STATUS = "POST_ALPHA_WEYLPAIR_SOURCE_EMISSION_OR_HONEST_GALERKIN_C1_EXECUTION_VALUERUN_IMPORTED_PROMOTION_BLOCKED"
NEXT = "MTT_Selected_EnrichedWeylPairSourceProvenance_or_GalerkinC1Values_v1"


def require(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)


def main() -> None:
    cert = json.loads(CERT.read_text(encoding="utf-8"))
    packet = json.loads(Path(cert["packet_written"]).read_text(encoding="utf-8"))
    note = Path(cert["note_written"]).read_text(encoding="utf-8")

    require(cert["status"] == STATUS, "unexpected status")
    require(cert["closure_claimed"] is False, "closure overclaimed")
    require(cert["theorem"]["proved"] is True, "Weyl-pair value-run import should be proved")
    require(all(cert["what_closes_now"].values()), "closed checks should pass")
    require(all(cert["what_remains_open"].values()), "open gates should remain open")
    require(all(cert["guardrails"].values()), "guardrails should hold")
    require(cert["frontier_decision"]["next_required_artifact"] == NEXT, "wrong next artifact")

    decision = packet["source_candidate_summary"]["promotion_decision"]
    for key in [
        "enriched_weylpair_source_emission_promoted",
        "honest_Galerkin_C1_execution_promoted",
        "A_selected_promoted",
        "b_selected_promoted",
        "deltaTheta_C1_promoted",
        "SM_parity_dynamic_packet_closed",
        "no_knob_flavor_constants_closed",
        "true_SM_equivalence_closed",
    ]:
        require(decision[key] is False, f"promotion overclaimed: {key}")

    conditional = packet["conditional_weylpair_value_run"]
    require(conditional["status"] == "CONDITIONAL_VALUE_RUN_READY_NOT_PROMOTED", "conditional run status drift")
    require(conditional["operator_is_A_selected"] is False, "conditional operator promoted")
    require(conditional["operator_shape"] == [72, 2], "operator shape drift")
    require(conditional["rank"] == 2, "rank drift")
    require(abs(conditional["condition_number"] - 1.0) < 1e-12, "condition number drift")
    require(conditional["relative_residual"] < 1e-12, "relative residual too large")
    require(conditional["A_transpose_A_if_promoted"] == [[12.0, 0.0], [0.0, 12.0]], "A^T A drift")
    require(conditional["A_transpose_b_if_promoted"] == [12.0, 12.0], "A^T b drift")
    require(conditional["deltaTheta_C1_if_promoted"] == [1.0, 1.0], "deltaTheta drift")
    require(conditional["selected_value_promotion_allowed_now"] is False, "conditional promotion allowed unexpectedly")

    promotion = packet["weylpair_source_emission_promotion_attempt"]
    require(promotion["status"] == "PROMOTION_BLOCKED_SOURCE_EMISSION_NOT_THEOREM_DERIVED", "promotion blocker status drift")
    require(promotion["candidate_route"] == "B_enriched_weylpair_basis_transport_or_vertex_source", "candidate route drift")
    require(promotion["already_closed_support"]["target_in_weylpair_span"] is True, "span support missing")
    require(promotion["promotion_inputs_missing"]["A_selected_currently_emitted"] is False, "A_selected overemitted")
    require(promotion["promotion_inputs_missing"]["b_selected_currently_emitted"] is False, "b_selected overemitted")
    require(promotion["promotion_inputs_missing"]["rank_test_now_computable_for_selected_A"] is False, "rank test overcomputed")

    honest = packet["honest_galerkin_execution_value_run_gate"]
    require(honest["status"] == "HONEST_GALERKIN_EXECUTION_VALUES_STILL_OPEN", "honest gate status drift")
    require(honest["selected_source_verified"] is False, "honest source overclaimed")
    require(honest["would_close_SM_parity_dynamic_packet_if_values_emitted"] is True, "honest closure implication missing")
    require(honest["would_close_no_knob_flavor_constants_if_values_emitted"] is False, "honest no-knob overclaim")

    require(STATUS in note and NEXT in note and "conditional value run is numerically ready" in note, "note missing essentials")
    print("AUDIT_PASS: Weyl-pair conditional value run imported; source-emission promotion remains blocked")


if __name__ == "__main__":
    main()
