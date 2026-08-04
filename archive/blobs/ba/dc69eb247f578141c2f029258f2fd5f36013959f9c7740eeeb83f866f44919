from __future__ import annotations

from dataclasses import dataclass
import math

import numpy as np
from flint import acb, acb_mat, arb


def upper(value: arb) -> float:
    return math.nextafter(float(value.upper()), math.inf)


def lower(value: arb) -> float:
    return math.nextafter(float(value.lower()), -math.inf)


def midpoint_acb(value: acb) -> acb:
    return acb(str(value.real.mid()), str(value.imag.mid()))


def _as_acb(value: acb | arb | complex | float | int) -> acb:
    if isinstance(value, acb):
        return value
    if isinstance(value, arb):
        return acb(value)
    if isinstance(value, complex):
        return acb(format(value.real, ".17g"), format(value.imag, ".17g"))
    return acb(str(value))


@dataclass
class ComplexAffine:
    """Complex affine form on independent unit disks plus a uniform disk remainder."""

    center: acb
    coefficients: list[acb]
    remainder: arb

    @classmethod
    def constant(
        cls,
        value: acb | arb | complex | float | int,
        dimension: int,
    ) -> "ComplexAffine":
        return cls(_as_acb(value), [acb(0) for _ in range(dimension)], arb(0))

    @property
    def dimension(self) -> int:
        return len(self.coefficients)

    def coerce(self, value: object) -> "ComplexAffine":
        if isinstance(value, ComplexAffine):
            if value.dimension != self.dimension:
                raise ValueError("affine-form dimensions do not agree")
            return value
        return self.constant(value, self.dimension)  # type: ignore[arg-type]

    def linear_bound(self) -> arb:
        return sum((abs(value) for value in self.coefficients), arb(0))

    def absolute_bound(self) -> arb:
        return abs(self.center) + self.linear_bound() + self.remainder

    def centered_radius(self) -> arb:
        return self.center.rad() + self.linear_bound() + self.remainder

    def absolute_lower(self) -> float:
        return lower(abs(self.center)) - upper(self.linear_bound() + self.remainder)

    def __neg__(self) -> "ComplexAffine":
        return ComplexAffine(
            -self.center,
            [-value for value in self.coefficients],
            self.remainder,
        )

    def __add__(self, other: object) -> "ComplexAffine":
        right = self.coerce(other)
        return ComplexAffine(
            self.center + right.center,
            [left + value for left, value in zip(self.coefficients, right.coefficients)],
            self.remainder + right.remainder,
        )

    def __radd__(self, other: object) -> "ComplexAffine":
        return self + other

    def __sub__(self, other: object) -> "ComplexAffine":
        return self + (-self.coerce(other))

    def __rsub__(self, other: object) -> "ComplexAffine":
        return self.coerce(other) - self

    def __mul__(self, other: object) -> "ComplexAffine":
        right = self.coerce(other)
        left_linear = self.linear_bound()
        right_linear = right.linear_bound()
        remainder = (
            left_linear * right_linear
            + (abs(self.center) + left_linear) * right.remainder
            + (abs(right.center) + right_linear) * self.remainder
            + self.remainder * right.remainder
        )
        return ComplexAffine(
            self.center * right.center,
            [
                self.center * right_value + right.center * left_value
                for left_value, right_value in zip(
                    self.coefficients, right.coefficients
                )
            ],
            remainder,
        )

    def __rmul__(self, other: object) -> "ComplexAffine":
        return self * other

    def reciprocal(self) -> "ComplexAffine":
        if float(abs(self.center).lower()) <= 0.0:
            raise ZeroDivisionError("affine reciprocal center contains zero")
        candidate = ComplexAffine(
            acb(1) / self.center,
            [-(value / (self.center**2)) for value in self.coefficients],
            arb(0),
        )
        residual = self.constant(1, self.dimension) - self * candidate
        residual_bound = residual.absolute_bound()
        residual_upper = upper(residual_bound)
        if residual_upper >= 1.0:
            raise ZeroDivisionError(
                "affine reciprocal residual is not contractive: "
                f"{residual_upper:.6e}"
            )
        candidate.remainder += (
            candidate.absolute_bound()
            * residual_bound
            / (arb(1) - residual_bound)
        )
        return candidate

    def __truediv__(self, other: object) -> "ComplexAffine":
        return self * self.coerce(other).reciprocal()

    def __rtruediv__(self, other: object) -> "ComplexAffine":
        return self.coerce(other) / self

    def __pow__(self, power: int) -> "ComplexAffine":
        if power < 0:
            return self.reciprocal() ** (-power)
        result = self.constant(1, self.dimension)
        factor = self
        exponent = power
        while exponent:
            if exponent & 1:
                result *= factor
            exponent >>= 1
            if exponent:
                factor *= factor
        return result


def zero_like(prototype: ComplexAffine) -> ComplexAffine:
    return ComplexAffine.constant(0, prototype.dimension)


