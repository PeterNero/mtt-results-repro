from __future__ import annotations

import argparse
import hashlib
import json
import math
import time
from pathlib import Path

import numpy as np
from flint import acb, acb_mat, arb, ctx

import certify_q79_height4_d087_full_residue_main_interval as main_engine
import certify_q79_height4_dynamic_target_full_residue_interval as dynamic
import certify_q79_height4_rank3_beta_hessian_interval as beta_hessian
import certify_q79_height4_tight_target_full_residue_interval as tight
import certify_q79_selected_alignment_E32_handle_combination_interval as handle
import certify_q79_selected_alignment_single_E32_thimble_main_interval as pilot
import certify_q79_selected_side_beta_defect_transport as validated


ROOT = Path(__file__).resolve().parents[1]
PROBE = main_engine.PROBE_DIRECTORY
VALIDATED = PROBE / "validated_transport"
OUTPUT_DIRECTORY = VALIDATED / "hessian"
A378 = VALIDATED / "n3.hessian_source.json"
ARTIFACT = "A380"


TM = validated.TaylorModel


def load(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def dump(path: Path, value: dict) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(value, indent=2, sort_keys=True) + "\n", encoding="utf-8")


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def relative(path: Path) -> str:
    return str(path.relative_to(ROOT)).replace("\\", "/")


def pair(value: complex) -> dict[str, str]:
    return {
        "real": format(float(value.real), ".17g"),
        "imaginary": format(float(value.imag), ".17g"),
    }


def complex_value(value: dict[str, str]) -> complex:
    return complex(float(value["real"]), float(value["imaginary"]))


def target_paths(index: int) -> dict[str, Path]:
    stem = f"d{index:03d}.mainH"
    return {
        "canonical_main": tight.canonical_paths(index)["main"],
        "canonical_full": tight.canonical_paths(index)["full"],
        "output": OUTPUT_DIRECTORY / f"{stem}.interval.json",
        "checkpoint": OUTPUT_DIRECTORY / f"{stem}.checkpoint.json",
        "note": ROOT
        / "proof_corpus"
        / f"MTT_q79HeightFourD{index:03d}MainHessianInterval_A380_v1.md",
    }


def tm_connection(
    system: validated.SelectedQ79IntervalSystem,
    line: list[TM],
    line_derivative: list[TM],
) -> tuple[list[list[TM]], dict]:
    f_coefficients, f_derivative = validated.aligned_tm_coefficients_and_derivative(
        system.evaluator.tables["F6"],
        line,
        line_derivative,
        chart=system.line_chart,
    )
    connection, _exact_terms, solve_neumann, solve_error = (
        beta_hessian.tm_reduction_solution(f_coefficients, f_derivative)
    )
    return connection, {
        "reduction_neumann_norm": solve_neumann,
        "reduction_solution_remainder": solve_error,
    }


def aligned_tm_coefficients_and_derivatives_batch(
    table: list[dict],
    line: list[TM],
    line_derivatives: list[list[TM]],
    *,
    chart: str,
) -> tuple[list[TM], list[list[TM]]]:
    """Evaluate one homogeneous table and all directional derivatives together."""
    degree = sum(int(value) for value in table[0]["powers_xyz"])
    prototype = line[0]
    zero = beta_hessian.tm_zero(prototype)
    one = prototype.constant(1, prototype.order, prototype.radius)
    powers_by_coordinate: list[list[TM]] = []
    for coordinate in line:
        powers = [one]
        for _power in range(1, degree + 1):
            powers.append(powers[-1] * coordinate)
        powers_by_coordinate.append(powers)

    ascending = [zero for _ in range(degree + 1)]
    partials = [
        [zero for _ in range(degree + 1)] for _ in range(len(line))
    ]
    for row in table:
        x_power, y_power, z_power = [int(value) for value in row["powers_xyz"]]
        coefficient = int(row["coefficient"])
        if chart == "y":
            expansions = (
                (
                    index + z_power,
                    [y_power - index, x_power + z_power, index],
                    coefficient * (-1) ** y_power * math.comb(y_power, index),
                )
                for index in range(y_power + 1)
            )
        elif chart == "z":
            expansions = (
                (
                    index + y_power,
                    [z_power - index, index, x_power + y_power],
                    coefficient * (-1) ** z_power * math.comb(z_power, index),
                )
                for index in range(z_power + 1)
            )
        else:
            raise ValueError(f"unsupported chart {chart!r}")
        for output_index, powers, scalar in expansions:
            value = one
            for coordinate_index, power in enumerate(powers):
                value *= powers_by_coordinate[coordinate_index][power]
            ascending[output_index] += scalar * value
            for selected, power in enumerate(powers):
                if power == 0:
                    continue
                partial = one
                for coordinate_index, other_power in enumerate(powers):
                    partial *= powers_by_coordinate[coordinate_index][
                        other_power - int(coordinate_index == selected)
                    ]
                partials[selected][output_index] += scalar * power * partial

    derivatives = []
    for line_derivative in line_derivatives:
        derivatives.append(
            [
                sum(
                    (
                        partials[coordinate][output_index]
                        * line_derivative[coordinate]
                        for coordinate in range(len(line))
                    ),
                    zero,
                )
                for output_index in range(degree + 1)
            ]
        )
    return ascending, derivatives


