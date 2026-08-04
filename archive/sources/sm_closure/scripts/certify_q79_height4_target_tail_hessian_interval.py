from __future__ import annotations

import argparse
import hashlib
import json
import math
from dataclasses import dataclass
from pathlib import Path

import numpy as np
from flint import acb, acb_mat, arb, ctx

import certify_q79_height4_dynamic_target_full_residue_interval as dynamic
import certify_q79_height4_target_main_hessian_interval as main_hessian
import certify_q79_height4_tight_target_full_residue_interval as tight
import certify_q79_selected_alignment_E32_handle_combination_interval as handle
import certify_q79_selected_alignment_single_E32_thimble_nodal_factor as nodal
import certify_q79_selected_alignment_single_E32_thimble_tail_interval as tail
import certify_q79_selected_side_beta_defect_transport as validated


ROOT = Path(__file__).resolve().parents[1]
PROBE = main_hessian.PROBE
VALIDATED = main_hessian.VALIDATED
OUTPUT_DIRECTORY = VALIDATED / "hessian"
A135 = (
    PROBE.parent
    / "selected_alignment_height4_E32_thimble_regular_singular_reduction.packet.json"
)
A378 = main_hessian.A378
ARTIFACT = "A381"


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


def complex_value(value: dict[str, str]) -> complex:
    return complex(float(value["real"]), float(value["imaginary"]))


def output_paths(index: int) -> dict[str, Path]:
    canonical = tight.canonical_paths(index)
    stem = f"d{index:03d}.tailH"
    return {
        "main": canonical["main"],
        "tail": canonical["tail"],
        "output": OUTPUT_DIRECTORY / f"{stem}.interval.json",
        "note": ROOT
        / "proof_corpus"
        / f"MTT_q79HeightFourD{index:03d}TailHessianInterval_A381_v1.md",
    }


def outward(value: float) -> float:
    return math.nextafter(value * (1.0 + 4.0e-15) + 1.0e-300, math.inf)


def tm_with_extra_remainder(value: TM, extra: float) -> TM:
    return value.copy_with_remainder(
        value.remainder + arb(format(outward(extra), ".17g"))
    )


def tm_sqrt(value: TM) -> TM:
    if validated.lower(abs(value.coefficients[0])) <= 0.0:
        raise ZeroDivisionError("Taylor square-root center contains zero")
    coefficients = [acb(0) for _ in range(value.order + 1)]
    coefficients[0] = value.coefficients[0].sqrt()
    for degree in range(1, value.order + 1):
        convolution = sum(
            (
                coefficients[index] * coefficients[degree - index]
                for index in range(1, degree)
            ),
            acb(0),
        )
        coefficients[degree] = (
            value.coefficients[degree] - convolution
        ) / (acb(2) * coefficients[0])
    candidate = TM(coefficients, value.radius)
    residual = value - candidate * candidate
    residual_upper = validated.upper(residual.absolute_bound())
    lower_candidate = candidate.absolute_lower()
    if lower_candidate <= 0.0 or residual_upper >= lower_candidate**2:
        raise ArithmeticError(
            "Taylor square-root residual does not isolate a branch: "
            f"residual={residual_upper:.6e}, lower={lower_candidate:.6e}"
        )
    correction = lower_candidate - math.sqrt(
        lower_candidate**2 - residual_upper
    )
    return candidate.copy_with_remainder(arb(format(outward(correction), ".17g")))


