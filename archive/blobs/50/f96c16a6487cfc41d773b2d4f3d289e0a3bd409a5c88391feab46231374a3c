from __future__ import annotations

import argparse
import hashlib
import json
import math
from pathlib import Path

import numpy as np
import sympy as sp
from flint import acb, acb_poly, arb, ctx


ROOT = Path(__file__).resolve().parents[1]
FIBRATION = (
    ROOT
    / "candidate_data"
    / "selected_q79genus2lefschetzperiodreduction"
    / "explicit_genus2_fibration.packet.json"
)
A114 = (
    ROOT
    / "candidate_data"
    / "selected_q79genus2handlemonodromypromotion"
    / "two_promoted_torus_handle_monodromies.packet.json"
)
OUTPUT_DIR = (
    ROOT
    / "candidate_data"
    / "selected_q79genus2localroottrajectoryexecution"
)


def load(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def dump(path: Path, payload: dict) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(payload, indent=2, sort_keys=True) + "\n", encoding="utf-8")


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def midpoint(value: acb) -> complex:
    return complex(float(value.real.mid()), float(value.imag.mid()))


def radius_upper(value: acb) -> float:
    return math.nextafter(float(value.rad().upper()), math.inf)


def lower(value: arb) -> float:
    return math.nextafter(float(value.lower()), -math.inf)


def exact_complex(value: complex) -> acb:
    return acb(format(value.real, ".17g"), format(value.imag, ".17g"))


def strict_sign(value: arb, label: str) -> int:
    if value.lower() > 0:
        return 1
    if value.upper() < 0:
        return -1
    raise AssertionError(f"interval sign unresolved: {label}: {value}")


