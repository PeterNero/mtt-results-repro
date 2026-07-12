from __future__ import annotations

import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
CERT = ROOT / "certificates" / "post_alpha_differentiated_residual_projector_source_rule_or_honest_galerkin_c1_execution_certificate.json"
STATUS = "POST_ALPHA_DIFFERENTIATED_RESIDUAL_PROJECTOR_SOURCE_RULE_OR_HONEST_GALERKIN_C1_EXECUTION_IMPORTED_SOURCE_RULE_CONTRACT_OPEN"
NEXT = "MTT_Selected_WeylPairSourceEmission_or_HonestGalerkinC1Execution_ValueRun_v1"


def require(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)


def main() -> None:
    cert = json.loads(CERT.read_text(encoding="utf-8"))
    packet = json.loads(Path(cert["packet_written"]).read_text(encoding="utf-8"))
    note = Path(cert["note_written"]).read_text(encoding="utf-8")

    require(cert["status"] == STATUS, "unexpected status")
    require(cert["closure_claimed"] is False, "closure overclaimed")
    require(cert["theorem"]["proved"] is True, "differentiated source-rule cutset should be proved")
    require(all(cert["what_closes_now"].values()), "closed checks should pass")
    require(all(cert["what_remains_open"].values()), "open gates should remain open")
    require(all(cert["guardrails"].values()), "guardrails should hold")
    require(cert["frontier_decision"]["next_required_artifact"] == NEXT, "wrong next artifact")

    decision = packet["source_candidate_summary"]["promotion_decision"]
    for key in [
        "differentiated_residual_projector_source_rule_promoted",
        "enriched_weylpair_source_emission_promoted",
        "honest_Galerkin_C1_execution_promoted",
        "selected_A_selected_promoted",
        "selected_b_selected_promoted",
        "selected_deltaTheta_C1_promoted",
        "SM_parity_dynamic_packet_closed",
        "no_knob_flavor_constants_closed",
        "true_SM_equivalence_closed",
    ]:
        require(decision[key] is False, f"promotion overclaimed: {key}")

    source_rule = packet["differentiated_residual_projector_source_rule_contract"]
    require(source_rule["status"] == "SOURCE_RULE_CONTRACT_EMITTED_VALUES_OPEN", "source rule status drift")
    require(source_rule["already_selected_support"]["Q_residual_rank"] == 6, "Q rank drift")
    require(source_rule["currently_emitted"]["selected_differentiated_residual_projector_source_rule"] is False, "source rule overemitted")
    require(source_rule["why_selector_is_not_enough"]["stationary_transport_only_ruled_out"] is True, "stationary no-go missing")

    conditional = source_rule["exact_conditional_values_if_rule_is_proved"]
    require(conditional["A_transpose_A"] == [[12.0, 0.0], [0.0, 12.0]], "conditional A^T A drift")
    require(conditional["A_transpose_b"] == [12.0, 12.0], "conditional A^T b drift")
    require(conditional["deltaTheta_C1"] == [1.0, 1.0], "conditional deltaTheta drift")
    require(conditional["SM_parity_dynamic_packet_would_close"] is True, "conditional closure implication missing")
    require(conditional["no_knob_flavor_constants_would_close"] is False, "conditional no-knob overclaim")

    ladder = packet["source_rule_or_execution_route_ladder"]
    require(ladder["status"] == "ROUTE_LADDER_RANKED_NO_PROMOTION", "route ladder status drift")
    require(ladder["recommended_next"] == "B_enriched_weylpair_basis_transport_or_vertex_source", "recommended next drift")
    require(ladder["near_straight_source_path"]["algebraically_sufficient"] is True, "algebraic sufficiency missing")
    require(ladder["straight_path"]["current_status"] == "OPEN_NEW_SOURCE_RULE_REQUIRED", "straight path overclaimed")
    require(ladder["superset_execution_path"]["selected_source_verified"] is False, "Galerkin source overclaimed")

    execution = packet["honest_galerkin_c1_execution_requirement"]
    require(execution["status"] == "HONEST_EXECUTION_REQUIREMENT_REEMITTED_VALUES_OPEN", "execution requirement drift")
    require(execution["selected_source_verified"] is False, "execution source overclaimed")
    require(execution["would_close_SM_parity_dynamic_packet_if_values_emitted"] is True, "execution implication missing")
    require(execution["would_close_no_knob_flavor_constants_if_values_emitted"] is False, "execution no-knob overclaim")

    require(STATUS in note and NEXT in note and ladder["recommended_next"] in note, "note missing essentials")
    print("AUDIT_PASS: differentiated residual-projector source-rule contract imported; Weyl-pair emission is next")


if __name__ == "__main__":
    main()
