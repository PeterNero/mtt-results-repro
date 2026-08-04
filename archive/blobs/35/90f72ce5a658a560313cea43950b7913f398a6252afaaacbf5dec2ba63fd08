"""Audit same-branch U10/Ubar5/1_M source emission attempt."""

from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SCRIPT = ROOT / "scripts" / "build_selected_u10ubar5_1m_samebranch_emission_attempt.py"
CANDIDATE = ROOT / "candidate_data" / "selected_u10ubar5_1m_samebranch_emission_attempt.candidate.json"
CERT = ROOT / "certificates" / "selected_u10ubar5_1m_samebranch_emission_attempt_certificate.json"
NOTE = ROOT / "proof_corpus" / "MTT_Selected_U10Ubar5_1M_SourcePromotion_SameBranch_Emission_v1.md"

STATUS = "MTT_SELECTED_U10UBAR5_1M_SAMEBRANCH_EMISSION_ATTEMPT_REDUCED_TO_MATTERSLOT_TRANSVERSALITY_READOUT"
NEXT = "MTT_Selected_MatterSlot_Transversality_Readout_Functional_v1"


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
    stationary = data["stationary_selected_source"]
    readout = data["readout_tests"]
    decision = data["selection_decision"]
    contract = data["minimal_readout_contract"]
    remains = data["what_remains_open"]
    support = data["finite_su5_support"]

    tests = [
        check("status", data["status"] == STATUS and cert["status"] == STATUS, data["status"]),
        check(
            "stationary selected source imported",
            cert["stationary_selected_source_closed"] is True
            and decision["selected_stationary_source_available"] is True
            and stationary["selected_source_verified"] is True
            and stationary["selected_rho_s_validator_ready"] is True
            and stationary["functional_rho_s_promotion"] is True,
            stationary,
        ),
        check(
            "finite support retained",
            support["finite_transversality_theorem_closed"] is True
            and support["retarded_q79_orientation_closed"] is True
            and support["U_10"] == "I_3"
            and support["U_bar5"] == "F",
            support,
        ),
        check(
            "readout still missing",
            readout["selected_source_can_emit_generic_rho_s"] is True
            and readout["selected_source_emits_matter_slot_transversality_functional"] is False
            and readout["selected_source_distinguishes_10M_clock_from_bar5M_shift"] is False
            and readout["selected_source_attaches_1M_to_Dirac_shift_channel"] is False
            and readout["current_selected_sector_data_uniform"] is True,
            readout,
        ),
        check(
            "no selected overclaim",
            decision["selected_U10_Ubar5_1M_samebranch_emitted"] is False
            and decision["selected_U10_Ubar5_polarization_closed"] is False
            and decision["selected_1M_Dirac_neutrino_source_rule_closed"] is False
            and decision["selected_sector_charge_or_chirality_closed"] is False
            and data["closure_claimed"] is False
            and cert["closure_claimed"] is False,
            decision,
        ),
        check(
            "minimal readout contract",
            contract["name"] == "SelectedMatterSlotTransversalityReadoutFunctional"
            and contract["must_compute"]["phase_shift_partition"] == {"phase": ["u", "e"], "shift": ["d", "nuD"]}
            and "does not use locked C1 splitter columns, observed masses, CKM/PMNS, or benchmark matrices"
            in contract["acceptance_conditions"],
            contract,
        ),
        check(
            "remaining gates sharpened",
            remains["selected_matter_slot_transversality_readout_functional"] is True
            and remains["selected_10M_clock_readout"] is True
            and remains["selected_bar5M_shift_readout"] is True
            and remains["selected_1M_Dirac_shift_readout"] is True,
            remains,
        ),
        check(
            "next gate recorded",
            data["next_required_artifact"] == NEXT
            and cert["next_required_artifact"] == NEXT
            and f"Next artifact: `{NEXT}`" in note
            and "SelectedMatterSlotTransversalityReadoutFunctional" in note,
            NOTE,
        ),
    ]

    print("\nMTT selected U10/Ubar5/1_M same-branch emission attempt audit")
    return 0 if all(tests) else 1


if __name__ == "__main__":
    sys.exit(main())
