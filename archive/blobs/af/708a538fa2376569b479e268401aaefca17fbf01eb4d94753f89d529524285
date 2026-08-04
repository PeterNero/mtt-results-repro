from __future__ import annotations

import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
CERT = ROOT / "certificates" / "selected_physical_alpha_or_action_unit_theorem_certificate.json"


def require(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)


def main() -> None:
    cert = json.loads(CERT.read_text(encoding="utf-8"))
    note = Path(cert["note_written"]).read_text(encoding="utf-8")
    closed = cert["closed_inputs"]
    result = cert["theorem_result"]
    reduction = cert["final_reduction"]
    guards = cert["guardrails"]

    require(
        cert["status"] == "ALPHA_PHYS_REDUCED_TO_SINGLE_EXTERNAL_DIMENSIONFUL_ANCHOR",
        "unexpected alpha theorem status",
    )
    require(all(closed.values()), "all alpha theorem inputs must be ready")
    require(result["alpha_int"] == 1.0, "internal alpha must be one")
    require(result["G10_int"] == 1.0, "internal G10 must be one")
    require(result["physical_numeric_alpha_selected"] is False, "physical alpha must not be selected")
    require(result["alpha_phys_status"] == "SOLE_REMAINING_EXTERNAL_DIMENSIONFUL_ANCHOR", "alpha role changed")
    require(abs(reduction["Omega0_over_sqrt_alpha_phys"] - 1.5675093859261626) < 1e-15, "Omega0 factor changed")
    require(reduction["alpha_phys_backsolve_forbidden_as_prediction"] is True, "backsolve must be forbidden")

    require(guards["uses_observed_Newton_or_Planck_input"] is False, "must not use Newton/Planck input")
    require(guards["uses_observed_Omega0_input"] is False, "must not use observed Omega0")
    require(guards["uses_theta_5TeV_as_prediction"] is False, "must not use Theta 5 TeV as prediction")
    require(guards["sets_alpha_phys_to_internal_one_as_SI_prediction"] is False, "must not confuse internal/SI units")
    require(guards["backsolves_alpha_phys_from_target"] is False, "must not backsolve alpha")
    require(guards["claims_physical_Omega0_numeric_closed"] is False, "must not claim numeric Omega0")
    require(guards["claims_Newton_or_Planck_prediction"] is False, "must not claim Newton/Planck")
    require(guards["claims_full_physical_GR_closed"] is False, "must not claim full physical GR closure")

    require("alpha_phys is the only remaining absolute normalization object" in note, "note must state sole anchor")
    require("not a missing arithmetic step" in note, "note must identify obstruction")
    require("backsolve alpha_phys" in note, "note must forbid backsolve")
    print("AUDIT_PASS: alpha_int is closed; alpha_phys is the sole remaining external dimensionful anchor")


if __name__ == "__main__":
    main()