def matrix_vector(
    matrix: list[list[ComplexAffine]],
    vector: list[acb | ComplexAffine],
) -> list[ComplexAffine]:
    prototype = matrix[0][0]
    return [
        sum(
            (matrix[row][column] * vector[column] for column in range(len(vector))),
            zero_like(prototype),
        )
        for row in range(len(matrix))
    ]


def matrix_multiply(
    left: list[list[ComplexAffine]],
    right: list[list[ComplexAffine]],
) -> list[list[ComplexAffine]]:
    prototype = left[0][0]
    return [
        [
            sum(
                (left[row][inner] * right[inner][column] for inner in range(len(right))),
                zero_like(prototype),
            )
            for column in range(len(right[0]))
        ]
        for row in range(len(left))
    ]


def matrix_subtract(
    left: list[list[ComplexAffine]],
    right: list[list[ComplexAffine]],
) -> list[list[ComplexAffine]]:
    return [
        [left[row][column] - right[row][column] for column in range(len(left[0]))]
        for row in range(len(left))
    ]


def constant_left_multiply(
    matrix: acb_mat,
    right: list[list[ComplexAffine]],
) -> list[list[ComplexAffine]]:
    prototype = right[0][0]
    return [
        [
            sum(
                (matrix[row, inner] * right[inner][column] for inner in range(len(right))),
                zero_like(prototype),
            )
            for column in range(len(right[0]))
        ]
        for row in range(matrix.nrows())
    ]


def right_multiply_constant(
    matrix: list[list[ComplexAffine]],
    right: acb_mat,
) -> list[list[ComplexAffine]]:
    prototype = matrix[0][0]
    return [
        [
            sum(
                (matrix[row][inner] * right[inner, column] for inner in range(right.nrows())),
                zero_like(prototype),
            )
            for column in range(right.ncols())
        ]
        for row in range(len(matrix))
    ]


def constant_matrix(matrix: acb_mat, dimension: int) -> list[list[ComplexAffine]]:
    return [
        [ComplexAffine.constant(matrix[row, column], dimension) for column in range(matrix.ncols())]
        for row in range(matrix.nrows())
    ]


def _coefficient_matrix(
    matrix: list[list[ComplexAffine]],
    variable: int,
) -> acb_mat:
    return acb_mat(
        [
            [matrix[row][column].coefficients[variable] for column in range(len(matrix[0]))]
            for row in range(len(matrix))
        ]
    )


def _midpoint_center_matrix(matrix: list[list[ComplexAffine]]) -> acb_mat:
    return acb_mat(
        [
            [midpoint_acb(matrix[row][column].center) for column in range(len(matrix[0]))]
            for row in range(len(matrix))
        ]
    )


def weighted_verified_solve(
    matrix: list[list[ComplexAffine]],
    targets: list[list[ComplexAffine]],
) -> tuple[list[list[ComplexAffine]], dict]:
    """Solve A(z)X(z)=B(z), retaining the complete affine first variation."""

    size = len(matrix)
    if any(len(row) != size for row in matrix):
        raise ValueError("verified affine solve requires a square matrix")
    dimension = matrix[0][0].dimension
    center_matrix = _midpoint_center_matrix(matrix)
    center_targets = _midpoint_center_matrix(targets)
    inverse_ball = center_matrix.inv()
    inverse = acb_mat(
        [
            [midpoint_acb(inverse_ball[row, column]) for column in range(size)]
            for row in range(size)
        ]
    )
    center_solution = inverse * center_targets
    coefficient_solutions: list[acb_mat] = []
    for variable in range(dimension):
        coefficient_solutions.append(
            inverse
            * (
                _coefficient_matrix(targets, variable)
                - _coefficient_matrix(matrix, variable) * center_solution
            )
        )
    result = [
        [
            ComplexAffine(
                midpoint_acb(center_solution[row, column]),
                [
                    midpoint_acb(coefficient_solutions[variable][row, column])
                    for variable in range(dimension)
                ],
                arb(0),
            )
            for column in range(len(targets[0]))
        ]
        for row in range(size)
    ]

    identity = acb_mat(size, size)
    for index in range(size):
        identity[index, index] = acb(1)
    center_defect = identity - inverse * center_matrix
    variation = [
        [
            abs(matrix[row][column].center - center_matrix[row, column])
            + matrix[row][column].linear_bound()
            + matrix[row][column].remainder
            for column in range(size)
        ]
        for row in range(size)
    ]
    defect_bounds = [
        [
            abs(center_defect[row, column])
            + sum(
                (abs(inverse[row, inner]) * variation[inner][column] for inner in range(size)),
                arb(0),
            )
            for column in range(size)
        ]
        for row in range(size)
    ]
    floating_bounds = np.asarray(
        [[upper(value) for value in row] for row in defect_bounds],
        dtype=np.float64,
    )
    weights = np.ones(size, dtype=np.float64)
    for _ in range(512):
        updated = floating_bounds @ weights + 1.0e-300
        weights = updated / float(np.max(updated))
    weights = np.maximum(weights, 1.0e-300)
    weight_balls = [arb(format(float(value), ".17g")) for value in weights]
    weighted_rows = [
        sum(
            (
                defect_bounds[row][column] * weight_balls[column]
                for column in range(size)
            ),
            arb(0),
        )
        / weight_balls[row]
        for row in range(size)
    ]
    contraction = max(weighted_rows, key=upper)
    contraction_upper = upper(contraction)
    if contraction_upper >= 1.0:
        raise ZeroDivisionError(
            "verified affine midpoint inverse failed: "
            f"weighted contraction={contraction_upper:.6e}"
        )

    residual = matrix_subtract(targets, matrix_multiply(matrix, result))
    preconditioned_residual = constant_left_multiply(inverse, residual)
    maximum_error = 0.0
    column_error_uppers = []
    for column in range(len(targets[0])):
        residual_norm = max(
            (
                preconditioned_residual[row][column].absolute_bound()
                / weight_balls[row]
                for row in range(size)
            ),
            key=upper,
        )
        error_norm = residual_norm / (arb(1) - contraction)
        column_error = 0.0
        for row in range(size):
            component_error = error_norm * weight_balls[row]
            result[row][column].remainder += component_error
            component_upper = upper(component_error)
            maximum_error = max(maximum_error, component_upper)
            column_error = max(column_error, component_upper)
        column_error_uppers.append(column_error)
    return result, {
        "matrix_size": size,
        "target_column_count": len(targets[0]),
        "positive_weights": [float(value) for value in weights],
        "weighted_contraction_upper": contraction_upper,
        "maximum_solution_component_error_upper": maximum_error,
        "column_solution_error_uppers": column_error_uppers,
    }


