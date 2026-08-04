from __future__ import annotations

import argparse
import json
from pathlib import Path

import numpy as np
import sympy as sp
from flint import acb, acb_mat
from scipy.integrate import solve_ivp

from q79genus2_period_transport import (
    FORM_NAMES,
    Q79GenusTwoGaussManin,
    complex_pair,
)
from q79genus2_root_transport import Q79GenusTwoRootTransport, midpoint


ROOT = Path(__file__).resolve().parents[1]
FIBRATION = (
    ROOT
    / "candidate_data"
    / "selected_q79genus2lefschetzperiodreduction"
    / "explicit_genus2_fibration.packet.json"
)
MONODROMY = (
    ROOT
    / "candidate_data"
    / "selected_q79genus2picardlefschetzmonodromyexecution"
    / "numerical_monodromy_exploration.packet.json"
)
HANDLE_PERIODS = (
    ROOT
    / "candidate_data"
    / "selected_q79genus2handleandlerayperiodexecution"
    / "primitive_handle_periods.production.packet.json"
)
DISTINGUISHED_FAN = (
    ROOT
    / "candidate_data"
    / "selected_q79genus2distinguishedcutsystemandglobalrelation"
    / "distinguished_radial_fan.packet.json"
)
GLOBAL_FACTORIZATION = (
    ROOT
    / "candidate_data"
    / "selected_q79genus2distinguishedcutsystemandglobalrelation"
    / "global_integral_gauss_manin_factorization.packet.json"
)


