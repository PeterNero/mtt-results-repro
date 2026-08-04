from __future__ import annotations

import hashlib
import json
import math
from pathlib import Path

from flint import acb, acb_mat, arb, ctx

import build_q79_height4_covariant_hessian_integrand_source as hessian_source
import certify_q79_selected_side_beta_defect_transport as validated
import q79_multivariate_affine_runtime as affine


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
A385I = VALIDATED / "n3.pgl3.polydisk_hessian_source.json"
OUTPUT = VALIDATED / "n3.pgl3.centered_affine_hessian_source.json"
NOTE = ROOT / "proof_corpus" / "MTT_q79HeightFourPGL3CenteredAffineHessianSource_A385A_v1.md"
ARTIFACT = "A385A"
AF = affine.ComplexAffine


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
    rows = packet.get("authority", {})
    return bool(rows) and all(
        (ROOT / row.get("path", "")).is_file()
        and sha256(ROOT / row["path"]) == row.get("sha256")
        for row in rows.values()
    )


def encode_affine(value: AF) -> dict:
    center = affine.midpoint_acb(value.center)
    return {
        "center": validated.encoded_acb(center),
        "unit_disk_coefficients": [
            validated.encoded_acb(coefficient) for coefficient in value.coefficients
        ],
        "center_rounding_radius_upper": affine.upper(value.center.rad()),
        "uniform_nonlinear_remainder_upper": affine.upper(value.remainder),
        "centered_complex_disk_radius_upper": affine.upper(value.centered_radius()),
        "absolute_value_upper": affine.upper(value.absolute_bound()),
    }


def encode_rows(rows: list[list[AF]]) -> list[list[dict]]:
    return [[encode_affine(value) for value in row] for row in rows]


def encode_vector(values: list[AF]) -> list[dict]:
    return [encode_affine(value) for value in values]


def zero(dimension: int) -> AF:
    return AF.constant(0, dimension)


def chart_alignment_center(chart_source: dict, fallback: acb_mat) -> acb_mat:
    encoded = chart_source.get("affine_center_alignment")
    if encoded is None:
        return fallback
    center = validated.decoded_matrix(encoded)
    if center.nrows() != 3 or center.ncols() != 3:
        raise ValueError("PGL3 affine chart center is not 3 by 3")
    return center


def monomial_with_derivative(
    values: list[AF], derivatives: list[AF], powers: list[int]
) -> tuple[AF, AF]:
    dimension = values[0].dimension
    value = AF.constant(1, dimension)
    for coordinate, power in zip(values, powers):
        value *= coordinate**power
    derivative = zero(dimension)
    for selected, power in enumerate(powers):
        if power == 0:
            continue
        term = derivatives[selected] * power
        for index, (coordinate, other_power) in enumerate(zip(values, powers)):
            term *= coordinate ** (other_power - int(index == selected))
        derivative += term
    return value, derivative


def aligned_coefficients_and_derivative(
    table: list[dict],
    line: list[AF],
    line_derivative: list[AF],
    *,
    chart: str,
) -> tuple[list[AF], list[AF]]:
    degree = sum(int(value) for value in table[0]["powers_xyz"])
    dimension = line[0].dimension
    ascending = [zero(dimension) for _ in range(degree + 1)]
    derivative = [zero(dimension) for _ in range(degree + 1)]
    for row in table:
        x_power, y_power, z_power = [int(value) for value in row["powers_xyz"]]
        coefficient = int(row["coefficient"])
        if chart == "y":
            for index in range(y_power + 1):
                powers = [y_power - index, x_power + z_power, index]
                value, value_derivative = monomial_with_derivative(
                    line, line_derivative, powers
                )
                scalar = coefficient * (-1) ** y_power * math.comb(y_power, index)
                ascending[index + z_power] += scalar * value
                derivative[index + z_power] += scalar * value_derivative
        elif chart == "z":
            for index in range(z_power + 1):
                powers = [z_power - index, index, x_power + y_power]
                value, value_derivative = monomial_with_derivative(
                    line, line_derivative, powers
                )
                scalar = coefficient * (-1) ** z_power * math.comb(z_power, index)
                ascending[index + y_power] += scalar * value
                derivative[index + y_power] += scalar * value_derivative
        else:
            raise ValueError(f"unsupported chart {chart!r}")
    return ascending, derivative


