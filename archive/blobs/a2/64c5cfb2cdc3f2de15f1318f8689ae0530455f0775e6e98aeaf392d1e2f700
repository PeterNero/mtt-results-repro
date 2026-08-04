from __future__ import annotations

import math
import json
from pathlib import Path
from typing import Any

import numpy as np
from flint import acb

import q79genus2_period_transport as identity_engine
from q79_selected_alignment_genus2_root_transport import (
    Q79SelectedAlignmentRootTransport,
    decode_acb,
)
from q79genus2_root_transport import midpoint


SelectedTerm = tuple[int, int, acb]

SL3_GENERATORS = [
    np.asarray(value, dtype=np.complex128)
    for value in [
        [[0, 1, 0], [0, 0, 0], [0, 0, 0]],
        [[0, 0, 1], [0, 0, 0], [0, 0, 0]],
        [[0, 0, 0], [1, 0, 0], [0, 0, 0]],
        [[0, 0, 0], [0, 0, 1], [0, 0, 0]],
        [[0, 0, 0], [0, 0, 0], [1, 0, 0]],
        [[0, 0, 0], [0, 0, 0], [0, 1, 0]],
        [[1, 0, 0], [0, -1, 0], [0, 0, 0]],
        [[0, 0, 0], [0, 1, 0], [0, 0, -1]],
    ]
]


def add_term(
    row: dict[tuple[int, int], acb],
    key: tuple[int, int],
    value: acb,
) -> None:
    row[key] = row.get(key, acb(0)) + value


def derivative_terms(
    rows: list[list[SelectedTerm]],
    variable: str,
) -> list[list[SelectedTerm]]:
    result: list[list[SelectedTerm]] = []
    for row in rows:
        derivative: dict[tuple[int, int], acb] = {}
        for a_power, b_power, coefficient in row:
            if variable == "a" and a_power:
                add_term(
                    derivative,
                    (a_power - 1, b_power),
                    coefficient * a_power,
                )
            elif variable == "b" and b_power:
                add_term(
                    derivative,
                    (a_power, b_power - 1),
                    coefficient * b_power,
                )
        result.append(
            [
                (a_power, b_power, coefficient)
                for (a_power, b_power), coefficient in sorted(
                    derivative.items(), reverse=True
                )
            ]
        )
    return result


class Q79SelectedAlignmentPeriodRootTransport(
    Q79SelectedAlignmentRootTransport
):
    """Selected root transport with coefficient access for the period engine."""

    def __init__(
        self,
        fibration_path: Path,
        homology_convention: dict,
        omitted: complex = 2 + 3j,
        dps: int = 70,
        root_tolerance: float = 1.0e-35,
    ) -> None:
        super().__init__(
            fibration_path,
            homology_convention,
            omitted=omitted,
            dps=dps,
            root_tolerance=root_tolerance,
        )
        omitted_ball = acb(
            format(omitted.real, ".17g"), format(omitted.imag, ".17g")
        )
        transformed: list[dict[tuple[int, int], acb]] = [
            {} for _ in range(7)
        ]
        for t_power, row in enumerate(self.selected_coefficients):
            for inverse_power in range(t_power + 1):
                s_power = 6 - inverse_power
                scalar = (
                    math.comb(t_power, inverse_power)
                    * omitted_ball ** (t_power - inverse_power)
                )
                for a_power, b_power, coefficient in row:
                    add_term(
                        transformed[s_power],
                        (a_power, b_power),
                        coefficient * scalar,
                    )
        self.period_coefficients_ascending: list[list[SelectedTerm]] = [
            [
                (a_power, b_power, coefficient)
                for (a_power, b_power), coefficient in sorted(
                    row.items(), reverse=True
                )
            ]
            for row in transformed
        ]
        self.coefficient_terms = list(
            reversed(self.period_coefficients_ascending)
        )
        self.t_coefficient_terms = list(reversed(self.selected_coefficients))

    @staticmethod
    def coefficient_at(
        terms: list[SelectedTerm], a_value: acb, b_value: acb
    ) -> acb:
        value = acb(0)
        for a_power, b_power, coefficient in terms:
            value += coefficient * a_value**a_power * b_value**b_power
        return value


