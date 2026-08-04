"""Attempt the selected monad-difference L2 source for Qa/SU3 visible V_alpha."""

from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
CERTS = ROOT / "certificates"
Q79_REPO = Path(r"C:\Users\nero_\Downloads\TEXPAPERS\mtt-q79-proof-repro")

PREVIOUS = CERTS / "selected_qa_su3_visible_l2_orientation_source_attempt_certificate.json"
Q79_MONAD_CANDIDATE = Q79_REPO / "certificates" / "iwasawa_monad_l2_branch_orientation_candidate_certificate.json"
Q79_MONAD_SUFF = Q79_REPO / "certificates" / "monad_difference_l2_source_sufficiency_certificate.json"
Q79_MONAD_MAP_GATE = Q79_REPO / "certificates" / "iwasawa_monad_map_data_gate_certificate.json"
Q79_MONAD_ROLE = Q79_REPO / "certificates" / "iwasawa_monad_visible_source_role_certificate.json"
Q79_ORDERED_VALIDATOR = Q79_REPO / "scripts" / "validate_visible_rank2_l2_ordered_source_packet.py"
Q79_HYPOTHETICAL_SELECTED = (
    Q79_REPO / "candidate_data" / "visible_rank2_l2_ordered_source.monad_difference_hypothetical_selected.json"
)
Q79_UNSELECTED_CANDIDATE = (
    Q79_REPO / "candidate_data" / "visible_rank2_l2_ordered_source.monad_difference_candidate.json"
)

OUTPUT_TEMPLATE = CERTS / "selected_qa_su3_monad_difference_l2_source.template.json"
OUTPUT_CERT = CERTS / "selected_qa_su3_monad_difference_l2_source_attempt_certificate.json"


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


def make_template() -> dict[str, Any]:
    return {
        "schema": "SelectedQaSU3MonadDifferenceL2Source.v1",
        "status": "OPEN_SELECTED_QA_SU3_MONAD_DIFFERENCE_L2_SOURCE_REQUIRED",
        "purpose": (
            "Prove that the ordered Iwasawa monad pair L3,K2 is selected as "
            "the visible V_alpha L-branch source, not merely an arithmetic clue."
        ),
        "target": {
            "ordered_difference": "L3_minus_K2",
            "L3": [1, -1, 0],
            "K2": [0, 1, 0],
            "L": [1, -2, 0],
            "L2": [2, -4, 0],
        },
        "must_supply": {
            "selected_monad_pair_source_certificate": None,
            "typed_f_sections": None,
            "typed_g_sections": None,
            "transition_data_for_L3_K2_or_equivalent": None,
            "binds_to_appell_humbert_or_cech_L2_transitions": None,
            "standard_lattice_or_equivalent_selected": None,
            "base_ordering_selected_by_source": None,
            "Pic0_selected_or_quotiented": None,
            "ordered_source_validator_passes_unconditionally": None,
            "same_source_D_E_dotD_Riesz_Green": None,
        },
    }


