"""Audit the Qa/SU3 Repair A quotient or Repair B torsion source test."""

from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path


REPO = Path(__file__).resolve().parents[1]
CERT = REPO / "certificates" / "selected_qa_su3_repair_a_quotient_or_b_torsion_source_test_certificate.json"
NOTE = REPO / "proof_corpus" / "Selected_Qa_SU3_Repair_A_Quotient_or_Repair_B_Torsion_Source_Test_v1.md"
SCRIPT = REPO / "scripts" / "compute_selected_qa_su3_repair_a_quotient_or_b_torsion_source_test.py"


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
    conclusion = cert["conclusion"]

    checks = [
        check(
            "certificate status",
            cert["status"] == "QA_SU3_REPAIR_A_QUOTIENT_REFUTED_REPAIR_B_TORSION_SOURCE_OPEN",
            cert["status"],
        ),
        check(
            "script agrees with certificate",
            computed["conclusion"] == cert["conclusion"]
            and computed["repair_A_quotient_test"] == cert["repair_A_quotient_test"],
            computed["verdict"],
        ),
        check(
            "source supports indecomposable branch",
            cert["source_branch_support"]["supports_indecomposable_rank3_hym"] is True,
            cert["source_branch_support"],
        ),
        check(
            "repair A extra zero is noncentral stabilizer",
            conclusion["repair_A_extra_zero_is_noncentral_stabilizer"] is True
            and conclusion["repair_A_incompatible_with_selected_indecomposable_branch"] is True,
            conclusion,
        ),
        check(
            "repair B remains open",
            conclusion["repair_B_remains_only_live_repair_candidate"] is True
            and conclusion["repair_B_primitive_correction_source_certified"] is False,
            conclusion,
        ),
        check(
            "no Qa closure claimed",
            cert["verdict"]["safe_to_close_Qa_SU3"] is False
            and cert["verdict"]["route_B_closed"] is False,
            cert["verdict"],
        ),
        check(
            "note records next B correction gate",
            "Selected_Qa_SU3_Repair_B_Source_Certified_Primitive_Correction_or_No_Go_v1"
            in note,
            NOTE,
        ),
    ]

    print("\nSelected Qa/SU3 Repair A quotient or Repair B torsion source test audit")
    return 0 if all(checks) else 1


if __name__ == "__main__":
    raise SystemExit(main())
