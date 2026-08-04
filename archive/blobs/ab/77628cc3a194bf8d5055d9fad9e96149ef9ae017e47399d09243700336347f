from __future__ import annotations

import hashlib
import json
import math
from pathlib import Path

import numpy as np
import sympy as sp
from flint import acb, arb, ctx


ROOT = Path(__file__).resolve().parents[1]
EXPLORATION = (
    ROOT
    / "candidate_data"
    / "selected_q79genus2handlemonodromycandidate"
    / "handle_monodromy_exploration.packet.json"
)
TUBES = (
    ROOT
    / "candidate_data"
    / "selected_q79genus2handlemonodromycandidate"
    / "handle_continuous_root_tube_certificate.packet.json"
)
OUTPUT = (
    ROOT
    / "candidate_data"
    / "selected_q79genus2handlemonodromycandidate"
    / "handle_pl_braid_interval_certificate.packet.json"
)


def load(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def dump(path: Path, payload: dict) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(payload, indent=2, sort_keys=True) + "\n", encoding="utf-8")


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def upper(value: arb) -> float:
    return math.nextafter(float(value.upper()), math.inf)


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


def main() -> int:
    ctx.dps = 80
    exploration = load(EXPLORATION)
    tubes = load(TUBES)
    if tubes["status"] != "TWO_HANDLE_CONTINUOUS_ROOT_TUBES_CLOSED":
        raise AssertionError("continuous root tubes are not closed")
    if not all(tubes["acceptance"].values()):
        raise AssertionError("handle tube acceptance is incomplete")

    angle = arb.pi() / 7
    rotation = acb(angle.cos(), -angle.sin())
    intersection = sp.Matrix(exploration["homology"]["intersection_matrix"])
    identity = sp.eye(4)
    chain_vectors = [
        sp.Matrix(vector) for vector in exploration["homology"]["chain_vectors"]
    ]
    positive = [
        identity - vector * vector.T * intersection for vector in chain_vectors
    ]
    negative = [value.inv() for value in positive]

    certified_handles: list[dict] = []
    promoted_matrices: dict[str, sp.Matrix] = {}
    for handle in exploration["handles"]:
        trajectory_path = ROOT / handle["trajectory"]["path"]
        if sha256(trajectory_path) != handle["trajectory"]["sha256"]:
            raise AssertionError("trajectory hash mismatch")
        data = np.load(trajectory_path)
        roots = data["roots"]
        point_radii = data["root_radius_uppers"]
        if roots.shape[1] != 6:
            raise AssertionError("expected six branch-root strands")

        projected = [
            [rotation * exact_complex(complex(value)) for value in row]
            for row in roots
        ]
        order = sorted(range(6), key=lambda label: float(projected[0][label].real.mid()))
        if order != list(range(6)):
            raise AssertionError("base branch-root marking changed")

        word: list[tuple[int, int]] = []
        minimum_endpoint_projection_clearance = math.inf
        minimum_crossing_height = math.inf
        minimum_event_parameter_gap = math.inf
        multi_event_segment_count = 0
        for segment_index in range(len(roots) - 1):
            events: list[dict] = []
            for first in range(6):
                for second in range(first + 1, 6):
                    left_difference = projected[segment_index][first] - projected[segment_index][second]
                    right_difference = projected[segment_index + 1][first] - projected[segment_index + 1][second]
                    x0 = left_difference.real
                    x1 = right_difference.real
                    sign0 = strict_sign(
                        x0, f"{handle['name']} segment {segment_index} x0 {first},{second}"
                    )
                    sign1 = strict_sign(
                        x1, f"{handle['name']} segment {segment_index} x1 {first},{second}"
                    )
                    minimum_endpoint_projection_clearance = min(
                        minimum_endpoint_projection_clearance,
                        lower(abs(x0)),
                        lower(abs(x1)),
                    )
                    if sign0 == sign1:
                        continue
                    parameter = x0 / (x0 - x1)
                    if not parameter.lower() > 0 or not parameter.upper() < 1:
                        raise AssertionError("crossing parameter not strictly internal")
                    crossing_height = (
                        (1 - parameter) * left_difference.imag
                        + parameter * right_difference.imag
                    )
                    height_sign = strict_sign(
                        crossing_height,
                        f"{handle['name']} segment {segment_index} crossing height",
                    )
                    minimum_crossing_height = min(
                        minimum_crossing_height, lower(abs(crossing_height))
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
                multi_event_segment_count += 1
                for left_event, right_event in zip(events, events[1:]):
                    gap = right_event["parameter"].lower() - left_event["parameter"].upper()
                    if not gap > 0:
                        raise AssertionError("same-segment crossing order unresolved")
                    minimum_event_parameter_gap = min(
                        minimum_event_parameter_gap, lower(gap)
                    )

            for event in events:
                first = event["first"]
                second = event["second"]
                first_position = order.index(first)
                second_position = order.index(second)
                if abs(first_position - second_position) != 1:
                    raise AssertionError("certified crossing is not adjacent")
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
                range(6),
                key=lambda label: float(projected[segment_index + 1][label].real.mid()),
            )
            for left_label, right_label in zip(right_order, right_order[1:]):
                difference = (
                    projected[segment_index + 1][right_label].real
                    - projected[segment_index + 1][left_label].real
                )
                if not difference.lower() > 0:
                    raise AssertionError("endpoint projected order unresolved")
            if order != right_order:
                raise AssertionError("crossing replay disagrees with endpoint order")

        expected_word = [tuple(value) for value in handle["raw_braid_word"]]
        if word != expected_word:
            raise AssertionError(f"interval braid word mismatch for handle {handle['name']}")

        base_roots = roots[0]
        final_roots = roots[-1]
        final_permutation: list[int] = []
        minimum_endpoint_match_gap = math.inf
        for label, final_root in enumerate(final_roots):
            final_uncertainty = (
                point_radii[-1, label] + 4e-15 * (1 + abs(final_root))
            )
            distances = [abs(final_root - base_root) for base_root in base_roots]
            target = int(np.argmin(distances))
            target_uncertainty = (
                point_radii[0, target] + 4e-15 * (1 + abs(base_roots[target]))
            )
            target_upper = distances[target] + final_uncertainty + target_uncertainty
            other_lower = min(
                distances[other]
                - final_uncertainty
                - point_radii[0, other]
                - 4e-15 * (1 + abs(base_roots[other]))
                for other in range(6)
                if other != target
            )
            gap = other_lower - target_upper
            if gap <= 0:
                raise AssertionError("handle endpoint root matching unresolved")
            minimum_endpoint_match_gap = min(minimum_endpoint_match_gap, gap)
            final_permutation.append(target)
        if final_permutation != handle["final_root_permutation"]:
            raise AssertionError("endpoint permutation mismatch")

        action = identity
        for generator, sign in word:
            action = (positive if sign == 1 else negative)[generator - 1] * action
        expected_action = sp.Matrix(handle["integral_symplectic_matrix_candidate"])
        if action != expected_action:
            raise AssertionError("homology-action replay mismatch")
        if action.T * intersection * action != intersection:
            raise AssertionError("handle action is not symplectic")
        if action.det() != 1:
            raise AssertionError("handle action determinant mismatch")
        promoted_matrices[handle["name"]] = action

        certified_handles.append(
            {
                "name": handle["name"],
                "segments": len(roots) - 1,
                "crossing_count": len(word),
                "multi_event_segment_count": multi_event_segment_count,
                "minimum_projected_endpoint_pair_difference_lower": format(
                    minimum_endpoint_projection_clearance, ".17g"
                ),
                "minimum_crossing_height_lower": format(
                    minimum_crossing_height, ".17g"
                ),
                "minimum_same_segment_event_parameter_gap_lower": (
                    format(minimum_event_parameter_gap, ".17g")
                    if minimum_event_parameter_gap < math.inf
                    else None
                ),
                "minimum_endpoint_matching_gap_lower": format(
                    minimum_endpoint_match_gap, ".17g"
                ),
                "raw_braid_word": [[generator, sign] for generator, sign in word],
                "final_root_permutation": final_permutation,
                "promoted_integral_symplectic_matrix": matrix_rows(action),
                "determinant": int(action.det()),
                "symplectic": True,
                "continuous_root_tube_certificate": True,
                "promotion_accepted": True,
            }
        )

    handle_a = promoted_matrices["A"]
    handle_b = promoted_matrices["B"]
    commutator = handle_a * handle_b * handle_a.inv() * handle_b.inv()
    payload = {
        "schema": "MTTQ79GenusTwoHandlePLBraidIntervalCertificate.v1",
        "status": "TWO_HANDLE_BRAIDS_AND_SP4Z_ACTIONS_PROMOTED",
        "authority": {
            "exploration_sha256": sha256(EXPLORATION),
            "continuous_root_tube_certificate_sha256": sha256(TUBES),
            "python_flint_version": "0.9.0",
        },
        "projection": {
            "rotation": "exp(-i*pi/7)",
            "precision_decimal_digits": ctx.dps,
            "all_endpoint_orders_interval_certified": True,
            "all_crossing_heights_interval_certified_nonzero": True,
            "all_same_segment_event_orders_interval_certified": True,
        },
        "topological_bridge": {
            "name": "Birman-Hilden hyperelliptic lifting",
            "specialization": "each standard half-twist of six branch points lifts to the corresponding genus-two chain Dehn twist",
            "homology_action": "T_delta = I-delta*delta^T*J in the frozen [a1,b1,a2,b2] marking",
        },
        "handles": certified_handles,
        "aggregate": {
            "promoted_handle_count": len(certified_handles),
            "matrices_noncommuting": handle_a * handle_b != handle_b * handle_a,
            "handle_commutator": matrix_rows(commutator),
            "commutator_symplectic": commutator.T * intersection * commutator == intersection,
        },
        "strict_scope": {
            "ninety_local_meridian_matrices_promoted": 0,
            "distinguished_global_cut_system_closed": False,
            "global_surface_relation_checked": False,
            "beta_C_period_rows_emitted": 0,
        },
    }
    dump(OUTPUT, payload)
    print(f"wrote {OUTPUT}")
    for row in certified_handles:
        print(
            f"handle {row['name']}: {row['segments']} segments, "
            f"{row['crossing_count']} crossings, promoted Sp4Z action"
        )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
