from __future__ import annotations

import argparse
import hashlib
import json
import math
from pathlib import Path

import numpy as np
from flint import acb, acb_mat, arb, ctx

import certify_q79_selected_alignment_E32_handle_combination_interval as handle
import certify_q79_selected_alignment_single_E32_thimble_main_interval as pilot
import certify_q79_selected_side_beta_defect_transport as validated
from q79genus2_period_transport import FORM_NAMES


ROOT = Path(__file__).resolve().parents[1]
DIRECTORY = (
    ROOT
    / "candidate_data"
    / "selected_q79covariantperiodbranchcutsetandtightbetatransport"
)
PERIOD_DIRECTORY = DIRECTORY / "selected_alignment_thimble_periods"
DUAL = DIRECTORY / "selected_alignment_dual_discriminant.interval.packet.json"
Z_WALL = DIRECTORY / "selected_alignment_zchart_wall.interval.packet.json"
FAN = DIRECTORY / "selected_alignment_distinguished_radial_fan.interval.packet.json"
ORIENTATION_SYNCHRONIZATION = (
    PERIOD_DIRECTORY / "selected_alignment_thimble_orientation_synchronization.packet.json"
)
BASE = 0.25 + 0.25j
LOW = 0.25
HIGH = 1.25
ROUNDING_GUARD = 1.0e-12


def load(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def dump(path: Path, value: dict) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(value, indent=2, sort_keys=True) + "\n", encoding="utf-8")


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def relative(path: Path) -> str:
    return str(path.relative_to(ROOT)).replace("\\", "/")


def encoded(value: complex) -> dict[str, str]:
    return {
        "real": format(value.real, ".17g"),
        "imaginary": format(value.imag, ".17g"),
    }


def canonical_coordinate(value: float) -> float:
    shift = math.floor(LOW - value) + 1
    lifted = value + shift
    while lifted <= LOW:
        lifted += 1
    while lifted >= HIGH:
        lifted -= 1
    if not LOW < lifted < HIGH:
        raise AssertionError("point misses the selected cut square")
    return lifted


def canonical_lift(value: complex) -> complex:
    return complex(canonical_coordinate(value.real), canonical_coordinate(value.imag))


def segment_distance(start: complex, end: complex, point: complex) -> float:
    direction = end - start
    if direction == 0:
        return abs(point - start)
    parameter = ((point - start).conjugate() * direction).real / abs(direction) ** 2
    parameter = min(1.0, max(0.0, parameter))
    return abs(point - (start + parameter * direction))


def path_clearance(path: list[complex], points: list[tuple[complex, float]]) -> float:
    return min(
        segment_distance(start, end, point + complex(horizontal, vertical)) - radius
        for start, end in zip(path, path[1:])
        for point, radius in points
        for horizontal in range(-2, 3)
        for vertical in range(-2, 3)
    ) - ROUNDING_GUARD


def pole_clearance(path: list[complex]) -> float:
    return min(
        segment_distance(start, end, complex(horizontal, vertical))
        for start, end in zip(path, path[1:])
        for horizontal in range(-1, 3)
        for vertical in range(-1, 3)
    ) - ROUNDING_GUARD


def winding_number(path: list[complex], point: complex) -> tuple[int, float]:
    total = 0.0
    for start, end in zip(path, path[1:]):
        left = start - point
        right = end - point
        if left == 0 or right == 0:
            raise ZeroDivisionError("homotopy boundary meets an excluded point")
        total += math.atan2(
            left.real * right.imag - left.imag * right.real,
            (left.conjugate() * right).real,
        )
    value = total / (2 * math.pi)
    integer = round(value)
    return integer, abs(value - integer)


def source_points(dual: dict, key: str) -> list[tuple[str, complex, float]]:
    rows = []
    for index, point in enumerate(dual[key]["points"]):
        lift = point["canonical_uniformizing_lift"]
        principal = complex(float(lift["real"]), float(lift["imaginary"]))
        rows.append(
            (
                point.get("root_id", point.get("chart_zero_id", f"point_{index}")),
                canonical_lift(principal),
                float(lift["radius_upper"]),
            )
        )
    return rows


def build_detour(
    target: complex,
    *,
    epsilon: float,
    detour_fraction: float,
    detour_offset: float,
    return_fraction: float,
) -> tuple[list[complex], dict]:
    displacement = target - BASE
    unit_right = complex(displacement.imag, -displacement.real) / abs(displacement)
    cutoff = BASE + (1 - epsilon) * displacement
    detour = BASE + detour_fraction * displacement + detour_offset * unit_right
    return_point = BASE + return_fraction * displacement
    path = [BASE, detour, return_point, cutoff]
    return path, {
        "detour_fraction": detour_fraction,
        "detour_signed_right_offset": detour_offset,
        "return_fraction": return_fraction,
        "points_in_base_to_node_order": [encoded(point) for point in path],
    }


