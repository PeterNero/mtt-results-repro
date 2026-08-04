from __future__ import annotations

import argparse
import hashlib
import json
import math
from pathlib import Path

import numpy as np
from flint import acb, acb_mat, arb, ctx

import certify_q79_selected_side_beta_defect_transport as validated
import q79_fast_taylor_runtime as fast


ROOT = Path(__file__).resolve().parents[1]
DIRECTORY = (
    ROOT
    / "candidate_data"
    / "selected_q79covariantperiodbranchcutsetandtightbetatransport"
    / "selected_alignment_thimble_periods"
    / "covariant_floating_probe"
    / "validated_transport"
)
OUTPUT = DIRECTORY / "n3.beta.augmented.a392.json"
CHECKPOINT = DIRECTORY / "n3.beta.augmented.a392.ckpt.json"
NOTE = ROOT / "proof_corpus" / "MTT_q79AugmentedBetaTransport_A392_v1.md"
A376 = DIRECTORY / "n3.rank3.anchored_beta.interval.json"
A379 = DIRECTORY / "n3.beta_hessian.interval.json"
FAST_AUDIT = ROOT / "proof_corpus" / "selected_q79fasttaylorruntime_equivalence_audit.py"
ARTIFACT = "A392"
WAYPOINTS = [
    0 + 0j,
    0.65 + 0j,
    0.65 - 0.1j,
    0.82 - 0.1j,
    0.82 + 0j,
    1 + 0j,
]


