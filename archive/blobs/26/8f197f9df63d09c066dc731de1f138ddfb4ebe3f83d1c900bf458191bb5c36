"""Audit the internal-logdet to coupling-response bridge gate."""

from __future__ import annotations

import json
import math
import subprocess
import sys
from pathlib import Path


REPO = Path(__file__).resolve().parents[1]
CERT = REPO / "certificates" / "internal_logdet_to_coupling_response_bridge_certificate.json"
DATA = REPO / "candidate_data" / "internal_logdet_to_coupling_response_bridge.candidate.json"
NOTE = REPO / "proof_corpus" / "Selected_Qa_SU3_Internal_Logdet_to_Coupling_Response_Bridge_v1.md"
SCRIPT = REPO / "scripts" / "build_internal_logdet_to_coupling_response_bridge.py"


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
    payload = data["locked_finite_payload"]
    decision = data["decision"]
    routes = {route["route"]: route for route in data["tested_bridge_routes"]}
    guardrails = data["guardrails"]
    response = data["response_functional"]
    checks = [
        check("status", cert["status"] == "QA_SU3_INTERNAL_UNIT_RESPONSE_BRIDGE_CLOSED_PHYSICAL_CHI_QA_OPEN", cert["status"]),
        check("script agreement", computed["what_closes"] == cert["what_closes"], computed["what_closes"]),
        check("imports locked determinant", payload["determinant"] == 2008 and payload["finite_rank_logdet"] == "log(2008)", payload),
        check("numeric logdet", abs(payload["finite_rank_logdet_numeric"] - math.log(2008)) < 1e-12, payload["finite_rank_logdet_numeric"]),
        check("internal unit bridge closed", decision["internal_unit_response_bridge"] == "CLOSED_LOG_2008", decision),
        check("physical bridge stays open", decision["physical_coupling_bridge"] == "OPEN_SELECTED_CHI_QA_RESPONSE_FUNCTIONAL_REQUIRED", decision),
        check("next object is chi", decision["next_required_object"] == "Selected_Qa_SU3_Response_Functional_Chi_Qa_v1" and "chi_Qa" in response["minimal_form"], response),
        check("direct unit route scoped", routes["direct_unit_internal_response"]["status"] == "ACCEPTED_AS_INTERNAL_UNIT_CONVENTION_ONLY" and "not source-selected" in routes["direct_unit_internal_response"]["why_not_physical_closure"], routes["direct_unit_internal_response"]),
        check("QFT/heat/torsion/theta shortcuts rejected", all(routes[key]["status"] == "REJECTED_AS_CLOSURE_CURRENT_SOURCE" for key in ["one_loop_threshold", "heat_kernel_response", "torsion_response", "theta_or_retarded_overlap_kernel"]), routes),
        check("GR route kept out of internal determinant", routes["GR_surface_response"]["status"] == "ROUTED_OUT_OF_QA_SU3_INTERNAL_DETERMINANT", routes["GR_surface_response"]),
        check("no physical/full closure claimed", decision["full_electroweak_closure_now"] is False and decision["full_SM_closure_now"] is False, decision),
        check("guardrails block fitting and overpromotion", any("observed masses" in item for item in guardrails) and any("full SM closure" in item for item in guardrails), guardrails),
        check("note records exact split", "Delta_Qa_internal_units = log(2008)" in note and "physical coupling bridge = OPEN_SELECTED_CHI_QA_RESPONSE_FUNCTIONAL_REQUIRED" in note, NOTE),
    ]
    print("\nSelected Qa/SU3 internal logdet to coupling response bridge audit")
    return 0 if all(checks) else 1


if __name__ == "__main__":
    raise SystemExit(main())
