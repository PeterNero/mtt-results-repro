from __future__ import annotations

import hashlib
import json
import time
from pathlib import Path

import numpy as np
from flint import ctx
from scipy.linalg import expm

import explore_q79_height4_covariant_floating_probe as probe
from build_q79_height4_covariant_recentered_step import (
    handle_coordinates,
    radial_coordinates,
)


ROOT = probe.ROOT
JACOBIAN = probe.PROBE_DIRECTORY / "height4_covariant_PL_recentered_jacobian.packet.json"
BASE_TRIAL = probe.PROBE_DIRECTORY / "tr3_s1d000ep00" / "trial.packet.json"
OUTPUT = probe.PROBE_DIRECTORY / "rank4_PL_recentered_step_01.packet.json"


def load(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def dump(path: Path, value: dict) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(value, indent=2, sort_keys=True) + "\n", encoding="utf-8")


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def relative(path: Path) -> str:
    return str(path.relative_to(ROOT)).replace("\\", "/")


def main() -> int:
    ctx.dps = 100
    started = time.perf_counter()
    packet = load(JACOBIAN)
    selected = next(
        row
        for row in packet["candidate_Jacobians"]
        if int(row["A132_objective_rank"]) == 4
    )
    unconstrained_step = np.asarray(
        selected["local_least_squares_step_on_available_directions"],
        dtype=np.float64,
    )
    center_residual = probe.complex_vector(selected["center_residual"])
    jacobian = np.asarray(
        [
            [probe.complex_value(value) for value in row]
            for row in selected["covariant_residual_Jacobian_8_by_k"]
        ],
        dtype=np.complex128,
    )
    evaluator = probe.PGL3BetaEvaluator()
    base_trial = load(BASE_TRIAL)
    base_alignment = probe.complex_matrix(base_trial["alignment"])
    active_margin = -2.0e-6
    active_names = (
        "selected_090_B",
        "selected_073_selected_061_radial",
        "selected_039_selected_038_radial",
    )

    def active_coordinates(alignment: np.ndarray) -> tuple[np.ndarray, dict]:
        centers, diagnostics = probe.continued_critical_centers(alignment)
        value = centers["selected_090"].real - 0.25
        radial = radial_coordinates(centers, {"selected_073", "selected_039"})
        coordinates = np.asarray(
            [
                float(value - round(value)),
                radial["selected_073|selected_061|+0|+0"][
                    "signed_transverse_coordinate"
                ],
                radial["selected_039|selected_038|+0|+0"][
                    "signed_transverse_coordinate"
                ],
            ],
            dtype=np.float64,
        )
        return coordinates, diagnostics

    base_active, base_active_diagnostics = active_coordinates(base_alignment)
    gradient_step = 1.0e-6
    gradient_columns = []
    gradient_inventory = []
    for direction, generator in enumerate(evaluator.generators):
        plus, plus_diagnostics = active_coordinates(
            base_alignment @ expm(gradient_step * generator)
        )
        minus, minus_diagnostics = active_coordinates(
            base_alignment @ expm(-gradient_step * generator)
        )
        derivative = (plus - minus) / (2 * gradient_step)
        gradient_columns.append(derivative)
        gradient_inventory.append(
            {
                "direction_one_based": direction + 1,
                "plus_signed_coordinates": [float(value) for value in plus],
                "minus_signed_coordinates": [float(value) for value in minus],
                "central_difference_derivatives": [
                    float(value) for value in derivative
                ],
                "plus_critical_continuation": plus_diagnostics,
                "minus_critical_continuation": minus_diagnostics,
            }
        )
    active_gradients = np.column_stack(gradient_columns)
    real_jacobian = np.vstack([jacobian.real, jacobian.imag])
    real_residual = np.concatenate([center_residual.real, center_residual.imag])
    normal = real_jacobian.T @ real_jacobian
    linear = real_jacobian.T @ real_residual
    kkt = np.block(
        [
            [normal, active_gradients.T],
            [active_gradients, np.zeros((3, 3))],
        ]
    )
    active_targets = np.full(3, active_margin, dtype=np.float64) - base_active
    right_hand_side = np.concatenate(
        [-linear, active_targets]
    )
    solution = np.linalg.solve(kkt, right_hand_side)
    step = solution[:8]
    tangent = sum(
        (step[index] * evaluator.generators[index] for index in range(8)),
        np.zeros((3, 3), dtype=np.complex128),
    )
    a208 = load(probe.A208)
    candidates = a208["height_four_candidates"][1:]
    support_indices = {
        int(row["distinguished_index"])
        for candidate in candidates
        for row in candidate["primitive_thimble_chain"]
    }
    fan = load(probe.FAN)["distinguished_positive_meridians"]
    target_root_ids = {
        row["root_id"]
        for row in fan
        if int(row["distinguished_index"]) in support_indices
    }

    samples = []
    previous_radial = None
    previous_handles = None
    crossings = []
    for sample_index, scale in enumerate(np.linspace(0.0, 1.0, 17)):
        alignment = base_alignment @ expm(float(scale) * tangent)
        centers, diagnostics = probe.continued_critical_centers(alignment)
        radial = radial_coordinates(centers, target_root_ids)
        handles = handle_coordinates(centers)
        new_crossings = []
        if previous_radial is not None:
            for key in sorted(set(previous_radial) & set(radial)):
                old = previous_radial[key]["signed_transverse_coordinate"]
                new = radial[key]["signed_transverse_coordinate"]
                if old * new < 0:
                    new_crossings.append(
                        {
                            "kind": "radial_thimble",
                            "pair": key,
                            "lower_scale": samples[-1]["scale"],
                            "upper_scale": float(scale),
                            "lower_signed_coordinate": old,
                            "upper_signed_coordinate": new,
                        }
                    )
            for name in ("A", "B"):
                for root_id, new in handles[name].items():
                    old = previous_handles[name][root_id]
                    if old * new < 0:
                        new_crossings.append(
                            {
                                "kind": "global_handle",
                                "handle": name,
                                "root_id": root_id,
                                "lower_scale": samples[-1]["scale"],
                                "upper_scale": float(scale),
                                "lower_signed_coordinate": old,
                                "upper_signed_coordinate": new,
                            }
                        )
        nearest = min(radial.values(), key=lambda row: row["clearance"])
        samples.append(
            {
                "sample_index": sample_index,
                "scale": float(scale),
                "nearest_radial_pair": nearest,
                "minimum_A_handle_clearance": min(
                    abs(value) for value in handles["A"].values()
                ),
                "minimum_B_handle_clearance": min(
                    abs(value) for value in handles["B"].values()
                ),
                "crossings_from_previous_sample": new_crossings,
                "critical_continuation": diagnostics,
            }
        )
        crossings.extend(new_crossings)
        previous_radial = radial
        previous_handles = handles
        print(
            f"[{sample_index + 1}/17] scale={scale:.4f} "
            f"nearest={nearest['target_root_id']}/{nearest['other_root_id']}:"
            f"{nearest['signed_transverse_coordinate']:+.3e} "
            f"crossings={len(new_crossings)}",
            flush=True,
        )

    crossing_lower_scales = [float(row["lower_scale"]) for row in crossings]
    selected_scale = min(crossing_lower_scales) if crossing_lower_scales else 1.0
    selected_step = selected_scale * step
    selected_prediction = center_residual + jacobian @ selected_step
    target_alignment = base_alignment @ expm(
        sum(
            (
                selected_step[index] * evaluator.generators[index]
                for index in range(8)
            ),
            np.zeros((3, 3), dtype=np.complex128),
        )
    )
    output = {
        "schema": "MTTQ79HeightFourPLRecenteredRank4Step.v1",
        "status": "RANK4_PL_RECENTERED_STEP_PROFILED",
        "candidate_rank": 4,
        "base_alignment": probe.encoded_complex_matrix(base_alignment),
        "center_residual": probe.encoded_complex_vector(center_residual),
        "center_residual_l2_norm": float(np.linalg.norm(center_residual)),
        "unconstrained_step": [float(value) for value in unconstrained_step],
        "unconstrained_linearized_residual_l2_norm": selected[
            "linearized_residual_l2_norm"
        ],
        "active_topological_walls": {
            "coordinate_names": list(active_names),
            "base_signed_coordinates": [float(value) for value in base_active],
            "required_negative_margin": active_margin,
            "finite_difference_step": gradient_step,
            "gradient_3_by_8": active_gradients.tolist(),
            "gradient_inventory": gradient_inventory,
            "base_critical_continuation": base_active_diagnostics,
        },
        "three_wall_constrained_step": [float(value) for value in step],
        "three_wall_constrained_linearized_coordinates": [
            float(value) for value in base_active + active_gradients @ step
        ],
        "three_wall_KKT_constraint_maximum_residual": float(
            np.max(abs(active_gradients @ step - active_targets))
        ),
        "three_wall_KKT_multipliers": [float(value) for value in solution[8:]],
        "three_wall_constrained_predicted_residual_l2_norm": float(
            np.linalg.norm(center_residual + jacobian @ step)
        ),
        "chamber_profile": {"samples": samples, "crossings": crossings},
        "selected_scale": selected_scale,
        "selected_step": [float(value) for value in selected_step],
        "selected_step_maximum_absolute_coordinate": float(
            np.max(abs(selected_step))
        ),
        "selected_predicted_residual": probe.encoded_complex_vector(
            selected_prediction
        ),
        "selected_predicted_residual_l2_norm": float(
            np.linalg.norm(selected_prediction)
        ),
        "target_alignment": probe.encoded_complex_matrix(target_alignment),
        "summary": {
            "candidate_rank": 4,
            "center_residual_l2_norm": float(np.linalg.norm(center_residual)),
            "selected_scale": selected_scale,
            "selected_predicted_residual_l2_norm": float(
                np.linalg.norm(selected_prediction)
            ),
            "three_wall_constrained_full_predicted_residual_l2_norm": float(
                np.linalg.norm(center_residual + jacobian @ step)
            ),
            "crossing_count": len(crossings),
            "first_crossing_lower_scale": (
                min(crossing_lower_scales) if crossing_lower_scales else None
            ),
            "elapsed_seconds": time.perf_counter() - started,
        },
        "authority": {
            "Jacobian": relative(JACOBIAN),
            "Jacobian_sha256": sha256(JACOBIAN),
            "base_trial": relative(BASE_TRIAL),
            "base_trial_sha256": sha256(BASE_TRIAL),
            "radial_helper_source": relative(
                ROOT / "scripts" / "build_q79_height4_covariant_recentered_step.py"
            ),
            "radial_helper_source_sha256": sha256(
                ROOT / "scripts" / "build_q79_height4_covariant_recentered_step.py"
            ),
            "source": relative(Path(__file__)),
            "source_sha256": sha256(Path(__file__)),
        },
        "strict_scope": {
            "all_eight_PL_recentered_Jacobian_columns_used": True,
            "three_active_wall_gradients_computed_in_all_eight_directions": True,
            "linearized_negative_three_wall_margins_imposed": True,
            "sampled_radial_and_global_handle_profile": True,
            "complete_no_crossing_certificate": False,
            "step_executed": False,
            "floating_only": True,
            "covariant_zero_proved": False,
        },
    }
    dump(OUTPUT, output)
    print(f"wrote {relative(OUTPUT)}")
    print(json.dumps(output["summary"], indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
