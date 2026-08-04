"""Audit off-diagonal Ext control / sector-transfer gate."""

from __future__ import annotations

import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
CANDIDATE = ROOT / "candidate_data" / "selected_offdiagonal_ext_control_or_sector_transfer.candidate.json"
CERT = ROOT / "certificates" / "selected_offdiagonal_ext_control_or_sector_transfer_certificate.json"
PROOF = ROOT / "proof_corpus" / "MTT_Selected_OffDiagonal_Ext_Control_or_SectorTransfer_From_Full_Diagonal_End0_Green_v1.md"


def require(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)


def main() -> int:
    data = json.loads(CANDIDATE.read_text(encoding="utf-8"))
    cert = json.loads(CERT.read_text(encoding="utf-8"))
    proof = PROOF.read_text(encoding="utf-8")

    require(
        data["status"] == "MTT_SELECTED_ROW_MODEL_OFFDIAGONAL_EXT_CONTROL_CLOSED_SECTOR_TRANSFER_OPEN",
        "unexpected status",
    )
    require(data["closure_claimed"] is False, "must not claim full closure")
    require(data["target_fitting_used"] is False, "must not use target fitting")
    path_a = data["path_A_straight_offdiagonal_Ext_control"]
    require(path_a["closed"] is True, "row-model offdiagonal control should close")
    require(path_a["selected_Ext_matrix"] == "E12", "wrong Ext matrix")
    pairings = path_a["trace_pairings"]
    require(pairings["T1_trace_pairing"] == 0.0, "T1 source should vanish")
    require(pairings["T2_trace_pairing"] == 0.0, "T2 source should vanish")
    require(pairings["T3_trace_pairing"] != 0.0, "T3 source should be nonzero")
    require(path_a["uses_full_diagonal_End0_Green"] is True, "full diagonal Green should be available")
    path_b = data["path_B_superset_sector_transfer"]
    require(path_b["closed"] is False, "sector transfer must remain open")
    require(path_b["q79_supports_same_missing_gate"] is True, "q79 should support same missing gate")
    boundary = data["operator_payload_boundary"]
    require(boundary["row_model_offdiagonal_T1T2_source_controlled"] is True, "offdiag control missing")
    require(boundary["physical_dotD_alpha1_payload_extracted"] is False, "physical dotD must remain open")
    require(boundary["rank2_to_rank3_sector_transfer_values_extracted"] is False, "sector transfer must remain open")
    require(boundary["validator_ready"] is False, "must not be validator ready")
    require(data["what_remains_open"]["full_AH_Cech_offdiagonal_control_beyond_single_row_model"] is True, "row-model scope guardrail missing")
    require(cert["row_model_offdiagonal_control_closed"] is True, "certificate should close row-model control")
    require(cert["sector_transfer_closed"] is False, "certificate should keep sector transfer open")
    require("Path B: Superset Sector Transfer" in proof, "proof must document both paths")
    require("only in the selected `eta_00` row model" in proof, "proof must state scope guardrail")

    print("PASS selected off-diagonal Ext control or sector transfer audit")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
