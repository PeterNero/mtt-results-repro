"""Audit the electroweak two-key frontier interface."""

from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path


REPO = Path(__file__).resolve().parents[1]
SCRIPT = REPO / "scripts" / "build_selected_electroweak_two_key_frontier_interface.py"
DATA = REPO / "candidate_data" / "selected_electroweak_two_key_frontier_interface.candidate.json"
CERT = REPO / "certificates" / "selected_electroweak_two_key_frontier_interface_certificate.json"
U1_TEMPLATE = REPO / "certificates" / "selected_electroweak_u1y_local_determinant_key.template.json"
ALPHA_TEMPLATE = REPO / "certificates" / "selected_electroweak_physical_action_anchor_key.template.json"
NOTE = REPO / "proof_corpus" / "Selected_Electroweak_Two_Key_Frontier_Interface_v1.md"

STATUS = "ELECTROWEAK_TWO_KEY_FRONTIER_INTERFACE_BUILT_KEYS_OPEN"
NEXT = "Selected_Electroweak_Two_Key_FillAttempt_v1"


def check(name: str, ok: bool, detail: object) -> bool:
    print(f"{'PASS' if ok else 'FAIL'}: {name} -- {detail}")
    return ok


def main() -> int:
    proc = subprocess.run(
        [sys.executable, str(SCRIPT)],
        cwd=REPO,
        text=True,
        stdout=subprocess.PIPE,
        stderr=subprocess.STDOUT,
        check=True,
    )
    data = json.loads(DATA.read_text(encoding="utf-8"))
    cert = json.loads(CERT.read_text(encoding="utf-8"))
    u1 = json.loads(U1_TEMPLATE.read_text(encoding="utf-8"))
    alpha = json.loads(ALPHA_TEMPLATE.read_text(encoding="utf-8"))
    note = NOTE.read_text(encoding="utf-8")
    logic = data["two_key_logic"]
    decision = data["decision"]
    checks = [
        check("status", data["status"] == STATUS and cert["status"] == STATUS, cert["status"]),
        check("script reruns", len([line for line in proc.stdout.splitlines() if line.startswith("wrote ")]) == 5, proc.stdout),
        check("next artifact", decision["next_required_artifact"] == NEXT and cert["next_required_artifact"] == NEXT and NEXT in note, cert["next_required_artifact"]),
        check("internal kernel closed", logic["internal_kernel_closed"] is True and logic["selected_internal_kernel"]["I_Qa_or_SU3"] == "log(2008)", logic),
        check("two keys independent", logic["u1_key_can_replace_alpha_key"] is False and logic["alpha_key_can_replace_u1_key"] is False, logic),
        check("u1 key open", data["u1y_local_determinant_key_status"]["lambda_12_closed"] is False and u1["source_evidence"]["selected_by_mtt"] is None, data["u1y_local_determinant_key_status"]),
        check("alpha key open", data["physical_action_anchor_key_status"]["physical_numeric_alpha_selected"] is False and alpha["source_evidence"]["selected_by_mtt"] is None, data["physical_action_anchor_key_status"]),
        check("templates open", u1["status"].startswith("OPEN_") and alpha["status"].startswith("OPEN_"), (u1["status"], alpha["status"])),
        check("no closure", cert["closure_claimed"] is False and decision["measured_electroweak_closure"] is False, decision),
        check("note records branch", "constants/electroweak branch" in note and "two independent open keys" in note, NOTE),
    ]
    print("\nSelected electroweak two-key frontier interface audit")
    return 0 if all(checks) else 1


if __name__ == "__main__":
    raise SystemExit(main())