@dataclass(frozen=True)
class DualTM:
    value: TM
    derivative: TM

    @classmethod
    def constant(cls, prototype: TM, value: object, derivative: object = 0) -> "DualTM":
        return cls(prototype.coerce(value), prototype.coerce(derivative))

    def coerce(self, other: object) -> "DualTM":
        if isinstance(other, DualTM):
            return other
        return self.constant(self.value, other)

    def __neg__(self) -> "DualTM":
        return DualTM(-self.value, -self.derivative)

    def __add__(self, other: object) -> "DualTM":
        right = self.coerce(other)
        return DualTM(
            self.value + right.value,
            self.derivative + right.derivative,
        )

    def __radd__(self, other: object) -> "DualTM":
        return self + other

    def __sub__(self, other: object) -> "DualTM":
        return self + (-self.coerce(other))

    def __rsub__(self, other: object) -> "DualTM":
        return self.coerce(other) - self

    def __mul__(self, other: object) -> "DualTM":
        right = self.coerce(other)
        return DualTM(
            self.value * right.value,
            self.derivative * right.value + self.value * right.derivative,
        )

    def __rmul__(self, other: object) -> "DualTM":
        return self * other

    def reciprocal(self) -> "DualTM":
        inverse = self.value.reciprocal()
        return DualTM(inverse, -self.derivative * inverse**2)

    def __truediv__(self, other: object) -> "DualTM":
        return self * self.coerce(other).reciprocal()

    def __rtruediv__(self, other: object) -> "DualTM":
        return self.coerce(other) / self

    def __pow__(self, power: int) -> "DualTM":
        if power < 0:
            return self.reciprocal() ** (-power)
        result = self.constant(self.value, 1)
        factor = self
        exponent = power
        while exponent:
            if exponent & 1:
                result = result * factor
            exponent >>= 1
            if exponent:
                factor = factor * factor
        return result


def dual_sqrt(value: DualTM) -> DualTM:
    root = tm_sqrt(value.value)
    return DualTM(root, value.derivative / (acb(2) * root))


def polynomial(coefficients: list[acb], point: acb) -> acb:
    result = acb(0)
    for coefficient in reversed(coefficients):
        result = result * point + coefficient
    return result


def derivative_coefficients(coefficients: list[acb]) -> list[acb]:
    return [acb(index) * coefficients[index] for index in range(1, len(coefficients))]


def node_directional_derivative(
    system: validated.SelectedQ79IntervalSystem,
    node_parameter: acb,
    node_root: acb,
    selected_direction: int,
) -> tuple[acb, acb, dict]:
    a_value, b_value, line, line_w = system.ab_line_data(node_parameter)
    elliptic = [a_value, b_value, acb(1)]
    line_s = validated.matrix_vector(
        system.alignment * system.generators[selected_direction], elliptic
    )
    f_coefficients, f_w = validated.aligned_coefficients_and_derivative(
        system.evaluator.tables["F6"], line, line_w, chart=system.line_chart
    )
    _same_f, f_s = validated.aligned_coefficients_and_derivative(
        system.evaluator.tables["F6"], line, line_s, chart=system.line_chart
    )
    f_t = derivative_coefficients(f_coefficients)
    f_tt = derivative_coefficients(f_t)
    f_tw = derivative_coefficients(f_w)
    f_ts = derivative_coefficients(f_s)
    jacobian = acb_mat(
        [
            [acb(0, 1) * polynomial(f_w, node_root), polynomial(f_t, node_root)],
            [acb(0, 1) * polynomial(f_tw, node_root), polynomial(f_tt, node_root)],
        ]
    )
    right = acb_mat(
        [
            [-polynomial(f_s, node_root)],
            [-polynomial(f_ts, node_root)],
        ]
    )
    if validated.lower(abs(jacobian.det())) <= 0.0:
        raise ZeroDivisionError("node deformation Jacobian contains zero")
    solved = jacobian.solve(right)
    parameter_s = solved[0, 0]
    root_s = solved[1, 0]
    residual = jacobian * solved - right
    return parameter_s, root_s, {
        "direction_zero_based": selected_direction,
        "node_parameter_derivative": validated.encoded_acb(parameter_s),
        "node_root_derivative": validated.encoded_acb(root_s),
        "node_deformation_jacobian_determinant_absolute_lower": validated.lower(
            abs(jacobian.det())
        ),
        "node_deformation_residual_absolute_upper": max(
            validated.upper(abs(residual[row, 0])) for row in range(2)
        ),
    }


