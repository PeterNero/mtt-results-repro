from __future__ import annotations

import json
import math
from pathlib import Path

import numpy as np
import sympy as sp
from flint import acb, arb, ctx

from certify_q79genus2local_pl_braids import (
    dump,
    exact_complex,
    load,
    lower,
    matrix_rows,
    sha256,
    strict_sign,
    word_sha256,
)


ROOT = Path(__file__).resolve().parents[1]
DATA = (
    ROOT
    / "candidate_data"
    / "selected_q79genus2distinguishedmeridianexecution"
)
TRAJECTORY_BATCH = DATA / "distinguished_trajectory_batch.packet.json"
TUBE_BATCH = DATA / "distinguished_root_tube_batch.packet.json"
FAN = (
    ROOT
    / "candidate_data"
    / "selected_q79genus2distinguishedcutsystemandglobalrelation"
    / "distinguished_radial_fan.packet.json"
)
A113_EXPLORATION = (
    ROOT
    / "candidate_data"
    / "selected_q79genus2picardlefschetzmonodromyexecution"
    / "numerical_monodromy_exploration.packet.json"
)
HANDLE_PROMOTION = (
    ROOT
    / "candidate_data"
    / "selected_q79genus2handlemonodromypromotion"
    / "two_promoted_torus_handle_monodromies.packet.json"
)
LOCAL_ATLAS = (
    ROOT / "candidate_data" / "selected_q79genus2localroottrajectoryexecution"
)
ZERO_TRANSITION = LOCAL_ATLAS / "old_to_zero_branch_chart_transition.packet.json"
MINUS_ONE_TRANSITION = (
    LOCAL_ATLAS / "old_to_minus_one_branch_chart_transition.packet.json"
)
OUTPUT = DATA / "distinguished_pl_braid_and_global_relation_certificate.packet.json"


