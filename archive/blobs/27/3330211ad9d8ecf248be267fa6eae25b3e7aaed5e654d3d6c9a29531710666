"""Attempt the selected monad-difference L^2 source theorem.

The current corpus proves a strong conditional statement:

    if the visible ordered L source is selected from the terminal Iwasawa
    monad differences L_i-K2, then the target branch is uniquely L3-K2.

It does not yet prove the stronger unconditional source theorem.  This script
records both facts in a machine-readable certificate so the proof frontier does
not drift.
"""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
TEXPAPERS = ROOT.parent
CONSTANTS_REPO = TEXPAPERS / "mtt-nonsm-constants-no-knob"

CERTIFICATES = ROOT / "certificates"
CANDIDATE_DATA = ROOT / "candidate_data"

MONAD_GATE = CERTIFICATES / "iwasawa_monad_map_data_gate_certificate.json"
MONAD_ROLE = CERTIFICATES / "iwasawa_monad_visible_source_role_certificate.json"
MONAD_CANDIDATE = CERTIFICATES / "iwasawa_monad_l2_branch_orientation_candidate_certificate.json"
MONAD_SUFFICIENCY = CERTIFICATES / "monad_difference_l2_source_sufficiency_certificate.json"
SELECTOR_OBSTRUCTION = CERTIFICATES / "visible_rank2_l2_selector_obstruction_certificate.json"

CONSTANTS_MONAD_ATTEMPT = (
    CONSTANTS_REPO
    / "certificates"
    / "selected_qa_su3_monad_difference_l2_source_attempt_certificate.json"
)
CONSTANTS_MAP_ATTEMPT = (
    CONSTANTS_REPO
    / "certificates"
    / "selected_qa_su3_monad_map_construction_or_source_augmentation_certificate.json"
)

CANDIDATE = CANDIDATE_DATA / "selected_monad_difference_l2_source_proof_attempt.candidate.json"
CERTIFICATE = CERTIFICATES / "selected_monad_difference_l2_source_proof_attempt_certificate.json"

TARGET_L = [1, -2, 0]
TARGET_L2 = [2, -4, 0]


