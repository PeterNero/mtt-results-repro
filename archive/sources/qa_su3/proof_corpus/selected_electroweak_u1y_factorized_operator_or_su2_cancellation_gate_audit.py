"""Audit the factorized U1/Y operator or SU2 cancellation gate."""

from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path


REPO = Path(__file__).resolve().parents[1]
SCRIPT = REPO / "scripts" / "build_selected_electroweak_u1y_factorized_operator_or_su2_cancellation_gate.py"
DATA = REPO / "candidate_data" / "selected_electroweak_u1y_factorized_operator_or_su2_cancellation_gate.candidate.json"
CERT = REPO / "certificates" / "selected_electroweak_u1y_factorized_operator_or_su2_cancellation_gate_certificate.json"
TEMPLATE = REPO / "candidate_data" / "selected_electroweak_u1y_factorized_threshold_operator_source.template.json"
NOTE = REPO / "proof_corpus" / "Selected_Electroweak_U1Y_Factorized_ThresholdOperator_SourceEmission_or_SU2_Cancellation_v1.md"

STATUS = "ELECTROWEAK_U1Y_FACTORIZED_OPERATOR_SOURCE_OPEN_SU2_WEAKSPLIT_CLOSED"
NEXT = "Selected_Electroweak_U1Y_FactorizedThresholdOperator_SourceEmission_v1"


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
    tests = data["source_tests"]
    guardrails = data["guardrails"]

    checks = [
        check("status", data["status"] == STATUS and cert["status"] == STATUS, (data["status"], cert["status"])),
        check("script reruns", len([line for line in proc.stdout.splitlines() if line.startswith("wrote ")]) == 4, proc.stdout),
        check("next artifact", decision["next_required_artifact"] == NEXT and cert["next_required_artifact"] == NEXT and NEXT in note, cert["next_required_artifact"]),
        check("SU2 scoped closed", decision["SU2_same_scheme_row_or_cancellation_closed_for_weaksplit"] is True and tests["SU2_same_scheme_weaksplit_row"]["status"] == "CLOSED_SCOPED_WEAKSPLIT", tests["SU2_same_scheme_weaksplit_row"]),
        check("U1 source open", decision["U1_factorized_threshold_operator_source_closed"] is False and tests["U1_factorized_operator_source"]["status"] == "OPEN", tests["U1_factorized_operator_source"]),
        check("quotient row conditional", data["conditional_quotient_row"]["logdet"] == 29.201650332199108 and data["conditional_quotient_row"]["usable_for_lambda12_now"] is False, data["conditional_quotient_row"]),
        check("hypercharge weights open", decision["hypercharge_index_Dynkin_weights_closed"] is False and tests["hypercharge_index_Dynkin_weights"]["status"] == "OPEN", tests["hypercharge_index_Dynkin_weights"]),
        check("lambda still open", decision["lambda_12_closed"] is False and cert["open"]["lambda_12"] is True, decision),
        check("template exact", template["status"] == "OPEN_SELECTED_FACTORIZED_U1Y_THRESHOLD_OPERATOR_REQUIRED" and template["operator_payload"]["hypercharge_index_Dynkin_weights"] is None, template),
        check("guardrails", all(value is False for value in guardrails.values()), guardrails),
        check("note records forbidden diagnostic", "Forbidden Diagnostic" in note and "cross-convention" in note, NOTE),
    ]
    print("\nSelected electroweak U1/Y factorized operator or SU2 cancellation gate audit")
    return 0 if all(checks) else 1


if __name__ == "__main__":
    raise SystemExit(main())
