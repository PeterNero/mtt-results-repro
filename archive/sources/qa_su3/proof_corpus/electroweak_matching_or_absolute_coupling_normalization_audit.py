"""Audit the Qa/SU3 electroweak matching / absolute coupling gate."""

from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path


REPO = Path(__file__).resolve().parents[1]
CERT = REPO / "certificates" / "electroweak_matching_or_absolute_coupling_normalization_certificate.json"
DATA = REPO / "candidate_data" / "electroweak_matching_or_absolute_coupling_normalization.candidate.json"
NOTE = REPO / "proof_corpus" / "Selected_Qa_SU3_Electroweak_Matching_or_Absolute_Coupling_Normalization_v1.md"
SCRIPT = REPO / "scripts" / "build_electroweak_matching_or_absolute_coupling_normalization.py"


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
    decision = data["decision"]
    payload = data["selected_internal_payload"]
    findings = data["cross_repo_findings"]
    routes = {route["route"]: route for route in data["tested_routes"]}
    guardrails = data["guardrails"]
    theta = findings["theta_electroweak_matching"]["scanned_clauses"]
    checks = [
        check("status", cert["status"] == "QA_SU3_ELECTROWEAK_MATCHING_INTERFACE_BUILT_ABSOLUTE_K_GAUGE_OPEN", cert["status"]),
        check("script agreement", computed["what_closes"] == cert["what_closes"], computed["what_closes"]),
        check("payload imported", payload["Qa_SU3_internal_overlap_payload"] == "log(2008)" and payload["chi_Qa"] == "1", payload),
        check("physical interface built", decision["allowed_conditional_formula"] == "1/g_Qa^2(mu_match)=K_gauge*log(2008)", decision),
        check("absolute gauge normalization open", decision["absolute_gauge_normalization_K_gauge"] == "OPEN", decision),
        check("U1 SU2 payloads open", decision["U1_SU2_same_scheme_payloads"] == "OPEN", decision),
        check("no measured closure", decision["no_knob_measured_electroweak_closure_now"] is False, decision),
        check("theta warning imported", theta["absolute_scale_not_fixed"] and theta["one_dimensionless_coupling_needed"], theta),
        check("nonSM physical absolute open", findings["nonsm_physical_action"]["physical_absolute_closed"] is False, findings["nonsm_physical_action"]),
        check("GR alpha open", findings["gr_alpha_or_action_unit"]["physical_numeric_alpha_selected"] is False and findings["gr_anchor_search"]["current_corpus_closes_alpha_phys"] is False, findings["gr_alpha_or_action_unit"]),
        check("direct absolute rejected", routes["direct_Qa_absolute_coupling"]["status"] == "REJECTED_AS_PHYSICAL_CLOSURE", routes["direct_Qa_absolute_coupling"]),
        check("theta interface accepted only as interface", routes["Theta_overlap_matching_scaffold"]["status"] == "ACCEPTED_AS_INTERFACE_ONLY", routes["Theta_overlap_matching_scaffold"]),
        check("full no knob route open", routes["full_no_knob_electroweak_closure"]["status"] == "OPEN", routes["full_no_knob_electroweak_closure"]),
        check("guardrails block target fitting", any("alpha_EM" in item for item in guardrails) and any("K_gauge=1" in item for item in guardrails), guardrails),
        check("note records decision", "K_gauge = OPEN" in note and "no-knob measured electroweak closure = false" in note, NOTE),
    ]
    print("\nSelected Qa/SU3 electroweak matching or absolute coupling normalization audit")
    return 0 if all(checks) else 1


if __name__ == "__main__":
    raise SystemExit(main())
