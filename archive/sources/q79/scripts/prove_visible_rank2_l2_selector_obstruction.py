"""Prove the current-data obstruction to selecting visible L=(1,-2,0).

The previous packet constructed the ordered Appell-Humbert representative for
L^2=(2,-4,0).  This script asks whether the *existing selected MTT data* prove
that this representative, rather than the swapped one and rather than a Pic0
twist, is selected.

The result is a no-hidden-selector theorem.  With the currently closed inputs,
target and swapped branches are related by the base-swap symmetry, and all
closed invariants used so far are equal on them.  Likewise flat Pic0 twists are
invisible to the topological/cohomological/curvature data currently closed.
Therefore a proof of unique target selection cannot be extracted from the
existing packets without adding a symmetry-breaking source: selected wall,
selected ordered integral source, or same-source D_E/dotD/Hessian data.
"""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
CERTIFICATES = ROOT / "certificates"
CANDIDATE_DATA = ROOT / "candidate_data"

SOURCE_AMBIGUITY = CERTIFICATES / "visible_rank2_l2_source_ambiguity_classification_certificate.json"
BRANCH_REDUCTION = CERTIFICATES / "visible_rank2_l2_branch_selection_reduction_certificate.json"
ORIENTATION_GATE = CERTIFICATES / "selected_pullback_l2_branch_orientation_source_gate_certificate.json"
GAUDUCHON_GATE = CERTIFICATES / "selected_gauduchon_wall_radius_gate_certificate.json"
INTEGRAL_GAP = CERTIFICATES / "visible_rank2_l2_integral_lift_source_gap_certificate.json"
APPELL_HUMBERT = CERTIFICATES / "visible_rank2_l2_appell_humbert_automorphy_certificate.json"
TIME_ORIENTED = CERTIFICATES / "time_oriented_conjugate_branch_selection_certificate.json"
FOURIER_TYPE = CERTIFICATES / "selected_gerbe_fourier_type_theorem_certificate.json"
DECK = CERTIFICATES / "iwasawa_standard_lattice_deck_scaffold_certificate.json"

CANDIDATE = CANDIDATE_DATA / "visible_rank2_l2_selector_obstruction.candidate.json"
CERTIFICATE = CERTIFICATES / "visible_rank2_l2_selector_obstruction_certificate.json"

TARGET = (1, -2, 0)
SWAPPED = (-2, 1, 0)
CONJ_TARGET = (-1, 2, 0)
CONJ_SWAPPED = (2, -1, 0)
BRANCHES = [SWAPPED, CONJ_TARGET, TARGET, CONJ_SWAPPED]


