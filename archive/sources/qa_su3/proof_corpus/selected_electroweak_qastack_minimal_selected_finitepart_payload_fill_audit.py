"""Audit the minimal selected finite-part payload fill."""

from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "candidate_data"
CERTS = ROOT / "certificates"
PROOF = ROOT / "proof_corpus"
SCRIPT = ROOT / "scripts" / "build_selected_electroweak_qastack_minimal_selected_finitepart_payload_fill.py"
OUTPUT_DATA = DATA / "selected_electroweak_qastack_minimal_selected_finitepart_payload_fill.candidate.json"
OUTPUT_CERT = CERTS / "selected_electroweak_qastack_minimal_selected_finitepart_payload_fill_certificate.json"
OUTPUT_NOTE = PROOF / "Selected_Electroweak_QaStack_Minimal_SelectedFinitePart_Payload_Fill_v1.md"

EXPECTED_STATUS = "ELECTROWEAK_QASTACK_MINIMAL_SELECTED_FINITEPART_PAYLOAD_PARTIAL_FILL_FINITEPART_PROMOTION_OPEN"
EXPECTED_NEXT = "Selected_Electroweak_QaStack_FinitePartPolicy_and_IndexScale_SourceTheorem_v1"


def load(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def check(name: str, condition: bool, detail: object = "") -> None:
    if not condition:
        print(f"FAIL: {name} -- {detail}")
        raise SystemExit(1)
    print(f"PASS: {name} -- {detail}")


def main() -> int:
    proc = subprocess.run([sys.executable, str(SCRIPT)], cwd=ROOT, text=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
    check("script reruns", proc.returncode == 0, proc.stdout)

    candidate = load(OUTPUT_DATA)
    cert = load(OUTPUT_CERT)
    note = OUTPUT_NOTE.read_text(encoding="utf-8")

    check("status", candidate["status"] == EXPECTED_STATUS, candidate["status"])
    check("cert status", cert["status"] == EXPECTED_STATUS, cert["status"])
    check("next", candidate["decision"]["next_required_artifact"] == EXPECTED_NEXT, candidate["decision"])

    payload = candidate["filled_payload"]
    decision = candidate["decision"]
    blockers = candidate["blockers"]
    guards = candidate["guardrails"]

    check("DE source filled only for gap", payload["source_identity"]["selected_by_mtt_for_DE_gap_layer"] is True and payload["source_identity"]["selected_by_mtt_for_determinant_finite_part"] is False, payload["source_identity"])
    check("V/s conditional table", payload["domain_and_operator"]["positive_eigenvalue_table_on_V_mod_s"]["status"] == "CONDITIONAL_COMPUTABLE_NOT_SELECTED_FINITE_PART", payload["domain_and_operator"])
    check("kernel partial", payload["domain_and_operator"]["kernel_policy"]["status"] == "PARTIAL", payload["domain_and_operator"]["kernel_policy"])
    check("eta neutral open", payload["domain_and_operator"]["H_zero_cluster_policy"]["status"] == "OPEN_NEUTRAL_FOR_CURRENT_ETA1", payload["domain_and_operator"]["H_zero_cluster_policy"])
    check("finite part not selected", payload["finite_part"]["regularization"]["selected_as_finite_part"] is False, payload["finite_part"])
    check("scale open", payload["finite_part"]["determinant_scale"]["status"] == "OPEN", payload["finite_part"])

    check("partial fill decisions", decision["source_identity_for_DE_gap_layer_filled"] is True and decision["V_mod_s_positive_table_computed_conditionally"] is True, decision)
    check("promotion blocks remain", all(value is False for value in blockers.values()), blockers)
    check("no p/lambda closure", decision["selected_p_a_promoted"] is False and decision["lambda_12_closed"] is False, decision)
    check("guardrails false", all(value is False for value in guards.values()), guards)
    check("note says partial", "partially filled" in note and "not source-selected" in note, OUTPUT_NOTE)

    print("\nSelected electroweak Qa-stack minimal finite-part payload fill audit")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
