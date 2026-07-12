"""Audit the Qa/SU3 internal-packet alignment theorem."""

from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path


REPO = Path(__file__).resolve().parents[1]
CERT = REPO / "certificates" / "qa_su3_internal_packet_alignment_certificate.json"
DATA = REPO / "candidate_data" / "qa_su3_internal_packet_alignment.candidate.json"
NOTE = REPO / "proof_corpus" / "Selected_Qa_SU3_Internal_Packet_Alignment_v1.md"
SCRIPT = REPO / "scripts" / "build_qa_su3_internal_packet_alignment.py"


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
    diagnostics = data["inputs"]["local_diagnostic_notes"]
    decision = data["decision"]
    checks = [
        check("status", cert["status"] == "QA_SU3_INTERNAL_PACKET_ALIGNMENT_BUILT_OLD_NIL_TRAIL_DIAGNOSTIC_ONLY", cert["status"]),
        check("script agreement", computed["what_closes"] == cert["what_closes"], computed["what_closes"]),
        check("qa theorem imported", "GR_SURFACE_INTERNAL_QUANTUM_SEPARATION" in data["inputs"]["qa_surface_internal_status"], data["inputs"]),
        check("local diagnostics present", all(item["present"] for item in diagnostics.values()), diagnostics),
        check("old trail retained not endangered", decision["old_nil_smooth_determinant_trail_in_danger"] is False and "diagnostics" in decision["old_nil_smooth_determinant_trail_role"], decision),
        check("log2008 scoped", decision["selected_internal_reduced_Qa_SU3_determinant"] == "log(2008)", decision),
        check("no closure overclaim", data["closure_claimed"] is False and decision["full_electroweak_or_SM_closure_now"] is False, decision),
        check("guardrails block smooth double count", any("smooth internal complement" in item for item in data["guardrails"]) and any("GR/protospinor" in item for item in data["guardrails"]), data["guardrails"]),
        check("note records bridge", "internal reduced logdet log(2008)" in note and "full electroweak or SM closure = not claimed" in note, NOTE),
    ]
    print("\nQa/SU3 internal-packet alignment audit")
    return 0 if all(checks) else 1


if __name__ == "__main__":
    raise SystemExit(main())
