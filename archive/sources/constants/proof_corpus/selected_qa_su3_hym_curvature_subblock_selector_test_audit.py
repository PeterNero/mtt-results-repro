"""Audit the Qa/SU3 HYM algebraic curvature subblock selector test."""

from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path


REPO = Path(__file__).resolve().parents[1]
CERT = REPO / "certificates" / "selected_qa_su3_hym_curvature_subblock_selector_test_certificate.json"
NOTE = REPO / "proof_corpus" / "Selected_Qa_SU3_HYM_Curvature_Subblock_Selector_Test_v1.md"
SCRIPT = REPO / "scripts" / "compute_selected_qa_su3_hym_curvature_subblock_selector_test.py"


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
            cert["status"] == "QA_SU3_HYM_CURVATURE_COMMUTATOR_SUBBLOCK_COMPUTED_NO_INTERIOR_SELECTOR",
            cert["status"],
        ),
        check(
            "script agrees with certificate",
            computed["norm_formula"] == cert["norm_formula"]
            and computed["selector_consequence"] == cert["selector_consequence"],
            computed["verdict"],
        ),
        check(
            "polynomial formula verified on samples",
            all(sample["agrees_with_polynomial"] for sample in cert["norm_formula"]["samples"]),
            cert["norm_formula"]["samples"],
        ),
        check(
            "derivative positive on samples",
            all(sample["derivative"] > 0.0 for sample in cert["norm_formula"]["samples"]),
            cert["norm_formula"]["samples"],
        ),
        check(
            "subblock does not select interior mu",
            cert["selector_consequence"]["commutator_curvature_norm_selects_interior_mu"] is False,
            cert["selector_consequence"],
        ),
        check(
            "full curvature still not overclaimed",
            cert["verdict"]["full_curvature_matrix_computed"] is False
            and "not the complete left-invariant curvature matrix"
            in cert["computed_subblock"]["scope_warning"],
            cert["computed_subblock"]["scope_warning"],
        ),
        check(
            "note records full curvature next gate",
            "Selected_Qa_SU3_Full_Left_Invariant_Curvature_Matrix_v1" in note,
            NOTE,
        ),
    ]

    print("\nSelected Qa/SU3 HYM curvature subblock selector audit")
    return 0 if all(checks) else 1


if __name__ == "__main__":
    raise SystemExit(main())
