from __future__ import annotations

import hashlib
import json
import math
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
A113_PATHS = (
    ROOT
    / "candidate_data"
    / "selected_q79genus2basedpathsystemandmonodromycandidate"
    / "certified_based_meridian_and_handle_paths.packet.json"
)
OUTPUT = (
    ROOT
    / "candidate_data"
    / "selected_q79genus2handlemonodromycandidate"
    / "handle_monodromy_exploration.packet.json"
)


def load(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def dump(path: Path, payload: dict) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(payload, indent=2, sort_keys=True) + "\n", encoding="utf-8")


def midpoint(value: acb) -> complex:
    return complex(float(value.real.mid()), float(value.imag.mid()))


def radius_upper(value: acb) -> float:
    return float(value.rad().upper())


def complex_packet(value: complex) -> list[str]:
    return [format(value.real, ".17g"), format(value.imag, ".17g")]


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
    ctx.dps = 55
    fibration = load(FIBRATION)
    path_packet = load(A113_PATHS)

    a, b, t, s = sp.symbols("a b t s")
    t_coefficients = [
        sp.sympify(value)
        for value in fibration["fiber_chart"]["f_coefficients_t_descending"]
    ]
    f_ab = sum(
        coefficient * t ** (6 - index)
        for index, coefficient in enumerate(t_coefficients)
    )
    omitted = 2 + 3 * sp.I
    transformed = sp.Poly(
        sp.expand(s**6 * f_ab.subs(t, omitted + 1 / s)), s
    ).all_coeffs()

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

    def roots_at(w_value: complex) -> tuple[np.ndarray, list[float]]:
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

    intersection = np.asarray(
        [[0, 1, 0, 0], [-1, 0, 0, 0], [0, 0, 0, 1], [0, 0, -1, 0]],
        dtype=object,
    )
    chain_vectors = [
        np.asarray(vector, dtype=object).reshape(4, 1)
        for vector in [
            (1, 0, 0, 0),
            (0, 1, 0, 0),
            (-1, 0, 1, 0),
            (0, 0, 0, 1),
            (0, 0, -1, 0),
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
        ratio = float(costs[rows, columns].max() / minimum_separation)
        return current, radii, ratio

    def transport(endpoint: complex) -> tuple[list[complex], list[np.ndarray], list[list[float]], float]:
        points: list[complex] = [base]
        trajectories: list[np.ndarray] = [base_roots.copy()]
        radii_rows: list[list[float]] = [base_radii.copy()]
        maximum_ratio = 0.0

        def advance(
            start: complex,
            end: complex,
            previous: np.ndarray,
            depth: int,
        ) -> np.ndarray:
            nonlocal maximum_ratio
            unordered, unordered_radii = roots_at(end)
            current, radii, ratio = match(previous, unordered, unordered_radii)
            if ratio > 0.075:
                if depth >= 22:
                    raise AssertionError(f"handle transport did not resolve at {end!r}")
                middle = (start + end) / 2
                middle_roots = advance(start, middle, previous, depth + 1)
                return advance(middle, end, middle_roots, depth + 1)
            maximum_ratio = max(maximum_ratio, ratio)
            points.append(end)
            trajectories.append(current)
            radii_rows.append(radii)
            return current

        previous = base_roots
        coarse_points = np.linspace(base, endpoint, 129)
        for start, end in zip(coarse_points, coarse_points[1:]):
            previous = advance(complex(start), complex(end), previous, 0)
        return points, trajectories, radii_rows, maximum_ratio

    def word_from_trajectories(trajectories: list[np.ndarray]) -> tuple[list[tuple[int, int]], list[int], float]:
        order = list(range(6))
        word: list[tuple[int, int]] = []
        minimum_event_gap = 1.0
        for left_roots, right_roots in zip(trajectories, trajectories[1:]):
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
                    raise AssertionError("nonadjacent handle-braid crossing")
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

    handles: list[dict] = []
    for path_row in path_packet["torus_handle_paths"]:
        name = path_row["name"]
        endpoint = base + (1 if name == "A" else 1j)
        print(f"transporting handle {name}", flush=True)
        points, trajectories, radii_rows, maximum_ratio = transport(endpoint)
        word, final_order, minimum_event_gap = word_from_trajectories(trajectories)
        reduced = free_reduce(word)
        action = np.eye(4, dtype=object)
        for generator, sign in word:
            action = (positive[generator - 1] if sign == 1 else negative[generator - 1]) @ action
        if not np.array_equal(action.T @ intersection @ action, intersection):
            raise AssertionError(f"handle {name} matrix is not symplectic")

        final_permutation = [
            int(np.argmin(abs(trajectories[-1][label] - base_roots)))
            for label in range(6)
        ]
        if sorted(final_permutation) != list(range(6)):
            raise AssertionError("handle endpoint matching is not a permutation")

        trajectory_path = OUTPUT.parent / f"handle_{name}_pointwise_root_trajectory.npz"
        trajectory_path.parent.mkdir(parents=True, exist_ok=True)
        np.savez_compressed(
            trajectory_path,
            w=np.asarray(points, dtype=np.complex128),
            roots=np.asarray(trajectories, dtype=np.complex128),
            root_radius_uppers=np.asarray(radii_rows, dtype=np.float64),
        )
        handles.append(
            {
                "name": name,
                "path": f"w(s)=(1+i)/4+s*{'1' if name == 'A' else 'i'}, 0<=s<=1",
                "sample_count": len(points),
                "maximum_step_to_root_separation_ratio": format(maximum_ratio, ".17g"),
                "minimum_projected_event_parameter_separation": format(minimum_event_gap, ".17g"),
                "raw_braid_word": [[generator, sign] for generator, sign in word],
                "raw_braid_word_length": len(word),
                "free_reduced_braid_word": [[generator, sign] for generator, sign in reduced],
                "free_reduced_braid_word_length": len(reduced),
                "final_root_permutation": final_permutation,
                "integral_symplectic_matrix_candidate": matrix_rows(action),
                "determinant": int(sp.Matrix(action.tolist()).det()),
                "pointwise_root_balls_certified": True,
                "continuous_root_tubes_certified": False,
                "trajectory": {
                    "path": str(trajectory_path.relative_to(ROOT)).replace("\\", "/"),
                    "sha256": hashlib.sha256(trajectory_path.read_bytes()).hexdigest(),
                    "arrays": {
                        "w": [len(points)],
                        "roots": [len(points), 6],
                        "root_radius_uppers": [len(points), 6],
                    },
                    "maximum_pointwise_root_radius_upper": format(
                        max(max(row) for row in radii_rows), ".8g"
                    ),
                },
            }
        )
        print(
            f"handle {name}: samples={len(points)} word={len(word)}/{len(reduced)} "
            f"perm={final_permutation} M={matrix_rows(action)}",
            flush=True,
        )

    payload = {
        "schema": "MTTQ79GenusTwoHandleMonodromyExploration.v1",
        "status": "TWO_HANDLE_SP4Z_CANDIDATES_COMPUTED_CONTINUOUS_ROOT_TUBES_OPEN",
        "authority": {
            "fibration_sha256": hashlib.sha256(FIBRATION.read_bytes()).hexdigest(),
            "A113_paths_sha256": hashlib.sha256(A113_PATHS.read_bytes()).hexdigest(),
            "python_flint_version": "0.9.0",
        },
        "fiber_chart": {
            "coordinate": "s=1/(t-(2+3i))",
            "projection_angle": "pi/7",
            "base_w": "(1+i)/4",
            "base_fiber": "(a,b)=(-i,1+i)",
        },
        "homology": {
            "basis": ["a1", "b1", "a2", "b2"],
            "intersection_matrix": matrix_rows(intersection),
            "chain_vectors": [[int(entry) for entry in vector.flat] for vector in chain_vectors],
        },
        "handles": handles,
        "strict_scope": {
            "handle_matrices_promoted": 0,
            "reason": "Pointwise root balls and exact braid-word matrix replay are available; continuous disjoint root tubes over every adaptive segment are not yet certified.",
        },
    }
    dump(OUTPUT, payload)
    print(f"wrote {OUTPUT}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
