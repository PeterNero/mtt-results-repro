from __future__ import annotations

import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
CERT = ROOT / "certificates" / "m_theory_modal_gap_dimensional_anchor_candidate_certificate.json"


def require(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)


def main() -> None:
    cert = json.loads(CERT.read_text(encoding="utf-8"))
    require(
        cert["status"] == "M_THEORY_MODAL_GAP_ANCHOR_CANDIDATE_FORMULATED_DIMENSIONFUL_GAP_OPEN",
        "unexpected status",
    )
    source = cert["source_tests"]
    closed = cert["closed_tests"]
    open_tests = cert["open_tests"]
    guards = cert["guardrails"]

    require(source["m_theory_source_present"] is True, "M-theory source should be present")
    require(source["planck_relation_source_present"] is True, "Planck relation should be source-supported")
    require(source["gauge_matrix_source_present"] is True, "gauge matrix relation should be source-supported")
    require(
        source["modal_gap_condition_source_present"] is True,
        "source should condition fixed data on modal gap scales",
    )
    require(closed["internal_scale_lift_available"] is True, "internal scale lift should be available")
    require(closed["m_theory_planck_slot_identified"] is True, "Planck slot should be identified")
    require(open_tests["dimensionful_modal_gap_value_computed"] is False, "dimensionful gap should remain open")
    require(open_tests["ell_p_or_kappa11_selected_without_backsolve"] is False, "ell_p/kappa11 should remain open")
    require(open_tests["physical_newton_or_planck_prediction_allowed"] is False, "physical prediction should not be allowed")
    require(guards["claims_physical_GN"] is False, "must not claim physical G_N")
    require(guards["claims_physical_MPl"] is False, "must not claim physical M_Pl")
    require(guards["claims_dimensionful_modal_gap_closed"] is False, "must not claim modal gap closure")
    require(guards["forbids_relative_scale_fix_as_absolute_prediction"] is True, "relative scale guard required")

    print("AUDIT_PASS: M-theory modal-gap anchor formulated; dimensionful modal gap remains open")


if __name__ == "__main__":
    main()
