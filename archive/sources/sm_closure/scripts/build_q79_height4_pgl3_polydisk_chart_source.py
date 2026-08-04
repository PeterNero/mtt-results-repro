from __future__ import annotations

import argparse
import hashlib
import json
import math
from pathlib import Path

import numpy as np
from flint import acb, acb_mat, arb, ctx

import build_q79_height4_covariant_hessian_integrand_source as hessian_source
import certify_q79_selected_side_beta_defect_transport as validated


ROOT = Path(__file__).resolve().parents[1]
VALIDATED = (
    ROOT
    / "candidate_data"
    / "selected_q79covariantperiodbranchcutsetandtightbetatransport"
    / "selected_alignment_thimble_periods"
    / "covariant_floating_probe"
    / "validated_transport"
)
A378 = VALIDATED / "n3.hessian_source.json"
OUTPUT = VALIDATED / "n3.pgl3.polydisk_chart_source.json"
NOTE = ROOT / "proof_corpus" / "MTT_q79HeightFourPGL3PolydiskChartSource_A385S_v1.md"
ARTIFACT = "A385S"


def dump(path: Path, value: dict) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(value, indent=2, sort_keys=True) + "\n", encoding="utf-8")


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def relative(path: Path) -> str:
    return str(path.relative_to(ROOT)).replace("\\", "/")


def upper(value: arb) -> float:
    return float(value.upper())


def lower(value: arb) -> float:
    return float(value.lower())


def midpoint(value: acb) -> complex:
    return complex(float(value.real.mid()), float(value.imag.mid()))


def encode_acb(value: acb) -> dict:
    center = midpoint(value)
    return {
        "center": {
            "real": format(center.real, ".17g"),
            "imaginary": format(center.imag, ".17g"),
        },
        "real_radius_upper": upper(value.real.rad()),
        "imaginary_radius_upper": upper(value.imag.rad()),
        "complex_radius_upper": validated.radius_upper(value),
    }


def encode_matrix(matrix: acb_mat) -> list[list[dict]]:
    return [
        [encode_acb(matrix[row, column]) for column in range(matrix.ncols())]
        for row in range(matrix.nrows())
    ]


def maximum_matrix_radius(matrix: acb_mat) -> float:
    return max(
        validated.radius_upper(matrix[row, column])
        for row in range(matrix.nrows())
        for column in range(matrix.ncols())
    )


def maximum_matrix_absolute_upper(matrix: acb_mat) -> float:
    return max(
        upper(abs(matrix[row, column]))
        for row in range(matrix.nrows())
        for column in range(matrix.ncols())
    )


def frechet_exponential(z_matrix: acb_mat, direction: acb_mat) -> acb_mat:
    size = z_matrix.nrows()
    if z_matrix.ncols() != size or direction.nrows() != size or direction.ncols() != size:
        raise ValueError("Frechet block requires equal square matrices")
    block = acb_mat(2 * size, 2 * size)
    for row in range(size):
        for column in range(size):
            block[row, column] = z_matrix[row, column]
            block[row, size + column] = direction[row, column]
            block[size + row, size + column] = z_matrix[row, column]
    exponential = block.exp()
    return acb_mat(
        [
            [exponential[row, size + column] for column in range(size)]
            for row in range(size)
        ]
    )


def center_replay(system: validated.SelectedQ79IntervalSystem) -> dict:
    zero = acb_mat(3, 3)
    exponential = zero.exp()
    alignment = system.alignment * exponential
    directions = []
    maximum_alignment_replay = maximum_matrix_absolute_upper(alignment - system.alignment)
    maximum_direction_replay = 0.0
    maximum_frame_replay = 0.0
    for direction, generator in enumerate(system.generators):
        derivative = system.alignment * frechet_exponential(zero, generator)
        direct = system.alignment * generator
        direction_replay = maximum_matrix_absolute_upper(derivative - direct)
        maximum_direction_replay = max(maximum_direction_replay, direction_replay)
        frame_replay = 0.0
        for frame_generator in system.generators:
            frame_replay = max(
                frame_replay,
                maximum_matrix_absolute_upper(
                    derivative * frame_generator
                    - system.alignment * generator * frame_generator
                ),
            )
        maximum_frame_replay = max(maximum_frame_replay, frame_replay)
        directions.append(
            {
                "direction_zero_based": direction,
                "Dexp_zero_replay_absolute_upper": direction_replay,
                "moving_right_frame_replay_absolute_upper": frame_replay,
            }
        )
    return {
        "maximum_alignment_center_replay_absolute_upper": maximum_alignment_replay,
        "maximum_coordinate_derivative_center_replay_absolute_upper": maximum_direction_replay,
        "maximum_moving_right_frame_center_replay_absolute_upper": maximum_frame_replay,
        "directions": directions,
    }


