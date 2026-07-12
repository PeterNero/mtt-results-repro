"""Audit the electroweak U1/Y operator-row or anchor value-packet fill attempt."""

from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path


REPO = Path(__file__).resolve().parents[1]
SCRIPT = REPO / "scripts" / "build_selected_electroweak_u1y_operatorrow_or_anchor_valuepacket_fill.py"
DATA = REPO / "candidate_data" / "selected_electroweak_u1y_operatorrow_or_anchor_valuepacket_fill.candidate.json"
CERT = REPO / "certificates" / "selected_electroweak_u1y_operatorrow_or_anchor_valuepacket_fill_certificate.json"
U1_FILL = REPO / "candidate_data" / "selected_electroweak_u1y_operator_row_source_packet.fill_attempt.json"
ANCHOR_FILL = REPO / "candidate_data" / "selected_electroweak_dimensional_action_anchor_source_packet.fill_attempt.json"
NOTE = REPO / "proof_corpus" / "Selected_Electroweak_U1Y_OperatorRow_SourcePacket_or_PhysicalActionAnchor_ValuePacket_Fill_v1.md"

STATUS = "ELECTROWEAK_U1Y_OPERATORROW_OR_ANCHOR_VALUEPACKET_FILL_PARTIAL_SPECTRAL_MAP_OPEN"
NEXT = "Selected_Electroweak_U1Y_LocalDeterminant_From_27Mode_DE_GapLayer_v1"


def check(name: str, ok: bool, detail: object) -> bool:
    print(f"{'PASS' if ok else 'FAIL'}: {name} -- {detail}")
    return ok


def main() -> int:
    proc = subprocess.run(
        [sys.executable, str(SCRIPT)],
        cwd=REPO,
        text=True,
        stdout=subprocess.PIPE,
        stderr=subprocess.STDOUT,
        check=True,
    )
    data = json.loads(DATA.read_text(encoding="utf-8"))
    cert = json.loads(CERT.read_text(encoding="utf-8"))
    u1 = json.loads(U1_FILL.read_text(encoding="utf-8"))
    anchor = json.loads(ANCHOR_FILL.read_text(encoding="utf-8"))
    note = NOTE.read_text(encoding="utf-8")

    decision = data["decision"]
    u1_attempt = data["u1_attempt"]
    anchor_attempt = data["anchor_attempt"]
    guardrails = data["guardrails"]

    checks = [
        check("status", data["status"] == STATUS and cert["status"] == STATUS, (data["status"], cert["status"])),
        check("script reruns", len([line for line in proc.stdout.splitlines() if line.startswith("wrote ")]) == 5, proc.stdout),
        check("next artifact", decision["next_required_artifact"] == NEXT and cert["next_required_artifact"] == NEXT and NEXT in note, cert["next_required_artifact"]),
        check("routec prefix filled", all(u1_attempt["prefix_filled"].values()), u1_attempt["prefix_filled"]),
        check("u1 fill marks support only", u1["status"].startswith("FILL_ATTEMPT") and u1["finite_part"]["positive_eigenvalues"] is None, u1["status"]),
        check("u1 blocks spectral fields", "finite_part.positive_eigenvalues" in u1_attempt["blocking_fields"] and "finite_part.lambda_12_contribution" in u1_attempt["blocking_fields"], u1_attempt["blocking_fields"]),
        check("u1 does not promote determinant", u1_attempt["promotes_u1y_operator_row_packet"] is False and decision["u1y_local_determinant_packet_closed"] is False, decision),
        check("anchor still value open", anchor["status"].startswith("FILL_ATTEMPT") and anchor["dimensionful_anchor"]["value"] is None, anchor["status"]),
        check("anchor blocks value and source", "dimensionful_anchor.value" in anchor_attempt["blocking_fields"] and "source_identity.selected_by_mtt" in anchor_attempt["blocking_fields"], anchor_attempt["blocking_fields"]),
        check("guardrails forbid shortcuts", all(value is False for value in guardrails.values()), guardrails),
        check("no closure", cert["closure_claimed"] is False and decision["lambda_12_closed"] is False and decision["measured_electroweak_closure"] is False, decision),
        check("note records spectral map", "spectral map" in note and "U1/Y local determinant finite part" in note, NOTE),
    ]
    print("\nSelected electroweak U1/Y operator-row or anchor value-packet fill audit")
    return 0 if all(checks) else 1


if __name__ == "__main__":
    raise SystemExit(main())