def matrix_rows(value: sp.Matrix) -> list[list[int]]:
    return [[int(entry) for entry in value.row(index)] for index in range(value.rows)]


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--target", choices=("zero", "minus-one"), default="zero")
    args = parser.parse_args()
    if args.target == "zero":
        target_name = "zero"
        target_value = 0 + 0j
        waypoints = [2 + 3j, 0 + 0.8j, target_value]
        waypoint_packet: list[list[int | str]] = [[2, 3], [0, "4/5"], [0, 0]]
        new_coordinate = "s_0=1/t"
    else:
        target_name = "minus_one"
        target_value = -1 + 0j
        waypoints = [2 + 3j, -0.5 + 1.3j, target_value]
        waypoint_packet = [[2, 3], ["-1/2", "13/10"], [-1, 0]]
        new_coordinate = "s_minus1=1/(t+1)"
    output = OUTPUT_DIR / f"old_to_{target_name}_branch_chart_transition.packet.json"

    ctx.dps = 80
    fibration = load(FIBRATION)
    a, b, t = sp.symbols("a b t")
    expressions = [
        sp.sympify(value)
        for value in fibration["fiber_chart"]["f_coefficients_t_descending"]
    ]

    def expression_terms(expression: sp.Expr) -> list[tuple[int, int, str, str]]:
        rows: list[tuple[int, int, str, str]] = []
        for (a_power, b_power), coefficient in sp.Poly(
            expression, a, b, domain=sp.QQ_I
        ).terms():
            rows.append(
                (
                    a_power,
                    b_power,
                    str(sp.re(coefficient)),
                    str(sp.im(coefficient)),
                )
            )
        return rows

    def evaluate(
        terms: list[tuple[int, int, str, str]], a_value: acb, b_value: acb
    ) -> acb:
        value = acb(0)
        for a_power, b_power, real, imaginary in terms:
            value += acb(real, imaginary) * a_value**a_power * b_value**b_power
        return value

    a_base = acb(0, -1)
    b_base = acb(1, 1)
    coefficients = [
        evaluate(expression_terms(expression), a_base, b_base)
        for expression in expressions
    ]
    t_roots_unordered = acb_poly(list(reversed(coefficients))).roots(
        tol=1e-45, maxprec=2048
    )
    if len(t_roots_unordered) != 6:
        raise AssertionError("base t-root isolation failed")

    old_omitted = acb(2, 3)
    rotation_angle = arb.pi() / 7
    rotation = acb(rotation_angle.cos(), -rotation_angle.sin())
    old_s_unordered = [1 / (root - old_omitted) for root in t_roots_unordered]
    old_order = sorted(
        range(6),
        key=lambda index: float((rotation * old_s_unordered[index]).real.mid()),
    )
    t_roots = [t_roots_unordered[index] for index in old_order]

    coarse_points: list[complex] = []
    for start, end in zip(waypoints, waypoints[1:]):
        segment = list(np.linspace(start, end, 65))
        if coarse_points:
            segment = segment[1:]
        coarse_points.extend(complex(value) for value in segment)

    minimum_omitted_value_clearance = math.inf
    for root in t_roots:
        root_midpoint = midpoint(root)
        root_radius = radius_upper(root)
        for start, end in zip(waypoints, waypoints[1:]):
            direction = end - start
            parameter = (
                ((root_midpoint - start).conjugate() * direction).real
                / abs(direction) ** 2
            )
            parameter = min(1.0, max(0.0, parameter))
            minimum_omitted_value_clearance = min(
                minimum_omitted_value_clearance,
                abs(root_midpoint - (start + parameter * direction))
                - root_radius
                - 2e-14,
            )
    if minimum_omitted_value_clearance <= 0:
        raise AssertionError("chart-transition omitted value meets a branch root")

    def c_box(start: complex, end: complex) -> acb:
        midpoint_value = (start + end) / 2
        return acb(
            arb(
                format(midpoint_value.real, ".17g"),
                format(abs(end.real - start.real) / 2 + 3e-16, ".17g"),
            ),
            arb(
                format(midpoint_value.imag, ".17g"),
                format(abs(end.imag - start.imag) / 2 + 3e-16, ".17g"),
            ),
        )

    def endpoint_values(c_value: complex) -> tuple[list[complex], list[float]]:
        c_point = exact_complex(c_value)
        values = [1 / (root - c_point) for root in t_roots]
        return [midpoint(value) for value in values], [radius_upper(value) for value in values]

    minimum_tube_separation = math.inf
    maximum_subdivision_depth = 0
    certified_segment_count = 0

    def certify_segment(start: complex, end: complex, depth: int = 0) -> list[complex]:
        nonlocal minimum_tube_separation
        nonlocal maximum_subdivision_depth
        nonlocal certified_segment_count
        start_centers, _ = endpoint_values(start)
        end_centers, _ = endpoint_values(end)
        box = c_box(start, end)
        centers = [
            (start_center + end_center) / 2
            for start_center, end_center in zip(start_centers, end_centers)
        ]
        radii: list[float] = []
        for root, center in zip(t_roots, centers):
            denominator = root - box
            if not abs(denominator).lower() > 0:
                if depth >= 16:
                    raise AssertionError("chart-transition denominator unresolved")
                break
            image = 1 / denominator
            radius = (
                abs(midpoint(image) - center)
                + radius_upper(image)
                + 8e-15 * (1 + abs(center))
            )
            radii.append(math.nextafter(radius, math.inf))
        if len(radii) == 6:
            separation = min(
                abs(centers[left] - centers[right])
                - radii[left]
                - radii[right]
                - 8e-15 * (1 + abs(centers[left]) + abs(centers[right]))
                for left in range(6)
                for right in range(left)
            )
            if separation > 0:
                minimum_tube_separation = min(minimum_tube_separation, separation)
                maximum_subdivision_depth = max(maximum_subdivision_depth, depth)
                certified_segment_count += 1
                return [start, end]
        if depth >= 16:
            raise AssertionError("chart-transition root tubes did not separate")
        middle = (start + end) / 2
        left_points = certify_segment(start, middle, depth + 1)
        right_points = certify_segment(middle, end, depth + 1)
        return left_points[:-1] + right_points

    points: list[complex] = [coarse_points[0]]
    for start, end in zip(coarse_points, coarse_points[1:]):
        certified = certify_segment(start, end)
        points.extend(certified[1:])

    trajectories: list[list[complex]] = []
    endpoint_radii: list[list[float]] = []
    for point in points:
        centers, radii = endpoint_values(point)
        trajectories.append(centers)
        endpoint_radii.append(radii)

    order = list(range(6))
    word: list[tuple[int, int]] = []
    minimum_projection_clearance = math.inf
    minimum_crossing_height = math.inf
    minimum_event_gap = math.inf
    for segment_index, (left_row, right_row) in enumerate(
        zip(trajectories, trajectories[1:])
    ):
        left = [rotation * exact_complex(value) for value in left_row]
        right = [rotation * exact_complex(value) for value in right_row]
        events: list[dict] = []
        for first in range(6):
            for second in range(first + 1, 6):
                difference_left = left[first] - left[second]
                difference_right = right[first] - right[second]
                x0 = difference_left.real
                x1 = difference_right.real
                sign0 = strict_sign(x0, "transition left projection")
                sign1 = strict_sign(x1, "transition right projection")
                minimum_projection_clearance = min(
                    minimum_projection_clearance, lower(abs(x0)), lower(abs(x1))
                )
                if sign0 == sign1:
                    continue
                parameter = x0 / (x0 - x1)
                if not parameter.lower() > 0 or not parameter.upper() < 1:
                    raise AssertionError("chart-transition event parameter unresolved")
                height = (
                    (1 - parameter) * difference_left.imag
                    + parameter * difference_right.imag
                )
                height_sign = strict_sign(height, "transition crossing height")
                minimum_crossing_height = min(
                    minimum_crossing_height, lower(abs(height))
                )
                events.append(
                    {
                        "first": first,
                        "second": second,
                        "parameter": parameter,
                        "height_sign": height_sign,
                    }
                )
        events.sort(key=lambda row: float(row["parameter"].mid()))
        for left_event, right_event in zip(events, events[1:]):
            gap = right_event["parameter"].lower() - left_event["parameter"].upper()
            if not gap > 0:
                raise AssertionError("chart-transition event order unresolved")
            minimum_event_gap = min(minimum_event_gap, lower(gap))
        for event in events:
            first_position = order.index(event["first"])
            second_position = order.index(event["second"])
            if abs(first_position - second_position) != 1:
                raise AssertionError("chart-transition crossing is not adjacent")
            generator = min(first_position, second_position)
            left_label = order[generator]
            sign = 1 if (
                (event["height_sign"] > 0 and left_label == event["first"])
                or (event["height_sign"] < 0 and left_label == event["second"])
            ) else -1
            word.append((generator + 1, sign))
            order[generator], order[generator + 1] = (
                order[generator + 1],
                order[generator],
            )

    endpoint_order = sorted(
        range(6),
        key=lambda label: float(
            (rotation * exact_complex(trajectories[-1][label])).real.mid()
        ),
    )
    if order != endpoint_order:
        raise AssertionError("chart-transition braid replay/order mismatch")

    intersection = sp.Matrix(
        [[0, 1, 0, 0], [-1, 0, 0, 0], [0, 0, 0, 1], [0, 0, -1, 0]]
    )
    vectors = [
        sp.Matrix(vector)
        for vector in [
            (1, 0, 0, 0),
            (0, 1, 0, 0),
            (-1, 0, 1, 0),
            (0, 0, 0, 1),
            (0, 0, -1, 0),
        ]
    ]
    positive = [sp.eye(4) - vector * vector.T * intersection for vector in vectors]
    negative = [value.inv() for value in positive]
    action = sp.eye(4)
    for generator, sign in word:
        action = (positive if sign == 1 else negative)[generator - 1] * action
    if action.T * intersection * action != intersection or action.det() != 1:
        raise AssertionError("chart-transition action is not symplectic")

    payload = {
        "schema": "MTTQ79GenusTwoBranchChartTransitionCertificate.v1",
        "status": f"OLD_TO_{target_name.upper()}_BRANCH_CHART_MARKING_TRANSITION_PROMOTED",
        "authority": {
            "fibration_sha256": sha256(FIBRATION),
            "A114_promoted_handles_sha256": sha256(A114),
            "python_flint_version": "0.9.0",
        },
        "base_fiber": {
            "w": "(1+i)/4",
            "a": "-i",
            "b": "1+i",
            "branch_root_count": 6,
        },
        "transition": {
            "old_coordinate": "s_old=1/(t-(2+3i))",
            "new_coordinate": new_coordinate,
            "target_omitted_value": [int(target_value.real), int(target_value.imag)],
            "omitted_value_waypoints": waypoint_packet,
            "minimum_omitted_value_to_branch_root_clearance_lower": format(
                minimum_omitted_value_clearance, ".17g"
            ),
            "certified_PL_segments": len(points) - 1,
            "certified_rational_image_tube_subsegments": certified_segment_count,
            "maximum_tube_subdivision_depth": maximum_subdivision_depth,
            "minimum_pairwise_tube_separation_lower": format(
                minimum_tube_separation, ".17g"
            ),
            "projection": "exp(-i*pi/7)",
            "minimum_projected_endpoint_pair_difference_lower": format(
                minimum_projection_clearance, ".17g"
            ),
            "minimum_crossing_height_lower": format(
                minimum_crossing_height, ".17g"
            ),
            "minimum_same_segment_event_parameter_gap_lower": (
                format(minimum_event_gap, ".17g")
                if minimum_event_gap < math.inf
                else None
            ),
            "raw_braid_word": [[generator, sign] for generator, sign in word],
            "raw_braid_word_length": len(word),
            "new_sorted_order_in_old_labels": endpoint_order,
        },
        "homology_marking": {
            "basis": ["a1", "b1", "a2", "b2"],
            "intersection_matrix": matrix_rows(intersection),
            "old_to_target_transport_matrix_P": matrix_rows(action),
            "matrix_transport_rule": "M_old=P^(-1)*M_target*P",
            "integral_symplectic": True,
        },
        "acceptance": {
            "continuous_chart_transition_certified": True,
            "PL_braid_isotopy_certified": True,
            "marking_transport_promoted": True,
        },
    }
    dump(output, payload)
    print(f"wrote {output}")
    print(f"word_length={len(word)} P={matrix_rows(action)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
