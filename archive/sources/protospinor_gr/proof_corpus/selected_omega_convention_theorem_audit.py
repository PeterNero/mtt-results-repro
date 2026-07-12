from __future__ import annotations

import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
CERT = ROOT / "certificates" / "selected_omega_convention_theorem_certificate.json"


def require(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)


def main() -> None:
    cert = json.loads(CERT.read_text(encoding="utf-8"))
    note = Path(cert["note_written"]).read_text(encoding="utf-8")
    closed = cert["closed_inputs"]
    convention = cert["convention_selection"]
    formula = cert["reduced_formula"]
    guards = cert["guardrails"]
    still_open = cert["still_open"]

    require(cert["status"] == "CHI_OMEGA_CONVENTION_CLOSED_ALPHA_OPEN", "unexpected omega convention status")
    require(all(closed.values()), "all omega convention inputs must close")
    require(convention["chi_omega"] == 1.0, "chi_omega must be one")
    require("not a physical parameter" in convention["why_not_physical_parameter"], "must classify chi as convention")
    require(abs(formula["Omega0_over_sqrt_alpha_phys"] - 1.5675093859261626) < 1e-15, "Omega0 factor changed")
    require(abs(formula["omega_gap_phys_over_sqrt_alpha_phys"] - 1.0702303196927971) < 1e-15, "omega gap factor changed")
    require(abs(formula["Lambda_gap_phys_over_sqrt_alpha_phys"] - 4.144984204776443) < 1e-15, "Lambda gap factor changed")

    require(guards["uses_observed_Newton_or_Planck_input"] is False, "must not use Newton/Planck input")
    require(guards["uses_observed_Omega0_input"] is False, "must not use observed Omega0")
    require(guards["fits_chi_omega_to_target"] is False, "must not fit chi")
    require(guards["adds_dimensionless_physical_parameter"] is False, "must not add parameter")
    require(guards["claims_alpha_phys_selected"] is False, "must not close alpha")
    require(guards["claims_physical_Omega0_numeric_closed"] is False, "must not claim physical Omega0")
    require(guards["claims_Newton_or_Planck_prediction"] is False, "must not claim Newton/Planck")

    require(still_open["alpha_phys_or_action_unit_selected"] is False, "alpha must remain open")
    require(still_open["physical_Omega0_numeric_closed"] is False, "physical Omega0 must remain open")
    require("chi_omega = 1" in note, "note must state chi")
    require("Only the actual physical action/unit anchor remains" in note, "note must identify remaining gate")
    print("AUDIT_PASS: chi_omega=1 convention closed; alpha_phys remains the sole Omega0 gate")


if __name__ == "__main__":
    main()
