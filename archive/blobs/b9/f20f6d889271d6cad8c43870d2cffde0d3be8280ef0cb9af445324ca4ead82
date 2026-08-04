from __future__ import annotations

import argparse
import hashlib
import json
import math
from pathlib import Path

import numpy as np
from flint import acb, acb_mat, arb, ctx

import certify_q79_height4_d087_full_residue_main_interval as n3_engine
import certify_q79_selected_side_beta_defect_transport as validated
import q79_fast_taylor_runtime as fast
import run_q79_augmented_beta_transport as augmented


ROOT = Path(__file__).resolve().parents[1]
DIRECTORY = (
    ROOT
    / "candidate_data"
    / "selected_q79covariantperiodbranchcutsetandtightbetatransport"
    / "selected_alignment_thimble_periods"
    / "covariant_floating_probe"
    / "validated_transport"
)
SOURCE = DIRECTORY / "n3.beta_minus_B.source.a402s.json"
A401 = DIRECTORY / "n3.lower_b_contour_homotopy.a401.json"
A376 = DIRECTORY / "n3.rank3.anchored_beta.interval.json"
B_CHECKPOINT = DIRECTORY / "n3.handleB.hessian.checkpoint.json"
OUTPUT = DIRECTORY / "n3.beta_minus_B.augmented.a402.json"
CHECKPOINT = DIRECTORY / "n3.beta_minus_B.augmented.a402.ckpt.json"
SOURCE_AUDIT = ROOT / "proof_corpus" / "selected_q79heightfourbetaminusbhandlesource_audit.py"
FAST_AUDIT = ROOT / "proof_corpus" / "selected_q79fasttaylorruntime_equivalence_audit.py"
NOTE = ROOT / "proof_corpus" / "MTT_q79CorrelatedBetaMinusBHandleTransport_A402_v1.md"
ARTIFACT = "A402"


