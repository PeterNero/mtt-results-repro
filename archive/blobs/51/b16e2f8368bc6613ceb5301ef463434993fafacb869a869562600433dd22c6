"""Audit the locked Qa/SU3 proof state."""

from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path


REPO = Path(__file__).resolve().parents[1]
CERT = REPO / "certificates" / "locked_proof_state_certificate.json"
DATA = REPO / "candidate_data" / "locked_proof_state.candidate.json"
NOTE = REPO / "proof_corpus" / "Selected_Qa_SU3_Locked_Proof_State_v1.md"
SCRIPT = REPO / "scripts" / "build_locked_proof_state.py"


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
    state = data["locked_state"]
    finite = state["finite_hessian"]
    checks = [
        check("status", cert["status"] == "QA_SU3_PROOF_STATE_LOCKED_FINITE_REDUCED_DETERMINANT_CONDITIONAL_SMOOTH_SOURCE_OPEN", cert["status"]),
        check("script agreement", computed["what_closes"] == cert["what_closes"], computed["what_closes"]),
        check("finite determinant locked", finite["determinant"] == 2008 and finite["finite_rank_logdet"] == "log(2008)", finite),
        check("tau locked", finite["Pi_tw"] == [0, 0, 1] and finite["tau"]["P"] == 0 and finite["tau"]["F1"] + finite["tau"]["G1"] == 0, finite["tau"]),
        check("open gate exact", state["open_gate"]["name"] == "Selected_Qa_SU3_Source_Amendment_Complement_Quotient_or_Smooth_Spectrum_v1" and len(state["open_gate"]["required_one_of"]) == 2, state["open_gate"]),
        check("forbidden promotions include overclaim", any("full Qa/SU3 threshold closure from log(2008)" in item for item in state["forbidden_promotions"]), state["forbidden_promotions"]),
        check("future acceptance rule strict", "new work must preserve target_fitting_used=false" in data["acceptance_rule_for_future_work"], data["acceptance_rule_for_future_work"]),
        check("not closure", cert["closure_claimed"] is False and cert["what_remains_open"]["qa_su3_packet_closed"] is False, cert),
        check("note records lock", "full smooth Qa/SU3 threshold closure = no" in note and cert["next_required_artifact"] in note, NOTE),
    ]
    print("\nSelected Qa/SU3 locked proof state audit")
    return 0 if all(checks) else 1


if __name__ == "__main__":
    raise SystemExit(main())
