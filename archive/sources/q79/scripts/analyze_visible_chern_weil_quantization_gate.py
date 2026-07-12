"""Analyze the quantization gate for the formal visible Chern-Weil row.

The previous packet proves only formal trace-free row realizability.  This
script asks the next stricter question: what would be required to promote that
row to an integral/topological Chern-Weil source?

The honest result is a reduction, not a closure.  In absorbed Green-Schwarz
units the visible row is fixed.  Integral Chern-Weil data require restoring the
alpha-prime/trace/period normalization and selecting an actual visible bundle,
sheaf, or Route-C source.
"""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
CERTIFICATES = ROOT / "certificates"
CANDIDATE_DATA = ROOT / "candidate_data"

FORMAL_SOURCE = CERTIFICATES / "visible_chern_weil_formal_source_certificate.json"
REQUIREMENT = CERTIFICATES / "time_oriented_m1_visible_green_schwarz_requirement_certificate.json"
RPLUS_SUPPORT = CERTIFICATES / "c1_iwasawa_rplus_support_certificate.json"
POST_S3 = CERTIFICATES / "visible_operator_source_after_s3_closure_certificate.json"

CANDIDATE = CANDIDATE_DATA / "visible_chern_weil_quantization_gate.candidate.json"
CERTIFICATE = CERTIFICATES / "visible_chern_weil_quantization_gate_certificate.json"