def load_json(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def real_system_matrix(periods: np.ndarray) -> np.ndarray:
    return np.vstack([periods.real, periods.imag])


class Q79DeltaNormalFunction:
    """Inhomogeneous Gauss-Manin execution for the splitting divisor.

    The five affine de Rham forms are propagated because an even sextic has
    two points at infinity.  The physical Abel-Jacobi coordinates are the
    first two entries.  Summing both infinity sheets cancels every exact-term
    boundary value there, including the affine-chart pole contributions.
    """

    def __init__(self) -> None:
        self.fibration = load_json(FIBRATION)
        homology = load_json(MONODROMY)["homology_convention"]
        self.root_transport = Q79GenusTwoRootTransport(FIBRATION, homology)
        self.gauss_manin = Q79GenusTwoGaussManin(
            FIBRATION, self.root_transport
        )
        self.gauss_manin_reciprocal = Q79GenusTwoGaussManin(
            FIBRATION,
            self.root_transport,
            coordinate="frozen_reciprocal",
            omitted=0j,
        )

        a, b, t = sp.symbols("a b t")
        self.a_symbol = a
        self.b_symbol = b
        self.t_symbol = t
        coefficients = [
            sp.sympify(value)
            for value in self.fibration["fiber_chart"][
                "f_coefficients_t_descending"
            ]
        ]
        self.f_expression = sum(
            coefficient * t ** (6 - index)
            for index, coefficient in enumerate(coefficients)
        )
        self.q_expression = sp.expand(
            sp.sympify(self.fibration["splitting"]["q_ab"])
        )
        self.g_expression = sp.sympify(self.fibration["splitting"]["g_ab"])
        q_polynomial = sp.Poly(self.q_expression, t)
        if q_polynomial.degree() != 2:
            raise ValueError("the splitting divisor must be quadratic in t")
        s = sp.symbols("s")
        self.s_symbol = s
        self.q_reciprocal_expression = sp.cancel(
            s**2 * self.q_expression.subs(t, 1 / s)
        )
        self.g_reciprocal_expression = sp.cancel(
            s**3 * self.g_expression.subs(t, 1 / s)
        )
        self.f = sp.lambdify((a, b, t), self.f_expression, "numpy")
        self.f_t = sp.lambdify(
            (a, b, t), sp.diff(self.f_expression, t), "numpy"
        )
        self.g = sp.lambdify((a, b, t), self.g_expression, "numpy")
        self.g_reciprocal = sp.lambdify(
            (a, b, s), self.g_reciprocal_expression, "numpy"
        )
        self.q_coefficient_functions = {
            False: sp.lambdify(
                (a, b), sp.Poly(self.q_expression, t).all_coeffs(), "numpy"
            ),
            True: sp.lambdify(
                (a, b),
                sp.Poly(self.q_reciprocal_expression, s).all_coeffs(),
                "numpy",
            ),
        }
        self.q_derivative_functions = {
            False: sp.lambdify(
                (a, b, t),
                (
                    sp.diff(self.q_expression, a),
                    sp.diff(self.q_expression, b),
                    sp.diff(self.q_expression, t),
                ),
                "numpy",
            ),
            True: sp.lambdify(
                (a, b, s),
                (
                    sp.diff(self.q_reciprocal_expression, a),
                    sp.diff(self.q_reciprocal_expression, b),
                    sp.diff(self.q_reciprocal_expression, s),
                ),
                "numpy",
            ),
        }

        handle_packet = load_json(HANDLE_PERIODS)
        self.base_periods = np.asarray(
            [
                [
                    complex(float(value["real"]), float(value["imaginary"]))
                    for value in row
                ]
                for row in handle_packet["marking"][
                    "base_holomorphic_period_matrix"
                ]
            ],
            dtype=np.complex128,
        )
        self.base_period_real_system = real_system_matrix(self.base_periods)
        self.maximum_reduction_condition_number = 0.0
        self.maximum_equilibrated_condition_number = 0.0
        self.high_precision_reduction_count = 0
        self.high_precision_condition_threshold = 1.0e7

    def high_precision_reduction(
        self, w_value: complex, gauss_manin: Q79GenusTwoGaussManin
    ) -> np.ndarray:
        a_value, b_value = self.root_transport.ab_at(w_value)
        da_dw = acb(2) * gauss_manin.period_length * b_value
        db_dw = gauss_manin.period_length * (
            acb(3) * a_value**2 - acb(1)
        )
        descending = [
            self.root_transport.coefficient_at(terms, a_value, b_value)
            for terms in gauss_manin.coefficient_terms
        ]
        derivative_descending = [
            self.root_transport.coefficient_at(a_terms, a_value, b_value)
            * da_dw
            + self.root_transport.coefficient_at(b_terms, a_value, b_value)
            * db_dw
            for a_terms, b_terms in zip(
                gauss_manin.a_derivative_terms,
                gauss_manin.b_derivative_terms,
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
        solutions = np.empty((5, 11), dtype=np.complex128)
        for power in range(5):
            for index in range(11):
                solutions[power, index] = midpoint(solved[index, power])
        self.high_precision_reduction_count += 1
        return solutions

    def exact_mumford_certificate(self) -> dict:
        a = self.a_symbol
        b = self.b_symbol
        t = self.t_symbol
        q = t**2 + b * t + a
        v = sp.rem(self.g_expression, q, t)
        elliptic = b**2 - a**3 + a
        groebner = sp.groebner([q, elliptic], t, b, a, order="lex")
        f_minus_v_squared = groebner.reduce(
            sp.expand(self.f_expression - v**2)
        )[1]
        g_minus_v = sp.rem(self.g_expression - v, q, t)
        discriminant_residual = sp.expand(
            (b**2 - 4 * a) - (a**3 - 5 * a)
        )
        discriminant_residual = sp.rem(
            discriminant_residual, elliptic, b
        )
        return {
            "base_curve": "b^2=a^3-a",
            "balanced_even_sextic_divisor": (
                "P_1+P_2-P_infinity_plus-P_infinity_minus"
            ),
            "q_monic": str(q),
            "v_equals_g_mod_q": str(sp.expand(v)),
            "degree_q": int(sp.degree(q, t)),
            "degree_v": int(sp.degree(v, t)),
            "g_minus_v_mod_q": str(sp.expand(g_minus_v)),
            "f_minus_v_squared_mod_q_and_base_curve": str(
                sp.expand(f_minus_v_squared)
            ),
            "q_discriminant": "b^2-4*a=a^3-5*a",
            "q_discriminant_identity_residual": str(
                sp.expand(discriminant_residual)
            ),
            "all_exact_checks_pass": bool(
                g_minus_v == 0
                and f_minus_v_squared == 0
                and discriminant_residual == 0
                and sp.degree(v, t) < sp.degree(q, t)
            ),
        }

    def integrate_fixed_fiber_segment(
        self,
        state: np.ndarray,
        z,
        dz,
        *,
        rtol: float,
        atol: float,
        form_powers: np.ndarray | None = None,
        form_scale: complex = 1 + 0j,
    ) -> tuple[np.ndarray, int]:
        a_value = -1j
        b_value = 1 + 1j
        if form_powers is None:
            form_powers = np.arange(5)

        def differential(parameter: float, real_state: np.ndarray) -> np.ndarray:
            current = real_state[:6] + 1j * real_state[6:]
            t_value = z(parameter)
            displacement = dz(parameter)
            u_value = current[0]
            derivative = np.empty(6, dtype=np.complex128)
            derivative[0] = (
                self.f_t(a_value, b_value, t_value)
                * displacement
                * u_value
                / (2 * self.f(a_value, b_value, t_value))
            )
            derivative[1:] = (
                form_scale
                * t_value**form_powers
                * displacement
                / u_value
            )
            return np.concatenate([derivative.real, derivative.imag])

        solution = solve_ivp(
            differential,
            (0.0, 1.0),
            np.concatenate([state.real, state.imag]),
            rtol=rtol,
            atol=atol,
            method="DOP853",
        )
        if not solution.success:
            raise AssertionError(solution.message)
        endpoint = solution.y[:6, -1] + 1j * solution.y[6:, -1]
        return endpoint, int(solution.nfev)

    def integrate_line(
        self,
        state: np.ndarray,
        start: complex,
        end: complex,
        *,
        rtol: float,
        atol: float,
        form_powers: np.ndarray | None = None,
        form_scale: complex = 1 + 0j,
    ) -> tuple[np.ndarray, int]:
        return self.integrate_fixed_fiber_segment(
            state,
            lambda parameter: start + parameter * (end - start),
            lambda _parameter: end - start,
            rtol=rtol,
            atol=atol,
            form_powers=form_powers,
            form_scale=form_scale,
        )

    def integrate_circle(
        self,
        state: np.ndarray,
        center: complex,
        radius: float,
        *,
        rtol: float,
        atol: float,
        form_powers: np.ndarray | None = None,
        form_scale: complex = 1 + 0j,
    ) -> tuple[np.ndarray, int]:
        return self.integrate_fixed_fiber_segment(
            state,
            lambda parameter: center
            + radius * np.exp(2j * np.pi * parameter),
            lambda parameter: 2j
            * np.pi
            * radius
            * np.exp(2j * np.pi * parameter),
            rtol=rtol,
            atol=atol,
            form_powers=form_powers,
            form_scale=form_scale,
        )

    def base_abel_jacobi_lift(
        self, *, rtol: float, atol: float, reciprocal: bool = False
    ) -> tuple[np.ndarray, dict]:
        a_value = -1j
        b_value = 1 + 1j
        q_roots = np.sort_complex(np.roots([1, b_value, a_value]))
        coefficients = np.asarray(
            [
                complex(
                    sp.N(
                        sp.sympify(value).subs(
                            {
                                self.a_symbol: -sp.I,
                                self.b_symbol: 1 + sp.I,
                            }
                        ),
                        17,
                    )
                )
                for value in self.fibration["fiber_chart"][
                    "f_coefficients_t_descending"
                ]
            ],
            dtype=np.complex128,
        )
        branch_points = np.roots(coefficients)
        winding_branch = branch_points[np.argmax(branch_points.imag)]
        winding_radius = 0.12
        other_clearance = min(
            abs(winding_branch - other) - winding_radius
            for other in branch_points
            if other != winding_branch
        )
        if other_clearance <= 0:
            raise AssertionError("base-chain winding circle encloses another root")

        outer = 20 + 7j
        outer_u = np.sqrt(self.f(a_value, b_value, outer))
        asymptotic = np.sqrt(coefficients[0]) * outer**3
        if abs(-outer_u - asymptotic) < abs(outer_u - asymptotic):
            outer_u = -outer_u

        right_root = q_roots[-1]
        left_root = q_roots[0]
        circle_start = winding_branch + winding_radius
        right_state = np.concatenate(
            [[outer_u], np.zeros(5, dtype=np.complex128)]
        )
        form_powers = (
            np.asarray([1, 0, -1, -2, -3])
            if reciprocal
            else np.arange(5)
        )
        form_scale = -1 + 0j if reciprocal else 1 + 0j
        evaluations = 0
        for kind, first, second in [
            ("line", outer, circle_start),
            ("circle", winding_branch, winding_radius),
            ("line", circle_start, outer),
            ("line", outer, right_root),
        ]:
            if kind == "line":
                right_state, count = self.integrate_line(
                    right_state,
                    first,
                    second,
                    rtol=rtol,
                    atol=atol,
                    form_powers=form_powers,
                    form_scale=form_scale,
                )
            else:
                right_state, count = self.integrate_circle(
                    right_state,
                    first,
                    second,
                    rtol=rtol,
                    atol=atol,
                    form_powers=form_powers,
                    form_scale=form_scale,
                )
            evaluations += count

        left_state = np.concatenate(
            [[-outer_u], np.zeros(5, dtype=np.complex128)]
        )
        left_state, count = self.integrate_line(
            left_state,
            outer,
            left_root,
            rtol=rtol,
            atol=atol,
            form_powers=form_powers,
            form_scale=form_scale,
        )
        evaluations += count

        right_sheet_residual = abs(
            right_state[0] - self.g(a_value, b_value, right_root)
        )
        left_sheet_residual = abs(
            left_state[0] - self.g(a_value, b_value, left_root)
        )
        lift = right_state[1:] + left_state[1:]
        diagnostics = {
            "outer_point": complex_pair(outer),
            "wound_branch_point": complex_pair(winding_branch),
            "winding_radius": format(winding_radius, ".17g"),
            "winding_other_root_clearance": format(other_clearance, ".17g"),
            "q_roots": [complex_pair(value) for value in q_roots],
            "right_endpoint_sheet_residual": format(
                right_sheet_residual, ".17g"
            ),
            "left_endpoint_sheet_residual": format(
                left_sheet_residual, ".17g"
            ),
            "function_evaluations": evaluations,
            "coordinate": "s=1/t" if reciprocal else "t",
            "regularization": (
                "The two common outer tails on opposite infinity sheets cancel "
                "exactly; one branch-point winding sends the plus outer sheet "
                "to the required u=g sheet at the right q-root."
            ),
        }
        return lift, diagnostics

    def connection_and_source(
        self, w_value: complex, *, reciprocal: bool = False
    ) -> tuple[np.ndarray, np.ndarray, complex, complex]:
        gauss_manin = (
            self.gauss_manin_reciprocal if reciprocal else self.gauss_manin
        )
        a_value, b_value, coefficients, derivative = (
            gauss_manin.fiber_data(w_value)
        )
        polynomial_derivative = np.asarray(
            [index * coefficients[index] for index in range(1, 7)],
            dtype=np.complex128,
        )
        columns: list[np.ndarray] = []
        for power in range(6):
            column = np.zeros(11, dtype=np.complex128)
            if power:
                column += power * gauss_manin.shift(
                    coefficients, power - 1
                )
            column -= 0.5 * gauss_manin.shift(
                polynomial_derivative, power
            )
            columns.append(column)
        for power in range(5):
            columns.append(gauss_manin.shift(coefficients, power))
        reduction = np.column_stack(columns)
        self.maximum_reduction_condition_number = max(
            self.maximum_reduction_condition_number,
            float(np.linalg.cond(reduction)),
        )
        equilibrated = reduction.copy()
        left_scale = np.ones(11, dtype=np.float64)
        right_scale = np.ones(11, dtype=np.float64)
        for _ in range(4):
            row_norms = np.max(np.abs(equilibrated), axis=1)
            equilibrated /= row_norms[:, None]
            left_scale /= row_norms
            column_norms = np.max(np.abs(equilibrated), axis=0)
            equilibrated /= column_norms[None, :]
            right_scale /= column_norms
        self.maximum_equilibrated_condition_number = max(
            self.maximum_equilibrated_condition_number,
            float(np.linalg.cond(equilibrated)),
        )
        if (
            np.linalg.cond(equilibrated)
            > self.high_precision_condition_threshold
        ):
            solutions = self.high_precision_reduction(w_value, gauss_manin)
        else:
            solutions = np.asarray(
                [
                    right_scale
                    * np.linalg.solve(
                        equilibrated,
                        left_scale
                        * (-0.5 * gauss_manin.shift(derivative, power)),
                    )
                    for power in range(5)
                ]
            )
        connection = solutions[:, 6:]
        exact_terms = solutions[:, :6]

        da_dw = 2 * gauss_manin.period_length * b_value
        db_dw = gauss_manin.period_length * (3 * a_value**2 - 1)
        source = np.zeros(5, dtype=np.complex128)
        q_coefficients = np.asarray(
            self.q_coefficient_functions[reciprocal](a_value, b_value),
            dtype=np.complex128,
        )
        roots = np.roots(q_coefficients)
        for root in roots:
            q_a, q_b, q_coordinate = self.q_derivative_functions[reciprocal](
                a_value, b_value, root
            )
            root_derivative = -(
                q_a * da_dw + q_b * db_dw
            ) / q_coordinate
            if reciprocal:
                g_value = self.g_reciprocal(a_value, b_value, root)
            else:
                g_value = self.g(a_value, b_value, root)
            source += (
                exact_terms @ (root ** np.arange(6))
            ) / g_value
            source += (
                root ** np.arange(5) * root_derivative / g_value
            )
        return connection, source, a_value, b_value

    def execute_path(
        self,
        initial_lift: np.ndarray,
        z,
        dz,
        *,
        rtol: float,
        atol: float,
        accumulate_relative_periods: bool = True,
        reciprocal: bool = False,
    ) -> tuple[np.ndarray, np.ndarray, int]:
        if reciprocal and accumulate_relative_periods:
            raise ValueError(
                "reciprocal execution currently supports monodromy only"
            )
        period_count = len(FORM_NAMES) if accumulate_relative_periods else 0
        complex_length = 5 + period_count

        def differential(parameter: float, real_state: np.ndarray) -> np.ndarray:
            state = (
                real_state[:complex_length]
                + 1j * real_state[complex_length:]
            )
            w_value = z(parameter)
            displacement = dz(parameter)
            connection, source, a_value, b_value = (
                self.connection_and_source(w_value, reciprocal=reciprocal)
            )
            derivative = np.empty(complex_length, dtype=np.complex128)
            derivative[:5] = displacement * (
                connection @ state[:5] + source
            )
            if accumulate_relative_periods:
                derivative[5:] = (
                    self.gauss_manin.period_length
                    * displacement
                    * self.gauss_manin.residue_rows(
                        state[:5], a_value, b_value
                    )
                )
            return np.concatenate([derivative.real, derivative.imag])

        initial = np.concatenate(
            [initial_lift, np.zeros(period_count, dtype=np.complex128)]
        )
        solution = solve_ivp(
            differential,
            (0.0, 1.0),
            np.concatenate([initial.real, initial.imag]),
            rtol=rtol,
            atol=atol,
            method="DOP853",
        )
        if not solution.success:
            raise AssertionError(solution.message)
        endpoint = (
            solution.y[:complex_length, -1]
            + 1j * solution.y[complex_length:, -1]
        )
        return endpoint[:5], endpoint[5:], int(solution.nfev)

    def execute_handle(
        self,
        name: str,
        displacement: complex,
        initial_lift: np.ndarray,
        *,
        rtol: float,
        atol: float,
    ) -> dict:
        endpoint, relative_periods, evaluations = self.execute_path(
            initial_lift,
            lambda parameter: self.root_transport.base
            + parameter * displacement,
            lambda _parameter: displacement,
            rtol=rtol,
            atol=atol,
        )
        physical_jump = endpoint[:2] - initial_lift[:2]
        fitted = np.linalg.solve(
            self.base_period_real_system,
            np.concatenate([physical_jump.real, physical_jump.imag]),
        )
        integer_translation = np.rint(fitted).astype(int)
        reconstructed = self.base_periods @ integer_translation
        residual = physical_jump - reconstructed
        scaled_residual = np.linalg.norm(
            np.concatenate([residual.real, residual.imag])
        ) / max(
            np.linalg.norm(
                np.concatenate([physical_jump.real, physical_jump.imag])
            ),
            np.finfo(float).tiny,
        )
        return {
            "name": name,
            "base_path": (
                "w(s)=(1+i)/4+s" if name == "A" else "w(s)=(1+i)/4+i*s"
            ),
            "endpoint_lift": [complex_pair(value) for value in endpoint],
            "physical_jump": [complex_pair(value) for value in physical_jump],
            "fitted_homology_coordinates": [
                format(float(value), ".17g") for value in fitted
            ],
            "selected_integer_translation": integer_translation.tolist(),
            "translation_basis": ["a1", "b1", "a2", "b2"],
            "period_fit_residual": [complex_pair(value) for value in residual],
            "period_fit_scaled_residual": format(scaled_residual, ".17g"),
            "relative_period_form_order": FORM_NAMES,
            "relative_periods": [
                complex_pair(value) for value in relative_periods
            ],
            "function_evaluations": evaluations,
        }

    def execute_meridian(
        self,
        meridian: dict,
        factor: dict,
        initial_lift: np.ndarray,
        *,
        rtol: float,
        atol: float,
    ) -> dict:
        outbound = meridian["outbound_segment"]
        circle = meridian["positive_meridian"]
        base = complex(
            float(outbound["start"]["real"]),
            float(outbound["start"]["imaginary"]),
        )
        circle_start = complex(
            float(outbound["end"]["real"]),
            float(outbound["end"]["imaginary"]),
        )
        center = complex(
            float(circle["center"]["real"]),
            float(circle["center"]["imaginary"]),
        )
        center_a, center_b = self.root_transport.ab_at(center)
        if max(abs(midpoint(center_a)), abs(midpoint(center_b))) > 50:
            raise ValueError(
                "pole-adjacent meridian requires exact affine-relation "
                "completion instead of ill-conditioned direct continuation"
            )
        reciprocal = False
        radius = float(circle["radius"])
        start_angle = float(circle["start_angle"])
        expected_start = center + radius * np.exp(1j * start_angle)
        endpoint_match = abs(expected_start - circle_start)

        state = initial_lift.copy()
        evaluations = 0
        segments = [
            (
                lambda parameter: base
                + parameter * (circle_start - base),
                lambda _parameter: circle_start - base,
            ),
            (
                lambda parameter: center
                + radius
                * np.exp(1j * (start_angle + 2 * np.pi * parameter)),
                lambda parameter: 2j
                * np.pi
                * radius
                * np.exp(1j * (start_angle + 2 * np.pi * parameter)),
            ),
            (
                lambda parameter: circle_start
                + parameter * (base - circle_start),
                lambda _parameter: base - circle_start,
            ),
        ]
        for z, dz in segments:
            state, _unused_periods, count = self.execute_path(
                state,
                z,
                dz,
                rtol=rtol,
                atol=atol,
                accumulate_relative_periods=False,
                reciprocal=reciprocal,
            )
            evaluations += count

        coordinate_jump = state[:2] - initial_lift[:2]
        physical_jump = (
            np.asarray([-coordinate_jump[1], -coordinate_jump[0]])
            if reciprocal
            else coordinate_jump
        )
        fitted = np.linalg.solve(
            self.base_period_real_system,
            np.concatenate([physical_jump.real, physical_jump.imag]),
        )
        integer_translation = np.rint(fitted).astype(int)
        reconstructed = self.base_periods @ integer_translation
        residual = physical_jump - reconstructed
        scaled_residual = np.linalg.norm(
            np.concatenate([residual.real, residual.imag])
        ) / max(
            np.linalg.norm(
                np.concatenate([physical_jump.real, physical_jump.imag])
            ),
            np.finfo(float).tiny,
        )

        vanishing = np.asarray(
            factor["positive_vanishing_cycle_up_to_sign"], dtype=int
        )
        nonzero = np.flatnonzero(vanishing)
        multiplier = None
        if len(nonzero):
            pivot = int(nonzero[0])
            if integer_translation[pivot] % vanishing[pivot] == 0:
                candidate = integer_translation[pivot] // vanishing[pivot]
                if np.array_equal(integer_translation, candidate * vanishing):
                    multiplier = int(candidate)
        return {
            "distinguished_index": meridian["distinguished_index"],
            "root_id": meridian["root_id"],
            "gauss_manin_coordinate": "s=1/t" if reciprocal else "t",
            "circle_start_match_residual": format(endpoint_match, ".17g"),
            "physical_jump": [complex_pair(value) for value in physical_jump],
            "fitted_homology_coordinates": [
                format(float(value), ".17g") for value in fitted
            ],
            "selected_integer_translation": integer_translation.tolist(),
            "period_fit_scaled_residual": format(scaled_residual, ".17g"),
            "positive_vanishing_cycle_up_to_sign": vanishing.tolist(),
            "translation_vanishing_cycle_multiplier": multiplier,
            "zero_local_singularity_class": multiplier is not None,
            "function_evaluations": evaluations,
        }

    def run(
        self,
        *,
        rtol: float,
        atol: float,
        meridian_start: int = 0,
        meridian_limit: int = 0,
    ) -> dict:
        base_lift, base_diagnostics = self.base_abel_jacobi_lift(
            rtol=min(rtol * 0.01, 2.0e-12),
            atol=min(atol * 0.01, 2.0e-13),
        )
        handles = [
            self.execute_handle(
                "A", 1 + 0j, base_lift, rtol=rtol, atol=atol
            ),
            self.execute_handle(
                "B", 1j, base_lift, rtol=rtol, atol=atol
            ),
        ]
        meridian_rows: list[dict] = []
        if meridian_limit:
            fan = load_json(DISTINGUISHED_FAN)[
                "distinguished_positive_meridians"
            ]
            factors = load_json(GLOBAL_FACTORIZATION)["factors"]
            if len(fan) != len(factors):
                raise AssertionError("distinguished factor count mismatch")
            stop = min(meridian_start + meridian_limit, len(fan))
            for meridian, factor in zip(
                fan[meridian_start:stop], factors[meridian_start:stop]
            ):
                if meridian["root_id"] != factor["root_id"]:
                    raise AssertionError("distinguished factor order mismatch")
                meridian_rows.append(
                    self.execute_meridian(
                        meridian,
                        factor,
                        base_lift,
                        rtol=rtol,
                        atol=atol,
                    )
                )
        return {
            "schema": "MTTQ79DeltaNormalFunctionHandleExecution.v1",
            "status": (
                "EXACT_MUMFORD_SOURCE_AND_FLOATING_AFFINE_HANDLE_MONODROMY_CLOSED"
            ),
            "tolerances": {
                "relative": format(rtol, ".17g"),
                "absolute": format(atol, ".17g"),
            },
            "exact_mumford_source": self.exact_mumford_certificate(),
            "base_abel_jacobi_lift": {
                "basis": [f"t^{power} dt/u" for power in range(5)],
                "values": [complex_pair(value) for value in base_lift],
                "physical_coordinate_indices": [0, 1],
                "diagnostics": base_diagnostics,
            },
            "base_holomorphic_period_matrix": [
                [complex_pair(value) for value in row]
                for row in self.base_periods
            ],
            "handles": handles,
            "distinguished_meridians": meridian_rows,
            "distinguished_meridian_count": len(meridian_rows),
            "distinguished_meridian_start_zero_based": meridian_start,
            "reduction_diagnostics": {
                "maximum_raw_condition_number": format(
                    self.maximum_reduction_condition_number, ".17g"
                ),
                "maximum_equilibrated_condition_number": format(
                    self.maximum_equilibrated_condition_number, ".17g"
                ),
                "high_precision_reduction_count": (
                    self.high_precision_reduction_count
                ),
                "high_precision_condition_threshold": format(
                    self.high_precision_condition_threshold, ".17g"
                ),
            },
            "scope": {
                "exact": [
                    "balanced even-sextic Mumford source",
                    "inhomogeneous endpoint plus exact-term source formula",
                ],
                "floating": [
                    "base Abel-Jacobi lift",
                    "A/B affine translations",
                    "A/B eight-row relative periods",
                ],
                "not_yet_claimed": [
                    "interval enclosure",
                    "final Deligne beta vector z_8",
                    "integral branch ell_92",
                    "beta_C zero or nonzero",
                ],
            },
        }


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--output", type=Path, required=True)
    parser.add_argument("--rtol", type=float, default=2.0e-10)
    parser.add_argument("--atol", type=float, default=2.0e-12)
    parser.add_argument("--meridian-start", type=int, default=0)
    parser.add_argument("--meridian-limit", type=int, default=0)
    arguments = parser.parse_args()
    execution = Q79DeltaNormalFunction().run(
        rtol=arguments.rtol,
        atol=arguments.atol,
        meridian_start=arguments.meridian_start,
        meridian_limit=arguments.meridian_limit,
    )
    arguments.output.parent.mkdir(parents=True, exist_ok=True)
    arguments.output.write_text(
        json.dumps(execution, indent=2, sort_keys=True) + "\n",
        encoding="utf-8",
    )


if __name__ == "__main__":
    main()
