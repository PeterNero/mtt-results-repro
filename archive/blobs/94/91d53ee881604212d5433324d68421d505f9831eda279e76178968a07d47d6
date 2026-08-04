from __future__ import annotations

import hashlib
import json
from pathlib import Path

from flint import acb, acb_mat, ctx

import certify_q79_selected_side_beta_defect_transport as validated


ROOT = Path(__file__).resolve().parents[1]
PERIOD_DIRECTORY = (
    ROOT
    / "candidate_data"
    / "selected_q79covariantperiodbranchcutsetandtightbetatransport"
    / "selected_alignment_thimble_periods"
)
PROBE = PERIOD_DIRECTORY / "covariant_floating_probe"
N3 = PROBE / "cplx" / "n3ud"
FIBRATIONS = {"y": N3 / "fy.packet.json", "z": N3 / "fz.packet.json"}
A135 = PERIOD_DIRECTORY / "selected_alignment_height4_E32_thimble_regular_singular_reduction.packet.json"
OUTPUT = PROBE / "validated_transport" / "n3.hessian_source.json"
NOTE = ROOT / "proof_corpus" / "MTT_q79HeightFourCovariantHessianIntegrandSource_A378_v1.md"
ARTIFACT = "A378"
SAMPLE_PARAMETER = "0"


def load(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def dump(path: Path, value: dict) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(value, indent=2, sort_keys=True) + "\n", encoding="utf-8")


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def relative(path: Path) -> str:
    return str(path.relative_to(ROOT)).replace("\\", "/")


def encode_vector(values: list[acb]) -> list[dict[str, str]]:
    return [validated.encoded_acb(value) for value in values]


def encode_rows(values: list[list[acb]]) -> list[list[dict[str, str]]]:
    return [encode_vector(row) for row in values]


def matrix_vector(matrix: acb_mat, vector: list[acb]) -> list[acb]:
    return [
        sum(
            (matrix[row, column] * vector[column] for column in range(matrix.ncols())),
            acb(0),
        )
        for row in range(matrix.nrows())
    ]


def row_matrix(row: list[acb], matrix: list[list[acb]]) -> list[acb]:
    return [
        sum((row[index] * matrix[index][column] for index in range(len(row))), acb(0))
        for column in range(len(matrix[0]))
    ]


def vector_add(left: list[acb], right: list[acb]) -> list[acb]:
    return [a + b for a, b in zip(left, right)]


def quotient_multiply(
    left: tuple[acb, acb],
    right: tuple[acb, acb],
    relation_constant: acb,
    relation_linear: acb,
) -> tuple[acb, acb]:
    quadratic = left[1] * right[1]
    return (
        left[0] * right[0] + quadratic * relation_constant,
        left[0] * right[1]
        + left[1] * right[0]
        + quadratic * relation_linear,
    )


def quotient_power(
    power: int, relation_constant: acb, relation_linear: acb
) -> tuple[acb, acb]:
    result = (acb(1), acb(0))
    factor = (acb(0), acb(1))
    exponent = power
    while exponent:
        if exponent & 1:
            result = quotient_multiply(
                result, factor, relation_constant, relation_linear
            )
        exponent >>= 1
        if exponent:
            factor = quotient_multiply(
                factor, factor, relation_constant, relation_linear
            )
    return result


def quotient_reduce(
    coefficients: list[acb], relation_constant: acb, relation_linear: acb
) -> tuple[acb, acb]:
    result = (acb(0), acb(0))
    for power, coefficient in enumerate(coefficients):
        basis = quotient_power(power, relation_constant, relation_linear)
        result = (
            result[0] + coefficient * basis[0],
            result[1] + coefficient * basis[1],
        )
    return result


def exact_n3_system(chart: str, dps: int) -> validated.SelectedQ79IntervalSystem:
    packet = load(FIBRATIONS[chart])
    if packet["source"]["line_chart"] != chart:
        raise AssertionError(f"n3 {chart}-chart fibration identity changed")
    if not packet["splitting_identity"]["every_residual_coefficient_contains_zero"]:
        raise AssertionError(f"n3 {chart}-chart splitting identity is not certified")
    system = validated.SelectedQ79IntervalSystem(dps=dps, line_chart=chart)
    system.alignment = validated.decoded_matrix(packet["source"]["alignment_interval"])
    system.alignment_0 = system.alignment
    system.diagnostics = validated.IntervalSystemDiagnostics()
    if validated.lower(abs(system.alignment.det())) <= 0.0:
        raise AssertionError(f"n3 {chart}-chart alignment determinant contains zero")
    return system


