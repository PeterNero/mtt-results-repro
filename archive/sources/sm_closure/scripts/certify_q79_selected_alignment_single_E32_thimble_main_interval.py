from __future__ import annotations

import argparse
import hashlib
import json
import math
from dataclasses import dataclass
from pathlib import Path

import numpy as np
from flint import acb, acb_mat, acb_poly, arb, ctx

import certify_q79_selected_alignment_E32_handle_combination_interval as handle
import certify_q79_selected_side_beta_defect_transport as validated
from q79genus2_period_transport import FORM_NAMES


ROOT = Path(__file__).resolve().parents[1]
DIRECTORY = (
    ROOT
    / "candidate_data"
    / "selected_q79covariantperiodbranchcutsetandtightbetatransport"
)
PERIOD_DIRECTORY = DIRECTORY / "selected_alignment_thimble_periods"
FAN = DIRECTORY / "selected_alignment_distinguished_radial_fan.interval.packet.json"
DEFAULT_INDEX = 4


def load(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def dump(path: Path, value: dict) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(value, indent=2, sort_keys=True) + "\n", encoding="utf-8")


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def relative(path: Path) -> str:
    return str(path.relative_to(ROOT)).replace("\\", "/")


def candidate_path(index: int) -> Path:
    matches = list(PERIOD_DIRECTORY.glob(f"d{index:03d}_*.thimble_period.candidate.json"))
    if len(matches) != 1:
        raise FileNotFoundError(f"expected one floating thimble candidate for d{index:03d}")
    return matches[0]


def closest_pair(roots: list[acb]) -> tuple[tuple[int, int], dict]:
    rows = []
    for left in range(len(roots)):
        for right in range(left + 1, len(roots)):
            rows.append(
                (
                    validated.upper(abs(roots[left] - roots[right])),
                    validated.lower(abs(roots[left] - roots[right])),
                    left,
                    right,
                )
            )
    rows.sort()
    selected = rows[0]
    second = rows[1]
    if selected[0] >= second[1]:
        raise AssertionError("near-node colliding root pair is not interval-separated")
    minimum_root_ball_separation = min(
        validated.lower(abs(roots[left] - roots[right]))
        for left in range(len(roots))
        for right in range(left)
    )
    if minimum_root_ball_separation <= 0:
        raise AssertionError("near-node root balls overlap")
    return (selected[2], selected[3]), {
        "selected_pair_distance_lower": selected[1],
        "selected_pair_distance_upper": selected[0],
        "second_pair_distance_lower": second[1],
        "second_to_selected_distance_ratio_lower": second[1] / selected[0],
        "minimum_root_ball_separation_lower": minimum_root_ball_separation,
    }


def roots_at(
    system: validated.SelectedQ79IntervalSystem, parameter: complex
) -> tuple[list[acb], acb]:
    _a, _b, line, line_derivative = system.ab_line_data(
        acb(format(parameter.real, ".17g"), format(parameter.imag, ".17g"))
    )
    coefficients, _derivative = validated.aligned_coefficients_and_derivative(
        system.evaluator.tables["F6"],
        line,
        line_derivative,
        chart=system.line_chart,
    )
    roots = acb_poly(coefficients).roots(tol=1e-55, maxprec=8192)
    if len(roots) != 6:
        raise AssertionError("near-node selected sextic root isolation failed")
    return roots, coefficients[6]


def homogeneous_builder(
    original,
    system: validated.SelectedQ79IntervalSystem,
    start: complex,
    direction: complex,
    step: float,
    order: int,
):
    matrix, forcing, diagnostics = original(system, start, direction, step, order)
    zero = forcing[0].constant(0, forcing[0].order, forcing[0].radius)
    e32_index = FORM_NAMES.index("E32")
    for residue_index in range(8):
        if residue_index == e32_index:
            continue
        for column in range(13):
            matrix[5 + residue_index][column] = zero
    return matrix, [zero for _ in forcing], diagnostics


