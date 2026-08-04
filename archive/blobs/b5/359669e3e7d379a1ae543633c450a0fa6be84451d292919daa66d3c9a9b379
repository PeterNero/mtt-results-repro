from __future__ import annotations

import argparse
import ctypes
import hashlib
import json
import math
import os
import time
from dataclasses import asdict
from pathlib import Path

import numpy as np
from flint import acb, acb_poly, arb, ctx

import certify_q79_height4_d087_full_residue_main_interval as main_engine
import certify_q79_height4_d087_full_residue_tail_interval as all_tail_engine
import certify_q79_selected_alignment_E32_handle_combination_interval as handle
import certify_q79_selected_alignment_single_E32_thimble_main_interval as pilot
import certify_q79_selected_alignment_single_E32_thimble_nodal_factor as nodal
import certify_q79_selected_alignment_single_E32_thimble_tail_interval as tail
import certify_q79_selected_side_beta_defect_transport as validated


ROOT = main_engine.ROOT
PROBE_DIRECTORY = main_engine.PROBE_DIRECTORY
TRIAL = main_engine.TRIAL
FIBRATION = main_engine.FIBRATION
BOUNDARY = PROBE_DIRECTORY / "rank3_complex_PGL3_floating_boundary.packet.json"
VALIDATED_DIRECTORY = PROBE_DIRECTORY / "validated_transport"


def load(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def dump(path: Path, value: dict) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(value, indent=2, sort_keys=True) + "\n", encoding="utf-8")


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def relative(path: Path) -> str:
    return str(path.relative_to(ROOT)).replace("\\", "/")


def complex_value(value: dict[str, str]) -> complex:
    return complex(float(value["real"]), float(value["imaginary"]))


def encoded_complex(value: complex) -> dict[str, str]:
    return {
        "real": format(float(value.real), ".17g"),
        "imaginary": format(float(value.imag), ".17g"),
    }


def paths(index: int) -> dict[str, Path]:
    stem = f"d{index:03d}.n3"
    return {
        "thimble": PROBE_DIRECTORY / "cplx" / "n3ud" / "thimbles" / f"t{index:03d}.json",
        "node": VALIDATED_DIRECTORY / f"{stem}.node.refined.json",
        "main": VALIDATED_DIRECTORY / f"{stem}.main8.refined.json",
        "main_checkpoint": VALIDATED_DIRECTORY / f"{stem}.main8.refined.checkpoint.json",
        "tail": VALIDATED_DIRECTORY / f"{stem}.tail8.refined.json",
        "full": VALIDATED_DIRECTORY / f"{stem}.full8.refined.json",
    }


def target(index: int) -> tuple[dict, dict[str, Path]]:
    target_paths = paths(index)
    thimble = load(target_paths["thimble"])
    if int(thimble["distinguished_index"]) != index:
        raise AssertionError(f"target cache is not d{index:03d}")
    if thimble["line_chart"] != "y":
        raise AssertionError("generic n3 all-row certificate currently requires y chart")
    return thimble, target_paths


def signed_chain_coefficient(index: int, root_id: str) -> int:
    boundary = load(BOUNDARY)
    matches = [
        row
        for row in boundary["difference_decomposition"]["ranked_thimble_contributions"]
        if int(row["distinguished_index"]) == index
    ]
    if len(matches) != 1:
        raise AssertionError(f"A219 does not select exactly one d{index:03d} chain row")
    row = matches[0]
    if row["root_id"] != root_id:
        raise AssertionError(f"A219 root ID changed for d{index:03d}")
    coefficient = int(row["signed_coefficient"])
    if coefficient == 0:
        raise AssertionError("selected chain coefficient is zero")
    return coefficient


def set_below_normal_priority() -> bool:
    if os.name != "nt":
        return False
    below_normal_priority_class = 0x00004000
    kernel32 = ctypes.windll.kernel32
    handle = kernel32.GetCurrentProcess()
    return bool(kernel32.SetPriorityClass(handle, below_normal_priority_class))


def encoded_frame(frame: pilot.E32LiftErrorFrame) -> dict:
    return {
        "fundamental": validated.encoded_matrix(frame.fundamental),
        "coordinate_radii": [str(value) for value in frame.coordinate_radii],
    }


def decoded_frame(value: dict) -> pilot.E32LiftErrorFrame:
    return pilot.E32LiftErrorFrame(
        fundamental=validated.decoded_matrix(value["fundamental"]),
        coordinate_radii=[arb(entry) for entry in value["coordinate_radii"]],
    )


