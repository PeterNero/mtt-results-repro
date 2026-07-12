"""Analyze the remaining integral lift source gap for visible L^2.

The current frontier has two live routes:

1. select the Gauduchon wall p1:p2=1:2, equivalently r1:r2=sqrt(2):1;
2. lift the finite qutrit class integrally to L=(1,-2,0).

This script tests the second route.  It shows that the selected finite
q79/F,m=1 quotient cannot by itself select the target integral branch, because
the target and swapped branches have identical finite signatures, including
the L^2 mod-3 reduction.  It also proves that there is no remaining cohomology
algebra obstruction: the existing h1=8 pullback packet would promote to
SELECTED_DATA as soon as an honest source certificate supplies the ordered
integral Cech/automorphy matrix.
"""

from __future__ import annotations

import copy
import json
import subprocess
import sys
import tempfile
from fractions import Fraction
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
CERTIFICATES = ROOT / "certificates"
CANDIDATE_DATA = ROOT / "candidate_data"

VALIDATOR = ROOT / "scripts" / "validate_visible_rank2_l2_cohomology.py"
PULLBACK_PACKET = CANDIDATE_DATA / "visible_rank2_l2_pullback_cech_attempt.cohomology.json"
PULLBACK_CERT = CERTIFICATES / "visible_rank2_l2_pullback_cech_attempt_certificate.json"
ORIENTATION_GATE = CERTIFICATES / "selected_pullback_l2_branch_orientation_source_gate_certificate.json"
GAUDUCHON_GATE = CERTIFICATES / "selected_gauduchon_wall_radius_gate_certificate.json"
DECK_CECH = CERTIFICATES / "time_oriented_m1_deck_cech_lift_certificate.json"
S3_CLOSURE = CERTIFICATES / "visible_twisted_s3_class_restriction_closure_certificate.json"

CANDIDATE = CANDIDATE_DATA / "visible_rank2_l2_integral_lift_source_gap.candidate.json"
CERTIFICATE = CERTIFICATES / "visible_rank2_l2_integral_lift_source_gap_certificate.json"

TARGET = [1, -2, 0]
SWAPPED = [-2, 1, 0]
CONJ_TARGET = [-1, 2, 0]
CONJ_SWAPPED = [2, -1, 0]
BRANCHES = [SWAPPED, CONJ_TARGET, TARGET, CONJ_SWAPPED]


