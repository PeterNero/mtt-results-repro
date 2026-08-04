from __future__ import annotations

import math
from pathlib import Path

import numpy as np
import sympy as sp
from flint import acb, acb_poly, acb_series, ctx
from scipy.optimize import linear_sum_assignment


def load_json(path: Path) -> dict:
    import json

    return json.loads(path.read_text(encoding="utf-8"))


def midpoint(value: acb) -> complex:
    return complex(float(value.real.mid()), float(value.imag.mid()))


def radius_upper(value: acb) -> float:
    return math.nextafter(float(value.rad().upper()), math.inf)


def matrix_rows(value: np.ndarray | sp.Matrix) -> list[list[int]]:
    if isinstance(value, sp.MatrixBase):
        return [[int(value[row, column]) for column in range(value.cols)] for row in range(value.rows)]
    return [[int(entry) for entry in row] for row in value.tolist()]


def free_reduce(word: list[tuple[int, int]]) -> list[tuple[int, int]]:
    reduced: list[tuple[int, int]] = []
    for letter in word:
        if reduced and reduced[-1] == (letter[0], -letter[1]):
            reduced.pop()
        else:
            reduced.append(letter)
    return reduced


class Q79GenusTwoRootTransport:
    def __init__(
        self,
        fibration_path: Path,
        homology_convention: dict,
        omitted: complex = 0j,
        dps: int = 55,
        root_tolerance: float = 1.0e-28,
    ) -> None:
        ctx.dps = dps
        self.omitted = omitted
        self.root_tolerance = root_tolerance
        self.root_solve_count = 0
        self.projection_angle = math.pi / 7
        self.rotation = np.exp(-1j * self.projection_angle)
        self.base = 0.25 + 0.25j

        fibration = load_json(fibration_path)
        a, b, t, s = sp.symbols("a b t s")
        t_coefficients = [
            sp.sympify(value)
            for value in fibration["fiber_chart"][
                "f_coefficients_t_descending"
            ]
        ]
        f_ab = sum(
            coefficient * t ** (6 - index)
            for index, coefficient in enumerate(t_coefficients)
        )
        omitted_exact = sp.Rational(str(omitted.real)) + sp.I * sp.Rational(
            str(omitted.imag)
        )
        transformed = sp.Poly(
            sp.expand(s**6 * f_ab.subs(t, omitted_exact + 1 / s)), s
        ).all_coeffs()
        if len(transformed) != 7:
            raise AssertionError("transformed branch polynomial is not degree six")

        self.coefficient_terms: list[list[tuple[int, int, str, str]]] = []
        for expression in transformed:
            terms: list[tuple[int, int, str, str]] = []
            for (a_power, b_power), coefficient in sp.Poly(
                expression, a, b, domain=sp.QQ_I
            ).terms():
                terms.append(
                    (
                        a_power,
                        b_power,
                        str(sp.re(coefficient)),
                        str(sp.im(coefficient)),
                    )
                )
            self.coefficient_terms.append(terms)

        self.tau = acb(0, 1)
        self.period_length = acb("0.5").elliptic_k() * acb(2).sqrt()
        self.period_square = self.period_length**2
        self.period_cube = self.period_length**3

        base_unordered, base_radii_unordered = self.roots_at(self.base)
        base_order = np.argsort((self.rotation * base_unordered).real)
        self.base_roots = base_unordered[base_order]
        self.base_radii = [base_radii_unordered[index] for index in base_order]

        self.intersection = np.asarray(
            homology_convention["intersection_matrix"], dtype=object
        )
        self.chain_vectors = [
            np.asarray(vector, dtype=object).reshape(4, 1)
            for vector in homology_convention["chain_vectors_for_sigma_1_to_sigma_5"]
        ]
        self.positive = [
            np.eye(4, dtype=object)
            - vector @ vector.T @ self.intersection
            for vector in self.chain_vectors
        ]
        self.negative = [
            np.asarray(sp.Matrix(value.tolist()).inv().tolist(), dtype=object)
            for value in self.positive
        ]

    def ab_at(self, w_value: complex) -> tuple[acb, acb]:
        w_ball = acb(format(w_value.real, ".17g"), format(w_value.imag, ".17g"))
        series = acb_series([w_ball, acb(1)], 2).elliptic_p(self.tau)
        return series[0] / self.period_square, series[1] / (2 * self.period_cube)

    @staticmethod
    def coefficient_at(
        terms: list[tuple[int, int, str, str]], a_value: acb, b_value: acb
    ) -> acb:
        value = acb(0)
        for a_power, b_power, real, imaginary in terms:
            value += acb(real, imaginary) * a_value**a_power * b_value**b_power
        return value

    def roots_at(self, w_value: complex) -> tuple[np.ndarray, list[float]]:
        self.root_solve_count += 1
        a_value, b_value = self.ab_at(w_value)
        descending = [
            self.coefficient_at(terms, a_value, b_value)
            for terms in self.coefficient_terms
        ]
        roots = acb_poly(list(reversed(descending))).roots(
            tol=self.root_tolerance, maxprec=1024
        )
        if len(roots) != 6 or not all(root.is_finite() for root in roots):
            raise AssertionError(f"root isolation failed at {w_value!r}")
        return (
            np.asarray([midpoint(root) for root in roots], dtype=np.complex128),
            [radius_upper(root) for root in roots],
        )

    @staticmethod
    def match(
        previous: np.ndarray,
        unordered: np.ndarray,
        unordered_radii: list[float],
    ) -> tuple[np.ndarray, list[float], float]:
        costs = abs(previous[:, None] - unordered[None, :])
        rows, columns = linear_sum_assignment(costs)
        current = np.empty(6, dtype=np.complex128)
        radii = [0.0] * 6
        for row, column in zip(rows, columns):
            current[row] = unordered[column]
            radii[row] = unordered_radii[column]
        minimum_separation = min(
            abs(current[left] - current[right]) - radii[left] - radii[right]
            for left in range(6)
            for right in range(left)
        )
        if minimum_separation <= 0:
            raise AssertionError("pointwise root balls overlap")
        ratio = float(costs[rows, columns].max() / minimum_separation)
        return current, radii, ratio

    def advance(
        self,
        start: complex,
        end: complex,
        previous: np.ndarray,
        points: list[complex],
        trajectories: list[np.ndarray],
        radii_rows: list[list[float]],
        step_ratio: float,
        ratio_state: list[float],
        depth: int = 0,
    ) -> np.ndarray:
        unordered, unordered_radii = self.roots_at(end)
        current, radii, ratio = self.match(previous, unordered, unordered_radii)
        if ratio > step_ratio:
            if depth >= 24:
                raise AssertionError(f"root transport did not resolve at {end!r}")
            middle = (start + end) / 2
            middle_roots = self.advance(
                start,
                middle,
                previous,
                points,
                trajectories,
                radii_rows,
                step_ratio,
                ratio_state,
                depth + 1,
            )
            return self.advance(
                middle,
                end,
                middle_roots,
                points,
                trajectories,
                radii_rows,
                step_ratio,
                ratio_state,
                depth + 1,
            )
        ratio_state[0] = max(ratio_state[0], ratio)
        points.append(end)
        trajectories.append(current)
        radii_rows.append(radii)
        return current

    def braid_word(
        self, trajectory_rows: list[np.ndarray]
    ) -> tuple[list[tuple[int, int]], list[int], float]:
        order = list(range(6))
        word: list[tuple[int, int]] = []
        minimum_event_gap = 1.0
        for left_roots, right_roots in zip(
            trajectory_rows, trajectory_rows[1:]
        ):
            left = self.rotation * left_roots
            right = self.rotation * right_roots
            events: list[tuple[float, int, int, float]] = []
            for first in range(6):
                for second in range(first + 1, 6):
                    x0 = (left[first] - left[second]).real
                    x1 = (right[first] - right[second]).real
                    if x0 * x1 < 0:
                        parameter = x0 / (x0 - x1)
                        y = (
                            (1 - parameter) * (left[first] - left[second])
                            + parameter * (right[first] - right[second])
                        ).imag
                        events.append((parameter, first, second, y))
            events.sort()
            if len(events) > 1:
                minimum_event_gap = min(
                    minimum_event_gap,
                    min(
                        events[index + 1][0] - events[index][0]
                        for index in range(len(events) - 1)
                    ),
                )
            for _, first, second, y in events:
                first_position = order.index(first)
                second_position = order.index(second)
                if abs(first_position - second_position) != 1:
                    raise AssertionError("nonadjacent projected braid crossing")
                generator = min(first_position, second_position)
                left_label = order[generator]
                sign = 1 if (
                    (y > 0 and left_label == first)
                    or (y < 0 and left_label == second)
                ) else -1
                word.append((generator + 1, sign))
                order[generator], order[generator + 1] = (
                    order[generator + 1],
                    order[generator],
                )
        return word, order, minimum_event_gap

    def action(self, word: list[tuple[int, int]]) -> np.ndarray:
        action = np.eye(4, dtype=object)
        for generator, sign in word:
            action = (
                self.positive if sign == 1 else self.negative
            )[generator - 1] @ action
        return action

    def endpoint_permutation(self, final_roots: np.ndarray) -> list[int]:
        permutation = [
            int(np.argmin(abs(final_roots[label] - self.base_roots)))
            for label in range(6)
        ]
        if sorted(permutation) != list(range(6)):
            raise AssertionError("endpoint matching is not a root permutation")
        return permutation