def transport_configuration(
    *,
    index: int,
    root_id: str,
    start: complex,
    endpoint: complex,
    order: int,
    maximum_step: float,
    minimum_step: float,
    maximum_lift_correction: float,
    maximum_integral_radius: float,
) -> dict:
    return {
        "index": index,
        "root_id": root_id,
        "start": encoded_complex(start),
        "endpoint": encoded_complex(endpoint),
        "order": order,
        "maximum_step": format(maximum_step, ".17g"),
        "minimum_step": format(minimum_step, ".17g"),
        "maximum_lift_correction": format(maximum_lift_correction, ".17g"),
        "maximum_integral_radius": format(maximum_integral_radius, ".17g"),
    }


def execute_main_transport_resumable(
    system: validated.SelectedQ79IntervalSystem,
    initial_periods: list[acb],
    *,
    index: int,
    root_id: str,
    checkpoint_path: Path,
    start: complex,
    endpoint: complex,
    order: int,
    maximum_step: float,
    initial_step: float,
    minimum_step: float,
    maximum_lift_correction: float,
    maximum_integral_radius: float,
    cooling_pause_every: int,
    cooling_pause_seconds: float,
) -> dict:
    source_path = Path(__file__).resolve()
    configuration = transport_configuration(
        index=index,
        root_id=root_id,
        start=start,
        endpoint=endpoint,
        order=order,
        maximum_step=maximum_step,
        minimum_step=minimum_step,
        maximum_lift_correction=maximum_lift_correction,
        maximum_integral_radius=maximum_integral_radius,
    )
    distance = abs(endpoint - start)
    direction = (endpoint - start) / distance
    if checkpoint_path.exists():
        checkpoint = load(checkpoint_path)
        if checkpoint["schema"] != "MTTQ79HeightFourAllRowMainCheckpoint.v1":
            raise ValueError("all-row checkpoint schema changed")
        if checkpoint["source_sha256"] != sha256(source_path):
            raise ValueError("all-row checkpoint source hash is stale")
        if checkpoint["configuration"] != configuration:
            raise ValueError("all-row checkpoint configuration changed")
        position = float(checkpoint["position"])
        proposed = float(checkpoint["proposed_step"])
        centers = [
            [validated.decoded_acb(entry) for entry in row]
            for row in checkpoint["centers"]
        ]
        frames = [decoded_frame(value) for value in checkpoint["frames"]]
        accepted = checkpoint["accepted_steps"]
        rejected = int(checkpoint["rejected_step_count"])
        minimum_accepted = float(checkpoint["minimum_accepted_step"])
        print(
            f"resumed d{index:03d} all-row main checkpoint steps={len(accepted)} "
            f"fraction={position / distance:.12g}",
            flush=True,
        )
    else:
        initial_center = [system.midpoint_acb(value) for value in initial_periods]
        centers = [initial_center + [acb(0)] for _ in range(8)]
        frames = []
        for _residue_index in range(8):
            identity = validated.acb_mat(6, 6)
            for coordinate in range(6):
                identity[coordinate, coordinate] = acb(1)
            frames.append(
                pilot.E32LiftErrorFrame(
                    fundamental=identity,
                    coordinate_radii=[
                        value.rad().upper() for value in initial_periods
                    ]
                    + [arb(0)],
                )
            )
        position = 0.0
        proposed = min(initial_step, maximum_step, distance)
        accepted = []
        rejected = 0
        minimum_accepted = math.inf

    def write_checkpoint() -> None:
        validated.atomic_dump(
            checkpoint_path,
            {
                "schema": "MTTQ79HeightFourAllRowMainCheckpoint.v1",
                "source_sha256": sha256(source_path),
                "configuration": configuration,
                "position": format(position, ".17g"),
                "path_length": format(distance, ".17g"),
                "proposed_step": format(proposed, ".17g"),
                "centers": [
                    [validated.encoded_acb(entry) for entry in row]
                    for row in centers
                ],
                "frames": [encoded_frame(frame) for frame in frames],
                "accepted_steps": accepted,
                "rejected_step_count": rejected,
                "minimum_accepted_step": format(minimum_accepted, ".17g"),
                "complete": bool(position >= distance),
            },
        )

    while position < distance:
        step = min(proposed, distance - position)
        parameter_start = start + direction * position
        try:
            next_centers, next_frames, diagnostics = (
                main_engine.validated_all_residue_rows_step(
                    system,
                    parameter_start,
                    direction,
                    step,
                    centers,
                    frames,
                    order=order,
                )
            )
            if (
                diagnostics["maximum_transformed_lift_correction"]
                > maximum_lift_correction
            ):
                raise ArithmeticError("lift correction exceeds local budget")
            if (
                diagnostics["maximum_residue_coordinate_radius_upper"]
                > maximum_integral_radius
            ):
                raise ArithmeticError("full-residue radius exceeds global budget")
        except (ArithmeticError, ZeroDivisionError, ValueError) as error:
            rejected += 1
            proposed = step / 2.0
            if rejected % 10 == 0:
                print(
                    f"validated d{index:03d} all-row main rejections={rejected} "
                    f"fraction={position / distance:.12g} next_step={proposed:.3e} "
                    f"reason={type(error).__name__}: {error}",
                    flush=True,
                )
            if proposed < minimum_step:
                raise
            continue
        centers = next_centers
        frames = next_frames
        position = min(distance, position + step)
        minimum_accepted = min(minimum_accepted, step)
        accepted.append(
            {
                "start_arclength": position - step,
                "end_arclength": position,
                "step": step,
                **diagnostics,
            }
        )
        quality = max(
            diagnostics["reduction_neumann_norm"],
            diagnostics["maximum_fundamental_inverse_neumann_norm"],
        )
        proposed = min(maximum_step, step * (1.8 if quality < 0.05 else 1.35))
        write_checkpoint()
        if len(accepted) <= 3 or len(accepted) % 10 == 0 or position == distance:
            print(
                f"validated d{index:03d} all-row main steps={len(accepted)} "
                f"fraction={position / distance:.12g} "
                f"radius={diagnostics['maximum_residue_coordinate_radius_upper']:.3e}",
                flush=True,
            )
        if (
            cooling_pause_seconds > 0.0
            and cooling_pause_every > 0
            and len(accepted) % cooling_pause_every == 0
            and position < distance
        ):
            time.sleep(cooling_pause_seconds)

    period_centers = np.asarray(
        [
            [
                complex(float(value.real.mid()), float(value.imag.mid()))
                for value in center[:5]
            ]
            for center in centers
        ],
        dtype=np.complex128,
    )
    period_dispersion = float(np.max(abs(period_centers - period_centers[0])))
    residue_radii = []
    for frame in frames:
        generator = frame.physical_generator_matrix()
        residue_radii.append(
            validated.upper(
                sum((abs(generator[5, column]) for column in range(6)), arb(0))
            )
        )
    output_center = centers[0][:5] + [center[5] for center in centers]
    return {
        "center": [encoded_complex(handle.midpoint(value)) for value in output_center],
        "residue_coordinate_radius_uppers": residue_radii,
        "uniform_integral_radius_upper": max(residue_radii),
        "lift_radius_uppers": [
            validated.upper(frame.physical_radius()) for frame in frames
        ],
        "period_center_dispersion_across_frames": period_dispersion,
        "certificate_method": (
            "eight correlated six-dimensional homogeneous augmented frames "
            "sharing one validated Taylor-system construction per step with "
            "atomic exact-ball checkpoint replay"
        ),
        "accepted_step_count": len(accepted),
        "rejected_step_count": rejected,
        "minimum_accepted_step": minimum_accepted,
        "path_length": distance,
        "checkpoint_path": relative(checkpoint_path),
        "steps": accepted,
    }


