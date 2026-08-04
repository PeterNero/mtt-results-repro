from __future__ import annotations

import argparse
import json
from pathlib import Path

import numpy as np
import sympy as sp
from scipy.optimize import minimize_scalar

from explore_q79_pgl3_beta_zero import PGL3BetaEvaluator
from q79_pgl3_beta_diagnostics import SmoothnessProbe
from q79genus2_root_transport import midpoint


ROOT = Path(__file__).resolve().parents[1]
DIRECTORY = (
    ROOT
    / "candidate_data"
    / "selected_q79genus2delignebetaperiodandintegralbranchexecution"
)
IDENTITY = DIRECTORY / "pgl3_identity_generalized_evaluator.diagnostic.json"
OLD_CARRIER = DIRECTORY / "pgl3_retired_pre_fix_alignment_seed.exploratory.json"
CORRECTED_PROBE = (
    DIRECTORY / "pgl3_corrected_aligned_divisor_continuity_probe.exploratory.json"
)
OLD_DESCENT = DIRECTORY / "pgl3_corrected_source_zero_search.exploratory.json"
OLD_LOW_1 = DIRECTORY / "pgl3_corrected_source_zero_search_lowclearance_01.exploratory.json"
OLD_LOW_2 = DIRECTORY / "pgl3_corrected_source_zero_search_lowclearance_02.exploratory.json"
CLEAN_DESCENT = [
    DIRECTORY / f"pgl3_corrected_identity_zero_search_{index:02d}.exploratory.json"
    for index in range(1, 5)
]


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


def alignment_from(packet: dict, key: str) -> np.ndarray:
    return np.asarray(
        [
            [complex_value(value) for value in row]
            for row in packet[key]
        ],
        dtype=np.complex128,
    )


def beta_from(packet: dict, key: str) -> np.ndarray:
    return np.asarray(
        [complex_value(value) for value in packet[key]],
        dtype=np.complex128,
    )


def closest_branch_pair(
    evaluator: PGL3BetaEvaluator,
    probe: SmoothnessProbe,
    alignment: np.ndarray,
) -> dict:
    packet = evaluator.fibration_packet(alignment)
    a, b = probe.a, probe.b
    coefficient_functions = [
        sp.lambdify((a, b), sp.sympify(value), "numpy")
        for value in packet["fiber_chart"]["f_coefficients_t_descending"]
    ]

    def root_data(parameter: float) -> tuple[float, complex, complex]:
        a_ball, b_ball = probe.uniformization.ab_at(
            probe.uniformization.base + 1j * parameter
        )
        a_value = midpoint(a_ball)
        b_value = midpoint(b_ball)
        roots = np.roots(
            [
                function(a_value, b_value)
                for function in coefficient_functions
            ]
        )
        left, right = min(
            (
                (left, right)
                for left in range(6)
                for right in range(left)
            ),
            key=lambda pair: abs(roots[pair[0]] - roots[pair[1]]),
        )
        return (
            float(abs(roots[left] - roots[right])),
            roots[left],
            roots[right],
        )

    samples = np.linspace(0.0, 1.0, 1001)
    separations = np.asarray([root_data(value)[0] for value in samples])
    index = int(np.argmin(separations))
    lower = float(samples[max(0, index - 2)])
    upper = float(samples[min(len(samples) - 1, index + 2)])
    optimized = minimize_scalar(
        lambda value: root_data(float(value))[0] ** 2,
        bounds=(lower, upper),
        method="bounded",
        options={"xatol": 1.0e-13},
    )
    separation, root_left, root_right = root_data(float(optimized.x))
    difference = root_left - root_right
    return {
        "base_parameter": format(float(optimized.x), ".17g"),
        "branch_separation": format(separation, ".17g"),
        "branch_midpoint": complex_pair((root_left + root_right) / 2.0),
        "branch_difference": complex_pair(difference),
        "local_discriminant_coordinate_difference_squared": complex_pair(
            difference**2
        ),
        "dense_sample_count": len(samples),
        "bounded_minimizer_success": bool(optimized.success),
    }


def projective_overlap(left: np.ndarray, right: np.ndarray) -> float:
    return float(
        abs(np.vdot(left, right))
        / (np.linalg.norm(left) * np.linalg.norm(right))
    )


