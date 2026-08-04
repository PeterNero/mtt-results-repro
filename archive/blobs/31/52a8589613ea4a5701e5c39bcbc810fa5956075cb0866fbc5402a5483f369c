"""Audit the endomorphism/local-system torsion route decision."""

from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path


REPO = Path(__file__).resolve().parents[1]
CERT = REPO / "certificates" / "endomorphism_or_local_system_torsion_decision_certificate.json"
DATA = REPO / "candidate_data" / "endomorphism_or_local_system_torsion_decision.candidate.json"
NOTE = REPO / "proof_corpus" / "Selected_Qa_SU3_Endomorphism_or_Local_System_Torsion_Decision_v1.md"
SCRIPT = REPO / "scripts" / "build_endomorphism_or_local_system_torsion_decision.py"


def check(name: str, ok: bool, detail: object) -> bool:
    print(f"{'PASS' if ok else 'FAIL'}: {name} -- {detail}")
    return ok


def lane(data: dict[str, object], lane_id: str) -> dict[str, object]:
    for item in data["lanes"]:
        if item["id"] == lane_id:
            return item
    raise KeyError(lane_id)


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
    decision = data["decision"]
    checks = [
        check("status", cert["status"] == "QA_SU3_ENDOMORPHISM_OR_LOCAL_SYSTEM_TORSION_DECISION_BUILT_GERBE_RESPONSE_PRIMARY", cert["status"]),
        check("script agreement", computed["decision"] == cert["decision"], computed["decision"]),
        check("repair B retained only", lane(data, "source_certified_A01_repair_B")["status"] == "BLOCKED_SOURCE_CERTIFICATION_MISSING", lane(data, "source_certified_A01_repair_B")),
        check("endomorphism lane live open", lane(data, "endomorphism_E_threshold_operator")["status"] == "LIVE_BUT_OPERATOR_LAYER_OPEN", lane(data, "endomorphism_E_threshold_operator")),
        check("torsion lane live open", lane(data, "selected_local_system_torsion")["status"] == "LIVE_AS_FINITE_RESPONSE_EXIT_NOT_SOURCE_FILLED", lane(data, "selected_local_system_torsion")),
        check("gerbe response primary", decision["primary_next_lane"] == "projective_gerbe_twisted_module_response", decision),
        check("no closure", cert["closure_claimed"] is False and cert["what_remains_open"]["qa_su3_packet_closed"] is False, cert),
        check("no target fitting", cert["target_fitting_used"] is False and data["target_fitting_used"] is False, cert),
        check("note records next", data["next_required_artifact"] in note and "closure claimed: no" in note, NOTE),
    ]
    print("\nSelected Qa/SU3 endomorphism or local-system torsion decision audit")
    return 0 if all(checks) else 1


if __name__ == "__main__":
    raise SystemExit(main())
