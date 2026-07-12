"""Estimate a zeta/heat-kernel finite part from cutoff determinant diagnostics.

This is a regulator candidate, not a final theorem.  It computes cutoff
determinant responses from the generated selected spectral-table candidate and
fits the large-cutoff sequence to a heat-kernel-style asymptotic basis.  The
constant term is reported as the finite-part diagnostic.
"""

from __future__ import annotations

import json
import math
import subprocess
import sys
import tempfile
from pathlib import Path

from generate_selected_gauge_factor_spectral_table import build_table


ROOT = Path(__file__).resolve().parents[1]
CALCULATOR = ROOT / "scripts" / "compute_selected_local_determinant_response.py"
BASIS = ("K2logK", "K2", "KlogK", "K", "logK", "constant")


def compute(table: dict) -> dict:
    with tempfile.NamedTemporaryFile("w", suffix=".json", delete=False, encoding="utf-8") as handle:
        json.dump(table, handle)
        path = Path(handle.name)
    try:
        proc = subprocess.run(
            [sys.executable, str(CALCULATOR), str(path)],
            cwd=ROOT,
            text=True,
            stdout=subprocess.PIPE,
            stderr=subprocess.STDOUT,
            check=True,
        )
        return json.loads(proc.stdout)
    finally:
        path.unlink(missing_ok=True)


def row(cutoff: int) -> dict:
    table = build_table(
        n=79,
        circle_n_max=cutoff,
        sphere_ell_max=cutoff,
        nil_m_max=cutoff,
        nil_p_max=cutoff,
        nil_k_max=cutoff,
    )
    result = compute(table)
    return {
        "cutoff": cutoff,
        "lambda_12": result["lambda_12"],
        "p": result["local_determinant_response_per_v1"],
        "mode_counts": result["mode_counts"],
    }


def basis_values(k: float) -> list[float]:
    logk = math.log(k)
    return [k * k * logk, k * k, k * logk, k, logk, 1.0]


def solve_linear_system(matrix: list[list[float]], vector: list[float]) -> list[float]:
    n = len(vector)
    aug = [matrix[i][:] + [vector[i]] for i in range(n)]
    for col in range(n):
        pivot = max(range(col, n), key=lambda row_index: abs(aug[row_index][col]))
        if abs(aug[pivot][col]) < 1e-12:
            raise ValueError("singular normal equation")
        aug[col], aug[pivot] = aug[pivot], aug[col]
        scale = aug[col][col]
        aug[col] = [entry / scale for entry in aug[col]]
        for row_index in range(n):
            if row_index == col:
                continue
            factor = aug[row_index][col]
            aug[row_index] = [
                entry - factor * aug[col][idx]
                for idx, entry in enumerate(aug[row_index])
            ]
    return [aug[i][-1] for i in range(n)]


def least_squares(rows: list[dict], key: str) -> dict:
    x_rows = [basis_values(float(item["cutoff"])) for item in rows]
    y = [float(item["lambda_12"] if key == "lambda_12" else item["p"][key]) for item in rows]
    cols = len(BASIS)
    normal = [[0.0 for _ in range(cols)] for _ in range(cols)]
    rhs = [0.0 for _ in range(cols)]
    for x, value in zip(x_rows, y):
        for i in range(cols):
            rhs[i] += x[i] * value
            for j in range(cols):
                normal[i][j] += x[i] * x[j]
    coeffs = solve_linear_system(normal, rhs)
    residuals = []
    for x, value in zip(x_rows, y):
        predicted = sum(c * xi for c, xi in zip(coeffs, x))
        residuals.append(value - predicted)
    return {
        "basis": list(BASIS),
        "coefficients": dict(zip(BASIS, coeffs)),
        "finite_part_constant": coeffs[-1],
        "max_abs_residual": max(abs(item) for item in residuals),
    }


def main() -> int:
    rows = [row(cutoff) for cutoff in range(3, 13)]
    fits = {
        "lambda_12": least_squares(rows, "lambda_12"),
        "U1": least_squares(rows, "U1"),
        "SU2": least_squares(rows, "SU2"),
        "SU3": least_squares(rows, "SU3"),
    }
    output = {
        "status": "FINITE_PART_ESTIMATOR_DIAGNOSTIC_NOT_FINAL_ZETA_THEOREM",
        "cutoff_range": [rows[0]["cutoff"], rows[-1]["cutoff"]],
        "rows": rows,
        "asymptotic_basis": list(BASIS),
        "fits": fits,
        "verdict": {
            "regularization_pipeline_built": True,
            "finite_part_candidate_available": True,
            "final_zeta_determinant_certified": False,
            "numeric_electroweak_closure": False,
            "reason": "The finite part depends on the proxy Nil spectrum, unit weights, and chosen asymptotic subtraction basis.",
        },
    }
    print(json.dumps(output, indent=2, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
