"""Audit the electroweak Qa-stack threshold-operator fill from nonidentity rho_E/B_N."""

from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "candidate_data"
CERTS = ROOT / "certificates"
PROOF = ROOT / "proof_corpus"
SCRIPT = ROOT / "scripts" / "build_selected_electroweak_qastack_threshold_operator_from_nonidentity_rhoe_quotientbn.py"
OUTPUT_DATA = DATA / "selected_electroweak_qastack_threshold_operator_from_nonidentity_rhoe_quotientbn.candidate.json"
OUTPUT_CERT = CERTS / "selected_electroweak_qastack_threshold_operator_from_nonidentity_rhoe_quotientbn_certificate.json"
OUTPUT_NOTE = PROOF / "Selected_Electroweak_QaStack_ThresholdOperator_From_NonIdentityRhoE_QuotientBN_Fill_v1.md"

EXPECTED_STATUS = "ELECTROWEAK_QASTACK_NONIDENTITY_RHOE_QUOTIENTBN_PREFIX_IMPORTED_THRESHOLD_IDENTITY_OPEN"
EXPECTED_NEXT = "Selected_Electroweak_QaStack_SelectedTraceEquality_or_FullThresholdOperatorFormula_v1"


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

    prefix = candidate["prefix_payload"]
    tests = candidate["threshold_adapter_tests"]
    decision = candidate["decision"]
    guards = candidate["guardrails"]

    check("prefix imported", decision["nonidentity_rhoE_BN_prefix_imported"] is True, decision)
    check("prefix can host", tests["prefix_can_host_threshold_operator"]["passed"] is True, tests)
    check("nonidentity candidate present", prefix["nonidentity_rhoE_candidate_present"] is True and prefix["smooth_27mode_BN_present"] is True, prefix)
    check("operator data present", prefix["D_E_matrix_present"] is True and prefix["Riesz_Green_gap_present"] is True and prefix["dotD_alpha1_present"] is True, prefix)
    check("selection still open", tests["selected_source_certificate"]["passed"] is False and prefix["rhoE_selected_by_mtt"] is False, tests)
    check("quotient validity still open", tests["quotient_valid_BN_for_shared_line"]["passed"] is False, tests)
    check("threshold identity still open", tests["exact_A_base_tensor_I3_threshold_identity"]["passed"] is False, tests)
    check("weights scale open", tests["Qa_stack_weights_and_scale_policy"]["passed"] is False, tests)
    check("no closure", decision["threshold_operator_identity_closed"] is False and decision["lambda_12_closed"] is False, decision)
    check("guardrails false", all(value is False for value in guards.values()), guards)
    check("note says prefix not selected", "not yet a selected threshold identity" in note and "prefix is not promoted" in note, OUTPUT_NOTE)

    print("\nSelected electroweak Qa-stack threshold operator from nonidentity rhoE/BN audit")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
