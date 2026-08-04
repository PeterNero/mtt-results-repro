"""Audit oriented Phi_fin source-identity / oriented-BN operator-emission theorem."""

from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SCRIPT = ROOT / "scripts" / "build_selected_heterotic_orientedphifin_sourceidentity_or_orientedbn_operatoremission.py"
DATA = ROOT / "candidate_data" / "selected_heterotic_orientedphifin_sourceidentity_or_orientedbn_operatoremission.candidate.json"
FRONTIER = ROOT / "candidate_data" / "selected_heterotic_orientedphifin_sourceidentity_single_frontier.json"
CERT = ROOT / "certificates" / "selected_heterotic_orientedphifin_sourceidentity_or_orientedbn_operatoremission_certificate.json"
NOTE = ROOT / "proof_corpus" / "Selected_Heterotic_OrientedPhiFin_SourceIdentity_or_OrientedBN_OperatorEmission_v1.md"

STATUS = "HETEROTIC_ORIENTEDPHIFIN_SOURCEIDENTITY_OPERATORPAYLOAD_READY_SINGLE_SOURCE_FRONTIER_OPEN"
NEXT = "Selected_Heterotic_OrientedPhiFin_SourceOwnership_Theorem_or_SmoothEQa_Quotient_v1"


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
    frontier = load(FRONTIER)
    cert = load(CERT)
    note = NOTE.read_text(encoding="utf-8")
    decision = data["decision"]
    support = frontier["support_closed"]
    open_source = frontier["not_yet_source_owned"]

    check("status", data["status"] == STATUS and cert["status"] == STATUS, (data["status"], cert["status"]))
    check("next artifact", decision["next_required_artifact"] == NEXT and cert["next_required_artifact"] == NEXT, decision)
    check("all support closed", all(support.values()) and frontier["operator_payload_ready"] is True, support)
    check("decision records ready payload", decision["operator_payload_ready"] is True and decision["support_closed_count"] == decision["support_required_count"], decision)
    check("single frontier built", decision["single_root_frontier_built"] is True and frontier["status"] == "SINGLE_SOURCE_OWNERSHIP_FRONTIER_OPEN", frontier)
    check("source ownership remains open", open_source["heterotic_QaSU3_owns_positive_PhiFin_DE_on_oriented_BN"] is False and open_source["smooth_EQa_or_threshold_complex_has_finite_quotient_equal_to_packet"] is False, open_source)
    check("finitepart remains open", open_source["finitepart_trace_identity_after_source_ownership"] is False and decision["finitepart_trace_identity_closed"] is False, open_source)
    check("no promotion", decision["heterotic_source_ownership_closed"] is False and decision["oriented_threshold_value_promoted"] is False, decision)
    check("guardrails", all(value is True for key, value in data["guardrails"].items() if key != "target_fitting_used") and data["guardrails"]["target_fitting_used"] is False, data["guardrails"])
    check("no overclaim", data["closure_claimed"] is False and cert["closure_claimed"] is False and data["target_fitting_used"] is False, cert)
    check("note records frontier", str(FRONTIER.relative_to(ROOT)) in note and NEXT in note, NOTE)

    print("\nSelected heterotic oriented Phi_fin source-identity/operator-emission audit passed")


if __name__ == "__main__":
    main()
