from __future__ import annotations

import hashlib
import json
import math
from pathlib import Path

from flint import arb


ROOT = Path(__file__).resolve().parents[1]
DIRECTORY = (
    ROOT
    / "candidate_data"
    / "selected_q79covariantperiodbranchcutsetandtightbetatransport"
    / "selected_alignment_thimble_periods"
    / "covariant_floating_probe"
    / "validated_transport"
)
PACKET = DIRECTORY / "n3.beta_minus_B.augmented.a402.json"
SOURCE = DIRECTORY / "n3.beta_minus_B.source.a402s.json"
A401 = DIRECTORY / "n3.lower_b_contour_homotopy.a401.json"
A376 = DIRECTORY / "n3.rank3.anchored_beta.interval.json"
B_CHECKPOINT = DIRECTORY / "n3.handleB.hessian.checkpoint.json"


def load(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def complex_value(value: dict[str, str]) -> complex:
    return complex(float(value["real"]), float(value["imaginary"]))


def midpoint_ball(value: dict[str, str]) -> complex:
    def midpoint(text: str) -> float:
        body = text.strip().removeprefix("[").split("+/-", 1)[0].strip()
        return float(body)

    return complex(midpoint(value["real"]), midpoint(value["imaginary"]))


def main() -> int:
    packet = load(PACKET)
    source = load(SOURCE)
    homotopy = load(A401)
    beta = load(A376)
    b_checkpoint = load(B_CHECKPOINT)
    if packet["artifact"] != "A402" or packet["schema"] != (
        "MTTQ79CorrelatedBetaMinusBHandleTransportInterval.v1"
    ):
        raise AssertionError("A402 packet identity changed")

    for name, path in {
        "A402S_correlated_source": SOURCE,
        "A401_common_contour_homotopy": A401,
        "A376_independent_beta_interval": A376,
        "A383_validated_B_path_checkpoint": B_CHECKPOINT,
    }.items():
        if packet["authority"][name]["sha256"] != sha256(path):
            raise AssertionError(f"stale A402 authority: {name}")
    checkpoint = ROOT / packet["execution_configuration"]["checkpoint"]
    if packet["execution_configuration"]["checkpoint_sha256"] != sha256(checkpoint):
        raise AssertionError("A402 checkpoint authority is stale")

    source_waypoints = source["theorem"]["common_contour_waypoints"]
    a401_waypoints = homotopy["contour_homotopy"]["selected_lower_waypoints"]
    if source_waypoints != a401_waypoints:
        raise AssertionError("A402S and A401 waypoint packets differ")
    execution_waypoints = packet["method"]["waypoints"]
    if execution_waypoints != a401_waypoints:
        raise AssertionError("A402 execution did not use the A401 waypoints")
    complex_waypoints = [complex_value(value) for value in a401_waypoints]

    steps = packet["execution"]["steps"]
    if not steps:
        raise AssertionError("A402 contains no validated steps")
    if len(steps) != int(packet["execution"]["accepted_step_count"]):
        raise AssertionError("A402 accepted-step count does not replay")
    positions = list(complex_waypoints[:-1])
    for step in steps:
        segment = int(step["segment_index"])
        if not 0 <= segment < len(positions):
            raise AssertionError("A402 step has an invalid segment index")
        start = complex_value(step["start"])
        end = complex_value(step["end"])
        width = float(step["step"])
        if abs(start - positions[segment]) > 3.0e-14:
            raise AssertionError("A402 path cover has a gap")
        direction = (complex_waypoints[segment + 1] - complex_waypoints[segment])
        direction /= abs(direction)
        if abs(end - start - width * direction) > 3.0e-14:
            raise AssertionError("A402 step leaves the selected segment")
        positions[segment] = end
    for index, position in enumerate(positions):
        if abs(position - complex_waypoints[index + 1]) > 3.0e-14:
            raise AssertionError(f"A402 does not cover segment {index}")
    if any(int(step["augmented_state_dimension"]) != 13 for step in steps):
        raise AssertionError("A402 contains a non-augmented step")
    scale = float(packet["execution_configuration"]["residue_coordinate_scale"])
    if not 0.0 < scale <= 1.0:
        raise AssertionError("A402 weighted-coordinate scale is invalid")
    if any(not step["diagonal_weighted_norm_used"] for step in steps):
        raise AssertionError("A402 contains an unweighted augmented step")
    if any(
        not math.isclose(
            float(step["residue_coordinate_scale"]),
            scale,
            rel_tol=0.0,
            abs_tol=1.0e-17,
        )
        for step in steps
    ):
        raise AssertionError("A402 weighted-coordinate scale changed during transport")
    if any(not step["all_returned_bounds_finite"] for step in steps):
        raise AssertionError("A402 contains a nonfinite step bound")
    radii = [float(value) for value in packet["endpoint"]["component_radius_uppers"]]
    if len(radii) != 8 or not all(math.isfinite(value) and value >= 0 for value in radii):
        raise AssertionError("A402 endpoint radii are invalid")

    beta_centers = [complex_value(value) for value in beta["endpoint"]["beta_center"]]
    b_centers = [midpoint_ball(value) for value in b_checkpoint["center"][5:13]]
    joint_centers = [complex_value(value) for value in packet["endpoint"]["beta_center"]]
    beta_radius = float(beta["endpoint"]["uniform_component_radius_upper"])
    b_radii = [float(arb(value).upper()) for value in b_checkpoint["output_radii"][:8]]
    independent_radii = [beta_radius + value for value in b_radii]
    for index, (left, right, joint, independent, radius) in enumerate(
        zip(beta_centers, b_centers, joint_centers, independent_radii, radii)
    ):
        if abs(joint - (left - right)) > independent + radius:
            raise AssertionError(f"A402 endpoint row {index} misses the independent box")
    comparison = packet["comparison_to_independent_boxes"]
    maximum_joint = max(radii)
    maximum_independent = max(independent_radii)
    for actual, expected, label in (
        (
            float(comparison["maximum_correlated_component_radius_upper"]),
            maximum_joint,
            "maximum correlated radius",
        ),
        (
            float(comparison["maximum_independent_triangle_radius_upper"]),
            maximum_independent,
            "maximum independent radius",
        ),
        (
            float(comparison["radius_tightening_factor"]),
            maximum_independent / maximum_joint,
            "tightening factor",
        ),
    ):
        if not math.isclose(actual, expected, rel_tol=2.0e-14, abs_tol=0.0):
            raise AssertionError(f"A402 does not replay its {label}")

    scope = packet["strict_scope"]
    if not scope["joint_beta_minus_B_handle_transport_executed"]:
        raise AssertionError("A402 joint transport closure flag is false")
    if not scope["exact_diagonal_weighted_coordinate_conjugation_used"]:
        raise AssertionError("A402 weighted-coordinate theorem flag is false")
    if (
        scope["full_relative_chain_transport_executed"]
        or scope["interval_Newton_existence_and_uniqueness_closed"]
        or scope["covariant_zero_proved"]
        or scope["full_SM_closure_proved"]
    ):
        raise AssertionError("A402 overclaims the remaining relative-chain theorem")
    print(
        "PASS: A402 uses the A401 contour, has a complete finite 13-state "
        "weighted execution, and all eight endpoint boxes overlap the independent replay"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
