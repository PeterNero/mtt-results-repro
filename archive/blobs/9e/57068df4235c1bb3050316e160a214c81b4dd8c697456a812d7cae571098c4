from __future__ import annotations

import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
CERT = ROOT / "certificates" / "physical_modal_gap_closure_plan_and_first_attempt_certificate.json"


def require(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)


def main() -> None:
    cert = json.loads(CERT.read_text(encoding="utf-8"))
    packet = json.loads(Path(cert["packet_written"]).read_text(encoding="utf-8"))
    note = Path(cert["note_written"]).read_text(encoding="utf-8")
    routes = cert["route_tests"]
    guards = cert["guardrails"]

    require(
        cert["status"] == "PHYSICAL_MODAL_GAP_PLAN_EXECUTED_FIRST_ATTEMPT_VALUE_OPEN",
        "unexpected modal gap plan status",
    )
    require(all(cert["closed_inputs"].values()), "all modal gap plan inputs must be closed")
    require(cert["verdict"]["plan_executed"] is True, "plan must be executed")
    require(cert["verdict"]["physical_value_closed"] is False, "physical modal gap must remain open")
    require(packet["status"] == "FIRST_ATTEMPT_VALUE_OPEN", "packet must remain value-open")
    require(abs(packet["dimensionless_values_closed"]["tau_internal"] - 0.40698621549433236) < 1e-15, "tau changed")
    require(abs(packet["dimensionless_values_closed"]["Lambda_eff_internal"] - 1.5675093859261626) < 1e-15, "Lambda_eff changed")
    require(all(value is None for value in packet["physical_value_fields"].values()), "physical fields must be unfilled")

    require(
        routes["R1_internal_tau_route"]["classification"] == "DIMENSIONLESS_INTERNAL_SCALE_NOT_PHYSICAL_ANCHOR",
        "tau route must not promote",
    )
    require(routes["M_theory_slot_route"]["classification"] == "STRUCTURAL_SLOT_VALUE_OPEN", "M-theory route status changed")
    require(routes["Theta_matching_route"]["classification"] == "FORBIDDEN_CALIBRATION", "Theta route must be forbidden")
    require(routes["Planck_or_Newton_route"]["classification"] == "FORBIDDEN_TARGET_BACKSOLVE", "Planck/Newton route must be forbidden")

    require(guards["claims_physical_modal_gap_value"] is False, "must not claim physical modal gap")
    require(guards["claims_alpha_phys_closed"] is False, "must not claim alpha closure")
    require(guards["uses_observed_Newton_or_Planck"] is False, "must not use Newton/Planck")
    require(guards["uses_observed_cosmology_or_masses"] is False, "must not use observed targets")
    require(guards["uses_Theta_5TeV_as_prediction"] is False, "must not use TeV calibration")
    require(guards["uses_unit_convention_as_prediction"] is False, "must not use unit convention")

    require("Same_Branch_Physical_Clock_or_Length_Source_Search_v1" in note, "note must name next artifact")
    print("AUDIT_PASS: plan executed; dimensionless tau computed; physical modal-gap value remains the exact blocker")


if __name__ == "__main__":
    main()
