"""Audit diagonal HYM operator payload extraction."""

from __future__ import annotations

import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
CANDIDATE = ROOT / "candidate_data" / "selected_hym_operator_payload_extraction_from_diagonal_replay.candidate.json"
CERT = ROOT / "certificates" / "selected_hym_operator_payload_extraction_from_diagonal_replay_certificate.json"
PROOF = ROOT / "proof_corpus" / "MTT_Selected_HYM_Operator_Payload_Extraction_From_Diagonal_Replay_v1.md"


def require(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)


def main() -> int:
    data = json.loads(CANDIDATE.read_text(encoding="utf-8"))
    cert = json.loads(CERT.read_text(encoding="utf-8"))
    proof = PROOF.read_text(encoding="utf-8")

    require(
        data["status"] == "MTT_SELECTED_HYM_DIAGONAL_OPERATOR_PAYLOAD_EXTRACTED_FULL_SECTOR_PAYLOAD_OPEN",
        "unexpected status",
    )
    require(data["closure_claimed"] is False, "must not claim full closure")
    require(data["target_fitting_used"] is False, "must not use target fitting")
    metric = data["diagonal_metric_payload"]
    require(metric["closed"] is True, "metric payload should close")
    require(metric["exp_u_min"] > 0 and metric["exp_minus_u_min"] > 0, "metric must be positive")
    require(metric["u_mean_abs"] < 1e-14, "u must be zero mean")
    connection = data["diagonal_connection_payload"]
    require(connection["closed"] is True, "connection payload should close")
    require(connection["gradient_l2"] > 0, "connection should be nontrivial")
    require(connection["central_z3_direction"].startswith("zero"), "central direction should vanish")
    curvature = data["curvature_residual_payload"]
    require(curvature["closed"] is True, "curvature residual should close")
    require(curvature["residual_l2"] < 1e-12, "residual too large")
    boundary = data["operator_payload_boundary"]
    require(boundary["diagonal_rank2_metric_connection_payload_extracted"] is True, "diagonal payload missing")
    require(boundary["validator_ready"] is False, "must not be validator ready")
    require(boundary["D_E_matrix_on_selected_End0_basis_extracted"] is False, "DE must remain open")
    require(data["what_remains_open"]["rank2_to_rank3_sector_transfer_values"] is True, "sector transfer must remain open")
    require(cert["diagonal_payload_closed"] is True, "certificate should close diagonal payload")
    require(cert["validator_ready"] is False, "certificate must keep validator blocked")
    require("not yet validator-ready" in proof, "proof must state guardrail")

    print("PASS selected HYM diagonal operator payload extraction audit")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
