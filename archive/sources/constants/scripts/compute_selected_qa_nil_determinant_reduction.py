"""Reduce the remaining Qa/SU3-Nil determinant gate to computable data.

This calculation deliberately separates three layers:

1. The selected weak-split value required of Qa after Qc and SU2 closure.
2. The old cutoff-fitted SU3/Nil proxy already carried by the repo.
3. Oscillator-completion diagnostics for the compact Nil p != 0 sector.

The oscillator branches are not selected proof data.  They are useful because
the Theta corpus reduces the p != 0 Nil Laplacian to a magnetic oscillator
operator, but the corpus does not yet certify the compact-theta multiplicities
or the selected Qa gauge/ghost quotient determinant.
"""

from __future__ import annotations

import json
import math
import subprocess
import sys
from pathlib import Path
from typing import Any, Callable


ROOT = Path(__file__).resolve().parents[1]
ESTIMATOR = ROOT / "scripts" / "estimate_selected_zeta_finite_part.py"
HEAT_CERT = ROOT / "certificates" / "selected_physical_quotient_heat_coefficients_certificate.json"
QC_CERT = ROOT / "certificates" / "selected_qc_circle_gauge_block_equivalence_certificate.json"
SU2_CERT = ROOT / "certificates" / "selected_flat_fp_quotient_normalization_policy_certificate.json"
R1_CERT = ROOT / "certificates" / "selected_central_circle_damping_identification_lemma_certificate.json"

BASIS = ("K2logK", "K2", "KlogK", "K", "logK", "constant")


