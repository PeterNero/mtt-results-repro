"""Audit selected-connection witness export fill attempt."""

from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SCRIPT = ROOT / "scripts" / "build_selected_heterotic_orientedphifin_selectedconnectionwitness_export_fill.py"
DATA = ROOT / "candidate_data" / "selected_heterotic_orientedphifin_selectedconnectionwitness_export_fill.candidate.json"
PACKET = ROOT / "candidate_data" / "selected_heterotic_orientedphifin_selectedconnectionwitness_minimal_source_values_packet.json"
CERT = ROOT / "certificates" / "selected_heterotic_orientedphifin_selectedconnectionwitness_export_fill_certificate.json"
NOTE = ROOT / "proof_corpus" / "Selected_Heterotic_OrientedPhiFin_SelectedConnectionWitness_Export_Fill_v1.md"

STATUS = "HETEROTIC_ORIENTEDPHIFIN_SELECTEDCONNECTIONWITNESS_EXPORT_FILL_SUPPORT_READY_SOURCE_OPEN"
NEXT = "Selected_Heterotic_OrientedPhiFin_SourceIdentityTransport_or_ConnectionValues_MinimalPacket_v1"


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
    fields = data["export_fields"]

    check("status", data["status"] == STATUS and cert["status"] == STATUS, (data["status"], cert["status"]))
    check("next", decision["next_required_artifact"] == NEXT and cert["next_required_artifact"] == NEXT, decision)
    check("all six fields present", set(fields) == {"source_identity", "BN27_deck_action", "operators", "kernel_policy", "trace_policy", "audit_replay"}, fields.keys())
    check("support ready count", decision["support_ready_count"] == 6 and cert["support_ready_count"] == 6, decision)
    check("only audit replay filled", decision["export_filled_count"] == 1 and fields["audit_replay"]["filled_for_export"] is True, fields["audit_replay"])
    check("source identity still open", fields["source_identity"]["filled_for_export"] is False and fields["source_identity"]["selected_source_owned"] is False, fields["source_identity"])
    check("deck support not promoted", fields["BN27_deck_action"]["support_present"] is True and fields["BN27_deck_action"]["filled_for_export"] is False, fields["BN27_deck_action"])
    check("operators support not promoted", fields["operators"]["support_present"] is True and fields["operators"]["filled_for_export"] is False, fields["operators"])
    check("trace exact but not promoted", fields["trace_policy"]["support_present"] is True and fields["trace_policy"]["value"]["oriented_abs_sector_product"] == 92160000 and fields["trace_policy"]["filled_for_export"] is False, fields["trace_policy"])
    check("family lanes open", all(item["closed"] is False for item in data["family_fill"].values()), data["family_fill"])
    check("minimal packet built", packet["status"] == "MINIMAL_SOURCE_VALUES_REQUIRED" and set(packet["acceptable_minimal_values"]) == {"source_identity_transport", "typed_connection_values", "direct_connection_values"}, packet)
    check("no closure", decision["selected_connection_witness_export_closed"] is False and cert["selected_connection_witness_export_closed"] is False, cert)
    check("no logdet promotion", decision["oriented_logdet_promoted"] is False and cert["oriented_logdet_promoted"] is False, cert)
    check("guardrails", all(v is True for k, v in data["guardrails"].items() if k != "target_fitting_used") and data["guardrails"]["target_fitting_used"] is False, data["guardrails"])
    check("note records result", NEXT in note and "selected_connection_witness_export_closed = false" in note and str(PACKET.relative_to(ROOT)) in note, NOTE)

    print("\nSelected heterotic oriented Phi_fin selected-connection witness export fill audit passed")


if __name__ == "__main__":
    main()