def primitive_vanishing_cycle(
    action: sp.Matrix, intersection: sp.Matrix
) -> tuple[list[int], int]:
    delta = action - sp.eye(4)
    column = next(
        delta[:, index]
        for index in range(delta.cols)
        if any(delta[row, index] != 0 for row in range(delta.rows))
    )
    divisor = 0
    for value in column:
        divisor = math.gcd(divisor, abs(int(value)))
    if divisor == 0:
        raise AssertionError("zero Picard-Lefschetz column")
    vector = sp.Matrix([int(value) // divisor for value in column])
    for value in vector:
        if value != 0:
            if value < 0:
                vector = -vector
            break
    positive_replay = sp.eye(4) + vector * vector.T * intersection
    negative_replay = sp.eye(4) - vector * vector.T * intersection
    if positive_replay == action:
        twist_sign = 1
    elif negative_replay == action:
        twist_sign = -1
    else:
        raise AssertionError("primitive vanishing-cycle replay failed")
    return [int(value) for value in vector], twist_sign


def main() -> int:
    ctx.dps = 80
    trajectory_batch = load(TRAJECTORY_BATCH)
    tube_batch = load(TUBE_BATCH)
    fan = load(FAN)
    old_exploration = load(A113_EXPLORATION)
    handles = load(HANDLE_PROMOTION)
    if trajectory_batch["counts"]["trajectory_packets_complete"] != 90:
        raise AssertionError("distinguished trajectory batch incomplete")
    if tube_batch["counts"]["continuous_root_tube_certificates"] != 90:
        raise AssertionError("distinguished tube batch incomplete")
    if not fan["topology"]["ordered_distinguished_cut_system_closed"]:
        raise AssertionError("distinguished fan topology is not certified")

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
        "s_0=1/t": sp.Matrix(
            load(ZERO_TRANSITION)["homology_marking"][
                "old_to_target_transport_matrix_P"
            ]
        ),
        "s_minus1=1/(t+1)": sp.Matrix(
            load(MINUS_ONE_TRANSITION)["homology_marking"][
                "old_to_target_transport_matrix_P"
            ]
        ),
    }
    tube_rows = {
        int(row["distinguished_index"]): row for row in tube_batch["rows"]
    }

    promoted_rows: list[dict] = []
    global_minimum_projection_clearance = math.inf
    global_minimum_crossing_height = math.inf
    global_minimum_event_gap = math.inf
    total_crossings = 0
    total_multi_event_segments = 0
    ordered_action_product = sp.eye(4)

    for batch_index, batch_row in enumerate(trajectory_batch["rows"], 1):
        index = int(batch_row["distinguished_index"])
        root_id = batch_row["root_id"]
        if index != batch_index:
            raise AssertionError("distinguished batch order changed")
        fan_row = fan["distinguished_positive_meridians"][index - 1]
        if fan_row["root_id"] != root_id:
            raise AssertionError("fan and trajectory order disagree")
        trajectory_packet_path = ROOT / batch_row["packet_path"]
        trajectory_packet = load(trajectory_packet_path)
        trajectory_path = ROOT / trajectory_packet["trajectory"]["path"]
        if sha256(trajectory_packet_path) != batch_row["packet_sha256"]:
            raise AssertionError(f"d{index:03d} trajectory-packet hash mismatch")
        if sha256(trajectory_path) != trajectory_packet["trajectory"]["sha256"]:
            raise AssertionError(f"d{index:03d} trajectory hash mismatch")
        tube_row = tube_rows[index]
        tube_path = ROOT / tube_row["certificate_path"]
        tube_certificate = load(tube_path)
        if sha256(tube_path) != tube_row["certificate_sha256"]:
            raise AssertionError(f"d{index:03d} tube-certificate hash mismatch")
        if not tube_certificate["acceptance"]["promotion_ready"]:
            raise AssertionError(f"d{index:03d} root tubes not promotion ready")

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
            raise AssertionError(f"d{index:03d} initial branch marking changed")

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
                        x0, f"d{index:03d} segment {segment_index} left projection"
                    )
                    sign1 = strict_sign(
                        x1, f"d{index:03d} segment {segment_index} right projection"
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
                        raise AssertionError(
                            f"d{index:03d} crossing parameter unresolved"
                        )
                    height = (
                        (1 - parameter) * left_difference.imag
                        + parameter * right_difference.imag
                    )
                    height_sign = strict_sign(
                        height,
                        f"d{index:03d} segment {segment_index} crossing height",
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
                        raise AssertionError(
                            f"d{index:03d} same-segment event order unresolved"
                        )
                    minimum_event_gap = min(minimum_event_gap, lower(gap))
            for event in events:
                first = event["first"]
                second = event["second"]
                first_position = order.index(first)
                second_position = order.index(second)
                if abs(first_position - second_position) != 1:
                    raise AssertionError(f"d{index:03d} crossing is not adjacent")
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
                    raise AssertionError(f"d{index:03d} endpoint order unresolved")
            if order != right_order:
                raise AssertionError(f"d{index:03d} crossing replay/order mismatch")
            left = right

        expected_word = [
            tuple(value) for value in trajectory_packet["braid"]["raw_word"]
        ]
        if word != expected_word:
            raise AssertionError(f"d{index:03d} interval word mismatch")
        if order != trajectory_packet["braid"]["final_order"]:
            raise AssertionError(f"d{index:03d} final order mismatch")
        permutation = trajectory_packet["braid"]["final_root_permutation"]
        moved = [slot for slot, target in enumerate(permutation) if slot != target]
        if (
            len(moved) != 2
            or permutation[moved[0]] != moved[1]
            or permutation[moved[1]] != moved[0]
        ):
            raise AssertionError(
                f"d{index:03d} endpoint permutation is not a transposition"
            )

        action_target = sp.eye(4)
        for generator, sign in word:
            action_target = (positive if sign == 1 else negative)[
                generator - 1
            ] * action_target
        chart = trajectory_packet["branch_chart"]["coordinate"]
        transition = transition_matrices[chart]
        action_old = transition.inv() * action_target * transition
        expected_old = sp.Matrix(
            trajectory_packet["homology"][
                "integral_picard_lefschetz_matrix_A114_marking"
            ]
        )
        if action_old != expected_old:
            raise AssertionError(f"d{index:03d} transported matrix mismatch")
        delta = action_old - sp.eye(4)
        if (
            action_old.T * intersection * action_old != intersection
            or action_old.det() != 1
            or delta.rank() != 1
            or delta * delta != sp.zeros(4)
        ):
            raise AssertionError(
                f"d{index:03d} promoted action is not a PL transvection"
            )
        vanishing_cycle, twist_sign = primitive_vanishing_cycle(
            action_old, intersection
        )
        if twist_sign != 1:
            raise AssertionError(f"d{index:03d} positive meridian gave a negative twist")
        ordered_action_product = action_old * ordered_action_product

        promoted_rows.append(
            {
                "distinguished_index": index,
                "root_id": root_id,
                "branch_chart": chart,
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
                "vanishing_cycle_primitive_up_to_sign": vanishing_cycle,
                "picard_lefschetz_twist_sign": twist_sign,
                "promoted_integral_symplectic_matrix_A114_marking": matrix_rows(
                    action_old
                ),
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
            print(f"distinguished braids: {batch_index}/90", flush=True)

    handle_by_name = {row["name"]: row for row in handles["handles"]}
    handle_a = sp.Matrix(handle_by_name["A"]["integral_symplectic_matrix"])
    handle_b = sp.Matrix(handle_by_name["B"]["integral_symplectic_matrix"])
    boundary_action = handle_b.inv() * handle_a.inv() * handle_b * handle_a
    global_relation_exact = ordered_action_product == boundary_action
    if not global_relation_exact:
        raise AssertionError("ordered distinguished product misses handle boundary")

    payload = {
        "schema": "MTTQ79GenusTwoDistinguishedPLBraidAndGlobalRelationCertificate.v1",
        "status": "ALL_90_DISTINGUISHED_PL_ACTIONS_PROMOTED_GLOBAL_SP4Z_SURFACE_RELATION_CLOSED",
        "authority": {
            "distinguished_fan_sha256": sha256(FAN),
            "trajectory_batch_sha256": sha256(TRAJECTORY_BATCH),
            "root_tube_batch_sha256": sha256(TUBE_BATCH),
            "A113_exploration_sha256": sha256(A113_EXPLORATION),
            "handle_promotion_sha256": sha256(HANDLE_PROMOTION),
            "zero_chart_transition_sha256": sha256(ZERO_TRANSITION),
            "minus_one_chart_transition_sha256": sha256(MINUS_ONE_TRANSITION),
            "python_flint_version": "0.9.0",
        },
        "projection": {
            "rotation": "exp(-i*pi/7)",
            "precision_decimal_digits": ctx.dps,
        },
        "action_convention": {
            "path_concatenation": "gamma then delta",
            "left_action_rule": "M(gamma then delta)=M(delta)*M(gamma)",
            "positive_cut_square_boundary_path": "A*B*A^-1*B^-1",
            "positive_boundary_action": "B^-1*A^-1*B*A",
            "positive_distinguished_path_product": "m1*m2*...*m90",
            "ordered_matrix_product": "M90*M89*...*M1",
        },
        "global_surface_relation": {
            "pi1_path_relation": "A*B*A^-1*B^-1=m1*m2*...*m90",
            "equivalent_identity_word": "A*B*A^-1*B^-1*m90^-1*...*m1^-1=1",
            "handle_boundary_action": matrix_rows(boundary_action),
            "ordered_distinguished_action_product": matrix_rows(
                ordered_action_product
            ),
            "exact_integer_matrix_equality": global_relation_exact,
            "relation_scope": "integral H1 Gauss-Manin representation in the frozen A114 genus-two marking",
        },
        "aggregate": {
            "promoted_distinguished_matrix_count": len(promoted_rows),
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
                [
                    row["vanishing_cycle_primitive_up_to_sign"]
                    for row in promoted_rows
                ]
            ).rank(),
        },
        "rows": promoted_rows,
        "acceptance": {
            "ordered_distinguished_cut_system_certified": True,
            "all_90_continuous_braid_isotopies_certified": True,
            "all_90_interval_braid_words_certified": True,
            "all_90_distinguished_PL_matrices_promoted": True,
            "global_integral_Gauss_Manin_surface_relation_closed": True,
        },
        "strict_scope": {
            "full_mapping_class_group_faithfulness_claimed": False,
            "beta_C_period_rows_emitted": 0,
            "integral_period_branch_selected": False,
            "gerbe_zero_or_no_go_executed": False,
        },
    }
    dump(OUTPUT, payload)
    print(f"wrote {OUTPUT}")
    print(json.dumps(payload["aggregate"], indent=2, sort_keys=True))
    print(json.dumps(payload["global_surface_relation"], indent=2, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
