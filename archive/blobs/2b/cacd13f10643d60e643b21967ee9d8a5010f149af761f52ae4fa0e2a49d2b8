"""Audit the MTT SM-parity closure ledger."""

from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path


REPO = Path(__file__).resolve().parents[1]
CERT = REPO / "certificates" / "sm_parity_closure_ledger_certificate.json"
DATA = REPO / "candidate_data" / "sm_parity_closure_ledger.candidate.json"
NOTE = REPO / "proof_corpus" / "MTT_SM_Parity_Closure_Ledger_v1.md"
SCRIPT = REPO / "scripts" / "build_sm_parity_closure_ledger.py"


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
    rows = data["ledger"]
    checks = [
        check("status", cert["status"] == "MTT_SM_PARITY_LEDGER_BUILT_NO_KNOB_UPGRADE_PATH_OPEN", cert["status"]),
        check("script agreement", computed["what_closes"] == cert["what_closes"], computed["what_closes"]),
        check("ledger broad enough", len(rows) >= 10, len(rows)),
        check("measured inputs allowed", all(row["measured_input_allowed_for_sm_parity"] for row in rows), rows),
        check("no-knob retained", gates["no_knob_targets_preserved"] is True and cert["what_remains_open"]["no_knob_constants"] is True, gates),
        check("parity not closed", gates["full_sm_parity_closed"] is False and cert["what_remains_open"]["sm_parity_closed"] is False, cert),
        check("next artifact selected", data["next_required_artifact"] == "MTT_Core_Axioms_and_Measured_Parameter_Interface_v1", data["recommended_start"]),
        check("no target fitting", cert["target_fitting_used"] is False and data["target_fitting_used"] is False, cert),
        check("note records distinction", "SM-parity" in note and "no-knob" in note, NOTE),
    ]
    print("\nMTT SM-parity closure ledger audit")
    return 0 if all(checks) else 1


if __name__ == "__main__":
    raise SystemExit(main())
