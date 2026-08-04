from __future__ import annotations

import argparse
import json
import math
from pathlib import Path

import numpy as np
from flint import acb, acb_mat, acb_poly, arb, ctx

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
DEFAULT_OUTPUT = DIRECTORY / "pgl3_selected_side_base_lift.interval.packet.json"


def load(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def dump(path: Path, value: dict) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(value, indent=2, sort_keys=True) + "\n", encoding="utf-8")


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


def complex_interval(value: acb) -> dict:
    return {
        "real": {
            "lower": str(value.real.lower()),
            "upper": str(value.real.upper()),
        },
        "imaginary": {
            "lower": str(value.imag.lower()),
            "upper": str(value.imag.upper()),
        },
    }


def radius_upper(value: acb) -> float:
    return math.nextafter(float(value.rad().upper()), math.inf)


def matrix_vector(matrix: acb_mat, vector: list[acb]) -> list[acb]:
    product = matrix * acb_mat([[value] for value in vector])
    return [product[index, 0] for index in range(matrix.nrows())]


def aligned_coefficients(
    table: list[dict], line: list[acb], *, chart: str
) -> list[acb]:
    degree = sum(int(value) for value in table[0]["powers_xyz"])
    ascending = [acb(0) for _ in range(degree + 1)]
    for row in table:
        x_power, y_power, z_power = [int(value) for value in row["powers_xyz"]]
        coefficient = int(row["coefficient"])
        if chart == "z":
            for index in range(z_power + 1):
                ascending[index + y_power] += (
                    acb(coefficient * (-1) ** z_power * math.comb(z_power, index))
                    * line[2] ** (x_power + y_power)
                    * line[0] ** (z_power - index)
                    * line[1] ** index
                )
        elif chart == "y":
            for index in range(y_power + 1):
                ascending[index + z_power] += (
                    acb(coefficient * (-1) ** y_power * math.comb(y_power, index))
                    * line[1] ** (x_power + z_power)
                    * line[0] ** (y_power - index)
                    * line[2] ** index
                )
        else:
            raise ValueError(f"unsupported chart {chart!r}")
    return ascending


def polynomial(coefficients: list[acb], value: acb) -> acb:
    result = acb(0)
    for coefficient in reversed(coefficients):
        result = result * value + coefficient
    return result


