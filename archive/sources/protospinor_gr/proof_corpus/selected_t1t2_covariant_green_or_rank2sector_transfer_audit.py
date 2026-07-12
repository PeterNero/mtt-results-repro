from __future__ import annotations

import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
CERT = ROOT / "certificates" / "selected_t1t2_covariant_green_or_rank2sector_transfer_certificate.json"
STATUS = "SELECTED_T1T2_COVARIANT_GREEN_CLOSED_RANK2_SECTOR_TRANSFER_OPEN"
NEXT = "MTT_Selected_Rank2_to_Rank3_Sector_Transfer_or_Physical_dotD_alpha1_From_HYM_v1"


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

    identification = packet["complex_T1T2_identification"]
    require(identification["closed"] is True, "T1/T2 identification should close")
    require(identification["kernel_dimension_real"] == 2, "wrong real kernel dimension")
    require("exp(i s)" in identification["gauge_trivialization"], "gauge trivialization missing")
    require("u + i v" in identification["complex_coordinate"], "complex coordinate missing")

    green = packet["reduced_projector_and_green"]
    require(green["closed"] is True, "reduced green should close")
    require("mean(exp(i s) f)" in green["kernel_projector"], "kernel projector missing")
    require("(-Delta)^(-1)" in green["reduced_green"], "reduced Green formula missing")
    require(green["min_positive_eigenvalue"] > 39.0, "lambda1 too small")
    require(green["green_operator_norm_bound"] < 0.026, "green bound too loose")
    require(green["green_residual_l2"] < 1.0e-12, "green residual too large")
    require(green["projector_idempotence_l2"] < 1.0e-14, "projector not idempotent")
    require(green["complement_orthogonality_abs"] < 1.0e-14, "complement not orthogonal")

    aliasing = packet["finite_aliasing_boundary"]
    require(aliasing["raw_truncated_product_rule_identity_claimed"] is False, "must not claim raw product rule exactness")
    require(aliasing["direct_D_exp_minus_is_kernel_residual_l2"] >= 0.0, "diagnostic residual missing")

    boundary = packet["operator_payload_boundary"]
    require(boundary["coupled_T1T2_covariant_Riesz_Green_extracted"] is True, "T1/T2 Green missing")
    require(boundary["rank2_to_sector_transfer_values_extracted"] is False, "sector transfer must remain open")
    require(boundary["physical_dotD_alpha1_extracted"] is False, "physical alpha1 must remain open")
    require(boundary["validator_ready"] is False, "must not be validator ready")

    require(packet["guardrails"]["does_not_promote_T1T2_green_to_sector_transfer"], "sector guardrail missing")
    require(packet["guardrails"]["does_not_claim_raw_truncated_product_rule_exactness"], "aliasing guardrail missing")
    require(STATUS in note and NEXT in note and "pure-gauge complex line" in note, "note missing essentials")

    print("AUDIT_PASS: T1/T2 covariant reduced Green closed; rank2-sector and physical alpha1 remain open")


if __name__ == "__main__":
    main()
