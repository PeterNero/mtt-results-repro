from __future__ import annotations

import argparse
import json
from pathlib import Path

import numpy as np
from scipy.linalg import expm

from explore_q79_pgl3_beta_zero import PGL3BetaEvaluator
from q79_pgl3_beta_diagnostics import SmoothnessProbe, damping_for_radius


ROOT = Path(__file__).resolve().parents[1]
DEFAULT_INPUT = (
    ROOT
    / "candidate_data"
    / "selected_q79genus2delignebetaperiodandintegralbranchexecution"
    / "pgl3_adaptive_trust_region.exploratory.json"
)


def load(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def complex_value(value: dict) -> complex:
    if "r" in value:
        return complex(float(value["r"]), float(value["i"]))
    return complex(float(value["real"]), float(value["imaginary"]))


def complex_pair(value: complex) -> dict[str, float]:
    return {"r": float(value.real), "i": float(value.imag)}


def decode_carrier(source: dict) -> tuple[np.ndarray, complex]:
    alignment_rows = source.get("final_alignment", source.get("alignment"))
    if alignment_rows is None:
        raise KeyError("input packet has no alignment carrier")
    reference_value = source.get(
        "final_winding_reference",
        source.get("winding_reference_for_next", source.get("winding_reference")),
    )
    if reference_value is None:
        reference_value = (
            source.get("diagnostics", {})
            .get("base_lift_diagnostics", {})
            .get("wound_branch_point")
        )
    if reference_value is None:
        raise KeyError("input packet has no winding reference")
    return (
        np.asarray(
            [
                [complex_value(value) for value in row]
                for row in alignment_rows
            ],
            dtype=np.complex128,
        ),
        complex_value(reference_value),
    )


def shifted_alignment(
    alignment: np.ndarray,
    coordinates: np.ndarray,
    generators: list[np.ndarray],
) -> np.ndarray:
    tangent = sum(
        (
            coordinates[index] * generators[index]
            for index in range(8)
        ),
        np.zeros((3, 3), dtype=np.complex128),
    )
    return alignment @ expm(tangent)


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--input", type=Path, default=DEFAULT_INPUT)
    parser.add_argument("--output", type=Path, required=True)
    parser.add_argument("--iterations", type=int, default=6)
    parser.add_argument("--finite-difference-step", type=float, default=1.0e-4)
    parser.add_argument("--initial-radius", type=float, default=3.0e-2)
    parser.add_argument("--minimum-radius", type=float, default=2.0e-5)
    parser.add_argument("--minimum-clearance", type=float, default=1.5e-2)
    parser.add_argument(
        "--minimum-projective-clearance", type=float, default=0.0
    )
    parser.add_argument("--rtol", type=float, default=3.0e-6)
    parser.add_argument("--atol", type=float, default=3.0e-8)
    parser.add_argument("--base-rtol", type=float, default=3.0e-8)
    parser.add_argument("--base-atol", type=float, default=3.0e-10)
    parser.add_argument("--line-chart", choices=["z", "y"], default="z")
    parser.add_argument(
        "--base-lift-source-chart", choices=["z", "y"], default=None
    )
    arguments = parser.parse_args()

    input_path = arguments.input.resolve()
    source = load(input_path)
    source_relative = str(input_path.relative_to(ROOT.resolve())).replace(
        "\\", "/"
    )
    evaluator = PGL3BetaEvaluator()
    smoothness_probe = SmoothnessProbe(evaluator)
    alignment, winding_reference = decode_carrier(source)
    radius = arguments.initial_radius
    trace: list[dict] = []
    evaluation_kwargs = {
        "line_chart": arguments.line_chart,
        "base_lift_source_chart": arguments.base_lift_source_chart,
        "rtol": arguments.rtol,
        "atol": arguments.atol,
        "base_rtol": arguments.base_rtol,
        "base_atol": arguments.base_atol,
    }

    beta, diagnostics = evaluator.evaluate(
        alignment,
        winding_reference=winding_reference,
        **evaluation_kwargs,
    )
    branch = diagnostics["base_lift_diagnostics"]["wound_branch_point"]
    winding_reference = complex_value(branch)

    for iteration in range(1, arguments.iterations + 1):
        input_norm = float(np.linalg.norm(beta))
        finite_difference_rows: list[dict] = []
        jacobian = np.empty((8, 8), dtype=np.complex128)
        for index in range(8):
            coordinate = np.zeros(8, dtype=np.complex128)
            coordinate[index] = arguments.finite_difference_step
            shifted = shifted_alignment(
                alignment, coordinate, evaluator.generators
            )
            shifted_beta, shifted_diagnostics = evaluator.evaluate(
                shifted,
                winding_reference=winding_reference,
                **evaluation_kwargs,
            )
            jacobian[:, index] = (
                shifted_beta - beta
            ) / arguments.finite_difference_step
            finite_difference_rows.append(
                {
                    "direction": index,
                    "shifted_norm": float(np.linalg.norm(shifted_beta)),
                    "high_precision_reduction_count": shifted_diagnostics[
                        "high_precision_reduction_count"
                    ],
                }
            )
            print(
                f"iteration {iteration}: Jacobian column {index + 1}/8",
                flush=True,
            )

        singular_values = np.linalg.svd(jacobian, compute_uv=False)
        attempts: list[dict] = []
        accepted = None
        trial_radius = radius
        while trial_radius >= arguments.minimum_radius:
            damping, step = damping_for_radius(jacobian, beta, trial_radius)
            trial_alignment = shifted_alignment(
                alignment, step, evaluator.generators
            )
            try:
                trial_beta, trial_diagnostics = evaluator.evaluate(
                    trial_alignment,
                    winding_reference=winding_reference,
                    **evaluation_kwargs,
                )
                smoothness = smoothness_probe.execute(
                    trial_alignment, line_chart=arguments.line_chart
                )
                trial_norm = float(np.linalg.norm(trial_beta))
                attempt = {
                    "radius": trial_radius,
                    "damping": damping,
                    "step_maximum_absolute_value": float(np.max(abs(step))),
                    "predicted_norm": float(
                        np.linalg.norm(beta + jacobian @ step)
                    ),
                    "actual_norm": trial_norm,
                    "smoothness": smoothness,
                    "wound_branch": trial_diagnostics[
                        "base_lift_diagnostics"
                    ]["wound_branch_point"],
                }
                attempts.append(attempt)
                print(
                    "iteration "
                    f"{iteration}: radius={trial_radius:.8g}, "
                    f"norm={trial_norm:.12g}, "
                    "separation="
                    f"{smoothness['minimum_branch_point_separation']:.8g}",
                    flush=True,
                )
                if (
                    trial_norm < input_norm
                    and smoothness["minimum_branch_point_separation"]
                    >= arguments.minimum_clearance
                    and smoothness[
                        "minimum_projective_branch_point_separation"
                    ]
                    >= arguments.minimum_projective_clearance
                ):
                    accepted = (
                        step,
                        trial_alignment,
                        trial_beta,
                        trial_diagnostics,
                        smoothness,
                        damping,
                        trial_radius,
                    )
                    break
            except (AssertionError, ValueError) as error:
                attempts.append(
                    {
                        "radius": trial_radius,
                        "rejected": True,
                        "reason": str(error),
                    }
                )
            trial_radius /= 2.0

        iteration_packet = {
            "iteration": iteration,
            "input_norm": input_norm,
            "finite_difference_step": arguments.finite_difference_step,
            "jacobian_singular_values": [
                float(value) for value in singular_values
            ],
            "jacobian": [
                [complex_pair(value) for value in row] for row in jacobian
            ],
            "jacobian_condition_number": float(
                singular_values[0] / singular_values[-1]
            ),
            "finite_difference_rows": finite_difference_rows,
            "attempts": attempts,
            "accepted": accepted is not None,
        }
        if accepted is None:
            trace.append(iteration_packet)
            radius = trial_radius
            break

        (
            step,
            alignment,
            beta,
            diagnostics,
            smoothness,
            damping,
            radius,
        ) = accepted
        branch = diagnostics["base_lift_diagnostics"]["wound_branch_point"]
        winding_reference = complex_value(branch)
        iteration_packet.update(
            {
                "accepted_norm": float(np.linalg.norm(beta)),
                "accepted_radius": radius,
                "accepted_damping": damping,
                "accepted_step": [complex_pair(value) for value in step],
                "smoothness": smoothness,
                "wound_branch": complex_pair(winding_reference),
            }
        )
        trace.append(iteration_packet)
        radius = min(arguments.initial_radius, radius * 1.5)
        if np.linalg.norm(beta) < 1.0e-7:
            break

    result = {
        "schema": "MTTQ79PGL3CorrectedAlignedDivisorZeroSearch.v1",
        "status": "EXPLORATORY_CORRECTED_SOURCE_FRESH_JACOBIAN_TRUST_SEARCH",
        "source": source_relative,
        "source_correction": (
            "Every carrier uses the packet-selected aligned q_A roots and "
            "implicit q_A root velocities; no identity-divisor source is reused."
        ),
        "line_chart": arguments.line_chart,
        "base_lift_source_chart": (
            arguments.line_chart
            if arguments.base_lift_source_chart is None
            else arguments.base_lift_source_chart
        ),
        "trace": trace,
        "final_beta_norm": float(np.linalg.norm(beta)),
        "final_beta": [complex_pair(value) for value in beta],
        "final_alignment": [
            [complex_pair(value) for value in row] for row in alignment
        ],
        "final_winding_reference": complex_pair(winding_reference),
        "final_radius": radius,
        "strict_scope": {
            "floating_exploration_only": True,
            "target_branch": "ell_92=0",
            "observed_SM_values_used": False,
            "interval_certified": False,
            "PGL3_zero_found": bool(np.linalg.norm(beta) < 1.0e-6),
        },
    }
    arguments.output.parent.mkdir(parents=True, exist_ok=True)
    arguments.output.write_text(
        json.dumps(result, indent=2, sort_keys=True) + "\n",
        encoding="utf-8",
    )
    print(
        json.dumps(
            {
                "iterations_executed": len(trace),
                "accepted_iterations": sum(
                    int(value["accepted"]) for value in trace
                ),
                "final_beta_norm": result["final_beta_norm"],
                "final_radius": radius,
                "zero_found": result["strict_scope"]["PGL3_zero_found"],
            },
            indent=2,
        )
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
