"""Audit the hypercharge weights and typed convention gate."""

from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path


REPO = Path(__file__).resolve().parents[1]
SCRIPT = REPO / "scripts" / "build_selected_electroweak_u1y_hypercharge_weights_typed_convention_gate.py"
DATA = REPO / "candidate_data" / "selected_electroweak_u1y_hypercharge_weights_typed_convention_gate.candidate.json"
CERT = REPO / "certificates" / "selected_electroweak_u1y_hypercharge_weights_typed_convention_gate_certificate.json"
NOTE = REPO / "proof_corpus" / "Selected_Electroweak_U1Y_HyperchargeWeights_TypedConvention_Gate_v1.md"

STATUS = "ELECTROWEAK_U1Y_TYPED_HYPERCHARGE_MAP_CLOSED_STACK_DETERMINANT_SOURCE_OPEN"
NEXT = "Selected_Electroweak_QaStack_Determinant_SourceEmission_or_U1YRowPromotion_v1"


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
    note = NOTE.read_text(encoding="utf-8")
    decision = data["decision"]
    tests = data["route_tests"]
    guardrails = data["guardrails"]

    checks = [
        check("status", data["status"] == STATUS and cert["status"] == STATUS, (data["status"], cert["status"])),
        check("script reruns", len([line for line in proc.stdout.splitlines() if line.startswith("wrote ")]) == 3, proc.stdout),
        check("next artifact", decision["next_required_artifact"] == NEXT and cert["next_required_artifact"] == NEXT and NEXT in note, cert["next_required_artifact"]),
        check("typed map closed", decision["typed_hypercharge_convention_map_closed"] is True and data["typed_convention_map"]["threshold_combination"] == "p_Y = (1/36) p_a + (1/4) p_c", data["typed_convention_map"]),
        check("weights structural", data["typed_convention_map"]["selected_weights"]["Qa_stack_weight_in_pY"] == "1/36" and data["typed_convention_map"]["selected_weights"]["Qc_circle_weight_in_pY"] == "1/4", data["typed_convention_map"]["selected_weights"]),
        check("Qc SU2 closed", decision["Qc_row_closed_for_weaksplit"] is True and decision["SU2_row_closed_for_weaksplit"] is True and tests["Qc_and_SU2_rows"]["status"] == "CLOSED_FOR_WEAK_SPLIT", tests["Qc_and_SU2_rows"]),
        check("direct row rejected", tests["direct_U1Y_row_shortcut"]["accepted"] is False and decision["direct_U1Y_row_promoted"] is False, tests["direct_U1Y_row_shortcut"]),
        check("Qa conditional only", tests["Qa_stack_interpretation_of_quotient_operator"]["status"] == "CONDITIONAL_NOT_PROMOTED" and decision["Qa_stack_p_a_source_closed"] is False, tests["Qa_stack_interpretation_of_quotient_operator"]),
        check("conditional lambda computed not closed", abs(decision["conditional_lambda12_if_quotient_is_p_a"] - 2.6179362173268497) < 1e-12 and decision["lambda_12_closed"] is False, decision),
        check("guardrails", all(value is False for value in guardrails.values()), guardrails),
        check("note records legal path", "direct-row shortcut is rejected" in note and "selected `p_a` stack determinant" in note, NOTE),
    ]
    print("\nSelected electroweak U1/Y hypercharge weights typed convention gate audit")
    return 0 if all(checks) else 1


if __name__ == "__main__":
    raise SystemExit(main())
