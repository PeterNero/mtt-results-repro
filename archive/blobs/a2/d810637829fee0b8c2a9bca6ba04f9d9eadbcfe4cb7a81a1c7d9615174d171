from __future__ import annotations

import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
CERT = ROOT / "certificates" / "selected_scalar_exps_to_full_hym_row_model_lift_certificate.json"
STATUS = "SELECTED_SCALAR_EXPS_TO_FULL_HYM_ROW_MODEL_LIFT_PROVED_OPERATOR_PAYLOAD_OPEN"
NEXT = "MTT_Selected_Diagonal_HYM_Operator_Payload_Extraction_v1"


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

    theorem = packet["theorem"]
    require(theorem["proved"] is True, "row-model theorem should be proved")
    proof = packet["proof_reduction"]
    require(proof["selected_holomorphic_structure"]["single_active_ext_row"] == "eta_00", "wrong row")
    require(proof["metric_ansatz"]["determinant"] == "det(H)=1 pointwise", "det one missing")
    require(proof["offdiagonal_equations"]["offdiagonal_hym_residual"] == 0, "offdiag must vanish")
    require(proof["diagonal_tracefree_equation"]["finite_grid_residual_l2"] < 1e-12, "scalar residual too large")
    require(proof["coercivity"]["zero_mean_bound"] > 39.0, "coercivity missing")

    payload = packet["closed_row_model_payload"]
    require(payload["H"] == "diag(exp(s), exp(-s))", "metric payload wrong")
    require(payload["A_diag"] == "d s * T3", "connection payload wrong")
    require(payload["finite_residual_l2"] < 1e-12, "row model residual too large")

    guards = packet["guardrails"]
    require(guards["proves_full_hym_only_inside_selected_one_row_model"], "scope guard missing")
    require(guards["does_not_claim_continuum_truncation_from_finite_residual"], "truncation guard missing")
    require(guards["does_not_promote_to_SM_sector_payload"], "sector guard missing")
    require(STATUS in note and NEXT in note and "off-diagonal HYM residual = 0" in note, "note missing essentials")

    print("AUDIT_PASS: scalar exp(S) replay lifted to full selected row-model HYM; operator payload remains open")


if __name__ == "__main__":
    main()