def execute_main(arguments: argparse.Namespace) -> dict:
    started = time.perf_counter()
    ctx.dps = arguments.main_dps
    thimble, target_paths = target(arguments.index)
    root_id = thimble["root_id"]
    label = f"d{arguments.index:03d}"
    system = main_engine.exact_target_system(arguments.main_dps)
    print(f"initialized exact n3 y-chart interval system for {label}", flush=True)
    critical = complex_value(thimble["critical_center"])
    node_parameter, node_root, node_diagnostics = main_engine.fast_certify_node(
        system,
        critical,
        epsilon=arguments.epsilon,
        iterations=arguments.node_iterations,
    )
    factor_diagnostics = nodal.nodal_factor_certificate(
        system, node_parameter, node_root
    )
    node_payload = {
        "schema": "MTTQ79HeightFourTargetNodeInterval.v1",
        "status": "N3_TARGET_NODE_AND_LOCAL_FACTOR_INTERVAL_CERTIFIED",
        "selected_target": {
            "distinguished_index": arguments.index,
            "root_id": root_id,
            "line_chart": "y",
            "critical_center_floating_seed": thimble["critical_center"],
        },
        "certified_node": {
            "parameter_ball": nodal.encoded_acb(node_parameter),
            "double_root_ball": nodal.encoded_acb(node_root),
            "parameter_radius_upper": validated.radius_upper(node_parameter),
            "double_root_radius_upper": validated.radius_upper(node_root),
            "node_diagnostics": node_diagnostics,
            "factor_diagnostics": factor_diagnostics,
        },
        "authority": {
            name: {"path": relative(path), "sha256": sha256(path)}
            for name, path in {
                "n3_y_fibration": FIBRATION,
                "n3_target_cache": target_paths["thimble"],
                "generic_source": Path(__file__).resolve(),
                "A220_node_kernel": Path(main_engine.__file__).resolve(),
                "node_engine": Path(nodal.__file__).resolve(),
            }.items()
        },
        "strict_scope": {
            "observed_SM_values_used": False,
            "target_node_interval_Newton_closed": True,
            "simple_node_factor_closed": True,
            "full_period_vector_interval_closed": False,
        },
    }
    dump(target_paths["node"], node_payload)
    print(
        f"certified {label} node parameter_radius="
        f"{validated.radius_upper(node_parameter):.3e} root_radius="
        f"{validated.radius_upper(node_root):.3e}",
        flush=True,
    )

    node_center = handle.midpoint(node_parameter)
    start_ball = node_center * acb(format(1.0 - arguments.epsilon, ".17g"))
    start = handle.midpoint(start_ball)
    start_complex = complex(float(start.real), float(start.imag))
    roots, leading = pilot.roots_at(system, start_complex)
    pair, pair_diagnostics = pilot.closest_pair(roots)
    initial_periods, cut_diagnostics = handle.direct_cut_periods(
        roots,
        leading,
        pair,
        segments=arguments.cut_segments,
        tolerance=arguments.cut_tolerance,
    )
    initial_step = min(
        arguments.maximum_step,
        abs(complex(float(node_center.real), float(node_center.imag)) - start_complex)
        / 4.0,
    )
    execution = execute_main_transport_resumable(
        system,
        initial_periods,
        index=arguments.index,
        root_id=root_id,
        checkpoint_path=target_paths["main_checkpoint"],
        start=start_complex,
        endpoint=0.0 + 0.0j,
        order=arguments.order,
        maximum_step=arguments.maximum_step,
        initial_step=initial_step,
        minimum_step=arguments.minimum_step,
        maximum_lift_correction=arguments.maximum_lift_correction,
        maximum_integral_radius=arguments.maximum_integral_radius,
        cooling_pause_every=arguments.cooling_pause_every,
        cooling_pause_seconds=arguments.cooling_pause_seconds,
    )
    base_center = np.asarray(
        [complex_value(value) for value in execution["center"][:5]],
        dtype=np.complex128,
    )
    floating_base = np.asarray(
        [complex_value(value) for value in thimble["base_fiber_propagated_periods"]],
        dtype=np.complex128,
    )
    plus = float(np.max(abs(base_center - floating_base)))
    minus = float(np.max(abs(-base_center - floating_base)))
    orientation_sign = 1 if plus <= minus else -1
    selected_difference = min(plus, minus)
    rejected_difference = max(plus, minus)
    if rejected_difference <= 1000.0 * max(selected_difference, 1.0e-15):
        raise AssertionError(f"validated {label} orientation is not separated")
    transported_integrals = np.asarray(
        [complex_value(value) for value in execution["center"][5:]],
        dtype=np.complex128,
    )
    main_center = -orientation_sign * transported_integrals
    floating_full = np.asarray(
        [complex_value(value) for value in thimble["period_values"]],
        dtype=np.complex128,
    )
    diagnostic_tail = floating_full - main_center
    payload = {
        "schema": "MTTQ79HeightFourTargetFullResidueMainInterval.v1",
        "status": "N3_NODE_AND_ALL_EIGHT_MAIN_RESIDUE_ROWS_INTERVAL_CERTIFIED_TAIL_OPEN",
        "selected_target": {
            "distinguished_index": arguments.index,
            "root_id": root_id,
            "line_chart": "y",
            "candidate_rank": 3,
            "endpoint_cutoff_epsilon": arguments.epsilon,
            "critical_center_floating_seed": thimble["critical_center"],
            "near_node_colliding_pair_zero_based": list(pair),
            **pair_diagnostics,
        },
        "certified_node": node_payload["certified_node"],
        "near_node_direct_cycle_interval": {
            **cut_diagnostics,
            "initial_period_intervals": [
                handle.complex_interval(value) for value in initial_periods
            ],
        },
        "validated_main_transport": execution,
        "orientation": {
            "selected_sign": orientation_sign,
            "selected_base_center_maximum_difference": selected_difference,
            "opposite_base_center_maximum_difference": rejected_difference,
            "reference": f"n3 ultra {label} continuity-synchronized floating cache",
        },
        "all_eight_main_residue_rows": {
            "interval_centers": [encoded_complex(value) for value in main_center],
            "common_complex_disk_radius_upper": execution[
                "uniform_integral_radius_upper"
            ],
            "floating_full_thimble_values_diagnostic_only": [
                encoded_complex(value) for value in floating_full
            ],
            "diagnostic_unvalidated_tail_centers": [
                encoded_complex(value) for value in diagnostic_tail
            ],
            "diagnostic_maximum_tail_absolute_value": float(
                np.max(abs(diagnostic_tail))
            ),
        },
        "authority": {
            name: {"path": relative(path), "sha256": sha256(path)}
            for name, path in {
                "n3_ultra_trial": TRIAL,
                "n3_y_fibration": FIBRATION,
                "n3_target_cache": target_paths["thimble"],
                "validated_taylor_engine": Path(validated.__file__).resolve(),
                "node_engine": Path(nodal.__file__).resolve(),
                "main_interval_engine": Path(pilot.__file__).resolve(),
                "A220_all_row_kernel": Path(main_engine.__file__).resolve(),
                "completed_transport_checkpoint": target_paths["main_checkpoint"],
                "generic_source": Path(__file__).resolve(),
            }.items()
        },
        "numerics": {
            "dps": arguments.main_dps,
            "Taylor_order": arguments.order,
            "maximum_step": arguments.maximum_step,
            "minimum_step": arguments.minimum_step,
            "maximum_lift_correction": arguments.maximum_lift_correction,
            "maximum_integral_radius": arguments.maximum_integral_radius,
            "cut_segments": arguments.cut_segments,
            "cut_tolerance": arguments.cut_tolerance,
            "cooling_pause_every": arguments.cooling_pause_every,
            "cooling_pause_seconds": arguments.cooling_pause_seconds,
            "below_normal_priority_requested": True,
            "interval_system_diagnostics": asdict(system.diagnostics),
            "elapsed_seconds": time.perf_counter() - started,
        },
        "strict_scope": {
            "observed_SM_values_used": False,
            "target_alignment_interval_used": True,
            "target_node_interval_Newton_closed": True,
            "all_eight_main_residue_rows_interval_closed": True,
            "node_to_cutoff_tail_interval_closed": False,
            "full_period_vector_interval_closed": False,
            "covariant_zero_proved": False,
        },
        "next_required_artifact": (
            "certify the all-eight node-to-cutoff residue tail on the same n3 "
            "alignment and splice it to this main vector"
        ),
    }
    dump(target_paths["main"], payload)
    print(f"wrote {relative(target_paths['node'])}", flush=True)
    print(f"wrote {relative(target_paths['main'])}", flush=True)
    print(
        json.dumps(
            {
                "main_maximum_radius": execution["uniform_integral_radius_upper"],
                "accepted_steps": execution["accepted_step_count"],
                "rejected_steps": execution["rejected_step_count"],
                "orientation_sign": orientation_sign,
                "elapsed_seconds": time.perf_counter() - started,
            },
            indent=2,
        ),
        flush=True,
    )
    return payload