def load(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def relative(path: Path) -> str:
    return str(path.relative_to(ROOT)).replace("\\", "/")


def authority(path: Path) -> dict[str, str]:
    return {"path": relative(path), "sha256": sha256(path)}


def complex_value(value: dict[str, str]) -> complex:
    return complex(float(value["real"]), float(value["imaginary"]))


def common_waypoints() -> list[complex]:
    packet = load(A401)
    if not packet["strict_scope"]["A130_B_handle_may_use_A376_lower_contour"]:
        raise AssertionError("A401 no longer authorizes the common lower contour")
    return [
        complex(float(value["real"]), float(value["imaginary"]))
        for value in packet["contour_homotopy"]["selected_lower_waypoints"]
    ]


def initial_state() -> tuple[list[acb], validated.LiftErrorFrame]:
    source = load(SOURCE)
    if not source["strict_scope"]["beta_minus_B_initial_source_interval_closed"]:
        raise AssertionError("A402S source is not closed")
    balls = [
        validated.interval_from_bounds(value) for value in source["y_chart_base_lift"]
    ]
    center = [validated.SelectedQ79IntervalSystem.midpoint_acb(value) for value in balls]
    center.extend(acb(0) for _ in range(8))
    fundamental = acb_mat(5, 5)
    for index in range(5):
        fundamental[index, index] = acb(1)
    frame = validated.LiftErrorFrame(
        fundamental=fundamental,
        coordinate_radii=[value.rad().upper() for value in balls],
    )
    return center, frame


def lift_block_physical_radius(frame: validated.LiftErrorFrame) -> arb:
    generators = augmented.dynamic_generator_matrix(frame)
    return max(
        (
            sum(
                (abs(generators[row, column]) for column in range(generators.ncols())),
                arb(0),
            )
            for row in range(5)
        ),
        key=validated.upper,
    )


def row_scaled_matrix(matrix: acb_mat, scales: list[acb]) -> acb_mat:
    if matrix.nrows() != len(scales):
        raise ValueError("A402 row scaling dimension changed")
    return acb_mat(
        [
            [scales[row] * matrix[row, column] for column in range(matrix.ncols())]
            for row in range(matrix.nrows())
        ]
    )


def weighted_augmented_flow_step(
    system: validated.SelectedQ79IntervalSystem,
    start: complex,
    direction: complex,
    step: float,
    center: list[acb],
    input_lift_frame: validated.LiftErrorFrame,
    input_beta_radius: arb,
    *,
    order: int,
    residue_scale: float,
) -> tuple[list[acb], validated.LiftErrorFrame, arb, dict]:
    """Validate the triangular 5+8 system in a diagonal weighted norm."""
    if not 0.0 < residue_scale <= 1.0:
        raise ValueError("A402 residue scale must lie in (0,1]")
    matrix, forcing, system_diagnostics = validated.build_taylor_system(
        system, start, direction, step, order
    )
    if len(matrix) != 13 or len(center) != 13:
        raise AssertionError("A402 selected system is no longer 5+8 dimensional")
    physical_frame = augmented.expand_frame(input_lift_frame, input_beta_radius)
    scales = [acb(1) for _ in range(5)] + [
        acb(format(residue_scale, ".17g")) for _ in range(8)
    ]
    inverse_scales = [acb(1) / value for value in scales]
    scaled_matrix = [
        [
            matrix[row][column] * scales[row] * inverse_scales[column]
            for column in range(13)
        ]
        for row in range(13)
    ]
    scaled_forcing = [forcing[row] * scales[row] for row in range(13)]
    scaled_center = [center[row] * scales[row] for row in range(13)]
    scaled_input_frame = validated.LiftErrorFrame(
        fundamental=row_scaled_matrix(physical_frame.fundamental, scales),
        coordinate_radii=physical_frame.coordinate_radii.copy(),
    )

    state, fundamental = augmented.full_candidate_flow(
        scaled_matrix, scaled_forcing, scaled_center
    )
    state_derivative = validated.tm_vector_derivative(state)
    state_residual = [
        value + scaled_forcing[index] - state_derivative[index]
        for index, value in enumerate(
            validated.tm_matrix_vector_multiply(scaled_matrix, state)
        )
    ]
    fundamental_residual = validated.tm_matrix_subtract(
        validated.tm_matrix_multiply(scaled_matrix, fundamental),
        validated.tm_matrix_derivative(fundamental),
    )
    inverse_norm, inverse_defect = validated.tm_verified_inverse_bound(fundamental)
    linear_defect = inverse_norm * validated.tm_matrix_infinity_norm(
        fundamental_residual
    )
    affine_defect = inverse_norm * validated.tm_vector_infinity_norm(state_residual)
    step_ball = arb(format(step, ".17g"))
    growth = (linear_defect * step_ball).exp()
    forced_error = affine_defect * step_ball * growth
    input_radius = validated.acb_matrix_infinity_norm(
        augmented.dynamic_generator_matrix(scaled_input_frame)
    )
    transformed_correction = (growth - arb(1)) * input_radius + forced_error

    endpoint_state = [value.evaluate_polynomial(step_ball) for value in state]
    endpoint_fundamental = acb_mat(
        [
            [
                fundamental[row][column].evaluate_polynomial(step_ball)
                for column in range(13)
            ]
            for row in range(13)
        ]
    )
    output_scaled_fundamental = endpoint_fundamental * scaled_input_frame.fundamental
    output_scaled_inverse = output_scaled_fundamental.inv()
    correction_pullback = output_scaled_inverse * endpoint_fundamental
    rounding = arb(str(max(validated.radius_upper(value) for value in endpoint_state)))
    correction_upper = validated.upper(transformed_correction)
    rounding_upper = validated.upper(rounding)
    output_coordinate_radii = []
    for row in range(13):
        correction_norm = sum(
            (abs(correction_pullback[row, column]) for column in range(13)),
            arb(0),
        )
        rounding_norm = sum(
            (abs(output_scaled_inverse[row, column]) for column in range(13)),
            arb(0),
        )
        output_coordinate_radii.append(
            scaled_input_frame.coordinate_radii[row]
            + arb(str(correction_upper)) * correction_norm
            + arb(str(rounding_upper)) * rounding_norm
        )
    output_scaled_frame = validated.LiftErrorFrame(
        fundamental=output_scaled_fundamental,
        coordinate_radii=output_coordinate_radii,
    )
    output_frame = validated.LiftErrorFrame(
        fundamental=row_scaled_matrix(output_scaled_fundamental, inverse_scales),
        coordinate_radii=output_coordinate_radii,
    )
    input_components = augmented.component_radii(physical_frame)
    output_components = augmented.component_radii(output_frame)
    output_beta_radius = max(output_components[5:], key=validated.upper)
    output_lift_radius = lift_block_physical_radius(output_frame)
    beta_increment = max(
        0.0,
        max(
            validated.upper(output_components[index])
            - validated.upper(input_components[index])
            for index in range(5, 13)
        ),
    )
    endpoint_center = [
        validated.SelectedQ79IntervalSystem.midpoint_acb(
            endpoint_state[index] * inverse_scales[index]
        )
        for index in range(13)
    ]
    weighted_output_radius = validated.acb_matrix_infinity_norm(
        augmented.dynamic_generator_matrix(output_scaled_frame)
    )
    finite_values = [
        validated.upper(output_lift_radius),
        validated.upper(output_beta_radius),
        validated.upper(weighted_output_radius),
        *[validated.upper(value) for value in output_coordinate_radii],
    ]
    if not all(math.isfinite(value) for value in finite_values):
        raise ArithmeticError("A402 weighted augmented step produced a nonfinite bound")
    return endpoint_center, output_frame, output_beta_radius, {
        **system_diagnostics,
        "fundamental_inverse_neumann_norm": inverse_defect,
        "linear_defect_bound": validated.upper(linear_defect),
        "affine_defect_bound": validated.upper(affine_defect),
        "transformed_lift_correction": correction_upper,
        "input_lift_radius": validated.upper(lift_block_physical_radius(physical_frame)),
        "output_lift_radius": validated.upper(output_lift_radius),
        "weighted_input_state_radius": validated.upper(input_radius),
        "weighted_output_state_radius": validated.upper(weighted_output_radius),
        "input_beta_radius": validated.upper(input_beta_radius),
        "output_beta_radius": validated.upper(output_beta_radius),
        "beta_increment_error": beta_increment,
        "augmented_state_dimension": 13,
        "beta_component_radius_uppers": [
            validated.upper(value) for value in output_components[5:]
        ],
        "residue_coordinate_scale": residue_scale,
        "diagonal_weighted_norm_used": True,
        "full_affine_error_frame_used": True,
        "all_returned_bounds_finite": True,
    }


def smoke(
    system: validated.SelectedQ79IntervalSystem,
    order: int,
    residue_scale: float,
) -> dict:
    center, frame = initial_state()
    original_generator = validated.LiftErrorFrame.physical_generator_matrix
    original_radius = validated.LiftErrorFrame.physical_radius
    validated.LiftErrorFrame.physical_generator_matrix = augmented.dynamic_generator_matrix
    validated.LiftErrorFrame.physical_radius = lift_block_physical_radius
    try:
        endpoint, output_frame, output_radius, diagnostics = (
            weighted_augmented_flow_step(
                system,
                0 + 0j,
                1 + 0j,
                1.0e-4,
                center,
                frame,
                arb(0),
                order=order,
                residue_scale=residue_scale,
            )
        )
    finally:
        validated.LiftErrorFrame.physical_generator_matrix = original_generator
        validated.LiftErrorFrame.physical_radius = original_radius
    if len(endpoint) != 13 or output_frame.fundamental.nrows() != 13:
        raise AssertionError("the A402 smoke step did not preserve 13 states")
    return {
        "step": 1.0e-4,
        "order": order,
        "output_beta_radius_upper": validated.upper(output_radius),
        "output_lift_radius_upper": validated.upper(lift_block_physical_radius(output_frame)),
        "linear_defect_bound": diagnostics["linear_defect_bound"],
        "affine_defect_bound": diagnostics["affine_defect_bound"],
        "all_returned_bounds_finite": diagnostics["all_returned_bounds_finite"],
        "residue_coordinate_scale": residue_scale,
        "diagonal_weighted_norm_used": diagnostics["diagonal_weighted_norm_used"],
    }


def endpoint_overlap(
    packet: dict, component_radii: list[float]
) -> dict:
    beta = load(A376)
    b_checkpoint = load(B_CHECKPOINT)
    beta_centers = [complex_value(value) for value in beta["endpoint"]["beta_center"]]
    b_balls = [validated.decoded_acb(value) for value in b_checkpoint["center"][5:13]]
    b_centers = [validated.midpoint(value) for value in b_balls]
    joint_centers = [complex_value(value) for value in packet["endpoint"]["beta_center"]]
    beta_radius = float(beta["endpoint"]["uniform_component_radius_upper"])
    b_radii = [
        validated.upper(arb(value)) for value in b_checkpoint["output_radii"][:8]
    ]
    independent_radii = [beta_radius + value for value in b_radii]
    differences = [
        abs(joint - (left - right))
        for joint, left, right in zip(joint_centers, beta_centers, b_centers)
    ]
    overlaps = [
        difference <= independent + radius
        for difference, independent, radius in zip(
            differences, independent_radii, component_radii
        )
    ]
    if not all(overlaps):
        raise AssertionError("correlated endpoint misses the independent beta-minus-B boxes")
    maximum_joint = max(component_radii)
    maximum_independent = max(independent_radii)
    return {
        "independent_A376_beta_radius_upper": beta_radius,
        "independent_A383_B_component_radius_uppers": b_radii,
        "independent_triangle_component_radius_uppers": independent_radii,
        "maximum_independent_triangle_radius_upper": maximum_independent,
        "maximum_correlated_component_radius_upper": maximum_joint,
        "radius_tightening_factor": maximum_independent / maximum_joint,
        "strictly_tighter_than_independent_triangle_box": maximum_joint
        < maximum_independent,
        "maximum_center_difference": max(differences),
        "all_eight_endpoint_boxes_overlap": all(overlaps),
    }


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--dps", type=int, default=120)
    parser.add_argument("--order", type=int, default=48)
    parser.add_argument("--initial-step", type=float, default=0.01)
    parser.add_argument("--minimum-step", type=float, default=1.0e-12)
    parser.add_argument("--maximum-steps", type=int, default=50000)
    parser.add_argument("--residue-scale", type=float, default=0.1)
    parser.add_argument("--restart", action="store_true")
    parser.add_argument("--smoke-only", action="store_true")
    arguments = parser.parse_args()
    if arguments.dps < 70 or arguments.order < 24:
        raise ValueError("A402 requires at least 70 digits and Taylor order 24")
    ctx.dps = arguments.dps
    waypoints = common_waypoints()
    system = n3_engine.exact_target_system(arguments.dps)
    if not 0.0 < arguments.residue_scale <= 1.0:
        raise ValueError("A402 residue scale must lie in (0,1]")
    smoke_packet = smoke(system, min(arguments.order, 30), arguments.residue_scale)
    if arguments.smoke_only:
        print(json.dumps(smoke_packet, indent=2))
        return 0
    if arguments.restart and CHECKPOINT.exists():
        CHECKPOINT.unlink()

    source_fingerprint = sha256(SOURCE)[:16]
    builder_fingerprint = sha256(Path(__file__).resolve())[:16]
    path_name = (
        f"A402 exact n3 correlated beta-minus-B lower route dps={arguments.dps} "
        f"scale={arguments.residue_scale:.17g} source={source_fingerprint} "
        f"builder={builder_fingerprint}"
    )
    original_base_lift = validated.BASE_LIFT
    original_step = validated.validated_flow_step
    original_generator = validated.LiftErrorFrame.physical_generator_matrix
    original_radius = validated.LiftErrorFrame.physical_radius
    validated.BASE_LIFT = SOURCE
    validated.validated_flow_step = lambda *args, **kwargs: weighted_augmented_flow_step(
        *args, **kwargs, residue_scale=arguments.residue_scale
    )
    validated.LiftErrorFrame.physical_generator_matrix = augmented.dynamic_generator_matrix
    validated.LiftErrorFrame.physical_radius = lift_block_physical_radius
    fast.install()
    try:
        packet = validated.execute_validated_path(
            system,
            waypoints=waypoints,
            path_name=path_name,
            order=arguments.order,
            initial_step=arguments.initial_step,
            minimum_step=arguments.minimum_step,
            maximum_steps=arguments.maximum_steps,
            checkpoint_path=CHECKPOINT,
            resume=CHECKPOINT.exists(),
        )
    finally:
        fast.uninstall()
        validated.BASE_LIFT = original_base_lift
        validated.validated_flow_step = original_step
        validated.LiftErrorFrame.physical_generator_matrix = original_generator
        validated.LiftErrorFrame.physical_radius = original_radius

    serialization_radius = float(packet["endpoint"]["center_serialization_radius_upper"])
    final_step = packet["execution"]["steps"][-1]
    component_radii = [
        float(value) + serialization_radius
        for value in final_step["beta_component_radius_uppers"]
    ]
    if len(component_radii) != 8 or not all(math.isfinite(value) for value in component_radii):
        raise AssertionError("A402 did not emit eight finite component radii")
    comparison = endpoint_overlap(packet, component_radii)

    packet.update(
        {
            "schema": "MTTQ79CorrelatedBetaMinusBHandleTransportInterval.v1",
            "status": "N3_CORRELATED_BETA_MINUS_B_HANDLE_INTERVAL_EXECUTED",
            "artifact": ARTIFACT,
            "source_theorem": {
                "source_artifact": "A402S",
                "identity": "I_rel(1) = beta(1) - H_B(1)",
                "same_A401_lower_contour_used": True,
                "exact_n3_interval_system_used": True,
                "full_13_state_affine_error_frame_used": True,
                "exact_diagonal_weighted_coordinate_conjugation_used": True,
            },
            "smoke_test": smoke_packet,
            "comparison_to_independent_boxes": comparison,
            "execution_configuration": {
                "dps": arguments.dps,
                "order": arguments.order,
                "initial_step": arguments.initial_step,
                "minimum_step": arguments.minimum_step,
                "maximum_steps": arguments.maximum_steps,
                "residue_coordinate_scale": arguments.residue_scale,
                "path_name": path_name,
                "checkpoint": relative(CHECKPOINT),
                "checkpoint_sha256": sha256(CHECKPOINT),
            },
            "authority": {
                "A402S_correlated_source": authority(SOURCE),
                "A402S_independent_audit": authority(SOURCE_AUDIT),
                "A401_common_contour_homotopy": authority(A401),
                "A376_independent_beta_interval": authority(A376),
                "A383_validated_B_path_checkpoint": authority(B_CHECKPOINT),
                "n3_exact_fibration": authority(n3_engine.FIBRATION),
                "n3_interval_system": authority(Path(n3_engine.__file__).resolve()),
                "validated_transport_engine": authority(Path(validated.__file__).resolve()),
                "augmented_affine_transport_engine": authority(Path(augmented.__file__).resolve()),
                "C_backed_Taylor_runtime": authority(Path(fast.__file__).resolve()),
                "C_backed_Taylor_equivalence_audit": authority(FAST_AUDIT),
                "builder_source": authority(Path(__file__).resolve()),
            },
            "strict_scope": {
                "observed_SM_values_used": False,
                "A402S_correlated_source_consumed": True,
                "A401_common_contour_consumed": True,
                "exact_n3_interval_system_used": True,
                "full_13_state_affine_error_frame_used": True,
                "exact_diagonal_weighted_coordinate_conjugation_used": True,
                "joint_beta_minus_B_handle_transport_executed": True,
                "all_eight_endpoint_boxes_overlap_independent_execution": comparison[
                    "all_eight_endpoint_boxes_overlap"
                ],
                "full_relative_chain_transport_executed": False,
                "interval_Newton_existence_and_uniqueness_closed": False,
                "covariant_zero_proved": False,
                "full_SM_closure_proved": False,
            },
            "next_required_artifact": (
                "combine this correlated beta-minus-B block with the selected "
                "A-handle, 76-thimble chain, and wall correction on common paths"
            ),
        }
    )
    packet["endpoint"]["component_radius_uppers"] = component_radii
    packet["endpoint"]["uniform_component_radius_upper"] = format(
        max(component_radii), ".17g"
    )
    OUTPUT.write_text(json.dumps(packet, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    NOTE.write_text(
        "# MTT q79 Correlated Beta Minus B-Handle Transport (A402) v1\n\n"
        "A402 transports the A402S shifted lift on the exact n3 system and the "
        "A401 common lower contour. The resulting eight outputs are therefore "
        "the correlated interval for `beta-H_B`, not a post hoc subtraction of "
        "independent endpoint boxes.\n\n"
        f"The maximum correlated component radius is `{max(component_radii):.12g}`; "
        f"the independent triangle-box radius is "
        f"`{comparison['maximum_independent_triangle_radius_upper']:.12g}`. The full "
        "relative-chain transport and interval-Newton zero theorem remain open.\n",
        encoding="utf-8",
    )
    print(json.dumps(comparison, indent=2), flush=True)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
