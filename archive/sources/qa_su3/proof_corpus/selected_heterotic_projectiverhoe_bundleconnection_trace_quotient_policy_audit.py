"""Audit projective rho_E bundle-connection/trace/quotient-policy replay."""

from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SCRIPT = ROOT / "scripts" / "build_selected_heterotic_projectiverhoe_bundleconnection_trace_quotient_policy.py"
DATA = ROOT / "candidate_data" / "selected_heterotic_projectiverhoe_bundleconnection_trace_quotient_policy.candidate.json"
CERT = ROOT / "certificates" / "selected_heterotic_projectiverhoe_bundleconnection_trace_quotient_policy_certificate.json"
CONTRACT = ROOT / "candidate_data" / "selected_heterotic_projectiverhoe_smooth_trace_lift_or_eqa_finitepart_contract.json"
NOTE = ROOT / "proof_corpus" / "Selected_Heterotic_ProjectiveRhoE_BundleConnection_RepresentationTrace_QuotientPolicy_v1.md"

STATUS = "HETEROTIC_PROJECTIVERHOE_BUNDLECONNECTION_TRACE_QUOTIENT_POLICY_FINITE_INTERNAL_CLOSED_SMOOTH_LIFT_OPEN"
NEXT = "Selected_Heterotic_ProjectiveRhoE_SmoothTraceLift_or_EQaFinitePartOperator_v1"


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
    cert = load(CERT)
    contract = load(CONTRACT)
    note = NOTE.read_text(encoding="utf-8")

    check("status", data["status"] == STATUS and cert["status"] == STATUS, (data["status"], cert["status"]))
    check("next artifact", data["decision"]["next_required_artifact"] == NEXT and cert["next_required_artifact"] == NEXT, data["decision"])
    check("finite internal policy closed", data["decision"]["finite_internal_trace_and_quotient_policy_closed"] is True and all(data["closed_subclaims"].values()), data["closed_subclaims"])
    check("finite domain exact", data["finite_internal_policy"]["finite_domain_closed"] is True and data["finite_internal_policy"]["finite_domain_labels"] == ["F1", "F2", "F3", "F4", "F5", "G1", "G2", "G3", "G4", "G5", "P"], data["finite_internal_policy"]["finite_domain_labels"])
    check("finite value log2008", data["finite_internal_policy"]["finite_threshold_value"] == "log(2008)", data["finite_internal_policy"])
    check("smooth open", data["decision"]["smooth_operator_identity_closed"] is False and not any(data["open_subclaims"].values()), data["open_subclaims"])
    check("standard embedding retired", data["decision"]["standard_embedding_route_retired_for_current_branch"] is True and data["smooth_bridge_policy"]["standard_embedding_route"]["retired_as_current_proof_source"] is True, data["smooth_bridge_policy"]["standard_embedding_route"])
    check("contract exact", contract["next_required_artifact"] == NEXT and contract["status"] == "OPEN", contract)
    check("contract forbids trace shortcut", "treat finite eleven-label trace as the smooth heat trace without a trace-lift theorem" in contract["forbidden_shortcuts"], contract["forbidden_shortcuts"])
    check("no E_Qa", data["decision"]["E_Qa_computed"] is False and cert["E_Qa_computed"] is False, cert)
    check("guardrails true except target flag false", all(v is True for k, v in data["guardrails"].items() if k != "target_fitting_used") and data["guardrails"]["target_fitting_used"] is False, data["guardrails"])
    check("note records boundary", "finite_internal_trace_and_quotient_policy_closed = true" in note and "A=GammaPlus" in note and NEXT in note, NOTE)

    print("\nSelected heterotic projective rho_E bundle trace quotient policy audit")


if __name__ == "__main__":
    main()
