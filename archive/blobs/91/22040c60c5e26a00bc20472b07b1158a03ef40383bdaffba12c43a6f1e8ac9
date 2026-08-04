"""Audit the Qa/SU3 repaired pipeline A/B diagnostic comparison."""

from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path


REPO = Path(__file__).resolve().parents[1]
CERT = REPO / "certificates" / "selected_qa_su3_repaired_pipeline_ab_diagnostic_comparison_certificate.json"
NOTE = REPO / "proof_corpus" / "Selected_Qa_SU3_Repaired_Pipeline_A_B_Diagnostic_Comparison_v1.md"
SCRIPT = REPO / "scripts" / "compute_selected_qa_su3_repaired_pipeline_ab_diagnostic_comparison.py"


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
    comparison = cert["comparison"]

    checks = [
        check(
            "certificate status",
            cert["status"] == "QA_SU3_REPAIRED_PIPELINE_A_B_DIAGNOSTIC_COMPARISON_DONE_NO_SOURCE_CLOSURE",
            cert["status"],
        ),
        check(
            "script agrees with certificate",
            computed["diagnostics"] == cert["diagnostics"]
            and computed["comparison"] == cert["comparison"],
            computed["verdict"],
        ),
        check(
            "both repairs restore integrability",
            comparison["both_restore_integrability_on_samples"] is True,
            comparison,
        ),
        check(
            "repair A has extra zero mode",
            comparison["repair_A_extra_zero_mode"] is True,
            cert["diagnostics"][0],
        ),
        check(
            "repair B preserves rank pattern",
            comparison["repair_B_expected_hessian_rank_pattern"] is True,
            cert["diagnostics"][1],
        ),
        check(
            "neither selects mu by logdet samples",
            comparison["neither_selects_mu_by_logdet_samples"] is True,
            comparison,
        ),
        check(
            "no source closure claimed",
            cert["verdict"]["repair_B_source_certified"] is False
            and cert["verdict"]["safe_to_close_Qa_SU3"] is False,
            cert["verdict"],
        ),
        check(
            "note records repair B next test",
            "Selected_Qa_SU3_Repair_B_Chern_Weil_and_Operator_Test_v1" in note,
            NOTE,
        ),
    ]

    print("\nSelected Qa/SU3 repaired pipeline A/B diagnostic comparison audit")
    return 0 if all(checks) else 1


if __name__ == "__main__":
    raise SystemExit(main())
