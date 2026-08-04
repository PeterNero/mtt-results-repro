from __future__ import annotations

import argparse
import json
from pathlib import Path

import numpy as np

from explore_q79_a126_integral_period_branch_lll import (
    candidate_record,
    kannan_candidates,
    realification,
)


ROOT = Path(__file__).resolve().parents[1]
DIRECTORY = (
    ROOT
    / "candidate_data"
    / "selected_q79covariantperiodbranchcutsetandtightbetatransport"
)
PERIOD_DIRECTORY = DIRECTORY / "selected_alignment_thimble_periods"
PERIODS = PERIOD_DIRECTORY / "selected_alignment_full_integral_basis_period_table.packet.json"
CONVERGENCE = PERIOD_DIRECTORY / "selected_alignment_full_integral_basis_convergence.packet.json"
INTEGRAL_BASIS = (
    ROOT
    / "candidate_data"
    / "selected_q79alignmentintegralh2presentation"
    / "selected_alignment_exact_integral_H2_basis.packet.json"
)
BETA = DIRECTORY / "tight_selected_side_endpoint_beta.theorem.packet.json"
DEFAULT_OUTPUT = PERIOD_DIRECTORY / "selected_alignment_integral_period_branch_lll_exploration.packet.json"


def load(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def complex_value(value: dict[str, str]) -> complex:
    return complex(float(value["real"]), float(value["imaginary"]))


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--output", type=Path, default=DEFAULT_OUTPUT)
    parser.add_argument(
        "--scales", type=int, nargs="+", default=[1000, 10000, 100000]
    )
    parser.add_argument(
        "--coefficient-weights", type=int, nargs="+", default=[1, 3, 10]
    )
    parser.add_argument(
        "--marker-multipliers", type=int, nargs="+", default=[1, 3, 10]
    )
    parser.add_argument("--candidate-limit", type=int, default=64)
    arguments = parser.parse_args()
    if arguments.candidate_limit < 1:
        raise ValueError("candidate limit must be positive")

    period_packet = load(PERIODS)
    convergence_packet = load(CONVERGENCE)
    basis_packet = load(INTEGRAL_BASIS)
    beta_packet = load(BETA)
    period_matrix = np.asarray(
        [
            [complex_value(value) for value in row]
            for row in period_packet["period_matrix_rows"]
        ],
        dtype=np.complex128,
    )
    beta = np.asarray(
        [
            complex_value(value)
            for value in beta_packet["tight_endpoint"]["beta_center"]
        ],
        dtype=np.complex128,
    )
    beta_radius = float(
        beta_packet["tight_endpoint"]["uniform_component_radius_upper"]
    )
    if period_matrix.shape != (8, 92) or beta.shape != (8,):
        raise AssertionError("unexpected selected period/beta dimensions")
    real_matrix = np.vstack([period_matrix.real, period_matrix.imag])
    real_beta = realification(beta)
    active_indices = np.flatnonzero(
        np.max(np.abs(real_matrix), axis=0) > 1.0e-14
    )
    zero_indices = np.flatnonzero(
        np.max(np.abs(real_matrix), axis=0) <= 1.0e-14
    )
    if active_indices.size != 90 or zero_indices.tolist() != [90, 91]:
        raise AssertionError("selected active/zero period columns changed")
    entrywise_primary = np.asarray(
        [
            [float(value) for value in row]
            for row in convergence_packet[
                "primary_entrywise_absolute_difference_envelope_rows"
            ]
        ],
        dtype=np.float64,
    )
    entrywise_error = np.hstack(
        [entrywise_primary, np.zeros((8, 2), dtype=np.float64)]
    )
    primary_basis = np.asarray(
        basis_packet["primary_basis"]["basis_columns"], dtype=object
    )
    if primary_basis.shape != (98, 90):
        raise AssertionError("selected primary integral basis shape changed")

    records: list[dict] = []
    seen: set[tuple[int, ...]] = set()
    active_matrix = real_matrix[:, active_indices]
    for scale in arguments.scales:
        for coefficient_weight in arguments.coefficient_weights:
            for marker_multiplier in arguments.marker_multipliers:
                marker_weight = coefficient_weight * marker_multiplier
                for method, ell_active in kannan_candidates(
                    active_matrix,
                    real_beta,
                    scale=scale,
                    coefficient_weight=coefficient_weight,
                    marker_weight=marker_weight,
                ):
                    key = tuple(int(value) for value in ell_active)
                    if key in seen:
                        continue
                    seen.add(key)
                    records.append(
                        candidate_record(
                            ell_active=ell_active,
                            active_indices=active_indices,
                            period_matrix=period_matrix,
                            beta=beta,
                            entrywise_error=entrywise_error,
                            primary_basis=primary_basis,
                            beta_radius=beta_radius,
                            method=method,
                            scale=scale,
                            coefficient_weight=coefficient_weight,
                            marker_weight=marker_weight,
                        )
                    )
    records.sort(
        key=lambda row: (
            row["residual_l2_norm"],
            row["coefficient_l1_norm"],
        )
    )
    packet = {
        "schema": "MTTQ79SelectedAlignmentIntegralPeriodBranchLLLExploration.v1",
        "status": "SAME_CARRIER_LLL_BRANCH_CANDIDATES_COMPUTED_NO_EXACT_PROMOTION",
        "inputs": {
            "period_table": str(PERIODS.relative_to(ROOT)).replace("\\", "/"),
            "period_two_run_envelope": str(CONVERGENCE.relative_to(ROOT)).replace(
                "\\", "/"
            ),
            "exact_integral_basis": str(INTEGRAL_BASIS.relative_to(ROOT)).replace(
                "\\", "/"
            ),
            "beta_vector": str(BETA.relative_to(ROOT)).replace("\\", "/"),
            "same_selected_carrier": True,
        },
        "real_period_system": {
            "shape": [16, 92],
            "floating_rank": int(np.linalg.matrix_rank(real_matrix)),
            "active_columns": int(active_indices.size),
            "exact_zero_columns_zero_based": [
                int(value) for value in zero_indices
            ],
            "singular_values": [
                float(value)
                for value in np.linalg.svd(real_matrix, compute_uv=False)
            ],
        },
        "search": {
            "method": "FLINT LLL Kannan embeddings",
            "scales": arguments.scales,
            "coefficient_weights": arguments.coefficient_weights,
            "marker_multipliers": arguments.marker_multipliers,
            "distinct_target_coefficient_one_candidates": len(records),
            "stored_candidate_limit": arguments.candidate_limit,
        },
        "candidates_by_residual": records[: arguments.candidate_limit],
        "strict_scope": {
            "observed_SM_values_used": False,
            "same_carrier_equation_executed": True,
            "floating_search_only": True,
            "period_two_run_envelopes_are_not_interval_bounds": True,
            "beta_component_radius_is_rigorous": True,
            "exact_Z92_membership_proved": False,
            "exact_Z92_nonmembership_proved": False,
            "small_residual_accepted_as_proof": False,
            "branch_height_theorem_supplied": False,
        },
    }
    output = arguments.output
    if not output.is_absolute():
        output = ROOT / output
    output.parent.mkdir(parents=True, exist_ok=True)
    output.write_text(
        json.dumps(packet, indent=2, sort_keys=True) + "\n",
        encoding="utf-8",
    )
    print(
        json.dumps(
            {
                "candidate_count": len(records),
                "best": records[0] if records else None,
            },
            indent=2,
        )
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
