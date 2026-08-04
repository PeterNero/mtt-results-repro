"""Audit the sharper selected Qa/SU3 same-source VAlpha/S3 attempt import."""

from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path


REPO = Path(__file__).resolve().parents[1]
CERT = REPO / "certificates" / "selected_qa_su3_same_source_valpha_s3_attempt_import_certificate.json"
NOTE = REPO / "proof_corpus" / "Selected_Qa_SU3_Same_Source_VAlpha_S3_Attempt_Import_v1.md"
SCRIPT = REPO / "scripts" / "import_selected_qa_su3_same_source_valpha_s3_attempt.py"


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
    computed = run_script()
    note = NOTE.read_text(encoding="utf-8")
    validator = cert["validator_result"]
    layers = cert["dependency_layers"]
    first_gate = cert["first_true_gate"]

    checks = [
        check(
            "certificate status",
            cert["status"]
            == "QA_SU3_SAME_SOURCE_VALPHA_S3_ATTEMPT_IMPORTED_S3_CONSUMED_SOURCE_OPEN",
            cert["status"],
        ),
        check(
            "script agrees with certificate",
            computed["validator_result"] == validator
            and computed["dependency_layers"] == layers
            and computed["first_true_gate"] == first_gate,
            computed["status"],
        ),
        check(
            "s3 consumed but packet open",
            cert["closed_now"]["closed_s3_support_consumed"] is True
            and validator["subvalidator_exit_codes"]["s3_class_restriction"] == 0
            and validator["exit_code"] == 2
            and validator["open_item_count"] == 24,
            validator,
        ),
        check(
            "layering has four gates",
            sorted(layers) == [
                "L0_identity_and_selected_source",
                "L1_valpha_ordered_source",
                "L2_s3_gs_same_source",
                "L3_operator_execution",
            ],
            layers,
        ),
        check(
            "first true gate identified",
            first_gate["layer"] == "L0_identity_and_selected_source"
            and first_gate["minimal_object"]
            == "Selected_Source_Certificate_for_VAlpha_S3_DE.v1",
            first_gate,
        ),
        check(
            "core blockers explicit",
            "same_source_valpha_s3_operator must be true"
            in layers["L0_identity_and_selected_source"]
            and "Pic0 resolution is not selected or quotiented"
            in layers["L1_valpha_ordered_source"]
            and "visible GS source validator did not pass (exit 1)"
            in layers["L2_s3_gs_same_source"]
            and "selected-source promotion validator did not pass (exit 1)"
            in layers["L3_operator_execution"],
            layers,
        ),
        check(
            "no overclaim",
            cert["guardrails"]["claims_same_source_binding"] is False
            and cert["guardrails"]["claims_selected_visible_valpha_source"] is False
            and cert["guardrails"]["claims_selected_operator_execution"] is False
            and cert["guardrails"]["claims_full_SM_closure"] is False,
            cert["guardrails"],
        ),
        check(
            "note records first true gate",
            "Selected_Source_Certificate_for_VAlpha_S3_DE.v1" in note
            and "s3_class_restriction subvalidator: PASS" in note
            and "open_item_count: 24" in note,
            NOTE,
        ),
    ]

    print("\nSelected Qa/SU3 same-source VAlpha/S3 attempt import audit")
    return 0 if all(checks) else 1


if __name__ == "__main__":
    raise SystemExit(main())
