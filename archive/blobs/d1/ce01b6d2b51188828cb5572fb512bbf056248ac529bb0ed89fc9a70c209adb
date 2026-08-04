"""Attempt the selected orientation source for the visible rank-two L2 branch."""

from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
CERTS = ROOT / "certificates"
Q79_REPO = Path(r"C:\Users\nero_\Downloads\TEXPAPERS\mtt-q79-proof-repro")

PREVIOUS = CERTS / "selected_qa_su3_visible_rank2_valpha_source_attempt_certificate.json"
Q79_ORIENTATION = Q79_REPO / "certificates" / "selected_pullback_l2_branch_orientation_source_gate_certificate.json"
Q79_GAUDUCHON = Q79_REPO / "certificates" / "selected_gauduchon_wall_radius_gate_certificate.json"
Q79_ORDERED = Q79_REPO / "certificates" / "visible_rank2_l2_ordered_source_promotion_gate_certificate.json"
Q79_RADIUS_NOGO = Q79_REPO / "certificates" / "visible_rank2_l2_selected_radius_import_nogo_certificate.json"
Q79_SELECTOR_OBSTRUCTION = Q79_REPO / "certificates" / "visible_rank2_l2_selector_obstruction_certificate.json"
Q79_ORDERED_ATTEMPT = Q79_REPO / "candidate_data" / "visible_rank2_l2_ordered_source.current_attempt.json"
Q79_ORDERED_TEMPLATE = Q79_REPO / "certificates" / "visible_rank2_l2_ordered_source.template.json"
Q79_ORDERED_VALIDATOR = Q79_REPO / "scripts" / "validate_visible_rank2_l2_ordered_source_packet.py"

OUTPUT_TEMPLATE = CERTS / "selected_qa_su3_visible_l2_orientation_source.template.json"
OUTPUT_CERT = CERTS / "selected_qa_su3_visible_l2_orientation_source_attempt_certificate.json"


