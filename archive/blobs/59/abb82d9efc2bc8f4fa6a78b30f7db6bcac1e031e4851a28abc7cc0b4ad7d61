from __future__ import annotations

import math

from flint import acb

import certify_q79_height4_target_tail_hessian_interval as base


def disk_cauchy_bounds(
    local_coefficients: list[base.DualTM],
    delta: base.DualTM,
) -> tuple[float, float, float, float, list[float], list[float], float]:
    """Certify h != 0 on a true complex disk by a polynomial majorant."""
    value_uppers = [
        base.validated.upper(value.value.absolute_bound())
        for value in local_coefficients
    ]
    derivative_uppers = [
        base.validated.upper(value.derivative.absolute_bound())
        for value in local_coefficients
    ]
    constant_lower = local_coefficients[0].value.absolute_lower()
    delta_upper = base.validated.upper(delta.value.absolute_bound())
    for exponent in range(30):
        rho = 0.5 / (2**exponent)
        variation_upper = 0.0
        for degree in range(1, len(value_uppers)):
            term = math.nextafter(value_uppers[degree] * rho**degree, math.inf)
            variation_upper = math.nextafter(variation_upper + term, math.inf)
        h_lower = math.nextafter(constant_lower - variation_upper, -math.inf)
        ratio = math.nextafter(delta_upper / (4.0 * rho**2), math.inf)
        if h_lower > 0.0 and ratio < 0.5:
            derivative_upper = 0.0
            for degree in range(len(derivative_uppers)):
                term = math.nextafter(
                    derivative_uppers[degree] * rho**degree, math.inf
                )
                derivative_upper = math.nextafter(
                    derivative_upper + term, math.inf
                )
            return (
                rho,
                h_lower,
                ratio,
                derivative_upper,
                value_uppers,
                derivative_uppers,
                constant_lower,
            )
    raise ArithmeticError("no disk-majorant Cauchy domain separates the nodal quartic")


def period_models(
    factors: list[base.DualTM],
    *,
    series_terms: int,
) -> tuple[list[base.DualTM], dict]:
    q0, q1, *h = factors
    center = -q1 / 2
    delta = q1**2 - 4 * q0
    maximum_y_degree = 2 * series_terms
    zero = base.DualTM.constant(q0.value, 0)
    h_local = [zero for _ in range(maximum_y_degree + 1)]
    for degree in range(min(4, maximum_y_degree) + 1):
        h_local[degree] = sum(
            (
                math.comb(power, degree)
                * h[power]
                * center ** (power - degree)
                for power in range(degree, 5)
            ),
            zero,
        )
    sqrt_h = base.formal_sqrt_series(h_local)
    inverse_sqrt_h = base.formal_reciprocal_series(sqrt_h)
    (
        rho,
        h_lower,
        ratio,
        h_s_upper,
        local_value_uppers,
        local_derivative_uppers,
        local_constant_lower,
    ) = disk_cauchy_bounds(h_local[:5], delta)
    delta_upper = base.validated.upper(delta.value.absolute_bound())
    delta_s_upper = base.validated.upper(delta.derivative.absolute_bound())
    center_upper = base.validated.upper(center.value.absolute_bound())
    center_s_upper = base.validated.upper(center.derivative.absolute_bound())
    point_upper = math.nextafter(center_upper + rho, math.inf)

    periods = []
    remainder_rows = []
    for power in range(5):
        t_power = [zero for _ in range(maximum_y_degree + 1)]
        for degree in range(min(power, maximum_y_degree) + 1):
            t_power[degree] = math.comb(power, degree) * center ** (power - degree)
        g = [zero for _ in range(maximum_y_degree + 1)]
        for degree in range(maximum_y_degree + 1):
            g[degree] = sum(
                (
                    t_power[index] * inverse_sqrt_h[degree - index]
                    for index in range(degree + 1)
                ),
                zero,
            )
        period = zero
        for term in range(series_terms + 1):
            period += (
                math.comb(2 * term, term)
                * g[2 * term]
                * (delta / 16) ** term
            )
        period *= acb(0, 2) * base.arb.pi()

        base_bound = point_upper**power / math.sqrt(h_lower)
        derivative_bound = (
            (
                0.0
                if power == 0
                else power
                * point_upper ** (power - 1)
                * center_s_upper
                / math.sqrt(h_lower)
            )
            + 0.5 * point_upper**power * h_s_upper / h_lower**1.5
        )
        value_tail = (
            2.0
            * math.pi
            * base_bound
            * ratio ** (series_terms + 1)
            / (1.0 - ratio)
        )
        derivative_tail = 2.0 * math.pi * (
            derivative_bound
            * ratio ** (series_terms + 1)
            / (1.0 - ratio)
            + base_bound
            * delta_s_upper
            / (4.0 * rho**2)
            * ratio**series_terms
            * ((series_terms + 1) - series_terms * ratio)
            / (1.0 - ratio) ** 2
        )
        periods.append(
            base.DualTM(
                base.tm_with_extra_remainder(period.value, value_tail),
                base.tm_with_extra_remainder(period.derivative, derivative_tail),
            )
        )
        remainder_rows.append(
            {
                "period_power": power,
                "value_Cauchy_tail_upper": base.outward(value_tail),
                "derivative_Cauchy_tail_upper": base.outward(derivative_tail),
                "base_Cauchy_bound_upper": base.outward(base_bound),
                "derivative_Cauchy_bound_upper": base.outward(derivative_bound),
            }
        )
    return periods, {
        "series_terms": series_terms,
        "maximum_y_degree": maximum_y_degree,
        "Cauchy_radius": rho,
        "Cauchy_domain_geometry": "closed complex disk",
        "Cauchy_quartic_bound_method": "constant-lower-minus-polynomial-disk-majorant",
        "quartic_absolute_lower_on_Cauchy_disk": h_lower,
        "nodal_series_ratio_upper": base.outward(ratio),
        "delta_absolute_upper": delta_upper,
        "delta_derivative_absolute_upper": delta_s_upper,
        "quartic_local_coefficient_absolute_uppers": local_value_uppers,
        "quartic_local_constant_absolute_lower": local_constant_lower,
        "quartic_variation_majorant_upper": math.nextafter(
            local_constant_lower - h_lower, math.inf
        ),
        "quartic_local_derivative_coefficient_absolute_uppers": local_derivative_uppers,
        "quartic_derivative_absolute_upper_on_Cauchy_disk": base.outward(h_s_upper),
        "period_remainders": remainder_rows,
    }


def direction_tail(*args: object, **kwargs: object):
    original = base.period_models
    try:
        base.period_models = period_models
        return base.direction_tail(*args, **kwargs)
    finally:
        base.period_models = original
