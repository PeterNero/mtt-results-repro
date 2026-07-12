"""Audit smooth-transition source-gap closure or direct-operator payload gate."""

from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SCRIPT = ROOT / "scripts" / "build_selected_heterotic_projectiverhoe_smoothtransition_sourcegap_closure_or_directoperatorpayload.py"
DATA = ROOT / "candidate_data" / "selected_heterotic_projectiverhoe_smoothtransition_sourcegap_closure_or_directoperatorpayload.candidate.json"
ACCEPTANCE = ROOT / "candidate_data" / "selected_heterotic_projectiverhoe_direct_operator_payload_acceptance_template.json"
FORK = ROOT / "candidate_data" / "selected_heterotic_projectiverhoe_transition_or_directoperator_closure_fork.json"
CERT = ROOT / "certificates" / "selected_heterotic_projectiverhoe_smoothtransition_sourcegap_closure_or_directoperatorpayload_certificate.json"
NOTE = ROOT / "proof_corpus" / "Selected_Heterotic_ProjectiveRhoE_SmoothTransitionSourceGap_Closure_or_DirectOperatorPayload_v1.md"

STATUS = "HETEROTIC_PROJECTIVERHOE_SOURCEGAP_FORK_BUILT_DIRECT_OPERATOR_PAYLOAD_TEMPLATE_OPEN"
NEXT = "Selected_Heterotic_ProjectiveRhoE_DirectOperatorPayload_FillAttempt_v1"


def check(label: str, condition: bool, detail: object) -> None:
    if not condition:
        print(f"FAIL: {label} -- {detail}")
        sys.exit(1)
    print(f"PASS: {label} -- {detail}")


def load(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def main() -> None:
    proc = subprocess.run([sys.executable, str(SCRIPT)], cwd=ROOT, text=True, capture_output=True)
    check("script reruns", proc.returncode == 0, proc.stdout + proc.stderr)

    data = load(DATA)
    acceptance = load(ACCEPTANCE)
    fork = load(FORK)
    cert = load(CERT)
    note = NOTE.read_text(encoding="utf-8")
    decision = data["decision"]

    check("status", data["status"] == STATUS and cert["status"] == STATUS and acceptance["status"] == "TEMPLATE_OPEN", (data["status"], cert["status"], acceptance["status"]))
    check("next artifact", decision["next_required_artifact"] == NEXT and cert["next_required_artifact"] == NEXT, decision)
    check("fork built", decision["sourcegap_fork_built"] is True and cert["sourcegap_fork_built"] is True and fork["selected_next_lane"] == "Lane_B_direct_same_branch_operator_payload", fork)
    check("lane A blocked correctly", decision["lane_A_formal_validators_pass"] is True and decision["lane_A_smooth_source_closed"] is False and decision["lane_A_current_source_nogo"] is True, decision)
    check("lane B selected", decision["lane_B_direct_operator_acceptance_template_built"] is True and decision["lane_B_selected_as_next_executable"] is True, decision)
    check("available internal values", acceptance["already_available_internal_values"]["finite_internal_part"] == "log(2008)" and len(acceptance["already_available_internal_values"]["labels"]) == 11, acceptance["already_available_internal_values"])
    check("acceptance checks", all(acceptance["acceptance_checks"].values()), acceptance["acceptance_checks"])
    check("required payload open", all(value is None for value in acceptance["required_payload"].values()), acceptance["required_payload"])
    check("finite retained internal only", decision["selected_finite_internal_packet_retained"] is True and decision["internal_finitepart_retained"] is True and decision["physical_normalization_claimed"] is False, decision)
    check("direct payload still open", decision["direct_operator_payload_closed"] is False and cert["direct_operator_payload_closed"] is False, decision)
    check("guardrails", all(v is True for k, v in data["guardrails"].items() if k != "target_fitting_used") and data["guardrails"]["target_fitting_used"] is False, data["guardrails"])
    check("no closure or fitting", data["closure_claimed"] is False and acceptance["closure_claimed"] is False and fork["closure_claimed"] is False and cert["target_fitting_used"] is False, cert)
    check("note records fork and template", str(FORK.relative_to(ROOT)) in note and str(ACCEPTANCE.relative_to(ROOT)) in note and NEXT in note, NOTE)

    print("\nSelected heterotic projective rho_E source-gap/direct-operator fork audit")


if __name__ == "__main__":
    main()
