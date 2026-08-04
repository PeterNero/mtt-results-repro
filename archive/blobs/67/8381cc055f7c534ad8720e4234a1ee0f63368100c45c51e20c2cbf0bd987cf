"""Import and test the selected Qa/SU3 m=1 rank-two Ext H1 source data gate."""

from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
CERTS = ROOT / "certificates"
Q79 = Path(r"C:\Users\nero_\Downloads\TEXPAPERS\mtt-q79-proof-repro")
Q79_CERTS = Q79 / "certificates"
Q79_DATA = Q79 / "candidate_data"
Q79_VALIDATOR = Q79 / "scripts" / "validate_visible_rank2_l2_cohomology.py"

CW_ATTEMPT = CERTS / "selected_qa_su3_m1_cw_operator_source_attempt_certificate.json"
PULLBACK_PACKET = Q79_DATA / "visible_rank2_l2_pullback_cech_attempt.cohomology.json"
PULLBACK_CERT = Q79_CERTS / "visible_rank2_l2_pullback_cech_attempt_certificate.json"
ORDERED_GATE = Q79_CERTS / "visible_rank2_l2_ordered_source_promotion_gate_certificate.json"
SELECTOR_OBSTRUCTION = Q79_CERTS / "visible_rank2_l2_selector_obstruction_certificate.json"
MONAD_CANDIDATE = Q79_CERTS / "iwasawa_monad_l2_branch_orientation_candidate_certificate.json"

OUTPUT_CERT = CERTS / "selected_qa_su3_m1_rank2_ext_h1_source_data_attempt_certificate.json"


