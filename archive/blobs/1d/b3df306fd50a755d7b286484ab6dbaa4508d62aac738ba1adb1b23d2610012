from __future__ import annotations

import math
from collections.abc import Callable

from flint import acb, acb_mat, arb

import certify_q79_height4_rank3_beta_hessian_interval as beta_hessian
import certify_q79_selected_side_beta_defect_transport as validated


ORIGINAL_STEP: Callable = beta_hessian.validated_affine_hessian_step
_INSTALLED = False


def exponential_integral_upper_bound(
    linear_defect: arb, affine_defect: arb, step: arb
) -> tuple[arb, arb]:
    """Bound integral_0^h exp(L s) A ds without dividing by L."""
    growth = (linear_defect * step).exp()
    return growth, affine_defect * step * growth


def stable_validated_affine_hessian_step(
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
        system_builder = beta_hessian.build_affine_hessian_system
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
    output_state = beta_hessian.candidate_output_polynomials(
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
    inverse_norm, inverse_defect = validated.tm_verified_inverse_bound(fundamental)
    linear_defect = inverse_norm * validated.tm_matrix_infinity_norm(
        fundamental_residual
    )
    affine_defect = inverse_norm * validated.tm_vector_infinity_norm(lift_residual)
    step_ball = arb(format(step, ".17g"))
    growth, forced_error = exponential_integral_upper_bound(
        linear_defect, affine_defect, step_ball
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
            (abs(output_inverse[row, column]) for column in range(5)), arb(0)
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
            beta_hessian.tm_zero(row[0]),
        )
        residual = row_action + output_forcing[index] - output_derivatives[index]
        residual_bound = residual.absolute_bound()
        row_norm = sum((value.absolute_bound() for value in row), arb(0))
        increment = step_ball * (row_norm * lift_error_uniform + residual_bound)
        polynomial_rounding = arb(
            str(validated.radius_upper(endpoint_outputs[index]))
        )
        output_radii.append(
            input_output_radii[index] + increment + polynomial_rounding
        )
        increment_uppers.append(validated.upper(increment))
        residual_uppers.append(validated.upper(residual_bound))
        row_norm_uppers.append(validated.upper(row_norm))

    finite_values = [
        correction_upper,
        validated.upper(output_lift_frame.physical_radius()),
        *[validated.upper(value) for value in coordinate_radii],
        *[validated.upper(value) for value in output_radii],
    ]
    if not all(math.isfinite(value) for value in finite_values):
        raise ArithmeticError("stable affine Hessian step produced a non-finite bound")

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
        "output_lift_radius": validated.upper(output_lift_frame.physical_radius()),
        "maximum_output_row_norm": max(row_norm_uppers),
        "maximum_output_residual_bound": max(residual_uppers),
        "maximum_output_increment_error": max(increment_uppers),
        "maximum_output_radius": max(
            validated.upper(value) for value in output_radii
        ),
        "affine_growth_integral_bound": "A*h*exp(L*h)",
        "zero_linear_defect_regularization_by_division": False,
        "all_returned_bounds_finite": True,
    }


def install() -> None:
    global _INSTALLED
    if _INSTALLED:
        return
    beta_hessian.validated_affine_hessian_step = stable_validated_affine_hessian_step
    _INSTALLED = True


def uninstall() -> None:
    global _INSTALLED
    if not _INSTALLED:
        return
    beta_hessian.validated_affine_hessian_step = ORIGINAL_STEP
    _INSTALLED = False
