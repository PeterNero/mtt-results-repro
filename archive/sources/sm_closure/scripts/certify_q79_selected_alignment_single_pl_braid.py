from __future__ import annotations

import argparse
import hashlib
import json
import math
from pathlib import Path

import numpy as np
import sympy as sp
from flint import acb, arb, ctx


ROOT = Path(__file__).resolve().parents[1]
DIRECTORY = (
    ROOT
    / "candidate_data"
    / "selected_q79covariantperiodbranchcutsetandtightbetatransport"
)
MONODROMY = DIRECTORY / "selected_alignment_meridian_monodromy"
TUBES = DIRECTORY / "selected_alignment_continuous_root_tubes"
OUTPUT = DIRECTORY / "selected_alignment_interval_braid_certificates"
HOMOLOGY = (
    ROOT
    / "candidate_data"
    / "selected_q79genus2picardlefschetzmonodromyexecution"
    / "numerical_monodromy_exploration.packet.json"
)


def load(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


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


def word_sha256(word: list[list[int]]) -> str:
    return hashlib.sha256(
        json.dumps(word, separators=(",", ":")).encode("ascii")
    ).hexdigest()


def matrix_rows(value: sp.Matrix) -> list[list[int]]:
    return [[int(value[row, column]) for column in range(value.cols)] for row in range(value.rows)]


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--distinguished-index", type=int, required=True)
    parser.add_argument("--root-id", required=True)
    arguments = parser.parse_args()
    index = arguments.distinguished_index
    root_id = arguments.root_id
    stem = f"d{index:03d}_{root_id}"
    packet_path = MONODROMY / f"{stem}.packet.json"
    packet = load(packet_path)
    numeric_packet = packet
    if packet["schema"] == "MTTQ79SelectedAlignmentHandleRootTubeAdapter.v1":
        source_path = ROOT / packet["authority"]["handle_monodromy_packet_path"]
        if sha256(source_path) != packet["authority"]["handle_monodromy_packet_sha256"]:
            raise AssertionError("selected handle adapter authority mismatch")
        numeric_packet = load(source_path)
    trajectory_path = ROOT / packet["trajectory"]["path"]
    if sha256(trajectory_path) != packet["trajectory"]["sha256"]:
        raise AssertionError("selected braid trajectory hash mismatch")
    tube_path = TUBES / f"{stem}.root_tube_certificate.packet.json"
    tube = load(tube_path)
    if tube["authority"]["monodromy_packet_sha256"] != sha256(packet_path):
        raise AssertionError("selected braid/tube carrier mismatch")
    if not tube["acceptance"]["promotion_ready"]:
        raise AssertionError("selected braid root tubes are not promotion ready")

    ctx.dps = 80
    homology = load(HOMOLOGY)["homology_convention"]
    intersection = sp.Matrix(homology["intersection_matrix"])
    vectors = [sp.Matrix(vector) for vector in homology["chain_vectors_for_sigma_1_to_sigma_5"]]
    positive = [sp.eye(4) - vector * vector.T * intersection for vector in vectors]
    negative = [value.inv() for value in positive]
    angle = arb.pi() / 7
    rotation = acb(angle.cos(), -angle.sin())

    with np.load(trajectory_path) as data:
        roots = data["roots"]
    order = list(range(6))
    word: list[tuple[int, int]] = []
    minimum_projection_clearance = math.inf
    minimum_crossing_height = math.inf
    minimum_event_gap = math.inf
    multi_event_segments = 0
    left = [rotation * exact_complex(complex(value)) for value in roots[0]]
    initial_order = sorted(range(6), key=lambda label: float(left[label].real.mid()))
    if initial_order != order:
        raise AssertionError(f"{stem} initial branch marking changed")

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
                    x0, f"{stem} segment {segment_index} left projection"
                )
                sign1 = strict_sign(
                    x1, f"{stem} segment {segment_index} right projection"
                )
                minimum_projection_clearance = min(
                    minimum_projection_clearance, lower(abs(x0)), lower(abs(x1))
                )
                if sign0 == sign1:
                    continue
                parameter = x0 / (x0 - x1)
                if not parameter.lower() > 0 or not parameter.upper() < 1:
                    raise AssertionError(f"{stem} crossing parameter unresolved")
                height = (
                    (1 - parameter) * left_difference.imag
                    + parameter * right_difference.imag
                )
                height_sign = strict_sign(
                    height, f"{stem} segment {segment_index} crossing height"
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
                gap = right_event["parameter"].lower() - left_event["parameter"].upper()
                if not gap > 0:
                    raise AssertionError(f"{stem} same-segment event order unresolved")
                minimum_event_gap = min(minimum_event_gap, lower(gap))
        for event in events:
            first = event["first"]
            second = event["second"]
            first_position = order.index(first)
            second_position = order.index(second)
            if abs(first_position - second_position) != 1:
                raise AssertionError(f"{stem} crossing is not adjacent")
            generator = min(first_position, second_position)
            left_label = order[generator]
            sign = 1 if (
                (event["height_sign"] > 0 and left_label == first)
                or (event["height_sign"] < 0 and left_label == second)
            ) else -1
            word.append((generator + 1, sign))
            order[generator], order[generator + 1] = (
                order[generator + 1], order[generator]
            )

        right_order = sorted(
            range(6), key=lambda label: float(right[label].real.mid())
        )
        for left_label, right_label in zip(right_order, right_order[1:]):
            if not (
                right[right_label].real - right[left_label].real
            ).lower() > 0:
                raise AssertionError(f"{stem} endpoint order unresolved")
        if order != right_order:
            raise AssertionError(f"{stem} crossing replay/order mismatch")
        left = right

    expected_word = [tuple(value) for value in numeric_packet["braid"]["raw_word"]]
    if word != expected_word:
        raise AssertionError(f"{stem} interval word mismatch")
    if order != numeric_packet["braid"]["final_order"]:
        raise AssertionError(f"{stem} final order mismatch")

    action = sp.eye(4)
    for generator, sign in word:
        action = (positive if sign == 1 else negative)[generator - 1] * action
    expected_matrix = sp.Matrix(
        numeric_packet["homology"].get(
            "integral_picard_lefschetz_matrix",
            numeric_packet["homology"].get("integral_symplectic_matrix"),
        )
    )
    if action != expected_matrix:
        raise AssertionError(f"{stem} exact braid replay matrix mismatch")
    if action.det() != 1 or action.T * intersection * action != intersection:
        raise AssertionError(f"{stem} replay matrix is not integral symplectic")

    payload = {
        "schema": "MTTQ79SelectedAlignmentSingleIntervalBraidCertificate.v1",
        "status": "SELECTED_ALIGNMENT_INTERVAL_BRAID_WORD_CERTIFIED",
        "distinguished_index": index,
        "root_id": root_id,
        "authority": {
            "typed_monodromy_packet_sha256": sha256(packet_path),
            "trajectory_sha256": sha256(trajectory_path),
            "root_tube_certificate_sha256": sha256(tube_path),
            "homology_convention_sha256": sha256(HOMOLOGY),
        },
        "projection": {
            "rotation": "exp(-i*pi/7)",
            "precision_decimal_digits": ctx.dps,
        },
        "certificate": {
            "certified_path_segments": len(roots) - 1,
            "interval_certified_crossings": len(word),
            "raw_braid_word_sha256": word_sha256(
                [[generator, sign] for generator, sign in word]
            ),
            "minimum_projected_endpoint_pair_difference_lower": format(
                minimum_projection_clearance, ".17g"
            ),
            "minimum_crossing_height_lower": (
                format(minimum_crossing_height, ".17g")
                if minimum_crossing_height < math.inf
                else None
            ),
            "minimum_same_segment_event_parameter_gap_lower": (
                format(minimum_event_gap, ".17g")
                if minimum_event_gap < math.inf
                else None
            ),
            "multi_event_segment_count": multi_event_segments,
            "final_order": order,
            "final_root_permutation": numeric_packet["braid"]["final_root_permutation"],
            "integral_symplectic_matrix": matrix_rows(action),
        },
        "acceptance": {
            "continuous_root_tube_isotopy_certified": True,
            "polygonal_braid_word_interval_certified": True,
            "exact_integral_matrix_replay_matches": True,
            "promotion_ready": True,
        },
    }
    OUTPUT.mkdir(parents=True, exist_ok=True)
    output = OUTPUT / f"{stem}.braid_certificate.packet.json"
    output.write_text(
        json.dumps(payload, indent=2, sort_keys=True) + "\n",
        encoding="utf-8",
    )
    print(f"wrote {output.relative_to(ROOT)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
