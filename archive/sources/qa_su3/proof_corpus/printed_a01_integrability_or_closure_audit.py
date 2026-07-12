"""Audit the printed A01 integrability/closure check."""

from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path


REPO = Path(__file__).resolve().parents[1]
CERT = REPO / "certificates" / "printed_a01_integrability_or_closure_certificate.json"
DATA = REPO / "candidate_data" / "printed_a01_integrability_or_closure.candidate.json"
NOTE = REPO / "proof_corpus" / "Selected_Qa_SU3_Printed_A01_Integrability_or_Closure_v1.md"
SCRIPT = REPO / "scripts" / "audit_printed_a01_integrability_or_closure.py"


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
    gates = data["gate_results"]
    nonzero = data["nonzero_curvature_entries"]
    checks = [
        check("status", cert["status"] == "QA_SU3_PRINTED_A01_AUDITED_INTEGRABILITY_FAILS_OPERATOR_CLOSURE_REJECTED", cert["status"]),
        check("script agreement", computed["what_closes"] == cert["what_closes"], computed["what_closes"]),
        check("printed A01 found", gates["printed_A01_found"] is True and gates["printed_integrability_claim_found"] is True, data["printed_A01"]),
        check("integrability fails", gates["integrability_fails"] is True and gates["computed_dbar_A_plus_A_wedge_A_zero"] is False, gates),
        check("nonzero 12 curvature", any(item["entry"] == [1, 2] and "e12" in item["curvature_02"] for item in nonzero), nonzero),
        check("opposite sign still nonzero", data["opposite_sign_check"]["curvature_02_if_dbar_e3_is_minus_e12"]["e12"] == "-mu", data["opposite_sign_check"]),
        check("printed A01 rejected", gates["printed_A01_can_supply_DE_closure"] is False and gates["selected_DE_or_rhoE_matrix_source_found"] is False, gates),
        check("closure not claimed", cert["closure_claimed"] is False and cert["what_remains_open"]["qa_su3_packet_closed"] is False, cert),
        check("no target fitting", cert["target_fitting_used"] is False and data["target_fitting_used"] is False, cert),
        check("note records residual", "F^{0,2}_{12} = mu" in note and "cannot be the selected operator exit" in note, NOTE),
    ]
    print("\nSelected Qa/SU3 printed A01 integrability or closure audit")
    return 0 if all(checks) else 1


if __name__ == "__main__":
    raise SystemExit(main())