def execute_tail(arguments: argparse.Namespace) -> dict:
    started = time.perf_counter()
    ctx.dps = arguments.tail_dps
    thimble, target_paths = target(arguments.index)
    root_id = thimble["root_id"]
    label = f"d{arguments.index:03d}"
    node_packet = load(target_paths["node"])
    if node_packet["selected_target"]["root_id"] != root_id:
        raise AssertionError(f"{label} node identity changed")
    node_parameter = validated.decoded_acb(
        node_packet["certified_node"]["parameter_ball"]
    )
    node_root = validated.decoded_acb(
        node_packet["certified_node"]["double_root_ball"]
    )
    system = main_engine.exact_target_system(arguments.tail_dps)
    factor_models, factor_disk_diagnostics = tail.factor_taylor_models(
        system,
        node_parameter,
        node_root,
        epsilon=arguments.epsilon,
        order=arguments.factor_order,
    )
    cutoff_parameter = nodal.midpoint(node_parameter) * acb(
        format(1.0 - arguments.epsilon, ".17g")
    )
    cutoff_coefficients, _derivative = nodal.fiber_coefficients(
        system, cutoff_parameter
    )
    cutoff_roots = acb_poly(cutoff_coefficients).roots(tol=1.0e-45, maxprec=4096)
    if len(cutoff_roots) != 6:
        raise AssertionError(f"{label} cutoff root isolation failed")
    cutoff_pair = nodal.closest_pair(cutoff_roots)
    cutoff_periods, cutoff_diagnostics = handle.direct_cut_periods(
        cutoff_roots,
        cutoff_coefficients[6],
        cutoff_pair,
        segments=arguments.theta_segments,
        tolerance=1.0e-35,
    )
    reference = cutoff_periods[:2]
    node_factor = tail.evaluate_factor_models(
        factor_models,
        0.0,
        arguments.node_width,
        factor_disk_diagnostics["center_x"],
    )
    node_x_box = arb(
        format(arguments.node_width / 2.0, ".17g"),
        format(arguments.node_width / 2.0, ".17g"),
    )
    node_parameter_box = node_parameter * (acb(1) - acb(node_x_box))
    node_contributions, node_bound = all_tail_engine.all_row_node_segment_bound(
        node_factor,
        system,
        node_parameter_box,
        node_parameter,
        arguments.node_width,
    )
    totals = list(node_contributions)
    rows = []
    previous_factor: list[acb] | None = None
    ratio = (arguments.epsilon / arguments.node_width) ** (
        1.0 / arguments.outer_segments
    )
    edges = [
        arguments.node_width * ratio**index
        for index in range(arguments.outer_segments)
    ]
    edges.append(arguments.epsilon)
    intervals = list(zip(edges[:-1], edges[1:]))
    progress_interval = max(1, arguments.outer_segments // 20)
    for reverse_index, (x_left, x_right) in enumerate(reversed(intervals)):
        factor = tail.evaluate_factor_models(
            factor_models,
            x_left,
            x_right,
            factor_disk_diagnostics["center_x"],
        )
        x_box = arb(
            format((x_left + x_right) / 2.0, ".17g"),
            format((x_right - x_left) / 2.0, ".17g"),
        )
        parameter_box = node_parameter * (acb(1) - acb(x_box))
        periods, period_diagnostics = tail.period_enclosure(
            factor, theta_segments=arguments.theta_segments
        )
        periods, sign, selected_difference, rejected_difference = tail.orient_periods(
            periods, reference
        )
        reference = periods
        width = acb(format(x_right - x_left, ".17g"))
        row_integrals = []
        for residue_index, (constant, linear) in enumerate(
            all_tail_engine.residue_coefficients(system, parameter_box)
        ):
            integrand = acb(0, 1) * node_parameter * (
                constant * periods[0] + linear * periods[1]
            )
            contribution = width * integrand
            totals[residue_index] += contribution
            row_integrals.append(
                {
                    "residue_index_zero_based": residue_index,
                    "integrand_interval": handle.complex_interval(integrand),
                    "contribution_interval": handle.complex_interval(contribution),
                }
            )
        overlap = (
            [True for _ in range(7)]
            if previous_factor is None
            else [
                previous_factor[index].overlaps(factor[index])
                for index in range(7)
            ]
        )
        rows.append(
            {
                "reverse_index_from_cutoff": reverse_index,
                "x_interval": {"lower": x_left, "upper": x_right},
                "maximum_factor_radius_upper": max(
                    validated.radius_upper(value) for value in factor
                ),
                **period_diagnostics,
                "selected_period_sign": sign,
                "selected_orientation_difference_upper": selected_difference,
                "opposite_orientation_difference_lower": rejected_difference,
                "factor_overlap_with_node_side_neighbor": bool(all(overlap)),
                "row_integrals": row_integrals,
            }
        )
        previous_factor = factor
        if (reverse_index + 1) % progress_interval == 0:
            print(
                f"certified {label} all-row tail segments="
                f"{reverse_index + 1}/{arguments.outer_segments} radius="
                f"{max(validated.radius_upper(value) for value in totals):.3e}",
                flush=True,
            )
    if previous_factor is None or not all(
        previous_factor[index].overlaps(node_factor[index]) for index in range(7)
    ):
        raise AssertionError(f"{label} factor chain does not overlap node segment")
    radii = [validated.radius_upper(value) for value in totals]
    payload = {
        "schema": "MTTQ79HeightFourTargetFullResidueTailInterval.v1",
        "status": "N3_ALL_EIGHT_NODE_TO_CUTOFF_RESIDUE_TAILS_INTERVAL_CERTIFIED",
        "selected_target": {
            "distinguished_index": arguments.index,
            "root_id": root_id,
            "line_chart": "y",
            "endpoint_cutoff_epsilon": arguments.epsilon,
            "cutoff_pair_zero_based": list(cutoff_pair),
        },
        "cutoff_direct_period_reference": {
            **cutoff_diagnostics,
            "I0_I1_intervals": [
                handle.complex_interval(value) for value in cutoff_periods[:2]
            ],
        },
        "quantitative_Hensel_disk": factor_disk_diagnostics,
        "node_segment": {
            "x_interval": {"lower": 0.0, "upper": arguments.node_width},
            "absolute_bounds": node_bound,
            "contribution_intervals": [
                handle.complex_interval(value) for value in node_contributions
            ],
        },
        "regular_segments": rows,
        "all_eight_endpoint_tails": {
            "intervals": [handle.complex_interval(value) for value in totals],
            "interval_centers": [
                encoded_complex(handle.midpoint(value)) for value in totals
            ],
            "interval_radius_uppers": radii,
            "maximum_interval_radius_upper": max(radii),
        },
        "authority": {
            name: {"path": relative(path), "sha256": sha256(path)}
            for name, path in {
                "target_node": target_paths["node"],
                "n3_target_cache": target_paths["thimble"],
                "A221_all_row_kernel": Path(all_tail_engine.__file__).resolve(),
                "tail_engine": Path(tail.__file__).resolve(),
                "generic_source": Path(__file__).resolve(),
            }.items()
        },
        "numerics": {
            "dps": arguments.tail_dps,
            "factor_order": arguments.factor_order,
            "outer_segments": arguments.outer_segments,
            "theta_segments": arguments.theta_segments,
            "node_width": arguments.node_width,
            "elapsed_seconds": time.perf_counter() - started,
        },
        "strict_scope": {
            "observed_SM_values_used": False,
            "target_node_consumed": True,
            "quantitative_Hensel_disk_closed": True,
            "all_eight_node_to_cutoff_tail_intervals_closed": True,
            "full_period_vector_interval_closed": False,
            "covariant_zero_proved": False,
        },
        "next_required_artifact": (
            "splice these eight oriented tail balls to the target's eight "
            "validated main balls"
        ),
    }
    dump(target_paths["tail"], payload)
    print(f"wrote {relative(target_paths['tail'])}", flush=True)
    print(
        json.dumps(
            {
                "maximum_tail_radius": max(radii),
                "regular_segments": len(rows),
                "elapsed_seconds": time.perf_counter() - started,
            },
            indent=2,
        ),
        flush=True,
    )
    return payload


def execute_full(arguments: argparse.Namespace) -> dict:
    thimble, target_paths = target(arguments.index)
    main_packet = load(target_paths["main"])
    tail_packet = load(target_paths["tail"])
    orientation = int(main_packet["orientation"]["selected_sign"])
    coefficient = signed_chain_coefficient(arguments.index, thimble["root_id"])
    main_centers = np.asarray(
        [
            complex_value(value)
            for value in main_packet["all_eight_main_residue_rows"][
                "interval_centers"
            ]
        ],
        dtype=np.complex128,
    )
    tail_centers = np.asarray(
        [
            complex_value(value)
            for value in tail_packet["all_eight_endpoint_tails"][
                "interval_centers"
            ]
        ],
        dtype=np.complex128,
    )
    main_radii = np.asarray(
        main_packet["validated_main_transport"][
            "residue_coordinate_radius_uppers"
        ],
        dtype=np.float64,
    )
    tail_radii = np.asarray(
        tail_packet["all_eight_endpoint_tails"]["interval_radius_uppers"],
        dtype=np.float64,
    )
    floating = np.asarray(
        [complex_value(value) for value in thimble["period_values"]],
        dtype=np.complex128,
    )
    full_centers = main_centers + orientation * tail_centers
    full_radii = main_radii + tail_radii
    differences = abs(floating - full_centers)
    contained = differences <= full_radii
    if not bool(np.all(contained)):
        raise AssertionError(
            f"d{arguments.index:03d} floating vector left refined intervals: "
            f"{np.flatnonzero(~contained).tolist()}"
        )
    rows = []
    for index in range(8):
        rows.append(
            {
                "residue_index_zero_based": index,
                "full_interval_center": encoded_complex(full_centers[index]),
                "full_interval_radius_upper": float(full_radii[index]),
                "selected_chain_contribution_center": encoded_complex(
                    coefficient * full_centers[index]
                ),
                "selected_chain_contribution_radius_upper": float(
                    abs(coefficient) * full_radii[index]
                ),
                "floating_value_diagnostic_only": encoded_complex(floating[index]),
                "floating_to_interval_center_distance": float(differences[index]),
                "floating_value_contained": bool(contained[index]),
                "containment_margin": float(full_radii[index] - differences[index]),
            }
        )
    chain_radii = abs(coefficient) * full_radii
    payload = {
        "schema": "MTTQ79HeightFourTargetRefinedFullResidueInterval.v1",
        "status": "N3_REFINED_FULL_EIGHT_ROW_CHAIN_CONTRIBUTION_INTERVAL_CERTIFIED",
        "artifact": arguments.artifact,
        "selected_target": {
            "distinguished_index": arguments.index,
            "root_id": thimble["root_id"],
            "line_chart": "y",
            "orientation_sign": orientation,
            "selected_chain_coefficient": coefficient,
            "endpoint_cutoff_epsilon": arguments.epsilon,
        },
        "residue_rows": rows,
        "summary": {
            "certified_rows": 8,
            "maximum_full_interval_radius_upper": float(np.max(full_radii)),
            "maximum_chain_coordinate_radius_upper": float(np.max(chain_radii)),
            "selected_chain_product_disk_l2_radius_upper": float(
                np.linalg.norm(chain_radii)
            ),
            "maximum_floating_center_difference": float(np.max(differences)),
            "minimum_floating_containment_margin": float(
                np.min(full_radii - differences)
            ),
            "all_floating_values_contained": bool(np.all(contained)),
        },
        "authority": {
            name: {"path": relative(path), "sha256": sha256(path)}
            for name, path in {
                "refined_main": target_paths["main"],
                "refined_tail": target_paths["tail"],
                "n3_target_cache": target_paths["thimble"],
                "A219_chain_coefficient": BOUNDARY,
                "generic_source": Path(__file__).resolve(),
            }.items()
        },
        "strict_scope": {
            "observed_SM_values_used": False,
            "target_node_interval_Newton_closed": True,
            "all_eight_main_rows_interval_closed": True,
            "all_eight_tail_rows_interval_closed": True,
            "orientation_splice_closed": True,
            "full_period_vector_interval_closed": True,
            "selected_chain_contribution_interval_closed": True,
            "floating_values_used_as_bounds": False,
            "rank3_selected_chain_recomposition_closed": False,
            "interval_Jacobian_certificate": False,
            "covariant_zero_proved": False,
        },
        "next_required_artifact": (
            "certify the remaining A219-ranked target rows, recompose the "
            "selected chain, and enclose the complex Jacobian"
        ),
    }
    dump(target_paths["full"], payload)
    note = (
        ROOT
        / "proof_corpus"
        / f"MTT_q79HeightFourD{arguments.index:03d}RefinedFullResidueInterval_"
        f"{arguments.artifact}_v1.md"
    )
    note.write_text(
        f"# MTT q79 Height-Four d{arguments.index:03d} Refined Full-Residue "
        f"Interval ({arguments.artifact}) v1\n\n"
        "The target-parametric all-eight pipeline certifies the node, main "
        "transport, local tail, orientation, and selected-chain multiplier "
        "from the same n3/A219 authorities.\n\n"
        f"The maximum full-row radius is `{np.max(full_radii):.12g}`. After "
        f"the signed chain coefficient `{coefficient}`, the product-disk L2 "
        f"radius is `{np.linalg.norm(chain_radii):.12g}`. The independent "
        "floating cache lies inside all eight intervals and was not used as "
        "an error bound.\n\n"
        "This closes one selected-chain contribution. It does not close the "
        "remaining chain, the interval Jacobian, the covariant zero, or full "
        "SM closure.\n",
        encoding="utf-8",
    )
    print(f"wrote {relative(target_paths['full'])}", flush=True)
    print(f"wrote {relative(note)}", flush=True)
    print(json.dumps(payload["summary"], indent=2), flush=True)
    return payload


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--index", type=int, required=True)
    parser.add_argument("--artifact", default="A226")
    parser.add_argument("--phase", choices=("main", "tail", "full", "all"), default="all")
    parser.add_argument("--epsilon", type=float, default=1.0e-5)
    parser.add_argument("--node-iterations", type=int, default=3)
    parser.add_argument("--main-dps", type=int, default=70)
    parser.add_argument("--order", type=int, default=16)
    parser.add_argument("--maximum-step", type=float, default=0.006)
    parser.add_argument("--minimum-step", type=float, default=1.0e-12)
    parser.add_argument("--maximum-lift-correction", type=float, default=1.0e-10)
    parser.add_argument("--maximum-integral-radius", type=float, default=1.0e-4)
    parser.add_argument("--cut-segments", type=int, default=32)
    parser.add_argument("--cut-tolerance", type=float, default=1.0e-40)
    parser.add_argument("--tail-dps", type=int, default=100)
    parser.add_argument("--node-width", type=float, default=1.0e-10)
    parser.add_argument("--outer-segments", type=int, default=9600)
    parser.add_argument("--theta-segments", type=int, default=32)
    parser.add_argument("--factor-order", type=int, default=32)
    parser.add_argument("--cooling-pause-every", type=int, default=10)
    parser.add_argument("--cooling-pause-seconds", type=float, default=2.0)
    arguments = parser.parse_args()
    if not 1 <= arguments.index <= 90:
        raise ValueError("index must lie in [1,90]")
    if not 0.0 < arguments.node_width < arguments.epsilon < 0.01:
        raise ValueError("require 0 < node width < epsilon < 0.01")
    if arguments.cooling_pause_every < 0 or arguments.cooling_pause_seconds < 0.0:
        raise ValueError("cooling pause controls must be nonnegative")
    priority_lowered = set_below_normal_priority()
    print(
        f"process below-normal priority applied={priority_lowered}; "
        f"checkpoint cooling={arguments.cooling_pause_seconds}s/"
        f"{arguments.cooling_pause_every} accepted steps",
        flush=True,
    )
    if arguments.phase in {"main", "all"}:
        execute_main(arguments)
    if arguments.phase in {"tail", "all"}:
        execute_tail(arguments)
    if arguments.phase in {"full", "all"}:
        execute_full(arguments)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