def factor_derivative_models(
    system: validated.SelectedQ79IntervalSystem,
    factor_models: list[TM],
    node_parameter: acb,
    parameter_s: acb,
    selected_direction: int,
    *,
    epsilon: float,
    order: int,
) -> tuple[list[TM], list[DualTM], list[DualTM], dict]:
    center_x = epsilon / 2.0
    radius = arb(format(epsilon / 2.0, ".17g"))
    a_model, b_model, elliptic_diagnostics = tail.validated_ab_models_from_node_path(
        system, node_parameter, center_x, radius, order
    )
    prototype = a_model
    one = prototype.constant(1, order, radius)
    zero = prototype.constant(0, order, radius)
    one_minus_center = acb(format(1.0 - center_x, ".17g"))
    physical_center_x = acb(1) - one_minus_center
    x_model = TM(
        [physical_center_x, acb(1)]
        + [acb(0) for _ in range(order - 1)],
        radius,
    )
    one_minus_x = one - x_model
    a_w = acb(2) * system.period_length * b_model
    b_w = system.period_length * (acb(3) * a_model**2 - 1)
    a_s = acb(0, 1) * a_w * parameter_s * one_minus_x
    b_s = acb(0, 1) * b_w * parameter_s * one_minus_x
    elliptic = [a_model, b_model, one]
    elliptic_s = [a_s, b_s, zero]
    line = validated.tm_matrix_vector(system.alignment, elliptic)
    line_s = [
        left + right
        for left, right in zip(
            validated.tm_matrix_vector(
                system.alignment * system.generators[selected_direction], elliptic
            ),
            validated.tm_matrix_vector(system.alignment, elliptic_s),
        )
    ]
    f_models, f_s_models = validated.aligned_tm_coefficients_and_derivative(
        system.evaluator.tables["F6"], line, line_s, chart=system.line_chart
    )
    factor_jacobian = tail.factor_jacobian_models(factor_models)
    solved, solve_neumann, solve_error = validated.tm_matrix_solve(
        factor_jacobian, [[value] for value in f_s_models]
    )
    factor_s = [solved[index][0] for index in range(7)]
    factors = [
        DualTM(value, derivative)
        for value, derivative in zip(factor_models, factor_s)
    ]
    elliptic_dual = [
        DualTM(a_model, a_s),
        DualTM(b_model, b_s),
        DualTM(one, zero),
    ]
    return factor_s, factors, elliptic_dual, {
        "factor_derivative_solve_neumann_norm": solve_neumann,
        "factor_derivative_solution_remainder": solve_error,
        "declared_center_x": center_x,
        "physical_center_x_from_selected_parameter_decimal": str(
            physical_center_x.real
        ),
        "endpoint_coordinate_sliver_width_upper": validated.upper(
            abs(physical_center_x - acb(format(center_x, ".17g")))
        ),
        **elliptic_diagnostics,
    }


def formal_sqrt_series(values: list[DualTM]) -> list[DualTM]:
    result = [DualTM.constant(values[0].value, 0) for _ in values]
    result[0] = dual_sqrt(values[0])
    for degree in range(1, len(values)):
        convolution = sum(
            (
                result[index] * result[degree - index]
                for index in range(1, degree)
            ),
            DualTM.constant(values[0].value, 0),
        )
        result[degree] = (values[degree] - convolution) / (2 * result[0])
    return result


def formal_reciprocal_series(values: list[DualTM]) -> list[DualTM]:
    result = [DualTM.constant(values[0].value, 0) for _ in values]
    result[0] = 1 / values[0]
    for degree in range(1, len(values)):
        convolution = sum(
            (
                values[index] * result[degree - index]
                for index in range(1, degree + 1)
            ),
            DualTM.constant(values[0].value, 0),
        )
        result[degree] = -convolution / values[0]
    return result


def evaluate_dual_polynomial(values: list[DualTM], point: DualTM) -> DualTM:
    result = DualTM.constant(point.value, 0)
    for value in reversed(values):
        result = result * point + value
    return result


