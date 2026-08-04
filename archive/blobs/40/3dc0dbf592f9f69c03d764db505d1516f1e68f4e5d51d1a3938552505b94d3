"""Audit the Qa/SU3 central period selector search."""

from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path


REPO = Path(__file__).resolve().parents[1]
CERT = REPO / "certificates" / "central_period_selector_search_certificate.json"
DATA = REPO / "candidate_data" / "central_period_selector_search.candidate.json"
NOTE = REPO / "proof_corpus" / "Selected_Qa_SU3_Central_Period_Selector_Search_v1.md"
SCRIPT = REPO / "scripts" / "build_central_period_selector_search.py"


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
    routes = {row["route_id"]: row for row in data["route_tests"]}
    checks = [
        check("status", cert["status"] == "QA_SU3_CENTRAL_PERIOD_SELECTOR_SEARCH_COMPLETE_SELECTOR_NOT_FOUND", cert["status"]),
        check("script agreement", computed["what_closes"] == cert["what_closes"], computed["what_closes"]),
        check("scalar target positive", data["scalar_target"]["R4_over_alpha_prime_required"] > 0, data["scalar_target"]),
        check("exact ratio not independently selected", routes["exact_A_unit_ratio_search"]["promotes_selector"] is False and not routes["exact_A_unit_ratio_search"]["independent_selector_hits"], routes["exact_A_unit_ratio_search"]),
        check("q79 retained as guardrail", gates["q79_nontrivial_finite_pattern_found"] is True and gates["q79_pattern_promoted_to_Qa_SU3"] is False, gates),
        check("FCC method identified", gates["superset_FCC_method_identified"] is True and routes["fcc_superset_selector_route"]["promotes_selector"] is False, routes["fcc_superset_selector_route"]),
        check("selector not found", gates["period_selector_found"] is False and gates["gerbe_period_promotion_allowed"] is False, gates),
        check("operator exit still required", gates["A01_DE_or_selected_operator_exit_still_required"] is True and cert["what_remains_open"]["selected_D_E_or_rho_E_operator_exit"] is True, cert),
        check("closure not claimed", cert["closure_claimed"] is False and cert["what_remains_open"]["qa_su3_packet_closed"] is False, cert),
        check("no target fitting", cert["target_fitting_used"] is False and data["target_fitting_used"] is False, cert),
        check("note records next packet", cert["next_required_artifact"] in note and "No same-branch selector was found" in note, NOTE),
    ]
    print("\nSelected Qa/SU3 central period selector search audit")
    return 0 if all(checks) else 1


if __name__ == "__main__":
    raise SystemExit(main())
