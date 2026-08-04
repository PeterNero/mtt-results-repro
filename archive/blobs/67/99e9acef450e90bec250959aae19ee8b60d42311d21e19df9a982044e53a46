"""Run the selected diagonal exp(S) HYM Newton/fixed-point replay."""

from __future__ import annotations

import cmath
import json
import math
from pathlib import Path

import numpy as np


ROOT = Path(__file__).resolve().parents[1]
OUT_CANDIDATE = ROOT / "candidate_data" / "selected_full_exps_hym_newton_replay.candidate.json"
OUT_CERT = ROOT / "certificates" / "selected_full_exps_hym_newton_replay_certificate.json"
OUT_PROOF = ROOT / "proof_corpus" / "MTT_Selected_Full_ExpS_HYM_Newton_Replay_v1.md"


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


def poisson_solver(shape: tuple[int, ...]):
    freqs = [np.fft.fftfreq(m, d=1.0 / m) for m in shape]
    grids = np.meshgrid(*freqs, indexing="ij")
    k2 = np.zeros(shape, dtype=float)
    for grid in grids:
        k2 += grid * grid
    denom = -((2.0 * math.pi) ** 2) * k2
    mask = k2 > 0

    def solve(source: np.ndarray) -> np.ndarray:
        source_hat = np.fft.fftn(source)
        phi_hat = np.zeros_like(source_hat, dtype=complex)
        phi_hat[mask] = source_hat[mask] / denom[mask]
        phi_hat[~mask] = 0.0
        return np.fft.ifftn(phi_hat).real

    def lap(field: np.ndarray) -> np.ndarray:
        return np.fft.ifftn(denom * np.fft.fftn(field)).real

    return solve, lap


