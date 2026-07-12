"""Audit the electroweak U1/Y-or-dimensional-anchor source-augmentation gate."""

from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path


REPO = Path(__file__).resolve().parents[1]
SCRIPT = REPO / "scripts" / "build_selected_electroweak_u1y_operatorrow_or_dimensionalanchor_sourceaugmentation.py"
DATA = REPO / "candidate_data" / "selected_electroweak_u1y_operatorrow_or_dimensionalanchor_sourceaugmentation.candidate.json"
CERT = REPO / "certificates" / "selected_electroweak_u1y_operatorrow_or_dimensionalanchor_sourceaugmentation_certificate.json"
U1_TEMPLATE = REPO / "candidate_data" / "selected_electroweak_u1y_operator_row_source_packet.template.json"
ANCHOR_TEMPLATE = REPO / "candidate_data" / "selected_electroweak_dimensional_action_anchor_source_packet.template.json"
NOTE = REPO / "proof_corpus" / "Selected_Electroweak_U1Y_OperatorRow_or_DimensionalAnchor_SourceAugmentation_v1.md"

STATUS = "ELECTROWEAK_U1Y_OR_DIMENSIONAL_ANCHOR_SOURCE_AUGMENTATION_BUILT_VALUES_OPEN"
NEXT = "Selected_Electroweak_U1Y_OperatorRow_SourcePacket_or_PhysicalActionAnchor_ValuePacket_Fill_v1"


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
    u1 = json.loads(U1_TEMPLATE.read_text(encoding="utf-8"))
    anchor = json.loads(ANCHOR_TEMPLATE.read_text(encoding="utf-8"))
    note = NOTE.read_text(encoding="utf-8")

    decision = data["decision"]
    gate = data["source_augmentation_gate"]
    joint = gate["joint_promotion_rule"]
    guardrails = data["guardrails"]

    checks = [
        check("status", data["status"] == STATUS and cert["status"] == STATUS, (data["status"], cert["status"])),
        check("script reruns", len([line for line in proc.stdout.splitlines() if line.startswith("wrote ")]) == 5, proc.stdout),
        check("next artifact", decision["next_required_artifact"] == NEXT and cert["next_required_artifact"] == NEXT and NEXT in note, cert["next_required_artifact"]),
        check("u1 template open", u1["status"] == "OPEN_SELECTED_U1Y_OPERATOR_ROW_SOURCE_PACKET_REQUIRED" and u1["operator_row"]["operator_identity"] is None, u1["status"]),
        check("u1 quotient not spectrum", u1["domain_and_quotient"]["central_circle_double_counting_forbidden"] is True and "not the spectrum" in u1["domain_and_quotient"]["P_perp_policy"], u1["domain_and_quotient"]),
        check("anchor template open", anchor["status"] == "OPEN_SELECTED_DIMENSIONAL_ACTION_ANCHOR_SOURCE_PACKET_REQUIRED" and anchor["dimensionful_anchor"]["value"] is None, anchor["status"]),
        check("anchor forbids target inputs", "observed Newton constant" in anchor["acceptance_contract"]["must_not_use"] and "Theta 5 TeV calibration" in anchor["acceptance_contract"]["must_not_use"], anchor["acceptance_contract"]),
        check("branches cannot replace each other", "physical action anchor" in gate["u1y_operator_row_branch"]["cannot_replace"] and "U1/Y local determinant" in gate["dimensional_action_anchor_branch"]["cannot_replace"], gate),
        check("joint rule requires both", joint["either_branch_may_be_filled_next"] is True and joint["measured_electroweak_closure_requires_both_branches"] is True, joint),
        check("recommended u1 first", decision["recommended_next_fill"] == "U1Y_operator_row_source_packet" and cert["recommended_next_fill"] == "U1Y_operator_row_source_packet", decision),
        check("guardrails forbid shortcuts", all(value is False for value in guardrails.values()), guardrails),
        check("no closure", cert["closure_claimed"] is False and decision["measured_electroweak_closure"] is False and data["closure_claimed"] is False, decision),
        check("note records practical next move", "U1/Y operator-row packet first" in note and "target-independent" in note, NOTE),
    ]
    print("\nSelected electroweak U1/Y operator-row or dimensional-anchor source-augmentation audit")
    return 0 if all(checks) else 1


if __name__ == "__main__":
    raise SystemExit(main())
