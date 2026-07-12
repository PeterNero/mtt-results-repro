from __future__ import annotations

import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
CERT = ROOT / "certificates" / "selected_modal_gap_to_physical_unit_theorem_certificate.json"


def require(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)


def main() -> None:
    cert = json.loads(CERT.read_text(encoding="utf-8"))
    note = Path(cert["note_written"]).read_text(encoding="utf-8")
    closure = cert["closure_checks"]
    open_checks = cert["open_checks"]
    theorem = cert["conditional_theorem"]
    guards = cert["guardrails"]

    require(
        cert["status"] == "CONDITIONAL_MAP_CLOSED_PHYSICAL_UNIT_COEFFICIENT_OPEN",
        "unexpected status",
    )
    require(all(closure.values()), "all structural closure checks must pass")
    require(open_checks["omega_gap_phys_selected"] is False, "omega_gap_phys must remain open")
    require(open_checks["physical_ellp_or_kappa11_selected"] is False, "ell_p/kappa11 must remain open")
    require(open_checks["physical_G10_selected"] is False, "G10 must remain open")
    require(
        open_checks["physical_Newton_or_Planck_prediction_allowed"] is False,
        "Newton/Planck prediction must remain forbidden",
    )
    require(
        open_checks["numeric_CUV_delta_ratio_source_certified"] is False,
        "C_UV/delta ratio should remain open",
    )

    require(theorem["status"] == "CONDITIONAL_ALGEBRA_CLOSED_ONLY", "conditional theorem status wrong")
    exact = theorem["conditional_map"]["exact_branch"]
    require(exact["lambda_internal"] == 15.0, "exact lambda mismatch")
    require("sqrt(15)" in exact["Lambda_gap_phys"], "physical gap formula missing")
    require("kappa_11" in theorem["statement"], "kappa_11 bridge missing")

    require(guards["claims_physical_omega_gap"] is False, "must not claim physical omega")
    require(guards["claims_physical_ellp"] is False, "must not claim ell_p")
    require(guards["claims_physical_kappa11"] is False, "must not claim kappa11")
    require(guards["claims_physical_G10"] is False, "must not claim G10")
    require(guards["claims_Newton_or_Planck_prediction"] is False, "must not claim Newton/Planck")
    require(guards["uses_observed_target_backsolve"] is False, "must not backsolve")
    require(guards["uses_Theta_5TeV_as_prediction"] is False, "must not use 5 TeV")

    require("Selected_Physical_Omega_Gap_Theorem" in note, "note must name next theorem")
    print("AUDIT_PASS: modal-gap-to-physical-unit map closed conditionally; omega_gap_phys remains open")


if __name__ == "__main__":
    main()
