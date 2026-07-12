"""Audit minimal source-transport or connection-values packet."""

from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SCRIPT = ROOT / "scripts" / "build_selected_heterotic_orientedphifin_sourceidentitytransport_or_connectionvalues_minimalpacket.py"
DATA = ROOT / "candidate_data" / "selected_heterotic_orientedphifin_sourceidentitytransport_or_connectionvalues_minimalpacket.candidate.json"
OBLIGATIONS = ROOT / "candidate_data" / "selected_heterotic_orientedphifin_sourceidentitytransport_obligation_skeleton.json"
CERT = ROOT / "certificates" / "selected_heterotic_orientedphifin_sourceidentitytransport_or_connectionvalues_minimalpacket_certificate.json"
NOTE = ROOT / "proof_corpus" / "Selected_Heterotic_OrientedPhiFin_SourceIdentityTransport_or_ConnectionValues_MinimalPacket_v1.md"

STATUS = "HETEROTIC_ORIENTEDPHIFIN_SOURCEIDENTITYTRANSPORT_MINIMAL_PACKET_BUILT_PROOF_OBJECT_OPEN"
NEXT = "Selected_Heterotic_OrientedPhiFin_SourceIdentityTransport_ProofAttempt_v1"


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
    obligations = load(OBLIGATIONS)
    cert = load(CERT)
    note = NOTE.read_text(encoding="utf-8")
    decision = data["decision"]
    routes = data["route_comparison"]

    check("status", data["status"] == STATUS and cert["status"] == STATUS, (data["status"], cert["status"]))
    check("next", decision["next_required_artifact"] == NEXT and cert["next_required_artifact"] == NEXT, decision)
    check("primary route selected", decision["primary_route_selected"] == "source_identity_transport" and routes["source_identity_transport"]["route_rank"] == 1, routes["source_identity_transport"])
    check("support prefilter passes only", decision["support_prefilter_passes"] is True and decision["proof_object_emitted"] is False, decision)
    check("three routes open", routes["source_identity_transport"]["closed_now"] is False and routes["typed_connection_values"]["closed_now"] is False and routes["direct_connection_values"]["closed_now"] is False, routes)
    check("three sublemmas", set(obligations["sublemmas"]) == {"source_branch_identity", "operator_coemission_before_finite_comparison", "no_lift_audit_replay_from_emitted_source"}, obligations["sublemmas"])
    check("all sublemmas open", all(item["current_status"] == "OPEN" for item in obligations["sublemmas"].values()), obligations["sublemmas"])
    check("acceptance rule strict", "all three sublemmas must close" in obligations["acceptance_rule"], obligations["acceptance_rule"])
    check("no export closure", decision["selected_connection_witness_export_closed"] is False and cert["selected_connection_witness_export_closed"] is False, cert)
    check("no logdet promotion", decision["oriented_logdet_promoted"] is False and cert["oriented_logdet_promoted"] is False, cert)
    check("guardrails", all(v is True for k, v in data["guardrails"].items() if k != "target_fitting_used") and data["guardrails"]["target_fitting_used"] is False, data["guardrails"])
    check("note records skeleton", NEXT in note and str(OBLIGATIONS.relative_to(ROOT)) in note and "source_identity_transport_closed = false" in note, NOTE)

    print("\nSelected heterotic oriented Phi_fin source-identity transport minimal packet audit passed")


if __name__ == "__main__":
    main()
