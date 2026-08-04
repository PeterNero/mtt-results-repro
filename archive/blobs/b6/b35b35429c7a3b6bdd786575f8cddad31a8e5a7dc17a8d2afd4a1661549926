"""Audit the Qa/SU3 repair Chern-Weil/operator diagnostic."""

from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path


REPO = Path(__file__).resolve().parents[1]
CERT = REPO / "certificates" / "selected_qa_su3_repair_chern_weil_operator_diagnostic_certificate.json"
NOTE = REPO / "proof_corpus" / "Selected_Qa_SU3_Repair_Chern_Weil_Operator_Diagnostic_v1.md"
SCRIPT = REPO / "scripts" / "compute_selected_qa_su3_repair_chern_weil_operator_diagnostic.py"


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
            cert["status"] == "QA_SU3_REPAIR_CHERN_WEIL_OPERATOR_DIAGNOSTIC_SPLIT_NO_CLOSURE",
            cert["status"],
        ),
        check(
            "script agrees with certificate",
            computed["diagnostics"] == cert["diagnostics"]
            and computed["comparison"] == cert["comparison"],
            computed["verdict"],
        ),
        check(
            "repair A passes integrable primitive diagnostic",
            comparison["repair_A_integrable_and_primitive"] is True,
            comparison,
        ),
        check(
            "repair A retains prior rank problem",
            comparison["repair_A_hessian_rank_problem_from_prior_gate"] is True,
            comparison,
        ),
        check(
            "repair B integrable but primitive obstructed",
            comparison["repair_B_integrable"] is True
            and comparison["repair_B_primitive_obstructed"] is True,
            comparison,
        ),
        check(
            "repair B retains prior rank advantage",
            comparison["repair_B_hessian_rank_good_from_prior_gate"] is True,
            comparison,
        ),
        check(
            "no closure claimed",
            cert["verdict"]["safe_to_close_Qa_SU3"] is False
            and cert["verdict"]["source_certified_repair_found"] is False,
            cert["verdict"],
        ),
        check(
            "note records next source/torsion gate",
            "Selected_Qa_SU3_Source_Certified_Connection_or_Full_Torsion_Primitive_Correction_v1"
            in note,
            NOTE,
        ),
    ]

    print("\nSelected Qa/SU3 repair Chern-Weil/operator diagnostic audit")
    return 0 if all(checks) else 1


if __name__ == "__main__":
    raise SystemExit(main())
