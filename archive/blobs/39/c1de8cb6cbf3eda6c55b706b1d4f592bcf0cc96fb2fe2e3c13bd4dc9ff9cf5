from __future__ import annotations

import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
CERT = ROOT / "certificates" / "post_alpha_residual_completion_source_promotion_or_honest_galerkin_c1_emission_certificate.json"
STATUS = "POST_ALPHA_RESIDUAL_COMPLETION_SOURCE_PROMOTION_OR_HONEST_GALERKIN_C1_EMISSION_GATE_OPEN"
NEXT = "MTT_Selected_ResidualSourceTheorem_or_GalerkinC1Run_ValueFill_v1"


def require(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)


def main() -> None:
    cert = json.loads(CERT.read_text(encoding="utf-8"))
    packet = json.loads(Path(cert["packet_written"]).read_text(encoding="utf-8"))
    note = Path(cert["note_written"]).read_text(encoding="utf-8")

    require(cert["status"] == STATUS, "unexpected status")
    require(cert["closure_claimed"] is False, "closure overclaimed")
    require(cert["SM_parity_dynamic_packet_closure_claimed"] is False, "SM parity overclaimed")
    require(cert["true_SM_equivalence_claimed"] is False, "true SM equivalence overclaimed")
    require(cert["no_knob_closure_claimed"] is False, "no-knob closure overclaimed")
    require(cert["theorem"]["proved"] is True, "promotion-gate theorem should be proved")
    require(all(cert["what_closes_now"].values()), "closed checks should pass")
    require(all(cert["what_remains_open"].values()), "open gates should remain open")
    require(all(cert["guardrails"].values()), "guardrails should hold")
    require(cert["frontier_decision"]["next_required_artifact"] == NEXT, "wrong next artifact")

    decision = packet["source_candidate_summary"]["promotion_decision"]
    for key in [
        "lane_A_promoted",
        "lane_B_promoted",
        "selected_residual_source_packet_promoted",
        "honest_Galerkin_C1_emission_promoted",
        "A_selected_promoted",
        "b_selected_promoted",
        "deltaTheta_C1_promoted",
        "SM_parity_dynamic_packet_closed",
        "no_knob_flavor_constants_closed",
    ]:
        require(decision[key] is False, f"promotion overclaimed: {key}")

    source_packet = packet["minimal_residual_source_packet"]
    require(source_packet["status"] == "TEMPLATE_EMITTED_SOURCE_THEOREM_OPEN", "source template status drift")
    require(source_packet["same_branch_source_required"] is True, "same branch source not required")
    require(source_packet["observed_data_forbidden"] is True, "observed data not forbidden")
    require(source_packet["target_fitting_forbidden"] is True, "target fitting not forbidden")
    phase = source_packet["required_source_emissions"]["phase_residual_operator_R_Z"]
    shift = source_packet["required_source_emissions"]["shift_residual_operator_R_X"]
    require(phase["selected_by_MTT_now"] is False, "phase residual overselected")
    require(shift["selected_by_MTT_now"] is False, "shift residual overselected")
    require(phase["shape"]["residual_norm_sq"] == 4.0, "phase residual norm drift")
    require(shift["shape"]["residual_norm_sq"] == 2.0, "shift residual norm drift")
    require(phase["shape"]["residual_rank"] == 2, "phase residual rank drift")
    require(shift["shape"]["residual_rank"] == 2, "shift residual rank drift")
    require(phase["shape"]["closure_error_norm_sq"] == 0.0, "phase closure error drift")
    require(shift["shape"]["closure_error_norm_sq"] == 0.0, "shift closure error drift")
    implied = source_packet["if_emitted_then"]
    require(implied["A_transpose_A"] == [[12.0, 0.0], [0.0, 12.0]], "implied Gram drift")
    require(implied["A_transpose_b"] == [12.0, 12.0], "implied b drift")
    require(implied["deltaTheta_C1"] == [1.0, 1.0], "implied deltaTheta drift")
    require(implied["rank"] == 2, "implied rank drift")

    parity = packet["sm_parity_vs_no_knob_acceptance_gate"]
    require(parity["this_repo_view"] == "SM_PARITY_FIRST", "SM parity view missing")
    require(parity["sibling_repo_default_view"] == "NO_KNOB_RESEARCH", "no-knob sibling view missing")
    require(parity["current_decision"] == "OPEN_FOR_SM_PARITY_BECAUSE_NO_TYPED_SELECTED_DYNAMIC_PACKET_IS_EMITTED_YET", "parity decision drift")
    require(parity["measured_constants_used_as_selector"] is False, "measured constants selector misuse")

    lane_a, lane_b = packet["lane_results"]
    require(lane_a["status"] == "OPEN_SOURCE_THEOREM_MISSING", "Lane A overclosed")
    require(lane_b["status"] == "OPEN_RUN_VALUES_MISSING", "Lane B overclosed")
    require(lane_a["closes_SM_parity_dynamic_packet_if_source_theorem_supplied"] is True, "Lane A parity implication missing")
    require(lane_b["closes_SM_parity_dynamic_packet_if_selected_run_emits_values"] is True, "Lane B parity implication missing")
    require(STATUS in note and NEXT in note and "minimal typed source-packet template" in note, "note missing essentials")
    print("AUDIT_PASS: residual-completion promotion gate imported; source theorem/Galerkin lanes remain open")


if __name__ == "__main__":
    main()