def load(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def relative(path: Path) -> str:
    return str(path.relative_to(ROOT)).replace("\\", "/")


def authority(path: Path) -> dict[str, str]:
    return {"path": relative(path), "sha256": sha256(path)}


def dynamic_generator_matrix(frame: validated.LiftErrorFrame) -> acb_mat:
    dimension = frame.fundamental.nrows()
    if frame.fundamental.ncols() != dimension or len(frame.coordinate_radii) != dimension:
        raise ValueError("augmented error frame dimensions disagree")
    diagonal = acb_mat(dimension, dimension)
    for index, radius in enumerate(frame.coordinate_radii):
        diagonal[index, index] = acb(radius)
    return frame.fundamental * diagonal


def dynamic_physical_radius(frame: validated.LiftErrorFrame) -> arb:
    return validated.acb_matrix_infinity_norm(dynamic_generator_matrix(frame))


def component_radii(frame: validated.LiftErrorFrame) -> list[arb]:
    generators = dynamic_generator_matrix(frame)
    return [
        sum((abs(generators[row, column]) for column in range(generators.ncols())), arb(0))
        for row in range(generators.nrows())
    ]


def full_candidate_flow(
    matrix: list[list[validated.TaylorModel]],
    forcing: list[validated.TaylorModel],
    initial_center: list[acb],
) -> tuple[list[validated.TaylorModel], list[list[validated.TaylorModel]]]:
    order = matrix[0][0].order
    radius = matrix[0][0].radius
    dimension = len(matrix)
    if any(len(row) != dimension for row in matrix) or len(initial_center) != dimension:
        raise ValueError("augmented Taylor system is not square")
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


def expand_frame(
    frame: validated.LiftErrorFrame, input_beta_radius: arb
) -> validated.LiftErrorFrame:
    if frame.fundamental.nrows() == 13:
        return frame
    if frame.fundamental.nrows() != 5 or len(frame.coordinate_radii) != 5:
        raise ValueError("unexpected initial error-frame dimension")
    fundamental = acb_mat(13, 13)
    for row in range(5):
        for column in range(5):
            fundamental[row, column] = frame.fundamental[row, column]
    for index in range(5, 13):
        fundamental[index, index] = acb(1)
    return validated.LiftErrorFrame(
        fundamental=fundamental,
        coordinate_radii=[*frame.coordinate_radii, *[arb(input_beta_radius) for _ in range(8)]],
    )


def augmented_validated_flow_step(
    system: validated.SelectedQ79IntervalSystem,
    start: complex,
    direction: complex,
    step: float,
    center: list[acb],
    input_lift_frame: validated.LiftErrorFrame,
    input_beta_radius: arb,
    *,
    order: int,
) -> tuple[list[acb], validated.LiftErrorFrame, arb, dict]:
    matrix, forcing, system_diagnostics = validated.build_taylor_system(
        system, start, direction, step, order
    )
    if len(matrix) != 13 or len(center) != 13:
        raise AssertionError("selected beta system is no longer 5+8 dimensional")
    frame = expand_frame(input_lift_frame, input_beta_radius)
    state, fundamental = full_candidate_flow(matrix, forcing, center)
    state_derivative = validated.tm_vector_derivative(state)
    state_residual = [
        value + forcing[index] - state_derivative[index]
        for index, value in enumerate(
            validated.tm_matrix_vector_multiply(matrix, state)
        )
    ]
    fundamental_residual = validated.tm_matrix_subtract(
        validated.tm_matrix_multiply(matrix, fundamental),
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
    input_radius = frame.physical_radius()
    transformed_error = growth * input_radius + forced_error
    transformed_correction = (growth - arb(1)) * input_radius + forced_error

    endpoint = step_ball
    endpoint_state = [value.evaluate_polynomial(endpoint) for value in state]
    endpoint_fundamental = acb_mat(
        [
            [fundamental[row][column].evaluate_polynomial(endpoint) for column in range(13)]
            for row in range(13)
        ]
    )
    output_fundamental = endpoint_fundamental * frame.fundamental
    output_inverse = output_fundamental.inv()
    correction_pullback = output_inverse * endpoint_fundamental
    rounding = arb(str(max(validated.radius_upper(value) for value in endpoint_state)))
    correction_upper = validated.upper(transformed_correction)
    rounding_upper = validated.upper(rounding)
    output_coordinate_radii = []
    for row in range(13):
        correction_norm = sum(
            (abs(correction_pullback[row, column]) for column in range(13)), arb(0)
        )
        rounding_norm = sum(
            (abs(output_inverse[row, column]) for column in range(13)), arb(0)
        )
        output_coordinate_radii.append(
            frame.coordinate_radii[row]
            + arb(str(correction_upper)) * correction_norm
            + arb(str(rounding_upper)) * rounding_norm
        )
    output_frame = validated.LiftErrorFrame(
        fundamental=output_fundamental,
        coordinate_radii=output_coordinate_radii,
    )
    input_components = component_radii(frame)
    output_components = component_radii(output_frame)
    output_beta_radius = max(output_components[5:], key=validated.upper)
    beta_increment = max(
        0.0,
        max(
            validated.upper(output_components[index])
            - validated.upper(input_components[index])
            for index in range(5, 13)
        ),
    )
    endpoint_center = [
        validated.SelectedQ79IntervalSystem.midpoint_acb(value)
        for value in endpoint_state
    ]
    finite_values = [
        validated.upper(output_frame.physical_radius()),
        validated.upper(output_beta_radius),
        *[validated.upper(value) for value in output_coordinate_radii],
    ]
    if not all(math.isfinite(value) for value in finite_values):
        raise ArithmeticError("augmented beta step produced a nonfinite bound")
    return endpoint_center, output_frame, output_beta_radius, {
        **system_diagnostics,
        "fundamental_inverse_neumann_norm": inverse_defect,
        "linear_defect_bound": validated.upper(linear_defect),
        "affine_defect_bound": validated.upper(affine_defect),
        "transformed_lift_correction": correction_upper,
        "input_lift_radius": validated.upper(input_radius),
        "output_lift_radius": validated.upper(output_frame.physical_radius()),
        "input_beta_radius": validated.upper(input_beta_radius),
        "output_beta_radius": validated.upper(output_beta_radius),
        "beta_increment_error": beta_increment,
        "augmented_state_dimension": 13,
        "beta_component_radius_uppers": [
            validated.upper(value) for value in output_components[5:]
        ],
        "full_affine_error_frame_used": True,
        "all_returned_bounds_finite": True,
    }


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--dps", type=int, default=120)
    parser.add_argument("--order", type=int, default=48)
    parser.add_argument("--initial-step", type=float, default=0.01)
    parser.add_argument("--minimum-step", type=float, default=1.0e-12)
    parser.add_argument("--maximum-steps", type=int, default=50000)
    parser.add_argument("--restart", action="store_true")
    arguments = parser.parse_args()
    if arguments.dps < 70 or arguments.order < 24:
        raise ValueError("A392 requires at least 70 digits and Taylor order 24")
    ctx.dps = arguments.dps
    if arguments.restart and CHECKPOINT.exists():
        CHECKPOINT.unlink()
    source_fingerprint = sha256(Path(validated.__file__).resolve())[:16]
    builder_fingerprint = sha256(Path(__file__).resolve())[:16]
    path_name = (
        f"A392 augmented selected A379 route dps={arguments.dps} "
        f"source={source_fingerprint} builder={builder_fingerprint}"
    )
    original_step = validated.validated_flow_step
    original_generator = validated.LiftErrorFrame.physical_generator_matrix
    original_radius = validated.LiftErrorFrame.physical_radius
    validated.validated_flow_step = augmented_validated_flow_step
    validated.LiftErrorFrame.physical_generator_matrix = dynamic_generator_matrix
    validated.LiftErrorFrame.physical_radius = dynamic_physical_radius
    fast.install()
    try:
        system = validated.SelectedQ79IntervalSystem(dps=arguments.dps)
        packet = validated.execute_validated_path(
            system,
            waypoints=WAYPOINTS,
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
        validated.validated_flow_step = original_step
        validated.LiftErrorFrame.physical_generator_matrix = original_generator
        validated.LiftErrorFrame.physical_radius = original_radius

    reference = load(A379)
    old_maximum = float(reference["summary"]["maximum_beta_component_radius_upper"])
    new_maximum = float(packet["endpoint"]["uniform_component_radius_upper"])
    serialization_radius = float(
        packet["endpoint"]["center_serialization_radius_upper"]
    )
    final_components = [
        float(value) + serialization_radius
        for value in packet["execution"]["steps"][-1][
            "beta_component_radius_uppers"
        ]
    ]
    packet.update(
        {
            "artifact": ARTIFACT,
            "schema": "MTTQ79AugmentedBetaTransportInterval.v1",
            "status": "N3_AUGMENTED_13_STATE_BETA_INTERVAL_EXECUTED",
            "comparison_to_A379": {
                "A379_maximum_beta_component_radius_upper": old_maximum,
                "A392_maximum_beta_component_radius_upper": new_maximum,
                "radius_tightening_factor": old_maximum / new_maximum,
                "strictly_tighter_than_A379": new_maximum < old_maximum,
            },
            "execution_configuration": {
                "dps": arguments.dps,
                "order": arguments.order,
                "initial_step": arguments.initial_step,
                "minimum_step": arguments.minimum_step,
                "maximum_steps": arguments.maximum_steps,
                "path_name": path_name,
                "checkpoint": relative(CHECKPOINT),
                "checkpoint_sha256": sha256(CHECKPOINT),
            },
            "authority": {
                "A376_prior_beta_interval": authority(A376),
                "A379_beta_Hessian_interval": authority(A379),
                "selected_base_lift": authority(validated.BASE_LIFT),
                "validated_beta_transport_source": authority(
                    Path(validated.__file__).resolve()
                ),
                "C_backed_Taylor_runtime": authority(Path(fast.__file__).resolve()),
                "C_backed_Taylor_equivalence_audit": authority(FAST_AUDIT),
                "builder_source": authority(Path(__file__).resolve()),
            },
            "strict_scope": {
                "same_A379_selected_route_used": True,
                "same_selected_beta_differential_system_used": True,
                "full_13_state_affine_error_frame_used": True,
                "eight_component_beta_radii_emitted": len(final_components) == 8,
                "strictly_tighter_than_A379": new_maximum < old_maximum,
                "observed_SM_values_used": False,
                "coupled_beta_period_residual_transport_closed": False,
                "interval_Newton_existence_and_uniqueness_closed": False,
                "covariant_zero_proved": False,
                "full_SM_closure_proved": False,
            },
            "next_required_artifact": (
                "replace the A379 ordinary beta rows in A386 and quantify the "
                "remaining 76-cycle and handle widths"
                if new_maximum < old_maximum
                else "retain A379 and build the coupled beta-period residual ODE"
            ),
        }
    )
    packet["endpoint"]["component_radius_uppers"] = final_components
    OUTPUT.write_text(
        json.dumps(packet, indent=2, sort_keys=True) + "\n", encoding="utf-8"
    )
    NOTE.write_text(
        "# MTT q79 Augmented Beta Transport (A392) v1\n\n"
        "A392 executes the same selected beta differential system as A379, but "
        "tracks the five lift and eight beta coordinates in one 13-dimensional "
        "validated affine error frame. This preserves lift-to-beta correlations "
        "that the prior monotone scalar beta radius discarded.\n\n"
        f"The maximum beta radius changes from `{old_maximum:.12g}` to "
        f"`{new_maximum:.12g}`, a tightening factor of "
        f"`{old_maximum / new_maximum:.12g}`.\n\n"
        "This improves only the beta value enclosure. It does not yet couple the "
        "beta to the 76-cycle period or prove a Krawczyk self-map.\n",
        encoding="utf-8",
    )
    print(json.dumps(packet["comparison_to_A379"], indent=2), flush=True)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
