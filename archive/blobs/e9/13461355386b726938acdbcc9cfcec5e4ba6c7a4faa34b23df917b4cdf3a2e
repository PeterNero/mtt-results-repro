"""Audit the selected sector-charge / 1_M Dirac-neutrino rule attempt."""

from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SCRIPT = ROOT / "scripts" / "build_selected_sectorcharge_1m_dirac_rule_attempt.py"
CANDIDATE = ROOT / "candidate_data" / "selected_sectorcharge_1m_dirac_rule_attempt.candidate.json"
CERT = ROOT / "certificates" / "selected_sectorcharge_1m_dirac_rule_attempt_certificate.json"
NOTE = ROOT / "proof_corpus" / "MTT_Selected_SectorCharge_1M_DiracRule_Attempt_v1.md"

STATUS = "MTT_SELECTED_SECTORCHARGE_1M_DIRAC_RULE_ATTEMPT_BUILT_SOURCE_POLARIZATION_OPEN"
NEXT = "MTT_Selected_1M_DiracNeutrino_Source_or_SelectedU10Ubar5Polarization_v1"


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
    rule = data["structural_rule_candidate"]
    tests = data["selected_proof_tests"]
    decision = data["decision"]
    remains = data["what_remains_open"]
    superset = data["superset_strategy"]

    audit_tests = [
        check("status", data["status"] == STATUS and cert["status"] == STATUS, data["status"]),
        check(
            "E6 dictionary gives 1_M Dirac rule",
            rule["one_M_maps_to_Nc"] is True
            and rule["dirac_operator_uses_bar5_1M_5H"] is True
            and rule["dirac_operator_outputs_L_Nc_Hu"] is True
            and "bar5_M 1_M 5_H" in rule["dirac_operator"],
            rule,
        ),
        check(
            "required partition rederived",
            rule["proposed_phase_route"] == ["u", "e"]
            and rule["proposed_shift_route"] == ["d", "nuD"]
            and rule["matches_required_route"] is True,
            rule,
        ),
        check(
            "selected proof still open",
            tests["selected_U10_Ubar5_source"] is False
            and tests["selected_sector_charge_table"] is False
            and tests["selected_1M_Dirac_neutrino_rule"] is False
            and decision["selected_sector_charge_closed"] is False
            and decision["selected_1M_Dirac_rule_closed"] is False,
            {"tests": tests, "decision": decision},
        ),
        check(
            "source gaps recorded",
            remains["selected_U10_clock_source"] is True
            and remains["selected_Ubar5_shift_source"] is True
            and remains["selected_1M_Dirac_neutrino_shift_rule"] is True
            and remains["selected_source_to_C1_transfer_map"] is True,
            remains,
        ),
        check(
            "no target fitting or overclaim",
            data["closure_claimed"] is False
            and cert["closure_claimed"] is False
            and data["target_fitting_used"] is False
            and superset["observed_data_used"] is False
            and superset["diagnostic_lift_used_as_proof"] is False,
            {"cert": cert, "superset": superset},
        ),
        check(
            "next gate recorded",
            data["next_required_artifact"] == NEXT
            and cert["next_required_artifact"] == NEXT
            and f"Next artifact: `{NEXT}`" in note
            and "selected `1_M` Dirac-neutrino shift rule" in note,
            NOTE,
        ),
    ]

    print("\nMTT selected sector-charge / 1_M Dirac-neutrino rule attempt audit")
    return 0 if all(audit_tests) else 1


if __name__ == "__main__":
    sys.exit(main())
