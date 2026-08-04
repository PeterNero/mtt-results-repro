from __future__ import annotations

import argparse
import json
import math
import tempfile
import types
from dataclasses import dataclass
from pathlib import Path

import numpy as np
from flint import acb, acb_mat, acb_series, arb, ctx
from scipy.linalg import expm

import compute_q79genus2normalfunction as normal_function_module
from analyze_q79_picard_lefschetz_wall import (
    complex_matrix as floating_complex_matrix,
    complex_value,
)
from compute_q79genus2normalfunction import Q79DeltaNormalFunction
from explore_q79_pgl3_beta_zero import PGL3BetaEvaluator


ROOT = Path(__file__).resolve().parents[1]
DIRECTORY = (
    ROOT
    / "candidate_data"
    / "selected_q79genus2delignebetaperiodandintegralbranchexecution"
)
A124 = DIRECTORY / "pgl3_transverse_simple_node_and_transport_pl_jump.packet.json"
WALL = DIRECTORY / "pgl3_transverse_simple_node.interval.packet.json"
SOURCE = DIRECTORY / "pgl3_projective_ychart_broyden_04.exploratory.json"
BASE_LIFT = DIRECTORY / "pgl3_selected_side_base_lift.interval.packet.json"
DEFAULT_OUTPUT = (
    DIRECTORY / "pgl3_selected_side_beta.local_lower.defect_interval.packet.json"
)
DEFAULT_CHECKPOINT = (
    DIRECTORY
    / "pgl3_selected_side_beta.local_lower.defect_interval.checkpoint.json"
)


def load(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def dump(path: Path, value: dict) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(value, indent=2, sort_keys=True) + "\n", encoding="utf-8")


def atomic_dump(path: Path, value: dict) -> None:
    temporary = path.with_suffix(path.suffix + ".tmp")
    dump(temporary, value)
    temporary.replace(path)


def encoded_acb(value: acb) -> dict[str, str]:
    return {"real": str(value.real), "imaginary": str(value.imag)}


def decoded_acb(value: dict[str, str]) -> acb:
    return acb(arb(value["real"]), arb(value["imaginary"]))


def encoded_matrix(matrix: acb_mat) -> list[list[dict[str, str]]]:
    return [
        [encoded_acb(matrix[row, column]) for column in range(matrix.ncols())]
        for row in range(matrix.nrows())
    ]


def decoded_matrix(value: list[list[dict[str, str]]]) -> acb_mat:
    return acb_mat([[decoded_acb(entry) for entry in row] for row in value])


def exact_acb(value: dict) -> acb:
    if "r" in value:
        return acb(value["r"], value["i"])
    return acb(value["real"], value["imaginary"])


def midpoint(value: acb) -> complex:
    return complex(float(value.real.mid()), float(value.imag.mid()))


def lower(value: arb) -> float:
    return math.nextafter(float(value.lower()), -math.inf)


def upper(value: arb) -> float:
    return math.nextafter(float(value.upper()), math.inf)


def radius_upper(value: acb) -> float:
    return upper(value.rad())


def complex_interval(value: acb) -> dict[str, dict[str, str]]:
    return {
        "real": {
            "lower": format(lower(value.real), ".17g"),
            "upper": format(upper(value.real), ".17g"),
        },
        "imaginary": {
            "lower": format(lower(value.imag), ".17g"),
            "upper": format(upper(value.imag), ".17g"),
        },
    }


def matrix_vector(matrix: acb_mat, vector: list[acb]) -> list[acb]:
    product = matrix * acb_mat([[value] for value in vector])
    return [product[index, 0] for index in range(matrix.nrows())]


def polynomial(coefficients: list[acb], value: acb) -> acb:
    result = acb(0)
    for coefficient in reversed(coefficients):
        result = result * value + coefficient
    return result


def monomial_with_derivative(
    values: list[acb], derivatives: list[acb], powers: list[int]
) -> tuple[acb, acb]:
    value = acb(1)
    for coordinate, power in zip(values, powers):
        value *= coordinate**power
    derivative = acb(0)
    for selected, power in enumerate(powers):
        if power == 0:
            continue
        term = acb(power) * derivatives[selected]
        for index, (coordinate, other_power) in enumerate(zip(values, powers)):
            term *= coordinate ** (other_power - int(index == selected))
        derivative += term
    return value, derivative


def aligned_coefficients_and_derivative(
    table: list[dict],
    line: list[acb],
    line_derivative: list[acb],
    *,
    chart: str,
) -> tuple[list[acb], list[acb]]:
    degree = sum(int(value) for value in table[0]["powers_xyz"])
    ascending = [acb(0) for _ in range(degree + 1)]
    derivative = [acb(0) for _ in range(degree + 1)]
    for row in table:
        x_power, y_power, z_power = [int(value) for value in row["powers_xyz"]]
        coefficient = int(row["coefficient"])
        if chart == "z":
            for index in range(z_power + 1):
                powers = [z_power - index, index, x_power + y_power]
                value, value_derivative = monomial_with_derivative(
                    line, line_derivative, powers
                )
                scalar = coefficient * (-1) ** z_power * math.comb(z_power, index)
                ascending[index + y_power] += acb(scalar) * value
                derivative[index + y_power] += acb(scalar) * value_derivative
        elif chart == "y":
            for index in range(y_power + 1):
                powers = [y_power - index, x_power + z_power, index]
                value, value_derivative = monomial_with_derivative(
                    line, line_derivative, powers
                )
                scalar = coefficient * (-1) ** y_power * math.comb(y_power, index)
                ascending[index + z_power] += acb(scalar) * value
                derivative[index + z_power] += acb(scalar) * value_derivative
        else:
            raise ValueError(f"unsupported chart {chart!r}")
    return ascending, derivative


@dataclass
class IntervalSystemDiagnostics:
    evaluation_count: int = 0
    maximum_connection_radius: float = 0.0
    maximum_source_radius: float = 0.0
    minimum_q_discriminant_absolute_lower: float = math.inf
    minimum_q_root_derivative_denominator_lower: float = math.inf
    minimum_q_sheet_value_lower: float = math.inf
    minimum_chart_scale_lower: float = math.inf
    maximum_verified_solve_neumann_norm: float = 0.0
    maximum_verified_solve_error_radius: float = 0.0


