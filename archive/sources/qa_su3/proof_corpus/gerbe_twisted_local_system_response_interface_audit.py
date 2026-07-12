"""Audit the gerbe-twisted local-system response interface."""

from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path


REPO = Path(__file__).resolve().parents[1]
CERT = REPO / "certificates" / "gerbe_twisted_local_system_response_interface_certificate.json"
DATA = REPO / "candidate_data" / "gerbe_twisted_local_system_response_interface.candidate.json"
TEMPLATE = REPO / "certificates" / "gerbe_twisted_local_system_response.template.json"
NOTE = REPO / "proof_corpus" / "Selected_Qa_SU3_Gerbe_Twisted_Local_System_Response_Interface_v1.md"
SCRIPT = REPO / "scripts" / "build_gerbe_twisted_local_system_response_interface.py"


def check(name: str, ok: bool, detail: object) -> bool:
    print(f"{'PASS' if ok else 'FAIL'}: {name} -- {detail}")
    return ok


def main() -> int:
    cert = json.loads(CERT.read_text(encoding="utf-8"))
    data = json.loads(DATA.read_text(encoding="utf-8"))
    template = json.loads(TEMPLATE.read_text(encoding="utf-8"))
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
    checks = [
        check("status", cert["status"] == "QA_SU3_GERBE_TWISTED_LOCAL_SYSTEM_RESPONSE_INTERFACE_BUILT_VALUES_OPEN", cert["status"]),
        check("script agreement", computed["what_closes"] == cert["what_closes"], computed["what_closes"]),
        check("template open", template["status"] == "OPEN_SELECTED_QA_SU3_GERBE_TWISTED_LOCAL_SYSTEM_RESPONSE_REQUIRED", template["status"]),
        check("twists cancel", data["interface_checks"]["all_pair_twists_cancel"] is True and data["interface_checks"]["all_products_land_in_P"] is True, data["interface_checks"]),
        check("requires source", template["source_certificate"]["source_identity"] is None and cert["what_remains_open"]["selected_source_identity"] is True, template["source_certificate"]),
        check("requires finite response", all(value is None for value in template["finite_response"].values()), template["finite_response"]),
        check("rejects shortcuts", "using q79 torsion as direct Qa/SU3 data" in data["rejected_shortcuts"], data["rejected_shortcuts"]),
        check("no closure", cert["closure_claimed"] is False and cert["what_remains_open"]["qa_su3_packet_closed"] is False, cert),
        check("note records next", data["next_required_artifact"] in note and "target fitting used: no" in note, NOTE),
    ]
    print("\nSelected Qa/SU3 gerbe-twisted local-system response interface audit")
    return 0 if all(checks) else 1


if __name__ == "__main__":
    raise SystemExit(main())
