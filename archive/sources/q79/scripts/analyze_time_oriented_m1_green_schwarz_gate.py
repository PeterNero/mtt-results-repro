"""Analyze the Green-Schwarz/Bianchi gate for the time-oriented m=1 flat gerbe."""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
CERTIFICATES = ROOT / "certificates"
CANDIDATE_DATA = ROOT / "candidate_data"
CANDIDATE = CANDIDATE_DATA / "time_oriented_m1_green_schwarz_gate.candidate.json"
CERTIFICATE = CERTIFICATES / "time_oriented_m1_green_schwarz_gate_certificate.json"
TEMPLATE = CERTIFICATES / "time_oriented_m1_visible_green_schwarz_curvature.template.json"
FLAT_GERBE_CERT = CERTIFICATES / "time_oriented_m1_flat_gerbe_promotion_certificate.json"
FREED_WITTEN_CERT = CERTIFICATES / "time_oriented_m1_freed_witten_cycle_gate_certificate.json"
Z7_CHARGE_CERT = CERTIFICATES / "z7_fuyau_mukai_charge_sector_certificate.json"
C1_RPLUS_CERT = CERTIFICATES / "c1_iwasawa_rplus_support_certificate.json"
HYM_ATTEMPT_CERT = CERTIFICATES / "selected_hym_operator_source_attempt_certificate.json"
VALIDATOR = ROOT / "scripts" / "validate_time_oriented_m1_visible_green_schwarz_curvature.py"


