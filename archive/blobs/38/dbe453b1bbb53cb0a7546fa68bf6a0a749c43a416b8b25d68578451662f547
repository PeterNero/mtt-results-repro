"""Audit the selected matter-slot transversality readout attempt."""

from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SCRIPT = ROOT / "scripts" / "build_selected_matterslot_transversality_readout_functional.py"
CANDIDATE = ROOT / "candidate_data" / "selected_matterslot_transversality_readout_functional.candidate.json"
CERT = ROOT / "certificates" / "selected_matterslot_transversality_readout_functional_certificate.json"
NOTE = ROOT / "proof_corpus" / "MTT_Selected_MatterSlot_Transversality_Readout_Functional_v1.md"

STATUS = "MTT_SELECTED_MATTERSLOT_TRANSVERSALITY_READOUT_FUNCTIONAL_ATTEMPT_RHOS_INVARIANT_NOGO_GRADING_OPEN"
NEXT = "MTT_Selected_MatterSlot_Grading_or_SectionRing_Readout_v1"


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
    rho = data["rho_s_invariant_test"]
    decision = data["selected_functional_decision"]
    readouts = data["candidate_readouts_tested"]
    next_readout = data["required_next_readout"]
    selection = data["selection_decision"]
    closes = data["what_closes_now"]

    legal_distinguishers = [
        row for row in readouts
        if row["allowed_as_selected_source"] and row["available_now"] and row["distinguishes_required_partition"]
    ]
    forbidden_distinguishers = [
        row for row in readouts
        if not row["allowed_as_selected_source"] and row["distinguishes_required_partition"]
    ]

    tests = [
        check("status", data["status"] == STATUS and cert["status"] == STATUS, data["status"]),
        check(
            "rho_s invariants uniform",
            rho["all_matter_rho_matrices_identical"] is True
            and rho["all_matter_maps_use_same_adjoint_matrices"] is True
            and rho["conditional_gram_forces_common_I3"] is True,
            rho,
        ),
        check(
            "no legal readout closes",
            decision["domain_source_closed"] is True
            and decision["selected_readout_functional_emitted"] is False
            and legal_distinguishers == [],
            {"decision": decision, "legal_distinguishers": legal_distinguishers},
        ),
        check(
            "forbidden distinguishers rejected",
            len(forbidden_distinguishers) == 2
            and closes["locked_c1_target_rejected_as_source_selector"] is True,
            forbidden_distinguishers,
        ),
        check(
            "no selected overclaim",
            selection["selected_matter_slot_transversality_readout_functional_closed"] is False
            and selection["selected_U10_Ubar5_polarization_closed"] is False
            and selection["selected_1M_Dirac_neutrino_source_rule_closed"] is False
            and data["closure_claimed"] is False
            and cert["closure_claimed"] is False,
            selection,
        ),
        check(
            "next grading contract",
            next_readout["name"] == "SelectedMatterSlotGradingOrSectionRingReadout"
            and next_readout["must_emit"]["matter_slot_grading"]["10_M"] == ["u", "e"]
            and next_readout["must_emit"]["matter_slot_grading"]["bar5_M"] == ["d"]
            and next_readout["must_emit"]["matter_slot_grading"]["1_M_Dirac"] == ["nuD"]
            and "line-bundle section-ring degree readout" in next_readout["allowed_source_types"],
            next_readout,
        ),
        check(
            "next gate recorded",
            data["next_required_artifact"] == NEXT
            and cert["next_required_artifact"] == NEXT
            and f"Next artifact: `{NEXT}`" in note
            and "SelectedMatterSlotGradingOrSectionRingReadout" in note,
            NOTE,
        ),
    ]

    print("\nMTT selected matter-slot transversality readout audit")
    return 0 if all(tests) else 1


if __name__ == "__main__":
    sys.exit(main())
