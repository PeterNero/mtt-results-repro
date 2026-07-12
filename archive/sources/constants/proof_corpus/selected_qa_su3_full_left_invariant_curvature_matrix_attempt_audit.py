"""Audit the full left-invariant curvature matrix attempt for Qa/SU3 HYM."""

from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path


REPO = Path(__file__).resolve().parents[1]
CERT = REPO / "certificates" / "selected_qa_su3_full_left_invariant_curvature_matrix_attempt_certificate.json"
NOTE = REPO / "proof_corpus" / "Selected_Qa_SU3_Full_Left_Invariant_Curvature_Matrix_Attempt_v1.md"
SCRIPT = REPO / "scripts" / "compute_selected_qa_su3_full_left_invariant_curvature_matrix_attempt.py"


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
    samples = cert["computed_integrability_residual"]["samples"]

    checks = [
        check(
            "certificate status",
            cert["status"] == "QA_SU3_FULL_CURVATURE_MATRIX_BLOCKED_BY_PRINTED_INTEGRABILITY_MISMATCH",
            cert["status"],
        ),
        check(
            "script agrees with certificate",
            computed["computed_integrability_residual"] == cert["computed_integrability_residual"]
            and computed["verdict"] == cert["verdict"],
            computed["verdict"],
        ),
        check(
            "residual formula is nonzero for samples",
            all(sample["standard_residual_frobenius_squared"] > 0.0 for sample in samples),
            samples,
        ),
        check(
            "residual equals 3 mu squared",
            all(
                abs(
                    sample["standard_residual_frobenius_squared"]
                    - sample["standard_closed_formula"]
                )
                < 1e-12
                for sample in samples
            ),
            samples,
        ),
        check(
            "opposite structure sign does not repair residual",
            all(
                sample["opposite_structure_sign_residual_frobenius_squared"] > 0.0
                for sample in samples
            ),
            samples,
        ),
        check(
            "curvature closure not overclaimed",
            cert["verdict"]["full_left_invariant_curvature_matrix_computed"] is False
            and cert["verdict"]["source_erratum_or_convention_needed"] is True,
            cert["verdict"],
        ),
        check(
            "note records erratum/convention next gate",
            "Selected_Qa_SU3_HYM_Connection_Erratum_or_Convention_Resolution_v1" in note,
            NOTE,
        ),
    ]

    print("\nSelected Qa/SU3 full left-invariant curvature matrix attempt audit")
    return 0 if all(checks) else 1


if __name__ == "__main__":
    raise SystemExit(main())
