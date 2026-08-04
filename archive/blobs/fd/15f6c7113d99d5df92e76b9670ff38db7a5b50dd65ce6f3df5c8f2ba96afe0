"""Audit the c-twist period-normalization or A01 exit gate."""

from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path


REPO = Path(__file__).resolve().parents[1]
CERT = REPO / "certificates" / "ctwist_period_normalization_or_a01_exit_certificate.json"
DATA = REPO / "candidate_data" / "ctwist_period_normalization_or_a01_exit.candidate.json"
NOTE = REPO / "proof_corpus" / "Selected_Qa_SU3_CTwist_Period_Normalization_or_A01_Exit_v1.md"
SCRIPT = REPO / "scripts" / "build_ctwist_period_normalization_or_a01_exit.py"


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
    scalar = data["scalar_period_gate"]
    routes = data["normalization_route_tests"]
    checks = [
        check("status", cert["status"] == "QA_SU3_CTWIST_PERIOD_NORMALIZATION_SCALAR_GATE_DERIVED_SELECTOR_OPEN_A01_EXIT_REQUIRED", cert["status"]),
        check("script agreement", computed["what_closes"] == cert["what_closes"], computed["what_closes"]),
        check("scalar condition derived", gates["absolute_A_unit_condition_derived"] is True and "R^4" in scalar["A_unit_condition"], scalar),
        check("numeric scalar positive", scalar["numeric_R4_over_alpha_prime_for_A_unit"] > 0, scalar),
        check("integral periods not promoted", routes[0]["verdict"] == "INTEGRAL_LATTICE_YES_UNIT_NOT_SELECTED" and gates["period_normalization_promoted"] is False, routes[0]),
        check("q79 remains off branch", any(row["route_id"] == "q79_s3_finite_torsion" and row["verdict"] == "OFF_BRANCH_PATTERN_ONLY" for row in routes), routes),
        check("A01 exit required", gates["A01_DE_exit_required"] is True and cert["what_closes"]["A01_DE_exit_marked_required"] is True, cert),
        check("closure not claimed", cert["closure_claimed"] is False and cert["what_remains_open"]["qa_su3_packet_closed"] is False, cert),
        check("no target fitting", cert["target_fitting_used"] is False and data["target_fitting_used"] is False, cert),
        check("note records A unit condition", "A=1" in note and cert["next_required_artifact"] in note, NOTE),
    ]
    print("\nSelected Qa/SU3 c-twist period normalization or A01 exit audit")
    return 0 if all(checks) else 1


if __name__ == "__main__":
    raise SystemExit(main())
