"""Audit the projective rho_E or D_E response source hunt."""

from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path


REPO = Path(__file__).resolve().parents[1]
CERT = REPO / "certificates" / "projective_rhoe_or_de_response_source_hunt_certificate.json"
DATA = REPO / "candidate_data" / "projective_rhoe_or_de_response_source_hunt.candidate.json"
NOTE = REPO / "proof_corpus" / "Selected_Qa_SU3_Projective_RhoE_or_DE_Response_Source_Hunt_v1.md"
SCRIPT = REPO / "scripts" / "build_projective_rhoe_or_de_response_source_hunt.py"


def check(name: str, ok: bool, detail: object) -> bool:
    print(f"{'PASS' if ok else 'FAIL'}: {name} -- {detail}")
    return ok


def route(data: dict[str, object], route_id: str) -> dict[str, object]:
    for item in data["route_tests"]:
        if item["route_id"] == route_id:
            return item
    raise KeyError(route_id)


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
    hunt = data["hunt_result"]
    checks = [
        check("status", cert["status"] == "QA_SU3_PROJECTIVE_RHOE_OR_DE_RESPONSE_SOURCE_HUNT_DONE_VALIDATORS_FOUND_SOURCE_OPEN", cert["status"]),
        check("script agreement", computed["what_closes"] == cert["what_closes"], computed["what_closes"]),
        check("projective validator found", hunt["projective_rhoe_validator_available"] is True, hunt),
        check("promotion contract found", hunt["twisted_promotion_contract_available"] is True, hunt),
        check("q79 transfer remains guardrail", route(data, "q79_projective_rhoe_mesh_validator_transfer")["promotes_qa_su3_source"] is False, route(data, "q79_projective_rhoe_mesh_validator_transfer")),
        check("source hunt still open", hunt["selected_qa_su3_projective_rhoE_found"] is False and hunt["selected_qa_su3_D_E_or_dotD_found"] is False, hunt),
        check("rejected direct reuse", "direct q79/S3 finite table as Qa/SU3 representative" in data["rejected_reuse"], data["rejected_reuse"]),
        check("no closure", cert["closure_claimed"] is False and cert["what_remains_open"]["qa_su3_packet_closed"] is False, cert),
        check("no target fitting", cert["target_fitting_used"] is False and data["target_fitting_used"] is False and hunt["target_fitting_used"] is False, hunt),
        check("note records next", data["next_required_artifact"] in note and "selected Qa/SU3 response source" in note, NOTE),
    ]
    print("\nSelected Qa/SU3 projective rho_E or D_E response source hunt audit")
    return 0 if all(checks) else 1


if __name__ == "__main__":
    raise SystemExit(main())
