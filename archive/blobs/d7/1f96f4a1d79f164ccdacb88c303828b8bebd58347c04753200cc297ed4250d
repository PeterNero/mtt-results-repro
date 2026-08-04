from __future__ import annotations

import hashlib
import json
import math
from pathlib import Path

import numpy as np
from flint import acb, acb_mat, arb, ctx

import certify_q79_selected_alignment_E32_handle_combination_interval as legacy
import certify_q79_selected_side_beta_defect_transport as validated
from q79genus2_period_transport import FORM_NAMES


ROOT = Path(__file__).resolve().parents[1]
PERIOD_DIRECTORY = (
    ROOT
    / "candidate_data"
    / "selected_q79covariantperiodbranchcutsetandtightbetatransport"
    / "selected_alignment_thimble_periods"
)
A208 = PERIOD_DIRECTORY / "selected_alignment_height4_survivor_queue_and_E32_priority.packet.json"
FLOATING_HANDLES = PERIOD_DIRECTORY / "selected_alignment_primitive_handle_periods.packet.json"
ORIENTATION = PERIOD_DIRECTORY / "selected_alignment_thimble_orientation_synchronization.packet.json"
A207_HANDLE = PERIOD_DIRECTORY / "selected_alignment_E32_handle_combination.interval.packet.json"
PACKET = PERIOD_DIRECTORY / "selected_alignment_E32_primitive_handle_basis.intervals.packet.json"
CANDIDATE = ROOT / "candidate_data" / "selected_q79e32primitivehandlebasisintervals.candidate.json"
CERTIFICATE = ROOT / "certificates" / "selected_q79e32primitivehandlebasisintervals.certificate.json"
NOTE = ROOT / "proof_corpus" / "MTT_Selected_q79E32PrimitiveHandleBasisIntervals_A209_v1.md"
E32_INDEX = FORM_NAMES.index("E32")
HANDLE_ORDER = [
    "A:a1",
    "A:b1",
    "A:a2",
    "A:b2",
    "B:a1",
    "B:b1",
    "B:a2",
    "B:b2",
]


def load(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def dump(path: Path, value: dict) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(value, indent=2, sort_keys=True) + "\n", encoding="utf-8")


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def relative(path: Path) -> str:
    return str(path.relative_to(ROOT)).replace("\\", "/")


def interval_ball(center: complex, radius: float) -> acb:
    return acb(
        arb(format(center.real, ".17g"), format(radius, ".17g")),
        arb(format(center.imag, ".17g"), format(radius, ".17g")),
    )


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
    return matrix, [zero for _ in forcing], diagnostics


def validated_handle_transport(
    system: validated.SelectedQ79IntervalSystem,
    initial_periods: list[acb],
    *,
    endpoint: complex,
    label: str,
    order: int,
    initial_step: float,
    minimum_step: float,
) -> tuple[list[acb], arb, dict]:
    center = [system.midpoint_acb(value) for value in initial_periods] + [
        acb(0) for _ in range(8)
    ]
    identity = acb_mat(5, 5)
    for index in range(5):
        identity[index, index] = acb(1)
    lift_frame = validated.LiftErrorFrame(
        fundamental=identity,
        coordinate_radii=[value.rad().upper() for value in initial_periods],
    )
    integral_radius = arb(0)
    start = 0 + 0j
    if abs(endpoint) != 1.0:
        raise AssertionError("selected handle endpoint must have unit path length")
    direction = endpoint
    position = 0.0
    proposed = initial_step
    accepted: list[dict] = []
    rejected = 0
    minimum_accepted = math.inf
    original = validated.build_taylor_system
    validated.build_taylor_system = lambda *args, **kwargs: homogeneous_builder(
        original, *args, **kwargs
    )
    try:
        while position < 1.0:
            step = min(proposed, 1.0 - position)
            parameter_start = start + direction * position
            try:
                next_center, next_frame, next_radius, diagnostics = (
                    validated.validated_flow_step(
                        system,
                        parameter_start,
                        direction,
                        step,
                        center,
                        lift_frame,
                        integral_radius,
                        order=order,
                    )
                )
                if diagnostics["transformed_lift_correction"] > 1.0e-7:
                    raise ArithmeticError("handle lift correction exceeds budget")
                if diagnostics["beta_increment_error"] > 1.0e-5:
                    raise ArithmeticError("handle integral increment exceeds budget")
            except (ArithmeticError, ZeroDivisionError, ValueError):
                rejected += 1
                proposed = step / 2
                if proposed < minimum_step:
                    raise
                continue
            center = next_center
            lift_frame = next_frame
            integral_radius = next_radius
            position = min(1.0, position + step)
            minimum_accepted = min(minimum_accepted, step)
            accepted.append(
                {
                    "start_position": float(position - step),
                    "end_position": float(position),
                    "step": float(step),
                    **diagnostics,
                }
            )
            quality = max(
                diagnostics["reduction_neumann_norm"],
                diagnostics["fundamental_inverse_neumann_norm"],
            )
            proposed = min(initial_step, step * (1.5 if quality < 0.25 else 1.15))
            if len(accepted) % 25 == 0 or position == 1.0:
                print(
                    f"validated {label} steps={len(accepted)} position={position:.12g} "
                    f"step={step:.3e} radius={validated.upper(integral_radius):.3e}",
                    flush=True,
                )
    finally:
        validated.build_taylor_system = original

    return center, integral_radius, {
        "parameter_endpoint": legacy.complex_pair(endpoint),
        "accepted_step_count": len(accepted),
        "rejected_step_count": rejected,
        "minimum_accepted_step": minimum_accepted,
        "uniform_integral_radius_upper": validated.upper(integral_radius),
        "lift_radius_upper": validated.upper(lift_frame.physical_radius()),
        "steps": accepted,
    }