def certify_detour(
    path: list[complex],
    dual: dict,
    selected_root: str,
    *,
    line_chart: str = "y",
    z_wall: dict | None = None,
) -> dict:
    if line_chart not in {"y", "z"}:
        raise ValueError("selected line chart must be y or z")
    critical_rows = source_points(dual, "critical_points_on_E")
    chart_source = dual if line_chart == "y" else z_wall
    if chart_source is None:
        raise ValueError("z-chart detour certification requires the z-wall packet")
    chart_key = f"selected_{line_chart}_line_chart_zeros"
    chart_rows = source_points(chart_source, chart_key)
    other_critical = [
        (center, radius)
        for root_id, center, radius in critical_rows
        if root_id != selected_root
    ]
    chart_points = [(center, radius) for _name, center, radius in chart_rows]
    closed = path + [BASE]
    maximum_winding_residual = 0.0
    nonzero_critical_windings = []
    for root_id, center, _radius in critical_rows:
        for horizontal in range(-2, 3):
            for vertical in range(-2, 3):
                integer, residual = winding_number(
                    closed, center + complex(horizontal, vertical)
                )
                maximum_winding_residual = max(maximum_winding_residual, residual)
                if integer != 0:
                    nonzero_critical_windings.append(
                        [root_id, horizontal, vertical, integer]
                    )
    nonzero_chart_windings = []
    for name, center, _radius in chart_rows:
        for horizontal in range(-2, 3):
            for vertical in range(-2, 3):
                integer, residual = winding_number(
                    closed, center + complex(horizontal, vertical)
                )
                maximum_winding_residual = max(maximum_winding_residual, residual)
                if integer != 0:
                    nonzero_chart_windings.append([name, horizontal, vertical, integer])
    nonzero_pole_windings = []
    for horizontal in range(-1, 3):
        for vertical in range(-1, 3):
            integer, residual = winding_number(
                closed, complex(horizontal, vertical)
            )
            maximum_winding_residual = max(maximum_winding_residual, residual)
            if integer != 0:
                nonzero_pole_windings.append([horizontal, vertical, integer])
    if nonzero_critical_windings or nonzero_chart_windings or nonzero_pole_windings:
        raise AssertionError("detour is not null-homotopic relative to the radial path")
    if maximum_winding_residual >= 1.0e-10:
        raise AssertionError("detour winding computation is not numerically separated")
    result = {
        "other_critical_ball_clearance_lower": path_clearance(path, other_critical),
        f"selected_{line_chart}_chart_zero_clearance_lower": path_clearance(
            path, chart_points
        ),
        "elliptic_infinity_clearance_lower": pole_clearance(path),
        "critical_winding_vector_is_zero": True,
        "chart_zero_winding_vector_is_zero": True,
        "elliptic_pole_winding_vector_is_zero": True,
        "maximum_integer_winding_residual": maximum_winding_residual,
        "relative_homotopy_class_equals_original_radial_path": True,
    }
    if min(
        result["other_critical_ball_clearance_lower"],
        result[f"selected_{line_chart}_chart_zero_clearance_lower"],
        result["elliptic_infinity_clearance_lower"],
    ) <= 0:
        raise AssertionError("detour misses the selected regular domain")
    return result