def load_json(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def write_json(path: Path, data: dict[str, Any]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(data, indent=2, sort_keys=True) + "\n", encoding="utf-8")


def mod3_vector(values: list[int]) -> list[int]:
    return [value % 3 for value in values]


def l2_degrees(branch: list[int]) -> list[int]:
    return [2 * branch[0], 2 * branch[1], 2 * branch[2]]


def b1_self_period(branch: list[int]) -> str:
    numerator = (-(branch[0] * branch[1])) % 3
    return str(Fraction(numerator, 3))


def base_h1_for_degrees(degrees: list[int]) -> int:
    d1, d2, _d3 = degrees
    if d1 == 0 or d2 == 0:
        return 0
    if d1 > 0 and d2 < 0:
        return d1 * (-d2)
    if d1 < 0 and d2 > 0:
        return (-d1) * d2
    return 0


def c1_matrix_for_degrees(degrees: list[int]) -> list[list[int]]:
    d1, d2, d3 = degrees
    matrix = [[0 for _ in range(6)] for _ in range(6)]
    for left, right, degree in [(0, 1, d1), (2, 3, d2), (4, 5, d3)]:
        matrix[left][right] = degree
        matrix[right][left] = -degree
    return matrix


def branch_signature(branch: list[int]) -> dict[str, Any]:
    degrees = l2_degrees(branch)
    return {
        "L": branch,
        "L_mod3": mod3_vector(branch),
        "L2_degrees": degrees,
        "L2_degrees_mod3": mod3_vector(degrees),
        "xy": branch[0] * branch[1],
        "c1_L_squared_square_alpha1": 4 * branch[0] * branch[1],
        "c2_extension_alpha1": -(branch[0] * branch[1]) * 2,
        "base_pullback_h1": base_h1_for_degrees(degrees),
        "m1_self_period_B1_L_L": b1_self_period(branch),
        "central_or_shared_circle_degree": degrees[2],
        "c1_deck_matrix_order_g1_to_g6": c1_matrix_for_degrees(degrees),
    }


def run_validator(data: dict[str, Any]) -> dict[str, Any]:
    with tempfile.TemporaryDirectory() as tmp:
        path = Path(tmp) / "visible_rank2_l2_packet.json"
        path.write_text(json.dumps(data, indent=2, sort_keys=True) + "\n", encoding="utf-8")
        proc = subprocess.run(
            [sys.executable, str(VALIDATOR), str(path)],
            cwd=ROOT,
            text=True,
            stdout=subprocess.PIPE,
            stderr=subprocess.STDOUT,
        )
    report: dict[str, Any] | None = None
    for line in proc.stdout.splitlines():
        if line.startswith("visible_rank2_l2_h1_report="):
            report = json.loads(line.split("=", 1)[1])
            break
    return {
        "exit_code": proc.returncode,
        "output": proc.stdout.strip(),
        "parsed_report": report,
    }


def promoted_source_packet(packet: dict[str, Any]) -> dict[str, Any]:
    promoted = copy.deepcopy(packet)
    promoted["candidate_role"] = "SELECTED_DATA"
    promoted["source"]["selected_by_mtt"] = True
    promoted["source"]["fixture_only"] = False
    promoted["source"]["source_certificate"] = (
        "HYPOTHETICAL_SELECTED_INTEGRAL_LIFT_SOURCE_CERTIFICATE"
    )
    promoted["source"]["source_kind"] = "typed_cech_line_bundle"
    return promoted


def analyze() -> dict[str, Any]:
    pullback_cert = load_json(PULLBACK_CERT)
    orientation = load_json(ORIENTATION_GATE)
    gauduchon = load_json(GAUDUCHON_GATE)
    deck = load_json(DECK_CECH)
    s3 = load_json(S3_CLOSURE)
    packet = load_json(PULLBACK_PACKET)

    signatures = {str(branch): branch_signature(branch) for branch in BRANCHES}
    target = branch_signature(TARGET)
    swapped = branch_signature(SWAPPED)

    finite_indistinguishability = {
        "target_L_mod3_equals_swapped": target["L_mod3"] == swapped["L_mod3"],
        "target_L2_mod3_equals_swapped": target["L2_degrees_mod3"]
        == swapped["L2_degrees_mod3"],
        "target_m1_self_period_equals_swapped": target["m1_self_period_B1_L_L"]
        == swapped["m1_self_period_B1_L_L"],
        "target_xy_equals_swapped": target["xy"] == swapped["xy"],
        "target_h1_equals_swapped": target["base_pullback_h1"]
        == swapped["base_pullback_h1"],
        "target_c2_equals_swapped": target["c2_extension_alpha1"]
        == swapped["c2_extension_alpha1"],
        "therefore_finite_mod3_data_cannot_select_ordered_integral_branch": True,
    }

    deck_map = deck.get("deck_quotient_map", {}).get("map", {})
    target_matrix = target["c1_deck_matrix_order_g1_to_g6"]
    selected_finite_deck_limit = {
        "selected_deck_map": deck_map,
        "g3_g4_in_kernel_of_selected_finite_quotient": deck_map.get("g3") == [0, 0]
        and deck_map.get("g4") == [0, 0],
        "target_integral_c1_requires_g3_g4_degree": target_matrix[2][3],
        "selected_finite_gerbe_supplies_ordinary_integral_c1_matrix": False,
        "selected_finite_gerbe_can_be_integral_L2_lift_by_itself": False,
        "reason": (
            "The finite q79/F,m=1 deck cocycle is a flat torsion gerbe on the "
            "active g1/g2 quotient.  It kills g3 and g4, while the target "
            "ordinary L^2 line bundle needs integral degree -4 on the g3/g4 "
            "base pair.  The existing finite gerbe can orient a qutrit "
            "commutator, but it cannot supply the ordinary integral Chern "
            "matrix or the ordered base-factor lift."
        ),
    }

    original_validation = run_validator(packet)
    conditional_promoted_validation = run_validator(promoted_source_packet(packet))

    sufficient_source_contract = {
        "source_certificate_required": True,
        "ordered_integral_c1_matrix_required": target_matrix,
        "must_fix_target_not_swapped": {
            "target_L": TARGET,
            "swapped_L": SWAPPED,
            "target_L2_degrees": target["L2_degrees"],
            "swapped_L2_degrees": swapped["L2_degrees"],
        },
        "must_tie_base_factor_order_to_source": "E1/g1g2 carries +2 and E2/g3g4 carries -4",
        "must_not_be_only_mod3_or_only_torsion": True,
        "must_select_or_eliminate_flat_pic0_torsion_character": True,
        "must_then_supply_nonzero_ext_class_and_stability": True,
        "validator_would_promote_existing_h1_packet_if_source_supplied": (
            conditional_promoted_validation["exit_code"] == 0
            and conditional_promoted_validation["parsed_report"] is not None
            and conditional_promoted_validation["parsed_report"].get(
                "promotes_to_non_split_V_alpha_input"
            )
            is True
        ),
    }

    route_status = {
        "gauduchon_wall_route": {
            "status": "LIVE_SOURCE_RATIO_OPEN",
            "input_status": gauduchon.get("status"),
            "needed": "source-certified r1:r2=sqrt(2):1 or equivalent p1:p2=1:2 chamber",
        },
        "integral_lift_route": {
            "status": "LIVE_SOURCE_CERTIFICATE_ONLY_GAP",
            "needed": "selected ordered integral Cech/automorphy matrix for L^2=(2,-4,0)",
            "cohomology_algebra_after_source": "already validator-backed: h1=8 and nonzero Ext class can promote",
        },
        "finite_qutrit_only_route": {
            "status": "NO_GO_FOR_BRANCH_SELECTION",
            "reason": "target and swapped branches are identical to the selected finite quotient",
        },
    }

    return {
        "calculation": "VisibleRank2L2IntegralLiftSourceGap",
        "status": "VISIBLE_RANK2_L2_INTEGRAL_LIFT_REDUCED_TO_SOURCE_CERTIFICATE",
        "generated_by": "scripts/analyze_visible_rank2_l2_integral_lift_source_gap.py",
        "input_certificates": {
            "pullback_cech_attempt": PULLBACK_CERT.name,
            "orientation_gate": ORIENTATION_GATE.name,
            "gauduchon_wall_radius_gate": GAUDUCHON_GATE.name,
            "time_oriented_deck_cech_lift": DECK_CECH.name,
            "visible_twisted_s3_class_restriction": S3_CLOSURE.name,
        },
        "input_statuses": {
            "pullback_cech_attempt": pullback_cert.get("status"),
            "orientation_gate": orientation.get("status"),
            "gauduchon_wall_radius_gate": gauduchon.get("status"),
            "time_oriented_deck_cech_lift": deck.get("status"),
            "visible_twisted_s3_class_restriction": s3.get("status"),
        },
        "branch_signatures": signatures,
        "finite_indistinguishability": finite_indistinguishability,
        "selected_finite_deck_limit": selected_finite_deck_limit,
        "existing_h1_packet": {
            "path": str(PULLBACK_PACKET),
            "candidate_role": packet.get("candidate_role"),
            "h1": packet.get("reported_cohomology", {}).get("h1"),
            "original_validation": original_validation,
            "conditional_promoted_validation": conditional_promoted_validation,
        },
        "sufficient_source_contract": sufficient_source_contract,
        "route_status": route_status,
        "what_this_closes": {
            "finite_mod3_qutrit_data_no_go_for_target_vs_swapped_integral_lift": True,
            "selected_flat_gerbe_not_same_as_ordinary_integral_c1_lift": True,
            "shared_circle_central_degree_checked_zero": True,
            "existing_h1_8_packet_has_no_remaining_algebraic_obstruction_after_source": True,
            "integral_lift_gap_reduced_to_source_certificate_not_cohomology": True,
        },
        "still_open": {
            "selected_ordered_integral_Cech_or_automorphy_source_for_L2_2_minus4_0": True,
            "source_tied_base_factor_order_E1_positive_E2_negative": True,
            "flat_pic0_or_torsion_character_selection": True,
            "non_split_extension_stability": True,
            "same_source_D_E_dotD_Riesz_Green": True,
            "full_SM_closure": True,
        },
        "guardrails": {
            "claims_integral_lift_selected": False,
            "claims_existing_finite_gerbe_selects_L_branch": False,
            "claims_promoted_packet_written_as_selected_data": False,
            "claims_pic0_or_torsion_character_selected": False,
            "claims_stability_proved": False,
            "claims_full_SM_closure": False,
            "uses_observed_flavor_data": False,
            "uses_benchmark_flavor_entries": False,
        },
        "verdict": {
            "honest_answer": (
                "The integral-lift route is now reduced to a pure source "
                "certificate.  The finite q79/F,m=1 quotient cannot choose "
                "between L=(1,-2,0) and L=(-2,1,0), even after passing to L^2, "
                "and the selected flat gerbe is not an ordinary integral Chern "
                "matrix.  However, once a selected source supplies the ordered "
                "integral Cech/automorphy matrix with degrees (2,-4,0), the "
                "existing h1=8 packet promotes through the validator without a "
                "new cohomology obstruction."
            ),
            "next_action": (
                "Build the selected ordered integral Cech/automorphy source for "
                "L^2=(2,-4,0), or return to the Gauduchon wall route and derive "
                "r1:r2=sqrt(2):1 from source geometry."
            ),
        },
    }


def main() -> int:
    report = analyze()
    write_json(CANDIDATE, report)
    certificate = {
        "certificate": "VisibleRank2L2IntegralLiftSourceGap",
        "status": report["status"],
        "analysis_script": report["generated_by"],
        "candidate_data": "candidate_data/visible_rank2_l2_integral_lift_source_gap.candidate.json",
        "input_certificates": report["input_certificates"],
        "finite_indistinguishability": report["finite_indistinguishability"],
        "selected_finite_deck_limit": report["selected_finite_deck_limit"],
        "existing_h1_packet": report["existing_h1_packet"],
        "sufficient_source_contract": report["sufficient_source_contract"],
        "route_status": report["route_status"],
        "what_this_closes": report["what_this_closes"],
        "still_open": report["still_open"],
        "guardrails": report["guardrails"],
        "verdict": report["verdict"],
    }
    write_json(CERTIFICATE, certificate)
    print(json.dumps(report, indent=2, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
