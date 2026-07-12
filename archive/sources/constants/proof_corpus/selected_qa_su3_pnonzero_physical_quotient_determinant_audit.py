"""Audit the selected Qa/SU3 p!=0 physical quotient determinant theorem."""

from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path


REPO = Path(__file__).resolve().parents[1]
CERT = REPO / "certificates" / "selected_qa_su3_pnonzero_physical_quotient_determinant_certificate.json"
NOTE = REPO / "proof_corpus" / "Selected_Qa_SU3_PNonzero_Physical_Quotient_Determinant_Theorem_v1.md"
SCRIPT = REPO / "scripts" / "compute_selected_qa_su3_pnonzero_physical_quotient_determinant.py"


def read(path: Path) -> str:
    return path.read_text(encoding="utf-8")


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


def report(name: str, ok: bool, detail: object = "") -> bool:
    status = "PASS" if ok else "FAIL"
    print(f"{status}: {name} -- {detail}")
    return ok


def main() -> int:
    cert = json.loads(read(CERT))
    note = read(NOTE)
    computed = run_script()
    failures = []

    failures.append(
        not report(
            "certificate status",
            cert["status"]
            == "QA_SU3_PNONZERO_PHYSICAL_QUOTIENT_DETERMINANT_SELECTED_NOT_FULL_CLOSURE",
            cert["status"],
        )
    )
    failures.append(
        not report(
            "script agrees with selected response",
            abs(
                computed["finite_parts"]["selected_pnonzero_physical_quotient_response"]
                - cert["finite_parts"]["selected_pnonzero_physical_quotient_response"]
            )
            < 1e-12,
            computed["finite_parts"],
        )
    )
    failures.append(
        not report(
            "lowest-mode identity preserved",
            abs(computed["finite_parts"]["identity_difference"]) < 1e-12,
            computed["finite_parts"],
        )
    )
    failures.append(
        not report(
            "p nonzero quotient selected but does not close",
            computed["verdict"]["pnonzero_physical_quotient_rule_selected"] is True
            and computed["verdict"]["selected_Qa_SU3_operator_closed"] is False,
            computed["numeric_effect"],
        )
    )
    failures.append(
        not report(
            "note records final obstruction or projector gate",
            "p_selected = p_nonzero_scalar - 1/2 p_nonzero_coclosed_oneform" in note
            and "Selected_Qa_SU3_Final_Obstruction_or_Projector_Jacobian_Resolution_v1"
            in note,
            NOTE,
        )
    )

    print("\nSelected Qa/SU3 p nonzero physical quotient determinant audit")
    if any(failures):
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
