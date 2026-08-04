from __future__ import annotations

import argparse
import hashlib
import json
import math
from pathlib import Path

import numpy as np
from flint import acb, acb_mat, arb, ctx

import certify_q79_height4_d087_full_residue_main_interval as n3_engine
import certify_q79_selected_side_beta_defect_transport as validated


ROOT = Path(__file__).resolve().parents[1]
PERIOD_DIRECTORY = (
    ROOT
    / "candidate_data"
    / "selected_q79covariantperiodbranchcutsetandtightbetatransport"
    / "selected_alignment_thimble_periods"
)
PROBE = PERIOD_DIRECTORY / "covariant_floating_probe"
VALIDATED = PROBE / "validated_transport"
BASE_LIFT = VALIDATED / "n3.rank3.base_lift.interval.json"
BETA = VALIDATED / "n3.rank3.anchored_beta.interval.json"
A378 = VALIDATED / "n3.hessian_source.json"
OUTPUT = VALIDATED / "n3.beta_hessian.interval.json"
CHECKPOINT = VALIDATED / "n3.beta_hessian.checkpoint.json"
NOTE = ROOT / "proof_corpus" / "MTT_q79HeightFourRank3BetaHessianInterval_A379_v1.md"
ARTIFACT = "A379"
WAYPOINTS = [
    0 + 0j,
    0.65 + 0j,
    0.65 - 0.1j,
    0.82 - 0.1j,
    0.82 + 0j,
    1 + 0j,
]


TM = validated.TaylorModel


def load(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def dump(path: Path, value: dict) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(value, indent=2, sort_keys=True) + "\n", encoding="utf-8")


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def relative(path: Path) -> str:
    return str(path.relative_to(ROOT)).replace("\\", "/")


def pair(value: complex) -> dict[str, str]:
    return {
        "real": format(float(value.real), ".17g"),
        "imaginary": format(float(value.imag), ".17g"),
    }


def tm_zero(prototype: TM) -> TM:
    return prototype.constant(0, prototype.order, prototype.radius)


def tm_row_matrix(row: list[TM], matrix: list[list[TM]]) -> list[TM]:
    zero = tm_zero(row[0])
    return [
        sum((row[index] * matrix[index][column] for index in range(len(row))), zero)
        for column in range(len(matrix[0]))
    ]


def tm_reduction_solution(
    f_coefficients: list[TM], f_derivative: list[TM]
) -> tuple[list[list[TM]], list[list[TM]], float, float]:
    prototype = f_coefficients[0]
    zero = tm_zero(prototype)
    polynomial_derivative = [
        index * f_coefficients[index] for index in range(1, 7)
    ]
    reduction = [[zero for _ in range(11)] for _ in range(11)]
    targets = [[zero for _ in range(5)] for _ in range(11)]
    half = acb("0.5")
    for power in range(6):
        if power:
            for index, coefficient in enumerate(f_coefficients):
                reduction[index + power - 1][power] += power * coefficient
        for index, coefficient in enumerate(polynomial_derivative):
            reduction[index + power][power] -= half * coefficient
    for power in range(5):
        for index, coefficient in enumerate(f_coefficients):
            reduction[index + power][6 + power] += coefficient
        for index, coefficient in enumerate(f_derivative):
            targets[index + power][power] -= half * coefficient
    solved, solve_neumann, solve_error = validated.tm_matrix_solve(
        reduction, targets
    )
    exact_terms = [
        [solved[index][power] for index in range(6)] for power in range(5)
    ]
    connection = [
        [solved[6 + index][power] for index in range(5)]
        for power in range(5)
    ]
    return connection, exact_terms, solve_neumann, solve_error


