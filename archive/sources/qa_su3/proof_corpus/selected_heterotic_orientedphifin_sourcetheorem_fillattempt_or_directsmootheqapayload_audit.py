"""Audit oriented Phi_fin source-theorem fill attempt / direct smooth E_Qa payload gate."""

from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SCRIPT = ROOT / "scripts" / "build_selected_heterotic_orientedphifin_sourcetheorem_fillattempt_or_directsmootheqapayload.py"
DATA = ROOT / "candidate_data" / "selected_heterotic_orientedphifin_sourcetheorem_fillattempt_or_directsmootheqapayload.candidate.json"
PACKET = ROOT / "candidate_data" / "selected_heterotic_orientedphifin_sourcetheorem_fillattempt_packet.json"
CERT = ROOT / "certificates" / "selected_heterotic_orientedphifin_sourcetheorem_fillattempt_or_directsmootheqapayload_certificate.json"
NOTE = ROOT / "proof_corpus" / "Selected_Heterotic_OrientedPhiFin_SourceTheorem_FillAttempt_or_DirectSmoothEQaPayload_v1.md"

STATUS = "HETEROTIC_ORIENTEDPHIFIN_SOURCETHEOREM_FILLATTEMPT_VALUES_OPEN_END0_OR_RHOE_NEXT"
NEXT = "Selected_Heterotic_OrientedPhiFin_EndE_Basis_or_NonidentityRhoE_ValueInsertion_v1"


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
    packet = load(PACKET)
    cert = load(CERT)
    note = NOTE.read_text(encoding="utf-8")
    decision = data["decision"]
    leaves = packet["leaf_status_after_attempt"]

    check("status", data["status"] == STATUS and cert["status"] == STATUS, (data["status"], cert["status"]))
    check("next artifact", decision["next_required_artifact"] == NEXT and cert["next_required_artifact"] == NEXT, decision)
    check("three forms attempted", decision["attempted_source_theorem_forms_count"] == 3 and all(item["attempted"] for item in packet["attempted_forms"].values()), packet["attempted_forms"])
    check("kernel carried only", decision["closed_leaf_count"] == 1 and leaves["kernel_policy_closed"]["closed"] is True and decision["new_leaves_closed"] == 0, decision)
    check("source context partial", leaves["source_certificate_closed"]["partial_source_context_closed"] is True and leaves["source_certificate_closed"]["closed"] is False, leaves["source_certificate_closed"])
    check("embedding not functor", leaves["quotient_functor_closed"]["partial_embedding_support"] is True and leaves["quotient_functor_closed"]["closed"] is False, leaves["quotient_functor_closed"])
    check("operator identity open", leaves["operator_identity_closed"]["closed"] is False and leaves["operator_identity_closed"]["support"]["C_tau_orientation"] is True, leaves["operator_identity_closed"])
    check("finitepart open", leaves["finitepart_trace_identity_closed"]["closed"] is False and "PhiFin_all_positive_logdet" in leaves["finitepart_trace_identity_closed"]["support"], leaves["finitepart_trace_identity_closed"])
    check("next value object", decision["next_value_object_selected"] == "EndE_domain_basis_or_nonidentity_rhoE", packet["next_value_object"])
    check("no promotion", decision["finite_quotient_identity_constructed"] is False and decision["oriented_threshold_logdet_promoted"] is False, decision)
    check("guardrails", all(value is True for key, value in data["guardrails"].items() if key != "target_fitting_used") and data["guardrails"]["target_fitting_used"] is False, data["guardrails"])
    check("no overclaim", data["closure_claimed"] is False and cert["closure_claimed"] is False and data["target_fitting_used"] is False, cert)
    check("note records packet", str(PACKET.relative_to(ROOT)) in note and NEXT in note, NOTE)

    print("\nSelected heterotic oriented Phi_fin source-theorem fill attempt audit")


if __name__ == "__main__":
    main()
