from __future__ import annotations

import argparse
import json
from pathlib import Path

import numpy as np
from flint import fmpz_mat


ROOT = Path(__file__).resolve().parents[1]
PERIODS = (
    ROOT
    / "candidate_data"
    / "selected_q79genus2handleandlerayperiodexecution"
    / "full_integral_basis_period_table.packet.json"
)
CONVERGENCE = (
    ROOT
    / "candidate_data"
    / "selected_q79genus2handleandlerayperiodexecution"
    / "full_integral_basis_convergence.packet.json"
)
PRESENTATION = (
    ROOT
    / "candidate_data"
    / "selected_q79genus2handleandlerayperiodexecution"
    / "coupled_integral_H2_chain_presentation.packet.json"
)
BETA_IDENTITY = (
    ROOT
    / "candidate_data"
    / "selected_q79genus2delignebetaperiodandintegralbranchexecution"
    / "selected_beta_period_vector.floating.packet.json"
)
BETA_A126 = (
    ROOT
    / "candidate_data"
    / "selected_q79genus2delignebetaperiodandintegralbranchexecution"
    / "pgl3_selected_side_beta.local_lower.defect_interval.packet.json"
)


def load(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def complex_value(value: dict) -> complex:
    return complex(float(value["real"]), float(value["imaginary"]))


def realification(values: np.ndarray) -> np.ndarray:
    return np.concatenate([values.real, values.imag], axis=0)


def integer_rows(matrix: fmpz_mat) -> list[list[int]]:
    return [
        [int(matrix[row, column]) for column in range(matrix.ncols())]
        for row in range(matrix.nrows())
    ]


def candidate_record(
    *,
    ell_active: np.ndarray,
    active_indices: np.ndarray,
    period_matrix: np.ndarray,
    beta: np.ndarray,
    entrywise_error: np.ndarray,
    primary_basis: np.ndarray,
    beta_radius: float,
    method: str,
    scale: int,
    coefficient_weight: int,
    marker_weight: int,
) -> dict:
    ell = np.zeros(period_matrix.shape[1], dtype=object)
    for local, global_index in enumerate(active_indices):
        ell[int(global_index)] = int(ell_active[local])
    ell_int = np.asarray([int(value) for value in ell], dtype=object)
    period_sum = np.zeros(period_matrix.shape[0], dtype=np.complex128)
    for index, coefficient in enumerate(ell_int):
        if coefficient:
            period_sum += int(coefficient) * period_matrix[:, index]
    residual = beta - period_sum
    coefficient_abs = np.asarray(
        [abs(int(value)) for value in ell_int], dtype=np.float64
    )
    propagated_period_radius = entrywise_error @ coefficient_abs
    component_radius = propagated_period_radius + beta_radius
    residual_abs = np.abs(residual)
    component_lower = np.maximum(0.0, residual_abs - component_radius)
    primary_coefficients = np.asarray(
        [int(value) for value in ell_int[:90]], dtype=object
    )
    primitive_chain = primary_basis @ primary_coefficients
    primitive_chain_int = np.asarray(
        [int(value) for value in primitive_chain], dtype=object
    )
    thimble_chain = primitive_chain_int[:90]
    handle_chain = primitive_chain_int[90:]
    return {
        "method": method,
        "embedding_scale": scale,
        "coefficient_weight": coefficient_weight,
        "marker_weight": marker_weight,
        "ell_Z92": [int(value) for value in ell_int],
        "support_size": int(np.count_nonzero(coefficient_abs)),
        "coefficient_height": int(np.max(coefficient_abs)),
        "coefficient_l1_norm": int(np.sum(coefficient_abs)),
        "primitive_chain_coordinates": {
            "order": "90 oriented thimbles, A:a1,A:b1,A:a2,A:b2,B:a1,B:b1,B:a2,B:b2",
            "thimble_support_size": int(np.count_nonzero(thimble_chain)),
            "thimble_coefficient_height": int(
                max(abs(int(value)) for value in thimble_chain)
            ),
            "thimble_coefficient_l1_norm": int(
                sum(abs(int(value)) for value in thimble_chain)
            ),
            "handle_coordinates": [int(value) for value in handle_chain],
            "handle_coefficient_height": int(
                max(abs(int(value)) for value in handle_chain)
            ),
        },
        "residual_maximum_absolute_value": float(np.max(residual_abs)),
        "residual_l2_norm": float(np.linalg.norm(residual)),
        "period_plus_beta_error_proxy_component_maximum": float(
            np.max(component_radius)
        ),
        "componentwise_separation_lower_maximum": float(
            np.max(component_lower)
        ),
        "floating_residual": [
            {
                "real": format(float(value.real), ".17g"),
                "imaginary": format(float(value.imag), ".17g"),
            }
            for value in residual
        ],
    }


def kannan_candidates(
    matrix: np.ndarray,
    beta: np.ndarray,
    *,
    scale: int,
    coefficient_weight: int,
    marker_weight: int,
) -> list[tuple[str, np.ndarray]]:
    coordinate_count, generator_count = matrix.shape
    rows: list[list[int]] = []
    scaled_matrix = np.rint(scale * matrix).astype(object)
    scaled_beta = np.rint(scale * beta).astype(object)
    for generator in range(generator_count):
        row = [0] * (generator_count + coordinate_count + 1)
        row[generator] = coefficient_weight
        for coordinate in range(coordinate_count):
            row[generator_count + coordinate] = int(
                scaled_matrix[coordinate, generator]
            )
        rows.append(row)
    target_row = [0] * (generator_count + coordinate_count + 1)
    for coordinate in range(coordinate_count):
        target_row[generator_count + coordinate] = -int(
            scaled_beta[coordinate]
        )
    target_row[-1] = marker_weight
    rows.append(target_row)
    reduced, transform = fmpz_mat(rows).lll(transform=True)
    transform_rows = integer_rows(transform)
    found: list[tuple[str, np.ndarray]] = []
    for row_index, row in enumerate(transform_rows):
        target_coefficient = row[-1]
        if abs(target_coefficient) != 1:
            continue
        sign = target_coefficient
        ell = sign * np.asarray(row[:-1], dtype=object)
        found.append((f"kannan_reduced_row_{row_index}", ell))
    return found


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--output", type=Path, required=True)
    parser.add_argument(
        "--scales", type=int, nargs="+", default=[1000, 10000, 100000]
    )
    parser.add_argument(
        "--coefficient-weights", type=int, nargs="+", default=[1, 3, 10]
    )
    parser.add_argument(
        "--marker-multipliers", type=int, nargs="+", default=[1, 3, 10]
    )
    parser.add_argument(
        "--beta-source", choices=["identity", "a126"], default="identity"
    )
    arguments = parser.parse_args()

    period_packet = load(PERIODS)
    convergence_packet = load(CONVERGENCE)
    presentation_packet = load(PRESENTATION)
    beta_path = BETA_IDENTITY if arguments.beta_source == "identity" else BETA_A126
    beta_packet = load(beta_path)
    period_matrix = np.asarray(
        [
            [complex_value(value) for value in row]
            for row in period_packet["period_rows"]
        ],
        dtype=np.complex128,
    )
    if arguments.beta_source == "identity":
        beta = np.asarray(
            [complex_value(value) for value in beta_packet["production_values"]],
            dtype=np.complex128,
        )
        beta_radius = float(beta_packet["maximum_absolute_difference"])
    else:
        beta = np.asarray(
            [
                complex_value(value)
                for value in beta_packet["endpoint"]["beta_center"]
            ],
            dtype=np.complex128,
        )
        beta_radius = float(
            beta_packet["endpoint"]["uniform_component_radius_upper"]
        )
    if period_matrix.shape != (8, 92) or beta.shape != (8,):
        raise AssertionError("unexpected period/beta dimensions")
    real_matrix = np.vstack([period_matrix.real, period_matrix.imag])
    real_beta = realification(beta)
    active_indices = np.flatnonzero(np.max(np.abs(real_matrix), axis=0) > 1.0e-14)
    zero_indices = np.flatnonzero(np.max(np.abs(real_matrix), axis=0) <= 1.0e-14)
    if active_indices.size != 90 or zero_indices.tolist() != [90, 91]:
        raise AssertionError("A119 active/zero column inventory changed")
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
        presentation_packet["saturated_kernel_and_quotient"][
            "primary_integral_basis_columns"
        ],
        dtype=object,
    )
    if primary_basis.shape != (98, 90):
        raise AssertionError("A119 primary integral basis shape changed")

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
        "schema": "MTTQ79A126IntegralPeriodBranchLLLExploration.v1",
        "status": "EXPLORATORY_ONLY_NO_INTEGRAL_BRANCH_PROMOTION",
        "inputs": {
            "period_table": str(PERIODS.relative_to(ROOT)).replace("\\", "/"),
            "period_two_run_envelope": str(CONVERGENCE.relative_to(ROOT)).replace(
                "\\", "/"
            ),
            "exact_integral_presentation": str(PRESENTATION.relative_to(ROOT)).replace(
                "\\", "/"
            ),
            "beta_vector": str(beta_path.relative_to(ROOT)).replace("\\", "/"),
            "beta_source": arguments.beta_source,
            "same_carrier_as_A119_period_table": arguments.beta_source == "identity",
        },
        "real_period_system": {
            "shape": [16, 92],
            "floating_rank": int(np.linalg.matrix_rank(real_matrix)),
            "active_columns": int(active_indices.size),
            "exact_zero_columns_zero_based": [int(value) for value in zero_indices],
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
        },
        "candidates_by_residual": records[:32],
        "strict_scope": {
            "observed_SM_values_used": False,
            "floating_search_only": True,
            "A119_two_run_differences_are_not_interval_bounds": True,
            "beta_error_proxy_is_rigorous": arguments.beta_source == "a126",
            "identity_beta_two_run_difference_is_not_an_interval_bound": (
                arguments.beta_source == "identity"
            ),
            "cross_carrier_A126_comparison_forbidden": arguments.beta_source == "a126",
            "exact_Z92_membership_proved": False,
            "exact_Z92_nonmembership_proved": False,
            "small_residual_accepted_as_proof": False,
            "branch_height_theorem_supplied": False,
        },
    }
    arguments.output.parent.mkdir(parents=True, exist_ok=True)
    arguments.output.write_text(
        json.dumps(packet, indent=2, sort_keys=True) + "\n", encoding="utf-8"
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