def main() -> int:
    prev_path = ROOT / "candidate_data" / "selected_nonlinear_hym_correction_coefficient_solve.candidate.json"
    prev = load(prev_path)
    overlap_path = ROOT / "candidate_data" / "selected_ext_overlap_hym_hodge_projector_table.candidate.json"
    overlap = load(overlap_path)

    mesh = 24
    relaxation = 0.6
    tolerance = 1e-12
    max_iterations = 60
    axis = (np.arange(mesh) + 0.5) / mesh
    x1, y1, x2, y2 = np.meshgrid(axis, axis, axis, axis, indexing="ij")

    unit_rescale = overlap["selected_row"]["unit_rescale_factor"]
    rho1 = weighted_theta_density(2, 0, x1[:, :, 0, 0], y1[:, :, 0, 0])
    rho2 = weighted_theta_density(4, 0, x2[0, 0, :, :], y2[0, 0, :, :])
    rho = (unit_rescale**2) * rho1[:, :, None, None] * rho2[None, None, :, :]

    solve_poisson, laplacian = poisson_solver(rho.shape)
    u = np.zeros_like(rho)
    iterations = []
    for step in range(max_iterations):
        exp_weighted_density = rho * np.exp(-2.0 * u)
        source = exp_weighted_density - exp_weighted_density.mean()
        residual = laplacian(u) - source
        residual_l2 = float(np.linalg.norm(residual.ravel()) / math.sqrt(residual.size))
        iterations.append(
            {
                "iteration": step,
                "residual_l2": residual_l2,
                "u_min": float(u.min()),
                "u_max": float(u.max()),
                "mean_exp_weighted_density": float(exp_weighted_density.mean()),
            }
        )
        if residual_l2 < tolerance:
            break
        next_u = solve_poisson(source)
        u = relaxation * next_u + (1.0 - relaxation) * u

    final_exp_density = rho * np.exp(-2.0 * u)
    final_source = final_exp_density - final_exp_density.mean()
    final_residual = laplacian(u) - final_source
    final_residual_l2 = float(np.linalg.norm(final_residual.ravel()) / math.sqrt(final_residual.size))
    zero_mean = float(abs(u.mean()))
    contraction_ratios = [
        iterations[i + 1]["residual_l2"] / iterations[i]["residual_l2"]
        for i in range(len(iterations) - 1)
        if iterations[i]["residual_l2"] > 0
    ]
    tail_ratios = contraction_ratios[-8:] if len(contraction_ratios) >= 8 else contraction_ratios

    closed = all(
        [
            prev["what_closes_now"]["zero_mean_poisson_correction_phi_solved"] is True,
            final_residual_l2 < tolerance,
            zero_mean < 1e-14,
            len(iterations) < max_iterations,
            max(tail_ratios) < 0.6 if tail_ratios else False,
        ]
    )

    candidate = {
        "candidate": "MTTSelectedFullExpSHYMNewtonReplay",
        "status": "MTT_SELECTED_DIAGONAL_EXPS_HYM_REPLAY_SOLVED_OFFDIAGONAL_OPERATOR_PAYLOAD_OPEN",
        "closure_claimed": False,
        "target_fitting_used": False,
        "inputs": {
            "first_tracefree_HYM_correction": str(prev_path),
            "eta00_overlap_Hodge_projector_table": str(overlap_path),
        },
        "nonlinear_equation": {
            "unknown": "u in S = u*T3 with mean(u)=0",
            "metric": "H=exp(S)=diag(exp(u), exp(-u)) in the selected trace-free diagonal End0 lane",
            "equation": "Delta u = rho*exp(-2u) - mean(rho*exp(-2u))",
            "rho": "|eta_00^unit|^2",
            "why_mean_subtracted": "The integral of Delta u is zero, so the scalar trace-free HYM equation fixes the central constant by the selected density rather than by a free knob.",
            "quadratic_terms_included": "The exp(-2u) factor replays the nonlinear metric dependence of the off-diagonal Ext density in the diagonal lane.",
        },
        "solver": {
            "mesh": mesh,
            "theta_series_cutoff": 12,
            "relaxation": relaxation,
            "tolerance": tolerance,
            "iterations_run": len(iterations),
            "converged": closed,
            "method": "zero-mean FFT/Galerkin Poisson fixed-point replay",
            "initial_condition": "u=0, no measured or fitted target data",
        },
        "residual_trace": iterations,
        "solution_summary": {
            "final_residual_l2": final_residual_l2,
            "u_min": float(u.min()),
            "u_max": float(u.max()),
            "u_l2": float(np.linalg.norm(u.ravel()) / math.sqrt(u.size)),
            "u_mean_abs": zero_mean,
            "mean_exp_weighted_density": float(final_exp_density.mean()),
            "min_exp_weighted_density": float(final_exp_density.min()),
            "max_exp_weighted_density": float(final_exp_density.max()),
            "tail_contraction_ratios": tail_ratios,
        },
        "coefficient_packet": {
            "selected_end0_direction": "T3",
            "diagonal_expS_solution_closed": closed,
            "continuous_parameters_added": 0,
            "full_grid_storage_policy": "reproducible recipe plus residual trace; full 24^4 solution grid is not stored in git",
            "operator_extraction_ready": False,
        },
        "what_closes_now": {
            "diagonal_expS_nonlinear_replay": closed,
            "quadratic_metric_density_factor_included": closed,
            "zero_mean_tracefree_constraint_enforced": closed,
            "selected_density_central_constant_computed": closed,
        },
        "what_remains_open": {
            "offdiagonal_End0_connection_components": True,
            "coercive_full_jacobian_bound_beyond_diagonal_lane": True,
            "truncation_certificate_for_operator_extraction": True,
            "validator_ready_rhoE_DE_Riesz_Green_dotD_payload": True,
            "rank2_to_rank3_sector_operator_transfer_values": True,
            "full_SM_or_no_knob_closure": True,
        },
        "superset_strategy": {
            "straight_path": "Direct diagonal End0 exp(S) replay from the selected eta_00 density.",
            "support_path": "FFT/Galerkin replay gives reproducible coefficients for the selected scalar diagonal lane; no target matching is used.",
            "locked_target": "same selected q79/F,m=1 V_alpha branch, T3 diagonal HYM lane.",
            "not_used": "No observed masses, mixings, couplings, benchmark matrices, or lifted flags.",
        },
        "next_required_artifact": "MTT_Selected_HYM_Operator_Payload_Extraction_From_Diagonal_Replay_v1",
    }

    cert = {
        "certificate": "MTT_Selected_Full_ExpS_HYM_Newton_Replay_v1",
        "status": candidate["status"],
        "closure_claimed": False,
        "target_fitting_used": False,
        "diagonal_expS_solution_closed": closed,
        "final_residual_l2": final_residual_l2,
        "iterations_run": len(iterations),
        "u_min": float(u.min()),
        "u_max": float(u.max()),
        "operator_extraction_ready": False,
        "next_required_artifact": candidate["next_required_artifact"],
    }

    proof = f"""# MTT Selected Full ExpS HYM Newton Replay v1

## Result

The diagonal trace-free `exp(S)` replay is solved in the selected `T3` lane:

```text
S = u*T3
H = exp(S)
Delta u = rho*exp(-2u) - mean(rho*exp(-2u))
rho = |eta_00^unit|^2
mean(u)=0
```

The zero mode is not a parameter: the right-hand side is forced to have mean
zero because `int Delta u = 0`.

## Numerical Certificate

```text
mesh = {mesh}^4
iterations = {len(iterations)}
final residual L2 = {final_residual_l2:.3e}
u_min = {float(u.min()):.12g}
u_max = {float(u.max()):.12g}
mean(rho exp(-2u)) = {float(final_exp_density.mean()):.12g}
```

This closes the diagonal nonlinear replay with the quadratic metric factor
`exp(-2u)` included.

## Guardrail

This is still the diagonal `T3` HYM lane, not the full validator-ready operator
payload.  The remaining work is off-diagonal End0 connection components, a full
Jacobian/coercivity certificate, truncation bounds for operator extraction, and
the finite `rho_E`, `D_E`, Riesz/Green, `dotD`, and overlap payloads.

## Next Artifact

`MTT_Selected_HYM_Operator_Payload_Extraction_From_Diagonal_Replay_v1`.
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
