"""Build the protected diagonal-lane Riesz/Green/dotD packet."""

from __future__ import annotations

import json
import math
from pathlib import Path

import numpy as np

from build_selected_hym_operator_payload_extraction_from_diagonal_replay import fft_operators, replay_solution


ROOT = Path(__file__).resolve().parents[1]
OUT_CANDIDATE = ROOT / "candidate_data" / "selected_riesz_green_dotd_from_diagonal_end0_de.candidate.json"
OUT_CERT = ROOT / "certificates" / "selected_riesz_green_dotd_from_diagonal_end0_de_certificate.json"
OUT_PROOF = ROOT / "proof_corpus" / "MTT_Selected_Riesz_Green_dotD_From_Diagonal_End0_DE_v1.md"


def load(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def scalar_green(field: np.ndarray, solve_delta) -> np.ndarray:
    return -solve_delta(field - field.mean())


def main() -> int:
    end0_path = ROOT / "candidate_data" / "selected_end0_de_payload_from_diagonal_hym.candidate.json"
    replay_path = ROOT / "candidate_data" / "selected_full_exps_hym_newton_replay.candidate.json"
    overlap_path = ROOT / "candidate_data" / "selected_ext_overlap_hym_hodge_projector_table.candidate.json"

    end0 = load(end0_path)
    replay = load(replay_path)
    overlap = load(overlap_path)

    mesh = int(replay["solver"]["mesh"])
    unit_rescale = float(overlap["selected_row"]["unit_rescale_factor"])
    u, _rho, _lap = replay_solution(mesh, unit_rescale)
    solve_delta, lap_delta, deriv = fft_operators(u.shape)

    rng = np.random.default_rng(79)
    test = rng.normal(size=u.shape)
    test -= test.mean()
    green_test = scalar_green(test, solve_delta)
    green_residual = (-lap_delta(green_test)) - test
    green_residual_l2 = float(np.linalg.norm(green_residual.ravel()) / math.sqrt(green_residual.size))
    mean_projector_residual = float(abs(test.mean()))

    min_positive_eigenvalue = (2.0 * math.pi) ** 2
    green_norm_bound = 1.0 / min_positive_eigenvalue
    ad_t3 = end0["adjoint_connection_packet"]["ad_T3_matrix_on_basis_T1_T2_T3"]
    protected_t3_lane = [0.0, 0.0, 1.0]

    dotd_u_driver = {}
    for axis, label in enumerate(["x1", "y1", "x2", "y2"]):
        du = deriv(u, axis)
        dotd_u_driver[label] = {
            "formula": f"dotD_{label}[h] = (partial_{label} h) ad(T3); evaluated here on h=u",
            "driver": "u from selected diagonal HYM replay",
            "l2": float(np.linalg.norm(du.ravel()) / math.sqrt(du.size)),
            "min": float(du.min()),
            "max": float(du.max()),
        }

    protected_lane_closed = all(
        [
            end0["operator_payload_boundary"]["diagonal_End0_D_E_formula_extracted"] is True,
            ad_t3 == [[0, -1, 0], [1, 0, 0], [0, 0, 0]],
            green_residual_l2 < 1e-12,
            mean_projector_residual < 1e-14,
            min_positive_eigenvalue > 0,
        ]
    )

    candidate = {
        "candidate": "MTTSelectedRieszGreenDotDFromDiagonalEnd0DE",
        "status": "MTT_SELECTED_DIAGONAL_END0_RIESZ_GREEN_DOTD_PARTIAL_BUILT_ALPHA1_TRANSFER_OPEN",
        "closure_claimed": False,
        "target_fitting_used": False,
        "inputs": {
            "diagonal_End0_D_E_payload": str(end0_path),
            "diagonal_expS_replay": str(replay_path),
            "eta00_overlap_Hodge_projector_table": str(overlap_path),
        },
        "protected_T3_lane": {
            "closed": protected_lane_closed,
            "reason": "ad(T3) kills the T3 basis vector, so the diagonal T3 lane sees the scalar zero-mean Laplacian.",
            "basis_vector_T3": protected_t3_lane,
            "riesz_projector_formula": "P0[f] = mean(f) * T3",
            "complement_projector_formula": "Q[f] = f - mean(f)",
            "reduced_green_formula": "G = (-Delta)^(-1) on zero-mean scalar fields, tensor T3",
            "min_positive_eigenvalue_minus_delta": min_positive_eigenvalue,
            "green_operator_norm_bound": green_norm_bound,
            "mesh": mesh,
        },
        "numerical_green_replay": {
            "deterministic_seed": 79,
            "test_field_mean_abs_after_projection": mean_projector_residual,
            "green_residual_checked": "||(-Delta)GQf - Qf||_L2",
            "green_residual_l2": green_residual_l2,
        },
        "dotD_frechet_packet": {
            "formula_closed": protected_lane_closed,
            "general_formula": "For a scalar connection variation h*T3, dotD_a[h] = (partial_a h) ad(T3).",
            "evaluated_u_driver": dotd_u_driver,
            "physical_alpha1_driver_selected": False,
            "why_alpha1_still_open": "The replay supplies u, but the same-branch alpha1/sector derivative that downstream validators call dotD_alpha1 is not emitted by the selected rank2-to-sector transfer.",
        },
        "operator_payload_boundary": {
            "protected_T3_Riesz_projector_extracted": protected_lane_closed,
            "protected_T3_reduced_Green_extracted": protected_lane_closed,
            "formal_dotD_frechet_formula_extracted": protected_lane_closed,
            "physical_dotD_alpha1_payload_extracted": False,
            "T1_T2_coupled_covariant_Green_extracted": False,
            "rank2_to_rank3_sector_transfer_values_extracted": False,
            "validator_ready": False,
            "why_not_validator_ready": "Only the protected diagonal T3 scalar lane is closed. T1/T2 covariant spectral data, physical alpha1 dotD, sector transfer, and off-diagonal control remain open.",
        },
        "what_closes_now": {
            "protected_T3_zero_mode_Riesz_projector": protected_lane_closed,
            "protected_T3_zero_mean_reduced_Green": protected_lane_closed,
            "dotD_as_Frechet_derivative_schema": protected_lane_closed,
            "no_target_fitting_or_measured_constants": True,
        },
        "what_remains_open": {
            "T1_T2_coupled_covariant_Riesz_Green": True,
            "physical_dotD_alpha1_same_branch_driver": True,
            "rank2_to_rank3_sector_transfer_values": True,
            "offdiagonal_End0_vanish_or_control_bound": True,
            "validator_ready_D_E_Riesz_Green_dotD": True,
            "full_SM_or_no_knob_closure": True,
        },
        "superset_strategy": {
            "straight_path": "Protect and solve the T3 diagonal End0 spectral lane directly from D_E=d+ad(du*T3).",
            "support_path": "Use this as a legal same-source spectral seed for later sector transfer; do not promote Route-C/B_N or qutrit values.",
            "locked_target": "selected eta_00, diagonal HYM replay, T3 protected End0 lane, no measured constants.",
            "not_used": "No observed masses, mixings, couplings, benchmark matrices, inverse-search targets, or lifted flags.",
        },
        "next_required_artifact": "MTT_Selected_T1T2_Covariant_Green_or_Rank2Sector_Transfer_From_Diagonal_HYM_v1",
    }

    cert = {
        "certificate": "MTT_Selected_Riesz_Green_dotD_From_Diagonal_End0_DE_v1",
        "status": candidate["status"],
        "closure_claimed": False,
        "target_fitting_used": False,
        "protected_T3_lane_closed": protected_lane_closed,
        "green_residual_l2": green_residual_l2,
        "physical_dotD_alpha1_payload_extracted": False,
        "validator_ready": False,
        "next_required_artifact": candidate["next_required_artifact"],
    }

    proof = f"""# MTT Selected Riesz Green dotD From Diagonal End0 DE v1

## Result

The protected diagonal `T3` End0 spectral lane is closed:

```text
D_E = d + ad(du*T3)
ad(T3) T3 = 0
P0[f] = mean(f) * T3
G = (-Delta)^(-1) on zero-mean scalar fields, tensor T3
```

The deterministic Fourier replay gives:

```text
||(-Delta)GQf - Qf||_L2 = {green_residual_l2:.3e}
lambda_1(-Delta) = {min_positive_eigenvalue:.12g}
||G|| <= {green_norm_bound:.12g}
```

The formal Frechet derivative is also fixed:

```text
dotD_a[h] = (partial_a h) ad(T3)
```

## Guardrail

This is not full validator-ready `Riesz/Green/dotD` data. It closes the
protected diagonal `T3` spectral lane and the formal variation schema only.
The coupled `T1/T2` covariant Green operator, physical same-branch
`dotD_alpha1`, rank2-to-sector transfer, and off-diagonal control theorem
remain open.

## Next Artifact

`MTT_Selected_T1T2_Covariant_Green_or_Rank2Sector_Transfer_From_Diagonal_HYM_v1`.
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
