"""Build the selected diagonal End0 D_E payload from the HYM replay."""

from __future__ import annotations

import json
import math
from pathlib import Path

import numpy as np

from build_selected_hym_operator_payload_extraction_from_diagonal_replay import fft_operators, replay_solution


ROOT = Path(__file__).resolve().parents[1]
OUT_CANDIDATE = ROOT / "candidate_data" / "selected_end0_de_payload_from_diagonal_hym.candidate.json"
OUT_CERT = ROOT / "certificates" / "selected_end0_de_payload_from_diagonal_hym_certificate.json"
OUT_PROOF = ROOT / "proof_corpus" / "MTT_Selected_End0_DE_Payload_From_Diagonal_HYM_v1.md"


def load(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def matrix_scale(matrix: list[list[float]], scalar: float) -> list[list[float]]:
    return [[float(scalar * entry) for entry in row] for row in matrix]


def matrix_frobenius(matrix: list[list[float]]) -> float:
    return math.sqrt(sum(float(entry) ** 2 for row in matrix for entry in row))


def sample_matrix_packet(du: np.ndarray, ad_t3: list[list[float]]) -> dict:
    flat_index = int(np.argmax(np.abs(du)))
    idx = tuple(int(i) for i in np.unravel_index(flat_index, du.shape))
    value = float(du[idx])
    return {
        "grid_index": idx,
        "du_value": value,
        "connection_matrix_value": matrix_scale(ad_t3, value),
        "frobenius_norm": matrix_frobenius(matrix_scale(ad_t3, value)),
    }


def main() -> int:
    diagonal_path = ROOT / "candidate_data" / "selected_hym_operator_payload_extraction_from_diagonal_replay.candidate.json"
    replay_path = ROOT / "candidate_data" / "selected_full_exps_hym_newton_replay.candidate.json"
    overlap_path = ROOT / "candidate_data" / "selected_ext_overlap_hym_hodge_projector_table.candidate.json"
    adjoint_path = ROOT / "candidate_data" / "selected_hym_adjoint_galerkin_first_coefficient_solve.candidate.json"

    diagonal = load(diagonal_path)
    replay = load(replay_path)
    overlap = load(overlap_path)
    adjoint = load(adjoint_path)

    mesh = int(replay["solver"]["mesh"])
    unit_rescale = float(overlap["selected_row"]["unit_rescale_factor"])
    u, _rho, _lap = replay_solution(mesh, unit_rescale)
    _solve, _laplacian, deriv = fft_operators(u.shape)

    basis = adjoint["algebraic_adjoint_packet"]["basis"]
    ad_t3 = adjoint["algebraic_adjoint_packet"]["ad_matrices_on_End0_basis"]["T3"]
    ad_t3_frobenius = matrix_frobenius(ad_t3)

    direction_payload = {}
    for axis, label in enumerate(["x1", "y1", "x2", "y2"]):
        du = deriv(u, axis)
        du_l2 = float(np.linalg.norm(du.ravel()) / math.sqrt(du.size))
        direction_payload[label] = {
            "operator_formula": f"D_{label} = partial_{label} I_3 + (partial_{label} u) ad(T3)",
            "du_l2": du_l2,
            "du_min": float(du.min()),
            "du_max": float(du.max()),
            "connection_matrix_frobenius_l2": float(ad_t3_frobenius * du_l2),
            "sample_at_absmax_du": sample_matrix_packet(du, ad_t3),
        }

    zero_matrix = [[0.0, 0.0, 0.0] for _ in range(3)]
    diagonal_de_payload_closed = all(
        [
            diagonal["operator_payload_boundary"]["diagonal_rank2_metric_connection_payload_extracted"] is True,
            diagonal["diagonal_connection_payload"]["closed"] is True,
            basis == ["T1", "T2", "T3"],
            ad_t3 == [[0, -1, 0], [1, 0, 0], [0, 0, 0]],
            all(payload["du_l2"] > 0 for payload in direction_payload.values()),
            abs(float(u.mean())) < 1e-14,
        ]
    )

    candidate = {
        "candidate": "MTTSelectedEnd0DEPayloadFromDiagonalHYM",
        "status": "MTT_SELECTED_END0_DE_DIAGONAL_PAYLOAD_BUILT_RIESZ_DOTD_TRANSFER_OPEN",
        "closure_claimed": False,
        "target_fitting_used": False,
        "inputs": {
            "diagonal_HYM_operator_payload": str(diagonal_path),
            "diagonal_expS_replay": str(replay_path),
            "eta00_overlap_Hodge_projector_table": str(overlap_path),
            "su2_adjoint_packet": str(adjoint_path),
        },
        "selected_End0_basis": {
            "basis": basis,
            "carrier": "End_0(V_alpha) real adjoint carrier induced from the selected rank-2 HYM lane",
            "rank": 3,
            "basis_source": "su2 adjoint packet; B_N/qutrit scaffold is not promoted as the selected End0 basis here",
        },
        "adjoint_connection_packet": {
            "closed": diagonal_de_payload_closed,
            "rank2_connection": "A_diag = d u * T3",
            "induced_End0_connection": "ad(A_diag) = d u * ad(T3)",
            "ad_T3_matrix_on_basis_T1_T2_T3": ad_t3,
            "ad_T3_frobenius_norm": ad_t3_frobenius,
            "central_shared_circle_directions": {
                "x3": {"du": 0.0, "connection_matrix": zero_matrix},
                "y3": {"du": 0.0, "connection_matrix": zero_matrix},
            },
        },
        "D_E_direction_payload": direction_payload,
        "finite_payload_policy": {
            "full_24_power_4_matrix_grid_stored": False,
            "why_not_stored": "The pointwise 3x3 coefficient grid is reproducible from the selected diagonal replay and would be large for git; this artifact emits the exact formula, samples, and norms.",
            "reconstruction_recipe": [
                "replay u from selected_full_exps_hym_newton_replay",
                "compute spectral derivatives partial_a u for a in x1,y1,x2,y2",
                "form D_a = partial_a I_3 + (partial_a u) ad(T3)",
                "set x3,y3 connection coefficients to zero in the eta_00 central-neutral row",
            ],
        },
        "operator_payload_boundary": {
            "diagonal_End0_D_E_formula_extracted": diagonal_de_payload_closed,
            "selected_finite_derivative_basis_for_full_validator_extracted": False,
            "Riesz_Green_payload_extracted": False,
            "dotD_payload_extracted": False,
            "rank2_to_rank3_sector_transfer_values_extracted": False,
            "offdiagonal_End0_terms_proved_zero_or_controlled": False,
            "validator_ready": False,
            "why_not_validator_ready": "This closes the diagonal End0 induced connection formula, but downstream validators still require a finite derivative basis, Riesz/Green/dotD payloads, sector transfer values, and an off-diagonal control theorem.",
        },
        "what_closes_now": {
            "End0_adjoint_basis_used_legally": diagonal_de_payload_closed,
            "diagonal_End0_connection_formula": diagonal_de_payload_closed,
            "directionwise_D_E_connection_matrices": diagonal_de_payload_closed,
            "central_shared_circle_zero_direction_preserved": diagonal_de_payload_closed,
        },
        "what_remains_open": {
            "selected_finite_derivative_basis_for_validator": True,
            "Riesz_Green_payload": True,
            "dotD_payload": True,
            "rank2_to_rank3_sector_transfer_values": True,
            "offdiagonal_End0_vanish_or_control_bound": True,
            "full_SM_or_no_knob_closure": True,
        },
        "superset_strategy": {
            "straight_path": "Use the selected rank-2 diagonal HYM connection and the canonical End0 adjoint functor to emit D_E = d + ad(A_diag).",
            "support_path": "Use qutrit/B_N and sector packets only as downstream validator shapes; no B_N coefficient is promoted here.",
            "locked_target": "selected eta_00, T3 diagonal HYM lane, End0(V_alpha) adjoint basis, no measured constants.",
            "not_used": "No observed masses, mixings, couplings, benchmark matrices, inverse-search targets, or lifted flags.",
        },
        "next_required_artifact": "MTT_Selected_Riesz_Green_dotD_From_Diagonal_End0_DE_v1",
    }

    cert = {
        "certificate": "MTT_Selected_End0_DE_Payload_From_Diagonal_HYM_v1",
        "status": candidate["status"],
        "closure_claimed": False,
        "target_fitting_used": False,
        "diagonal_End0_D_E_payload_closed": diagonal_de_payload_closed,
        "basis": basis,
        "ad_T3_matrix_on_basis_T1_T2_T3": ad_t3,
        "active_direction_count": len(direction_payload),
        "validator_ready": False,
        "next_required_artifact": candidate["next_required_artifact"],
    }

    proof = f"""# MTT Selected End0 DE Payload From Diagonal HYM v1

## Result

The diagonal HYM connection now induces a selected `End_0(V_alpha)` operator
payload:

```text
A_diag = d u * T3
D_E = d + ad(A_diag)
D_a = partial_a I_3 + (partial_a u) ad(T3)
```

on the real adjoint basis:

```text
{basis}
```

with

```text
ad(T3) = {ad_t3}
```

The shared central circle directions remain zero for this `eta_00` replay.

## Guardrail

This is a straight rank-2-to-`End0` extraction, not a qutrit/sector promotion.
It does not yet emit the validator-ready finite derivative basis,
Riesz/Green operator, `dotD`, rank2-to-sector transfer, or off-diagonal control
certificate.

## Next Artifact

`MTT_Selected_Riesz_Green_dotD_From_Diagonal_End0_DE_v1`.
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
