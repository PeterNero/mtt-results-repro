from __future__ import annotations

import argparse
import hashlib
import json
import math
import time
from pathlib import Path

import numpy as np
import sympy as sp
from flint import acb, acb_poly, acb_series, ctx
from scipy.optimize import linear_sum_assignment


ROOT = Path(__file__).resolve().parents[1]
FIBRATION = (
    ROOT
    / "candidate_data"
    / "selected_q79genus2lefschetzperiodreduction"
    / "explicit_genus2_fibration.packet.json"
)
PATHS = (
    ROOT
    / "candidate_data"
    / "selected_q79genus2basedpathsystemandmonodromycandidate"
    / "certified_based_meridian_and_handle_paths.packet.json"
)
A113_EXPLORATION = (
    ROOT
    / "candidate_data"
    / "selected_q79genus2picardlefschetzmonodromyexecution"
    / "numerical_monodromy_exploration.packet.json"
)
ZERO_CHART_TRANSITION = (
    ROOT
    / "candidate_data"
    / "selected_q79genus2localroottrajectoryexecution"
    / "old_to_zero_branch_chart_transition.packet.json"
)
MINUS_ONE_CHART_TRANSITION = (
    ROOT
    / "candidate_data"
    / "selected_q79genus2localroottrajectoryexecution"
    / "old_to_minus_one_branch_chart_transition.packet.json"
)
OUTPUT = (
    ROOT
    / "candidate_data"
    / "selected_q79genus2localroottrajectoryexecution"
)


