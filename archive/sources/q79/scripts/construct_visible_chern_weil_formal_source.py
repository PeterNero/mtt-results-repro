"""Construct a formal visible Chern-Weil source for the required alpha1 row.

This is deliberately weaker than a selected visible bundle/HYM source.  It
checks whether the required visible Green-Schwarz row has an elementary
trace-free Chern-Weil realization at the level of real curvature eigenvalues.
If this passes, the remaining blocker is not algebraic row realizability; it is
integrality, stability/HYM selection, and same-source D_E/dotD spectral data.
"""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
CERTIFICATES = ROOT / "certificates"
CANDIDATE_DATA = ROOT / "candidate_data"

REQUIREMENT = CERTIFICATES / "time_oriented_m1_visible_green_schwarz_requirement_certificate.json"
S3_CLOSURE = CERTIFICATES / "visible_twisted_s3_class_restriction_closure_certificate.json"
POST_S3 = CERTIFICATES / "visible_operator_source_after_s3_closure_certificate.json"
CANDIDATE = CANDIDATE_DATA / "visible_chern_weil_formal_source.candidate.json"
CERTIFICATE = CERTIFICATES / "visible_chern_weil_formal_source_certificate.json"


def load_json(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def write_json(path: Path, data: dict[str, Any]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(data, indent=2, sort_keys=True) + "\n", encoding="utf-8")


def doubled_terms(terms: list[dict[str, Any]]) -> list[dict[str, Any]]:
    return [
        {"coefficient": 2 * int(term["coefficient"]), "monomial": term["monomial"]}
        for term in terms
    ]


def construct() -> dict[str, Any]:
    requirement = load_json(REQUIREMENT)
    s3 = load_json(S3_CLOSURE)
    post_s3 = load_json(POST_S3)
    required_row = requirement.get("derived_required_visible_row", {}).get(
        "Tr_F_visible_squared"
    )
    required_alpha1_terms = [
        {"coefficient": 8, "monomial": "r3^2/(r1^2*r2^2)"},
        {"coefficient": 4, "monomial": "r3^2"},
    ]
    f_squared_terms = [
        {"coefficient": 4, "monomial": "r3^2/(r1^2*r2^2)"},
        {"coefficient": 2, "monomial": "r3^2"},
    ]
    trace_terms = doubled_terms(f_squared_terms)

    algebraic_match = (
        required_row
        == ["8*r3^2/(r1^2*r2^2) + 4*r3^2", "0", "0"]
        and trace_terms == required_alpha1_terms
    )
    upstream_ready = (
        requirement.get("status")
        == "TIME_ORIENTED_M1_VISIBLE_GS_REQUIREMENT_DERIVED_SOURCE_OPEN"
        and s3.get("status")
        == "VISIBLE_TWISTED_S3_CLASS_RESTRICTION_CLOSED_OPERATOR_SOURCE_OPEN"
        and post_s3.get("status")
        == "VISIBLE_OPERATOR_SOURCE_REDUCED_TO_SELECTED_CW_OPERATOR_SOURCE_OPEN"
    )

    return {
        "calculation": "VisibleChernWeilFormalSource",
        "status": (
            "VISIBLE_CHERN_WEIL_FORMAL_SOURCE_ROW_REALIZED_SELECTION_OPEN"
            if algebraic_match and upstream_ready
            else "VISIBLE_CHERN_WEIL_FORMAL_SOURCE_NOT_VERIFIED"
        ),
        "generated_by": "scripts/construct_visible_chern_weil_formal_source.py",
        "inputs": {
            "visible_green_schwarz_requirement_certificate": REQUIREMENT.name,
            "s3_class_restriction_closure_certificate": S3_CLOSURE.name,
            "operator_source_after_s3_closure_certificate": POST_S3.name,
        },
        "required_row": {
            "basis": ["alpha_1", "alpha_2", "alpha_3"],
            "Tr_F_visible_squared": required_row,
            "alpha1_terms": required_alpha1_terms,
        },
        "formal_trace_free_source": {
            "source_kind": "formal_su2_chern_weil_realization",
            "rank": 2,
            "curvature_eigenvalues": ["+f alpha_1^(1/2)", "-f alpha_1^(1/2)"],
            "trace_F": "f + (-f) = 0",
            "f_squared": {
                "expression": "4*r3^2/(r1^2*r2^2) + 2*r3^2",
                "terms": f_squared_terms,
            },
            "trace_F_squared": {
                "rule": "Tr diag(f,-f)^2 = 2*f^2",
                "terms": trace_terms,
                "row": ["8*r3^2/(r1^2*r2^2) + 4*r3^2", "0", "0"],
            },
            "trace_free": True,
            "alpha2_alpha3_zero": True,
            "matches_required_row": algebraic_match,
        },
        "calculation_results": {
            "required_row_read": required_row is not None,
            "upstream_s3_and_curvature_ready": upstream_ready,
            "trace_free_rank_two_realization_exists_formally": algebraic_match,
            "no_algebraic_chern_weil_row_obstruction": algebraic_match and upstream_ready,
            "selected_visible_bundle_constructed": False,
            "integral_c2_or_c1_class_verified": False,
            "HYM_or_route_C_residual_verified": False,
            "selected_D_E_dotD_Riesz_Green_constructed": False,
        },
        "what_this_closes": {
            "formal_trace_free_Chern_Weil_row_realizability": algebraic_match and upstream_ready,
            "alpha2_alpha3_absence_compatible_with_trace_free_source": algebraic_match,
            "S3_closure_can_feed_a_visible_Chern_Weil_target": upstream_ready,
        },
        "still_open": {
            "integral_quantized_bundle_or_sheaf_class": True,
            "stable_visible_bundle_or_sheaf_model": True,
            "selected_by_MTT": True,
            "HYM_or_Route_C_residual": True,
            "source_derived_Chern_Weil_representative": True,
            "sector_D_E_dotD_Riesz_Green": True,
            "coherent_spectral_projectors": True,
            "primitive_C1_contractions": True,
            "Yukawa_CKM_PMNS_magnitudes": True,
            "full_SM_closure": True,
        },
        "guardrails": {
            "claims_selected_visible_bundle_constructed": False,
            "claims_integrality_or_stability_verified": False,
            "claims_HYM_solution_constructed": False,
            "claims_route_C_residual_solved": False,
            "claims_selected_D_E_dotD_constructed": False,
            "claims_full_SM_closure": False,
            "uses_observed_flavor_data": False,
            "uses_benchmark_flavor_entries": False,
        },
        "verdict": {
            "honest_answer": (
                "The required visible Tr_F^2 row is formally realizable by a "
                "trace-free rank-two curvature block with eigenvalues (+f,-f) "
                "and 2 f^2 equal to the required alpha1 coefficient. This "
                "removes a possible algebraic Chern-Weil obstruction, but does "
                "not supply an integral selected bundle, HYM/Route-C source, "
                "or D_E/dotD data."
            ),
            "next_action": (
                "Promote the formal row to an integral/stable selected visible "
                "bundle or Route-C source, then run the HYM/source, D_E, "
                "Riesz/Green, dotD, and C1 validators."
            ),
        },
    }


def main() -> int:
    report = construct()
    write_json(CANDIDATE, report)
    certificate = {
        "certificate": "VisibleChernWeilFormalSource",
        "status": report["status"],
        "analysis_script": report["generated_by"],
        "candidate_data": "candidate_data/visible_chern_weil_formal_source.candidate.json",
        "inputs": report["inputs"],
        "required_row": report["required_row"],
        "formal_trace_free_source": report["formal_trace_free_source"],
        "calculation_results": report["calculation_results"],
        "what_this_closes": report["what_this_closes"],
        "still_open": report["still_open"],
        "guardrails": report["guardrails"],
        "verdict": report["verdict"],
    }
    write_json(CERTIFICATE, certificate)
    print(json.dumps(report, indent=2, sort_keys=True))
    return 0 if report["calculation_results"]["no_algebraic_chern_weil_row_obstruction"] else 1


if __name__ == "__main__":
    raise SystemExit(main())