@dataclass
class E32LiftErrorFrame:
    fundamental: acb_mat
    coordinate_radii: list[arb]

    def physical_generator_matrix(self) -> acb_mat:
        dimension = len(self.coordinate_radii)
        if self.fundamental.nrows() != dimension or self.fundamental.ncols() != dimension:
            raise ValueError("E32 lift frame dimension mismatch")
        diagonal = acb_mat(dimension, dimension)
        for index, radius in enumerate(self.coordinate_radii):
            diagonal[index, index] = acb(radius)
        return self.fundamental * diagonal

    def physical_radius(self) -> arb:
        return validated.acb_matrix_infinity_norm(self.physical_generator_matrix())


def e32_candidate_flow_polynomials(
    matrix: list[list[validated.TaylorModel]],
    forcing: list[validated.TaylorModel],
    initial_center: list[acb],
) -> tuple[list[validated.TaylorModel], list[list[validated.TaylorModel]]]:
    order = matrix[0][0].order
    radius = matrix[0][0].radius
    dimension = len(matrix)
    matrix_coefficients = validated.tm_matrix_coefficients(matrix)
    forcing_coefficients = [
        validated.acb_column([value.coefficients[degree] for value in forcing])
        for degree in range(order + 1)
    ]
    state_coefficients = [validated.acb_column(initial_center)]
    fundamental_coefficients = [acb_mat(dimension, dimension)]
    for index in range(dimension):
        fundamental_coefficients[0][index, index] = acb(1)
    for degree in range(order):
        state_right = forcing_coefficients[degree]
        fundamental_right = acb_mat(dimension, dimension)
        for index in range(degree + 1):
            state_right += matrix_coefficients[index] * state_coefficients[degree - index]
            fundamental_right += (
                matrix_coefficients[index]
                * fundamental_coefficients[degree - index]
            )
        state_coefficients.append(state_right / acb(degree + 1))
        fundamental_coefficients.append(fundamental_right / acb(degree + 1))
    state = [
        validated.TaylorModel(
            [state_coefficients[degree][row, 0] for degree in range(order + 1)],
            radius,
        ).midpoint_polynomial()
        for row in range(dimension)
    ]
    fundamental = [
        [
            validated.TaylorModel(
                [
                    fundamental_coefficients[degree][row, column]
                    for degree in range(order + 1)
                ],
                radius,
            ).midpoint_polynomial()
            for column in range(dimension)
        ]
        for row in range(dimension)
    ]
    return state, fundamental


