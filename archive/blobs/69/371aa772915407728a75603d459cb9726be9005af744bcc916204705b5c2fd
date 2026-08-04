from __future__ import annotations

import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
CERT = (
    ROOT
    / "certificates"
    / "post_alpha_independent_long_residual_completion_source_promotion_or_honest_galerkin_c1_emission_certificate.json"
)
STATUS = "POST_ALPHA_INDEPENDENT_LONG_RESIDUAL_COMPLETION_SOURCE_PROMOTION_OR_HONEST_GALERKIN_C1_EMISSION_GATE_OPEN"
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
    require(cert["true_SM_equivalence_claimed"] is False, "true SM overclaimed")
    require(cert["no_knob_closure_claimed"] is False, "no-knob overclaimed")
    require(cert["theorem"]["proved"] is True, "long-chain residual gate should be proved")
    require(all(cert["what_closes_now"].values()), "closed checks should pass")
    require(all(cert["what_remains_open"].values()), "open gates should remain open")
    require(all(cert["guardrails"].values()), "guardrails should hold")
    require(cert["frontier_decision"]["next_required_artifact"] == NEXT, "wrong next artifact")

    previous = packet["fresh_previous_certificate"]
    require(previous["theorem"]["proved"] is True, "previous theorem not proved")
    require(previous["frontier_decision"]["next_required_artifact"].endswith("C1_Emission_v1"), "previous frontier drift")

    source_template = packet["minimal_residual_source_packet"]
    require(source_template["status"] == "TEMPLATE_EMITTED_SOURCE_THEOREM_OPEN", "source template status drift")
    require(source_template["same_branch_source_required"] is True, "same-branch source requirement missing")
    require(source_template["observed_data_forbidden"] is True, "observed data guardrail missing")
    phase = source_template["required_source_emissions"]["phase_residual_operator_R_Z"]
    shift = source_template["required_source_emissions"]["shift_residual_operator_R_X"]
    require(phase["selected_by_MTT_now"] is False, "phase residual overselected")
    require(shift["selected_by_MTT_now"] is False, "shift residual overselected")
    require(phase["shape"]["residual_norm_sq"] == 4.0, "phase norm drift")
    require(shift["shape"]["residual_norm_sq"] == 2.0, "shift norm drift")
    require(phase["shape"]["residual_rank"] == 2, "phase rank drift")
    require(shift["shape"]["residual_rank"] == 2, "shift rank drift")
    implied = source_template["if_emitted_then"]
    require(implied["A_transpose_A"] == [[12.0, 0.0], [0.0, 12.0]], "implied Gram drift")
    require(implied["A_transpose_b"] == [12.0, 12.0], "implied b drift")
    require(implied["deltaTheta_C1"] == [1.0, 1.0], "implied deltaTheta drift")
    require(implied["rank"] == 2, "implied rank drift")

    parity = packet["sm_parity_vs_no_knob_acceptance_gate"]
    require(parity["this_repo_view"] == "SM_PARITY_FIRST", "SM parity view missing")
    require(parity["sibling_repo_default_view"] == "NO_KNOB_RESEARCH", "no-knob sibling view missing")
    require(parity["measured_constants_used_as_selector"] is False, "measured constants selector misuse")

    lane_a, lane_b = packet["lane_results"]
    require(lane_a["status"] == "OPEN_SOURCE_THEOREM_MISSING", "Lane A overclosed")
    require(lane_b["status"] == "OPEN_RUN_VALUES_MISSING", "Lane B overclosed")
    require(lane_a["closes_SM_parity_dynamic_packet_if_source_theorem_supplied"] is True, "Lane A SM implication missing")
    require(lane_b["closes_SM_parity_dynamic_packet_if_selected_run_emits_values"] is True, "Lane B SM implication missing")

    require(STATUS in note and NEXT in note and "typed residual source-packet template" in note, "note missing essentials")
    print(
        "AUDIT_PASS: reanchored long-chain residual source template emitted; "
        "source theorem/Galerkin lanes remain open"
    )


if __name__ == "__main__":
    main()
