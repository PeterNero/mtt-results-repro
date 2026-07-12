"""Build the pullback L^2 branch-orientation source gate.

The branch-selection reduction leaves a sharp ambiguity:

    L=(1,-2,0)  versus  L=(-2,1,0)

after the symmetric/shared-base chamber is imposed.  This script checks
whether the already selected finite qutrit orientation can distinguish those
two branches.  It cannot: both branches have the same active F_3^2 image and
the same m=1 self-period.  Therefore the next source must be stronger than the
finite m=1 qutrit table: either a selected Gauduchon wall/chamber such as
p1:p2=1:2, or an integral/geometric lift that orders the two base factors.
"""

from __future__ import annotations

import json
from fractions import Fraction
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
CERTIFICATES = ROOT / "certificates"
CANDIDATE_DATA = ROOT / "candidate_data"

BRANCH_REDUCTION = CERTIFICATES / "visible_rank2_l2_branch_selection_reduction_certificate.json"
DECK_CECH = CERTIFICATES / "time_oriented_m1_deck_cech_lift_certificate.json"
QUTRIT_LINES = CERTIFICATES / "time_oriented_m1_qutrit_line_cycle_restrictions_certificate.json"
RPLUS_SUPPORT = CERTIFICATES / "c1_iwasawa_rplus_support_certificate.json"
CHERN_GATE = CERTIFICATES / "visible_chern_weil_quantization_gate_certificate.json"

CANDIDATE = CANDIDATE_DATA / "selected_pullback_l2_branch_orientation_source_gate.candidate.json"
CERTIFICATE = CERTIFICATES / "selected_pullback_l2_branch_orientation_source_gate_certificate.json"

TARGET = [1, -2, 0]
SWAPPED = [-2, 1, 0]
OTHER_PAIR = [[-1, 2, 0], [2, -1, 0]]
BRANCHES = [SWAPPED, OTHER_PAIR[0], TARGET, OTHER_PAIR[1]]


