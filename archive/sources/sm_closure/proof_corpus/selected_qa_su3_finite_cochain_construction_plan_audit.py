"""Audit the selected Qa/SU3 finite cochain construction plan artifact."""

from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path


REPO = Path(__file__).resolve().parents[1]
CERT = REPO / "certificates" / "selected_qa_su3_finite_cochain_construction_plan_certificate.json"
DATA = REPO / "candidate_data" / "selected_qa_su3_finite_cochain_construction_plan.candidate.json"
NOTE = REPO / "proof_corpus" / "MTT_Selected_Qa_SU3_Finite_Cochain_Construction_Plan_v1.md"
SCRIPT = REPO / "scripts" / "build_selected_qa_su3_finite_cochain_construction_plan.py"

REQUIRED_STEPS = {
    "C1_select_source_convention",
    "C2_solve_full_nil_theta_cocycle",
    "C3_construct_section_or_cochain_bases",
    "C4_compute_product_tables",
    "C5_extract_f_g_entries",
    "C6_bridge_operator_response",
    "C7_admissibility_retention",
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
    steps = {row["id"] for row in data["construction_steps"]}
    sources_present = all(body["present"] for body in data["source_status"].values())
    blocked = " ".join(data["attempt_result"]["blocked_reasons"]).lower()
    scaffold = data["candidate_primitive_ansatz_policy"]
    checks = [
        check("status", cert["status"] == "MTT_SELECTED_QA_SU3_FINITE_COCHAIN_CONSTRUCTION_PLAN_BUILT_ATTEMPT_BLOCKED_BY_CURRENT_SOURCE_NO_GO", cert["status"]),
        check("script agreement", computed["what_closes"] == cert["what_closes"], computed["what_closes"]),
        check("sources present", sources_present, data["source_status"]),
        check("steps complete", REQUIRED_STEPS.issubset(steps), steps),
        check("eleven spaces lifted", gates["eleven_spaces_lifted"] is True and data["lifted_packet"]["space_count"] == 11, data["lifted_packet"]["space_count"]),
        check("five product pairs lifted", gates["five_product_pairs_lifted"] is True and data["lifted_packet"]["typed_product_pair_count"] == 5, data["lifted_packet"]["typed_product_pair_count"]),
        check("charge products land in P", gates["charge_products_land_in_P"] is True, gates),
        check("twist cancellation lifted", gates["twist_cancellation_lifted"] is True, gates),
        check("attempted solve", gates["attempted_selected_source_solve"] is True and data["attempt_result"]["attempted_now"] is True, data["attempt_result"]),
        check("current source no-go imported", gates["current_source_no_go_imported"] is True and data["attempt_result"]["current_source_no_go_imported"] is True, data["attempt_result"]),
        check("blocked reasons complete", "selected finite bases absent" in blocked and "selected d_e" in blocked, data["attempt_result"]["blocked_reasons"]),
        check("primitive scaffold not promoted", scaffold["primitive_one_generator_scaffold_allowed"] is True and scaffold["primitive_one_generator_scaffold_promoted"] is False and gates["primitive_scaffold_promoted"] is False, scaffold),
        check("selected packet still open", gates["selected_finite_cochain_packet_supplied"] is False and gates["selected_Qa_SU3_packet_closed"] is False, gates),
        check("closure not claimed", gates["sm_parity_closure_claimed"] is False and gates["no_knob_closure_claimed"] is False and cert["closure_claimed"] is False, cert),
        check("no target fitting", data["target_fitting_used"] is False and cert["target_fitting_used"] is False, cert),
        check("note records scoped no-go", "current-source no-go" in note and "not claim that Qa/SU3 closure is mathematically impossible" in note, NOTE),
        check("next artifact selected", data["next_required_artifact"] == "MTT_Selected_Qa_SU3_Operator_Source_Import_Audit_v1", data["next_required_artifact"]),
    ]
    print("\nMTT selected Qa/SU3 finite cochain construction plan audit")
    return 0 if all(checks) else 1


if __name__ == "__main__":
    raise SystemExit(main())
