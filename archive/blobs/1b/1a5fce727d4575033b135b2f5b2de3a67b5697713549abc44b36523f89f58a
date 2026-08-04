from __future__ import annotations

import hashlib
import json
import math
import sys
import types
from pathlib import Path

import numpy as np
from flint import acb, acb_mat, arb


ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))

import build_q79_height4_covariant_hessian_integrand_source as hessian_source
import certify_q79_selected_side_beta_defect_transport as validated


VALIDATED = (
    ROOT
    / "candidate_data"
    / "selected_q79covariantperiodbranchcutsetandtightbetatransport"
    / "selected_alignment_thimble_periods"
    / "covariant_floating_probe"
    / "validated_transport"
)
PACKET = VALIDATED / "n3.pgl3.polydisk_hessian_source.json"
A378 = VALIDATED / "n3.hessian_source.json"
A385S = VALIDATED / "n3.pgl3.polydisk_chart_source.json"


def load(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def require(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)


def close(left: float, right: float, *, scale: float = 1.0) -> bool:
    return abs(left - right) <= 2.0e-12 * max(scale, abs(left), abs(right))


def decode_box(value: dict) -> acb:
    return acb(
        arb(
            value["center"]["real"],
            format(float(value["real_radius_upper"]), ".17g"),
        ),
        arb(
            value["center"]["imaginary"],
            format(float(value["imaginary_radius_upper"]), ".17g"),
        ),
    )


def decode_box_matrix(values: list[list[dict]]) -> acb_mat:
    return acb_mat([[decode_box(value) for value in row] for row in values])


def decode_rows(values: list[list[dict]]) -> list[list[acb]]:
    return [
        [validated.decoded_acb(value) for value in row]
        for row in values
    ]


def install_weighted_solve(system: validated.SelectedQ79IntervalSystem) -> None:
    system.audit_weighted_solves = []

    def solve(
        self: validated.SelectedQ79IntervalSystem,
        matrix: acb_mat,
        targets: acb_mat,
    ) -> acb_mat:
        center_matrix = acb_mat(
            [
                [self.midpoint_acb(matrix[row, column]) for column in range(matrix.ncols())]
                for row in range(matrix.nrows())
            ]
        )
        center_targets = acb_mat(
            [
                [self.midpoint_acb(targets[row, column]) for column in range(targets.ncols())]
                for row in range(targets.nrows())
            ]
        )
        inverse = center_matrix.inv()
        identity = acb_mat(matrix.nrows(), matrix.ncols())
        for index in range(matrix.nrows()):
            identity[index, index] = acb(1)
        defect = identity - inverse * matrix
        bounds = [
            [abs(defect[row, column]) for column in range(matrix.ncols())]
            for row in range(matrix.nrows())
        ]
        floating = np.asarray(
            [[validated.upper(value) for value in row] for row in bounds],
            dtype=np.float64,
        )
        weights = np.ones(matrix.nrows(), dtype=np.float64)
        for _ in range(512):
            updated = floating @ weights + 1.0e-300
            weights = updated / float(np.max(updated))
        weights = np.maximum(weights, 1.0e-300)
        weight_balls = [arb(format(float(value), ".17g")) for value in weights]
        row_bounds = [
            sum(
                (
                    bounds[row][column] * weight_balls[column]
                    for column in range(matrix.ncols())
                ),
                arb(0),
            )
            / weight_balls[row]
            for row in range(matrix.nrows())
        ]
        contraction = max(row_bounds, key=validated.upper)
        contraction_upper = validated.upper(contraction)
        require(contraction_upper < 1.0, "A385I weighted inverse is not contractive")
        center_ball = inverse * center_targets
        center = acb_mat(
            [
                [self.midpoint_acb(center_ball[row, column]) for column in range(center_ball.ncols())]
                for row in range(center_ball.nrows())
            ]
        )
        preconditioned_residual = inverse * (targets - matrix * center)
        result = acb_mat(center.nrows(), center.ncols())
        maximum_error = 0.0
        for column in range(center.ncols()):
            residual_norm = max(
                (
                    abs(preconditioned_residual[row, column]) / weight_balls[row]
                    for row in range(center.nrows())
                ),
                key=validated.upper,
            )
            error_norm = residual_norm / (arb(1) - contraction)
            for row in range(center.nrows()):
                error_upper = validated.upper(error_norm * weight_balls[row])
                maximum_error = max(maximum_error, error_upper)
                result[row, column] = acb(
                    arb(str(center[row, column].real.mid()), str(error_upper)),
                    arb(str(center[row, column].imag.mid()), str(error_upper)),
                )
        self.diagnostics.maximum_verified_solve_neumann_norm = max(
            self.diagnostics.maximum_verified_solve_neumann_norm,
            contraction_upper,
        )
        self.diagnostics.maximum_verified_solve_error_radius = max(
            self.diagnostics.maximum_verified_solve_error_radius,
            maximum_error,
        )
        self.audit_weighted_solves.append(
            {
                "matrix_size": matrix.nrows(),
                "target_column_count": targets.ncols(),
                "weighted_contraction_upper": contraction_upper,
                "maximum_solution_component_error_upper": maximum_error,
            }
        )
        return result

    system.verified_solve = types.MethodType(solve, system)


def direct_rows(
    system: validated.SelectedQ79IntervalSystem,
    elliptic: list[acb],
    line: list[acb],
    alignment_derivative: acb_mat,
) -> list[list[acb]]:
    line_s = hessian_source.matrix_vector(alignment_derivative, elliptic)
    rows: list[list[acb]] = []
    for generator_r in system.generators:
        variation_r = hessian_source.matrix_vector(
            system.alignment * generator_r, elliptic
        )
        variation_rs = hessian_source.matrix_vector(
            alignment_derivative * generator_r, elliptic
        )
        if system.line_chart == "z":
            bracket_0 = variation_r[0] * line[2] - variation_r[2] * line[0]
            bracket_1 = variation_r[1] * line[2] - variation_r[2] * line[1]
            bracket_0_s = (
                variation_rs[0] * line[2]
                + variation_r[0] * line_s[2]
                - variation_rs[2] * line[0]
                - variation_r[2] * line_s[0]
            )
            bracket_1_s = (
                variation_rs[1] * line[2]
                + variation_r[1] * line_s[2]
                - variation_rs[2] * line[1]
                - variation_r[2] * line_s[1]
            )
            constant_s = line_s[2] * bracket_0 + line[2] * bracket_0_s
            linear_s = line_s[2] * bracket_1 + line[2] * bracket_1_s
        else:
            bracket_0 = variation_r[0] * line[1] - variation_r[1] * line[0]
            bracket_1 = variation_r[2] * line[1] - variation_r[1] * line[2]
            bracket_0_s = (
                variation_rs[0] * line[1]
                + variation_r[0] * line_s[1]
                - variation_rs[1] * line[0]
                - variation_r[1] * line_s[0]
            )
            bracket_1_s = (
                variation_rs[2] * line[1]
                + variation_r[2] * line_s[1]
                - variation_rs[1] * line[2]
                - variation_r[1] * line_s[2]
            )
            constant_s = -(line_s[1] * bracket_0 + line[1] * bracket_0_s)
            linear_s = -(line_s[1] * bracket_1 + line[1] * bracket_1_s)
        rows.append(
            [
                system.period_length * constant_s,
                system.period_length * linear_s,
                acb(0),
                acb(0),
                acb(0),
            ]
        )
    return rows


def audit_authorities(packet: dict) -> None:
    authority = packet.get("authority", {})
    require(bool(authority), "A385I authority is absent")
    for name, row in authority.items():
        path = ROOT / row.get("path", "")
        require(path.is_file(), f"A385I authority is absent: {name}")
        require(row.get("sha256") == sha256(path), f"A385I authority is stale: {name}")


def main() -> int:
    packet = load(PACKET)
    a378 = load(A378)
    a385s = load(A385S)
    require(
        packet.get("schema")
        == "MTTQ79HeightFourPGL3PolydiskHessianIntegrandSource.v1",
        "A385I schema changed",
    )
    require(packet.get("artifact") == "A385I", "A385I artifact changed")
    require(
        packet.get("status")
        == "PGL3_POLYDISK_ALL_LOCAL_RESIDUAL_JACOBIAN_INTEGRAND_ROWS_CERTIFIED",
        "A385I status changed",
    )
    source_by_chart = {row["line_chart"]: row for row in a385s["charts"]}
    point_by_chart = {row["line_chart"]: row for row in a378["chart_executions"]}
    charts = packet["chart_executions"]
    require([row["line_chart"] for row in charts] == ["y", "z"], "A385I chart order changed")

    maximum_covariant_radius = 0.0
    maximum_forcing_radius = 0.0
    minimum_chart_scale = math.inf
    minimum_q2 = math.inf
    minimum_g3 = math.inf
    maximum_weighted_contraction = 0.0
    row_count = 0
    forcing_count = 0
    for chart_packet in charts:
        chart = chart_packet["line_chart"]
        chart_source = source_by_chart[chart]
        point_source = point_by_chart[chart]
        require(
            chart_packet["coordinate_complex_box"]
            == chart_source["coordinate_complex_box"],
            f"A385I {chart} coordinate box changed",
        )
        system = hessian_source.exact_n3_system(chart, dps=100)
        system.alignment = decode_box_matrix(chart_source["alignment_box"])
        install_weighted_solve(system)
        require(
            validated.lower(abs(system.alignment.det())) > 0.0,
            f"A385I {chart} alignment can be singular",
        )
        elliptic, line, _f, _fw, _cw = hessian_source.local_geometry(system, acb(0))
        base_rows = hessian_source.residue_rows(system, elliptic, line)
        stored_base = decode_rows(chart_packet["base_residue_rows_R_r"])
        require(
            all(a.overlaps(b) for left, right in zip(base_rows, stored_base) for a, b in zip(left, right)),
            f"A385I {chart} base residue rows do not replay",
        )
        directions = chart_packet["deformation_directions"]
        require(len(directions) == 8, f"A385I {chart} direction count changed")
        for direction, stored in enumerate(directions):
            require(
                int(stored["deformation_direction_zero_based"]) == direction,
                f"A385I {chart} direction order changed",
            )
            derivative = decode_box_matrix(
                chart_source["coordinate_derivatives"][direction][
                    "alignment_coordinate_derivative"
                ]
            )
            line_s = hessian_source.matrix_vector(derivative, elliptic)
            connection, source, diagnostics = (
                hessian_source.deformation_connection_and_source(system, line, line_s)
            )
            direct = direct_rows(system, elliptic, line, derivative)
            covariant = [
                [
                    direct[row][column]
                    + sum(
                        (
                            base_rows[row][inner] * connection[inner][column]
                            for inner in range(5)
                        ),
                        acb(0),
                    )
                    for column in range(5)
                ]
                for row in range(8)
            ]
            forcing = [
                sum(
                    (base_rows[row][column] * source[column] for column in range(5)),
                    acb(0),
                )
                for row in range(8)
            ]
            stored_direct = decode_rows(stored["direct_residue_row_derivative_R_rs"])
            stored_covariant = decode_rows(stored["covariant_hessian_integrand_rows"])
            stored_forcing = [
                validated.decoded_acb(value)
                for value in stored["anchored_beta_affine_forcing_R_r_eta_s"]
            ]
            require(
                all(a.overlaps(b) for left, right in zip(direct, stored_direct) for a, b in zip(left, right)),
                f"A385I {chart}/{direction} direct rows do not replay",
            )
            require(
                all(a.overlaps(b) for left, right in zip(covariant, stored_covariant) for a, b in zip(left, right)),
                f"A385I {chart}/{direction} covariant rows do not replay",
            )
            require(
                all(a.overlaps(b) for a, b in zip(forcing, stored_forcing)),
                f"A385I {chart}/{direction} beta forcing does not replay",
            )

            point = point_source["deformation_directions"][direction]
            point_covariant = decode_rows(point["covariant_hessian_integrand_rows"])
            point_forcing = [
                validated.decoded_acb(value)
                for value in point["anchored_beta_affine_forcing_R_r_eta_s"]
            ]
            require(
                all(a.overlaps(b) for left, right in zip(stored_covariant, point_covariant) for a, b in zip(left, right)),
                f"A385I {chart}/{direction} misses A378 covariant center",
            )
            require(
                all(a.overlaps(b) for a, b in zip(stored_forcing, point_forcing)),
                f"A385I {chart}/{direction} misses A378 forcing center",
            )
            maximum_covariant_radius = max(
                maximum_covariant_radius,
                max(validated.radius_upper(value) for row in stored_covariant for value in row),
            )
            maximum_forcing_radius = max(
                maximum_forcing_radius,
                max(validated.radius_upper(value) for value in stored_forcing),
            )
            minimum_q2 = min(minimum_q2, diagnostics["Q2_discriminant_absolute_lower"])
            minimum_g3 = min(minimum_g3, diagnostics["G3_quotient_norm_absolute_lower"])
            row_count += len(stored_covariant)
            forcing_count += len(stored_forcing)
        minimum_chart_scale = min(
            minimum_chart_scale, system.diagnostics.minimum_chart_scale_lower
        )
        stored_solves = chart_packet["weighted_verified_reduction_solves"]
        require(
            len(stored_solves) == len(system.audit_weighted_solves) == 9,
            f"A385I {chart} weighted-solve count changed",
        )
        for stored, replay in zip(stored_solves, system.audit_weighted_solves):
            require(
                int(stored["matrix_size"]) == int(replay["matrix_size"])
                and int(stored["target_column_count"])
                == int(replay["target_column_count"]),
                f"A385I {chart} weighted-solve shape changed",
            )
            require(
                close(
                    float(stored["weighted_contraction_upper"]),
                    float(replay["weighted_contraction_upper"]),
                ),
                f"A385I {chart} weighted contraction does not replay",
            )
        chart_contraction = max(
            float(row["weighted_contraction_upper"]) for row in system.audit_weighted_solves
        )
        require(
            close(
                float(chart_packet["maximum_verified_weighted_reduction_contraction_upper"]),
                chart_contraction,
            ),
            f"A385I {chart} contraction summary does not replay",
        )
        maximum_weighted_contraction = max(
            maximum_weighted_contraction, chart_contraction
        )

    summary = packet["summary"]
    require(int(summary["certified_chart_count"]) == 2, "A385I chart summary changed")
    require(int(summary["coordinate_count"]) == 8, "A385I coordinate count changed")
    require(int(summary["certified_covariant_integrand_rows"]) == row_count == 128, "A385I row count changed")
    require(int(summary["certified_anchored_beta_forcing_entries"]) == forcing_count == 128, "A385I forcing count changed")
    require(close(float(summary["maximum_covariant_row_component_radius_upper"]), maximum_covariant_radius), "A385I covariant-radius summary does not replay")
    require(close(float(summary["maximum_beta_affine_forcing_radius_upper"]), maximum_forcing_radius), "A385I forcing-radius summary does not replay")
    require(close(float(summary["minimum_chart_scale_lower"]), minimum_chart_scale), "A385I chart-scale summary does not replay")
    require(close(float(summary["minimum_deformation_Q2_discriminant_absolute_lower"]), minimum_q2), "A385I Q2 summary does not replay")
    require(close(float(summary["minimum_deformation_G3_quotient_norm_absolute_lower"]), minimum_g3), "A385I G3 summary does not replay")
    require(close(float(summary["maximum_verified_weighted_reduction_contraction_upper"]), maximum_weighted_contraction), "A385I weighted-contraction summary does not replay")
    require(summary["every_polydisk_row_contains_A378_center_row"] is True, "A385I center containment changed")
    audit_authorities(packet)

    scope = packet["strict_scope"]
    for key in (
        "full_exponential_polydisk_alignment_used",
        "all_eight_Frechet_coordinate_derivatives_consumed",
        "all_64_local_residual_Jacobian_integrand_rows_per_chart_closed",
        "anchored_beta_affine_forcing_over_polydisk_closed",
        "A378_point_source_contained_in_every_polydisk_row",
        "positive_weighted_reduction_norm_used",
    ):
        require(scope[key] is True, f"A385I strict scope lost {key}")
    require(scope["observed_SM_values_used"] is False, "observed values entered A385I")
    for key in (
        "moving_initial_cycle_polydisk_enclosure_closed",
        "full_path_Hessian_polydisk_transport_closed",
        "wall_free_polydisk_closed",
        "full_residual_Jacobian_polydisk_transport_closed",
        "interval_Newton_existence_and_uniqueness_closed",
        "covariant_zero_proved",
        "full_SM_closure_proved",
    ):
        require(scope[key] is False, f"A385I overclaims {key}")
    print(
        "PASS: independently replayed all 128 A385I covariant rows and 128 "
        "anchored forcing entries on the two-chart PGL3 box"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
