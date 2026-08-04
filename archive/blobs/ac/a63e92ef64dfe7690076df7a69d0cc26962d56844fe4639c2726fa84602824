from __future__ import annotations

import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
CERT = ROOT / "certificates" / "selected_physical_anchor_source_hunt_certificate.json"


def require(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)


def main() -> None:
    cert = json.loads(CERT.read_text(encoding="utf-8"))
    note = Path(cert["note_written"]).read_text(encoding="utf-8")
    source = cert["source_tests"]
    hard_negative = cert["hard_negative"]
    synthesis = cert["synthesis"]
    guards = cert["guardrails"]

    require(
        cert["status"] == "PHYSICAL_ANCHOR_SOURCE_HUNT_COMPLETE_DIRECT_ANCHOR_NOT_FOUND",
        "unexpected status",
    )
    require(source["m_theory_ellp_fixed_by_modal_gap_and_topology"] is True, "M-theory modal-gap route missing")
    require(source["m_theory_planck_relation_present"] is True, "M-theory Planck relation missing")
    require(source["theta_i_tev_is_calibration"] is True, "Theta calibration guard missing")
    require(source["propagator_tau_physical_value_not_fixed"] is True, "tau open-source guard missing")
    require(source["meta_absolute_normalization_collapses_to_single_scalar"] is True, "single scalar obstruction missing")

    require(hard_negative["direct_physical_anchor_found_in_current_sources"] is False, "direct anchor should not be found")
    require(hard_negative["physical_G10_selected"] is False, "G10 must remain unselected")
    require(hard_negative["physical_ellp_selected"] is False, "ell_p must remain unselected")
    require(hard_negative["physical_alpha_prime_selected"] is False, "alpha_prime must remain unselected")
    require(hard_negative["theta_5TeV_promotable_to_prediction"] is False, "5 TeV must not promote")

    require(synthesis["dimensionful_obstruction_certified"] is True, "dimensionful obstruction should be active")
    require(synthesis["canonical_internal_action_units_closed"] is True, "internal action units should be closed")
    require(synthesis["best_route"] == "route_A_m_theory_modal_gap_to_ellp", "wrong best route")
    require(synthesis["direct_closure_available_now"] is False, "direct closure must remain unavailable")

    require(guards["claims_measured_Newton_constant"] is False, "must not claim Newton")
    require(guards["claims_measured_Planck_scale"] is False, "must not claim Planck")
    require(guards["uses_Theta_5TeV_as_prediction"] is False, "must not use TeV prediction")
    require(guards["uses_observed_target_backsolve"] is False, "must not backsolve")
    require(guards["hides_scale_in_unit_convention"] is False, "must not hide unit convention")
    require(guards["claims_full_physical_GR_closed"] is False, "must not claim full GR closure")

    require("Selected_Modal_Gap_to_Physical_Unit_Theorem" in note, "note must name next theorem")
    print("AUDIT_PASS: physical-anchor source hunt complete; modal-gap-to-unit theorem is next")


if __name__ == "__main__":
    main()
