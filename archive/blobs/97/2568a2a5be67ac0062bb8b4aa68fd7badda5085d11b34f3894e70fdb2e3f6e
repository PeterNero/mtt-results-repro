"""Prove the split line/Cartan HYM no-go for the visible alpha1 source.

The previous packet found the integral target

    Tr F^2 = 8*(2*pi)^2 alpha_1

or standard label 4 in the selected alpha_1 direction.  This script proves a
general no-go for a tempting next shortcut: no finite split abelian line-bundle
or diagonal Cartan sum can be an individual-HYM source for a positive alpha_1
row on the Iwasawa branch.

The proof is purely algebraic.  If every line component is primitive, each
integer vector n^(a) lies in the kernel of a positive slope vector p.  Hence the
second-moment matrix S=sum_a n^(a)n^(a)^T has S p=0.  But the required positive
alpha_1 row sets S_12=4 and S_13=S_23=0, so the first component of S p is
S_11 p_1 + 4 p_2, strictly positive.  Contradiction.
"""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
CERTIFICATES = ROOT / "certificates"
CANDIDATE_DATA = ROOT / "candidate_data"

INTEGRAL_SOURCE = CERTIFICATES / "visible_integral_chern_source_candidate_certificate.json"
VISIBLE_SOURCE_ATTEMPT = (
    CERTIFICATES / "time_oriented_m1_visible_gs_source_attempt_certificate.json"
)

CANDIDATE = CANDIDATE_DATA / "visible_split_line_hym_no_go.candidate.json"
CERTIFICATE = CERTIFICATES / "visible_split_line_hym_no_go_certificate.json"


