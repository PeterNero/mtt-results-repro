from __future__ import annotations

import argparse
import hashlib
import json
import math
import time
from dataclasses import asdict
from pathlib import Path

import numpy as np
from flint import acb, acb_mat, arb, ctx

import certify_q79_selected_alignment_E32_handle_combination_interval as handle
import certify_q79_selected_alignment_single_E32_thimble_main_interval as pilot
import certify_q79_selected_alignment_single_E32_thimble_nodal_factor as nodal
import certify_q79_selected_side_beta_defect_transport as validated


ROOT = Path(__file__).resolve().parents[1]
PROBE_DIRECTORY = (
    ROOT
    / "candidate_data"
    / "selected_q79covariantperiodbranchcutsetandtightbetatransport"
    / "selected_alignment_thimble_periods"
    / "covariant_floating_probe"
)
TRIAL = PROBE_DIRECTORY / "cplx" / "n3ud" / "probe.packet.json"
FIBRATION = PROBE_DIRECTORY / "cplx" / "n3ud" / "fy.packet.json"
THIMBLE = PROBE_DIRECTORY / "cplx" / "n3ud" / "thimbles" / "t087.json"
OUTPUT = (
    PROBE_DIRECTORY
    / "validated_transport"
    / "d087.n3.main8.interval.json"
)
NODE_OUTPUT = (
    PROBE_DIRECTORY
    / "validated_transport"
    / "d087_selected_085.n3.node.interval.packet.json"
)
NOTE = ROOT / "proof_corpus" / "MTT_q79HeightFourD087FullResidueMainInterval_A220_v1.md"


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


def exact_target_system(dps: int) -> validated.SelectedQ79IntervalSystem:
    packet = load(FIBRATION)
    if packet["source"]["line_chart"] != "y":
        raise AssertionError("A220 expects the n3 y-chart fibration")
    print("loaded n3 y-chart fibration packet", flush=True)
    system = validated.SelectedQ79IntervalSystem(dps=dps, line_chart="y")
    print("constructed selected q79 interval system", flush=True)
    system.alignment = validated.decoded_matrix(
        packet["source"]["alignment_interval"]
    )
    system.alignment_0 = system.alignment
    system.diagnostics = validated.IntervalSystemDiagnostics()
    if validated.lower(abs(system.alignment.det())) <= 0:
        raise AssertionError("target alignment determinant contains zero")
    return system


