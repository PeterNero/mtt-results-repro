"""Audit physical-normalization or smooth-EQa source-data request."""

from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SCRIPT = ROOT / "scripts" / "build_selected_heterotic_projectiverhoe_physicalnormalization_or_smootheqa_sourcedata_request.py"
DATA = ROOT / "candidate_data" / "selected_heterotic_projectiverhoe_physicalnormalization_or_smootheqa_sourcedata_request.candidate.json"
REQUEST = ROOT / "candidate_data" / "selected_heterotic_projectiverhoe_physicalnormalization_or_smootheqa_source_request.json"
LOCK = ROOT / "candidate_data" / "selected_heterotic_projectiverhoe_internal_closure_lock_after_source_request.json"
CERT = ROOT / "certificates" / "selected_heterotic_projectiverhoe_physicalnormalization_or_smootheqa_sourcedata_request_certificate.json"
NOTE = ROOT / "proof_corpus" / "Selected_Heterotic_ProjectiveRhoE_PhysicalNormalization_or_SmoothEQa_SourceData_Request_v1.md"

STATUS = "HETEROTIC_PROJECTIVERHOE_INTERNAL_CLOSED_SOURCE_REQUEST_BUILT_PHYSICAL_SMOOTHEQA_OPEN"
NEXT = "Selected_Heterotic_ProjectiveRhoE_PhysicalAnchor_or_SmoothEQa_SourceFillAttempt_v1"


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
    request = load(REQUEST)
    lock = load(LOCK)
    cert = load(CERT)
    note = NOTE.read_text(encoding="utf-8")
    decision = data["decision"]

    check("status", data["status"] == STATUS and cert["status"] == STATUS and request["status"] == "SOURCE_DATA_REQUIRED", (data["status"], cert["status"], request["status"]))
    check("next artifact", decision["next_required_artifact"] == NEXT and cert["next_required_artifact"] == NEXT and lock["next_required_artifact"] == NEXT, decision)
    check("internal branch locked", decision["internal_branch_locked"] is True and cert["internal_branch_locked"] is True and lock["locked_claims"]["selected_internal_logdet"] == "log(2008)", lock)
    check("source request built", decision["source_request_built"] is True and cert["source_request_built"] is True, decision)
    check("physical lane open with leaves", all(value is None for value in request["lane_A_physical_normalization_required"].values()) and len(request["lane_A_physical_normalization_required"]) == 7, request["lane_A_physical_normalization_required"])
    check("smooth lane open with leaves", all(value is None for value in request["lane_B_optional_smooth_EQa_required"].values()) and len(request["lane_B_optional_smooth_EQa_required"]) == 7, request["lane_B_optional_smooth_EQa_required"])
    check("available internal branch recorded", request["already_closed_internal_branch"]["finite_internal_logdet"] == "log(2008)" and request["already_closed_internal_branch"]["internal_complement_quotient_policy"] is True, request["already_closed_internal_branch"])
    check("slots known but open", decision["physical_slots_identified_but_values_open"] is True and decision["smooth_geometry_support_present_but_operator_values_open"] is True, decision)
    check("no more internal computation", decision["no_more_internal_computation_required_for_log2008"] is True, decision)
    check("locked nonclaims", all(lock["locked_nonclaims"].values()), lock["locked_nonclaims"])
    check("guardrails", all(v is True for k, v in data["guardrails"].items() if k != "target_fitting_used") and data["guardrails"]["target_fitting_used"] is False, data["guardrails"])
    check("no closure overclaim", data["closure_claimed"] is False and request["closure_claimed"] is False and lock["closure_claimed"] is False and cert["closure_claimed"] is False, cert)
    check("note records outputs", str(REQUEST.relative_to(ROOT)) in note and str(LOCK.relative_to(ROOT)) in note and NEXT in note, NOTE)

    print("\nSelected heterotic projective rho_E physical-normalization / smooth-EQa source request audit")


if __name__ == "__main__":
    main()
