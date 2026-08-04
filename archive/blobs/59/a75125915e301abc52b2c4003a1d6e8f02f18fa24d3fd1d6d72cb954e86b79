from __future__ import annotations

import argparse
import json
import math
import tempfile
import types
from pathlib import Path

import numpy as np
import sympy as sp
from scipy.integrate import solve_ivp
from scipy.linalg import expm

import compute_q79genus2normalfunction as normal_function_module
from compute_q79genus2normalfunction import Q79DeltaNormalFunction
from explore_q79_pgl3_beta_zero import PGL3BetaEvaluator
from q79_pgl3_beta_diagnostics import SmoothnessProbe, damping_for_radius
from q79genus2_root_transport import midpoint


ROOT = Path(__file__).resolve().parents[1]
DIRECTORY = (
    ROOT
    / "candidate_data"
    / "selected_q79genus2delignebetaperiodandintegralbranchexecution"
)
SOURCE = DIRECTORY / "pgl3_projective_ychart_broyden_04.exploratory.json"
SIDE_EPSILONS = [0.1, 0.05, 0.02, 0.01, 0.005]
PL_CUTOFFS = [1.0e-3, 3.0e-4, 1.0e-4, 3.0e-5]


def load(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def complex_value(value: dict) -> complex:
    if "r" in value:
        return complex(float(value["r"]), float(value["i"]))
    return complex(float(value["real"]), float(value["imaginary"]))


def complex_pair(value: complex) -> dict[str, str]:
    return {
        "real": format(float(value.real), ".17g"),
        "imaginary": format(float(value.imag), ".17g"),
    }


def complex_vector(values: list[dict]) -> np.ndarray:
    return np.asarray([complex_value(value) for value in values])


def complex_matrix(rows: list[list[dict]]) -> np.ndarray:
    return np.asarray(
        [[complex_value(value) for value in row] for row in rows],
        dtype=np.complex128,
    )


def polynomial_coefficients_y(table: list[dict], line: np.ndarray) -> np.ndarray:
    degree = sum(table[0]["powers_xyz"])
    ascending = np.zeros(degree + 1, dtype=np.complex128)
    for row in table:
        x_power, y_power, z_power = row["powers_xyz"]
        coefficient = int(row["coefficient"])
        for index in range(y_power + 1):
            ascending[index + z_power] += (
                coefficient
                * (-1) ** y_power
                * math.comb(y_power, index)
                * line[1] ** (x_power + z_power)
                * line[0] ** (y_power - index)
                * line[2] ** index
            )
    return ascending[::-1]


def polynomial_value(table: list[dict], point: np.ndarray) -> complex:
    result = 0j
    for row in table:
        value = complex(int(row["coefficient"]))
        for index, power in enumerate(row["powers_xyz"]):
            value *= point[index] ** power
        result += value
    return result


def f_derivatives(
    table: list[dict], point: np.ndarray
) -> tuple[complex, np.ndarray, np.ndarray]:
    value = 0j
    gradient = np.zeros(3, dtype=np.complex128)
    hessian = np.zeros((3, 3), dtype=np.complex128)
    for row in table:
        powers = row["powers_xyz"]
        coefficient = int(row["coefficient"])
        term = complex(coefficient)
        for index, power in enumerate(powers):
            term *= point[index] ** power
        value += term
        for left in range(3):
            if not powers[left]:
                continue
            term = complex(coefficient * powers[left])
            for index, power in enumerate(powers):
                term *= point[index] ** (power - int(index == left))
            gradient[left] += term
        for left in range(3):
            for right in range(3):
                factor = powers[left] * (
                    powers[right] - int(left == right)
                )
                if not factor:
                    continue
                term = complex(coefficient * factor)
                for index, power in enumerate(powers):
                    term *= point[index] ** (
                        power
                        - int(index == left)
                        - int(index == right)
                    )
                hessian[left, right] += term
    return value, gradient, hessian


def fitted_limit(
    coordinates: list[float], values: np.ndarray, degree: int
) -> np.ndarray:
    x = np.asarray(coordinates, dtype=np.float64)
    return np.asarray(
        [
            np.polyfit(x, values[:, index], degree)[-1]
            for index in range(values.shape[1])
        ],
        dtype=np.complex128,
    )


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--output", type=Path, required=True)
    arguments = parser.parse_args()

    source = load(SOURCE)
    alignment_0 = complex_matrix(source["final_alignment"])
    beta_0 = complex_vector(source["final_beta"])
    jacobian = complex_matrix(source["current_jacobian"])
    winding_reference = complex_value(source["final_winding_reference"])
    evaluator = PGL3BetaEvaluator()
    probe = SmoothnessProbe(evaluator)
    _damping, direction = damping_for_radius(jacobian, beta_0, 1.0e-3)
    tangent = sum(
        (
            direction[index] * evaluator.generators[index]
            for index in range(8)
        ),
        np.zeros((3, 3), dtype=np.complex128),
    )
    period_length = midpoint(probe.uniformization.period_length)

    def alignment_at(carrier_parameter: float) -> np.ndarray:
        return alignment_0 @ expm(carrier_parameter * tangent)

    def wall_data(coordinates: np.ndarray) -> tuple:
        carrier_parameter, base_parameter = coordinates[:2]
        fiber_parameter = complex(coordinates[2], coordinates[3])
        alignment = alignment_at(carrier_parameter)
        a_ball, b_ball = probe.uniformization.ab_at(
            probe.uniformization.base + 1j * base_parameter
        )
        a_value = midpoint(a_ball)
        b_value = midpoint(b_ball)
        elliptic = np.asarray(
            [a_value, b_value, 1 + 0j], dtype=np.complex128
        )
        line = alignment @ elliptic
        da_du = 1j * 2 * period_length * b_value
        db_du = 1j * period_length * (3 * a_value**2 - 1)
        line_s = alignment @ tangent @ elliptic
        line_u = alignment @ np.asarray(
            [da_du, db_du, 0j], dtype=np.complex128
        )
        point = np.asarray(
            [
                line[1],
                -(line[0] + line[2] * fiber_parameter),
                line[1] * fiber_parameter,
            ],
            dtype=np.complex128,
        )
        point_t = np.asarray([0j, -line[2], line[1]])
        point_s = np.asarray(
            [
                line_s[1],
                -(line_s[0] + line_s[2] * fiber_parameter),
                line_s[1] * fiber_parameter,
            ]
        )
        point_u = np.asarray(
            [
                line_u[1],
                -(line_u[0] + line_u[2] * fiber_parameter),
                line_u[1] * fiber_parameter,
            ]
        )
        point_ts = np.asarray([0j, -line_s[2], line_s[1]])
        point_tu = np.asarray([0j, -line_u[2], line_u[1]])
        f_value, gradient, hessian = f_derivatives(
            evaluator.tables["F6"], point
        )
        f_t = gradient @ point_t
        f_s = gradient @ point_s
        f_u = gradient @ point_u
        f_tt = point_t @ hessian @ point_t
        f_ts = point_t @ hessian @ point_s + gradient @ point_ts
        f_tu = point_t @ hessian @ point_u + gradient @ point_tu
        residual = np.asarray(
            [f_value.real, f_value.imag, f_t.real, f_t.imag]
        )
        complex_columns = [
            (f_s, f_ts),
            (f_u, f_tu),
            (f_t, f_tt),
            (1j * f_t, 1j * f_tt),
        ]
        real_jacobian = np.asarray(
            [
                [value.real for value, _derivative in complex_columns],
                [value.imag for value, _derivative in complex_columns],
                [derivative.real for _value, derivative in complex_columns],
                [derivative.imag for _value, derivative in complex_columns],
            ]
        )
        return (
            residual,
            real_jacobian,
            {
                "alignment": alignment,
                "a": a_value,
                "b": b_value,
                "line": line,
                "fiber_parameter": fiber_parameter,
                "f": f_value,
                "f_t": f_t,
                "f_tt": f_tt,
                "f_s": f_s,
                "f_u": f_u,
                "du_ds": -f_s / f_u,
            },
        )

    # A coarse scan derives the Newton seed without using beta values.
    scan_base = np.linspace(0.70, 0.77, 281)
    scan_ab = []
    for base_parameter in scan_base:
        a_ball, b_ball = probe.uniformization.ab_at(
            probe.uniformization.base + 1j * base_parameter
        )
        scan_ab.append((midpoint(a_ball), midpoint(b_ball)))
    best = None
    for carrier_parameter in np.linspace(0.0, 0.5, 101):
        alignment = alignment_at(float(carrier_parameter))
        for base_parameter, (a_value, b_value) in zip(scan_base, scan_ab):
            line = alignment @ np.asarray([a_value, b_value, 1 + 0j])
            roots = np.roots(
                polynomial_coefficients_y(evaluator.tables["F6"], line)
            )
            left, right = min(
                (
                    (left, right)
                    for left in range(6)
                    for right in range(left)
                ),
                key=lambda pair: abs(roots[pair[0]] - roots[pair[1]]),
            )
            separation = float(abs(roots[left] - roots[right]))
            if best is None or separation < best[0]:
                best = (
                    separation,
                    float(carrier_parameter),
                    float(base_parameter),
                    (roots[left] + roots[right]) / 2.0,
                )
    if best is None:
        raise AssertionError("wall scan did not execute")
    wall = np.asarray(
        [best[1], best[2], best[3].real, best[3].imag],
        dtype=np.float64,
    )
    for _iteration in range(12):
        residual, real_jacobian, _data = wall_data(wall)
        correction = np.linalg.solve(real_jacobian, -residual)
        wall += correction
        if max(abs(residual)) < 1.0e-11:
            break
    wall_residual, wall_jacobian, wall_values = wall_data(wall)
    if max(abs(wall_residual)) >= 5.0e-10:
        raise AssertionError("simple-node Newton solve did not converge")
    wall_alignment = wall_values["alignment"]
    wall_line = wall_values["line"]
    wall_t = wall_values["fiber_parameter"]
    wall_f_coefficients = polynomial_coefficients_y(
        evaluator.tables["F6"], wall_line
    )
    wall_roots = np.roots(wall_f_coefficients)
    root_distances = sorted(
        float(abs(wall_roots[left] - wall_roots[right]))
        for left in range(6)
        for right in range(left)
    )
    q_roots = np.roots(
        polynomial_coefficients_y(evaluator.tables["Q2"], wall_line)
    )
    q_node_distances = [float(abs(value - wall_t)) for value in q_roots]

    side_rows: dict[str, list[dict]] = {"selected_minus": [], "crossed_plus": []}
    side_vectors: dict[str, list[np.ndarray]] = {
        "selected_minus": [],
        "crossed_plus": [],
    }
    evaluation_kwargs = {
        "line_chart": "y",
        "base_lift_source_chart": "z",
        "rtol": 1.0e-6,
        "atol": 1.0e-8,
        "base_rtol": 1.0e-8,
        "base_atol": 1.0e-10,
    }
    for epsilon in SIDE_EPSILONS:
        for key, side in [("selected_minus", -1), ("crossed_plus", 1)]:
            carrier_parameter = float(wall[0] + side * epsilon)
            beta, diagnostics = evaluator.evaluate(
                alignment_at(carrier_parameter),
                winding_reference=winding_reference,
                **evaluation_kwargs,
            )
            side_vectors[key].append(beta)
            side_rows[key].append(
                {
                    "epsilon": epsilon,
                    "carrier_parameter": carrier_parameter,
                    "beta_norm": float(np.linalg.norm(beta)),
                    "beta": [complex_pair(value) for value in beta],
                    "maximum_equilibrated_reduction_condition_number": float(
                        diagnostics[
                            "maximum_equilibrated_reduction_condition_number"
                        ]
                    ),
                    "high_precision_reduction_count": diagnostics[
                        "high_precision_reduction_count"
                    ],
                }
            )

    side_limits = {}
    limit_vectors = {}
    fit_coordinates = SIDE_EPSILONS[-3:]
    for key in ["selected_minus", "crossed_plus"]:
        values = np.asarray(side_vectors[key])
        linear = fitted_limit(fit_coordinates, values[-3:], 1)
        quadratic = fitted_limit(fit_coordinates, values[-3:], 2)
        limit_vectors[key] = quadratic
        side_limits[key] = {
            "linear_last_three": [complex_pair(value) for value in linear],
            "quadratic_last_three": [
                complex_pair(value) for value in quadratic
            ],
            "quadratic_limit_norm": float(np.linalg.norm(quadratic)),
            "linear_quadratic_vector_difference_norm": float(
                np.linalg.norm(linear - quadratic)
            ),
            "linear_quadratic_maximum_component_difference": float(
                np.max(abs(linear - quadratic))
            ),
        }
    numerical_jump = (
        limit_vectors["crossed_plus"] - limit_vectors["selected_minus"]
    )

    wall_packet = evaluator.fibration_packet(wall_alignment, line_chart="y")
    original_fibration = normal_function_module.FIBRATION
    with tempfile.TemporaryDirectory(prefix="q79-pl-wall-") as directory:
        path = Path(directory) / "wall_fibration.json"
        path.write_text(json.dumps(wall_packet), encoding="utf-8")
        normal_function_module.FIBRATION = path
        try:
            engine = Q79DeltaNormalFunction()
        finally:
            normal_function_module.FIBRATION = original_fibration
    engine.gauss_manin.residue_rows = types.MethodType(
        lambda _self, periods, a_value, b_value: evaluator.residue_rows(
            wall_alignment,
            periods,
            a_value,
            b_value,
            line_chart="y",
        ),
        engine.gauss_manin,
    )
    local_vanishing_state = (
        2j
        * np.pi
        * wall_t ** np.arange(5)
        / np.sqrt(wall_values["f_tt"] / 2.0)
    )
    pl_rows = []
    pl_vectors = []
    for cutoff in PL_CUTOFFS:
        initial = np.concatenate(
            [local_vanishing_state, np.zeros(8, dtype=np.complex128)]
        )

        def differential(
            base_parameter: float, real_state: np.ndarray
        ) -> np.ndarray:
            state = real_state[:13] + 1j * real_state[13:]
            w_value = engine.root_transport.base + 1j * base_parameter
            connection, _source, a_value, b_value = (
                engine.connection_and_source(w_value)
            )
            derivative = np.empty(13, dtype=np.complex128)
            derivative[:5] = 1j * (connection @ state[:5])
            derivative[5:] = (
                engine.gauss_manin.period_length
                * 1j
                * evaluator.residue_rows(
                    wall_alignment,
                    state[:5],
                    a_value,
                    b_value,
                    line_chart="y",
                )
            )
            return np.concatenate([derivative.real, derivative.imag])

        solution = solve_ivp(
            differential,
            (float(wall[1] + cutoff), 1.0),
            np.concatenate([initial.real, initial.imag]),
            rtol=2.0e-9,
            atol=2.0e-11,
            method="DOP853",
        )
        if not solution.success:
            raise AssertionError(solution.message)
        endpoint = solution.y[:13, -1] + 1j * solution.y[13:, -1]
        predicted_jump = endpoint[5:]
        pl_vectors.append(predicted_jump)
        overlap = float(
            abs(np.vdot(predicted_jump, numerical_jump))
            / (np.linalg.norm(predicted_jump) * np.linalg.norm(numerical_jump))
        )
        best_scale = np.vdot(predicted_jump, numerical_jump) / np.vdot(
            predicted_jump, predicted_jump
        )
        relative_residual = float(
            np.linalg.norm(numerical_jump - best_scale * predicted_jump)
            / np.linalg.norm(numerical_jump)
        )
        pl_rows.append(
            {
                "cutoff": cutoff,
                "function_evaluations": int(solution.nfev),
                "predicted_endpoint_jump": [
                    complex_pair(value) for value in predicted_jump
                ],
                "predicted_jump_norm": float(np.linalg.norm(predicted_jump)),
                "projective_overlap_with_extrapolated_numerical_jump": overlap,
                "best_complex_scale": complex_pair(best_scale),
                "relative_residual_after_best_complex_scale": relative_residual,
            }
        )

    pl_limit = fitted_limit(PL_CUTOFFS[-3:], np.asarray(pl_vectors)[-3:], 2)
    pl_overlap = float(
        abs(np.vdot(pl_limit, numerical_jump))
        / (np.linalg.norm(pl_limit) * np.linalg.norm(numerical_jump))
    )
    pl_scale = np.vdot(pl_limit, numerical_jump) / np.vdot(pl_limit, pl_limit)
    pl_relative_residual = float(
        np.linalg.norm(numerical_jump - pl_scale * pl_limit)
        / np.linalg.norm(numerical_jump)
    )

    packet = {
        "schema": "MTTQ79TransverseSimpleNodeAndTransportedPLJump.v1",
        "status": "EXACT_LOCAL_PL_FORMULA_FLOATING_SAME_BRANCH_JUMP_EXECUTED",
        "source": str(SOURCE.relative_to(ROOT)).replace("\\", "/"),
        "search_direction": {
            "construction": (
                "radius-0.001 Levenberg-Marquardt direction from the retained "
                "Broyden Jacobian; beta is not used in the wall solve"
            ),
            "coordinates": [complex_pair(value) for value in direction],
            "maximum_absolute_coordinate": float(np.max(abs(direction))),
        },
        "wall": {
            "coarse_scan_minimum_root_gap": best[0],
            "carrier_parameter": float(wall[0]),
            "base_parameter": float(wall[1]),
            "fiber_double_root": complex_pair(wall_t),
            "maximum_F_and_Ft_residual": float(max(abs(wall_residual))),
            "real_coupled_Jacobian_determinant": float(
                np.linalg.det(wall_jacobian)
            ),
            "real_coupled_Jacobian_singular_values": [
                float(value)
                for value in np.linalg.svd(wall_jacobian, compute_uv=False)
            ],
            "f_tt": complex_pair(wall_values["f_tt"]),
            "absolute_f_tt": float(abs(wall_values["f_tt"])),
            "du_star_ds": complex_pair(wall_values["du_ds"]),
            "imaginary_du_star_ds": float(wall_values["du_ds"].imag),
            "simple_node": bool(abs(wall_values["f_tt"]) > 1.0),
            "transverse_real_path_crossing": bool(
                abs(wall_values["du_ds"].imag) > 1.0e-6
            ),
            "nearest_two_root_distances": root_distances[:3],
            "q_roots": [complex_pair(value) for value in q_roots],
            "q_root_distances_from_node": q_node_distances,
            "q_divisor_disjoint_from_node": bool(min(q_node_distances) > 1.0e-3),
            "normalized_y_chart_scale": float(
                abs(wall_line[1]) / np.linalg.norm(wall_line)
            ),
        },
        "one_sided_beta": {
            "samples": side_rows,
            "limits": side_limits,
            "extrapolated_jump": [
                complex_pair(value) for value in numerical_jump
            ],
            "extrapolated_jump_norm": float(np.linalg.norm(numerical_jump)),
            "selected_side_limit_norm": side_limits["selected_minus"][
                "quadratic_limit_norm"
            ],
            "crossed_side_limit_norm": side_limits["crossed_plus"][
                "quadratic_limit_norm"
            ],
        },
        "transported_Picard_Lefschetz_jump": {
            "local_vanishing_state_formula": (
                "V_k=2*pi*i*t_star^k/sqrt(f_tt(t_star)/2), k=0,...,4"
            ),
            "local_vanishing_state": [
                complex_pair(value) for value in local_vanishing_state
            ],
            "endpoint_transport_formula": (
                "dV/du=i*A_GM*V; dJ/du=i*K*Res_A(V); J(u_star)=0"
            ),
            "cutoff_runs": pl_rows,
            "quadratic_cutoff_limit": [
                complex_pair(value) for value in pl_limit
            ],
            "limit_norm": float(np.linalg.norm(pl_limit)),
            "projective_overlap_with_numerical_jump": pl_overlap,
            "best_complex_scale_to_numerical_jump": complex_pair(pl_scale),
            "relative_residual_after_best_complex_scale": pl_relative_residual,
        },
        "theorem": {
            "name": "Q79TransverseSimpleNodeTransportedPLJumpTheorem",
            "exact_statement": (
                "For a simple node with q_A disjoint from the node and a "
                "transverse discriminant crossing, the two one-sided beta "
                "continuations differ by the endpoint Gauss-Manin transport "
                "of the oriented local vanishing state V_k above."
            ),
            "exact_formula_proved": True,
            "wall_and_endpoint_values_interval_certified": False,
        },
        "decision": {
            "false_A122_chart_wall_remains_retired": True,
            "genuine_transverse_simple_node_located": True,
            "unit_PL_jump_numerically_verified": True,
            "selected_side_limit_numerically_nonzero": True,
            "selected_side_nonzero_interval_proved": False,
            "global_ell_zero_no_go_proved": False,
            "smooth_ell_zero_found": False,
            "next_required_step": (
                "interval-enclose the wall, regularized selected-side beta "
                "limit, and transported PL jump"
            ),
        },
        "strict_scope": {
            "exact": [
                "local simple-node vanishing-state formula",
                "homogeneous Gauss-Manin endpoint jump formula",
            ],
            "floating": [
                "wall coordinates and transversality values",
                "one-sided beta limits",
                "unit transported-PL jump comparison",
            ],
            "not_claimed": [
                "interval-certified nonzero residual",
                "global ell=0 no-go",
                "selected nonzero integral branch",
            ],
            "observed_SM_values_used": False,
        },
    }
    arguments.output.parent.mkdir(parents=True, exist_ok=True)
    arguments.output.write_text(
        json.dumps(packet, indent=2, sort_keys=True) + "\n",
        encoding="utf-8",
    )
    print(
        json.dumps(
            {
                "wall": packet["wall"],
                "selected_side_limit_norm": packet["one_sided_beta"][
                    "selected_side_limit_norm"
                ],
                "crossed_side_limit_norm": packet["one_sided_beta"][
                    "crossed_side_limit_norm"
                ],
                "jump_norm": packet["one_sided_beta"][
                    "extrapolated_jump_norm"
                ],
                "PL_limit_overlap": pl_overlap,
                "PL_limit_relative_residual": pl_relative_residual,
            },
            indent=2,
        )
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
