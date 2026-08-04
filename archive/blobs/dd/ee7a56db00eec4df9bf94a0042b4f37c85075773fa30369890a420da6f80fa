"""Build the ordered integral source promotion gate for visible L^2."""

from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
CERTIFICATES = ROOT / "certificates"
CANDIDATE_DATA = ROOT / "candidate_data"

VALIDATOR = ROOT / "scripts" / "validate_visible_rank2_l2_ordered_source_packet.py"

APPELL_HUMBERT = CERTIFICATES / "visible_rank2_l2_appell_humbert_automorphy_certificate.json"
INTEGRAL_GAP = CERTIFICATES / "visible_rank2_l2_integral_lift_source_gap_certificate.json"
SELECTOR_OBSTRUCTION = CERTIFICATES / "visible_rank2_l2_selector_obstruction_certificate.json"
RADIUS_NOGO = CERTIFICATES / "visible_rank2_l2_selected_radius_import_nogo_certificate.json"
ORIENTATION_GATE = CERTIFICATES / "selected_pullback_l2_branch_orientation_source_gate_certificate.json"

TEMPLATE = CERTIFICATES / "visible_rank2_l2_ordered_source.template.json"
CURRENT_ATTEMPT = CANDIDATE_DATA / "visible_rank2_l2_ordered_source.current_attempt.json"
CANDIDATE = CANDIDATE_DATA / "visible_rank2_l2_ordered_source_promotion_gate.candidate.json"
CERTIFICATE = CERTIFICATES / "visible_rank2_l2_ordered_source_promotion_gate_certificate.json"

TARGET_L = [1, -2, 0]
TARGET_L2 = [2, -4, 0]