def oriented_base_cycles(
    system: validated.SelectedQ79IntervalSystem,
    *,
    cut_segments: int,
    cut_tolerance: float,
) -> tuple[list[list[acb]], dict]:
    roots, leading = legacy.selected_base_roots(system)
    marked_packet = load(ORIENTATION)
    marked = np.asarray(
        [
            [legacy.complex_value(value) for value in row]
            for row in marked_packet["marked_base_period_matrix"]
        ],
        dtype=np.complex128,
    )
    cut_specs = {
        "a2": ((0, 1), [0, 0, 1, 0]),
        "b2": ((1, 4), [0, 0, 0, 1]),
        "minus_a1_plus_a2": ((3, 4), [-1, 0, 1, 0]),
        "minus_a1_minus_b1": ((3, 5), [-1, -1, 0, 0]),
    }
    cuts: dict[str, list[acb]] = {}
    diagnostics = {}
    for name, (pair, coordinates) in cut_specs.items():
        print(f"certifying base cut {name} pair={pair}", flush=True)
        raw, direct_diagnostics = legacy.direct_cut_periods(
            roots,
            leading,
            pair,
            segments=cut_segments,
            tolerance=cut_tolerance,
        )
        reference = marked @ np.asarray(coordinates, dtype=np.float64)
        oriented, sign, selected, rejected = legacy.orient_cut(raw, reference)
        cuts[name] = oriented
        diagnostics[name] = {
            "marked_coordinates": coordinates,
            "orientation_sign": sign,
            "selected_center_error": selected,
            "rejected_center_error": rejected,
            **direct_diagnostics,
        }
        print(
            f"certified base cut {name} radius={direct_diagnostics['maximum_component_radius']:.3e}",
            flush=True,
        )

    a2 = cuts["a2"]
    b2 = cuts["b2"]
    a1 = [left - right for left, right in zip(a2, cuts["minus_a1_plus_a2"])]
    b1 = [
        -left - right
        for left, right in zip(a1, cuts["minus_a1_minus_b1"])
    ]
    basis = [a1, b1, a2, b2]
    center_errors = []
    for column, periods in enumerate(basis):
        center = np.asarray([legacy.midpoint(value) for value in periods])
        error = float(np.max(np.abs(center - marked[:, column])))
        if error >= 1.0e-6:
            raise AssertionError("rigorous cut basis disagrees with A131 marking")
        center_errors.append(error)
    return basis, {
        "basis_order": ["a1", "b1", "a2", "b2"],
        "basis_identity": {
            "a2": "cut(0,1)",
            "b2": "cut(1,4)",
            "a1": "cut(0,1)-cut(3,4)",
            "b1": "-a1-cut(3,5)",
        },
        "basis_center_errors_against_A131": center_errors,
        "cut_certificates": diagnostics,
    }


