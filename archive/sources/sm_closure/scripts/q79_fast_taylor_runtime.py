from __future__ import annotations

from collections.abc import Callable

from flint import acb, acb_poly, arb

import certify_q79_height4_rank3_beta_hessian_interval as beta_hessian
import certify_q79_selected_side_beta_defect_transport as validated


TM = validated.TaylorModel
ORIGINAL_MULTIPLY: Callable = TM.__mul__
ORIGINAL_POLYNOMIAL_BOUND: Callable = TM.polynomial_absolute_bound
ORIGINAL_CANDIDATE_OUTPUTS: Callable = beta_hessian.candidate_output_polynomials
_POWERS: dict[tuple[int, str], list[arb]] = {}
_INSTALLED = False


def powers(order: int, radius: arb) -> list[arb]:
    key = (order, str(radius))
    cached = _POWERS.get(key)
    if cached is None:
        cached = [arb(1)]
        for _ in range(2 * order):
            cached.append(cached[-1] * radius)
        _POWERS[key] = cached
    return cached


def polynomial_bound(value: TM) -> arb:
    domain_powers = powers(value.order, value.radius)
    return sum(
        (
            abs(coefficient) * domain_powers[index]
            for index, coefficient in enumerate(value.coefficients)
        ),
        arb(0),
    )


def multiply(left: TM, other: object) -> TM:
    right = left.coerce(other)
    order = left.order
    product = acb_poly(left.coefficients) * acb_poly(right.coefficients)
    coefficients = [
        product[index] if index < len(product) else acb(0)
        for index in range(order + 1)
    ]
    domain_powers = powers(order, left.radius)
    omitted = sum(
        (
            abs(product[index]) * domain_powers[index]
            for index in range(order + 1, len(product))
        ),
        arb(0),
    )
    left_bound = polynomial_bound(left)
    right_bound = polynomial_bound(right)
    remainder = (
        omitted
        + left_bound * right.remainder
        + right_bound * left.remainder
        + left.remainder * right.remainder
    )
    return TM(coefficients, left.radius, remainder)


def candidate_output_polynomials(
    output_rows: list[list[TM]],
    output_forcing: list[TM],
    lift_state: list[TM],
    initial_values: list[acb],
) -> list[TM]:
    order = lift_state[0].order
    radius = lift_state[0].radius
    lift_polynomials = [acb_poly(value.coefficients) for value in lift_state]
    values = []
    for row, forcing, initial in zip(
        output_rows, output_forcing, initial_values
    ):
        derivative = acb_poly(forcing.coefficients)
        for column in range(5):
            derivative += acb_poly(row[column].coefficients) * lift_polynomials[column]
        coefficients = [initial]
        for degree in range(order):
            value = derivative[degree] if degree < len(derivative) else acb(0)
            coefficients.append(value / acb(degree + 1))
        values.append(TM(coefficients, radius).midpoint_polynomial())
    return values


def install() -> None:
    global _INSTALLED
    if _INSTALLED:
        return
    TM.__mul__ = multiply
    TM.__rmul__ = multiply
    TM.polynomial_absolute_bound = polynomial_bound
    beta_hessian.candidate_output_polynomials = candidate_output_polynomials
    _INSTALLED = True


def uninstall() -> None:
    global _INSTALLED
    if not _INSTALLED:
        return
    TM.__mul__ = ORIGINAL_MULTIPLY
    TM.__rmul__ = ORIGINAL_MULTIPLY
    TM.polynomial_absolute_bound = ORIGINAL_POLYNOMIAL_BOUND
    beta_hessian.candidate_output_polynomials = ORIGINAL_CANDIDATE_OUTPUTS
    _INSTALLED = False
