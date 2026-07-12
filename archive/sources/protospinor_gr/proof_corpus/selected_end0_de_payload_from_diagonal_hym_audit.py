from __future__ import annotations

import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
CERT = ROOT / "certificates" / "selected_end0_de_payload_from_diagonal_hym_certificate.json"
STATUS = "SELECTED_END0_DE_DIAGONAL_PAYLOAD_BUILT_RIESZ_DOTD_TRANSFER_OPEN"
NEXT = "MTT_Selected_Riesz_Green_dotD_From_Diagonal_End0_DE_v1"


def require(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)


def main() -> None:
    cert = json.loads(CERT.read_text(encoding="utf-8"))
    packet = json.loads(Path(cert["packet_written"]).read_text(encoding="utf-8"))
    note = Path(cert["note_written"]).read_text(encoding="utf-8")

    require(cert["status"] == STATUS, "unexpected status")
    require(cert["closure_claimed"] is False, "must not claim downstream closure")
    require(all(cert["checks"].values()), "all checks should pass")
    require(all(cert["what_closes_now"].values()), "all closure flags should be true")
    require(all(cert["what_remains_open"].values()), "all blockers should remain open")
    require(cert["next_required_artifact"] == NEXT, "wrong next artifact")

    basis = packet["selected_End0_basis"]
    require(basis["basis"] == ["T1", "T2", "T3"], "wrong End0 basis")
    require("not promoted" in basis["basis_source"], "B_N guardrail missing")

    adjoint = packet["adjoint_connection_packet"]
    require(adjoint["closed"] is True, "adjoint connection should close")
    require(adjoint["ad_T3_matrix_on_basis_T1_T2_T3"] == [[0, -1, 0], [1, 0, 0], [0, 0, 0]], "wrong adT3")
    require(adjoint["ad_T3_frobenius_norm"] > 1.4, "adT3 norm too small")
    require(adjoint["central_shared_circle_directions"]["x3"]["ds"] == 0.0, "x3 should vanish")
    require(adjoint["central_shared_circle_directions"]["y3"]["ds"] == 0.0, "y3 should vanish")

    for label in ["x1", "y1", "x2", "y2"]:
        row = packet["D_E_direction_payload"][label]
        require(row["ds_l2"] > 0, f"{label} derivative should be nonzero")
        require("ad(T3)" in row["operator_formula"], f"{label} formula missing ad(T3)")
        require(row["connection_matrix_frobenius_l2"] > 0, f"{label} connection norm should be nonzero")
        require(len(row["sample_at_absmax_ds"]["connection_matrix_value"]) == 3, f"{label} sample matrix wrong size")

    boundary = packet["operator_payload_boundary"]
    require(boundary["diagonal_End0_D_E_formula_extracted"] is True, "diagonal D_E formula missing")
    require(boundary["validator_ready"] is False, "must not be validator ready")
    require(boundary["Riesz_Green_payload_extracted"] is False, "Riesz/Green must remain open")
    require(boundary["rank2_to_sector_transfer_values_extracted"] is False, "sector transfer must remain open")
    require(packet["what_remains_open"]["offdiagonal_End0_vanish_or_control_bound"] is True, "offdiagonal guardrail missing")
    require(packet["guardrails"]["does_not_promote_to_qutrit_or_sector_payload"], "sector guardrail missing")
    require(STATUS in note and NEXT in note and "not a qutrit/sector promotion" in note, "note missing essentials")

    print("AUDIT_PASS: selected End0 D_E payload from diagonal HYM built; Riesz/dotD/transfer remain open")


if __name__ == "__main__":
    main()
