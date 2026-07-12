from __future__ import annotations

import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
CERT = ROOT / "certificates" / "dimensional_metrology_no_go_and_relative_closure_theorem_certificate.json"


def require(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)


def main() -> None:
    cert = json.loads(CERT.read_text(encoding="utf-8"))
    packet = json.loads(Path(cert["packet_written"]).read_text(encoding="utf-8"))
    note = Path(cert["note_written"]).read_text(encoding="utf-8")
    no_go = cert["no_go"]
    verdict = cert["verdict"]
    closure = cert["closure_result"]
    guards = cert["guardrails"]
    sol = cert["solution_family"]["dimensionless_branch_solution"]

    require(
        cert["status"] == "RELATIVE_PHYSICAL_SCALE_SOLUTION_CLOSED_ABSOLUTE_METROLOGY_REQUIRED",
        "unexpected metrology theorem status",
    )
    require(all(cert["closed_inputs"].values()), "all metrology theorem inputs must be closed")
    require(verdict["calculated_solution"] is True, "solution must be calculated")
    require(verdict["relative_solution_closed"] is True, "relative solution must close")
    require(verdict["absolute_solution_closed_without_metrology"] is False, "absolute closure must remain blocked")
    require(closure["relative_physical_closure"] is True, "relative closure flag must be true")
    require(closure["absolute_SI_closure"] is False, "absolute SI closure flag must be false")
    require(packet["relative_physical_closure"] is True, "packet relative closure must be true")
    require(packet["absolute_SI_closure"] is False, "packet absolute closure must be false")

    require(abs(sol["tau_int"] - 0.40698621549433234) < 1e-15, "tau changed")
    require(abs(sol["ell_coh_over_alpha_phys_minus_half"] - 0.6379547127299338) < 1e-15, "ell factor changed")
    require(abs(sol["Lambda_eff_over_sqrt_alpha_phys"] - 1.5675093859261626) < 1e-15, "lambda factor changed")
    require(abs(sol["invariant_product"] - 1.0) < 1e-15, "ell*lambda invariant must be one")

    require(no_go["status"] == "PROVED_IN_CURRENT_FORMALIZATION", "no-go status changed")
    require(no_go["free_parameter_count_for_absolute_units"] == 1, "absolute unit count must be one")
    require(no_go["free_parameter_count_for_relative_predictions"] == 0, "relative parameter count must be zero")

    require("alpha_phys = tau_int / L0^2" in note, "note must give length-anchor solution")
    require("alpha_phys = tau_int * E0^2" in note, "note must give energy-anchor solution")
    require("relative physical scale solution: CLOSED" in note, "note must state relative closure")
    require("absolute SI scale without metrology: NOT AVAILABLE" in note, "note must state absolute nonclosure")

    require(guards["claims_absolute_SI_prediction_without_anchor"] is False, "must not claim SI prediction")
    require(guards["sets_alpha_phys_to_one_as_physics"] is False, "must not set alpha=1 as physics")
    require(guards["backsolves_from_Newton_or_Planck"] is False, "must not backsolve Newton/Planck")
    require(guards["backsolves_from_cosmology_or_masses"] is False, "must not backsolve observed targets")
    require(guards["uses_Theta_5TeV_as_prediction"] is False, "must not use 5 TeV")
    require(guards["counts_metrological_primitive_as_sector_knob"] is False, "metrology primitive is not a sector knob")

    print("AUDIT_PASS: relative physical scale solution closed; absolute SI closure requires one metrological primitive")


if __name__ == "__main__":
    main()