def execute_polyline(
    system: validated.SelectedQ79IntervalSystem,
    initial_periods: list[acb],
    parameters: list[complex],
    *,
    critical_parameter: complex,
    order: int,
    maximum_step: float,
    minimum_step: float,
    maximum_lift_correction: float,
    target_main_radius: float,
) -> dict:
    center = [system.midpoint_acb(value) for value in initial_periods] + [acb(0)]
    identity = acb_mat(6, 6)
    for index in range(6):
        identity[index, index] = acb(1)
    frame = pilot.E32LiftErrorFrame(
        fundamental=identity,
        coordinate_radii=[value.rad().upper() for value in initial_periods] + [arb(0)],
    )
    lengths = [abs(end - start) for start, end in zip(parameters, parameters[1:])]
    total_length = sum(lengths)
    covered = 0.0
    accepted = []
    rejected = 0
    minimum_accepted = math.inf
    proposed = min(maximum_step, abs(critical_parameter - parameters[0]) / 4)
    for segment_index, (start, endpoint, distance) in enumerate(
        zip(parameters, parameters[1:], lengths)
    ):
        direction = (endpoint - start) / distance
        position = 0.0
        if segment_index:
            proposed = min(proposed, maximum_step / 4)
        while position < distance:
            step = min(proposed, distance - position)
            parameter_start = start + direction * position
            try:
                next_center, next_frame, diagnostics = pilot.validated_e32_flow_step(
                    system,
                    parameter_start,
                    direction,
                    step,
                    center,
                    frame,
                    order=order,
                )
                if diagnostics["transformed_lift_correction"] > maximum_lift_correction:
                    raise ArithmeticError("E32 lift correction exceeds local budget")
                fraction = min(1.0, (covered + position + step) / total_length)
                diagnostics["completed_path_fraction"] = fraction
                diagnostics["E32_final_radius_cap"] = target_main_radius
            except (ArithmeticError, ZeroDivisionError, ValueError) as error:
                rejected += 1
                proposed = step / 2
                if rejected % 10 == 0:
                    print(
                        "validated polygonal E32 main "
                        f"rejections={rejected} segment={segment_index + 1}/3 "
                        f"fraction={(covered + position) / total_length:.12g} "
                        f"next_step={proposed:.3e} reason={type(error).__name__}: {error}",
                        flush=True,
                    )
                if proposed < minimum_step:
                    raise
                continue
            center = next_center
            frame = next_frame
            position = min(distance, position + step)
            minimum_accepted = min(minimum_accepted, step)
            accepted.append(
                {
                    "segment_index": segment_index,
                    "start_arclength": covered + position - step,
                    "end_arclength": covered + position,
                    "step": step,
                    **diagnostics,
                }
            )
            quality = (
                diagnostics["transformed_lift_correction"]
                / maximum_lift_correction
            )
            proposed = min(maximum_step, step * (1.8 if quality < 0.05 else 1.35))
            if len(accepted) % 10 == 0 or position == distance:
                print(
                    "validated polygonal E32 main "
                    f"steps={len(accepted)} segment={segment_index + 1}/3 "
                    f"fraction={(covered + position) / total_length:.12g} "
                    f"radius={diagnostics['E32_coordinate_radius_upper']:.3e}",
                    flush=True,
                )
        covered += distance
    generator = frame.physical_generator_matrix()
    integral_radius = sum((abs(generator[5, column]) for column in range(6)), arb(0))
    if validated.upper(integral_radius) > target_main_radius:
        raise ArithmeticError(
            "final polygonal E32 radius exceeds the selected main-segment cap"
        )
    return {
        "center": [handle.complex_pair(handle.midpoint(value)) for value in center],
        "uniform_integral_radius_upper": validated.upper(integral_radius),
        "certificate_method": "six-dimensional augmented frame on a certified polygonal homotopy",
        "lift_radius_upper": validated.upper(frame.physical_radius()),
        "accepted_step_count": len(accepted),
        "rejected_step_count": rejected,
        "minimum_accepted_step": minimum_accepted,
        "path_length": total_length,
        "segment_lengths": lengths,
        "steps": accepted,
    }


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--distinguished-index", type=int, default=47)
    parser.add_argument("--epsilon", type=float, default=1.0e-5)
    parser.add_argument("--dps", type=int, default=90)
    parser.add_argument("--cut-segments", type=int, default=24)
    parser.add_argument("--cut-tolerance", type=float, default=1.0e-35)
    parser.add_argument("--order", type=int, default=48)
    parser.add_argument("--maximum-step", type=float, default=0.01)
    parser.add_argument("--minimum-step", type=float, default=1.0e-12)
    parser.add_argument("--maximum-lift-correction", type=float, default=1.0e-8)
    parser.add_argument("--target-main-radius", type=float, default=1.9e-5)
    parser.add_argument("--detour-fraction", type=float, default=0.385)
    parser.add_argument("--detour-offset", type=float, default=0.03)
    parser.add_argument("--return-fraction", type=float, default=0.7)
    parser.add_argument("--output", type=Path)
    arguments = parser.parse_args()
    ctx.dps = arguments.dps
    if not 0 < arguments.epsilon < 0.01:
        raise ValueError("epsilon must lie in (0,0.01)")
    if not 0 < arguments.detour_fraction < arguments.return_fraction < 1:
        raise ValueError("detour fractions are not ordered")
    if arguments.target_main_radius <= 0:
        raise ValueError("final main-segment radius cap must be positive")

    source_path = pilot.candidate_path(arguments.distinguished_index)
    source = load(source_path)
    critical = handle.complex_value(source["critical_center"])
    path_w, path_design = build_detour(
        critical,
        epsilon=arguments.epsilon,
        detour_fraction=arguments.detour_fraction,
        detour_offset=arguments.detour_offset,
        return_fraction=arguments.return_fraction,
    )
    dual = load(DUAL)
    z_wall = load(Z_WALL) if source["line_chart"] == "z" else None
    geometry = certify_detour(
        path_w,
        dual,
        source["root_id"],
        line_chart=source["line_chart"],
        z_wall=z_wall,
    )
    parameters = [-1j * (point - BASE) for point in reversed(path_w)]
    critical_parameter = -1j * (critical - BASE)

    fan = load(FAN)
    fan_rows = [
        row
        for row in fan["distinguished_positive_meridians"]
        if int(row["distinguished_index"]) == arguments.distinguished_index
    ]
    if len(fan_rows) != 1 or fan_rows[0]["root_id"] != source["root_id"]:
        raise AssertionError("distinguished fan row mismatch")

    system = validated.SelectedQ79IntervalSystem(
        dps=arguments.dps, line_chart=source["line_chart"]
    )
    roots, leading = pilot.roots_at(system, parameters[0])
    pair, pair_diagnostics = pilot.closest_pair(roots)
    initial_periods, cut_diagnostics = handle.direct_cut_periods(
        roots,
        leading,
        pair,
        segments=arguments.cut_segments,
        tolerance=arguments.cut_tolerance,
    )
    execution = execute_polyline(
        system,
        initial_periods,
        parameters,
        critical_parameter=critical_parameter,
        order=arguments.order,
        maximum_step=arguments.maximum_step,
        minimum_step=arguments.minimum_step,
        maximum_lift_correction=arguments.maximum_lift_correction,
        target_main_radius=arguments.target_main_radius,
    )

    base_center = np.asarray(
        [handle.complex_value(value) for value in execution["center"][:5]],
        dtype=np.complex128,
    )
    floating_base = np.asarray(
        [
            handle.complex_value(row["value"])
            for row in source["execution"]["base_fiber_propagated_periods"]
        ],
        dtype=np.complex128,
    )
    orientation_source = load(ORIENTATION_SYNCHRONIZATION)
    orientation_scope = orientation_source["strict_scope"]
    compact_count = int(
        orientation_scope["compact_H1_holomorphic_rows_used_for_orientation"]
    )
    if compact_count != 2:
        raise AssertionError("selected compact-H1 orientation rank changed")
    if orientation_scope["higher_meromorphic_rows_used_for_orientation"] != 0:
        raise AssertionError("puncture-lift rows entered the orientation gate")
    if not orientation_scope[
        "higher_meromorphic_rows_retain_puncture_lift_dependence"
    ]:
        raise AssertionError("puncture-lift dependence theorem is missing")
    compact_center = base_center[:compact_count]
    compact_floating = floating_base[:compact_count]
    plus = float(np.max(np.abs(compact_center - compact_floating)))
    minus = float(np.max(np.abs(-compact_center - compact_floating)))
    orientation_sign = 1 if plus <= minus else -1
    selected_base_difference = min(plus, minus)
    rejected_base_difference = max(plus, minus)
    if rejected_base_difference <= 1000 * max(selected_base_difference, 1.0e-15):
        raise AssertionError("compact-H1 thimble orientation is not separated at the base")
    signed_base_center = orientation_sign * base_center
    full_five_period_difference = float(
        np.max(np.abs(signed_base_center - floating_base))
    )
    opposite_full_five_period_difference = float(
        np.max(np.abs(-signed_base_center - floating_base))
    )
    higher_meromorphic_difference = float(
        np.max(
            np.abs(
                signed_base_center[compact_count:] - floating_base[compact_count:]
            )
        )
    )

    e32_index = FORM_NAMES.index("E32")
    transported_integral = handle.complex_value(execution["center"][5])
    main_center = -orientation_sign * transported_integral
    main_radius = float(execution["uniform_integral_radius_upper"])
    floating_full = handle.complex_value(source["execution"]["period_values"][e32_index])
    diagnostic_tail = floating_full - main_center

    output = arguments.output
    if output is None:
        output = PERIOD_DIRECTORY / (
            f"d{arguments.distinguished_index:03d}_{source['root_id']}.E32_main.interval.packet.json"
        )
    elif not output.is_absolute():
        output = ROOT / output
    engine = ROOT / "scripts" / "certify_q79_selected_side_beta_defect_transport.py"
    payload = {
        "schema": "MTTQ79SelectedAlignmentSingleE32ThimbleMainInterval.v1",
        "status": "SELECTED_E32_THIMBLE_POLYGONAL_MAIN_INTERVAL_CERTIFIED_ENDPOINT_TAIL_OPEN",
        "authority": {
            "floating_candidate": relative(source_path),
            "floating_candidate_sha256": sha256(source_path),
            "distinguished_fan": relative(FAN),
            "distinguished_fan_sha256": sha256(FAN),
            "dual_discriminant": relative(DUAL),
            "dual_discriminant_sha256": sha256(DUAL),
            "z_chart_wall": (
                relative(Z_WALL) if source["line_chart"] == "z" else None
            ),
            "z_chart_wall_sha256": (
                sha256(Z_WALL) if source["line_chart"] == "z" else None
            ),
            "validated_transport_engine": relative(engine),
            "validated_transport_engine_sha256": sha256(engine),
            "A136_augmented_frame_source": relative(Path(pilot.__file__)),
            "A136_augmented_frame_source_sha256": sha256(Path(pilot.__file__)),
            "builder_source": relative(Path(__file__)),
            "builder_source_sha256": sha256(Path(__file__)),
            "orientation_synchronization": relative(ORIENTATION_SYNCHRONIZATION),
            "orientation_synchronization_sha256": sha256(
                ORIENTATION_SYNCHRONIZATION
            ),
        },
        "selected_thimble": {
            "distinguished_index": arguments.distinguished_index,
            "root_id": source["root_id"],
            "line_chart": source["line_chart"],
            "critical_center": source["critical_center"],
            "critical_ball_radius_upper": float(fan_rows[0]["target_ball_radius_upper"]),
            "endpoint_cutoff_epsilon": arguments.epsilon,
            "near_node_colliding_pair_zero_based": list(pair),
            **pair_diagnostics,
        },
        "polygonal_homotopy": {**path_design, **geometry},
        "near_node_direct_cycle_interval": {
            **cut_diagnostics,
            "initial_period_intervals": [
                handle.complex_interval(value) for value in initial_periods
            ],
        },
        "validated_main_transport": execution,
        "orientation": {
            "selected_sign": orientation_sign,
            "selected_base_center_maximum_difference": selected_base_difference,
            "opposite_base_center_maximum_difference": rejected_base_difference,
            "compact_H1_holomorphic_component_count": compact_count,
            "selection_basis": "compact H1 holomorphic periods only",
            "full_five_period_selected_sign_difference_diagnostic": full_five_period_difference,
            "full_five_period_opposite_sign_difference_diagnostic": opposite_full_five_period_difference,
            "higher_meromorphic_puncture_lift_difference_diagnostic": higher_meromorphic_difference,
            "higher_meromorphic_rows_used_for_orientation": False,
            "reference": "A130/A131 synchronized compact-H1 marking plus certified relative homotopy",
        },
        "E32_main_segment": {
            "interval_center": handle.complex_pair(main_center),
            "interval_radius_upper": main_radius,
            "A131_full_floating_thimble_value": handle.complex_pair(floating_full),
            "diagnostic_unvalidated_endpoint_tail_center": handle.complex_pair(
                diagnostic_tail
            ),
            "diagnostic_unvalidated_endpoint_tail_absolute_value": abs(diagnostic_tail),
        },
        "scope": {
            "observed_SM_values_used": False,
            "relative_homotopy_to_distinguished_radial_path_closed": True,
            "near_node_direct_cycle_interval_closed": True,
            "main_homogeneous_Gauss_Manin_segment_interval_closed": True,
            "endpoint_tail_interval_closed": False,
            "full_E32_thimble_interval_closed": False,
            "A131_values_used_as_orientation_and_diagnostic_only": True,
            "compact_H1_orientation_synchronization_consumed": True,
            "higher_meromorphic_puncture_lift_rows_excluded_from_orientation": True,
            "A123_projective_line_chart_covariance_consumed": (
                source["line_chart"] == "z"
            ),
            "floating_tail_difference_promoted_to_error_bound": False,
        },
    }
    dump(output, payload)
    print(f"wrote {relative(output)}")
    print(
        json.dumps(
            {
                "distinguished_index": arguments.distinguished_index,
                "main_radius": main_radius,
                "base_center_difference": selected_base_difference,
                "other_critical_clearance": geometry[
                    "other_critical_ball_clearance_lower"
                ],
                "accepted_steps": execution["accepted_step_count"],
                "rejected_steps": execution["rejected_step_count"],
            },
            indent=2,
        )
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