def tm_connection_and_source(
    system: validated.SelectedQ79IntervalSystem,
    line: list[TM],
    line_derivative: list[TM],
) -> tuple[list[list[TM]], list[TM], dict]:
    f_coefficients, f_derivative = validated.aligned_tm_coefficients_and_derivative(
        system.evaluator.tables["F6"],
        line,
        line_derivative,
        chart=system.line_chart,
    )
    g_coefficients, _g_derivative = validated.aligned_tm_coefficients_and_derivative(
        system.evaluator.tables["G3"],
        line,
        line_derivative,
        chart=system.line_chart,
    )
    q_coefficients, q_derivative = validated.aligned_tm_coefficients_and_derivative(
        system.evaluator.tables["Q2"],
        line,
        line_derivative,
        chart=system.line_chart,
    )
    connection, exact_terms, solve_neumann, solve_error = tm_reduction_solution(
        f_coefficients, f_derivative
    )
    q0, q1, q2 = q_coefficients
    discriminant = q1**2 - 4 * q2 * q0
    discriminant_lower = discriminant.absolute_lower()
    if discriminant_lower <= 0.0:
        raise ZeroDivisionError("Hessian transport Q2 discriminant contains zero")
    root_sum = -q1 / q2
    root_product = q0 / q2
    relation_constant = -root_product
    relation_linear = root_sum
    q_derivative_pair = validated.quotient_reduce(
        q_derivative, relation_constant, relation_linear
    )
    g_pair = validated.quotient_reduce(
        g_coefficients, relation_constant, relation_linear
    )
    g_norm = (
        g_pair[0] ** 2
        + root_sum * g_pair[0] * g_pair[1]
        + root_product * g_pair[1] ** 2
    )
    g_norm_lower = g_norm.absolute_lower()
    if g_norm_lower <= 0.0:
        raise ZeroDivisionError("Hessian transport G3 quotient norm contains zero")
    g_inverse = validated.quotient_pair_inverse(
        g_pair, root_sum, root_product
    )
    zero = tm_zero(q0)
    source = [zero for _ in range(5)]
    for power in range(5):
        exact_pair = validated.quotient_reduce(
            exact_terms[power], relation_constant, relation_linear
        )
        power_pair = validated.quotient_pair_power(
            power, relation_constant, relation_linear
        )
        velocity_numerator = validated.quotient_pair_multiply(
            power_pair,
            q_derivative_pair,
            relation_constant,
            relation_linear,
        )
        exact_weight = validated.quotient_pair_multiply(
            exact_pair, g_inverse, relation_constant, relation_linear
        )
        velocity_weight = validated.quotient_pair_multiply(
            velocity_numerator,
            g_inverse,
            relation_constant,
            relation_linear,
        )
        source[power] = (
            2 * exact_weight[0]
            + root_sum * exact_weight[1]
            - velocity_weight[1] / q2
        )
    return connection, source, {
        "reduction_neumann_norm": solve_neumann,
        "reduction_solution_remainder": solve_error,
        "q_discriminant_absolute_lower": discriminant_lower,
        "g3_quotient_norm_absolute_lower": g_norm_lower,
    }


def tm_residue_rows(
    system: validated.SelectedQ79IntervalSystem,
    elliptic: list[TM],
    line: list[TM],
) -> list[list[TM]]:
    zero = tm_zero(elliptic[0])
    rows: list[list[TM]] = []
    for generator in system.generators:
        variation = validated.tm_matrix_vector(
            system.alignment * generator, elliptic
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
                zero,
                zero,
                zero,
            ]
        )
    return rows


def tm_residue_directional_derivatives(
    system: validated.SelectedQ79IntervalSystem,
    elliptic: list[TM],
    line: list[TM],
    direction: int,
) -> list[list[TM]]:
    generator_s = system.generators[direction]
    line_s = validated.tm_matrix_vector(
        system.alignment * generator_s, elliptic
    )
    zero = tm_zero(elliptic[0])
    rows: list[list[TM]] = []
    for generator_r in system.generators:
        variation_r = validated.tm_matrix_vector(
            system.alignment * generator_r, elliptic
        )
        variation_rs = validated.tm_matrix_vector(
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
                zero,
                zero,
                zero,
            ]
        )
    return rows