def cauchy_radius(
    h: list[DualTM],
    center: DualTM,
    delta: DualTM,
) -> tuple[float, float, float, DualTM]:
    for exponent in range(0, 30):
        rho = 0.5 / (2**exponent)
        square = acb(arb(0, format(rho, ".17g")), arb(0, format(rho, ".17g")))
        point = center + square
        h_on_disk = evaluate_dual_polynomial(h, point)
        h_lower = h_on_disk.value.absolute_lower()
        delta_upper = validated.upper(delta.value.absolute_bound())
        ratio = delta_upper / (4.0 * rho**2)
        if h_lower > 0.0 and ratio < 0.5:
            return rho, h_lower, ratio, h_on_disk
    raise ArithmeticError("no common Cauchy disk separates the nodal quartic")


def period_models(
    factors: list[DualTM],
    *,
    series_terms: int,
) -> tuple[list[DualTM], dict]:
    q0, q1, *h = factors
    center = -q1 / 2
    delta = q1**2 - 4 * q0
    maximum_y_degree = 2 * series_terms
    zero = DualTM.constant(q0.value, 0)
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
    sqrt_h = formal_sqrt_series(h_local)
    inverse_sqrt_h = formal_reciprocal_series(sqrt_h)
    rho, h_lower, ratio, h_on_disk = cauchy_radius(h, center, delta)
    delta_upper = validated.upper(delta.value.absolute_bound())
    delta_s_upper = validated.upper(delta.derivative.absolute_bound())
    center_upper = validated.upper(center.value.absolute_bound())
    center_s_upper = validated.upper(center.derivative.absolute_bound())
    h_s_upper = validated.upper(h_on_disk.derivative.absolute_bound())
    point_upper = center_upper + math.sqrt(2.0) * rho

    periods = []
    remainder_rows = []
    for power in range(5):
        t_power = [zero for _ in range(maximum_y_degree + 1)]
        for degree in range(min(power, maximum_y_degree) + 1):
            t_power[degree] = (
                math.comb(power, degree) * center ** (power - degree)
            )
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
        period *= acb(0, arb(2) * arb.pi())

        base_bound = point_upper**power / math.sqrt(h_lower)
        derivative_bound = (
            (0.0 if power == 0 else power * point_upper ** (power - 1) * center_s_upper / math.sqrt(h_lower))
            + 0.5
            * point_upper**power
            * h_s_upper
            / h_lower ** 1.5
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
            DualTM(
                tm_with_extra_remainder(period.value, value_tail),
                tm_with_extra_remainder(period.derivative, derivative_tail),
            )
        )
        remainder_rows.append(
            {
                "period_power": power,
                "value_Cauchy_tail_upper": outward(value_tail),
                "derivative_Cauchy_tail_upper": outward(derivative_tail),
                "base_Cauchy_bound_upper": outward(base_bound),
                "derivative_Cauchy_bound_upper": outward(derivative_bound),
            }
        )
    return periods, {
        "series_terms": series_terms,
        "maximum_y_degree": maximum_y_degree,
        "Cauchy_radius": rho,
        "quartic_absolute_lower_on_Cauchy_disk": h_lower,
        "nodal_series_ratio_upper": outward(ratio),
        "delta_absolute_upper": delta_upper,
        "delta_derivative_absolute_upper": delta_s_upper,
        "period_remainders": remainder_rows,
    }


def matrix_dual_vector(matrix: acb_mat, values: list[DualTM]) -> list[DualTM]:
    zero = DualTM.constant(values[0].value, 0)
    return [
        sum(
            (matrix[row, column] * values[column] for column in range(len(values))),
            zero,
        )
        for row in range(matrix.nrows())
    ]


