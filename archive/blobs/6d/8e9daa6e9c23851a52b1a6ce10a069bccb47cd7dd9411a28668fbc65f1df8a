"""Analyze the minimal rank-two extension route for V_alpha.

The additive source-factor packet reduced the missing visible source to a
genuinely nonabelian factor V_alpha with c1=0, c2=+4 alpha_1, and c3=0.  The
smallest classical construction to test is a non-split rank-two extension

    0 -> L -> V_alpha -> L^{-1} -> 0.

For l=c1(L)=x a + y b + z c in the Iwasawa alpha basis, use

    l^2 = 2(xy alpha_1 + xz alpha_2 + yz alpha_3),
    c2(V_alpha) = -l^2.

Thus c2(V_alpha)=+4 alpha_1 requires xy=-2 and xz=yz=0.  This script enumerates
the primitive integer classes and records the exact missing non-split Ext and
stability data needed before this can be a selected source.
"""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
CERTIFICATES = ROOT / "certificates"
CANDIDATE_DATA = ROOT / "candidate_data"

ADDITIVE_ROUTE = CERTIFICATES / "visible_additive_source_factor_route_certificate.json"
SPLIT_NO_GO = CERTIFICATES / "visible_split_line_hym_no_go_certificate.json"
SIGN_GATE = CERTIFICATES / "visible_stable_source_sign_gate_certificate.json"

CANDIDATE = CANDIDATE_DATA / "visible_rank2_extension_valpha_route.candidate.json"
CERTIFICATE = CERTIFICATES / "visible_rank2_extension_valpha_route_certificate.json"


Vector3 = tuple[int, int, int]