def load(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def run_ordered_validator(packet: Path) -> dict[str, Any]:
    proc = subprocess.run(
        [sys.executable, str(Q79_ORDERED_VALIDATOR), str(packet)],
        cwd=Q79_REPO,
        text=True,
        stdout=subprocess.PIPE,
        stderr=subprocess.STDOUT,
    )
    lines = [line for line in proc.stdout.strip().splitlines() if line]
    report = None
    for line in lines:
        if line.startswith("visible_rank2_l2_ordered_source_validation_report="):
            report = json.loads(line.removeprefix("visible_rank2_l2_ordered_source_validation_report="))
    return {
        "exit_code": proc.returncode,
        "output": lines,
        "report": report,
    }


def make_template(ordered: dict[str, Any]) -> dict[str, Any]:
    return {
        "schema": "SelectedQaSU3VisibleL2OrientationSource.v1",
        "status": "OPEN_SELECTED_QA_SU3_VISIBLE_L2_ORIENTATION_SOURCE_REQUIRED",
        "purpose": (
            "Supply the selected source that promotes the ordered L^2 branch "
            "L=(1,-2,0), resolves/quotients Pic0, and breaks target-vs-swapped "
            "base-swap degeneracy before the V_alpha Ext packet is promoted."
        ),
        "target_ordered_matrix": ordered["target_ordered_matrix"],
        "recognized_selected_statuses": ordered["valid_selected_source_statuses"],
        "must_supply": {
            "selected_source_status": None,
            "standard_lattice_or_equivalent_selected": None,
            "base_factor_order_selected": None,
            "base_swap_broken_by_source": None,
            "not_only_finite_mod3_qutrit": None,
            "not_equal_radius_import": None,
            "pic0_resolution_rule": None,
            "pic0_character_selected_or_quotiented": None,
            "raw_transition_or_automorphy_data": None,
        },
    }


def main() -> None:
    previous = load(PREVIOUS)
    orientation = load(Q79_ORIENTATION)
    gauduchon = load(Q79_GAUDUCHON)
    ordered = load(Q79_ORDERED)
    radius_nogo = load(Q79_RADIUS_NOGO)
    obstruction = load(Q79_SELECTOR_OBSTRUCTION)
    attempt_validation = run_ordered_validator(Q79_ORDERED_ATTEMPT)
    template_validation = run_ordered_validator(Q79_ORDERED_TEMPLATE)
    template = make_template(ordered)

    attempt_report = attempt_validation["report"] or {}
    open_items = attempt_report.get("open_items", [])
    finite_qutrit_insufficient = orientation["finite_qutrit_gate"]["target_and_swapped_same_finite_signature"] is True
    target_wall_identified = (
        orientation["gauduchon_chamber_gate"]["target_wall_would_select_L_1_minus2_0"] is True
        and gauduchon["wall_dictionary"]["target_wall"]["p1:p2"] == "1:2"
        and gauduchon["wall_dictionary"]["target_wall"]["equivalent_radius_ratio"] == "r1:r2 = sqrt(2):1"
    )
    current_sources_do_not_select_wall = (
        gauduchon["current_source_status"]["source_certified_target_wall_present"] is False
        and radius_nogo["no_go_theorem"]["theorem"]
        == "The closed constants selected radius cannot be the visible L2 target-wall selector."
    )
    ordered_gate_machine_checkable = (
        ordered["status"] == "VISIBLE_RANK2_L2_ORDERED_SOURCE_PROMOTION_GATE_FORMULATED_SELECTION_OPEN"
        and attempt_validation["exit_code"] == 2
        and "source.selected_by_mtt is not true" in open_items
        and "Pic0 character not selected or quotiented" in open_items
    )

    output = {
        "certificate": "SelectedQaSU3VisibleL2OrientationSourceAttempt",
        "status": "QA_SU3_VISIBLE_L2_ORIENTATION_SOURCE_ATTEMPT_REDUCED_TO_ORDERED_SOURCE_PACKET",
        "inputs": {
            "previous_valpha_gate": str(PREVIOUS.relative_to(ROOT)),
            "q79_orientation_gate": str(Q79_ORIENTATION),
            "q79_gauduchon_wall_gate": str(Q79_GAUDUCHON),
            "q79_ordered_source_gate": str(Q79_ORDERED),
            "q79_selected_radius_import_nogo": str(Q79_RADIUS_NOGO),
            "q79_selector_obstruction": str(Q79_SELECTOR_OBSTRUCTION),
            "q79_ordered_attempt": str(Q79_ORDERED_ATTEMPT),
            "q79_ordered_validator": str(Q79_ORDERED_VALIDATOR),
        },
        "template_written": str(OUTPUT_TEMPLATE.relative_to(ROOT)),
        "closed_now": {
            "finite_qutrit_orientation_insufficient": finite_qutrit_insufficient,
            "target_wall_identified": target_wall_identified,
            "equal_radius_import_rejected": radius_nogo["what_this_closes"][
                "constants_import_does_not_match_target_wall"
            ]
            is True,
            "ordered_source_validator_available": ordered_gate_machine_checkable,
            "current_appell_humbert_attempt_refused_honestly": ordered["blockers"][
                "current_appell_humbert_packet_refused_by_validator"
            ]
            is True,
            "selector_obstruction_preserved": obstruction["no_breaking_source_available"] is True,
        },
        "ordered_source_validation": {
            "current_attempt_exit_code": attempt_validation["exit_code"],
            "current_attempt_status": attempt_report.get("status"),
            "current_attempt_open_items": open_items,
            "template_exit_code": template_validation["exit_code"],
            "target_matrix": attempt_report.get("target_matrix"),
            "recognized_selected_statuses": attempt_report.get("recognized_selected_statuses"),
        },
        "not_closed": {
            "selected_source_status": "source.selected_by_mtt is not true" in open_items,
            "base_factor_order_selected": "selection evidence missing: base_factor_order_selected" in open_items,
            "base_swap_broken_by_source": "selection evidence missing: base_swap_broken_by_source" in open_items,
            "Pic0_resolution": "Pic0 resolution rule missing" in open_items
            or "Pic0 character not selected or quotiented" in open_items,
            "selected_target_wall_source": current_sources_do_not_select_wall,
            "integral_lift_from_qutrit_to_integer_branch": orientation["still_open"][
                "integral_lift_from_finite_qutrit_image_to_integer_branch"
            ],
            "non_split_extension_stability": previous["not_closed"]["non_split_stability"],
            "same_source_D_E_dotD_Riesz_Green": previous["not_closed"]["same_source_D_E_dotD_Riesz_Green"],
            "full_SM_closure": True,
        },
        "minimal_next_object": {
            "name": "visible_rank2_l2_ordered_source.selected.json",
            "accepted_statuses": ordered["valid_selected_source_statuses"],
            "validator": str(Q79_ORDERED_VALIDATOR),
            "must_pass_before_selected_ext_promotion": ordered["promotion_contract"],
        },
        "guardrails": {
            "claims_orientation_source_closed": False,
            "claims_target_wall_selected": False,
            "claims_equal_radius_import_selects_target": False,
            "claims_finite_qutrit_selects_integer_branch": False,
            "claims_Pic0_resolved": False,
            "claims_selected_D_E_dotD_constructed": False,
            "claims_full_SM_closure": False,
            "uses_observed_masses_or_mixings": False,
            "uses_benchmark_flavor_entries": False,
        },
        "gate_result": {
            "visible_l2_orientation_source_closed": False,
            "orientation_gap_machine_checkable": True,
            "remaining_gate_is_ordered_selected_source_packet": True,
            "target_fitting_used": False,
        },
    }

    cert_text = json.dumps(output, indent=2, sort_keys=True)
    template_text = json.dumps(template, indent=2, sort_keys=True)
    if "--write-certificate" in sys.argv:
        OUTPUT_CERT.write_text(cert_text + "\n", encoding="utf-8")
        OUTPUT_TEMPLATE.write_text(template_text + "\n", encoding="utf-8")
    print(cert_text)


if __name__ == "__main__":
    main()
