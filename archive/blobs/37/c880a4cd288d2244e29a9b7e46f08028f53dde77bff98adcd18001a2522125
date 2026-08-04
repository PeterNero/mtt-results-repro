"""Audit the Qa-stack determinant or direct U1/Y-row promotion gate."""

from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path


REPO = Path(__file__).resolve().parents[1]
SCRIPT = REPO / "scripts" / "build_selected_electroweak_qastack_determinant_or_u1yrow_promotion.py"
DATA = REPO / "candidate_data" / "selected_electroweak_qastack_determinant_or_u1yrow_promotion.candidate.json"
CERT = REPO / "certificates" / "selected_electroweak_qastack_determinant_or_u1yrow_promotion_certificate.json"
TEMPLATE = REPO / "candidate_data" / "selected_electroweak_qastack_or_u1yrow_source_payload.template.json"
NOTE = REPO / "proof_corpus" / "Selected_Electroweak_QaStack_Determinant_SourceEmission_or_U1YRowPromotion_v1.md"

STATUS = "ELECTROWEAK_QASTACK_OR_U1YROW_PROMOTION_GATE_BUILT_SOURCE_EMISSION_OPEN"
NEXT = "Selected_Electroweak_QaStack_or_U1YRow_SourcePayload_Fill_v1"


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
    template = json.loads(TEMPLATE.read_text(encoding="utf-8"))
    note = NOTE.read_text(encoding="utf-8")
    decision = data["decision"]
    tests = data["route_tests"]
    guardrails = data["guardrails"]

    checks = [
        check("status", data["status"] == STATUS and cert["status"] == STATUS, (data["status"], cert["status"])),
        check("script reruns", len([line for line in proc.stdout.splitlines() if line.startswith("wrote ")]) == 4, proc.stdout),
        check("next artifact", decision["next_required_artifact"] == NEXT and cert["next_required_artifact"] == NEXT and NEXT in note, cert["next_required_artifact"]),
        check("Qa conditional not promoted", tests["new_factorized_quotient_as_Qa_stack"]["status"] == "CONDITIONAL_NOT_PROMOTED" and decision["Qa_stack_route_promoted"] is False, tests["new_factorized_quotient_as_Qa_stack"]),
        check("direct pY open", tests["direct_hypercharge_normalized_pY_row"]["status"] == "OPEN_NO_SOURCE_ROW" and decision["direct_pY_route_promoted"] is False, tests["direct_hypercharge_normalized_pY_row"]),
        check("old heat proxy rejected", tests["old_Qa_heat_proxy_table"]["accepted"] is False and "DIAGNOSTIC" in tests["old_Qa_heat_proxy_table"]["status"], tests["old_Qa_heat_proxy_table"]),
        check("old nil rejected", tests["old_nil_reduction"]["accepted"] is False and "OPEN" in tests["old_nil_reduction"]["status"], tests["old_nil_reduction"]),
        check("old brst rejected", tests["old_BRST_Weitzenbock_table"]["accepted"] is False and tests["old_BRST_Weitzenbock_table"]["forbidden_target_reference"] == "scalar_plus_required_gap_for_reference_forbidden", tests["old_BRST_Weitzenbock_table"]),
        check("no selected payload", decision["selected_Qa_or_pY_source_payload_found"] is False and decision["lambda_12_closed"] is False, decision),
        check("template open", template["status"] == "OPEN_SELECTED_QASTACK_OR_U1YROW_SOURCE_PAYLOAD_REQUIRED" and "Qa_stack_route" in template["allowed_promotion_routes"], template),
        check("guardrails", all(value is False for value in guardrails.values()), guardrails),
        check("note records single source payload", "single source-payload problem" in note and "selected `p_a`" in note, NOTE),
    ]
    print("\nSelected electroweak Qa-stack determinant or U1/Y-row promotion audit")
    return 0 if all(checks) else 1


if __name__ == "__main__":
    raise SystemExit(main())
