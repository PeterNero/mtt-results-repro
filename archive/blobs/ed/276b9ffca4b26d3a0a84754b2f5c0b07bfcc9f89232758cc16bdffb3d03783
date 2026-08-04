from __future__ import annotations

import json
import math
from pathlib import Path

import numpy as np
import sympy as sp
from flint import acb, acb_poly, arb, ctx

from q79genus2_root_transport import (
    Q79GenusTwoRootTransport,
    midpoint,
    radius_upper,
)


def load(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def decode_acb(value: dict[str, str]) -> acb:
    return acb(arb(value["real"]), arb(value["imaginary"]))


class Q79SelectedAlignmentRootTransport(Q79GenusTwoRootTransport):
    """Root transport for the selected-alignment interval binary sextic.

    The distinguished path packet certifies avoidance of the three L1=0
    points, so the fixed y-line chart t=z/x is valid on every executed path.
    """

    def __init__(
        self,
        fibration_seed_path: Path,
        homology_convention: dict,
        *,
        omitted: complex | None = 2 + 3j,
        dps: int = 70,
        root_tolerance: float = 1.0e-35,
    ) -> None:
        ctx.dps = dps
        self.omitted = omitted
        self.root_tolerance = root_tolerance
        self.root_solve_count = 0
        self.projection_angle = math.pi / 7
        self.rotation = np.exp(-1j * self.projection_angle)
        self.base = 0.25 + 0.25j

        packet = load(fibration_seed_path)
        rows = packet["fiber_polynomials"]["F6"]
        if len(rows) != 7:
            raise AssertionError("selected F6 coefficient inventory changed")
        self.selected_coefficients: list[list[tuple[int, int, acb]]] = []
        for row in rows:
            self.selected_coefficients.append(
                [
                    (
                        int(term["a_power"]),
                        int(term["b_power"]),
                        decode_acb(term["coefficient"]),
                    )
                    for term in row
                ]
            )

        # Reuse the exact square-elliptic uniformization and braid action.
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
            for vector in homology_convention[
                "chain_vectors_for_sigma_1_to_sigma_5"
            ]
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

    def coefficient_at_selected(
        self, terms: list[tuple[int, int, acb]], a_value: acb, b_value: acb
    ) -> acb:
        value = acb(0)
        for a_power, b_power, coefficient in terms:
            value += coefficient * a_value**a_power * b_value**b_power
        return value

    def braid_word(
        self,
        trajectory_rows: list[np.ndarray],
        initial_order: list[int] | None = None,
    ) -> tuple[list[tuple[int, int]], list[int], float]:
        order = list(range(6)) if initial_order is None else list(initial_order)
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
                        y_value = (
                            (1 - parameter) * (left[first] - left[second])
                            + parameter * (right[first] - right[second])
                        ).imag
                        events.append((parameter, first, second, y_value))
            events.sort()
            if len(events) > 1:
                minimum_event_gap = min(
                    minimum_event_gap,
                    min(
                        events[index + 1][0] - events[index][0]
                        for index in range(len(events) - 1)
                    ),
                )
            for _parameter, first, second, y_value in events:
                first_position = order.index(first)
                second_position = order.index(second)
                if abs(first_position - second_position) != 1:
                    raise AssertionError("nonadjacent projected braid crossing")
                generator = min(first_position, second_position)
                left_label = order[generator]
                sign = 1 if (
                    (y_value > 0 and left_label == first)
                    or (y_value < 0 and left_label == second)
                ) else -1
                word.append((generator + 1, sign))
                order[generator], order[generator + 1] = (
                    order[generator + 1],
                    order[generator],
                )
        return word, order, minimum_event_gap

    def roots_at(self, w_value: complex) -> tuple[np.ndarray, list[float]]:
        self.root_solve_count += 1
        a_value, b_value = self.ab_at(w_value)
        ascending = [
            self.coefficient_at_selected(terms, a_value, b_value)
            for terms in self.selected_coefficients
        ]
        if self.omitted is not None:
            omitted = acb(
                format(self.omitted.real, ".17g"),
                format(self.omitted.imag, ".17g"),
            )
            transformed = [acb(0) for _ in range(7)]
            for t_power, coefficient in enumerate(ascending):
                for inverse_power in range(t_power + 1):
                    s_power = 6 - inverse_power
                    transformed[s_power] += (
                        coefficient
                        * math.comb(t_power, inverse_power)
                        * omitted ** (t_power - inverse_power)
                    )
            ascending = transformed
        roots = acb_poly(ascending).roots(
            tol=self.root_tolerance,
            maxprec=2048,
        )
        if len(roots) != 6 or not all(root.is_finite() for root in roots):
            raise AssertionError(f"selected root isolation failed at {w_value!r}")
        return (
            np.asarray([midpoint(root) for root in roots], dtype=np.complex128),
            [radius_upper(root) for root in roots],
        )
