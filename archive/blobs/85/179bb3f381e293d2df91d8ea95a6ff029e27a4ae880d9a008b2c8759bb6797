"""Audit the finite-part policy and index/scale source theorem."""

from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "candidate_data"
CERTS = ROOT / "certificates"
PROOF = ROOT / "proof_corpus"
SCRIPT = ROOT / "scripts" / "build_selected_electroweak_qastack_finitepart_policy_and_indexscale.py"
OUTPUT_DATA = DATA / "selected_electroweak_qastack_finitepart_policy_and_indexscale.candidate.json"
OUTPUT_CERT = CERTS / "selected_electroweak_qastack_finitepart_policy_and_indexscale_certificate.json"
OUTPUT_NOTE = PROOF / "Selected_Electroweak_QaStack_FinitePartPolicy_and_IndexScale_SourceTheorem_v1.md"

EXPECTED_STATUS = "ELECTROWEAK_QASTACK_INTERNAL_FINITEPART_POLICY_INDEXSCALE_CLOSED_SU2_PHYSICAL_OPEN"
EXPECTED_NEXT = "Selected_Electroweak_QaStack_SU2Row_or_Cancellation_and_PhysicalAnchor_v1"


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

    policy = candidate["finitepart_policy"]
    index_scale = candidate["index_and_scale"]
    decision = candidate["decision"]
    guards = candidate["guardrails"]
    p_a = candidate["p_a_internal"]

    check("regularization selected internally", policy["regularization"]["selected_for_internal_finite_quotient_row"] is True, policy)
    check("kernel selected internally", policy["kernel_policy"]["zero_shared_line_removed_before_positive_determinant"] is True, policy)
    check("eta neutral only current", policy["H_zero_cluster_policy"]["selected_for_current_value"] is True and policy["H_zero_cluster_policy"]["general_policy_closed"] is False, policy)
    check("unit weights after quotient", index_scale["determinant_index_weights"]["selected_for_internal_row"] is True and all(item["index_weight"] == 1 for item in index_scale["determinant_index_weights"]["weights"]), index_scale)
    check("internal mu one only", index_scale["determinant_scale"]["mu"] == "1" and index_scale["determinant_scale"]["physical_K_gauge_closed"] is False, index_scale)
    check("p_a internal promoted", p_a["promoted_as_internal_finite_part"] is True and abs(p_a["value"] - 29.201650332199108) < 1e-12, p_a)
    check("decision closes internal only", decision["selected_p_a_internal_promoted"] is True and decision["lambda_12_closed"] is False and decision["measured_electroweak_closure"] is False, decision)
    check("no double count guard", guards["double_counts_Pperp_as_weight"] is False and guards["claims_physical_K_gauge"] is False, guards)
    check("no target fitting", candidate["target_fitting_used"] is False and guards["uses_observed_electroweak_data"] is False, guards)
    check("note boundary", "internal determinant scale only" in note and "lambda_12" in note, OUTPUT_NOTE)

    print("\nSelected electroweak Qa-stack finite-part policy/index-scale audit")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