def build_affine_hessian_system(
    system: validated.SelectedQ79IntervalSystem,
    start: complex,
    direction: complex,
    step: float,
    order: int,
) -> tuple[list[list[TM]], list[TM], list[list[TM]], list[TM], dict]:
    radius = arb(format(step, ".17g"))
    a_value, b_value, elliptic_residual, elliptic_remainder = (
        validated.validated_ab_taylor_models(
            system, start, direction, radius, order
        )
    )
    one = a_value.constant(1, order, radius)
    zero = a_value.constant(0, order, radius)
    elliptic = [a_value, b_value, one]
    elliptic_w = [
        acb(2) * system.period_length * b_value,
        system.period_length * (acb(3) * a_value**2 - 1),
        zero,
    ]
    line = validated.tm_matrix_vector(system.alignment, elliptic)
    line_w = validated.tm_matrix_vector(system.alignment, elliptic_w)
    connection_w, source_w, w_diagnostics = tm_connection_and_source(
        system, line, line_w
    )
    residues = tm_residue_rows(system, elliptic, line)
    hessian_rows: list[list[TM]] = []
    hessian_forcing: list[TM] = []
    direction_diagnostics = []
    for selected_direction in range(8):
        generator = system.generators[selected_direction]
        line_s = validated.tm_matrix_vector(
            system.alignment * generator, elliptic
        )
        connection_s, source_s, diagnostics_s = tm_connection_and_source(
            system, line, line_s
        )
        direct_rows = tm_residue_directional_derivatives(
            system, elliptic, line, selected_direction
        )
        for residue_index in range(8):
            transported = tm_row_matrix(residues[residue_index], connection_s)
            hessian_rows.append(
                [
                    direct_rows[residue_index][column] + transported[column]
                    for column in range(5)
                ]
            )
            hessian_forcing.append(
                sum(
                    (
                        residues[residue_index][column] * source_s[column]
                        for column in range(5)
                    ),
                    zero,
                )
            )
        direction_diagnostics.append(diagnostics_s)

    displacement = acb(0, 1) * validated.as_acb(direction)
    lift_matrix = [
        [displacement * value for value in row] for row in connection_w
    ]
    lift_forcing = [displacement * value for value in source_w]
    output_rows = [
        [displacement * value for value in row]
        for row in residues + hessian_rows
    ]
    output_forcing = [zero for _ in range(8)] + [
        displacement * value for value in hessian_forcing
    ]
    all_diagnostics = [w_diagnostics, *direction_diagnostics]
    return lift_matrix, lift_forcing, output_rows, output_forcing, {
        "elliptic_residual_bound": elliptic_residual,
        "elliptic_remainder_bound": elliptic_remainder,
        "maximum_reduction_neumann_norm": max(
            row["reduction_neumann_norm"] for row in all_diagnostics
        ),
        "maximum_reduction_solution_remainder": max(
            row["reduction_solution_remainder"] for row in all_diagnostics
        ),
        "minimum_q_discriminant_absolute_lower": min(
            row["q_discriminant_absolute_lower"] for row in all_diagnostics
        ),
        "minimum_g3_quotient_norm_absolute_lower": min(
            row["g3_quotient_norm_absolute_lower"] for row in all_diagnostics
        ),
        "derived_output_row_count": len(output_rows),
        "derived_hessian_row_count": len(hessian_rows),
    }


def candidate_output_polynomials(
    output_rows: list[list[TM]],
    output_forcing: list[TM],
    lift_state: list[TM],
    initial_values: list[acb],
) -> list[TM]:
    order = lift_state[0].order
    radius = lift_state[0].radius
    values = []
    for row, forcing, initial in zip(
        output_rows, output_forcing, initial_values
    ):
        coefficients = [initial]
        for degree in range(order):
            right = forcing.coefficients[degree]
            for coefficient_degree in range(degree + 1):
                state_degree = degree - coefficient_degree
                right += sum(
                    (
                        row[column].coefficients[coefficient_degree]
                        * lift_state[column].coefficients[state_degree]
                        for column in range(5)
                    ),
                    acb(0),
                )
            coefficients.append(right / acb(degree + 1))
        values.append(TM(coefficients, radius).midpoint_polynomial())
    return values


