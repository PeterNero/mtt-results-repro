from __future__ import annotations

import argparse
import hashlib
import json
import math
from pathlib import Path

from flint import acb, acb_mat, acb_poly, arb, ctx

import certify_q79_selected_side_beta_defect_transport as validated


ROOT = Path(__file__).resolve().parents[1]
DIRECTORY = (
    ROOT
    / "candidate_data"
    / "selected_q79covariantperiodbranchcutsetandtightbetatransport"
)
PERIOD_DIRECTORY = DIRECTORY / "selected_alignment_thimble_periods"
FAN = DIRECTORY / "selected_alignment_distinguished_radial_fan.interval.packet.json"
DEFAULT_INDEX = 4


def load(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def dump(path: Path, value: dict) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(value, indent=2, sort_keys=True) + "\n", encoding="utf-8")


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def relative(path: Path) -> str:
    return str(path.relative_to(ROOT)).replace("\\", "/")


def candidate_path(index: int) -> Path:
    matches = list(PERIOD_DIRECTORY.glob(f"d{index:03d}_*.thimble_period.candidate.json"))
    if len(matches) != 1:
        raise FileNotFoundError(f"expected one floating thimble candidate for d{index:03d}")
    return matches[0]


def midpoint(value: acb) -> acb:
    return acb(str(value.real.mid()), str(value.imag.mid()))


def encoded_acb(value: acb) -> dict[str, str]:
    return {"real": str(value.real), "imaginary": str(value.imag)}


def encoded_interval(value: acb) -> dict[str, dict[str, str]]:
    return {
        "real": {
            "lower": format(validated.lower(value.real), ".17g"),
            "upper": format(validated.upper(value.real), ".17g"),
        },
        "imaginary": {
            "lower": format(validated.lower(value.imag), ".17g"),
            "upper": format(validated.upper(value.imag), ".17g"),
        },
    }


def inflated(value: acb, factor: float = 2.0, floor: float = 1.0e-80) -> acb:
    radius = max(factor * validated.radius_upper(value), floor)
    center = midpoint(value)
    return acb(
        arb(str(center.real), format(radius, ".17g")),
        arb(str(center.imag), format(radius, ".17g")),
    )


def polynomial(coefficients: list[acb], value: acb) -> acb:
    result = acb(0)
    for coefficient in reversed(coefficients):
        result = result * value + coefficient
    return result


def derivative_coefficients(coefficients: list[acb], order: int = 1) -> list[acb]:
    result = coefficients
    for _ in range(order):
        result = [acb(index) * result[index] for index in range(1, len(result))]
    return result


def fiber_coefficients(
    system: validated.SelectedQ79IntervalSystem, parameter: acb
) -> tuple[list[acb], list[acb]]:
    _a, _b, line, line_derivative = system.ab_line_data(parameter)
    coefficients, derivative_w = validated.aligned_coefficients_and_derivative(
        system.evaluator.tables["F6"],
        line,
        line_derivative,
        chart=system.line_chart,
    )
    # The interval system uses w=base+i*parameter.
    derivative_parameter = [acb(0, 1) * value for value in derivative_w]
    return coefficients, derivative_parameter


def node_equations_and_jacobian(
    system: validated.SelectedQ79IntervalSystem,
    parameter: acb,
    root: acb,
) -> tuple[list[acb], acb_mat, dict[str, float]]:
    coefficients, parameter_derivative = fiber_coefficients(system, parameter)
    first = derivative_coefficients(coefficients)
    second = derivative_coefficients(coefficients, 2)
    parameter_first = derivative_coefficients(parameter_derivative)
    f_value = polynomial(coefficients, root)
    f_t = polynomial(first, root)
    f_parameter = polynomial(parameter_derivative, root)
    f_t_parameter = polynomial(parameter_first, root)
    f_tt = polynomial(second, root)
    jacobian = acb_mat(
        [
            [f_parameter, f_t],
            [f_t_parameter, f_tt],
        ]
    )
    return [f_value, f_t], jacobian, {
        "F_parameter_absolute_lower": validated.lower(abs(f_parameter)),
        "F_tt_absolute_lower": validated.lower(abs(f_tt)),
        "jacobian_determinant_absolute_lower": validated.lower(abs(jacobian.det())),
    }


