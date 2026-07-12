"""Audit the Qa/SU3 repair retirement stress test."""

from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path


REPO = Path(__file__).resolve().parents[1]
CERT = REPO / "certificates" / "selected_qa_su3_repair_retirement_stress_test_certificate.json"
NOTE = REPO / "proof_corpus" / "Selected_Qa_SU3_Repair_Retirement_Stress_Test_v1.md"
SCRIPT = REPO / "scripts" / "compute_selected_qa_su3_repair_retirement_stress_test.py"


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
    signatures = cert["computed_signatures"]
    conclusion = cert["stress_test_conclusion"]

    checks = [
        check(
            "certificate status",
            cert["status"] == "QA_SU3_REPAIR_A_RETIREMENT_STRESS_TEST_CONDITIONAL_RETIREMENT_UPHELD",
            cert["status"],
        ),
        check(
            "script agrees with certificate",
            computed["computed_signatures"] == cert["computed_signatures"]
            and computed["stress_test_conclusion"] == cert["stress_test_conclusion"],
            computed["verdict"],
        ),
        check(
            "repair A has extra centralizer and direct split",
            signatures["repair_A"]["centralizer"]["centralizer_dimension_minus_center"] >= 1
            and signatures["repair_A"]["has_invariant_direct_sum_coordinate_split"] is True,
            signatures["repair_A"],
        ),
        check(
            "repair B nuance recorded",
            "does have invariant coordinate flags"
            in conclusion["previous_repair_B_flag_wording_corrected"]
            and signatures["repair_B"]["centralizer"]["centralizer_dimension_minus_center"] == 0,
            conclusion,
        ),
        check(
            "retirement is conditional not absolute",
            cert["verdict"]["repair_A_retired_under_current_selection"] is True
            and cert["verdict"]["repair_A_forbidden_as_any_math_object"] is False,
            cert["verdict"],
        ),
        check(
            "revival options recorded",
            len(cert["revival_options"]) >= 5,
            cert["revival_options"],
        ),
        check(
            "external sources recorded",
            len(cert["external_research_principles"]) == 3,
            cert["external_research_principles"],
        ),
        check(
            "note records conditional statement",
            "Repair A is mathematically impossible" in note
            and "is not claimed" in note,
            NOTE,
        ),
    ]

    print("\nSelected Qa/SU3 repair retirement stress test audit")
    return 0 if all(checks) else 1


if __name__ == "__main__":
    raise SystemExit(main())
