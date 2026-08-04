from __future__ import annotations

import hashlib
import json
import math
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SOURCE = (
    ROOT
    / "candidate_data"
    / "selected_q79covariantperiodbranchcutsetandtightbetatransport"
    / "selected_alignment_dual_discriminant.interval.packet.json"
)
OUTPUT = (
    ROOT
    / "candidate_data"
    / "selected_q79covariantperiodbranchcutsetandtightbetatransport"
    / "selected_alignment_distinguished_radial_fan.interval.packet.json"
)

BASE = 0.25 + 0.25j
LOW = 0.25
HIGH = 1.25
ROUNDING_GUARD = 2.0e-14


def load(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def dump(path: Path, value: dict) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(
        json.dumps(value, indent=2, sort_keys=True) + "\n",
        encoding="utf-8",
    )


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def encoded_complex(value: complex) -> dict[str, str]:
    return {
        "real": format(value.real, ".17g"),
        "imaginary": format(value.imag, ".17g"),
    }


def canonical_coordinate(value: float) -> tuple[float, int]:
    shift = math.floor(LOW - value) + 1
    lifted = value + shift
    while lifted <= LOW:
        lifted += 1
        shift += 1
    while lifted >= HIGH:
        lifted -= 1
        shift -= 1
    if not LOW < lifted < HIGH:
        raise AssertionError("critical coordinate misses the open cut square")
    return lifted, shift


def canonical_lift(value: complex) -> tuple[complex, tuple[int, int]]:
    real, horizontal = canonical_coordinate(value.real)
    imaginary, vertical = canonical_coordinate(value.imag)
    return complex(real, imaginary), (horizontal, vertical)


def segment_distance(start: complex, end: complex, point: complex) -> float:
    direction = end - start
    if direction == 0:
        return abs(point - start)
    parameter = ((point - start).conjugate() * direction).real / abs(direction) ** 2
    parameter = min(1.0, max(0.0, parameter))
    return abs(point - (start + parameter * direction))


def cross(left: complex, right: complex) -> float:
    return left.real * right.imag - left.imag * right.real


def main() -> int:
    source = load(SOURCE)
    points = source["critical_points_on_E"]["points"]
    if len(points) != 90:
        raise AssertionError("selected critical-point inventory changed")

    centers: dict[str, complex] = {}
    radii: dict[str, float] = {}
    shifts: dict[str, tuple[int, int]] = {}
    for point in points:
        root_id = point["root_id"]
        lift = point["canonical_uniformizing_lift"]
        principal = complex(float(lift["real"]), float(lift["imaginary"]))
        center, shift = canonical_lift(principal)
        centers[root_id] = center
        radii[root_id] = float(lift["radius_upper"])
        shifts[root_id] = shift

    chart_centers: list[complex] = []
    chart_radii: list[float] = []
    for point in source["selected_y_line_chart_zeros"]["points"]:
        lift = point["canonical_uniformizing_lift"]
        principal = complex(float(lift["real"]), float(lift["imaginary"]))
        center, _shift = canonical_lift(principal)
        chart_centers.append(center)
        chart_radii.append(float(lift["radius_upper"]))

    root_ids = list(centers)
    directions = {root_id: centers[root_id] - BASE for root_id in root_ids}
    angles = {
        root_id: math.atan2(directions[root_id].imag, directions[root_id].real)
        for root_id in root_ids
    }
    if not all(0 < value < math.pi / 2 for value in angles.values()):
        raise AssertionError("a selected critical lift lies on the fan boundary")
    ordered = sorted(root_ids, key=angles.get)
    minimum_angle_gap = min(
        angles[right] - angles[left]
        for left, right in zip(ordered, ordered[1:])
    )
    if minimum_angle_gap <= 0:
        raise AssertionError("selected radial directions are not distinct")

    determinant_lowers = []
    for left_index, left in enumerate(ordered):
        for right in ordered[left_index + 1 :]:
            determinant_lowers.append(
                abs(cross(directions[left], directions[right]))
                - abs(directions[left]) * radii[right]
                - abs(directions[right]) * radii[left]
                - radii[left] * radii[right]
                - ROUNDING_GUARD
            )
    minimum_direction_determinant = min(determinant_lowers)
    if minimum_direction_determinant <= 0:
        raise AssertionError("selected critical balls lack a strict radial order")

    loop_radii: dict[str, float] = {}
    for root_id in ordered:
        center = centers[root_id]
        nearest_center = min(
            abs(center - centers[other]) - radii[root_id] - radii[other]
            for other in ordered
            if other != root_id
        )
        nearest_ray = min(
            segment_distance(BASE, centers[other], center)
            for other in ordered
            if other != root_id
        )
        boundary = min(
            center.real - LOW,
            HIGH - center.real,
            center.imag - LOW,
            HIGH - center.imag,
        )
        pole = min(
            abs(center - complex(horizontal, vertical))
            for horizontal in range(0, 3)
            for vertical in range(0, 3)
        )
        radius = min(0.002, nearest_center / 5, nearest_ray / 5, boundary / 5, pole / 5)
        if radius <= 100 * radii[root_id] + ROUNDING_GUARD:
            raise AssertionError(f"no selected meridian radius for {root_id}")
        loop_radii[root_id] = radius

    endpoints = {
        root_id: centers[root_id]
        + loop_radii[root_id]
        * (BASE - centers[root_id])
        / abs(BASE - centers[root_id])
        for root_id in ordered
    }
    rows = []
    segment_critical = []
    segment_pole = []
    circle_critical = []
    circle_pole = []
    circle_boundary = []
    segment_chart = []
    circle_chart = []
    for root_id in ordered:
        center = centers[root_id]
        radius = loop_radii[root_id]
        endpoint = endpoints[root_id]
        other_segment = math.inf
        other_circle = math.inf
        for other in ordered:
            for horizontal in range(-2, 3):
                for vertical in range(-2, 3):
                    lifted = centers[other] + complex(horizontal, vertical)
                    if other == root_id and horizontal == 0 and vertical == 0:
                        continue
                    other_segment = min(
                        other_segment,
                        segment_distance(BASE, endpoint, lifted) - radii[other],
                    )
                    other_circle = min(
                        other_circle,
                        abs(center - lifted) - radius - radii[other],
                    )
        own_margin = radius - radii[root_id]
        segment_critical.append(other_segment - ROUNDING_GUARD)
        circle_critical.append(min(other_circle, own_margin) - ROUNDING_GUARD)
        segment_pole.append(
            min(
                segment_distance(BASE, endpoint, complex(horizontal, vertical))
                for horizontal in range(-1, 3)
                for vertical in range(-1, 3)
            )
            - ROUNDING_GUARD
        )
        circle_pole.append(
            min(
                abs(center - complex(horizontal, vertical)) - radius
                for horizontal in range(-1, 3)
                for vertical in range(-1, 3)
            )
            - ROUNDING_GUARD
        )
        circle_boundary.append(
            min(
                center.real - LOW,
                HIGH - center.real,
                center.imag - LOW,
                HIGH - center.imag,
            )
            - radius
            - ROUNDING_GUARD
        )
        segment_chart.append(
            min(
                segment_distance(
                    BASE,
                    endpoint,
                    chart_center + complex(horizontal, vertical),
                )
                - chart_radius
                for chart_center, chart_radius in zip(chart_centers, chart_radii)
                for horizontal in range(-2, 3)
                for vertical in range(-2, 3)
            )
            - ROUNDING_GUARD
        )
        circle_chart.append(
            min(
                abs(center - chart_center - complex(horizontal, vertical))
                - radius
                - chart_radius
                for chart_center, chart_radius in zip(chart_centers, chart_radii)
                for horizontal in range(-2, 3)
                for vertical in range(-2, 3)
            )
            - ROUNDING_GUARD
        )
        direction_to_base = (BASE - center) / abs(BASE - center)
        rows.append(
            {
                "distinguished_index": len(rows) + 1,
                "root_id": root_id,
                "angle_from_positive_A_edge_radians": format(angles[root_id], ".17g"),
                "canonical_lift": encoded_complex(center),
                "deck_shift_from_principal_lift": list(shifts[root_id]),
                "target_ball_radius_upper": format(radii[root_id], ".17g"),
                "outbound_segment": {
                    "start": encoded_complex(BASE),
                    "end": encoded_complex(endpoint),
                    "critical_ball_clearance_lower": format(segment_critical[-1], ".17g"),
                    "elliptic_infinity_clearance_lower": format(segment_pole[-1], ".17g"),
                    "selected_y_chart_zero_clearance_lower": format(segment_chart[-1], ".17g"),
                },
                "positive_meridian": {
                    "center": encoded_complex(center),
                    "radius": format(radius, ".17g"),
                    "start_angle": format(math.atan2(direction_to_base.imag, direction_to_base.real), ".17g"),
                    "orientation": "counterclockwise",
                    "target_winding_number": 1,
                    "target_enclosure_margin_lower": format(own_margin - ROUNDING_GUARD, ".17g"),
                    "other_critical_ball_clearance_lower": format(other_circle - ROUNDING_GUARD, ".17g"),
                    "elliptic_infinity_clearance_lower": format(circle_pole[-1], ".17g"),
                    "cut_square_boundary_clearance_lower": format(circle_boundary[-1], ".17g"),
                    "selected_y_chart_zero_clearance_lower": format(circle_chart[-1], ".17g"),
                },
                "return_segment": "exact reverse of outbound_segment",
            }
        )

    arc_circle = []
    circle_circle = []
    for left_index, left in enumerate(ordered):
        for right in ordered[left_index + 1 :]:
            arc_circle.extend(
                [
                    segment_distance(BASE, endpoints[right], centers[left])
                    - loop_radii[left]
                    - ROUNDING_GUARD,
                    segment_distance(BASE, endpoints[left], centers[right])
                    - loop_radii[right]
                    - ROUNDING_GUARD,
                ]
            )
            circle_circle.append(
                abs(centers[left] - centers[right])
                - loop_radii[left]
                - loop_radii[right]
                - ROUNDING_GUARD
            )

    certificate = {
        "minimum_angle_gap": minimum_angle_gap,
        "minimum_direction_determinant_lower": minimum_direction_determinant,
        "minimum_segment_critical_ball_clearance_lower": min(segment_critical),
        "minimum_segment_elliptic_infinity_clearance_lower": min(segment_pole),
        "minimum_circle_critical_ball_clearance_lower": min(circle_critical),
        "minimum_circle_elliptic_infinity_clearance_lower": min(circle_pole),
        "minimum_circle_cut_square_boundary_clearance_lower": min(circle_boundary),
        "minimum_segment_selected_y_chart_zero_clearance_lower": min(segment_chart),
        "minimum_circle_selected_y_chart_zero_clearance_lower": min(circle_chart),
        "minimum_arc_to_other_circle_clearance_lower": min(arc_circle),
        "minimum_pairwise_circle_clearance_lower": min(circle_circle),
    }
    if not all(value > 0 for value in certificate.values()):
        raise AssertionError(f"selected radial fan is not certified: {certificate}")

    packet = {
        "schema": "MTTQ79SelectedAlignmentDistinguishedRadialFanInterval.v1",
        "status": "SELECTED_ALIGNMENT_90_MERIDIAN_DISTINGUISHED_CUT_SYSTEM_CERTIFIED",
        "authority": {
            "critical_values_path": str(SOURCE.relative_to(ROOT)).replace("\\", "/"),
            "critical_values_sha256": sha256(SOURCE),
        },
        "cut_square": {
            "normalized_torus": "C/(Z+iZ)",
            "open_square": "(1/4,5/4) x (1/4,5/4)",
            "base_corner": encoded_complex(BASE),
            "critical_disks_in_open_square": 90,
            "selected_y_chart_zero_disks_in_open_square": 3,
        },
        "ordering": {
            "rule": "strictly increasing polar angle from the positive A edge",
            "root_ids": ordered,
        },
        "distinguished_positive_meridians": rows,
        "geometric_certificate": {
            key: format(value, ".17g") for key, value in certificate.items()
        },
        "topology": {
            "pairwise_arc_interiors_disjoint": True,
            "arcs_meet_only_at_base": True,
            "each_meridian_encloses_exactly_one_selected_critical_ball": True,
            "all_paths_avoid_selected_y_chart_zero_balls": True,
            "ordered_distinguished_cut_system_closed": True,
        },
        "strict_scope": {
            "selected_alignment_used": True,
            "critical_value_paths_certified": 90,
            "local_monodromy_matrices_emitted": 0,
            "period_columns_emitted": 0,
            "observed_SM_values_used": False,
        },
    }
    dump(OUTPUT, packet)
    print(f"wrote {OUTPUT.relative_to(ROOT)}")
    print(json.dumps(packet["geometric_certificate"], indent=2, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