def roots_at(
    system: validated.SelectedQ79IntervalSystem, parameter: complex
) -> list[acb]:
    coefficients, _derivative = fiber_coefficients(
        system,
        acb(format(parameter.real, ".17g"), format(parameter.imag, ".17g")),
    )
    roots = acb_poly(coefficients).roots(tol=1.0e-55, maxprec=8192)
    if len(roots) != 6:
        raise AssertionError("selected sextic root isolation failed")
    return roots


def closest_pair(roots: list[acb]) -> tuple[int, int]:
    rows = []
    for left in range(6):
        for right in range(left):
            rows.append((validated.upper(abs(roots[left] - roots[right])), right, left))
    rows.sort()
    if rows[0][0] >= validated.lower(
        abs(roots[rows[1][1]] - roots[rows[1][2]])
    ):
        raise AssertionError("colliding pair is not interval-separated")
    return rows[0][1], rows[0][2]


def certify_node(
    system: validated.SelectedQ79IntervalSystem,
    critical: complex,
    *,
    epsilon: float,
    initial_parameter_radius: float,
    initial_root_radius: float,
    iterations: int,
) -> tuple[acb, acb, dict]:
    base = 0.25 + 0.25j
    critical_parameter_center = -1j * (critical - base)
    start_parameter = (1.0 - epsilon) * critical_parameter_center
    roots = roots_at(system, start_parameter)
    pair = closest_pair(roots)
    root_center = midpoint((roots[pair[0]] + roots[pair[1]]) / acb(2))
    parameter_center = acb(
        format(critical_parameter_center.real, ".17g"),
        format(critical_parameter_center.imag, ".17g"),
    )
    point_newton_rows = []
    for iteration in range(5):
        values, jacobian, diagnostics = node_equations_and_jacobian(
            system, parameter_center, root_center
        )
        correction = jacobian.solve(acb_mat([[values[0]], [values[1]]]))
        parameter_center -= correction[0, 0]
        root_center -= correction[1, 0]
        point_newton_rows.append(
            {
                "iteration": iteration + 1,
                "parameter_correction_absolute_upper": validated.upper(
                    abs(correction[0, 0])
                ),
                "root_correction_absolute_upper": validated.upper(
                    abs(correction[1, 0])
                ),
                **diagnostics,
            }
        )
    parameter_box = acb(
        arb(str(parameter_center.real.mid()), str(initial_parameter_radius)),
        arb(str(parameter_center.imag.mid()), str(initial_parameter_radius)),
    )
    root_box = acb(
        arb(str(root_center.real.mid()), str(initial_root_radius)),
        arb(str(root_center.imag.mid()), str(initial_root_radius)),
    )
    rows = []
    for iteration in range(iterations):
        parameter_midpoint = midpoint(parameter_box)
        root_midpoint = midpoint(root_box)
        values_midpoint, _jacobian_midpoint, _ = node_equations_and_jacobian(
            system, parameter_midpoint, root_midpoint
        )
        _values_box, jacobian_box, diagnostics = node_equations_and_jacobian(
            system, parameter_box, root_box
        )
        correction = system.verified_solve(
            jacobian_box,
            acb_mat([[values_midpoint[0]], [values_midpoint[1]]]),
        )
        new_parameter = parameter_midpoint - correction[0, 0]
        new_root = root_midpoint - correction[1, 0]
        parameter_interior = parameter_box.contains_interior(new_parameter)
        root_interior = root_box.contains_interior(new_root)
        rows.append(
            {
                "iteration": iteration + 1,
                "parameter_radius_before": validated.radius_upper(parameter_box),
                "root_radius_before": validated.radius_upper(root_box),
                "parameter_newton_radius": validated.radius_upper(new_parameter),
                "root_newton_radius": validated.radius_upper(new_root),
                "parameter_interior_inclusion": bool(parameter_interior),
                "root_interior_inclusion": bool(root_interior),
                **diagnostics,
            }
        )
        if not parameter_interior or not root_interior:
            raise ArithmeticError(
                "interval Newton inclusion failed at iteration "
                f"{iteration + 1}: {json.dumps(rows[-1], sort_keys=True)}"
            )
        parameter_box = inflated(new_parameter)
        root_box = inflated(new_root)

    values, jacobian, diagnostics = node_equations_and_jacobian(
        system, parameter_box, root_box
    )
    if not values[0].contains(0) or not values[1].contains(0):
        raise AssertionError("certified node boxes do not enclose F=F_t=0")
    if diagnostics["jacobian_determinant_absolute_lower"] <= 0:
        raise AssertionError("node Jacobian is not separated from singularity")
    return parameter_box, root_box, {
        "incoming_closest_pair_zero_based": list(pair),
        "point_newton_refinement": point_newton_rows,
        "iterations": rows,
        "final_F_interval": encoded_acb(values[0]),
        "final_F_t_interval": encoded_acb(values[1]),
        "final_jacobian_determinant": encoded_acb(jacobian.det()),
        **diagnostics,
    }


