from __future__ import annotations

import hashlib
import json
import math
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
A113_PATHS = (
    ROOT
    / "candidate_data"
    / "selected_q79genus2basedpathsystemandmonodromycandidate"
    / "certified_based_meridian_and_handle_paths.packet.json"
)
OUTPUT_DIR = (
    ROOT
    / "candidate_data"
    / "selected_q79genus2distinguishedcutsystemandglobalrelation"
)
OUTPUT = OUTPUT_DIR / "distinguished_radial_fan.packet.json"

BASE = 0.25 + 0.25j
LOW = 0.25
HIGH = 1.25
ROUNDING_GUARD = 2.0e-14


def load(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def packet_complex(value: dict[str, str]) -> complex:
    return complex(float(value["real"]), float(value["imaginary"]))


def complex_packet(value: complex) -> dict[str, str]:
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
        raise AssertionError("canonical coordinate did not enter the open cut square")
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
    if not A113_PATHS.exists():
        raise FileNotFoundError(A113_PATHS)
    source = load(A113_PATHS)
    if len(source["positive_based_meridians"]) != 90:
        raise AssertionError("A113 meridian count")

    rows: list[dict] = []
    centers: dict[str, complex] = {}
    ball_radii: dict[str, float] = {}
    shifts: dict[str, tuple[int, int]] = {}
    for old in source["positive_based_meridians"]:
        root_id = old["root_id"]
        old_center = packet_complex(old["target_lift"])
        center, shift = canonical_lift(old_center)
        centers[root_id] = center
        ball_radii[root_id] = float(old["target_ball_radius_upper"])
        shifts[root_id] = shift

    root_ids = list(centers)
    directions = {root_id: centers[root_id] - BASE for root_id in root_ids}
    angles = {
        root_id: math.atan2(directions[root_id].imag, directions[root_id].real)
        for root_id in root_ids
    }
    if not all(0 < angle < math.pi / 2 for angle in angles.values()):
        raise AssertionError("a canonical critical lift lies outside the open fan quadrant")

    ordered = sorted(root_ids, key=lambda root_id: angles[root_id])
    angle_gaps = [
        angles[right] - angles[left]
        for left, right in zip(ordered, ordered[1:])
    ]
    minimum_angle_gap = min(angle_gaps)
    if minimum_angle_gap <= 0:
        raise AssertionError("radial fan directions are not strictly ordered")

    determinant_lowers: list[float] = []
    for left_index, left in enumerate(ordered):
        for right in ordered[left_index + 1 :]:
            determinant_lower = (
                abs(cross(directions[left], directions[right]))
                - abs(directions[left]) * ball_radii[right]
                - abs(directions[right]) * ball_radii[left]
                - ball_radii[left] * ball_radii[right]
                - ROUNDING_GUARD
            )
            determinant_lowers.append(determinant_lower)
    minimum_direction_determinant_lower = min(determinant_lowers)
    if minimum_direction_determinant_lower <= 0:
        raise AssertionError("critical balls do not have a certified radial order")

    loop_radii: dict[str, float] = {}
    for root_id in ordered:
        center = centers[root_id]
        nearest_other_center = min(
            abs(center - centers[other])
            - ball_radii[root_id]
            - ball_radii[other]
            for other in ordered
            if other != root_id
        )
        nearest_other_ray = min(
            segment_distance(BASE, centers[other], center)
            for other in ordered
            if other != root_id
        )
        boundary_clearance = min(
            center.real - LOW,
            HIGH - center.real,
            center.imag - LOW,
            HIGH - center.imag,
        )
        pole_clearance = min(
            abs(center - (horizontal + 1j * vertical))
            for horizontal in range(0, 3)
            for vertical in range(0, 3)
        )
        radius = min(
            0.004,
            nearest_other_center / 5,
            nearest_other_ray / 5,
            boundary_clearance / 5,
            pole_clearance / 5,
        )
        if radius <= 100 * ball_radii[root_id] + ROUNDING_GUARD:
            raise AssertionError(f"no certified fan-meridian radius for {root_id}")
        loop_radii[root_id] = radius

    segment_critical_clearances: list[float] = []
    segment_pole_clearances: list[float] = []
    circle_critical_clearances: list[float] = []
    circle_pole_clearances: list[float] = []
    circle_boundary_clearances: list[float] = []
    arc_circle_clearances: list[float] = []
    circle_circle_clearances: list[float] = []
    endpoints: dict[str, complex] = {}

    for root_id in ordered:
        center = centers[root_id]
        direction_to_base = (BASE - center) / abs(BASE - center)
        endpoint = center + loop_radii[root_id] * direction_to_base
        endpoints[root_id] = endpoint

    for root_id in ordered:
        center = centers[root_id]
        radius = loop_radii[root_id]
        endpoint = endpoints[root_id]
        own_shift = shifts[root_id]
        direction_to_base = (BASE - center) / abs(BASE - center)
        segment_clearance = math.inf
        circle_clearance = math.inf
        for other in ordered:
            other_center = centers[other]
            other_radius = ball_radii[other]
            for horizontal in range(-2, 3):
                for vertical in range(-2, 3):
                    lifted = other_center + horizontal + 1j * vertical
                    is_own = (
                        other == root_id and horizontal == 0 and vertical == 0
                    )
                    if not is_own:
                        segment_clearance = min(
                            segment_clearance,
                            segment_distance(BASE, endpoint, lifted) - other_radius,
                        )
                        circle_clearance = min(
                            circle_clearance,
                            abs(center - lifted) - radius - other_radius,
                        )
        target_margin = radius - ball_radii[root_id]
        other_circle_clearance = circle_clearance
        circle_clearance = min(other_circle_clearance, target_margin)
        pole_segment = min(
            segment_distance(BASE, endpoint, horizontal + 1j * vertical)
            for horizontal in range(-1, 3)
            for vertical in range(-1, 3)
        )
        pole_circle = min(
            abs(center - (horizontal + 1j * vertical)) - radius
            for horizontal in range(-1, 3)
            for vertical in range(-1, 3)
        )
        boundary_circle = min(
            center.real - LOW,
            HIGH - center.real,
            center.imag - LOW,
            HIGH - center.imag,
        ) - radius
        segment_critical_clearances.append(segment_clearance - ROUNDING_GUARD)
        segment_pole_clearances.append(pole_segment - ROUNDING_GUARD)
        circle_critical_clearances.append(circle_clearance - ROUNDING_GUARD)
        circle_pole_clearances.append(pole_circle - ROUNDING_GUARD)
        circle_boundary_clearances.append(boundary_circle - ROUNDING_GUARD)

        rows.append(
            {
                "distinguished_index": len(rows) + 1,
                "root_id": root_id,
                "angle_from_positive_A_edge_radians": format(
                    angles[root_id], ".17g"
                ),
                "canonical_lift": complex_packet(center),
                "deck_shift_from_A113_lift": list(own_shift),
                "target_ball_radius_upper": format(ball_radii[root_id], ".17g"),
                "outbound_segment": {
                    "start": complex_packet(BASE),
                    "end": complex_packet(endpoint),
                    "critical_ball_clearance_lower": format(
                        segment_critical_clearances[-1], ".17g"
                    ),
                    "elliptic_infinity_clearance_lower": format(
                        segment_pole_clearances[-1], ".17g"
                    ),
                },
                "positive_meridian": {
                    "center": complex_packet(center),
                    "radius": format(radius, ".17g"),
                    "start_angle": format(
                        math.atan2(
                            direction_to_base.imag, direction_to_base.real
                        ),
                        ".17g",
                    ),
                    "orientation": "counterclockwise",
                    "target_winding_number": 1,
                    "target_enclosure_margin_lower": format(
                        target_margin - ROUNDING_GUARD, ".17g"
                    ),
                    "other_critical_ball_clearance_lower": format(
                        other_circle_clearance - ROUNDING_GUARD, ".17g"
                    ),
                    "elliptic_infinity_clearance_lower": format(
                        circle_pole_clearances[-1], ".17g"
                    ),
                    "cut_square_boundary_clearance_lower": format(
                        circle_boundary_clearances[-1], ".17g"
                    ),
                },
                "return_segment": "exact reverse of outbound_segment",
            }
        )

    for left_index, left in enumerate(ordered):
        for right in ordered[left_index + 1 :]:
            arc_circle_clearances.append(
                segment_distance(BASE, endpoints[right], centers[left])
                - loop_radii[left]
                - ROUNDING_GUARD
            )
            arc_circle_clearances.append(
                segment_distance(BASE, endpoints[left], centers[right])
                - loop_radii[right]
                - ROUNDING_GUARD
            )
            circle_circle_clearances.append(
                abs(centers[left] - centers[right])
                - loop_radii[left]
                - loop_radii[right]
                - ROUNDING_GUARD
            )

    all_positive = {
        "minimum_angle_gap": minimum_angle_gap,
        "minimum_direction_determinant_lower": minimum_direction_determinant_lower,
        "minimum_segment_critical_ball_clearance_lower": min(
            segment_critical_clearances
        ),
        "minimum_segment_elliptic_infinity_clearance_lower": min(
            segment_pole_clearances
        ),
        "minimum_circle_critical_ball_clearance_lower": min(
            circle_critical_clearances
        ),
        "minimum_circle_elliptic_infinity_clearance_lower": min(
            circle_pole_clearances
        ),
        "minimum_circle_cut_square_boundary_clearance_lower": min(
            circle_boundary_clearances
        ),
        "minimum_arc_to_other_circle_clearance_lower": min(arc_circle_clearances),
        "minimum_pairwise_circle_clearance_lower": min(circle_circle_clearances),
    }
    if not all(value > 0 for value in all_positive.values()):
        raise AssertionError(f"uncertified radial fan: {all_positive}")

    payload = {
        "schema": "MTTQ79GenusTwoDistinguishedRadialFan.v1",
        "status": "ORDERED_90_MERIDIAN_DISTINGUISHED_CUT_SYSTEM_CERTIFIED_GLOBAL_ACTION_RELATION_OPEN",
        "authority": {
            "A113_paths_path": str(A113_PATHS.relative_to(ROOT)).replace("\\", "/"),
            "A113_paths_sha256": sha256(A113_PATHS),
            "constructor_sha256": hashlib.sha256(
                Path(__file__).read_bytes()
            ).hexdigest(),
        },
        "cut_square": {
            "normalized_torus": "C/(Z+iZ)",
            "closed_square": "[1/4,5/4] x [1/4,5/4]",
            "base_corner": complex_packet(BASE),
            "positive_A_edge": "w(s)=1/4+i/4+s",
            "positive_B_edge": "w(s)=1/4+i/4+i*s",
            "oriented_boundary_word": "A*B*A^-1*B^-1",
            "critical_disks_on_boundary": 0,
            "critical_disks_in_open_square": 90,
        },
        "ordering": {
            "rule": "strictly increasing polar angle from the positive A edge toward the positive B edge",
            "root_ids": ordered,
            "minimum_adjacent_angle_gap_radians_lower": format(
                minimum_angle_gap, ".17g"
            ),
            "minimum_pairwise_direction_determinant_lower": format(
                minimum_direction_determinant_lower, ".17g"
            ),
        },
        "distinguished_positive_meridians": rows,
        "geometric_certificate": {
            key: format(value, ".17g") for key, value in all_positive.items()
        },
        "topology": {
            "pairwise_arc_interiors_disjoint": True,
            "arcs_meet_only_at_the_base_corner": True,
            "each_meridian_encloses_exactly_one_certified_critical_disk": True,
            "all_arcs_and_meridians_lie_in_the_open_cut_square_away_from_the_base": True,
            "ordered_distinguished_cut_system_closed": True,
            "reason": "The strictly ordered radial arcs form an embedded planar fan in the A/B cut square; the certified circles are mutually disjoint and avoid every non-target arc and critical disk.",
        },
        "strict_scope": {
            "distinguished_local_monodromy_matrices_emitted": 0,
            "global_surface_relation_checked": False,
            "next_required_execution": "transport the six branch roots over these 90 loops in the A114 marking and compare their ordered product with the handle commutator under the measured action convention",
        },
    }
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
    OUTPUT.write_text(
        json.dumps(payload, indent=2, sort_keys=True) + "\n", encoding="utf-8"
    )
    print(f"wrote {OUTPUT}")
    print(json.dumps(payload["geometric_certificate"], indent=2, sort_keys=True))
    print("order=" + ",".join(ordered))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
