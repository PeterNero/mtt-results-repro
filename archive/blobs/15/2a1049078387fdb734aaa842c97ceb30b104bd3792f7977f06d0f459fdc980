"""Audit the Qa/SU3 twisted-source promotion packet interface."""

from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path


REPO = Path(__file__).resolve().parents[1]
CERT = REPO / "certificates" / "twisted_source_promotion_packet_interface_certificate.json"
DATA = REPO / "candidate_data" / "twisted_source_promotion_packet_interface.candidate.json"
TEMPLATE = REPO / "certificates" / "twisted_source_promotion_packet.template.json"
NOTE = REPO / "proof_corpus" / "Selected_Qa_SU3_Twisted_Source_Promotion_Packet_Interface_v1.md"
SCRIPT = REPO / "scripts" / "build_twisted_source_promotion_packet_interface.py"


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
        check("status", cert["status"] == "QA_SU3_TWISTED_SOURCE_PROMOTION_PACKET_INTERFACE_BUILT_VALUES_OPEN", cert["status"]),
        check("script agreement", computed["what_closes"] == cert["what_closes"], computed["what_closes"]),
        check("template open", template["status"] == "OPEN_SELECTED_QA_SU3_TWISTED_SOURCE_PROMOTION_PACKET_REQUIRED", template["status"]),
        check("selected fields open", template["source_evidence"]["selected_by_mtt"] is None and template["source_evidence"]["same_branch_Qa_SU3"] is None, template["source_evidence"]),
        check("projective response required", template["projective_rhoE"]["projective_mesh_tables"] is None and template["operator_response"]["D_E"] is None, template),
        check("validator patterns available", data["interface_checks"]["projective_validator_pattern_available"] is True and data["interface_checks"]["twisted_promotion_contract_available"] is True, data["interface_checks"]),
        check("no closure", cert["closure_claimed"] is False and cert["what_remains_open"]["qa_su3_packet_closed"] is False, cert),
        check("no target fitting", cert["target_fitting_used"] is False and data["target_fitting_used"] is False, cert),
        check("note records next", data["next_required_artifact"] in note and "without importing q79 values" in note, NOTE),
    ]
    print("\nSelected Qa/SU3 twisted-source promotion packet interface audit")
    return 0 if all(checks) else 1


if __name__ == "__main__":
    raise SystemExit(main())