def local_geometry(
    system: validated.SelectedQ79IntervalSystem, parameter: acb
) -> tuple[list[acb], list[acb], list[acb], list[acb], list[list[acb]]]:
    a_value, b_value, line, line_w = system.ab_line_data(parameter)
    f_coefficients, f_w = validated.aligned_coefficients_and_derivative(
        system.evaluator.tables["F6"], line, line_w, chart=system.line_chart
    )
    connection_w, _exact_terms = system.reduction_solution(f_coefficients, f_w)
    return [a_value, b_value, acb(1)], line, f_coefficients, f_w, connection_w


def deformation_connection_and_source(
    system: validated.SelectedQ79IntervalSystem,
    line: list[acb],
    line_s: list[acb],
) -> tuple[list[list[acb]], list[acb], dict]:
    f_coefficients, f_s = validated.aligned_coefficients_and_derivative(
        system.evaluator.tables["F6"], line, line_s, chart=system.line_chart
    )
    g_coefficients, _g_s = validated.aligned_coefficients_and_derivative(
        system.evaluator.tables["G3"], line, line_s, chart=system.line_chart
    )
    q_coefficients, q_s = validated.aligned_coefficients_and_derivative(
        system.evaluator.tables["Q2"], line, line_s, chart=system.line_chart
    )
    connection_s, exact_terms = system.reduction_solution(f_coefficients, f_s)

    q0, q1, q2 = q_coefficients
    discriminant = q1**2 - acb(4) * q2 * q0
    discriminant_lower = validated.lower(abs(discriminant))
    if discriminant_lower <= 0.0:
        raise ZeroDivisionError("deformation source Q2 discriminant contains zero")
    root_sum = -q1 / q2
    root_product = q0 / q2
    relation_constant = -root_product
    relation_linear = root_sum
    g_pair = quotient_reduce(
        g_coefficients, relation_constant, relation_linear
    )
    g_norm = (
        g_pair[0] ** 2
        + root_sum * g_pair[0] * g_pair[1]
        + root_product * g_pair[1] ** 2
    )
    g_norm_lower = validated.lower(abs(g_norm))
    if g_norm_lower <= 0.0:
        raise ZeroDivisionError("deformation source G3 quotient norm contains zero")
    g_inverse = (
        (g_pair[0] + root_sum * g_pair[1]) / g_norm,
        -g_pair[1] / g_norm,
    )
    q_s_pair = quotient_reduce(q_s, relation_constant, relation_linear)
    source_s = [acb(0) for _ in range(5)]
    for power in range(5):
        exact_weight = quotient_multiply(
            quotient_reduce(
                exact_terms[power], relation_constant, relation_linear
            ),
            g_inverse,
            relation_constant,
            relation_linear,
        )
        velocity_numerator = quotient_multiply(
            quotient_power(power, relation_constant, relation_linear),
            q_s_pair,
            relation_constant,
            relation_linear,
        )
        velocity_weight = quotient_multiply(
            velocity_numerator,
            g_inverse,
            relation_constant,
            relation_linear,
        )
        source_s[power] = (
            acb(2) * exact_weight[0]
            + root_sum * exact_weight[1]
            - velocity_weight[1] / q2
        )
    return connection_s, source_s, {
        "Q2_discriminant_absolute_lower": discriminant_lower,
        "G3_quotient_norm_absolute_lower": g_norm_lower,
        "maximum_source_component_radius_upper": max(
            validated.radius_upper(value) for value in source_s
        ),
        "sextic_directional_derivative": encode_vector(f_s),
        "Q2_directional_derivative": encode_vector(q_s),
    }


def residue_rows(
    system: validated.SelectedQ79IntervalSystem,
    elliptic: list[acb],
    line: list[acb],
) -> list[list[acb]]:
    rows: list[list[acb]] = []
    for generator in system.generators:
        variation = matrix_vector(system.alignment * generator, elliptic)
        if system.line_chart == "z":
            constant = line[2] * (
                variation[0] * line[2] - variation[2] * line[0]
            )
            linear = line[2] * (
                variation[1] * line[2] - variation[2] * line[1]
            )
        else:
            constant = -line[1] * (
                variation[0] * line[1] - variation[1] * line[0]
            )
            linear = -line[1] * (
                variation[2] * line[1] - variation[1] * line[2]
            )
        rows.append(
            [
                system.period_length * constant,
                system.period_length * linear,
                acb(0),
                acb(0),
                acb(0),
            ]
        )
    return rows


