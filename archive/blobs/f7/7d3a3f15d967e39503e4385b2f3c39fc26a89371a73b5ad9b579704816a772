"""Attempt to promote the q79 rank-two V_alpha route to a selected Qa/SU3 source."""

from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
CERTS = ROOT / "certificates"
Q79_REPO = Path(r"C:\Users\nero_\Downloads\TEXPAPERS\mtt-q79-proof-repro")

PREVIOUS = CERTS / "selected_qa_su3_visible_operator_source_packet_attempt_certificate.json"
Q79_VALPHA_CANDIDATES = Q79_REPO / "certificates" / "visible_valpha_chern_bianchi_source_packet_candidates_certificate.json"
Q79_RANK2_ROUTE = Q79_REPO / "certificates" / "visible_rank2_extension_valpha_route_certificate.json"
Q79_EXT_H1_GATE = Q79_REPO / "certificates" / "visible_rank2_l2_ext_h1_gate_certificate.json"
Q79_PULLBACK_CECH = Q79_REPO / "certificates" / "visible_rank2_l2_pullback_cech_attempt_certificate.json"
Q79_APPELL = Q79_REPO / "certificates" / "visible_rank2_l2_appell_humbert_automorphy_certificate.json"
Q79_SELECTION = Q79_REPO / "certificates" / "visible_rank2_l2_pullback_selection_attempt_certificate.json"
Q79_BRANCH = Q79_REPO / "certificates" / "visible_rank2_l2_branch_selection_reduction_certificate.json"
Q79_SELECTOR_OBSTRUCTION = Q79_REPO / "certificates" / "visible_rank2_l2_selector_obstruction_certificate.json"
Q79_COHOMOLOGY_PACKET = Q79_REPO / "candidate_data" / "visible_rank2_l2_pullback_cech_attempt.cohomology.json"
Q79_COHOMOLOGY_TEMPLATE = Q79_REPO / "certificates" / "visible_rank2_l2_cohomology_data.template.json"
Q79_COHOMOLOGY_VALIDATOR = Q79_REPO / "scripts" / "validate_visible_rank2_l2_cohomology.py"

OUTPUT_TEMPLATE = CERTS / "selected_qa_su3_visible_rank2_valpha_source_packet.template.json"
OUTPUT_CERT = CERTS / "selected_qa_su3_visible_rank2_valpha_source_attempt_certificate.json"