def reduction_solution(
    f_coefficients: list[AF],
    f_derivative: list[AF],
) -> tuple[list[list[AF]], list[list[AF]], dict]:
    dimension = f_coefficients[0].dimension
    reduction = [[zero(dimension) for _ in range(11)] for _ in range(11)]
    targets = [[zero(dimension) for _ in range(5)] for _ in range(11)]
    polynomial_derivative = [
        index * f_coefficients[index] for index in range(1, 7)
    ]
    for power in range(6):
        if power:
            for index, coefficient in enumerate(f_coefficients):
                reduction[index + power - 1][power] += power * coefficient
        for index, coefficient in enumerate(polynomial_derivative):
            reduction[index + power][power] -= acb("0.5") * coefficient
    for power in range(5):
        for index, coefficient in enumerate(f_coefficients):
            reduction[index + power][6 + power] += coefficient
        for index, coefficient in enumerate(f_derivative):
            targets[index + power][power] -= acb("0.5") * coefficient
    solved, diagnostics = affine.weighted_verified_solve(reduction, targets)
    exact_terms = [[solved[index][power] for index in range(6)] for power in range(5)]
    connection = [
        [solved[6 + index][power] for index in range(5)] for power in range(5)
    ]
    return connection, exact_terms, diagnostics


def quotient_multiply(
    left: tuple[AF, AF],
    right: tuple[AF, AF],
    relation_constant: AF,
    relation_linear: AF,
) -> tuple[AF, AF]:
    quadratic = left[1] * right[1]
    return (
        left[0] * right[0] + quadratic * relation_constant,
        left[0] * right[1] + left[1] * right[0] + quadratic * relation_linear,
    )


def quotient_power(
    power: int,
    relation_constant: AF,
    relation_linear: AF,
) -> tuple[AF, AF]:
    dimension = relation_constant.dimension
    result = (AF.constant(1, dimension), zero(dimension))
    factor = (zero(dimension), AF.constant(1, dimension))
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
    coefficients: list[AF],
    relation_constant: AF,
    relation_linear: AF,
) -> tuple[AF, AF]:
    dimension = relation_constant.dimension
    result = (zero(dimension), zero(dimension))
    for power, coefficient in enumerate(coefficients):
        basis = quotient_power(power, relation_constant, relation_linear)
        result = (
            result[0] + coefficient * basis[0],
            result[1] + coefficient * basis[1],
        )
    return result


