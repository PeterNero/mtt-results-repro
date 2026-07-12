"""Extract diagonal HYM operator payload summaries from the exp(S) replay."""

from __future__ import annotations

import cmath
import json
import math
from pathlib import Path

import numpy as np


ROOT = Path(__file__).resolve().parents[1]
OUT_CANDIDATE = ROOT / "candidate_data" / "selected_hym_operator_payload_extraction_from_diagonal_replay.candidate.json"
OUT_CERT = ROOT / "certificates" / "selected_hym_operator_payload_extraction_from_diagonal_replay_certificate.json"
OUT_PROOF = ROOT / "proof_corpus" / "MTT_Selected_HYM_Operator_Payload_Extraction_From_Diagonal_Replay_v1.md"


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


def fft_operators(shape: tuple[int, ...]):
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

    def deriv(field: np.ndarray, axis: int) -> np.ndarray:
        field_hat = np.fft.fftn(field)
        factor = 2j * math.pi * grids[axis]
        return np.fft.ifftn(factor * field_hat).real

    return solve, lap, deriv


def replay_solution(mesh: int, unit_rescale: float) -> tuple[np.ndarray, np.ndarray, np.ndarray]:
    axis = (np.arange(mesh) + 0.5) / mesh
    x1, y1, x2, y2 = np.meshgrid(axis, axis, axis, axis, indexing="ij")
    rho1 = weighted_theta_density(2, 0, x1[:, :, 0, 0], y1[:, :, 0, 0])
    rho2 = weighted_theta_density(4, 0, x2[0, 0, :, :], y2[0, 0, :, :])
    rho = (unit_rescale**2) * rho1[:, :, None, None] * rho2[None, None, :, :]
    solve, lap, _ = fft_operators(rho.shape)
    u = np.zeros_like(rho)
    for _ in range(60):
        q = rho * np.exp(-2.0 * u)
        src = q - q.mean()
        residual = lap(u) - src
        if float(np.linalg.norm(residual.ravel()) / math.sqrt(residual.size)) < 1e-12:
            break
        u = 0.6 * solve(src) + 0.4 * u
    return u, rho, lap


