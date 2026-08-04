from __future__ import annotations

import argparse
import json
from pathlib import Path

import numpy as np
from scipy.linalg import expm

from explore_q79_pgl3_beta_zero import PGL3BetaEvaluator


ROOT = Path(__file__).resolve().parents[1]
DEFAULT_INPUT = (
    ROOT
    / "candidate_data"
    / "selected_q79genus2delignebetaperiodandintegralbranchexecution"
    / "pgl3_retired_pre_fix_alignment_seed.exploratory.json"
)


def load(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def complex_value(value: dict) -> complex:
    return complex(float(value["r"]), float(value["i"]))


def complex_pair(value: complex) -> dict[str, float]:
    return {"r": float(value.real), "i": float(value.imag)}


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--input", type=Path, default=DEFAULT_INPUT)
    parser.add_argument("--output", type=Path, required=True)
    parser.add_argument("--radius", type=float, default=1.171875e-5)
    parser.add_argument("--rtol", type=float, default=3.0e-6)
    parser.add_argument("--atol", type=float, default=3.0e-8)
    parser.add_argument("--base-rtol", type=float, default=3.0e-8)
    parser.add_argument("--base-atol", type=float, default=3.0e-10)
    arguments = parser.parse_args()

    input_path = arguments.input.resolve()
    source = load(input_path)
    evaluator = PGL3BetaEvaluator()
    alignment = np.asarray(
        [
            [complex_value(value) for value in row]
            for row in source["alignment"]
        ],
        dtype=np.complex128,
    )
    winding_reference = complex_value(source["winding_reference"])
    phases = np.exp(0.25j * np.pi * np.arange(8))
    step = arguments.radius * phases
    tangent = sum(
        (
            step[index] * evaluator.generators[index]
            for index in range(8)
        ),
        np.zeros((3, 3), dtype=np.complex128),
    )
    trial_alignment = alignment @ expm(tangent)

    common = {
        "rtol": arguments.rtol,
        "atol": arguments.atol,
        "base_rtol": arguments.base_rtol,
        "base_atol": arguments.base_atol,
        "winding_reference": winding_reference,
        "high_precision_condition_threshold": 0.0,
    }
    forced_base, base_diagnostics = evaluator.evaluate(alignment, **common)
    forced_trial, trial_diagnostics = evaluator.evaluate(
        trial_alignment, **common
    )
    delta = forced_trial - forced_base
    result = {
        "schema": "MTTQ79PGL3ReductionSwitchDiagnostic.v1",
        "status": "EXPLORATORY_FORCED_HIGH_PRECISION_TWO_POINT_PROBE",
        "source": str(input_path.relative_to(ROOT)).replace("\\", "/"),
        "trust_radius": arguments.radius,
        "perturbation_rule": "radius*exp(i*pi*j/4), j=0,...,7",
        "step_maximum_absolute_value": float(np.max(abs(step))),
        "step": [complex_pair(value) for value in step],
        "forced_base_norm": float(np.linalg.norm(forced_base)),
        "forced_trial_norm": float(np.linalg.norm(forced_trial)),
        "forced_endpoint_difference_norm": float(np.linalg.norm(delta)),
        "forced_endpoint_difference_over_step": float(
            np.linalg.norm(delta) / np.max(abs(step))
        ),
        "forced_base": [complex_pair(value) for value in forced_base],
        "forced_trial": [complex_pair(value) for value in forced_trial],
        "forced_delta": [complex_pair(value) for value in delta],
        "base_diagnostics": base_diagnostics,
        "trial_diagnostics": trial_diagnostics,
        "strict_scope": {
            "floating_exploration_only": True,
            "high_precision_reduction_forced_for_every_connection_rhs": True,
            "retired_beta_or_jacobian_used": False,
            "retired_alignment_coordinates_used_only_as_arbitrary_seed": True,
            "PGL3_zero_claimed": False,
            "interval_certified": False,
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
                "forced_base_norm": result["forced_base_norm"],
                "forced_trial_norm": result["forced_trial_norm"],
                "forced_endpoint_difference_norm": result[
                    "forced_endpoint_difference_norm"
                ],
                "base_high_precision_reductions": base_diagnostics[
                    "high_precision_reduction_count"
                ],
                "trial_high_precision_reductions": trial_diagnostics[
                    "high_precision_reduction_count"
                ],
            },
            indent=2,
        )
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