def load_json(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def write_json(path: Path, data: dict[str, Any]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(data, indent=2, sort_keys=True) + "\n", encoding="utf-8")


def analyze() -> dict[str, Any]:
    formal = load_json(FORMAL_SOURCE)
    requirement = load_json(REQUIREMENT)
    rplus = load_json(RPLUS_SUPPORT)
    post_s3 = load_json(POST_S3)

    required_row = requirement.get("derived_required_visible_row", {}).get("Tr_F_visible_squared")
    formal_row = formal.get("formal_trace_free_source", {}).get("trace_F_squared", {}).get("row")
    normalization = requirement.get("normalization", {})
    existing_flux = requirement.get("relation_to_existing_gauge_flux_row", {})
    bianchi_support = rplus.get("bianchi_support", {})
    equal_radius = rplus.get("rplus_support", {}).get("equal_radius_specialization", {})

    formal_ready = (
        formal.get("status") == "VISIBLE_CHERN_WEIL_FORMAL_SOURCE_ROW_REALIZED_SELECTION_OPEN"
        and formal_row == required_row
        and formal.get("calculation_results", {}).get("no_algebraic_chern_weil_row_obstruction")
        is True
    )
    requirement_ready = (
        requirement.get("status") == "TIME_ORIENTED_M1_VISIBLE_GS_REQUIREMENT_DERIVED_SOURCE_OPEN"
        and normalization.get("alpha_prime_over_4_absorbed") is True
    )
    rplus_ready = (
        rplus.get("status") == "C1_IWASAWA_RPLUS_INVARIANT_SUPPORT_CLOSED_OVERLAPS_OPEN"
        and bianchi_support.get("gauge_flux_choice") == "u1 = 8(2*pi)^2, u2 = u3 = 0"
    )
    post_s3_ready = post_s3.get("status") == "VISIBLE_OPERATOR_SOURCE_REDUCED_TO_SELECTED_CW_OPERATOR_SOURCE_OPEN"
    copied_flux_forbidden = existing_flux.get("usable_as_visible_source_now") is False

    absorbed_alpha1 = "8*r3^2/(r1^2*r2^2) + 4*r3^2"
    restored_unabsorbed_alpha1 = "8*r3^2/(r1^2*r2^2) + (16/alpha_prime)*r3^2"
    existing_flux_integer_label = 8
    standard_instanton_label = 4

    gate_formulated = formal_ready and requirement_ready and rplus_ready and post_s3_ready
    no_quantization_contradiction = gate_formulated and copied_flux_forbidden

    return {
        "calculation": "VisibleChernWeilQuantizationGate",
        "status": (
            "VISIBLE_CHERN_WEIL_QUANTIZATION_REDUCED_TO_PERIOD_SOURCE_SELECTION_OPEN"
            if no_quantization_contradiction
            else "VISIBLE_CHERN_WEIL_QUANTIZATION_GATE_NOT_VERIFIED"
        ),
        "generated_by": "scripts/analyze_visible_chern_weil_quantization_gate.py",
        "inputs": {
            "visible_chern_weil_formal_source_certificate": FORMAL_SOURCE.name,
            "visible_green_schwarz_requirement_certificate": REQUIREMENT.name,
            "c1_iwasawa_rplus_support_certificate": RPLUS_SUPPORT.name,
            "operator_source_after_s3_closure_certificate": POST_S3.name,
        },
        "row_normalization_split": {
            "basis": normalization.get("basis"),
            "absorbed_green_schwarz_equation": normalization.get("equation"),
            "alpha_prime_over_4_absorbed": normalization.get("alpha_prime_over_4_absorbed"),
            "absorbed_visible_alpha1_coefficient": absorbed_alpha1,
            "restored_unabsorbed_bianchi_component": restored_unabsorbed_alpha1,
            "reason_for_split": (
                "The formal source proves a row in the absorbed Green-Schwarz "
                "normalization. Integral Chern-Weil quantization is a period "
                "statement after restoring alpha_prime, trace, and alpha_1 "
                "normalization conventions."
            ),
        },
        "period_quantization_gate": {
            "period_symbol": "P_alpha1 = integral_{Sigma4} alpha_1 in the selected integral basis",
            "trace_unit_symbol": "C_Tr = selected Chern-Weil trace/2pi normalization",
            "absorbed_condition": (
                "P_alpha1*(8*r3^2/(r1^2*r2^2)+4*r3^2)/C_Tr lies in the visible "
                "Chern character lattice only after absorbed-unit conventions are fixed"
            ),
            "unabsorbed_condition": (
                "P_alpha1*(8*r3^2/(r1^2*r2^2)+(16/alpha_prime)*r3^2)/C_Tr lies "
                "in the selected visible Chern character lattice"
            ),
            "minimal_missing_inputs": [
                "selected alpha_1 period normalization",
                "selected trace convention for Tr_F",
                "selected alpha_prime restoration convention",
                "selected visible integral Chern character or K-theory class",
                "selected bundle/sheaf/Chan-Paton or Route-C source realizing that class",
            ],
            "integrality_proved_now": False,
        },
        "existing_flux_row_consistency": {
            "existing_c1_gauge_flux_choice": existing_flux.get("existing_c1_gauge_flux_choice"),
            "c1_support_gauge_flux_choice": bianchi_support.get("gauge_flux_choice"),
            "component_equation": existing_flux.get("component_equations")
            or bianchi_support.get("component_equations"),
            "equal_radius_specialization": {
                "assumption": equal_radius.get("assumption"),
                "fixed_r3_squared": equal_radius.get("fixed_r3_squared"),
            },
            "conditional_integer_label_if_period_unit_is_2pi_squared": existing_flux_integer_label,
            "conditional_integer_label_if_unit_is_8pi_squared": standard_instanton_label,
            "trace_convention_warning": (
                "The label is 8 in the coefficient unit (2*pi)^2, but 4 in the "
                "standard instanton unit 8*pi^2. The selected trace convention "
                "must be fixed before this becomes a topological charge claim."
            ),
            "conditional_consistency_statement": (
                "If the C1 support row u1=8(2*pi)^2 is later selected as the "
                "same visible Chern-Weil class with matching period and trace "
                "normalization, then the unabsorbed component equation is "
                "quantized. Current certificates explicitly do not allow copying "
                "this row as the visible SM source."
            ),
            "usable_as_visible_source_now": copied_flux_forbidden is False,
        },
        "calculation_results": {
            "formal_absorbed_row_loaded": formal_ready,
            "absorbed_to_unabsorbed_normalization_split_identified": requirement_ready,
            "existing_c1_flux_row_conditionally_integral": rplus_ready,
            "existing_flux_row_forbidden_as_visible_source_now": copied_flux_forbidden,
            "no_quantization_contradiction_found": no_quantization_contradiction,
            "integral_visible_bundle_or_sheaf_constructed": False,
            "selected_visible_c2_or_ch2_class_verified": False,
            "HYM_or_Route_C_residual_verified": False,
            "same_source_D_E_dotD_Riesz_Green_constructed": False,
        },
        "what_this_closes": {
            "formal_to_integral_normalization_gate": gate_formulated,
            "absorbed_vs_unabsorbed_row_not_confused": requirement_ready,
            "existing_integer_flux_row_is_conditionally_consistent": rplus_ready,
            "no_current_integrality_contradiction": no_quantization_contradiction,
        },
        "still_open": {
            "selected_alpha1_integral_period_basis": True,
            "selected_trace_normalization": True,
            "selected_alpha_prime_restoration": True,
            "selected_visible_integral_Chern_character_or_K_theory_class": True,
            "stable_visible_bundle_or_sheaf_model": True,
            "source_derived_Chern_Weil_representative": True,
            "HYM_or_Route_C_residual": True,
            "same_source_D_E_dotD_Riesz_Green": True,
            "coherent_spectral_projectors": True,
            "primitive_C1_contractions": True,
            "full_SM_closure": True,
        },
        "guardrails": {
            "claims_integrality_proved": False,
            "claims_existing_c1_flux_is_visible_source": False,
            "claims_selected_visible_bundle_constructed": False,
            "claims_HYM_solution_constructed": False,
            "claims_selected_D_E_dotD_constructed": False,
            "claims_full_SM_closure": False,
            "uses_observed_flavor_data": False,
            "uses_benchmark_flavor_entries": False,
        },
        "verdict": {
            "honest_answer": (
                "The formal visible row is compatible with quantization in the "
                "sense that no contradiction appears. The existing C1 support "
                "row u1=8(2*pi)^2 gives a conditional integer label 8 in "
                "coefficient units, or 4 in the standard 8*pi^2 instanton unit, "
                "once the unabsorbed normalization and trace convention are "
                "selected. But this does not yet prove an integral selected "
                "visible bundle/sheaf or HYM/Route-C source."
            ),
            "next_action": (
                "Fill a selected source packet that supplies the alpha_1 period "
                "basis, trace normalization, visible Chern character/K-theory "
                "class, and same-source HYM/Route-C plus D_E/dotD data."
            ),
        },
    }


def main() -> int:
    report = analyze()
    write_json(CANDIDATE, report)
    certificate = {
        "certificate": "VisibleChernWeilQuantizationGate",
        "status": report["status"],
        "analysis_script": report["generated_by"],
        "candidate_data": "candidate_data/visible_chern_weil_quantization_gate.candidate.json",
        "inputs": report["inputs"],
        "row_normalization_split": report["row_normalization_split"],
        "period_quantization_gate": report["period_quantization_gate"],
        "existing_flux_row_consistency": report["existing_flux_row_consistency"],
        "calculation_results": report["calculation_results"],
        "what_this_closes": report["what_this_closes"],
        "still_open": report["still_open"],
        "guardrails": report["guardrails"],
        "verdict": report["verdict"],
    }
    write_json(CERTIFICATE, certificate)
    print(json.dumps(report, indent=2, sort_keys=True))
    return 0 if report["calculation_results"]["no_quantization_contradiction_found"] else 1


if __name__ == "__main__":
    raise SystemExit(main())