def acb_matrix_copy(value: acb_mat) -> acb_mat:
    return acb_mat(
        [
            [value[row, column] for column in range(value.ncols())]
            for row in range(value.nrows())
        ]
    )


def tm_matrix_solve_batched(
    matrix: list[list[TM]], targets: list[list[TM]]
) -> tuple[list[list[TM]], float, float]:
    """Verified Taylor solve with coefficient-matrix residual accumulation."""
    order = matrix[0][0].order
    radius = matrix[0][0].radius
    matrix_coefficients = validated.tm_matrix_coefficients(matrix)
    target_coefficients = validated.tm_matrix_coefficients(targets)
    center_inverse = matrix_coefficients[0].inv()
    recurrence_inverse = acb_mat(
        [
            [
                validated.SelectedQ79IntervalSystem.midpoint_acb(
                    center_inverse[row, column]
                )
                for column in range(center_inverse.ncols())
            ]
            for row in range(center_inverse.nrows())
        ]
    )
    solution_coefficients: list[acb_mat] = []
    for degree in range(order + 1):
        right = acb_matrix_copy(target_coefficients[degree])
        for index in range(1, degree + 1):
            right -= matrix_coefficients[index] * solution_coefficients[
                degree - index
            ]
        solution_coefficients.append(recurrence_inverse * right)
    result = [
        [
            TM(
                [
                    solution_coefficients[degree][row, column]
                    for degree in range(order + 1)
                ],
                radius,
            ).midpoint_polynomial()
            for column in range(len(targets[0]))
        ]
        for row in range(len(matrix))
    ]
    midpoint_solution_coefficients = validated.tm_matrix_coefficients(result)

    residual_coefficients: list[acb_mat] = []
    for degree in range(order + 1):
        residual = acb_matrix_copy(target_coefficients[degree])
        for matrix_degree in range(degree + 1):
            residual -= (
                matrix_coefficients[matrix_degree]
                * midpoint_solution_coefficients[degree - matrix_degree]
            )
        residual_coefficients.append(residual)
    omitted_coefficients: list[tuple[int, acb_mat]] = []
    for degree in range(order + 1, 2 * order + 1):
        omitted = acb_mat(len(matrix), len(targets[0]))
        for matrix_degree in range(max(0, degree - order), order + 1):
            solution_degree = degree - matrix_degree
            if 0 <= solution_degree <= order:
                omitted += (
                    matrix_coefficients[matrix_degree]
                    * midpoint_solution_coefficients[solution_degree]
                )
        omitted_coefficients.append((degree, omitted))

    powers = [arb(1)]
    for _degree in range(2 * order):
        powers.append(powers[-1] * radius)
    residual_bounds = [
        [targets[row][column].remainder for column in range(len(targets[0]))]
        for row in range(len(matrix))
    ]
    solution_polynomial_bounds = [
        [result[row][column].polynomial_absolute_bound() for column in range(len(targets[0]))]
        for row in range(len(matrix))
    ]
    for row in range(len(matrix)):
        for column in range(len(targets[0])):
            bound = residual_bounds[row][column]
            for degree, coefficient in enumerate(residual_coefficients):
                bound += abs(coefficient[row, column]) * powers[degree]
            for degree, coefficient in omitted_coefficients:
                bound += abs(coefficient[row, column]) * powers[degree]
            for inner in range(len(matrix)):
                bound += (
                    matrix[row][inner].remainder
                    * solution_polynomial_bounds[inner][column]
                )
            residual_bounds[row][column] = bound

    inverse_norm, neumann_upper = validated.tm_verified_inverse_bound(matrix)
    maximum_error = 0.0
    for column in range(len(targets[0])):
        residual_norm = max(
            (residual_bounds[row][column] for row in range(len(matrix))),
            key=validated.upper,
        )
        error = inverse_norm * residual_norm
        maximum_error = max(maximum_error, validated.upper(error))
        for row in range(len(matrix)):
            result[row][column].remainder += error
    return result, neumann_upper, maximum_error


