from __future__ import annotations

import json
import sys
from pathlib import Path

from flint import acb, acb_mat, arb

import certify_q79_selected_alignment_E32_thimble_polygonal_main_interval as polygonal
import certify_q79_selected_alignment_E32_thimble_polygonal_main_interval_node_pair as node_pair


ROOT = Path(__file__).resolve().parents[1]
PERIOD_DIRECTORY = (
    ROOT
    / "candidate_data"
    / "selected_q79covariantperiodbranchcutsetandtightbetatransport"
    / "selected_alignment_thimble_periods"
)


class PhysicalGeneratorFrame:
    def __init__(
        self,
        fundamental: acb_mat | None = None,
        coordinate_radii: list[arb] | None = None,
        *,
        blocks: list[acb_mat] | None = None,
    ) -> None:
        if blocks is not None:
            self.blocks = blocks
            return
        if fundamental is None or coordinate_radii is None:
            raise ValueError("physical-generator frame needs source data or blocks")
        dimension = len(coordinate_radii)
        diagonal = acb_mat(dimension, dimension)
        for index, radius in enumerate(coordinate_radii):
            diagonal[index, index] = acb(radius)
        self.blocks = [fundamental * diagonal]

    def row_radius(self, row: int) -> arb:
        return sum(
            (
                abs(block[row, column])
                for block in self.blocks
                for column in range(block.ncols())
            ),
            arb(0),
        )

    def physical_radius(self) -> arb:
        radii = [self.row_radius(row) for row in range(6)]
        return max(radii, key=polygonal.validated.upper)

    def physical_generator_matrix(self) -> acb_mat:
        # The caller only consumes row sums. A diagonal row-sum enclosure keeps
        # that interface without reboxing the frame during propagation.
        result = acb_mat(6, 6)
        for row in range(6):
            result[row, row] = acb(self.row_radius(row))
        return result


def diagonal_block(radius: arb) -> acb_mat:
    result = acb_mat(6, 6)
    for index in range(6):
        result[index, index] = acb(radius)
    return result


def validated_e32_zonotope_flow_step(
    system,
    start: complex,
    direction: complex,
    step: float,
    center: list[acb],
    input_frame: PhysicalGeneratorFrame,
    *,
    order: int,
):
    validated = polygonal.validated
    pilot = polygonal.pilot
    full_matrix, forcing, system_diagnostics = validated.build_taylor_system(
        system, start, direction, step, order
    )
    e32_state_index = 5 + polygonal.FORM_NAMES.index("E32")
    selected = [0, 1, 2, 3, 4, e32_state_index]
    matrix = [
        [full_matrix[row][column] for column in selected] for row in selected
    ]
    zero = forcing[0].constant(0, forcing[0].order, forcing[0].radius)
    state, fundamental = pilot.e32_candidate_flow_polynomials(
        matrix, [zero for _ in range(6)], center
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
    correction_upper = validated.upper(transformed_correction)
    rounding_upper = max(
        validated.radius_upper(value) for value in endpoint_state
    )
    correction_radius = arb(str(correction_upper))
    rounding_radius = arb(str(rounding_upper))
    output_blocks = [
        endpoint_fundamental * block for block in input_frame.blocks
    ]
    output_blocks.append(endpoint_fundamental * diagonal_block(correction_radius))
    output_blocks.append(diagonal_block(rounding_radius))
    output_frame = PhysicalGeneratorFrame(blocks=output_blocks)
    e32_radius = output_frame.row_radius(5)
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
        "physical_generator_block_count": len(output_blocks),
        "physical_generator_column_count": 6 * len(output_blocks),
        "error_frame_kind": "uncompressed physical-generator zonotope",
        "elliptic_residual_bound": validated.upper(
            validated.tm_vector_infinity_norm(state_residual)
        ),
        "elliptic_remainder_bound": validated.upper(forced_error),
    }
    return endpoint_center, output_frame, diagnostics


if __name__ == "__main__":
    if "--output" in sys.argv:
        raise AssertionError("zonotope wrapper currently requires the default output path")
    index = node_pair.argument_value("--distinguished-index", 4)
    selector, node_file = node_pair.certified_node_pair_selector(index)
    polygonal.pilot.closest_pair = selector
    polygonal.pilot.E32LiftErrorFrame = PhysicalGeneratorFrame
    polygonal.pilot.validated_e32_flow_step = validated_e32_zonotope_flow_step
    polygonal.__file__ = __file__
    result = polygonal.main()
    source = json.loads(node_pair.source_path(index).read_text(encoding="utf-8"))
    output = PERIOD_DIRECTORY / (
        f"d{index:03d}_{source['root_id']}.E32_main.interval.packet.json"
    )
    packet = json.loads(output.read_text(encoding="utf-8"))
    packet["authority"]["certified_node_pair_source"] = str(
        node_file.relative_to(ROOT)
    ).replace("\\", "/")
    packet["authority"]["certified_node_pair_source_sha256"] = node_pair.sha256(
        node_file
    )
    packet["scope"]["certified_nodal_pair_selector_consumed"] = True
    packet["scope"]["uncompressed_physical_generator_zonotope_consumed"] = True
    packet["validated_main_transport"]["certificate_method"] = (
        "six-dimensional augmented uncompressed physical-generator zonotope "
        "on a certified polygonal homotopy"
    )
    polygonal.dump(output, packet)
    raise SystemExit(result)
