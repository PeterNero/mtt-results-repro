from __future__ import annotations

import math
import sys
from pathlib import Path

from flint import acb, ctx


ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))

import certify_q79_height4_d087_full_residue_main_interval as n3_engine
import certify_q79_selected_side_beta_defect_transport as validated
import run_q79_augmented_beta_transport as augmented
import run_q79_correlated_beta_minus_bhandle_transport as correlated


def require(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)


def main() -> int:
    ctx.dps = 120
    system = n3_engine.exact_target_system(120)
    center, frame = correlated.initial_state()
    step = 1.0e-4
    order = 30
    scale = 0.1

    matrix, forcing, _diagnostics = validated.build_taylor_system(
        system, 0.0 + 0.0j, 1.0 + 0.0j, step, order
    )
    scales = [acb(1) for _ in range(5)] + [acb("0.1") for _ in range(8)]
    inverse_scales = [acb(1) / value for value in scales]
    for row in range(13):
        for column in range(13):
            transformed = matrix[row][column] * scales[row] * inverse_scales[column]
            recovered = transformed * inverse_scales[row] * scales[column]
            require(
                all(
                    left.overlaps(right)
                    for left, right in zip(
                        matrix[row][column].coefficients,
                        recovered.coefficients,
                    )
                ),
                f"weighted matrix conjugation failed at ({row},{column})",
            )
            require(
                matrix[row][column].remainder.overlaps(recovered.remainder),
                f"weighted matrix remainder failed at ({row},{column})",
            )
        transformed_forcing = forcing[row] * scales[row]
        recovered_forcing = transformed_forcing * inverse_scales[row]
        require(
            all(
                left.overlaps(right)
                for left, right in zip(
                    forcing[row].coefficients,
                    recovered_forcing.coefficients,
                )
            ),
            f"weighted forcing conjugation failed at row {row}",
        )
    for row in range(5):
        for column in range(5, 13):
            require(
                validated.upper(matrix[row][column].absolute_bound()) < 1.0e-300,
                "residue output feeds back into the lift block",
            )
    for row in range(5, 13):
        for column in range(5, 13):
            require(
                validated.upper(matrix[row][column].absolute_bound()) < 1.0e-300,
                "residue-output homogeneous block is not zero",
            )

    original_generator = validated.LiftErrorFrame.physical_generator_matrix
    original_radius = validated.LiftErrorFrame.physical_radius
    validated.LiftErrorFrame.physical_generator_matrix = augmented.dynamic_generator_matrix
    validated.LiftErrorFrame.physical_radius = augmented.dynamic_physical_radius
    try:
        ordinary_endpoint, ordinary_frame, ordinary_radius, ordinary_diagnostics = (
            augmented.augmented_validated_flow_step(
                system,
                0.0 + 0.0j,
                1.0 + 0.0j,
                step,
                center,
                frame,
                validated.arb(0),
                order=order,
            )
        )
        weighted_endpoint, weighted_frame, weighted_radius, weighted_diagnostics = (
            correlated.weighted_augmented_flow_step(
                system,
                0.0 + 0.0j,
                1.0 + 0.0j,
                step,
                center,
                frame,
                validated.arb(0),
                order=order,
                residue_scale=scale,
            )
        )
    finally:
        validated.LiftErrorFrame.physical_generator_matrix = original_generator
        validated.LiftErrorFrame.physical_radius = original_radius

    ordinary_components = augmented.component_radii(ordinary_frame)
    weighted_components = augmented.component_radii(weighted_frame)
    differences = [
        validated.upper(abs(left - right))
        for left, right in zip(ordinary_endpoint, weighted_endpoint)
    ]
    for index, difference in enumerate(differences):
        overlap_radius = validated.upper(ordinary_components[index]) + validated.upper(
            weighted_components[index]
        )
        require(difference <= overlap_radius, f"weighted endpoint misses row {index}")
    require(
        math.isfinite(validated.upper(ordinary_radius))
        and math.isfinite(validated.upper(weighted_radius)),
        "weighted equivalence produced a nonfinite radius",
    )
    require(ordinary_diagnostics["full_affine_error_frame_used"], "ordinary 13-state frame absent")
    require(weighted_diagnostics["full_affine_error_frame_used"], "weighted 13-state frame absent")
    require(weighted_diagnostics["diagonal_weighted_norm_used"], "weighted norm flag absent")
    require(
        math.isclose(
            float(weighted_diagnostics["residue_coordinate_scale"]),
            scale,
            rel_tol=0.0,
            abs_tol=1.0e-17,
        ),
        "weighted scale changed",
    )
    print(
        "PASS: exact diagonal conjugation recovers the original 13-state Taylor "
        f"system and the two certified one-step endpoints overlap (max center difference "
        f"{max(differences):.6g})"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