def chart_box(chart: str, coordinate_radius: float, dps: int) -> dict:
    system = hessian_source.exact_n3_system(chart, dps=dps)
    radius = arb(format(coordinate_radius, ".17g"))
    coordinate_box = acb(arb(0, radius), arb(0, radius))
    z_matrix = acb_mat(3, 3)
    for generator in system.generators:
        z_matrix += coordinate_box * generator
    exponential = z_matrix.exp()
    inverse_exponential = (-z_matrix).exp()
    alignment = system.alignment * exponential
    identity = acb_mat(3, 3)
    for index in range(3):
        identity[index, index] = acb(1)
    inverse_defect = exponential * inverse_exponential - identity

    derivatives = []
    maximum_derivative_radius = 0.0
    maximum_frame_derivative_radius = 0.0
    for direction, generator in enumerate(system.generators):
        derivative_exponential = frechet_exponential(z_matrix, generator)
        alignment_derivative = system.alignment * derivative_exponential
        maximum_derivative_radius = max(
            maximum_derivative_radius,
            maximum_matrix_radius(alignment_derivative),
        )
        frame_derivative_radius = max(
            maximum_matrix_radius(alignment_derivative * frame_generator)
            for frame_generator in system.generators
        )
        maximum_frame_derivative_radius = max(
            maximum_frame_derivative_radius,
            frame_derivative_radius,
        )
        derivatives.append(
            {
                "direction_zero_based": direction,
                "alignment_coordinate_derivative": encode_matrix(alignment_derivative),
                "maximum_alignment_derivative_component_radius_upper": (
                    maximum_matrix_radius(alignment_derivative)
                ),
                "maximum_moving_right_frame_derivative_component_radius_upper": (
                    frame_derivative_radius
                ),
            }
        )
    determinant = alignment.det()
    determinant_lower = lower(abs(determinant))
    if determinant_lower <= 0.0:
        raise ArithmeticError(f"{chart}-chart alignment determinant contains zero")
    replay = center_replay(system)
    if max(
        replay["maximum_alignment_center_replay_absolute_upper"],
        replay["maximum_coordinate_derivative_center_replay_absolute_upper"],
        replay["maximum_moving_right_frame_center_replay_absolute_upper"],
    ) > 1.0e-70:
        raise AssertionError(f"{chart}-chart Frechet source does not replay A378 at zero")
    return {
        "line_chart": chart,
        "coordinate_complex_box": {
            "real_radius_requested": coordinate_radius,
            "imaginary_radius_requested": coordinate_radius,
            "complex_modulus_radius_upper": math.sqrt(2.0) * coordinate_radius,
            "coordinate_count": 8,
        },
        "Z_box": encode_matrix(z_matrix),
        "alignment_box": encode_matrix(alignment),
        "alignment_determinant_absolute_lower": determinant_lower,
        "exponential_inverse_defect_absolute_upper": maximum_matrix_absolute_upper(
            inverse_defect
        ),
        "maximum_alignment_component_radius_upper": maximum_matrix_radius(alignment),
        "maximum_alignment_derivative_component_radius_upper": maximum_derivative_radius,
        "maximum_moving_right_frame_derivative_component_radius_upper": (
            maximum_frame_derivative_radius
        ),
        "coordinate_derivatives": derivatives,
        "center_A378_replay": replay,
    }


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--dps", type=int, default=100)
    parser.add_argument("--coordinate-radius", type=float, default=1.0e-4)
    arguments = parser.parse_args()
    if arguments.dps < 50:
        raise ValueError("polydisk chart source requires at least 50 digits")
    if not 0.0 < arguments.coordinate_radius < 0.01:
        raise ValueError("require 0 < coordinate radius < 0.01")
    ctx.dps = arguments.dps
    charts = [
        chart_box(chart, arguments.coordinate_radius, arguments.dps)
        for chart in ("y", "z")
    ]
    y_center = np.asarray(
        [
            [
                complex(
                    float(entry["center"]["real"]),
                    float(entry["center"]["imaginary"]),
                )
                for entry in row
            ]
            for row in charts[0]["alignment_box"]
        ]
    )
    z_center = np.asarray(
        [
            [
                complex(
                    float(entry["center"]["real"]),
                    float(entry["center"]["imaginary"]),
                )
                for entry in row
            ]
            for row in charts[1]["alignment_box"]
        ]
    )
    chart_center_difference = float(np.max(abs(y_center - z_center)))
    if chart_center_difference > 1.0e-14:
        raise AssertionError("y/z chart alignment centers differ")

    payload = {
        "schema": "MTTQ79HeightFourPGL3PolydiskChartSource.v1",
        "status": "PGL3_COMPLEX_BOX_CHART_AND_ALL_EIGHT_FRECHET_DERIVATIVES_CERTIFIED",
        "artifact": ARTIFACT,
        "chart_definition": "A(z)=A_n3*exp(Z), Z=sum_{s=1}^8 z_s G_s",
        "coordinate_derivative_identity": (
            "partial_s A(z)=A_n3*Dexp_Z[G_s], where Dexp_Z[G_s] is the "
            "upper-right block of exp([[Z,G_s],[0,Z]])"
        ),
        "moving_residue_frame_identity": (
            "partial_s(A(z)G_r)=(partial_s A(z))G_r"
        ),
        "charts": charts,
        "summary": {
            "coordinate_count": 8,
            "certified_chart_count": 2,
            "certified_alignment_derivative_matrices": 16,
            "minimum_alignment_determinant_absolute_lower": min(
                row["alignment_determinant_absolute_lower"] for row in charts
            ),
            "maximum_exponential_inverse_defect_absolute_upper": max(
                row["exponential_inverse_defect_absolute_upper"] for row in charts
            ),
            "maximum_alignment_derivative_component_radius_upper": max(
                row["maximum_alignment_derivative_component_radius_upper"]
                for row in charts
            ),
            "maximum_moving_right_frame_derivative_component_radius_upper": max(
                row[
                    "maximum_moving_right_frame_derivative_component_radius_upper"
                ]
                for row in charts
            ),
            "maximum_y_z_alignment_center_difference": chart_center_difference,
            "maximum_A378_center_replay_absolute_upper": max(
                max(
                    row["center_A378_replay"][key]
                    for key in (
                        "maximum_alignment_center_replay_absolute_upper",
                        "maximum_coordinate_derivative_center_replay_absolute_upper",
                        "maximum_moving_right_frame_center_replay_absolute_upper",
                    )
                )
                for row in charts
            ),
        },
        "authority": {
            name: {"path": relative(path), "sha256": sha256(path)}
            for name, path in {
                "A378_Hessian_integrand_source": A378,
                "A378_builder": Path(hessian_source.__file__).resolve(),
                "validated_ACB_transport_engine": Path(validated.__file__).resolve(),
                "builder_source": Path(__file__).resolve(),
            }.items()
        },
        "strict_scope": {
            "observed_SM_values_used": False,
            "same_selected_n3_alignment_and_PGL3_generators_used": True,
            "multivariate_exponential_chart_fixed": True,
            "all_eight_Frechet_coordinate_derivatives_interval_closed": True,
            "moving_right_residue_frame_derivatives_interval_closed": True,
            "A378_point_source_replayed_at_chart_center": True,
            "full_residual_Jacobian_polydisk_transport_closed": False,
            "wall_free_polydisk_closed": False,
            "interval_Newton_existence_and_uniqueness_closed": False,
            "covariant_zero_proved": False,
            "full_SM_closure_proved": False,
        },
        "next_required_artifact": (
            "feed these alignment and Frechet-derivative boxes through the A379, "
            "A380/A381, and A383 same-source systems on an adaptively selected "
            "wall-free coordinate box"
        ),
    }
    dump(OUTPUT, payload)
    NOTE.write_text(
        "# MTT q79 Height-Four PGL3 Polydisk Chart Source (A385S) v1\n\n"
        "A385S fixes the genuine multivariate chart needed after A384. For "
        "`Z=sum z_s G_s`, the coordinate derivative is evaluated by the exact "
        "block-exponential Frechet identity, so noncommuting PGL3 generators "
        "are retained. At `z=0` all eight derivatives and all moving right-frame "
        "derivatives replay A378.\n\n"
        f"For real and imaginary coordinate radii "
        f"`{arguments.coordinate_radius:.12g}`, the minimum certified alignment "
        f"determinant lower bound is "
        f"`{payload['summary']['minimum_alignment_determinant_absolute_lower']:.12g}`.\n\n"
        "This closes the interval chart kinematics, not the full residual "
        "transport over the box. The latter remains the input to Krawczyk.\n",
        encoding="utf-8",
    )
    print(f"wrote {relative(OUTPUT)}")
    print(f"wrote {relative(NOTE)}")
    print(json.dumps(payload["summary"], indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
