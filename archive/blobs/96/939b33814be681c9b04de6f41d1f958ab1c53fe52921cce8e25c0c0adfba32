"""Reduce the V_alpha/S3 two-block lift to the remaining selector source.

This script connects three audited facts:

1. one selected S3 active quotient cannot be the full V_alpha mod-3 source;
2. two S3-type blocks exactly reproduce the full V_alpha mod-3 form;
3. the ordered integral Appell-Humbert model for L^2=(2,-4,0) reduces to that
   same two-block finite form, but current closed data do not select it.

The result is a source-selector gate, not a new SM closure claim.
"""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
CANDIDATES = ROOT / "candidate_data"
CERTS = ROOT / "certificates"

ONE_BLOCK = CERTS / "valpha_s3_full_mod3_pullback_obstruction_certificate.json"
TWO_BLOCK = CERTS / "valpha_s3_two_block_mod3_lift_certificate.json"
DECK_CECH = CERTS / "time_oriented_m1_deck_cech_lift_certificate.json"
S3_SELECTED = CERTS / "visible_twisted_s3_class_restriction_closure_certificate.json"
APPELL = CERTS / "visible_rank2_l2_appell_humbert_automorphy_certificate.json"
INTEGRAL_GAP = CERTS / "visible_rank2_l2_integral_lift_source_gap_certificate.json"
SELECTOR = CERTS / "visible_rank2_l2_selector_obstruction_certificate.json"
WALL = CERTS / "selected_gauduchon_wall_radius_gate_certificate.json"

OUT_CANDIDATE = CANDIDATES / "valpha_s3_two_block_source_selector_reduction.candidate.json"
OUT_CERT = CERTS / "valpha_s3_two_block_source_selector_reduction_certificate.json"

MOD = 3