def residue_dual_rows(
    system: validated.SelectedQ79IntervalSystem,
    elliptic: list[DualTM],
    selected_direction: int,
) -> list[tuple[DualTM, DualTM]]:
    line_value = matrix_dual_vector(system.alignment, elliptic)
    explicit_line_s = matrix_dual_vector(
        system.alignment * system.generators[selected_direction],
        [DualTM(value.value, value.value.constant(0, value.value.order, value.value.radius)) for value in elliptic],
    )
    line = [
        DualTM(value.value, value.derivative + explicit.derivative + explicit.value)
        for value, explicit in zip(line_value, explicit_line_s)
    ]
    rows = []
    for generator in system.generators:
        variation_value = matrix_dual_vector(system.alignment * generator, elliptic)
        explicit_variation_s = matrix_dual_vector(
            system.alignment * system.generators[selected_direction] * generator,
            [DualTM(value.value, value.value.constant(0, value.value.order, value.value.radius)) for value in elliptic],
        )
        variation = [
            DualTM(value.value, value.derivative + explicit.value)
            for value, explicit in zip(variation_value, explicit_variation_s)
        ]
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
            (
                system.period_length * constant,
                system.period_length * linear,
            )
        )
    return rows


def integrate_symmetric(model: TM, endpoint_sliver: float = 0.0) -> acb:
    radius = model.radius
    result = acb(0)
    for degree in range(0, model.order + 1, 2):
        result += (
            acb(2)
            * model.coefficients[degree]
            * acb(radius ** (degree + 1))
            / acb(degree + 1)
        )
    error = arb(2) * radius * model.remainder
    error_upper = validated.upper(error) + 2.0 * endpoint_sliver * validated.upper(
        model.absolute_bound()
    )
    return result + acb(
        arb(0, format(outward(error_upper), ".17g")),
        arb(0, format(outward(error_upper), ".17g")),
    )


def evaluate_at_series_center(model: TM) -> acb:
    error = validated.upper(model.remainder)
    return model.coefficients[0] + acb(
        arb(0, format(outward(error), ".17g")),
        arb(0, format(outward(error), ".17g")),
    )


def period_connection_identity(
    system: validated.SelectedQ79IntervalSystem,
    periods: list[DualTM],
    node_parameter: acb,
    parameter_s: acb,
    selected_direction: int,
    epsilon: float,
) -> dict:
    center_x = epsilon / 2.0
    parameter = node_parameter * acb(format(1.0 - center_x, ".17g"))
    a_value, b_value, line, line_w = system.ab_line_data(parameter)
    elliptic = [a_value, b_value, acb(1)]
    explicit_line_s = validated.matrix_vector(
        system.alignment * system.generators[selected_direction], elliptic
    )
    line_total_s = [
        explicit
        + acb(0, 1)
        * derivative
        * parameter_s
        * acb(format(1.0 - center_x, ".17g"))
        for explicit, derivative in zip(explicit_line_s, line_w)
    ]
    f_coefficients, f_s = validated.aligned_coefficients_and_derivative(
        system.evaluator.tables["F6"],
        line,
        line_total_s,
        chart=system.line_chart,
    )
    connection_s, _exact_terms = system.reduction_solution(f_coefficients, f_s)
    values = [evaluate_at_series_center(value.value) for value in periods]
    derivatives = [
        evaluate_at_series_center(value.derivative) for value in periods
    ]
    predicted = [
        sum(
            (connection_s[row][column] * values[column] for column in range(5)),
            acb(0),
        )
        for row in range(5)
    ]
    overlap = [
        derivatives[row].overlaps(predicted[row]) for row in range(5)
    ]
    differences = [
        validated.upper(abs(derivatives[row] - predicted[row]))
        for row in range(5)
    ]
    if not all(overlap):
        raise AssertionError(
            "differentiated Frobenius periods do not satisfy D_s P=C_s P: "
            f"failed_rows={[index for index, value in enumerate(overlap) if not value]}, "
            f"differences={differences}, "
            f"derivative_radii={[validated.radius_upper(value) for value in derivatives]}, "
            f"predicted_radii={[validated.radius_upper(value) for value in predicted]}"
        )
    return {
        "period_connection_identity": "D_s P=C_s P",
        "period_connection_identity_overlaps_all_five_rows": True,
        "maximum_period_connection_interval_difference_upper": max(differences),
    }


