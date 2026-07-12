"""Audit the complement-spectrum or smooth-operator source gate."""

from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path


REPO = Path(__file__).resolve().parents[1]
CERT = REPO / "certificates" / "complement_spectrum_or_smooth_operator_source_certificate.json"
DATA = REPO / "candidate_data" / "complement_spectrum_or_smooth_operator_source.candidate.json"
NOTE = REPO / "proof_corpus" / "Selected_Qa_SU3_Complement_Spectrum_or_Smooth_Operator_Source_v1.md"
SCRIPT = REPO / "scripts" / "build_complement_spectrum_or_smooth_operator_source.py"


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
    routes = data["route_tests"]
    reduced = data["reduced_determinant_conditional"]
    checks = [
        check("status", cert["status"] == "QA_SU3_COMPLEMENT_SPECTRUM_GATE_CURRENT_SOURCE_EXHAUSTED_REDUCED_DETERMINANT_CONDITIONAL", cert["status"]),
        check("script agreement", computed["what_closes"] == cert["what_closes"], computed["what_closes"]),
        check("reduced determinant isolated", reduced["value"] == "log(2008)" and reduced["status"] == "CONDITIONAL_NOT_PROMOTED", reduced),
        check("conditions not met", reduced["conditions_met_now"]["finite_projected_H_sel_sector"] is True and reduced["conditions_met_now"]["complement_cancellation_or_quotient"] is False and reduced["conditions_met_now"]["no_double_count_proof"] is False, reduced["conditions_met_now"]),
        check("route statuses exact", routes["coherent_sector_quotient"]["status"] == "PARTIAL_NOT_CLOSED" and routes["gap_suppression"]["status"] == "REJECT_AS_EXACT_CLOSURE" and routes["same_source_smooth_operator"]["status"] == "OPEN_PRIMARY", routes),
        check("no-go exhausts current source", data["no_go"]["verdict"] == "CURRENT_SOURCE_EXHAUSTED_AT_CONDITIONAL_REDUCED_DETERMINANT", data["no_go"]),
        check("prior finite determinant imported", data["prior_finite_determinant"]["determinant_exact"] == 2008, data["prior_finite_determinant"]),
        check("not full closure", cert["closure_claimed"] is False and cert["what_remains_open"]["qa_su3_packet_closed"] is False, cert),
        check("note records next", cert["next_required_artifact"] in note and "conditional reduced coherent-sector determinant = log(2008)" in note, NOTE),
    ]
    print("\nSelected Qa/SU3 complement spectrum or smooth operator source audit")
    return 0 if all(checks) else 1


if __name__ == "__main__":
    raise SystemExit(main())