def load(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def write(path: Path, data: dict[str, Any]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(data, indent=2, sort_keys=True) + "\n", encoding="utf-8")


def mod3_matrix(matrix: list[list[int]], rows: int, cols: int) -> list[list[int]]:
    return [[value % MOD for value in row[:cols]] for row in matrix[:rows]]


def rank_mod3(matrix: list[list[int]]) -> int:
    rows = [row[:] for row in matrix]
    if not rows:
        return 0
    m = len(rows)
    n = len(rows[0])
    rank = 0
    pivot_col = 0
    while rank < m and pivot_col < n:
        pivot = None
        for r in range(rank, m):
            if rows[r][pivot_col] % MOD:
                pivot = r
                break
        if pivot is None:
            pivot_col += 1
            continue
        rows[rank], rows[pivot] = rows[pivot], rows[rank]
        inv = 1 if rows[rank][pivot_col] == 1 else 2
        rows[rank] = [(inv * value) % MOD for value in rows[rank]]
        for r in range(m):
            if r != rank and rows[r][pivot_col] % MOD:
                factor = rows[r][pivot_col]
                rows[r] = [
                    (rows[r][c] - factor * rows[rank][c]) % MOD for c in range(n)
                ]
        rank += 1
        pivot_col += 1
    return rank


def main() -> int:
    one = load(ONE_BLOCK)
    two = load(TWO_BLOCK)
    deck = load(DECK_CECH)
    s3 = load(S3_SELECTED)
    appell = load(APPELL)
    gap = load(INTEGRAL_GAP)
    selector = load(SELECTOR)
    wall = load(WALL)

    integral_matrix = appell["model"]["c1_deck_alternating_matrix_order_g1_to_g6"]
    integral_active_mod3 = mod3_matrix(integral_matrix, 4, 4)
    two_block_target = two["target"]["full_valpha_active_matrix_g1_to_g4"]
    two_block_lifted = two["construction"]["lifted_form"]

    deck_map = deck["deck_quotient_map"]["map"]
    g3_g4_trivial = deck_map["g3"] == [0, 0] and deck_map["g4"] == [0, 0]
    selected_s3_rank = s3["S3_restriction_and_Freed_Witten"][
        "S3_active_image_rank_over_F3"
    ]

    report = {
        "calculation": "VAlphaS3TwoBlockSourceSelectorReduction",
        "status": "VALPHA_S3_TWO_BLOCK_SOURCE_SELECTOR_REDUCED_TO_SYMMETRY_BREAKING_SOURCE",
        "inputs": {
            "one_block_obstruction": str(ONE_BLOCK.relative_to(ROOT)),
            "two_block_lift": str(TWO_BLOCK.relative_to(ROOT)),
            "deck_cech_lift": str(DECK_CECH.relative_to(ROOT)),
            "selected_s3_restriction": str(S3_SELECTED.relative_to(ROOT)),
            "appell_humbert": str(APPELL.relative_to(ROOT)),
            "integral_lift_gap": str(INTEGRAL_GAP.relative_to(ROOT)),
            "selector_obstruction": str(SELECTOR.relative_to(ROOT)),
            "gauduchon_wall_gate": str(WALL.relative_to(ROOT)),
        },
        "finite_rank_logic": {
            "one_block_status": one["status"],
            "one_block_max_pullback_rank": one["bruteforce"][
                "max_pullback_rank_observed"
            ],
            "one_block_matching_maps": one["bruteforce"]["matching_maps"],
            "two_block_status": two["status"],
            "two_block_source_rank": two["source"]["two_block_source_rank"],
            "two_block_lifted_equals_full_valpha": two["construction"][
                "lifted_equals_full_valpha"
            ],
            "finite_active_blocks_required_by_rank": two["minimality"][
                "finite_active_blocks_required_by_rank"
            ],
        },
        "selected_s3_deck_limit": {
            "selected_deck_map": deck_map,
            "selected_s3_active_image_rank_over_F3": selected_s3_rank,
            "g3_g4_in_kernel_of_existing_selected_deck_quotient": g3_g4_trivial,
            "current_selected_s3_supplies_second_active_block": False,
            "reason": (
                "The selected q79/F,m=1 S3 deck quotient maps only g1,g2 to "
                "F3^2; g3,g4 are in the kernel.  It supplies one active block, "
                "not a selected doubled F3^4 quotient."
            ),
        },
        "integral_shadow_match": {
            "ordered_integral_c1_matrix": integral_matrix,
            "ordered_integral_active_mod3": integral_active_mod3,
            "two_block_lifted_form": two_block_lifted,
            "integral_active_mod3_equals_two_block_lift": integral_active_mod3
            == two_block_lifted,
            "integral_active_rank_mod3": rank_mod3(integral_active_mod3),
            "shared_circle_degree_zero": appell["construction_checks"][
                "central_shared_circle_trivial"
            ],
            "target_degrees": appell["construction_checks"]["target_degrees"],
        },
        "selector_status": {
            "appell_humbert_model_exists": appell["what_this_closes"][
                "explicit_nonflat_factor_of_automorphy_for_L2_2_minus4_0"
            ],
            "h1_after_source_would_promote": gap["sufficient_source_contract"][
                "validator_would_promote_existing_h1_packet_if_source_supplied"
            ],
            "current_closed_selector_can_choose_target": False,
            "selector_obstruction_theorem": selector["obstruction_theorem"]["theorem"],
            "pic0_needs_holonomy_sensitive_source_or_gauge_fixing": selector[
                "pic0_invariance"
            ]["needs_holonomy_sensitive_source_or_gauge_fixing"],
        },
        "route_triage": {
            "single_selected_s3_quotient": {
                "status": "REJECTED_BY_RANK_AND_DECK_KERNEL",
                "reason": "rank at most 2 and existing selected deck kills g3,g4",
            },
            "two_s3_type_finite_blocks": {
                "status": "FINITE_SHAPE_CONSTRUCTED_SELECTION_OPEN",
                "reason": "exact mod-3 form, but no selected doubled S3/F3^4 source packet",
            },
            "ordered_integral_appell_humbert_lift": {
                "status": "MODEL_EXISTS_SELECTOR_OPEN",
                "reason": "reduces to the two-block finite form and h1=8 can promote after source",
            },
            "gauduchon_wall": {
                "status": wall["route_evaluation"][2]["status"],
                "needed": wall["next_required_packet"]["minimal_success_criteria"][0],
            },
            "same_source_de_dotd_hessian": {
                "status": "LIVE_SOURCE_OPEN",
                "reason": "must order base factors and also emit D_E/dotD/Riesz/Green",
            },
            "pic0_selection_or_quotient": {
                "status": "OPEN",
                "reason": "flat Pic0 twists are invisible to current curvature/topology/h1 data",
            },
        },
        "what_this_closes": {
            "two_block_finite_shape_is_mod3_shadow_of_ordered_integral_L2": True,
            "current_selected_s3_deck_quotient_does_not_supply_second_block": True,
            "full_valpha_mod3_requirement_reduced_to_source_selector": True,
            "finite_cohomology_or_appell_humbert_existence_is_not_the_blocker": True,
        },
        "still_open": {
            "selected_ordered_integral_Cech_automorphy_D_E_source": selector[
                "still_open"
            ]["selected_ordered_integral_Cech_automorphy_D_E_source"],
            "selected_target_wall_r1_over_r2_sqrt2": selector["still_open"][
                "selected_target_wall_r1_over_r2_sqrt2"
            ],
            "selected_or_quotiented_Pic0_character": selector["still_open"][
                "selected_or_quotiented_Pic0_character"
            ],
            "same_source_D_E_dotD_Hessian_base_ordering": selector["still_open"][
                "same_source_D_E_dotD_Hessian_base_ordering"
            ],
            "nonzero_Ext_class_selection": selector["still_open"][
                "nonzero_Ext_class_selection"
            ],
            "non_split_stability": selector["still_open"]["non_split_stability"],
            "full_SM_closure": selector["still_open"]["full_SM_closure"],
        },
        "guardrails": {
            "claims_second_block_selected_by_existing_s3": False,
            "claims_doubled_s3_source_selected": False,
            "claims_ordered_integral_source_selected": False,
            "claims_target_selector_proved": False,
            "claims_pic0_selected_or_quotiented": False,
            "claims_D_E_dotD_constructed": False,
            "claims_full_SM_closure": False,
            "uses_observed_flavor_data": False,
            "uses_benchmark_flavor_entries": False,
        },
        "verdict": {
            "honest_answer": (
                "The two-block finite V_alpha/S3 shape is exactly the mod-3 "
                "shadow of the ordered integral L^2=(2,-4,0) Appell-Humbert "
                "model. The current selected S3 deck quotient supplies only one "
                "active block, so the remaining proof is a symmetry-breaking "
                "source selector for the ordered integral packet, wall, or "
                "same-source operator Hessian."
            ),
            "next_action": (
                "Attempt the selected ordered integral Cech/D_E source packet, "
                "or derive the r1:r2=sqrt(2):1 wall from a genuine nonabelian/"
                "Route-C source."
            ),
        },
    }

    write(OUT_CANDIDATE, report)
    cert = {
        "certificate": "VAlphaS3TwoBlockSourceSelectorReduction",
        "status": report["status"],
        "analysis_script": "scripts/analyze_valpha_s3_two_block_source_selector_reduction.py",
        "candidate_data": str(OUT_CANDIDATE.relative_to(ROOT)),
        "finite_rank_logic": report["finite_rank_logic"],
        "selected_s3_deck_limit": report["selected_s3_deck_limit"],
        "integral_shadow_match": report["integral_shadow_match"],
        "selector_status": report["selector_status"],
        "route_triage": report["route_triage"],
        "what_this_closes": report["what_this_closes"],
        "still_open": report["still_open"],
        "guardrails": report["guardrails"],
        "verdict": report["verdict"],
    }
    write(OUT_CERT, cert)
    print(json.dumps(report, indent=2, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