def fast_certify_node(
    system: validated.SelectedQ79IntervalSystem,
    critical: complex,
    *,
    epsilon: float,
    iterations: int,
) -> tuple[acb, acb, dict]:
    base = 0.25 + 0.25j
    critical_parameter = -1j * (critical - base)
    start_parameter = (1.0 - epsilon) * critical_parameter
    coefficients, _derivative = nodal.fiber_coefficients(
        system,
        acb(
            format(start_parameter.real, ".17g"),
            format(start_parameter.imag, ".17g"),
        ),
    )
    midpoint_coefficients = np.asarray(
        [
            complex(float(value.real.mid()), float(value.imag.mid()))
            for value in coefficients
        ],
        dtype=np.complex128,
    )
    roots = np.roots(midpoint_coefficients[::-1])
    distances = sorted(
        (abs(roots[left] - roots[right]), left, right)
        for left in range(6)
        for right in range(left)
    )
    pair = (distances[0][1], distances[0][2])
    if distances[0][0] >= 0.5 * distances[1][0]:
        raise AssertionError("midpoint colliding-pair seed is not separated")
    root_seed = (roots[pair[0]] + roots[pair[1]]) / 2.0
    parameter_center = acb(
        format(critical_parameter.real, ".17g"),
        format(critical_parameter.imag, ".17g"),
    )
    root_center = acb(
        format(root_seed.real, ".17g"), format(root_seed.imag, ".17g")
    )
    point_rows = []
    for iteration in range(7):
        values, jacobian, diagnostics = nodal.node_equations_and_jacobian(
            system, parameter_center, root_center
        )
        correction = jacobian.solve(acb_mat([[values[0]], [values[1]]]))
        parameter_center -= correction[0, 0]
        root_center -= correction[1, 0]
        point_rows.append(
            {
                "iteration": iteration + 1,
                "parameter_correction_absolute_upper": validated.upper(
                    abs(correction[0, 0])
                ),
                "root_correction_absolute_upper": validated.upper(
                    abs(correction[1, 0])
                ),
                **diagnostics,
            }
        )
    parameter_box = nodal.inflated(parameter_center, factor=4.0, floor=1.0e-24)
    root_box = nodal.inflated(root_center, factor=4.0, floor=1.0e-24)
    interval_rows = []
    for iteration in range(iterations):
        parameter_midpoint = nodal.midpoint(parameter_box)
        root_midpoint = nodal.midpoint(root_box)
        midpoint_values, _midpoint_jacobian, _ = (
            nodal.node_equations_and_jacobian(
                system, parameter_midpoint, root_midpoint
            )
        )
        _box_values, box_jacobian, diagnostics = (
            nodal.node_equations_and_jacobian(system, parameter_box, root_box)
        )
        correction = system.verified_solve(
            box_jacobian,
            acb_mat([[midpoint_values[0]], [midpoint_values[1]]]),
        )
        new_parameter = parameter_midpoint - correction[0, 0]
        new_root = root_midpoint - correction[1, 0]
        parameter_interior = parameter_box.contains_interior(new_parameter)
        root_interior = root_box.contains_interior(new_root)
        interval_rows.append(
            {
                "iteration": iteration + 1,
                "parameter_radius_before": validated.radius_upper(parameter_box),
                "root_radius_before": validated.radius_upper(root_box),
                "parameter_newton_radius": validated.radius_upper(new_parameter),
                "root_newton_radius": validated.radius_upper(new_root),
                "parameter_interior_inclusion": bool(parameter_interior),
                "root_interior_inclusion": bool(root_interior),
                **diagnostics,
            }
        )
        if not parameter_interior or not root_interior:
            raise ArithmeticError(
                "fast-seeded node interval Newton inclusion failed: "
                + json.dumps(interval_rows[-1], sort_keys=True)
            )
        parameter_box = nodal.inflated(new_parameter)
        root_box = nodal.inflated(new_root)
    values, jacobian, diagnostics = nodal.node_equations_and_jacobian(
        system, parameter_box, root_box
    )
    if not values[0].contains(0) or not values[1].contains(0):
        raise AssertionError("final node box does not enclose F=F_t=0")
    if diagnostics["jacobian_determinant_absolute_lower"] <= 0:
        raise AssertionError("final node Jacobian contains singularity")
    return parameter_box, root_box, {
        "seed_method": "midpoint sextic roots followed by interval Newton authority",
        "incoming_closest_pair_zero_based": list(pair),
        "midpoint_pair_to_next_distance_ratio": (
            distances[0][0] / distances[1][0]
        ),
        "point_newton_refinement": point_rows,
        "iterations": interval_rows,
        "final_F_interval": nodal.encoded_acb(values[0]),
        "final_F_t_interval": nodal.encoded_acb(values[1]),
        "final_jacobian_determinant": nodal.encoded_acb(jacobian.det()),
        **diagnostics,
    }


