"""Audit the deep guardrail scan for Qa/SU3 HYM erratum options."""

from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path


REPO = Path(__file__).resolve().parents[1]
CERT = REPO / "certificates" / "selected_qa_su3_hym_erratum_guardrail_deep_scan_certificate.json"
NOTE = REPO / "proof_corpus" / "Selected_Qa_SU3_HYM_Erratum_Guardrail_Deep_Scan_v1.md"
SCRIPT = REPO / "scripts" / "compute_selected_qa_su3_hym_erratum_guardrail_deep_scan.py"


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
    repairs = cert["named_repair_options"]
    note = NOTE.read_text(encoding="utf-8")

    checks = [
        check(
            "certificate status",
            cert["status"] == "QA_SU3_HYM_ERRATUM_GUARDRAIL_DEEP_SCAN_DONE_NO_PREMATURE_REPAIR_CLOSURE",
            cert["status"],
        ),
        check(
            "script agrees with certificate",
            computed["sparse_integrability_scan"] == cert["sparse_integrability_scan"]
            and computed["verdict"] == cert["verdict"],
            computed["verdict"],
        ),
        check(
            "sparse scan found printed-B1 repair",
            repairs["repair_B_hold_B1_B3_fixed"]["residual_zero"] is True
            and cert["sparse_integrability_scan"]["solutions_with_printed_B1_E13"]
            == [{"B1": "+E13", "B2": "-E32"}],
            cert["sparse_integrability_scan"]["solutions_with_printed_B1_E13"],
        ),
        check(
            "no sparse repair keeps printed B2",
            cert["sparse_integrability_scan"]["solutions_with_printed_B2_minus_E31"] == [],
            cert["sparse_integrability_scan"]["solutions_with_printed_B2_minus_E31"],
        ),
        check(
            "diagonal repair not unique globally",
            cert["verdict"]["diagonal_B3_repair_unique_without_qualification"] is False
            and cert["verdict"]["one_entry_B2_move_repair_exists"] is True,
            cert["verdict"],
        ),
        check(
            "no repair source certified",
            cert["verdict"]["any_repair_source_certified"] is False
            and cert["verdict"]["safe_to_close_Qa_SU3_from_repair_now"] is False,
            cert["verdict"],
        ),
        check(
            "note records diagnostic comparison next gate",
            "Selected_Qa_SU3_Repaired_Pipeline_A_B_Diagnostic_Comparison_v1" in note,
            NOTE,
        ),
    ]

    print("\nSelected Qa/SU3 HYM erratum guardrail deep scan audit")
    return 0 if all(checks) else 1


if __name__ == "__main__":
    raise SystemExit(main())