def load_json(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def write_json(path: Path, data: dict[str, Any]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(data, indent=2, sort_keys=True) + "\n", encoding="utf-8")


def template_packet() -> dict[str, Any]:
    return {
        "schema": "TimeOrientedM1VisibleGreenSchwarzCurvature.v1",
        "status": "OPEN",
        "selected_by_mtt": None,
        "same_branch_as_q79_m1": None,
        "flat_gerbe_certificate": "time_oriented_m1_flat_gerbe_promotion_certificate.json",
        "green_schwarz_gate_certificate": "time_oriented_m1_green_schwarz_gate_certificate.json",
        "selected_visible_source_certificate": None,
        "curvature_basis": None,
        "alpha_prime_over_4_absorbed": None,
        "flat_m1_torsion_curvature_zero": True,
        "dH_coefficients": None,
        "tr_R_plus_squared_coefficients": None,
        "tr_F_visible_squared_coefficients": None,
        "bianchi_residual_coefficients": None,
        "bianchi_residual_zero": None,
        "route_c_or_hym_source_certificate": None,
        "projector_retention_certificate": None,
        "uses_observed_flavor_data": False,
        "uses_benchmark_flavor_entries": False,
    }


def analyze() -> dict[str, Any]:
    flat = load_json(FLAT_GERBE_CERT)
    freed_witten = load_json(FREED_WITTEN_CERT)
    z7 = load_json(Z7_CHARGE_CERT)
    c1 = load_json(C1_RPLUS_CERT)
    hym = load_json(HYM_ATTEMPT_CERT)

    flat_model = flat.get("flat_gerbe_model", {})
    flat_results = flat.get("calculation_results", {})
    z7_geometry = z7.get("geometry", {})
    c1_rplus = c1.get("rplus_support", {})
    c1_bianchi = c1.get("bianchi_support", {})
    hym_results = hym.get("calculation_results", {})

    flat_curvature_zero = (
        flat_model.get("curvature_H_form") == "0"
        and flat_results.get("curvature_H_zero_for_flat_representative") is True
    )
    charge_sector_bianchi_closed = (
        z7.get("status") == "CLOSED_CHARGE_SECTOR"
        and z7_geometry.get("green_schwarz_bianchi_identity_verified") is True
    )
    finite_freed_witten_gate_closed = (
        freed_witten.get("status")
        == "TIME_ORIENTED_M1_FREED_WITTEN_CYCLE_GATE_FORMULATED_SELECTED_CYCLES_OPEN"
    )
    visible_operator_source_open = (
        hym_results.get("selected_hym_operator_source_verified") is False
        and hym.get("status") == "SELECTED_HYM_OPERATOR_SOURCE_ATTEMPT_BLOCKED_OPERATOR_SOURCE_MISSING"
    )
    iwasawa_rplus_row_available = (
        c1.get("closed", {}).get("Rplus_alpha1_only") is True
        and c1_rplus.get("alpha_2_component") == 0
        and c1_rplus.get("alpha_3_component") == 0
    )

    preservation_gate_closed = (
        flat_curvature_zero
        and charge_sector_bianchi_closed
        and finite_freed_witten_gate_closed
        and visible_operator_source_open
        and iwasawa_rplus_row_available
        and VALIDATOR.exists()
    )

    return {
        "candidate": "TimeOrientedM1GreenSchwarzGate",
        "status": (
            "TIME_ORIENTED_M1_GREEN_SCHWARZ_GATE_PRESERVATION_CLOSED_VISIBLE_SOURCE_OPEN"
            if preservation_gate_closed
            else "TIME_ORIENTED_M1_GREEN_SCHWARZ_GATE_NOT_CLOSED"
        ),
        "generated_by": "scripts/analyze_time_oriented_m1_green_schwarz_gate.py",
        "inputs": {
            "flat_gerbe_certificate": "time_oriented_m1_flat_gerbe_promotion_certificate.json",
            "freed_witten_cycle_gate_certificate": "time_oriented_m1_freed_witten_cycle_gate_certificate.json",
            "z7_charge_sector_certificate": "z7_fuyau_mukai_charge_sector_certificate.json",
            "c1_iwasawa_rplus_support_certificate": "c1_iwasawa_rplus_support_certificate.json",
            "selected_hym_operator_source_attempt_certificate": "selected_hym_operator_source_attempt_certificate.json",
        },
        "flat_torsion_curvature_effect": {
            "curvature_H_form": flat_model.get("curvature_H_form"),
            "curvature_H_zero_for_flat_representative": flat_curvature_zero,
            "delta_dH_from_m1_flat_torsion": 0,
            "changes_green_schwarz_curvature_equation": False,
            "can_cancel_missing_visible_curvature_residual": False,
            "reason": (
                "The m=1 class is represented here by locally constant U(1) "
                "Cech data with B_i=A_ij=0, so it is torsion in differential "
                "cohomology and contributes no de Rham H-flux."
            ),
        },
        "charge_sector_preservation": {
            "z7_charge_sector_status": z7.get("status"),
            "charge_sector_green_schwarz_bianchi_verified": charge_sector_bianchi_closed,
            "preserved_under_flat_m1_torsion": flat_curvature_zero
            and charge_sector_bianchi_closed,
            "scope": (
                "This imports only the already-closed Fu-Yau/Mukai charge-sector "
                "Bianchi equation. It does not construct the visible SM bundle "
                "operator source."
            ),
        },
        "iwasawa_curvature_row_available": {
            "Rplus_alpha1_only": iwasawa_rplus_row_available,
            "Tr_grav_R_plus_squared": c1_rplus.get("formula"),
            "coefficient": c1_rplus.get("coefficient"),
            "dH_support": c1_bianchi.get("dH"),
            "gauge_flux_choice": c1_bianchi.get("gauge_flux_choice"),
            "values_to_dotD_open": c1.get("open", {}).get("map_alpha1_row_to_deltaTheta_C1")
            is True,
        },
        "visible_operator_source_status": {
            "selected_hym_operator_source_verified": hym_results.get(
                "selected_hym_operator_source_verified"
            ),
            "route_c_q79_branch_available": hym_results.get("route_c_q79_branch_available"),
            "selected_D_E_dotD_open": hym.get("still_open", {}).get(
                "selected_D_E_dotD_same_branch"
            ),
            "selected_visible_sm_bundle_model_open": hym.get("still_open", {}).get(
                "selected_visible_sm_bundle_model"
            ),
        },
        "visible_curvature_packet": {
            "template": "certificates/time_oriented_m1_visible_green_schwarz_curvature.template.json",
            "validator": "scripts/validate_time_oriented_m1_visible_green_schwarz_curvature.py",
            "template_written": True,
            "validator_exists": VALIDATOR.exists(),
            "filled_selected_packet_present": False,
        },
        "calculation_results": {
            "flat_m1_adds_no_deRham_H_flux": flat_curvature_zero,
            "charge_sector_bianchi_preserved": flat_curvature_zero
            and charge_sector_bianchi_closed,
            "finite_Freed_Witten_DD_gate_available": finite_freed_witten_gate_closed,
            "iwasawa_Rplus_alpha1_row_available": iwasawa_rplus_row_available,
            "visible_green_schwarz_verified": False,
            "green_schwarz_not_a_torsion_label_selector": True,
            "future_visible_curvature_packet_template_written": True,
        },
        "what_this_closes": {
            "m1_flat_torsion_preserves_GS_curvature_bianchi": preservation_gate_closed,
            "no_hidden_GS_repair_from_flat_torsion": preservation_gate_closed,
            "closed_charge_sector_can_be_preserved_without_visible_source_promotion": preservation_gate_closed,
            "visible_GS_input_contract_formulated": preservation_gate_closed,
        },
        "still_open": {
            "selected_visible_gauge_bundle_curvature_TrFvis_squared": True,
            "selected_gravity_curvature_on_same_visible_branch": True,
            "selected_visible_Bianchi_residual_zero_packet": True,
            "selected_route_c_or_hym_operator_source": True,
            "selected_projector_retention_for_visible_zero_modes": True,
            "selected_D_E_dotD_Riesz_Green_files_from_same_branch": True,
            "primitive_C1_contractions": True,
            "full_SM_closure": True,
        },
        "guardrails": {
            "claims_visible_green_schwarz_verified": False,
            "claims_selected_visible_bundle_constructed": False,
            "claims_selected_D_E_dotD_constructed": False,
            "claims_projector_retention": False,
            "claims_full_SM_closure": False,
            "uses_observed_flavor_data": False,
            "uses_benchmark_flavor_entries": False,
        },
        "verdict": {
            "honest_answer": (
                "The time-oriented m=1 flat torsion gerbe is curvature-invisible: "
                "it preserves the already closed Fu-Yau/Mukai charge-sector "
                "Bianchi equation and cannot be used as a hidden source that "
                "cancels missing visible gauge/gravity curvature. The visible "
                "Green-Schwarz calculation remains a same-branch selected "
                "bundle/operator-source packet."
            ),
            "next_closing_object": (
                "Fill the visible Green-Schwarz curvature packet with selected "
                "basis coefficients for dH, Tr R_+^2, and Tr F_visible^2 from "
                "the same q79/F,m=1 branch, then validate zero residual before "
                "promoting twisted source or C1 responses."
            ),
        },
    }


def write_outputs(report: dict[str, Any]) -> None:
    write_json(CANDIDATE, report)
    certificate = {
        "certificate": "TimeOrientedM1GreenSchwarzGate",
        "status": report["status"],
        "analysis_script": "scripts/analyze_time_oriented_m1_green_schwarz_gate.py",
        "candidate_data": "candidate_data/time_oriented_m1_green_schwarz_gate.candidate.json",
        "validator_script": "scripts/validate_time_oriented_m1_visible_green_schwarz_curvature.py",
        "inputs": report["inputs"],
        "flat_torsion_curvature_effect": report["flat_torsion_curvature_effect"],
        "charge_sector_preservation": report["charge_sector_preservation"],
        "iwasawa_curvature_row_available": report["iwasawa_curvature_row_available"],
        "visible_operator_source_status": report["visible_operator_source_status"],
        "visible_curvature_packet": report["visible_curvature_packet"],
        "calculation_results": report["calculation_results"],
        "what_this_closes": report["what_this_closes"],
        "still_open": report["still_open"],
        "guardrails": report["guardrails"],
        "verdict": report["verdict"],
    }
    write_json(CERTIFICATE, certificate)
    if not TEMPLATE.exists():
        write_json(TEMPLATE, template_packet())


def main() -> int:
    report = analyze()
    write_outputs(report)
    print(json.dumps(report, indent=2, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
