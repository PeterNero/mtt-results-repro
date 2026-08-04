from __future__ import annotations

import argparse
import hashlib
import json
import math
import time
from pathlib import Path

import numpy as np
import sympy as sp

from q79genus2_root_transport import (
    Q79GenusTwoRootTransport,
    free_reduce,
    load_json,
    matrix_rows,
)


ROOT = Path(__file__).resolve().parents[1]
FIBRATION = (
    ROOT
    / "candidate_data"
    / "selected_q79genus2lefschetzperiodreduction"
    / "explicit_genus2_fibration.packet.json"
)
A113_EXPLORATION = (
    ROOT
    / "candidate_data"
    / "selected_q79genus2picardlefschetzmonodromyexecution"
    / "numerical_monodromy_exploration.packet.json"
)
FAN = (
    ROOT
    / "candidate_data"
    / "selected_q79genus2distinguishedcutsystemandglobalrelation"
    / "distinguished_radial_fan.packet.json"
)
ZERO_CHART_TRANSITION = (
    ROOT
    / "candidate_data"
    / "selected_q79genus2localroottrajectoryexecution"
    / "old_to_zero_branch_chart_transition.packet.json"
)
MINUS_ONE_CHART_TRANSITION = (
    ROOT
    / "candidate_data"
    / "selected_q79genus2localroottrajectoryexecution"
    / "old_to_minus_one_branch_chart_transition.packet.json"
)
OUTPUT = (
    ROOT
    / "candidate_data"
    / "selected_q79genus2distinguishedmeridianexecution"
)


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def packet_complex(value: dict[str, str]) -> complex:
    return complex(float(value["real"]), float(value["imaginary"]))


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--root-id", required=True)
    parser.add_argument("--step-ratio", type=float, default=0.16)
    parser.add_argument("--coarse-outbound", type=int, default=48)
    parser.add_argument("--coarse-circle", type=int, default=128)
    parser.add_argument("--omitted-real", type=float, default=0.0)
    parser.add_argument("--omitted-imag", type=float, default=0.0)
    parser.add_argument("--no-save", action="store_true")
    args = parser.parse_args()
    if not 0 < args.step_ratio < 0.4:
        raise AssertionError("step ratio must lie in (0,0.4)")

    started = time.perf_counter()
    fan = load_json(FAN)
    old_exploration = load_json(A113_EXPLORATION)
    path_row = next(
        row
        for row in fan["distinguished_positive_meridians"]
        if row["root_id"] == args.root_id
    )
    index = int(path_row["distinguished_index"])
    omitted = complex(args.omitted_real, args.omitted_imag)
    transport = Q79GenusTwoRootTransport(
        FIBRATION,
        old_exploration["homology_convention"],
        omitted=omitted,
    )

    points: list[complex] = [transport.base]
    trajectories: list[np.ndarray] = [transport.base_roots.copy()]
    radii_rows: list[list[float]] = [transport.base_radii.copy()]
    ratio_state = [0.0]
    previous = transport.base_roots

    outbound_end = packet_complex(path_row["outbound_segment"]["end"])
    coarse_outbound = np.linspace(
        transport.base, outbound_end, args.coarse_outbound + 1
    )
    for start, end in zip(coarse_outbound, coarse_outbound[1:]):
        previous = transport.advance(
            complex(start),
            complex(end),
            previous,
            points,
            trajectories,
            radii_rows,
            args.step_ratio,
            ratio_state,
        )
    outbound_point_count = len(points)
    outbound_points = list(points)
    outbound_roots = [row.copy() for row in trajectories]
    outbound_radii = [list(row) for row in radii_rows]

    circle = path_row["positive_meridian"]
    center = packet_complex(circle["center"])
    radius = float(circle["radius"])
    start_angle = float(circle["start_angle"])
    circle_points = [
        center
        + radius
        * np.exp(
            1j * (start_angle + 2 * math.pi * step / args.coarse_circle)
        )
        for step in range(args.coarse_circle + 1)
    ]
    circle_points[0] = outbound_end
    circle_points[-1] = outbound_end
    for start, end in zip(circle_points, circle_points[1:]):
        previous = transport.advance(
            complex(start),
            complex(end),
            previous,
            points,
            trajectories,
            radii_rows,
            args.step_ratio,
            ratio_state,
        )
    circle_point_count = len(points) - outbound_point_count + 1

    reused_reverse_steps = 0
    for outbound_index in range(len(outbound_points) - 2, -1, -1):
        current, radii, ratio = transport.match(
            previous,
            outbound_roots[outbound_index],
            outbound_radii[outbound_index],
        )
        if ratio >= 0.44:
            raise AssertionError("cached reverse matching is not geometrically unique")
        ratio_state[0] = max(ratio_state[0], ratio)
        points.append(outbound_points[outbound_index])
        trajectories.append(current)
        radii_rows.append(radii)
        previous = current
        reused_reverse_steps += 1

    word, final_order, minimum_event_gap = transport.braid_word(trajectories)
    reduced = free_reduce(word)
    action_chart = transport.action(word)
    final_permutation = transport.endpoint_permutation(trajectories[-1])

    transition_path: Path | None = None
    action_old = sp.Matrix(action_chart.tolist())
    marking_transport = "identity"
    if omitted == 0j or omitted == -1 + 0j:
        transition_path = (
            ZERO_CHART_TRANSITION if omitted == 0j else MINUS_ONE_CHART_TRANSITION
        )
        transition = load_json(transition_path)
        if not transition["acceptance"]["marking_transport_promoted"]:
            raise AssertionError("branch-chart marking transport is not promoted")
        marking = sp.Matrix(
            transition["homology_marking"]["old_to_target_transport_matrix_P"]
        )
        action_old = marking.inv() * action_old * marking
        marking_transport = "M_old=P_target^-1*M_target*P_target"

    intersection = sp.Matrix(
        old_exploration["homology_convention"]["intersection_matrix"]
    )
    delta = action_old - sp.eye(4)
    if action_old.T * intersection * action_old != intersection:
        raise AssertionError("distinguished local action is not symplectic")
    if delta.rank() != 1 or delta * delta != sp.zeros(4):
        raise AssertionError("distinguished local action is not a Lefschetz transvection")
    if sum(value != index for index, value in enumerate(final_permutation)) != 2:
        raise AssertionError("distinguished local endpoint is not a transposition")

    chart_name = (
        "s_0=1/t"
        if omitted == 0j
        else (
            "s_minus1=1/(t+1)"
            if omitted == -1 + 0j
            else f"s=1/(t-({args.omitted_real}+{args.omitted_imag}i))"
        )
    )
    packet = {
        "schema": "MTTQ79GenusTwoSingleDistinguishedMeridianTrajectory.v1",
        "status": "DISTINGUISHED_MERIDIAN_TRAJECTORY_COMPUTED_CONTINUOUS_ROOT_TUBES_OPEN",
        "root_id": args.root_id,
        "distinguished_index": index,
        "authority": {
            "fibration_sha256": sha256(FIBRATION),
            "A113_exploration_sha256": sha256(A113_EXPLORATION),
            "distinguished_fan_sha256": sha256(FAN),
            "branch_chart_transition_sha256": (
                sha256(transition_path) if transition_path is not None else None
            ),
        },
        "branch_chart": {
            "coordinate": chart_name,
            "projection_angle": "pi/7",
            "marking_transport": marking_transport,
        },
        "transport": {
            "step_to_root_separation_threshold": format(args.step_ratio, ".17g"),
            "maximum_step_to_root_separation_ratio": format(
                ratio_state[0], ".17g"
            ),
            "root_solve_count": transport.root_solve_count,
            "saved_sample_count": len(points),
            "outbound_point_count": outbound_point_count,
            "circle_point_count": circle_point_count,
            "cached_reverse_steps": reused_reverse_steps,
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
            "integral_symplectic_matrix_in_branch_chart": matrix_rows(
                action_chart
            ),
            "integral_picard_lefschetz_matrix_A114_marking": matrix_rows(
                action_old
            ),
            "rank_M_minus_I": delta.rank(),
            "M_minus_I_square_zero": delta * delta == sp.zeros(4),
        },
        "strict_scope": {
            "pointwise_root_balls_certified": True,
            "continuous_root_tubes_certified": False,
            "promotion_accepted": False,
        },
    }

    if not args.no_save:
        OUTPUT.mkdir(parents=True, exist_ok=True)
        stem = f"d{index:03d}_{args.root_id}"
        trajectory_path = OUTPUT / f"{stem}_pointwise_root_trajectory.npz"
        np.savez_compressed(
            trajectory_path,
            w=np.asarray(points, dtype=np.complex128),
            roots=np.asarray(trajectories, dtype=np.complex128),
            root_radius_uppers=np.asarray(radii_rows, dtype=np.float64),
        )
        packet["trajectory"] = {
            "path": str(trajectory_path.relative_to(ROOT)).replace("\\", "/"),
            "sha256": sha256(trajectory_path),
        }
        packet_path = OUTPUT / f"{stem}.trajectory.packet.json"
        packet_path.write_text(
            json.dumps(packet, indent=2, sort_keys=True) + "\n", encoding="utf-8"
        )
        print(f"wrote {packet_path}")
    print(
        f"d{index:03d} {args.root_id}: chart={chart_name} "
        f"samples={len(points)} solves={transport.root_solve_count} "
        f"word={len(word)} matrix={matrix_rows(action_old)}",
        flush=True,
    )
    print(f"elapsed_seconds={time.perf_counter() - started:.8g}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
