"""Compute the exact scalar-proxy weak split from U1 circle and SU2 sphere pieces."""

from __future__ import annotations

import json
import math
import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
CIRCLE_SPHERE = ROOT / "scripts" / "compute_exact_circle_sphere_zeta.py"
C1_CERT = ROOT / "certificates" / "selected_electroweak_c1_response_interface_certificate.json"


def run_circle_sphere() -> dict:
    proc = subprocess.run(
        [sys.executable, str(CIRCLE_SPHERE)],
        cwd=ROOT,
        text=True,
        stdout=subprocess.PIPE,
        stderr=subprocess.STDOUT,
        check=True,
    )
    return json.loads(proc.stdout)


def main() -> int:
    pieces = run_circle_sphere()
    c1 = json.loads(C1_CERT.read_text(encoding="utf-8"))
    v1_tilde = float(c1["selected_values"]["v1_tilde"])
    target = float(c1["diagnostic_expected"]["lambda_12"])
    exact_split = float(pieces["finite_parts"]["U1_minus_SU2"])
    delta_g_12 = v1_tilde * exact_split / (4.0 * math.pi)
    target_delta_g_12 = v1_tilde * target / (4.0 * math.pi)

    output = {
        "status": "EXACT_SCALAR_PROXY_WEAK_SPLIT_COMPUTED_NOT_FINAL_CLOSURE",
        "input_pieces": pieces["finite_parts"],
        "weak_split": {
            "lambda_12": exact_split,
            "Delta_G_12": delta_g_12,
            "diagnostic_target_lambda_12": target,
            "diagnostic_target_Delta_G_12": target_delta_g_12,
            "residual_lambda_12": exact_split - target,
            "residual_Delta_G_12": delta_g_12 - target_delta_g_12,
        },
        "nil_independence": {
            "lambda_12_formula": "p_U1 - p_SU2",
            "SU3_nil_enters_lambda_12": False,
        },
        "verdict": {
            "u1_su2_scalar_proxy_split_closed": True,
            "matches_diagnostic_target": False,
            "numeric_electroweak_closure": False,
            "next_required_computation": "Promote scalar-proxy determinants and unit weights to selected gauge-threshold operators and topology-certified weights, or explain the residual.",
        },
    }
    print(json.dumps(output, indent=2, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