def nodal_factor_certificate(
    system: validated.SelectedQ79IntervalSystem,
    parameter: acb,
    root: acb,
) -> dict:
    coefficients, _derivative = fiber_coefficients(system, parameter)
    q0 = root**2
    q1 = -acb(2) * root
    h = [acb(0) for _ in range(5)]
    h[4] = coefficients[6]
    h[3] = coefficients[5] - q1 * h[4]
    h[2] = coefficients[4] - q1 * h[3] - q0 * h[4]
    h[1] = coefficients[3] - q1 * h[2] - q0 * h[3]
    h[0] = coefficients[2] - q1 * h[1] - q0 * h[2]
    product = [acb(0) for _ in range(7)]
    for q_degree, q_value in enumerate((q0, q1, acb(1))):
        for h_degree, h_value in enumerate(h):
            product[q_degree + h_degree] += q_value * h_value
    residual = [left - right for left, right in zip(product, coefficients)]
    if not all(value.contains(0) for value in residual):
        raise AssertionError("nodal quadratic-times-quartic factor residual excludes zero")
    h_at_root = polynomial(h, root)
    h_lower = validated.lower(abs(h_at_root))
    if h_lower <= 0:
        raise AssertionError("nodal quadratic and quartic factors are not coprime")

    # Unknowns are q0,q1,h0,...,h4; equations are the seven t coefficients.
    jacobian = acb_mat(7, 7)
    for degree in range(7):
        if 0 <= degree <= 4:
            jacobian[degree, 0] = h[degree]
        if 0 <= degree - 1 <= 4:
            jacobian[degree, 1] = h[degree - 1]
        for h_degree in range(5):
            q_degree = degree - h_degree
            if q_degree == 0:
                jacobian[degree, 2 + h_degree] = q0
            elif q_degree == 1:
                jacobian[degree, 2 + h_degree] = q1
            elif q_degree == 2:
                jacobian[degree, 2 + h_degree] = acb(1)
    determinant = jacobian.det()
    determinant_lower = validated.lower(abs(determinant))
    if determinant_lower <= 0:
        raise AssertionError("Hensel factor Jacobian is not invertible")
    identity = acb_mat(7, 7)
    for index in range(7):
        identity[index, index] = acb(1)
    inverse = system.verified_solve(jacobian, identity)
    inverse_norm = max(
        sum((abs(inverse[row, column]) for column in range(7)), arb(0))
        for row in range(7)
    )
    return {
        "monic_quadratic_coefficients_ascending": [
            encoded_acb(q0),
            encoded_acb(q1),
            encoded_acb(acb(1)),
        ],
        "quartic_coefficients_ascending": [encoded_acb(value) for value in h],
        "factorization_residuals": [encoded_acb(value) for value in residual],
        "quadratic_discriminant": encoded_acb(q1**2 - acb(4) * q0),
        "quartic_at_double_root": encoded_acb(h_at_root),
        "quartic_at_double_root_absolute_lower": h_lower,
        "hensel_jacobian_determinant": encoded_acb(determinant),
        "hensel_jacobian_determinant_absolute_lower": determinant_lower,
        "hensel_jacobian_inverse_infinity_norm_upper": validated.upper(inverse_norm),
        "analytic_factor_germ_selected": True,
    }


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--distinguished-index", type=int, default=DEFAULT_INDEX)
    parser.add_argument("--epsilon", type=float, default=1.0e-5)
    parser.add_argument("--dps", type=int, default=100)
    parser.add_argument("--initial-parameter-radius", type=float, default=1.0e-20)
    parser.add_argument("--initial-root-radius", type=float, default=1.0e-20)
    parser.add_argument("--iterations", type=int, default=3)
    parser.add_argument("--output", type=Path)
    arguments = parser.parse_args()
    ctx.dps = arguments.dps

    source_path = candidate_path(arguments.distinguished_index)
    source = load(source_path)
    fan = load(FAN)
    fan_rows = [
        row
        for row in fan["distinguished_positive_meridians"]
        if int(row["distinguished_index"]) == arguments.distinguished_index
    ]
    if len(fan_rows) != 1 or fan_rows[0]["root_id"] != source["root_id"]:
        raise AssertionError("distinguished fan row mismatch")
    critical = complex(
        float(source["critical_center"]["real"]),
        float(source["critical_center"]["imaginary"]),
    )
    system = validated.SelectedQ79IntervalSystem(
        dps=arguments.dps, line_chart=source["line_chart"]
    )
    parameter_box, root_box, node = certify_node(
        system,
        critical,
        epsilon=arguments.epsilon,
        initial_parameter_radius=arguments.initial_parameter_radius,
        initial_root_radius=arguments.initial_root_radius,
        iterations=arguments.iterations,
    )
    factor = nodal_factor_certificate(system, parameter_box, root_box)

    output = arguments.output
    if output is None:
        output = PERIOD_DIRECTORY / (
            f"d{arguments.distinguished_index:03d}_{source['root_id']}.nodal_factor.interval.packet.json"
        )
    elif not output.is_absolute():
        output = ROOT / output
    payload = {
        "schema": "MTTQ79SelectedAlignmentSingleE32ThimbleNodalFactorInterval.v1",
        "status": "SELECTED_NODE_AND_LOCAL_WEIERSTRASS_FACTOR_INTERVAL_CERTIFIED",
        "authority": {
            "floating_candidate": relative(source_path),
            "floating_candidate_sha256": sha256(source_path),
            "distinguished_fan": relative(FAN),
            "distinguished_fan_sha256": sha256(FAN),
            "builder_source": relative(Path(__file__)),
            "builder_source_sha256": sha256(Path(__file__)),
        },
        "selected_thimble": {
            "distinguished_index": arguments.distinguished_index,
            "root_id": source["root_id"],
            "line_chart": source["line_chart"],
            "incoming_cutoff_epsilon": arguments.epsilon,
        },
        "certified_node": {
            "parameter_interval": encoded_interval(parameter_box),
            "parameter_ball": encoded_acb(parameter_box),
            "double_root_interval": encoded_interval(root_box),
            "double_root_ball": encoded_acb(root_box),
            "parameter_radius_upper": validated.radius_upper(parameter_box),
            "double_root_radius_upper": validated.radius_upper(root_box),
            **node,
        },
        "local_weierstrass_factor": factor,
        "scope": {
            "observed_SM_values_used": False,
            "node_F_equals_F_t_interval_newton_closed": True,
            "simple_transverse_node_closed": True,
            "nodal_quadratic_times_quartic_factor_closed": True,
            "analytic_Hensel_factor_germ_closed": True,
            "quantitative_factor_radius_to_epsilon_closed": False,
            "desingularized_E32_tail_interval_closed": False,
            "full_E32_thimble_interval_closed": False,
        },
        "next_required_artifact": (
            "extend the certified Hensel factor germ to the epsilon disk, integrate the "
            "desingularized E32 tail, and splice it to the validated main interval"
        ),
    }
    dump(output, payload)
    print(f"wrote {relative(output)}")
    print(
        json.dumps(
            {
                "distinguished_index": arguments.distinguished_index,
                "root_id": source["root_id"],
                "parameter_radius": validated.radius_upper(parameter_box),
                "double_root_radius": validated.radius_upper(root_box),
                "node_jacobian_lower": node["jacobian_determinant_absolute_lower"],
                "quartic_at_node_lower": factor["quartic_at_double_root_absolute_lower"],
                "hensel_jacobian_lower": factor["hensel_jacobian_determinant_absolute_lower"],
            },
            indent=2,
        )
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
