"""Audit the conditional selected physical quotient heat-coefficient gate."""

from __future__ import annotations

import json
import math
import subprocess
import sys
from pathlib import Path


REPO = Path(__file__).resolve().parents[1]
CERT = REPO / "certificates" / "selected_physical_quotient_heat_coefficients_certificate.json"
NOTE = REPO / "proof_corpus" / "Selected_Physical_Quotient_Heat_Coefficients_v1.md"
SCRIPT = REPO / "scripts" / "compute_selected_physical_quotient_heat_coefficients.py"


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
    computed = run_script()
    failures = []

    failures.append(
        not report(
            "certificate status",
            cert["status"] == "CONDITIONAL_CASIMIR_HEAT_COEFFICIENT_MODEL_COMPUTED_NOT_SELECTED",
            cert["status"],
        )
    )
    failures.append(
        not report(
            "script agrees with certificate",
            approx(
                computed["hypercharge_accounting"]["lambda_12"],
                cert["hypercharge_accounting"]["lambda_12"],
            )
            and approx(
                computed["hypercharge_accounting"]["Delta_G_12"],
                cert["hypercharge_accounting"]["Delta_G_12"],
            ),
            computed["hypercharge_accounting"],
        )
    )
    failures.append(
        not report(
            "Casimir heat coefficients are explicit",
            computed["selected_physical_quotient_heat_coefficients"]["Qa_SU3_stack"]["coefficient"] == 3.0
            and computed["selected_physical_quotient_heat_coefficients"]["Qc_circle_stack"]["coefficient"] == 1.0
            and computed["selected_physical_quotient_heat_coefficients"]["SU2_stack"]["coefficient"] == 2.0,
            computed["selected_physical_quotient_heat_coefficients"],
        )
    )
    failures.append(
        not report(
            "candidate remains offset from diagnostic witness",
            approx(computed["diagnostic_comparison"]["residual_lambda_12"], 0.22027629619491407),
            computed["diagnostic_comparison"],
        )
    )
    failures.append(
        not report(
            "selection and closure are not claimed",
            cert["verdict"]["selected_by_corpus"] is False
            and cert["verdict"]["numeric_electroweak_closure"] is False
            and cert["verdict"]["new_no_knob_prediction_certified"] is False,
            cert["verdict"],
        )
    )
    failures.append(
        not report(
            "note records theorem gate and non-closure",
            "Selected_Gauge_Threshold_Operator_Heat_Kernel_Theorem_v1" in note
            and "It is not a new no-knob electroweak prediction." in note
            and "derive the selected heat coefficients" in note,
            NOTE,
        )
    )

    print("\nSelected physical quotient heat-coefficients audit")
    if any(failures):
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
