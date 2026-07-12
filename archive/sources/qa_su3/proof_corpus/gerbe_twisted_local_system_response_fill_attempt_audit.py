"""Audit the gerbe-twisted local-system response fill attempt."""

from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path


REPO = Path(__file__).resolve().parents[1]
CERT = REPO / "certificates" / "gerbe_twisted_local_system_response_fill_attempt_certificate.json"
DATA = REPO / "candidate_data" / "gerbe_twisted_local_system_response_fill_attempt.candidate.json"
NOTE = REPO / "proof_corpus" / "Selected_Qa_SU3_Gerbe_Twisted_Local_System_Response_Fill_Attempt_v1.md"
SCRIPT = REPO / "scripts" / "attempt_fill_gerbe_twisted_local_system_response.py"


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
    fill = data["fill_result"]
    packet = data["partial_packet"]
    checks = [
        check("status", cert["status"] == "QA_SU3_GERBE_TWISTED_LOCAL_SYSTEM_RESPONSE_FILL_ATTEMPT_PARTIAL_SOURCE_BLOCKED", cert["status"]),
        check("script agreement", computed["what_closes"] == cert["what_closes"], computed["what_closes"]),
        check("source family filled", fill["source_family_filled"] is True and fill["global_gerbe_curvature_available"] is True, fill),
        check("primitive support filled", fill["primitive_complex_central_support_filled"] is True and fill["twist_cancellation_table_filled"] is True, fill),
        check("representative missing", fill["same_branch_representative_filled"] is False and packet["gerbe_or_local_system"]["Deligne_Cech_or_B_field_representative"] is None, packet["gerbe_or_local_system"]),
        check("sections missing", fill["section_bases_and_constants_filled"] is False and packet["twisted_sections"]["section_bases_FG_P"] is None, packet["twisted_sections"]),
        check("finite response missing", fill["finite_response_filled"] is False and all(value is None for value in packet["finite_response"].values()), packet["finite_response"]),
        check("does not promote shortcuts", "q79 finite Z3/S3 table as direct Qa/SU3 data" in data["do_not_promote"], data["do_not_promote"]),
        check("no closure", cert["closure_claimed"] is False and cert["what_remains_open"]["qa_su3_packet_closed"] is False, cert),
        check("no target fitting", cert["target_fitting_used"] is False and data["target_fitting_used"] is False and fill["target_fitting_used"] is False, fill),
        check("note records next", data["next_required_artifact"] in note and "projective `rho_E` or `D_E`" in note, NOTE),
    ]
    print("\nSelected Qa/SU3 gerbe-twisted local-system response fill attempt audit")
    return 0 if all(checks) else 1


if __name__ == "__main__":
    raise SystemExit(main())
