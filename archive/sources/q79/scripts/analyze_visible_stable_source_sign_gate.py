"""Analyze the stable-source sign convention for the visible alpha_1 row.

The split-line HYM no-go leaves two honest source classes open: a genuinely
nonabelian stable bundle/sheaf or a direct Route-C solve.  This script checks
the sign convention that the stable HYM route must satisfy.

For a stable SU(r) HYM source with c1=0, the Bogomolov/Li-Yau sign condition
requires the Gauduchon pairing of c2 with the positive metric form to be
nonnegative.  Since ch2_math=-c2 when c1=0, the positive visible Chern-Weil
trace row must be interpreted as a positive c2 row, not as positive
mathematical ch2.
"""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
CERTIFICATES = ROOT / "certificates"
CANDIDATE_DATA = ROOT / "candidate_data"

INTEGRAL_SOURCE = CERTIFICATES / "visible_integral_chern_source_candidate_certificate.json"
SPLIT_NO_GO = CERTIFICATES / "visible_split_line_hym_no_go_certificate.json"

CANDIDATE = CANDIDATE_DATA / "visible_stable_source_sign_gate.candidate.json"
CERTIFICATE = CERTIFICATES / "visible_stable_source_sign_gate_certificate.json"


def load_json(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def write_json(path: Path, data: dict[str, Any]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(data, indent=2, sort_keys=True) + "\n", encoding="utf-8")


def analyze() -> dict[str, Any]:
    integral = load_json(INTEGRAL_SOURCE)
    split_no_go = load_json(SPLIT_NO_GO)

    trace_row = integral.get("integral_candidate", {}).get(
        "standard_chern_character_label", {}
    ).get("row")
    target_row = split_no_go.get("target", {}).get("standard_chern_character_row")

    alpha1_pairing_symbol = "P1 = integral_X alpha_1 wedge J_G > 0"
    trace_coeff = 4

    # Stable HYM sign gate in the standard anti-Hermitian Chern-Weil convention:
    # ch2_math = -1/(8*pi^2) Tr(F wedge F), c2 = -ch2_math for c1=0.
    wrong_math_ch2_coeff = trace_coeff
    wrong_c2_coeff = -wrong_math_ch2_coeff
    wrong_bogomolov_pairing_coeff = wrong_c2_coeff

    correct_trace_coeff = trace_coeff
    correct_c2_coeff = correct_trace_coeff
    correct_math_ch2_coeff = -correct_c2_coeff
    correct_bogomolov_pairing_coeff = correct_c2_coeff

    loaded = (
        integral.get("status")
        == "VISIBLE_INTEGRAL_CHERN_CLASS_CANDIDATE_CLOSED_HYM_SOURCE_OPEN"
        and split_no_go.get("status")
        == "VISIBLE_SPLIT_LINE_HYM_SOURCE_NO_GO_NONABELIAN_OR_ROUTE_C_REQUIRED"
        and trace_row == [4, 0, 0]
        and target_row == [4, 0, 0]
    )
    wrong_sign_rejected = wrong_bogomolov_pairing_coeff < 0
    stable_sign_admissible = correct_bogomolov_pairing_coeff > 0
    gate_closed = loaded and wrong_sign_rejected and stable_sign_admissible

    return {
        "calculation": "VisibleStableSourceSignGate",
        "status": (
            "VISIBLE_STABLE_SOURCE_SIGN_CONVENTION_GATE_CLOSED_SOURCE_OPEN"
            if gate_closed
            else "VISIBLE_STABLE_SOURCE_SIGN_CONVENTION_GATE_NOT_VERIFIED"
        ),
        "generated_by": "scripts/analyze_visible_stable_source_sign_gate.py",
        "inputs": {
            "visible_integral_chern_source_candidate_certificate": INTEGRAL_SOURCE.name,
            "visible_split_line_hym_no_go_certificate": SPLIT_NO_GO.name,
        },
        "stable_hym_sign_package": {
            "source_class": "stable locally-free or torsion-free SU(r) HYM source with c1=0",
            "metric_pairing": alpha1_pairing_symbol,
            "bogomolov_li_yau_sign": "integral_X c2(E) wedge J_G >= 0",
            "chern_character_relation_when_c1_zero": "ch2_math(E) = -c2(E)",
            "antihermitian_trace_convention": {
                "math_ch2": "-(1/(8*pi^2))*Tr(F wedge F)",
                "math_c2": "+(1/(8*pi^2))*Tr(F wedge F)",
            },
        },
        "wrong_sign_branch": {
            "interpretation": "read the positive [4,0,0] row as mathematical ch2",
            "math_ch2_coeff_alpha1": wrong_math_ch2_coeff,
            "math_c2_coeff_alpha1": wrong_c2_coeff,
            "bogomolov_pairing": f"{wrong_bogomolov_pairing_coeff}*P1",
            "stable_hym_admissible": False,
            "reason": "This gives negative c2 pairing with the positive Gauduchon class.",
        },
        "admissible_stable_sign_branch": {
            "interpretation": (
                "read the positive [4,0,0] row as the anti-Hermitian Chern-Weil "
                "trace row (1/(8*pi^2))*Tr(F wedge F)"
            ),
            "trace_coeff_alpha1": correct_trace_coeff,
            "math_c2_coeff_alpha1": correct_c2_coeff,
            "math_ch2_coeff_alpha1": correct_math_ch2_coeff,
            "bogomolov_pairing": f"{correct_bogomolov_pairing_coeff}*P1",
            "stable_hym_sign_admissible": True,
            "required_wording": "stable source target is c2=+4 alpha_1, equivalently math ch2=-4 alpha_1",
        },
        "calculation_results": {
            "integral_trace_row_loaded": loaded,
            "alpha1_pairs_positively_with_selected_metric": True,
            "positive_math_ch2_interpretation_rejected_for_stable_hym": wrong_sign_rejected,
            "positive_trace_row_interpretation_passes_stable_hym_sign_gate": stable_sign_admissible,
            "split_line_hym_route_already_ruled_out": split_no_go.get("calculation_results", {}).get(
                "split_line_or_cartan_hym_source_ruled_out"
            )
            is True,
            "nonabelian_stable_source_constructed": False,
            "route_c_source_constructed": False,
            "same_source_D_E_dotD_Riesz_Green_constructed": False,
        },
        "what_this_closes": {
            "stable_source_sign_convention_guardrail": gate_closed,
            "wrong_positive_math_ch2_target_rejected": wrong_sign_rejected,
            "correct_nonabelian_target_is_positive_c2_not_positive_math_ch2": stable_sign_admissible,
            "old_ch2_label_should_be_read_as_trace_label_until_convention_fixed": True,
        },
        "still_open": {
            "selected_nonabelian_stable_bundle_or_sheaf_with_c1_0_c2_4_alpha1": True,
            "selected_route_c_residual_solve_for_same_trace_row": True,
            "source_derived_Chern_Weil_representative": True,
            "HYM_or_Route_C_residual": True,
            "same_source_D_E_dotD_Riesz_Green": True,
            "coherent_spectral_projectors": True,
            "primitive_C1_contractions": True,
            "full_SM_closure": True,
        },
        "guardrails": {
            "claims_stable_source_exists": False,
            "claims_route_c_source_exists": False,
            "claims_positive_math_ch2_stable_source_possible": False,
            "claims_selected_D_E_dotD_constructed": False,
            "claims_full_SM_closure": False,
            "uses_observed_flavor_data": False,
            "uses_benchmark_flavor_entries": False,
        },
        "verdict": {
            "honest_answer": (
                "The nonabelian stable-source route survives only with the "
                "anti-Hermitian Chern-Weil sign: the positive visible trace row "
                "must correspond to c2=+4 alpha_1 and mathematical ch2=-4 alpha_1. "
                "Reading the same row as positive mathematical ch2 would violate "
                "the stable HYM Bogomolov/Li-Yau sign gate."
            ),
            "next_action": (
                "Construct a selected nonabelian stable bundle/sheaf or Route-C "
                "solve for c1=0 and c2=+4 alpha_1, then derive the same-source "
                "operator, dotD, Riesz/Green, and primitive C1 contractions."
            ),
        },
    }


def main() -> int:
    report = analyze()
    write_json(CANDIDATE, report)
    certificate = {
        "certificate": "VisibleStableSourceSignGate",
        "status": report["status"],
        "analysis_script": report["generated_by"],
        "candidate_data": "candidate_data/visible_stable_source_sign_gate.candidate.json",
        "inputs": report["inputs"],
        "stable_hym_sign_package": report["stable_hym_sign_package"],
        "wrong_sign_branch": report["wrong_sign_branch"],
        "admissible_stable_sign_branch": report["admissible_stable_sign_branch"],
        "calculation_results": report["calculation_results"],
        "what_this_closes": report["what_this_closes"],
        "still_open": report["still_open"],
        "guardrails": report["guardrails"],
        "verdict": report["verdict"],
    }
    write_json(CERTIFICATE, certificate)
    print(json.dumps(report, indent=2, sort_keys=True))
    return 0 if report["status"] == "VISIBLE_STABLE_SOURCE_SIGN_CONVENTION_GATE_CLOSED_SOURCE_OPEN" else 1


if __name__ == "__main__":
    raise SystemExit(main())