class SelectedQ79IntervalSystem:
    def __init__(self, *, dps: int, line_chart: str = "y") -> None:
        ctx.dps = dps
        if line_chart not in {"y", "z"}:
            raise ValueError("selected line chart must be y or z")
        self.line_chart = line_chart
        self.line_chart_denominator_index = 1 if line_chart == "y" else 2
        self.a124 = load(A124)
        self.wall = load(WALL)
        self.source_packet = load(SOURCE)
        self.evaluator = PGL3BetaEvaluator()
        self.alignment_0 = acb_mat(
            [
                [exact_acb(value) for value in row]
                for row in self.source_packet["final_alignment"]
            ]
        )
        direction = [
            exact_acb(value)
            for value in self.a124["search_direction"]["coordinates"]
        ]
        self.generators = [
            acb_mat(
                [
                    [
                        acb(str(complex(value).real), str(complex(value).imag))
                        for value in row
                    ]
                    for row in generator
                ]
            )
            for generator in self.evaluator.generators
        ]
        tangent = acb_mat(3, 3)
        for coefficient, generator in zip(direction, self.generators):
            tangent += coefficient * generator
        self.selected_carrier = arb(self.wall["initial_box"][0]["lower"]) - arb(
            "0.005"
        )
        self.alignment = self.alignment_0 * (self.selected_carrier * tangent).exp()
        self.tau = acb(0, 1)
        self.period_length = acb("0.5").elliptic_k() * acb(2).sqrt()
        self.period_square = self.period_length**2
        self.period_cube = self.period_length**3
        self.base = acb("0.25", "0.25")
        self.diagnostics = IntervalSystemDiagnostics()

    def ab_line_data(
        self, parameter: acb
    ) -> tuple[acb, acb, list[acb], list[acb]]:
        w_value = self.base + acb(0, 1) * parameter
        series = acb_series([w_value, acb(1)], 2).elliptic_p(self.tau)
        a_value = series[0] / self.period_square
        b_value = series[1] / (acb(2) * self.period_cube)
        da_dw = acb(2) * self.period_length * b_value
        db_dw = self.period_length * (acb(3) * a_value**2 - acb(1))
        elliptic = [a_value, b_value, acb(1)]
        elliptic_derivative = [da_dw, db_dw, acb(0)]
        line = matrix_vector(self.alignment, elliptic)
        line_derivative = matrix_vector(self.alignment, elliptic_derivative)
        self.diagnostics.minimum_chart_scale_lower = min(
            self.diagnostics.minimum_chart_scale_lower,
            lower(abs(line[self.line_chart_denominator_index])),
        )
        return a_value, b_value, line, line_derivative

    @staticmethod
    def midpoint_acb(value: acb) -> acb:
        return acb(str(value.real.mid()), str(value.imag.mid()))

    def verified_solve(
        self, matrix: acb_mat, targets: acb_mat
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
        approximate_inverse_ball = midpoint_matrix.inv()
        approximate_inverse = acb_mat(
            [
                [
                    self.midpoint_acb(approximate_inverse_ball[row, column])
                    for column in range(approximate_inverse_ball.ncols())
                ]
                for row in range(approximate_inverse_ball.nrows())
            ]
        )
        identity = acb_mat(matrix.nrows(), matrix.ncols())
        for index in range(matrix.nrows()):
            identity[index, index] = acb(1)
        neumann_error = identity - approximate_inverse * matrix
        neumann_norm = max(
            (
                sum(
                    (abs(neumann_error[row, column]) for column in range(matrix.ncols())),
                    arb(0),
                )
                for row in range(matrix.nrows())
            ),
            key=lambda value: upper(value),
        )
        neumann_upper = upper(neumann_norm)
        if not neumann_upper < 1.0:
            raise ZeroDivisionError(
                "verified midpoint inverse failed: "
                f"Neumann norm upper={neumann_upper:.6e}"
            )
        inverse_norm = max(
            (
                sum(
                    (abs(approximate_inverse[row, column]) for column in range(matrix.ncols())),
                    arb(0),
                )
                for row in range(matrix.nrows())
            ),
            key=lambda value: upper(value),
        ) / (arb(1) - neumann_norm)
        center_ball = approximate_inverse * midpoint_targets
        center = acb_mat(
            [
                [self.midpoint_acb(center_ball[row, column]) for column in range(center_ball.ncols())]
                for row in range(center_ball.nrows())
            ]
        )
        residual = targets - matrix * center
        result = acb_mat(center.nrows(), center.ncols())
        maximum_error = 0.0
        for column in range(center.ncols()):
            residual_norm = max(
                (abs(residual[row, column]) for row in range(residual.nrows())),
                key=lambda value: upper(value),
            )
            error = inverse_norm * residual_norm
            error_upper = upper(error)
            maximum_error = max(maximum_error, error_upper)
            for row in range(center.nrows()):
                result[row, column] = acb(
                    arb(str(center[row, column].real.mid()), str(error_upper)),
                    arb(str(center[row, column].imag.mid()), str(error_upper)),
                )
        self.diagnostics.maximum_verified_solve_neumann_norm = max(
            self.diagnostics.maximum_verified_solve_neumann_norm,
            neumann_upper,
        )
        self.diagnostics.maximum_verified_solve_error_radius = max(
            self.diagnostics.maximum_verified_solve_error_radius,
            maximum_error,
        )
        return result

    def reduction_solution(
        self, coefficients: list[acb], derivative: list[acb]
    ) -> tuple[list[list[acb]], list[list[acb]]]:
        polynomial_derivative = [
            acb(index) * coefficients[index] for index in range(1, 7)
        ]
        reduction = acb_mat(11, 11)
        half = acb("0.5")
        for power in range(6):
            if power:
                for index, coefficient in enumerate(coefficients):
                    reduction[index + power - 1, power] += (
                        acb(power) * coefficient
                    )
            for index, coefficient in enumerate(polynomial_derivative):
                reduction[index + power, power] -= half * coefficient
        for power in range(5):
            for index, coefficient in enumerate(coefficients):
                reduction[index + power, 6 + power] += coefficient
        targets = acb_mat(11, 5)
        for power in range(5):
            for index, coefficient in enumerate(derivative):
                targets[index + power, power] -= half * coefficient
        solved = self.verified_solve(reduction, targets)
        exact_terms = [
            [solved[index, power] for index in range(6)] for power in range(5)
        ]
        connection = [
            [solved[6 + index, power] for index in range(5)]
            for power in range(5)
        ]
        return connection, exact_terms

    def connection_source_residue(
        self, parameter: acb
    ) -> tuple[list[list[acb]], list[acb], list[list[acb]]]:
        a_value, b_value, line, line_derivative = self.ab_line_data(parameter)
        f_coefficients, f_derivative = aligned_coefficients_and_derivative(
            self.evaluator.tables["F6"],
            line,
            line_derivative,
            chart=self.line_chart,
        )
        g_coefficients, _ = aligned_coefficients_and_derivative(
            self.evaluator.tables["G3"],
            line,
            line_derivative,
            chart=self.line_chart,
        )
        q_coefficients, q_derivative = aligned_coefficients_and_derivative(
            self.evaluator.tables["Q2"],
            line,
            line_derivative,
            chart=self.line_chart,
        )
        connection, exact_terms = self.reduction_solution(
            f_coefficients, f_derivative
        )

        q0, q1, q2 = q_coefficients
        discriminant = q1**2 - acb(4) * q2 * q0
        self.diagnostics.minimum_q_discriminant_absolute_lower = min(
            self.diagnostics.minimum_q_discriminant_absolute_lower,
            lower(abs(discriminant)),
        )
        root_sum = -q1 / q2
        root_product = q0 / q2
        relation_constant = -root_product
        relation_linear = root_sum

        def pair_multiply(
            left: tuple[acb, acb], right: tuple[acb, acb]
        ) -> tuple[acb, acb]:
            quadratic = left[1] * right[1]
            return (
                left[0] * right[0] + quadratic * relation_constant,
                left[0] * right[1]
                + left[1] * right[0]
                + quadratic * relation_linear,
            )

        def pair_power(power: int) -> tuple[acb, acb]:
            result = (acb(1), acb(0))
            factor = (acb(0), acb(1))
            exponent = power
            while exponent:
                if exponent & 1:
                    result = pair_multiply(result, factor)
                exponent >>= 1
                if exponent:
                    factor = pair_multiply(factor, factor)
            return result

        def pair_reduce(coefficients: list[acb]) -> tuple[acb, acb]:
            result = (acb(0), acb(0))
            for power, coefficient in enumerate(coefficients):
                basis = pair_power(power)
                result = (
                    result[0] + coefficient * basis[0],
                    result[1] + coefficient * basis[1],
                )
            return result

        def pair_inverse(value: tuple[acb, acb]) -> tuple[acb, acb]:
            norm = (
                value[0] ** 2
                + root_sum * value[0] * value[1]
                + root_product * value[1] ** 2
            )
            self.diagnostics.minimum_q_sheet_value_lower = min(
                self.diagnostics.minimum_q_sheet_value_lower,
                lower(abs(norm)),
            )
            return (
                (value[0] + root_sum * value[1]) / norm,
                -value[1] / norm,
            )

        q_w_pair = pair_reduce(q_derivative)
        g_inverse = pair_inverse(pair_reduce(g_coefficients))
        source = [acb(0) for _ in range(5)]
        for power in range(5):
            exact_weight = pair_multiply(
                pair_reduce(exact_terms[power]), g_inverse
            )
            velocity_weight = pair_multiply(
                pair_multiply(pair_power(power), q_w_pair), g_inverse
            )
            source[power] = (
                acb(2) * exact_weight[0]
                + root_sum * exact_weight[1]
                - velocity_weight[1] / q2
            )

        residue = [[acb(0) for _ in range(5)] for _ in range(8)]
        elliptic = [a_value, b_value, acb(1)]
        for row, generator in enumerate(self.generators):
            variation = matrix_vector(self.alignment * generator, elliptic)
            if self.line_chart == "z":
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
            residue[row][0] = self.period_length * constant
            residue[row][1] = self.period_length * linear

        self.diagnostics.evaluation_count += 1
        self.diagnostics.maximum_connection_radius = max(
            self.diagnostics.maximum_connection_radius,
            max(radius_upper(value) for row in connection for value in row),
        )
        self.diagnostics.maximum_source_radius = max(
            self.diagnostics.maximum_source_radius,
            max(radius_upper(value) for value in source),
        )
        return connection, source, residue

    def full_system(
        self, parameter: acb, parameter_derivative: acb
    ) -> tuple[list[list[acb]], list[acb]]:
        connection, source, residue = self.connection_source_residue(parameter)
        matrix = [[acb(0) for _ in range(13)] for _ in range(13)]
        forcing = [acb(0) for _ in range(13)]
        displacement = acb(0, 1) * parameter_derivative
        for row in range(5):
            forcing[row] = displacement * source[row]
            for column in range(5):
                matrix[row][column] = displacement * connection[row][column]
        for row in range(8):
            for column in range(5):
                matrix[5 + row][column] = displacement * residue[row][column]
        return matrix, forcing


def as_acb(value: acb | arb | complex | float | int) -> acb:
    if isinstance(value, acb):
        return value
    if isinstance(value, arb):
        return acb(value)
    if isinstance(value, complex):
        return acb(format(value.real, ".17g"), format(value.imag, ".17g"))
    return acb(str(value))


class TaylorModel:
    """Univariate complex Taylor polynomial plus a rigorous uniform remainder."""

    def __init__(
        self,
        coefficients: list[acb],
        radius: arb,
        remainder: arb | None = None,
    ) -> None:
        self.coefficients = coefficients
        self.radius = radius
        self.remainder = arb(0) if remainder is None else remainder

    @property
    def order(self) -> int:
        return len(self.coefficients) - 1

    @classmethod
    def constant(
        cls, value: acb | arb | complex | float | int, order: int, radius: arb
    ) -> "TaylorModel":
        return cls([as_acb(value)] + [acb(0) for _ in range(order)], radius)

    def coerce(self, value: object) -> "TaylorModel":
        if isinstance(value, TaylorModel):
            if value.order != self.order or str(value.radius) != str(self.radius):
                raise ValueError("Taylor-model domains do not agree")
            return value
        return self.constant(value, self.order, self.radius)  # type: ignore[arg-type]

    def copy_with_remainder(self, remainder: arb) -> "TaylorModel":
        return TaylorModel(self.coefficients.copy(), self.radius, remainder)

    def midpoint_polynomial(self) -> "TaylorModel":
        return TaylorModel(
            [SelectedQ79IntervalSystem.midpoint_acb(value) for value in self.coefficients],
            self.radius,
        )

    def polynomial_absolute_bound(self) -> arb:
        total = arb(0)
        power = arb(1)
        for coefficient in self.coefficients:
            total += abs(coefficient) * power
            power *= self.radius
        return total

    def absolute_bound(self) -> arb:
        return self.polynomial_absolute_bound() + self.remainder

    def absolute_lower(self) -> float:
        tail = self.remainder
        power = self.radius
        for coefficient in self.coefficients[1:]:
            tail += abs(coefficient) * power
            power *= self.radius
        return math.nextafter(
            lower(abs(self.coefficients[0])) - upper(tail),
            -math.inf,
        )

    def evaluate_polynomial(self, value: arb | float) -> acb:
        argument = acb(value if isinstance(value, arb) else str(value))
        result = acb(0)
        for coefficient in reversed(self.coefficients):
            result = result * argument + coefficient
        return result

    def derivative_polynomial(self) -> "TaylorModel":
        coefficients = [
            acb(index) * self.coefficients[index]
            for index in range(1, self.order + 1)
        ] + [acb(0)]
        return TaylorModel(coefficients, self.radius)

    def __neg__(self) -> "TaylorModel":
        return TaylorModel(
            [-value for value in self.coefficients],
            self.radius,
            self.remainder,
        )

    def __add__(self, other: object) -> "TaylorModel":
        right = self.coerce(other)
        return TaylorModel(
            [left + value for left, value in zip(self.coefficients, right.coefficients)],
            self.radius,
            self.remainder + right.remainder,
        )

    def __radd__(self, other: object) -> "TaylorModel":
        return self + other

    def __sub__(self, other: object) -> "TaylorModel":
        return self + (-self.coerce(other))

    def __rsub__(self, other: object) -> "TaylorModel":
        return self.coerce(other) - self

    def __mul__(self, other: object) -> "TaylorModel":
        right = self.coerce(other)
        coefficients = [acb(0) for _ in range(self.order + 1)]
        omitted = arb(0)
        powers = [arb(1)]
        for _ in range(2 * self.order):
            powers.append(powers[-1] * self.radius)
        for left_index, left in enumerate(self.coefficients):
            for right_index, value in enumerate(right.coefficients):
                degree = left_index + right_index
                if degree <= self.order:
                    coefficients[degree] += left * value
                else:
                    omitted += abs(left) * abs(value) * powers[degree]
        left_polynomial_bound = self.polynomial_absolute_bound()
        right_polynomial_bound = right.polynomial_absolute_bound()
        remainder = (
            omitted
            + left_polynomial_bound * right.remainder
            + right_polynomial_bound * self.remainder
            + self.remainder * right.remainder
        )
        return TaylorModel(coefficients, self.radius, remainder)

    def __rmul__(self, other: object) -> "TaylorModel":
        return self * other

    def reciprocal(self) -> "TaylorModel":
        if not lower(abs(self.coefficients[0])) > 0:
            raise ZeroDivisionError("Taylor-model center contains zero")
        coefficients = [acb(0) for _ in range(self.order + 1)]
        coefficients[0] = acb(1) / self.coefficients[0]
        for degree in range(1, self.order + 1):
            convolution = sum(
                (
                    self.coefficients[index] * coefficients[degree - index]
                    for index in range(1, degree + 1)
                ),
                acb(0),
            )
            coefficients[degree] = -convolution / self.coefficients[0]
        candidate = TaylorModel(coefficients, self.radius)
        residual = self.constant(1, self.order, self.radius) - self * candidate
        residual_bound = residual.absolute_bound()
        if not upper(residual_bound) < 1.0:
            raise ZeroDivisionError(
                "Taylor reciprocal residual is not contractive: "
                f"{upper(residual_bound):.6e}"
            )
        remainder = (
            candidate.polynomial_absolute_bound()
            * residual_bound
            / (arb(1) - residual_bound)
        )
        return TaylorModel(coefficients, self.radius, remainder)

    def __truediv__(self, other: object) -> "TaylorModel":
        return self * self.coerce(other).reciprocal()

    def __rtruediv__(self, other: object) -> "TaylorModel":
        return self.coerce(other) / self

    def __pow__(self, power: int) -> "TaylorModel":
        if power < 0:
            return (self.reciprocal()) ** (-power)
        result = self.constant(1, self.order, self.radius)
        factor = self
        exponent = power
        while exponent:
            if exponent & 1:
                result = result * factor
            exponent >>= 1
            if exponent:
                factor = factor * factor
        return result


def tm_matrix_coefficients(matrix: list[list[TaylorModel]]) -> list[acb_mat]:
    order = matrix[0][0].order
    return [
        acb_mat(
            [
                [matrix[row][column].coefficients[degree] for column in range(len(matrix[0]))]
                for row in range(len(matrix))
            ]
        )
        for degree in range(order + 1)
    ]


def tm_matrix_multiply(
    left: list[list[TaylorModel]], right: list[list[TaylorModel]]
) -> list[list[TaylorModel]]:
    return [
        [
            sum(
                (left[row][index] * right[index][column] for index in range(len(right))),
                left[0][0].constant(0, left[0][0].order, left[0][0].radius),
            )
            for column in range(len(right[0]))
        ]
        for row in range(len(left))
    ]


def tm_matrix_subtract(
    left: list[list[TaylorModel]], right: list[list[TaylorModel]]
) -> list[list[TaylorModel]]:
    return [
        [left[row][column] - right[row][column] for column in range(len(left[0]))]
        for row in range(len(left))
    ]


def tm_identity(size: int, prototype: TaylorModel) -> list[list[TaylorModel]]:
    return [
        [prototype.constant(int(row == column), prototype.order, prototype.radius) for column in range(size)]
        for row in range(size)
    ]


def tm_matrix_infinity_norm(matrix: list[list[TaylorModel]]) -> arb:
    return max(
        (
            sum((value.absolute_bound() for value in row), arb(0))
            for row in matrix
        ),
        key=lambda value: upper(value),
    )


def tm_verified_inverse_bound(
    matrix: list[list[TaylorModel]],
) -> tuple[arb, float]:
    """Bound the inverse using a validated polynomial right inverse."""

    size = len(matrix)
    order = matrix[0][0].order
    radius = matrix[0][0].radius
    coefficients = tm_matrix_coefficients(matrix)
    center_inverse_ball = coefficients[0].inv()
    center_inverse = acb_mat(
        [
            [
                SelectedQ79IntervalSystem.midpoint_acb(
                    center_inverse_ball[row, column]
                )
                for column in range(size)
            ]
            for row in range(size)
        ]
    )
    inverse_coefficients = [center_inverse]
    for degree in range(1, order + 1):
        convolution = acb_mat(size, size)
        for index in range(1, degree + 1):
            convolution += (
                coefficients[index]
                * inverse_coefficients[degree - index]
            )
        inverse_coefficients.append(-center_inverse * convolution)
    candidate = [
        [
            TaylorModel(
                [
                    inverse_coefficients[degree][row, column]
                    for degree in range(order + 1)
                ],
                radius,
            ).midpoint_polynomial()
            for column in range(size)
        ]
        for row in range(size)
    ]
    defect = tm_matrix_subtract(
        tm_identity(size, matrix[0][0]),
        tm_matrix_multiply(matrix, candidate),
    )
    defect_norm = tm_matrix_infinity_norm(defect)
    defect_upper = upper(defect_norm)
    if not defect_upper < 1.0:
        raise ZeroDivisionError(
            "Taylor polynomial inverse is not contractive: "
            f"{defect_upper:.6e}"
        )
    inverse_norm = tm_matrix_infinity_norm(candidate) / (
        arb(1) - defect_norm
    )
    return inverse_norm, defect_upper


def tm_matrix_solve(
    matrix: list[list[TaylorModel]], targets: list[list[TaylorModel]]
) -> tuple[list[list[TaylorModel]], float, float]:
    order = matrix[0][0].order
    radius = matrix[0][0].radius
    matrix_coefficients = tm_matrix_coefficients(matrix)
    target_coefficients = tm_matrix_coefficients(targets)
    center_matrix = matrix_coefficients[0]
    series_inverse = center_matrix.inv()
    recurrence_inverse = acb_mat(
        [
            [SelectedQ79IntervalSystem.midpoint_acb(series_inverse[row, column]) for column in range(series_inverse.ncols())]
            for row in range(series_inverse.nrows())
        ]
    )
    solution_coefficients: list[acb_mat] = []
    for degree in range(order + 1):
        right = target_coefficients[degree]
        for index in range(1, degree + 1):
            right -= matrix_coefficients[index] * solution_coefficients[degree - index]
        solution_coefficients.append(recurrence_inverse * right)
    result = [
        [
            TaylorModel(
                [solution_coefficients[degree][row, column] for degree in range(order + 1)],
                radius,
            ).midpoint_polynomial()
            for column in range(len(targets[0]))
        ]
        for row in range(len(matrix))
    ]
    residual = tm_matrix_subtract(targets, tm_matrix_multiply(matrix, result))
    inverse_norm, neumann_upper = tm_verified_inverse_bound(matrix)
    maximum_error = 0.0
    for column in range(len(targets[0])):
        residual_norm = max(
            (residual[row][column].absolute_bound() for row in range(len(matrix))),
            key=lambda value: upper(value),
        )
        error = inverse_norm * residual_norm
        error_upper = upper(error)
        maximum_error = max(maximum_error, error_upper)
        for row in range(len(matrix)):
            result[row][column].remainder += error
    return result, neumann_upper, maximum_error


def tm_matrix_vector(
    matrix: acb_mat, vector: list[TaylorModel]
) -> list[TaylorModel]:
    return [
        sum(
            (matrix[row, column] * vector[column] for column in range(matrix.ncols())),
            vector[0].constant(0, vector[0].order, vector[0].radius),
        )
        for row in range(matrix.nrows())
    ]


def tm_monomial_with_derivative(
    values: list[TaylorModel],
    derivatives: list[TaylorModel],
    powers: list[int],
) -> tuple[TaylorModel, TaylorModel]:
    value = values[0].constant(1, values[0].order, values[0].radius)
    for coordinate, power in zip(values, powers):
        value *= coordinate**power
    derivative = values[0].constant(0, values[0].order, values[0].radius)
    for selected, power in enumerate(powers):
        if power == 0:
            continue
        term = derivatives[selected] * power
        for index, (coordinate, other_power) in enumerate(zip(values, powers)):
            term *= coordinate ** (other_power - int(index == selected))
        derivative += term
    return value, derivative


def aligned_tm_coefficients_and_derivative(
    table: list[dict],
    line: list[TaylorModel],
    line_derivative: list[TaylorModel],
    *,
    chart: str,
) -> tuple[list[TaylorModel], list[TaylorModel]]:
    degree = sum(int(value) for value in table[0]["powers_xyz"])
    prototype = line[0]
    ascending = [
        prototype.constant(0, prototype.order, prototype.radius)
        for _ in range(degree + 1)
    ]
    derivative = [
        prototype.constant(0, prototype.order, prototype.radius)
        for _ in range(degree + 1)
    ]
    for row in table:
        x_power, y_power, z_power = [int(value) for value in row["powers_xyz"]]
        coefficient = int(row["coefficient"])
        if chart == "y":
            for index in range(y_power + 1):
                powers = [y_power - index, x_power + z_power, index]
                value, value_derivative = tm_monomial_with_derivative(
                    line, line_derivative, powers
                )
                scalar = coefficient * (-1) ** y_power * math.comb(y_power, index)
                ascending[index + z_power] += scalar * value
                derivative[index + z_power] += scalar * value_derivative
        elif chart == "z":
            for index in range(z_power + 1):
                powers = [z_power - index, index, x_power + y_power]
                value, value_derivative = tm_monomial_with_derivative(
                    line, line_derivative, powers
                )
                scalar = coefficient * (-1) ** z_power * math.comb(z_power, index)
                ascending[index + y_power] += scalar * value
                derivative[index + y_power] += scalar * value_derivative
        else:
            raise ValueError(f"unsupported chart {chart!r}")
    return ascending, derivative


def quotient_pair_multiply(
    left: tuple[TaylorModel, TaylorModel],
    right: tuple[TaylorModel, TaylorModel],
    relation_constant: TaylorModel,
    relation_linear: TaylorModel,
) -> tuple[TaylorModel, TaylorModel]:
    quadratic = left[1] * right[1]
    return (
        left[0] * right[0] + quadratic * relation_constant,
        left[0] * right[1]
        + left[1] * right[0]
        + quadratic * relation_linear,
    )


def quotient_pair_power(
    power: int,
    relation_constant: TaylorModel,
    relation_linear: TaylorModel,
) -> tuple[TaylorModel, TaylorModel]:
    one = relation_constant.constant(1, relation_constant.order, relation_constant.radius)
    zero = relation_constant.constant(0, relation_constant.order, relation_constant.radius)
    result = (one, zero)
    factor = (zero, one)
    exponent = power
    while exponent:
        if exponent & 1:
            result = quotient_pair_multiply(
                result, factor, relation_constant, relation_linear
            )
        exponent >>= 1
        if exponent:
            factor = quotient_pair_multiply(
                factor, factor, relation_constant, relation_linear
            )
    return result


def quotient_reduce(
    coefficients: list[TaylorModel],
    relation_constant: TaylorModel,
    relation_linear: TaylorModel,
) -> tuple[TaylorModel, TaylorModel]:
    zero = relation_constant.constant(0, relation_constant.order, relation_constant.radius)
    result = (zero, zero)
    for power, coefficient in enumerate(coefficients):
        basis = quotient_pair_power(power, relation_constant, relation_linear)
        result = (result[0] + coefficient * basis[0], result[1] + coefficient * basis[1])
    return result


def quotient_pair_inverse(
    value: tuple[TaylorModel, TaylorModel],
    root_sum: TaylorModel,
    root_product: TaylorModel,
) -> tuple[TaylorModel, TaylorModel]:
    norm = value[0] ** 2 + root_sum * value[0] * value[1] + root_product * value[1] ** 2
    inverse_norm = norm.reciprocal()
    return (
        (value[0] + root_sum * value[1]) * inverse_norm,
        -value[1] * inverse_norm,
    )


def validated_ab_taylor_models(
    system: SelectedQ79IntervalSystem,
    start: complex,
    direction: complex,
    radius: arb,
    order: int,
) -> tuple[TaylorModel, TaylorModel, float, float]:
    parameter = acb(format(start.real, ".17g"), format(start.imag, ".17g"))
    a_value, b_value, _line, _line_derivative = system.ab_line_data(parameter)
    scale = acb(0, 1) * as_acb(direction) * system.period_length
    a_coefficients = [acb(0) for _ in range(order + 1)]
    b_coefficients = [acb(0) for _ in range(order + 1)]
    a_coefficients[0] = a_value
    b_coefficients[0] = b_value
    for degree in range(order):
        a_coefficients[degree + 1] = (
            acb(2) * scale * b_coefficients[degree] / acb(degree + 1)
        )
        a_squared_coefficient = sum(
            (
                a_coefficients[index] * a_coefficients[degree - index]
                for index in range(degree + 1)
            ),
            acb(0),
        )
        b_coefficients[degree + 1] = scale * (
            acb(3) * a_squared_coefficient - acb(int(degree == 0))
        ) / acb(degree + 1)
    a_candidate = TaylorModel(a_coefficients, radius).midpoint_polynomial()
    b_candidate = TaylorModel(b_coefficients, radius).midpoint_polynomial()
    residual_a = a_candidate.derivative_polynomial() - acb(2) * scale * b_candidate
    residual_b = b_candidate.derivative_polynomial() - scale * (
        acb(3) * a_candidate**2 - 1
    )
    residual_bound = max(
        residual_a.absolute_bound(),
        residual_b.absolute_bound(),
        key=lambda value: upper(value),
    )
    initial_error = arb(
        str(max(radius_upper(a_value), radius_upper(b_value)))
    )
    error = initial_error
    scale_absolute = abs(scale)
    for _ in range(12):
        a_bound = a_candidate.absolute_bound() + error
        lipschitz = max(
            acb(2).real * scale_absolute,
            acb(6).real * scale_absolute * a_bound,
            key=lambda value: upper(value),
        )
        argument = lipschitz * radius
        growth = argument.exp()
        if upper(lipschitz) == 0:
            defect = residual_bound * radius
        else:
            defect = residual_bound * (growth - arb(1)) / lipschitz
        updated = growth * initial_error + defect
        if upper(updated) <= upper(error) * (1.0 + 1.0e-12):
            error = updated
            break
        error = updated
    else:
        raise ArithmeticError("elliptic Taylor enclosure did not stabilize")
    a_model = a_candidate.copy_with_remainder(error)
    b_model = b_candidate.copy_with_remainder(error)
    return a_model, b_model, upper(residual_bound), upper(error)


def build_taylor_system(
    system: SelectedQ79IntervalSystem,
    start: complex,
    direction: complex,
    step: float,
    order: int,
) -> tuple[list[list[TaylorModel]], list[TaylorModel], dict]:
    radius = arb(format(step, ".17g"))
    a_value, b_value, elliptic_residual, elliptic_remainder = validated_ab_taylor_models(
        system, start, direction, radius, order
    )
    prototype = a_value
    one = prototype.constant(1, order, radius)
    zero = prototype.constant(0, order, radius)
    elliptic = [a_value, b_value, one]
    da_dw = acb(2) * system.period_length * b_value
    db_dw = system.period_length * (acb(3) * a_value**2 - 1)
    elliptic_derivative = [da_dw, db_dw, zero]
    line = tm_matrix_vector(system.alignment, elliptic)
    line_derivative = tm_matrix_vector(system.alignment, elliptic_derivative)
    f_coefficients, f_derivative = aligned_tm_coefficients_and_derivative(
        system.evaluator.tables["F6"],
        line,
        line_derivative,
        chart=system.line_chart,
    )
    g_coefficients, _ = aligned_tm_coefficients_and_derivative(
        system.evaluator.tables["G3"],
        line,
        line_derivative,
        chart=system.line_chart,
    )
    q_coefficients, q_derivative = aligned_tm_coefficients_and_derivative(
        system.evaluator.tables["Q2"],
        line,
        line_derivative,
        chart=system.line_chart,
    )

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
    solved, solve_neumann, solve_error = tm_matrix_solve(reduction, targets)
    exact_terms = [[solved[index][power] for index in range(6)] for power in range(5)]
    connection = [[solved[6 + index][power] for index in range(5)] for power in range(5)]

    q0, q1, q2 = q_coefficients
    root_sum = -q1 / q2
    root_product = q0 / q2
    relation_constant = -root_product
    relation_linear = root_sum
    discriminant = q1**2 - 4 * q2 * q0
    discriminant_lower = discriminant.absolute_lower()
    q_w_pair = quotient_reduce(
        q_derivative, relation_constant, relation_linear
    )
    g_pair = quotient_reduce(g_coefficients, relation_constant, relation_linear)
    g_inverse = quotient_pair_inverse(g_pair, root_sum, root_product)
    source = [zero for _ in range(5)]
    for power in range(5):
        exact_pair = quotient_reduce(
            exact_terms[power], relation_constant, relation_linear
        )
        power_pair = quotient_pair_power(power, relation_constant, relation_linear)
        velocity_numerator = quotient_pair_multiply(
            power_pair, q_w_pair, relation_constant, relation_linear
        )
        exact_weight = quotient_pair_multiply(
            exact_pair, g_inverse, relation_constant, relation_linear
        )
        velocity_weight = quotient_pair_multiply(
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

    residue = [[zero for _ in range(5)] for _ in range(8)]
    for row, generator in enumerate(system.generators):
        variation = tm_matrix_vector(system.alignment * generator, elliptic)
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
        residue[row][0] = system.period_length * constant
        residue[row][1] = system.period_length * linear

    displacement = acb(0, 1) * as_acb(direction)
    matrix = [[zero for _ in range(13)] for _ in range(13)]
    forcing = [zero for _ in range(13)]
    for row in range(5):
        forcing[row] = displacement * source[row]
        for column in range(5):
            matrix[row][column] = displacement * connection[row][column]
    for row in range(8):
        for column in range(5):
            matrix[5 + row][column] = displacement * residue[row][column]
    return matrix, forcing, {
        "elliptic_residual_bound": elliptic_residual,
        "elliptic_remainder_bound": elliptic_remainder,
        "reduction_neumann_norm": solve_neumann,
        "reduction_solution_remainder": solve_error,
        "q_discriminant_absolute_lower": discriminant_lower,
    }


def acb_column(values: list[acb]) -> acb_mat:
    return acb_mat([[value] for value in values])


def midpoint_matrix(matrix: acb_mat) -> acb_mat:
    return acb_mat(
        [
            [SelectedQ79IntervalSystem.midpoint_acb(matrix[row, column]) for column in range(matrix.ncols())]
            for row in range(matrix.nrows())
        ]
    )


def acb_matrix_infinity_norm(matrix: acb_mat) -> arb:
    return max(
        (
            sum(
                (abs(matrix[row, column]) for column in range(matrix.ncols())),
                arb(0),
            )
            for row in range(matrix.nrows())
        ),
        key=lambda value: upper(value),
    )


@dataclass
class LiftErrorFrame:
    fundamental: acb_mat
    coordinate_radii: list[arb]

    def physical_generator_matrix(self) -> acb_mat:
        diagonal = acb_mat(5, 5)
        for index, radius in enumerate(self.coordinate_radii):
            diagonal[index, index] = acb(radius)
        return self.fundamental * diagonal

    def physical_radius(self) -> arb:
        return acb_matrix_infinity_norm(self.physical_generator_matrix())


def tm_vector_derivative(values: list[TaylorModel]) -> list[TaylorModel]:
    return [value.derivative_polynomial() for value in values]


def tm_matrix_derivative(values: list[list[TaylorModel]]) -> list[list[TaylorModel]]:
    return [[value.derivative_polynomial() for value in row] for row in values]


def tm_matrix_vector_multiply(
    matrix: list[list[TaylorModel]], vector: list[TaylorModel]
) -> list[TaylorModel]:
    return [
        sum(
            (matrix[row][column] * vector[column] for column in range(len(vector))),
            vector[0].constant(0, vector[0].order, vector[0].radius),
        )
        for row in range(len(matrix))
    ]


def tm_vector_infinity_norm(values: list[TaylorModel]) -> arb:
    return max(
        (value.absolute_bound() for value in values),
        key=lambda value: upper(value),
    )


def candidate_flow_polynomials(
    matrix: list[list[TaylorModel]],
    forcing: list[TaylorModel],
    initial_center: list[acb],
) -> tuple[list[TaylorModel], list[list[TaylorModel]]]:
    order = matrix[0][0].order
    radius = matrix[0][0].radius
    dimension = len(matrix)
    matrix_coefficients = tm_matrix_coefficients(matrix)
    forcing_coefficients = [
        acb_column([value.coefficients[degree] for value in forcing])
        for degree in range(order + 1)
    ]
    state_coefficients = [acb_column(initial_center)]
    lift_dimension = 5
    fundamental_coefficients = [acb_mat(lift_dimension, lift_dimension)]
    for index in range(lift_dimension):
        fundamental_coefficients[0][index, index] = acb(1)
    for degree in range(order):
        state_right = forcing_coefficients[degree]
        fundamental_right = acb_mat(lift_dimension, lift_dimension)
        for index in range(degree + 1):
            state_right += matrix_coefficients[index] * state_coefficients[degree - index]
            lift_matrix = acb_mat(
                [
                    [
                        matrix_coefficients[index][row, column]
                        for column in range(lift_dimension)
                    ]
                    for row in range(lift_dimension)
                ]
            )
            fundamental_right += lift_matrix * fundamental_coefficients[degree - index]
        state_coefficients.append(state_right / acb(degree + 1))
        fundamental_coefficients.append(fundamental_right / acb(degree + 1))
    state = [
        TaylorModel(
            [state_coefficients[degree][row, 0] for degree in range(order + 1)],
            radius,
        ).midpoint_polynomial()
        for row in range(dimension)
    ]
    fundamental = [
        [
            TaylorModel(
                [
                    fundamental_coefficients[degree][row, column]
                    for degree in range(order + 1)
                ],
                radius,
            ).midpoint_polynomial()
            for column in range(lift_dimension)
        ]
        for row in range(lift_dimension)
    ]
    return state, fundamental


def validated_flow_step(
    system: SelectedQ79IntervalSystem,
    start: complex,
    direction: complex,
    step: float,
    center: list[acb],
    input_lift_frame: LiftErrorFrame,
    input_beta_radius: arb,
    *,
    order: int,
) -> tuple[list[acb], LiftErrorFrame, arb, dict]:
    matrix, forcing, system_diagnostics = build_taylor_system(
        system, start, direction, step, order
    )
    state, fundamental = candidate_flow_polynomials(matrix, forcing, center)
    state_derivative = tm_vector_derivative(state)
    state_residual = [
        value + forcing[index] - state_derivative[index]
        for index, value in enumerate(tm_matrix_vector_multiply(matrix, state))
    ]
    lift_matrix = [row[:5] for row in matrix[:5]]
    fundamental_residual = tm_matrix_subtract(
        tm_matrix_multiply(lift_matrix, fundamental),
        tm_matrix_derivative(fundamental),
    )

    inverse_norm, inverse_defect_upper = tm_verified_inverse_bound(
        fundamental
    )
    linear_defect = inverse_norm * tm_matrix_infinity_norm(fundamental_residual)
    affine_defect = inverse_norm * tm_vector_infinity_norm(state_residual[:5])
    step_ball = arb(format(step, ".17g"))
    exponent = linear_defect * step_ball
    growth = exponent.exp()
    if upper(linear_defect) == 0:
        forced_error = affine_defect * step_ball
    else:
        forced_error = affine_defect * (growth - arb(1)) / linear_defect
    input_lift_radius = input_lift_frame.physical_radius()
    transformed_lift_error = growth * input_lift_radius + forced_error
    transformed_lift_correction = (
        (growth - arb(1)) * input_lift_radius + forced_error
    )

    endpoint_parameter = arb(format(step, ".17g"))
    endpoint_state = [value.evaluate_polynomial(endpoint_parameter) for value in state]
    endpoint_fundamental = acb_mat(
        [
            [fundamental[row][column].evaluate_polynomial(endpoint_parameter) for column in range(5)]
            for row in range(5)
        ]
    )
    endpoint_fundamental_norm = max(
        (
            sum((abs(endpoint_fundamental[row, column]) for column in range(5)), arb(0))
            for row in range(5)
        ),
        key=lambda value: upper(value),
    )
    lift_polynomial_endpoint_radius = arb(
        str(max(radius_upper(value) for value in endpoint_state[:5]))
    )
    beta_polynomial_endpoint_radius = arb(
        str(max(radius_upper(value) for value in endpoint_state[5:]))
    )
    output_fundamental = (
        endpoint_fundamental * input_lift_frame.fundamental
    )
    output_fundamental_inverse = output_fundamental.inv()
    correction_pullback = (
        output_fundamental_inverse * endpoint_fundamental
    )
    correction_upper = upper(transformed_lift_correction)
    rounding_upper = upper(lift_polynomial_endpoint_radius)
    output_coordinate_radii = []
    for row in range(5):
        correction_coordinate_norm = sum(
            (abs(correction_pullback[row, column]) for column in range(5)),
            arb(0),
        )
        rounding_coordinate_norm = sum(
            (
                abs(output_fundamental_inverse[row, column])
                for column in range(5)
            ),
            arb(0),
        )
        output_coordinate_radii.append(
            input_lift_frame.coordinate_radii[row]
            + arb(str(correction_upper)) * correction_coordinate_norm
            + arb(str(rounding_upper)) * rounding_coordinate_norm
        )
    output_lift_frame = LiftErrorFrame(
        fundamental=output_fundamental,
        coordinate_radii=output_coordinate_radii,
    )
    output_lift_radius = output_lift_frame.physical_radius()

    fundamental_uniform_norm = tm_matrix_infinity_norm(fundamental)
    lift_error_uniform = fundamental_uniform_norm * transformed_lift_error
    residue_matrix = [row[:5] for row in matrix[5:]]
    residue_norm = tm_matrix_infinity_norm(residue_matrix)
    beta_residual = tm_vector_infinity_norm(state_residual[5:])
    beta_increment_error = step_ball * (
        residue_norm * lift_error_uniform + beta_residual
    )
    output_beta_radius = (
        input_beta_radius
        + beta_increment_error
        + beta_polynomial_endpoint_radius
    )
    endpoint_center = [
        SelectedQ79IntervalSystem.midpoint_acb(value) for value in endpoint_state
    ]
    if not math.isfinite(upper(output_lift_radius)):
        raise ArithmeticError("validated lift endpoint radius is nonfinite")
    if not math.isfinite(upper(output_beta_radius)):
        raise ArithmeticError("validated beta endpoint radius is nonfinite")
    diagnostics = {
        **system_diagnostics,
        "fundamental_inverse_neumann_norm": inverse_defect_upper,
        "linear_defect_bound": upper(linear_defect),
        "affine_defect_bound": upper(affine_defect),
        "transformed_lift_correction": upper(
            transformed_lift_correction
        ),
        "input_lift_radius": upper(input_lift_radius),
        "input_beta_radius": upper(input_beta_radius),
        "output_lift_radius": upper(output_lift_radius),
        "output_beta_radius": upper(output_beta_radius),
        "endpoint_fundamental_norm": upper(endpoint_fundamental_norm),
        "fundamental_uniform_norm": upper(fundamental_uniform_norm),
        "residue_norm": upper(residue_norm),
        "beta_residual_bound": upper(beta_residual),
        "beta_increment_error": upper(beta_increment_error),
        "global_frame_norm": upper(
            acb_matrix_infinity_norm(output_fundamental)
        ),
        "global_frame_inverse_norm": upper(
            acb_matrix_infinity_norm(output_fundamental_inverse)
        ),
    }
    return (
        endpoint_center,
        output_lift_frame,
        output_beta_radius,
        diagnostics,
    )


def interval_from_bounds(value: dict) -> acb:
    real_lower = arb(value["real"]["lower"])
    real_upper = arb(value["real"]["upper"])
    imaginary_lower = arb(value["imaginary"]["lower"])
    imaginary_upper = arb(value["imaginary"]["upper"])
    real_midpoint = (real_lower + real_upper) / arb(2)
    imaginary_midpoint = (imaginary_lower + imaginary_upper) / arb(2)
    real_radius = (real_upper - real_lower) / arb(2)
    imaginary_radius = (imaginary_upper - imaginary_lower) / arb(2)
    return acb(
        arb(str(real_midpoint.mid()), str(real_radius.upper())),
        arb(str(imaginary_midpoint.mid()), str(imaginary_radius.upper())),
    )


def execute_validated_path(
    system: SelectedQ79IntervalSystem,
    *,
    waypoints: list[complex],
    path_name: str,
    order: int,
    initial_step: float,
    minimum_step: float,
    maximum_steps: int,
    checkpoint_path: Path | None,
    resume: bool,
) -> dict:
    waypoint_packet = [
        {"real": format(value.real, ".17g"), "imaginary": format(value.imag, ".17g")}
        for value in waypoints
    ]
    if resume:
        if checkpoint_path is None or not checkpoint_path.exists():
            raise FileNotFoundError("the requested transport checkpoint is absent")
        checkpoint = load(checkpoint_path)
        if checkpoint["path_name"] != path_name:
            raise ValueError("checkpoint path does not match this execution")
        if checkpoint["waypoints"] != waypoint_packet:
            raise ValueError("checkpoint waypoints do not match this execution")
        if int(checkpoint["order"]) != order:
            raise ValueError("checkpoint Taylor order does not match")
        center = [decoded_acb(value) for value in checkpoint["center"]]
        lift_frame = LiftErrorFrame(
            fundamental=decoded_matrix(checkpoint["lift_fundamental"]),
            coordinate_radii=[arb(value) for value in checkpoint["coordinate_radii"]],
        )
        beta_radius = arb(checkpoint["beta_radius"])
        proposed_step = float(checkpoint["proposed_step"])
        accepted = checkpoint["accepted_steps"]
        rejected = int(checkpoint["rejected_step_count"])
        minimum_accepted_step = float(checkpoint["minimum_accepted_step"])
        maximum_lift_radius = float(checkpoint["maximum_lift_radius"])
        maximum_beta_radius = float(checkpoint["maximum_beta_radius"])
        starting_segment = int(checkpoint["segment_index"])
        starting_position = float(checkpoint["segment_position"])
    else:
        base_lift = load(BASE_LIFT)
        initial_balls = [
            interval_from_bounds(value)
            for value in base_lift["y_chart_base_lift"]
        ]
        center = [
            SelectedQ79IntervalSystem.midpoint_acb(value)
            for value in initial_balls
        ] + [acb(0) for _ in range(8)]
        initial_fundamental = acb_mat(5, 5)
        for index in range(5):
            initial_fundamental[index, index] = acb(1)
        lift_frame = LiftErrorFrame(
            fundamental=initial_fundamental,
            coordinate_radii=[value.rad().upper() for value in initial_balls],
        )
        beta_radius = arb(0)
        proposed_step = initial_step
        accepted = []
        rejected = 0
        minimum_accepted_step = math.inf
        maximum_lift_radius = upper(lift_frame.physical_radius())
        maximum_beta_radius = upper(beta_radius)
        starting_segment = 0
        starting_position = 0.0

    lift_radius = lift_frame.physical_radius()
    segment_pairs = list(zip(waypoints, waypoints[1:]))
    completed_length = sum(
        abs(right - left)
        for left, right in segment_pairs[:starting_segment]
    )

    def save_checkpoint(segment_index: int, position: float) -> None:
        if checkpoint_path is None:
            return
        atomic_dump(
            checkpoint_path,
            {
                "schema": "MTTQ79ValidatedBetaTransportCheckpoint.v1",
                "path_name": path_name,
                "waypoints": waypoint_packet,
                "order": order,
                "segment_index": segment_index,
                "segment_position": format(position, ".17g"),
                "proposed_step": format(proposed_step, ".17g"),
                "center": [encoded_acb(value) for value in center],
                "lift_fundamental": encoded_matrix(lift_frame.fundamental),
                "coordinate_radii": [
                    str(value) for value in lift_frame.coordinate_radii
                ],
                "beta_radius": str(beta_radius),
                "accepted_steps": accepted,
                "rejected_step_count": rejected,
                "minimum_accepted_step": format(minimum_accepted_step, ".17g"),
                "maximum_lift_radius": format(maximum_lift_radius, ".17g"),
                "maximum_beta_radius": format(maximum_beta_radius, ".17g"),
            },
        )

    for segment_index in range(starting_segment, len(segment_pairs)):
        left, right = segment_pairs[segment_index]
        segment_length = abs(right - left)
        if segment_length == 0:
            continue
        direction = (right - left) / segment_length
        position = (
            starting_position if segment_index == starting_segment else 0.0
        )
        if segment_index != starting_segment:
            proposed_step = min(initial_step, segment_length)
        while position < segment_length:
            if len(accepted) >= maximum_steps:
                raise ArithmeticError(
                    "validated transport exceeded the step budget"
                )
            step = min(proposed_step, segment_length - position)
            if step < minimum_step:
                raise ArithmeticError(
                    "validated transport requires a step below "
                    f"{minimum_step:.3e}"
                )
            parameter_start = left + direction * position
            try:
                (
                    next_center,
                    next_lift_frame,
                    next_beta_radius,
                    diagnostics,
                ) = validated_flow_step(
                    system,
                    parameter_start,
                    direction,
                    step,
                    center,
                    lift_frame,
                    beta_radius,
                    order=order,
                )
                if diagnostics["transformed_lift_correction"] > 1.0e-6:
                    raise ArithmeticError(
                        "local transformed lift correction exceeds its budget: "
                        f"{diagnostics['transformed_lift_correction']:.6e}"
                    )
                if diagnostics["beta_increment_error"] > 1.0e-3:
                    raise ArithmeticError(
                        "local beta increment error exceeds its budget: "
                        f"{diagnostics['beta_increment_error']:.6e}"
                    )
                if upper(next_beta_radius) > 0.5:
                    raise ArithmeticError(
                        "validated beta radius exceeds the endpoint decision budget: "
                        f"{upper(next_beta_radius):.6e}"
                    )
            except (ArithmeticError, ZeroDivisionError, ValueError) as error:
                rejected += 1
                proposed_step = step / 2.0
                if proposed_step < minimum_step:
                    raise ArithmeticError(
                        "step validation failed at "
                        f"{parameter_start.real:.17g}"
                        f"{parameter_start.imag:+.17g}i: {error}"
                    ) from error
                continue
            old_position = position
            position = min(old_position + step, segment_length)
            parameter_end = left + direction * position
            center = next_center
            lift_frame = next_lift_frame
            lift_radius = lift_frame.physical_radius()
            beta_radius = next_beta_radius
            minimum_accepted_step = min(minimum_accepted_step, step)
            maximum_lift_radius = max(
                maximum_lift_radius, upper(lift_radius)
            )
            maximum_beta_radius = max(
                maximum_beta_radius, upper(beta_radius)
            )
            accepted.append(
                {
                    "segment_index": segment_index,
                    "start": {
                        "real": format(parameter_start.real, ".17g"),
                        "imaginary": format(parameter_start.imag, ".17g"),
                    },
                    "end": {
                        "real": format(parameter_end.real, ".17g"),
                        "imaginary": format(parameter_end.imag, ".17g"),
                    },
                    "step": format(step, ".17g"),
                    **diagnostics,
                }
            )
            if len(accepted) % 25 == 0 or position == segment_length:
                print(
                    "validated transport "
                    f"steps={len(accepted)} segment={segment_index} "
                    f"position={position:.12g}/{segment_length:.12g} "
                    f"step={step:.3e} "
                    f"lift_radius={upper(lift_radius):.3e} "
                    f"beta_radius={upper(beta_radius):.3e}",
                    flush=True,
                )
            quality = max(
                diagnostics["reduction_neumann_norm"],
                diagnostics["fundamental_inverse_neumann_norm"],
            )
            proposed_step = min(
                initial_step,
                step * (1.5 if quality < 0.25 else 1.15),
            )
            if len(accepted) % 10 == 0 or position == segment_length:
                save_checkpoint(segment_index, position)
        completed_length += segment_length

    beta_center = np.asarray(
        [midpoint(value) for value in center[5:]],
        dtype=np.complex128,
    )
    serialized_centers = [as_acb(complex(value)) for value in beta_center]
    serialization_radius = max(
        (
            abs(value - serialized)
            for value, serialized in zip(center[5:], serialized_centers)
        ),
        key=upper,
    )
    reported_beta_radius = beta_radius + serialization_radius
    center_norm_ball = sum(
        (abs(value) ** 2 for value in serialized_centers),
        arb(0),
    ).sqrt()
    beta_center_norm = float(center_norm_ball.mid())
    beta_norm_lower = math.nextafter(
        lower(center_norm_ball)
        - math.nextafter(
            math.sqrt(8.0) * upper(reported_beta_radius),
            math.inf,
        ),
        -math.inf,
    )
    maximum_component_lower = math.nextafter(
        max(lower(abs(value)) for value in serialized_centers)
        - upper(reported_beta_radius),
        -math.inf,
    )
    if not beta_norm_lower > 0 or not maximum_component_lower > 0:
        raise ArithmeticError("validated endpoint beta enclosure still contains zero")
    return {
        "schema": "MTTQ79SelectedSideBetaDefectIntervalCertificate.v1",
        "status": "EXECUTED_CONTOUR_ENDPOINT_BETA_NONZERO_INTERVAL_CERTIFIED",
        "method": {
            "name": "adaptive defect-corrected Taylor-model transport",
            "order": order,
            "path": path_name,
            "waypoints": [
                {
                    "real": format(value.real, ".17g"),
                    "imaginary": format(value.imag, ".17g"),
                }
                for value in waypoints
            ],
            "approximate_fundamental_matrix_used_as_error_coordinates": True,
            "raw_connection_exponential_bound_used": False,
            "aligned_quadratic_source_evaluated_by_exact_quotient_trace": True,
        },
        "endpoint": {
            "beta_center": [
                {"real": format(value.real, ".17g"), "imaginary": format(value.imag, ".17g")}
                for value in beta_center
            ],
            "uniform_component_radius_upper": format(
                upper(reported_beta_radius), ".17g"
            ),
            "center_serialization_radius_upper": format(
                upper(serialization_radius), ".17g"
            ),
            "lift_uniform_component_radius_upper": format(
                upper(lift_radius), ".17g"
            ),
            "center_norm": format(beta_center_norm, ".17g"),
            "euclidean_norm_lower": format(beta_norm_lower, ".17g"),
            "maximum_component_absolute_lower": format(maximum_component_lower, ".17g"),
            "zero_excluded": True,
        },
        "execution": {
            "accepted_step_count": len(accepted),
            "rejected_step_count": rejected,
            "minimum_accepted_step": format(minimum_accepted_step, ".17g"),
            "total_contour_length": format(completed_length, ".17g"),
            "maximum_lift_radius": format(maximum_lift_radius, ".17g"),
            "maximum_beta_radius": format(maximum_beta_radius, ".17g"),
            "steps": accepted,
        },
        "strict_scope": {
            "executed_contour_endpoint_beta_zero_excluded": True,
            "selected_side_ell_zero_branch_excluded": False,
            "global_ell_zero_no_go": False,
            "nonzero_integral_branch_selected": False,
            "observed_SM_values_used": False,
        },
    }


def build_floating_engine() -> tuple[
    Q79DeltaNormalFunction, PGL3BetaEvaluator, np.ndarray
]:
    a124 = load(A124)
    wall = load(WALL)
    source = load(SOURCE)
    evaluator = PGL3BetaEvaluator()
    alignment_0 = floating_complex_matrix(source["final_alignment"])
    direction = np.asarray(
        [complex_value(value) for value in a124["search_direction"]["coordinates"]]
    )
    tangent = sum(
        (
            direction[index] * evaluator.generators[index]
            for index in range(8)
        ),
        np.zeros((3, 3), dtype=np.complex128),
    )
    selected_carrier = float(wall["initial_box"][0]["lower"]) - 0.005
    alignment = alignment_0 @ expm(selected_carrier * tangent)
    fibration = evaluator.fibration_packet(alignment, line_chart="y")
    original_fibration = normal_function_module.FIBRATION
    with tempfile.TemporaryDirectory(prefix="q79-selected-interval-audit-") as directory:
        path = Path(directory) / "selected_fibration.json"
        path.write_text(json.dumps(fibration), encoding="utf-8")
        normal_function_module.FIBRATION = path
        try:
            engine = Q79DeltaNormalFunction()
        finally:
            normal_function_module.FIBRATION = original_fibration
    engine.gauss_manin.residue_rows = types.MethodType(
        lambda _self, periods, a_value, b_value: evaluator.residue_rows(
            alignment,
            periods,
            a_value,
            b_value,
            line_chart="y",
        ),
        engine.gauss_manin,
    )
    return engine, evaluator, alignment


def point_audit(system: SelectedQ79IntervalSystem) -> dict:
    engine, evaluator, alignment = build_floating_engine()
    rows = []
    maximum_connection_difference = 0.0
    maximum_source_difference = 0.0
    maximum_residue_difference = 0.0
    maximum_connection_relative_difference = 0.0
    maximum_source_relative_difference = 0.0
    maximum_residue_relative_difference = 0.0
    maximum_interval_radius = 0.0
    for parameter in [0.0, 0.2295, 0.65, 0.73455287, 0.82, 1.0]:
        interval_connection, interval_source, interval_residue = (
            system.connection_source_residue(acb(format(parameter, ".17g")))
        )
        w_value = engine.root_transport.base + 1j * parameter
        connection, source, a_value, b_value = engine.connection_and_source(w_value)
        residue = np.column_stack(
            [
                evaluator.residue_rows(
                    alignment,
                    np.eye(5, dtype=np.complex128)[:, column],
                    a_value,
                    b_value,
                    line_chart="y",
                )
                for column in range(5)
            ]
        ) * engine.gauss_manin.period_length
        interval_connection_midpoint = np.asarray(
            [[midpoint(value) for value in row] for row in interval_connection]
        )
        interval_source_midpoint = np.asarray(
            [midpoint(value) for value in interval_source]
        )
        interval_residue_midpoint = np.asarray(
            [[midpoint(value) for value in row] for row in interval_residue]
        )
        connection_difference = float(
            np.max(abs(interval_connection_midpoint - connection))
        )
        source_difference = float(np.max(abs(interval_source_midpoint - source)))
        residue_difference = float(np.max(abs(interval_residue_midpoint - residue)))
        connection_relative_difference = connection_difference / max(
            1.0, float(np.max(abs(interval_connection_midpoint)))
        )
        source_relative_difference = source_difference / max(
            1.0, float(np.max(abs(interval_source_midpoint)))
        )
        residue_relative_difference = residue_difference / max(
            1.0, float(np.max(abs(interval_residue_midpoint)))
        )
        interval_radius = max(
            radius_upper(value)
            for values in [interval_connection, [interval_source], interval_residue]
            for row in values
            for value in (row if isinstance(row, list) else [row])
        )
        maximum_connection_difference = max(
            maximum_connection_difference, connection_difference
        )
        maximum_source_difference = max(maximum_source_difference, source_difference)
        maximum_residue_difference = max(maximum_residue_difference, residue_difference)
        maximum_connection_relative_difference = max(
            maximum_connection_relative_difference, connection_relative_difference
        )
        maximum_source_relative_difference = max(
            maximum_source_relative_difference, source_relative_difference
        )
        maximum_residue_relative_difference = max(
            maximum_residue_relative_difference, residue_relative_difference
        )
        maximum_interval_radius = max(maximum_interval_radius, interval_radius)
        rows.append(
            {
                "parameter": format(parameter, ".17g"),
                "connection_maximum_difference": connection_difference,
                "source_maximum_difference": source_difference,
                "residue_maximum_difference": residue_difference,
                "connection_relative_difference": connection_relative_difference,
                "source_relative_difference": source_relative_difference,
                "residue_relative_difference": residue_relative_difference,
                "maximum_interval_radius": interval_radius,
            }
        )
    if maximum_connection_relative_difference >= 2.0e-7:
        raise AssertionError(
            "ACB connection does not reproduce the floating engine: "
            f"{maximum_connection_relative_difference:.6e}; rows={rows!r}"
        )
    if maximum_source_relative_difference >= 2.0e-7:
        raise AssertionError(
            "ACB source does not reproduce the floating engine: "
            f"{maximum_source_relative_difference:.6e}; rows={rows!r}"
        )
    if maximum_residue_relative_difference >= 2.0e-8:
        raise AssertionError(
            "ACB residue rows do not reproduce the floating engine: "
            f"{maximum_residue_relative_difference:.6e}; rows={rows!r}"
        )
    return {
        "rows": rows,
        "maximum_connection_difference": maximum_connection_difference,
        "maximum_source_difference": maximum_source_difference,
        "maximum_residue_difference": maximum_residue_difference,
        "maximum_connection_relative_difference": (
            maximum_connection_relative_difference
        ),
        "maximum_source_relative_difference": maximum_source_relative_difference,
        "maximum_residue_relative_difference": maximum_residue_relative_difference,
        "maximum_point_ball_radius": maximum_interval_radius,
    }


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--output", type=Path, default=DEFAULT_OUTPUT)
    parser.add_argument("--dps", type=int, default=80)
    parser.add_argument("--order", type=int, default=28)
    parser.add_argument("--initial-step", type=float, default=0.015)
    parser.add_argument("--minimum-step", type=float, default=1.0e-10)
    parser.add_argument("--maximum-steps", type=int, default=20000)
    parser.add_argument("--point-audit-only", action="store_true")
    parser.add_argument("--skip-point-audit", action="store_true")
    parser.add_argument("--checkpoint", type=Path, default=DEFAULT_CHECKPOINT)
    parser.add_argument("--resume", action="store_true")
    parser.add_argument(
        "--path",
        choices=["local-lower-contour", "full-lower-contour", "straight"],
        default="local-lower-contour",
    )
    arguments = parser.parse_args()
    system = SelectedQ79IntervalSystem(dps=arguments.dps)
    audit = None if arguments.skip_point_audit else point_audit(system)
    if audit is not None:
        print(json.dumps(audit, indent=2, sort_keys=True))
    if arguments.point_audit_only:
        return 0
    if arguments.path == "straight":
        waypoints = [0 + 0j, 1 + 0j]
        path_name = "original selected straight base path"
    elif arguments.path == "full-lower-contour":
        waypoints = [
            0 + 0j,
            0 - 0.1j,
            1 - 0.1j,
            1 + 0j,
        ]
        path_name = "full lower diagnostic contour"
    else:
        waypoints = [
            0 + 0j,
            0.65 + 0j,
            0.65 - 0.1j,
            0.82 - 0.1j,
            0.82 + 0j,
            1 + 0j,
        ]
        path_name = "selected local lower contour"
    packet = execute_validated_path(
        system,
        waypoints=waypoints,
        path_name=path_name,
        order=arguments.order,
        initial_step=arguments.initial_step,
        minimum_step=arguments.minimum_step,
        maximum_steps=arguments.maximum_steps,
        checkpoint_path=arguments.checkpoint,
        resume=arguments.resume,
    )
    if audit is not None:
        packet["point_audit"] = audit
    packet["interval_system_diagnostics"] = {
        key: value
        for key, value in vars(system.diagnostics).items()
        if not isinstance(value, float) or math.isfinite(value)
    }
    dump(arguments.output, packet)
    print(json.dumps(packet["endpoint"], indent=2, sort_keys=True))
    print(json.dumps(packet["execution"], indent=2, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
