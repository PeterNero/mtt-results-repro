"""Audit source-identity transport proof attempt."""

from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SCRIPT = ROOT / "scripts" / "build_selected_heterotic_orientedphifin_sourceidentitytransport_proofattempt.py"
DATA = ROOT / "candidate_data" / "selected_heterotic_orientedphifin_sourceidentitytransport_proofattempt.candidate.json"
REDUCTION = ROOT / "candidate_data" / "selected_heterotic_orientedphifin_sourceidentitytransport_reduction_to_sourcebranchidentity.json"
CERT = ROOT / "certificates" / "selected_heterotic_orientedphifin_sourceidentitytransport_proofattempt_certificate.json"
NOTE = ROOT / "proof_corpus" / "Selected_Heterotic_OrientedPhiFin_SourceIdentityTransport_ProofAttempt_v1.md"

STATUS = "HETEROTIC_ORIENTEDPHIFIN_SOURCEIDENTITYTRANSPORT_PROOFATTEMPT_REDUCED_TO_SOURCEBRANCHIDENTITY"
NEXT = "Selected_Heterotic_OrientedPhiFin_SourceBranchIdentity_Emission_or_NoGo_v1"


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
    reduction = load(REDUCTION)
    cert = load(CERT)
    note = NOTE.read_text(encoding="utf-8")
    decision = data["decision"]
    sub = data["sublemma_attempts"]

    check("status", data["status"] == STATUS and cert["status"] == STATUS, (data["status"], cert["status"]))
    check("next", decision["next_required_artifact"] == NEXT and cert["next_required_artifact"] == NEXT, decision)
    check("source identity still open", sub["source_branch_identity"]["unconditional_closed"] is False and decision["source_branch_identity_closed"] is False, sub["source_branch_identity"])
    check("coemission conditional only", sub["operator_coemission_before_finite_comparison"]["conditional_closure_ready"] is True and sub["operator_coemission_before_finite_comparison"]["unconditional_closed"] is False, sub["operator_coemission_before_finite_comparison"])
    check("no lift conditional only", sub["no_lift_audit_replay_from_emitted_source"]["conditional_closure_ready"] is True and sub["no_lift_audit_replay_from_emitted_source"]["unconditional_closed"] is False, sub["no_lift_audit_replay_from_emitted_source"])
    check("reduced to one leaf", decision["transport_reduced_to_single_leaf"] is True and decision["single_remaining_leaf"] == "source_branch_identity", decision)
    check("reduction packet", reduction["status"] == "REDUCED_TO_SOURCE_BRANCH_IDENTITY" and reduction["remaining_unconditional_leaf"] == "source_branch_identity", reduction)
    check("conditional implications", all(reduction["proved_conditional_implications"].values()), reduction["proved_conditional_implications"])
    check("no export closure", decision["selected_connection_witness_export_closed"] is False and cert["selected_connection_witness_export_closed"] is False, cert)
    check("no logdet promotion", decision["oriented_logdet_promoted"] is False and cert["oriented_logdet_promoted"] is False, cert)
    check("guardrails", all(v is True for k, v in data["guardrails"].items() if k != "target_fitting_used") and data["guardrails"]["target_fitting_used"] is False, data["guardrails"])
    check("note records reduction", NEXT in note and str(REDUCTION.relative_to(ROOT)) in note and "transport_reduced_to_single_leaf = true" in note, NOTE)

    print("\nSelected heterotic oriented Phi_fin source-identity transport proof attempt audit passed")


if __name__ == "__main__":
    main()
