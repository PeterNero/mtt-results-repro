"""Audit the selected finite source solve attempt."""

from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path


REPO = Path(__file__).resolve().parents[1]
CERT = REPO / "certificates" / "selected_finite_source_solve_attempt_certificate.json"
DATA = REPO / "candidate_data" / "selected_finite_source_solve_attempt.candidate.json"
NOTE = REPO / "proof_corpus" / "Selected_Qa_SU3_Selected_Finite_Source_Solve_Attempt_v1.md"
SCRIPT = REPO / "scripts" / "build_selected_finite_source_solve_attempt.py"


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
    results = data["finite_solve_results"]
    route_ids = [row["route_id"] for row in data["route_tests"]]
    checks = [
        check("status", cert["status"] == "QA_SU3_SELECTED_FINITE_SOURCE_SOLVE_ATTEMPT_CURRENT_CORPUS_NO_GO_OPERATOR_SOURCE_MISSING", cert["status"]),
        check("script agreement", computed["what_closes"] == cert["what_closes"], computed["what_closes"]),
        check("external certificates present", all(row["present"] for row in data["external_certificates"].values()), data["external_certificates"]),
        check("cochain lane not filled", results["selected_finite_cochain_packet_supplied"] is False, results),
        check("DE lane not filled", results["selected_DE_dotD_response_supplied"] is False, results),
        check("HYM retired", results["explicit_HYM_matrix_route_retired_current_record"] is True, results),
        check("Repair B no-go", results["repair_B_current_source_no_go"] is True, results),
        check("endomorphism missing", results["selected_endomorphism_E_found"] is False and results["selected_Qa_SU3_operator_source_found"] is False, results),
        check("all route tests present", set(route_ids) == {"finite_cochain_product_lane", "explicit_hym_matrix_lane", "repair_b_primitive_correction_lane", "projective_clock_shift_lane", "endomorphism_or_threshold_operator_lane"}, route_ids),
        check("no false closure", results["qa_su3_packet_closed"] is False and cert["closure_claimed"] is False, cert),
        check("note records current-source scope", "current source record" in note and cert["next_required_artifact"] in note, NOTE),
        check("no target fitting", cert["target_fitting_used"] is False and data["target_fitting_used"] is False, cert),
    ]
    print("\nSelected Qa/SU3 selected finite source solve attempt audit")
    return 0 if all(checks) else 1


if __name__ == "__main__":
    raise SystemExit(main())
