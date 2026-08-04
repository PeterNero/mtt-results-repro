"""Compute the hypercharge-embedding fork for the U1 threshold slot."""

from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
CIRCLE_SPHERE = ROOT / "scripts" / "compute_exact_circle_sphere_zeta.py"
C1_CERT = ROOT / "certificates" / "selected_electroweak_c1_response_interface_certificate.json"
ZETA_ESTIMATOR = ROOT / "scripts" / "estimate_selected_zeta_finite_part.py"


def run_json(script: Path) -> dict[str, Any]:
    proc = subprocess.run(
        [sys.executable, str(script)],
        cwd=ROOT,
        text=True,
        stdout=subprocess.PIPE,
        stderr=subprocess.STDOUT,
        check=True,
    )
    return json.loads(proc.stdout)


def main() -> int:
    pieces = run_json(CIRCLE_SPHERE)
    estimator = run_json(ZETA_ESTIMATOR)
    c1 = json.loads(C1_CERT.read_text(encoding="utf-8"))

    p_circle = float(pieces["finite_parts"]["U1_circle"])
    p_su2 = float(pieces["finite_parts"]["SU2_effective_sphere"])
    p_su3_proxy = float(estimator["fits"]["SU3"]["finite_part_constant"])
    target_lambda = float(c1["diagnostic_expected"]["lambda_12"])

    # ProtoSpinor three-stack benchmark:
    # Y = (1/6) Q_a - (1/2) Q_c
    # so threshold/inverse-coupling contributions combine as
    # p_Y = (1/36) p_a + (1/4) p_c.
    p_y_without_qa = 0.25 * p_circle
    lambda_without_qa = p_y_without_qa - p_su2
    p_y_with_proxy_qa = (p_su3_proxy / 36.0) + (p_circle / 4.0)
    lambda_with_proxy_qa = p_y_with_proxy_qa - p_su2
    required_p_qa = 36.0 * (target_lambda + p_su2 - p_circle / 4.0)

    output = {
        "status": "HYPERCHARGE_EMBEDDING_GATE_BUILT_NIL_RELEVANCE_REOPENED_FOR_U1_SELECTION",
        "source_formula": {
            "hypercharge_embedding": "Y = (1/6) Q_a - (1/2) Q_c",
            "threshold_combination": "p_Y = (1/36) p_a + (1/4) p_c",
            "interpretation": (
                "SU3/Nil still does not enter lambda_12 after p_U1 is selected, "
                "but it can enter the selection of p_U1 when p_U1 is physical hypercharge."
            ),
        },
        "inputs": {
            "p_c_circle_exact": p_circle,
            "p_SU2_sphere_exact": p_su2,
            "p_a_SU3_proxy_finite_part": p_su3_proxy,
            "target_lambda_12_witness": target_lambda,
        },
        "computed_branches": {
            "hypercharge_without_Qa_term": {
                "p_Y": p_y_without_qa,
                "lambda_12": lambda_without_qa,
                "residual_lambda_12": lambda_without_qa - target_lambda,
            },
            "hypercharge_with_proxy_SU3_finite_part": {
                "p_Y": p_y_with_proxy_qa,
                "lambda_12": lambda_with_proxy_qa,
                "residual_lambda_12": lambda_with_proxy_qa - target_lambda,
                "proxy_warning": estimator["verdict"]["reason"],
            },
            "required_Qa_threshold_for_target_if_embedding_is_correct": {
                "p_a_required": required_p_qa,
                "role": "diagnostic required value only, not proof data",
            },
        },
        "verdict": {
            "hypercharge_embedding_changes_u1_selection_problem": True,
            "nil_relevance_reopened_only_inside_pY_selection": True,
            "proxy_SU3_does_not_close": True,
            "numeric_electroweak_closure": False,
            "next_required_computation": (
                "Compute the selected p_a determinant for the Q_a stack and the "
                "selected p_c circle determinant in the same hypercharge-normalized "
                "threshold scheme."
            ),
        },
    }
    print(json.dumps(output, indent=2, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
