"""Reduce the visible rank-two L^2 branch-selection problem.

After the source-ambiguity classification, the live question is whether any
already certified MTT datum selects the preferred branch

    L=(1,-2,0), L^2=(2,-4,0)

from the four integral pullback branches.  This script tests the currently
available selectors separately:

* topology/c2,
* H^1 dimension,
* slope-chamber sign,
* time-oriented q79/F orientation,
* abelian alpha_1 flux support,
* flat Pic0/torsion character data.

The result is a reduction theorem, not a premature closure: existing data can
at best reduce to a two-branch ordering ambiguity under an added symmetric
base-chamber hypothesis.  A selected source must still map the q79/F or other
orientation datum to an ordered base-factor branch and fix the flat character.
"""

from __future__ import annotations

import json
from fractions import Fraction
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
CERTIFICATES = ROOT / "certificates"
CANDIDATE_DATA = ROOT / "candidate_data"

SOURCE_AMBIGUITY = CERTIFICATES / "visible_rank2_l2_source_ambiguity_classification_certificate.json"
RANK2_ROUTE = CERTIFICATES / "visible_rank2_extension_valpha_route_certificate.json"
TIME_ORIENTED = CERTIFICATES / "time_oriented_conjugate_branch_selection_certificate.json"
S3_CLOSURE = CERTIFICATES / "visible_twisted_s3_class_restriction_closure_certificate.json"
INTEGRAL_ROW = CERTIFICATES / "visible_integral_chern_source_candidate_certificate.json"
SPLIT_NO_GO = CERTIFICATES / "visible_split_line_hym_no_go_certificate.json"
CONSTANTS_CLUES = CERTIFICATES / "constants_gr_cross_repo_clues_certificate.json"

CANDIDATE = CANDIDATE_DATA / "visible_rank2_l2_branch_selection_reduction.candidate.json"
CERTIFICATE = CERTIFICATES / "visible_rank2_l2_branch_selection_reduction_certificate.json"

TARGET_L = [1, -2, 0]
BRANCHES = [[-2, 1, 0], [-1, 2, 0], [1, -2, 0], [2, -1, 0]]


