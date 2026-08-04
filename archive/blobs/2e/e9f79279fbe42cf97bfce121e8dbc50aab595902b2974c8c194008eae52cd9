"""Build the current best stack-determinant candidate table.

The hypercharge-normalized threshold gate requires three stack determinants:

    p_a    Q_a / SU3-side stack
    p_c    Q_c / circle stack
    p_SU2  weak stack

This script records the strongest current candidate without promoting it to a
prediction.  The Qc and SU2 entries use exact scalar-proxy zeta pieces.  The
Qa entry uses the existing proxy SU3 finite-part estimator and is therefore
not a selected determinant.
"""

from __future__ import annotations

import json
import subprocess
import sys
import tempfile
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
CIRCLE_SPHERE = ROOT / "scripts" / "compute_exact_circle_sphere_zeta.py"
ZETA_ESTIMATOR = ROOT / "scripts" / "estimate_selected_zeta_finite_part.py"
HYPERCHARGE_CALCULATOR = ROOT / "scripts" / "compute_hypercharge_normalized_threshold.py"
C1_CERT = ROOT / "certificates" / "selected_electroweak_c1_response_interface_certificate.json"


def run_json(script: Path, *args: str) -> dict[str, Any]:
    proc = subprocess.run(
        [sys.executable, str(script), *args],
        cwd=ROOT,
        text=True,
        stdout=subprocess.PIPE,
        stderr=subprocess.STDOUT,
        check=True,
    )
    return json.loads(proc.stdout)


def compute_hypercharge_fixture(p_a: float, p_c: float, p_su2: float, v1_tilde: float) -> dict[str, Any]:
    fixture = {
        "selected_hypercharge_normalized_threshold": {
            "selected_values": {"v1_tilde": v1_tilde},
            "stack_thresholds": {
                "Qa_SU3_stack": p_a,
                "Qc_circle_stack": p_c,
                "SU2_stack": p_su2,
            },
        }
    }
    with tempfile.NamedTemporaryFile("w", suffix=".json", delete=False, encoding="utf-8") as handle:
        json.dump(fixture, handle)
        path = Path(handle.name)
    try:
        return run_json(HYPERCHARGE_CALCULATOR, str(path))
    finally:
        path.unlink(missing_ok=True)


def main() -> int:
    exact = run_json(CIRCLE_SPHERE)
    estimator = run_json(ZETA_ESTIMATOR)
    c1 = json.loads(C1_CERT.read_text(encoding="utf-8"))

    p_c = float(exact["finite_parts"]["U1_circle"])
    p_su2 = float(exact["finite_parts"]["SU2_effective_sphere"])
    p_a_proxy = float(estimator["fits"]["SU3"]["finite_part_constant"])
    v1_tilde = float(c1["selected_values"]["v1_tilde"])
    target_lambda = float(c1["diagnostic_expected"]["lambda_12"])

    hypercharge = compute_hypercharge_fixture(p_a_proxy, p_c, p_su2, v1_tilde)
    lambda_12 = float(hypercharge["weak_split"]["lambda_12"])
    required_p_a = 36.0 * (target_lambda + p_su2 - p_c / 4.0)

    output = {
        "status": "STACK_DETERMINANT_CANDIDATE_TABLE_BUILT_QA_OPEN",
        "candidate_table": {
            "Qa_SU3_stack": {
                "value": p_a_proxy,
                "status": "PROXY_FINITE_PART_NOT_SELECTED",
                "source": "selected gauge-factor zeta finite-part candidate SU3 proxy",
                "blocker": "Exact selected Qa/SU3 stack determinant in physical quotient is not supplied.",
            },
            "Qc_circle_stack": {
                "value": p_c,
                "status": "EXACT_SCALAR_PROXY_ZETA",
                "source": "exact circle zeta finite part",
                "blocker": "Need proof that scalar proxy equals selected Qc gauge-threshold determinant and normalization.",
            },
            "SU2_stack": {
                "value": p_su2,
                "status": "EXACT_SCALAR_PROXY_ZETA",
                "source": "exact effective sphere zeta finite part",
                "blocker": "Need proof that scalar proxy equals selected SU2 gauge-threshold determinant and normalization.",
            },
        },
        "hypercharge_accounting": hypercharge,
        "diagnostic_comparison": {
            "target_lambda_12": target_lambda,
            "candidate_lambda_12": lambda_12,
            "residual_lambda_12": lambda_12 - target_lambda,
            "required_Qa_if_Qc_and_SU2_candidates_are_kept": required_p_a,
            "required_Qa_minus_proxy_Qa": required_p_a - p_a_proxy,
            "required_Qa_role": "diagnostic only; not a selected determinant",
        },
        "verdict": {
            "candidate_table_built": True,
            "Qa_selected_determinant_closed": False,
            "Qc_selected_gauge_determinant_closed": False,
            "SU2_selected_gauge_determinant_closed": False,
            "numeric_electroweak_closure": False,
            "next_required_computation": (
                "Replace the Qa proxy and scalar Qc/SU2 proxies with selected "
                "gauge-threshold determinants in one physical quotient scheme."
            ),
        },
    }
    print(json.dumps(output, indent=2, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
