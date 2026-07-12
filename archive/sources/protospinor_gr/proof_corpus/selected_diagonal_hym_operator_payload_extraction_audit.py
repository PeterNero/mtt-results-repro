from __future__ import annotations

import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
CERT = ROOT / "certificates" / "selected_diagonal_hym_operator_payload_extraction_certificate.json"
STATUS = "SELECTED_DIAGONAL_HYM_OPERATOR_PAYLOAD_EXTRACTED_END0_DE_OPEN"
NEXT = "MTT_Selected_End0_DE_Payload_From_Diagonal_HYM_v1"


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

    metric = packet["diagonal_metric_payload"]
    require(metric["closed"] is True, "metric payload should close")
    require(metric["exp_s_min"] > 0 and metric["exp_minus_s_min"] > 0, "metric must be positive")
    require(metric["determinant_max_error"] < 1e-14, "determinant error too large")
    require(metric["s_mean_abs"] < 1e-14, "s must be zero mean")

    connection = packet["diagonal_connection_payload"]
    require(connection["closed"] is True, "connection payload should close")
    require(connection["gradient_l2"] > 0, "connection should be nontrivial")
    require(connection["central_shared_circle_direction"].startswith("zero"), "central direction should vanish")

    curvature = packet["curvature_residual_payload"]
    require(curvature["closed"] is True, "curvature residual should close")
    require(curvature["residual_l2"] < 1e-12, "residual too large")

    boundary = packet["operator_payload_boundary"]
    require(boundary["diagonal_rank2_metric_connection_payload_extracted"] is True, "diagonal payload missing")
    require(boundary["validator_ready"] is False, "must not be validator ready")
    require(boundary["D_E_matrix_on_selected_End0_basis_extracted"] is False, "DE must remain open")
    require(packet["guardrails"]["does_not_promote_rank2_diagonal_payload_to_full_validator_payload"], "guardrail missing")
    require(STATUS in note and NEXT in note and "A_diag = d s * T3" in note, "note missing essentials")

    print("AUDIT_PASS: selected diagonal HYM metric/connection payload extracted; End0 D_E remains open")


if __name__ == "__main__":
    main()
