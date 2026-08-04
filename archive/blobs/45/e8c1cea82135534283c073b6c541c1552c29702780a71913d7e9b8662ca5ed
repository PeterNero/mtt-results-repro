"""Audit smooth-identity trace-lift or complement-quotient fill attempt."""

from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SCRIPT = ROOT / "scripts" / "build_selected_heterotic_projectiverhoe_smoothidentity_tracelift_or_complementquotient_fillattempt.py"
DATA = ROOT / "candidate_data" / "selected_heterotic_projectiverhoe_smoothidentity_tracelift_or_complementquotient_fillattempt.candidate.json"
QUOTIENT = ROOT / "candidate_data" / "selected_heterotic_projectiverhoe_internal_complement_quotient_theorem.json"
REMAINING = ROOT / "candidate_data" / "selected_heterotic_projectiverhoe_after_internal_complement_quotient_remaining.json"
CERT = ROOT / "certificates" / "selected_heterotic_projectiverhoe_smoothidentity_tracelift_or_complementquotient_fillattempt_certificate.json"
NOTE = ROOT / "proof_corpus" / "Selected_Heterotic_ProjectiveRhoE_SmoothIdentity_TraceLift_or_ComplementQuotient_FillAttempt_v1.md"

STATUS = "HETEROTIC_PROJECTIVERHOE_INTERNAL_COMPLEMENT_QUOTIENT_CLOSED_SMOOTH_TRACE_IDENTITY_OPEN"
NEXT = "Selected_Heterotic_ProjectiveRhoE_PhysicalNormalization_or_SmoothEQa_SourceData_Request_v1"


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
    quotient = load(QUOTIENT)
    remaining = load(REMAINING)
    cert = load(CERT)
    note = NOTE.read_text(encoding="utf-8")
    decision = data["decision"]

    check("status", data["status"] == STATUS and cert["status"] == STATUS and quotient["status"] == "CLOSED_INTERNAL_REDUCED_DETERMINANT_ONLY", (data["status"], cert["status"], quotient["status"]))
    check("next artifact", decision["next_required_artifact"] == NEXT and cert["next_required_artifact"] == NEXT and remaining["next_required_artifact"] == NEXT, decision)
    check("internal complement quotient closed", decision["internal_complement_quotient_policy_closed"] is True and cert["internal_complement_quotient_policy_closed"] is True, decision)
    check("logdet preserved", decision["selected_internal_logdet_preserved"] is True and quotient["closed_claims"]["selected_internal_logdet"] == "log(2008)", quotient["closed_claims"])
    check("trace lift remains open", decision["smooth_trace_lift_closed"] is False and decision["trace_lift_current_source_nogo_retained"] is True and cert["smooth_trace_lift_closed"] is False, decision)
    check("smooth EQa remains open", decision["smooth_EQa_closed"] is False and cert["smooth_EQa_closed"] is False, decision)
    check("physical remains open", decision["physical_normalization_closed"] is False and cert["physical_normalization_closed"] is False, decision)
    check("quotient not smooth trace", quotient["not_claimed"]["smooth_trace_lift"] is True and quotient["not_claimed"]["smooth_E_Qa_matrix"] is True, quotient["not_claimed"])
    check("remaining extensions", "physical_normalization" in remaining["remaining_legal_extensions"] and "optional_smooth_source_identity" in remaining["remaining_legal_extensions"], remaining)
    check("cross checks", all(data["cross_checks"].values()), data["cross_checks"])
    check("guardrails", all(v is True for k, v in data["guardrails"].items() if k != "target_fitting_used") and data["guardrails"]["target_fitting_used"] is False, data["guardrails"])
    check("no closure overclaim", data["closure_claimed"] is False and quotient["closure_claimed"] is False and remaining["closure_claimed"] is False, cert)
    check("note records outputs", str(QUOTIENT.relative_to(ROOT)) in note and str(REMAINING.relative_to(ROOT)) in note and NEXT in note, NOTE)

    print("\nSelected heterotic projective rho_E smooth identity trace-lift/complement quotient fill audit")


if __name__ == "__main__":
    main()
