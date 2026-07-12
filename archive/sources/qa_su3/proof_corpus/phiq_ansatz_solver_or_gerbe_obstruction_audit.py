"""Audit the Phi_q ansatz solver / gerbe obstruction gate."""

from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path


REPO = Path(__file__).resolve().parents[1]
CERT = REPO / "certificates" / "phiq_ansatz_solver_or_gerbe_obstruction_certificate.json"
DATA = REPO / "candidate_data" / "phiq_ansatz_solver_or_gerbe_obstruction.candidate.json"
NOTE = REPO / "proof_corpus" / "Selected_Qa_SU3_PhiQ_Ansatz_Solver_or_Gerbe_Obstruction_v1.md"
SCRIPT = REPO / "scripts" / "build_phiq_ansatz_solver_or_gerbe_obstruction.py"


def check(name: str, ok: bool, detail: object) -> bool:
    print(f"{'PASS' if ok else 'FAIL'}: {name} -- {detail}")
    return ok


def main() -> int:
    cert = json.loads(CERT.read_text(encoding="utf-8"))
    data = json.loads(DATA.read_text(encoding="utf-8"))
    note = NOTE.read_text(encoding="utf-8")
    proc = subprocess.run([sys.executable, str(SCRIPT)], cwd=REPO, text=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT, check=True)
    computed = json.loads(proc.stdout)
    tests = {item["id"]: item for item in data["ansatz_tests"]}
    checks = [
        check("status", cert["status"] == "QA_SU3_PHIQ_LITERAL_C_AXIS_OBSTRUCTION_GERBE_OR_SOURCE_AMENDMENT_REQUIRED", cert["status"]),
        check("script agreement", computed["counts"] == cert["counts"] and computed["what_closes"] == cert["what_closes"], computed["counts"]),
        check("c is not closed", data["form_differentials"]["c=(i/2)omega3 wedge baromega3"] != "0", data["form_differentials"]),
        check("eight c-axis spaces", data["counts"]["c_axis_obstructed_spaces"] == 8, data["counts"]),
        check("ordinary line bundle route obstructed", tests["ordinary_line_bundle_factor_literal_abc"]["status"] == "OBSTRUCTED", tests["ordinary_line_bundle_factor_literal_abc"]),
        check("gerbe route live", tests["twisted_gerbe_module"]["status"] == "LIVE_PRIMARY_AFTER_OBSTRUCTION", tests["twisted_gerbe_module"]),
        check("not claiming monad false", "This does not prove the monad idea false." in data["interpretation"], data["interpretation"]),
        check("values remain open", cert["what_remains_open"]["qa_su3_packet_closed"] is False and cert["closure_claimed"] is False, cert),
        check("no target fitting", cert["target_fitting_used"] is False and data["target_fitting_used"] is False, cert),
        check("note records next gate", "Selected_Qa_SU3_Gerbe_Twist_or_Closed_C_Source_Amendment_Gate_v1" in note, NOTE),
    ]
    print("\nSelected Qa/SU3 Phi_q ansatz solver or gerbe obstruction audit")
    return 0 if all(checks) else 1


if __name__ == "__main__":
    raise SystemExit(main())