def tm_connections_batch(
    system: validated.SelectedQ79IntervalSystem,
    line: list[TM],
    line_derivatives: list[list[TM]],
) -> tuple[list[list[list[TM]]], dict]:
    """Solve one reduction matrix against every deformation right-hand side."""
    if not line_derivatives:
        raise ValueError("at least one line derivative is required")
    f_coefficients, f_derivatives = (
        aligned_tm_coefficients_and_derivatives_batch(
            system.evaluator.tables["F6"],
            line,
            line_derivatives,
            chart=system.line_chart,
        )
    )

    prototype = f_coefficients[0]
    zero = beta_hessian.tm_zero(prototype)
    polynomial_derivative = [
        index * f_coefficients[index] for index in range(1, 7)
    ]
    reduction = [[zero for _ in range(11)] for _ in range(11)]
    target_columns = 5 * len(f_derivatives)
    targets = [[zero for _ in range(target_columns)] for _ in range(11)]
    half = acb("0.5")
    for power in range(6):
        if power:
            for index, coefficient in enumerate(f_coefficients):
                reduction[index + power - 1][power] += power * coefficient
        for index, coefficient in enumerate(polynomial_derivative):
            reduction[index + power][power] -= half * coefficient
    for derivative_index, f_derivative in enumerate(f_derivatives):
        column_offset = 5 * derivative_index
        for power in range(5):
            for index, coefficient in enumerate(f_coefficients):
                reduction[index + power][6 + power] += (
                    coefficient if derivative_index == 0 else zero
                )
            for index, coefficient in enumerate(f_derivative):
                targets[index + power][column_offset + power] -= half * coefficient

    solved, solve_neumann, solve_error = tm_matrix_solve_batched(reduction, targets)
    connections = []
    for derivative_index in range(len(f_derivatives)):
        column_offset = 5 * derivative_index
        connections.append(
            [
                [
                    solved[6 + index][column_offset + power]
                    for index in range(5)
                ]
                for power in range(5)
            ]
        )
    return connections, {
        "reduction_neumann_norm": solve_neumann,
        "reduction_solution_remainder": solve_error,
        "batched_reduction_right_hand_side_count": len(f_derivatives),
        "batched_reduction_target_column_count": target_columns,
    }


def build_homogeneous_hessian_system(
    system: validated.SelectedQ79IntervalSystem,
    start: complex,
    direction: complex,
    step: float,
    order: int,
) -> tuple[list[list[TM]], list[TM], list[list[TM]], list[TM], dict]:
    radius = arb(format(step, ".17g"))
    a_value, b_value, elliptic_residual, elliptic_remainder = (
        validated.validated_ab_taylor_models(
            system, start, direction, radius, order
        )
    )
    one = a_value.constant(1, order, radius)
    zero = a_value.constant(0, order, radius)
    elliptic = [a_value, b_value, one]
    elliptic_w = [
        acb(2) * system.period_length * b_value,
        system.period_length * (acb(3) * a_value**2 - 1),
        zero,
    ]
    line = validated.tm_matrix_vector(system.alignment, elliptic)
    line_w = validated.tm_matrix_vector(system.alignment, elliptic_w)
    residues = beta_hessian.tm_residue_rows(system, elliptic, line)

    hessian_rows: list[list[TM]] = []
    line_directions = []
    for selected_direction in range(8):
        generator = system.generators[selected_direction]
        line_directions.append(
            validated.tm_matrix_vector(system.alignment * generator, elliptic)
        )
    connections, reduction_diagnostics = tm_connections_batch(
        system, line, [line_w, *line_directions]
    )
    connection_w = connections[0]
    for selected_direction, connection_s in enumerate(connections[1:]):
        direct_rows = beta_hessian.tm_residue_directional_derivatives(
            system, elliptic, line, selected_direction
        )
        for residue_index in range(8):
            transported = beta_hessian.tm_row_matrix(
                residues[residue_index], connection_s
            )
            hessian_rows.append(
                [
                    direct_rows[residue_index][column] + transported[column]
                    for column in range(5)
                ]
            )

    displacement = acb(0, 1) * validated.as_acb(direction)
    lift_matrix = [
        [displacement * value for value in row] for row in connection_w
    ]
    output_rows = [
        [displacement * value for value in row]
        for row in residues + hessian_rows
    ]
    return (
        lift_matrix,
        [zero for _ in range(5)],
        output_rows,
        [zero for _ in range(72)],
        {
            "elliptic_residual_bound": elliptic_residual,
            "elliptic_remainder_bound": elliptic_remainder,
            "maximum_reduction_neumann_norm": reduction_diagnostics[
                "reduction_neumann_norm"
            ],
            "maximum_reduction_solution_remainder": reduction_diagnostics[
                "reduction_solution_remainder"
            ],
            "batched_reduction_right_hand_side_count": reduction_diagnostics[
                "batched_reduction_right_hand_side_count"
            ],
            "batched_reduction_target_column_count": reduction_diagnostics[
                "batched_reduction_target_column_count"
            ],
            "derived_output_row_count": len(output_rows),
            "derived_hessian_row_count": len(hessian_rows),
            "homogeneous_period_source_terms_omitted_exactly": True,
        },
    )


