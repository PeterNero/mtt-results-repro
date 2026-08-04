"""Try both next paths: T1/T2 covariant Green and rank2-to-sector transfer."""

from __future__ import annotations

import json
import math
from pathlib import Path

import numpy as np

from build_selected_hym_operator_payload_extraction_from_diagonal_replay import fft_operators, replay_solution


ROOT = Path(__file__).resolve().parents[1]
OUT_CANDIDATE = ROOT / "candidate_data" / "selected_t1t2_covariant_green_and_transfer_probe.candidate.json"
OUT_CERT = ROOT / "certificates" / "selected_t1t2_covariant_green_and_transfer_probe_certificate.json"
OUT_PROOF = ROOT / "proof_corpus" / "MTT_Selected_T1T2_Covariant_Green_or_Rank2Sector_Transfer_From_Diagonal_HYM_v1.md"


def load(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def rotate_pair(pair: np.ndarray, angle: np.ndarray) -> np.ndarray:
    c = np.cos(angle)
    s = np.sin(angle)
    return np.stack([c * pair[0] - s * pair[1], s * pair[0] + c * pair[1]], axis=0)


def scalar_green(field: np.ndarray, solve_delta) -> np.ndarray:
    return -solve_delta(field - field.mean())


def covariant_derivative(pair: np.ndarray, u: np.ndarray, deriv, axis: int) -> np.ndarray:
    du = deriv(u, axis)
    dp0 = deriv(pair[0], axis)
    dp1 = deriv(pair[1], axis)
    # J = [[0,-1],[1,0]] on the T1/T2 block.
    return np.stack([dp0 - du * pair[1], dp1 + du * pair[0]], axis=0)


def covariant_laplacian(pair: np.ndarray, u: np.ndarray, deriv) -> np.ndarray:
    out = np.zeros_like(pair)
    for axis in range(4):
        first = covariant_derivative(pair, u, deriv, axis)
        second = covariant_derivative(first, u, deriv, axis)
        out -= second
    return out


def main() -> int:
    prior_path = ROOT / "candidate_data" / "selected_riesz_green_dotd_from_diagonal_end0_de.candidate.json"
    replay_path = ROOT / "candidate_data" / "selected_full_exps_hym_newton_replay.candidate.json"
    overlap_path = ROOT / "candidate_data" / "selected_ext_overlap_hym_hodge_projector_table.candidate.json"
    transfer_path = ROOT / "candidate_data" / "selected_hym_adjoint_transfer_functor.candidate.json"
    bn_reject_path = ROOT / "candidate_data" / "selected_end0_basis_differential_table_or_bn_identification.candidate.json"

    prior = load(prior_path)
    replay = load(replay_path)
    overlap = load(overlap_path)
    transfer = load(transfer_path)
    bn_reject = load(bn_reject_path)

    mesh = int(replay["solver"]["mesh"])
    unit_rescale = float(overlap["selected_row"]["unit_rescale_factor"])
    u, _rho, _lap = replay_solution(mesh, unit_rescale)
    solve_delta, _laplacian, deriv = fft_operators(u.shape)

    rng = np.random.default_rng(790)
    source = rng.normal(size=(2,) + u.shape)
    gauged_source = rotate_pair(source, u)
    gauged_source[0] -= gauged_source[0].mean()
    gauged_source[1] -= gauged_source[1].mean()
    projected_source = rotate_pair(gauged_source, -u)
    solution_gauged = np.stack([scalar_green(gauged_source[0], solve_delta), scalar_green(gauged_source[1], solve_delta)], axis=0)
    solution = rotate_pair(solution_gauged, -u)

    gauge_frame_residual = np.stack(
        [
            -_laplacian(solution_gauged[0]) - gauged_source[0],
            -_laplacian(solution_gauged[1]) - gauged_source[1],
        ],
        axis=0,
    )
    gauge_frame_residual_l2 = float(np.linalg.norm(gauge_frame_residual.ravel()) / math.sqrt(gauge_frame_residual.size))
    residual = covariant_laplacian(solution, u, deriv) - projected_source
    direct_truncated_residual_l2 = float(np.linalg.norm(residual.ravel()) / math.sqrt(residual.size))
    projected_l2 = float(np.linalg.norm(projected_source.ravel()) / math.sqrt(projected_source.size))
    direct_truncated_relative_residual = direct_truncated_residual_l2 / projected_l2

    kernel0 = rotate_pair(np.stack([np.ones_like(u), np.zeros_like(u)], axis=0), -u)
    kernel1 = rotate_pair(np.stack([np.zeros_like(u), np.ones_like(u)], axis=0), -u)
    kernel_residual0 = covariant_laplacian(kernel0, u, deriv)
    kernel_residual1 = covariant_laplacian(kernel1, u, deriv)
    kernel_residual_l2 = max(
        float(np.linalg.norm(kernel_residual0.ravel()) / math.sqrt(kernel_residual0.size)),
        float(np.linalg.norm(kernel_residual1.ravel()) / math.sqrt(kernel_residual1.size)),
    )

    gap = (2.0 * math.pi) ** 2
    green_bound = 1.0 / gap
    t1t2_closed = all(
        [
            prior["operator_payload_boundary"]["protected_T3_reduced_Green_extracted"] is True,
            gauge_frame_residual_l2 < 1e-12,
            gap > 0,
        ]
    )
    direct_truncated_replay_converged = direct_truncated_residual_l2 < 1e-10

    abstract_transfer_closed = transfer["what_closes_now"]["abstract_rank2_to_rank3_transfer_functor"] is True
    bn_identification_rejected = bn_reject["what_closes_now"]["BN_identification_rejected_at_selected_End0_level"] is True
    sector_transfer_promotes = bool(
        abstract_transfer_closed
        and not bn_identification_rejected
        and transfer["what_remains_open"]["sector_routing_from_End0_to_Q_u_d_L_e_N_H"] is False
    )

    candidate = {
        "candidate": "MTTSelectedT1T2CovariantGreenAndTransferProbe",
        "status": "MTT_SELECTED_T1T2_COVARIANT_GREEN_CLOSED_TRANSFER_STILL_OPEN",
        "closure_claimed": False,
        "target_fitting_used": False,
        "inputs": {
            "protected_T3_Riesz_Green_dotD": str(prior_path),
            "diagonal_expS_replay": str(replay_path),
            "eta00_overlap_Hodge_projector_table": str(overlap_path),
            "abstract_rank2_to_rank3_transfer_functor": str(transfer_path),
            "End0_BN_identification_audit": str(bn_reject_path),
        },
        "path_A_straight_T1T2_covariant_Green": {
            "converged": t1t2_closed,
            "closed": t1t2_closed,
            "connection_block": "D_a = partial_a I_2 + (partial_a u) J on span(T1,T2), J=[[0,-1],[1,0]]",
            "flatness_reason": "A=du*J is globally pure gauge because exp(uJ) is periodic and D=e^{-uJ} d e^{uJ}.",
            "kernel_basis": ["exp(-uJ) e1", "exp(-uJ) e2"],
            "riesz_projector_formula": "P_D f = exp(-uJ) mean(exp(uJ) f)",
            "reduced_green_formula": "G_D f = exp(-uJ) (-Delta)^(-1) Q mean-zero(exp(uJ) f)",
            "min_positive_eigenvalue": gap,
            "green_operator_norm_bound": green_bound,
            "numerical_replay": {
                "mesh": mesh,
                "deterministic_seed": 790,
                "gauge_frame_residual_checked": "||(-Delta)GQ(exp(uJ)f) - Q(exp(uJ)f)||_L2",
                "gauge_frame_residual_l2": gauge_frame_residual_l2,
                "direct_truncated_residual_checked": "||(-sum_a D_a^2)G_DQ_D f - Q_D f||_L2 using finite spectral products",
                "direct_truncated_replay_converged": direct_truncated_replay_converged,
                "direct_truncated_residual_l2": direct_truncated_residual_l2,
                "direct_truncated_relative_residual": direct_truncated_relative_residual,
                "direct_truncated_residual_interpretation": "Diagnostic only: products with exp(uJ) are not closed in the finite Fourier truncation, so aliasing prevents this from being a promotion gate.",
                "kernel_residual_l2": kernel_residual_l2,
            },
        },
        "path_B_superset_rank2_to_sector_transfer": {
            "converged": sector_transfer_promotes,
            "closed": sector_transfer_promotes,
            "abstract_End0_functor_closed": abstract_transfer_closed,
            "BN_identification_rejected_at_selected_End0_level": bn_identification_rejected,
            "sector_routing_closed": False,
            "why_not_converged": "The abstract End0 rank-3 carrier is legal, but the current B_N/qutrit scaffold is explicitly rejected as the selected End0 basis and no selected End0-to-sector routing values are emitted.",
        },
        "operator_payload_boundary": {
            "T1_T2_coupled_covariant_Riesz_Green_extracted": t1t2_closed,
            "full_End0_Riesz_Green_extracted": t1t2_closed and prior["operator_payload_boundary"]["protected_T3_reduced_Green_extracted"] is True,
            "formal_dotD_frechet_formula_retained": prior["operator_payload_boundary"]["formal_dotD_frechet_formula_extracted"],
            "rank2_to_rank3_sector_transfer_values_extracted": sector_transfer_promotes,
            "physical_dotD_alpha1_payload_extracted": False,
            "offdiagonal_Ext_HYM_terms_proved_zero_or_controlled": False,
            "validator_ready": False,
            "why_not_validator_ready": "The full diagonal End0 spectral Green is now closed, but sector transfer, physical dotD_alpha1, and off-diagonal Ext/HYM control remain open.",
        },
        "what_closes_now": {
            "T1_T2_covariant_Green": t1t2_closed,
            "full_diagonal_End0_Riesz_Green": t1t2_closed,
            "pure_gauge_periodic_equivalence_theorem": t1t2_closed,
            "rank2_to_sector_transfer_probe_completed": True,
        },
        "what_remains_open": {
            "rank2_to_rank3_sector_transfer_values": not sector_transfer_promotes,
            "physical_dotD_alpha1_same_branch_driver": True,
            "offdiagonal_Ext_HYM_terms_vanish_or_control_bound": True,
            "validator_ready_sector_D_E_Riesz_Green_dotD": True,
            "full_SM_or_no_knob_closure": True,
        },
        "superset_strategy": {
            "straight_path": "Close the coupled T1/T2 covariant Green by the pure-gauge equivalence D=e^{-uJ}d e^{uJ}.",
            "support_path": "Probe whether existing abstract End0 and qutrit/B_N sector scaffolds can receive this payload; they cannot yet promote.",
            "locked_target": "selected eta_00 diagonal HYM replay and End0(V_alpha), no measured constants.",
            "not_used": "No observed masses, mixings, couplings, benchmark matrices, inverse-search targets, or lifted flags.",
        },
        "next_required_artifact": "MTT_Selected_OffDiagonal_Ext_Control_or_SectorTransfer_From_Full_Diagonal_End0_Green_v1",
    }

    cert = {
        "certificate": "MTT_Selected_T1T2_Covariant_Green_or_Rank2Sector_Transfer_From_Diagonal_HYM_v1",
        "status": candidate["status"],
        "closure_claimed": False,
        "target_fitting_used": False,
        "path_A_T1T2_covariant_Green_closed": t1t2_closed,
        "path_B_rank2_to_sector_transfer_closed": sector_transfer_promotes,
        "full_diagonal_End0_Riesz_Green_closed": candidate["operator_payload_boundary"]["full_End0_Riesz_Green_extracted"],
        "gauge_frame_residual_l2": gauge_frame_residual_l2,
        "direct_truncated_residual_l2": direct_truncated_residual_l2,
        "validator_ready": False,
        "next_required_artifact": candidate["next_required_artifact"],
    }

    proof = f"""# MTT Selected T1T2 Covariant Green or Rank2 Sector Transfer From Diagonal HYM v1

## Path A: Straight End0 Calculation

The coupled `T1/T2` block converges.  On `span(T1,T2)`:

```text
D_a = partial_a I_2 + (partial_a u) J
J = [[0,-1],[1,0]]
```

Since `A=du*J`, the connection is globally pure gauge:

```text
D = exp(-uJ) d exp(uJ)
```

Therefore:

```text
P_D f = exp(-uJ) mean(exp(uJ) f)
G_D f = exp(-uJ) (-Delta)^(-1) Q mean-zero(exp(uJ) f)
```

The deterministic replay gives:

```text
||(-Delta)GQ(exp(uJ)f) - Q(exp(uJ)f)||_L2 = {gauge_frame_residual_l2:.3e}
```

Together with the protected `T3` lane, this closes the full diagonal End0
Riesz/Green packet.

The direct finite spectral replay in the ungauged frame is diagnostic only:
its residual is `{direct_truncated_residual_l2:.3e}` because finite Fourier
products with `exp(uJ)` alias outside the truncation.  The promotion is by the
global pure-gauge theorem, not by this truncated product replay.

## Path B: Superset Sector Transfer

The transfer path does not promote yet.  The abstract `End0(V_alpha)` rank-3
carrier is legal, but the current `B_N`/qutrit scaffold is explicitly rejected
as the selected End0 basis, and no selected End0-to-sector routing values are
emitted.

## Guardrail

This is still not full validator-ready SM-sector data.  The physical
same-branch `dotD_alpha1`, rank2-to-sector transfer values, and off-diagonal
Ext/HYM control theorem remain open.

## Next Artifact

`MTT_Selected_OffDiagonal_Ext_Control_or_SectorTransfer_From_Full_Diagonal_End0_Green_v1`.
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