def validated_e32_flow_step(
    system: validated.SelectedQ79IntervalSystem,
    start: complex,
    direction: complex,
    step: float,
    center: list[acb],
    input_frame: E32LiftErrorFrame,
    *,
    order: int,
) -> tuple[list[acb], E32LiftErrorFrame, dict]:
    full_matrix, forcing, system_diagnostics = validated.build_taylor_system(
        system, start, direction, step, order
    )
    e32_state_index = 5 + FORM_NAMES.index("E32")
    selected = [0, 1, 2, 3, 4, e32_state_index]
    matrix = [
        [full_matrix[row][column] for column in selected] for row in selected
    ]
    zero = forcing[0].constant(0, forcing[0].order, forcing[0].radius)
    homogeneous_forcing = [zero for _ in range(6)]
    state, fundamental = e32_candidate_flow_polynomials(
        matrix, homogeneous_forcing, center
    )
    state_residual = [
        value - validated.tm_vector_derivative(state)[index]
        for index, value in enumerate(
            validated.tm_matrix_vector_multiply(matrix, state)
        )
    ]
    fundamental_residual = validated.tm_matrix_subtract(
        validated.tm_matrix_multiply(matrix, fundamental),
        validated.tm_matrix_derivative(fundamental),
    )
    inverse_norm, inverse_defect = validated.tm_verified_inverse_bound(fundamental)
    linear_defect = (
        inverse_norm * validated.tm_matrix_infinity_norm(fundamental_residual)
    )
    affine_defect = inverse_norm * validated.tm_vector_infinity_norm(state_residual)
    step_ball = arb(format(step, ".17g"))
    growth = (linear_defect * step_ball).exp()
    forced_error = (
        affine_defect * step_ball
        if validated.upper(linear_defect) == 0
        else affine_defect * (growth - arb(1)) / linear_defect
    )
    input_radius = input_frame.physical_radius()
    transformed_error = growth * input_radius + forced_error
    transformed_correction = (growth - arb(1)) * input_radius + forced_error

    endpoint = arb(format(step, ".17g"))
    endpoint_state = [value.evaluate_polynomial(endpoint) for value in state]
    endpoint_fundamental = acb_mat(
        [
            [
                fundamental[row][column].evaluate_polynomial(endpoint)
                for column in range(6)
            ]
            for row in range(6)
        ]
    )
    output_fundamental = endpoint_fundamental * input_frame.fundamental
    output_inverse = output_fundamental.inv()
    correction_pullback = output_inverse * endpoint_fundamental
    polynomial_radius = arb(
        str(max(validated.radius_upper(value) for value in endpoint_state))
    )
    correction_upper = validated.upper(transformed_correction)
    rounding_upper = validated.upper(polynomial_radius)
    coordinate_radii = []
    for row in range(6):
        correction_norm = sum(
            (abs(correction_pullback[row, column]) for column in range(6)),
            arb(0),
        )
        rounding_norm = sum(
            (abs(output_inverse[row, column]) for column in range(6)),
            arb(0),
        )
        coordinate_radii.append(
            input_frame.coordinate_radii[row]
            + arb(str(correction_upper)) * correction_norm
            + arb(str(rounding_upper)) * rounding_norm
        )
    output_frame = E32LiftErrorFrame(
        fundamental=output_fundamental,
        coordinate_radii=coordinate_radii,
    )
    generator = output_frame.physical_generator_matrix()
    e32_radius = sum((abs(generator[5, column]) for column in range(6)), arb(0))
    endpoint_center = [
        validated.SelectedQ79IntervalSystem.midpoint_acb(value)
        for value in endpoint_state
    ]
    diagnostics = {
        **system_diagnostics,
        "fundamental_inverse_neumann_norm": inverse_defect,
        "linear_defect_bound": validated.upper(linear_defect),
        "affine_defect_bound": validated.upper(affine_defect),
        "transformed_lift_correction": correction_upper,
        "input_lift_radius": validated.upper(input_radius),
        "output_lift_radius": validated.upper(output_frame.physical_radius()),
        "E32_coordinate_radius_upper": validated.upper(e32_radius),
        "homogeneous_augmented_dimension": 6,
    }
    return endpoint_center, output_frame, diagnostics