def trajectory_fit(points: list[dict]) -> dict:
    fit_points = points[-3:]
    separations = np.asarray(
        [float(point["geometry"]["branch_separation"]) for point in fit_points]
    )
    betas = np.asarray(
        [
            [complex_value(value) for value in point["beta_vector"]]
            for point in fit_points
        ],
        dtype=np.complex128,
    )
    norms = np.linalg.norm(betas, axis=1)

    def execute(coordinate: np.ndarray) -> dict:
        design = np.column_stack([np.ones(len(coordinate)), coordinate])
        norm_coefficients = np.linalg.lstsq(design, norms, rcond=None)[0]
        beta_coefficients = np.linalg.lstsq(design, betas, rcond=None)[0]
        fitted_norms = design @ norm_coefficients
        return {
            "extrapolated_norm_at_zero_coordinate": float(norm_coefficients[0]),
            "extrapolated_beta_at_zero_coordinate": [
                complex_pair(value) for value in beta_coefficients[0]
            ],
            "extrapolated_beta_norm_at_zero_coordinate": float(
                np.linalg.norm(beta_coefficients[0])
            ),
            "fit_norm_maximum_absolute_residual": float(
                np.max(abs(fitted_norms - norms))
            ),
        }

    return {
        "fit_point_ids": [point["id"] for point in fit_points],
        "linear_in_branch_separation": execute(separations),
        "linear_in_sqrt_branch_separation": execute(np.sqrt(separations)),
        "successive_projective_beta_overlaps": [
            projective_overlap(betas[index - 1], betas[index])
            for index in range(1, len(betas))
        ],
    }


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--output", type=Path, required=True)
    arguments = parser.parse_args()

    evaluator = PGL3BetaEvaluator()
    probe = SmoothnessProbe(evaluator)
    identity = load(IDENTITY)
    clean_specs = [
        (
            "clean_identity_00",
            IDENTITY,
            alignment_from(identity, "alignment"),
            beta_from(identity, "beta_vector"),
        )
    ]
    for index, path in enumerate(CLEAN_DESCENT, start=1):
        packet = load(path)
        clean_specs.append(
            (
                f"clean_identity_{index:02d}",
                path,
                alignment_from(packet, "final_alignment"),
                beta_from(packet, "final_beta"),
            )
        )

    old_carrier = load(OLD_CARRIER)
    corrected_probe = load(CORRECTED_PROBE)
    old_specs = [
        (
            "old_carrier_corrected_00",
            OLD_CARRIER,
            alignment_from(old_carrier, "alignment"),
            beta_from(corrected_probe, "forced_base"),
        )
    ]
    for index, path in enumerate([OLD_DESCENT, OLD_LOW_1, OLD_LOW_2], start=1):
        packet = load(path)
        old_specs.append(
            (
                f"old_carrier_corrected_{index:02d}",
                path,
                alignment_from(packet, "final_alignment"),
                beta_from(packet, "final_beta"),
            )
        )

    def execute(specifications: list[tuple]) -> list[dict]:
        points = []
        for identifier, path, alignment, beta in specifications:
            points.append(
                {
                    "id": identifier,
                    "source": str(path.relative_to(ROOT)).replace("\\", "/"),
                    "beta_norm": float(np.linalg.norm(beta)),
                    "beta_vector": [complex_pair(value) for value in beta],
                    "geometry": closest_branch_pair(
                        evaluator, probe, alignment
                    ),
                }
            )
        return points

    clean_points = execute(clean_specs)
    old_points = execute(old_specs)
    clean_fit = trajectory_fit(clean_points)
    old_fit = trajectory_fit(old_points)
    packet = {
        "schema": "MTTQ79CorrectedPGL3NodalApproachAnalysis.v1",
        "status": "EXPLORATORY_TWO_BASIN_NODAL_RESIDUAL_ANALYSIS",
        "source_correction": (
            "All nonidentity beta vectors use the aligned q_A divisor and "
            "implicit q_A root velocities."
        ),
        "trajectories": {
            "clean_identity_restart": {
                "points": clean_points,
                "three_point_local_fits": clean_fit,
            },
            "old_carrier_recomputed_after_source_fix": {
                "points": old_points,
                "three_point_local_fits": old_fit,
            },
        },
        "cross_trajectory_latest_projective_beta_overlap": projective_overlap(
            np.asarray(
                [complex_value(value) for value in clean_points[-1]["beta_vector"]]
            ),
            np.asarray(
                [complex_value(value) for value in old_points[-1]["beta_vector"]]
            ),
        ),
        "decision": {
            "smooth_ell_zero_branch_found": False,
            "exact_ell_zero_no_go_proved": False,
            "observed_pattern": (
                "Two corrected fresh-Jacobian trajectories reduce beta while "
                "approaching a branch collision with an order-one residual."
            ),
            "lawful_next_step": (
                "Use a Picard-Lefschetz local coordinate to prove or refute a "
                "nonzero residual limit, or continue on a fixed nonzero integral branch."
            ),
        },
        "strict_scope": {
            "floating_exploration_only": True,
            "regression_is_not_a_separation_theorem": True,
            "nodal_limit_interval_certified": False,
            "PGL3_zero_claimed": False,
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
                "clean_latest_norm": clean_points[-1]["beta_norm"],
                "clean_latest_separation": clean_points[-1]["geometry"][
                    "branch_separation"
                ],
                "clean_linear_limit_norm": clean_fit[
                    "linear_in_branch_separation"
                ]["extrapolated_beta_norm_at_zero_coordinate"],
                "old_latest_norm": old_points[-1]["beta_norm"],
                "old_latest_separation": old_points[-1]["geometry"][
                    "branch_separation"
                ],
                "old_linear_limit_norm": old_fit[
                    "linear_in_branch_separation"
                ]["extrapolated_beta_norm_at_zero_coordinate"],
                "cross_latest_projective_overlap": packet[
                    "cross_trajectory_latest_projective_beta_overlap"
                ],
            },
            indent=2,
        )
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