class Q79SelectedAlignmentGaussManin(
    identity_engine.Q79GenusTwoGaussManin
):
    """Gauss-Manin reduction for the selected interval sextic midpoint."""

    def __init__(
        self,
        _fibration_path: Path,
        root_transport: Q79SelectedAlignmentPeriodRootTransport,
        *,
        coordinate: str = "frozen_reciprocal",
        omitted: complex = 2 + 3j,
    ) -> None:
        packet = json.loads(Path(_fibration_path).read_text(encoding="utf-8"))
        self.transport = root_transport
        self.coordinate = coordinate
        self.omitted = omitted
        if coordinate == "frozen_reciprocal":
            self.basis_names = [f"s^{power} ds/U" for power in range(5)]
            self.coefficient_terms = root_transport.coefficient_terms
        elif coordinate == "t":
            self.basis_names = [f"t^{power} dt/u" for power in range(5)]
            self.coefficient_terms = root_transport.t_coefficient_terms
        else:
            raise ValueError(f"unsupported selected period chart: {coordinate}")
        self.a_derivative_terms = derivative_terms(
            self.coefficient_terms, "a"
        )
        self.b_derivative_terms = derivative_terms(
            self.coefficient_terms, "b"
        )
        self.period_length = midpoint(root_transport.period_length)
        self.maximum_reduction_condition_number = 0.0
        self.maximum_equilibrated_reduction_condition_number = 0.0
        self.maximum_reduction_relative_residual = 0.0
        self.connection_evaluation_count = 0
        self.high_precision_connection_evaluation_count = 0
        self.maximum_high_precision_solution_radius = 0.0
        self.high_precision_condition_threshold = 1.0e10
        alignment_rows = packet["source"]["alignment_interval"]
        self.alignment = np.asarray(
            [
                [midpoint(decode_acb(value)) for value in row]
                for row in alignment_rows
            ],
            dtype=np.complex128,
        )
        self.line_chart = packet["source"].get("line_chart", "y")
        if self.line_chart not in {"y", "z"}:
            raise ValueError("selected line chart must be y or z")

    @staticmethod
    def midpoint_coefficient(
        terms: list[SelectedTerm], a_value: complex, b_value: complex
    ) -> complex:
        return sum(
            midpoint(coefficient) * a_value**a_power * b_value**b_power
            for a_power, b_power, coefficient in terms
        )

    def fiber_data(
        self, w_value: complex
    ) -> tuple[complex, complex, np.ndarray, np.ndarray]:
        a_ball, b_ball = self.transport.ab_at(w_value)
        a_value = midpoint(a_ball)
        b_value = midpoint(b_ball)
        da_dw = 2 * self.period_length * b_value
        db_dw = self.period_length * (3 * a_value**2 - 1)
        descending = [
            self.midpoint_coefficient(terms, a_value, b_value)
            for terms in self.coefficient_terms
        ]
        derivative_descending = [
            self.midpoint_coefficient(a_terms, a_value, b_value) * da_dw
            + self.midpoint_coefficient(b_terms, a_value, b_value) * db_dw
            for a_terms, b_terms in zip(
                self.a_derivative_terms, self.b_derivative_terms
            )
        ]
        return (
            a_value,
            b_value,
            np.asarray(descending[::-1], dtype=np.complex128),
            np.asarray(derivative_descending[::-1], dtype=np.complex128),
        )

    def residue_rows(
        self, periods: np.ndarray, a_value: complex, b_value: complex
    ) -> np.ndarray:
        i0, i1 = self.physical_holomorphic_periods(periods)
        elliptic = np.asarray(
            [a_value, b_value, 1 + 0j], dtype=np.complex128
        )
        line = self.alignment @ elliptic
        rows: list[complex] = []
        for generator in SL3_GENERATORS:
            variation = self.alignment @ generator @ elliptic
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
            rows.append(constant * i0 + linear * i1)
        return np.asarray(rows, dtype=np.complex128)


def execute_selected_alignment_thimble_period(**kwargs: Any) -> dict:
    """Run the unchanged A118 period algorithm on the selected A127 carrier."""

    old_root = identity_engine.Q79GenusTwoRootTransport
    old_gauss_manin = identity_engine.Q79GenusTwoGaussManin
    identity_engine.Q79GenusTwoRootTransport = (
        Q79SelectedAlignmentPeriodRootTransport
    )
    identity_engine.Q79GenusTwoGaussManin = Q79SelectedAlignmentGaussManin
    try:
        return identity_engine.execute_thimble_period(**kwargs)
    finally:
        identity_engine.Q79GenusTwoRootTransport = old_root
        identity_engine.Q79GenusTwoGaussManin = old_gauss_manin
