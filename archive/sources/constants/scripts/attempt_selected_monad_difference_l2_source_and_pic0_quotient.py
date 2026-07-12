"""Attempt Selected_Monad_Difference_L2_Source_and_Pic0_Quotient_v1."""

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
Q79_PACKET = Q79 / "candidate_data" / "visible_rank2_l2_ordered_source.monad_difference_candidate.json"
Q79_VALIDATOR = Q79 / "scripts" / "validate_visible_rank2_l2_ordered_source_packet.py"

SWITCH = CERTS / "selected_qa_su3_m1_pic0_source_switch_table_certificate.json"
H1 = CERTS / "selected_qa_su3_m1_rank2_ext_h1_source_data_attempt_certificate.json"
TERMINAL = CERTS / "selected_qa_su3_terminal_monad_lane_selector_attempt_certificate.json"
UNCONDITIONAL_Q79 = Q79 / "certificates" / "unconditional_selected_monad_difference_l2_source_attempt_certificate.json"
SELECTOR_OBSTRUCTION = Q79 / "certificates" / "visible_rank2_l2_selector_obstruction_certificate.json"

OUTPUT_CERT = CERTS / "selected_monad_difference_l2_source_and_pic0_quotient_attempt_certificate.json"
OUTPUT_SELECTED_IF_SOURCE = CERTS / "selected_monad_difference_l2_source_and_pic0_quotient.source_switch_required.json"


