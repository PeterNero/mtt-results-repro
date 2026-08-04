from __future__ import annotations

import argparse
import json
from pathlib import Path

import numpy as np
from scipy.linalg import expm

from explore_q79_pgl3_beta_zero import PGL3BetaEvaluator
from q79_pgl3_beta_diagnostics import SmoothnessProbe


ROOT = Path(__file__).resolve().parents[1]
IDENTITY = (
    ROOT
    / "candidate_data"
    / "selected_q79genus2delignebetaperiodandintegralbranchexecution"
    / "pgl3_identity_generalized_evaluator.diagnostic.json"
)


def load(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def complex_value(value: dict) -> complex:
    if "r" in value:
        return complex(float(value["r"]), float(value["i"]))
    return complex(float(value["real"]), float(value["imaginary"]))


def complex_pair(value: complex) -> dict[str, float]:
    return {"r": float(value.real), "i": float(value.imag)}


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--output", type=Path, required=True)
    parser.add_argument("--seed", type=int, default=790121)
    parser.add_argument("--samples-per-scale", type=int, default=4)
    parser.add_argument("--scales", type=float, nargs="+", default=[0.06, 0.12, 0.20])
    parser.add_argument("--minimum-path-clearance", type=float, default=0.02)
    parser.add_argument("--path-samples", type=int, default=9)
    parser.add_argument("--rtol", type=float, default=1.0e-5)
    parser.add_argument("--atol", type=float, default=1.0e-7)
    parser.add_argument("--base-rtol", type=float, default=1.0e-7)
    parser.add_argument("--base-atol", type=float, default=1.0e-9)
    arguments = parser.parse_args()

    identity_packet = load(IDENTITY)
    identity_alignment = np.asarray(
        [
            [complex_value(value) for value in row]
            for row in identity_packet["alignment"]
        ],
        dtype=np.complex128,
    )
    identity_branch = complex_value(
        identity_packet["diagnostics"]["base_lift_diagnostics"][
            "wound_branch_point"
        ]
    )
    evaluator = PGL3BetaEvaluator()
    probe = SmoothnessProbe(evaluator)
    rng = np.random.default_rng(arguments.seed)
    rows: list[dict] = []

    for scale in arguments.scales:
        for sample in range(1, arguments.samples_per_scale + 1):
            coordinates = rng.normal(size=8) + 1j * rng.normal(size=8)
            coordinates *= scale / np.max(abs(coordinates))
            tangent = sum(
                (
                    coordinates[index] * evaluator.generators[index]
                    for index in range(8)
                ),
                np.zeros((3, 3), dtype=np.complex128),
            )
            alignment = identity_alignment @ expm(tangent)
            path_smoothness = []
            for fraction in np.linspace(0.0, 1.0, arguments.path_samples):
                intermediate = identity_alignment @ expm(fraction * tangent)
                path_smoothness.append(probe.execute(intermediate, samples=101))
            minimum_path_separation = min(
                value["minimum_branch_point_separation"]
                for value in path_smoothness
            )
            minimum_path_q_separation = min(
                value["minimum_q_root_separation"]
                for value in path_smoothness
            )
            row = {
                "scale": scale,
                "sample": sample,
                "coordinates": [complex_pair(value) for value in coordinates],
                "alignment": [
                    [complex_pair(value) for value in values]
                    for values in alignment
                ],
                "minimum_identity_path_branch_separation": float(
                    minimum_path_separation
                ),
                "minimum_identity_path_q_separation": float(
                    minimum_path_q_separation
                ),
                "path_samples": arguments.path_samples,
                "base_samples_per_path_carrier": 101,
            }
            if minimum_path_separation < arguments.minimum_path_clearance:
                row.update(
                    {
                        "evaluated": False,
                        "rejection": "identity-to-carrier path clearance guard",
                    }
                )
                rows.append(row)
                print(
                    f"scale={scale:.3g} sample={sample}: clearance rejected",
                    flush=True,
                )
                continue
            try:
                beta, diagnostics = evaluator.evaluate(
                    alignment,
                    rtol=arguments.rtol,
                    atol=arguments.atol,
                    base_rtol=arguments.base_rtol,
                    base_atol=arguments.base_atol,
                    winding_reference=identity_branch,
                )
                row.update(
                    {
                        "evaluated": True,
                        "beta_norm": float(np.linalg.norm(beta)),
                        "beta": [complex_pair(value) for value in beta],
                        "diagnostics": diagnostics,
                    }
                )
                print(
                    f"scale={scale:.3g} sample={sample}: "
                    f"norm={np.linalg.norm(beta):.9g}, "
                    f"clearance={minimum_path_separation:.6g}",
                    flush=True,
                )
            except (AssertionError, ValueError) as error:
                row.update(
                    {
                        "evaluated": False,
                        "rejection": str(error),
                    }
                )
                print(
                    f"scale={scale:.3g} sample={sample}: evaluation rejected",
                    flush=True,
                )
            rows.append(row)

    evaluated = [row for row in rows if row["evaluated"]]
    best = min(evaluated, key=lambda row: row["beta_norm"]) if evaluated else None
    packet = {
        "schema": "MTTQ79PGL3CorrectedRandomCarrierScan.v1",
        "status": "EXPLORATORY_PATH_GUARDED_RANDOM_CARRIER_SCAN",
        "seed": arguments.seed,
        "scales": arguments.scales,
        "samples_per_scale": arguments.samples_per_scale,
        "minimum_path_clearance": arguments.minimum_path_clearance,
        "rows": rows,
        "evaluated_carriers": len(evaluated),
        "best_carrier": best,
        "strict_scope": {
            "floating_exploration_only": True,
            "finite_random_scan_is_not_a_global_zero_or_no_go_proof": True,
            "identity_path_branch_clearance_screened": True,
            "observed_SM_values_used": False,
            "PGL3_zero_claimed": False,
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
                "evaluated_carriers": len(evaluated),
                "best_norm": None if best is None else best["beta_norm"],
                "best_scale": None if best is None else best["scale"],
                "best_sample": None if best is None else best["sample"],
                "best_path_clearance": (
                    None
                    if best is None
                    else best["minimum_identity_path_branch_separation"]
                ),
            },
            indent=2,
        )
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