def main() -> int:
    replay_path = ROOT / "candidate_data" / "selected_full_exps_hym_newton_replay.candidate.json"
    overlap_path = ROOT / "candidate_data" / "selected_ext_overlap_hym_hodge_projector_table.candidate.json"
    replay = load(replay_path)
    overlap = load(overlap_path)

    mesh = replay["solver"]["mesh"]
    unit_rescale = overlap["selected_row"]["unit_rescale_factor"]
    u, rho, lap = replay_solution(mesh, unit_rescale)
    _, _, deriv = fft_operators(u.shape)
    q = rho * np.exp(-2.0 * u)
    residual = lap(u) - (q - q.mean())
    residual_l2 = float(np.linalg.norm(residual.ravel()) / math.sqrt(residual.size))

    derivatives = {}
    grad_sq = np.zeros_like(u)
    for axis, label in enumerate(["x1", "y1", "x2", "y2"]):
        du = deriv(u, axis)
        grad_sq += du * du
        derivatives[label] = {
            "l2": float(np.linalg.norm(du.ravel()) / math.sqrt(du.size)),
            "min": float(du.min()),
            "max": float(du.max()),
        }
    grad_l2 = float(math.sqrt(float(grad_sq.mean())))
    exp_plus = np.exp(u)
    exp_minus = np.exp(-u)

    diagonal_payload_closed = all(
        [
            replay["coefficient_packet"]["diagonal_expS_solution_closed"] is True,
            residual_l2 < 1e-12,
            float(abs(u.mean())) < 1e-14,
            exp_plus.min() > 0,
            exp_minus.min() > 0,
        ]
    )

    candidate = {
        "candidate": "MTTSelectedHYMOperatorPayloadExtractionFromDiagonalReplay",
        "status": "MTT_SELECTED_HYM_DIAGONAL_OPERATOR_PAYLOAD_EXTRACTED_FULL_SECTOR_PAYLOAD_OPEN",
        "closure_claimed": False,
        "target_fitting_used": False,
        "inputs": {
            "diagonal_expS_replay": str(replay_path),
            "eta00_overlap_Hodge_projector_table": str(overlap_path),
        },
        "diagonal_metric_payload": {
            "closed": diagonal_payload_closed,
            "mesh": mesh,
            "H_diagonal": ["exp(u)", "exp(-u)"],
            "exp_u_min": float(exp_plus.min()),
            "exp_u_max": float(exp_plus.max()),
            "exp_minus_u_min": float(exp_minus.min()),
            "exp_minus_u_max": float(exp_minus.max()),
            "determinant": "exp(u)*exp(-u)=1 pointwise",
            "u_mean_abs": float(abs(u.mean())),
        },
        "diagonal_connection_payload": {
            "closed": diagonal_payload_closed,
            "connection_form": "A_diag = d u * T3 in the selected diagonal End0 lane",
            "gradient_direction_summaries": derivatives,
            "gradient_l2": grad_l2,
            "central_z3_direction": "zero in the current eta_00 diagonal replay because eta_00 has central degree zero",
        },
        "curvature_residual_payload": {
            "closed": diagonal_payload_closed,
            "equation_checked": "Delta u - (rho exp(-2u)-mean(rho exp(-2u)))",
            "residual_l2": residual_l2,
            "mean_rho_exp_minus_2u": float(q.mean()),
            "rho_exp_minus_2u_min": float(q.min()),
            "rho_exp_minus_2u_max": float(q.max()),
        },
        "operator_payload_boundary": {
            "diagonal_rank2_metric_connection_payload_extracted": diagonal_payload_closed,
            "rho_E_transition_tables_for_full_bundle_extracted": False,
            "D_E_matrix_on_selected_End0_basis_extracted": False,
            "Riesz_Green_dotD_payload_extracted": False,
            "rank2_to_rank3_sector_transfer_values_extracted": False,
            "validator_ready": False,
            "why_not_validator_ready": "The diagonal replay supplies a rank-2 metric/connection lane, but the existing downstream validators require full finite rho_E, D_E, Riesz/Green, dotD, and sector-transfer payloads.",
        },
        "what_closes_now": {
            "diagonal_metric_bounds": diagonal_payload_closed,
            "diagonal_connection_gradient_summaries": diagonal_payload_closed,
            "diagonal_curvature_residual_certificate": diagonal_payload_closed,
            "central_shared_circle_zero_direction_preserved": diagonal_payload_closed,
        },
        "what_remains_open": {
            "full_rhoE_transition_payload": True,
            "selected_DE_matrix_payload": True,
            "Riesz_Green_dotD_payload": True,
            "rank2_to_rank3_sector_transfer_values": True,
            "proof_offdiagonal_terms_vanish_or_are_controlled": True,
            "full_SM_or_no_knob_closure": True,
        },
        "superset_strategy": {
            "straight_path": "Extract rank-2 diagonal metric and connection payload from the selected exp(S) replay.",
            "support_path": "Use this payload as the source for a later End0/sector transfer extraction; do not promote it to full SM operator data yet.",
            "locked_target": "selected eta_00, T3 diagonal HYM lane, no measured constants.",
            "not_used": "No observed masses, mixings, couplings, benchmark matrices, or lifted flags.",
        },
        "next_required_artifact": "MTT_Selected_End0_DE_Payload_From_Diagonal_HYM_v1",
    }

    cert = {
        "certificate": "MTT_Selected_HYM_Operator_Payload_Extraction_From_Diagonal_Replay_v1",
        "status": candidate["status"],
        "closure_claimed": False,
        "target_fitting_used": False,
        "diagonal_payload_closed": diagonal_payload_closed,
        "residual_l2": residual_l2,
        "gradient_l2": grad_l2,
        "validator_ready": False,
        "next_required_artifact": candidate["next_required_artifact"],
    }

    proof = f"""# MTT Selected HYM Operator Payload Extraction From Diagonal Replay v1

## Result

The diagonal replay now emits a rank-2 metric/connection payload:

```text
H = diag(exp(u), exp(-u))
A_diag = d u * T3
```

The curvature residual remains at:

```text
||Delta u - (rho exp(-2u)-mean(rho exp(-2u)))||_L2 = {residual_l2:.3e}
```

The determinant is pointwise fixed:

```text
det(H)=1
```

and the central shared-circle direction remains zero.

## Guardrail

This is not yet validator-ready `rho_E/D_E/Riesz/Green/dotD` data. It is the
rank-2 diagonal metric/connection payload from which the next End0 extraction
must be built.

## Next Artifact

`MTT_Selected_End0_DE_Payload_From_Diagonal_HYM_v1`.
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
