"""Audit selected diagonal End0 D_E payload extraction."""

from __future__ import annotations

import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
CANDIDATE = ROOT / "candidate_data" / "selected_end0_de_payload_from_diagonal_hym.candidate.json"
CERT = ROOT / "certificates" / "selected_end0_de_payload_from_diagonal_hym_certificate.json"
PROOF = ROOT / "proof_corpus" / "MTT_Selected_End0_DE_Payload_From_Diagonal_HYM_v1.md"


def require(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)


def main() -> int:
    data = json.loads(CANDIDATE.read_text(encoding="utf-8"))
    cert = json.loads(CERT.read_text(encoding="utf-8"))
    proof = PROOF.read_text(encoding="utf-8")

    require(
        data["status"] == "MTT_SELECTED_END0_DE_DIAGONAL_PAYLOAD_BUILT_RIESZ_DOTD_TRANSFER_OPEN",
        "unexpected status",
    )
    require(data["closure_claimed"] is False, "must not claim full closure")
    require(data["target_fitting_used"] is False, "must not use target fitting")
    basis = data["selected_End0_basis"]
    require(basis["basis"] == ["T1", "T2", "T3"], "wrong End0 basis")
    require("not promoted" in basis["basis_source"], "B_N guardrail missing")
    adjoint = data["adjoint_connection_packet"]
    require(adjoint["closed"] is True, "adjoint connection should close")
    require(adjoint["ad_T3_matrix_on_basis_T1_T2_T3"] == [[0, -1, 0], [1, 0, 0], [0, 0, 0]], "wrong adT3")
    require(adjoint["ad_T3_frobenius_norm"] > 1.4, "adT3 norm too small")
    for label in ["x1", "y1", "x2", "y2"]:
        packet = data["D_E_direction_payload"][label]
        require(packet["du_l2"] > 0, f"{label} derivative should be nonzero")
        require("ad(T3)" in packet["operator_formula"], f"{label} formula missing ad(T3)")
        require(packet["connection_matrix_frobenius_l2"] > 0, f"{label} connection norm should be nonzero")
        sample = packet["sample_at_absmax_du"]
        require(len(sample["connection_matrix_value"]) == 3, f"{label} sample matrix wrong size")
    boundary = data["operator_payload_boundary"]
    require(boundary["diagonal_End0_D_E_formula_extracted"] is True, "diagonal D_E formula missing")
    require(boundary["validator_ready"] is False, "must not be validator ready")
    require(boundary["Riesz_Green_payload_extracted"] is False, "Riesz/Green must remain open")
    require(boundary["rank2_to_rank3_sector_transfer_values_extracted"] is False, "sector transfer must remain open")
    require(data["what_remains_open"]["offdiagonal_End0_vanish_or_control_bound"] is True, "offdiagonal guardrail missing")
    require(cert["diagonal_End0_D_E_payload_closed"] is True, "certificate should close diagonal End0 D_E payload")
    require(cert["validator_ready"] is False, "certificate must keep validator blocked")
    require("not a qutrit/sector promotion" in proof, "proof must state sector guardrail")

    print("PASS selected End0 D_E payload from diagonal HYM audit")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
