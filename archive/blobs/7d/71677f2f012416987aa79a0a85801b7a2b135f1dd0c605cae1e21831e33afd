"""Classify the source-selection ambiguity for the visible rank-two L^2 route.

The pullback-Cech packet proved that L=(1,-2,0) gives a conditional
H^1(X,L^2) packet with h1=8.  The next question is whether the selected source
can be recovered from the topological target c2(V)=4 alpha_1 alone.

It cannot.  This script solves the exact integer Chern equations for rank-two
extensions

    0 -> L -> V -> L^{-1} -> 0,
    c1(V)=0,
    c2(V)=4 alpha_1,

under the pullback/no-central-degree constraint z=0.  It also records the
standard Pic^0 flat-character ambiguity: for nonzero elliptic degrees the
cohomology dimensions are constant under flat twists, so c1 and h1 cannot rule
out hidden flat characters.  The output is a precise certificate for what the
missing selected source must still provide.
"""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
CERTIFICATES = ROOT / "certificates"
CANDIDATE_DATA = ROOT / "candidate_data"

PULLBACK_CERT = CERTIFICATES / "visible_rank2_l2_pullback_cech_attempt_certificate.json"
SELECTION_CERT = CERTIFICATES / "visible_rank2_l2_pullback_selection_attempt_certificate.json"
RANK2_ROUTE = CERTIFICATES / "visible_rank2_extension_valpha_route_certificate.json"

CANDIDATE = CANDIDATE_DATA / "visible_rank2_l2_source_ambiguity_classification.candidate.json"
CERTIFICATE = CERTIFICATES / "visible_rank2_l2_source_ambiguity_classification_certificate.json"

TARGET_C2 = [4, 0, 0]
TARGET_L = [1, -2, 0]


