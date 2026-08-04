"""Audit the oriented Phi_fin finite-quotient identity source-theorem gate."""

from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SCRIPT = ROOT / "scripts" / "build_selected_heterotic_orientedphifin_finitequotientidentity_sourcetheorem_or_smootheqapayload.py"
DATA = ROOT / "candidate_data" / "selected_heterotic_orientedphifin_finitequotientidentity_sourcetheorem_or_smootheqapayload.candidate.json"
REQUEST = ROOT / "candidate_data" / "selected_heterotic_orientedphifin_finitequotientidentity_source_theorem_request.json"
CERT = ROOT / "certificates" / "selected_heterotic_orientedphifin_finitequotientidentity_sourcetheorem_or_smootheqapayload_certificate.json"
NOTE = ROOT / "proof_corpus" / "Selected_Heterotic_OrientedPhiFin_FiniteQuotientIdentity_SourceTheorem_or_SmoothEQaPayload_v1.md"

STATUS = "HETEROTIC_ORIENTEDPHIFIN_FINITEQUOTIENT_SOURCE_THEOREM_REQUEST_BUILT_KERNEL_POLICY_CLOSED"
NEXT = "Selected_Heterotic_OrientedPhiFin_SourceTheorem_FillAttempt_or_DirectSmoothEQaPayload_v1"


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
    cert = load(CERT)
    note = NOTE.read_text(encoding="utf-8")
    decision = data["decision"]
    leaves = data["leaf_status"]

    check("status", data["status"] == STATUS and cert["status"] == STATUS, (data["status"], cert["status"]))
    check("next artifact", decision["next_required_artifact"] == NEXT and cert["next_required_artifact"] == NEXT, decision)
    check("one leaf closed", decision["closed_leaf_count"] == 1 and decision["remaining_open_leaf_count"] == 5, decision)
    check("kernel policy closed only", leaves["kernel_policy_closed"]["closed"] is True and all(leaves[key]["closed"] is False for key in leaves if key != "kernel_policy_closed"), leaves)
    check("source request built", decision["source_theorem_request_built"] is True and request["status"] == "SOURCE_THEOREM_REQUIRED", request)
    check("request lists five missing leaves", len(request["must_emit"]) == 5 and "kernel_policy_closed" in request["already_closed"], request)
    check("support imported", leaves["operator_identity_closed"]["support"]["ctau_orientation_operator_closed"] is True and leaves["operator_identity_closed"]["support"]["same_domain_commutation_table_complete"] is True, leaves["operator_identity_closed"])
    check("no quotient identity", decision["finite_quotient_identity_constructed"] is False and decision["heterotic_threshold_magnitude_promoted"] is False, decision)
    check("current source nogo", decision["current_source_nogo"] is True and decision["mathematical_impossibility_claimed"] is False, decision)
    check("guardrails", all(value is True for key, value in data["guardrails"].items() if key != "target_fitting_used") and data["guardrails"]["target_fitting_used"] is False, data["guardrails"])
    check("no overclaim", data["closure_claimed"] is False and cert["closure_claimed"] is False and data["target_fitting_used"] is False, cert)
    check("note records request", str(REQUEST.relative_to(ROOT)) in note and NEXT in note, NOTE)

    print("\nSelected heterotic oriented Phi_fin finite-quotient identity source-theorem audit")


if __name__ == "__main__":
    main()