def matrix_infinity_norm(matrix: acb_mat) -> arb:
    return max(
        (
            sum((abs(matrix[row, column]) for column in range(matrix.ncols())), arb(0))
            for row in range(matrix.nrows())
        ),
        key=upper,
    )


def exponential_chart_affine_source(
    alignment: acb_mat,
    generators: list[acb_mat],
    coordinate_disk_radius: arb,
) -> tuple[
    list[list[ComplexAffine]],
    list[list[list[ComplexAffine]]],
    dict,
]:
    """Enclose A exp(sum z_s G_s) and all coordinate derivatives affinely."""

    dimension = len(generators)
    generator_norms = [matrix_infinity_norm(generator) for generator in generators]
    z_norm = sum(
        (coordinate_disk_radius * value for value in generator_norms),
        arb(0),
    )
    exponential_tail = z_norm.exp() - arb(1) - z_norm
    alignment_row_sums = [
        sum((abs(alignment[row, column]) for column in range(alignment.ncols())), arb(0))
        for row in range(alignment.nrows())
    ]

    first_variations = [alignment * generator for generator in generators]
    affine_alignment = [
        [
            ComplexAffine(
                alignment[row, column],
                [
                    coordinate_disk_radius * first_variations[variable][row, column]
                    for variable in range(dimension)
                ],
                alignment_row_sums[row] * exponential_tail,
            )
            for column in range(alignment.ncols())
        ]
        for row in range(alignment.nrows())
    ]

    derivative_matrices: list[list[list[ComplexAffine]]] = []
    for direction, generator in enumerate(generators):
        center = first_variations[direction]
        first_derivatives = [
            alignment
            * (
                generators[variable] * generator
                + generator * generators[variable]
            )
            / acb(2)
            for variable in range(dimension)
        ]
        derivative_tail = generator_norms[direction] * exponential_tail
        derivative_matrices.append(
            [
                [
                    ComplexAffine(
                        center[row, column],
                        [
                            coordinate_disk_radius
                            * first_derivatives[variable][row, column]
                            for variable in range(dimension)
                        ],
                        alignment_row_sums[row] * derivative_tail,
                    )
                    for column in range(alignment.ncols())
                ]
                for row in range(alignment.nrows())
            ]
        )
    return affine_alignment, derivative_matrices, {
        "coordinate_complex_disk_radius_upper": upper(coordinate_disk_radius),
        "Z_matrix_infinity_norm_upper": upper(z_norm),
        "matrix_exponential_second_order_tail_upper": upper(exponential_tail),
        "maximum_generator_infinity_norm_upper": max(upper(value) for value in generator_norms),
        "maximum_alignment_affine_remainder_upper": max(
            upper(value * exponential_tail) for value in alignment_row_sums
        ),
        "maximum_alignment_derivative_affine_remainder_upper": max(
            upper(
                alignment_row_sums[row]
                * generator_norms[direction]
                * exponential_tail
            )
            for row in range(alignment.nrows())
            for direction in range(dimension)
        ),
    }
