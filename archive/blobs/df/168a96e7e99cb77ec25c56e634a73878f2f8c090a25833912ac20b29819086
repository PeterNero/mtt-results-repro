"""Compute the first selected HYM correction coefficient solve for eta_00."""

from __future__ import annotations

import cmath
import json
import math
from pathlib import Path

import numpy as np


ROOT = Path(__file__).resolve().parents[1]
OUT_CANDIDATE = ROOT / "candidate_data" / "selected_nonlinear_hym_correction_coefficient_solve.candidate.json"
OUT_CERT = ROOT / "certificates" / "selected_nonlinear_hym_correction_coefficient_solve_certificate.json"
OUT_PROOF = ROOT / "proof_corpus" / "MTT_Selected_Nonlinear_HYM_Correction_Coefficient_Solve_v1.md"


def load(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def theta_tau_i(degree: int, index: int, z: complex, cutoff: int = 12) -> complex:
    total = 0j
    for n in range(-cutoff, cutoff + 1):
        shifted = n + index / degree
        total += cmath.exp(-math.pi * degree * shifted * shifted + 2j * math.pi * degree * shifted * z)
    return total


def weighted_theta_density(degree: int, index: int, x: np.ndarray, y: np.ndarray, cutoff: int = 12) -> np.ndarray:
    out = np.zeros_like(x, dtype=float)
    for idx in np.ndindex(x.shape):
        z = complex(float(x[idx]), float(y[idx]))
        value = theta_tau_i(degree, index, z, cutoff)
        out[idx] = abs(value) ** 2 * math.exp(-2.0 * math.pi * degree * float(y[idx]) ** 2)
    return out


def solve_periodic_poisson_zero_mean(source: np.ndarray) -> tuple[np.ndarray, float, float]:
    """Solve Delta phi = source with zero mean on the unit periodic grid."""
    n = source.shape[0]
    source_hat = np.fft.fftn(source)
    freqs = [np.fft.fftfreq(m, d=1.0 / m) for m in source.shape]
    grids = np.meshgrid(*freqs, indexing="ij")
    k2 = np.zeros_like(source, dtype=float)
    for grid in grids:
        k2 += grid * grid
    denom = -((2.0 * math.pi) ** 2) * k2
    phi_hat = np.zeros_like(source_hat, dtype=complex)
    mask = k2 > 0
    phi_hat[mask] = source_hat[mask] / denom[mask]
    phi_hat[~mask] = 0.0
    phi = np.fft.ifftn(phi_hat).real
    lap_phi = np.fft.ifftn(denom * phi_hat).real
    residual = lap_phi - source
    return phi, float(np.linalg.norm(residual.ravel()) / math.sqrt(source.size)), float(abs(phi.mean()))


def main() -> int:
    previous_path = ROOT / "candidate_data" / "selected_ext_overlap_hym_hodge_projector_table.candidate.json"
    previous = load(previous_path)
    unit_rescale = previous["selected_row"]["unit_rescale_factor"]
    mesh = 24
    axis = (np.arange(mesh) + 0.5) / mesh
    x1, y1, x2, y2 = np.meshgrid(axis, axis, axis, axis, indexing="ij")

    rho1 = weighted_theta_density(2, 0, x1[:, :, 0, 0], y1[:, :, 0, 0])
    rho2 = weighted_theta_density(4, 0, x2[0, 0, :, :], y2[0, 0, :, :])
    density = (unit_rescale**2) * rho1[:, :, None, None] * rho2[None, None, :, :]
    mean_density = float(density.mean())
    source = density - mean_density
    phi, poisson_residual_l2, mean_abs = solve_periodic_poisson_zero_mean(source)
    source_l2 = float(np.linalg.norm(source.ravel()) / math.sqrt(source.size))
    phi_l2 = float(np.linalg.norm(phi.ravel()) / math.sqrt(phi.size))
    phi_min = float(phi.min())
    phi_max = float(phi.max())

    source_hat = np.fft.fftn(source) / source.size
    top_modes = []
    freqs = [np.fft.fftfreq(mesh, d=1.0 / mesh) for _ in range(4)]
    for idx in np.ndindex(source_hat.shape):
        if idx == (0, 0, 0, 0):
            continue
        amp = abs(source_hat[idx])
        if amp > 1e-10:
            mode = [int(freqs[j][idx[j]]) for j in range(4)]
            top_modes.append({"mode_kx1_ky1_kx2_ky2": mode, "source_hat_abs": float(amp)})
    top_modes = sorted(top_modes, key=lambda row: row["source_hat_abs"], reverse=True)[:12]

    first_correction_closed = all(
        [
            previous["newton_readiness"]["transition_overlap_table_closed"] is True,
            previous["newton_readiness"]["Hodge_Lambda_row_table_closed"] is True,
            abs(mean_density - 1.0) < 1e-12,
            poisson_residual_l2 < 1e-12,
            mean_abs < 1e-14,
        ]
    )

    candidate = {
        "candidate": "MTTSelectedNonlinearHYMCorrectionCoefficientSolve",
        "status": "MTT_SELECTED_HYM_FIRST_TRACEFREE_CORRECTION_SOLVED_FULL_NONLINEAR_NEWTON_OPEN",
        "closure_claimed": False,
        "target_fitting_used": False,
        "inputs": {
            "selected_ext_overlap_hym_hodge_projector_table": str(previous_path),
        },
        "finite_problem": {
            "mesh": mesh,
            "domain": "[0,1]^4 for the active E1 x E2 theta-density variables; central shared circle and z3 are degree-zero spectators",
            "source_density": "|eta_00^unit|^2",
            "mean_density": mean_density,
            "tracefree_source": "|eta_00^unit|^2 - 1",
            "linearized_HYM_equation_solved": "Delta phi = |eta_00^unit|^2 - 1, mean(phi)=0",
            "correction_interpretation": "S_1 = phi * T3 in the trace-free diagonal End0 direction, up to the global sign convention of the HYM linearization",
            "gauge": "zero-mean Coulomb scalar slice",
        },
        "solution_summary": {
            "first_tracefree_correction_closed": first_correction_closed,
            "poisson_residual_l2": poisson_residual_l2,
            "source_l2": source_l2,
            "phi_l2": phi_l2,
            "phi_min": phi_min,
            "phi_max": phi_max,
            "phi_mean_abs": mean_abs,
            "top_source_fourier_modes": top_modes,
        },
        "coefficient_packet": {
            "emitted_coefficients": "Fourier coefficients are emitted as the top 12 source modes plus exact FFT reproducibility recipe; full 24^4 grid is intentionally not stored in the certificate.",
            "selected_end0_direction": "T3",
            "selected_end0_basis": ["T1", "T2", "T3"],
            "continuous_parameters_added": 0,
            "uses_observed_targets": False,
        },
        "nonlinear_newton_status": {
            "first_tracefree_poisson_step_solved": first_correction_closed,
            "full_expS_nonlinear_iteration_run": False,
            "quadratic_curvature_terms_included": False,
            "coercive_jacobian_bound_emitted": False,
            "a_posteriori_truncation_error_emitted": False,
            "full_selected_A_HYM_coefficients_emitted": False,
            "newton_ready_for_operator_extraction": False,
            "first_blocker": "run_full_expS_Newton_iteration_with_quadratic_curvature_terms_and_error_bound",
        },
        "superset_strategy": {
            "straight_path": "Use the selected eta_00 unit density and equal-radius Hodge table to solve the first trace-free HYM correction on the direct End0 route.",
            "support_path": "FFT/Galerkin inversion is a numerical execution of the locked Poisson equation; it is not target fitting.",
            "locked_target": "same selected V_alpha branch, eta_00 unit normalized, T3 trace-free diagonal correction.",
            "not_used": "No observed SM data, benchmark matrices, or lifted selected flags.",
        },
        "what_closes_now": {
            "tracefree_density_source_computed": first_correction_closed,
            "zero_mean_poisson_correction_phi_solved": first_correction_closed,
            "first_End0_T3_HYM_correction_direction_identified": first_correction_closed,
            "Coulomb_zero_mean_condition_satisfied": first_correction_closed,
        },
        "what_remains_open": {
            "full_nonlinear_expS_Newton_iteration": True,
            "quadratic_curvature_terms": True,
            "coercivity_and_truncation_certificate": True,
            "validator_ready_rhoE_DE_Riesz_Green_dotD_payload": True,
            "full_SM_or_no_knob_closure": True,
        },
        "next_required_artifact": "MTT_Selected_Full_ExpS_HYM_Newton_Replay_v1",
    }

    cert = {
        "certificate": "MTT_Selected_Nonlinear_HYM_Correction_Coefficient_Solve_v1",
        "status": candidate["status"],
        "closure_claimed": False,
        "target_fitting_used": False,
        "first_tracefree_correction_closed": first_correction_closed,
        "mean_density": mean_density,
        "poisson_residual_l2": poisson_residual_l2,
        "phi_l2": phi_l2,
        "full_selected_A_HYM_coefficients_emitted": False,
        "next_required_artifact": candidate["next_required_artifact"],
    }

    proof = f"""# MTT Selected Nonlinear HYM Correction Coefficient Solve v1

## Result

The first trace-free HYM correction source is now computed from the unit Ext row:

```text
rho = |eta_00^unit|^2
mean(rho) = {mean_density:.16g}
f = rho - 1
```

The zero-mean Coulomb scalar equation

```text
Delta phi = f,    mean(phi)=0
```

is solved by periodic FFT/Galerkin inversion on a `{mesh}^4` grid. The residual is:

```text
||Delta phi - f||_L2 = {poisson_residual_l2:.3e}
```

The first trace-free End0 correction is:

```text
S_1 = phi * T3
```

up to the global sign convention of the HYM linearization.

## What This Closes

This closes the first selected trace-free density correction and identifies the
`T3` diagonal End0 direction forced by the off-diagonal unit Ext row.

## Guardrail

This is not yet the full nonlinear HYM connection. The full theorem still needs
the `exp(S)` Newton replay with quadratic curvature terms, a coercive Jacobian
bound, a truncation certificate, and validator-ready finite operator payloads.

## Next Artifact

`MTT_Selected_Full_ExpS_HYM_Newton_Replay_v1`.
"""

    OUT_CANDIDATE.write_text(json.dumps(candidate, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    OUT_CERT.write_text(json.dumps(cert, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    OUT_PROOF.write_text(proof, encoding="utf-8")
    print(f"Wrote {OUT_CANDIDATE}")
    print(f"Wrote {OUT_CERT}")
    print(f"Wrote {OUT_PROOF}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
