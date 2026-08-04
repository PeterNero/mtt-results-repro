from __future__ import annotations

import argparse
import json
import math
from pathlib import Path

import numpy as np
import sympy as sp
from flint import ctx

import certify_q79_height4_target_main_hessian_interval as base
import certify_q79_selected_alignment_single_E32_thimble_main_interval as pilot
from q79genus2_root_transport import Q79GenusTwoRootTransport, matrix_rows


ROOT = Path(__file__).resolve().parents[1]
HOMOLOGY = (
    ROOT
    / "candidate_data"
    / "selected_q79genus2picardlefschetzmonodromyexecution"
    / "numerical_monodromy_exploration.packet.json"
)


def parser() -> argparse.ArgumentParser:
    value = argparse.ArgumentParser()
    value.add_argument("--index", type=int, required=True)
    value.add_argument("--canonical-main", type=Path, required=True)
    value.add_argument("--dps", type=int, default=80)
    value.add_argument("--maximum-match-ratio", type=float, default=0.08)
    value.add_argument("--maximum-step", type=float, default=0.005)
    value.add_argument("--output", type=Path)
    return value


def roots_at(system: object, parameter: complex) -> tuple[np.ndarray, list[float]]:
    roots, _leading = pilot.roots_at(system, parameter)
    return (
        np.asarray([base.validated.midpoint(value) for value in roots]),
        [base.validated.radius_upper(value) for value in roots],
    )


def main() -> int:
    arguments = parser().parse_args()
    arguments.canonical_main = arguments.canonical_main.resolve()
    if arguments.output is not None:
        arguments.output = arguments.output.resolve()
    if not 0.0 < arguments.maximum_match_ratio < 0.25:
        raise ValueError("maximum match ratio must lie in (0,0.25)")
    ctx.dps = arguments.dps
    selected_main = base.load(arguments.canonical_main)
    system, _rank, _row = base.selected_system(arguments.index, arguments.dps)
    _node_center, cutoff = base.canonical_cutoff_start(selected_main)
    distance = abs(cutoff)
    direction = cutoff / distance

    rotation = np.exp(-1j * math.pi / 7)
    unordered, unordered_radii = roots_at(system, 0.0 + 0.0j)
    initial_order = np.argsort((rotation * unordered).real)
    previous = unordered[initial_order]
    previous_radii = [unordered_radii[index] for index in initial_order]
    trajectories = [previous.copy()]
    radius_rows = [previous_radii]
    parameters = [0.0 + 0.0j]
    position = 0.0
    step = min(arguments.maximum_step, distance / 128.0)
    maximum_ratio = 0.0
    rejected = 0
    while position < distance:
        trial_step = min(step, distance - position)
        parameter = direction * (position + trial_step)
        unordered, unordered_radii = roots_at(system, parameter)
        current, current_radii, ratio = Q79GenusTwoRootTransport.match(
            previous,
            unordered,
            unordered_radii,
        )
        if ratio >= arguments.maximum_match_ratio:
            rejected += 1
            step = trial_step / 2.0
            if step < 1.0e-12:
                raise ArithmeticError("n3 path root matching requires a smaller step")
            continue
        position = min(distance, position + trial_step)
        previous = current
        previous_radii = current_radii
        trajectories.append(current.copy())
        radius_rows.append(list(current_radii))
        parameters.append(direction * position)
        maximum_ratio = max(maximum_ratio, ratio)
        step = min(arguments.maximum_step, trial_step * 1.5)

    homology = base.load(HOMOLOGY)["homology_convention"]
    transport = object.__new__(Q79GenusTwoRootTransport)
    transport.rotation = rotation
    transport.intersection = np.asarray(homology["intersection_matrix"], dtype=object)
    transport.chain_vectors = [
        np.asarray(value, dtype=object).reshape(4, 1)
        for value in homology["chain_vectors_for_sigma_1_to_sigma_5"]
    ]
    transport.positive = [
        np.eye(4, dtype=object)
        - vector @ vector.T @ transport.intersection
        for vector in transport.chain_vectors
    ]
    transport.negative = [
        np.asarray(sp.Matrix(value.tolist()).inv().tolist(), dtype=object)
        for value in transport.positive
    ]
    word, final_order, minimum_event_gap = transport.braid_word(trajectories)
    action = sp.Matrix(transport.action(word).tolist())

    final_raw, final_raw_radii = roots_at(system, cutoff)
    final_labelled, _final_radii, final_match_ratio = Q79GenusTwoRootTransport.match(
        trajectories[-1], final_raw, final_raw_radii
    )
    if final_match_ratio >= arguments.maximum_match_ratio:
        raise AssertionError("final raw cutoff labels are not uniquely matched")
    raw_to_label = [int(np.argmin(abs(final_labelled - root))) for root in final_raw]
    selected_pair = [
        int(value)
        for value in selected_main["selected_target"][
            "near_node_colliding_pair_zero_based"
        ]
    ]
    selected_labels = [raw_to_label[index] for index in selected_pair]
    selected_positions = [final_order.index(label) for label in selected_labels]
    if abs(selected_positions[0] - selected_positions[1]) != 1:
        raise AssertionError("selected cutoff pair is not adjacent in projected order")
    generator = min(selected_positions)
    final_chain = sp.Matrix(transport.chain_vectors[generator].tolist())
    base_inverse = action.inv() * final_chain
    base_forward = action * final_chain

    packet = {
        "schema": "MTTQ79HeightFourN3PathHomologyDiagnostic.v1",
        "distinguished_index": arguments.index,
        "path": {
            "cutoff": base.pair(cutoff),
            "sample_count": len(parameters),
            "rejected_match_steps": rejected,
            "maximum_root_match_ratio": maximum_ratio,
            "maximum_allowed_root_match_ratio": arguments.maximum_match_ratio,
        },
        "braid": {
            "raw_word": [[int(a), int(b)] for a, b in word],
            "raw_word_length": len(word),
            "final_order": [int(value) for value in final_order],
            "minimum_linear_crossing_event_gap": minimum_event_gap,
            "integral_action": matrix_rows(action),
        },
        "selected_cycle": {
            "cutoff_pair_raw_indices": selected_pair,
            "cutoff_pair_continuous_labels": selected_labels,
            "cutoff_pair_projected_positions": selected_positions,
            "cutoff_adjacent_chain_generator_one_based": generator + 1,
            "final_standard_chain_vector": [int(value) for value in final_chain],
            "base_pullback_candidate_action_inverse": [
                int(value) for value in base_inverse
            ],
            "base_pushforward_candidate_action": [int(value) for value in base_forward],
        },
        "strict_scope": {
            "pointwise_root_balls_separated": True,
            "continuous_root_tubes_certified": False,
            "interval_braid_crossings_certified": False,
            "homology_selection_promoted": False,
        },
    }
    if arguments.output is not None:
        base.dump(arguments.output, packet)
        print(f"wrote {base.relative(arguments.output)}")
    print(json.dumps(packet, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
