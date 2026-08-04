from __future__ import annotations

import hashlib
import json
import math
import types
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
A385S = VALIDATED / "n3.pgl3.polydisk_chart_source.json"
OUTPUT = VALIDATED / "n3.pgl3.polydisk_hessian_source.json"
NOTE = (
    ROOT
    / "proof_corpus"
    / "MTT_q79HeightFourPGL3PolydiskHessianIntegrandSource_A385I_v1.md"
)
ARTIFACT = "A385I"


def load(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def dump(path: Path, value: dict) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(value, indent=2, sort_keys=True) + "\n", encoding="utf-8")


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def relative(path: Path) -> str:
    return str(path.relative_to(ROOT)).replace("\\", "/")


def authority(path: Path) -> dict[str, str]:
    return {"path": relative(path), "sha256": sha256(path)}


def authorities_current(packet: dict) -> bool:
    for row in packet.get("authority", {}).values():
        path = ROOT / row.get("path", "")
        if not path.is_file() or row.get("sha256") != sha256(path):
            return False
    return True


def decode_box_value(value: dict) -> acb:
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
    return acb_mat([[decode_box_value(value) for value in row] for row in values])


def encode_vector(values: list[acb]) -> list[dict[str, str]]:
    return [validated.encoded_acb(value) for value in values]


def encode_rows(values: list[list[acb]]) -> list[list[dict[str, str]]]:
    return [encode_vector(row) for row in values]


def vector_add(left: list[acb], right: list[acb]) -> list[acb]:
    return [a + b for a, b in zip(left, right)]


