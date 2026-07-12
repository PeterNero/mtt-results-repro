"""Audit the Qa/SU3 color-bundle operator packet fill attempt."""

from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path


REPO = Path(__file__).resolve().parents[1]
CERT = REPO / "certificates" / "color_bundle_operator_packet_fill_attempt_certificate.json"
DATA = REPO / "candidate_data" / "color_bundle_operator_packet_fill_attempt.candidate.json"
NOTE = REPO / "proof_corpus" / "Selected_Qa_SU3_Color_Bundle_Operator_Packet_Fill_Attempt_v1.md"
SCRIPT = REPO / "scripts" / "build_color_bundle_operator_packet_fill_attempt.py"


def check(name: str, ok: bool, detail: object) -> bool:
    print(f"{'PASS' if ok else 'FAIL'}: {name} -- {detail}")
    return ok


def main() -> int:
    cert = json.loads(CERT.read_text(encoding="utf-8"))
    data = json.loads(DATA.read_text(encoding="utf-8"))
    note = NOTE.read_text(encoding="utf-8")
    proc = subprocess.run([sys.executable, str(SCRIPT)], cwd=REPO, text=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT, check=True)
    computed = json.loads(proc.stdout)
    fill = data["fill_result"]
    gates = data["gate_results"]
    checks = [
        check("status", cert["status"] == "QA_SU3_COLOR_BUNDLE_OPERATOR_PACKET_FILL_ATTEMPT_PARTIAL_SOURCE_OPEN", cert["status"]),
        check("script agreement", computed["what_closes"] == cert["what_closes"], computed["what_closes"]),
        check("domain imported", fill["domain_constraints_imported"] is True and gates["domain_compatibility"].startswith("PARTIAL"), gates),
        check("templates found", fill["strominger_hym_templates_found"] is True, data["source_templates"]),
        check("source missing", fill["same_branch_qa_su3_source_found"] is False, fill),
        check("operator missing", gates["operator_data"] == "FAIL_ENDOMORPHISM_E_AND_CURVATURE_DATA_MISSING", gates),
        check("finite part missing", gates["finite_part_data"] == "FAIL_HEAT_SPECTRUM_TORSION_MISSING", gates),
        check("retired HYM not used", fill["retired_hym_matrix_used"] is False, fill),
        check("no determinant closure", fill["determinant_computable_now"] is False and cert["closure_claimed"] is False, cert),
        check("note records next", cert["next_required_artifact"] in note and "operator layer" in note, NOTE),
        check("no fitting", cert["target_fitting_used"] is False and data["target_fitting_used"] is False, cert),
    ]
    print("\nSelected Qa/SU3 color-bundle operator packet fill attempt audit")
    return 0 if all(checks) else 1


if __name__ == "__main__":
    raise SystemExit(main())
