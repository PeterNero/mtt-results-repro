from __future__ import annotations

import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
CERT = ROOT / "certificates" / "post_alpha_independent_primitive_c1_tensor_hessian_source_map_or_honest_galerkin_c1_execution_certificate.json"
STATUS = "POST_ALPHA_INDEPENDENT_PRIMITIVE_C1_TENSOR_HESSIAN_SOURCE_MAP_OR_HONEST_GALERKIN_C1_EXECUTION_IMPORTED_CANDIDATE_VALUES_OPEN"
NEXT = "MTT_Selected_SourceMapSelectionTheorem_or_HonestGalerkinC1ValueRun_v1"


def require(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)


def main() -> None:
    cert = json.loads(CERT.read_text(encoding="utf-8"))
    packet = json.loads(Path(cert["packet_written"]).read_text(encoding="utf-8"))
    note = Path(cert["note_written"]).read_text(encoding="utf-8")

    require(cert["status"] == STATUS, "unexpected status")
    require(cert["closure_claimed"] is False, "closure overclaimed")
    require(cert["theorem"]["proved"] is True, "independent source-map candidate import should be proved")
    require(all(cert["what_closes_now"].values()), "closed checks should pass")
    require(all(cert["what_remains_open"].values()), "open gates should remain open")
    require(all(cert["guardrails"].values()), "guardrails should hold")
    require(cert["frontier_decision"]["next_required_artifact"] == NEXT, "wrong next artifact")
    require(cert["frontier_decision"]["source_map_candidate_constructed"] is True, "source-map candidate not constructed")
    require(cert["frontier_decision"]["source_map_selection_open"] is True, "selection gate overclosed")

    source_map = packet["primitive_tensor_hessian_source_map_candidate"]
    require(source_map["status"] == "SOURCE_MAP_CANDIDATE_CONSTRUCTED_SELECTION_OPEN", "source-map status drift")
    require(source_map["selected_by_MTT_now"] is False, "source map overselected")
    require(source_map["closed_support"]["strict_72_real_acceptance_target"]["total_real_coordinates"] == 72, "coordinate target drift")
    require(source_map["candidate_residual_operators"]["phase_R_Z"]["shape"]["residual_norm_sq"] == 4.0, "phase residual norm drift")
    require(source_map["candidate_residual_operators"]["shift_R_X"]["shape"]["residual_norm_sq"] == 2.0, "shift residual norm drift")
    require(source_map["residual_completion_replay"]["phase_projection_plus_residual_equals_target"] is True, "phase completion drift")
    require(source_map["residual_completion_replay"]["shift_projection_plus_residual_equals_target"] is True, "shift completion drift")
    require(source_map["if_source_map_selected_then"]["A_transpose_A"] == [[12.0, 0.0], [0.0, 12.0]], "A^T A drift")
    require(source_map["if_source_map_selected_then"]["A_transpose_b"] == [12.0, 12.0], "A^T b drift")
    require(source_map["if_source_map_selected_then"]["deltaTheta_C1"] == [1.0, 1.0], "deltaTheta drift")

    kernel = packet["source_map_selection_obligation_kernel"]
    require(kernel["status"] == "SELECTION_OBLIGATION_KERNEL_BUILT_VALUES_OPEN", "kernel status drift")
    require(kernel["closed_numeric_facts"]["rank_2_condition_number_1"] is True, "rank/condition fact missing")
    require(kernel["closed_numeric_facts"]["A_transpose_A_equals_12I2"] is True, "A^T A fact missing")
    require(kernel["currently_emitted"]["selected_A_selected"] is False, "A_selected overemitted")
    require(kernel["currently_emitted"]["selected_b_selected"] is False, "b_selected overemitted")
    require(kernel["currently_emitted"]["selected_deltaTheta_C1"] is False, "deltaTheta overemitted")
    require(kernel["minimal_truth_table"]["current_case"]["phase_R_Z_selected"] is False, "phase source overselected")
    require(kernel["minimal_truth_table"]["current_case"]["shift_R_X_selected"] is False, "shift source overselected")
    require(kernel["minimal_truth_table"]["current_case"]["b_source_emitted"] is False, "b source overemitted")
    require(
        kernel["minimal_truth_table"]["if_phase_and_shift_residual_sources_selected_and_b_source_emitted"][
            "SM_parity_dynamic_packet_would_close"
        ]
        is True,
        "conditional closure implication missing",
    )
    require(kernel["strict_acceptance_field_status"]["A_selected"] == "CONDITIONAL_REFERENCE_ONLY_NOT_SELECTED", "A status drift")

    galerkin = packet["honest_galerkin_execution_value_slots"]
    require(galerkin["status"] == "HONEST_GALERKIN_EXECUTION_SLOTS_RESTATED_VALUES_OPEN", "Galerkin slot status drift")
    require(galerkin["can_replace_source_map_now"] is False, "Galerkin replacement overclaimed")
    require(galerkin["selected_source_verified"] is False, "Galerkin source overclaimed")

    require(STATUS in note and NEXT in note and "selection-obligation kernel" in note, "note missing essentials")
    print("AUDIT_PASS: long-chain primitive/Hessian source-map candidate imported; selection theorem remains open")


if __name__ == "__main__":
    main()
