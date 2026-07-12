"""Audit the minimal closing source-data request."""

from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path


REPO = Path(__file__).resolve().parents[1]
CERT = REPO / "certificates" / "minimal_closing_source_data_request_certificate.json"
DATA = REPO / "candidate_data" / "minimal_closing_source_data_request.candidate.json"
NOTE = REPO / "proof_corpus" / "Selected_Qa_SU3_Minimal_Closing_Source_Data_Request_v1.md"
SCRIPT = REPO / "scripts" / "build_minimal_closing_source_data_request.py"


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
    required = data["required_fields"]
    result = data["acceptance_result"]
    checks = [
        check("status", cert["status"] == "QA_SU3_MINIMAL_CLOSING_SOURCE_DATA_REQUEST_BUILT_CURRENT_CORPUS_OPEN", cert["status"]),
        check("script agreement", computed["what_closes"] == cert["what_closes"], computed["what_closes"]),
        check("required field groups", set(required) == {"source_identity", "typed_monad_maps", "operator_exit", "admissibility"}, required),
        check("forbidden shortcuts listed", len(data["forbidden_fields"]) >= 6 and any("printed A01" in item for item in data["forbidden_fields"]), data["forbidden_fields"]),
        check("validator plan present", len(data["validator_plan"]) == 4, data["validator_plan"]),
        check("current corpus open", result["current_corpus_satisfies_request"] is False and result["qa_su3_packet_closed"] is False, result),
        check("A01 and matrix gaps included", result["printed_A01_rejected"] is True and result["selected_matrix_source_missing"] is True, result),
        check("closure not claimed", cert["closure_claimed"] is False and cert["what_remains_open"]["qa_su3_packet_closed"] is False, cert),
        check("no target fitting", cert["target_fitting_used"] is False and data["target_fitting_used"] is False, cert),
        check("note records three close routes", "A. corrected" in note and "B. typed" in note and "C. selected" in note, NOTE),
    ]
    print("\nSelected Qa/SU3 minimal closing source-data request audit")
    return 0 if all(checks) else 1


if __name__ == "__main__":
    raise SystemExit(main())
