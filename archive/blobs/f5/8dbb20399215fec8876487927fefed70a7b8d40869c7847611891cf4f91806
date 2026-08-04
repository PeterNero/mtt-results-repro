from __future__ import annotations

import hashlib
import json
import math
from pathlib import Path
import sys

from flint import ctx

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))

import certify_q79_selected_side_beta_defect_transport as validated


VALIDATED = (
    ROOT
    / "candidate_data"
    / "selected_q79covariantperiodbranchcutsetandtightbetatransport"
    / "selected_alignment_thimble_periods"
    / "covariant_floating_probe"
    / "validated_transport"
)
PACKET = VALIDATED / "n3.beta_minus_B.source.a402s.json"
A375 = VALIDATED / "n3.rank3.base_lift.interval.json"
A374 = VALIDATED / "n3.rank3.handle_combination.interval.json"
A383 = VALIDATED / "n3.rank3.handle_hessian.interval.json"
B_CHECKPOINT = VALIDATED / "n3.handleB.hessian.checkpoint.json"
A401 = VALIDATED / "n3.lower_b_contour_homotopy.a401.json"


def load(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def main() -> int:
    ctx.dps = 100
    packet = load(PACKET)
    base = load(A375)
    handle = load(A374)
    handle_hessian = load(A383)
    checkpoint = load(B_CHECKPOINT)
    homotopy = load(A401)

    expected_authorities = {
        "A375_rank3_beta_base_lift": A375,
        "A374_selected_handle": A374,
        "A383_handle_Hessian_interval": A383,
        "A383_validated_B_path_checkpoint": B_CHECKPOINT,
        "A401_lower_B_contour_homotopy": A401,
    }
    for name, path in expected_authorities.items():
        if packet["authority"][name]["sha256"] != sha256(path):
            raise AssertionError(f"stale A402S authority: {name}")

    coordinates = [
        int(value)
        for value in handle["selected_rank3_chain"]["primitive_handle_coordinates"]
    ]
    if coordinates[4:] != [1, 0, 0, 1]:
        raise AssertionError("the independently read B-handle coordinates changed")
    if not homotopy["strict_scope"]["straight_to_lower_B_contour_homotopy_closed"]:
        raise AssertionError("A401 no longer certifies the contour homotopy")
    if (
        handle_hessian["authority"]["B_path_checkpoint"]["sha256"]
        != sha256(B_CHECKPOINT)
    ):
        raise AssertionError("A383 B-path checkpoint authority changed")

    beta = [validated.interval_from_bounds(value) for value in base["y_chart_base_lift"]]
    b_initial = [
        validated.decoded_acb(value)
        for value in checkpoint["configuration"]["initial_periods"]
    ]
    emitted = [
        validated.interval_from_bounds(value) for value in packet["y_chart_base_lift"]
    ]
    if not (len(beta) == len(b_initial) == len(emitted) == 5):
        raise AssertionError("A402S source dimensions changed")
    for index, (left, right, actual) in enumerate(zip(beta, b_initial, emitted)):
        expected = left - right
        if not actual.overlaps(expected):
            raise AssertionError(f"A402S row {index} does not enclose beta-B")
        if not (actual + right).overlaps(left):
            raise AssertionError(f"A402S row {index} fails reconstruction")
    emitted_maximum_radius = max(validated.radius_upper(value) for value in emitted)
    if not math.isclose(
        float(packet["summary"]["maximum_component_ball_radius_upper"]),
        emitted_maximum_radius,
        rel_tol=2.0e-15,
        abs_tol=0.0,
    ):
        raise AssertionError("A402S serialized source radius does not replay")

    scope = packet["strict_scope"]
    if not scope["beta_minus_B_initial_source_interval_closed"]:
        raise AssertionError("A402S source closure flag is false")
    if scope["joint_beta_minus_B_handle_transport_executed"]:
        raise AssertionError("A402S overclaims endpoint execution")
    identity = packet["theorem"]["transport_identity"]
    if "nu_rel'=A nu_rel+s" not in identity or "homogeneous" in identity:
        raise AssertionError("A402S states the affine difference equation incorrectly")
    print(
        "PASS: A402S independently reconstructs all five beta-minus-B source "
        "intervals and consumes the A401 contour theorem"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
