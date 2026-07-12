"""Audit the Qa/SU3 FCC invariant-equation packet or D_E exit gate."""

from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path


REPO = Path(__file__).resolve().parents[1]
CERT = REPO / "certificates" / "fcc_invariant_equation_packet_or_de_exit_certificate.json"
DATA = REPO / "candidate_data" / "fcc_invariant_equation_packet_or_de_exit.candidate.json"
NOTE = REPO / "proof_corpus" / "Selected_Qa_SU3_FCC_Invariant_Equation_Packet_or_DE_Exit_v1.md"
SCRIPT = REPO / "scripts" / "build_fcc_invariant_equation_packet_or_de_exit.py"


def check(name: str, ok: bool, detail: object) -> bool:
    print(f"{'PASS' if ok else 'FAIL'}: {name} -- {detail}")
    return ok


def main() -> int:
    cert = json.loads(CERT.read_text(encoding="utf-8"))
    data = json.loads(DATA.read_text(encoding="utf-8"))
    note = NOTE.read_text(encoding="utf-8")
    proc = subprocess.run(
        [sys.executable, str(SCRIPT)],
        cwd=REPO,
        text=True,
        stdout=subprocess.PIPE,
        stderr=subprocess.STDOUT,
        check=True,
    )
    computed = json.loads(proc.stdout)
    gates = data["gate_results"]
    tests = {row["test_id"]: row for row in data["fcc_tests"]}
    equations = data["finite_equation_packet"]["equations"]
    checks = [
        check("status", cert["status"] == "QA_SU3_FCC_INVARIANT_EQUATION_PACKET_BUILT_PERIOD_AND_OPERATOR_VALUES_OPEN", cert["status"]),
        check("script agreement", computed["what_closes"] == cert["what_closes"], computed["what_closes"]),
        check("three equations present", len(equations) == 3, equations),
        check("Bianchi and ctwist included", gates["componentwise_bianchi_row_included"] is True and gates["ctwist_amplitude_included"] is True, gates),
        check("A unit solves s", gates["A_unit_condition_solves_s"] is True and data["finite_equation_packet"]["derived_if_A_unit_imposed"]["numeric_s"] > 0, data["finite_equation_packet"]),
        check("A unit not selected", tests["A_unit_as_equation_not_selector"]["passes"] is True and gates["A_unit_condition_source_selected"] is False, tests["A_unit_as_equation_not_selector"]),
        check("integer data gap remains", tests["integer_data_selection"]["passes"] is False and gates["integer_data_selects_s_or_finite_quotient"] is False, tests["integer_data_selection"]),
        check("operator exit remains open", tests["DE_exit_availability"]["passes"] is False and gates["same_source_DE_or_rhoE_exit_available"] is False, tests["DE_exit_availability"]),
        check("closure not claimed", cert["closure_claimed"] is False and gates["qa_su3_packet_closed"] is False and cert["what_remains_open"]["qa_su3_packet_closed"] is False, cert),
        check("no target fitting", cert["target_fitting_used"] is False and data["target_fitting_used"] is False, cert),
        check("note records next matrix hunt", cert["next_required_artifact"] in note and "A=1" in note, NOTE),
    ]
    print("\nSelected Qa/SU3 FCC invariant-equation packet or D_E exit audit")
    return 0 if all(checks) else 1


if __name__ == "__main__":
    raise SystemExit(main())
