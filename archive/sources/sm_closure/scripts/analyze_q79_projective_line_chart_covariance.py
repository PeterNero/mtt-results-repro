from __future__ import annotations

import argparse
import json
import math
from pathlib import Path

import numpy as np
import sympy as sp

from explore_q79_pgl3_beta_zero import PGL3BetaEvaluator
from q79_pgl3_beta_diagnostics import SmoothnessProbe
from q79genus2_root_transport import midpoint


ROOT = Path(__file__).resolve().parents[1]
DIRECTORY = (
    ROOT
    / "candidate_data"
    / "selected_q79genus2delignebetaperiodandintegralbranchexecution"
)
CLEAN = DIRECTORY / "pgl3_corrected_identity_zero_search_04.exploratory.json"
OLD = DIRECTORY / "pgl3_corrected_source_zero_search_lowclearance_02.exploratory.json"
FRESH = [
    DIRECTORY / f"pgl3_projective_ychart_zero_search_{index:02d}.exploratory.json"
    for index in range(1, 4)
]
BROYDEN = [
    DIRECTORY / f"pgl3_projective_ychart_broyden_{index:02d}.exploratory.json"
    for index in range(4, 6)
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


def alignment(packet: dict) -> np.ndarray:
    rows = packet.get("final_alignment", packet.get("alignment"))
    return np.asarray(
        [[complex_value(value) for value in row] for row in rows],
        dtype=np.complex128,
    )


def exact_chart_checks() -> dict:
    ell_0, ell_1, ell_2, t, s = sp.symbols("ell_0 ell_1 ell_2 t s")
    transition = -(ell_0 + ell_2 * s) / ell_1
    degree_checks: dict[str, bool] = {}
    for degree in [2, 3, 4, 6]:
        residuals = []
        for x_power in range(degree + 1):
            for y_power in range(degree - x_power + 1):
                z_power = degree - x_power - y_power
                z_chart = (
                    ell_2**x_power
                    * (ell_2 * t) ** y_power
                    * (-(ell_0 + ell_1 * t)) ** z_power
                )
                y_chart = (
                    ell_1**x_power
                    * (-(ell_0 + ell_2 * s)) ** y_power
                    * (ell_1 * s) ** z_power
                )
                residuals.append(
                    sp.cancel(
                        z_chart.subs(t, transition)
                        - (ell_2 / ell_1) ** degree * y_chart
                    )
                )
        degree_checks[str(degree)] = all(value == 0 for value in residuals)

    v_0, v_1, v_2 = sp.symbols("v_0 v_1 v_2")
    numerator_z = ell_2 * (
        (v_0 * ell_2 - v_2 * ell_0)
        + (v_1 * ell_2 - v_2 * ell_1) * t
    )
    numerator_y = -ell_1 * (
        (v_0 * ell_1 - v_1 * ell_0)
        + (v_2 * ell_1 - v_1 * ell_2) * s
    )
    residue_transition = sp.cancel(
        numerator_z.subs(t, transition)
        * sp.diff(transition, s)
        / ell_2**3
        - numerator_y / ell_1**3
    )

    alpha = -ell_0 / ell_1
    beta = -ell_2 / ell_1
    common = -(ell_1**2) / (ell_2**2)
    period_transition = sp.zeros(5, 5)
    for power in range(5):
        for index in range(power + 1):
            period_transition[power, index] = (
                common
                * math.comb(power, index)
                * alpha ** (power - index)
                * beta**index
            )
    determinant = sp.cancel(period_transition.det())
    return {
        "homogeneous_degree_transition_residuals_zero": degree_checks,
        "residue_form_transition_residual": str(residue_transition),
        "five_period_transition_determinant": str(determinant),
        "transition": "t_z=-(ell_0+ell_2*t_y)/ell_1",
        "fiber_scaling": "U_z=(ell_2/ell_1)^3*U_y",
    }


def chart_metrics(
    evaluator: PGL3BetaEvaluator,
    probe: SmoothnessProbe,
    carrier: np.ndarray,
    samples: int = 1001,
) -> dict:
    a, b = sp.symbols("a b")
    packets = {
        chart: evaluator.fibration_packet(carrier, line_chart=chart)
        for chart in ["z", "y"]
    }
    functions = {
        chart: [
            sp.lambdify((a, b), sp.sympify(value), "numpy")
            for value in packet["fiber_chart"][
                "f_coefficients_t_descending"
            ]
        ]
        for chart, packet in packets.items()
    }
    minimum_separation = {"z": float("inf"), "y": float("inf")}
    minimum_normalized_scale = {"z": float("inf"), "y": float("inf")}
    maximum_root_transition_residual = 0.0
    for parameter in np.linspace(0.0, 1.0, samples):
        a_ball, b_ball = probe.uniformization.ab_at(
            probe.uniformization.base + 1j * parameter
        )
        a_value = midpoint(a_ball)
        b_value = midpoint(b_ball)
        line = carrier @ np.asarray(
            [a_value, b_value, 1 + 0j], dtype=np.complex128
        )
        roots = {
            chart: np.roots(
                [function(a_value, b_value) for function in chart_functions]
            )
            for chart, chart_functions in functions.items()
        }
        for chart in ["z", "y"]:
            separation = min(
                abs(roots[chart][left] - roots[chart][right])
                for left in range(6)
                for right in range(left)
            )
            minimum_separation[chart] = min(
                minimum_separation[chart], float(separation)
            )
        line_norm = np.linalg.norm(line)
        minimum_normalized_scale["z"] = min(
            minimum_normalized_scale["z"], float(abs(line[2]) / line_norm)
        )
        minimum_normalized_scale["y"] = min(
            minimum_normalized_scale["y"], float(abs(line[1]) / line_norm)
        )
        mapped = [
            -(line[0] + line[1] * value) / line[2]
            for value in roots["z"]
        ]
        maximum_root_transition_residual = max(
            maximum_root_transition_residual,
            max(
                min(abs(value - target) for target in roots["y"])
                for value in mapped
            ),
        )
    y_probe = probe.execute(carrier, samples=samples, line_chart="y")
    return {
        "sample_count": samples,
        "minimum_affine_branch_separation": minimum_separation,
        "minimum_normalized_line_chart_scale": minimum_normalized_scale,
        "maximum_root_transition_matching_residual": float(
            maximum_root_transition_residual
        ),
        "minimum_projective_branch_separation_in_y_chart": y_probe[
            "minimum_projective_branch_point_separation"
        ],
    }


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--output", type=Path, required=True)
    arguments = parser.parse_args()

    evaluator = PGL3BetaEvaluator()
    probe = SmoothnessProbe(evaluator)
    clean = load(CLEAN)
    old = load(OLD)
    clean_alignment = alignment(clean)
    clean_beta = np.asarray(
        [complex_value(value) for value in clean["final_beta"]]
    )
    y_beta, y_diagnostics = evaluator.evaluate(
        clean_alignment,
        line_chart="y",
        base_lift_source_chart="z",
        winding_reference=complex_value(clean["final_winding_reference"]),
        rtol=3.0e-6,
        atol=3.0e-8,
        base_rtol=3.0e-8,
        base_atol=3.0e-10,
    )

    fresh = [load(path) for path in FRESH]
    broyden = [load(path) for path in BROYDEN]
    continuation_packets = [clean, *fresh, *broyden]
    continuation = []
    for path, packet in zip([CLEAN, *FRESH, *BROYDEN], continuation_packets):
        smoothness = probe.execute(alignment(packet), line_chart="y")
        continuation.append(
            {
                "source": str(path.relative_to(ROOT)).replace("\\", "/"),
                "beta_norm": float(packet["final_beta_norm"]),
                "minimum_affine_y_chart_separation": smoothness[
                    "minimum_branch_point_separation"
                ],
                "minimum_projective_branch_separation": smoothness[
                    "minimum_projective_branch_point_separation"
                ],
                "minimum_normalized_y_chart_scale": smoothness[
                    "minimum_normalized_line_chart_scale"
                ],
            }
        )

    packet = {
        "schema": "MTTQ79ProjectiveLineChartCovarianceAndEllZeroContinuation.v1",
        "status": "EXACT_TWO_CHART_COVARIANCE_AND_FLOATING_ELL_ZERO_CONTINUATION",
        "exact_chart_checks": exact_chart_checks(),
        "A122_endpoint_reclassification": {
            "clean_identity_endpoint": chart_metrics(
                evaluator, probe, clean_alignment
            ),
            "independent_old_carrier_endpoint": chart_metrics(
                evaluator, probe, alignment(old)
            ),
            "decision": (
                "The small z-chart root gaps are not nodal invariants. The "
                "regular y-chart keeps both endpoints uniformly separated."
            ),
        },
        "same_branch_beta_chart_covariance": {
            "z_chart_beta_norm": float(np.linalg.norm(clean_beta)),
            "y_chart_beta_norm": float(np.linalg.norm(y_beta)),
            "maximum_absolute_difference": float(
                np.max(abs(y_beta - clean_beta))
            ),
            "projective_overlap": float(
                abs(np.vdot(y_beta, clean_beta))
                / (np.linalg.norm(y_beta) * np.linalg.norm(clean_beta))
            ),
            "base_lift_transition_maximum_absolute_residual": float(
                y_diagnostics["base_lift_diagnostics"][
                    "base_lift_transition_maximum_absolute_residual"
                ]
            ),
            "base_lift_source_chart": "z",
            "execution_chart": "y",
        },
        "ell_zero_continuation": {
            "points": continuation,
            "beta_norms": [value["beta_norm"] for value in continuation],
            "fresh_Jacobian_steps": 3,
            "guarded_Broyden_steps": 2,
            "latest_beta_norm": continuation[-1]["beta_norm"],
            "latest_projective_branch_separation": continuation[-1][
                "minimum_projective_branch_separation"
            ],
            "larger_step_one_sided_jump_diagnostics": broyden[-1]["attempts"][:3],
        },
        "decision": {
            "A122_nodal_wall_interpretation_retired": True,
            "A122_exact_aligned_source_theorem_preserved": True,
            "ell_zero_search_advanced_beyond_old_chart_wall": True,
            "smooth_ell_zero_found": False,
            "ell_zero_no_go_proved": False,
            "genuine_Picard_Lefschetz_boundary_localized": True,
            "next_required_step": (
                "regularize the one-sided simple-node transport by its local "
                "Picard-Lefschetz residue and certify the limiting beta vector"
            ),
        },
        "strict_scope": {
            "exact": [
                "homogeneous z/y chart transition in degrees 2,3,4,6",
                "residue one-form covariance",
                "five-period transition determinant -1",
            ],
            "floating": [
                "root matching and projective clearances",
                "same-branch beta chart comparison",
                "fresh-Jacobian and Broyden continuation",
            ],
            "not_claimed": [
                "a PGL3 zero",
                "an ell=0 no-go",
                "an interval-certified one-sided PL limit",
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
                "exact_chart_checks": packet["exact_chart_checks"],
                "beta_chart_maximum_difference": packet[
                    "same_branch_beta_chart_covariance"
                ]["maximum_absolute_difference"],
                "beta_norm_chain": packet["ell_zero_continuation"][
                    "beta_norms"
                ],
                "latest_projective_separation": packet[
                    "ell_zero_continuation"
                ]["latest_projective_branch_separation"],
            },
            indent=2,
        )
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
