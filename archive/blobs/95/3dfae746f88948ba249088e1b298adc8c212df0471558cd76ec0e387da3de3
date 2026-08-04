from __future__ import annotations

import argparse
import json
from pathlib import Path

import numpy as np
from flint import acb, ctx

import certify_q79_selected_alignment_E32_handle_combination_interval as handle
import certify_q79_selected_alignment_E32_primitive_handle_basis_intervals as basis
import certify_q79_selected_side_beta_defect_transport as validated


ROOT = basis.ROOT
PERIOD_DIRECTORY = basis.PERIOD_DIRECTORY


def step_label(step: float) -> str:
    return format(step, ".8g").replace(".", "p").replace("-", "m")


def output_path(
    rank: int,
    handle_name: str,
    candidate_id: str,
    order: int,
    initial_step: float,
) -> Path:
    return PERIOD_DIRECTORY / (
        f"height4_rank{rank}_{candidate_id}.{handle_name}_handle_direct."
        f"order{order}_step{step_label(initial_step)}.E32.interval.packet.json"
    )


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--rank", type=int, required=True)
    parser.add_argument("--handle", choices=["A", "B"], required=True)
    parser.add_argument("--order", type=int, default=44)
    parser.add_argument("--initial-step", type=float, default=0.005)
    parser.add_argument("--minimum-step", type=float, default=1.0e-9)
    parser.add_argument("--dps", type=int, default=100)
    parser.add_argument("--cut-segments", type=int, default=8)
    parser.add_argument("--cut-tolerance", type=float, default=1.0e-22)
    parser.add_argument("--output", type=Path)
    arguments = parser.parse_args()
    if arguments.order < 32:
        raise ValueError("refined handle order must be at least 32")
    if arguments.initial_step <= 0 or arguments.minimum_step <= 0:
        raise ValueError("handle steps must be positive")

    a208 = basis.load(basis.A208)
    rows = [
        row
        for row in a208["height_four_candidates"]
        if int(row["A132_objective_rank"]) == arguments.rank
    ]
    if len(rows) != 1:
        raise AssertionError("requested A208 survivor rank is not unique")
    candidate = rows[0]
    offset = 0 if arguments.handle == "A" else 4
    coordinates = [
        int(value)
        for value in candidate["primitive_handle_coordinates"][offset : offset + 4]
    ]
    if not any(coordinates):
        raise ValueError("requested refined handle component is identically zero")

    ctx.dps = arguments.dps
    system = validated.SelectedQ79IntervalSystem(dps=arguments.dps)
    base_cycles, base_diagnostics = basis.oriented_base_cycles(
        system,
        cut_segments=arguments.cut_segments,
        cut_tolerance=arguments.cut_tolerance,
    )
    initial = [acb(0) for _ in range(5)]
    for coefficient, cycle in zip(coordinates, base_cycles):
        for index, value in enumerate(cycle):
            initial[index] += acb(coefficient) * value
    endpoint = -1j if arguments.handle == "A" else 1 + 0j
    label = (
        f"rank{arguments.rank}:{arguments.handle}:{coordinates}:"
        f"order{arguments.order}:step{arguments.initial_step}"
    )
    center, radius, execution = basis.validated_handle_transport(
        system,
        initial,
        endpoint=endpoint,
        label=label,
        order=arguments.order,
        initial_step=arguments.initial_step,
        minimum_step=arguments.minimum_step,
    )
    value = handle.midpoint(center[5 + basis.E32_INDEX])
    radius_float = validated.upper(radius)
    ball = basis.interval_ball(value, radius_float)
    floating_packet = basis.load(basis.FLOATING_HANDLES)
    floating_matrix = np.asarray(
        [
            [handle.complex_value(item) for item in row]
            for row in floating_packet["primitive_handle_period_matrix"]
        ],
        dtype=np.complex128,
    )
    expected = floating_matrix[basis.E32_INDEX, offset : offset + 4] @ np.asarray(
        coordinates, dtype=np.float64
    )
    center_difference = float(abs(value - expected))
    if center_difference >= 2.0e-6:
        raise AssertionError("refined survivor handle interval disagrees with A131 center")

    output = arguments.output or output_path(
        arguments.rank,
        arguments.handle,
        candidate["candidate_id"],
        arguments.order,
        arguments.initial_step,
    )
    if not output.is_absolute():
        output = ROOT / output
    packet = {
        "schema": "MTTQ79SelectedAlignmentE32SurvivorRefinedHandleInterval.v1",
        "status": "SURVIVOR_REFINED_HANDLE_E32_INTERVAL_CERTIFIED",
        "candidate_id": candidate["candidate_id"],
        "A132_objective_rank": arguments.rank,
        "handle": arguments.handle,
        "authority": {
            "A208_survivor_queue": basis.relative(basis.A208),
            "A208_survivor_queue_sha256": basis.sha256(basis.A208),
            "A131_floating_handle_packet": basis.relative(basis.FLOATING_HANDLES),
            "A131_floating_handle_packet_sha256": basis.sha256(basis.FLOATING_HANDLES),
            "A131_orientation_packet": basis.relative(basis.ORIENTATION),
            "A131_orientation_packet_sha256": basis.sha256(basis.ORIENTATION),
            "basis_certifier_source": basis.relative(Path(basis.__file__).resolve()),
            "basis_certifier_source_sha256": basis.sha256(Path(basis.__file__).resolve()),
            "refined_certifier_source": basis.relative(Path(__file__).resolve()),
            "refined_certifier_source_sha256": basis.sha256(Path(__file__).resolve()),
        },
        "rigorous_base_cut_basis": base_diagnostics,
        "execution_parameters": {
            "dps": arguments.dps,
            "order": arguments.order,
            "initial_step": arguments.initial_step,
            "minimum_step": arguments.minimum_step,
            "cut_segments": arguments.cut_segments,
            "cut_tolerance": arguments.cut_tolerance,
        },
        "refined_handle_interval": {
            "primitive_coordinates": coordinates,
            "parameter_endpoint": handle.complex_pair(endpoint),
            "E32_interval": handle.complex_interval(ball),
            "E32_interval_center": handle.complex_pair(value),
            "E32_uniform_component_radius_upper": radius_float,
            "A131_floating_center": handle.complex_pair(expected),
            "A131_center_difference": center_difference,
            "transport": execution,
        },
        "scope": {
            "observed_SM_values_used": False,
            "candidate_specific_refined_handle_E32_interval_closed": True,
            "floating_center_accepted_as_exact_interval": False,
            "carrier_selected": False,
        },
    }
    basis.dump(output, packet)
    print(f"wrote {basis.relative(output)}")
    print(
        json.dumps(
            {
                "rank": arguments.rank,
                "handle": arguments.handle,
                "coordinates": coordinates,
                "order": arguments.order,
                "initial_step": arguments.initial_step,
                "radius": radius_float,
                "A131_center_difference": center_difference,
            },
            indent=2,
        )
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