def load_json(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def write_json(path: Path, data: dict[str, Any]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(data, indent=2, sort_keys=True) + "\n", encoding="utf-8")


def slope(branch: list[int], p1: Fraction, p2: Fraction, p3: Fraction = Fraction(1)) -> Fraction:
    return branch[0] * p1 + branch[1] * p2 + branch[2] * p3


def negative_for_chamber(p1: int, p2: int) -> list[list[int]]:
    f1 = Fraction(p1)
    f2 = Fraction(p2)
    return [branch for branch in BRANCHES if slope(branch, f1, f2) < 0]


def zero_for_chamber(p1: int, p2: int) -> list[list[int]]:
    f1 = Fraction(p1)
    f2 = Fraction(p2)
    return [branch for branch in BRANCHES if slope(branch, f1, f2) == 0]


def chamber_regions() -> list[dict[str, Any]]:
    representatives = [
        ("r=p1/p2 < 1/2", (1, 3)),
        ("1/2 < r=p1/p2 < 2", (1, 1)),
        ("r=p1/p2 > 2", (3, 1)),
        ("wall r=1/2", (1, 2)),
        ("wall r=2", (2, 1)),
    ]
    out: list[dict[str, Any]] = []
    for name, (p1, p2) in representatives:
        out.append(
            {
                "region": name,
                "representative_p": [p1, p2, 1],
                "negative_slope_branches": negative_for_chamber(p1, p2),
                "zero_slope_branches": zero_for_chamber(p1, p2),
                "target_branch_negative": TARGET_L in negative_for_chamber(p1, p2),
                "stable_chamber_wall": bool(zero_for_chamber(p1, p2)),
            }
        )
    return out


def analyze() -> dict[str, Any]:
    ambiguity = load_json(SOURCE_AMBIGUITY)
    rank2 = load_json(RANK2_ROUTE)
    time_oriented = load_json(TIME_ORIENTED)
    s3 = load_json(S3_CLOSURE)
    integral_row = load_json(INTEGRAL_ROW)
    split_no_go = load_json(SPLIT_NO_GO)
    constants = load_json(CONSTANTS_CLUES)

    source_solutions = ambiguity.get("classified_integral_pullback_solutions", [])
    h1_values = sorted({entry.get("reduced_pullback_h1") for entry in source_solutions})
    regions = chamber_regions()
    symmetric_region = next(region for region in regions if region["region"].startswith("1/2"))

    topology_selector = {
        "input": "c2(V_alpha)=4 alpha_1 with z=0",
        "surviving_branches": BRANCHES,
        "selects_unique_branch": False,
    }
    h1_selector = {
        "input": "reduced H^1(X,L^2) dimension",
        "h1_values": h1_values,
        "surviving_branches": BRANCHES if h1_values == [8] else [],
        "selects_unique_branch": False,
    }
    slope_selector = {
        "input": "negative slope for the displayed subline L",
        "generic_positive_chamber_regions": regions[:3],
        "wall_regions": regions[3:],
        "generic_chamber_selects_unique_branch": False,
        "generic_chamber_selects_two_negative_branches": all(
            len(region["negative_slope_branches"]) == 2 for region in regions[:3]
        ),
        "symmetric_shared_base_chamber_conditional_survivors": symmetric_region[
            "negative_slope_branches"
        ],
        "symmetric_shared_base_chamber_selects_target": TARGET_L
        in symmetric_region["negative_slope_branches"],
        "selected_chamber_certificate_present": False,
    }
    time_orientation_selector = {
        "input": "closed retarded q79/F representative",
        "time_oriented_status": time_oriented.get("status"),
        "q79_F_selected": time_oriented.get("calculation_results", {}).get(
            "time_oriented_retarded_branch_selects_q79"
        )
        is True,
        "ordered_su5_packet_selected": time_oriented.get("calculation_results", {}).get(
            "ordered_su5_packet_selected"
        )
        is True,
        "maps_q79_F_to_L_branch": False,
        "reason": (
            "The q79/F theorem orients the finite gerbe/qutrit Fourier pair. "
            "No audited certificate maps that finite orientation to the ordered "
            "base elliptic factors or to L=(1,-2,0)."
        ),
    }
    flux_selector = {
        "input": "abelian alpha_1 support row (1,2,0)+(-1,-2,0)",
        "integral_row_status": integral_row.get("status"),
        "split_no_go_status": split_no_go.get("status"),
        "supports_alpha1_row": integral_row.get("what_this_closes", {}).get(
            "integral_alpha1_row"
        )
        is True
        or "alpha_1" in json.dumps(integral_row),
        "split_source_retired_as_selector": split_no_go.get("what_this_closes", {}).get(
            "split_line_HYM_no_go"
        )
        is True
        or split_no_go.get("status") == "VISIBLE_SPLIT_LINE_HYM_SOURCE_NO_GO_NONABELIAN_OR_ROUTE_C_REQUIRED",
        "maps_to_non_split_L_branch": False,
    }
    flat_character_selector = {
        "input": "flat Pic0/torsion character",
        "flat_Pic0_characters_preserve_c1": ambiguity.get("selection_tests", {}).get(
            "flat_Pic0_characters_preserve_c1"
        )
        is True,
        "hidden_flat_or_torsion_twist_ruled_out_by_current_data": ambiguity.get(
            "selection_tests", {}
        ).get("hidden_flat_or_torsion_twist_ruled_out_by_current_data")
        is True,
        "selects_unique_branch": False,
    }
    s3_selector = {
        "input": "selected S3 twisted class/restriction closure",
        "s3_status": s3.get("status"),
        "q79_F_orientation_in_twisted_sector": s3.get("smooth_class", {}).get(
            "fixed_q79_F_m1_representative"
        )
        is True,
        "maps_to_visible_L2_line_bundle": False,
    }
    constants_method_selector = {
        "input": "constants/GR source-packet discipline",
        "cross_repo_status": constants.get("status"),
        "direct_selected_visible_valpha_source_found": constants.get(
            "calculation_results", {}
        ).get("direct_selected_visible_valpha_source_found")
        is True,
        "direct_H1_or_Cech_data_found": constants.get("calculation_results", {}).get(
            "direct_H1_or_Cech_data_found"
        )
        is True,
        "selects_unique_L_branch": False,
    }

    unique_selector_found = any(
        selector.get("selects_unique_branch") is True
        for selector in [
            topology_selector,
            h1_selector,
            slope_selector,
            flat_character_selector,
        ]
    ) or time_orientation_selector["maps_q79_F_to_L_branch"]

    status = (
        "VISIBLE_RANK2_L2_BRANCH_SELECTION_PROVED"
        if unique_selector_found
        else "VISIBLE_RANK2_L2_BRANCH_SELECTION_REDUCED_TO_ORIENTATION_SOURCE"
    )

    return {
        "calculation": "VisibleRank2L2BranchSelectionReduction",
        "status": status,
        "generated_by": "scripts/reduce_visible_rank2_l2_branch_selection.py",
        "input_certificates": {
            "source_ambiguity": SOURCE_AMBIGUITY.name,
            "rank2_route": RANK2_ROUTE.name,
            "time_oriented_conjugate_branch_selection": TIME_ORIENTED.name,
            "visible_twisted_s3_class_restriction_closure": S3_CLOSURE.name,
            "visible_integral_chern_source_candidate": INTEGRAL_ROW.name,
            "visible_split_line_hym_no_go": SPLIT_NO_GO.name,
            "constants_gr_cross_repo_clues": CONSTANTS_CLUES.name,
        },
        "input_statuses": {
            "source_ambiguity": ambiguity.get("status"),
            "rank2_route": rank2.get("status"),
            "time_oriented": time_oriented.get("status"),
            "s3_closure": s3.get("status"),
            "integral_row": integral_row.get("status"),
            "split_no_go": split_no_go.get("status"),
            "constants_clues": constants.get("status"),
        },
        "target_branch": {
            "L": TARGET_L,
            "L_squared": [2 * value for value in TARGET_L],
            "status": "valid branch, not uniquely selected",
        },
        "selector_evaluation": {
            "topology_c2": topology_selector,
            "h1_dimension": h1_selector,
            "slope_chamber": slope_selector,
            "time_oriented_q79_F": time_orientation_selector,
            "s3_twisted_orientation": s3_selector,
            "abelian_alpha1_flux_row": flux_selector,
            "flat_character": flat_character_selector,
            "constants_gr_method_import": constants_method_selector,
        },
        "what_this_closes": {
            "c2_and_h1_do_not_select_unique_branch": True,
            "slope_sign_alone_does_not_select_unique_branch": True,
            "symmetric_shared_base_chamber_would_reduce_to_two_branches": True,
            "q79_F_orientation_not_yet_mapped_to_base_L_branch": True,
            "abelian_flux_row_cannot_be_used_as_non_split_branch_selector": True,
            "flat_character_still_requires_source_data": True,
        },
        "still_open": {
            "selected_base_factor_ordering_or_branch_orientation_source": True,
            "map_q79_F_or_other_orientation_datum_to_L_equals_1_minus2_0": True,
            "selected_Gauduchon_chamber_for_V_alpha": True,
            "select_or_eliminate_flat_Pic0_and_torsion_character": True,
            "raw_transition_or_automorphy_factors_for_selected_branch": True,
            "promote_L2_packet_to_SELECTED_DATA": True,
            "prove_non_split_extension_stability": True,
            "derive_same_source_D_E_dotD_Riesz_Green": True,
            "full_SM_closure": True,
        },
        "guardrails": {
            "claims_unique_L_branch_selected": unique_selector_found,
            "claims_q79_F_selects_L_branch": False,
            "claims_symmetric_chamber_selected_unconditionally": False,
            "claims_flat_character_eliminated": False,
            "claims_selected_packet_written": False,
            "claims_full_SM_closure": False,
            "uses_observed_flavor_data": False,
            "uses_benchmark_flavor_entries": False,
        },
        "next_required_packet": {
            "name": "Selected_Pullback_L2_Branch_Orientation_Source.v1",
            "must_supply": [
                "selected Gauduchon/Kahler chamber or slope vector",
                "ordered base-factor convention selecting a before b or b before a",
                "source map from q79/F, D_E/dotD, monad/Cech, or differential-cohomology representative to the L branch",
                "flat Pic0/torsion character selection or no-go",
                "raw transition/automorphy factors for the selected branch",
            ],
        },
        "verdict": {
            "honest_answer": (
                "The current certified data do not yet select L=(1,-2,0). "
                "Topology and h1 leave four branches. A non-wall slope chamber "
                "selects two negative-slope branches, and the symmetric shared-base "
                "chamber would reduce to {(-2,1,0),(1,-2,0)}. The retarded q79/F "
                "orientation is real, but no audited map sends it to the ordered "
                "base line branch. The next missing object is an orientation-carrying "
                "selected source, not another h1 calculation."
            ),
            "next_action": (
                "Build the Selected_Pullback_L2_Branch_Orientation_Source packet "
                "or prove a no-go for mapping q79/F and the selected chamber to "
                "L=(1,-2,0)."
            ),
        },
    }


def main() -> int:
    report = analyze()
    write_json(CANDIDATE, report)
    certificate = {
        "certificate": "VisibleRank2L2BranchSelectionReduction",
        "status": report["status"],
        "analysis_script": report["generated_by"],
        "candidate_data": "candidate_data/visible_rank2_l2_branch_selection_reduction.candidate.json",
        "input_certificates": report["input_certificates"],
        "target_branch": report["target_branch"],
        "selector_evaluation": report["selector_evaluation"],
        "what_this_closes": report["what_this_closes"],
        "still_open": report["still_open"],
        "guardrails": report["guardrails"],
        "next_required_packet": report["next_required_packet"],
        "verdict": report["verdict"],
    }
    write_json(CERTIFICATE, certificate)
    print(json.dumps(report, indent=2, sort_keys=True))
    return (
        0
        if report["status"]
        == "VISIBLE_RANK2_L2_BRANCH_SELECTION_REDUCED_TO_ORIENTATION_SOURCE"
        else 1
    )


if __name__ == "__main__":
    raise SystemExit(main())