def load(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def run_l2_validator() -> dict[str, Any]:
    proc = subprocess.run(
        [sys.executable, str(Q79_COHOMOLOGY_VALIDATOR), str(Q79_COHOMOLOGY_PACKET)],
        cwd=Q79_REPO,
        text=True,
        stdout=subprocess.PIPE,
        stderr=subprocess.STDOUT,
    )
    lines = [line for line in proc.stdout.strip().splitlines() if line]
    report = None
    for line in lines:
        if line.startswith("visible_rank2_l2_h1_report="):
            report = json.loads(line.removeprefix("visible_rank2_l2_h1_report="))
    return {
        "exit_code": proc.returncode,
        "output": lines,
        "report": report,
    }


def make_template(q79_template: dict[str, Any]) -> dict[str, Any]:
    template = dict(q79_template)
    template["schema"] = "SelectedQaSU3VisibleRank2VAlphaSourcePacket.v1"
    template["status"] = "OPEN_SELECTED_QA_SU3_VISIBLE_RANK2_VALPHA_SOURCE_PACKET_REQUIRED"
    template["purpose"] = (
        "Promotion slot for the q79 rank-two non-split extension "
        "0 -> L -> V_alpha -> L^{-1} -> 0, with L=(1,-2,0), "
        "as the selected visible Qa/SU3 source."
    )
    template["must_supply_after_q79_conditional_packet"] = {
        "selected_branch_orientation_source_for_L_equals_1_minus2_0": None,
        "selected_ordered_base_factor_or_Gauduchon_wall": None,
        "neutral_or_quotiented_Pic0_character_source": None,
        "selected_L2_automorphy_or_Cech_source_certificate": None,
        "same_source_nonzero_Ext_class_selection": None,
        "non_split_stability_certificate": None,
        "HYM_or_Route_C_residual_for_V_alpha": None,
        "same_source_D_E_dotD_Riesz_Green": None,
        "SM_sector_projector_retention": None,
    }
    return template


def main() -> None:
    previous = load(PREVIOUS)
    valpha = load(Q79_VALPHA_CANDIDATES)
    rank2 = load(Q79_RANK2_ROUTE)
    ext_h1 = load(Q79_EXT_H1_GATE)
    pullback = load(Q79_PULLBACK_CECH)
    appell = load(Q79_APPELL)
    selection = load(Q79_SELECTION)
    branch = load(Q79_BRANCH)
    obstruction = load(Q79_SELECTOR_OBSTRUCTION)
    q79_template = load(Q79_COHOMOLOGY_TEMPLATE)
    validation = run_l2_validator()
    report = validation["report"] or {}
    template = make_template(q79_template)

    target = rank2["calculation_results"]
    algebraic_ext_closed = (
        validation["exit_code"] == 0
        and report.get("h1") == 8
        and report.get("nonzero_ext_class") is True
        and report.get("extension_class_closed") is True
        and report.get("extension_class_exact") is False
    )
    automorphy_exists = all(
        appell["construction_checks"].get(key) is True
        for key in (
            "c1_matrix_matches_required_order",
            "c1_L_squared_square_is_minus_16_alpha1",
            "c2_extension_target_is_plus_4_alpha1",
            "shared_circle_degree_zero_retained",
        )
        if key in appell["construction_checks"]
    ) and appell["construction_checks"]["c2_extension_target_is_plus_4_alpha1"] is True
    selected_source_absent = (
        report.get("selected_source_promotes") is False
        and pullback["calculation_results"]["selected_L2_packet_constructed"] is False
        and selection["unconditional_selection_theorem"]["proved"] is False
        and obstruction["no_breaking_source_available"] is True
    )
    target_branch_valid_open = (
        branch["target_branch"]["L"] == [1, -2, 0]
        and branch["target_branch"]["status"] == "valid branch, not uniquely selected"
    )

    output = {
        "certificate": "SelectedQaSU3VisibleRank2VAlphaSourceAttempt",
        "status": "QA_SU3_VISIBLE_RANK2_VALPHA_SOURCE_ATTEMPT_CONDITIONAL_EXT_CLOSED_SELECTION_OPEN",
        "inputs": {
            "previous_visible_operator_gate": str(PREVIOUS.relative_to(ROOT)),
            "q79_valpha_candidates": str(Q79_VALPHA_CANDIDATES),
            "q79_rank2_route": str(Q79_RANK2_ROUTE),
            "q79_ext_h1_gate": str(Q79_EXT_H1_GATE),
            "q79_pullback_cech": str(Q79_PULLBACK_CECH),
            "q79_appell_humbert": str(Q79_APPELL),
            "q79_selection_attempt": str(Q79_SELECTION),
            "q79_branch_reduction": str(Q79_BRANCH),
            "q79_selector_obstruction": str(Q79_SELECTOR_OBSTRUCTION),
            "q79_cohomology_packet": str(Q79_COHOMOLOGY_PACKET),
            "q79_cohomology_validator": str(Q79_COHOMOLOGY_VALIDATOR),
        },
        "template_written": str(OUTPUT_TEMPLATE.relative_to(ROOT)),
        "selected_rank2_route": {
            "source_shape": "0 -> L -> V_alpha -> L^{-1} -> 0",
            "target_branch_L": [1, -2, 0],
            "target_L_squared": [2, -4, 0],
            "c1_V_alpha": [0, 0, 0],
            "c2_V_alpha": [4, 0, 0],
            "math_ch2": [-4, 0, 0],
            "shared_circle_degree": 0,
            "rank2_topological_route_formulated": target["number_of_primitive_line_classes"] == 4
            and valpha["best_current_route"]["candidate_id"] == "rank2_non_split_extension_preferred_L_1_-2_0",
        },
        "validated_conditional_ext_packet": {
            "validator_exit_code": validation["exit_code"],
            "candidate_role": report.get("candidate_role"),
            "h1": report.get("h1"),
            "d1_d0_zero": report.get("d1_d0_zero"),
            "extension_class_closed": report.get("extension_class_closed"),
            "extension_class_exact": report.get("extension_class_exact"),
            "nonzero_ext_class": report.get("nonzero_ext_class"),
            "selected_source_promotes": report.get("selected_source_promotes"),
            "promotes_to_non_split_V_alpha_input": report.get("promotes_to_non_split_V_alpha_input"),
        },
        "closed_now": {
            "topological_rank2_target_c1_c2": rank2["status"]
            == "VISIBLE_RANK2_EXTENSION_VALPHA_ROUTE_FORMULATED_EXT_STABILITY_OPEN",
            "explicit_appell_humbert_automorphy_for_L2": appell["selection_analysis"][
                "mathematical_automorphy_representative_constructed"
            ]
            is True,
            "conditional_h1_equals_8_and_nonzero_ext": algebraic_ext_closed,
            "relative_selection_theorem_if_source_certificate_supplied": selection["relative_selection_theorem"][
                "proved"
            ]
            is True,
            "selector_obstruction_from_current_closed_invariants": obstruction["obstruction_theorem"][
                "theorem"
            ]
            == "No current closed selector can uniquely select L=(1,-2,0)",
        },
        "not_closed": {
            "unique_MTT_branch_orientation_for_L": target_branch_valid_open,
            "selected_L2_packet": selected_source_absent,
            "neutral_or_quotiented_Pic0_character": obstruction["still_open"][
                "selected_or_quotiented_Pic0_character"
            ],
            "selected_ordered_integral_Cech_automorphy_D_E_source": obstruction["still_open"][
                "selected_ordered_integral_Cech_automorphy_D_E_source"
            ],
            "non_split_stability": obstruction["still_open"]["non_split_stability"],
            "same_source_D_E_dotD_Riesz_Green": selection["still_open"][
                "derive_same_total_source_D_E_dotD_Riesz_Green"
            ],
            "HYM_or_Route_C_residual_for_visible_source": previous["not_closed"][
                "HYM_or_Route_C_residual_for_visible_source"
            ],
            "full_SM_closure": True,
        },
        "minimal_next_object": {
            "name": "Selected_Pullback_L2_Branch_Orientation_Source.v1",
            "must_break": [
                "base-swap degeneracy between target and swapped branch",
                "flat Pic0 character degeneracy",
            ],
            "allowed_sources": obstruction["obstruction_theorem"]["does_not_apply_if_new_source_supplies"],
            "promotion_rule": (
                "After a selected source certificate is supplied, rerun the same H1=8 "
                "cochain matrices as SELECTED_DATA and then prove stability/HYM or Route-C "
                "for the same V_alpha source."
            ),
        },
        "guardrails": {
            "claims_selected_visible_valpha_source_constructed": False,
            "claims_unique_L_branch_selected": False,
            "claims_neutral_Pic0_selected": False,
            "claims_non_split_stability_proved": False,
            "claims_HYM_or_Route_C_residual_proved": False,
            "claims_selected_D_E_dotD_constructed": False,
            "claims_full_SM_closure": False,
            "uses_observed_masses_or_mixings": False,
            "uses_benchmark_flavor_entries": False,
        },
        "gate_result": {
            "visible_rank2_valpha_source_closed": False,
            "conditional_ext_math_closed": algebraic_ext_closed and automorphy_exists,
            "remaining_gate_is_selector_not_ext_existence": selected_source_absent,
            "template_ready": True,
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