def validated_affine_hessian_step(
    system: validated.SelectedQ79IntervalSystem,
    start: complex,
    direction: complex,
    step: float,
    center: list[acb],
    input_lift_frame: validated.LiftErrorFrame,
    input_output_radii: list[arb],
    *,
    order: int,
    system_builder=None,
) -> tuple[list[acb], validated.LiftErrorFrame, list[arb], dict]:
    if system_builder is None:
        system_builder = build_affine_hessian_system
    (
        lift_matrix,
        lift_forcing,
        output_rows,
        output_forcing,
        system_diagnostics,
    ) = system_builder(system, start, direction, step, order)
    lift_state, fundamental = validated.candidate_flow_polynomials(
        lift_matrix, lift_forcing, center[:5]
    )
    output_state = candidate_output_polynomials(
        output_rows, output_forcing, lift_state, center[5:]
    )
    lift_derivative = validated.tm_vector_derivative(lift_state)
    lift_residual = [
        value + lift_forcing[index] - lift_derivative[index]
        for index, value in enumerate(
            validated.tm_matrix_vector_multiply(lift_matrix, lift_state)
        )
    ]
    fundamental_residual = validated.tm_matrix_subtract(
        validated.tm_matrix_multiply(lift_matrix, fundamental),
        validated.tm_matrix_derivative(fundamental),
    )
    inverse_norm, inverse_defect = validated.tm_verified_inverse_bound(
        fundamental
    )
    linear_defect = (
        inverse_norm
        * validated.tm_matrix_infinity_norm(fundamental_residual)
    )
    affine_defect = inverse_norm * validated.tm_vector_infinity_norm(
        lift_residual
    )
    step_ball = arb(format(step, ".17g"))
    growth = (linear_defect * step_ball).exp()
    forced_error = (
        affine_defect * step_ball
        if validated.upper(linear_defect) == 0.0
        else affine_defect * (growth - arb(1)) / linear_defect
    )
    input_lift_radius = input_lift_frame.physical_radius()
    transformed_lift_error = growth * input_lift_radius + forced_error
    transformed_lift_correction = (
        (growth - arb(1)) * input_lift_radius + forced_error
    )

    endpoint = step_ball
    endpoint_lift = [value.evaluate_polynomial(endpoint) for value in lift_state]
    endpoint_outputs = [
        value.evaluate_polynomial(endpoint) for value in output_state
    ]
    endpoint_fundamental = acb_mat(
        [
            [
                fundamental[row][column].evaluate_polynomial(endpoint)
                for column in range(5)
            ]
            for row in range(5)
        ]
    )
    output_fundamental = endpoint_fundamental * input_lift_frame.fundamental
    output_inverse = output_fundamental.inv()
    correction_pullback = output_inverse * endpoint_fundamental
    lift_rounding = arb(
        str(max(validated.radius_upper(value) for value in endpoint_lift))
    )
    correction_upper = validated.upper(transformed_lift_correction)
    rounding_upper = validated.upper(lift_rounding)
    coordinate_radii = []
    for row in range(5):
        correction_norm = sum(
            (abs(correction_pullback[row, column]) for column in range(5)),
            arb(0),
        )
        rounding_norm = sum(
            (abs(output_inverse[row, column]) for column in range(5)),
            arb(0),
        )
        coordinate_radii.append(
            input_lift_frame.coordinate_radii[row]
            + arb(str(correction_upper)) * correction_norm
            + arb(str(rounding_upper)) * rounding_norm
        )
    output_lift_frame = validated.LiftErrorFrame(
        fundamental=output_fundamental,
        coordinate_radii=coordinate_radii,
    )
    fundamental_uniform_norm = validated.tm_matrix_infinity_norm(fundamental)
    lift_error_uniform = fundamental_uniform_norm * transformed_lift_error
    output_derivatives = validated.tm_vector_derivative(output_state)
    output_radii = []
    increment_uppers = []
    residual_uppers = []
    row_norm_uppers = []
    for index, row in enumerate(output_rows):
        row_action = sum(
            (row[column] * lift_state[column] for column in range(5)),
            tm_zero(row[0]),
        )
        residual = (
            row_action
            + output_forcing[index]
            - output_derivatives[index]
        )
        residual_bound = residual.absolute_bound()
        row_norm = sum((value.absolute_bound() for value in row), arb(0))
        increment = step_ball * (
            row_norm * lift_error_uniform + residual_bound
        )
        polynomial_rounding = arb(
            str(validated.radius_upper(endpoint_outputs[index]))
        )
        output_radii.append(
            input_output_radii[index] + increment + polynomial_rounding
        )
        increment_uppers.append(validated.upper(increment))
        residual_uppers.append(validated.upper(residual_bound))
        row_norm_uppers.append(validated.upper(row_norm))
    endpoint_center = [
        validated.SelectedQ79IntervalSystem.midpoint_acb(value)
        for value in endpoint_lift + endpoint_outputs
    ]
    return endpoint_center, output_lift_frame, output_radii, {
        **system_diagnostics,
        "fundamental_inverse_neumann_norm": inverse_defect,
        "linear_defect_bound": validated.upper(linear_defect),
        "affine_defect_bound": validated.upper(affine_defect),
        "transformed_lift_correction": correction_upper,
        "input_lift_radius": validated.upper(input_lift_radius),
        "output_lift_radius": validated.upper(
            output_lift_frame.physical_radius()
        ),
        "maximum_output_row_norm": max(row_norm_uppers),
        "maximum_output_residual_bound": max(residual_uppers),
        "maximum_output_increment_error": max(increment_uppers),
        "maximum_output_radius": max(
            validated.upper(value) for value in output_radii
        ),
    }


