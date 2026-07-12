"""Audit the Qa/SU3 twisted section-ring and gerbe-source gate."""

from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path


REPO = Path(__file__).resolve().parents[1]
CERT = REPO / "certificates" / "twisted_section_ring_and_gerbe_source_gate_certificate.json"
DATA = REPO / "candidate_data" / "twisted_section_ring_and_gerbe_source_gate.candidate.json"
NOTE = REPO / "proof_corpus" / "Selected_Qa_SU3_Twisted_Section_Ring_and_Gerbe_Source_Gate_v1.md"
SCRIPT = REPO / "scripts" / "build_twisted_section_ring_and_gerbe_source_gate.py"


def check(name: str, ok: bool, detail: object) -> bool:
    print(f"{'PASS' if ok else 'FAIL'}: {name} -- {detail}")
    return ok


def main() -> int:
    cert = json.loads(CERT.read_text(encoding="utf-8"))
    data = json.loads(DATA.read_text(encoding="utf-8"))
    note = NOTE.read_text(encoding="utf-8")
    proc = subprocess.run([sys.executable, str(SCRIPT)], cwd=REPO, text=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT, check=True)
    computed = json.loads(proc.stdout)
    fields = data["source_packet_fields"]
    laws = data["typed_multiplication_law"]
    scans = data["source_scans"]
    checks = [
        check("status", cert["status"] == "QA_SU3_TWISTED_SECTION_RING_GATE_TYPING_PASS_SOURCE_VALUES_OPEN", cert["status"]),
        check("script agreement", computed["what_closes"] == cert["what_closes"], computed["what_closes"]),
        check("five typed products", len(laws) == 5, len(laws)),
        check("all typed products pass", all(item["twist_cancellation_verified"] and item["ordinary_ab_target_verified"] for item in laws), laws),
        check("source fields remain open", all(value is False for value in fields.values()), fields),
        check("q79 twisted guardrail found", scans["q79_twisted_s3_source_attempt"]["terms"]["twisted_CP"] is True and scans["q79_twisted_s3_source_attempt"]["terms"]["Freed_Witten"] is True, scans["q79_twisted_s3_source_attempt"]),
        check("closure not claimed", cert["closure_claimed"] is False and cert["what_remains_open"]["qa_su3_packet_closed"] is False, cert),
        check("no target fitting", cert["target_fitting_used"] is False and data["target_fitting_used"] is False, cert),
        check("note records next artifact", "Selected_Qa_SU3_Minimal_Gerbe_Source_Candidate_or_NoGo_v1" in note, NOTE),
    ]
    print("\nSelected Qa/SU3 twisted section-ring and gerbe-source gate audit")
    return 0 if all(checks) else 1


if __name__ == "__main__":
    raise SystemExit(main())
