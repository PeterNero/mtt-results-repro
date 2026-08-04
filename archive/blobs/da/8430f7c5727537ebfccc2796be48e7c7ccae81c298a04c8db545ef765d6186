from __future__ import annotations

import argparse
import json
import math
from pathlib import Path

import numpy as np
from flint import acb, acb_mat, acb_series, arb, ctx

from explore_q79_pgl3_beta_zero import PGL3BetaEvaluator
from q79genus2_root_transport import Q79GenusTwoRootTransport


ROOT = Path(__file__).resolve().parents[1]
DIRECTORY = (
    ROOT
    / "candidate_data"
    / "selected_q79genus2delignebetaperiodandintegralbranchexecution"
)
A124 = DIRECTORY / "pgl3_transverse_simple_node_and_transport_pl_jump.packet.json"
SOURCE = DIRECTORY / "pgl3_projective_ychart_broyden_04.exploratory.json"
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
DEFAULT_OUTPUT = DIRECTORY / "pgl3_transverse_simple_node.interval.packet.json"


def load(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def dump(path: Path, value: dict) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(value, indent=2, sort_keys=True) + "\n", encoding="utf-8")


def exact_arb(value: float | str) -> arb:
    return arb(str(value))


def ball(midpoint: float | str, radius: float | str) -> arb:
    return arb(str(midpoint), str(radius))


def exact_acb(value: dict) -> acb:
    if "r" in value:
        return acb(value["r"], value["i"])
    return acb(value["real"], value["imaginary"])


def complex_matrix(rows: list[list[dict]]) -> acb_mat:
    return acb_mat([[exact_acb(value) for value in row] for row in rows])


def matrix_vector(matrix: acb_mat, vector: list[acb]) -> list[acb]:
    product = matrix * acb_mat([[value] for value in vector])
    return [product[index, 0] for index in range(matrix.nrows())]


def dot(left: list[acb], right: list[acb]) -> acb:
    return sum((a_value * b_value for a_value, b_value in zip(left, right)), acb(0))


def f_derivatives(
    table: list[dict], point: list[acb]
) -> tuple[acb, list[acb], list[list[acb]]]:
    value = acb(0)
    gradient = [acb(0) for _ in range(3)]
    hessian = [[acb(0) for _ in range(3)] for _ in range(3)]
    for row in table:
        powers = [int(power) for power in row["powers_xyz"]]
        coefficient = int(row["coefficient"])
        term = acb(coefficient)
        for index, power in enumerate(powers):
            term *= point[index] ** power
        value += term
        for left in range(3):
            if powers[left] == 0:
                continue
            term = acb(coefficient * powers[left])
            for index, power in enumerate(powers):
                term *= point[index] ** (power - int(index == left))
            gradient[left] += term
        for left in range(3):
            for right in range(3):
                factor = powers[left] * (powers[right] - int(left == right))
                if factor == 0:
                    continue
                term = acb(coefficient * factor)
                for index, power in enumerate(powers):
                    term *= point[index] ** (
                        power - int(index == left) - int(index == right)
                    )
                hessian[left][right] += term
    return value, gradient, hessian


def quadratic(left: list[acb], matrix: list[list[acb]], right: list[acb]) -> acb:
    return sum(
        (
            left[row] * matrix[row][column] * right[column]
            for row in range(3)
            for column in range(3)
        ),
        acb(0),
    )


def lower(value: arb) -> float:
    return math.nextafter(float(value.lower()), -math.inf)


def upper(value: arb) -> float:
    return math.nextafter(float(value.upper()), math.inf)


def interval(value: arb) -> dict[str, str]:
    return {
        "lower": format(lower(value), ".17g"),
        "upper": format(upper(value), ".17g"),
    }


def complex_interval(value: acb) -> dict[str, dict[str, str]]:
    return {"real": interval(value.real), "imaginary": interval(value.imag)}


