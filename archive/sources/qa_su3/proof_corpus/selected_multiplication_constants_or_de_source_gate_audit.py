"""Audit the selected multiplication constants or D_E source gate."""

from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path


REPO = Path(__file__).resolve().parents[1]
CERT = REPO / "certificates" / "selected_multiplication_constants_or_de_source_gate_certificate.json"
DATA = REPO / "candidate_data" / "selected_multiplication_constants_or_de_source_gate.candidate.json"
NOTE = REPO / "proof_corpus" / "Selected_Qa_SU3_Selected_Multiplication_Constants_or_DE_Source_v1.md"
SCRIPT = REPO / "scripts" / "build_selected_multiplication_constants_or_de_source_gate.py"


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
    analysis = data["formal_equation_analysis"]
    gates = data["gate_results"]
    route_ids = [row["route_id"] for row in data["route_tests"]]
    checks = [
        check("status", cert["status"] == "QA_SU3_SELECTED_MULTIPLICATION_CONSTANTS_OR_DE_SOURCE_GATE_BUILT_VALUES_OPEN", cert["status"]),
        check("script agreement", computed["what_closes"] == cert["what_closes"], computed["what_closes"]),
        check("gf equation imported", gates["gf_zero_equation_imported"] is True and "mu_1*a_1*b_1" in analysis["gf_zero_equation"], analysis),
        check("formal variable count", analysis["formal_variable_count"] == 15 and analysis["equation_count"] == 1, analysis),
        check("underdetermined", gates["formal_under_determination_proved"] is True and analysis["formal_dimension_if_nonzero_coefficients"] == 14, analysis),
        check("convenience rejected", gates["convenience_solve_rejected"] is True and "pure_convenience_solve_gf_zero" in route_ids, data["route_tests"]),
        check("primary routes", gates["primary_routes_identified"] is True, data["route_tests"]),
        check("selected values open", gates["selected_mu_i_supplied"] is False and gates["selected_f_g_entries_supplied"] is False, gates),
        check("no closure/no target fitting", cert["closure_claimed"] is False and cert["target_fitting_used"] is False, cert),
        check("note records frontier", cert["next_required_artifact"] in note and "underdetermined" in note.lower(), NOTE),
    ]
    print("\nSelected Qa/SU3 multiplication constants or D_E source gate audit")
    return 0 if all(checks) else 1


if __name__ == "__main__":
    raise SystemExit(main())
