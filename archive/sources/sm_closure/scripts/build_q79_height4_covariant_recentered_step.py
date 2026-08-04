from __future__ import annotations

import hashlib
import json
import time
from pathlib import Path

import numpy as np
from flint import ctx
from scipy.linalg import expm

import explore_q79_height4_covariant_floating_probe as probe


ROOT = probe.ROOT
JACOBIAN = (
    probe.PROBE_DIRECTORY / "height4_covariant_floating_jacobian.packet.json"
)
BASE_TRIAL = (
    probe.PROBE_DIRECTORY / "tr3_s5d000em01" / "trial.packet.json"
)
OUTPUT = probe.PROBE_DIRECTORY / "rank3_recentered_step_02.packet.json"


def load(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def dump(path: Path, value: dict) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(value, indent=2, sort_keys=True) + "\n", encoding="utf-8")


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def relative(path: Path) -> str:
    return str(path.relative_to(ROOT)).replace("\\", "/")


def encoded_vector(vector: np.ndarray) -> list[dict[str, str]]:
    return [probe.complex_pair(value) for value in vector]


def interior_segment_coordinates(
    start: complex, end: complex, point: complex
) -> list[dict]:
    vector = end - start
    squared_length = vector.real**2 + vector.imag**2
    if squared_length == 0:
        return []
    rows = []
    for real_shift in range(-2, 3):
        for imaginary_shift in range(-2, 3):
            lifted = point + real_shift + 1j * imaginary_shift
            offset = lifted - start
            parameter = (
                offset.real * vector.real + offset.imag * vector.imag
            ) / squared_length
            if not 0 < parameter < 1:
                continue
            signed = (
                vector.real * offset.imag - vector.imag * offset.real
            ) / abs(vector)
            row = {
                "longitudinal_parameter": float(parameter),
                "signed_transverse_coordinate": float(signed),
                "clearance": float(abs(signed)),
                "deck_shift": [real_shift, imaginary_shift],
            }
            rows.append(row)
    return rows


def interior_segment_coordinate(
    start: complex, end: complex, point: complex
) -> dict | None:
    rows = interior_segment_coordinates(start, end, point)
    return min(rows, key=lambda row: row["clearance"]) if rows else None


def radial_coordinates(
    centers: dict[str, complex], target_root_ids: set[str]
) -> dict[str, dict]:
    base = 0.25 + 0.25j
    rows = {}
    for target_root_id in sorted(target_root_ids):
        target = centers[target_root_id]
        for other_root_id, other in centers.items():
            if other_root_id == target_root_id:
                continue
            for coordinates in interior_segment_coordinates(base, target, other):
                shift = coordinates["deck_shift"]
                key = (
                    f"{target_root_id}|{other_root_id}|"
                    f"{shift[0]:+d}|{shift[1]:+d}"
                )
                rows[key] = {
                    "target_root_id": target_root_id,
                    "other_root_id": other_root_id,
                    **coordinates,
                }
    return rows


def handle_coordinates(centers: dict[str, complex]) -> dict[str, dict[str, float]]:
    return {
        "A": {
            root_id: float((value.imag - 0.25) - round(value.imag - 0.25))
            for root_id, value in centers.items()
        },
        "B": {
            root_id: float((value.real - 0.25) - round(value.real - 0.25))
            for root_id, value in centers.items()
        },
    }


