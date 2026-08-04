"""Audit the selected Qa/SU3 response functional chi_Qa packet."""

from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path


REPO = Path(__file__).resolve().parents[1]
CERT = REPO / "certificates" / "selected_response_functional_chi_qa_certificate.json"
DATA = REPO / "candidate_data" / "selected_response_functional_chi_qa.candidate.json"
NOTE = REPO / "proof_corpus" / "Selected_Qa_SU3_Response_Functional_Chi_Qa_v1.md"
SCRIPT = REPO / "scripts" / "build_selected_response_functional_chi_qa.py"


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
    derivation = data["derivation"]
    inputs = derivation["inputs"]
    decision = data["decision"]
    routes = {route["route"]: route for route in data["tested_normalizations"]}
    guardrails = data["guardrails"]
    checks = [
        check("status", cert["status"] == "QA_SU3_SELECTED_FINITE_RESPONSE_FUNCTIONAL_CHI_QA_CLOSED_MEASURED_MATCH_OPEN", cert["status"]),
        check("script agreement", computed["what_closes"] == cert["what_closes"], computed["what_closes"]),
        check("retarded overlap selected", inputs["Pi_tw"] == [0, 0, 1] and inputs["G_ret_Pi_tw_Pi_tw"] == "1/8", inputs),
        check("finite trace selected", inputs["finite_trace_tau_squared"] == 8, inputs),
        check("chi computed", derivation["result"]["chi_Qa"] == "1" and derivation["result"]["selected"] is True, derivation["result"]),
        check("finite response closed", decision["finite_internal_coupling_normalization"] == "CLOSED" and decision["finite_response_functional"] == "Delta_Qa_selected_finite = log(2008)", decision),
        check("measured match open", decision["measured_electroweak_or_running_coupling_match"] == "OPEN" and decision["full_SM_closure_now"] is False, decision),
        check("unit declaration replaced", routes["bare_unit_declaration"]["status"] == "REPLACED_BY_DERIVATION", routes["bare_unit_declaration"]),
        check("fit route rejected", routes["measured_coupling_fit"]["status"] == "REJECTED", routes["measured_coupling_fit"]),
        check("guardrails block physical overclaim", any("not a measured coupling" in item for item in guardrails) and any("sin^2" in item for item in guardrails), guardrails),
        check("note records product", "8 * 1/8" in note and "Delta_Qa_selected_finite" in note and "does not compute a measured" in note, NOTE),
    ]
    print("\nSelected Qa/SU3 response functional chi_Qa audit")
    return 0 if all(checks) else 1


if __name__ == "__main__":
    raise SystemExit(main())
