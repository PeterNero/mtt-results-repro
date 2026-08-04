"""Audit the selected gauge-factor zeta finite-part candidate."""

from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path


REPO = Path(__file__).resolve().parents[1]
CERT = REPO / "certificates" / "selected_gauge_factor_zeta_finite_part_candidate_certificate.json"
NOTE = REPO / "proof_corpus" / "Selected_Gauge_Factor_Zeta_Finite_Part_Candidate_v1.md"
ESTIMATOR = REPO / "scripts" / "estimate_selected_zeta_finite_part.py"


def read(path: Path) -> str:
    return path.read_text(encoding="utf-8")


def run_estimator() -> dict:
    proc = subprocess.run(
        [sys.executable, str(ESTIMATOR)],
        cwd=REPO,
        text=True,
        stdout=subprocess.PIPE,
        stderr=subprocess.STDOUT,
        check=True,
    )
    return json.loads(proc.stdout)


def check(name: str, ok: bool, detail: object = "") -> bool:
    print(f"{'PASS' if ok else 'FAIL'}: {name} -- {detail}")
    return ok


def main() -> int:
    cert = json.loads(read(CERT))
    note = read(NOTE)
    result = run_estimator()
    fits = result["fits"]

    checks = [
        check(
            "certificate status",
            cert["status"] == "ZETA_FINITE_PART_ESTIMATOR_BUILT_FINAL_DETERMINANT_OPEN",
            cert["status"],
        ),
        check(
            "estimator returns finite parts",
            set(fits.keys()) == {"lambda_12", "U1", "SU2", "SU3"}
            and all("finite_part_constant" in fit for fit in fits.values()),
            {key: fits[key]["finite_part_constant"] for key in fits},
        ),
        check(
            "basis recorded",
            result["asymptotic_basis"] == ["K2logK", "K2", "KlogK", "K", "logK", "constant"],
            result["asymptotic_basis"],
        ),
        check(
            "fit residuals controlled for diagnostic sequence",
            all(fit["max_abs_residual"] < 1e-5 for fit in fits.values()),
            {key: fits[key]["max_abs_residual"] for key in fits},
        ),
        check(
            "note names exact upgrade",
            "Exact_Selected_Gauge_Threshold_Operator_and_Zeta_Determinant_v1" in note,
            "exact zeta upgrade",
        ),
        check(
            "numeric closure not claimed",
            result["verdict"]["regularization_pipeline_built"] is True
            and result["verdict"]["final_zeta_determinant_certified"] is False
            and cert["verdict"]["numeric_electroweak_closure"] is False,
            cert["verdict"],
        ),
    ]

    print("\nSelected gauge-factor zeta finite-part candidate audit")
    print("======================================================")
    return 0 if all(checks) else 1


if __name__ == "__main__":
    raise SystemExit(main())
