from __future__ import annotations

import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
CERT = ROOT / "certificates" / "selected_gr_hessian_kernel_candidate_certificate.json"


def require(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)


def main() -> None:
    cert = json.loads(CERT.read_text(encoding="utf-8"))
    require(
        cert["status"] == "SELECTED_GR_HESSIAN_KERNEL_CANDIDATE_BUILT_SELECTION_OPEN",
        "unexpected status",
    )
    evidence = cert["evidence_patterns"]
    for key in [
        "gr_eh_reduction_formula_present",
        "gr_stress_energy_formula_present",
        "qg_tt_lichnerowicz_operator_present",
        "qg_retarded_kernel_present",
        "proto_anchor_hessian_present",
    ]:
        require(evidence[key] is True, f"missing source evidence: {key}")

    checks = cert["finite_numeric_checks"]
    require(checks["spin2_polarization_count_positive"] is True, "spin-2 polarization check failed")
    require(checks["symmetric_tensor_component_count"] == 10, "4D symmetric tensor count must be 10")
    require(checks["rho_uv_positive"] is True, "rho_UV must be positive")
    require(checks["R_star_positive"] is True, "R_star must be positive")
    require(checks["lambda_floor_positive"] is True, "lambda floor must be positive")

    gates = cert["selection_gates"]
    require(gates["EH_universality_target_identified"] is True, "EH target not identified")
    require(gates["TT_kinetic_target_identified"] is True, "TT target not identified")
    require(gates["selected_numeric_H_anchor_matrix_available"] is False, "H_anchor should remain open")
    require(gates["selected_GR_Hessian_blocks_available"] is False, "GR Hessian should remain open")
    require(gates["absolute_G_eff_normalization_available"] is False, "G_eff normalization should remain open")

    guardrails = cert["guardrails"]
    require(guardrails["claims_full_GR_derivation"] is False, "must not claim full GR")
    require(guardrails["claims_Newton_constant_prediction"] is False, "must not claim Newton prediction")
    require(
        guardrails["treats_structural_EH_reduction_as_selected_Hessian"] is False,
        "must separate EH target from selected Hessian",
    )
    require(
        0.0 < cert["gate_accounting"]["closure_ratio"] < 1.0,
        "candidate should be partially but not fully closed",
    )

    print("AUDIT_PASS: selected GR Hessian kernel candidate is built and honestly open")


if __name__ == "__main__":
    main()

