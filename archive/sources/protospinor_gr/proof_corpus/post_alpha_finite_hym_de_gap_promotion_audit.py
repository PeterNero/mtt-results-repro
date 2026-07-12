from __future__ import annotations

import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
CERT = ROOT / "certificates" / "post_alpha_finite_hym_de_gap_promotion_certificate.json"
STATUS = "POST_ALPHA_FINITE_HYM_DE_GAP_PROMOTED_DOTD_SOURCE_OPEN"
NEXT = "Selected_U1Y_RouteC_dotDAlpha1_SourceNormalization_or_End0SectorRouting_v1"


def require(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)


def main() -> None:
    cert = json.loads(CERT.read_text(encoding="utf-8"))
    packet = json.loads(Path(cert["packet_written"]).read_text(encoding="utf-8"))
    note = Path(cert["note_written"]).read_text(encoding="utf-8")

    require(cert["status"] == STATUS, "unexpected status")
    require(cert["closure_claimed"] is False, "must not claim closure")
    require(cert["full_finite_HYM_connection_solve_closed"] is False, "full HYM must remain open")
    require(cert["dotD_alpha1_source_closed"] is False, "dotD source must remain open")
    require(all(cert["checks"].values()), "all certificate checks should pass")

    require(packet["theorem"]["proved"] is True, "theorem should be proved")
    promoted = packet["promoted_finite_routec_payload"]
    require(promoted["finite_basis_BN"]["basis_dimension"] == 27, "wrong BN dimension")
    require(promoted["finite_basis_BN"]["selected_trace_equality_proved"] is True, "trace equality should be proved")
    require(promoted["DE_action"]["D_E_source_flags_are_theorem_derived"] is True, "DE source flags should be theorem-derived")
    require(promoted["DE_action"]["D_E_honest_replay_passes_after_theorem_derived_source_flags"] is True, "DE replay should pass")
    require(promoted["DE_action"]["selected_trace_equality"]["zero_cluster_indices"] == [12, 13, 14], "wrong zero cluster")
    require(promoted["riesz_gap"]["selected_eta_N"] < promoted["riesz_gap"]["eta_threshold"], "eta must sit below threshold")
    require(promoted["riesz_gap"]["selected_gap_lower_bound"] > 0, "gap should be positive")
    require(promoted["reduced_green"]["Riesz_Green_layer_closes"] is True, "Green layer should close")
    require(promoted["reduced_green"]["selected_green_norm_bound"] > 0, "Green norm should be positive")

    alpha = packet["alpha1_frontier"]["analytic_formula"]
    require(alpha["status"] == "ANALYTIC_FORMULA_PROVED_SELECTED_TANGENT_VALUES_OPEN", "alpha1 formula should be source-open")
    require(
        alpha["what_the_formula_closes"]["analytic_riesz_projection_derivative_formula"] is True,
        "Riesz formula should close",
    )
    require(alpha["what_the_formula_does_not_close"]["selected_alpha1_tangent_parameter"] is True, "selected tangent should remain open")
    require(alpha["what_the_formula_does_not_close"]["selected_retarded_overlap_values"] is True, "overlap values should remain open")

    open_payload = packet["still_open_finite_routec_payload"]
    require("selected tangent/source normalization open" in open_payload["dotD_alpha1"], "dotD source should remain open")
    require("full connection lift remains open" in open_payload["local_A01_or_discrete_connection_variables"], "connection lift should remain open")
    require("selected primitive/non-invariant C1 values open" in open_payload["primitive_C1_contractions"], "C1 should remain open")

    require(packet["next_required_artifact"] == NEXT, "wrong next artifact")
    require(all(packet["what_closes_now"].values()), "closure flags should pass")
    require(all(packet["what_remains_open"].values()), "open flags should remain")
    require(all(packet["guardrails"].values()), "guardrails should hold")
    require(STATUS in note and NEXT in note and "selected gap lower bound" in note, "note missing essentials")

    print("AUDIT_PASS: finite HYM D_E gap/Riesz/Green layer promoted; dotD source remains open")


if __name__ == "__main__":
    main()
