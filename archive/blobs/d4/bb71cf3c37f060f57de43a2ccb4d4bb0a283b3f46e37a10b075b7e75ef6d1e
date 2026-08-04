"""Audit the terminal-monad matter-slot source-selector reduction."""

from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SCRIPT = ROOT / "scripts" / "build_selected_terminalmonad_matterslot_sectionring_source_selector.py"
CANDIDATE = ROOT / "candidate_data" / "selected_terminalmonad_matterslot_sectionring_source_selector.candidate.json"
CERT = ROOT / "certificates" / "selected_terminalmonad_matterslot_sectionring_source_selector_certificate.json"
NOTE = ROOT / "proof_corpus" / "MTT_Selected_TerminalMonad_MatterSlot_SectionRing_SourceSelector_v1.md"

STATUS = "MTT_SELECTED_TERMINALMONAD_MATTERSLOT_SECTIONRING_SELECTOR_REDUCED_TO_SOURCE_BASEORDER_AND_SLOTMAP"
NEXT = "MTT_Selected_TerminalMonad_BaseOrder_AHBinding_SMSlotMap_v1"


def check(name: str, condition: bool, detail: object) -> bool:
    print(("PASS" if condition else "FAIL") + f": {name} -- {detail}")
    return condition


def main() -> int:
    proc = subprocess.run(
        [sys.executable, str(SCRIPT)],
        cwd=ROOT,
        text=True,
        stdout=subprocess.PIPE,
        stderr=subprocess.STDOUT,
    )
    if proc.returncode != 0:
        print(proc.stdout)
        return 1

    data = json.loads(CANDIDATE.read_text(encoding="utf-8"))
    cert = json.loads(CERT.read_text(encoding="utf-8"))
    note = NOTE.read_text(encoding="utf-8")

    source = data["source_switch_contract"]
    pic0 = data["pic0_accounting"]
    switches = data["two_switch_reduction"]
    slot_map = data["matter_slot_map_contract"]
    closes = data["what_closes_now"]
    remains = data["what_remains_open"]

    tests = [
        check("status", data["status"] == STATUS and cert["status"] == STATUS, data["status"]),
        check(
            "superset strategy is guarded",
            data["superset_strategy"]["using_one_straight_path"] is False
            and data["superset_strategy"]["observed_data_used"] is False
            and data["superset_strategy"]["target_fitting_used"] is False
            and "no C1 columns" in data["superset_strategy"]["locked_or_constrained_target_role"],
            data["superset_strategy"],
        ),
        check(
            "L3-K2 candidate fixed",
            source["central_neutral_member"]["closed"] is True
            and source["central_neutral_member"]["forced_label"] == "L3-K2"
            and source["central_neutral_member"]["forced_value"] == [1, -2, 0]
            and source["central_neutral_member"]["forced_double"] == [2, -4, 0]
            and source["monad_orientation"]["ordered_difference"] == "L3_minus_K2",
            source,
        ),
        check(
            "source switch remains honest",
            source["terminal_monad_lane_selection"]["closed"] is False
            and source["standard_lattice_or_equivalent"]["closed"] is False
            and source["base_factor_order"]["closed"] is False
            and source["AH_or_Cech_binding"]["support_closed"] is True
            and source["AH_or_Cech_binding"]["closed"] is False,
            source,
        ),
        check(
            "ordered Pic0 closed only at ordered layer",
            pic0["ordered_layer_pic0_closed"] is True
            and pic0["ordered_layer_validator_after_quotient"]["pic0_items_absent"] is True
            and pic0["ordered_layer_validator_after_quotient"]["only_source_selection_items_remain"] is True
            and pic0["operator_layer_pic0_closed"] is False,
            pic0,
        ),
        check(
            "switch table imported and reduced",
            switches["pic0_only_fails_only_source_switch"] is True
            and switches["source_only_fails_only_pic0_switch"] is True
            and switches["source_and_pic0_passes_ordered_validator"] is True
            and switches["ordered_pic0_quotient_removes_pic0_switch_at_ordered_layer"] is True,
            switches,
        ),
        check(
            "matter slot map contract built but open",
            slot_map["closed"] is False
            and slot_map["must_map_without_locked_C1_columns"]["10_M_clock"] == ["u", "e"]
            and slot_map["must_map_without_locked_C1_columns"]["bar5_M_shift"] == ["d"]
            and slot_map["must_map_without_locked_C1_columns"]["1_M_Dirac_shift"] == ["nuD"]
            and slot_map["must_preserve_q79_polarization"]["U_10"] == "I_3",
            slot_map,
        ),
        check(
            "closure/remainder accounting",
            closes["ordered_layer_Pic0_removed_as_ordered_source_blocker"] is True
            and closes["terminal_selector_reduced_to_source_baseorder_AHbinding"] is True
            and remains["terminal_monad_lane_selected_by_MTT"] is True
            and remains["section_ring_to_SU5_E6_matter_slot_map"] is True
            and remains["operator_layer_Pic0_selection_or_quotient"] is True,
            {"closes": closes, "remains": remains},
        ),
        check(
            "no closure or target fitting",
            data["closure_claimed"] is False
            and cert["closure_claimed"] is False
            and data["target_fitting_used"] is False
            and data["observed_data_used"] is False
            and cert["target_fitting_used"] is False,
            cert,
        ),
        check(
            "theorem and next gate recorded",
            data["theorem"]["proved"] is True
            and data["next_required_artifact"] == NEXT
            and cert["next_required_artifact"] == NEXT
            and f"Next artifact: `{NEXT}`" in note,
            NOTE,
        ),
    ]

    print("\nMTT terminal-monad matter-slot source-selector audit")
    return 0 if all(tests) else 1


if __name__ == "__main__":
    sys.exit(main())
