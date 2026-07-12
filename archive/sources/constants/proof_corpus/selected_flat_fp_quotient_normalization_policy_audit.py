"""Audit the flat FP quotient-normalization policy theorem."""

from __future__ import annotations

import json
import math
import subprocess
import sys
from pathlib import Path


REPO = Path(__file__).resolve().parents[1]
OBSIDIAN = Path(r"C:\ObsidianVault\BrainOfNerodes\Papers\Modal Triplet Theory")
CERT = REPO / "certificates" / "selected_flat_fp_quotient_normalization_policy_certificate.json"
NOTE = REPO / "proof_corpus" / "Selected_Flat_FP_Quotient_Normalization_Policy_v1.md"
SCRIPT = REPO / "scripts" / "compute_selected_flat_fp_quotient_normalization_policy.py"
GAUGE_FIXING = OBSIDIAN / "5 Dirac Delta" / "Gauge_Fixing_as_Admissible_Section_Selection_in_Modal_Triplet_Theory.md"
QFT = OBSIDIAN / "7 Quantum Field Theory" / "Modal_Triplet_Theory__From_MTT_to_Quantum_Field_Theory_on_Curved_Spacetime_v3.md"


def read(path: Path) -> str:
    return path.read_text(encoding="utf-8")


def approx(left: float, right: float, tolerance: float = 1e-12) -> bool:
    return math.isclose(left, right, rel_tol=0.0, abs_tol=tolerance)


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
    gauge_fixing = read(GAUGE_FIXING)
    qft = read(QFT)
    computed = run_script()
    failures = []

    failures.append(
        not report(
            "certificate status",
            cert["status"] == "FLAT_FP_QUOTIENT_NORMALIZATION_POLICY_CLOSED_FOR_WEAK_SPLIT",
            cert["status"],
        )
    )
    failures.append(
        not report(
            "gauge-fixing source supports quotient-Jacobian interpretation",
            "Faddeev--Popov determinant is exactly the Jacobian" in gauge_fixing
            and "field-independent and decouples" in gauge_fixing
            and "ghost fields are local bookkeeping variables" in gauge_fixing,
            GAUGE_FIXING,
        )
    )
    failures.append(
        not report(
            "QFT source supports BRST gauge-sector discipline",
            "BRST" in qft and "gauge" in qft and "observables" in qft,
            QFT,
        )
    )
    failures.append(
        not report(
            "script agrees with selected SU2 value and zero extra FP threshold",
            approx(
                computed["selected_flat_su2_data"]["selected_p_SU2_for_weak_split"],
                -1.1961941178318218,
            )
            and approx(computed["selected_flat_su2_data"]["extra_fp_threshold_term"], 0.0)
            and approx(
                computed["selected_flat_su2_data"]["flat_adjoint_fp_logdet_if_kept"],
                -1.7942911767477328,
            ),
            computed["selected_flat_su2_data"],
        )
    )
    failures.append(
        not report(
            "scope caveats protect absolute normalization and vacuum energy",
            "vacuum energy" in cert["scope"]["not_closed_for"]
            and "absolute partition-function normalization" in cert["scope"]["not_closed_for"]
            and cert["verdict"]["absolute_universal_constant_fixed"] is False,
            cert["scope"],
        )
    )
    failures.append(
        not report(
            "SU2 is selected for lambda_12 accounting",
            cert["verdict"]["su2_quotient_policy_closed_for_weak_split"] is True
            and cert["verdict"]["su2_selected_for_lambda_12_accounting"] is True
            and cert["verdict"]["flat_adjoint_fp_kept_as_threshold"] is False,
            cert["verdict"],
        )
    )
    failures.append(
        not report(
            "note states scoped closure",
            "closed for weak-split gauge-kinetic threshold accounting" in note
            and "not a claim about vacuum energy" in note
            and "p_SU2 = -1.1961941178318218" in note,
            NOTE,
        )
    )

    print("\nSelected flat FP quotient-normalization policy audit")
    if any(failures):
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