def generalized_residue_directional_derivatives(
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


def overlap_rows(left: list[list[acb]], right: list[list[acb]]) -> list[list[bool]]:
    return [
        [a.overlaps(b) for a, b in zip(left_row, right_row)]
        for left_row, right_row in zip(left, right)
    ]


def maximum_radius_rows(rows: list[list[acb]]) -> float:
    return max(serialized_radius_upper(value) for row in rows for value in row)


def serialized_radius_upper(value: acb) -> float:
    persisted = validated.encoded_acb(value)
    return validated.radius_upper(validated.decoded_acb(persisted))


def install_weighted_verified_solve(
    system: validated.SelectedQ79IntervalSystem,
) -> None:
    system.weighted_solve_diagnostics = []

    def weighted_verified_solve(
        self: validated.SelectedQ79IntervalSystem,
        matrix: acb_mat,
        targets: acb_mat,
    ) -> acb_mat:
        midpoint_matrix = acb_mat(
            [
                [self.midpoint_acb(matrix[row, column]) for column in range(matrix.ncols())]
                for row in range(matrix.nrows())
            ]
        )
        midpoint_targets = acb_mat(
            [
                [self.midpoint_acb(targets[row, column]) for column in range(targets.ncols())]
                for row in range(targets.nrows())
            ]
        )
        inverse = midpoint_matrix.inv()
        identity = acb_mat(matrix.nrows(), matrix.ncols())
        for index in range(matrix.nrows()):
            identity[index, index] = acb(1)
        defect = identity - inverse * matrix
        bounds = [
            [abs(defect[row, column]) for column in range(matrix.ncols())]
            for row in range(matrix.nrows())
        ]
        floating_bounds = np.asarray(
            [
                [validated.upper(value) for value in row]
                for row in bounds
            ],
            dtype=np.float64,
        )
        weights = np.ones(matrix.nrows(), dtype=np.float64)
        for _ in range(512):
            updated = floating_bounds @ weights + 1.0e-300
            weights = updated / float(np.max(updated))
        weights = np.maximum(weights, 1.0e-300)
        weight_balls = [arb(format(float(value), ".17g")) for value in weights]
        weighted_rows = [
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
        contraction = max(weighted_rows, key=validated.upper)
        contraction_upper = validated.upper(contraction)
        if not contraction_upper < 1.0:
            raise ZeroDivisionError(
                "verified weighted midpoint inverse failed: "
                f"contraction upper={contraction_upper:.6e}"
            )

        center_ball = inverse * midpoint_targets
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
                component_error = error_norm * weight_balls[row]
                error_upper = validated.upper(component_error)
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
        self.weighted_solve_diagnostics.append(
            {
                "matrix_size": matrix.nrows(),
                "target_column_count": targets.ncols(),
                "positive_weights": [float(value) for value in weights],
                "weighted_contraction_upper": contraction_upper,
                "maximum_solution_component_error_upper": maximum_error,
            }
        )
        return result

    system.verified_solve = types.MethodType(weighted_verified_solve, system)


def chart_execution(
    chart_source: dict,
    point_source: dict,
    *,
    dps: int,
) -> dict:
    chart = chart_source["line_chart"]
    if point_source["line_chart"] != chart:
        raise AssertionError("A378/A385S chart order changed")
    system = hessian_source.exact_n3_system(chart, dps=dps)
    system.alignment = decode_box_matrix(chart_source["alignment_box"])
    install_weighted_verified_solve(system)
    if validated.lower(abs(system.alignment.det())) <= 0.0:
        raise ArithmeticError(f"{chart}-chart polydisk alignment contains a singular matrix")
    elliptic, line, f_coefficients, _f_w, _connection_w = hessian_source.local_geometry(
        system, acb(0)
    )
    base_rows = hessian_source.residue_rows(system, elliptic, line)
    point_directions = point_source["deformation_directions"]
    directions = []
    for direction, derivative_source in enumerate(
        chart_source["coordinate_derivatives"]
    ):
        if int(derivative_source["direction_zero_based"]) != direction:
            raise AssertionError("A385S coordinate derivative order changed")
        alignment_derivative = decode_box_matrix(
            derivative_source["alignment_coordinate_derivative"]
        )
        line_s = hessian_source.matrix_vector(alignment_derivative, elliptic)
        connection_s, source_s, diagnostics = (
            hessian_source.deformation_connection_and_source(system, line, line_s)
        )
        direct_rows = generalized_residue_directional_derivatives(
            system, elliptic, line, alignment_derivative
        )
        covariant_rows = [
            vector_add(
                direct_rows[row],
                hessian_source.row_matrix(base_rows[row], connection_s),
            )
            for row in range(8)
        ]
        beta_forcing = [
            sum(
                (base_rows[row][column] * source_s[column] for column in range(5)),
                acb(0),
            )
            for row in range(8)
        ]

        point = point_directions[direction]
        point_direct = [
            [validated.decoded_acb(value) for value in row]
            for row in point["direct_residue_row_derivative_R_rs"]
        ]
        point_covariant = [
            [validated.decoded_acb(value) for value in row]
            for row in point["covariant_hessian_integrand_rows"]
        ]
        point_forcing = [
            validated.decoded_acb(value)
            for value in point["anchored_beta_affine_forcing_R_r_eta_s"]
        ]
        direct_overlap = overlap_rows(direct_rows, point_direct)
        covariant_overlap = overlap_rows(covariant_rows, point_covariant)
        forcing_overlap = [
            value.overlaps(reference)
            for value, reference in zip(beta_forcing, point_forcing)
        ]
        if not all(all(row) for row in direct_overlap):
            raise AssertionError(f"{chart} direction {direction} misses A378 direct rows")
        if not all(all(row) for row in covariant_overlap):
            raise AssertionError(f"{chart} direction {direction} misses A378 covariant rows")
        if not all(forcing_overlap):
            raise AssertionError(f"{chart} direction {direction} misses A378 beta forcing")
        directions.append(
            {
                "deformation_direction_zero_based": direction,
                "alignment_coordinate_derivative_box": derivative_source[
                    "alignment_coordinate_derivative"
                ],
                "generalized_frame_identity": (
                    "R_r(z) uses A(z)G_r and partial_s R_r(z) uses "
                    "(partial_s A(z))G_r"
                ),
                "deformation_Gauss_Manin_connection_C_s": encode_rows(connection_s),
                "deformation_normal_function_source_eta_s": encode_vector(source_s),
                "direct_residue_row_derivative_R_rs": encode_rows(direct_rows),
                "covariant_hessian_integrand_rows": encode_rows(covariant_rows),
                "anchored_beta_affine_forcing_R_r_eta_s": encode_vector(beta_forcing),
                "Q2_discriminant_absolute_lower": diagnostics[
                    "Q2_discriminant_absolute_lower"
                ],
                "G3_quotient_norm_absolute_lower": diagnostics[
                    "G3_quotient_norm_absolute_lower"
                ],
                "maximum_connection_component_radius_upper": maximum_radius_rows(
                    connection_s
                ),
                "maximum_source_component_radius_upper": max(
                    serialized_radius_upper(value) for value in source_s
                ),
                "maximum_covariant_row_component_radius_upper": maximum_radius_rows(
                    covariant_rows
                ),
                "maximum_beta_affine_forcing_radius_upper": max(
                    serialized_radius_upper(value) for value in beta_forcing
                ),
                "A378_center_direct_row_overlap": direct_overlap,
                "A378_center_covariant_row_overlap": covariant_overlap,
                "A378_center_beta_forcing_overlap": forcing_overlap,
            }
        )
    return {
        "line_chart": chart,
        "coordinate_complex_box": chart_source["coordinate_complex_box"],
        "alignment_box": chart_source["alignment_box"],
        "alignment_determinant_absolute_lower": chart_source[
            "alignment_determinant_absolute_lower"
        ],
        "minimum_chart_scale_lower": system.diagnostics.minimum_chart_scale_lower,
        "base_residue_rows_R_r": encode_rows(base_rows),
        "deformation_directions": directions,
        "direction_count": len(directions),
        "covariant_row_count": sum(
            len(row["covariant_hessian_integrand_rows"]) for row in directions
        ),
        "minimum_deformation_Q2_discriminant_absolute_lower": min(
            row["Q2_discriminant_absolute_lower"] for row in directions
        ),
        "minimum_deformation_G3_quotient_norm_absolute_lower": min(
            row["G3_quotient_norm_absolute_lower"] for row in directions
        ),
        "maximum_covariant_row_component_radius_upper": max(
            row["maximum_covariant_row_component_radius_upper"] for row in directions
        ),
        "maximum_beta_affine_forcing_radius_upper": max(
            row["maximum_beta_affine_forcing_radius_upper"] for row in directions
        ),
        "weighted_verified_reduction_solves": system.weighted_solve_diagnostics,
        "maximum_verified_weighted_reduction_contraction_upper": max(
            row["weighted_contraction_upper"]
            for row in system.weighted_solve_diagnostics
        ),
    }


def main() -> int:
    ctx.dps = 100
    a378 = load(A378)
    a385s = load(A385S)
    if (
        a378.get("artifact") != "A378"
        or not a378.get("strict_scope", {}).get(
            "all_64_homogeneous_period_hessian_integrand_rows_derived", False
        )
        or not authorities_current(a378)
    ):
        raise AssertionError("A385I requires the current A378 source")
    if (
        a385s.get("artifact") != "A385S"
        or not a385s.get("strict_scope", {}).get(
            "all_eight_Frechet_coordinate_derivatives_interval_closed", False
        )
        or not authorities_current(a385s)
    ):
        raise AssertionError("A385I requires the current A385S chart source")
    point_by_chart = {
        row["line_chart"]: row for row in a378["chart_executions"]
    }
    charts = [
        chart_execution(row, point_by_chart[row["line_chart"]], dps=100)
        for row in a385s["charts"]
    ]
    if [row["line_chart"] for row in charts] != ["y", "z"]:
        raise AssertionError("A385I requires both selected line charts")

    payload = {
        "schema": "MTTQ79HeightFourPGL3PolydiskHessianIntegrandSource.v1",
        "status": "PGL3_POLYDISK_ALL_LOCAL_RESIDUAL_JACOBIAN_INTEGRAND_ROWS_CERTIFIED",
        "artifact": ARTIFACT,
        "chart_definition": a385s["chart_definition"],
        "generalized_coordinate_formula": (
            "line=A(z)e, line_s=(partial_s A(z))e, R_r uses A(z)G_r, "
            "and R_rs uses (partial_s A(z))G_r"
        ),
        "covariant_formula": "D_s(R_r P)=(R_rs+R_r C_s)P",
        "anchored_beta_formula": (
            "D_s(R_r Y)=(R_rs+R_r C_s)Y+R_r eta_s"
        ),
        "chart_executions": charts,
        "summary": {
            "certified_chart_count": len(charts),
            "coordinate_count": 8,
            "certified_covariant_integrand_rows": sum(
                row["covariant_row_count"] for row in charts
            ),
            "certified_covariant_integrand_scalar_entries": sum(
                row["covariant_row_count"] * 5 for row in charts
            ),
            "certified_anchored_beta_forcing_entries": 2 * 8 * 8,
            "minimum_alignment_determinant_absolute_lower": min(
                row["alignment_determinant_absolute_lower"] for row in charts
            ),
            "minimum_chart_scale_lower": min(
                row["minimum_chart_scale_lower"] for row in charts
            ),
            "minimum_deformation_Q2_discriminant_absolute_lower": min(
                row["minimum_deformation_Q2_discriminant_absolute_lower"]
                for row in charts
            ),
            "minimum_deformation_G3_quotient_norm_absolute_lower": min(
                row["minimum_deformation_G3_quotient_norm_absolute_lower"]
                for row in charts
            ),
            "maximum_covariant_row_component_radius_upper": max(
                row["maximum_covariant_row_component_radius_upper"]
                for row in charts
            ),
            "maximum_beta_affine_forcing_radius_upper": max(
                row["maximum_beta_affine_forcing_radius_upper"] for row in charts
            ),
            "maximum_verified_weighted_reduction_contraction_upper": max(
                row["maximum_verified_weighted_reduction_contraction_upper"]
                for row in charts
            ),
            "every_polydisk_row_contains_A378_center_row": True,
        },
        "authority": {
            "A378_point_Hessian_integrand_source": authority(A378),
            "A385S_polydisk_chart_source": authority(A385S),
            "A378_source_builder": authority(Path(hessian_source.__file__).resolve()),
            "validated_ACB_transport_engine": authority(Path(validated.__file__).resolve()),
            "builder_source": authority(Path(__file__).resolve()),
        },
        "strict_scope": {
            "observed_SM_values_used": False,
            "same_selected_n3_alignment_and_PGL3_generators_used": True,
            "full_exponential_polydisk_alignment_used": True,
            "all_eight_Frechet_coordinate_derivatives_consumed": True,
            "all_64_local_residual_Jacobian_integrand_rows_per_chart_closed": True,
            "anchored_beta_affine_forcing_over_polydisk_closed": True,
            "A378_point_source_contained_in_every_polydisk_row": True,
            "positive_weighted_reduction_norm_used": True,
            "moving_initial_cycle_polydisk_enclosure_closed": False,
            "full_path_Hessian_polydisk_transport_closed": False,
            "wall_free_polydisk_closed": False,
            "full_residual_Jacobian_polydisk_transport_closed": False,
            "interval_Newton_existence_and_uniqueness_closed": False,
            "covariant_zero_proved": False,
            "full_SM_closure_proved": False,
        },
        "next_required_artifact": (
            "enclose the moving affine H1 initial cycles and execute these "
            "polydisk rows through the 76 thimbles, handle, beta, and PL paths"
        ),
    }
    dump(OUTPUT, payload)
    NOTE.write_text(
        "# MTT q79 Height-Four PGL3 Polydisk Hessian Integrand Source (A385I) v1\n\n"
        "A385I consumes the full A385S exponential alignment box and all eight "
        "Frechet coordinate derivatives. In each selected line chart it evaluates "
        "the A378 Gauss-Manin reduction, moving right-frame derivative, covariant "
        "Hessian rows, and anchored normal-function forcing over the whole box.\n\n"
        f"The packet certifies `{payload['summary']['certified_covariant_integrand_rows']}` "
        "five-component covariant rows and "
        f"`{payload['summary']['certified_anchored_beta_forcing_entries']}` anchored "
        "forcing entries. Every box contains its independently fixed A378 center "
        "entry. No observed Standard Model value enters.\n\n"
        "This closes the local polydisk source, not the moving initial cycles or "
        "the path integrals. Those are the remaining inputs to a whole-box "
        "residual Jacobian and Krawczyk certificate.\n",
        encoding="utf-8",
    )
    print(f"wrote {relative(OUTPUT)}")
    print(f"wrote {relative(NOTE)}")
    print(json.dumps(payload["summary"], indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