def initial_state() -> tuple[list[acb], validated.LiftErrorFrame, list[arb]]:
    base_lift = load(BASE_LIFT)
    initial_balls = [
        validated.interval_from_bounds(value)
        for value in base_lift["y_chart_base_lift"]
    ]
    center = [
        validated.SelectedQ79IntervalSystem.midpoint_acb(value)
        for value in initial_balls
    ] + [acb(0) for _ in range(72)]
    fundamental = acb_mat(5, 5)
    for index in range(5):
        fundamental[index, index] = acb(1)
    frame = validated.LiftErrorFrame(
        fundamental=fundamental,
        coordinate_radii=[value.rad().upper() for value in initial_balls],
    )
    return center, frame, [arb(0) for _ in range(72)]


def configuration(arguments: argparse.Namespace) -> dict:
    return {
        "dps": arguments.dps,
        "order": arguments.order,
        "initial_step": format(arguments.initial_step, ".17g"),
        "minimum_step": format(arguments.minimum_step, ".17g"),
        "waypoints": [pair(value) for value in WAYPOINTS],
        "base_lift_sha256": sha256(BASE_LIFT),
        "n3_fibration_sha256": sha256(n3_engine.FIBRATION),
        "A378_sha256": sha256(A378),
        "builder_source_sha256": sha256(Path(__file__).resolve()),
        "validated_engine_sha256": sha256(Path(validated.__file__).resolve()),
    }


def smoke_test(system: validated.SelectedQ79IntervalSystem, order: int) -> dict:
    step = 1.0e-5
    lift_matrix, lift_forcing, output_rows, output_forcing, diagnostics = (
        build_affine_hessian_system(system, 0 + 0j, 1 + 0j, step, order)
    )
    original_matrix, original_forcing, _original_diagnostics = (
        validated.build_taylor_system(system, 0 + 0j, 1 + 0j, step, order)
    )
    maximum_coefficient_difference = 0.0
    for row in range(5):
        for column in range(5):
            for degree in range(order + 1):
                difference = (
                    lift_matrix[row][column].coefficients[degree]
                    - original_matrix[row][column].coefficients[degree]
                )
                maximum_coefficient_difference = max(
                    maximum_coefficient_difference,
                    validated.upper(abs(difference)),
                )
        for degree in range(order + 1):
            difference = (
                lift_forcing[row].coefficients[degree]
                - original_forcing[row].coefficients[degree]
            )
            maximum_coefficient_difference = max(
                maximum_coefficient_difference,
                validated.upper(abs(difference)),
            )
    for row in range(8):
        for column in range(5):
            for degree in range(order + 1):
                difference = (
                    output_rows[row][column].coefficients[degree]
                    - original_matrix[5 + row][column].coefficients[degree]
                )
                maximum_coefficient_difference = max(
                    maximum_coefficient_difference,
                    validated.upper(abs(difference)),
                )
        for degree in range(order + 1):
            difference = (
                output_forcing[row].coefficients[degree]
                - original_forcing[5 + row].coefficients[degree]
            )
            maximum_coefficient_difference = max(
                maximum_coefficient_difference,
                validated.upper(abs(difference)),
            )
    if maximum_coefficient_difference > 1.0e-32:
        raise AssertionError(
            "affine Hessian system does not reproduce the validated beta system: "
            f"maximum coefficient difference={maximum_coefficient_difference:.6e}"
        )
    return {
        "step": step,
        "order": order,
        "maximum_original_beta_system_coefficient_difference": (
            maximum_coefficient_difference
        ),
        "output_row_count": len(output_rows),
        "hessian_row_count": len(output_rows) - 8,
        **diagnostics,
    }


