from __future__ import annotations

import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
CERT = ROOT / "certificates" / "selected_sharp_semigroup_bound_theorem_certificate.json"


def require(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)


def main() -> None:
    cert = json.loads(CERT.read_text(encoding="utf-8"))
    note = Path(cert["note_written"]).read_text(encoding="utf-8")
    closed = cert["closed_inputs"]
    proof = cert["semigroup_proof"]
    formula = cert["omega0_formula"]
    guards = cert["guardrails"]
    still_open = cert["still_open"]

    require(
        cert["status"] == "CQ1_SHARP_SEMIGROUP_BOUND_CLOSED_ALPHA_CHI_OPEN",
        "unexpected sharp semigroup status",
    )
    require(all(closed.values()), "all sharp semigroup inputs must close")
    require(proof["prefactor"] == 1.0, "C_Q must be one")
    require(proof["lambda_star"] == 15.0, "lambda_star changed")
    require(proof["schur_correction"] == 0.0, "Schur correction must be zero")
    require("self-adjoint" in proof["why_sharp"], "sharpness must be spectral-theorem based")
    require(proof["scope"] == "selected exact branch only; not a nonnormal full mixed Hessian claim", "scope guardrail changed")

    require(formula["C_Q"] == 1.0, "formula C_Q changed")
    require(abs(formula["epsilon_adm"] - 1 / 448) < 1e-15, "epsilon changed")
    require(abs(formula["Omega0_over_chi_sqrt_alpha"] - 1.5675093859261626) < 1e-15, "Omega0 factor changed")
    require(abs(formula["R1_sigma1"] - 0.6379547127299338) < 1e-15, "R1 changed")

    require(guards["uses_observed_Newton_or_Planck_input"] is False, "must not use Newton/Planck input")
    require(guards["uses_observed_Omega0_input"] is False, "must not use observed Omega0")
    require(guards["fits_C_Q_to_target"] is False, "must not fit C_Q")
    require(guards["claims_full_mixed_hessian_semigroup_is_normal"] is False, "must not overclaim full mixed Hessian")
    require(guards["claims_unconditional_full_GR_response_closed"] is False, "must not overclaim full GR")
    require(guards["claims_alpha_phys_selected"] is False, "must not close alpha")
    require(guards["claims_chi_omega_selected"] is False, "must not close chi")
    require(guards["claims_physical_Omega0_closed"] is False, "must not claim physical Omega0")

    require(still_open["alpha_phys_or_action_unit_selected"] is False, "alpha gate should remain open")
    require(still_open["chi_omega_convention_selected"] is False, "chi gate should remain open")
    require(still_open["physical_Omega0_closed"] is False, "Omega0 should remain open")

    require("C_Q = 1" in note, "note must state C_Q")
    require("does not assert a" in note and "full mixed Hessian" in note, "note must include full-Hessian guardrail")
    print("AUDIT_PASS: C_Q=1 is sharp on the selected exact branch; alpha and chi remain open")


if __name__ == "__main__":
    main()
