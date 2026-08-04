from __future__ import annotations

import argparse
import hashlib
import json
import math
import time
from concurrent.futures import ProcessPoolExecutor, as_completed
from pathlib import Path

import numpy as np
from flint import ctx
from scipy.linalg import expm

import explore_q79_height4_covariant_floating_probe as probe
import q79_height4_deformed_beta_transport as deformed_beta_transport


ROOT = probe.ROOT
BASE_TRIAL = probe.PROBE_DIRECTORY / "tr3_s1d000ep00" / "trial.packet.json"
A212 = probe.PROBE_DIRECTORY / "height4_picard_lefschetz_corrected_newton.packet.json"
COMPLEX_COMPLETION = probe.PROBE_DIRECTORY / "rank3_complex_PGL3_completion.packet.json"
COMPLEX_REFINEMENT = probe.PROBE_DIRECTORY / "rank3_complex_PGL3_refinement_02.packet.json"
COMPLEX_TRIAL_01 = probe.PROBE_DIRECTORY / "cplx" / "n1" / "probe.packet.json"
COMPLEX_REFINEMENT_03 = probe.PROBE_DIRECTORY / "rank3_complex_PGL3_refinement_03.packet.json"
COMPLEX_TRIAL_02 = probe.PROBE_DIRECTORY / "cplx" / "n2ud" / "probe.packet.json"
STEP = 1.0e-6


def load(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def dump(path: Path, value: dict) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(value, indent=2, sort_keys=True) + "\n", encoding="utf-8")


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def relative(path: Path) -> str:
    return str(path.relative_to(ROOT)).replace("\\", "/")


def selected_radial_wall_coordinate(centers: dict[str, complex]) -> dict:
    start = 0.25 + 0.25j
    end = centers["selected_039"]
    vector = end - start
    squared_length = vector.real**2 + vector.imag**2
    rows = []
    for real_shift in range(-2, 3):
        for imaginary_shift in range(-2, 3):
            point = centers["selected_038"] + real_shift + 1j * imaginary_shift
            offset = point - start
            parameter = (
                offset.real * vector.real + offset.imag * vector.imag
            ) / squared_length
            if not 0 < parameter < 1:
                continue
            signed = (
                vector.real * offset.imag - vector.imag * offset.real
            ) / abs(vector)
            rows.append(
                {
                    "longitudinal_parameter": float(parameter),
                    "signed_transverse_coordinate": float(signed),
                    "clearance": float(abs(signed)),
                    "deck_shift": [real_shift, imaginary_shift],
                }
            )
    if not rows:
        raise AssertionError("selected radial wall left the interior segment")
    return min(rows, key=lambda row: row["clearance"])


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser()
    parser.add_argument("--direction", type=int, choices=range(8))
    parser.add_argument("--sign", type=int, choices=(-1, 1))
    parser.add_argument(
        "--tangent-axis",
        choices=("real", "imaginary"),
        default="real",
        help="Use G or iG in the selected complex PGL(3) tangent direction.",
    )
    parser.add_argument("--step", type=float, default=STEP)
    parser.add_argument(
        "--complex-completion",
        action="store_true",
        help="Execute the wall-profiled full complex Newton step from A215.",
    )
    parser.add_argument(
        "--complex-refinement",
        action="store_true",
        help="Execute the wall-profiled recentered correction from A217.",
    )
    parser.add_argument(
        "--complex-refinement-03",
        action="store_true",
        help="Execute the ultra-profiled third correction from A218.",
    )
    parser.add_argument("--workers", type=int, default=4)
    parser.add_argument(
        "--numerical-profile",
        choices=(
            "production",
            "high_accuracy",
            "ultra_accuracy",
            "extreme_accuracy",
        ),
        default="production",
    )
    parser.add_argument(
        "--beta-path",
        choices=("straight", "selected090_same_chamber_detour"),
        default="straight",
    )
    parser.add_argument("--force", action="store_true")
    parser.add_argument(
        "--force-beta",
        action="store_true",
        help="Recompute beta and the final packet while retaining valid thimble caches.",
    )
    return parser.parse_args()


