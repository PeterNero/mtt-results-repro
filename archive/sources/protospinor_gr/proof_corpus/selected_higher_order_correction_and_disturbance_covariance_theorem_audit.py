from __future__ import annotations

import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
CERT = ROOT / "certificates" / "selected_higher_order_correction_and_disturbance_covariance_theorem_certificate.json"


def require(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)


def main() -> None:
    cert = json.loads(CERT.read_text(encoding="utf-8"))
    note = Path(cert["note_written"]).read_text(encoding="utf-8")
    closed = cert["closed_inputs"]
    primitives = cert["primitive_source_objects"]
    formula = cert["repaired_rho_formula"]
    open_gates = cert["open_gates"]
    guards = cert["guardrails"]

    require(
        cert["status"] == "SOURCE_DATA_THEOREM_REDUCED_TO_QTAU_CUV_AND_OMEGA0",
        "unexpected source-data theorem status",
    )
    require(all(closed.values()), "all imported positive/negative inputs must be settled")

    require(primitives["C_UV"]["current_status"].startswith("symbolic support"), "C_UV status wrong")
    require(primitives["Q_tau"]["current_status"] == "not supplied by current corpus", "Q_tau status wrong")
    require(primitives["Omega_0"]["current_status"] == "not selected", "Omega_0 status wrong")

    require(formula["G_11"] == 1.0, "G_11 must be closed as 1")
    require(formula["D_raw_norm_squared"] == "d_Q = int_R P K_ret Q_tau K_ret^* P^* dt", "D norm formula changed")
    require(formula["rho_UV"] == "C_UV^2 / delta = ||U||^2 / d_Q", "rho formula changed")
    require(formula["Lambda_gap_phys"] == "sqrt(15) * Omega_0 / s_star", "physical gap formula changed")

    require(open_gates["selected_higher_order_correction_functional_evaluated"] is False, "C_UV gate should remain open")
    require(open_gates["selected_finite_memory_covariance_Q_tau_derived"] is False, "Q_tau gate should remain open")
    require(open_gates["projected_covariance_integral_d_Q_evaluated"] is False, "d_Q gate should remain open")
    require(open_gates["same_branch_fluctuation_dissipation_theorem"] is False, "FD gate should remain open")
    require(open_gates["physical_Omega_0_selected"] is False, "Omega_0 gate should remain open")

    require(guards["sets_D_raw_norm_to_one"] is False, "must not set D_raw norm to one")
    require(guards["imports_threshold_delta_as_covariance"] is False, "must not import threshold delta")
    require(guards["uses_observed_Newton_or_Planck"] is False, "must not use observed constants")
    require(guards["claims_C_UV_numeric"] is False, "must not claim C_UV numeric")
    require(guards["claims_Q_tau_numeric"] is False, "must not claim Q_tau numeric")
    require(guards["claims_Omega_0_numeric"] is False, "must not claim Omega_0 numeric")

    require("Q_tau" in note and "C_UV" in note and "Omega_0" in note, "note must name all primitives")
    require("int_R P K_ret Q_tau K_ret^* P^* dt" in note, "note must include covariance integral")
    print("AUDIT_PASS: source-data theorem reduced to C_UV, Q_tau, and Omega_0")


if __name__ == "__main__":
    main()
