"""Audit protected diagonal-lane Riesz/Green/dotD extraction."""

from __future__ import annotations

import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
CANDIDATE = ROOT / "candidate_data" / "selected_riesz_green_dotd_from_diagonal_end0_de.candidate.json"
CERT = ROOT / "certificates" / "selected_riesz_green_dotd_from_diagonal_end0_de_certificate.json"
PROOF = ROOT / "proof_corpus" / "MTT_Selected_Riesz_Green_dotD_From_Diagonal_End0_DE_v1.md"


def require(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)


def main() -> int:
    data = json.loads(CANDIDATE.read_text(encoding="utf-8"))
    cert = json.loads(CERT.read_text(encoding="utf-8"))
    proof = PROOF.read_text(encoding="utf-8")

    require(
        data["status"] == "MTT_SELECTED_DIAGONAL_END0_RIESZ_GREEN_DOTD_PARTIAL_BUILT_ALPHA1_TRANSFER_OPEN",
        "unexpected status",
    )
    require(data["closure_claimed"] is False, "must not claim full closure")
    require(data["target_fitting_used"] is False, "must not use target fitting")
    protected = data["protected_T3_lane"]
    require(protected["closed"] is True, "protected T3 lane should close")
    require("ad(T3) kills" in protected["reason"], "protected-lane reason missing")
    require(protected["min_positive_eigenvalue_minus_delta"] > 39.0, "gap too small")
    require(protected["green_operator_norm_bound"] < 0.026, "Green bound too large")
    replay = data["numerical_green_replay"]
    require(replay["green_residual_l2"] < 1e-12, "Green residual too large")
    dotd = data["dotD_frechet_packet"]
    require(dotd["formula_closed"] is True, "dotD Frechet formula should close")
    require(dotd["physical_alpha1_driver_selected"] is False, "alpha1 driver must remain open")
    require("not emitted" in dotd["why_alpha1_still_open"], "alpha1 guardrail missing")
    boundary = data["operator_payload_boundary"]
    require(boundary["protected_T3_Riesz_projector_extracted"] is True, "Riesz missing")
    require(boundary["protected_T3_reduced_Green_extracted"] is True, "Green missing")
    require(boundary["physical_dotD_alpha1_payload_extracted"] is False, "physical dotD must remain open")
    require(boundary["T1_T2_coupled_covariant_Green_extracted"] is False, "T1/T2 Green must remain open")
    require(boundary["validator_ready"] is False, "must not be validator ready")
    require(data["what_remains_open"]["rank2_to_rank3_sector_transfer_values"] is True, "sector transfer guardrail missing")
    require(cert["protected_T3_lane_closed"] is True, "certificate should close protected lane")
    require(cert["validator_ready"] is False, "certificate must keep validator blocked")
    require("not full validator-ready" in proof, "proof must state validator guardrail")

    print("PASS selected Riesz/Green/dotD from diagonal End0 D_E audit")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
