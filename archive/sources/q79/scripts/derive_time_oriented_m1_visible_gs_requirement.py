"""Derive the visible Green-Schwarz gauge-curvature row required by m=1."""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
CERTIFICATES = ROOT / "certificates"
CANDIDATE_DATA = ROOT / "candidate_data"
CANDIDATE = CANDIDATE_DATA / "time_oriented_m1_visible_green_schwarz_requirement.candidate.json"
CERTIFICATE = CERTIFICATES / "time_oriented_m1_visible_green_schwarz_requirement_certificate.json"
GS_GATE_CERT = CERTIFICATES / "time_oriented_m1_green_schwarz_gate_certificate.json"
C1_RPLUS_CERT = CERTIFICATES / "c1_iwasawa_rplus_support_certificate.json"
HYM_ATTEMPT_CERT = CERTIFICATES / "selected_hym_operator_source_attempt_certificate.json"


def load_json(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def write_json(path: Path, data: dict[str, Any]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(data, indent=2, sort_keys=True) + "\n", encoding="utf-8")


def derive() -> dict[str, Any]:
    gs_gate = load_json(GS_GATE_CERT)
    c1 = load_json(C1_RPLUS_CERT)
    hym = load_json(HYM_ATTEMPT_CERT)

    gs_preservation_closed = (
        gs_gate.get("status")
        == "TIME_ORIENTED_M1_GREEN_SCHWARZ_GATE_PRESERVATION_CLOSED_VISIBLE_SOURCE_OPEN"
    )
    rplus_alpha1_only = c1.get("closed", {}).get("Rplus_alpha1_only") is True
    bianchi_support = c1.get("bianchi_support", {})
    rplus_support = c1.get("rplus_support", {})
    selected_source_absent = (
        hym.get("calculation_results", {}).get("selected_hym_operator_source_verified") is False
    )

    requirement_derived = gs_preservation_closed and rplus_alpha1_only and selected_source_absent

    report = {
        "candidate": "TimeOrientedM1VisibleGreenSchwarzRequirement",
        "status": (
            "TIME_ORIENTED_M1_VISIBLE_GS_REQUIREMENT_DERIVED_SOURCE_OPEN"
            if requirement_derived
            else "TIME_ORIENTED_M1_VISIBLE_GS_REQUIREMENT_NOT_DERIVED"
        ),
        "generated_by": "scripts/derive_time_oriented_m1_visible_gs_requirement.py",
        "inputs": {
            "green_schwarz_gate_certificate": "time_oriented_m1_green_schwarz_gate_certificate.json",
            "c1_iwasawa_rplus_support_certificate": "c1_iwasawa_rplus_support_certificate.json",
            "selected_hym_operator_source_attempt_certificate": "selected_hym_operator_source_attempt_certificate.json",
        },
        "normalization": {
            "equation": "dH = Tr R_+^2 - Tr F_visible^2",
            "alpha_prime_over_4_absorbed": True,
            "basis": [
                "alpha_1 = a wedge b",
                "alpha_2 = a wedge c",
                "alpha_3 = b wedge c",
            ],
        },
        "known_rows": {
            "dH": ["-4*r3^2", "0", "0"],
            "Tr_R_plus_squared": [
                "8*r3^2/(r1^2*r2^2)",
                "0",
                "0",
            ],
            "source_dH_statement": bianchi_support.get("dH"),
            "source_Rplus_statement": rplus_support.get("formula"),
        },
        "derived_required_visible_row": {
            "rule": "Tr F_visible^2 = Tr R_+^2 - dH",
            "Tr_F_visible_squared": [
                "8*r3^2/(r1^2*r2^2) + 4*r3^2",
                "0",
                "0",
            ],
            "residual_if_supplied": ["0", "0", "0"],
        },
        "relation_to_existing_gauge_flux_row": {
            "existing_c1_gauge_flux_choice": bianchi_support.get("gauge_flux_choice"),
            "component_equations": bianchi_support.get("component_equations"),
            "usable_as_visible_source_now": False,
            "reason": (
                "The existing row records the invariant Bianchi support used by "
                "the C1 curvature source. It does not select a visible SM bundle "
                "or provide a same-branch HYM/Route-C operator-source certificate."
            ),
        },
        "calculation_results": {
            "green_schwarz_preservation_gate_closed": gs_preservation_closed,
            "rplus_and_dH_have_alpha1_support_only": rplus_alpha1_only,
            "alpha2_alpha3_visible_curvature_forced_zero_in_invariant_basis": True,
            "visible_gauge_curvature_reduced_to_one_alpha1_coefficient": requirement_derived,
            "selected_visible_source_absent": selected_source_absent,
            "visible_curvature_packet_validator_can_pass_now": False,
        },
        "what_this_closes": {
            "coefficient_level_visible_TrF_requirement": requirement_derived,
            "alpha2_alpha3_zero_requirement": requirement_derived,
            "single_missing_alpha1_visible_gauge_row_identified": requirement_derived,
        },
        "still_open": {
            "selected_visible_bundle_or_HYM_source_for_required_TrF_row": True,
            "selected_same_branch_coefficients_in_validator_packet": True,
            "projector_retention_for_visible_zero_modes": True,
            "selected_D_E_dotD_Riesz_Green_files": True,
            "primitive_C1_contractions": True,
            "full_SM_closure": True,
        },
        "guardrails": {
            "claims_required_row_is_selected_visible_bundle": False,
            "claims_visible_green_schwarz_verified": False,
            "claims_selected_D_E_dotD_constructed": False,
            "claims_full_SM_closure": False,
            "uses_observed_flavor_data": False,
            "uses_benchmark_flavor_entries": False,
        },
        "verdict": {
            "honest_answer": (
                "The visible Bianchi equation is now reduced algebraically: in "
                "the invariant Iwasawa basis, a selected visible bundle would "
                "need Tr F_visible^2 = (8*r3^2/(r1^2*r2^2)+4*r3^2) alpha_1, "
                "with no alpha_2 or alpha_3 component. Current certificates do "
                "not supply the selected visible bundle/operator source that "
                "realizes this row."
            ),
            "next_closing_object": (
                "Construct or validate a selected visible HYM/Route-C source "
                "whose Chern-Weil row equals the derived alpha_1 coefficient, "
                "then fill the visible Green-Schwarz curvature validator packet."
            ),
        },
    }
    return report


def write_outputs(report: dict[str, Any]) -> None:
    write_json(CANDIDATE, report)
    certificate = {
        "certificate": "TimeOrientedM1VisibleGreenSchwarzRequirement",
        "status": report["status"],
        "analysis_script": "scripts/derive_time_oriented_m1_visible_gs_requirement.py",
        "candidate_data": "candidate_data/time_oriented_m1_visible_green_schwarz_requirement.candidate.json",
        "inputs": report["inputs"],
        "normalization": report["normalization"],
        "known_rows": report["known_rows"],
        "derived_required_visible_row": report["derived_required_visible_row"],
        "relation_to_existing_gauge_flux_row": report["relation_to_existing_gauge_flux_row"],
        "calculation_results": report["calculation_results"],
        "what_this_closes": report["what_this_closes"],
        "still_open": report["still_open"],
        "guardrails": report["guardrails"],
        "verdict": report["verdict"],
    }
    write_json(CERTIFICATE, certificate)


def main() -> int:
    report = derive()
    write_outputs(report)
    print(json.dumps(report, indent=2, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