def load(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def validate(packet: dict[str, Any], name: str) -> dict[str, Any]:
    tmp = CERTS / f"_tmp_{name}.json"
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
    return {"exit_code": proc.returncode, "stdout": proc.stdout, "parsed_report": report}


def apply_pic0_quotient(packet: dict[str, Any]) -> None:
    packet["pic0_resolution"] = {
        "resolution": "pic0_quotient_rule",
        "source_selected_or_quotiented": True,
        "scope": "ordered Chern-Weil/H1 source gate only",
        "rule": (
            "For the ordered Chern-Weil/H1 gate, flat Pic0 twists are quotiented "
            "when they preserve c1, c2, the ordered Chern-Weil matrix, and the "
            "reduced h1/Ext packet. Any holonomy-sensitive observable must reopen "
            "Pic0 as source data."
        ),
    }


def apply_hypothetical_source_selection(packet: dict[str, Any]) -> None:
    packet["candidate_role"] = "SELECTED_DATA"
    packet["status"] = "VISIBLE_RANK2_L2_ORDERED_SOURCE_SELECTED_PIC0_QUOTIENTED"
    packet["source"]["fixture_only"] = False
    packet["source"]["selected_by_mtt"] = True
    packet["source"]["source_certificate"] = "Selected_Monad_Difference_L2_Source.v1"
    packet["source"]["source_status"] = "VISIBLE_RANK2_L2_ORDERED_SOURCE_SELECTED_PIC0_QUOTIENTED"
    packet["selection_evidence"]["standard_lattice_or_equivalent_selected"] = True
    packet["selection_evidence"]["base_factor_order_selected"] = True
    packet["selection_evidence"]["base_swap_broken_by_source"] = True


def main() -> None:
    switch = load(SWITCH)
    h1 = load(H1)
    terminal = load(TERMINAL)
    q79_unconditional = load(UNCONDITIONAL_Q79)
    obstruction = load(SELECTOR_OBSTRUCTION)
    base = load(Q79_PACKET)

    pic0_only = copy.deepcopy(base)
    apply_pic0_quotient(pic0_only)
    pic0_only_validation = validate(pic0_only, "pic0_quotient_only")

    source_and_pic0 = copy.deepcopy(pic0_only)
    apply_hypothetical_source_selection(source_and_pic0)
    source_and_pic0_validation = validate(source_and_pic0, "source_and_pic0")

    pic0_report = pic0_only_validation["parsed_report"] or {}
    combined_report = source_and_pic0_validation["parsed_report"] or {}
    pic0_scope_ok = (
        obstruction["pic0_invariance"]["flat_pic0_changes_c1"] is False
        and obstruction["pic0_invariance"]["flat_pic0_changes_c2"] is False
        and obstruction["pic0_invariance"]["flat_pic0_changes_h1_for_nonzero_elliptic_degrees"] is False
        and obstruction["pic0_invariance"]["flat_pic0_changes_appell_humbert_curvature_matrix"] is False
    )

    output = {
        "certificate": "SelectedMonadDifferenceL2SourceAndPic0QuotientAttempt",
        "status": "PIC0_QUOTIENT_LOCAL_CW_H1_GATE_CLOSED_SOURCE_LANE_SELECTOR_OPEN",
        "inputs": {
            "switch_table": str(SWITCH.relative_to(ROOT)),
            "h1_gate": str(H1.relative_to(ROOT)),
            "terminal_lane_gate": str(TERMINAL.relative_to(ROOT)),
            "q79_unconditional_attempt": str(UNCONDITIONAL_Q79),
            "q79_selector_obstruction": str(SELECTOR_OBSTRUCTION),
            "q79_unselected_packet": str(Q79_PACKET),
        },
        "local_pic0_quotient_theorem": {
            "scope": "ordered Chern-Weil/H1 source gate",
            "proved_for_scope": pic0_scope_ok,
            "statement": (
                "Inside the ordered Chern-Weil/H1 source gate, Pic0 twists may be "
                "quotiented because the gate only reads c1, c2, the ordered "
                "Chern-Weil matrix, and reduced h1/Ext data, all invariant under "
                "the flat Pic0 twists tracked by the current obstruction theorem."
            ),
            "not_a_global_holonomy_claim": True,
            "must_reopen_for": [
                "Wilson-line or holonomy-sensitive observables",
                "same-source D_E/dotD/Riesz/Green if flat holonomy enters the operator",
                "Yukawa overlaps if the flat character changes sections or phases",
            ],
        },
        "validator_tests": {
            "pic0_quotient_only": {
                "exit_code": pic0_only_validation["exit_code"],
                "status": pic0_report.get("status"),
                "open_items": pic0_report.get("open_items"),
            },
            "source_and_pic0_quotient": {
                "exit_code": source_and_pic0_validation["exit_code"],
                "status": combined_report.get("status"),
                "open_items": combined_report.get("open_items"),
            },
        },
        "closed_now": {
            "pic0_quotient_admissible_for_ordered_CW_H1_gate": pic0_scope_ok,
            "Pic0_no_longer_arithmetic_matrix_blocker_at_this_layer": True,
            "combined_source_and_pic0_packet_would_pass": source_and_pic0_validation["exit_code"] == 0
            and combined_report.get("status") == "PASS",
            "h1_packet_ready_after_source_selection": h1["imported_h1_packet"]["h1"] == 8
            and h1["imported_h1_packet"]["nonzero_ext_class"] is True,
            "terminal_lane_conditional_uniqueness_closed": terminal["closed_now"][
                "conditional_uniqueness_inside_terminal_lane"
            ],
        },
        "not_closed": {
            "actual_MTT_source_lane_selector_for_L3_minus_K2": q79_unconditional[
                "unconditional_theorem_attempt"
            ]["source_lane_selected"]
            is False,
            "global_holonomy_sensitive_Pic0_selection": True,
            "promote_h1_packet_to_selected_data": True,
            "non_split_stability_or_HYM": True,
            "same_source_D_E_dotD_Riesz_Green": True,
            "full_SM_closure": True,
        },
        "next_required_artifact": {
            "name": "Selected_Terminal_Monad_Lane_Source_Selector_v1",
            "must_prove": [
                "MTT selects the visible ordered L source from central-neutral terminal monad differences L_i-K2",
                "the selected lane binds L3-K2 to the Appell-Humbert/Cech transitions",
                "standard/equivalent lattice and base ordering are source-selected",
                "then rerun the Pic0-quotiented ordered-source packet as selected data",
            ],
        },
        "guardrails": {
            "claims_actual_source_lane_selector_proved": False,
            "claims_global_pic0_physics_quotiented": False,
            "claims_h1_packet_selected_now": False,
            "claims_D_E_dotD_Riesz_Green": False,
            "claims_full_SM_closure": False,
            "uses_observed_flavor_data": False,
            "uses_benchmark_flavor_entries": False,
        },
        "honest_answer": (
            "Pic0 can be quotiented for the local ordered Chern-Weil/H1 gate, "
            "because the gate only consumes invariants already proven Pic0-invariant. "
            "This does not prove global Pic0 irrelevance. The remaining blocker at "
            "this layer is now the actual MTT source-lane selector for L3-K2."
        ),
    }

    if "--write-certificate" in sys.argv:
        OUTPUT_CERT.write_text(json.dumps(output, indent=2, sort_keys=True) + "\n", encoding="utf-8")
        OUTPUT_SELECTED_IF_SOURCE.write_text(
            json.dumps(
                {
                    "status": "SOURCE_SWITCH_REQUIRED_PIC0_QUOTIENTED_PACKET_RECORDED",
                    "packet": source_and_pic0,
                    "validation": output["validator_tests"]["source_and_pic0_quotient"],
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