def load_json(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8")) if path.exists() else {}


def write_json(path: Path, data: dict[str, Any]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(data, indent=2, sort_keys=True) + "\n", encoding="utf-8")


def target_matrix() -> list[list[int]]:
    matrix = [[0 for _ in range(6)] for _ in range(6)]
    for degree, left, right in [(2, 0, 1), (-4, 2, 3), (0, 4, 5)]:
        matrix[left][right] = degree
        matrix[right][left] = -degree
    return matrix


def run_validator(path: Path) -> dict[str, Any]:
    proc = subprocess.run(
        [sys.executable, str(VALIDATOR), str(path)],
        cwd=ROOT,
        text=True,
        stdout=subprocess.PIPE,
        stderr=subprocess.STDOUT,
    )
    parsed: dict[str, Any] | None = None
    for line in proc.stdout.splitlines():
        if line.startswith("visible_rank2_l2_ordered_source_validation_report="):
            parsed = json.loads(line.split("=", 1)[1])
            break
    return {
        "packet": str(path),
        "exit_code": proc.returncode,
        "output": proc.stdout.strip(),
        "parsed_report": parsed,
    }


def template_packet() -> dict[str, Any]:
    return {
        "schema": "VisibleRank2L2OrderedSourcePacket.v1",
        "status": "OPEN",
        "candidate_role": "SELECTED_DATA",
        "target": {
            "L": TARGET_L,
            "L2": TARGET_L2,
            "base_ordering": "E1_positive_E2_negative",
            "c1_deck_matrix_order_g1_to_g6": target_matrix(),
        },
        "source": {
            "source_kind": None,
            "source_certificate": None,
            "source_status": None,
            "selected_by_mtt": None,
            "fixture_only": None,
            "uses_observed_flavor_inputs": False,
            "uses_benchmark_flavor_inputs": False,
        },
        "automorphy": {
            "cocycle_checked": None,
            "ordinary_integral_c1_realized": None,
            "finite_torsion_gerbe_used_as_ordinary_c1": False,
        },
        "selection_evidence": {
            "standard_lattice_or_equivalent_selected": None,
            "base_factor_order_selected": None,
            "base_swap_broken_by_source": None,
            "not_only_finite_mod3_qutrit": None,
            "not_equal_radius_import": None,
        },
        "pic0_resolution": {
            "resolution": None,
            "flat_character_values_g1_to_g6": None,
            "source_selected_or_quotiented": None,
        },
    }


def current_appell_humbert_attempt(appell: dict[str, Any]) -> dict[str, Any]:
    checks = appell.get("construction_checks", {})
    selection = appell.get("selection_analysis", {})
    return {
        "schema": "VisibleRank2L2OrderedSourcePacket.v1",
        "status": "OPEN_CURRENT_APPELL_HUMBERT_EXISTS_SELECTION_OPEN",
        "candidate_role": "UNSELECTED_FIXTURE",
        "target": {
            "L": TARGET_L,
            "L2": TARGET_L2,
            "base_ordering": "E1_positive_E2_negative",
            "c1_deck_matrix_order_g1_to_g6": target_matrix(),
        },
        "source": {
            "source_kind": "appell_humbert_formula",
            "source_certificate": "visible_rank2_l2_appell_humbert_automorphy_certificate.json",
            "source_status": appell.get("status"),
            "selected_by_mtt": selection.get("selected_by_mtt"),
            "fixture_only": True,
            "uses_observed_flavor_inputs": False,
            "uses_benchmark_flavor_inputs": False,
        },
        "automorphy": {
            "cocycle_checked": checks.get("cocycle_law_holds_on_small_lattice_box_mod_2pi_i"),
            "ordinary_integral_c1_realized": checks.get("c1_matrix_matches_required_order"),
            "finite_torsion_gerbe_used_as_ordinary_c1": False,
        },
        "selection_evidence": {
            "standard_lattice_or_equivalent_selected": selection.get(
                "standard_gaussian_lattice_selected_by_mtt"
            ),
            "base_factor_order_selected": selection.get("target_branch_L_selected_by_mtt"),
            "base_swap_broken_by_source": selection.get("target_branch_L_selected_by_mtt"),
            "not_only_finite_mod3_qutrit": True,
            "not_equal_radius_import": True,
        },
        "pic0_resolution": {
            "resolution": "neutral_allowed_not_selected",
            "flat_character_values_g1_to_g6": [[1, 0]] * 6,
            "source_selected_or_quotiented": selection.get("neutral_pic0_character_selected_by_mtt"),
        },
    }


def analyze() -> dict[str, Any]:
    appell = load_json(APPELL_HUMBERT)
    integral_gap = load_json(INTEGRAL_GAP)
    selector_obstruction = load_json(SELECTOR_OBSTRUCTION)
    radius_nogo = load_json(RADIUS_NOGO)
    orientation = load_json(ORIENTATION_GATE)

    write_json(TEMPLATE, template_packet())
    write_json(CURRENT_ATTEMPT, current_appell_humbert_attempt(appell))

    template_validation = run_validator(TEMPLATE)
    current_validation = run_validator(CURRENT_ATTEMPT)

    input_statuses = {
        "appell_humbert": appell.get("status"),
        "integral_lift_gap": integral_gap.get("status"),
        "selector_obstruction": selector_obstruction.get("status"),
        "selected_radius_import_nogo": radius_nogo.get("status"),
        "orientation_gate": orientation.get("status"),
    }

    current_open_items = current_validation.get("parsed_report", {}).get("open_items", [])
    blockers = {
        "explicit_appell_humbert_formula_exists": appell.get("what_this_closes", {}).get(
            "explicit_nonflat_factor_of_automorphy_for_L2_2_minus4_0"
        )
        is True,
        "finite_mod3_qutrit_not_enough": orientation.get("finite_qutrit_branch_test", {}).get(
            "target_equals_swapped_in_F3"
        )
        is True
        or integral_gap.get("what_this_closes", {}).get(
            "finite_mod3_qutrit_data_no_go_for_target_vs_swapped_integral_lift"
        )
        is True,
        "equal_radius_import_ruled_out": radius_nogo.get("what_this_closes", {}).get(
            "constants_import_does_not_match_target_wall"
        )
        is True,
        "current_appell_humbert_packet_refused_by_validator": current_validation.get("exit_code")
        == 2,
        "missing_selected_source_status": "source status is not a selected ordered-source status"
        in current_open_items,
        "missing_base_order_selection": "selection evidence missing: base_factor_order_selected"
        in current_open_items,
        "missing_pic0_resolution": "Pic0 character not selected or quotiented" in current_open_items,
    }

    gate_formulated = (
        input_statuses["appell_humbert"]
        == "VISIBLE_RANK2_L2_APPELL_HUMBERT_AUTOMORPHY_CONSTRUCTED_SELECTION_OPEN"
        and input_statuses["integral_lift_gap"]
        == "VISIBLE_RANK2_L2_INTEGRAL_LIFT_REDUCED_TO_SOURCE_CERTIFICATE"
        and input_statuses["selector_obstruction"]
        == "VISIBLE_RANK2_L2_SELECTOR_OBSTRUCTION_PROVED_SOURCE_REQUIRED"
        and input_statuses["selected_radius_import_nogo"]
        == "VISIBLE_RANK2_L2_SELECTED_RADIUS_IMPORT_NO_GO_EQUAL_RADIUS"
        and all(blockers.values())
    )

    return {
        "calculation": "VisibleRank2L2OrderedSourcePromotionGate",
        "status": (
            "VISIBLE_RANK2_L2_ORDERED_SOURCE_PROMOTION_GATE_FORMULATED_SELECTION_OPEN"
            if gate_formulated
            else "VISIBLE_RANK2_L2_ORDERED_SOURCE_PROMOTION_GATE_INCONCLUSIVE"
        ),
        "generated_by": "scripts/build_visible_rank2_l2_ordered_source_promotion_gate.py",
        "validator": "scripts/validate_visible_rank2_l2_ordered_source_packet.py",
        "template": "certificates/visible_rank2_l2_ordered_source.template.json",
        "current_attempt": "candidate_data/visible_rank2_l2_ordered_source.current_attempt.json",
        "input_statuses": input_statuses,
        "valid_selected_source_statuses": [
            "VISIBLE_RANK2_L2_ORDERED_SOURCE_SELECTED",
            "VISIBLE_RANK2_L2_ORDERED_SOURCE_SELECTED_PIC0_QUOTIENTED",
        ],
        "target_ordered_matrix": {
            "L": TARGET_L,
            "L2": TARGET_L2,
            "E_g1_g2": 2,
            "E_g3_g4": -4,
            "E_g5_g6": 0,
            "matrix_order_g1_to_g6": target_matrix(),
        },
        "validation_results": {
            "template": template_validation,
            "current_appell_humbert_attempt": current_validation,
        },
        "blockers": blockers,
        "promotion_contract": {
            "must_supply_selected_source_status": True,
            "must_select_standard_lattice_or_equivalent": True,
            "must_select_ordered_base_factors": "E1/g1g2 carries +2 and E2/g3g4 carries -4",
            "must_break_target_vs_swapped_base_swap": True,
            "must_not_be_only_finite_mod3_qutrit": True,
            "must_not_be_equal_radius_import": True,
            "must_resolve_pic0": [
                "neutral_character_selected",
                "pic0_quotient_rule",
                "specific_flat_character_selected",
            ],
            "must_forbid_proxy_inputs": True,
        },
        "what_this_closes": {
            "ordered_source_packet_schema_and_validator": True,
            "current_appell_humbert_existence_packet_tested_against_promotion_gate": True,
            "current_appell_humbert_packet_correctly_refused_as_unselected_fixture": True,
            "remaining_ordered_source_gap_made_machine_checkable": True,
        },
        "still_open": {
            "selected_ordered_integral_source_certificate": True,
            "standard_lattice_or_equivalent_source_selection": True,
            "base_ordering_source_selection": True,
            "pic0_selection_or_quotient_rule": True,
            "nonzero_Ext_class_selection": True,
            "non_split_extension_stability": True,
            "same_source_D_E_dotD_Riesz_Green": True,
            "full_SM_closure": True,
        },
        "guardrails": {
            "claims_current_appell_humbert_packet_selected": False,
            "claims_ordered_source_closed": False,
            "claims_pic0_resolved": False,
            "claims_nonzero_Ext_class_selected": False,
            "claims_stability_proved": False,
            "claims_D_E_dotD_constructed": False,
            "claims_full_SM_closure": False,
            "uses_observed_flavor_data": False,
            "uses_benchmark_flavor_entries": False,
        },
        "verdict": {
            "honest_answer": (
                "The ordered Appell-Humbert representative is mathematically built, "
                "but it still fails the stricter selected-source promotion gate. "
                "The missing items are now executable: source status, selected "
                "lattice/base ordering, target-vs-swapped symmetry breaking, and "
                "Pic0 selection or quotienting."
            ),
            "next_action": (
                "Find or construct a source certificate with status "
                "VISIBLE_RANK2_L2_ORDERED_SOURCE_SELECTED or "
                "VISIBLE_RANK2_L2_ORDERED_SOURCE_SELECTED_PIC0_QUOTIENTED, then "
                "fill visible_rank2_l2_ordered_source.template.json and run the validator."
            ),
        },
    }


def main() -> int:
    report = analyze()
    write_json(CANDIDATE, report)
    certificate = {
        "certificate": "VisibleRank2L2OrderedSourcePromotionGate",
        "status": report["status"],
        "analysis_script": report["generated_by"],
        "validator": report["validator"],
        "candidate_data": "candidate_data/visible_rank2_l2_ordered_source_promotion_gate.candidate.json",
        "template": report["template"],
        "current_attempt": report["current_attempt"],
        "input_statuses": report["input_statuses"],
        "valid_selected_source_statuses": report["valid_selected_source_statuses"],
        "target_ordered_matrix": report["target_ordered_matrix"],
        "validation_results": report["validation_results"],
        "blockers": report["blockers"],
        "promotion_contract": report["promotion_contract"],
        "what_this_closes": report["what_this_closes"],
        "still_open": report["still_open"],
        "guardrails": report["guardrails"],
        "verdict": report["verdict"],
    }
    write_json(CERTIFICATE, certificate)
    print(json.dumps(report, indent=2, sort_keys=True))
    return 0 if report["status"].endswith("SELECTION_OPEN") else 1


if __name__ == "__main__":
    raise SystemExit(main())