def deformation_connection_and_source(
    system: validated.SelectedQ79IntervalSystem,
    line: list[AF],
    line_s: list[AF],
) -> tuple[list[list[AF]], list[AF], dict]:
    f_coefficients, f_s = aligned_coefficients_and_derivative(
        system.evaluator.tables["F6"], line, line_s, chart=system.line_chart
    )
    g_coefficients, _ = aligned_coefficients_and_derivative(
        system.evaluator.tables["G3"], line, line_s, chart=system.line_chart
    )
    q_coefficients, q_s = aligned_coefficients_and_derivative(
        system.evaluator.tables["Q2"], line, line_s, chart=system.line_chart
    )
    connection, exact_terms, solve_diagnostics = reduction_solution(
        f_coefficients, f_s
    )
    q0, q1, q2 = q_coefficients
    discriminant = q1**2 - acb(4) * q2 * q0
    discriminant_lower = discriminant.absolute_lower()
    if discriminant_lower <= 0.0:
        raise ZeroDivisionError("affine Q2 discriminant contains zero")
    root_sum = -q1 / q2
    root_product = q0 / q2
    relation_constant = -root_product
    relation_linear = root_sum
    g_pair = quotient_reduce(g_coefficients, relation_constant, relation_linear)
    g_norm = (
        g_pair[0] ** 2
        + root_sum * g_pair[0] * g_pair[1]
        + root_product * g_pair[1] ** 2
    )
    g_norm_lower = g_norm.absolute_lower()
    if g_norm_lower <= 0.0:
        raise ZeroDivisionError("affine G3 quotient norm contains zero")
    g_inverse = (
        (g_pair[0] + root_sum * g_pair[1]) / g_norm,
        -g_pair[1] / g_norm,
    )
    q_s_pair = quotient_reduce(q_s, relation_constant, relation_linear)
    dimension = line[0].dimension
    source = [zero(dimension) for _ in range(5)]
    for power in range(5):
        exact_weight = quotient_multiply(
            quotient_reduce(exact_terms[power], relation_constant, relation_linear),
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
        source[power] = (
            acb(2) * exact_weight[0]
            + root_sum * exact_weight[1]
            - velocity_weight[1] / q2
        )
    return connection, source, {
        "Q2_discriminant_absolute_lower": discriminant_lower,
        "G3_quotient_norm_absolute_lower": g_norm_lower,
        "reduction_solve": solve_diagnostics,
    }


def residue_rows(
    system: validated.SelectedQ79IntervalSystem,
    alignment: list[list[AF]],
    elliptic: list[acb],
    line: list[AF],
) -> list[list[AF]]:
    dimension = line[0].dimension
    rows = []
    for generator in system.generators:
        variation = affine.matrix_vector(
            affine.right_multiply_constant(alignment, generator), elliptic
        )
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
                zero(dimension),
                zero(dimension),
                zero(dimension),
            ]
        )
    return rows


def direct_residue_derivative_rows(
    system: validated.SelectedQ79IntervalSystem,
    alignment: list[list[AF]],
    alignment_s: list[list[AF]],
    elliptic: list[acb],
    line: list[AF],
    line_s: list[AF],
) -> list[list[AF]]:
    dimension = line[0].dimension
    rows = []
    for generator in system.generators:
        variation_r = affine.matrix_vector(
            affine.right_multiply_constant(alignment, generator), elliptic
        )
        variation_rs = affine.matrix_vector(
            affine.right_multiply_constant(alignment_s, generator), elliptic
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
                zero(dimension),
                zero(dimension),
                zero(dimension),
            ]
        )
    return rows


def row_matrix(row: list[AF], matrix: list[list[AF]]) -> list[AF]:
    dimension = row[0].dimension
    return [
        sum(
            (row[index] * matrix[index][column] for index in range(len(row))),
            zero(dimension),
        )
        for column in range(len(matrix[0]))
    ]


def disk_ball(value: AF) -> acb:
    center = affine.midpoint_acb(value.center)
    radius = affine.upper(value.centered_radius())
    return acb(
        arb(str(center.real), format(radius, ".17g")),
        arb(str(center.imag), format(radius, ".17g")),
    )


def maximum_radius(rows: list[list[AF]]) -> float:
    return max(affine.upper(value.centered_radius()) for row in rows for value in row)


