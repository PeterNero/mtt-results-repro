from __future__ import annotations

import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
CERT = ROOT / "certificates" / "same_branch_physical_clock_or_length_source_search_certificate.json"


def require(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)


def main() -> None:
    cert = json.loads(CERT.read_text(encoding="utf-8"))
    packet = json.loads(Path(cert["packet_written"]).read_text(encoding="utf-8"))
    note = Path(cert["note_written"]).read_text(encoding="utf-8")
    routes = cert["candidate_routes"]
    guards = cert["guardrails"]
    verdict = cert["verdict"]

    require(
        cert["status"] == "SAME_BRANCH_CLOCK_LENGTH_SOURCE_FOUND_ABSOLUTE_METROLOGY_OPEN",
        "unexpected same-branch source status",
    )
    require(all(cert["closed_inputs"].values()), "all source-search inputs must be ready")
    require(packet["status"] == "STRUCTURAL_SOURCE_FOUND_ABSOLUTE_VALUE_OPEN", "packet status changed")
    require(verdict["same_branch_physical_clock_or_length_source_found"] is True, "structural source should be found")
    require(verdict["structural_bridge_closed"] is True, "structural bridge should close")
    require(verdict["absolute_physical_value_closed"] is False, "absolute physical value must remain open")

    require(
        routes["coherent_length_bridge"]["classification"]
        == "SAME_BRANCH_STRUCTURAL_BRIDGE_CLOSED_ABSOLUTE_SCALE_OPEN",
        "coherent length route classification changed",
    )
    require(
        routes["spectral_action_cutoff_bridge"]["classification"] == "RELATIVE_CUTOFF_CLOSED_ABSOLUTE_SCALE_OPEN",
        "spectral action route classification changed",
    )
    require(
        routes["kk_radius_bridge"]["classification"] == "PHENOMENOLOGY_READY_IF_FCC_RADIUS_PACKET_FILLED",
        "KK route classification changed",
    )
    require(
        routes["m_theory_planck_bridge"]["classification"] == "STRUCTURAL_SLOT_CONFIRMED_VALUE_OPEN",
        "M-theory route classification changed",
    )

    rel = packet["relative_values"]
    absvals = packet["absolute_values"]
    require(abs(rel["tau_int"] - 0.40698621549433236) < 1e-15, "tau_int changed")
    require(abs(rel["ell_coh_over_alpha_phys_minus_half"] - 0.6379547127299338) < 1e-15, "ell_coh factor changed")
    require(abs(rel["Lambda_eff_over_sqrt_alpha_phys"] - 1.5675093859261626) < 1e-15, "Lambda factor changed")
    require(all(value is None for value in absvals.values()), "absolute fields must remain unfilled")

    require(cert["metrology_no_go"]["applies_here"] is True, "metrology no-go should apply")
    require("relative physical chain" in note, "note must identify relative chain")
    require("Dimensional_Metrology_NoGo_and_Relative_Closure_Theorem_v1" in note, "note must name next theorem")

    require(guards["claims_alpha_phys_closed"] is False, "must not claim alpha closure")
    require(guards["claims_absolute_SI_length_or_energy"] is False, "must not claim absolute SI scale")
    require(guards["uses_observed_Newton_or_Planck"] is False, "must not use Newton/Planck")
    require(guards["uses_observed_cosmology_or_masses"] is False, "must not use observed targets")
    require(guards["uses_Theta_5TeV_as_prediction"] is False, "must not use 5 TeV")
    require(guards["uses_unit_convention_as_physics"] is False, "must not confuse unit convention with physics")

    print("AUDIT_PASS: same-branch tau/coherent-length bridge closed; absolute metrology remains open")


if __name__ == "__main__":
    main()