def execute(arguments: argparse.Namespace) -> dict:
    system = n3_engine.exact_target_system(arguments.dps)
    smoke = smoke_test(system, min(arguments.order, 18))
    if arguments.smoke_only:
        print(json.dumps(smoke, indent=2))
        return {"smoke_test": smoke}
    config = configuration(arguments)
    if arguments.resume:
        if not CHECKPOINT.exists():
            raise FileNotFoundError("beta-Hessian checkpoint is absent")
        checkpoint = load(CHECKPOINT)
        if checkpoint.get("schema") != "MTTQ79BetaHessianCheckpoint.v1":
            raise ValueError("beta-Hessian checkpoint schema changed")
        if checkpoint.get("configuration") != config:
            raise ValueError("beta-Hessian checkpoint configuration changed")
        center = [validated.decoded_acb(value) for value in checkpoint["center"]]
        frame = validated.LiftErrorFrame(
            fundamental=validated.decoded_matrix(checkpoint["lift_fundamental"]),
            coordinate_radii=[arb(value) for value in checkpoint["coordinate_radii"]],
        )
        output_radii = [arb(value) for value in checkpoint["output_radii"]]
        accepted = checkpoint["accepted_steps"]
        rejected = int(checkpoint["rejected_step_count"])
        minimum_accepted_step = float(checkpoint["minimum_accepted_step"])
        proposed_step = float(checkpoint["proposed_step"])
        starting_segment = int(checkpoint["segment_index"])
        starting_position = float(checkpoint["segment_position"])
        print(
            f"resumed beta-Hessian checkpoint steps={len(accepted)} "
            f"segment={starting_segment} position={starting_position:.12g}",
            flush=True,
        )
    else:
        center, frame, output_radii = initial_state()
        accepted = []
        rejected = 0
        minimum_accepted_step = math.inf
        proposed_step = arguments.initial_step
        starting_segment = 0
        starting_position = 0.0

    def save_checkpoint(segment_index: int, position: float) -> None:
        validated.atomic_dump(
            CHECKPOINT,
            {
                "schema": "MTTQ79BetaHessianCheckpoint.v1",
                "configuration": config,
                "segment_index": segment_index,
                "segment_position": format(position, ".17g"),
                "proposed_step": format(proposed_step, ".17g"),
                "center": [validated.encoded_acb(value) for value in center],
                "lift_fundamental": validated.encoded_matrix(frame.fundamental),
                "coordinate_radii": [str(value) for value in frame.coordinate_radii],
                "output_radii": [str(value) for value in output_radii],
                "accepted_steps": accepted,
                "rejected_step_count": rejected,
                "minimum_accepted_step": format(minimum_accepted_step, ".17g"),
            },
        )

    segment_pairs = list(zip(WAYPOINTS, WAYPOINTS[1:]))
    for segment_index in range(starting_segment, len(segment_pairs)):
        left, right = segment_pairs[segment_index]
        length = abs(right - left)
        if length == 0.0:
            continue
        direction = (right - left) / length
        position = starting_position if segment_index == starting_segment else 0.0
        if segment_index != starting_segment:
            proposed_step = min(arguments.initial_step, length)
        while position < length:
            if len(accepted) >= arguments.maximum_steps:
                raise ArithmeticError("beta-Hessian transport exceeded step budget")
            step = min(proposed_step, length - position)
            if step < arguments.minimum_step:
                raise ArithmeticError("beta-Hessian transport requires a smaller step")
            start = left + direction * position
            try:
                next_center, next_frame, next_radii, diagnostics = (
                    validated_affine_hessian_step(
                        system,
                        start,
                        direction,
                        step,
                        center,
                        frame,
                        output_radii,
                        order=arguments.order,
                    )
                )
                if diagnostics["transformed_lift_correction"] > 1.0e-6:
                    raise ArithmeticError("lift correction exceeds local budget")
                if diagnostics["maximum_output_increment_error"] > 1.0e-3:
                    raise ArithmeticError("output increment exceeds local budget")
                if diagnostics["maximum_output_radius"] > arguments.maximum_radius:
                    raise ArithmeticError("output radius exceeds global budget")
            except (ArithmeticError, ZeroDivisionError, ValueError) as error:
                rejected += 1
                proposed_step = step / 2.0
                if rejected % 10 == 0:
                    print(
                        f"beta-Hessian rejections={rejected} segment={segment_index} "
                        f"position={position:.12g} next={proposed_step:.3e} "
                        f"reason={type(error).__name__}: {error}",
                        flush=True,
                    )
                if proposed_step < arguments.minimum_step:
                    raise
                continue
            center = next_center
            frame = next_frame
            output_radii = next_radii
            position = min(length, position + step)
            minimum_accepted_step = min(minimum_accepted_step, step)
            accepted.append(
                {
                    "segment_index": segment_index,
                    "position": position,
                    "step": step,
                    **diagnostics,
                }
            )
            quality = max(
                diagnostics["maximum_reduction_neumann_norm"],
                diagnostics["fundamental_inverse_neumann_norm"],
            )
            proposed_step = min(
                arguments.initial_step,
                step * (1.5 if quality < 0.25 else 1.15),
            )
            if len(accepted) % 10 == 0 or position == length:
                save_checkpoint(segment_index, position)
            if len(accepted) <= 3 or len(accepted) % 10 == 0 or position == length:
                print(
                    f"beta-Hessian steps={len(accepted)} segment={segment_index} "
                    f"position={position:.12g}/{length:.12g} "
                    f"radius={max(validated.upper(value) for value in output_radii):.3e}",
                    flush=True,
                )

    beta_centers = np.asarray(
        [validated.midpoint(value) for value in center[5:13]],
        dtype=np.complex128,
    )
    hessian = np.empty((8, 8), dtype=np.complex128)
    hessian_radii = np.empty((8, 8), dtype=np.float64)
    for selected_direction in range(8):
        for residue_index in range(8):
            offset = selected_direction * 8 + residue_index
            hessian[residue_index, selected_direction] = validated.midpoint(
                center[13 + offset]
            )
            hessian_radii[residue_index, selected_direction] = validated.upper(
                output_radii[8 + offset]
            )
    beta_radii = np.asarray(
        [validated.upper(value) for value in output_radii[:8]],
        dtype=np.float64,
    )
    beta_packet = load(BETA)
    beta_reference = np.asarray(
        [
            complex(float(value["real"]), float(value["imaginary"]))
            for value in beta_packet["endpoint"]["beta_center"]
        ],
        dtype=np.complex128,
    )
    beta_reference_radius = float(
        beta_packet["endpoint"]["uniform_component_radius_upper"]
    )
    beta_difference = abs(beta_centers - beta_reference)
    beta_replay_contained = beta_difference <= beta_radii + beta_reference_radius
    if not bool(np.all(beta_replay_contained)):
        raise AssertionError("beta-Hessian transport does not overlap A376")

    payload = {
        "schema": "MTTQ79HeightFourRank3BetaHessianInterval.v1",
        "status": "N3_RANK3_ANCHORED_BETA_COMPLEX_8_BY_8_HESSIAN_INTERVAL_CERTIFIED",
        "artifact": ARTIFACT,
        "coordinate_convention": (
            "right exponential PGL3 chart A(z_s)=A exp(z_s G_s); "
            "rows r and columns s are D_s beta_r"
        ),
        "beta_rows": [
            {
                "residue_index_zero_based": index,
                "interval_center": pair(beta_centers[index]),
                "component_radius_upper": float(beta_radii[index]),
                "A376_center_difference": float(beta_difference[index]),
                "A376_intervals_overlap": bool(beta_replay_contained[index]),
            }
            for index in range(8)
        ],
        "complex_beta_Hessian_8_by_8": [
            [
                {
                    "row_zero_based": row,
                    "column_zero_based": column,
                    "interval_center": pair(hessian[row, column]),
                    "component_radius_upper": float(hessian_radii[row, column]),
                }
                for column in range(8)
            ]
            for row in range(8)
        ],
        "summary": {
            "certified_beta_rows": 8,
            "certified_Hessian_entries": 64,
            "maximum_beta_component_radius_upper": float(np.max(beta_radii)),
            "maximum_Hessian_component_radius_upper": float(
                np.max(hessian_radii)
            ),
            "Hessian_product_box_frobenius_radius_upper": float(
                np.linalg.norm(hessian_radii)
            ),
            "Hessian_center_Frobenius_norm": float(np.linalg.norm(hessian)),
            "all_A376_beta_intervals_overlap": bool(np.all(beta_replay_contained)),
            "maximum_A376_beta_center_difference": float(np.max(beta_difference)),
            "accepted_step_count": len(accepted),
            "rejected_step_count": rejected,
            "minimum_accepted_step": minimum_accepted_step,
        },
        "smoke_test": smoke,
        "execution": {
            "waypoints": [pair(value) for value in WAYPOINTS],
            "configuration": config,
            "steps": accepted,
            "checkpoint": relative(CHECKPOINT),
            "checkpoint_sha256": sha256(CHECKPOINT),
        },
        "authority": {
            name: {"path": relative(path), "sha256": sha256(path)}
            for name, path in {
                "A375_base_lift": BASE_LIFT,
                "A376_beta_interval": BETA,
                "A378_Hessian_integrand_source": A378,
                "n3_fibration": n3_engine.FIBRATION,
                "validated_Taylor_engine": Path(validated.__file__).resolve(),
                "builder_source": Path(__file__).resolve(),
            }.items()
        },
        "strict_scope": {
            "observed_SM_values_used": False,
            "same_source_beta_and_Hessian_integrands_used": True,
            "A378_affine_Hessian_source_consumed": True,
            "A376_beta_rows_independently_replayed": True,
            "rank3_anchored_beta_Hessian_interval_closed": True,
            "thimble_and_handle_Hessian_intervals_closed": False,
            "full_residual_interval_Jacobian_closed": False,
            "interval_Newton_existence_and_uniqueness_closed": False,
            "covariant_zero_proved": False,
            "full_SM_closure_proved": False,
        },
        "next_required_artifact": (
            "integrate the same A378 Hessian rows on the selected 76 thimbles, "
            "handle combination, and PL correction, then subtract from this "
            "beta Hessian to form the residual interval Jacobian"
        ),
    }
    dump(OUTPUT, payload)
    NOTE.write_text(
        "# MTT q79 Height-Four Rank-3 Beta Hessian Interval (A379) v1\n\n"
        "A379 integrates the A378 affine same-source second-response system "
        "along the exact A376 local-lower contour. The triangular validated "
        "Taylor model transports five lift coordinates, eight beta rows, and "
        "64 complex Hessian entries with separate output radii.\n\n"
        f"The maximum Hessian component radius is "
        f"`{np.max(hessian_radii):.12g}`. The ordinary beta rows overlap all "
        "eight independently computed A376 intervals. No observed Standard "
        "Model value or fitted Jacobian entry is used.\n\n"
        "This closes the anchored-beta contribution to the interval Jacobian. "
        "The thimble, handle, and Picard-Lefschetz Hessian contributions remain "
        "to be integrated before interval Newton can be executed.\n",
        encoding="utf-8",
    )
    print(f"wrote {relative(OUTPUT)}")
    print(f"wrote {relative(NOTE)}")
    print(json.dumps(payload["summary"], indent=2))
    return payload


def parser() -> argparse.ArgumentParser:
    value = argparse.ArgumentParser()
    value.add_argument("--dps", type=int, default=90)
    value.add_argument("--order", type=int, default=28)
    value.add_argument("--initial-step", type=float, default=0.006)
    value.add_argument("--minimum-step", type=float, default=1.0e-10)
    value.add_argument("--maximum-steps", type=int, default=50000)
    value.add_argument("--maximum-radius", type=float, default=0.5)
    value.add_argument("--resume", action="store_true")
    value.add_argument("--smoke-only", action="store_true")
    return value


def main() -> int:
    arguments = parser().parse_args()
    ctx.dps = arguments.dps
    a378 = load(A378)
    if not a378["strict_scope"][
        "all_64_anchored_beta_affine_hessian_integrand_rows_derived"
    ]:
        raise AssertionError("A379 requires the full A378 affine source")
    execute(arguments)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
