"""Audit the imported selected Qa/SU3 same-source VAlpha/S3 packet frontier."""

from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path


REPO = Path(__file__).resolve().parents[1]
CERT = REPO / "certificates" / "selected_qa_su3_same_source_valpha_s3_packet_import_certificate.json"
TEMPLATE = REPO / "certificates" / "selected_qa_su3_same_source_valpha_s3_operator_packet.template.json"
NOTE = REPO / "proof_corpus" / "Selected_Qa_SU3_Same_Source_VAlpha_S3_Packet_Import_v1.md"
SCRIPT = REPO / "scripts" / "import_selected_qa_su3_same_source_valpha_s3_packet.py"


def check(name: str, ok: bool, detail: object) -> bool:
    print(f"{'PASS' if ok else 'FAIL'}: {name} -- {detail}")
    return ok


def run_script() -> dict:
    proc = subprocess.run(
        [sys.executable, str(SCRIPT)],
        cwd=REPO,
        text=True,
        stdout=subprocess.PIPE,
        stderr=subprocess.STDOUT,
        check=True,
    )
    return json.loads(proc.stdout)


def main() -> int:
    cert = json.loads(CERT.read_text(encoding="utf-8"))
    template = json.loads(TEMPLATE.read_text(encoding="utf-8"))
    computed = run_script()
    note = NOTE.read_text(encoding="utf-8")
    validator = cert["validator_result"]
    closed = cert["closed_now"]
    open_items = cert["not_closed"]

    checks = [
        check(
            "certificate status",
            cert["status"] == "QA_SU3_SAME_SOURCE_VALPHA_S3_PACKET_IMPORTED_OPEN_ITEMS_CERTIFIED",
            cert["status"],
        ),
        check(
            "script agrees with certificate",
            computed["closed_now"] == closed
            and computed["not_closed"] == open_items
            and computed["validator_result"] == validator,
            computed["status"],
        ),
        check(
            "template imported",
            template["schema"] == "SelectedQaSU3SameSourceVAlphaS3OperatorPacket.v1"
            and template["status"]
            == "OPEN_SELECTED_QA_SU3_SAME_SOURCE_VALPHA_S3_OPERATOR_PACKET_REQUIRED",
            template,
        ),
        check(
            "q79 executable gate imported",
            closed["q79_same_source_fusion_gate_executable"] is True
            and closed["same_source_template_imported"] is True
            and closed["current_best_patchwork_attempt_refused"] is True,
            closed,
        ),
        check(
            "validator frontier exact",
            validator["exit_code"] == 2
            and validator["open_item_count"] == 20
            and validator["ordered_source_exit_code"] == 2
            and validator["selected_source_promotion_exit_code"] == 1
            and validator["would_close_selected_monad_difference_source"] is False,
            validator,
        ),
        check(
            "first open items include core blockers",
            "same_source_for_ordered_L_pic0_GS_and_DE must be true"
            in validator["first_open_items"]
            and "Pic0 resolution is not selected or quotiented"
            in validator["first_open_items"]
            and "selected-source promotion validator did not pass (exit 1)"
            in validator["first_open_items"],
            validator["first_open_items"],
        ),
        check(
            "remaining blockers explicit",
            open_items["same_source_valpha_s3_binding"] is True
            and open_items["selected_L3_minus_K2_source"] is True
            and open_items["Pic0_selection_or_quotient"] is True
            and open_items["selected_D_E_dotD_Riesz_Green"] is True,
            open_items,
        ),
        check(
            "no overclaim",
            cert["guardrails"]["claims_same_source_binding_proved"] is False
            and cert["guardrails"]["claims_selected_D_E_constructed"] is False
            and cert["guardrails"]["claims_pic0_resolved"] is False
            and cert["guardrails"]["claims_full_SM_closure"] is False,
            cert["guardrails"],
        ),
        check(
            "note records exact frontier",
            "open_item_count: 20" in note
            and "SameSourceMonadGSOperatorFusionPacket.v1" in note
            and "selected-source promotion validator did not pass" in note,
            NOTE,
        ),
    ]

    print("\nSelected Qa/SU3 same-source VAlpha/S3 packet import audit")
    return 0 if all(checks) else 1


if __name__ == "__main__":
    raise SystemExit(main())
