"""Audit the central-cocycle map source search or derivation artifact."""

from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path


REPO = Path(__file__).resolve().parents[1]
CERT = REPO / "certificates" / "central_cocycle_map_source_search_or_derivation_certificate.json"
DATA = REPO / "candidate_data" / "central_cocycle_map_source_search_or_derivation.candidate.json"
NOTE = REPO / "proof_corpus" / "Selected_Qa_SU3_Central_Cocycle_Map_Source_Search_or_Derivation_v1.md"
SCRIPT = REPO / "scripts" / "build_central_cocycle_map_source_search_or_derivation.py"


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
    result = data["source_search_result"]
    derivation = data["derivation_interface"]
    checks = [
        check("status", cert["status"] == "QA_SU3_CENTRAL_COCYCLE_MAP_SOURCE_SEARCH_DONE_DERIVATION_GATE_BUILT_VALUES_OPEN", cert["status"]),
        check("script agreement", computed["what_closes"] == cert["what_closes"], computed["what_closes"]),
        check("source search did not close", result["selected_Qa_SU3_source_packet_found"] is False and result["central_cocycle_map_verified"] is False, result),
        check("q79 guardrail found", result["q79_guardrail_packet_found"] is True, result),
        check("same branch Hessian language found", result["same_branch_hessian_language_found"] is True, result),
        check("actual Hessian/kernel open", result["actual_selected_H_sel_found"] is False and result["actual_retarded_kernel_found"] is False, result),
        check("response payload open", result["response_payload_found"] is False, result),
        check("derivation objects complete", set(derivation["objects_to_supply"]) == {"H_sel", "G_ret", "Pi_tw", "tau", "response"}, derivation["objects_to_supply"]),
        check("acceptance equations include cocycle and twist", any("delta tau" in item for item in derivation["acceptance_equations"]) and any("tau(F_i)" in item for item in derivation["acceptance_equations"]), derivation["acceptance_equations"]),
        check("no closure", cert["closure_claimed"] is False and cert["what_remains_open"]["qa_su3_packet_closed"] is False, cert),
        check("no target fitting", cert["target_fitting_used"] is False and data["target_fitting_used"] is False and result["target_fitting_used"] is False, result),
        check("note records next", data["next_required_artifact"] in note and "H_sel" in note and "G_ret" in note, NOTE),
    ]
    print("\nSelected Qa/SU3 central-cocycle map source search or derivation audit")
    return 0 if all(checks) else 1


if __name__ == "__main__":
    raise SystemExit(main())