def main() -> int:
    ctx.dps = 90
    order = 32
    initial_step = 0.01
    minimum_step = 1.0e-8
    cut_segments = 8
    cut_tolerance = 1.0e-22
    a208 = load(A208)
    floating_packet = load(FLOATING_HANDLES)
    floating_matrix = np.asarray(
        [
            [legacy.complex_value(value) for value in row]
            for row in floating_packet["primitive_handle_period_matrix"]
        ],
        dtype=np.complex128,
    )
    if floating_packet["primitive_column_order"] != HANDLE_ORDER:
        raise AssertionError("A131 primitive handle order changed")

    partial_paths = [
        PERIOD_DIRECTORY
        / f"primitive_handle_{index:02d}_{label.replace(':', '_')}.E32.interval.packet.json"
        for index, label in enumerate(HANDLE_ORDER)
    ]
    if not all(path.exists() for path in partial_paths):
        missing = [relative(path) for path in partial_paths if not path.exists()]
        raise FileNotFoundError(f"primitive handle column packets missing: {missing}")
    partial_packets = [load(path) for path in partial_paths]
    base_diagnostics = partial_packets[0]["rigorous_base_cut_basis"]
    if any(
        packet["rigorous_base_cut_basis"] != base_diagnostics
        for packet in partial_packets[1:]
    ):
        raise AssertionError("primitive columns used different rigorous base-cut packets")
    primitive_rows = []
    primitive_balls: list[acb] = []
    for index, packet in enumerate(partial_packets):
        if not packet["scope"]["single_primitive_handle_E32_interval_closed"]:
            raise AssertionError(f"primitive handle column {index} is open")
        row = packet["primitive_E32_handle_interval"]
        if row["column_index"] != index or row["label"] != HANDLE_ORDER[index]:
            raise AssertionError("primitive handle column identity changed")
        primitive_rows.append(row)
        primitive_balls.append(validated.interval_from_bounds(row["E32_interval"]))

    survivor_rows = []
    for row in a208["height_four_candidates"]:
        coordinates = [int(value) for value in row["primitive_handle_coordinates"]]
        combination = acb(0)
        for coefficient, ball in zip(coordinates, primitive_balls):
            combination += acb(coefficient) * ball
        expected = floating_matrix[E32_INDEX] @ np.asarray(coordinates)
        center = legacy.midpoint(combination)
        center_difference = float(abs(center - expected))
        if center_difference >= 5.0e-6:
            raise AssertionError("survivor handle combination disagrees with A131")
        survivor_rows.append(
            {
                "candidate_id": row["candidate_id"],
                "A132_objective_rank": row["A132_objective_rank"],
                "primitive_handle_coordinates": coordinates,
                "E32_interval": legacy.complex_interval(combination),
                "E32_interval_center": legacy.complex_pair(center),
                "E32_interval_radius_upper": validated.radius_upper(combination),
                "A131_floating_center": legacy.complex_pair(expected),
                "A131_center_difference": center_difference,
            }
        )

    old_handle = load(A207_HANDLE)["E32_handle_combination"]
    old_center = legacy.complex_value(old_handle["interval"]["center"])
    old_radius = float(old_handle["interval"]["uniform_radius_upper"])
    first = survivor_rows[0]
    first_center = legacy.complex_value(first["E32_interval_center"])
    independent_intervals_overlap = (
        abs(first_center - old_center)
        <= float(first["E32_interval_radius_upper"]) + old_radius
    )
    if not independent_intervals_overlap:
        raise AssertionError("primitive-basis reconstruction misses the A207 handle interval")

    packet = {
        "schema": "MTTQ79SelectedAlignmentE32PrimitiveHandleBasisIntervals.v1",
        "status": "EIGHT_PRIMITIVE_HANDLE_E32_INTERVALS_AND_FIVE_COMBINATIONS_CERTIFIED",
        "artifact": "A209",
        "authority": {
            "A208_survivor_queue": relative(A208),
            "A208_survivor_queue_sha256": sha256(A208),
            "A131_floating_handle_packet": relative(FLOATING_HANDLES),
            "A131_floating_handle_packet_sha256": sha256(FLOATING_HANDLES),
            "A131_orientation_packet": relative(ORIENTATION),
            "A131_orientation_packet_sha256": sha256(ORIENTATION),
            "A207_handle_interval": relative(A207_HANDLE),
            "A207_handle_interval_sha256": sha256(A207_HANDLE),
            "certifier_source": relative(Path(__file__)),
            "certifier_source_sha256": sha256(Path(__file__)),
            "primitive_column_packets": {
                relative(path): sha256(path) for path in partial_paths
            },
        },
        "coordinate_identity": {
            "interval_parameter_to_elliptic_base": "w=1/4+i/4+i*t",
            "A_endpoint": "t=-i gives w=1/4+i/4+1",
            "B_endpoint": "t=1 gives w=1/4+i/4+i",
            "primitive_column_order": HANDLE_ORDER,
            "same_marked_base_fiber_basis_used_for_A_and_B": True,
        },
        "rigorous_base_cut_basis": base_diagnostics,
        "primitive_E32_handle_intervals": primitive_rows,
        "height_four_candidate_handle_combinations": survivor_rows,
        "A207_independent_cross_check": {
            "coordinates": [-1, 0, 1, 1, 0, 0, 0, 0],
            "primitive_basis_interval_overlaps_direct_A207_interval": independent_intervals_overlap,
            "direct_A207_center": old_handle["interval"]["center"],
            "direct_A207_radius_upper": old_radius,
        },
        "scope": {
            "observed_SM_values_used": False,
            "four_base_cut_cycles_interval_certified": True,
            "eight_primitive_handle_E32_intervals_certified": True,
            "five_A132_height_four_handle_combinations_certified": True,
            "A_and_B_paths_independently_transported": True,
            "floating_centers_accepted_as_exact_intervals": False,
            "survivor_thimble_combinations_certified": False,
            "survivor_E32_zero_decisions_closed": False,
        },
        "next_required_artifact": (
            "combine these handle intervals with the 15-row incremental thimble "
            "certificates and apply E32 zero-exclusion to all four A207 survivors"
        ),
    }
    dump(PACKET, packet)

    note = f"""# MTT Selected q79 E32 Primitive Handle Basis Intervals A209 v1

## Result

A209 certifies the E32 periods of all eight primitive A/B handle columns used by
the A130 integral basis. It starts from four interval-oriented base cuts,

```text
a2 = cut(0,1),
b2 = cut(1,4),
a1 = cut(0,1)-cut(3,4),
b1 = -a1-cut(3,5),
```

and transports each marked fiber cycle through the selected homogeneous
Gauss-Manin system. In the interval parameter `t`, the A path ends at `-i` and
the B path ends at `1`; under `w=1/4+i/4+i*t` these are exactly the selected
unit real and unit imaginary handle paths.

All eight primitive E32 intervals agree with the independently computed A131
floating centers within `1e-6`. Integer interval combinations are emitted for
all five A208 height-four rows. The published A132 combination independently
overlaps the sharper direct A207 handle interval.

This closes the survivor-specific handle dependency. It does not decide a
carrier: the corresponding thimble combinations and refined beta interval must
still be combined. No observed Standard Model value is used.
"""
    NOTE.write_text(note, encoding="utf-8")
    candidate = {
        "schema": "MTTSelectedQ79E32PrimitiveHandleBasisIntervals.v1",
        "status": packet["status"],
        "artifact": "A209",
        "packet": relative(PACKET),
        "packet_sha256": sha256(PACKET),
        "note": relative(NOTE),
        "note_sha256": sha256(NOTE),
        "what_closes": {
            "eight_primitive_E32_handle_intervals": True,
            "five_height_four_handle_combinations": True,
        },
        "what_remains_open": {
            "survivor_thimble_intervals": True,
            "survivor_E32_zero_decisions": True,
            "covariant_PGL3_zero_and_Jacobian": True,
        },
        "closure_claimed": False,
        "observed_SM_values_used": False,
        "next_required_artifact": packet["next_required_artifact"],
    }
    dump(CANDIDATE, candidate)
    certificate = {
        "schema": "MTTCertificate.v1",
        "certificate": "MTTSelectedQ79E32PrimitiveHandleBasisIntervals",
        "candidate_path": relative(CANDIDATE),
        "candidate_sha256": sha256(CANDIDATE),
        "status": candidate["status"],
        "closure_claimed": False,
        "observed_SM_values_used": False,
        "next_required_artifact": candidate["next_required_artifact"],
    }
    dump(CERTIFICATE, certificate)
    print(f"wrote {relative(PACKET)}")
    print(f"wrote {relative(CANDIDATE)}")
    print(f"wrote {relative(CERTIFICATE)}")
    print(f"wrote {relative(NOTE)}")
    print(
        json.dumps(
            {
                "primitive_intervals": len(primitive_rows),
                "candidate_combinations": len(survivor_rows),
                "maximum_primitive_radius": max(
                    row["E32_interval_radius_upper"] for row in primitive_rows
                ),
                "maximum_combination_radius": max(
                    row["E32_interval_radius_upper"] for row in survivor_rows
                ),
            },
            indent=2,
        )
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