def load_json(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def write_json(path: Path, data: dict[str, Any]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(data, indent=2, sort_keys=True) + "\n", encoding="utf-8")


def c1_square_alpha_coeffs(vector: list[int]) -> list[int]:
    x, y, z = vector
    return [2 * x * y, 2 * x * z, 2 * y * z]


def c2_extension_alpha_coeffs(vector: list[int]) -> list[int]:
    return [-value for value in c1_square_alpha_coeffs(vector)]


def divisors(value: int) -> list[int]:
    value = abs(value)
    out: set[int] = set()
    for candidate in range(1, value + 1):
        if value % candidate == 0:
            out.add(candidate)
            out.add(-candidate)
    return sorted(out)


def solve_rank2_pullback_c2(target_c2: list[int]) -> list[list[int]]:
    """Solve -c1(L)^2 = target_c2 with z=0 exactly over integers."""
    first, second, third = target_c2
    if second != 0 or third != 0:
        return []
    if first % 2 != 0:
        return []
    product = -first // 2
    solutions: list[list[int]] = []
    for x in divisors(product):
        if product % x != 0:
            continue
        y = product // x
        candidate = [x, y, 0]
        if c2_extension_alpha_coeffs(candidate) == target_c2:
            solutions.append(candidate)
    return sorted(solutions)


def elliptic_hodge_for_degree(degree: int) -> dict[str, int]:
    if degree > 0:
        return {"h0": degree, "h1": 0}
    if degree < 0:
        return {"h0": 0, "h1": -degree}
    return {"h0": 1, "h1": 1}


def base_hodge_for_l2(l_vector: list[int]) -> dict[str, Any]:
    l2 = [2 * value for value in l_vector]
    first = elliptic_hodge_for_degree(l2[0])
    second = elliptic_hodge_for_degree(l2[1])
    h0 = first["h0"] * second["h0"]
    h1 = first["h0"] * second["h1"] + first["h1"] * second["h0"]
    h2 = first["h1"] * second["h1"]
    return {
        "l_vector_abc": l_vector,
        "l_squared_vector_abc": l2,
        "c2_extension_alpha_coeffs": c2_extension_alpha_coeffs(l_vector),
        "c1_L_squared_square_alpha_coeffs": c1_square_alpha_coeffs(l2),
        "factor_hodge": {
            "E1": {"degree": l2[0], **first},
            "E2": {"degree": l2[1], **second},
        },
        "base_hodge": {"h0": h0, "h1": h1, "h2": h2},
        "reduced_pullback_h1": h1,
        "is_target_branch_representative": l_vector == TARGET_L,
    }


def analyze() -> dict[str, Any]:
    pullback = load_json(PULLBACK_CERT)
    selection = load_json(SELECTION_CERT)
    rank2 = load_json(RANK2_ROUTE)

    solutions = solve_rank2_pullback_c2(TARGET_C2)
    classified = [base_hodge_for_l2(solution) for solution in solutions]
    h1_values = sorted({entry["reduced_pullback_h1"] for entry in classified})
    target_entry = next(
        entry for entry in classified if entry["l_vector_abc"] == TARGET_L
    )

    topology_selects_unique_l = len(classified) == 1
    cohomology_selects_unique_l = len(h1_values) == 1 and len(classified) == 1
    flat_twist_invisible_to_c1_h1 = all(
        entry["factor_hodge"]["E1"]["degree"] != 0
        and entry["factor_hodge"]["E2"]["degree"] != 0
        and entry["reduced_pullback_h1"] == 8
        for entry in classified
    )
    branch_orientation_required = (
        len(classified) > 1
        and target_entry["reduced_pullback_h1"] == 8
        and selection.get("unconditional_selection_theorem", {}).get("proved") is False
    )

    status = (
        "VISIBLE_RANK2_L2_SOURCE_AMBIGUITY_CLASSIFIED_SELECTION_DATA_REQUIRED"
        if len(classified) == 4
        and h1_values == [8]
        and flat_twist_invisible_to_c1_h1
        and branch_orientation_required
        else "VISIBLE_RANK2_L2_SOURCE_AMBIGUITY_CLASSIFICATION_FAILED"
    )

    return {
        "calculation": "VisibleRank2L2SourceAmbiguityClassification",
        "status": status,
        "generated_by": "scripts/classify_visible_rank2_l2_source_ambiguity.py",
        "input_certificates": {
            "rank2_route": RANK2_ROUTE.name,
            "pullback_cech_attempt": PULLBACK_CERT.name,
            "pullback_selection_attempt": SELECTION_CERT.name,
        },
        "input_statuses": {
            "rank2_route": rank2.get("status"),
            "pullback_cech_attempt": pullback.get("status"),
            "pullback_selection_attempt": selection.get("status"),
        },
        "equations_solved": {
            "extension_sequence": "0 -> L -> V_alpha -> L^{-1} -> 0",
            "c1_V": [0, 0, 0],
            "c2_target_alpha_coeffs": TARGET_C2,
            "pullback_no_central_degree_constraint": "z=0",
            "integer_equation": "xy=-2, z=0",
        },
        "classified_integral_pullback_solutions": classified,
        "selection_tests": {
            "number_of_c2_compatible_integral_pullback_L_vectors": len(classified),
            "all_c2_compatible_solutions_have_reduced_h1_8": h1_values == [8],
            "topological_c2_data_selects_unique_L": topology_selects_unique_l,
            "cohomology_dimension_selects_unique_L": cohomology_selects_unique_l,
            "target_L_1_minus2_0_is_one_valid_branch": target_entry["is_target_branch_representative"],
            "flat_Pic0_characters_preserve_c1": True,
            "nonzero_elliptic_degrees_make_hodge_dimensions_flat_twist_invariant": flat_twist_invisible_to_c1_h1,
            "hidden_flat_or_torsion_twist_ruled_out_by_current_data": False,
        },
        "what_this_proves": {
            "c2_target_forces_base_pullback_no_central_degree": True,
            "c2_target_does_not_select_orientation_or_factor_order": True,
            "h1_8_is_robust_across_the_four_integral_c2_branches": True,
            "flat_character_choice_is_extra_source_data_not_seen_by_c1_or_h1": True,
            "selected_source_certificate_must_choose_branch_and_twist": True,
        },
        "still_open": {
            "select_L_equals_1_minus2_0_over_the_other_three_c2_branches": True,
            "rule_out_or_select_flat_Pic0_character": True,
            "rule_out_central_or_torsion_twist_if_the_source_allows_it": True,
            "supply_raw_transition_or_automorphy_factors_for_the_selected_character": True,
            "promote_pullback_packet_to_SELECTED_DATA": True,
            "prove_non_split_extension_stability": True,
            "derive_same_source_D_E_dotD_Riesz_Green": True,
            "full_SM_closure": True,
        },
        "guardrails": {
            "claims_unconditional_selection": False,
            "claims_c2_or_h1_selects_unique_source": False,
            "claims_flat_twist_eliminated": False,
            "claims_selected_packet_written": False,
            "claims_stability_proved": False,
            "claims_full_SM_closure": False,
            "uses_observed_flavor_data": False,
            "uses_benchmark_flavor_entries": False,
        },
        "verdict": {
            "honest_answer": (
                "The c2=4 alpha_1 rank-two topology narrows the visible line to "
                "four pullback integral branches and forces zero central degree, "
                "but it does not uniquely select L=(1,-2,0).  All four branches "
                "give the same reduced h1=8.  Flat Pic0 characters also preserve "
                "c1 and these hodge dimensions, so the selected-source certificate "
                "must include branch orientation and flat/torsion character data."
            ),
            "next_action": (
                "Find the MTT branch-orientation rule or raw automorphy source "
                "that chooses L=(1,-2,0) and fixes the flat character.  Without "
                "that source datum, promoting the packet would be a hidden knob."
            ),
        },
    }


def main() -> int:
    report = analyze()
    write_json(CANDIDATE, report)
    certificate = {
        "certificate": "VisibleRank2L2SourceAmbiguityClassification",
        "status": report["status"],
        "analysis_script": report["generated_by"],
        "candidate_data": "candidate_data/visible_rank2_l2_source_ambiguity_classification.candidate.json",
        "input_certificates": report["input_certificates"],
        "equations_solved": report["equations_solved"],
        "classified_integral_pullback_solutions": report[
            "classified_integral_pullback_solutions"
        ],
        "selection_tests": report["selection_tests"],
        "what_this_proves": report["what_this_proves"],
        "still_open": report["still_open"],
        "guardrails": report["guardrails"],
        "verdict": report["verdict"],
    }
    write_json(CERTIFICATE, certificate)
    print(json.dumps(report, indent=2, sort_keys=True))
    return (
        0
        if report["status"]
        == "VISIBLE_RANK2_L2_SOURCE_AMBIGUITY_CLASSIFIED_SELECTION_DATA_REQUIRED"
        else 1
    )


if __name__ == "__main__":
    raise SystemExit(main())