class CertifiedPathIntegrator:
    def __init__(self, f_coefficients: list[acb], *, dps: int) -> None:
        self.f_coefficients = f_coefficients
        self.maximum_depth = 0
        self.segment_count = 0
        self.integral_count = 0
        self.minimum_half_plane_margin = math.inf
        self.minimum_sign_margin = math.inf
        self.tolerance = arb(f"1e-{max(25, dps - 25)}")

    def f(self, value: acb) -> acb:
        return polynomial(self.f_coefficients, value)

    @staticmethod
    def rotations() -> list[acb]:
        return [acb(1), acb(-1), acb(0, 1), acb(0, -1)]

    def phase(self, start: acb, end: acb) -> tuple[acb, float] | None:
        parameter = acb(arb("0.5", "0.5"), arb(0))
        path_box = start + parameter * (end - start)
        f_box = self.f(path_box)
        rows = [(rotation, lower((rotation * f_box).real)) for rotation in self.rotations()]
        rotation, margin = max(rows, key=lambda row: row[1])
        if margin <= 0:
            return None
        return rotation, margin

    @staticmethod
    def select_sign(candidate: acb, reference: acb) -> tuple[int, float]:
        same_upper = upper(abs(candidate - reference))
        opposite_lower = lower(abs(candidate + reference))
        opposite_upper = upper(abs(candidate + reference))
        same_lower = lower(abs(candidate - reference))
        if same_upper < opposite_lower:
            return 1, opposite_lower - same_upper
        if opposite_upper < same_lower:
            return -1, same_lower - opposite_upper
        raise AssertionError("square-root branch sign is not interval-separated")

    def integrate_segment(
        self,
        start: acb,
        end: acb,
        sheet_value: acb,
        periods: list[acb],
        *,
        depth: int = 0,
    ) -> tuple[acb, list[acb]]:
        self.maximum_depth = max(self.maximum_depth, depth)
        phase = self.phase(start, end)
        if phase is None:
            if depth >= 24:
                raise AssertionError("path segment could not be placed in a square-root half-plane")
            middle = (start + end) / acb(2)
            sheet_value, periods = self.integrate_segment(
                start, middle, sheet_value, periods, depth=depth + 1
            )
            return self.integrate_segment(
                middle, end, sheet_value, periods, depth=depth + 1
            )
        rotation, margin = phase
        rotation_root = rotation.sqrt()

        def root(value: acb, analytic: bool) -> acb:
            rotated = rotation * self.f(value)
            if analytic and not rotated.real.lower() > 0:
                return acb("nan")
            return rotated.sqrt(analytic=analytic) / rotation_root

        candidate_start = root(start, False)
        sign, sign_margin = self.select_sign(candidate_start, sheet_value)

        def integrand(parameter: acb, analytic: bool, power: int) -> acb:
            value = start + parameter * (end - start)
            denominator = root(value, analytic)
            if not denominator.is_finite():
                return denominator
            return acb(sign) * value**power * (end - start) / denominator

        additions = []
        try:
            for power in range(5):
                value = acb.integral(
                    lambda parameter, analytic, p=power: integrand(
                        parameter, analytic, p
                    ),
                    acb(0),
                    acb(1),
                    rel_tol=self.tolerance,
                    abs_tol=self.tolerance,
                    depth_limit=20,
                    eval_limit=200000,
                )
                if not value.is_finite():
                    raise ArithmeticError("nonfinite integral enclosure")
                additions.append(value)
        except (ArithmeticError, ValueError):
            if depth >= 24:
                raise
            middle = (start + end) / acb(2)
            sheet_value, periods = self.integrate_segment(
                start, middle, sheet_value, periods, depth=depth + 1
            )
            return self.integrate_segment(
                middle, end, sheet_value, periods, depth=depth + 1
            )

        endpoint = acb(sign) * root(end, False)
        self.segment_count += 1
        self.integral_count += 5
        self.minimum_half_plane_margin = min(self.minimum_half_plane_margin, margin)
        self.minimum_sign_margin = min(self.minimum_sign_margin, sign_margin)
        return endpoint, [value + addition for value, addition in zip(periods, additions)]


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--output", type=Path, default=DEFAULT_OUTPUT)
    parser.add_argument("--dps", type=int, default=70)
    parser.add_argument("--winding-edges", type=int, default=48)
    arguments = parser.parse_args()
    ctx.dps = arguments.dps

    a124 = load(A124)
    wall = load(WALL)
    source = load(SOURCE)
    evaluator = PGL3BetaEvaluator()
    alignment_0 = acb_mat(
        [[exact_acb(value) for value in row] for row in source["final_alignment"]]
    )
    direction = [exact_acb(value) for value in a124["search_direction"]["coordinates"]]
    tangent = acb_mat(3, 3)
    for coefficient, generator_values in zip(direction, evaluator.generators):
        generator = acb_mat(
            [
                [acb(str(complex(value).real), str(complex(value).imag)) for value in row]
                for row in generator_values
            ]
        )
        tangent += coefficient * generator

    wall_lower = wall["initial_box"][0]["lower"]
    selected_carrier = arb(wall_lower) - arb("0.005")
    alignment = alignment_0 * (selected_carrier * tangent).exp()
    elliptic = [acb(0, -1), acb(1, 1), acb(1)]
    line = matrix_vector(alignment, elliptic)
    f_coefficients = aligned_coefficients(evaluator.tables["F6"], line, chart="z")
    g_coefficients = aligned_coefficients(evaluator.tables["G3"], line, chart="z")
    q_coefficients = aligned_coefficients(evaluator.tables["Q2"], line, chart="z")
    f_roots = acb_poly(f_coefficients).roots(tol=1e-45, maxprec=4096)
    q_roots = acb_poly(q_coefficients).roots(tol=1e-45, maxprec=4096)
    if len(f_roots) != 6 or len(q_roots) != 2:
        raise AssertionError("aligned base-fiber root isolation failed")
    q_roots.sort(key=lambda value: (midpoint(value).real, midpoint(value).imag))
    winding_reference = exact_acb(source["final_winding_reference"])
    winding_root = min(f_roots, key=lambda value: abs(midpoint(value - winding_reference)))
    clearances = [
        lower(abs(winding_root - value))
        for value in [*f_roots, *q_roots]
        if value is not winding_root
    ]
    winding_clearance_lower = min(clearances)
    winding_radius = arb(format(min(0.1, 0.15 * winding_clearance_lower), ".17g"))
    outer = acb(20, 7)

    integrator = CertifiedPathIntegrator(f_coefficients, dps=arguments.dps)
    states = []
    for root in q_roots:
        sheet = polynomial(g_coefficients, root)
        sheet, periods = integrator.integrate_segment(
            root, outer, sheet, [acb(0) for _ in range(5)]
        )
        states.append([sheet, periods])

    direct_difference_upper = upper(abs(states[0][0] - states[1][0]))
    direct_sum_lower = lower(abs(states[0][0] + states[1][0]))
    direct_same = direct_difference_upper < direct_sum_lower
    if not direct_same:
        raise AssertionError("the two direct outer paths are not rigorously on the same sheet")

    circle_start = winding_root + acb(winding_radius)
    sheet, periods = states[1]
    sheet, periods = integrator.integrate_segment(outer, circle_start, sheet, periods)
    vertices = []
    for index in range(arguments.winding_edges + 1):
        angle = arb.pi() * arb(-2 * index) / arb(arguments.winding_edges)
        vertices.append(
            winding_root
            + acb(angle.cos(), angle.sin()) * acb(winding_radius)
        )
    for start, end in zip(vertices, vertices[1:]):
        sheet, periods = integrator.integrate_segment(start, end, sheet, periods)
    sheet, periods = integrator.integrate_segment(circle_start, outer, sheet, periods)
    states[1] = [sheet, periods]

    outer_cancellation_upper = upper(abs(states[0][0] + states[1][0]))
    outer_sheet_lower = min(lower(abs(states[0][0])), lower(abs(states[1][0])))
    if not outer_cancellation_upper < 1.0e-20 * max(1.0, outer_sheet_lower):
        raise AssertionError("opposite outer sheets did not cancel rigorously")
    z_lift = [-(left + right) for left, right in zip(states[0][1], states[1][1])]

    alpha = -line[0] / line[1]
    beta = -line[2] / line[1]
    common = -(line[1] ** 2) / (line[2] ** 2)
    z_from_y = acb_mat(5, 5)
    for power in range(5):
        for index in range(power + 1):
            z_from_y[power, index] = (
                common
                * acb(math.comb(power, index))
                * alpha ** (power - index)
                * beta**index
            )
    y_lift_matrix = z_from_y.solve(acb_mat([[value] for value in z_lift]))
    y_lift = [y_lift_matrix[index, 0] for index in range(5)]
    maximum_radius = max(radius_upper(value) for value in [*z_lift, *y_lift])

    packet = {
        "schema": "MTTQ79SelectedSideBaseAbelJacobiLiftIntervalCertificate.v1",
        "status": "SELECTED_SIDE_BASE_ABEL_JACOBI_LIFT_INTERVAL_CERTIFIED",
        "selected_carrier": {
            "definition": "lower endpoint of the certified wall carrier box minus 0.005",
            "value": str(selected_carrier),
            "strictly_on_selected_minus_side": True,
        },
        "path": {
            "source_chart": "z",
            "outer_point": {"real": "20", "imaginary": "7"},
            "clockwise_winding_edges": arguments.winding_edges,
            "winding_clearance_lower": format(winding_clearance_lower, ".17g"),
            "winding_radius": str(winding_radius),
            "direct_outer_paths_same_sheet": direct_same,
            "opposite_outer_sheet_cancellation_upper": format(
                outer_cancellation_upper, ".17g"
            ),
            "minimum_square_root_half_plane_margin": format(
                integrator.minimum_half_plane_margin, ".17g"
            ),
            "minimum_branch_sign_separation_margin": format(
                integrator.minimum_sign_margin, ".17g"
            ),
            "certified_segment_count": integrator.segment_count,
            "maximum_subdivision_depth": integrator.maximum_depth,
            "rigorous_integral_count": integrator.integral_count,
        },
        "z_chart_base_lift": [complex_interval(value) for value in z_lift],
        "y_chart_base_lift": [complex_interval(value) for value in y_lift],
        "maximum_component_ball_radius_upper": format(maximum_radius, ".17g"),
        "closed": {
            "q_root_isolation": True,
            "selected_winding_isolation": True,
            "square_root_branch_continuation": True,
            "opposite_infinity_sheet_cancellation": True,
            "base_lift_interval_enclosure": True,
            "exact_projective_chart_transport": True,
        },
        "open": {
            "base_path_Gauss_Manin_interval_transport": True,
            "selected_side_beta_nonzero_interval": True,
        },
        "observed_SM_values_used": False,
    }
    dump(arguments.output, packet)
    print(json.dumps(packet, indent=2, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
