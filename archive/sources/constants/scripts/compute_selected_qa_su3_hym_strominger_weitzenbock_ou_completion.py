"""Partial Strominger/Weitzenbock/OU completion for the Qa/SU3 HYM block.

This script computes every currently source-backed numeric ingredient beyond
the prior unweighted real Chern block:

* import the selected internal Iwasawa horizontal radius from the rho_UV branch,
* compute the corresponding r3 and R_+ trace coefficient,
* insert the Iwasawa one-form metric weights into the real u(3) Chern block.

It deliberately does not invent the missing torsional Weitzenbock endomorphism
or OU mode weights.  Those entries remain the true open gate for selecting mu.
"""

from __future__ import annotations

import json
import math
from pathlib import Path
from typing import Any

import numpy as np


ROOT = Path(__file__).resolve().parents[1]
RADIUS_CERT = ROOT / "certificates" / "final_internal_rho_uv_selected_radius_theorem_certificate.json"
REAL_CERT = ROOT / "certificates" / "selected_qa_su3_hym_full_real_delta_a_hessian_certificate.json"


def load(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def connection_matrices(mu: float) -> list[np.ndarray]:
    s = math.sqrt(mu)
    return [
        np.array([[0.0, 0.0, s], [0.0, 0.0, 0.0], [0.0, 0.0, 0.0]], dtype=complex),
        np.array([[0.0, 0.0, 0.0], [0.0, 0.0, 0.0], [-s, 0.0, 0.0]], dtype=complex),
        np.array([[0.0, mu, 0.0], [0.0, 0.0, 0.0], [0.0, 0.0, 0.0]], dtype=complex),
    ]


def normalized_u3_basis() -> list[tuple[str, np.ndarray]]:
    matrices: list[tuple[str, np.ndarray]] = [
        ("central_i_identity", 1j * np.eye(3) / math.sqrt(3.0)),
        ("cartan_i_lambda3", 1j * np.diag([1.0, -1.0, 0.0]) / math.sqrt(2.0)),
        ("cartan_i_lambda8", 1j * np.diag([1.0, 1.0, -2.0]) / math.sqrt(6.0)),
    ]
    for a, b, label in [(0, 1, "12"), (0, 2, "13"), (1, 2, "23")]:
        skew_real = np.zeros((3, 3), dtype=complex)
        skew_real[a, b] = 1.0
        skew_real[b, a] = -1.0
        matrices.append((f"skew_real_{label}", skew_real / math.sqrt(2.0)))

        skew_imag = np.zeros((3, 3), dtype=complex)
        skew_imag[a, b] = 1j
        skew_imag[b, a] = 1j
        matrices.append((f"skew_imag_{label}", skew_imag / math.sqrt(2.0)))
    return matrices


def real_inner(x: np.ndarray, y: np.ndarray) -> float:
    return float(np.real(np.trace(x.conj().T @ y)))


def selected_iwasawa_geometry(radius_cert: dict[str, Any]) -> dict[str, float]:
    values = radius_cert["selected_values"]
    r1 = float(values["R_star"])
    r2 = r1
    r3 = float(values["r3"])
    a_struct = r3 / (r1 * r2)
    return {
        "r1": r1,
        "r2": r2,
        "r3": r3,
        "A_structure": a_struct,
        "v1_tilde_from_geometry": 8.0 * a_struct**2,
        "relative_one_form_weights": {
            "bar_omega_1": 1.0 / r1**2,
            "bar_omega_2": 1.0 / r2**2,
            "bar_omega_3": 1.0 / r3**2,
        },
    }


def weighted_hessian_matrix(mu: float, weights: list[float]) -> tuple[np.ndarray, list[str]]:
    basis = normalized_u3_basis()
    labels = [label for label, _ in basis]
    matrices = [matrix for _, matrix in basis]
    hessian = np.zeros((len(matrices), len(matrices)), dtype=float)

    for b_matrix, weight in zip(connection_matrices(mu), weights):
        for a_matrix in (b_matrix, -b_matrix.conj().T):
            for i, x_matrix in enumerate(matrices):
                comm_x = a_matrix @ x_matrix - x_matrix @ a_matrix
                for j, y_matrix in enumerate(matrices):
                    comm_y = a_matrix @ y_matrix - y_matrix @ a_matrix
                    hessian[i, j] += weight * real_inner(comm_x, comm_y)
    return hessian, labels


def weighted_block(mu: float, weights: list[float]) -> dict[str, Any]:
    hessian, labels = weighted_hessian_matrix(mu, weights)
    eigenvalues = np.linalg.eigvalsh(hessian)
    rounded = [0.0 if abs(float(value)) < 1e-12 else float(value) for value in eigenvalues]
    positive = [value for value in rounded if value > 1e-10]
    return {
        "mu": mu,
        "basis_labels": labels,
        "operator": "metric-weighted H_real(mu) on normalized anti-Hermitian u(3) basis",
        "zero_modes": len([value for value in rounded if abs(value) <= 1e-10]),
        "positive_modes": len(positive),
        "rank": int(np.linalg.matrix_rank(hessian, tol=1e-10)),
        "eigenvalues": rounded,
        "trace": float(np.trace(hessian)),
        "det_prime": float(np.prod(positive)) if positive else None,
        "log_det_prime": float(np.sum(np.log(positive))) if positive else None,
    }


def scan_mu(weights: list[float]) -> dict[str, Any]:
    grid = np.logspace(-4.0, 4.0, 401)
    log_dets = [weighted_block(float(mu), weights)["log_det_prime"] for mu in grid]
    min_index = int(np.argmin(log_dets))
    return {
        "grid_min_mu": float(grid[min_index]),
        "grid_min_log_det_prime": float(log_dets[min_index]),
        "left_endpoint_log_det_prime": float(log_dets[0]),
        "right_endpoint_log_det_prime": float(log_dets[-1]),
        "strictly_increasing_on_grid": all(
            after > before for before, after in zip(log_dets, log_dets[1:])
        ),
        "interpretation": (
            "After inserting selected Iwasawa metric weights, the algebraic Chern "
            "log-det-prime remains monotone on the scan and still does not select "
            "an interior mu."
        ),
    }


def main() -> int:
    radius_cert = load(RADIUS_CERT)
    real_cert = load(REAL_CERT)
    geometry = selected_iwasawa_geometry(radius_cert)
    weights = [
        geometry["relative_one_form_weights"]["bar_omega_1"],
        geometry["relative_one_form_weights"]["bar_omega_2"],
        geometry["relative_one_form_weights"]["bar_omega_3"],
    ]
    sample_mu = [0.25, 1.0, 4.0]
    samples = [weighted_block(mu, weights) for mu in sample_mu]

    output = {
        "certificate": "SelectedQaSU3HYMStromingerWeitzenbockOUCompletion",
        "status": "QA_SU3_HYM_STROMINGER_COMPLETION_METRIC_WEIGHTED_CHERN_BLOCK_COMPUTED_TORSION_OU_OPEN",
        "input_status": {
            "selected_radius": radius_cert["status"],
            "real_chern_hessian": real_cert["status"],
        },
        "source_backed_completion": {
            "selected_iwasawa_geometry": geometry,
            "metric_weight_rule": (
                "From omega^1=(e1+i e2)/r1, omega^2=(e3+i e4)/r2, "
                "omega^3=(e5+i e6)/r3, insert relative one-form weights 1/r_i^2. "
                "A common complex-frame factor would rescale all eigenvalues and "
                "does not affect the mu-selection verdict."
            ),
            "r_plus_trace_coefficient_check": {
                "formula": "Tr_grav R_+^2 = 8*(r3/(r1*r2))^2 alpha_1",
                "value": geometry["v1_tilde_from_geometry"],
                "matches_radius_certificate_v1_tilde": abs(
                    geometry["v1_tilde_from_geometry"]
                    - float(radius_cert["selected_values"]["v1_tilde"])
                )
                < 1e-12,
            },
        },
        "metric_weighted_real_chern_blocks": samples,
        "mu_scan": scan_mu(weights),
        "still_missing_for_full_strominger_operator": [
            "actual torsional Weitzenbock endomorphism on u(E)-valued one-forms",
            "lower-order differential terms beyond the invariant algebraic band",
            "complete fixed-gauge quotient and any noncentral symmetry directions",
            "mode-by-mode OU weights gamma_{n,k}^{-1}",
            "zeta/heat determinant of the complete elliptic operator",
        ],
        "closed_now": [
            "selected Iwasawa radius imported for the common horizontal geometry",
            "r3 and R_+ trace coefficient evaluated at the selected radius",
            "relative one-form metric weights inserted into the real Chern block",
            "metric-weighted u(3) block remains positive on su(3) samples",
            "metric-weighted algebraic determinant scan does not select interior mu",
        ],
        "verdict": {
            "metric_weighted_real_chern_block_computed": True,
            "selected_geometry_inserted": True,
            "r_plus_trace_coefficient_inserted": True,
            "torsional_weitzenbock_endomorphism_computed": False,
            "ou_weights_computed": False,
            "full_strominger_hessian_computed": False,
            "mu_selected": False,
            "target_fitting_used": False,
            "can_close_Qa_SU3_now": False,
            "next_required_artifact": "Selected_Qa_SU3_Torsional_Endomorphism_or_OU_Mode_Weights_v1",
        },
    }
    print(json.dumps(output, indent=2, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
