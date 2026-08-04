from __future__ import annotations

import json
from pathlib import Path

import numpy as np
import sympy as sp
from flint import acb, acb_mat
from numpy.polynomial.legendre import leggauss
from scipy.integrate import solve_ivp

from q79genus2_root_transport import (
    Q79GenusTwoRootTransport,
    midpoint,
    radius_upper,
)


FORM_NAMES = ["E12", "E13", "E21", "E23", "E31", "E32", "H1", "H2"]
SELECTED_LOCAL_DIRECT_CUTOFFS = {
    1: 0.13,
    3: 0.043,
    5: 0.024,
    37: 0.025,
    38: 0.30,
    40: 0.48,
    43: 0.25,
    45: 0.20,
    48: 0.49,
    49: 0.47,
    50: 0.30,
    59: 0.40,
    78: 0.009,
}
SELECTED_LOCAL_OUTER_ORDERS = {
    1: 64,
    3: 48,
    5: 48,
    37: 48,
    38: 64,
    40: 96,
    43: 32,
    45: 32,
    48: 128,
    49: 96,
    50: 64,
    59: 96,
    78: 48,
}


def load_json(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def complex_pair(value: complex) -> dict[str, str]:
    return {
        "real": format(value.real, ".17g"),
        "imaginary": format(value.imag, ".17g"),
    }


class Q79GenusTwoGaussManin:
    """Numerical compact-curve Gauss-Manin reduction in an affine chart.

    Five affine forms x^k dx/y, k=0,...,4, are propagated.  The fifth form
    keeps the even-sextic infinity contribution inside the reduction.  The
    eight A111 rows consume only dt/u and t dt/u; reciprocal-chart periods
    are converted to those two physical forms before residue evaluation.
    """

    def __init__(
        self,
        fibration_path: Path,
        root_transport: Q79GenusTwoRootTransport,
        *,
        coordinate: str = "t",
        omitted: complex = 0j,
    ) -> None:
        packet = load_json(fibration_path)
        a, b, t, s = sp.symbols("a b t s")
        t_descending = [
            sp.sympify(value)
            for value in packet["fiber_chart"]["f_coefficients_t_descending"]
        ]
        t_polynomial = sum(
            coefficient * t ** (6 - index)
            for index, coefficient in enumerate(t_descending)
        )
        if coordinate == "t":
            variable = t
            polynomial = t_polynomial
            self.basis_names = [f"t^{power} dt/u" for power in range(5)]
        elif coordinate == "frozen_reciprocal":
            if abs(omitted.imag) > 1.0e-15 or abs(omitted.real - round(omitted.real)) > 1.0e-15:
                raise ValueError("the frozen reciprocal chart requires an integral omitted point")
            omitted_exact = sp.Integer(round(omitted.real))
            variable = s
            polynomial = sp.cancel(
                s**6 * t_polynomial.subs(t, omitted_exact + 1 / s)
            )
            self.basis_names = [f"s^{power} ds/U" for power in range(5)]
        else:
            raise ValueError(f"unsupported Gauss-Manin coordinate: {coordinate}")
        poly = sp.Poly(sp.expand(polynomial), variable)
        if poly.degree() != 6:
            raise AssertionError("Gauss-Manin chart polynomial is not sextic")
        descending = poly.all_coeffs()
        self.coefficient_terms = [
            self.expression_terms(expression, a, b)
            for expression in descending
        ]
        self.a_derivative_terms = [
            self.expression_terms(sp.diff(expression, a), a, b)
            for expression in descending
        ]
        self.b_derivative_terms = [
            self.expression_terms(sp.diff(expression, b), a, b)
            for expression in descending
        ]
        self.coefficients = [
            sp.lambdify((a, b), value, "numpy") for value in descending
        ]
        self.a_derivatives = [
            sp.lambdify((a, b), sp.diff(value, a), "numpy")
            for value in descending
        ]
        self.b_derivatives = [
            sp.lambdify((a, b), sp.diff(value, b), "numpy")
            for value in descending
        ]
        self.transport = root_transport
        self.coordinate = coordinate
        self.omitted = omitted
        self.period_length = midpoint(root_transport.period_length)
        self.maximum_reduction_condition_number = 0.0
        self.maximum_equilibrated_reduction_condition_number = 0.0
        self.maximum_reduction_relative_residual = 0.0
        self.connection_evaluation_count = 0
        self.high_precision_connection_evaluation_count = 0
        self.maximum_high_precision_solution_radius = 0.0
        self.high_precision_condition_threshold = 1.0e10

    @staticmethod
    def expression_terms(
        expression: sp.Expr, a: sp.Symbol, b: sp.Symbol
    ) -> list[tuple[int, int, str, str]]:
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
        return terms

    @staticmethod
    def shift(polynomial: np.ndarray, power: int, size: int = 11) -> np.ndarray:
        result = np.zeros(size, dtype=np.complex128)
        result[power : power + len(polynomial)] = polynomial
        return result

    def fiber_data(
        self, w_value: complex
    ) -> tuple[complex, complex, np.ndarray, np.ndarray]:
        a_ball, b_ball = self.transport.ab_at(w_value)
        a_value = midpoint(a_ball)
        b_value = midpoint(b_ball)
        da_dw = 2 * self.period_length * b_value
        db_dw = self.period_length * (3 * a_value**2 - 1)
        coefficients = np.asarray(
            [function(a_value, b_value) for function in self.coefficients][::-1],
            dtype=np.complex128,
        )
        derivative = np.asarray(
            [
                derivative_a(a_value, b_value) * da_dw
                + derivative_b(a_value, b_value) * db_dw
                for derivative_a, derivative_b in zip(
                    self.a_derivatives, self.b_derivatives
                )
            ][::-1],
            dtype=np.complex128,
        )
        return a_value, b_value, coefficients, derivative

    def high_precision_connection(self, w_value: complex) -> np.ndarray:
        a_value, b_value = self.transport.ab_at(w_value)
        da_dw = acb(2) * self.period_length * b_value
        db_dw = self.period_length * (acb(3) * a_value**2 - acb(1))
        descending = [
            self.transport.coefficient_at(terms, a_value, b_value)
            for terms in self.coefficient_terms
        ]
        derivative_descending = [
            self.transport.coefficient_at(a_terms, a_value, b_value) * da_dw
            + self.transport.coefficient_at(b_terms, a_value, b_value) * db_dw
            for a_terms, b_terms in zip(
                self.a_derivative_terms, self.b_derivative_terms
            )
        ]
        coefficients = list(reversed(descending))
        derivative = list(reversed(derivative_descending))
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
        solved = reduction.solve(targets)
        connection = np.empty((5, 5), dtype=np.complex128)
        for power in range(5):
            for index in range(5):
                value = solved[6 + index, power]
                connection[power, index] = midpoint(value)
                self.maximum_high_precision_solution_radius = max(
                    self.maximum_high_precision_solution_radius,
                    radius_upper(value),
                )
        self.high_precision_connection_evaluation_count += 1
        return connection

    def connection(
        self, w_value: complex
    ) -> tuple[np.ndarray, complex, complex]:
        a_value, b_value, coefficients, derivative = self.fiber_data(w_value)
        polynomial_derivative = np.asarray(
            [index * coefficients[index] for index in range(1, 7)],
            dtype=np.complex128,
        )
        columns: list[np.ndarray] = []
        for power in range(6):
            column = np.zeros(11, dtype=np.complex128)
            if power:
                column += power * self.shift(coefficients, power - 1)
            column -= 0.5 * self.shift(polynomial_derivative, power)
            columns.append(column)
        for power in range(5):
            columns.append(self.shift(coefficients, power))
        reduction = np.column_stack(columns)
        condition = float(np.linalg.cond(reduction))
        self.maximum_reduction_condition_number = max(
            self.maximum_reduction_condition_number, condition
        )
        equilibrated = reduction.copy()
        left_scale = np.ones(11, dtype=np.float64)
        right_scale = np.ones(11, dtype=np.float64)
        for _ in range(4):
            row_norms = np.max(np.abs(equilibrated), axis=1)
            if np.any(row_norms == 0):
                raise AssertionError("zero row in Gauss-Manin reduction")
            equilibrated /= row_norms[:, None]
            left_scale /= row_norms
            column_norms = np.max(np.abs(equilibrated), axis=0)
            if np.any(column_norms == 0):
                raise AssertionError("zero column in Gauss-Manin reduction")
            equilibrated /= column_norms[None, :]
            right_scale /= column_norms
        equilibrated_condition = float(np.linalg.cond(equilibrated))
        self.maximum_equilibrated_reduction_condition_number = max(
            self.maximum_equilibrated_reduction_condition_number,
            equilibrated_condition,
        )
        use_high_precision = (
            equilibrated_condition > self.high_precision_condition_threshold
        )
        connection = (
            self.high_precision_connection(w_value)
            if use_high_precision
            else np.empty((5, 5), dtype=np.complex128)
        )
        for power in range(5):
            target = -0.5 * self.shift(derivative, power)
            if use_high_precision:
                solution = np.empty(11, dtype=np.complex128)
                solution[6:] = connection[power]
                solution[:6] = np.linalg.lstsq(
                    reduction[:, :6],
                    target - reduction[:, 6:] @ connection[power],
                    rcond=None,
                )[0]
            else:
                equilibrated_solution = np.linalg.solve(
                    equilibrated, left_scale * target
                )
                solution = right_scale * equilibrated_solution
                connection[power] = solution[6:]
            residual = np.linalg.norm(reduction @ solution - target) / max(
                np.linalg.norm(target), np.finfo(float).tiny
            )
            self.maximum_reduction_relative_residual = max(
                self.maximum_reduction_relative_residual, float(residual)
            )
        self.connection_evaluation_count += 1
        return connection, a_value, b_value

    def physical_holomorphic_periods(self, periods: np.ndarray) -> tuple[complex, complex]:
        if self.coordinate == "t":
            return periods[0], periods[1]
        # U=s^3 u, t=o+1/s, and dt=-ds/s^2.
        j0, j1 = periods[0], periods[1]
        return -j1, -(self.omitted * j1 + j0)

    def residue_rows(
        self, periods: np.ndarray, a_value: complex, b_value: complex
    ) -> np.ndarray:
        i0, i1 = self.physical_holomorphic_periods(periods)
        return np.asarray(
            [
                b_value * i0,
                i0,
                a_value * i1,
                i1,
                -(a_value**2) * i0 - a_value * b_value * i1,
                -a_value * b_value * i0 - (b_value**2) * i1,
                a_value * i0 - b_value * i1,
                a_value * i0 + 2 * b_value * i1,
            ],
            dtype=np.complex128,
        )


def transposed_pair(permutation: list[int]) -> tuple[int, int]:
    moved = [index for index, image in enumerate(permutation) if image != index]
    if len(moved) != 2 or permutation[moved[0]] != moved[1] or permutation[moved[1]] != moved[0]:
        raise AssertionError("endpoint permutation is not a transposition")
    return tuple(moved)


def initial_vanishing_periods(
    chart_roots: np.ndarray,
    pair: tuple[int, int],
    leading_coefficient: complex,
    omitted: complex,
    order: int,
    propagation_chart: str,
) -> tuple[np.ndarray, float]:
    nodes, weights = leggauss(order)
    theta = np.pi * (nodes + 1) / 2
    weights = np.pi * weights / 2
    first, second = chart_roots[pair[0]], chart_roots[pair[1]]
    midpoint_pair = (first + second) / 2
    half_difference = (second - first) / 2
    points = midpoint_pair + half_difference * np.cos(theta)
    remainder = np.full(order, leading_coefficient, dtype=np.complex128)
    for index, root in enumerate(chart_roots):
        if index not in pair:
            remainder *= points - root
    square_root = np.sqrt(remainder)
    for index in range(1, order):
        if abs(square_root[index] - square_root[index - 1]) > abs(
            -square_root[index] - square_root[index - 1]
        ):
            square_root[index] = -square_root[index]
    if propagation_chart == "t":
        t_points = omitted + 1 / points
        # The chord orientation fixes the common sign used by the existing
        # distinguished-thimble packets.
        periods = np.asarray(
            [
                2j * np.sum(weights * points * t_points**power / square_root)
                for power in range(5)
            ],
            dtype=np.complex128,
        )
    elif propagation_chart == "frozen_reciprocal":
        # With the same chord orientation, J_k=-2i int s^k/sqrt(R) dtheta.
        # Then I_0=-J_1 and I_1=-(o J_1+J_0), exactly reproducing the t-chart
        # initializer while avoiding powers of roots escaping to infinity.
        periods = np.asarray(
            [
                -2j * np.sum(weights * points**power / square_root)
                for power in range(5)
            ],
            dtype=np.complex128,
        )
    else:
        raise ValueError(f"unsupported propagation chart: {propagation_chart}")
    other_clearance = min(
        abs(root - midpoint_pair) / max(abs(half_difference), np.finfo(float).tiny)
        for index, root in enumerate(chart_roots)
        if index not in pair
    )
    return periods, float(other_clearance)


def execute_thimble_period(
    *,
    fibration_path: Path,
    homology_convention: dict,
    trajectory_path: Path,
    trajectory_packet: dict,
    critical_center: complex,
    omitted: complex,
    epsilon: float,
    inner_order: int,
    dps: int,
    root_step_ratio: float,
    rtol: float,
    atol: float,
    gauss_manin_chart: str = "t",
    local_direct_cutoff: float = 0.0,
    local_outer_order: int = 32,
    tail_outer_order: int = 24,
) -> dict:
    if not 0 < epsilon < 0.01:
        raise ValueError("epsilon must lie in (0,0.01)")
    if local_direct_cutoff and not epsilon < local_direct_cutoff < 1:
        raise ValueError("local direct cutoff must lie between epsilon and one")
    if local_outer_order < 8:
        raise ValueError("local outer quadrature order must be at least eight")
    if tail_outer_order < 8:
        raise ValueError("tail outer quadrature order must be at least eight")
    transport = Q79GenusTwoRootTransport(
        fibration_path,
        homology_convention,
        omitted=omitted,
        dps=dps,
    )
    gauss_manin = Q79GenusTwoGaussManin(
        fibration_path,
        transport,
        coordinate=gauss_manin_chart,
        omitted=omitted,
    )
    # The closest pair on the finite-radius meridian need not yet be the pair
    # that collides at its center.  The interval-certified endpoint
    # transposition identifies the vanishing pair without this ambiguity.
    with np.load(trajectory_path) as saved:
        saved_w = np.asarray(saved["w"], dtype=np.complex128)
        saved_roots = np.asarray(saved["roots"], dtype=np.complex128)
        if saved_roots.shape[1] != 6:
            raise AssertionError("saved trajectory root count")
    pair = transposed_pair(
        trajectory_packet["braid"]["final_root_permutation"]
    )

    base = transport.base
    displacement = critical_center - base
    start_parameter = 1 - epsilon
    start = base + start_parameter * displacement
    # Reuse the interval-certified incoming distinguished path.  Its first
    # closest-to-center point is the radial-to-meridian endpoint, before the
    # positive loop begins.  Only the short meridian-to-node segment must be
    # extended numerically.
    saved_distances = np.abs(saved_w - critical_center)
    saved_minimum = float(np.min(saved_distances))
    approach_candidates = np.flatnonzero(
        saved_distances <= saved_minimum * 1.001
    )
    if not len(approach_candidates):
        raise AssertionError("saved trajectory has no certified approach point")
    approach_index = int(approach_candidates[0])
    approach = complex(saved_w[approach_index])
    approach_roots = saved_roots[approach_index]
    points: list[complex] = []
    trajectories: list[np.ndarray] = []
    radii: list[list[float]] = []
    ratio_state = [0.0]
    chart_roots = transport.advance(
        approach,
        start,
        approach_roots,
        points,
        trajectories,
        radii,
        root_step_ratio,
        ratio_state,
    )
    a_ball, b_ball = transport.ab_at(start)
    transformed_leading = midpoint(
        transport.coefficient_at(
            transport.coefficient_terms[0], a_ball, b_ball
        )
    )
    initial_periods, initial_other_clearance = initial_vanishing_periods(
        chart_roots,
        pair,
        transformed_leading,
        omitted,
        inner_order,
        gauss_manin_chart,
    )
    tail_nodes, tail_weights = leggauss(tail_outer_order)
    tail_half_interval = epsilon / 2
    tail_parameters = start_parameter + tail_half_interval * (tail_nodes + 1)
    tail_integral = np.zeros(8, dtype=np.complex128)
    tail_current_w = start
    tail_current_roots = chart_roots
    tail_current_periods = initial_periods
    tail_minimum_clearance = initial_other_clearance
    for node_index, parameter in enumerate(tail_parameters):
        w_value = base + float(parameter) * displacement
        tail_current_roots = transport.advance(
            tail_current_w,
            w_value,
            tail_current_roots,
            points,
            trajectories,
            radii,
            root_step_ratio,
            ratio_state,
        )
        a_ball_tail, b_ball_tail = transport.ab_at(w_value)
        a_tail = midpoint(a_ball_tail)
        b_tail = midpoint(b_ball_tail)
        leading_tail = midpoint(
            transport.coefficient_at(
                transport.coefficient_terms[0],
                a_ball_tail,
                b_ball_tail,
            )
        )
        tail_periods, tail_clearance = initial_vanishing_periods(
            tail_current_roots,
            pair,
            leading_tail,
            omitted,
            inner_order,
            gauss_manin_chart,
        )
        if np.linalg.norm(
            tail_periods - tail_current_periods
        ) > np.linalg.norm(-tail_periods - tail_current_periods):
            tail_periods = -tail_periods
        tail_integral += (
            tail_half_interval
            * tail_weights[node_index]
            * gauss_manin.period_length
            * displacement
            * gauss_manin.residue_rows(tail_periods, a_tail, b_tail)
        )
        tail_minimum_clearance = min(
            tail_minimum_clearance, tail_clearance
        )
        tail_current_w = w_value
        tail_current_periods = tail_periods
    switch_parameter = start_parameter
    switch_periods = initial_periods
    switch_roots = chart_roots
    switch_other_clearance = initial_other_clearance
    local_minimum_clearance = initial_other_clearance
    local_integral = np.zeros(8, dtype=np.complex128)
    if local_direct_cutoff:
        switch_parameter = 1 - local_direct_cutoff
        switch = base + switch_parameter * displacement
        outer_nodes, outer_weights = leggauss(local_outer_order)
        half_interval = (start_parameter - switch_parameter) / 2
        midpoint_interval = (start_parameter + switch_parameter) / 2
        local_parameters = midpoint_interval + half_interval * outer_nodes
        current_w = start
        current_roots = chart_roots
        current_periods = initial_periods
        for node_index in np.argsort(-local_parameters):
            parameter = float(local_parameters[node_index])
            w_value = base + parameter * displacement
            current_roots = transport.advance(
                current_w,
                w_value,
                current_roots,
                points,
                trajectories,
                radii,
                root_step_ratio,
                ratio_state,
            )
            a_ball_node, b_ball_node = transport.ab_at(w_value)
            a_node = midpoint(a_ball_node)
            b_node = midpoint(b_ball_node)
            leading_node = midpoint(
                transport.coefficient_at(
                    transport.coefficient_terms[0],
                    a_ball_node,
                    b_ball_node,
                )
            )
            node_periods, node_clearance = initial_vanishing_periods(
                current_roots,
                pair,
                leading_node,
                omitted,
                inner_order,
                gauss_manin_chart,
            )
            if np.linalg.norm(node_periods - current_periods) > np.linalg.norm(
                -node_periods - current_periods
            ):
                node_periods = -node_periods
            local_integral += (
                half_interval
                * outer_weights[node_index]
                * gauss_manin.period_length
                * displacement
                * gauss_manin.residue_rows(node_periods, a_node, b_node)
            )
            local_minimum_clearance = min(
                local_minimum_clearance, node_clearance
            )
            current_w = w_value
            current_periods = node_periods
        switch_roots = transport.advance(
            current_w,
            switch,
            current_roots,
            points,
            trajectories,
            radii,
            root_step_ratio,
            ratio_state,
        )
        a_ball_switch, b_ball_switch = transport.ab_at(switch)
        leading_switch = midpoint(
            transport.coefficient_at(
                transport.coefficient_terms[0],
                a_ball_switch,
                b_ball_switch,
            )
        )
        switch_periods, switch_other_clearance = initial_vanishing_periods(
            switch_roots,
            pair,
            leading_switch,
            omitted,
            inner_order,
            gauss_manin_chart,
        )
        if np.linalg.norm(switch_periods - current_periods) > np.linalg.norm(
            -switch_periods - current_periods
        ):
            switch_periods = -switch_periods
        local_minimum_clearance = min(
            local_minimum_clearance, switch_other_clearance
        )
    initial_state = np.concatenate(
        [switch_periods, np.zeros(8, dtype=np.complex128)]
    )

    def differential(parameter: float, state: np.ndarray) -> np.ndarray:
        w_value = base + parameter * displacement
        connection, a_current, b_current = gauss_manin.connection(w_value)
        period_derivative = displacement * connection @ state[:5]
        integral_derivative = (
            gauss_manin.period_length
            * displacement
            * gauss_manin.residue_rows(state[:5], a_current, b_current)
        )
        return np.concatenate([period_derivative, integral_derivative])

    solution = solve_ivp(
        differential,
        (switch_parameter, 0.0),
        initial_state,
        method="DOP853",
        rtol=rtol,
        atol=atol,
    )
    if not solution.success:
        raise AssertionError(solution.message)
    main_integral = -solution.y[5:, -1]
    result = main_integral + local_integral + tail_integral
    base_periods = solution.y[:5, -1]
    physical_i0, physical_i1 = gauss_manin.physical_holomorphic_periods(
        base_periods
    )
    return {
        "form_names": FORM_NAMES,
        "period_values": [complex_pair(value) for value in result],
        "base_fiber_propagated_periods": [
            {"form": name, "value": complex_pair(value)}
            for name, value in zip(gauss_manin.basis_names, base_periods)
        ],
        "base_fiber_holomorphic_periods_dt_over_u_and_t_dt_over_u": [
            complex_pair(physical_i0),
            complex_pair(physical_i1),
        ],
        "orientation_convention": "The endpoint chord is oriented from the lower saved root-label index to the higher index; simultaneous sign reversal is an integral thimble basis change.",
        "colliding_saved_root_labels": sorted(pair),
        "numerics": {
            "endpoint_cutoff_epsilon": format(epsilon, ".17g"),
            "initial_colliding_root_separation_in_frozen_chart": format(
                abs(chart_roots[pair[0]] - chart_roots[pair[1]]), ".17g"
            ),
            "initial_other_root_normalized_clearance": format(
                initial_other_clearance, ".17g"
            ),
            "local_direct_cutoff": format(local_direct_cutoff, ".17g"),
            "local_outer_Gauss_Legendre_order": local_outer_order,
            "endpoint_tail_Gauss_Legendre_order": tail_outer_order,
            "endpoint_tail_minimum_other_root_normalized_clearance": format(
                tail_minimum_clearance, ".17g"
            ),
            "local_direct_minimum_other_root_normalized_clearance": format(
                local_minimum_clearance, ".17g"
            ),
            "switch_colliding_root_separation_in_frozen_chart": format(
                abs(switch_roots[pair[0]] - switch_roots[pair[1]]),
                ".17g",
            ),
            "switch_other_root_normalized_clearance": format(
                switch_other_clearance, ".17g"
            ),
            "inner_Gauss_Legendre_order": inner_order,
            "working_decimal_digits": dps,
            "ODE_method": "DOP853",
            "ODE_rtol": format(rtol, ".17g"),
            "ODE_atol": format(atol, ".17g"),
            "Gauss_Manin_coordinate": gauss_manin_chart,
            "ODE_function_evaluations": solution.nfev,
            "root_transport_solve_count": transport.root_solve_count,
            "root_transport_step_ratio_limit": format(
                root_step_ratio, ".17g"
            ),
            "saved_trajectory_approach_index": approach_index,
            "saved_trajectory_approach_distance": format(
                abs(approach - critical_center), ".17g"
            ),
            "root_transport_maximum_step_ratio": format(
                ratio_state[0], ".17g"
            ),
            "Gauss_Manin_connection_evaluations": gauss_manin.connection_evaluation_count,
            "high_precision_Gauss_Manin_connection_evaluations": gauss_manin.high_precision_connection_evaluation_count,
            "high_precision_condition_threshold": format(
                gauss_manin.high_precision_condition_threshold, ".17g"
            ),
            "maximum_high_precision_solution_radius": format(
                gauss_manin.maximum_high_precision_solution_radius, ".17g"
            ),
            "maximum_reduction_condition_number": format(
                gauss_manin.maximum_reduction_condition_number, ".17g"
            ),
            "maximum_equilibrated_reduction_condition_number": format(
                gauss_manin.maximum_equilibrated_reduction_condition_number,
                ".17g",
            ),
            "maximum_reduction_relative_residual": format(
                gauss_manin.maximum_reduction_relative_residual, ".17g"
            ),
            "tail_model": "desingularized direct-cycle Gauss-Legendre quadrature",
        },
        "strict_scope": {
            "Picard_Fuchs_continuation_executed": True,
            "direct_chord_used_only_inside_the_single_node_neighborhood": True,
            "desingularized_local_direct_segment_executed": bool(
                local_direct_cutoff
            ),
            "desingularized_endpoint_tail_quadrature_executed": True,
            "floating_convergence_candidate": True,
            "high_precision_reduction_ball_solve_used": (
                gauss_manin.high_precision_connection_evaluation_count > 0
            ),
            "interval_certificate": False,
            "integral_H2_column_promoted": False,
        },
    }