def direction_tail(
    system: validated.SelectedQ79IntervalSystem,
    factor_models: list[TM],
    node_parameter: acb,
    node_root: acb,
    selected_direction: int,
    *,
    epsilon: float,
    order: int,
    series_terms: int,
) -> tuple[list[acb], list[acb], dict]:
    parameter_s, _root_s, node_diagnostics = node_directional_derivative(
        system, node_parameter, node_root, selected_direction
    )
    _factor_s, factors, elliptic, factor_diagnostics = factor_derivative_models(
        system,
        factor_models,
        node_parameter,
        parameter_s,
        selected_direction,
        epsilon=epsilon,
        order=order,
    )
    periods, period_diagnostics = period_models(
        factors, series_terms=series_terms
    )
    connection_identity = period_connection_identity(
        system,
        periods,
        node_parameter,
        parameter_s,
        selected_direction,
        epsilon,
    )
    residues = residue_dual_rows(system, elliptic, selected_direction)
    prototype = factors[0].value
    path = DualTM.constant(
        prototype,
        acb(0, 1) * node_parameter,
        acb(0, 1) * parameter_s,
    )
    integrands = [
        path * (constant * periods[0] + linear * periods[1])
        for constant, linear in residues
    ]
    endpoint_sliver = float(
        factor_diagnostics["endpoint_coordinate_sliver_width_upper"]
    )
    values = [
        integrate_symmetric(value.value, endpoint_sliver) for value in integrands
    ]
    derivatives = [
        integrate_symmetric(value.derivative, endpoint_sliver)
        for value in integrands
    ]
    return values, derivatives, {
        **node_diagnostics,
        **factor_diagnostics,
        **period_diagnostics,
        **connection_identity,
        "maximum_integrand_value_remainder_upper": max(
            validated.upper(value.value.remainder) for value in integrands
        ),
        "maximum_integrand_derivative_remainder_upper": max(
            validated.upper(value.derivative.remainder) for value in integrands
        ),
    }


