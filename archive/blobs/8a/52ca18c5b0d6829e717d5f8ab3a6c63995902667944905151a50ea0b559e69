"""Audit the central-cocycle map source-augmentation request."""

from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path


REPO = Path(__file__).resolve().parents[1]
CERT = REPO / "certificates" / "central_cocycle_map_source_augmentation_request_certificate.json"
DATA = REPO / "candidate_data" / "central_cocycle_map_source_augmentation_request.candidate.json"
NOTE = REPO / "proof_corpus" / "Selected_Qa_SU3_Central_Cocycle_Map_Source_Augmentation_Request_v1.md"
SCRIPT = REPO / "scripts" / "build_central_cocycle_map_source_augmentation_request.py"


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
    required = data["required_packet"]
    tests = data["acceptance_tests"]
    checks = [
        check("status", cert["status"] == "QA_SU3_CENTRAL_COCYCLE_MAP_SOURCE_AUGMENTATION_REQUEST_BUILT_VALUES_OPEN", cert["status"]),
        check("script agreement", computed["what_closes"] == cert["what_closes"], computed["what_closes"]),
        check("five required groups", set(required) == {"source_identity", "representative", "central_cocycle_map", "admissibility", "response_payload"}, required),
        check("central map requirements explicit", any("c-twist" in item for item in required["central_cocycle_map"]), required["central_cocycle_map"]),
        check("response requirements explicit", any("D_E/dotD" in item for item in required["response_payload"]) and any("rho_E" in item for item in required["response_payload"]), required["response_payload"]),
        check("forbidden shortcuts explicit", len(data["forbidden_shortcuts"]) == 6 and any("q79" in item for item in data["forbidden_shortcuts"]), data["forbidden_shortcuts"]),
        check("values open", all(value is False for value in tests.values()), tests),
        check("lanes split", set(data["route_split"]) == {"source_augmentation_lane", "derivation_lane"}, data["route_split"]),
        check("no closure", cert["closure_claimed"] is False and data["closure_claimed"] is False, cert),
        check("no target fitting", cert["target_fitting_used"] is False and data["target_fitting_used"] is False, cert),
        check("note records next", data["next_required_artifact"] in note and "derivation lane" in note, NOTE),
    ]
    print("\nSelected Qa/SU3 central-cocycle map source-augmentation request audit")
    return 0 if all(checks) else 1


if __name__ == "__main__":
    raise SystemExit(main())
