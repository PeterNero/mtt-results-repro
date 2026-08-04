from __future__ import annotations

import hashlib
import json
import math
from pathlib import Path

import numpy as np
import sympy as sp
from flint import acb, arb, ctx


ROOT = Path(__file__).resolve().parents[1]
DATA = (
    ROOT
    / "candidate_data"
    / "selected_q79genus2localroottrajectoryexecution"
)
TRAJECTORY_BATCH = DATA / "local_trajectory_batch.packet.json"
TUBE_BATCH = DATA / "local_root_tube_batch.packet.json"
A113_EXPLORATION = (
    ROOT
    / "candidate_data"
    / "selected_q79genus2picardlefschetzmonodromyexecution"
    / "numerical_monodromy_exploration.packet.json"
)
ZERO_TRANSITION = DATA / "old_to_zero_branch_chart_transition.packet.json"
MINUS_ONE_TRANSITION = DATA / "old_to_minus_one_branch_chart_transition.packet.json"
OUTPUT = DATA / "local_pl_braid_interval_certificate.packet.json"
FALLBACK_ROOT_IDS = {"a34", "a41"}


def load(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def dump(path: Path, payload: dict) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(payload, indent=2, sort_keys=True) + "\n", encoding="utf-8")


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def lower(value: arb) -> float:
    return math.nextafter(float(value.lower()), -math.inf)


def exact_complex(value: complex) -> acb:
    return acb(format(value.real, ".17g"), format(value.imag, ".17g"))


def strict_sign(value: arb, label: str) -> int:
    if value.lower() > 0:
        return 1
    if value.upper() < 0:
        return -1
    raise AssertionError(f"interval sign unresolved: {label}: {value}")


def matrix_rows(value: sp.Matrix) -> list[list[int]]:
    return [[int(entry) for entry in value.row(index)] for index in range(value.rows)]


def word_sha256(word: list[list[int]]) -> str:
    encoded = json.dumps(word, separators=(",", ":")).encode("ascii")
    return hashlib.sha256(encoded).hexdigest()