def execute(arguments: argparse.Namespace) -> dict:
    paths = output_paths(arguments.index)
    main_packet = load(paths["main"])
    tail_packet = load(paths["tail"])
    system, rank, row = main_hessian.selected_system(arguments.index, arguments.dps)
    epsilon = float(main_packet["selected_target"]["endpoint_cutoff_epsilon"])
    if abs(epsilon - arguments.epsilon) > 1.0e-18:
        raise ValueError("requested epsilon differs from the canonical main/tail splice")
    node_parameter = validated.decoded_acb(
        main_packet["certified_node"]["parameter_ball"]
    )
    node_root = validated.decoded_acb(
        main_packet["certified_node"]["double_root_ball"]
    )
    factor_models, factor_disk = tail.factor_taylor_models(
        system,
        node_parameter,
        node_root,
        epsilon=epsilon,
        order=arguments.order,
    )
    ordinary_by_direction = []
    hessian_columns = []
    diagnostics = []
    for selected_direction in range(8):
        values, derivatives, row_diagnostics = direction_tail(
            system,
            factor_models,
            node_parameter,
            node_root,
            selected_direction,
            epsilon=epsilon,
            order=arguments.order,
            series_terms=arguments.series_terms,
        )
        ordinary_by_direction.append(values)
        hessian_columns.append(derivatives)
        diagnostics.append(row_diagnostics)
        print(
            f"d{arguments.index:03d} tail Hessian direction="
            f"{selected_direction + 1}/8 radius="
            f"{max(validated.radius_upper(value) for value in derivatives):.3e}",
            flush=True,
        )

    ordinary = ordinary_by_direction[0]
    inter_direction_overlap = []
    for residue_index in range(8):
        inter_direction_overlap.append(
            all(
                ordinary[residue_index].overlaps(values[residue_index])
                for values in ordinary_by_direction[1:]
            )
        )
    if not all(inter_direction_overlap):
        raise AssertionError("ordinary Frobenius tail depends on deformation label")

    canonical_centers = np.asarray(
        [
            complex_value(value)
            for value in tail_packet["all_eight_endpoint_tails"][
                "interval_centers"
            ]
        ],
        dtype=np.complex128,
    )
    canonical_radii = np.asarray(
        tail_packet["all_eight_endpoint_tails"]["interval_radius_uppers"],
        dtype=np.float64,
    )
    ordinary_centers = np.asarray(
        [validated.midpoint(value) for value in ordinary], dtype=np.complex128
    )
    ordinary_radii = np.asarray(
        [validated.radius_upper(value) for value in ordinary], dtype=np.float64
    )
    plus = np.max(abs(ordinary_centers - canonical_centers))
    minus = np.max(abs(-ordinary_centers - canonical_centers))
    branch_sign = 1 if plus <= minus else -1
    ordinary_centers *= branch_sign
    ordinary = [acb(branch_sign) * value for value in ordinary]
    hessian_columns = [
        [acb(branch_sign) * value for value in column]
        for column in hessian_columns
    ]
    differences = abs(ordinary_centers - canonical_centers)
    overlap = differences <= ordinary_radii + canonical_radii
    if not bool(np.all(overlap)):
        raise AssertionError(
            "coefficientwise Frobenius tail does not overlap canonical tail"
        )

    hessian = np.empty((8, 8), dtype=np.complex128)
    hessian_radii = np.empty((8, 8), dtype=np.float64)
    for column in range(8):
        for residue_index in range(8):
            hessian[residue_index, column] = validated.midpoint(
                hessian_columns[column][residue_index]
            )
            hessian_radii[residue_index, column] = validated.radius_upper(
                hessian_columns[column][residue_index]
            )

    payload = {
        "schema": "MTTQ79HeightFourTargetTailHessianInterval.v1",
        "status": "TARGET_LOG_FREE_FROBENIUS_TAIL_AND_COMPLEX_8_BY_8_HESSIAN_INTERVAL_CERTIFIED",
        "artifact": ARTIFACT,
        "selected_target": {
            "distinguished_index": arguments.index,
            "A219_contribution_rank": rank,
            "root_id": row["root_id"],
            "line_chart": dynamic.CHART,
            "signed_chain_coefficient": int(row["signed_coefficient"]),
            "endpoint_cutoff_epsilon": epsilon,
            "Frobenius_square_root_branch_sign_against_canonical_tail": branch_sign,
        },
        "tail_residue_rows": [
            {
                "residue_index_zero_based": index,
                "interval": handle.complex_interval(ordinary[index]),
                "interval_center": pair(ordinary_centers[index]),
                "component_radius_upper": float(ordinary_radii[index]),
                "canonical_center_difference": float(differences[index]),
                "canonical_intervals_overlap": bool(overlap[index]),
            }
            for index in range(8)
        ],
        "complex_tail_Hessian_8_by_8": [
            [
                {
                    "row_zero_based": residue_index,
                    "column_zero_based": column,
                    "interval_center": pair(hessian[residue_index, column]),
                    "component_radius_upper": float(
                        hessian_radii[residue_index, column]
                    ),
                }
                for column in range(8)
            ]
            for residue_index in range(8)
        ],
        "Frobenius_method": {
            "identity": (
                "P_k(x)=2*pi*i*sum_{m>=0} binom(2m,m) "
                "g_{k,2m}(x)*(Delta(x)/16)^m"
            ),
            "moving_coordinate": "w=w_c(s)*(1-x)",
            "node_and_factor_differentiation": (
                "differentiate F=F_t=0 for (w_c,t_c), then solve "
                "D_factorization(q,h)*(q_s,h_s)=F_s"
            ),
            "finite_series_terms": arguments.series_terms,
            "Cauchy_remainder_certified": True,
            "factor_disk": factor_disk,
            "direction_diagnostics": diagnostics,
        },
        "summary": {
            "certified_tail_rows": 8,
            "certified_tail_Hessian_entries": 64,
            "maximum_tail_row_component_radius_upper": float(
                np.max(ordinary_radii)
            ),
            "maximum_tail_Hessian_component_radius_upper": float(
                np.max(hessian_radii)
            ),
            "tail_Hessian_product_box_frobenius_radius_upper": float(
                np.linalg.norm(hessian_radii)
            ),
            "all_canonical_tail_intervals_overlap": bool(np.all(overlap)),
            "maximum_canonical_tail_center_difference": float(
                np.max(differences)
            ),
            "ordinary_rows_overlap_across_all_eight_dual_executions": all(
                inter_direction_overlap
            ),
        },
        "authority": {
            name: {"path": relative(path), "sha256": sha256(path)}
            for name, path in {
                "canonical_main_interval": paths["main"],
                "canonical_tail_interval": paths["tail"],
                "A135_log_free_Frobenius_theorem": A135,
                "A378_Hessian_integrand_source": A378,
                "tail_Hensel_engine": Path(tail.__file__).resolve(),
                "builder_source": Path(__file__).resolve(),
            }.items()
        },
        "strict_scope": {
            "observed_SM_values_used": False,
            "A135_log_free_branch_used": True,
            "moving_node_implicit_derivative_interval_closed": True,
            "moving_Hensel_factor_derivative_interval_closed": True,
            "automatic_finite_cutoff_exactness_used": True,
            "Cauchy_series_remainder_closed": True,
            "target_Frobenius_tail_Hessian_interval_closed": True,
            "target_main_Hessian_interval_closed": False,
            "target_full_Hessian_interval_closed": False,
            "full_76_target_chain_Hessian_interval_closed": False,
            "interval_Newton_existence_and_uniqueness_closed": False,
            "covariant_zero_proved": False,
            "full_SM_closure_proved": False,
        },
        "next_required_artifact": (
            "splice this tail Hessian to the matching A380 main Hessian and "
            "apply the preselected thimble orientation and chain coefficient"
        ),
    }
    dump(paths["output"], payload)
    paths["note"].write_text(
        f"# MTT q79 Height-Four d{arguments.index:03d} Tail Hessian Interval (A381) v1\n\n"
        "A381 differentiates the selected node and Hensel factor in the moving "
        "coordinate `w=w_c(s)(1-x)`. The vanishing-cycle periods are integrated "
        "with the log-free A135 coefficient formula, and the omitted infinite "
        "series is enclosed by a common Cauchy disk.\n\n"
        f"The maximum tail-Hessian component radius is "
        f"`{np.max(hessian_radii):.12g}`. The independently recomputed ordinary "
        "tail overlaps all eight canonical tail intervals.\n\n"
        "This is the endpoint derivative certificate; it does not include the "
        "matching main path or promote a full-chain Jacobian by itself.\n",
        encoding="utf-8",
    )
    print(f"wrote {relative(paths['output'])}")
    print(f"wrote {relative(paths['note'])}")
    print(json.dumps(payload["summary"], indent=2))
    return payload


def parser() -> argparse.ArgumentParser:
    value = argparse.ArgumentParser()
    value.add_argument("--index", type=int, required=True)
    value.add_argument("--epsilon", type=float, default=1.0e-5)
    value.add_argument("--dps", type=int, default=100)
    value.add_argument("--order", type=int, default=32)
    value.add_argument("--series-terms", type=int, default=10)
    return value


def main() -> int:
    arguments = parser().parse_args()
    if not 1 <= arguments.index <= 90:
        raise ValueError("index must lie in [1,90]")
    if not 0.0 < arguments.epsilon < 0.01:
        raise ValueError("epsilon must lie in (0,0.01)")
    if not 2 <= arguments.series_terms <= arguments.order // 2:
        raise ValueError("series terms must lie in [2, order/2]")
    ctx.dps = arguments.dps
    a135 = load(A135)
    if not a135["local_theorem"]["proved_for_all_selected_thimbles"]:
        raise AssertionError("A381 requires the selected A135 log-free theorem")
    execute(arguments)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
