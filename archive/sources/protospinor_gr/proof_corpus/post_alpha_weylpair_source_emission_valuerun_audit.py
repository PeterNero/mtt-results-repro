from __future__ import annotations

import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
CERT = ROOT / "certificates" / "post_alpha_weylpair_source_emission_valuerun_certificate.json"
STATUS = "POST_ALPHA_WEYLPAIR_SOURCE_EMISSION_VALUERUN_READY_PROMOTION_BLOCKED"
NEXT = "MTT_Selected_EnrichedWeylPairSourceProvenance_or_GalerkinC1Values_v1"


def require(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)


def main() -> None:
    cert = json.loads(CERT.read_text(encoding="utf-8"))
    packet = json.loads(Path(cert["packet_written"]).read_text(encoding="utf-8"))
    note = Path(cert["note_written"]).read_text(encoding="utf-8")

    require(cert["status"] == STATUS, "unexpected status")
    require(cert["closure_claimed"] is False, "must not claim closure")
    require(cert["theorem"]["proved"] is True, "value-run import theorem should be proved")
    require(all(cert["what_closes_now"].values()), "closed import checks should pass")
    require(all(cert["what_remains_open"].values()), "open gates should remain open")
    require(all(cert["guardrails"].values()), "guardrails should hold")

    decision = cert["frontier_decision"]
    require(decision["frontier_is_enriched_weylpair_source_provenance_or_honest_galerkin_values"] is True, "wrong frontier")
    require(decision["conditional_value_run_ready"] is True, "conditional run should be ready")
    require(decision["conditional_value_run_promoted"] is False, "conditional run promoted")
    require(decision["next_required_artifact"] == NEXT, "wrong next artifact")

    run = packet["conditional_value_run"]
    require(run["operator_name"] == "A_weylpair_conditional", "operator name drift")
    require(run["operator_shape"] == [72, 2], "operator shape drift")
    require(run["rank"] == 2, "rank drift")
    require(run["selected_now"] is False, "conditional operator selected")
    require(run["A_transpose_A_if_promoted"] == [[12.0, 0.0], [0.0, 12.0]], "wrong A^T A")
    require(run["A_transpose_b_if_promoted"] == [12.0, 12.0], "wrong A^T b")
    require(run["deltaTheta_C1_if_promoted"] == [1.0, 1.0], "wrong DeltaTheta")

    expected = {
        "A_selected_assembled_from_theorem_derived_packet",
        "b_selected_emitted",
        "deltaTheta_C1_solve_executed",
        "same_branch_weyl_pair_source_provenance",
        "selected_source_emits_phase_like_Z_or_basis_holonomy",
        "selected_source_emits_shift_like_X_vertex_response",
    }
    require(set(cert["missing_source_obligations"]) == expected, "missing obligation set drift")
    require(packet["already_closed_support"]["source_level_weyl_carrier_proved"] is True, "source carrier support lost")
    require(packet["already_closed_support"]["active_shift_proved"] is True, "active shift support lost")
    require("linear_response_matrices" in packet["honest_galerkin_required_outputs"], "honest outputs lost")
    require(STATUS in note and NEXT in note and "not promoted" in note, "note missing essentials")
    print("AUDIT_PASS: Weyl-pair value run ready but promotion remains source-blocked")


if __name__ == "__main__":
    main()