def main() -> None:
    previous = load(PREVIOUS)
    monad_candidate = load(Q79_MONAD_CANDIDATE)
    suff = load(Q79_MONAD_SUFF)
    map_gate = load(Q79_MONAD_MAP_GATE)
    role = load(Q79_MONAD_ROLE)
    selected_validation = run_ordered_validator(Q79_HYPOTHETICAL_SELECTED)
    unselected_validation = run_ordered_validator(Q79_UNSELECTED_CANDIDATE)
    selected_report = selected_validation["report"] or {}
    unselected_report = unselected_validation["report"] or {}

    ordered_candidate_found = (
        monad_candidate["key_candidate"]["ordered_difference"] == "L3_minus_K2"
        and monad_candidate["key_candidate"]["value"] == [1, -2, 0]
        and monad_candidate["key_candidate"]["double_value"] == [2, -4, 0]
        and monad_candidate["key_candidate"]["matches_target_L"] is True
    )
    hypothetical_passes = (
        selected_validation["exit_code"] == 0
        and selected_report.get("status") == "PASS"
        and selected_report.get("open_items") == []
    )
    current_candidate_refused = (
        unselected_validation["exit_code"] == 2
        and unselected_report.get("status") == "OPEN"
        and "source.selected_by_mtt is not true" in unselected_report.get("open_items", [])
    )
    source_selection_still_open = (
        suff["what_this_does_not_close"]["actual_MTT_selection_of_L3_minus_K2"] is False
        and map_gate["status"] == "IWASAWA_MONAD_MAP_DATA_GATE_BLOCKED_TYPED_MAP_SECTIONS_MISSING"
        and role["calculation_results"]["printed_monad_not_visible_alpha1_source"] is True
    )

    output = {
        "certificate": "SelectedQaSU3MonadDifferenceL2SourceAttempt",
        "status": "QA_SU3_MONAD_DIFFERENCE_L2_SOURCE_ATTEMPT_SUFFICIENCY_CLOSED_SELECTION_OPEN",
        "inputs": {
            "previous_orientation_gate": str(PREVIOUS.relative_to(ROOT)),
            "q79_monad_candidate": str(Q79_MONAD_CANDIDATE),
            "q79_monad_sufficiency": str(Q79_MONAD_SUFF),
            "q79_monad_map_gate": str(Q79_MONAD_MAP_GATE),
            "q79_monad_visible_role": str(Q79_MONAD_ROLE),
            "q79_hypothetical_selected_packet": str(Q79_HYPOTHETICAL_SELECTED),
            "q79_unselected_candidate_packet": str(Q79_UNSELECTED_CANDIDATE),
            "q79_ordered_validator": str(Q79_ORDERED_VALIDATOR),
        },
        "template_written": str(OUTPUT_TEMPLATE.relative_to(ROOT)),
        "closed_now": {
            "ordered_integral_lift_candidate_found": ordered_candidate_found,
            "candidate_stronger_than_finite_mod3_qutrit": monad_candidate["what_this_closes"][
                "candidate_is_stronger_than_finite_mod3_qutrit"
            ]
            is True,
            "candidate_not_equal_radius_import": monad_candidate["what_this_closes"][
                "candidate_is_not_equal_radius_import"
            ]
            is True,
            "hypothetical_selected_packet_passes_ordered_validator": hypothetical_passes,
            "unselected_candidate_refused_honestly": current_candidate_refused,
            "sufficiency_of_selected_monad_difference": suff["relative_theorem"]["proved"] is True,
        },
        "validator_comparison": {
            "hypothetical_selected": {
                "exit_code": selected_validation["exit_code"],
                "status": selected_report.get("status"),
                "open_items": selected_report.get("open_items"),
            },
            "unselected_candidate": {
                "exit_code": unselected_validation["exit_code"],
                "status": unselected_report.get("status"),
                "open_items": unselected_report.get("open_items"),
            },
            "promotion_delta_only_source_and_pic0_fields": suff["promotion_delta"][
                "only_source_selection_and_pic0_fields_changed"
            ],
        },
        "not_closed": {
            "actual_MTT_selection_of_L3_minus_K2": source_selection_still_open,
            "typed_monad_sections_for_source": map_gate["typed_map_check"][
                "requires_global_holomorphic_sections_or_transition_data"
            ],
            "bind_monad_difference_to_L2_transitions": monad_candidate["still_open"][
                "bind_monad_difference_to_Appell_Humbert_or_Cech_transitions"
            ],
            "Pic0_selection_or_quotient": suff["still_open"]["select_or_quotient_Pic0_without_notational_assumption"],
            "Ext_packet_promotion_and_stability": suff["still_open"]["promote_Ext_packet_and_prove_stability"],
            "same_source_D_E_dotD_Riesz_Green": suff["still_open"]["compute_same_source_D_E_dotD_Riesz_Green"],
            "printed_monad_is_not_whole_c2_4_alpha1_source": role["what_this_closes"][
                "do_not_reuse_c2_zero_monad_as_c2_4_alpha1_source"
            ],
            "full_SM_closure": True,
        },
        "minimal_next_object": {
            "name": "Selected_Monad_Difference_L2_Source.v1",
            "must_prove": [
                "L3-K2 is selected as the visible V_alpha ordered integral source slot",
                "standard/equivalent Iwasawa lattice and base order are selected by source data",
                "neutral Pic0 is selected or Pic0 is quotient-irrelevant",
                "the monad-difference label binds to the Appell-Humbert/Cech L2 transitions",
                "typed monad sections or equivalent transition data are supplied, not inferred from scalar constants",
            ],
            "after_success": [
                "rerun ordered-source validator as selected data",
                "promote the h1=8 nonzero Ext packet",
                "prove non-split stability and HYM/Route-C continuation",
                "derive same-source D_E/dotD/Riesz/Green",
            ],
        },
        "guardrails": {
            "claims_selected_monad_difference_source_proved": False,
            "claims_current_corpus_selects_L3_minus_K2": False,
            "claims_pic0_resolved_now": False,
            "claims_printed_monad_is_whole_visible_c2_source": False,
            "claims_ordered_source_closed_unconditionally": False,
            "claims_full_SM_closure": False,
            "uses_observed_masses_or_mixings": False,
            "uses_benchmark_flavor_entries": False,
        },
        "gate_result": {
            "monad_difference_l2_source_closed": False,
            "sufficiency_theorem_closed": hypothetical_passes,
            "remaining_gate_is_selected_monad_difference_source": source_selection_still_open,
            "target_fitting_used": False,
        },
    }

    cert_text = json.dumps(output, indent=2, sort_keys=True)
    template_text = json.dumps(make_template(), indent=2, sort_keys=True)
    if "--write-certificate" in sys.argv:
        OUTPUT_CERT.write_text(cert_text + "\n", encoding="utf-8")
        OUTPUT_TEMPLATE.write_text(template_text + "\n", encoding="utf-8")
    print(cert_text)


if __name__ == "__main__":
    main()