def selected_system(index: int, dps: int) -> tuple[validated.SelectedQ79IntervalSystem, int, dict]:
    rank, row, _prior_node = tight.configure_selected_target(index)
    if dynamic.CHART == "z":
        system = dynamic.z_helper.exact_z_system(dps)
    elif dynamic.CHART == "y":
        system = tight.ORIGINAL_EXACT_TARGET_SYSTEM(dps)
    else:
        raise AssertionError(f"unsupported target chart {dynamic.CHART!r}")
    return system, rank, row


def canonical_cutoff_start(main_packet: dict) -> tuple[complex, complex]:
    """Replay the ordinary certificate's cutoff-start rounding convention."""
    node_ball = validated.decoded_acb(
        main_packet["certified_node"]["parameter_ball"]
    )
    node_center = handle.midpoint(node_ball)
    epsilon = float(main_packet["selected_target"]["endpoint_cutoff_epsilon"])
    start_ball = node_center * acb(format(1.0 - epsilon, ".17g"))
    return node_center, handle.midpoint(start_ball)


def initial_state(
    system: validated.SelectedQ79IntervalSystem,
    main_packet: dict,
    start: complex,
) -> tuple[list[acb], validated.LiftErrorFrame, list[arb], dict]:
    display_balls = [
        validated.interval_from_bounds(value)
        for value in main_packet["near_node_direct_cycle_interval"][
            "initial_period_intervals"
        ]
    ]
    if len(display_balls) != 5:
        raise AssertionError("target cutoff packet no longer has five period coordinates")

    roots, leading = pilot.roots_at(system, start)
    cut_pair = tuple(
        int(value)
        for value in main_packet["selected_target"][
            "near_node_colliding_pair_zero_based"
        ]
    )
    if len(cut_pair) != 2 or not 0 <= cut_pair[0] < cut_pair[1] < len(roots):
        raise AssertionError("canonical cutoff pair is malformed")
    minimum_root_separation = min(
        validated.lower(abs(roots[left] - roots[right]))
        for left in range(len(roots))
        for right in range(left)
    )
    if minimum_root_separation <= 0.0:
        raise AssertionError("current-source cutoff roots are not interval-separated")

    numerics = main_packet["numerics"]
    initial_balls, cut_diagnostics = handle.direct_cut_periods(
        roots,
        leading,
        cut_pair,
        segments=int(numerics["cut_segments"]),
        tolerance=float(numerics["cut_tolerance"]),
    )
    display_overlaps = [
        current.overlaps(display)
        for current, display in zip(initial_balls, display_balls)
    ]
    if not all(display_overlaps):
        raise AssertionError(
            "current-source full-precision cutoff periods do not overlap the "
            "canonical ordinary certificate"
        )
    display_differences = [
        validated.upper(abs(current - display))
        for current, display in zip(initial_balls, display_balls)
    ]

    center = [
        validated.SelectedQ79IntervalSystem.midpoint_acb(value)
        for value in initial_balls
    ] + [acb(0) for _ in range(72)]
    fundamental = acb_mat(5, 5)
    for index in range(5):
        fundamental[index, index] = acb(1)
    frame = validated.LiftErrorFrame(
        fundamental=fundamental,
        coordinate_radii=[value.rad().upper() for value in initial_balls],
    )
    return center, frame, [arb(0) for _ in range(72)], {
        "method": (
            "current-source direct-cut Arb quadrature at the canonical ordinary "
            "cutoff start; display-rounded bounds are overlap witnesses only"
        ),
        "canonical_cutoff_start": pair(start),
        "canonical_pair_zero_based": list(cut_pair),
        "minimum_cutoff_root_ball_separation_lower": minimum_root_separation,
        "full_precision_period_balls": [
            validated.encoded_acb(value) for value in initial_balls
        ],
        "maximum_full_precision_period_radius_upper": max(
            validated.radius_upper(value) for value in initial_balls
        ),
        "canonical_display_intervals_overlap_all_five": all(display_overlaps),
        "canonical_display_overlap_by_period": display_overlaps,
        "maximum_canonical_display_interval_difference_upper": max(
            display_differences
        ),
        "direct_cut_diagnostics": cut_diagnostics,
    }