def load_json(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def write_json(path: Path, data: dict[str, Any]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(data, indent=2, sort_keys=True) + "\n", encoding="utf-8")


def mod3(value: int) -> int:
    return value % 3


def active_f3_image(branch: list[int]) -> list[int]:
    return [mod3(branch[0]), mod3(branch[1])]


def b1_self_period(branch: list[int]) -> str:
    """Return B_1(v,v)= -x*y/3 mod Z for v=(x,y)."""
    x, y = branch[:2]
    numerator = (-x * y) % 3
    return str(Fraction(numerator, 3))


def slope(branch: list[int], p1: int, p2: int) -> int:
    return branch[0] * p1 + branch[1] * p2


def chamber_signature(p1: int, p2: int) -> dict[str, Any]:
    slopes = [{"branch": branch, "slope": slope(branch, p1, p2)} for branch in BRANCHES]
    negative = [entry["branch"] for entry in slopes if entry["slope"] < 0]
    zero = [entry["branch"] for entry in slopes if entry["slope"] == 0]
    positive = [entry["branch"] for entry in slopes if entry["slope"] > 0]
    return {
        "p": [p1, p2, 1],
        "ratio_p1_over_p2": str(Fraction(p1, p2)),
        "slopes": slopes,
        "negative_branches": negative,
        "zero_branches": zero,
        "positive_branches": positive,
        "target_unique_negative": negative == [TARGET],
        "swapped_unique_negative": negative == [SWAPPED],
    }


def branch_signature(branch: list[int]) -> dict[str, Any]:
    return {
        "branch": branch,
        "c2_xy": branch[0] * branch[1],
        "active_F3_2_image": active_f3_image(branch),
        "m1_self_period_B1_v_v": b1_self_period(branch),
    }


def analyze() -> dict[str, Any]:
    reduction = load_json(BRANCH_REDUCTION)
    deck = load_json(DECK_CECH)
    qutrit = load_json(QUTRIT_LINES)
    rplus = load_json(RPLUS_SUPPORT)
    chern = load_json(CHERN_GATE)

    signatures = [branch_signature(branch) for branch in BRANCHES]
    target_signature = branch_signature(TARGET)
    swapped_signature = branch_signature(SWAPPED)
    same_qutrit_signature = (
        target_signature["active_F3_2_image"] == swapped_signature["active_F3_2_image"]
        and target_signature["m1_self_period_B1_v_v"]
        == swapped_signature["m1_self_period_B1_v_v"]
    )

    chambers = {
        "symmetric_shared_base": chamber_signature(1, 1),
        "target_wall": chamber_signature(1, 2),
        "swapped_wall": chamber_signature(2, 1),
        "target_strict_side": chamber_signature(1, 3),
        "swapped_strict_side": chamber_signature(3, 1),
    }

    equal_radius_sources = {
        "rplus_equal_radius_assumption": rplus.get("rplus_support", {})
        .get("equal_radius_specialization", {})
        .get("assumption"),
        "chern_gate_equal_radius_assumption": chern.get("existing_flux_row_consistency", {})
        .get("equal_radius_specialization", {})
        .get("assumption"),
        "supports_symmetric_not_wall_chamber": True,
        "selects_target_branch": False,
    }

    finite_qutrit_gate = {
        "deck_cech_status": deck.get("status"),
        "qutrit_line_status": qutrit.get("status"),
        "deck_map": "pi(g1)=(1,0), pi(g2)=(0,1), inactive g3..g6=0",
        "m1_period": "B_1((a,b),(c,d))=-c*b/3 mod Z",
        "target_signature": target_signature,
        "swapped_signature": swapped_signature,
        "target_and_swapped_same_finite_signature": same_qutrit_signature,
        "distinguishes_target_from_swapped": False,
        "reason": (
            "Modulo 3, (1,-2) and (-2,1) both map to (1,1), and both have "
            "B_1(v,v)=2/3. The selected q79/F,m=1 finite qutrit cocycle "
            "therefore orients the active clock-shift pair but does not order "
            "the two integral base coefficients."
        ),
    }

    source_routes = [
        {
            "id": "selected_gauduchon_wall_p1_p2_1_2",
            "status": "LIVE_NOT_SOURCE_CERTIFIED",
            "would_select_target": chambers["target_wall"]["target_unique_negative"],
            "what_must_be_proved": (
                "MTT selects the wall/chamber p1:p2=1:2 for V_alpha and treats "
                "zero-slope alternative branches as non-stable source candidates."
            ),
        },
        {
            "id": "integral_deck_or_cech_lift_ordering_base_factors",
            "status": "LIVE_NOT_SOURCE_CERTIFIED",
            "would_select_target": True,
            "what_must_be_proved": (
                "A smooth/integral Cech, Deligne, automorphy, or D_E/dotD "
                "packet lifts the finite (1,1) qutrit image to the integer "
                "branch (1,-2), not (-2,1)."
            ),
        },
        {
            "id": "flat_pic0_or_torsion_character_selector",
            "status": "OPEN_NOT_CURRENTLY_AVAILABLE",
            "would_select_target": None,
            "what_must_be_proved": (
                "The selected flat/torsion character is either trivial or tied "
                "to the same ordered branch; c1 and h1 cannot see it."
            ),
        },
    ]

    status = "PULLBACK_L2_BRANCH_ORIENTATION_GATE_REDUCED_TO_WALL_OR_INTEGRAL_LIFT"

    return {
        "calculation": "SelectedPullbackL2BranchOrientationSourceGate",
        "status": status,
        "generated_by": "scripts/build_selected_pullback_l2_branch_orientation_source_gate.py",
        "input_certificates": {
            "branch_selection_reduction": BRANCH_REDUCTION.name,
            "time_oriented_m1_deck_cech_lift": DECK_CECH.name,
            "time_oriented_m1_qutrit_line_cycle_restrictions": QUTRIT_LINES.name,
            "c1_iwasawa_rplus_support": RPLUS_SUPPORT.name,
            "visible_chern_weil_quantization_gate": CHERN_GATE.name,
        },
        "input_statuses": {
            "branch_selection_reduction": reduction.get("status"),
            "deck_cech": deck.get("status"),
            "qutrit_lines": qutrit.get("status"),
            "rplus_support": rplus.get("status"),
            "chern_gate": chern.get("status"),
        },
        "branch_signatures": signatures,
        "finite_qutrit_gate": finite_qutrit_gate,
        "gauduchon_chamber_gate": {
            "chambers": chambers,
            "equal_radius_sources": equal_radius_sources,
            "current_selected_wall_source_present": False,
            "target_wall_would_select_L_1_minus2_0": chambers["target_wall"][
                "target_unique_negative"
            ],
            "swapped_wall_would_select_L_minus2_1_0": chambers["swapped_wall"][
                "swapped_unique_negative"
            ],
            "symmetric_shared_base_selects_unique_branch": False,
        },
        "source_routes": source_routes,
        "what_this_closes": {
            "finite_qutrit_orientation_cannot_select_between_target_and_swapped": True,
            "equal_radius_or_symmetric_shared_base_chamber_not_enough": True,
            "p1_p2_1_2_wall_identified_as_minimal_target_selector": True,
            "p1_p2_2_1_wall_identified_as_conjugate_selector": True,
            "selected_orientation_source_must_be_stronger_than_F3_quotient": True,
        },
        "still_open": {
            "source_certified_p1_p2_1_2_wall_or_near_wall_chamber": True,
            "integral_lift_from_finite_qutrit_image_to_integer_branch": True,
            "raw_transition_or_automorphy_factors_for_L_1_minus2_0": True,
            "flat_pic0_or_torsion_character_selection": True,
            "non_split_extension_stability_after_branch_selection": True,
            "same_source_D_E_dotD_Riesz_Green": True,
            "full_SM_closure": True,
        },
        "guardrails": {
            "claims_L_branch_selected": False,
            "claims_q79_F_finite_data_selects_L_branch": False,
            "claims_p1_p2_1_2_wall_selected": False,
            "claims_flat_character_eliminated": False,
            "claims_full_SM_closure": False,
            "uses_observed_flavor_data": False,
            "uses_benchmark_flavor_entries": False,
        },
        "next_required_packet": {
            "name": "Selected_Pullback_L2_Branch_Orientation_Source.v1",
            "minimal_success_criteria": [
                "source-certified p1:p2=1:2 Gauduchon wall/chamber, or an integral lift selecting (1,-2,0)",
                "ordered base-factor convention tied to the selected source, not a notation choice",
                "flat Pic0/torsion character selected or proved trivial for the source",
                "raw transition/automorphy data for L=(1,-2,0)",
                "non-split extension stability and same-source D_E/dotD/Riesz/Green promotion",
            ],
        },
        "verdict": {
            "honest_answer": (
                "The selected q79/F,m=1 finite qutrit orientation is necessary "
                "but not sufficient for the visible L branch. It cannot distinguish "
                "L=(1,-2,0) from the swapped branch L=(-2,1,0). The first explicit "
                "target-selecting chamber is the p1:p2=1:2 wall, but current source "
                "certificates only support symmetric/equal-radius data and do not "
                "select that wall. The missing object is therefore a selected "
                "Gauduchon-wall source or an integral Cech/D_E lift."
            ),
            "next_action": (
                "Search for or construct a source-certified p1:p2=1:2 Gauduchon "
                "wall/near-wall theorem, or compute an integral deck/Cech lift "
                "that refines the finite (1,1) qutrit image to L=(1,-2,0)."
            ),
        },
    }


def main() -> int:
    report = analyze()
    write_json(CANDIDATE, report)
    certificate = {
        "certificate": "SelectedPullbackL2BranchOrientationSourceGate",
        "status": report["status"],
        "analysis_script": report["generated_by"],
        "candidate_data": "candidate_data/selected_pullback_l2_branch_orientation_source_gate.candidate.json",
        "input_certificates": report["input_certificates"],
        "finite_qutrit_gate": report["finite_qutrit_gate"],
        "gauduchon_chamber_gate": report["gauduchon_chamber_gate"],
        "source_routes": report["source_routes"],
        "what_this_closes": report["what_this_closes"],
        "still_open": report["still_open"],
        "guardrails": report["guardrails"],
        "next_required_packet": report["next_required_packet"],
        "verdict": report["verdict"],
    }
    write_json(CERTIFICATE, certificate)
    print(json.dumps(report, indent=2, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
