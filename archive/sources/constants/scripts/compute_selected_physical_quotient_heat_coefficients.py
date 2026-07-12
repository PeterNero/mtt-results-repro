"""Compute the Casimir heat-coefficient candidate for the physical quotient.

The previous quotient scan found that adjoint Casimir weights are the best
structural clue:

    Q_a / SU3 side: C_A(SU3) = 3
    Q_c / abelian circle side: normalized trace = 1
    SU2 side: C_A(SU2) = 2

This calculator promotes that clue into an auditable conditional gate.  It
does not certify selection.  Selection still requires deriving these weights
from the actual MTT gauge-threshold heat operator and physical quotient.
"""

from __future__ import annotations

import json
import math
import subprocess
import sys
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
STACK_TABLE = ROOT / "scripts" / "compute_stack_determinant_candidate_table.py"
C1_CERT = ROOT / "certificates" / "selected_electroweak_c1_response_interface_certificate.json"


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
    stack = run_json(STACK_TABLE)
    c1 = json.loads(C1_CERT.read_text(encoding="utf-8"))

    base = {
        "Qa_SU3_stack": float(stack["candidate_table"]["Qa_SU3_stack"]["value"]),
        "Qc_circle_stack": float(stack["candidate_table"]["Qc_circle_stack"]["value"]),
        "SU2_stack": float(stack["candidate_table"]["SU2_stack"]["value"]),
    }
    coefficients = {
        "Qa_SU3_stack": 3.0,
        "Qc_circle_stack": 1.0,
        "SU2_stack": 2.0,
    }
    weighted = {name: base[name] * coefficients[name] for name in base}

    p_y = weighted["Qa_SU3_stack"] / 36.0 + weighted["Qc_circle_stack"] / 4.0
    lambda_12 = p_y - weighted["SU2_stack"]
    v1_tilde = float(c1["selected_values"]["v1_tilde"])
    delta_g_12 = v1_tilde * lambda_12 / (4.0 * math.pi)
    target_lambda = float(c1["diagnostic_expected"]["lambda_12"])

    output = {
        "status": "CONDITIONAL_CASIMIR_HEAT_COEFFICIENT_MODEL_COMPUTED_NOT_SELECTED",
        "selected_physical_quotient_heat_coefficients": {
            "Qa_SU3_stack": {
                "coefficient": coefficients["Qa_SU3_stack"],
                "structural_source": "adjoint quadratic Casimir C_A(SU3)",
                "selection_status": "SOURCE_MOTIVATED_NOT_DERIVED_FROM_SELECTED_OPERATOR",
            },
            "Qc_circle_stack": {
                "coefficient": coefficients["Qc_circle_stack"],
                "structural_source": "normalized abelian trace",
                "selection_status": "SOURCE_MOTIVATED_NOT_DERIVED_FROM_SELECTED_OPERATOR",
            },
            "SU2_stack": {
                "coefficient": coefficients["SU2_stack"],
                "structural_source": "adjoint quadratic Casimir C_A(SU2)",
                "selection_status": "SOURCE_MOTIVATED_NOT_DERIVED_FROM_SELECTED_OPERATOR",
            },
        },
        "base_stack_values": base,
        "heat_weighted_stack_values": weighted,
        "hypercharge_accounting": {
            "p_Y": p_y,
            "lambda_12": lambda_12,
            "Delta_G_12": delta_g_12,
            "formula": "p_Y = p_a/36 + p_c/4; lambda_12 = p_Y - p_SU2; Delta_G_12 = v1_tilde*lambda_12/(4*pi)",
        },
        "diagnostic_comparison": {
            "target_lambda_12": target_lambda,
            "candidate_lambda_12": lambda_12,
            "residual_lambda_12": lambda_12 - target_lambda,
            "absolute_residual_lambda_12": abs(lambda_12 - target_lambda),
        },
        "verdict": {
            "heat_coefficient_accounting_built": True,
            "casimir_weights_source_motivated": True,
            "selected_by_corpus": False,
            "numeric_electroweak_closure": False,
            "new_no_knob_prediction_certified": False,
            "next_required_computation": (
                "Derive the heat coefficients and finite stack determinants from "
                "the selected gauge-threshold operator, retarded kernel, and "
                "physical quotient rather than from candidate proximity."
            ),
        },
    }
    print(json.dumps(output, indent=2, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