def main() -> int:
    ctx.dps = 80
    trajectory_batch = load(TRAJECTORY_BATCH)
    tube_batch = load(TUBE_BATCH)
    old_exploration = load(A113_EXPLORATION)
    if trajectory_batch["counts"]["trajectory_packets_complete"] != 90:
        raise AssertionError("local trajectory batch incomplete")
    if tube_batch["counts"]["continuous_root_tube_certificates"] != 90:
        raise AssertionError("local tube batch incomplete")

    intersection = sp.Matrix(
        old_exploration["homology_convention"]["intersection_matrix"]
    )
    vectors = [
        sp.Matrix(vector)
        for vector in old_exploration["homology_convention"][
            "chain_vectors_for_sigma_1_to_sigma_5"
        ]
    ]
    positive = [sp.eye(4) - vector * vector.T * intersection for vector in vectors]
    negative = [value.inv() for value in positive]
    angle = arb.pi() / 7
    rotation = acb(angle.cos(), -angle.sin())
    transition_matrices = {
        False: sp.Matrix(
            load(ZERO_TRANSITION)["homology_marking"][
                "old_to_target_transport_matrix_P"
            ]
        ),
        True: sp.Matrix(
            load(MINUS_ONE_TRANSITION)["homology_marking"][
                "old_to_target_transport_matrix_P"
            ]
        ),
    }
    old_rows = {row["root_id"]: row for row in old_exploration["monodromies"]}
    tube_rows = {row["root_id"]: row for row in tube_batch["rows"]}

    promoted_rows: list[dict] = []
    global_minimum_projection_clearance = math.inf
    global_minimum_crossing_height = math.inf
    global_minimum_event_gap = math.inf
    total_crossings = 0
    total_multi_event_segments = 0
    for batch_index, batch_row in enumerate(trajectory_batch["rows"], 1):
        root_id = batch_row["root_id"]
        trajectory_packet_path = ROOT / batch_row["packet_path"]
        trajectory_packet = load(trajectory_packet_path)
        trajectory_path = ROOT / trajectory_packet["trajectory"]["path"]
        if sha256(trajectory_path) != trajectory_packet["trajectory"]["sha256"]:
            raise AssertionError(f"{root_id} trajectory hash mismatch")
        tube_row = tube_rows[root_id]
        tube_path = ROOT / tube_row["certificate_path"]
        tube_certificate = load(tube_path)
        if sha256(tube_path) != tube_row["certificate_sha256"]:
            raise AssertionError(f"{root_id} tube-certificate hash mismatch")
        if not tube_certificate["acceptance"]["promotion_ready"]:
            raise AssertionError(f"{root_id} root tubes not promotion ready")

        with np.load(trajectory_path) as data:
            roots = data["roots"]
        order = list(range(6))
        word: list[tuple[int, int]] = []
        minimum_projection_clearance = math.inf
        minimum_crossing_height = math.inf
        minimum_event_gap = math.inf
        multi_event_segments = 0
        left = [rotation * exact_complex(complex(value)) for value in roots[0]]
        initial_order = sorted(
            range(6), key=lambda label: float(left[label].real.mid())
        )
        if initial_order != order:
            raise AssertionError(f"{root_id} initial branch marking changed")

        for segment_index in range(len(roots) - 1):
            right = [
                rotation * exact_complex(complex(value))
                for value in roots[segment_index + 1]
            ]
            events: list[dict] = []
            for first in range(6):
                for second in range(first + 1, 6):
                    left_difference = left[first] - left[second]
                    right_difference = right[first] - right[second]
                    x0 = left_difference.real
                    x1 = right_difference.real
                    sign0 = strict_sign(
                        x0, f"{root_id} segment {segment_index} left projection"
                    )
                    sign1 = strict_sign(
                        x1, f"{root_id} segment {segment_index} right projection"
                    )
                    minimum_projection_clearance = min(
                        minimum_projection_clearance,
                        lower(abs(x0)),
                        lower(abs(x1)),
                    )
                    if sign0 == sign1:
                        continue
                    parameter = x0 / (x0 - x1)
                    if not parameter.lower() > 0 or not parameter.upper() < 1:
                        raise AssertionError(f"{root_id} crossing parameter unresolved")
                    height = (
                        (1 - parameter) * left_difference.imag
                        + parameter * right_difference.imag
                    )
                    height_sign = strict_sign(
                        height, f"{root_id} segment {segment_index} crossing height"
                    )
                    minimum_crossing_height = min(
                        minimum_crossing_height, lower(abs(height))
                    )
                    events.append(
                        {
                            "first": first,
                            "second": second,
                            "parameter": parameter,
                            "height_sign": height_sign,
                        }
                    )
            events.sort(key=lambda row: float(row["parameter"].mid()))
            if len(events) > 1:
                multi_event_segments += 1
                for left_event, right_event in zip(events, events[1:]):
                    gap = right_event["parameter"].lower() - left_event[
                        "parameter"
                    ].upper()
                    if not gap > 0:
                        raise AssertionError(f"{root_id} same-segment event order unresolved")
                    minimum_event_gap = min(minimum_event_gap, lower(gap))
            for event in events:
                first = event["first"]
                second = event["second"]
                first_position = order.index(first)
                second_position = order.index(second)
                if abs(first_position - second_position) != 1:
                    raise AssertionError(f"{root_id} crossing is not adjacent")
                generator = min(first_position, second_position)
                left_label = order[generator]
                sign = 1 if (
                    (event["height_sign"] > 0 and left_label == first)
                    or (event["height_sign"] < 0 and left_label == second)
                ) else -1
                word.append((generator + 1, sign))
                order[generator], order[generator + 1] = (
                    order[generator + 1],
                    order[generator],
                )

            right_order = sorted(
                range(6), key=lambda label: float(right[label].real.mid())
            )
            for left_label, right_label in zip(right_order, right_order[1:]):
                difference = right[right_label].real - right[left_label].real
                if not difference.lower() > 0:
                    raise AssertionError(f"{root_id} endpoint order unresolved")
            if order != right_order:
                raise AssertionError(f"{root_id} crossing replay/order mismatch")
            left = right

        expected_word = [tuple(value) for value in trajectory_packet["braid"]["raw_word"]]
        if word != expected_word:
            raise AssertionError(f"{root_id} interval word mismatch")
        if order != trajectory_packet["braid"]["final_order"]:
            raise AssertionError(f"{root_id} final order mismatch")
        permutation = trajectory_packet["braid"]["final_root_permutation"]
        moved = [index for index, target in enumerate(permutation) if index != target]
        if (
            len(moved) != 2
            or permutation[moved[0]] != moved[1]
            or permutation[moved[1]] != moved[0]
        ):
            raise AssertionError(f"{root_id} endpoint permutation is not a transposition")

        action_target = sp.eye(4)
        for generator, sign in word:
            action_target = (positive if sign == 1 else negative)[generator - 1] * action_target
        transition = transition_matrices[root_id in FALLBACK_ROOT_IDS]
        action_old = transition.inv() * action_target * transition
        expected_old = sp.Matrix(
            old_rows[root_id]["homology"]["picard_lefschetz_matrix"]
        )
        if action_old != expected_old:
            raise AssertionError(f"{root_id} transported matrix mismatch")
        delta = action_old - sp.eye(4)
        if (
            action_old.T * intersection * action_old != intersection
            or action_old.det() != 1
            or delta.rank() != 1
            or delta * delta != sp.zeros(4)
        ):
            raise AssertionError(f"{root_id} promoted action is not a PL transvection")

        promoted_rows.append(
            {
                "root_id": root_id,
                "branch_chart": "s_minus1=1/(t+1)" if root_id in FALLBACK_ROOT_IDS else "s_0=1/t",
                "certified_path_segments": len(roots) - 1,
                "interval_certified_crossings": len(word),
                "raw_braid_word_sha256": word_sha256(
                    [[generator, sign] for generator, sign in word]
                ),
                "minimum_projected_endpoint_pair_difference_lower": format(
                    minimum_projection_clearance, ".17g"
                ),
                "minimum_crossing_height_lower": format(
                    minimum_crossing_height, ".17g"
                ),
                "minimum_same_segment_event_parameter_gap_lower": (
                    format(minimum_event_gap, ".17g")
                    if minimum_event_gap < math.inf
                    else None
                ),
                "multi_event_segment_count": multi_event_segments,
                "endpoint_root_permutation": permutation,
                "vanishing_cycle_primitive_up_to_sign": old_rows[root_id]["homology"][
                    "vanishing_cycle_primitive_up_to_sign"
                ],
                "promoted_integral_symplectic_matrix": matrix_rows(action_old),
                "tube_certificate_path": tube_row["certificate_path"],
                "tube_certificate_sha256": tube_row["certificate_sha256"],
                "promotion_accepted": True,
            }
        )
        total_crossings += len(word)
        total_multi_event_segments += multi_event_segments
        global_minimum_projection_clearance = min(
            global_minimum_projection_clearance, minimum_projection_clearance
        )
        global_minimum_crossing_height = min(
            global_minimum_crossing_height, minimum_crossing_height
        )
        if minimum_event_gap < math.inf:
            global_minimum_event_gap = min(
                global_minimum_event_gap, minimum_event_gap
            )
        if batch_index % 10 == 0:
            print(f"local braids: {batch_index}/90", flush=True)

    payload = {
        "schema": "MTTQ79GenusTwoLocalPLBraidIntervalCertificate.v1",
        "status": "ALL_90_LOCAL_BRAIDS_AND_SP4Z_ACTIONS_PROMOTED",
        "authority": {
            "trajectory_batch_sha256": sha256(TRAJECTORY_BATCH),
            "root_tube_batch_sha256": sha256(TUBE_BATCH),
            "A113_exploration_sha256": sha256(A113_EXPLORATION),
            "zero_chart_transition_sha256": sha256(ZERO_TRANSITION),
            "minus_one_chart_transition_sha256": sha256(MINUS_ONE_TRANSITION),
            "python_flint_version": "0.9.0",
        },
        "projection": {
            "rotation": "exp(-i*pi/7)",
            "precision_decimal_digits": ctx.dps,
        },
        "atlas": {
            "primary": "s_0=1/t on 88 local meridians",
            "fallback": "s_minus1=1/(t+1) on a34 and a41",
            "frozen_marking_transport": "M_old=P_target^(-1)*M_target*P_target",
        },
        "aggregate": {
            "promoted_local_matrix_count": len(promoted_rows),
            "certified_path_segment_count": sum(
                row["certified_path_segments"] for row in promoted_rows
            ),
            "interval_certified_crossing_count": total_crossings,
            "multi_event_segment_count": total_multi_event_segments,
            "minimum_projected_endpoint_pair_difference_lower": format(
                global_minimum_projection_clearance, ".17g"
            ),
            "minimum_crossing_height_lower": format(
                global_minimum_crossing_height, ".17g"
            ),
            "minimum_same_segment_event_parameter_gap_lower": (
                format(global_minimum_event_gap, ".17g")
                if global_minimum_event_gap < math.inf
                else None
            ),
            "vanishing_cycle_span_rank": sp.Matrix(
                [row["vanishing_cycle_primitive_up_to_sign"] for row in promoted_rows]
            ).rank(),
        },
        "rows": promoted_rows,
        "acceptance": {
            "all_90_continuous_local_braid_isotopies_certified": True,
            "all_90_interval_braid_words_certified": True,
            "all_90_A113_matrices_promoted": True,
        },
        "strict_scope": {
            "ordered_distinguished_cut_system_closed": False,
            "global_surface_relation_checked": False,
            "beta_C_period_rows_emitted": 0,
        },
    }
    dump(OUTPUT, payload)
    print(f"wrote {OUTPUT}")
    print(json.dumps(payload["aggregate"], indent=2, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
