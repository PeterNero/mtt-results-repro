from __future__ import annotations

import argparse
import json
from pathlib import Path

import numpy as np

import build_selected_q79_height4_survivor_queue_and_E32_priority as a208_builder
from explore_q79_a126_integral_period_branch_lll import (
    candidate_record,
    kannan_candidates,
    realification,
)


ROOT = a208_builder.ROOT
PERIOD_DIRECTORY = a208_builder.PERIOD_DIRECTORY
A208 = a208_builder.PACKET
DEFAULT_OUTPUT = PERIOD_DIRECTORY / "selected_alignment_extended_kannan_grid.exploratory.json"
DEFAULT_SCALES = [250_000, 500_000, 750_000, 1_000_000, 1_500_000, 2_000_000, 4_000_000]
DEFAULT_WEIGHTS = [200, 300, 400, 500, 650, 800, 900, 1000, 1200, 1400, 1600, 1900, 2300, 2800, 3400, 4000]
DEFAULT_MARKERS = [1, 2, 3, 5, 8, 13]


def objective(record: dict) -> tuple[float, float, int]:
    return (
        float(record["residual_maximum_absolute_value"]),
        float(record["residual_l2_norm"]),
        int(record["coefficient_l1_norm"]),
    )


def compact(record: dict) -> dict:
    ell = [int(value) for value in record["ell_Z92"]]
    primitive = record["primitive_chain_coordinates"]
    return {
        "candidate_id": a208_builder.vector_id(ell),
        "effective_coordinates_Z90": ell[:90],
        "coefficient_height": int(record["coefficient_height"]),
        "coefficient_l1_norm": int(record["coefficient_l1_norm"]),
        "support_size": int(record["support_size"]),
        "residual_maximum_absolute_value": float(
            record["residual_maximum_absolute_value"]
        ),
        "residual_l2_norm": float(record["residual_l2_norm"]),
        "primitive_thimble_support": int(primitive["thimble_support_size"]),
        "primitive_thimble_l1_norm": int(
            primitive["thimble_coefficient_l1_norm"]
        ),
        "primitive_handle_coordinates": [
            int(value) for value in primitive["handle_coordinates"]
        ],
        "witness": {
            "method": record["method"],
            "embedding_scale": int(record["embedding_scale"]),
            "coefficient_weight": int(record["coefficient_weight"]),
            "marker_weight": int(record["marker_weight"]),
        },
    }


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--output", type=Path, default=DEFAULT_OUTPUT)
    parser.add_argument("--scales", type=int, nargs="+", default=DEFAULT_SCALES)
    parser.add_argument(
        "--coefficient-weights", type=int, nargs="+", default=DEFAULT_WEIGHTS
    )
    parser.add_argument(
        "--marker-multipliers", type=int, nargs="+", default=DEFAULT_MARKERS
    )
    parser.add_argument("--stored-limit", type=int, default=128)
    arguments = parser.parse_args()
    if min(arguments.scales) <= 0 or min(arguments.coefficient_weights) <= 0:
        raise ValueError("Kannan scales and weights must be positive")
    if min(arguments.marker_multipliers) <= 0:
        raise ValueError("Kannan marker multipliers must be positive")

    inputs = a208_builder.search_inputs()
    period_matrix = inputs["period_matrix"]
    beta = inputs["beta"]
    real_matrix = np.vstack(
        [period_matrix[:, :90].real, period_matrix[:, :90].imag]
    )
    real_beta = realification(beta)
    active_indices = np.arange(90, dtype=np.int64)
    seen: set[tuple[int, ...]] = set()
    records: list[dict] = []
    embedding_count = 0
    for scale in arguments.scales:
        for coefficient_weight in arguments.coefficient_weights:
            for marker_multiplier in arguments.marker_multipliers:
                embedding_count += 1
                marker_weight = coefficient_weight * marker_multiplier
                for method, ell_active in kannan_candidates(
                    real_matrix,
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
                            entrywise_error=inputs["entrywise_error"],
                            primary_basis=inputs["primary_basis"],
                            beta_radius=inputs["beta_radius"],
                            method=method,
                            scale=scale,
                            coefficient_weight=coefficient_weight,
                            marker_weight=marker_weight,
                        )
                    )
                if embedding_count % 50 == 0:
                    print(
                        f"extended Kannan embeddings={embedding_count} unique={len(records)}",
                        flush=True,
                    )

    records.sort(key=objective)
    beta_radius = float(inputs["beta_radius"])
    height_four = [
        row for row in records if int(row["coefficient_height"]) == 4
    ]
    height_four_nonseparated = [
        row
        for row in height_four
        if float(row["residual_maximum_absolute_value"]) < beta_radius
    ]
    a208 = a208_builder.load(A208)
    a208_ids = {
        row["candidate_id"] for row in a208["height_four_candidates"]
    }
    discovered = [
        row
        for row in height_four_nonseparated
        if a208_builder.vector_id([int(value) for value in row["ell_Z92"]])
        not in a208_ids
    ]
    best_by_height = {}
    for height in range(0, 9):
        eligible = [
            row for row in records if int(row["coefficient_height"]) <= height
        ]
        best_by_height[str(height)] = (
            None if not eligible else compact(min(eligible, key=objective))
        )

    packet = {
        "schema": "MTTQ79SelectedAlignmentExtendedKannanGridExploration.v1",
        "status": "EXTENDED_KANNAN_GRID_EXECUTED_NO_EXACT_OR_EXHAUSTIVE_PROMOTION",
        "authority": {
            "period_table": a208_builder.relative(a208_builder.PERIODS),
            "period_table_sha256": a208_builder.sha256(a208_builder.PERIODS),
            "beta_packet": a208_builder.relative(a208_builder.BETA),
            "beta_packet_sha256": a208_builder.sha256(a208_builder.BETA),
            "integral_basis": a208_builder.relative(a208_builder.INTEGRAL_BASIS),
            "integral_basis_sha256": a208_builder.sha256(
                a208_builder.INTEGRAL_BASIS
            ),
            "A208_queue": a208_builder.relative(A208),
            "A208_queue_sha256": a208_builder.sha256(A208),
            "source": a208_builder.relative(Path(__file__)),
            "source_sha256": a208_builder.sha256(Path(__file__)),
        },
        "search": {
            "method": "FLINT LLL Kannan embeddings",
            "scales": arguments.scales,
            "coefficient_weights": arguments.coefficient_weights,
            "marker_multipliers": arguments.marker_multipliers,
            "embedding_count": embedding_count,
            "unique_candidate_count": len(records),
            "beta_uniform_component_radius_upper": beta_radius,
        },
        "height_four_screen": {
            "all_height_four_rows_emitted": len(height_four),
            "beta_center_nonseparated_rows": len(height_four_nonseparated),
            "new_nonseparated_rows_relative_to_A208": len(discovered),
            "new_candidate_ids": [
                compact(row)["candidate_id"] for row in discovered
            ],
            "best_rows": [
                compact(row)
                for row in height_four_nonseparated[: arguments.stored_limit]
            ],
        },
        "best_candidate_by_maximum_height": best_by_height,
        "strict_scope": {
            "observed_SM_values_used": False,
            "same_selected_carrier": True,
            "floating_period_centers_only": True,
            "finite_embedding_grid_only": True,
            "exhaustive_bounded_Z90_search_proved": False,
            "interval_membership_or_nonmembership_proved": False,
            "covariant_PGL3_zero_or_no_go_proved": False,
        },
    }
    output = arguments.output
    if not output.is_absolute():
        output = ROOT / output
    output.parent.mkdir(parents=True, exist_ok=True)
    output.write_text(json.dumps(packet, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    print(f"wrote {a208_builder.relative(output)}")
    print(
        json.dumps(
            {
                "embedding_count": embedding_count,
                "unique_candidates": len(records),
                "height_four_nonseparated": len(height_four_nonseparated),
                "new_relative_to_A208": len(discovered),
                "best_height_four": (
                    None if not height_four else compact(height_four[0])
                ),
            },
            indent=2,
        )
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
