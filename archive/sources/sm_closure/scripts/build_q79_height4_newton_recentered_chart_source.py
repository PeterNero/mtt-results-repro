from __future__ import annotations

import argparse
import hashlib
import json
import math
from pathlib import Path

import numpy as np
from flint import acb, acb_mat, arb, ctx

import build_q79_height4_covariant_hessian_integrand_source as hessian_source
import build_q79_height4_pgl3_polydisk_chart_source as chart_runtime
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
A387 = VALIDATED / "n3.rank3.krawczyk.seed.a387.json"
OUTPUT = VALIDATED / "n3.newton.chart.a388.json"
NOTE = ROOT / "proof_corpus" / "MTT_q79HeightFourNewtonRecenteredChartSource_A388_v1.md"
ARTIFACT = "A388"


def load(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def dump(path: Path, value: dict) -> None:
    path.write_text(json.dumps(value, indent=2, sort_keys=True) + "\n", encoding="utf-8")


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def relative(path: Path) -> str:
    return str(path.relative_to(ROOT)).replace("\\", "/")


def authority(path: Path) -> dict[str, str]:
    return {"path": relative(path), "sha256": sha256(path)}


def complex_value(value: dict[str, str]) -> complex:
    return complex(float(value["real"]), float(value["imaginary"]))


def candidate_system(chart: str, coordinates: list[complex], dps: int):
    system = hessian_source.exact_n3_system(chart, dps=dps)
    z_matrix = acb_mat(3, 3)
    for coordinate, generator in zip(coordinates, system.generators):
        z_matrix += acb(
            format(coordinate.real, ".17g"),
            format(coordinate.imag, ".17g"),
        ) * generator
    candidate_alignment = system.alignment * z_matrix.exp()
    system.alignment = candidate_alignment
    system.alignment_0 = candidate_alignment
    if chart_runtime.lower(abs(candidate_alignment.det())) <= 0.0:
        raise ArithmeticError(f"{chart}-chart Newton candidate alignment is singular")
    return system, z_matrix, candidate_alignment


def point_source(system, chart: str) -> dict:
    parameter = acb(0)
    elliptic, line, f_coefficients, f_w, connection_w = hessian_source.local_geometry(
        system, parameter
    )
    base_rows = hessian_source.residue_rows(system, elliptic, line)
    directions = [
        hessian_source.direction_packet(
            system,
            elliptic,
            line,
            f_coefficients,
            base_rows,
            direction,
        )
        for direction in range(8)
    ]
    return {
        "line_chart": chart,
        "sample_parameter": "0",
        "candidate_alignment": validated.encoded_matrix(system.alignment),
        "elliptic_coordinates_a_b_1": hessian_source.encode_vector(elliptic),
        "projective_line_coordinates": hessian_source.encode_vector(line),
        "sextic_coefficients_ascending": hessian_source.encode_vector(f_coefficients),
        "sextic_w_derivative_ascending": hessian_source.encode_vector(f_w),
        "path_Gauss_Manin_connection_C_w": hessian_source.encode_rows(connection_w),
        "residue_rows_R_r": hessian_source.encode_rows(base_rows),
        "deformation_directions": directions,
        "direction_count": len(directions),
        "covariant_row_count": sum(
            len(row["covariant_hessian_integrand_rows"]) for row in directions
        ),
        "minimum_chart_scale_lower": system.diagnostics.minimum_chart_scale_lower,
        "maximum_verified_reduction_Neumann_norm": (
            system.diagnostics.maximum_verified_solve_neumann_norm
        ),
        "maximum_verified_reduction_error_radius": (
            system.diagnostics.maximum_verified_solve_error_radius
        ),
        "maximum_covariant_row_component_radius_upper": max(
            row["maximum_covariant_row_component_radius_upper"] for row in directions
        ),
        "minimum_deformation_Q2_discriminant_absolute_lower": min(
            row["Q2_discriminant_absolute_lower"] for row in directions
        ),
        "minimum_deformation_G3_quotient_norm_absolute_lower": min(
            row["G3_quotient_norm_absolute_lower"] for row in directions
        ),
        "maximum_beta_affine_forcing_radius_upper": max(
            row["maximum_beta_affine_forcing_radius_upper"] for row in directions
        ),
    }


def chart_box(system, z0: acb_mat, chart: str, coordinate_radius: float) -> dict:
    radius = arb(format(coordinate_radius, ".17g"))
    coordinate_box = acb(arb(0, radius), arb(0, radius))
    w_matrix = acb_mat(3, 3)
    for generator in system.generators:
        w_matrix += coordinate_box * generator
    exponential = w_matrix.exp()
    inverse_exponential = (-w_matrix).exp()
    alignment = system.alignment * exponential
    identity = acb_mat(3, 3)
    for index in range(3):
        identity[index, index] = acb(1)
    inverse_defect = exponential * inverse_exponential - identity

    derivatives = []
    maximum_derivative_radius = 0.0
    maximum_frame_derivative_radius = 0.0
    for direction, generator in enumerate(system.generators):
        derivative_exponential = chart_runtime.frechet_exponential(w_matrix, generator)
        alignment_derivative = system.alignment * derivative_exponential
        derivative_radius = chart_runtime.maximum_matrix_radius(alignment_derivative)
        frame_radius = max(
            chart_runtime.maximum_matrix_radius(alignment_derivative * frame_generator)
            for frame_generator in system.generators
        )
        maximum_derivative_radius = max(maximum_derivative_radius, derivative_radius)
        maximum_frame_derivative_radius = max(maximum_frame_derivative_radius, frame_radius)
        derivatives.append(
            {
                "direction_zero_based": direction,
                "alignment_coordinate_derivative": chart_runtime.encode_matrix(
                    alignment_derivative
                ),
                "maximum_alignment_derivative_component_radius_upper": derivative_radius,
                "maximum_moving_right_frame_derivative_component_radius_upper": frame_radius,
            }
        )
    determinant_lower = chart_runtime.lower(abs(alignment.det()))
    if determinant_lower <= 0.0:
        raise ArithmeticError(f"{chart}-chart recentered alignment box is singular")
    replay = chart_runtime.center_replay(system)
    if max(
        replay["maximum_alignment_center_replay_absolute_upper"],
        replay["maximum_coordinate_derivative_center_replay_absolute_upper"],
        replay["maximum_moving_right_frame_center_replay_absolute_upper"],
    ) > 1.0e-70:
        raise AssertionError(f"{chart}-chart Newton-center Frechet replay failed")
    return {
        "line_chart": chart,
        "chart_definition": "A_*(w)=A_* exp(W), W=sum_s w_s G_s",
        "original_Newton_coordinate_matrix_Z0": validated.encoded_matrix(z0),
        "affine_center_alignment": validated.encoded_matrix(system.alignment),
        "coordinate_complex_box": {
            "real_radius_requested": coordinate_radius,
            "imaginary_radius_requested": coordinate_radius,
            "complex_modulus_radius_upper": math.sqrt(2.0) * coordinate_radius,
            "coordinate_count": 8,
        },
        "W_box": chart_runtime.encode_matrix(w_matrix),
        "alignment_box": chart_runtime.encode_matrix(alignment),
        "alignment_determinant_absolute_lower": determinant_lower,
        "exponential_inverse_defect_absolute_upper": (
            chart_runtime.maximum_matrix_absolute_upper(inverse_defect)
        ),
        "maximum_alignment_component_radius_upper": chart_runtime.maximum_matrix_radius(
            alignment
        ),
        "maximum_alignment_derivative_component_radius_upper": maximum_derivative_radius,
        "maximum_moving_right_frame_derivative_component_radius_upper": (
            maximum_frame_derivative_radius
        ),
        "coordinate_derivatives": derivatives,
        "center_point_replay": replay,
    }


def midpoint_matrix(matrix: acb_mat) -> np.ndarray:
    return np.asarray(
        [
            [validated.midpoint(matrix[row, column]) for column in range(matrix.ncols())]
            for row in range(matrix.nrows())
        ],
        dtype=np.complex128,
    )


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--dps", type=int, default=100)
    parser.add_argument("--coordinate-radius", type=float, default=1.0e-7)
    arguments = parser.parse_args()
    if arguments.dps < 60:
        raise ValueError("Newton-recentered chart requires at least 60 digits")
    if not 0.0 < arguments.coordinate_radius < 0.01:
        raise ValueError("require 0 < coordinate radius < 0.01")
    ctx.dps = arguments.dps
    a378 = load(A378)
    a387 = load(A387)
    if a378.get("artifact") != "A378" or a387.get("artifact") != "A387":
        raise AssertionError("A388 requires A378 and A387")
    coordinates = [
        complex_value(value) for value in a387["floating_residual_newton_seed"]
    ]
    charts = []
    point_sources = []
    candidate_centers = []
    for chart in ("y", "z"):
        system, z0, candidate_alignment = candidate_system(
            chart, coordinates, arguments.dps
        )
        candidate_centers.append(midpoint_matrix(candidate_alignment))
        point_sources.append(point_source(system, chart))
        charts.append(chart_box(system, z0, chart, arguments.coordinate_radius))
    center_difference = float(np.max(abs(candidate_centers[0] - candidate_centers[1])))
    if center_difference > 1.0e-14:
        raise AssertionError("Newton candidate differs between y and z charts")

    payload = {
        "schema": "MTTQ79HeightFourNewtonRecenteredChartSource.v1",
        "status": "NEWTON_RECENTERED_PGL3_CHART_AND_POINT_HESSIAN_SOURCE_CERTIFIED",
        "artifact": ARTIFACT,
        "Newton_coordinate_source": a387["floating_residual_newton_seed"],
        "recentered_chart_rule": (
            "A_*=A_n3 exp(sum_s z*_s G_s); A_*(w)=A_* exp(sum_s w_s G_s)"
        ),
        "charts": charts,
        "point_sources": point_sources,
        "summary": {
            "coordinate_count": 8,
            "certified_chart_count": 2,
            "certified_point_covariant_rows": 2 * 8 * 8,
            "certified_point_beta_forcing_rows": 2 * 8,
            "Newton_coordinate_maximum_absolute": float(max(abs(value) for value in coordinates)),
            "local_real_and_imaginary_coordinate_radius": arguments.coordinate_radius,
            "minimum_alignment_determinant_absolute_lower": min(
                row["alignment_determinant_absolute_lower"] for row in charts
            ),
            "minimum_point_Q2_discriminant_absolute_lower": min(
                row["minimum_deformation_Q2_discriminant_absolute_lower"]
                for row in point_sources
            ),
            "minimum_point_G3_quotient_norm_absolute_lower": min(
                row["minimum_deformation_G3_quotient_norm_absolute_lower"]
                for row in point_sources
            ),
            "maximum_y_z_candidate_alignment_center_difference": center_difference,
            "maximum_center_Frechet_replay_absolute_upper": max(
                max(
                    row["center_point_replay"][key]
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
            "A378_selected_point_source": authority(A378),
            "A387_Newton_seed": authority(A387),
            "point_Hessian_source_runtime": authority(Path(hessian_source.__file__).resolve()),
            "polydisk_chart_runtime": authority(Path(chart_runtime.__file__).resolve()),
            "validated_ACB_runtime": authority(Path(validated.__file__).resolve()),
            "builder_source": authority(Path(__file__).resolve()),
        },
        "strict_scope": {
            "observed_SM_values_used": False,
            "Newton_coordinates_derived_from_A384_and_A386_floating_diagnostic": True,
            "floating_diagnostic_promoted_to_rigorous_residual_bound": False,
            "same_selected_n3_fibration_and_PGL3_generators_used": True,
            "right_exponential_recentered_chart_fixed": True,
            "all_eight_Frechet_coordinate_derivatives_interval_closed": True,
            "all_64_point_covariant_Hessian_source_rows_derived_per_chart": True,
            "all_8_point_beta_forcing_rows_derived_per_chart": True,
            "candidate_alignment_locally_nondegenerate": True,
            "full_target_paths_reexecuted_at_candidate": False,
            "wall_free_full_path_polydisk_closed": False,
            "full_residual_Jacobian_polydisk_transport_closed": False,
            "interval_Newton_existence_and_uniqueness_closed": False,
            "covariant_zero_proved": False,
            "full_SM_closure_proved": False,
        },
        "next_required_artifact": (
            "evaluate the centered-affine Hessian source on this recentered box, "
            "then execute the coupled residual and full path transports"
        ),
    }
    dump(OUTPUT, payload)
    NOTE.write_text(
        "# MTT q79 Height-Four Newton-Recentered Chart Source (A388) v1\n\n"
        "A388 promotes the A387 floating-residual Newton seed into an explicit "
        "local PGL(3) "
        "chart. It retains the same selected n3 fibration and eight generators, "
        "but uses `A_*=A_n3 exp(Z_*)` as the computational center.\n\n"
        f"The maximum Newton coordinate magnitude is `{max(abs(value) for value in coordinates):.12g}` "
        f"and the local real/imaginary half-width is `{arguments.coordinate_radius:.12g}`. "
        f"The minimum alignment determinant bound is "
        f"`{payload['summary']['minimum_alignment_determinant_absolute_lower']:.12g}`. "
        "All 64 covariant point rows and eight beta-forcing rows per line chart "
        "are rederived at the new center.\n\n"
        "This certifies local chart kinematics and the local source at the Newton "
        "candidate. It does not yet reexecute target paths or prove a zero.\n",
        encoding="utf-8",
    )
    print(f"wrote {relative(OUTPUT)}")
    print(f"wrote {relative(NOTE)}")
    print(json.dumps(payload["summary"], indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