def chart_execution(
    chart_source: dict,
    point_source: dict,
    raw_source: dict,
) -> dict:
    chart = chart_source["line_chart"]
    if point_source["line_chart"] != chart or raw_source["line_chart"] != chart:
        raise AssertionError("A378/A385S/A385I chart order changed")
    system = hessian_source.exact_n3_system(chart, dps=100)
    # The affine expansion belongs to the chart packet's center. This equals the
    # selected A_n3 center for A385S and also supports a rigorously serialized
    # Newton-recentered chart without silently falling back to A_n3.
    system.alignment = chart_alignment_center(chart_source, system.alignment)
    system.alignment_0 = system.alignment
    requested_radius = float(
        chart_source["coordinate_complex_box"]["real_radius_requested"]
    )
    coordinate_disk_radius = arb(format(requested_radius, ".17g")) * arb(2).sqrt()
    alignment, derivatives, chart_diagnostics = (
        affine.exponential_chart_affine_source(
            system.alignment,
            system.generators,
            coordinate_disk_radius,
        )
    )
    a_value, b_value, _line, _line_w = system.ab_line_data(acb(0))
    elliptic = [a_value, b_value, acb(1)]
    line = affine.matrix_vector(alignment, elliptic)
    base_rows = residue_rows(system, alignment, elliptic, line)
    directions = []
    solve_rows = []
    maximum_covariant_radius = 0.0
    maximum_forcing_radius = 0.0
    all_point_centers_overlap = True
    all_raw_boxes_overlap = True
    for direction, alignment_s in enumerate(derivatives):
        line_s = affine.matrix_vector(alignment_s, elliptic)
        connection, source, diagnostics = deformation_connection_and_source(
            system, line, line_s
        )
        solve_rows.append(diagnostics["reduction_solve"])
        direct = direct_residue_derivative_rows(
            system, alignment, alignment_s, elliptic, line, line_s
        )
        covariant = [
            [left + right for left, right in zip(direct[row], row_matrix(base_rows[row], connection))]
            for row in range(8)
        ]
        forcing = [
            sum(
                (base_rows[row][column] * source[column] for column in range(5)),
                zero(8),
            )
            for row in range(8)
        ]
        point = point_source["deformation_directions"][direction]
        raw = raw_source["deformation_directions"][direction]
        point_covariant = [
            [validated.decoded_acb(value) for value in row]
            for row in point["covariant_hessian_integrand_rows"]
        ]
        point_forcing = [
            validated.decoded_acb(value)
            for value in point["anchored_beta_affine_forcing_R_r_eta_s"]
        ]
        raw_covariant = [
            [validated.decoded_acb(value) for value in row]
            for row in raw["covariant_hessian_integrand_rows"]
        ]
        raw_forcing = [
            validated.decoded_acb(value)
            for value in raw["anchored_beta_affine_forcing_R_r_eta_s"]
        ]
        center_overlap = all(
            covariant[row][column].center.overlaps(point_covariant[row][column])
            for row in range(8)
            for column in range(5)
        ) and all(
            forcing[row].center.overlaps(point_forcing[row]) for row in range(8)
        )
        raw_overlap = all(
            disk_ball(covariant[row][column]).overlaps(raw_covariant[row][column])
            for row in range(8)
            for column in range(5)
        ) and all(
            disk_ball(forcing[row]).overlaps(raw_forcing[row]) for row in range(8)
        )
        all_point_centers_overlap = all_point_centers_overlap and center_overlap
        all_raw_boxes_overlap = all_raw_boxes_overlap and raw_overlap
        covariant_radius = maximum_radius(covariant)
        forcing_radius = max(
            affine.upper(value.centered_radius()) for value in forcing
        )
        maximum_covariant_radius = max(maximum_covariant_radius, covariant_radius)
        maximum_forcing_radius = max(maximum_forcing_radius, forcing_radius)
        directions.append(
            {
                "deformation_direction_zero_based": direction,
                "deformation_Gauss_Manin_connection_C_s": encode_rows(connection),
                "deformation_normal_function_source_eta_s": encode_vector(source),
                "covariant_hessian_integrand_rows": encode_rows(covariant),
                "anchored_beta_affine_forcing_R_r_eta_s": encode_vector(forcing),
                "Q2_discriminant_absolute_lower": diagnostics[
                    "Q2_discriminant_absolute_lower"
                ],
                "G3_quotient_norm_absolute_lower": diagnostics[
                    "G3_quotient_norm_absolute_lower"
                ],
                "maximum_covariant_centered_disk_radius_upper": covariant_radius,
                "maximum_beta_forcing_centered_disk_radius_upper": forcing_radius,
                "A378_point_centers_overlap": center_overlap,
                "A385I_raw_boxes_overlap": raw_overlap,
            }
        )
    if not all_point_centers_overlap:
        raise AssertionError(f"{chart}-chart affine source misses A378 at the center")
    if not all_raw_boxes_overlap:
        raise AssertionError(f"{chart}-chart affine source misses the A385I outer box")
    return {
        "line_chart": chart,
        "coordinate_box": {
            "real_and_imaginary_coordinate_radius": requested_radius,
            "enclosing_independent_complex_disk_radius_upper": affine.upper(
                coordinate_disk_radius
            ),
            "coordinate_count": 8,
        },
        "chart_affine_source_diagnostics": chart_diagnostics,
        "base_residue_rows_R_r": encode_rows(base_rows),
        "deformation_directions": directions,
        "weighted_affine_reduction_solves": solve_rows,
        "minimum_reduction_weighted_contraction_margin": min(
            1.0 - row["weighted_contraction_upper"] for row in solve_rows
        ),
        "maximum_reduction_solution_component_error_upper": max(
            row["maximum_solution_component_error_upper"] for row in solve_rows
        ),
        "maximum_covariant_centered_disk_radius_upper": maximum_covariant_radius,
        "maximum_beta_forcing_centered_disk_radius_upper": maximum_forcing_radius,
        "all_A378_point_centers_overlap": all_point_centers_overlap,
        "all_A385I_raw_boxes_overlap": all_raw_boxes_overlap,
    }