def model_disk_overlap_diagnostics(left: TM, right: TM) -> tuple[float, float, float]:
    if len(left.coefficients) != len(right.coefficients):
        raise AssertionError("Taylor-model orders differ in smoke replay")
    radius = max(validated.upper(left.radius), validated.upper(right.radius))
    polynomial_center_difference_bound = sum(
        validated.upper(abs(a - b)) * radius**power
        for power, (a, b) in enumerate(zip(left.coefficients, right.coefficients))
    )
    combined_remainder_radius = (
        + validated.upper(left.remainder)
        + validated.upper(right.remainder)
    )
    return (
        polynomial_center_difference_bound,
        combined_remainder_radius,
        max(0.0, polynomial_center_difference_bound - combined_remainder_radius),
    )


def smoke_test(
    system: validated.SelectedQ79IntervalSystem,
    chart: str,
    order: int,
) -> dict:
    step = 1.0e-5
    direction = 1.0 + 0.0j
    lift, _forcing, outputs, _output_forcing, diagnostics = (
        build_homogeneous_hessian_system(
            system, 0.0 + 0.0j, direction, step, order
        )
    )
    original, _original_forcing, _original_diagnostics = (
        main_engine.build_thimble_taylor_system(
            system, 0.0 + 0.0j, direction, step, order
        )
    )
    replay_center_difference = 0.0
    replay_remainder_radius = 0.0
    replay_nonoverlap_excess = 0.0
    for row in range(5):
        for column in range(5):
            center_difference, remainder_radius, excess = (
                model_disk_overlap_diagnostics(
                    lift[row][column], original[row][column]
                )
            )
            replay_center_difference = max(
                replay_center_difference, center_difference
            )
            replay_remainder_radius = max(replay_remainder_radius, remainder_radius)
            replay_nonoverlap_excess = max(replay_nonoverlap_excess, excess)
    for row in range(8):
        for column in range(5):
            center_difference, remainder_radius, excess = (
                model_disk_overlap_diagnostics(
                    outputs[row][column], original[5 + row][column]
                )
            )
            replay_center_difference = max(
                replay_center_difference, center_difference
            )
            replay_remainder_radius = max(replay_remainder_radius, remainder_radius)
            replay_nonoverlap_excess = max(replay_nonoverlap_excess, excess)
    if replay_nonoverlap_excess > 0.0:
        raise AssertionError(
            "homogeneous Hessian transport Taylor disks do not overlap the "
            f"certified main system: excess={replay_nonoverlap_excess:.6e}"
        )

    a378 = load(A378)
    chart_packet = next(
        row for row in a378["chart_executions"] if row["line_chart"] == chart
    )
    displacement = acb(0, 1)
    source_difference = 0.0
    for selected_direction, direction_packet in enumerate(
        chart_packet["deformation_directions"]
    ):
        for residue_index, source_row in enumerate(
            direction_packet["covariant_hessian_integrand_rows"]
        ):
            output_index = 8 + selected_direction * 8 + residue_index
            for column, source_value in enumerate(source_row):
                current = outputs[output_index][column].coefficients[0] / displacement
                expected = validated.decoded_acb(source_value)
                source_difference = max(
                    source_difference, validated.upper(abs(current - expected))
                )
    if source_difference > 1.0e-30:
        raise AssertionError(
            "homogeneous Hessian rows do not reproduce A378: "
            f"{source_difference:.6e}"
        )
    return {
        "step": step,
        "order": order,
        "line_chart": chart,
        "maximum_original_main_system_polynomial_center_difference_bound": (
            replay_center_difference
        ),
        "maximum_original_main_system_combined_remainder_radius": (
            replay_remainder_radius
        ),
        "maximum_original_main_system_disk_nonoverlap_excess": (
            replay_nonoverlap_excess
        ),
        "maximum_A378_hessian_source_difference": source_difference,
        "output_row_count": len(outputs),
        "hessian_row_count": len(outputs) - 8,
        **diagnostics,
    }


def configuration(
    arguments: argparse.Namespace,
    paths: dict[str, Path],
    main_packet: dict,
    start: complex,
) -> dict:
    return {
        "index": arguments.index,
        "dps": arguments.dps,
        "order": arguments.order,
        "maximum_step": format(arguments.maximum_step, ".17g"),
        "minimum_step": format(arguments.minimum_step, ".17g"),
        "maximum_lift_correction": format(
            arguments.maximum_lift_correction, ".17g"
        ),
        "maximum_output_increment": format(
            arguments.maximum_output_increment, ".17g"
        ),
        "maximum_output_radius": format(arguments.maximum_output_radius, ".17g"),
        "start": pair(start),
        "endpoint": pair(0.0 + 0.0j),
        "canonical_main_sha256": sha256(paths["canonical_main"]),
        "A378_sha256": sha256(A378),
        "builder_source_sha256": sha256(Path(__file__).resolve()),
        "triangular_engine_sha256": sha256(Path(beta_hessian.__file__).resolve()),
        "validated_engine_sha256": sha256(Path(validated.__file__).resolve()),
        "direct_cut_period_engine_sha256": sha256(Path(handle.__file__).resolve()),
        "cutoff_root_engine_sha256": sha256(Path(pilot.__file__).resolve()),
        "cutoff_start_rounding_convention": "canonical ordinary handle.midpoint replay",
        "selected_root_id": main_packet["selected_target"]["root_id"],
    }