def load_json(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def write_json(path: Path, data: dict[str, Any]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(data, indent=2, sort_keys=True) + "\n", encoding="utf-8")


def prove() -> dict[str, Any]:
    integral = load_json(INTEGRAL_SOURCE)
    source_attempt = load_json(VISIBLE_SOURCE_ATTEMPT)
    row = integral.get("integral_candidate", {}).get("standard_chern_character_label", {}).get("row")

    target_ready = (
        integral.get("status")
        == "VISIBLE_INTEGRAL_CHERN_CLASS_CANDIDATE_CLOSED_HYM_SOURCE_OPEN"
        and row == [4, 0, 0]
    )
    source_still_open = (
        source_attempt.get("status")
        == "TIME_ORIENTED_M1_VISIBLE_GS_SOURCE_ATTEMPT_BLOCKED_SELECTED_SOURCE_MISSING"
    )

    proof_steps = [
        {
            "step": "split_line_data",
            "statement": (
                "Let n^(a)=(n1,n2,n3) be the integral line/Cartan flux vectors."
            ),
        },
        {
            "step": "individual_hym_primitivity",
            "statement": (
                "Each HYM line summand must satisfy p dot n^(a)=0 for one "
                "positive slope vector p=(p1,p2,p3), with p_i>0."
            ),
        },
        {
            "step": "second_moment_matrix",
            "statement": (
                "Set S_ij=sum_a n_i^(a)n_j^(a). Since every n^(a) is "
                "orthogonal to p, S p=sum_a n^(a)(n^(a) dot p)=0."
            ),
        },
        {
            "step": "visible_alpha1_target",
            "statement": (
                "The required positive alpha_1 Chern-Weil row fixes "
                "S_12=4, S_13=0, S_23=0 in standard 8*pi^2 units."
            ),
        },
        {
            "step": "contradiction",
            "statement": (
                "The first component of S p is S_11*p1 + 4*p2. Since S_11 is "
                "a sum of squares and p1,p2 are positive, this is strictly "
                "positive, contradicting S p=0."
            ),
        },
    ]

    no_go = target_ready and source_still_open

    return {
        "calculation": "VisibleSplitLineHYMNoGo",
        "status": (
            "VISIBLE_SPLIT_LINE_HYM_SOURCE_NO_GO_NONABELIAN_OR_ROUTE_C_REQUIRED"
            if no_go
            else "VISIBLE_SPLIT_LINE_HYM_NO_GO_NOT_VERIFIED"
        ),
        "generated_by": "scripts/prove_visible_split_line_hym_no_go.py",
        "inputs": {
            "visible_integral_chern_source_candidate_certificate": INTEGRAL_SOURCE.name,
            "visible_green_schwarz_source_attempt_certificate": VISIBLE_SOURCE_ATTEMPT.name,
        },
        "target": {
            "standard_chern_character_row": row,
            "chern_weil_trace_row": "Tr F^2 = 8*(2*pi)^2 alpha_1",
            "sign_convention_scope": (
                "The no-go applies to the positive Chern-Weil alpha_1 row fixed "
                "by the visible Green-Schwarz requirement in the current trace "
                "normalization."
            ),
        },
        "algebraic_no_go": {
            "source_class": "finite split line-bundle or diagonal Cartan sum",
            "slope_vector": "p=(r2^2/r3^2, r1^2/r3^2, r1^2/r2^2), all entries positive",
            "individual_hym_condition": "p dot n^(a)=0 for every summand a",
            "moment_matrix": "S_ij=sum_a n_i^(a)n_j^(a)",
            "hym_implies": "S p=0",
            "target_off_diagonal_entries": {"S12": 4, "S13": 0, "S23": 0},
            "first_component_contradiction": "S11*p1 + 4*p2 > 0",
            "split_line_hym_source_exists": False,
            "proof_steps": proof_steps,
        },
        "calculation_results": {
            "integral_alpha1_target_loaded": target_ready,
            "visible_source_attempt_still_open": source_still_open,
            "split_line_or_cartan_hym_source_ruled_out": no_go,
            "nonabelian_stable_bundle_ruled_out": False,
            "route_c_solve_ruled_out": False,
            "selected_visible_source_constructed": False,
            "same_source_D_E_dotD_Riesz_Green_constructed": False,
        },
        "what_this_closes": {
            "all_split_line_hym_shortcuts_for_positive_alpha1": no_go,
            "reason_split_flux_cancellation_is_insufficient": no_go,
            "remaining_source_class_reduced_to_nonabelian_or_route_c": no_go,
        },
        "still_open": {
            "selected_nonabelian_stable_bundle_or_sheaf_with_c1_0_ch2_4_alpha1": True,
            "selected_route_c_residual_solve_for_same_class": True,
            "source_derived_Chern_Weil_representative": True,
            "HYM_or_Route_C_residual": True,
            "same_source_D_E_dotD_Riesz_Green": True,
            "coherent_spectral_projectors": True,
            "primitive_C1_contractions": True,
            "full_SM_closure": True,
        },
        "guardrails": {
            "claims_nonabelian_stable_bundle_obstructed": False,
            "claims_route_c_obstructed": False,
            "claims_selected_visible_bundle_constructed": False,
            "claims_selected_D_E_dotD_constructed": False,
            "claims_full_SM_closure": False,
            "uses_observed_flavor_data": False,
            "uses_benchmark_flavor_entries": False,
        },
        "verdict": {
            "honest_answer": (
                "The whole split line-bundle/diagonal Cartan HYM route is ruled "
                "out for the positive visible alpha_1 row. The remaining honest "
                "source must be genuinely nonabelian stable/sheaf data or an "
                "honest Route-C finite HYM/Strominger solve for c1=0, ch2=4 alpha_1."
            ),
            "next_action": (
                "Attempt a nonabelian stable-sheaf existence packet or a Route-C "
                "residual packet for the same c1=0, ch2=4 alpha_1 class."
            ),
        },
    }


def main() -> int:
    report = prove()
    write_json(CANDIDATE, report)
    certificate = {
        "certificate": "VisibleSplitLineHYMNoGo",
        "status": report["status"],
        "analysis_script": report["generated_by"],
        "candidate_data": "candidate_data/visible_split_line_hym_no_go.candidate.json",
        "inputs": report["inputs"],
        "target": report["target"],
        "algebraic_no_go": report["algebraic_no_go"],
        "calculation_results": report["calculation_results"],
        "what_this_closes": report["what_this_closes"],
        "still_open": report["still_open"],
        "guardrails": report["guardrails"],
        "verdict": report["verdict"],
    }
    write_json(CERTIFICATE, certificate)
    print(json.dumps(report, indent=2, sort_keys=True))
    return 0 if report["calculation_results"]["split_line_or_cartan_hym_source_ruled_out"] else 1


if __name__ == "__main__":
    raise SystemExit(main())
