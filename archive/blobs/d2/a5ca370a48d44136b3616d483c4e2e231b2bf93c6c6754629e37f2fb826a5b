"""Audit the same-branch Strominger/HYM source packet search."""

from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path


REPO = Path(__file__).resolve().parents[1]
CERT = REPO / "certificates" / "strominger_hym_source_packet_search_certificate.json"
DATA = REPO / "candidate_data" / "strominger_hym_source_packet_search.candidate.json"
NOTE = REPO / "proof_corpus" / "Selected_Qa_SU3_Strominger_HYM_Source_Packet_Search_v1.md"
SCRIPT = REPO / "scripts" / "build_strominger_hym_source_packet_search.py"


def check(name: str, ok: bool, detail: object) -> bool:
    print(f"{'PASS' if ok else 'FAIL'}: {name} -- {detail}")
    return ok


def main() -> int:
    cert = json.loads(CERT.read_text(encoding="utf-8"))
    data = json.loads(DATA.read_text(encoding="utf-8"))
    note = NOTE.read_text(encoding="utf-8")
    proc = subprocess.run([sys.executable, str(SCRIPT)], cwd=REPO, text=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT, check=True)
    computed = json.loads(proc.stdout)
    result = data["search_result"]
    checks = [
        check("status", cert["status"] == "QA_SU3_STROMINGER_HYM_SOURCE_PACKET_SEARCH_DONE_SAME_BRANCH_SOURCE_NOT_FOUND", cert["status"]),
        check("script agreement", computed["what_closes"] == cert["what_closes"], computed["what_closes"]),
        check("templates found", result["general_strominger_hym_template_found"] is True and result["visible_source_packet_template_found"] is True, result),
        check("same branch missing", result["same_branch_qa_su3_source_packet_found"] is False, result),
        check("constructive spec", len(data["constructive_spec"]["required_fields"]) == 9, data["constructive_spec"]),
        check("no closure", result["qa_su3_closed"] is False and cert["closure_claimed"] is False, cert),
        check("note records next", cert["next_required_artifact"] in note and "same-branch Qa/SU3 source packet" in note, NOTE),
        check("no fitting", cert["target_fitting_used"] is False and data["target_fitting_used"] is False, cert),
    ]
    print("\nSelected Qa/SU3 Strominger HYM source packet search audit")
    return 0 if all(checks) else 1


if __name__ == "__main__":
    raise SystemExit(main())
