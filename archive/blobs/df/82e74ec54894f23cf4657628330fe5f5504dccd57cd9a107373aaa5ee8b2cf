from __future__ import annotations

import argparse
import json
from pathlib import Path

import numpy as np

from explore_q79_pgl3_beta_zero import PGL3BetaEvaluator
from q79_pgl3_beta_diagnostics import (
    SmoothnessProbe,
    damping_for_radius,
)
from solve_q79_pgl3_beta_zero_corrected import (
    decode_carrier,
    shifted_alignment,
)


ROOT = Path(__file__).resolve().parents[1]


def load(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def complex_value(value: dict) -> complex:
    if "r" in value:
        return complex(float(value["r"]), float(value["i"]))
    return complex(float(value["real"]), float(value["imaginary"]))


def complex_pair(value: complex) -> dict[str, float]:
    return {"r": float(value.real), "i": float(value.imag)}


def complex_vector(values: list[dict]) -> np.ndarray:
    return np.asarray([complex_value(value) for value in values])


def complex_matrix(rows: list[list[dict]]) -> np.ndarray:
    return np.asarray(
        [[complex_value(value) for value in row] for row in rows],
        dtype=np.complex128,
    )


def current_jacobian(packet: dict, packet_path: Path) -> np.ndarray:
    if "current_jacobian" in packet:
        return complex_matrix(packet["current_jacobian"])
    trace = packet["trace"][-1]
    if "jacobian" not in trace or "accepted_step" not in trace:
        raise ValueError("input packet does not retain an accepted Jacobian step")
    source_path = (ROOT / packet["source"]).resolve()
    source = load(source_path)
    beta_before = complex_vector(source["final_beta"])
    beta_after = complex_vector(packet["final_beta"])
    step = complex_vector(trace["accepted_step"])
    jacobian = complex_matrix(trace["jacobian"])
    secant_error = beta_after - beta_before - jacobian @ step
    denominator = np.vdot(step, step).real
    if denominator <= 0:
        raise ValueError("accepted step has zero norm")
    return jacobian + np.outer(secant_error, step.conj()) / denominator


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--input", type=Path, required=True)
    parser.add_argument("--output", type=Path, required=True)
    parser.add_argument("--initial-radius", type=float, default=2.0e-3)
    parser.add_argument("--minimum-radius", type=float, default=2.5e-5)
    parser.add_argument("--minimum-clearance", type=float, default=8.0e-3)
    parser.add_argument(
        "--minimum-projective-clearance", type=float, default=6.0e-3
    )
    parser.add_argument("--rtol", type=float, default=3.0e-6)
    parser.add_argument("--atol", type=float, default=3.0e-8)
    parser.add_argument("--base-rtol", type=float, default=3.0e-8)
    parser.add_argument("--base-atol", type=float, default=3.0e-10)
    arguments = parser.parse_args()

    input_path = arguments.input.resolve()
    packet = load(input_path)
    input_relative = str(input_path.relative_to(ROOT.resolve())).replace(
        "\\", "/"
    )
    evaluator = PGL3BetaEvaluator()
    probe = SmoothnessProbe(evaluator)
    alignment, winding_reference = decode_carrier(packet)
    beta = complex_vector(packet["final_beta"])
    jacobian = current_jacobian(packet, input_path)
    line_chart = packet.get("line_chart", "z")
    base_source_chart = packet.get("base_lift_source_chart", line_chart)
    evaluation_kwargs = {
        "line_chart": line_chart,
        "base_lift_source_chart": base_source_chart,
        "rtol": arguments.rtol,
        "atol": arguments.atol,
        "base_rtol": arguments.base_rtol,
        "base_atol": arguments.base_atol,
    }

    attempts: list[dict] = []
    accepted = None
    radius = arguments.initial_radius
    while radius >= arguments.minimum_radius:
        damping, step = damping_for_radius(jacobian, beta, radius)
        trial_alignment = shifted_alignment(
            alignment, step, evaluator.generators
        )
        trial_beta, diagnostics = evaluator.evaluate(
            trial_alignment,
            winding_reference=winding_reference,
            **evaluation_kwargs,
        )
        smoothness = probe.execute(
            trial_alignment, line_chart=line_chart
        )
        attempt = {
            "radius": radius,
            "damping": damping,
            "step_maximum_absolute_value": float(np.max(abs(step))),
            "predicted_norm": float(np.linalg.norm(beta + jacobian @ step)),
            "actual_norm": float(np.linalg.norm(trial_beta)),
            "smoothness": smoothness,
        }
        attempts.append(attempt)
        print(
            f"radius={radius:.8g}, norm={attempt['actual_norm']:.12g}, "
            "projective_separation="
            f"{smoothness['minimum_projective_branch_point_separation']:.8g}",
            flush=True,
        )
        if (
            attempt["actual_norm"] < float(np.linalg.norm(beta))
            and smoothness["minimum_branch_point_separation"]
            >= arguments.minimum_clearance
            and smoothness["minimum_projective_branch_point_separation"]
            >= arguments.minimum_projective_clearance
        ):
            accepted = (
                step,
                trial_alignment,
                trial_beta,
                diagnostics,
                smoothness,
                radius,
            )
            break
        radius /= 2.0

    input_norm = float(np.linalg.norm(beta))
    if accepted is not None:
        (
            step,
            alignment,
            trial_beta,
            diagnostics,
            smoothness,
            radius,
        ) = accepted
        secant_error = trial_beta - beta - jacobian @ step
        jacobian = jacobian + np.outer(
            secant_error, step.conj()
        ) / np.vdot(step, step).real
        beta = trial_beta
        winding_reference = complex_value(
            diagnostics["base_lift_diagnostics"]["wound_branch_point"]
        )

    singular_values = np.linalg.svd(jacobian, compute_uv=False)
    result = {
        "schema": "MTTQ79PGL3ProjectiveChartBroydenContinuation.v1",
        "status": "EXPLORATORY_SAME_BRANCH_PROJECTIVE_CHART_BROYDEN_CONTINUATION",
        "source": input_relative,
        "line_chart": line_chart,
        "base_lift_source_chart": base_source_chart,
        "input_beta_norm": input_norm,
        "attempts": attempts,
        "accepted": accepted is not None,
        "final_beta_norm": float(np.linalg.norm(beta)),
        "final_beta": [complex_pair(value) for value in beta],
        "final_alignment": [
            [complex_pair(value) for value in row] for row in alignment
        ],
        "final_winding_reference": complex_pair(winding_reference),
        "final_radius": radius,
        "current_jacobian": [
            [complex_pair(value) for value in row] for row in jacobian
        ],
        "current_jacobian_singular_values": [
            float(value) for value in singular_values
        ],
        "strict_scope": {
            "floating_exploration_only": True,
            "target_branch": "ell_92=0",
            "fresh_Jacobian_at_final_carrier": False,
            "Broyden_secant_update_used": True,
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
                "accepted": result["accepted"],
                "input_beta_norm": input_norm,
                "final_beta_norm": result["final_beta_norm"],
                "updated_Jacobian_minimum_singular_value": float(
                    singular_values[-1]
                ),
            },
            indent=2,
        )
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
