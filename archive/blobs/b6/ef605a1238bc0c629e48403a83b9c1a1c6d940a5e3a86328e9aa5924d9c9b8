"""Audit the two-path T1/T2 Green versus sector-transfer probe."""

from __future__ import annotations

import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
CANDIDATE = ROOT / "candidate_data" / "selected_t1t2_covariant_green_and_transfer_probe.candidate.json"
CERT = ROOT / "certificates" / "selected_t1t2_covariant_green_and_transfer_probe_certificate.json"
PROOF = ROOT / "proof_corpus" / "MTT_Selected_T1T2_Covariant_Green_or_Rank2Sector_Transfer_From_Diagonal_HYM_v1.md"


def require(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)


def main() -> int:
    data = json.loads(CANDIDATE.read_text(encoding="utf-8"))
    cert = json.loads(CERT.read_text(encoding="utf-8"))
    proof = PROOF.read_text(encoding="utf-8")

    require(
        data["status"] == "MTT_SELECTED_T1T2_COVARIANT_GREEN_CLOSED_TRANSFER_STILL_OPEN",
        "unexpected status",
    )
    require(data["closure_claimed"] is False, "must not claim full closure")
    require(data["target_fitting_used"] is False, "must not use target fitting")
    path_a = data["path_A_straight_T1T2_covariant_Green"]
    require(path_a["closed"] is True and path_a["converged"] is True, "path A should close")
    require("pure gauge" in path_a["flatness_reason"], "pure gauge reason missing")
    require(path_a["numerical_replay"]["gauge_frame_residual_l2"] < 1e-12, "gauge-frame residual too large")
    require(path_a["numerical_replay"]["direct_truncated_replay_converged"] is False, "direct truncated replay should remain diagnostic")
    require("Diagnostic only" in path_a["numerical_replay"]["direct_truncated_residual_interpretation"], "aliasing guardrail missing")
    path_b = data["path_B_superset_rank2_to_sector_transfer"]
    require(path_b["abstract_End0_functor_closed"] is True, "abstract transfer support should be closed")
    require(path_b["BN_identification_rejected_at_selected_End0_level"] is True, "B_N rejection should persist")
    require(path_b["closed"] is False and path_b["converged"] is False, "path B must remain open")
    boundary = data["operator_payload_boundary"]
    require(boundary["T1_T2_coupled_covariant_Riesz_Green_extracted"] is True, "T1/T2 Green missing")
    require(boundary["full_End0_Riesz_Green_extracted"] is True, "full diagonal End0 Green missing")
    require(boundary["rank2_to_rank3_sector_transfer_values_extracted"] is False, "sector transfer must remain open")
    require(boundary["physical_dotD_alpha1_payload_extracted"] is False, "physical dotD must remain open")
    require(boundary["validator_ready"] is False, "must not be validator ready")
    require(data["what_remains_open"]["offdiagonal_Ext_HYM_terms_vanish_or_control_bound"] is True, "offdiagonal guardrail missing")
    require(cert["path_A_T1T2_covariant_Green_closed"] is True, "certificate should close path A")
    require(cert["path_B_rank2_to_sector_transfer_closed"] is False, "certificate should keep path B open")
    require("Path B: Superset Sector Transfer" in proof, "proof must document both paths")
    require("direct finite spectral replay" in proof, "proof must document diagnostic direct replay")

    print("PASS selected T1/T2 covariant Green and transfer probe audit")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