def load(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def midpoint(value: acb) -> complex:
    return complex(float(value.real.mid()), float(value.imag.mid()))


def radius_upper(value: acb) -> float:
    return math.nextafter(float(value.rad().upper()), math.inf)


def packet_complex(value: dict[str, str]) -> complex:
    return complex(float(value["real"]), float(value["imaginary"]))


def matrix_rows(value: np.ndarray) -> list[list[int]]:
    return [[int(entry) for entry in row] for row in value.tolist()]


def free_reduce(word: list[tuple[int, int]]) -> list[tuple[int, int]]:
    reduced: list[tuple[int, int]] = []
    for letter in word:
        if reduced and reduced[-1] == (letter[0], -letter[1]):
            reduced.pop()
        else:
            reduced.append(letter)
    return reduced


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--root-id", required=True)
    parser.add_argument("--step-ratio", type=float, default=0.16)
    parser.add_argument("--coarse-outbound", type=int, default=48)
    parser.add_argument("--coarse-circle", type=int, default=96)
    parser.add_argument("--omitted-real", type=float, default=2.0)
    parser.add_argument("--omitted-imag", type=float, default=3.0)
    parser.add_argument("--no-save", action="store_true")
    args = parser.parse_args()
    if not 0 < args.step_ratio < 0.4:
        raise AssertionError("step ratio must lie in (0,0.4)")

    ctx.dps = 55
    started = time.perf_counter()
    fibration = load(FIBRATION)
    paths = load(PATHS)
    old_exploration = load(A113_EXPLORATION)
    path_row = next(
        row for row in paths["positive_based_meridians"] if row["root_id"] == args.root_id
    )
    old_row = next(row for row in old_exploration["monodromies"] if row["root_id"] == args.root_id)

    a, b, t, s = sp.symbols("a b t s")
    t_coefficients = [
        sp.sympify(value)
        for value in fibration["fiber_chart"]["f_coefficients_t_descending"]
    ]
    f_ab = sum(
        coefficient * t ** (6 - index)
        for index, coefficient in enumerate(t_coefficients)
    )
    omitted = sp.Rational(str(args.omitted_real)) + sp.I * sp.Rational(
        str(args.omitted_imag)
    )
    transformed = sp.Poly(
        sp.expand(s**6 * f_ab.subs(t, omitted + 1 / s)), s
    ).all_coeffs()
    if len(transformed) != 7:
        raise AssertionError("transformed branch polynomial is not degree six")

    coefficient_terms: list[list[tuple[int, int, str, str]]] = []
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
        coefficient_terms.append(terms)

    tau = acb(0, 1)
    period_length = acb("0.5").elliptic_k() * acb(2).sqrt()
    period_square = period_length**2
    period_cube = period_length**3

    def ab_at(w_value: complex) -> tuple[acb, acb]:
        w_ball = acb(format(w_value.real, ".17g"), format(w_value.imag, ".17g"))
        series = acb_series([w_ball, acb(1)], 2).elliptic_p(tau)
        return series[0] / period_square, series[1] / (2 * period_cube)

    def coefficient_at(
        terms: list[tuple[int, int, str, str]], a_value: acb, b_value: acb
    ) -> acb:
        value = acb(0)
        for a_power, b_power, real, imaginary in terms:
            value += acb(real, imaginary) * a_value**a_power * b_value**b_power
        return value

    root_solve_count = 0

    def roots_at(w_value: complex) -> tuple[np.ndarray, list[float]]:
        nonlocal root_solve_count
        root_solve_count += 1
        a_value, b_value = ab_at(w_value)
        descending = [
            coefficient_at(terms, a_value, b_value) for terms in coefficient_terms
        ]
        roots = acb_poly(list(reversed(descending))).roots(tol=1e-28, maxprec=1024)
        if len(roots) != 6 or not all(root.is_finite() for root in roots):
            raise AssertionError(f"root isolation failed at {w_value!r}")
        return (
            np.asarray([midpoint(root) for root in roots], dtype=np.complex128),
            [radius_upper(root) for root in roots],
        )

    projection_angle = math.pi / 7
    rotation = np.exp(-1j * projection_angle)
    base = 0.25 + 0.25j
    base_unordered, base_radii_unordered = roots_at(base)
    base_order = np.argsort((rotation * base_unordered).real)
    base_roots = base_unordered[base_order]
    base_radii = [base_radii_unordered[index] for index in base_order]

    def match(
        previous: np.ndarray, unordered: np.ndarray, unordered_radii: list[float]
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
        return current, radii, float(costs[rows, columns].max() / minimum_separation)

    points: list[complex] = [base]
    trajectories: list[np.ndarray] = [base_roots.copy()]
    radii_rows: list[list[float]] = [base_radii.copy()]
    maximum_ratio = 0.0

    def advance(start: complex, end: complex, previous: np.ndarray, depth: int) -> np.ndarray:
        nonlocal maximum_ratio
        unordered, unordered_radii = roots_at(end)
        current, radii, ratio = match(previous, unordered, unordered_radii)
        if ratio > args.step_ratio:
            if depth >= 24:
                raise AssertionError(f"local transport did not resolve at {end!r}")
            middle = (start + end) / 2
            middle_roots = advance(start, middle, previous, depth + 1)
            return advance(middle, end, middle_roots, depth + 1)
        maximum_ratio = max(maximum_ratio, ratio)
        points.append(end)
        trajectories.append(current)
        radii_rows.append(radii)
        return current

    outbound_end = packet_complex(path_row["outbound_segment"]["end"])
    outbound_coarse = np.linspace(base, outbound_end, args.coarse_outbound + 1)
    previous = base_roots
    for start, end in zip(outbound_coarse, outbound_coarse[1:]):
        previous = advance(complex(start), complex(end), previous, 0)
    outbound_point_count = len(points)
    outbound_points = list(points)
    outbound_roots = [row.copy() for row in trajectories]
    outbound_radii = [list(row) for row in radii_rows]

    circle = path_row["positive_meridian"]
    circle_center = packet_complex(circle["center"])
    circle_radius = float(circle["radius"])
    start_angle = float(circle["start_angle"])
    circle_points = [
        circle_center
        + circle_radius
        * np.exp(1j * (start_angle + 2 * math.pi * index / args.coarse_circle))
        for index in range(args.coarse_circle + 1)
    ]
    circle_points[0] = outbound_end
    circle_points[-1] = outbound_end
    for start, end in zip(circle_points, circle_points[1:]):
        previous = advance(complex(start), complex(end), previous, 0)
    circle_point_count = len(points) - outbound_point_count + 1

    reused_reverse_steps = 0
    for index in range(len(outbound_points) - 2, -1, -1):
        current, radii, ratio = match(
            previous,
            outbound_roots[index],
            outbound_radii[index],
        )
        if ratio >= 0.44:
            raise AssertionError("cached reverse root matching is not geometrically unique")
        maximum_ratio = max(maximum_ratio, ratio)
        points.append(outbound_points[index])
        trajectories.append(current)
        radii_rows.append(radii)
        previous = current
        reused_reverse_steps += 1

    def word_from_trajectories(
        trajectory_rows: list[np.ndarray],
    ) -> tuple[list[tuple[int, int]], list[int], float]:
        order = list(range(6))
        word: list[tuple[int, int]] = []
        minimum_event_gap = 1.0
        for left_roots, right_roots in zip(trajectory_rows, trajectory_rows[1:]):
            left = rotation * left_roots
            right = rotation * right_roots
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
                    raise AssertionError("nonadjacent local-braid crossing")
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

    word, final_order, minimum_event_gap = word_from_trajectories(trajectories)
    reduced = free_reduce(word)
    final_permutation = [
        int(np.argmin(abs(trajectories[-1][label] - base_roots)))
        for label in range(6)
    ]
    if sorted(final_permutation) != list(range(6)):
        raise AssertionError("local endpoint matching is not a permutation")

    intersection = np.asarray(
        old_exploration["homology_convention"]["intersection_matrix"], dtype=object
    )
    chain_vectors = [
        np.asarray(vector, dtype=object).reshape(4, 1)
        for vector in old_exploration["homology_convention"][
            "chain_vectors_for_sigma_1_to_sigma_5"
        ]
    ]
    positive = [
        np.eye(4, dtype=object) - vector @ vector.T @ intersection
        for vector in chain_vectors
    ]
    negative = [
        np.asarray(sp.Matrix(value.tolist()).inv().tolist(), dtype=object)
        for value in positive
    ]
    action = np.eye(4, dtype=object)
    for generator, sign in word:
        action = (positive if sign == 1 else negative)[generator - 1] @ action
    action_sympy = sp.Matrix(action.tolist())
    action_delta = action_sympy - sp.eye(4)
    expected_action = np.asarray(
        old_row["homology"]["picard_lefschetz_matrix"], dtype=object
    )

    chart_matches_a113 = args.omitted_real == 2.0 and args.omitted_imag == 3.0
    zero_chart = args.omitted_real == 0.0 and args.omitted_imag == 0.0
    minus_one_chart = args.omitted_real == -1.0 and args.omitted_imag == 0.0
    transported_action = action
    marking_transport = "identity"
    transition_path: Path | None = None
    if zero_chart or minus_one_chart:
        transition_path = (
            ZERO_CHART_TRANSITION if zero_chart else MINUS_ONE_CHART_TRANSITION
        )
        transition = load(transition_path)
        if not transition["acceptance"]["marking_transport_promoted"]:
            raise AssertionError("branch-chart marking transport is not promoted")
        transport = sp.Matrix(
            transition["homology_marking"]["old_to_target_transport_matrix_P"]
        )
        transported_action = np.asarray(
            (transport.inv() * sp.Matrix(action.tolist()) * transport).tolist(),
            dtype=object,
        )
        marking_transport = "M_old=P^(-1)*M_target*P"
    packet = {
        "schema": "MTTQ79GenusTwoSingleLocalMonodromyTrajectoryExploration.v1",
        "status": "LOCAL_TRAJECTORY_COMPUTED_CONTINUOUS_ROOT_TUBES_OPEN",
        "root_id": args.root_id,
        "authority": {
            "fibration_sha256": hashlib.sha256(FIBRATION.read_bytes()).hexdigest(),
            "paths_sha256": hashlib.sha256(PATHS.read_bytes()).hexdigest(),
            "A113_exploration_sha256": hashlib.sha256(
                A113_EXPLORATION.read_bytes()
            ).hexdigest(),
            "branch_chart_transition_sha256": (
                hashlib.sha256(transition_path.read_bytes()).hexdigest()
                if transition_path is not None
                else None
            ),
        },
        "branch_chart": {
            "coordinate": f"s=1/(t-({args.omitted_real}+{args.omitted_imag}i))",
            "projection_angle": "pi/7",
            "matches_A113_marking": chart_matches_a113,
        },
        "transport": {
            "step_to_root_separation_threshold": format(args.step_ratio, ".17g"),
            "maximum_step_to_root_separation_ratio": format(maximum_ratio, ".17g"),
            "root_solve_count": root_solve_count,
            "saved_sample_count": len(points),
            "outbound_point_count": outbound_point_count,
            "circle_point_count": circle_point_count,
            "cached_reverse_steps": reused_reverse_steps,
        },
        "braid": {
            "raw_word": [[generator, sign] for generator, sign in word],
            "raw_length": len(word),
            "free_reduced_word": [[generator, sign] for generator, sign in reduced],
            "free_reduced_length": len(reduced),
            "minimum_projected_event_parameter_separation": format(
                minimum_event_gap, ".17g"
            ),
            "final_order": final_order,
            "final_root_permutation": final_permutation,
        },
        "homology": {
            "integral_symplectic_matrix": matrix_rows(action),
            "rank_M_minus_I": action_delta.rank(),
            "M_minus_I_square_zero": action_delta * action_delta == sp.zeros(4),
            "matrix_in_A114_frozen_marking": matrix_rows(transported_action),
            "marking_transport": marking_transport,
            "matches_A113_candidate_matrix": bool(
                np.array_equal(transported_action, expected_action)
            ),
        },
        "strict_scope": {
            "pointwise_root_balls_certified": True,
            "continuous_root_tubes_certified": False,
            "promotion_accepted": False,
        },
    }

    if not args.no_save:
        OUTPUT.mkdir(parents=True, exist_ok=True)
        trajectory_path = OUTPUT / f"{args.root_id}_pointwise_root_trajectory.npz"
        np.savez_compressed(
            trajectory_path,
            w=np.asarray(points, dtype=np.complex128),
            roots=np.asarray(trajectories, dtype=np.complex128),
            root_radius_uppers=np.asarray(radii_rows, dtype=np.float64),
        )
        packet["trajectory"] = {
            "path": str(trajectory_path.relative_to(ROOT)).replace("\\", "/"),
            "sha256": hashlib.sha256(trajectory_path.read_bytes()).hexdigest(),
        }
        packet_path = OUTPUT / f"{args.root_id}.trajectory.packet.json"
        packet_path.write_text(
            json.dumps(packet, indent=2, sort_keys=True) + "\n", encoding="utf-8"
        )
        print(f"wrote {packet_path}")
    print(json.dumps(packet, indent=2, sort_keys=True))
    print(f"elapsed_seconds={time.perf_counter() - started:.8g}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