def main() -> int:
    ctx.dps = 100
    started = time.perf_counter()
    jacobian_packet = load(JACOBIAN)
    base_trial = load(BASE_TRIAL)
    selected_jacobian = next(
        row
        for row in jacobian_packet["candidate_Jacobians"]
        if int(row["A132_objective_rank"]) == 3
    )
    selected_trial = next(
        row
        for row in base_trial["candidate_trials"]
        if int(row["A132_objective_rank"]) == 3
    )
    jacobian = np.asarray(
        [
            [probe.complex_value(value) for value in row]
            for row in selected_jacobian["covariant_residual_Jacobian_8_by_k"]
        ],
        dtype=np.complex128,
    )
    center_residual = probe.complex_vector(selected_jacobian["center_residual"])
    current_residual = probe.complex_vector(selected_trial["actual_residual"])
    first_step = np.asarray(base_trial["executed_step"], dtype=np.float64)
    secant_error = current_residual - (center_residual + jacobian @ first_step)
    broyden_jacobian = jacobian + np.outer(secant_error, first_step) / float(
        first_step @ first_step
    )

    proposals = []
    for name, matrix in (
        ("frozen_center_Jacobian", jacobian),
        ("rank_one_secant_Broyden", broyden_jacobian),
    ):
        real_matrix = np.vstack([matrix.real, matrix.imag])
        real_residual = np.concatenate([current_residual.real, current_residual.imag])
        step, *_ = np.linalg.lstsq(real_matrix, -real_residual, rcond=None)
        prediction = current_residual + matrix @ step
        proposals.append(
            {
                "name": name,
                "step": [float(value) for value in step],
                "step_maximum_absolute_coordinate": float(np.max(abs(step))),
                "predicted_residual": encoded_vector(prediction),
                "predicted_residual_l2_norm": float(np.linalg.norm(prediction)),
                "predicted_residual_maximum_absolute_value": float(
                    np.max(abs(prediction))
                ),
            }
        )
    evaluator = probe.PGL3BetaEvaluator()
    current_alignment = probe.complex_matrix(base_trial["alignment"])
    wall_target = "selected_039"
    wall_other = "selected_038"
    wall_margin = 2.0e-6

    def active_wall_coordinates(
        alignment: np.ndarray,
    ) -> tuple[float, float, dict]:
        centers, diagnostics = probe.continued_critical_centers(alignment)
        row = interior_segment_coordinate(
            0.25 + 0.25j,
            centers[wall_target],
            centers[wall_other],
        )
        if row is None:
            raise AssertionError("active radial wall left the interior segment")
        selected_090 = centers["selected_090"]
        B_coordinate = float(
            (selected_090.real - 0.25) - round(selected_090.real - 0.25)
        )
        return row["signed_transverse_coordinate"], B_coordinate, diagnostics

    wall_center, B_wall_center, wall_center_diagnostics = active_wall_coordinates(
        current_alignment
    )
    wall_step = 1.0e-6
    wall_gradient = []
    B_wall_gradient = []
    wall_gradient_inventory = []
    for direction, generator in enumerate(evaluator.generators):
        plus_value, plus_B_value, plus_diagnostics = active_wall_coordinates(
            current_alignment @ expm(wall_step * generator)
        )
        minus_value, minus_B_value, minus_diagnostics = active_wall_coordinates(
            current_alignment @ expm(-wall_step * generator)
        )
        derivative = (plus_value - minus_value) / (2 * wall_step)
        B_derivative = (plus_B_value - minus_B_value) / (2 * wall_step)
        wall_gradient.append(derivative)
        B_wall_gradient.append(B_derivative)
        wall_gradient_inventory.append(
            {
                "direction_one_based": direction + 1,
                "plus_signed_coordinate": plus_value,
                "minus_signed_coordinate": minus_value,
                "central_difference_derivative": derivative,
                "plus_B_signed_coordinate": plus_B_value,
                "minus_B_signed_coordinate": minus_B_value,
                "B_central_difference_derivative": B_derivative,
                "plus_critical_continuation": plus_diagnostics,
                "minus_critical_continuation": minus_diagnostics,
            }
        )
    wall_gradient = np.asarray(wall_gradient, dtype=np.float64)
    B_wall_gradient = np.asarray(B_wall_gradient, dtype=np.float64)
    real_broyden = np.vstack([broyden_jacobian.real, broyden_jacobian.imag])
    real_residual = np.concatenate([current_residual.real, current_residual.imag])
    normal = real_broyden.T @ real_broyden
    linear = real_broyden.T @ real_residual
    constraints = np.vstack([wall_gradient, B_wall_gradient])
    constraint_targets = np.asarray(
        [wall_margin - wall_center, -wall_margin - B_wall_center],
        dtype=np.float64,
    )
    kkt = np.block(
        [
            [normal, constraints.T],
            [constraints, np.zeros((2, 2))],
        ]
    )
    right_hand_side = np.concatenate([-linear, constraint_targets])
    constrained_solution = np.linalg.solve(kkt, right_hand_side)
    constrained_step = constrained_solution[:8]
    constrained_prediction = current_residual + broyden_jacobian @ constrained_step
    proposals.append(
        {
            "name": "radial_and_B_wall_tangent_constrained_Broyden",
            "step": [float(value) for value in constrained_step],
            "step_maximum_absolute_coordinate": float(
                np.max(abs(constrained_step))
            ),
            "predicted_residual": encoded_vector(constrained_prediction),
            "predicted_residual_l2_norm": float(
                np.linalg.norm(constrained_prediction)
            ),
            "predicted_residual_maximum_absolute_value": float(
                np.max(abs(constrained_prediction))
            ),
            "linearized_wall_coordinate": float(
                wall_center + wall_gradient @ constrained_step
            ),
            "linearized_B_handle_wall_coordinate": float(
                B_wall_center + B_wall_gradient @ constrained_step
            ),
            "KKT_constraint_maximum_residual": float(
                np.max(abs(constraints @ constrained_step - constraint_targets))
            ),
            "KKT_multipliers": [float(value) for value in constrained_solution[8:]],
        }
    )
    selected_proposal = proposals[-1]
    proposed_step = constrained_step
    tangent = sum(
        (
            proposed_step[index] * evaluator.generators[index]
            for index in range(8)
        ),
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
    all_crossings = []
    for sample_index, scale in enumerate(np.linspace(0.0, 1.0, 17)):
        alignment = current_alignment @ expm(float(scale) * tangent)
        centers, diagnostics = probe.continued_critical_centers(alignment)
        radial = radial_coordinates(centers, target_root_ids)
        handles = handle_coordinates(centers)
        crossings = []
        if previous_radial is not None:
            for key in sorted(set(previous_radial) & set(radial)):
                old = previous_radial[key]["signed_transverse_coordinate"]
                new = radial[key]["signed_transverse_coordinate"]
                if old * new < 0:
                    crossings.append(
                        {
                            "kind": "radial_thimble",
                            "pair": key,
                            "lower_scale": float(samples[-1]["scale"]),
                            "upper_scale": float(scale),
                            "lower_signed_coordinate": old,
                            "upper_signed_coordinate": new,
                        }
                    )
            for name in ("A", "B"):
                for root_id, new in handles[name].items():
                    old = previous_handles[name][root_id]
                    if old * new < 0:
                        crossings.append(
                            {
                                "kind": "global_handle",
                                "handle": name,
                                "root_id": root_id,
                                "lower_scale": float(samples[-1]["scale"]),
                                "upper_scale": float(scale),
                                "lower_signed_coordinate": old,
                                "upper_signed_coordinate": new,
                            }
                        )
        nearest_radial = min(radial.values(), key=lambda row: row["clearance"])
        samples.append(
            {
                "sample_index": sample_index,
                "scale": float(scale),
                "nearest_radial_pair": nearest_radial,
                "minimum_A_handle_clearance": min(abs(value) for value in handles["A"].values()),
                "minimum_B_handle_clearance": min(abs(value) for value in handles["B"].values()),
                "crossings_from_previous_sample": crossings,
                "critical_continuation": diagnostics,
            }
        )
        all_crossings.extend(crossings)
        previous_radial = radial
        previous_handles = handles
        print(
            f"[{sample_index + 1}/17] scale={scale:.4f} "
            f"radial={nearest_radial['target_root_id']}/"
            f"{nearest_radial['other_root_id']}:"
            f"{nearest_radial['signed_transverse_coordinate']:+.3e} "
            f"crossings={len(crossings)}",
            flush=True,
        )

    crossing_lower_scales = [row["lower_scale"] for row in all_crossings]
    selected_scale = min(crossing_lower_scales) if crossing_lower_scales else 1.0
    selected_step = selected_scale * proposed_step
    selected_prediction = current_residual + broyden_jacobian @ selected_step
    packet = {
        "schema": "MTTQ79HeightFourCovariantRecenteredStepProposal.v1",
        "status": "RECENTERED_BROYDEN_STEP_WITH_SAMPLED_CHAMBER_PREFLIGHT",
        "candidate_rank": 3,
        "base_trial": relative(BASE_TRIAL),
        "base_alignment": probe.encoded_complex_matrix(current_alignment),
        "base_actual_residual": encoded_vector(current_residual),
        "base_actual_residual_l2_norm": float(np.linalg.norm(current_residual)),
        "first_step_secant_error": encoded_vector(secant_error),
        "first_step_secant_error_l2_norm": float(np.linalg.norm(secant_error)),
        "proposals": proposals,
        "active_radial_wall": {
            "target_root_id": wall_target,
            "other_root_id": wall_other,
            "base_signed_transverse_coordinate": wall_center,
            "selected_090_base_B_signed_coordinate": B_wall_center,
            "required_positive_margin": wall_margin,
            "required_negative_B_margin": -wall_margin,
            "finite_difference_step": wall_step,
            "gradient": [float(value) for value in wall_gradient],
            "selected_090_B_gradient": [
                float(value) for value in B_wall_gradient
            ],
            "gradient_inventory": wall_gradient_inventory,
            "base_critical_continuation": wall_center_diagnostics,
        },
        "selected_proposal": "radial_and_B_wall_tangent_constrained_Broyden",
        "sampled_chamber_preflight": {
            "samples": samples,
            "crossings": all_crossings,
        },
        "selected_scale": selected_scale,
        "selected_step": [float(value) for value in selected_step],
        "selected_step_maximum_absolute_coordinate": float(np.max(abs(selected_step))),
        "selected_predicted_residual": encoded_vector(selected_prediction),
        "selected_predicted_residual_l2_norm": float(np.linalg.norm(selected_prediction)),
        "target_alignment": probe.encoded_complex_matrix(
            current_alignment
            @ expm(
                sum(
                    (
                        selected_step[index] * evaluator.generators[index]
                        for index in range(8)
                    ),
                    np.zeros((3, 3), dtype=np.complex128),
                )
            )
        ),
        "summary": {
            "candidate_rank": 3,
            "base_residual_l2_norm": float(np.linalg.norm(current_residual)),
            "selected_scale": selected_scale,
            "selected_step_maximum_absolute_coordinate": float(np.max(abs(selected_step))),
            "selected_predicted_residual_l2_norm": float(np.linalg.norm(selected_prediction)),
            "sampled_crossing_count": len(all_crossings),
            "first_sampled_crossing_lower_scale": (
                min(crossing_lower_scales) if crossing_lower_scales else None
            ),
            "elapsed_seconds": time.perf_counter() - started,
        },
        "authority": {
            "Jacobian": relative(JACOBIAN),
            "Jacobian_sha256": sha256(JACOBIAN),
            "base_trial": relative(BASE_TRIAL),
            "base_trial_sha256": sha256(BASE_TRIAL),
            "source": relative(Path(__file__)),
            "source_sha256": sha256(Path(__file__)),
        },
        "strict_scope": {
            "same_source_base_residual": True,
            "rank_one_secant_update_only": True,
            "active_radial_wall_gradient_computed_in_all_eight_directions": True,
            "active_B_handle_wall_gradient_computed_in_all_eight_directions": True,
            "linearized_positive_wall_margin_imposed": True,
            "sampled_radial_and_handle_chamber_preflight": True,
            "complete_no_crossing_certificate": False,
            "new_step_executed": False,
            "floating_only": True,
            "covariant_zero_proved": False,
            "observed_SM_values_used": False,
        },
    }
    dump(OUTPUT, packet)
    print(f"wrote {relative(OUTPUT)}")
    print(json.dumps(packet["summary"], indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