def load_json(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def write_json(path: Path, data: dict[str, Any]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(data, indent=2, sort_keys=True) + "\n", encoding="utf-8")


def square_coeffs(vector: Vector3) -> Vector3:
    x, y, z = vector
    return (2 * x * y, 2 * x * z, 2 * y * z)


def c2_extension_coeffs(vector: Vector3) -> Vector3:
    sx, sy, sz = square_coeffs(vector)
    return (-sx, -sy, -sz)


def primitive(vector: Vector3) -> bool:
    x, y, z = (abs(value) for value in vector)
    from math import gcd

    return gcd(gcd(x, y), z) == 1


def slope_expression(vector: Vector3) -> str:
    x, y, z = vector
    terms = []
    for coeff, label in ((x, "p1"), (y, "p2"), (z, "p3")):
        if coeff:
            terms.append(f"{coeff}*{label}")
    return " + ".join(terms).replace("+ -", "- ") or "0"


def chamber_witness(vector: Vector3) -> dict[str, Any]:
    x, y, z = vector
    witnesses: dict[Vector3, tuple[int, int, int]] = {
        (1, -2, 0): (1, 1, 1),
        (-1, 2, 0): (3, 1, 1),
        (2, -1, 0): (1, 3, 1),
        (-2, 1, 0): (1, 1, 1),
    }
    p = witnesses[vector]
    value = x * p[0] + y * p[1] + z * p[2]
    return {
        "positive_slope_vector_p": list(p),
        "mu_L": value,
        "necessary_subline_slope_negative": value < 0,
    }


def analyze() -> dict[str, Any]:
    additive = load_json(ADDITIVE_ROUTE)
    split = load_json(SPLIT_NO_GO)
    sign = load_json(SIGN_GATE)

    target = (4, 0, 0)
    candidates: list[dict[str, Any]] = []
    for x in range(-4, 5):
        for y in range(-4, 5):
            for z in range(-2, 3):
                vector = (x, y, z)
                if vector == (0, 0, 0) or not primitive(vector):
                    continue
                c2 = c2_extension_coeffs(vector)
                if c2 == target:
                    candidates.append(
                        {
                            "l_vector_abc": list(vector),
                            "l_squared_alpha_coeffs": list(square_coeffs(vector)),
                            "c2_extension_alpha_coeffs": list(c2),
                            "slope_mu_L": slope_expression(vector),
                            "slope_chamber_witness": chamber_witness(vector),
                            "non_split_extension_space_needed": "Ext^1(L^{-1},L)=H^1(X,L^2)",
                        }
                    )

    route_ready = (
        additive.get("status")
        == "VISIBLE_ADDITIVE_SOURCE_FACTOR_TOPOLOGY_FORMULATED_SELECTION_OPEN"
        and split.get("status")
        == "VISIBLE_SPLIT_LINE_HYM_SOURCE_NO_GO_NONABELIAN_OR_ROUTE_C_REQUIRED"
        and sign.get("status")
        == "VISIBLE_STABLE_SOURCE_SIGN_CONVENTION_GATE_CLOSED_SOURCE_OPEN"
        and len(candidates) == 4
        and all(item["slope_chamber_witness"]["necessary_subline_slope_negative"] for item in candidates)
    )

    return {
        "calculation": "VisibleRank2ExtensionVAlphaRoute",
        "status": (
            "VISIBLE_RANK2_EXTENSION_VALPHA_ROUTE_FORMULATED_EXT_STABILITY_OPEN"
            if route_ready
            else "VISIBLE_RANK2_EXTENSION_VALPHA_ROUTE_NOT_VERIFIED"
        ),
        "generated_by": "scripts/analyze_visible_rank2_extension_valpha_route.py",
        "inputs": {
            "visible_additive_source_factor_route_certificate": ADDITIVE_ROUTE.name,
            "visible_split_line_hym_no_go_certificate": SPLIT_NO_GO.name,
            "visible_stable_source_sign_gate_certificate": SIGN_GATE.name,
        },
        "rank2_extension_schema": {
            "sequence": "0 -> L -> V_alpha -> L^{-1} -> 0",
            "rank": 2,
            "structure_group_target": "SU(2)-type if determinant is trivial and extension is non-split",
            "c1": [0, 0, 0],
            "c3": 0,
            "formula_l_squared": "l^2=2(xy alpha_1+xz alpha_2+yz alpha_3)",
            "formula_c2": "c2(V_alpha)=-l^2",
            "target_c2": list(target),
        },
        "finite_line_class_solutions": candidates,
        "why_split_no_go_not_violated": {
            "split_no_go_scope": "finite split line-bundle or diagonal Cartan HYM source for the positive trace row",
            "extension_route_difference": (
                "V_alpha must be a non-split extension. The line L is a subobject "
                "used to build the holomorphic bundle; the Chern-Weil/HYM source "
                "is not the direct sum L plus L^{-1}."
            ),
            "split_limit_forbidden": True,
        },
        "stability_contract": {
            "necessary_condition_checked": "the displayed subline L can have negative slope in a positive chamber",
            "slope_vector": "p=(p1,p2,p3), p_i>0",
            "not_sufficient": True,
            "missing_sufficient_inputs": [
                "nonzero extension class in H^1(X,L^2)",
                "proof the extension is non-split",
                "proof no other positive-slope line subsheaf injects into V_alpha",
                "selected Gauduchon/Kahler chamber for the slope vector",
                "source-derived HYM/Strominger residual or Li-Yau/HYM existence certificate",
            ],
        },
        "calculation_results": {
            "rank2_extension_topological_classes_found": True,
            "number_of_primitive_line_classes": len(candidates),
            "all_candidates_hit_c2_4_alpha1": all(
                item["c2_extension_alpha_coeffs"] == [4, 0, 0] for item in candidates
            ),
            "slope_negative_chambers_exist": all(
                item["slope_chamber_witness"]["necessary_subline_slope_negative"] for item in candidates
            ),
            "non_split_extension_constructed": False,
            "stability_proved": False,
            "selected_hym_source_constructed": False,
            "same_source_D_E_dotD_Riesz_Green_constructed": False,
        },
        "what_this_closes": {
            "minimal_rank2_extension_c2_arithmetic": route_ready,
            "finite_candidate_line_classes_for_L": True,
            "slope_chamber_necessary_condition": True,
            "exact_next_ext_stability_inputs_identified": True,
        },
        "still_open": {
            "compute_H1_X_L_squared_for_candidate_classes": True,
            "select_nonzero_extension_class": True,
            "prove_non_split_extension_stability": True,
            "derive_source_Chern_Weil_representative": True,
            "prove_HYM_or_Route_C_residual": True,
            "protect_or_recompute_E8_commutant_and_SM_sector_dictionary": True,
            "derive_same_total_source_D_E_dotD_Riesz_Green": True,
            "coherent_spectral_projectors": True,
            "primitive_C1_contractions": True,
            "full_SM_closure": True,
        },
        "guardrails": {
            "claims_extension_class_exists": False,
            "claims_stability_proved": False,
            "claims_selected_hym_source_exists": False,
            "claims_split_limit_allowed": False,
            "claims_selected_D_E_dotD_constructed": False,
            "claims_full_SM_closure": False,
            "uses_observed_flavor_data": False,
            "uses_benchmark_flavor_entries": False,
        },
        "verdict": {
            "honest_answer": (
                "The minimal rank-two extension route is arithmetically viable: "
                "four primitive line classes L have c2(V_alpha)=+4 alpha_1 for "
                "a non-split extension 0->L->V_alpha->L^{-1}->0, and each has "
                "a positive slope chamber where the displayed subline has "
                "negative slope. This does not yet prove a selected source; "
                "the missing object is now the nonzero Ext class plus a stability "
                "and HYM/Strominger certificate."
            ),
            "next_action": (
                "Compute H^1(X,L^2) or an equivalent Cech/monad extension class "
                "for one candidate line class, then prove non-split stability and "
                "feed the resulting V_alpha into the same-source operator pipeline."
            ),
        },
    }


def main() -> int:
    report = analyze()
    write_json(CANDIDATE, report)
    certificate = {
        "certificate": "VisibleRank2ExtensionVAlphaRoute",
        "status": report["status"],
        "analysis_script": report["generated_by"],
        "candidate_data": "candidate_data/visible_rank2_extension_valpha_route.candidate.json",
        "inputs": report["inputs"],
        "rank2_extension_schema": report["rank2_extension_schema"],
        "finite_line_class_solutions": report["finite_line_class_solutions"],
        "why_split_no_go_not_violated": report["why_split_no_go_not_violated"],
        "stability_contract": report["stability_contract"],
        "calculation_results": report["calculation_results"],
        "what_this_closes": report["what_this_closes"],
        "still_open": report["still_open"],
        "guardrails": report["guardrails"],
        "verdict": report["verdict"],
    }
    write_json(CERTIFICATE, certificate)
    print(json.dumps(report, indent=2, sort_keys=True))
    return 0 if report["status"] == "VISIBLE_RANK2_EXTENSION_VALPHA_ROUTE_FORMULATED_EXT_STABILITY_OPEN" else 1


if __name__ == "__main__":
    raise SystemExit(main())