def build_thimble_taylor_system(
    system: validated.SelectedQ79IntervalSystem,
    start: complex,
    direction: complex,
    step: float,
    order: int,
) -> tuple[list[list[validated.TaylorModel]], list[validated.TaylorModel], dict]:
    radius = arb(format(step, ".17g"))
    a_value, b_value, elliptic_residual, elliptic_remainder = (
        validated.validated_ab_taylor_models(
            system, start, direction, radius, order
        )
    )
    prototype = a_value
    one = prototype.constant(1, order, radius)
    zero = prototype.constant(0, order, radius)
    elliptic = [a_value, b_value, one]
    da_dw = acb(2) * system.period_length * b_value
    db_dw = system.period_length * (acb(3) * a_value**2 - 1)
    elliptic_derivative = [da_dw, db_dw, zero]
    line = validated.tm_matrix_vector(system.alignment, elliptic)
    line_derivative = validated.tm_matrix_vector(
        system.alignment, elliptic_derivative
    )
    f_coefficients, f_derivative = (
        validated.aligned_tm_coefficients_and_derivative(
            system.evaluator.tables["F6"],
            line,
            line_derivative,
            chart=system.line_chart,
        )
    )
    polynomial_derivative = [
        index * f_coefficients[index] for index in range(1, 7)
    ]
    reduction = [[zero for _ in range(11)] for _ in range(11)]
    targets = [[zero for _ in range(5)] for _ in range(11)]
    half = acb("0.5")
    for power in range(6):
        if power:
            for index, coefficient in enumerate(f_coefficients):
                reduction[index + power - 1][power] += power * coefficient
        for index, coefficient in enumerate(polynomial_derivative):
            reduction[index + power][power] -= half * coefficient
    for power in range(5):
        for index, coefficient in enumerate(f_coefficients):
            reduction[index + power][6 + power] += coefficient
        for index, coefficient in enumerate(f_derivative):
            targets[index + power][power] -= half * coefficient
    solved, solve_neumann, solve_error = validated.tm_matrix_solve(
        reduction, targets
    )
    connection = [
        [solved[6 + index][power] for index in range(5)]
        for power in range(5)
    ]
    residue = [[zero for _ in range(5)] for _ in range(8)]
    for row, generator in enumerate(system.generators):
        variation = validated.tm_matrix_vector(
            system.alignment * generator, elliptic
        )
        if system.line_chart == "z":
            constant = line[2] * (
                variation[0] * line[2] - variation[2] * line[0]
            )
            linear = line[2] * (
                variation[1] * line[2] - variation[2] * line[1]
            )
        else:
            constant = -line[1] * (
                variation[0] * line[1] - variation[1] * line[0]
            )
            linear = -line[1] * (
                variation[2] * line[1] - variation[1] * line[2]
            )
        residue[row][0] = system.period_length * constant
        residue[row][1] = system.period_length * linear
    displacement = acb(0, 1) * validated.as_acb(direction)
    matrix = [[zero for _ in range(13)] for _ in range(13)]
    forcing = [zero for _ in range(13)]
    for row in range(5):
        for column in range(5):
            matrix[row][column] = displacement * connection[row][column]
    for row in range(8):
        for column in range(5):
            matrix[5 + row][column] = displacement * residue[row][column]
    return matrix, forcing, {
        "elliptic_residual_bound": elliptic_residual,
        "elliptic_remainder_bound": elliptic_remainder,
        "reduction_neumann_norm": solve_neumann,
        "reduction_solution_remainder": solve_error,
        "homogeneous_thimble_source_terms_omitted_exactly": True,
    }