def residue_directional_derivatives(
    system: validated.SelectedQ79IntervalSystem,
    elliptic: list[acb],
    line: list[acb],
    direction: int,
) -> list[list[acb]]:
    generator_s = system.generators[direction]
    line_s = matrix_vector(system.alignment * generator_s, elliptic)
    rows: list[list[acb]] = []
    for generator_r in system.generators:
        variation_r = matrix_vector(system.alignment * generator_r, elliptic)
        variation_rs = matrix_vector(
            system.alignment * generator_s * generator_r, elliptic
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


def direction_packet(
    system: validated.SelectedQ79IntervalSystem,
    elliptic: list[acb],
    line: list[acb],
    f_coefficients: list[acb],
    base_residue_rows: list[list[acb]],
    direction: int,
) -> dict:
    generator = system.generators[direction]
    line_s = matrix_vector(system.alignment * generator, elliptic)
    connection_s, source_s, source_diagnostics = deformation_connection_and_source(
        system, line, line_s
    )
    direct_rows = residue_directional_derivatives(
        system, elliptic, line, direction
    )
    covariant_rows = [
        vector_add(direct_rows[row], row_matrix(base_residue_rows[row], connection_s))
        for row in range(8)
    ]
    beta_affine_forcing = [
        sum(
            (base_residue_rows[row][column] * source_s[column] for column in range(5)),
            acb(0),
        )
        for row in range(8)
    ]
    return {
        "deformation_direction_zero_based": direction,
        "deformation_rule": "A(z_s)=A*exp(z_s*G_s)",
        "alignment_derivative_at_zero": "dA/dz_s=A*G_s",
        "row_frame_derivative_at_zero": "d(A*G_r)/dz_s=A*G_s*G_r",
        **source_diagnostics,
        "deformation_Gauss_Manin_connection_C_s": encode_rows(connection_s),
        "deformation_normal_function_source_eta_s": encode_vector(source_s),
        "direct_residue_row_derivative_R_rs": encode_rows(direct_rows),
        "covariant_hessian_integrand_rows": encode_rows(covariant_rows),
        "covariant_formula": "D_s(R_r P)=(R_rs+R_r*C_s)P",
        "anchored_beta_affine_forcing_R_r_eta_s": encode_vector(
            beta_affine_forcing
        ),
        "anchored_beta_formula": (
            "D_s(R_r Y)=(R_rs+R_r*C_s)Y+R_r*eta_s"
        ),
        "maximum_connection_component_radius_upper": max(
            validated.radius_upper(value) for row in connection_s for value in row
        ),
        "maximum_covariant_row_component_radius_upper": max(
            validated.radius_upper(value) for row in covariant_rows for value in row
        ),
        "maximum_beta_affine_forcing_radius_upper": max(
            validated.radius_upper(value) for value in beta_affine_forcing
        ),
    }


def chart_packet(chart: str) -> dict:
    system = exact_n3_system(chart, dps=100)
    parameter = acb(SAMPLE_PARAMETER)
    elliptic, line, f_coefficients, f_w, connection_w = local_geometry(
        system, parameter
    )
    base_residue_rows = residue_rows(system, elliptic, line)
    directions = [
        direction_packet(
            system,
            elliptic,
            line,
            f_coefficients,
            base_residue_rows,
            direction,
        )
        for direction in range(8)
    ]
    return {
        "line_chart": chart,
        "sample_parameter": SAMPLE_PARAMETER,
        "elliptic_coordinates_a_b_1": encode_vector(elliptic),
        "projective_line_coordinates": encode_vector(line),
        "sextic_coefficients_ascending": encode_vector(f_coefficients),
        "sextic_w_derivative_ascending": encode_vector(f_w),
        "path_Gauss_Manin_connection_C_w": encode_rows(connection_w),
        "residue_rows_R_r": encode_rows(base_residue_rows),
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


def main() -> int:
    ctx.dps = 100
    a135 = load(A135)
    theorem = a135["local_theorem"]
    if not theorem["proved_for_all_selected_thimbles"]:
        raise AssertionError("A135 no longer covers all selected thimbles")
    if "log-free" not in theorem["vanishing_branch"]:
        raise AssertionError("A135 log-free vanishing branch statement changed")
    if "R^2=0" not in theorem["residue_nilpotence"]:
        raise AssertionError("A135 square-zero residue statement changed")

    charts = [chart_packet(chart) for chart in ("y", "z")]
    if any(row["direction_count"] != 8 or row["covariant_row_count"] != 64 for row in charts):
        raise AssertionError("the all-direction covariant row inventory is incomplete")
    payload = {
        "schema": "MTTQ79HeightFourCovariantHessianIntegrandSource.v1",
        "status": "SAME_SOURCE_ALL_64_FULL_COVARIANT_HESSIAN_INTEGRAND_ROWS_DERIVED",
        "artifact": ARTIFACT,
        "map": "F_r(A)=beta_r(A)-Pi_r(A,m)",
        "coordinate_convention": (
            "right exponential PGL3 chart A(z_s)=A exp(z_s G_s), with the "
            "output residue frame recomputed as A(z_s) G_r"
        ),
        "derived_identity": {
            "horizontal_period_variation": "D_s P=C_s P",
            "residue_integrand_variation": "D_s(R_r P)=(R_rs+R_r C_s)P",
            "connection_source": (
                "C_s is the verified Griffiths-Dwork reduction of partial_s F6 "
                "in the selected five-period basis"
            ),
            "row_source": (
                "R_rs is the exact product-rule derivative of the selected "
                "PGL3 residue row R_r"
            ),
            "normal_function_source": (
                "eta_s is the verified Q2/G3 quotient-algebra source obtained "
                "by replacing the path derivative with partial_s"
            ),
            "anchored_beta_variation": (
                "D_s(R_r Y)=(R_rs+R_r C_s)Y+R_r eta_s"
            ),
            "new_scalar_source_rows": 0,
        },
        "chart_executions": charts,
        "A135_endpoint_rule": {
            "regular_singular_system": theorem["regular_singular_system"],
            "residue_nilpotence": theorem["residue_nilpotence"],
            "vanishing_branch": theorem["vanishing_branch"],
            "tail_rule": theorem["E32_tail"],
            "consequence": (
                "differentiate the A135 log-free Frobenius tail coefficientwise; "
                "no singular endpoint value is introduced as an independent row"
            ),
        },
        "summary": {
            "selected_charts_executed": len(charts),
            "deformation_directions_per_chart": 8,
            "covariant_hessian_integrand_rows_per_chart": 64,
            "new_empirical_or_scalar_source_rows": 0,
            "maximum_verified_reduction_Neumann_norm": max(
                row["maximum_verified_reduction_Neumann_norm"] for row in charts
            ),
            "maximum_verified_reduction_error_radius": max(
                row["maximum_verified_reduction_error_radius"] for row in charts
            ),
            "maximum_covariant_row_component_radius_upper": max(
                row["maximum_covariant_row_component_radius_upper"] for row in charts
            ),
            "minimum_deformation_Q2_discriminant_absolute_lower": min(
                row["minimum_deformation_Q2_discriminant_absolute_lower"]
                for row in charts
            ),
            "minimum_deformation_G3_quotient_norm_absolute_lower": min(
                row["minimum_deformation_G3_quotient_norm_absolute_lower"]
                for row in charts
            ),
            "maximum_beta_affine_forcing_radius_upper": max(
                row["maximum_beta_affine_forcing_radius_upper"] for row in charts
            ),
        },
        "authority": {
            name: {"path": relative(path), "sha256": sha256(path)}
            for name, path in {
                "n3_y_fibration": FIBRATIONS["y"],
                "n3_z_fibration": FIBRATIONS["z"],
                "A135_log_free_Frobenius_branch": A135,
                "builder_source": Path(__file__).resolve(),
            }.items()
        },
        "strict_scope": {
            "observed_SM_values_used": False,
            "same_selected_fibration_and_PGL3_generators_used": True,
            "all_64_homogeneous_period_hessian_integrand_rows_derived": True,
            "all_64_anchored_beta_affine_hessian_integrand_rows_derived": True,
            "A135_log_free_tail_differentiation_rule_inherited": True,
            "new_scalar_source_rows_introduced": False,
            "anchored_beta_hessian_integrand_rows_derived": True,
            "full_paths_and_tails_integrated": False,
            "interval_Jacobian_certificate": False,
            "interval_Newton_existence_and_uniqueness_closed": False,
            "covariant_zero_proved": False,
            "full_SM_closure_proved": False,
        },
        "next_required_artifact": (
            "integrate these derived affine 64-row systems along the certified "
            "beta, main, handle, and A135 Frobenius-tail paths, then enclose "
            "their variation on a wall-free parameter box"
        ),
    }
    dump(OUTPUT, payload)
    NOTE.write_text(
        "# MTT q79 Height-Four Covariant Hessian Integrand Source (A378) v1\n\n"
        "A378 derives, in both selected line charts, every one of the 64 local "
        "second-response rows needed to differentiate the eight-component "
        "period and anchored-beta maps in the eight complex PGL(3) directions. "
        "The construction uses the verified Griffiths-Dwork deformation "
        "connection `C_s`, the Q2/G3 normal-function source `eta_s`, and the "
        "exact identities `D_s(R_r P)=(R_rs+R_r C_s)P` and "
        "`D_s(R_r Y)=(R_rs+R_r C_s)Y+R_r eta_s`.\n\n"
        "No benchmark Jacobian entries, observed Standard Model values, or new "
        "scalar source rows enter. A135 supplies the log-free square-zero nodal "
        "branch, so the endpoint tail is differentiated coefficientwise rather "
        "than assigned a singular boundary value.\n\n"
        "This closes the full local Hessian-integrand source problem, including "
        "the anchored-beta inhomogeneous term. It does not yet execute the full "
        "path integrals, enclose the Jacobian on a neighborhood, or prove a "
        "covariant zero.\n",
        encoding="utf-8",
    )
    print(f"wrote {relative(OUTPUT)}")
    print(f"wrote {relative(NOTE)}")
    print(json.dumps(payload["summary"], indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