def load_json(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8")) if path.exists() else {}


def write_json(path: Path, data: dict[str, Any]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(data, indent=2, sort_keys=True) + "\n", encoding="utf-8")


def swap(branch: tuple[int, int, int]) -> tuple[int, int, int]:
    x, y, z = branch
    return (y, x, z)


def dual(branch: tuple[int, int, int]) -> tuple[int, int, int]:
    x, y, z = branch
    return (-x, -y, -z)


def l2(branch: tuple[int, int, int]) -> tuple[int, int, int]:
    return (2 * branch[0], 2 * branch[1], 2 * branch[2])


def mod3(values: tuple[int, int, int]) -> tuple[int, int, int]:
    return tuple(value % 3 for value in values)


def base_h1_for_l2(branch: tuple[int, int, int]) -> int:
    d1, d2, _d3 = l2(branch)
    if d1 == 0 or d2 == 0:
        return 0
    if d1 > 0 > d2:
        return d1 * (-d2)
    if d1 < 0 < d2:
        return (-d1) * d2
    return 0


def signature(branch: tuple[int, int, int]) -> dict[str, Any]:
    x, y, z = branch
    return {
        "L": list(branch),
        "swap": list(swap(branch)),
        "dual": list(dual(branch)),
        "L2": list(l2(branch)),
        "L_mod3": list(mod3(branch)),
        "L2_mod3": list(mod3(l2(branch))),
        "xy": x * y,
        "z": z,
        "c2_extension_alpha1": -2 * x * y,
        "base_pullback_h1": base_h1_for_l2(branch),
    }


def same_on_target_and_swapped(key: str) -> bool:
    return signature(TARGET)[key] == signature(SWAPPED)[key]


def cert_statuses() -> dict[str, Any]:
    return {
        "source_ambiguity": load_json(SOURCE_AMBIGUITY).get("status"),
        "branch_reduction": load_json(BRANCH_REDUCTION).get("status"),
        "orientation_gate": load_json(ORIENTATION_GATE).get("status"),
        "gauduchon_gate": load_json(GAUDUCHON_GATE).get("status"),
        "integral_gap": load_json(INTEGRAL_GAP).get("status"),
        "appell_humbert": load_json(APPELL_HUMBERT).get("status"),
        "time_oriented_conjugate": load_json(TIME_ORIENTED).get("status"),
        "gerbe_fourier_type": load_json(FOURIER_TYPE).get("status"),
        "standard_deck": load_json(DECK).get("status"),
    }


def current_breaking_sources() -> dict[str, Any]:
    gauduchon = load_json(GAUDUCHON_GATE)
    integral = load_json(INTEGRAL_GAP)
    appell = load_json(APPELL_HUMBERT)
    time_oriented = load_json(TIME_ORIENTED)
    deck = load_json(DECK)
    return {
        "selected_target_wall_r1_over_r2_sqrt2": gauduchon.get("selection_analysis", {}).get(
            "source_certified_target_wall_present", False
        ),
        "selected_ordered_integral_source_for_L2": False
        if integral.get("still_open", {}).get(
            "selected_ordered_integral_Cech_or_automorphy_source_for_L2_2_minus4_0"
        )
        else None,
        "mathematical_appell_humbert_exists": appell.get("what_this_closes", {}).get(
            "explicit_nonflat_factor_of_automorphy_for_L2_2_minus4_0"
        ),
        "appell_humbert_selected_by_mtt": appell.get("selection_analysis", {}).get(
            "selected_by_mtt"
        ),
        "target_branch_selected_by_mtt": appell.get("selection_analysis", {}).get(
            "target_branch_L_selected_by_mtt"
        ),
        "neutral_pic0_selected_by_mtt": appell.get("selection_analysis", {}).get(
            "neutral_pic0_character_selected_by_mtt"
        ),
        "standard_gamma0_selected_by_mtt": not deck.get("still_open", {}).get(
            "MTT_selection_or_source_confirmation_of_Gamma0", True
        ),
        "time_oriented_q79_selected": time_oriented.get("calculation_results", {}).get(
            "time_oriented_retarded_branch_selects_q79", False
        )
        or time_oriented.get("what_this_proves", {}).get(
            "q79_is_selected_time_oriented_representative", False
        ),
        "time_orientation_maps_to_visible_base_order": False,
        "selected_D_E_dotD_Hessian_orders_base_factors": False,
    }


def prove_obstruction() -> dict[str, Any]:
    signatures = {str(branch): signature(branch) for branch in BRANCHES}
    target = signature(TARGET)
    swapped = signature(SWAPPED)

    equality_table = {
        "L_mod3_equal": same_on_target_and_swapped("L_mod3"),
        "L2_mod3_equal": same_on_target_and_swapped("L2_mod3"),
        "xy_equal": same_on_target_and_swapped("xy"),
        "z_equal": same_on_target_and_swapped("z"),
        "c2_equal": same_on_target_and_swapped("c2_extension_alpha1"),
        "h1_equal": same_on_target_and_swapped("base_pullback_h1"),
        "target_swapped_by_base_swap": swap(TARGET) == SWAPPED,
        "branch_orbit_under_swap_and_dual": sorted(BRANCHES)
        == sorted({TARGET, swap(TARGET), dual(TARGET), dual(swap(TARGET))}),
    }

    pic0_invariance = {
        "flat_pic0_changes_c1": False,
        "flat_pic0_changes_c2": False,
        "flat_pic0_changes_h1_for_nonzero_elliptic_degrees": False,
        "flat_pic0_changes_appell_humbert_curvature_matrix": False,
        "curvature_and_bianchi_terms_can_select_neutral_character": False,
        "needs_holonomy_sensitive_source_or_gauge_fixing": True,
    }

    breaking = current_breaking_sources()
    no_breaking_source_available = (
        breaking["selected_target_wall_r1_over_r2_sqrt2"] is False
        and breaking["selected_ordered_integral_source_for_L2"] is False
        and breaking["appell_humbert_selected_by_mtt"] is False
        and breaking["target_branch_selected_by_mtt"] is False
        and breaking["neutral_pic0_selected_by_mtt"] is False
        and breaking["standard_gamma0_selected_by_mtt"] is False
        and breaking["time_orientation_maps_to_visible_base_order"] is False
        and breaking["selected_D_E_dotD_Hessian_orders_base_factors"] is False
    )

    obstruction_theorem = {
        "theorem": "No current closed selector can uniquely select L=(1,-2,0)",
        "proof": [
            "The target and swapped branch are related by the base-swap automorphism E1<->E2.",
            "Every currently closed invariant used for the visible L2 route has the same value on target and swapped.",
            "A selector built only from base-swap-invariant closed data must therefore assign equal selection score to both.",
            "Unique selection of target would contradict that equality unless a source breaks the base-swap symmetry.",
            "Flat Pic0 twists leave c1, c2, h1, and the curvature matrix unchanged, so neutral Pic0 cannot be selected by curvature/topology alone.",
        ],
        "valid_for_selector_inputs": [
            "c2=4 alpha1 topology",
            "h1=8 reduced pullback cohomology",
            "finite q79/F,m=1 qutrit/torsion data",
            "Appell-Humbert matrix before MTT source selection",
            "curvature/Bianchi terms insensitive to flat Pic0 holonomy",
        ],
        "does_not_apply_if_new_source_supplies": [
            "selected target Gauduchon wall r1:r2=sqrt(2):1",
            "selected ordered integral Cech/automorphy/D_E source",
            "same-source D_E/dotD/Hessian term ordering the base factors",
            "holonomy-sensitive term selecting or quotienting Pic0 characters",
        ],
    }

    target_proved = False
    status = (
        "VISIBLE_RANK2_L2_SELECTOR_OBSTRUCTION_PROVED_SOURCE_REQUIRED"
        if all(equality_table.values()) and no_breaking_source_available
        else "VISIBLE_RANK2_L2_SELECTOR_OBSTRUCTION_INCONCLUSIVE"
    )

    return {
        "calculation": "VisibleRank2L2SelectorObstruction",
        "status": status,
        "generated_by": "scripts/prove_visible_rank2_l2_selector_obstruction.py",
        "input_statuses": cert_statuses(),
        "branch_signatures": signatures,
        "target_signature": target,
        "swapped_signature": swapped,
        "equality_table": equality_table,
        "pic0_invariance": pic0_invariance,
        "current_breaking_sources": breaking,
        "no_breaking_source_available": no_breaking_source_available,
        "obstruction_theorem": obstruction_theorem,
        "attempt_to_prove_target_selector": {
            "proved_unique_target_selection": target_proved,
            "reason_not_proved": (
                "The existing data prove the target Appell-Humbert representative "
                "exists, but do not select the base ordering, target wall, neutral "
                "Pic0 character, or same-source operator/Hessian package. Under "
                "the current closed invariants, target and swapped are degenerate."
            ),
        },
        "what_this_closes": {
            "no_hidden_selector_in_current_topology_h1_qutrit_or_appell_humbert_data": True,
            "pic0_neutrality_not_selected_by_current_curvature_topology_data": True,
            "proof_target_reduced_to_new_symmetry_breaking_source": True,
        },
        "still_open": {
            "selected_target_wall_r1_over_r2_sqrt2": True,
            "selected_ordered_integral_Cech_automorphy_D_E_source": True,
            "selected_or_quotiented_Pic0_character": True,
            "same_source_D_E_dotD_Hessian_base_ordering": True,
            "nonzero_Ext_class_selection": True,
            "non_split_stability": True,
            "full_SM_closure": True,
        },
        "guardrails": {
            "claims_target_selector_proved": False,
            "claims_neutral_pic0_selected": False,
            "claims_appell_humbert_selected_by_mtt": False,
            "claims_standard_gamma0_selected": False,
            "claims_D_E_dotD_Hessian_constructed": False,
            "claims_full_SM_closure": False,
            "uses_observed_flavor_data": False,
            "uses_benchmark_flavor_entries": False,
        },
        "verdict": {
            "honest_answer": (
                "The target selector is not provable from the current closed packets. "
                "What is proved is stronger discipline: no hidden combination of "
                "the existing topology, h1, finite qutrit, or Appell-Humbert data "
                "can uniquely choose L=(1,-2,0) or the neutral Pic0 twist. A new "
                "source must break base-swap/Pic0 degeneracy."
            ),
            "next_action": (
                "Construct the missing symmetry-breaking source: either selected "
                "r1:r2=sqrt(2):1 wall data, selected ordered Cech/D_E data, or a "
                "same-source Hessian/dotD package whose primitive response orders "
                "the two base factors."
            ),
        },
    }


def main() -> int:
    report = prove_obstruction()
    write_json(CANDIDATE, report)
    certificate = {
        "certificate": "VisibleRank2L2SelectorObstruction",
        "status": report["status"],
        "analysis_script": report["generated_by"],
        "candidate_data": "candidate_data/visible_rank2_l2_selector_obstruction.candidate.json",
        "input_statuses": report["input_statuses"],
        "equality_table": report["equality_table"],
        "pic0_invariance": report["pic0_invariance"],
        "current_breaking_sources": report["current_breaking_sources"],
        "no_breaking_source_available": report["no_breaking_source_available"],
        "obstruction_theorem": report["obstruction_theorem"],
        "attempt_to_prove_target_selector": report["attempt_to_prove_target_selector"],
        "what_this_closes": report["what_this_closes"],
        "still_open": report["still_open"],
        "guardrails": report["guardrails"],
        "verdict": report["verdict"],
    }
    write_json(CERTIFICATE, certificate)
    print(json.dumps(report, indent=2, sort_keys=True))
    return 0 if report["status"].endswith("SOURCE_REQUIRED") else 1


if __name__ == "__main__":
    raise SystemExit(main())