def validated_residue_row_step(
    full_matrix: list[list[validated.TaylorModel]],
    residue_index: int,
    center: list[acb],
    input_frame: pilot.E32LiftErrorFrame,
) -> tuple[list[acb], pilot.E32LiftErrorFrame, dict]:
    selected = [0, 1, 2, 3, 4, 5 + residue_index]
    matrix = [
        [full_matrix[row][column] for column in selected]
        for row in selected
    ]
    zero = matrix[0][0].constant(
        0, matrix[0][0].order, matrix[0][0].radius
    )
    forcing = [zero for _ in range(6)]
    state, fundamental = pilot.e32_candidate_flow_polynomials(
        matrix, forcing, center
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
    inverse_norm, inverse_defect = validated.tm_verified_inverse_bound(
        fundamental
    )
    linear_defect = (
        inverse_norm
        * validated.tm_matrix_infinity_norm(fundamental_residual)
    )
    affine_defect = (
        inverse_norm * validated.tm_vector_infinity_norm(state_residual)
    )
    step_ball = matrix[0][0].radius
    growth = (linear_defect * step_ball).exp()
    forced_error = (
        affine_defect * step_ball
        if validated.upper(linear_defect) == 0
        else affine_defect * (growth - arb(1)) / linear_defect
    )
    input_radius = input_frame.physical_radius()
    transformed_error = growth * input_radius + forced_error
    transformed_correction = (
        (growth - arb(1)) * input_radius + forced_error
    )
    endpoint = step_ball
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
    output_frame = pilot.E32LiftErrorFrame(
        fundamental=output_fundamental,
        coordinate_radii=coordinate_radii,
    )
    generator = output_frame.physical_generator_matrix()
    residue_radius = sum(
        (abs(generator[5, column]) for column in range(6)), arb(0)
    )
    endpoint_center = [
        validated.SelectedQ79IntervalSystem.midpoint_acb(value)
        for value in endpoint_state
    ]
    return endpoint_center, output_frame, {
        "residue_index_zero_based": residue_index,
        "fundamental_inverse_neumann_norm": inverse_defect,
        "linear_defect_bound": validated.upper(linear_defect),
        "affine_defect_bound": validated.upper(affine_defect),
        "transformed_lift_correction": correction_upper,
        "input_lift_radius": validated.upper(input_radius),
        "output_lift_radius": validated.upper(output_frame.physical_radius()),
        "residue_coordinate_radius_upper": validated.upper(residue_radius),
    }


def validated_all_residue_rows_step(
    system: validated.SelectedQ79IntervalSystem,
    start: complex,
    direction: complex,
    step: float,
    centers: list[list[acb]],
    frames: list[pilot.E32LiftErrorFrame],
    *,
    order: int,
) -> tuple[list[list[acb]], list[pilot.E32LiftErrorFrame], dict]:
    matrix, _forcing, system_diagnostics = build_thimble_taylor_system(
        system, start, direction, step, order
    )
    output_centers = []
    output_frames = []
    rows = []
    for residue_index in range(8):
        center, frame, diagnostics = validated_residue_row_step(
            matrix, residue_index, centers[residue_index], frames[residue_index]
        )
        output_centers.append(center)
        output_frames.append(frame)
        rows.append(diagnostics)
    return output_centers, output_frames, {
        **system_diagnostics,
        "maximum_fundamental_inverse_neumann_norm": max(
            row["fundamental_inverse_neumann_norm"] for row in rows
        ),
        "maximum_transformed_lift_correction": max(
            row["transformed_lift_correction"] for row in rows
        ),
        "maximum_residue_coordinate_radius_upper": max(
            row["residue_coordinate_radius_upper"] for row in rows
        ),
        "residue_row_diagnostics": rows,
    }


def execute_main_transport(
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
    maximum_integral_radius: float,
) -> dict:
    initial_center = [system.midpoint_acb(value) for value in initial_periods]
    centers = [initial_center + [acb(0)] for _ in range(8)]
    frames = []
    for _residue_index in range(8):
        identity = acb_mat(6, 6)
        for index in range(6):
            identity[index, index] = acb(1)
        frames.append(
            pilot.E32LiftErrorFrame(
                fundamental=identity,
                coordinate_radii=[
                    value.rad().upper() for value in initial_periods
                ]
                + [arb(0)],
            )
        )
    distance = abs(endpoint - start)
    direction = (endpoint - start) / distance
    position = 0.0
    proposed = min(initial_step, maximum_step, distance)
    accepted = []
    rejected = 0
    minimum_accepted = math.inf
    while position < distance:
        step = min(proposed, distance - position)
        parameter_start = start + direction * position
        try:
            next_centers, next_frames, diagnostics = (
                validated_all_residue_rows_step(
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
                    "validated d087 full-residue main "
                    f"rejections={rejected} fraction={position / distance:.12g} "
                    f"next_step={proposed:.3e} reason={type(error).__name__}: {error}",
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
        if len(accepted) <= 3 or len(accepted) % 10 == 0 or position == distance:
            print(
                "validated d087 full-residue main "
                f"steps={len(accepted)} fraction={position / distance:.12g} "
                f"radius={diagnostics['maximum_residue_coordinate_radius_upper']:.3e}",
                flush=True,
            )
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
                sum(
                    (abs(generator[5, column]) for column in range(6)),
                    arb(0),
                )
            )
        )
    output_center = centers[0][:5] + [center[5] for center in centers]
    return {
        "center": [
            encoded_complex(handle.midpoint(value)) for value in output_center
        ],
        "residue_coordinate_radius_uppers": residue_radii,
        "uniform_integral_radius_upper": max(residue_radii),
        "lift_radius_uppers": [
            validated.upper(frame.physical_radius()) for frame in frames
        ],
        "period_center_dispersion_across_frames": period_dispersion,
        "certificate_method": (
            "eight correlated six-dimensional homogeneous augmented frames "
            "sharing one validated Taylor-system construction per step"
        ),
        "accepted_step_count": len(accepted),
        "rejected_step_count": rejected,
        "minimum_accepted_step": minimum_accepted,
        "path_length": distance,
        "steps": accepted,
    }


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--dps", type=int, default=110)
    parser.add_argument("--epsilon", type=float, default=1.0e-5)
    parser.add_argument("--order", type=int, default=48)
    parser.add_argument("--maximum-step", type=float, default=0.006)
    parser.add_argument("--minimum-step", type=float, default=1.0e-12)
    parser.add_argument("--maximum-lift-correction", type=float, default=2.0e-7)
    parser.add_argument("--maximum-integral-radius", type=float, default=2.0e-5)
    parser.add_argument("--cut-segments", type=int, default=32)
    parser.add_argument("--cut-tolerance", type=float, default=1.0e-40)
    parser.add_argument("--output", type=Path, default=OUTPUT)
    arguments = parser.parse_args()
    started = time.perf_counter()
    ctx.dps = arguments.dps
    if not 0 < arguments.epsilon < 0.01:
        raise ValueError("epsilon must lie in (0,0.01)")

    trial = load(TRIAL)
    thimble = load(THIMBLE)
    if int(thimble["distinguished_index"]) != 87:
        raise AssertionError("target cache is not d087")
    if thimble["root_id"] != "selected_085" or thimble["line_chart"] != "y":
        raise AssertionError("d087 target identity changed")
    system = exact_target_system(arguments.dps)
    print("initialized exact n3 y-chart interval system", flush=True)
    critical = complex_value(thimble["critical_center"])
    node_parameter, node_root, node_diagnostics = fast_certify_node(
        system,
        critical,
        epsilon=arguments.epsilon,
        iterations=3,
    )
    print(
        "certified d087 n3 node "
        f"parameter_radius={validated.radius_upper(node_parameter):.3e} "
        f"root_radius={validated.radius_upper(node_root):.3e}",
        flush=True,
    )
    factor_diagnostics = nodal.nodal_factor_certificate(
        system, node_parameter, node_root
    )
    print("certified d087 n3 local nodal factor", flush=True)
    node_payload = {
        "schema": "MTTQ79HeightFourD087TargetNodeInterval.v1",
        "status": "D087_N3_TARGET_NODE_AND_LOCAL_FACTOR_INTERVAL_CERTIFIED",
        "selected_target": {
            "distinguished_index": 87,
            "root_id": "selected_085",
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
            "n3_y_fibration": {
                "path": relative(FIBRATION),
                "sha256": sha256(FIBRATION),
            },
            "n3_d087_cache": {
                "path": relative(THIMBLE),
                "sha256": sha256(THIMBLE),
            },
            "source": {
                "path": relative(Path(__file__).resolve()),
                "sha256": sha256(Path(__file__).resolve()),
            },
        },
        "strict_scope": {
            "observed_SM_values_used": False,
            "target_node_interval_Newton_closed": True,
            "simple_node_factor_closed": True,
            "full_d087_period_vector_interval_closed": False,
        },
    }
    dump(NODE_OUTPUT, node_payload)
    print(f"wrote {relative(NODE_OUTPUT)}", flush=True)
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
    print("certified d087 n3 cutoff direct-cycle periods", flush=True)
    initial_step = min(
        arguments.maximum_step,
        abs(complex(float(node_center.real), float(node_center.imag)) - start_complex)
        / 4.0,
    )
    execution = execute_main_transport(
        system,
        initial_periods,
        start=start_complex,
        endpoint=0.0 + 0.0j,
        order=arguments.order,
        maximum_step=arguments.maximum_step,
        initial_step=initial_step,
        minimum_step=arguments.minimum_step,
        maximum_lift_correction=arguments.maximum_lift_correction,
        maximum_integral_radius=arguments.maximum_integral_radius,
    )

    base_center = np.asarray(
        [complex_value(value) for value in execution["center"][:5]],
        dtype=np.complex128,
    )
    floating_base = np.asarray(
        [
            complex_value(value)
            for value in thimble["base_fiber_propagated_periods"]
        ],
        dtype=np.complex128,
    )
    plus = float(np.max(abs(base_center - floating_base)))
    minus = float(np.max(abs(-base_center - floating_base)))
    orientation_sign = 1 if plus <= minus else -1
    selected_difference = min(plus, minus)
    rejected_difference = max(plus, minus)
    if rejected_difference <= 1000.0 * max(selected_difference, 1.0e-15):
        raise AssertionError("validated d087 orientation is not separated")

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
    output = arguments.output
    if not output.is_absolute():
        output = ROOT / output
    payload = {
        "schema": "MTTQ79HeightFourD087FullResidueMainInterval.v1",
        "status": "D087_N3_NODE_AND_ALL_EIGHT_MAIN_RESIDUE_ROWS_INTERVAL_CERTIFIED_TAIL_OPEN",
        "selected_target": {
            "distinguished_index": 87,
            "root_id": "selected_085",
            "line_chart": "y",
            "candidate_rank": 3,
            "endpoint_cutoff_epsilon": arguments.epsilon,
            "critical_center_floating_seed": thimble["critical_center"],
            "near_node_colliding_pair_zero_based": list(pair),
            **pair_diagnostics,
        },
        "certified_node": {
            "parameter_ball": nodal.encoded_acb(node_parameter),
            "double_root_ball": nodal.encoded_acb(node_root),
            "parameter_radius_upper": validated.radius_upper(node_parameter),
            "double_root_radius_upper": validated.radius_upper(node_root),
            "node_diagnostics": node_diagnostics,
            "factor_diagnostics": factor_diagnostics,
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
            "selected_base_center_maximum_difference": selected_difference,
            "opposite_base_center_maximum_difference": rejected_difference,
            "reference": "n3 ultra d087 continuity-synchronized floating cache",
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
                "n3_d087_cache": THIMBLE,
                "validated_taylor_engine": Path(validated.__file__).resolve(),
                "node_engine": Path(nodal.__file__).resolve(),
                "main_interval_engine": Path(pilot.__file__).resolve(),
                "source": Path(__file__).resolve(),
            }.items()
        },
        "numerics": {
            "dps": arguments.dps,
            "Taylor_order": arguments.order,
            "maximum_step": arguments.maximum_step,
            "minimum_step": arguments.minimum_step,
            "cut_segments": arguments.cut_segments,
            "cut_tolerance": arguments.cut_tolerance,
            "interval_system_diagnostics": asdict(system.diagnostics),
            "elapsed_seconds": time.perf_counter() - started,
        },
        "strict_scope": {
            "observed_SM_values_used": False,
            "target_alignment_interval_used": True,
            "target_node_interval_Newton_closed": True,
            "all_eight_main_residue_rows_interval_closed": True,
            "node_to_cutoff_tail_interval_closed": False,
            "full_d087_period_vector_interval_closed": False,
            "covariant_zero_proved": False,
        },
        "next_required_artifact": (
            "certify the all-eight node-to-cutoff residue tail on the same n3 "
            "alignment and splice it to this main vector"
        ),
    }
    dump(output, payload)
    NOTE.write_text(
        "# MTT q79 Height-Four d087 Full-Residue Main Interval (A220) v1\n\n"
        "At the A218/n3 alignment, interval Newton certifies the selected_085 "
        "node and its simple quadratic-times-quartic factor. A homogeneous "
        "13-state defect-corrected Taylor transport then encloses the five "
        "Picard-Fuchs periods and all eight PGL(3) residue integrals from the "
        "epsilon cutoff to the base.\n\n"
        f"The common complex-disk radius for the eight main rows is "
        f"`{execution['uniform_integral_radius_upper']:.12g}` after "
        f"`{execution['accepted_step_count']}` accepted steps. The orientation "
        "is fixed against the continuity-synchronized n3 d087 cache.\n\n"
        "This closes the dominant thimble's node and full eight-row main "
        "transport. It does not promote the floating endpoint-tail subtraction "
        "to a bound. The all-eight desingularized local tail is the next proof "
        "object; no covariant zero or full SM closure is claimed here.\n",
        encoding="utf-8",
    )
    print(f"wrote {relative(output)}")
    print(f"wrote {relative(NOTE)}")
    print(
        json.dumps(
            {
                "node_parameter_radius": validated.radius_upper(node_parameter),
                "node_root_radius": validated.radius_upper(node_root),
                "main_common_radius": execution["uniform_integral_radius_upper"],
                "accepted_steps": execution["accepted_step_count"],
                "rejected_steps": execution["rejected_step_count"],
                "orientation_sign": orientation_sign,
                "maximum_diagnostic_tail": float(np.max(abs(diagnostic_tail))),
                "elapsed_seconds": time.perf_counter() - started,
            },
            indent=2,
        )
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
