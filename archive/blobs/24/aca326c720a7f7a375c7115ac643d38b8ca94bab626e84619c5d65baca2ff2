from __future__ import annotations

import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
CERT = ROOT / "certificates" / "selected_riesz_green_dotd_from_diagonal_end0_de_certificate.json"
STATUS = "SELECTED_DIAGONAL_END0_RIESZ_GREEN_DOTD_PARTIAL_BUILT_ALPHA1_TRANSFER_OPEN"
NEXT = "MTT_Selected_T1T2_Covariant_Green_or_Rank2Sector_Transfer_From_Diagonal_HYM_v1"


def require(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)


def main() -> None:
    cert = json.loads(CERT.read_text(encoding="utf-8"))
    packet = json.loads(Path(cert["packet_written"]).read_text(encoding="utf-8"))
    note = Path(cert["note_written"]).read_text(encoding="utf-8")

    require(cert["status"] == STATUS, "unexpected status")
    require(cert["closure_claimed"] is False, "must not claim full closure")
    require(all(cert["checks"].values()), "all checks should pass")
    require(all(cert["what_closes_now"].values()), "all closure flags should be true")
    require(all(cert["what_remains_open"].values()), "all blockers should remain open")
    require(cert["next_required_artifact"] == NEXT, "wrong next artifact")

    protected = packet["protected_T3_lane"]
    require(protected["closed"] is True, "protected T3 lane should close")
    require(protected["ad_T3_annihilates_T3"] is True, "ad(T3) should annihilate T3")
    require("mean(f)" in protected["projector_formula"], "projector formula missing mean")
    require("-Delta" in protected["operator_reduction"], "operator reduction missing")

    green = packet["scalar_Riesz_Green_packet"]
    require(green["closed"] is True, "green packet should close")
    require(green["min_positive_eigenvalue_minus_delta"] > 39.0, "lambda1 too small")
    require(green["green_operator_norm_bound"] < 0.026, "green bound too loose")
    require(green["green_residual_l2"] < 1.0e-12, "green residual too large")
    require(green["deterministic_test_seed"] == 79, "wrong deterministic seed")

    dotd = packet["dotD_frechet_packet"]
    require(dotd["formula_closed"] is True, "formal dotD should close")
    require(dotd["physical_alpha1_driver_selected"] is False, "alpha1 driver must remain open")
    require("ad(T3)" in dotd["formal_formula"], "dotD formula missing ad(T3)")
    for label in ["x1", "y1", "x2", "y2"]:
        row = dotd["active_direction_payload"][label]
        require(row["driver_partial_s_l2"] > 0, f"{label} driver should be nonzero")
        require(row["driver_dotD_frobenius_l2"] > 0, f"{label} dotD norm should be nonzero")
        require("ad(T3)" in row["formula"], f"{label} formula missing ad(T3)")

    boundary = packet["operator_payload_boundary"]
    require(boundary["protected_T3_Riesz_payload_extracted"] is True, "T3 Riesz missing")
    require(boundary["protected_T3_Green_payload_extracted"] is True, "T3 Green missing")
    require(boundary["formal_dotD_packet_extracted"] is True, "formal dotD missing")
    require(boundary["coupled_T1T2_covariant_Riesz_Green_extracted"] is False, "T1/T2 must remain open")
    require(boundary["physical_dotD_alpha1_extracted"] is False, "physical dotD must remain open")
    require(boundary["rank2_to_sector_transfer_values_extracted"] is False, "sector transfer must remain open")
    require(boundary["validator_ready"] is False, "must not be validator ready")

    require(packet["what_remains_open"]["rank2_to_rank3_sector_transfer_values"] is True, "sector transfer blocker missing")
    require(packet["guardrails"]["does_not_use_observed_or_benchmark_data"], "benchmark guardrail missing")
    require(packet["guardrails"]["does_not_claim_physical_alpha1_derivative"], "alpha1 guardrail missing")
    require(STATUS in note and NEXT in note and "not the full validator-ready payload" in note, "note missing essentials")

    print("AUDIT_PASS: protected diagonal T3 Riesz/Green and formal dotD built; coupled/physical/sector gates remain open")


if __name__ == "__main__":
    main()
