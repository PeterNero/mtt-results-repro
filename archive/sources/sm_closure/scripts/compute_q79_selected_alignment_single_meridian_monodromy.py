from __future__ import annotations

import argparse
import hashlib
import json
import math
import time
from pathlib import Path

import numpy as np
import sympy as sp

from q79_selected_alignment_genus2_root_transport import (
    Q79SelectedAlignmentRootTransport,
    load,
)
from q79genus2_root_transport import free_reduce, matrix_rows


ROOT = Path(__file__).resolve().parents[1]
DIRECTORY = (
    ROOT
    / "candidate_data"
    / "selected_q79covariantperiodbranchcutsetandtightbetatransport"
)
FIBRATION = DIRECTORY / "selected_alignment_genus2_fibration_seed.interval.packet.json"
FAN = DIRECTORY / "selected_alignment_distinguished_radial_fan.interval.packet.json"
HOMOLOGY = (
    ROOT
    / "candidate_data"
    / "selected_q79genus2picardlefschetzmonodromyexecution"
    / "numerical_monodromy_exploration.packet.json"
)
OUTPUT = DIRECTORY / "selected_alignment_meridian_monodromy"


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def encoded_complex(value: complex) -> dict[str, str]:
    return {
        "real": format(value.real, ".17g"),
        "imaginary": format(value.imag, ".17g"),
    }