def execute(arguments: argparse.Namespace) -> dict:
    started = time.perf_counter()
    paths = target_paths(arguments.index)
    if not paths["canonical_main"].exists():
        raise FileNotFoundError("canonical all-eight main interval is absent")
    main_packet = load(paths["canonical_main"])
    system, rank, row = selected_system(arguments.index, arguments.dps)
    chart = dynamic.CHART
    smoke = smoke_test(system, chart, min(arguments.order, 18))
    if arguments.smoke_only:
        print(json.dumps(smoke, indent=2))
        return {"smoke_test": smoke}

    node_center, start = canonical_cutoff_start(main_packet)
    epsilon = float(main_packet["selected_target"]["endpoint_cutoff_epsilon"])
    endpoint = 0.0 + 0.0j
    distance = abs(endpoint - start)
    direction = (endpoint - start) / distance
    config = configuration(arguments, paths, main_packet, start)
    initial_center, initial_frame, initial_output_radii, initial_period_source = (
        initial_state(system, main_packet, start)
    )

    if arguments.resume:
        checkpoint = load(paths["checkpoint"])
        if checkpoint.get("schema") != "MTTQ79TargetMainHessianCheckpoint.v1":
            raise ValueError("target Hessian checkpoint schema changed")
        if checkpoint.get("configuration") != config:
            raise ValueError("target Hessian checkpoint configuration changed")
        center = [validated.decoded_acb(value) for value in checkpoint["center"]]
        frame = validated.LiftErrorFrame(
            fundamental=validated.decoded_matrix(checkpoint["lift_fundamental"]),
            coordinate_radii=[arb(value) for value in checkpoint["coordinate_radii"]],
        )
        output_radii = [arb(value) for value in checkpoint["output_radii"]]
        accepted = checkpoint["accepted_steps"]
        rejected = int(checkpoint["rejected_step_count"])
        minimum_accepted_step = float(checkpoint["minimum_accepted_step"])
        proposed_step = float(checkpoint["proposed_step"])
        position = float(checkpoint["position"])
        print(
            f"resumed d{arguments.index:03d} main Hessian steps={len(accepted)} "
            f"fraction={position / distance:.12g}",
            flush=True,
        )
    else:
        center = initial_center
        frame = initial_frame
        output_radii = initial_output_radii
        accepted = []
        rejected = 0
        minimum_accepted_step = math.inf
        position = 0.0
        node_to_cutoff = abs(node_center - start)
        proposed_step = min(arguments.maximum_step, node_to_cutoff / 4.0)

    def save_checkpoint() -> None:
        validated.atomic_dump(
            paths["checkpoint"],
            {
                "schema": "MTTQ79TargetMainHessianCheckpoint.v1",
                "configuration": config,
                "position": format(position, ".17g"),
                "proposed_step": format(proposed_step, ".17g"),
                "center": [validated.encoded_acb(value) for value in center],
                "lift_fundamental": validated.encoded_matrix(frame.fundamental),
                "coordinate_radii": [str(value) for value in frame.coordinate_radii],
                "output_radii": [str(value) for value in output_radii],
                "accepted_steps": accepted,
                "rejected_step_count": rejected,
                "minimum_accepted_step": format(minimum_accepted_step, ".17g"),
            },
        )

    while position < distance:
        if len(accepted) >= arguments.maximum_steps:
            raise ArithmeticError("target Hessian transport exceeded step budget")
        step = min(proposed_step, distance - position)
        if step < arguments.minimum_step:
            raise ArithmeticError("target Hessian transport requires a smaller step")
        parameter_start = start + direction * position
        try:
            next_center, next_frame, next_radii, diagnostics = (
                beta_hessian.validated_affine_hessian_step(
                    system,
                    parameter_start,
                    direction,
                    step,
                    center,
                    frame,
                    output_radii,
                    order=arguments.order,
                    system_builder=build_homogeneous_hessian_system,
                )
            )
            if (
                diagnostics["transformed_lift_correction"]
                > arguments.maximum_lift_correction
            ):
                raise ArithmeticError("lift correction exceeds local budget")
            if (
                diagnostics["maximum_output_increment_error"]
                > arguments.maximum_output_increment
            ):
                raise ArithmeticError("output increment exceeds local budget")
            if diagnostics["maximum_output_radius"] > arguments.maximum_output_radius:
                raise ArithmeticError("output radius exceeds global budget")
        except (ArithmeticError, ZeroDivisionError, ValueError) as error:
            rejected += 1
            proposed_step = step / 2.0
            if rejected % 10 == 0:
                print(
                    f"d{arguments.index:03d} Hessian rejections={rejected} "
                    f"fraction={position / distance:.12g} next={proposed_step:.3e} "
                    f"reason={type(error).__name__}: {error}",
                    flush=True,
                )
            if proposed_step < arguments.minimum_step:
                raise
            continue
        center = next_center
        frame = next_frame
        output_radii = next_radii
        position = min(distance, position + step)
        minimum_accepted_step = min(minimum_accepted_step, step)
        accepted.append(
            {
                "start_arclength": position - step,
                "end_arclength": position,
                "step": step,
                **diagnostics,
            }
        )
        quality = max(
            diagnostics["maximum_reduction_neumann_norm"],
            diagnostics["fundamental_inverse_neumann_norm"],
        )
        proposed_step = min(
            arguments.maximum_step,
            step * (1.8 if quality < 0.05 else 1.35),
        )
        if len(accepted) % 10 == 0 or position == distance:
            save_checkpoint()
        if len(accepted) <= 3 or len(accepted) % 10 == 0 or position == distance:
            print(
                f"d{arguments.index:03d} Hessian steps={len(accepted)} "
                f"fraction={position / distance:.12g} "
                f"radius={max(validated.upper(value) for value in output_radii):.3e}",
                flush=True,
            )

    orientation = int(main_packet["orientation"]["selected_sign"])
    ordinary_centers = -orientation * np.asarray(
        [validated.midpoint(value) for value in center[5:13]],
        dtype=np.complex128,
    )
    ordinary_radii = np.asarray(
        [validated.upper(value) for value in output_radii[:8]], dtype=np.float64
    )
    hessian = np.empty((8, 8), dtype=np.complex128)
    hessian_radii = np.empty((8, 8), dtype=np.float64)
    for selected_direction in range(8):
        for residue_index in range(8):
            offset = selected_direction * 8 + residue_index
            hessian[residue_index, selected_direction] = -orientation * validated.midpoint(
                center[13 + offset]
            )
            hessian_radii[residue_index, selected_direction] = validated.upper(
                output_radii[8 + offset]
            )

    canonical_centers = np.asarray(
        [
            complex_value(value)
            for value in main_packet["all_eight_main_residue_rows"][
                "interval_centers"
            ]
        ],
        dtype=np.complex128,
    )
    canonical_radius = float(
        main_packet["all_eight_main_residue_rows"][
            "common_complex_disk_radius_upper"
        ]
    )
    replay_difference = abs(ordinary_centers - canonical_centers)
    replay_overlap = replay_difference <= ordinary_radii + canonical_radius
    if not bool(np.all(replay_overlap)):
        raise AssertionError("Hessian transport ordinary rows do not overlap canonical main")

    payload = {
        "schema": "MTTQ79HeightFourTargetMainHessianInterval.v1",
        "status": "TARGET_MAIN_EIGHT_ROWS_AND_COMPLEX_8_BY_8_HESSIAN_INTERVAL_CERTIFIED",
        "artifact": ARTIFACT,
        "selected_target": {
            "distinguished_index": arguments.index,
            "A219_contribution_rank": rank,
            "root_id": row["root_id"],
            "line_chart": chart,
            "signed_chain_coefficient": int(row["signed_coefficient"]),
            "orientation_sign": orientation,
            "endpoint_cutoff_epsilon": epsilon,
        },
        "main_residue_rows": [
            {
                "residue_index_zero_based": index,
                "interval_center": pair(ordinary_centers[index]),
                "component_radius_upper": float(ordinary_radii[index]),
                "canonical_center_difference": float(replay_difference[index]),
                "canonical_intervals_overlap": bool(replay_overlap[index]),
            }
            for index in range(8)
        ],
        "complex_main_Hessian_8_by_8": [
            [
                {
                    "row_zero_based": row_index,
                    "column_zero_based": column_index,
                    "interval_center": pair(hessian[row_index, column_index]),
                    "component_radius_upper": float(
                        hessian_radii[row_index, column_index]
                    ),
                }
                for column_index in range(8)
            ]
            for row_index in range(8)
        ],
        "summary": {
            "certified_main_rows": 8,
            "certified_main_Hessian_entries": 64,
            "maximum_main_row_component_radius_upper": float(
                np.max(ordinary_radii)
            ),
            "maximum_main_Hessian_component_radius_upper": float(
                np.max(hessian_radii)
            ),
            "main_Hessian_product_box_frobenius_radius_upper": float(
                np.linalg.norm(hessian_radii)
            ),
            "all_canonical_main_intervals_overlap": bool(np.all(replay_overlap)),
            "maximum_canonical_main_center_difference": float(
                np.max(replay_difference)
            ),
            "accepted_step_count": len(accepted),
            "rejected_step_count": rejected,
            "minimum_accepted_step": minimum_accepted_step,
            "elapsed_seconds": time.perf_counter() - started,
        },
        "smoke_test": smoke,
        "initial_period_source": initial_period_source,
        "execution": {
            "configuration": config,
            "steps": accepted,
            "checkpoint": relative(paths["checkpoint"]),
            "checkpoint_sha256": sha256(paths["checkpoint"]),
        },
        "authority": {
            name: {"path": relative(path), "sha256": sha256(path)}
            for name, path in {
                "canonical_main_interval": paths["canonical_main"],
                "A378_Hessian_integrand_source": A378,
                "triangular_validated_engine": Path(beta_hessian.__file__).resolve(),
                "validated_Taylor_engine": Path(validated.__file__).resolve(),
                "direct_cut_period_engine": Path(handle.__file__).resolve(),
                "cutoff_root_engine": Path(pilot.__file__).resolve(),
                "builder_source": Path(__file__).resolve(),
            }.items()
        },
        "strict_scope": {
            "observed_SM_values_used": False,
            "same_source_A378_homogeneous_Hessian_rows_used": True,
            "canonical_cutoff_start_rounding_replayed": True,
            "full_precision_direct_cut_periods_recomputed": True,
            "display_rounded_period_bounds_used_only_as_overlap_witnesses": True,
            "ordinary_main_rows_independently_replayed": True,
            "target_main_Hessian_interval_closed": True,
            "target_Frobenius_tail_Hessian_interval_closed": False,
            "target_full_Hessian_interval_closed": False,
            "full_76_target_chain_Hessian_interval_closed": False,
            "interval_Newton_existence_and_uniqueness_closed": False,
            "covariant_zero_proved": False,
            "full_SM_closure_proved": False,
        },
        "next_required_artifact": (
            "differentiate and certify the matching A135 log-free Frobenius tail, "
            "then splice it to this main Hessian interval"
        ),
    }
    dump(paths["output"], payload)
    paths["note"].write_text(
        f"# MTT q79 Height-Four d{arguments.index:03d} Main Hessian Interval (A380) v1\n\n"
        "This packet transports the five certified cutoff period coordinates once "
        "and simultaneously encloses the eight ordinary thimble rows and all 64 "
        "same-source covariant parameter derivatives from A378. The cutoff start "
        "uses the ordinary certificate's rounding convention, and its five Arb "
        "period balls are recomputed at full precision; display-rounded bounds are "
        "used only as independent overlap witnesses.\n\n"
        f"The maximum Hessian component radius is "
        f"`{np.max(hessian_radii):.12g}`. All eight ordinary rows overlap the "
        "independent canonical main certificate. No observed Standard Model value "
        "or fitted Jacobian entry is used.\n\n"
        "This closes the target's main-path Hessian. The A135 endpoint-tail "
        "derivative remains separate and is not silently absorbed into this result.\n",
        encoding="utf-8",
    )
    print(f"wrote {relative(paths['output'])}")
    print(f"wrote {relative(paths['note'])}")
    print(json.dumps(payload["summary"], indent=2))
    return payload


def parser() -> argparse.ArgumentParser:
    value = argparse.ArgumentParser()
    value.add_argument("--index", type=int, required=True)
    value.add_argument("--dps", type=int, default=90)
    value.add_argument("--order", type=int, default=20)
    value.add_argument("--maximum-step", type=float, default=0.003)
    value.add_argument("--minimum-step", type=float, default=1.0e-10)
    value.add_argument("--maximum-steps", type=int, default=50000)
    value.add_argument("--maximum-lift-correction", type=float, default=1.0e-6)
    value.add_argument("--maximum-output-increment", type=float, default=2.0e-3)
    value.add_argument("--maximum-output-radius", type=float, default=0.25)
    value.add_argument("--resume", action="store_true")
    value.add_argument("--smoke-only", action="store_true")
    return value


def main() -> int:
    arguments = parser().parse_args()
    if not 1 <= arguments.index <= 90:
        raise ValueError("index must lie in [1,90]")
    ctx.dps = arguments.dps
    a378 = load(A378)
    if not a378["strict_scope"][
        "all_64_homogeneous_period_hessian_integrand_rows_derived"
    ]:
        raise AssertionError("target Hessian transport requires A378")
    execute(arguments)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
