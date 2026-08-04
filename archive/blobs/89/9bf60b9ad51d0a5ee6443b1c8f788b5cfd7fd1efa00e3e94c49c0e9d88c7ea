"""Audit the inverse Qa/SU3 first search run artifact."""

from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path


REPO = Path(__file__).resolve().parents[1]
CERT = REPO / "certificates" / "inverse_qa_su3_first_search_run_certificate.json"
DATA = REPO / "candidate_data" / "inverse_qa_su3_first_search_run.candidate.json"
NOTE = REPO / "proof_corpus" / "MTT_Inverse_Qa_SU3_First_Search_Run_v1.md"
SCRIPT = REPO / "scripts" / "build_inverse_qa_su3_first_search_run.py"

REQUIRED_ROUTES = {
    "finite_cech_dolbeault_cochain_packet",
    "same_source_DE_dotD_or_rhoE_response",
    "fixed_gerbe_Bfield_or_period_selector",
    "a01_de_operator_exit_acceptance_gate",
    "q79_s3_finite_torsion_pattern",
    "pure_convenience_solve_gf_zero",
}


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
    run = data["search_run"]
    routes = data["ranked_candidates"]
    route_ids = {row["route_id"] for row in routes}
    totals = [row["scores"]["total"] for row in routes]
    rejected = {row["route_id"]: row["rejection_reason"] for row in routes if row["rejection_reason"]}
    sources_present = all(body["present"] for body in data["source_status"].values())
    checks = [
        check("status", cert["status"] == "MTT_INVERSE_QA_SU3_FIRST_SEARCH_RUN_EXECUTED_CANDIDATES_RANKED_NO_PROMOTION", cert["status"]),
        check("script agreement", computed["what_closes"] == cert["what_closes"], computed["what_closes"]),
        check("sources present", sources_present, data["source_status"]),
        check("routes complete", REQUIRED_ROUTES.issubset(route_ids), route_ids),
        check("scores sorted", totals == sorted(totals, reverse=True), totals),
        check("run executed", gates["numeric_search_executed"] is True and gates["ranked_candidate_packets_built"] is True, gates),
        check("no forbidden targets", run["forbidden_targets_used"] == [] and gates["forbidden_targets_used"] is False, run),
        check("no measured constants", run["measured_constants_used"] is False and gates["measured_constants_used"] is False, run),
        check("top candidate cochain", data["top_candidate"]["route_id"] == "finite_cech_dolbeault_cochain_packet", data["top_candidate"]),
        check("convenience solve rejected", rejected.get("pure_convenience_solve_gf_zero") == "TARGET_OR_CONVENIENCE_FIT_ONLY" and gates["convenience_solve_rejected"] is True, rejected),
        check("q79 import rejected", rejected.get("q79_s3_finite_torsion_pattern") == "OFF_BRANCH_PATTERN_ONLY" and gates["off_branch_q79_rejected"] is True, rejected),
        check("no promotion", gates["candidate_promoted"] is False and cert["what_remains_open"]["selected_Qa_SU3_color_operator_packet"] is True, cert),
        check("closure not claimed", gates["sm_parity_closure_claimed"] is False and gates["no_knob_closure_claimed"] is False and cert["closure_claimed"] is False, cert),
        check("next artifact selected", data["next_required_artifact"] == "MTT_Selected_Qa_SU3_Finite_Cochain_Construction_Plan_v1", data["next_required_artifact"]),
        check("note records verdict", "does not promote a selected packet" in note and "finite Cech/Dolbeault cochain packet" in note, NOTE),
    ]
    print("\nMTT inverse Qa/SU3 first search run audit")
    return 0 if all(checks) else 1


if __name__ == "__main__":
    raise SystemExit(main())
