"""Audit the matter-slot grading / section-ring readout attempt."""

from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SCRIPT = ROOT / "scripts" / "build_selected_matterslot_grading_or_sectionring_readout.py"
CANDIDATE = ROOT / "candidate_data" / "selected_matterslot_grading_or_sectionring_readout.candidate.json"
CERT = ROOT / "certificates" / "selected_matterslot_grading_or_sectionring_readout_certificate.json"
NOTE = ROOT / "proof_corpus" / "MTT_Selected_MatterSlot_Grading_or_SectionRing_Readout_v1.md"

STATUS = "MTT_SELECTED_MATTERSLOT_GRADING_SECTIONRING_READOUT_ATTEMPT_REDUCED_TO_TERMINAL_MONAD_SELECTOR"
NEXT = "MTT_Selected_TerminalMonad_MatterSlot_SectionRing_SourceSelector_v1"


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
    decision = data["selection_decision"]
    contract = data["terminal_monad_sectionring_contract"]
    routes = data["route_candidates"]
    closes = data["what_closes_now"]
    remains = data["what_remains_open"]

    primary = next(row for row in routes if row["id"] == "typed_monad_cech_sectionring")
    rejected = next(row for row in routes if row["id"] == "locked_c1_inverse_readout")

    tests = [
        check("status", data["status"] == STATUS and cert["status"] == STATUS, data["status"]),
        check(
            "primary route ranked",
            primary["rank"] == 1
            and primary["support_closed"] is True
            and primary["selected_closed"] is False
            and decision["primary_route_selected_for_next_attempt"] == "typed_monad_cech_sectionring",
            primary,
        ),
        check(
            "terminal contract fixed",
            contract["source_selector_to_prove"]["terminal_lane"] == "L_i-K2"
            and contract["source_selector_to_prove"]["forced_label_inside_lane"] == "L3-K2"
            and contract["source_selector_to_prove"]["forced_value"] == [1, -2, 0]
            and contract["source_selector_to_prove"]["forced_double"] == [2, -4, 0],
            contract["source_selector_to_prove"],
        ),
        check(
            "matter grading contract present",
            contract["must_bind_to_matter_slot_grading"]["10_M_clock"] == ["u", "e"]
            and contract["must_bind_to_matter_slot_grading"]["bar5_M_shift"] == ["d"]
            and contract["must_bind_to_matter_slot_grading"]["1_M_Dirac_shift"] == ["nuD"]
            and contract["must_bind_to_matter_slot_grading"]["polarization_output"]["U_10"] == "I_3",
            contract["must_bind_to_matter_slot_grading"],
        ),
        check(
            "support imports closed but grading open",
            decision["central_circle_filter_closed"] is True
            and decision["monad_sufficiency_closed_conditionally"] is True
            and decision["ah_goodcover_equivalence_closed"] is True
            and decision["selected_matter_slot_grading_readout_closed"] is False
            and closes["selected_grading_still_open"] is True,
            decision,
        ),
        check(
            "forbidden target route rejected",
            rejected["rank"] == 99 and rejected["selected_closed"] is False,
            rejected,
        ),
        check(
            "open selector fields retained",
            remains["selected_terminal_monad_lane_source_selector"] is False
            and remains["selected_lattice_and_base_factor_order"] is True
            and remains["operator_layer_Pic0_selection_or_quotient"] is True
            and remains["section_ring_to_SU5_E6_matter_slot_map"] is True,
            remains,
        ),
        check(
            "no closure or fitting",
            data["closure_claimed"] is False
            and cert["closure_claimed"] is False
            and data["target_fitting_used"] is False
            and cert["target_fitting_used"] is False,
            cert,
        ),
        check(
            "next gate recorded",
            data["next_required_artifact"] == NEXT
            and cert["next_required_artifact"] == NEXT
            and f"Next artifact: `{NEXT}`" in note
            and "terminal monad lane" in note,
            NOTE,
        ),
    ]

    print("\nMTT selected matter-slot grading / section-ring readout audit")
    return 0 if all(tests) else 1


if __name__ == "__main__":
    sys.exit(main())