def load(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


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


def least_squares(cutoff_rows: list[dict[str, float]], key: str = "total") -> dict[str, Any]:
    x_rows = [basis_values(float(item["cutoff"])) for item in cutoff_rows]
    y = [float(item[key]) for item in cutoff_rows]
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


def selected_r1_for_n(cert: dict[str, Any], n_value: int) -> float:
    for row in cert["tested_cases"]:
        if int(row["N"]) == n_value:
            return float(row["R1_z64_normalized"])
    raise KeyError(f"N={n_value} not found in selected central-circle certificate")


def nil_p0_logdet(cutoff: int) -> float:
    total = 0.0
    for m in range(-cutoff, cutoff + 1):
        for n in range(-cutoff, cutoff + 1):
            if m == 0 and n == 0:
                continue
            eigenvalue = 4.0 * math.pi * math.pi * float(m * m + n * n)
            total += math.log(eigenvalue)
    return total


def nil_p_nonzero_logdet(
    cutoff: int,
    c_nil: float,
    multiplicity: Callable[[int], float],
) -> float:
    total = 0.0
    for p in range(1, cutoff + 1):
        for k in range(0, cutoff + 1):
            eigenvalue = (
                2.0 * math.pi * p * (2.0 * k + 1.0)
                + (2.0 * math.pi * p) ** 2 / (c_nil * c_nil)
            )
            total += multiplicity(p) * math.log(eigenvalue)
    return total


def oscillator_branch(
    name: str,
    description: str,
    c_nil: float,
    multiplicity: Callable[[int], float],
) -> dict[str, Any]:
    rows = []
    for cutoff in range(6, 19):
        p0 = nil_p0_logdet(cutoff)
        p_nonzero = nil_p_nonzero_logdet(cutoff, c_nil, multiplicity)
        rows.append(
            {
                "cutoff": float(cutoff),
                "p0_torus_exact_cutoff_logdet": p0,
                "p_nonzero_oscillator_cutoff_logdet": p_nonzero,
                "total": p0 + p_nonzero,
            }
        )
    fit = least_squares(rows)
    return {
        "name": name,
        "status": "DIAGNOSTIC_OSCILLATOR_COMPLETION_NOT_SELECTED",
        "description": description,
        "cutoff_range": [int(rows[0]["cutoff"]), int(rows[-1]["cutoff"])],
        "finite_part_constant": fit["finite_part_constant"],
        "max_abs_residual": fit["max_abs_residual"],
        "fit": fit,
        "sample_rows": [rows[0], rows[len(rows) // 2], rows[-1]],
    }


def hypercharge_lambda(p_a_heat_weighted: float, p_c: float, p_su2: float) -> float:
    return p_a_heat_weighted / 36.0 + p_c / 4.0 - p_su2


def main() -> int:
    heat = load(HEAT_CERT)
    qc = load(QC_CERT)
    su2 = load(SU2_CERT)
    r1_cert = load(R1_CERT)
    estimator = run_json(ESTIMATOR)

    target_lambda = float(heat["diagnostic_comparison"]["target_lambda_12"])
    p_c = float(qc["selected_values"]["selected_p_Qc_for_weak_split"])
    p_su2 = float(su2["selected_flat_su2_data"]["selected_p_SU2_for_weak_split"])
    heat_weight = 3.0

    required_p_a_heat = 36.0 * (target_lambda + p_su2 - p_c / 4.0)
    required_p_a_unweighted = required_p_a_heat / heat_weight

    old_proxy_unweighted = float(estimator["fits"]["SU3"]["finite_part_constant"])
    old_proxy_heat = heat_weight * old_proxy_unweighted
    old_proxy_lambda = hypercharge_lambda(old_proxy_heat, p_c, p_su2)

    r1 = selected_r1_for_n(r1_cert, 79)
    c_nil = 1.439 * r1

    branches = [
        oscillator_branch(
            "sign_pair_unit_multiplicity",
            "p>0 oscillator levels with a sign-pair multiplicity 2; this matches the old lower-proxy convention.",
            c_nil,
            lambda p: 2.0,
        ),
        oscillator_branch(
            "single_abs_p_multiplicity",
            "p>0 oscillator levels with multiplicity |p|; diagnostic compact-Nil theta-sector candidate.",
            c_nil,
            lambda p: float(p),
        ),
        oscillator_branch(
            "sign_pair_abs_p_multiplicity",
            "p>0 oscillator levels with multiplicity 2|p|; diagnostic compact-Nil theta-sector candidate.",
            c_nil,
            lambda p: 2.0 * float(p),
        ),
    ]

    branch_summaries = []
    for branch in branches:
        unweighted = float(branch["finite_part_constant"])
        heat_value = heat_weight * unweighted
        candidate_lambda = hypercharge_lambda(heat_value, p_c, p_su2)
        branch_summaries.append(
            {
                "name": branch["name"],
                "unweighted_finite_part_candidate": unweighted,
                "heat_weighted_p_a_candidate": heat_value,
                "lambda_12_candidate": candidate_lambda,
                "residual_lambda_12": candidate_lambda - target_lambda,
                "absolute_residual_lambda_12": abs(candidate_lambda - target_lambda),
                "selected": False,
                "reason_not_selected": "Corpus does not yet certify the compact Nil p!=0 multiplicity/theta sectors or the selected Qa gauge/ghost quotient.",
            }
        )

    output = {
        "status": "QA_NIL_DETERMINANT_REDUCED_TO_EXACT_TARGET_AND_DIAGNOSTIC_OSCILLATOR_BRANCHES_OPEN",
        "selected_inputs": {
            "N": 79,
            "R1_z64_normalized": r1,
            "c_nil": c_nil,
            "c_nil_formula": "c_nil = 1.439 * R1_z64_normalized",
            "a_nil": 1.0,
            "b_nil": 1.0,
            "p_Qc_selected": p_c,
            "p_SU2_selected": p_su2,
            "target_lambda_12_diagnostic": target_lambda,
            "Qa_heat_weight": heat_weight,
        },
        "exact_required_Qa_after_Qc_SU2_closure": {
            "formula": "p_a_required = 36*(lambda_12_target + p_SU2_selected - p_Qc_selected/4)",
            "heat_weighted_p_a_required": required_p_a_heat,
            "unweighted_p_a_required_if_CA_SU3_is_3": required_p_a_unweighted,
            "not_a_fit": "This is the algebraic target imposed by already selected Qc/SU2 plus the diagnostic lambda_12 witness; it is not used to select a branch.",
        },
        "old_proxy_comparison": {
            "status": "OLD_PROXY_OVERSHOOTS_REQUIRED_QA",
            "unweighted_proxy_finite_part": old_proxy_unweighted,
            "heat_weighted_proxy_p_a": old_proxy_heat,
            "lambda_12_from_old_proxy": old_proxy_lambda,
            "residual_lambda_12_from_old_proxy": old_proxy_lambda - target_lambda,
            "heat_weighted_excess_over_required": old_proxy_heat - required_p_a_heat,
            "unweighted_excess_over_required": old_proxy_unweighted - required_p_a_unweighted,
        },
        "source_certified_nil_data": {
            "p0_torus_sector": "exact eigenvalues 4*pi^2*(m^2+n^2) for a=b=1",
            "p_nonzero_sector": "magnetic oscillator operator Delta_p is source-supported, but compact spectral multiplicities/theta characters are not certified here",
            "oscillator_eigenvalue_schema_used_diagnostically": "lambda_{p,k}=2*pi*p*(2*k+1)+(2*pi*p)^2/c_nil^2 for p>=1, k>=0",
        },
        "diagnostic_oscillator_branches": branches,
        "diagnostic_branch_summaries": branch_summaries,
        "verdict": {
            "required_Qa_value_computed": True,
            "old_proxy_shown_not_to_close": True,
            "oscillator_completion_calculated": True,
            "oscillator_completion_selected": False,
            "qa_nil_selected_determinant_closed": False,
            "numeric_electroweak_closure_certified": False,
            "next_required_artifact": "Exact_Selected_Nil_Gauge_Threshold_Zeta_Determinant_v1",
            "remaining_missing_inputs": [
                "compact Nil p!=0 multiplicities/theta-character sectors for the selected lattice",
                "selected Qa/SU3 gauge-threshold operator rather than scalar Laplacian proxy",
                "BRST/ghost quotient policy for the Qa nonabelian block",
                "analytic zeta finite part or source-certified heat coefficients",
            ],
        },
    }
    print(json.dumps(output, indent=2, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
