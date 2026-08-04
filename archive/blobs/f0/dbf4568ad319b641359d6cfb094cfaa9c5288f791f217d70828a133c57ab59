from __future__ import annotations

import argparse
import json
from pathlib import Path

import numpy as np
from flint import ctx

import certify_q79_selected_alignment_E32_handle_combination_interval as handle
import certify_q79_selected_alignment_E32_primitive_handle_basis_intervals as basis
import certify_q79_selected_side_beta_defect_transport as validated


ROOT = basis.ROOT
PERIOD_DIRECTORY = basis.PERIOD_DIRECTORY


def partial_path(index: int) -> Path:
    label = basis.HANDLE_ORDER[index].replace(":", "_")
    return PERIOD_DIRECTORY / f"primitive_handle_{index:02d}_{label}.E32.interval.packet.json"


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--column-index", type=int, required=True)
    parser.add_argument("--output", type=Path)
    arguments = parser.parse_args()
    index = arguments.column_index
    if index < 0 or index >= len(basis.HANDLE_ORDER):
        raise ValueError("primitive handle column index must lie in [0,7]")

    ctx.dps = 90
    system = validated.SelectedQ79IntervalSystem(dps=90)
    base_cycles, base_diagnostics = basis.oriented_base_cycles(
        system,
        cut_segments=8,
        cut_tolerance=1.0e-22,
    )
    handle_name = "A" if index < 4 else "B"
    local_index = index % 4
    endpoint = -1j if handle_name == "A" else 1 + 0j
    label = basis.HANDLE_ORDER[index]
    center, radius, execution = basis.validated_handle_transport(
        system,
        base_cycles[local_index],
        endpoint=endpoint,
        label=label,
        order=32,
        initial_step=0.01,
        minimum_step=1.0e-8,
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
    expected = floating_matrix[basis.E32_INDEX, index]
    center_difference = float(abs(value - expected))
    if center_difference >= 1.0e-6:
        raise AssertionError(f"{label} E32 interval disagrees with A131 center")

    output = arguments.output or partial_path(index)
    if not output.is_absolute():
        output = ROOT / output
    packet = {
        "schema": "MTTQ79SelectedAlignmentE32PrimitiveHandleColumnInterval.v1",
        "status": "PRIMITIVE_HANDLE_E32_COLUMN_INTERVAL_CERTIFIED",
        "column_index": index,
        "label": label,
        "authority": {
            "A131_floating_handle_packet": basis.relative(basis.FLOATING_HANDLES),
            "A131_floating_handle_packet_sha256": basis.sha256(basis.FLOATING_HANDLES),
            "A131_orientation_packet": basis.relative(basis.ORIENTATION),
            "A131_orientation_packet_sha256": basis.sha256(basis.ORIENTATION),
            "basis_certifier_source": basis.relative(Path(basis.__file__).resolve()),
            "basis_certifier_source_sha256": basis.sha256(Path(basis.__file__).resolve()),
            "column_certifier_source": basis.relative(Path(__file__)),
            "column_certifier_source_sha256": basis.sha256(Path(__file__)),
        },
        "rigorous_base_cut_basis": base_diagnostics,
        "primitive_E32_handle_interval": {
            "column_index": index,
            "label": label,
            "handle": handle_name,
            "fiber_cycle": base_diagnostics["basis_order"][local_index],
            "parameter_endpoint": handle.complex_pair(endpoint),
            "E32_interval": handle.complex_interval(ball),
            "E32_interval_center": handle.complex_pair(value),
            "E32_interval_radius_upper": radius_float,
            "A131_floating_center": handle.complex_pair(expected),
            "A131_center_difference": center_difference,
            "transport": execution,
        },
        "scope": {
            "observed_SM_values_used": False,
            "single_primitive_handle_E32_interval_closed": True,
            "floating_center_accepted_as_exact_interval": False,
        },
    }
    basis.dump(output, packet)
    print(f"wrote {basis.relative(output)}")
    print(
        json.dumps(
            {
                "column_index": index,
                "label": label,
                "radius": radius_float,
                "A131_center_difference": center_difference,
            },
            indent=2,
        )
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