def main() -> int:
    arguments = parse_args()
    ctx.dps = 100
    started = time.perf_counter()
    if arguments.step <= 0:
        raise ValueError("step must be positive")
    complex_modes = sum(
        int(value)
        for value in (
            arguments.complex_completion,
            arguments.complex_refinement,
            arguments.complex_refinement_03,
        )
    )
    if complex_modes > 1:
        raise ValueError("choose only one complex step")
    if complex_modes == 0 and (
        arguments.direction is None or arguments.sign is None
    ):
        raise ValueError("--direction and --sign are required for a signed probe")
    base_trial = load(BASE_TRIAL)
    a212 = load(A212)
    if a212["continuation_rule"]["selected_integer_coefficient"] != 1:
        raise AssertionError("A212 PL jump coefficient changed")
    completion = None
    refinement = None
    refinement_03 = None
    if arguments.complex_completion:
        completion = load(COMPLEX_COMPLETION)
        if (
            completion["complex_Jacobian_rank"] != 8
            or completion["realified_Jacobian_rank"] != 16
            or completion["summary"]["crossing_count"] != 0
        ):
            raise AssertionError("A215 complex completion gate is not accepted")
        delta = probe.complex_vector(completion["complex_Newton_step"])
        tag = "n1"
        probe_family = "cplx"
    elif arguments.complex_refinement:
        refinement = load(COMPLEX_REFINEMENT)
        if not all(refinement["acceptance_gate"].values()):
            raise AssertionError("A217 complex refinement gate is not accepted")
        if refinement["summary"]["step_02_crossing_count"] != 0:
            raise AssertionError("A217 refinement segment is not wall-free")
        delta = probe.complex_vector(
            refinement["step_02"]["complex_correction"]
        )
        tag = "n2"
        probe_family = "cplx"
    elif arguments.complex_refinement_03:
        refinement_03 = load(COMPLEX_REFINEMENT_03)
        if not all(refinement_03["acceptance_gate"].values()):
            raise AssertionError("A218 complex refinement gate is not accepted")
        if refinement_03["summary"]["step_03_crossing_count"] != 0:
            raise AssertionError("A218 refinement segment is not wall-free")
        delta = probe.complex_vector(
            refinement_03["step_03"]["complex_correction"]
        )
        tag = "n3"
        probe_family = "cplx"
    else:
        delta = np.zeros(8, dtype=np.complex128)
        tangent_factor = 1.0 if arguments.tangent_axis == "real" else 1.0j
        delta[arguments.direction] = (
            tangent_factor * arguments.sign * arguments.step
        )
        step_tag = format(arguments.step, ".1e").replace("+", "p").replace("-", "m").replace(".", "d")
        sign_tag = "p" if arguments.sign > 0 else "m"
        axis_tag = "d" if arguments.tangent_axis == "real" else "id"
        tag = f"{axis_tag}{arguments.direction + 1:02d}_{sign_tag}_h{step_tag}"
        probe_family = (
            "PL_recentered_full_step"
            if arguments.tangent_axis == "real"
            else "PL_recentered_imaginary_step"
        )
    if completion is not None:
        perturbation = {
            "model": "full_complex_PGL3_Newton_step",
            "complex_coefficients": probe.encoded_complex_vector(delta),
            "source": relative(COMPLEX_COMPLETION),
        }
    elif refinement is not None:
        perturbation = {
            "model": "recentered_complex_PGL3_Newton_step",
            "complex_coefficients": probe.encoded_complex_vector(delta),
            "source": relative(COMPLEX_REFINEMENT),
        }
    elif refinement_03 is not None:
        perturbation = {
            "model": "ultra_recentered_complex_PGL3_Newton_step",
            "complex_coefficients": probe.encoded_complex_vector(delta),
            "source": relative(COMPLEX_REFINEMENT_03),
        }
    else:
        complex_step = delta[arguments.direction]
        perturbation = {
            "model": "signed_generator_probe",
            "direction_zero_based": arguments.direction,
            "direction_one_based": arguments.direction + 1,
            "sign": arguments.sign,
            "step": arguments.step,
            "tangent_axis": arguments.tangent_axis,
            "complex_step": [float(complex_step.real), float(complex_step.imag)],
        }
    if arguments.numerical_profile == "high_accuracy":
        tag += "h"
    elif arguments.numerical_profile == "ultra_accuracy":
        tag += "u"
    elif arguments.numerical_profile == "extreme_accuracy":
        tag += "x"
    if arguments.beta_path != "straight":
        tag += "d"
    output_directory = probe.PROBE_DIRECTORY / probe_family / tag
    output = output_directory / "probe.packet.json"
    if output.exists() and not arguments.force and not arguments.force_beta:
        print(f"cached {relative(output)}")
        print(json.dumps(load(output)["summary"], indent=2))
        return 0

    a208 = load(probe.A208)
    candidates = a208["height_four_candidates"][1:]
    support = sorted(
        {
            int(row["distinguished_index"])
            for candidate in candidates
            for row in candidate["primitive_thimble_chain"]
        }
    )
    orientation = load(probe.ORIENTATION)
    support = sorted(
        set(support)
        | {int(value) for value in orientation["unimodular_pivot_indices_one_based"]}
    )
    evaluator = probe.PGL3BetaEvaluator()
    if refinement_03 is not None:
        prior_complex_trial = load(COMPLEX_TRIAL_02)
    elif refinement is not None:
        prior_complex_trial = load(COMPLEX_TRIAL_01)
    else:
        prior_complex_trial = None
    base_alignment = probe.complex_matrix(
        prior_complex_trial["alignment"]
        if prior_complex_trial is not None
        else base_trial["alignment"]
    )
    tangent = sum(
        (delta[index] * evaluator.generators[index] for index in range(8)),
        np.zeros((3, 3), dtype=np.complex128),
    )
    alignment = base_alignment @ expm(tangent)
    if refinement is not None:
        profiled_target = probe.complex_matrix(
            refinement["step_02"]["target_alignment"]
        )
        if np.max(abs(alignment - profiled_target)) > 1.0e-14:
            raise AssertionError("A217 profiled target does not replay")
    elif refinement_03 is not None:
        profiled_target = probe.complex_matrix(
            refinement_03["step_03"]["target_alignment"]
        )
        if np.max(abs(alignment - profiled_target)) > 1.0e-14:
            raise AssertionError("A218 profiled target does not replay")
    output_directory.mkdir(parents=True, exist_ok=True)
    y_path = output_directory / "fy.packet.json"
    z_path = output_directory / "fz.packet.json"
    dump(y_path, probe.build_point_fibration(alignment, "y"))
    dump(z_path, probe.build_point_fibration(alignment, "z"))
    centers, critical_diagnostics = probe.continued_critical_centers(alignment)
    radial_wall = selected_radial_wall_coordinate(centers)
    if radial_wall["signed_transverse_coordinate"] >= 0:
        raise AssertionError("PL-recentered probe returned to the pre-wall chamber")
    beta_path_offset = None
    beta_path_offset_derivative = None
    beta_path_diagnostics = {
        "model": "straight_B_segment",
        "homotopy_strip_root_ids": [],
    }
    if arguments.beta_path == "selected090_same_chamber_detour":
        path_base = 0.25 + 0.25j
        selected_090 = centers["selected_090"]
        selected_dx = float(
            (selected_090.real - path_base.real)
            - round(selected_090.real - path_base.real)
        )
        selected_height = float((selected_090.imag - path_base.imag) % 1.0)
        if selected_dx >= 0:
            raise AssertionError(
                "selected_090 is not on the left side of the detour path"
            )
        amplitude = 0.1
        sigma = 0.04
        normalization = math.sin(math.pi * selected_height) ** 2

        def bump(parameter: float) -> float:
            sine = math.sin(math.pi * parameter)
            gaussian = math.exp(-((parameter - selected_height) / sigma) ** 2)
            return amplitude * sine**2 * gaussian / normalization

        def bump_derivative(parameter: float) -> float:
            sine = math.sin(math.pi * parameter)
            cosine = math.cos(math.pi * parameter)
            gaussian = math.exp(-((parameter - selected_height) / sigma) ** 2)
            return amplitude / normalization * gaussian * (
                2.0 * math.pi * sine * cosine
                - 2.0
                * (parameter - selected_height)
                / sigma**2
                * sine**2
            )

        beta_path_offset = lambda parameter: 1j * parameter + bump(parameter)
        beta_path_offset_derivative = (
            lambda parameter: 1j + bump_derivative(parameter)
        )
        strip_inventory = []
        for root_id, center in centers.items():
            root_dx = float(
                (center.real - path_base.real)
                - round(center.real - path_base.real)
            )
            root_height = float((center.imag - path_base.imag) % 1.0)
            path_x = bump(root_height)
            if 0 < root_dx < path_x:
                strip_inventory.append(root_id)
        if strip_inventory:
            raise AssertionError(
                "same-chamber beta detour encloses critical roots: "
                + ", ".join(strip_inventory)
            )
        grid = np.linspace(0.0, 1.0, 10001)
        path_values = np.asarray(
            [
                path_base + beta_path_offset(float(parameter))
                for parameter in grid
            ]
        )
        clearance_rows = []
        for root_id, center in centers.items():
            difference = path_values - center
            difference = (
                difference.real - np.round(difference.real)
            ) + 1j * (difference.imag - np.round(difference.imag))
            clearance_rows.append((float(np.min(abs(difference))), root_id))
        minimum_clearance, nearest_root_id = min(clearance_rows)
        selected_difference = path_values - selected_090
        selected_difference = (
            selected_difference.real - np.round(selected_difference.real)
        ) + 1j * (
            selected_difference.imag - np.round(selected_difference.imag)
        )
        beta_path_diagnostics = {
            "model": "localized positive horizontal Gaussian-sine detour",
            "selected_090_signed_x_from_straight_path": selected_dx,
            "selected_090_height_parameter": selected_height,
            "amplitude": amplitude,
            "sigma": sigma,
            "homotopy_strip_root_ids": strip_inventory,
            "sampled_minimum_critical_clearance": minimum_clearance,
            "sampled_nearest_root_id": nearest_root_id,
            "sampled_selected_090_clearance": float(
                np.min(abs(selected_difference))
            ),
        }
    preflight = {
        "schema": "MTTQ79CovariantPLRecenteredProbePreflight.v1",
        "candidate_rank": 3,
        "perturbation": perturbation,
        "numerical_profile": arguments.numerical_profile,
        "executed_complex_step": probe.encoded_complex_vector(delta),
        "executed_step_maximum_absolute_coordinate": float(np.max(abs(delta))),
        "critical_continuation": critical_diagnostics,
        "selected_039_selected_038_radial_wall": radial_wall,
        "beta_path": beta_path_diagnostics,
        "elapsed_seconds": time.perf_counter() - started,
    }
    dump(output_directory / "preflight.packet.json", preflight)
    crossed_handles = [
        name
        for name, row in critical_diagnostics[
            "fixed_handle_path_wall_diagnostics"
        ].items()
        if not row["same_fixed_handle_chamber"]
    ]
    if crossed_handles:
        raise AssertionError(
            "trust-region step crosses fixed handle wall(s): "
            + ", ".join(crossed_handles)
        )

    fan_by_index = {
        int(row["distinguished_index"]): row
        for row in load(probe.FAN)["distinguished_positive_meridians"]
    }
    cache_directory = output_directory / "thimbles"
    cache_directory.mkdir(parents=True, exist_ok=True)
    thimbles: dict[int, dict] = {}
    tasks = []
    for index in support:
        fan_row = fan_by_index[index]
        cache = cache_directory / f"t{index:03d}.json"
        expected_center = centers[fan_row["root_id"]]
        if cache.exists() and not arguments.force:
            cached = load(cache)
            cached_center = probe.complex_value(cached["critical_center"])
            expected_cache_algorithm = (
                probe.HIGH_ACCURACY_THIMBLE_CACHE_ALGORITHM
                if arguments.numerical_profile == "high_accuracy"
                else (
                    probe.ULTRA_ACCURACY_THIMBLE_CACHE_ALGORITHM
                    if arguments.numerical_profile == "ultra_accuracy"
                    else (
                        probe.EXTREME_ACCURACY_THIMBLE_CACHE_ALGORITHM
                        if arguments.numerical_profile == "extreme_accuracy"
                        else probe.THIMBLE_CACHE_ALGORITHM
                    )
                )
            )
            if (
                cached.get("cache_algorithm") == expected_cache_algorithm
                and abs(cached_center - expected_center) <= 1.0e-14
            ):
                thimbles[index] = cached
                continue
        tasks.append(
            {
                "distinguished_index": index,
                "root_id": fan_row["root_id"],
                "central_packet_path": str(
                    probe.central_period_path(index, fan_row["root_id"])
                ),
                "critical_center": [expected_center.real, expected_center.imag],
                "y_fibration": str(y_path),
                "z_fibration": str(z_path),
                "numerical_profile": arguments.numerical_profile,
            }
        )
    if tasks:
        with ProcessPoolExecutor(max_workers=arguments.workers) as executor:
            futures = {
                executor.submit(probe.thimble_worker, task): task for task in tasks
            }
            for completed, future in enumerate(as_completed(futures), start=1):
                row = future.result()
                index = int(row["distinguished_index"])
                thimbles[index] = row
                dump(cache_directory / f"t{index:03d}.json", row)
                print(f"[{completed}/{len(tasks)}] continued d{index:03d}", flush=True)

    factorization = load(probe.FACTORIZATION)
    vectors = np.asarray(
        [
            row["positive_vanishing_cycle_up_to_sign"]
            for row in factorization["factors"]
        ],
        dtype=np.int64,
    ).T
    pivots = np.asarray(
        [
            int(value) - 1
            for value in orientation["unimodular_pivot_indices_one_based"]
        ],
        dtype=np.int64,
    )
    homology = load(probe.HOMOLOGY)["homology_convention"]
    y_to_z = probe.moving_y_to_z_transition(y_path, alignment, homology)
    pivot_columns = []
    for index in pivots:
        row = thimbles[int(index) + 1]
        values = probe.complex_vector(row["base_fiber_propagated_periods"])
        if row["line_chart"] == "z":
            values = np.linalg.solve(y_to_z, values)
        pivot_columns.append(values)
    pivot_periods = np.column_stack(pivot_columns)
    pivot_signs = np.asarray(orientation["pivot_signs"], dtype=np.int64)
    marked_basis = (pivot_periods * pivot_signs[np.newaxis, :]) @ np.linalg.inv(
        vectors[:, pivots]
    )
    actions = {
        name: np.asarray(factorization["handle_actions"][name], dtype=np.int64)
        for name in ("A", "B")
    }
    central_lifts = {
        name: int(value)
        for name, value in load(probe.CENTRAL_LIFTS)["selected_lifts"].items()
    }
    handle_blocks = []
    handle_rows = []
    for name, displacement in (("A", 1 + 0j), ("B", 1j)):
        block, diagnostics = probe.execute_moving_handle(
            name,
            displacement,
            actions[name],
            central_lifts[name],
            marked_basis,
            homology,
            y_path,
            numerical_profile=arguments.numerical_profile,
        )
        handle_blocks.append(block)
        handle_rows.append(diagnostics)
    handles = np.hstack(handle_blocks)

    center_floating_beta, wound_reference, anchor_packet = probe.beta_anchor(
        probe.central_alignment()
    )
    if arguments.numerical_profile == "high_accuracy":
        beta_rtol, beta_atol = 2.0e-11, 2.0e-13
    elif arguments.numerical_profile == "ultra_accuracy":
        beta_rtol, beta_atol = 2.0e-12, 2.0e-14
    elif arguments.numerical_profile == "extreme_accuracy":
        beta_rtol, beta_atol = 5.0e-13, 5.0e-15
    else:
        beta_rtol, beta_atol = 2.0e-9, 2.0e-11
    if beta_path_offset is None:
        perturbed_floating_beta, beta_diagnostics = evaluator.evaluate(
            alignment,
            line_chart="y",
            base_lift_source_chart="z",
            rtol=beta_rtol,
            atol=beta_atol,
            winding_reference=wound_reference,
        )
    else:
        perturbed_floating_beta, beta_diagnostics = (
            deformed_beta_transport.evaluate_deformed_beta_path(
            evaluator,
            alignment,
            line_chart="y",
            base_lift_source_chart="z",
            rtol=beta_rtol,
            atol=beta_atol,
            winding_reference=wound_reference,
            path_offset=beta_path_offset,
            path_offset_derivative=beta_path_offset_derivative,
            path_model=beta_path_diagnostics["model"],
        )
        )
    certified_beta, certified_beta_path = probe.selected_certified_beta()
    anchored_beta = certified_beta + perturbed_floating_beta - center_floating_beta
    column_signs = np.asarray(orientation["column_signs"], dtype=np.int64)
    if prior_complex_trial is not None:
        center_rows = {
            row["candidate_id"]: row
            for row in prior_complex_trial["candidate_residuals"]
        }
    else:
        center_rows = {
            row["candidate_id"]: row
            for row in next(
                trial
                for trial in a212["corrected_trials"]
                if float(trial["scale"]) == 1.0
            )["candidate_rows"]
        }
    crossing_period = probe.complex_vector(thimbles[65]["period_values"])
    candidate_rows = []
    for candidate in candidates:
        raw_period = np.zeros(8, dtype=np.complex128)
        coefficients = {}
        for chain_row in candidate["primitive_thimble_chain"]:
            index = int(chain_row["distinguished_index"])
            coefficients[index] = int(chain_row["coefficient"])
            value = probe.complex_vector(thimbles[index]["period_values"])
            raw_period += coefficients[index] * column_signs[index - 1] * value
        raw_period += handles @ np.asarray(
            candidate["primitive_handle_coordinates"], dtype=np.float64
        )
        period_correction = coefficients.get(64, 0) * column_signs[63] * crossing_period
        corrected_period = raw_period + period_correction
        raw_residual = anchored_beta - raw_period
        corrected_residual = anchored_beta - corrected_period
        center_residual = probe.complex_vector(
            center_rows[candidate["candidate_id"]]["PL_corrected_residual"]
        )
        row = {
                "candidate_id": candidate["candidate_id"],
                "A132_objective_rank": candidate["A132_objective_rank"],
                "primitive_d064_coefficient": coefficients.get(64, 0),
                "raw_moving_period": probe.encoded_complex_vector(raw_period),
                "PL_period_correction": probe.encoded_complex_vector(period_correction),
                "PL_corrected_moving_period": probe.encoded_complex_vector(corrected_period),
                "raw_residual": probe.encoded_complex_vector(raw_residual),
                "PL_corrected_residual": probe.encoded_complex_vector(corrected_residual),
                "PL_corrected_residual_l2_norm": float(np.linalg.norm(corrected_residual)),
                "PL_corrected_residual_maximum_absolute_value": float(
                    np.max(abs(corrected_residual))
                ),
                "base_PL_corrected_residual": probe.encoded_complex_vector(center_residual),
                "change_from_base_PL_corrected_residual_l2_norm": float(
                    np.linalg.norm(corrected_residual - center_residual)
                ),
        }
        candidate_rows.append(row)
    selected_trial = next(
        row
        for row in candidate_rows
        if int(row["A132_objective_rank"]) == 3
    )
    actual_residual = probe.complex_vector(selected_trial["PL_corrected_residual"])
    completion_summary = {}
    if completion is not None:
        predicted_residual = probe.complex_vector(completion["linearized_residual"])
        completion_summary = {
            "selected_predicted_PL_corrected_residual_l2_norm": float(
                np.linalg.norm(predicted_residual)
            ),
            "selected_model_error_l2_norm": float(
                np.linalg.norm(actual_residual - predicted_residual)
            ),
            "selected_reduction_factor_from_base": float(
                np.linalg.norm(actual_residual)
                / completion["center_residual_l2_norm"]
            ),
        }
    elif refinement is not None:
        predicted_residual = probe.complex_vector(
            refinement["step_02"]["linearized_residual"]
        )
        completion_summary = {
            "selected_predicted_PL_corrected_residual_l2_norm": float(
                np.linalg.norm(predicted_residual)
            ),
            "selected_model_error_l2_norm": float(
                np.linalg.norm(actual_residual - predicted_residual)
            ),
            "selected_reduction_factor_from_base": float(
                np.linalg.norm(actual_residual)
                / refinement["step_01"]["actual_residual_l2_norm"]
            ),
        }
    elif refinement_03 is not None:
        predicted_residual = probe.complex_vector(
            refinement_03["step_03"]["linearized_residual"]
        )
        completion_summary = {
            "selected_predicted_PL_corrected_residual_l2_norm": float(
                np.linalg.norm(predicted_residual)
            ),
            "selected_model_error_l2_norm": float(
                np.linalg.norm(actual_residual - predicted_residual)
            ),
            "selected_reduction_factor_from_base": float(
                np.linalg.norm(actual_residual)
                / refinement_03["step_02"]["actual_residual_l2_norm"]
            ),
        }
    packet = {
        "schema": "MTTQ79HeightFourCovariantPLRecenteredProbe.v1",
        "status": (
            "SAME_SOURCE_PL_RECENTERED_COMPLEX_NEWTON_TRIAL_EXECUTED"
            if completion is not None
            or refinement is not None
            or refinement_03 is not None
            else "SAME_SOURCE_PL_RECENTERED_SIGNED_PROBE_EXECUTED"
        ),
        "tag": tag,
        "perturbation": perturbation,
        "numerical_profile": arguments.numerical_profile,
        "base_alignment": probe.encoded_complex_matrix(base_alignment),
        "alignment": probe.encoded_complex_matrix(alignment),
        "critical_continuation": critical_diagnostics,
        "selected_039_selected_038_radial_wall": radial_wall,
        "moving_handles": {
            "diagnostics": handle_rows,
            "primitive_handle_period_matrix": probe.encoded_complex_matrix(handles),
        },
        "moving_beta": {
            "branch_route": probe.BETA_BRANCH_ROUTE,
            "path": beta_path_diagnostics,
            "center_anchor_difference": anchor_packet[
                "floating_to_certified_maximum_absolute_difference"
            ],
            "certified_beta_path": relative(certified_beta_path),
            "diagnostics": beta_diagnostics,
        },
        "candidate_residuals": candidate_rows,
        "summary": {
            "selected_candidate_rank": 3,
            "selected_base_PL_corrected_residual_l2_norm": float(
                np.linalg.norm(
                    probe.complex_vector(selected_trial["base_PL_corrected_residual"])
                )
            ),
            "selected_perturbed_PL_corrected_residual_l2_norm": selected_trial[
                "PL_corrected_residual_l2_norm"
            ],
            "selected_change_from_base_l2_norm": selected_trial[
                "change_from_base_PL_corrected_residual_l2_norm"
            ],
            "selected_radial_wall_signed_coordinate": radial_wall[
                "signed_transverse_coordinate"
            ],
            "elapsed_seconds": time.perf_counter() - started,
            **completion_summary,
        },
        "authority": {
            "base_trial": relative(BASE_TRIAL),
            "base_trial_sha256": sha256(BASE_TRIAL),
            "A212": relative(A212),
            "A212_sha256": sha256(A212),
            "complex_completion": (
                relative(COMPLEX_COMPLETION) if completion is not None else None
            ),
            "complex_completion_sha256": (
                sha256(COMPLEX_COMPLETION) if completion is not None else None
            ),
            "complex_refinement": (
                relative(COMPLEX_REFINEMENT) if refinement is not None else None
            ),
            "complex_refinement_sha256": (
                sha256(COMPLEX_REFINEMENT) if refinement is not None else None
            ),
            "prior_complex_trial": (
                relative(COMPLEX_TRIAL_01) if refinement is not None else None
            ),
            "prior_complex_trial_sha256": (
                sha256(COMPLEX_TRIAL_01) if refinement is not None else None
            ),
            "complex_refinement_03": (
                relative(COMPLEX_REFINEMENT_03)
                if refinement_03 is not None
                else None
            ),
            "complex_refinement_03_sha256": (
                sha256(COMPLEX_REFINEMENT_03)
                if refinement_03 is not None
                else None
            ),
            "prior_ultra_complex_trial": (
                relative(COMPLEX_TRIAL_02) if refinement_03 is not None else None
            ),
            "prior_ultra_complex_trial_sha256": (
                sha256(COMPLEX_TRIAL_02) if refinement_03 is not None else None
            ),
            "probe_engine_source": relative(Path(probe.__file__).resolve()),
            "probe_engine_source_sha256": sha256(Path(probe.__file__).resolve()),
            "runner_source": relative(Path(__file__)),
            "runner_source_sha256": sha256(Path(__file__)),
            "deformed_beta_transport_source": (
                relative(Path(deformed_beta_transport.__file__).resolve())
                if beta_path_offset is not None
                else None
            ),
            "deformed_beta_transport_source_sha256": (
                sha256(Path(deformed_beta_transport.__file__).resolve())
                if beta_path_offset is not None
                else None
            ),
        },
        "strict_scope": {
            "same_source_signed_probe": (
                completion is None
                and refinement is None
                and refinement_03 is None
            ),
            "same_source_nonlinear_complex_trial": (
                completion is not None
                or refinement is not None
                or refinement_03 is not None
            ),
            "complex_PGL3_tangent_axis": (
                "full_complex"
                if completion is not None
                or refinement is not None
                or refinement_03 is not None
                else arguments.tangent_axis
            ),
            "PL_corrected_candidate_periods": True,
            "same_fixed_handle_chamber": True,
            "same_post_selected_039_selected_038_radial_chamber": True,
            "floating_only": True,
            "high_accuracy_replay": arguments.numerical_profile
            in ("high_accuracy", "ultra_accuracy", "extreme_accuracy"),
            "beta_path_same_homotopy_strip_empty": not beta_path_diagnostics[
                "homotopy_strip_root_ids"
            ],
            "interval_derivative_certificate": False,
            "covariant_zero_proved": False,
            "observed_SM_values_used": False,
        },
    }
    dump(output, packet)
    print(f"wrote {relative(output)}")
    print(json.dumps(packet["summary"], indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