def execute_main_interval(
    system: validated.SelectedQ79IntervalSystem,
    initial_periods: list[acb],
    *,
    start: complex,
    endpoint: complex,
    order: int,
    maximum_step: float,
    initial_step: float,
    minimum_step: float,
    maximum_lift_correction: float,
    target_main_radius: float,
    initial_radius_allowance: float,
) -> dict:
    center = [system.midpoint_acb(value) for value in initial_periods] + [acb(0)]
    identity = acb_mat(6, 6)
    for index in range(6):
        identity[index, index] = acb(1)
    lift_frame = E32LiftErrorFrame(
        fundamental=identity,
        coordinate_radii=[value.rad().upper() for value in initial_periods]
        + [arb(0)],
    )
    distance = abs(endpoint - start)
    direction = (endpoint - start) / distance
    position = 0.0
    proposed = min(initial_step, maximum_step, distance)
    accepted: list[dict] = []
    rejected = 0
    minimum_accepted = math.inf
    while position < distance:
            step = min(proposed, distance - position)
            parameter_start = start + direction * position
            try:
                next_center, next_frame, diagnostics = validated_e32_flow_step(
                        system,
                        parameter_start,
                        direction,
                        step,
                        center,
                        lift_frame,
                        order=order,
                )
                if diagnostics["transformed_lift_correction"] > maximum_lift_correction:
                    raise ArithmeticError("thimble lift correction exceeds pilot budget")
                candidate_fraction = min(1.0, (position + step) / distance)
                radius_envelope = initial_radius_allowance + (
                    target_main_radius - initial_radius_allowance
                ) * math.sqrt(candidate_fraction)
                diagnostics["E32_radius_envelope"] = radius_envelope
                if diagnostics["E32_coordinate_radius_upper"] > radius_envelope:
                    raise ArithmeticError(
                        "E32 coordinate radius exceeds the selected global envelope"
                    )
            except (ArithmeticError, ZeroDivisionError, ValueError) as error:
                rejected += 1
                proposed = step / 2
                if rejected % 10 == 0:
                    print(
                        "validated E32 thimble main "
                        f"rejections={rejected} fraction={position / distance:.12g} "
                        f"next_step={proposed:.3e} reason={type(error).__name__}: {error}",
                        flush=True,
                    )
                if proposed < minimum_step:
                    raise
                continue
            center = next_center
            lift_frame = next_frame
            position = min(distance, position + step)
            minimum_accepted = min(minimum_accepted, step)
            accepted.append(
                {
                    "start_arclength": float(position - step),
                    "end_arclength": float(position),
                    "step": float(step),
                    **diagnostics,
                }
            )
            quality = max(
                diagnostics["reduction_neumann_norm"],
                diagnostics["fundamental_inverse_neumann_norm"],
            )
            growth = 1.8 if quality < 0.05 else 1.35
            proposed = min(maximum_step, step * growth)
            if len(accepted) % 5 == 0 or position == distance:
                print(
                    "validated E32 thimble main "
                    f"steps={len(accepted)} fraction={position / distance:.12g} "
                    f"step={step:.3e} "
                    f"radius={diagnostics['E32_coordinate_radius_upper']:.3e}",
                    flush=True,
                )

    generator = lift_frame.physical_generator_matrix()
    integral_radius = sum((abs(generator[5, column]) for column in range(6)), arb(0))

    return {
        "center": [handle.complex_pair(handle.midpoint(value)) for value in center],
        "uniform_integral_radius_upper": validated.upper(integral_radius),
        "certificate_method": "six-dimensional homogeneous augmented fundamental frame",
        "lift_radius_upper": validated.upper(lift_frame.physical_radius()),
        "accepted_step_count": len(accepted),
        "rejected_step_count": rejected,
        "minimum_accepted_step": minimum_accepted,
        "path_length": distance,
        "steps": accepted,
    }


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--distinguished-index", type=int, default=DEFAULT_INDEX)
    parser.add_argument("--epsilon", type=float, default=1.0e-5)
    parser.add_argument("--dps", type=int, default=90)
    parser.add_argument("--cut-segments", type=int, default=24)
    parser.add_argument("--cut-tolerance", type=float, default=1.0e-35)
    parser.add_argument("--order", type=int, default=48)
    parser.add_argument("--maximum-step", type=float, default=0.01)
    parser.add_argument("--minimum-step", type=float, default=1.0e-12)
    parser.add_argument("--maximum-lift-correction", type=float, default=2.0e-7)
    parser.add_argument("--target-main-radius", type=float, default=2.0e-5)
    parser.add_argument("--initial-radius-allowance", type=float, default=5.0e-6)
    parser.add_argument("--output", type=Path)
    arguments = parser.parse_args()
    ctx.dps = arguments.dps
    if not 0 < arguments.epsilon < 0.01:
        raise ValueError("epsilon must lie in (0,0.01)")
    if not 0 <= arguments.initial_radius_allowance < arguments.target_main_radius:
        raise ValueError("radius envelope requires 0 <= initial allowance < target")

    source_path = candidate_path(arguments.distinguished_index)
    source = load(source_path)
    critical = handle.complex_value(source["critical_center"])
    base = 0.25 + 0.25j
    displacement = critical - base
    start_w = base + (1 - arguments.epsilon) * displacement
    start_parameter = -1j * (start_w - base)
    endpoint_parameter = 0 + 0j
    critical_parameter = -1j * displacement
    singular_distance = abs(critical_parameter - start_parameter)
    initial_step = min(arguments.maximum_step, singular_distance / 4)

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
    roots, leading = roots_at(system, start_parameter)
    pair, pair_diagnostics = closest_pair(roots)
    initial_periods, cut_diagnostics = handle.direct_cut_periods(
        roots,
        leading,
        pair,
        segments=arguments.cut_segments,
        tolerance=arguments.cut_tolerance,
    )
    execution = execute_main_interval(
        system,
        initial_periods,
        start=start_parameter,
        endpoint=endpoint_parameter,
        order=arguments.order,
        maximum_step=arguments.maximum_step,
        initial_step=initial_step,
        minimum_step=arguments.minimum_step,
        maximum_lift_correction=arguments.maximum_lift_correction,
        target_main_radius=arguments.target_main_radius,
        initial_radius_allowance=arguments.initial_radius_allowance,
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
    plus = float(np.max(np.abs(base_center - floating_base)))
    minus = float(np.max(np.abs(-base_center - floating_base)))
    orientation_sign = 1 if plus <= minus else -1
    selected_base_difference = min(plus, minus)
    rejected_base_difference = max(plus, minus)
    if rejected_base_difference <= 1000 * max(selected_base_difference, 1.0e-15):
        raise AssertionError("thimble orientation is not separated at the base")

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
    payload = {
        "schema": "MTTQ79SelectedAlignmentSingleE32ThimbleMainInterval.v1",
        "status": "SELECTED_E32_THIMBLE_MAIN_SEGMENT_INTERVAL_CERTIFIED_ENDPOINT_TAIL_OPEN",
        "authority": {
            "floating_candidate": relative(source_path),
            "floating_candidate_sha256": sha256(source_path),
            "distinguished_fan": relative(FAN),
            "distinguished_fan_sha256": sha256(FAN),
            "validated_transport_engine": relative(
                ROOT / "scripts" / "certify_q79_selected_side_beta_defect_transport.py"
            ),
            "validated_transport_engine_sha256": sha256(
                ROOT / "scripts" / "certify_q79_selected_side_beta_defect_transport.py"
            ),
            "builder_source": relative(Path(__file__)),
            "builder_source_sha256": sha256(Path(__file__)),
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
            "reference": "A131 canonically synchronized floating thimble marking",
        },
        "E32_main_segment": {
            "interval_center": handle.complex_pair(main_center),
            "interval_radius_upper": main_radius,
            "A131_full_floating_thimble_value": handle.complex_pair(floating_full),
            "diagnostic_unvalidated_endpoint_tail_center": handle.complex_pair(
                diagnostic_tail
            ),
            "diagnostic_unvalidated_endpoint_tail_absolute_value": abs(
                diagnostic_tail
            ),
        },
        "scope": {
            "observed_SM_values_used": False,
            "near_node_direct_cycle_interval_closed": True,
            "main_homogeneous_Gauss_Manin_segment_interval_closed": True,
            "endpoint_tail_interval_closed": False,
            "full_E32_thimble_interval_closed": False,
            "A131_values_used_as_orientation_and_diagnostic_only": True,
            "floating_tail_difference_promoted_to_error_bound": False,
        },
    }
    dump(output, payload)
    print(f"wrote {relative(output)}")
    print(
        json.dumps(
            {
                "distinguished_index": arguments.distinguished_index,
                "colliding_pair": list(pair),
                "orientation_sign": orientation_sign,
                "main_radius": main_radius,
                "base_center_difference": selected_base_difference,
                "diagnostic_tail_absolute": abs(diagnostic_tail),
                "accepted_steps": execution["accepted_step_count"],
                "rejected_steps": execution["rejected_step_count"],
            },
            indent=2,
        )
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