def load_json(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8")) if path.exists() else {}


def write_json(path: Path, data: dict[str, Any]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(data, indent=2, sort_keys=True) + "\n", encoding="utf-8")


def sub(left: list[int], right: list[int]) -> list[int]:
    return [a - b for a, b in zip(left, right)]


def double(vec: list[int]) -> list[int]:
    return [2 * value for value in vec]


def terminal_differences(line_data: dict[str, list[int]]) -> list[dict[str, Any]]:
    k2 = line_data["K2"]
    rows: list[dict[str, Any]] = []
    for label in ["L1", "L2", "L3", "L4", "L5"]:
        value = sub(line_data[label], k2)
        dual = sub(k2, line_data[label])
        rows.append(
            {
                "label": f"{label}-K2",
                "ordered_pair": [label, "K2"],
                "value": value,
                "double_value": double(value),
                "central_degree": value[2],
                "matches_target_L": value == TARGET_L,
                "double_matches_target_L2": double(value) == TARGET_L2,
                "dual_label": f"K2-{label}",
                "dual_value": dual,
                "dual_matches_printed_g_type": label == "L3" and dual == [-1, 2, 0],
            }
        )
    return rows


def analyze() -> dict[str, Any]:
    monad_gate = load_json(MONAD_GATE)
    monad_role = load_json(MONAD_ROLE)
    monad_candidate = load_json(MONAD_CANDIDATE)
    sufficiency = load_json(MONAD_SUFFICIENCY)
    selector_obstruction = load_json(SELECTOR_OBSTRUCTION)
    constants_attempt = load_json(CONSTANTS_MONAD_ATTEMPT)
    constants_map_attempt = load_json(CONSTANTS_MAP_ATTEMPT)

    line_data = monad_gate.get("source_monad", {}).get("line_bundle_c1_vectors_abc", {})
    differences = terminal_differences(line_data)
    zero_central = [row for row in differences if row["central_degree"] == 0]
    target_matches = [row for row in differences if row["matches_target_L"]]
    double_target_matches = [row for row in differences if row["double_matches_target_L2"]]
    l3_row = target_matches[0] if target_matches else {}

    conditional_uniqueness = (
        monad_gate.get("status")
        == "IWASAWA_MONAD_MAP_DATA_GATE_BLOCKED_TYPED_MAP_SECTIONS_MISSING"
        and monad_candidate.get("status")
        == "IWASAWA_MONAD_L2_BRANCH_ORIENTATION_CANDIDATE_FOUND_SELECTION_OPEN"
        and len(zero_central) == 1
        and len(target_matches) == 1
        and len(double_target_matches) == 1
        and target_matches[0].get("label") == "L3-K2"
        and double_target_matches[0].get("label") == "L3-K2"
    )

    sufficiency_closed = (
        sufficiency.get("status")
        == "MONAD_DIFFERENCE_L2_SOURCE_SUFFICIENCY_PROVED_SELECTION_THEOREM_OPEN"
        and sufficiency.get("relative_theorem", {}).get("proved") is True
    )
    constants_agree = (
        constants_attempt.get("status")
        == "QA_SU3_MONAD_DIFFERENCE_L2_SOURCE_ATTEMPT_SUFFICIENCY_CLOSED_SELECTION_OPEN"
        and constants_attempt.get("gate_result", {}).get("monad_difference_l2_source_closed")
        is False
    )
    constants_sections_missing = (
        constants_map_attempt.get("status")
        == "QA_SU3_MONAD_MAP_CONSTRUCTION_BLOCKED_SECTION_RING_OR_SOURCE_AUGMENTATION_REQUIRED"
        and constants_map_attempt.get("construction_result", {}).get("section_data_found") is False
    )

    selected_source_open = (
        sufficiency.get("still_open", {}).get("prove_Selected_Monad_Difference_L2_Source_v1")
        is True
        and constants_attempt.get("not_closed", {}).get("actual_MTT_selection_of_L3_minus_K2")
        is True
    )
    pic0_open = (
        sufficiency.get("still_open", {}).get("select_or_quotient_Pic0_without_notational_assumption")
        is True
        and constants_attempt.get("not_closed", {}).get("Pic0_selection_or_quotient") is True
    )
    typed_maps_missing = (
        monad_gate.get("typed_map_check", {}).get("requires_global_holomorphic_sections_or_transition_data")
        is True
        and monad_gate.get("typed_map_check", {}).get("can_verify_g_after_f_zero") is False
    )
    not_whole_visible_c2_source = (
        monad_role.get("what_this_closes", {}).get("do_not_reuse_c2_zero_monad_as_c2_4_alpha1_source")
        is True
    )
    selector_no_hidden_shortcut = (
        selector_obstruction.get("status")
        == "VISIBLE_RANK2_L2_SELECTOR_OBSTRUCTION_PROVED_SOURCE_REQUIRED"
    )

    unconditional_selected_source_proved = (
        conditional_uniqueness
        and sufficiency_closed
        and not selected_source_open
        and not pic0_open
        and not typed_maps_missing
    )

    status = (
        "SELECTED_MONAD_DIFFERENCE_L2_SOURCE_PROVED"
        if unconditional_selected_source_proved
        else "SELECTED_MONAD_DIFFERENCE_L2_SOURCE_CONDITIONAL_UNIQUENESS_PROVED_SELECTION_OPEN"
    )

    return {
        "calculation": "SelectedMonadDifferenceL2SourceProofAttempt",
        "status": status,
        "generated_by": "scripts/prove_selected_monad_difference_l2_source_attempt.py",
        "input_certificates": {
            "iwasawa_monad_map_data_gate": MONAD_GATE.name,
            "iwasawa_monad_visible_source_role": MONAD_ROLE.name,
            "iwasawa_monad_l2_branch_orientation_candidate": MONAD_CANDIDATE.name,
            "monad_difference_l2_source_sufficiency": MONAD_SUFFICIENCY.name,
            "visible_rank2_l2_selector_obstruction": SELECTOR_OBSTRUCTION.name,
            "constants_monad_attempt": str(CONSTANTS_MONAD_ATTEMPT),
            "constants_map_attempt": str(CONSTANTS_MAP_ATTEMPT),
        },
        "input_statuses": {
            "monad_gate": monad_gate.get("status"),
            "monad_role": monad_role.get("status"),
            "monad_candidate": monad_candidate.get("status"),
            "monad_sufficiency": sufficiency.get("status"),
            "selector_obstruction": selector_obstruction.get("status"),
            "constants_monad_attempt": constants_attempt.get("status"),
            "constants_map_attempt": constants_map_attempt.get("status"),
        },
        "terminal_monad_difference_scan": {
            "target_L": TARGET_L,
            "target_L2": TARGET_L2,
            "differences": differences,
            "zero_central_terminal_differences": [row["label"] for row in zero_central],
            "target_matches": [row["label"] for row in target_matches],
            "double_target_matches": [row["label"] for row in double_target_matches],
            "selected_candidate_inside_lane": l3_row,
        },
        "conditional_uniqueness_theorem": {
            "proved": conditional_uniqueness,
            "hypotheses": [
                "the visible ordered L source is selected from terminal monad differences L_i-K2",
                "the source is base-pullback/central-neutral",
                "the selected L^2 target has c1(L^2)=(2,-4,0)",
                "the ordered sign convention is the Appell-Humbert/Cech convention E(g1,g2)=2, E(g3,g4)=-4",
            ],
            "conclusion": (
                "Under those hypotheses the unique terminal monad difference is "
                "L3-K2=(1,-2,0), whose double is (2,-4,0)."
            ),
            "dual_g3_check": {
                "printed_g3_type": [-1, 2, 0],
                "is_dual_to_selected_L3_minus_K2": l3_row.get("dual_matches_printed_g_type") is True,
            },
        },
        "sufficiency_import": {
            "proved": sufficiency_closed,
            "statement": sufficiency.get("relative_theorem", {}).get("statement"),
            "hypothetical_selected_packet_passes": (
                sufficiency.get("packets", {})
                .get("hypothetical_selected_validation", {})
                .get("exit_code")
                == 0
            ),
            "unselected_packet_refused": (
                sufficiency.get("packets", {}).get("unselected_validation", {}).get("exit_code")
                == 2
            ),
        },
        "unconditional_selection_attempt": {
            "proved": unconditional_selected_source_proved,
            "result": (
                "blocked: current audited corpus proves conditional uniqueness and sufficiency, "
                "not actual MTT source selection or Pic0 resolution"
            ),
            "open_blockers": {
                "actual_MTT_selection_of_terminal_monad_difference_lane": selected_source_open,
                "neutral_Pic0_selection_or_quotient": pic0_open,
                "typed_monad_sections_or_equivalent_transition_data": typed_maps_missing,
                "monad_is_not_whole_visible_c2_4_alpha1_source": not_whole_visible_c2_source,
                "no_hidden_selector_from_closed_invariants": selector_no_hidden_shortcut,
            },
        },
        "cross_repo_consistency": {
            "constants_repo_present": CONSTANTS_REPO.exists(),
            "constants_monad_attempt_agrees_selection_open": constants_agree,
            "constants_map_attempt_agrees_sections_missing": constants_sections_missing,
        },
        "what_this_closes": {
            "unique_L3_minus_K2_inside_ordered_terminal_monad_difference_lane": conditional_uniqueness,
            "dual_g3_type_identifies_the_same_line_up_to_dual": l3_row.get("dual_matches_printed_g_type")
            is True,
            "sufficiency_of_selected_monad_difference_imported": sufficiency_closed,
            "proof_frontier_no_longer_arithmetic": conditional_uniqueness and sufficiency_closed,
        },
        "what_this_does_not_close": {
            "unconditional_Selected_Monad_Difference_L2_Source_v1": unconditional_selected_source_proved,
            "actual_MTT_selection_of_L3_minus_K2": False,
            "Pic0_selection_or_quotient": False,
            "typed_monad_sections_for_source": False,
            "Ext_packet_promotion_and_stability": False,
            "same_source_D_E_dotD_Riesz_Green": False,
            "full_SM_closure": False,
        },
        "minimal_success_contract": {
            "name": "Selected_Monad_Difference_L2_Source.v1",
            "must_supply": [
                "a source axiom or derived selector that the visible ordered L source is a terminal monad difference L_i-K2",
                "the ordered sign/base convention binding L3-K2 to Appell-Humbert/Cech transitions",
                "neutral Pic0 selection, or a theorem quotienting Pic0 from the physical source",
                "typed f_i,g_i sections or equivalent transition/rho_E data for the monad lane",
                "a same-source path into Ext promotion, stability/HYM, D_E, dotD, Riesz, and Green data",
            ],
            "after_success": [
                "rerun the strict ordered-source validator as selected data",
                "promote the h1=8 nonzero Ext packet",
                "derive same-source selected operator and response matrices",
            ],
        },
        "guardrails": {
            "claims_unconditional_selected_source_proved": unconditional_selected_source_proved,
            "claims_current_corpus_selects_L3_minus_K2": False,
            "claims_pic0_resolved_now": False,
            "claims_printed_monad_is_whole_visible_c2_source": False,
            "claims_full_SM_closure": False,
            "uses_observed_flavor_data": False,
            "uses_benchmark_flavor_entries": False,
        },
        "verdict": {
            "honest_answer": (
                "The strongest current proof is conditional but sharp: if the selected "
                "visible ordered source is the terminal monad-difference lane, then "
                "L3-K2 is forced uniquely. The unconditional selection theorem is "
                "still open because the corpus has not supplied the lane selector, "
                "Pic0 rule, or typed transition/section data."
            ),
            "next_packet": "Selected_Monad_Difference_L2_Source.v1 with source-lane selector and Pic0 rule",
        },
    }


def main() -> int:
    report = analyze()
    write_json(CANDIDATE, report)
    certificate = {
        "certificate": "SelectedMonadDifferenceL2SourceProofAttempt",
        "status": report["status"],
        "analysis_script": report["generated_by"],
        "candidate_data": "candidate_data/selected_monad_difference_l2_source_proof_attempt.candidate.json",
        "input_certificates": report["input_certificates"],
        "input_statuses": report["input_statuses"],
        "terminal_monad_difference_scan": report["terminal_monad_difference_scan"],
        "conditional_uniqueness_theorem": report["conditional_uniqueness_theorem"],
        "sufficiency_import": report["sufficiency_import"],
        "unconditional_selection_attempt": report["unconditional_selection_attempt"],
        "cross_repo_consistency": report["cross_repo_consistency"],
        "what_this_closes": report["what_this_closes"],
        "what_this_does_not_close": report["what_this_does_not_close"],
        "minimal_success_contract": report["minimal_success_contract"],
        "guardrails": report["guardrails"],
        "verdict": report["verdict"],
    }
    write_json(CERTIFICATE, certificate)
    print(json.dumps(report, indent=2, sort_keys=True))
    return (
        0
        if report["status"]
        == "SELECTED_MONAD_DIFFERENCE_L2_SOURCE_CONDITIONAL_UNIQUENESS_PROVED_SELECTION_OPEN"
        else 1
    )


if __name__ == "__main__":
    raise SystemExit(main())