def decoded_complex(value: dict[str, str]) -> complex:
    return complex(float(value["real"]), float(value["imaginary"]))


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--root-id", required=True)
    parser.add_argument("--step-ratio", type=float, default=0.14)
    parser.add_argument("--coarse-outbound", type=int, default=48)
    parser.add_argument("--coarse-circle", type=int, default=128)
    parser.add_argument("--circle-scale", type=float, default=1.0)
    parser.add_argument("--omitted-real", type=float, default=2.0)
    parser.add_argument("--omitted-imag", type=float, default=3.0)
    parser.add_argument("--dps", type=int, default=70)
    parser.add_argument("--no-save", action="store_true")
    arguments = parser.parse_args()
    if not 0 < arguments.step_ratio < 0.4:
        raise AssertionError("step ratio must lie in (0,0.4)")
    if not 0 < arguments.circle_scale <= 1:
        raise AssertionError("circle scale must lie in (0,1]")

    started = time.perf_counter()
    fan = load(FAN)
    homology_packet = load(HOMOLOGY)
    path = next(
        row
        for row in fan["distinguished_positive_meridians"]
        if row["root_id"] == arguments.root_id
    )
    index = int(path["distinguished_index"])
    transport = Q79SelectedAlignmentRootTransport(
        FIBRATION,
        homology_packet["homology_convention"],
        omitted=complex(arguments.omitted_real, arguments.omitted_imag),
        dps=arguments.dps,
    )

    points: list[complex] = [transport.base]
    trajectories: list[np.ndarray] = [transport.base_roots.copy()]
    radii_rows: list[list[float]] = [transport.base_radii.copy()]
    ratio_state = [0.0]
    previous = transport.base_roots

    circle = path["positive_meridian"]
    center = decoded_complex(circle["center"])
    radius = float(circle["radius"]) * arguments.circle_scale
    start_angle = float(circle["start_angle"])
    outbound_end = center + radius * np.exp(1j * start_angle)
    outbound_grid = np.linspace(
        transport.base,
        outbound_end,
        arguments.coarse_outbound + 1,
    )
    for start, end in zip(outbound_grid, outbound_grid[1:]):
        previous = transport.advance(
            complex(start),
            complex(end),
            previous,
            points,
            trajectories,
            radii_rows,
            arguments.step_ratio,
            ratio_state,
        )
    outbound_points = list(points)
    outbound_roots = [row.copy() for row in trajectories]
    outbound_radii = [list(row) for row in radii_rows]
    outbound_point_count = len(points)
    outbound_word, outbound_order, outbound_event_gap = transport.braid_word(
        outbound_roots
    )

    circle_points = [
        center
        + radius
        * np.exp(
            1j
            * (
                start_angle
                + 2 * math.pi * step / arguments.coarse_circle
            )
        )
        for step in range(arguments.coarse_circle + 1)
    ]
    circle_points[0] = outbound_end
    circle_points[-1] = outbound_end
    circle_trajectory_start = len(trajectories) - 1
    for start, end in zip(circle_points, circle_points[1:]):
        previous = transport.advance(
            complex(start),
            complex(end),
            previous,
            points,
            trajectories,
            radii_rows,
            arguments.step_ratio,
            ratio_state,
        )
    circle_point_count = len(points) - outbound_point_count + 1
    circle_trajectories = trajectories[circle_trajectory_start:]
    circle_word, _circle_order, circle_event_gap = transport.braid_word(
        circle_trajectories,
        initial_order=outbound_order,
    )

    reused_reverse_steps = 0
    for outbound_index in range(len(outbound_points) - 2, -1, -1):
        current, radii, ratio = transport.match(
            previous,
            outbound_roots[outbound_index],
            outbound_radii[outbound_index],
        )
        if ratio >= 0.44:
            raise AssertionError("selected reverse matching is not unique")
        ratio_state[0] = max(ratio_state[0], ratio)
        points.append(outbound_points[outbound_index])
        trajectories.append(current)
        radii_rows.append(radii)
        previous = current
        reused_reverse_steps += 1

    reverse_outbound_word = [
        (generator, -sign) for generator, sign in reversed(outbound_word)
    ]
    word = outbound_word + circle_word + reverse_outbound_word
    minimum_event_gap = min(outbound_event_gap, circle_event_gap)
    final_order = list(range(6))
    for generator, _sign in word:
        position = generator - 1
        final_order[position], final_order[position + 1] = (
            final_order[position + 1],
            final_order[position],
        )
    reduced = free_reduce(word)
    action = sp.Matrix(transport.action(word).tolist())
    final_permutation = transport.endpoint_permutation(trajectories[-1])
    intersection = sp.Matrix(
        homology_packet["homology_convention"]["intersection_matrix"]
    )
    delta = action - sp.eye(4)
    if action.T * intersection * action != intersection:
        raise AssertionError("selected local action is not symplectic")
    if delta.rank() != 1 or delta * delta != sp.zeros(4):
        raise AssertionError(
            "selected local action is not a Lefschetz transvection: "
            f"rank={delta.rank()} matrix={matrix_rows(action)} "
            f"permutation={final_permutation} raw_word={word}"
        )
    if sum(value != index for index, value in enumerate(final_permutation)) != 2:
        raise AssertionError("selected local endpoint is not a transposition")

    packet = {
        "schema": "MTTQ79SelectedAlignmentSingleMeridianMonodromy.v1",
        "status": "SELECTED_ALIGNMENT_POINTWISE_ROOT_MONODROMY_COMPUTED",
        "root_id": arguments.root_id,
        "distinguished_index": index,
        "authority": {
            "fibration_sha256": sha256(FIBRATION),
            "fan_sha256": sha256(FAN),
            "homology_convention_sha256": sha256(HOMOLOGY),
        },
        "branch_chart": {
            "line_chart": "y solved, t=z/x",
            "coordinate": (
                "s=1/(t-("
                f"{arguments.omitted_real:.17g}+{arguments.omitted_imag:.17g}i))"
            ),
            "common_omitted_point": encoded_complex(
                complex(arguments.omitted_real, arguments.omitted_imag)
            ),
            "selected_fan_avoids_all_three_L1_zero_balls": True,
            "projection_angle": "pi/7",
        },
        "transport": {
            "step_to_root_separation_threshold": format(
                arguments.step_ratio, ".17g"
            ),
            "maximum_step_to_root_separation_ratio": format(
                ratio_state[0], ".17g"
            ),
            "root_solve_count": transport.root_solve_count,
            "saved_sample_count": len(points),
            "outbound_point_count": outbound_point_count,
            "circle_point_count": circle_point_count,
            "cached_reverse_steps": reused_reverse_steps,
            "circle_scale": format(arguments.circle_scale, ".17g"),
        },
        "braid": {
            "raw_word": [[generator, sign] for generator, sign in word],
            "raw_length": len(word),
            "free_reduced_word": [
                [generator, sign] for generator, sign in reduced
            ],
            "free_reduced_length": len(reduced),
            "minimum_projected_event_parameter_separation": format(
                minimum_event_gap, ".17g"
            ),
            "final_order": final_order,
            "final_root_permutation": final_permutation,
        },
        "homology": {
            "integral_picard_lefschetz_matrix": matrix_rows(action),
            "rank_M_minus_I": delta.rank(),
            "M_minus_I_square_zero": delta * delta == sp.zeros(4),
        },
        "strict_scope": {
            "pointwise_root_balls_certified": True,
            "continuous_root_tubes_certified": False,
            "local_monodromy_promoted": False,
            "observed_SM_values_used": False,
        },
    }
    if not arguments.no_save:
        OUTPUT.mkdir(parents=True, exist_ok=True)
        trajectory_path = OUTPUT / f"d{index:03d}_{arguments.root_id}.trajectory.npz"
        np.savez_compressed(
            trajectory_path,
            w=np.asarray(points, dtype=np.complex128),
            roots=np.asarray(trajectories, dtype=np.complex128),
            root_radius_uppers=np.asarray(radii_rows, dtype=np.float64),
        )
        packet["trajectory"] = {
            "path": str(trajectory_path.relative_to(ROOT)).replace("\\", "/"),
            "sha256": sha256(trajectory_path),
            "array_schema": {
                "w": [len(points)],
                "roots": [len(points), 6],
                "root_radius_uppers": [len(points), 6],
            },
        }
        packet_path = OUTPUT / f"d{index:03d}_{arguments.root_id}.packet.json"
        packet_path.write_text(
            json.dumps(packet, indent=2, sort_keys=True) + "\n",
            encoding="utf-8",
        )
        print(f"wrote {packet_path.relative_to(ROOT)}")
    print(
        f"d{index:03d} {arguments.root_id}: samples={len(points)} "
        f"solves={transport.root_solve_count} word={len(word)} "
        f"matrix={matrix_rows(action)}"
    )
    print(f"elapsed_seconds={time.perf_counter() - started:.8g}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