def load(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def run_q79_h1_validator(packet: Path) -> dict[str, Any]:
    proc = subprocess.run(
        [sys.executable, str(Q79_VALIDATOR), str(packet)],
        cwd=Q79,
        text=True,
        stdout=subprocess.PIPE,
        stderr=subprocess.STDOUT,
        check=False,
    )
    report = None
    for line in proc.stdout.splitlines():
        if line.startswith("visible_rank2_l2_h1_report="):
            report = json.loads(line.split("=", 1)[1])
    return {"exit_code": proc.returncode, "stdout": proc.stdout, "parsed_report": report}


def main() -> None:
    cw = load(CW_ATTEMPT)
    packet = load(PULLBACK_PACKET)
    pullback = load(PULLBACK_CERT)
    ordered = load(ORDERED_GATE)
    obstruction = load(SELECTOR_OBSTRUCTION)
    monad = load(MONAD_CANDIDATE)
    validation = run_q79_h1_validator(PULLBACK_PACKET)

    h1_report = validation["parsed_report"] or {}
    monad_key = monad["key_candidate"]

    output = {
        "certificate": "SelectedQaSU3M1Rank2ExtH1SourceDataAttempt",
        "status": "QA_SU3_M1_RANK2_EXT_H1_CONDITIONAL_PACKET_IMPORTED_SELECTION_OPEN",
        "inputs": {
            "current_cw_operator_source_attempt": str(CW_ATTEMPT.relative_to(ROOT)),
            "q79_pullback_cohomology_packet": str(PULLBACK_PACKET),
            "q79_pullback_certificate": str(PULLBACK_CERT),
            "q79_ordered_source_promotion_gate": str(ORDERED_GATE),
            "q79_selector_obstruction": str(SELECTOR_OBSTRUCTION),
            "q79_monad_branch_orientation_candidate": str(MONAD_CANDIDATE),
        },
        "imported_h1_packet": {
            "candidate_role": packet["candidate_role"],
            "source_selected_by_mtt": packet["source"]["selected_by_mtt"],
            "fixture_only": packet["source"]["fixture_only"],
            "target": packet["target"],
            "dimensions": h1_report.get("dimensions"),
            "h1": h1_report.get("h1"),
            "rank_d0": h1_report.get("rank_d0"),
            "rank_d1": h1_report.get("rank_d1"),
            "d1_d0_zero": h1_report.get("d1_d0_zero"),
            "nonzero_ext_class": h1_report.get("nonzero_ext_class"),
            "promotes_to_non_split_V_alpha_input": h1_report.get(
                "promotes_to_non_split_V_alpha_input"
            ),
            "validator_exit_code": validation["exit_code"],
        },
        "what_this_closes_conditionally": {
            "finite_Cech_Kunneth_H1_packet_exists": pullback["what_this_closes"][
                "conditional_h1_positive_for_base_pullback_model"
            ],
            "d1_d0_zero_and_h1_8_checked": validation["exit_code"] == 0
            and h1_report.get("d1_d0_zero") is True
            and h1_report.get("h1") == 8,
            "closed_nonexact_ext_vector_exists_in_fixture": h1_report.get(
                "nonzero_ext_class"
            )
            is True,
            "ordered_integral_monad_difference_candidate_found": monad[
                "what_this_closes"
            ]["exact_ordered_integral_target_L_candidate_found"],
            "monad_difference_matches_target_L": monad_key["matches_target_L"]
            and monad_key["matches_target_L2_after_doubling"],
        },
        "why_it_still_does_not_promote": {
            "packet_is_unselected_fixture": packet["candidate_role"] == "UNSELECTED_FIXTURE",
            "validator_refuses_selected_promotion": h1_report.get(
                "promotes_to_non_split_V_alpha_input"
            )
            is False,
            "ordered_source_gate_open_items": ordered["validation_results"][
                "current_appell_humbert_attempt"
            ]["parsed_report"]["open_items"],
            "selector_obstruction_theorem": obstruction["obstruction_theorem"]["theorem"],
            "pic0_needs_source_or_gauge_fixing": obstruction["pic0_invariance"][
                "needs_holonomy_sensitive_source_or_gauge_fixing"
            ],
        },
        "source_selector_options_now": [
            {
                "route": "monad_difference_L3_minus_K2",
                "status": "BEST_LIVE_SELECTION_HANDLE",
                "evidence": {
                    "ordered_difference": monad_key["ordered_difference"],
                    "value": monad_key["value"],
                    "double_value": monad_key["double_value"],
                    "unique_double_target_match": monad["ordered_difference_scan"][
                        "differences_whose_double_is_target_L2"
                    ],
                },
                "must_prove_next": [
                    "L3-K2 is selected as the visible V_alpha extension source slot.",
                    "The monad difference binds to the Appell-Humbert/Cech transitions.",
                    "Pic0 is either quotiented or neutral-character selected by source data.",
                ],
            },
            {
                "route": "same_source_D_E_dotD_Hessian",
                "status": "PARALLEL_HARD_EXIT",
                "evidence": obstruction["obstruction_theorem"][
                    "does_not_apply_if_new_source_supplies"
                ],
                "must_prove_next": [
                    "The same source orders the two base factors.",
                    "The source supplies D_E/Riesz/Green/dotD rather than only topology.",
                ],
            },
            {
                "route": "selected_Gauduchon_wall",
                "status": "LIVE_BUT_NO_CURRENT_SOURCE",
                "must_prove_next": [
                    "MTT selects r1:r2=sqrt(2):1 on this branch.",
                    "The selected wall is tied to the visible L2 source.",
                ],
            },
        ],
        "relation_to_cw_source_attempt": {
            "previous_next_object": cw["next_object"]["name"],
            "this_attempt_fills": [
                "actual finite h1 value for the pullback fixture",
                "actual closed non-exact Ext vector for the pullback fixture",
                "explicit reason this remains conditional rather than selected",
            ],
            "first_remaining_required_theorem": (
                "Selected_Monad_Difference_L2_Source_or_Pic0_Quotient_Theorem_v1"
            ),
        },
        "guardrails": {
            "claims_selected_h1_source_data": False,
            "claims_selected_nonzero_Ext_class": False,
            "claims_non_split_stability": False,
            "claims_D_E_dotD_Riesz_Green": False,
            "claims_full_SM_closure": False,
            "uses_observed_flavor_data": False,
            "uses_benchmark_flavor_entries": False,
        },
        "honest_answer": (
            "The finite H1 computation is no longer the numerical blocker: the "
            "pullback Cech/Kunneth packet has h1=8 and a closed non-exact Ext "
            "class. The true blocker is source selection. The best current path "
            "is to prove that the monad-difference lane L3-K2 selects the ordered "
            "Appell-Humbert/Cech representative, with Pic0 quotiented or fixed by "
            "source data."
        ),
    }

    text = json.dumps(output, indent=2, sort_keys=True)
    if "--write-certificate" in sys.argv:
        OUTPUT_CERT.write_text(text + "\n", encoding="utf-8")
    print(text)


if __name__ == "__main__":
    main()
