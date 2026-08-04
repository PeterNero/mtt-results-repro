"""Audit the Repair B primitive correction current-source no-go."""

from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path


REPO = Path(__file__).resolve().parents[1]
CERT = REPO / "certificates" / "selected_qa_su3_repair_b_primitive_correction_no_go_certificate.json"
NOTE = REPO / "proof_corpus" / "Selected_Qa_SU3_Repair_B_Primitive_Correction_No_Go_v1.md"
SCRIPT = REPO / "scripts" / "compute_selected_qa_su3_repair_b_primitive_correction_no_go.py"


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
    verdict = cert["verdict"]
    tests = cert["available_source_term_tests"]

    checks = [
        check(
            "certificate status",
            cert["status"] == "QA_SU3_REPAIR_B_PRIMITIVE_CORRECTION_CURRENT_SOURCE_NO_GO",
            cert["status"],
        ),
        check(
            "script agrees with certificate",
            computed["required_correction"] == cert["required_correction"]
            and computed["available_source_term_tests"] == cert["available_source_term_tests"],
            computed["verdict"],
        ),
        check(
            "required formula recorded",
            cert["required_correction"]["weighted_primitive_formula"]
            == "-(w1*mu + w3*mu^2) diag(1,-1,0)",
            cert["required_correction"],
        ),
        check(
            "all current source terms rejected",
            all(test["result"] == "reject" for test in tests),
            tests,
        ),
        check(
            "no-go scoped not absolute",
            cert["no_go_scope"]["proved_for_current_corpus_sources"] is True
            and cert["no_go_scope"]["not_proved_for_future_new_source"] is True
            and verdict["repair_B_mathematically_impossible"] is False,
            cert["no_go_scope"],
        ),
        check(
            "no Qa closure claimed",
            verdict["safe_to_close_Qa_SU3"] is False
            and verdict["target_fitting_used"] is False,
            verdict,
        ),
        check(
            "note records next route decision",
            "Selected_Qa_SU3_Explicit_Source_Certified_Connection_or_Route_Retirement_v1"
            in note,
            NOTE,
        ),
    ]

    print("\nSelected Qa/SU3 Repair B primitive correction no-go audit")
    return 0 if all(checks) else 1


if __name__ == "__main__":
    raise SystemExit(main())
