from __future__ import annotations

import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
CERT = ROOT / "certificates" / "post_alpha_source_map_selection_theorem_or_honest_galerkin_c1_value_run_certificate.json"
STATUS = "POST_ALPHA_SOURCE_MAP_SELECTION_THEOREM_OR_HONEST_GALERKIN_C1_VALUE_RUN_IMPORTED_SELECTION_TEST_OPEN"
NEXT = "MTT_Selected_DifferentiatedPhiFinC1ResidualProjectorAxiom_or_GalerkinC1Execution_v1"


def require(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)


def main() -> None:
    cert = json.loads(CERT.read_text(encoding="utf-8"))
    packet = json.loads(Path(cert["packet_written"]).read_text(encoding="utf-8"))
    note = Path(cert["note_written"]).read_text(encoding="utf-8")

    require(cert["status"] == STATUS, "unexpected status")
    require(cert["closure_claimed"] is False, "closure overclaimed")
    require(cert["theorem"]["proved"] is True, "source-map selection boundary import should be proved")
    require(all(cert["what_closes_now"].values()), "closed checks should pass")
    require(all(cert["what_remains_open"].values()), "open gates should remain open")
    require(all(cert["guardrails"].values()), "guardrails should hold")
    require(cert["frontier_decision"]["next_required_artifact"] == NEXT, "wrong next artifact")

    decision = packet["source_candidate_summary"]["promotion_decision"]
    for key in [
        "selection_theorem_proved_now",
        "source_map_selected_by_MTT_now",
        "sector_response_matrices_promoted",
        "honest_Galerkin_C1_value_run_promoted",
        "A_selected_promoted",
        "b_selected_promoted",
        "deltaTheta_C1_promoted",
        "SM_parity_dynamic_packet_closed",
        "no_knob_flavor_constants_closed",
        "true_SM_equivalence_closed",
    ]:
        require(decision[key] is False, f"promotion overclaimed: {key}")

    test = packet["source_map_selection_theorem_test"]
    require(test["status"] == "SELECTION_TEST_BUILT_DYNAMIC_APPLICATION_OPEN", "selection test status drift")
    require(test["already_selected_or_closed"]["canonical_residual_projector_unique"] is True, "canonical support missing")
    require(test["selection_attempt"]["source_map_selected_now"] is False, "source map overselected")
    require(test["selection_attempt"]["physical_projector_application_promoted_now"] is False, "physical application overclaimed")
    require(test["selection_attempt"]["b_source_emitted_now"] is False, "b source overemitted")

    selected = packet["if_selected_dynamic_packet_closure"]
    require(selected["status"] == "IF_SELECTED_CLOSURE_EXACT_BUT_ANTECEDENT_OPEN", "if-selected status drift")
    require(selected["promoted_now"] is False, "if-selected packet overpromoted")
    require(selected["antecedent_required"]["phase_R_Z_selected"] is True, "phase antecedent missing")
    require(selected["antecedent_required"]["shift_R_X_selected"] is True, "shift antecedent missing")
    require(selected["antecedent_required"]["b_source_emitted"] is True, "b antecedent missing")
    require(selected["current_antecedent"]["phase_R_Z_selected"] is False, "phase overselected")
    require(selected["current_antecedent"]["b_source_emitted"] is False, "b source overselected")
    require(selected["if_selected_numeric_replay"]["A_transpose_A"] == [[12.0, 0.0], [0.0, 12.0]], "A^T A drift")
    require(selected["if_selected_numeric_replay"]["A_transpose_b"] == [12.0, 12.0], "A^T b drift")
    require(selected["if_selected_numeric_replay"]["deltaTheta_C1"] == [1.0, 1.0], "deltaTheta drift")
    require(selected["would_promote_if_antecedent_met"]["SM_parity_dynamic_packet_would_close"] is True, "closure implication missing")
    require(selected["would_promote_if_antecedent_met"]["no_knob_flavor_constants_would_close"] is False, "no-knob overclaim")

    galerkin = packet["honest_galerkin_value_run_route"]
    require(galerkin["status"] == "HONEST_GALERKIN_VALUE_RUN_ROUTE_OPEN", "Galerkin route status drift")
    require(galerkin["can_replace_source_map_now"] is False, "Galerkin route overclaimed")
    require(galerkin["selected_source_verified"] is False, "Galerkin source overclaimed")

    require(STATUS in note and NEXT in note and "antecedent open" in note, "note missing essentials")
    print("AUDIT_PASS: source-map selection test imported; differentiated PhiFinC1 axiom remains open")


if __name__ == "__main__":
    main()