def main() -> int:
    ctx.dps = 100
    a378 = load(A378)
    a385s = load(A385S)
    a385i = load(A385I)
    if a378.get("artifact") != "A378" or not authorities_current(a378):
        raise AssertionError("A385A requires the current A378 point source")
    if a385s.get("artifact") != "A385S" or not authorities_current(a385s):
        raise AssertionError("A385A requires the current A385S chart source")
    if a385i.get("artifact") != "A385I" or not authorities_current(a385i):
        raise AssertionError("A385A requires the current A385I outer source")
    point_by_chart = {
        row["line_chart"]: row for row in a378["chart_executions"]
    }
    raw_by_chart = {
        row["line_chart"]: row for row in a385i["chart_executions"]
    }
    charts = [
        chart_execution(
            row,
            point_by_chart[row["line_chart"]],
            raw_by_chart[row["line_chart"]],
        )
        for row in a385s["charts"]
    ]
    maximum_covariant = max(
        row["maximum_covariant_centered_disk_radius_upper"] for row in charts
    )
    maximum_forcing = max(
        row["maximum_beta_forcing_centered_disk_radius_upper"] for row in charts
    )
    raw_covariant = float(
        a385i["summary"]["maximum_covariant_row_component_radius_upper"]
    )
    raw_forcing = float(
        a385i["summary"]["maximum_beta_affine_forcing_radius_upper"]
    )
    payload = {
        "schema": "MTTQ79HeightFourPGL3CenteredAffineHessianSource.v1",
        "status": "PGL3_POLYDISK_LOCAL_HESSIAN_SOURCE_CENTERED_AFFINE_DEPENDENCE_CERTIFIED",
        "artifact": ARTIFACT,
        "domain_model": (
            "each real-imaginary coordinate square is enclosed by an independent "
            "complex unit disk: z_s=rho*epsilon_s, |epsilon_s|<=1, rho=sqrt(2)*r"
        ),
        "affine_model": (
            "f(z)=f_0+sum_s f_s epsilon_s+Delta_f, with a rigorous uniform "
            "complex-disk bound on Delta_f"
        ),
        "exponential_remainder_identity": (
            "||exp(Z)-I-Z||_infinity <= exp(u)-1-u, "
            "u=sum_s rho||G_s||_infinity"
        ),
        "Frechet_remainder_identity": (
            "||Dexp_Z[G_s]-G_s-(ZG_s+G_sZ)/2||_infinity "
            "<= ||G_s||_infinity(exp(u)-1-u)"
        ),
        "chart_executions": charts,
        "summary": {
            "certified_chart_count": 2,
            "coordinate_count": 8,
            "certified_covariant_affine_forms": 2 * 8 * 8 * 5,
            "certified_beta_forcing_affine_forms": 2 * 8 * 8,
            "maximum_covariant_centered_disk_radius_upper": maximum_covariant,
            "maximum_beta_forcing_centered_disk_radius_upper": maximum_forcing,
            "A385I_raw_covariant_radius_upper": raw_covariant,
            "A385I_raw_beta_forcing_radius_upper": raw_forcing,
            "covariant_radius_compression_factor": raw_covariant / maximum_covariant,
            "beta_forcing_radius_compression_factor": raw_forcing / maximum_forcing,
            "maximum_affine_reduction_weighted_contraction_upper": max(
                solve["weighted_contraction_upper"]
                for chart in charts
                for solve in chart["weighted_affine_reduction_solves"]
            ),
            "every_affine_center_replays_A378": True,
            "every_affine_disk_overlaps_A385I_outer_box": True,
        },
        "authority": {
            "A378_point_Hessian_source": authority(A378),
            "A385S_polydisk_chart_source": authority(A385S),
            "A385I_raw_polydisk_outer_source": authority(A385I),
            "affine_runtime": authority(Path(affine.__file__).resolve()),
            "builder_source": authority(Path(__file__).resolve()),
        },
        "strict_scope": {
            "observed_SM_values_used": False,
            "same_selected_n3_alignment_and_PGL3_generators_used": True,
            "all_eight_coordinate_dependencies_retained_affinely": True,
            "matrix_exponential_quadratic_remainder_closed": True,
            "all_sixteen_Frechet_derivative_quadratic_remainders_closed": True,
            "all_reduction_solves_weighted_Neumann_certified": True,
            "local_covariant_Hessian_rows_centered_affine_closed": True,
            "local_anchored_beta_forcing_centered_affine_closed": True,
            "moving_initial_cycle_polydisk_enclosure_closed": False,
            "full_path_Hessian_polydisk_transport_closed": False,
            "wall_free_polydisk_closed": False,
            "full_residual_Jacobian_polydisk_transport_closed": False,
            "interval_Newton_existence_and_uniqueness_closed": False,
            "covariant_zero_proved": False,
            "full_SM_closure_proved": False,
        },
        "next_required_artifact": (
            "propagate the centered affine source and moving affine H1 initial "
            "cycles through the certified target, handle, beta, and PL paths"
        ),
    }
    dump(OUTPUT, payload)
    NOTE.write_text(
        "# MTT q79 Height-Four PGL3 Centered Affine Hessian Source (A385A) v1\n\n"
        "A385A replaces the dependency-forgetting A385I outer evaluation by a "
        "centered eight-variable complex affine model. It retains every first "
        "coordinate coefficient and bounds only quadratic-and-higher terms. "
        "Every parametric reduction solve is independently gated by a positive "
        "weighted Neumann contraction.\n\n"
        f"The maximum covariant-row disk radius is `{maximum_covariant:.12g}` "
        f"and the maximum anchored-beta forcing radius is "
        f"`{maximum_forcing:.12g}`. Relative to A385I this contracts the two "
        f"outer radii by factors `{raw_covariant / maximum_covariant:.12g}` and "
        f"`{raw_forcing / maximum_forcing:.12g}`.\n\n"
        "This certifies the local source on the polydisk. Moving initial cycles "
        "and complete path transport remain separate obligations before "
        "Krawczyk.\n",
        encoding="utf-8",
    )
    print(f"wrote {relative(OUTPUT)}")
    print(f"wrote {relative(NOTE)}")
    print(json.dumps(payload["summary"], indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
