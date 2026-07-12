"""Audit the electroweak Qa-stack or U1/Y-row source-payload fill attempt."""

from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "candidate_data"
CERTS = ROOT / "certificates"
PROOF = ROOT / "proof_corpus"
SCRIPT = ROOT / "scripts" / "build_selected_electroweak_qastack_or_u1yrow_source_payload_fill.py"
OUTPUT_DATA = DATA / "selected_electroweak_qastack_or_u1yrow_source_payload_fill.candidate.json"
OUTPUT_CERT = CERTS / "selected_electroweak_qastack_or_u1yrow_source_payload_fill_certificate.json"
OUTPUT_NOTE = PROOF / "Selected_Electroweak_QaStack_or_U1YRow_SourcePayload_Fill_v1.md"

EXPECTED_STATUS = "ELECTROWEAK_QASTACK_OR_U1YROW_SOURCE_PAYLOAD_FILL_NOGO_CURRENT_SOURCE_SUPPORT_ONLY"
EXPECTED_NEXT = "Selected_Electroweak_QaStack_SourceIdentity_and_pRowRegularization_Subpacket_v1"


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
    check("certificate status", cert["status"] == EXPECTED_STATUS, cert["status"])
    check("next artifact", candidate["next_required_artifact"] == EXPECTED_NEXT, candidate["next_required_artifact"])

    qa = candidate["route_fill_attempts"]["Qa_stack_route"]
    direct = candidate["route_fill_attempts"]["direct_pY_route"]
    summary = candidate["fill_summary"]
    guards = candidate["guardrails"]

    check("Qa route not accepted", qa["accepted"] is False, qa)
    check("Qa has support", qa["checks"]["exact_matrix_constructed"] is True and qa["checks"]["rank3_carrier_shape_found"] is True, qa["checks"])
    check("Qa selected source absent", qa["checks"]["q79_factorized_selected_by_mtt"] is False, qa["checks"])
    check("Qa regularization open", qa["checks"]["regularization_identifies_logdet_as_p_a"] is False, qa["checks"])
    check("direct pY not accepted", direct["accepted"] is False, direct)
    check("direct pY source absent", direct["checks"]["source_emitted_hypercharge_normalized_operator"] is False, direct["checks"])
    check("best route Qa", summary["best_live_route"] == "Qa_stack_route", summary)
    check("no closure", summary["lambda_12_closed"] is False and summary["measured_electroweak_closure"] is False, summary)
    check("current no-go scoped", summary["current_source_nogo_proved"] is True and summary["mathematical_impossibility_claimed"] is False, summary)
    check("guardrails", all(value is False for value in guards.values()), guards)
    check("note has minimal payload", EXPECTED_NEXT in note and "quotient determinant is not promoted" in note, OUTPUT_NOTE)

    print("\nSelected electroweak Qa-stack or U1/Y-row source-payload fill audit")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
