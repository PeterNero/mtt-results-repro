from __future__ import annotations

import json
from pathlib import Path

import numpy as np
import sympy as sp

from explore_q79_pgl3_beta_zero import PGL3BetaEvaluator
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


def load(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


class SmoothnessProbe:
    def __init__(self, evaluator: PGL3BetaEvaluator) -> None:
        self.evaluator = evaluator
        homology = load(MONODROMY)["homology_convention"]
        self.uniformization = Q79GenusTwoRootTransport(FIBRATION, homology)
        self.a, self.b, self.t = sp.symbols("a b t")

    def execute(
        self,
        alignment: np.ndarray,
        samples: int = 201,
        *,
        line_chart: str = "z",
    ) -> dict:
        packet = self.evaluator.fibration_packet(
            alignment, line_chart=line_chart
        )
        coefficient_functions = [
            sp.lambdify((self.a, self.b), sp.sympify(value), "numpy")
            for value in packet["fiber_chart"]["f_coefficients_t_descending"]
        ]
        q_polynomial = sp.Poly(
            sp.sympify(packet["splitting"]["q_ab"]), self.t
        )
        q_functions = [
            sp.lambdify((self.a, self.b), value, "numpy")
            for value in q_polynomial.all_coeffs()
        ]
        minimum_branch_separation = float("inf")
        minimum_projective_branch_separation = float("inf")
        minimum_q_separation = float("inf")
        minimum_normalized_chart_scale = float("inf")
        branch_parameter = 0.0
        projective_branch_parameter = 0.0
        for parameter in np.linspace(0.0, 1.0, samples):
            a_ball, b_ball = self.uniformization.ab_at(
                self.uniformization.base + 1j * parameter
            )
            a_value = midpoint(a_ball)
            b_value = midpoint(b_ball)
            roots = np.roots(
                [
                    function(a_value, b_value)
                    for function in coefficient_functions
                ]
            )
            separation = min(
                abs(roots[left] - roots[right])
                for left in range(6)
                for right in range(left)
            )
            if separation < minimum_branch_separation:
                minimum_branch_separation = float(separation)
                branch_parameter = float(parameter)
            line = alignment @ np.asarray(
                [a_value, b_value, 1 + 0j], dtype=np.complex128
            )
            if line_chart == "z":
                points = [
                    np.asarray(
                        [
                            line[2],
                            line[2] * root,
                            -(line[0] + line[1] * root),
                        ],
                        dtype=np.complex128,
                    )
                    for root in roots
                ]
                chart_scale = abs(line[2]) / np.linalg.norm(line)
            elif line_chart == "y":
                points = [
                    np.asarray(
                        [
                            line[1],
                            -(line[0] + line[2] * root),
                            line[1] * root,
                        ],
                        dtype=np.complex128,
                    )
                    for root in roots
                ]
                chart_scale = abs(line[1]) / np.linalg.norm(line)
            else:
                raise ValueError(f"unsupported line chart {line_chart!r}")
            minimum_normalized_chart_scale = min(
                minimum_normalized_chart_scale, float(chart_scale)
            )
            projective_separation = min(
                np.sqrt(
                    max(
                        0.0,
                        1.0
                        - abs(np.vdot(points[left], points[right])) ** 2
                        / (
                            np.vdot(points[left], points[left]).real
                            * np.vdot(points[right], points[right]).real
                        ),
                    )
                )
                for left in range(6)
                for right in range(left)
            )
            if projective_separation < minimum_projective_branch_separation:
                minimum_projective_branch_separation = float(
                    projective_separation
                )
                projective_branch_parameter = float(parameter)
            q_roots = np.roots(
                [function(a_value, b_value) for function in q_functions]
            )
            minimum_q_separation = min(
                minimum_q_separation, float(abs(q_roots[0] - q_roots[1]))
            )
        return {
            "line_chart": line_chart,
            "sample_count": samples,
            "minimum_branch_point_separation": minimum_branch_separation,
            "minimum_branch_point_parameter": branch_parameter,
            "minimum_projective_branch_point_separation": (
                minimum_projective_branch_separation
            ),
            "minimum_projective_branch_point_parameter": (
                projective_branch_parameter
            ),
            "minimum_normalized_line_chart_scale": (
                minimum_normalized_chart_scale
            ),
            "minimum_q_root_separation": minimum_q_separation,
        }


def lm_step(jacobian: np.ndarray, beta: np.ndarray, damping: float) -> np.ndarray:
    return -np.linalg.solve(
        jacobian.conj().T @ jacobian
        + damping * np.eye(8, dtype=np.complex128),
        jacobian.conj().T @ beta,
    )


def damping_for_radius(
    jacobian: np.ndarray, beta: np.ndarray, radius: float
) -> tuple[float, np.ndarray]:
    lower = 0.0
    upper = 1.0
    while np.max(abs(lm_step(jacobian, beta, upper))) > radius:
        upper *= 10.0
        if upper > 1.0e18:
            raise AssertionError("LM damping search did not bracket the trust radius")
    for _ in range(64):
        middle = (lower + upper) / 2.0
        step = lm_step(jacobian, beta, middle)
        if np.max(abs(step)) > radius:
            lower = middle
        else:
            upper = middle
    return upper, lm_step(jacobian, beta, upper)
