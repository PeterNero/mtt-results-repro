from __future__ import annotations

import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
CERT = ROOT / "certificates" / "post_alpha_primitive_c1_hessian_source_map_candidate_certificate.json"
STATUS = "POST_ALPHA_PRIMITIVE_C1_HESSIAN_SOURCE_MAP_CANDIDATE_BUILT_VALUES_OPEN"
NEXT = "MTT_Selected_SourceMapSelectionTheorem_or_HonestGalerkinC1ValueRun_v1"


def require(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)


def main() -> None:
    cert = json.loads(CERT.read_text(encoding="utf-8"))
    packet = json.loads(Path(cert["packet_written"]).read_text(encoding="utf-8"))
    note = Path(cert["note_written"]).read_text(encoding="utf-8")

    require(cert["status"] == STATUS, "unexpected status")
    require(cert["closure_claimed"] is False, "must not claim closure")
    require(cert["theorem"]["proved"] is True, "source-map candidate theorem should be proved")
    require(all(cert["what_closes_now"].values()), "closed checks should pass")
    require(all(cert["what_remains_open"].values()), "open gates should remain open")
    require(all(cert["guardrails"].values()), "guardrails should hold")

    decision = cert["frontier_decision"]
    require(decision["source_map_candidate_constructed"] is True, "candidate not constructed")
    require(decision["source_map_selected_by_MTT_now"] is False, "candidate overselected")
    require(decision["frontier_is_source_map_selection_or_honest_galerkin_value_run"] is True, "wrong frontier")
    require(decision["next_required_artifact"] == NEXT, "wrong next artifact")

    candidate = packet["source_map_candidate"]
    require(candidate["selected_by_MTT_now"] is False, "source map selected")
    require(candidate["closed_support"]["Q_residual_rank"] == 6, "Q_residual rank drift")
    require(candidate["closed_support"]["strict_72_real_acceptance_target"]["total_real_coordinates"] == 72, "coordinate drift")
    require(candidate["domain"]["active_shift"] == [1, 1], "active shift drift")
    require(candidate["if_source_map_selected_then"]["rank"] == 2, "conditional rank drift")
    require(candidate["if_source_map_selected_then"]["A_transpose_A"] == [[12.0, 0.0], [0.0, 12.0]], "wrong conditional Gram")
    require(candidate["if_source_map_selected_then"]["A_transpose_b"] == [12.0, 12.0], "wrong conditional ATb")
    require(candidate["if_source_map_selected_then"]["deltaTheta_C1"] == [1.0, 1.0], "wrong conditional DeltaTheta")

    residuals = packet["candidate_residual_shapes"]
    require(residuals["phase_R_Z"]["selected_by_MTT_now"] is False, "phase residual selected")
    require(residuals["shift_R_X"]["selected_by_MTT_now"] is False, "shift residual selected")
    require(residuals["phase_R_Z"]["shape"]["residual_norm_sq"] == 4.0, "phase residual norm drift")
    require(residuals["shift_R_X"]["shape"]["residual_norm_sq"] == 2.0, "shift residual norm drift")
    require(residuals["phase_R_Z"]["shape"]["closure_error_norm_sq"] == 0.0, "phase closure error drift")
    require(residuals["shift_R_X"]["shape"]["closure_error_norm_sq"] == 0.0, "shift closure error drift")

    truth = packet["selection_obligation_kernel"]["minimal_truth_table"]
    require(truth["current_case"]["A_selected_promotes"] is False, "current A promoted")
    require(truth["current_case"]["b_selected_promotes"] is False, "current b promoted")
    require(truth["if_phase_and_shift_residual_sources_selected_and_b_source_emitted"]["A_selected_promotes"] is True, "conditional A not promoted")
    require(truth["if_phase_and_shift_residual_sources_selected_and_b_source_emitted"]["b_selected_promotes"] is True, "conditional b not promoted")
    require(packet["honest_galerkin_value_slots"]["can_replace_source_map_now"] is False, "Galerkin replacement overclaimed")
    require(STATUS in note and NEXT in note and "does not select the source map" in note, "note missing essentials")
    print("AUDIT_PASS: primitive C1/Hessian source-map candidate built; source selection remains open")


if __name__ == "__main__":
    main()