def real_system(values: dict) -> tuple[list[arb], list[list[arb]]]:
    f_value = values["f"]
    f_t = values["f_t"]
    complex_columns = [
        (values["f_s"], values["f_ts"]),
        (values["f_u"], values["f_tu"]),
        (f_t, values["f_tt"]),
        (acb(0, 1) * f_t, acb(0, 1) * values["f_tt"]),
    ]
    residual = [f_value.real, f_value.imag, f_t.real, f_t.imag]
    jacobian = [
        [value.real for value, _derivative in complex_columns],
        [value.imag for value, _derivative in complex_columns],
        [derivative.real for _value, derivative in complex_columns],
        [derivative.imag for _value, derivative in complex_columns],
    ]
    return residual, jacobian


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--output", type=Path, default=DEFAULT_OUTPUT)
    parser.add_argument("--radius", type=float, default=1.0e-10)
    parser.add_argument("--dps", type=int, default=90)
    arguments = parser.parse_args()
    ctx.dps = arguments.dps

    a124 = load(A124)
    source = load(SOURCE)
    evaluator = PGL3BetaEvaluator()
    homology = load(MONODROMY)["homology_convention"]
    uniformization = Q79GenusTwoRootTransport(FIBRATION, homology, dps=arguments.dps)

    alignment_0 = complex_matrix(source["final_alignment"])
    direction = [exact_acb(value) for value in a124["search_direction"]["coordinates"]]
    generators = [
        acb_mat([[acb(str(complex(value).real), str(complex(value).imag)) for value in row] for row in generator])
        for generator in evaluator.generators
    ]
    tangent = acb_mat(3, 3)
    for coefficient, generator in zip(direction, generators):
        tangent += coefficient * generator

    period_length = uniformization.period_length
    tau = acb(0, 1)

    def evaluate(coordinates: list[arb]) -> dict:
        carrier_parameter, base_parameter, t_real, t_imag = coordinates
        fiber_parameter = acb(t_real, t_imag)
        alignment = alignment_0 * (carrier_parameter * tangent).exp()
        w_value = acb(exact_arb("0.25"), exact_arb("0.25") + base_parameter)
        series = acb_series([w_value, acb(1)], 2).elliptic_p(tau)
        a_value = series[0] / period_length**2
        b_value = series[1] / (acb(2) * period_length**3)
        elliptic = [a_value, b_value, acb(1)]
        line = matrix_vector(alignment, elliptic)
        line_s = matrix_vector(alignment * tangent, elliptic)
        da_du = acb(0, 1) * acb(2) * period_length * b_value
        db_du = acb(0, 1) * period_length * (acb(3) * a_value**2 - acb(1))
        line_u = matrix_vector(alignment, [da_du, db_du, acb(0)])

        point = [
            line[1],
            -(line[0] + line[2] * fiber_parameter),
            line[1] * fiber_parameter,
        ]
        point_t = [acb(0), -line[2], line[1]]
        point_s = [
            line_s[1],
            -(line_s[0] + line_s[2] * fiber_parameter),
            line_s[1] * fiber_parameter,
        ]
        point_u = [
            line_u[1],
            -(line_u[0] + line_u[2] * fiber_parameter),
            line_u[1] * fiber_parameter,
        ]
        point_ts = [acb(0), -line_s[2], line_s[1]]
        point_tu = [acb(0), -line_u[2], line_u[1]]
        f_value, gradient, hessian = f_derivatives(evaluator.tables["F6"], point)
        f_t = dot(gradient, point_t)
        f_s = dot(gradient, point_s)
        f_u = dot(gradient, point_u)
        f_tt = quadratic(point_t, hessian, point_t)
        f_ts = quadratic(point_t, hessian, point_s) + dot(gradient, point_ts)
        f_tu = quadratic(point_t, hessian, point_u) + dot(gradient, point_tu)
        q_value, _q_gradient, _q_hessian = f_derivatives(evaluator.tables["Q2"], point)
        return {
            "alignment": alignment,
            "line": line,
            "point": point,
            "f": f_value,
            "f_t": f_t,
            "f_s": f_s,
            "f_u": f_u,
            "f_tt": f_tt,
            "f_ts": f_ts,
            "f_tu": f_tu,
            "q": q_value,
        }

    wall = a124["wall"]
    midpoint_coordinates = np.asarray(
        [
            float(wall["carrier_parameter"]),
            float(wall["base_parameter"]),
            float(wall["fiber_double_root"]["real"]),
            float(wall["fiber_double_root"]["imaginary"]),
        ],
        dtype=np.float64,
    )
    refinement_rows = []
    for iteration in range(5):
        refinement_coordinates = [
            exact_arb(format(value, ".17g")) for value in midpoint_coordinates
        ]
        refinement_values = evaluate(refinement_coordinates)
        refinement_residual, refinement_jacobian = real_system(refinement_values)
        residual_midpoint = np.asarray(
            [float(value.mid()) for value in refinement_residual], dtype=np.float64
        )
        jacobian_midpoint = np.asarray(
            [[float(value.mid()) for value in row] for row in refinement_jacobian],
            dtype=np.float64,
        )
        correction = np.linalg.solve(jacobian_midpoint, -residual_midpoint)
        midpoint_coordinates += correction
        refinement_rows.append(
            {
                "iteration": iteration + 1,
                "maximum_residual_midpoint": format(
                    float(np.max(abs(residual_midpoint))), ".17g"
                ),
                "maximum_coordinate_correction": format(
                    float(np.max(abs(correction))), ".17g"
                ),
            }
        )
        if np.max(abs(correction)) < arguments.radius * 1.0e-3:
            break
    radii = np.full(4, arguments.radius, dtype=np.float64)
    point_coordinates = [exact_arb(format(value, ".17g")) for value in midpoint_coordinates]
    box_coordinates = [
        ball(format(value, ".17g"), format(radius, ".17g"))
        for value, radius in zip(midpoint_coordinates, radii)
    ]
    point_values = evaluate(point_coordinates)
    box_values = evaluate(box_coordinates)
    point_residual, point_jacobian = real_system(point_values)
    _box_residual, box_jacobian = real_system(box_values)

    midpoint_jacobian = np.asarray(
        [[float(value.mid()) for value in row] for row in point_jacobian],
        dtype=np.float64,
    )
    inverse = np.linalg.inv(midpoint_jacobian)
    inverse_interval = [
        [exact_arb(format(value, ".17g")) for value in row] for row in inverse
    ]
    correction = [
        sum(
            (inverse_interval[row][column] * point_residual[column] for column in range(4)),
            arb(0),
        )
        for row in range(4)
    ]
    image_center = [point_coordinates[index] - correction[index] for index in range(4)]
    krawczyk_matrix = [[arb(int(row == column)) for column in range(4)] for row in range(4)]
    for row in range(4):
        for column in range(4):
            krawczyk_matrix[row][column] -= sum(
                (
                    inverse_interval[row][inner] * box_jacobian[inner][column]
                    for inner in range(4)
                ),
                arb(0),
            )
    centered_box = [ball("0", format(radius, ".17g")) for radius in radii]
    krawczyk_image = [
        image_center[row]
        + sum(
            (
                krawczyk_matrix[row][column] * centered_box[column]
                for column in range(4)
            ),
            arb(0),
        )
        for row in range(4)
    ]
    inclusion_margins = [
        min(
            lower(krawczyk_image[index]) - lower(box_coordinates[index]),
            upper(box_coordinates[index]) - upper(krawczyk_image[index]),
        )
        for index in range(4)
    ]
    krawczyk_interior = all(margin > 0 for margin in inclusion_margins)
    if not krawczyk_interior:
        raise AssertionError(f"Krawczyk inclusion failed: {inclusion_margins}")

    f_tt_lower = lower(abs(box_values["f_tt"]))
    f_tt_upper = upper(abs(box_values["f_tt"]))
    f_u_lower = lower(abs(box_values["f_u"]))
    q_lower = lower(abs(box_values["q"]))
    du_ds = -box_values["f_s"] / box_values["f_u"]
    transverse = upper(du_ds.imag) < 0 or lower(du_ds.imag) > 0
    chart_numerator_lower = lower(abs(box_values["line"][1]))
    line_norm_upper = upper(
        sum((abs(value) ** 2 for value in box_values["line"]), arb(0)).sqrt()
    )
    chart_scale_lower = chart_numerator_lower / line_norm_upper
    local_vanishing_v0 = (
        acb(0, 2) * acb(arb.pi()) / (box_values["f_tt"] / acb(2)).sqrt()
    )
    local_vanishing_v0_lower = lower(abs(local_vanishing_v0))
    if not (
        f_tt_lower > 0
        and f_u_lower > 0
        and q_lower > 0
        and transverse
        and chart_scale_lower > 0.5
        and local_vanishing_v0_lower > 0
    ):
        raise AssertionError("one or more wall geometry interval gates failed")

    packet = {
        "schema": "MTTQ79TransverseSimpleNodeIntervalCertificate.v1",
        "status": "UNIQUE_TRANSVERSE_SIMPLE_NODE_INTERVAL_CERTIFIED",
        "input_semantics": {
            "carrier": "A(s)=A0 exp(s*T) with every A0 and T coefficient frozen from its stored decimal string",
            "uniformization": "Arb/ACB elliptic-p evaluation on w=1/4+i(1/4+u)",
            "wall_system": "Re(F), Im(F), Re(F_t), Im(F_t)",
            "observed_SM_values_used": False,
        },
        "precision_decimal_digits": arguments.dps,
        "center_refinement": {
            "role": "noncertifying center choice before the Krawczyk proof",
            "iterations": refinement_rows,
            "refined_midpoint": [format(value, ".17g") for value in midpoint_coordinates],
        },
        "initial_box": [interval(value) for value in box_coordinates],
        "krawczyk_image": [interval(value) for value in krawczyk_image],
        "krawczyk_inclusion_margins": [format(value, ".17g") for value in inclusion_margins],
        "unique_zero_in_box": krawczyk_interior,
        "point_residual_intervals": [interval(value) for value in point_residual],
        "geometric_bounds": {
            "absolute_f_tt_lower": format(f_tt_lower, ".17g"),
            "absolute_f_tt_upper": format(f_tt_upper, ".17g"),
            "absolute_f_u_lower": format(f_u_lower, ".17g"),
            "absolute_q_at_node_lower": format(q_lower, ".17g"),
            "du_star_ds": complex_interval(du_ds),
            "transverse_real_carrier_crossing": transverse,
            "normalized_y_chart_scale_lower": format(chart_scale_lower, ".17g"),
            "local_vanishing_state_V0_absolute_lower": format(
                local_vanishing_v0_lower, ".17g"
            ),
        },
        "closed": {
            "wall_existence_and_uniqueness": True,
            "simple_node": True,
            "transverse_crossing": True,
            "q_divisor_disjointness": True,
            "regular_projective_chart": True,
            "local_vanishing_state_nonzero": True,
            "transported_PL_jump_nonzero_by_fundamental_matrix_invertibility": True,
            "both_one_sided_beta_limits_cannot_vanish": True,
        },
        "open": {
            "selected_side_beta_nonzero_interval": True,
            "global_ell_zero_no_go": True,
            "exact_integral_branch_selection": True,
        },
    }
    dump(arguments.output, packet)
    print(json.dumps(packet, indent=2, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
