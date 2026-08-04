"""Audit the electroweak Qa-stack source-identity and p-row regularization subpacket."""

from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "candidate_data"
CERTS = ROOT / "certificates"
PROOF = ROOT / "proof_corpus"
SCRIPT = ROOT / "scripts" / "build_selected_electroweak_qastack_sourceidentity_and_prow_regularization.py"
OUTPUT_DATA = DATA / "selected_electroweak_qastack_sourceidentity_and_prow_regularization.candidate.json"
OUTPUT_CERT = CERTS / "selected_electroweak_qastack_sourceidentity_and_prow_regularization_certificate.json"
OUTPUT_NOTE = PROOF / "Selected_Electroweak_QaStack_SourceIdentity_and_pRowRegularization_Subpacket_v1.md"

EXPECTED_STATUS = "ELECTROWEAK_QASTACK_SOURCEIDENTITY_OPEN_PROW_REGULARIZATION_CONDITIONAL_BRIDGE_BUILT"
EXPECTED_NEXT = "Selected_Electroweak_QaStack_SourceIdentity_From_TerminalMonad_or_GerbeSource_v1"


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

    decision = candidate["decision"]
    bridge = candidate["regularization_bridge"]
    source = candidate["source_identity_checks"]
    guards = candidate["guardrails"]

    check("source identity open", decision["source_identity_closed"] is False, decision)
    check("conditional bridge closed", decision["p_row_regularization_bridge_conditional_closed"] is True, decision)
    check("no selected p_a", decision["selected_p_a_promoted"] is False and bridge["promotes_p_a_now"] is False, bridge)
    check("no lambda", decision["lambda_12_closed"] is False and decision["measured_electroweak_closure"] is False, decision)
    check("support present", source["exact_A_base_tensor_I3_matrix_constructed"] is True and source["rank3_carrier_support_closed"] is True, source)
    check("selection missing", source["q79_factorized_selected_by_mtt"] is False and source["q79_sector_maps_selected_by_mtt"] is False, source)
    check("operator response missing", source["DE_operator_response_pass"] is False and source["dotd_response_pass"] is False, source)
    check("bridge condition explicit", "selected source identity emits" in bridge["bridge_condition"], bridge)
    check("conditional numbers retained", bridge["conditional_p_a"] == cert["conditional_p_a"] and bridge["conditional_lambda12"] == cert["conditional_lambda12"], bridge)
    check("guardrails false", all(value is False for value in guards.values()), guards)
    check("note says conditional", "conditional bridge" in note and "not a promotion" in note, OUTPUT_NOTE)

    print("\nSelected electroweak Qa-stack source-identity and p-row regularization audit")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
