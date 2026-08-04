"""Build the Pic0/source-selection switch table for the Qa/SU3 m=1 L2 gate."""

from __future__ import annotations

import copy
import json
import subprocess
import sys
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
CERTS = ROOT / "certificates"
Q79 = Path(r"C:\Users\nero_\Downloads\TEXPAPERS\mtt-q79-proof-repro")
Q79_CANDIDATE = Q79 / "candidate_data" / "visible_rank2_l2_ordered_source.monad_difference_candidate.json"
Q79_VALIDATOR = Q79 / "scripts" / "validate_visible_rank2_l2_ordered_source_packet.py"

H1_GATE = CERTS / "selected_qa_su3_m1_rank2_ext_h1_source_data_attempt_certificate.json"
MONAD_GATE = CERTS / "selected_qa_su3_monad_difference_l2_source_attempt_certificate.json"
TERMINAL_GATE = CERTS / "selected_qa_su3_terminal_monad_lane_selector_attempt_certificate.json"

OUTPUT_CERT = CERTS / "selected_qa_su3_m1_pic0_source_switch_table_certificate.json"
OUTPUT_CANDIDATE = CERTS / "selected_qa_su3_m1_pic0_source_switch_table.candidates.json"


def load(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def selected_source_patch(packet: dict[str, Any]) -> None:
    packet["candidate_role"] = "SELECTED_DATA"
    packet["status"] = "VISIBLE_RANK2_L2_ORDERED_SOURCE_SELECTED"
    packet["source"]["fixture_only"] = False
    packet["source"]["selected_by_mtt"] = True
    packet["source"]["source_certificate"] = "Selected_Monad_Difference_L2_Source.v1"
    packet["source"]["source_status"] = "VISIBLE_RANK2_L2_ORDERED_SOURCE_SELECTED"
    packet["selection_evidence"]["standard_lattice_or_equivalent_selected"] = True
    packet["selection_evidence"]["base_factor_order_selected"] = True
    packet["selection_evidence"]["base_swap_broken_by_source"] = True


def pic0_quotient_patch(packet: dict[str, Any]) -> None:
    packet["pic0_resolution"] = {
        "resolution": "pic0_quotient_rule",
        "source_selected_or_quotiented": True,
        "rule": (
            "Flat Pic0 characters are quotiented for this ordered Chern-class "
            "source gate when they leave c1, c2, the reduced h1 packet, and the "
            "Chern-Weil curvature row unchanged. Holonomy-sensitive observables "
            "must reopen this rule."
        ),
    }
    if packet["source"].get("source_status") == "VISIBLE_RANK2_L2_ORDERED_SOURCE_SELECTED":
        packet["source"]["source_status"] = "VISIBLE_RANK2_L2_ORDERED_SOURCE_SELECTED_PIC0_QUOTIENTED"
        packet["status"] = "VISIBLE_RANK2_L2_ORDERED_SOURCE_SELECTED_PIC0_QUOTIENTED"


def validate(packet: dict[str, Any], name: str) -> dict[str, Any]:
    tmp = ROOT / "certificates" / f"_tmp_{name}.json"
    tmp.write_text(json.dumps(packet, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    try:
        proc = subprocess.run(
            [sys.executable, str(Q79_VALIDATOR), str(tmp)],
            cwd=Q79,
            text=True,
            stdout=subprocess.PIPE,
            stderr=subprocess.STDOUT,
            check=False,
        )
    finally:
        try:
            tmp.unlink()
        except OSError:
            pass

    report = None
    for line in proc.stdout.splitlines():
        if line.startswith("visible_rank2_l2_ordered_source_validation_report="):
            report = json.loads(line.split("=", 1)[1])
    return {
        "exit_code": proc.returncode,
        "stdout": proc.stdout,
        "parsed_report": report,
    }


def variant(base: dict[str, Any], source: bool, pic0: bool) -> dict[str, Any]:
    packet = copy.deepcopy(base)
    if source:
        selected_source_patch(packet)
    if pic0:
        pic0_quotient_patch(packet)
    return packet


def main() -> None:
    base = load(Q79_CANDIDATE)
    h1 = load(H1_GATE)
    monad = load(MONAD_GATE)
    terminal = load(TERMINAL_GATE)

    cases = []
    for name, source, pic0 in [
        ("none", False, False),
        ("pic0_only", False, True),
        ("source_only", True, False),
        ("source_and_pic0", True, True),
    ]:
        packet = variant(base, source=source, pic0=pic0)
        result = validate(packet, name)
        cases.append(
            {
                "case": name,
                "source_switch": source,
                "pic0_switch": pic0,
                "validator_exit_code": result["exit_code"],
                "validator_status": (result["parsed_report"] or {}).get("status"),
                "open_items": (result["parsed_report"] or {}).get("open_items"),
                "failures": (result["parsed_report"] or {}).get("failures"),
            }
        )

    case_by_name = {case["case"]: case for case in cases}
    output = {
        "certificate": "SelectedQaSU3M1Pic0SourceSwitchTable",
        "status": "QA_SU3_M1_PIC0_SOURCE_SWITCH_TABLE_BUILT_BOTH_SWITCHES_REQUIRED",
        "inputs": {
            "q79_unselected_monad_difference_packet": str(Q79_CANDIDATE),
            "q79_ordered_source_validator": str(Q79_VALIDATOR),
            "h1_gate": str(H1_GATE.relative_to(ROOT)),
            "monad_difference_gate": str(MONAD_GATE.relative_to(ROOT)),
            "terminal_lane_gate": str(TERMINAL_GATE.relative_to(ROOT)),
        },
        "switch_table": cases,
        "what_this_closes": {
            "pic0_is_independent_required_switch": case_by_name["pic0_only"]["validator_exit_code"] == 2
            and "source.selected_by_mtt is not true" in case_by_name["pic0_only"]["open_items"],
            "source_selection_is_independent_required_switch": case_by_name["source_only"]["validator_exit_code"] == 2
            and "Pic0 resolution rule missing" in case_by_name["source_only"]["open_items"],
            "both_switches_suffice_for_ordered_source_validator": case_by_name["source_and_pic0"][
                "validator_exit_code"
            ]
            == 0,
            "h1_packet_ready_after_ordered_source_success": h1["imported_h1_packet"]["h1"] == 8
            and h1["imported_h1_packet"]["nonzero_ext_class"] is True,
            "terminal_lane_conditional_uniqueness_already_closed": terminal["closed_now"][
                "conditional_uniqueness_inside_terminal_lane"
            ],
        },
        "what_this_does_not_close": {
            "actual_source_switch_from_MTT": monad["not_closed"]["actual_MTT_selection_of_L3_minus_K2"],
            "actual_pic0_rule_from_MTT_or_physical_quotient": True,
            "non_split_stability": True,
            "same_source_D_E_dotD_Riesz_Green": True,
            "full_SM_closure": True,
        },
        "next_required_artifact": {
            "name": "Selected_Monad_Difference_L2_Source_and_Pic0_Quotient_v1",
            "must_supply": [
                "source selection of the terminal monad lane L3-K2",
                "source-selected or physically justified Pic0 quotient rule",
                "binding to Appell-Humbert/Cech transitions",
                "then rerun h1=8 packet as SELECTED_DATA",
            ],
        },
        "guardrails": {
            "claims_pic0_rule_proved": False,
            "claims_source_selection_proved": False,
            "claims_ordered_source_closed_unconditionally": False,
            "claims_Ext_packet_selected": False,
            "claims_D_E_dotD_Riesz_Green": False,
            "uses_observed_flavor_data": False,
            "uses_benchmark_flavor_entries": False,
        },
        "honest_answer": (
            "The ordered-source gate is now split into two independent switches. "
            "Pic0-only still fails because source selection is open; source-only "
            "still fails because Pic0 is open; both switches together make the "
            "existing ordered packet pass. Thus no further arithmetic matrix is "
            "missing at this layer."
        ),
    }

    if "--write-certificate" in sys.argv:
        OUTPUT_CERT.write_text(json.dumps(output, indent=2, sort_keys=True) + "\n", encoding="utf-8")
        OUTPUT_CANDIDATE.write_text(
            json.dumps(
                {
                    "status": "QA_SU3_M1_PIC0_SOURCE_SWITCH_TABLE_CANDIDATES_RECORDED",
                    "cases": cases,
                },
                indent=2,
                sort_keys=True,
            )
            + "\n",
            encoding="utf-8",
        )
    print(json.dumps(output, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
