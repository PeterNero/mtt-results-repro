"""Audit the Qa/SU3 HYM connection convention/erratum resolution scan."""

from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path


REPO = Path(__file__).resolve().parents[1]
CERT = REPO / "certificates" / "selected_qa_su3_hym_connection_erratum_or_convention_resolution_certificate.json"
NOTE = REPO / "proof_corpus" / "Selected_Qa_SU3_HYM_Connection_Erratum_or_Convention_Resolution_v1.md"
SCRIPT = REPO / "scripts" / "compute_selected_qa_su3_hym_connection_erratum_or_convention_resolution.py"


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

    checks = [
        check(
            "certificate status",
            cert["status"] == "QA_SU3_HYM_CONNECTION_CONVENTION_SCAN_DONE_MINIMAL_ERRATUM_IDENTIFIED",
            cert["status"],
        ),
        check(
            "script agrees with certificate",
            computed["convention_scan"] == cert["convention_scan"]
            and computed["minimal_standard_repair"] == cert["minimal_standard_repair"],
            computed["verdict"],
        ),
        check(
            "no simple convention resolves integrability",
            cert["convention_scan"]["zero_residual_convention_found"] is False
            and cert["convention_scan"]["minimum_residual_norm_squared"] == 3.0,
            cert["convention_scan"]["best_rows"],
        ),
        check(
            "minimal repair is diagonal B3",
            cert["minimal_standard_repair"]["required_B3_symbolic"]
            == [["mu", "0", "0"], ["0", "0", "0"], ["0", "0", "-mu"]],
            cert["minimal_standard_repair"],
        ),
        check(
            "repair not source certified",
            cert["repair_status"]["source_support_for_repair"] is False
            and cert["verdict"]["minimal_repair_source_certified"] is False,
            cert["repair_status"],
        ),
        check(
            "note records retirement or repair next gate",
            "Selected_Qa_SU3_Erratum_Repaired_HYM_Pipeline_or_Source_Retirement_v1" in note,
            NOTE,
        ),
    ]

    print("\nSelected Qa/SU3 HYM connection erratum/convention audit")
    return 0 if all(checks) else 1


if __name__ == "__main__":
    raise SystemExit(main())
