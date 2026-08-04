from __future__ import annotations

import hashlib
import json
import sys
from pathlib import Path

import numpy as np
from flint import acb


ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))

import certify_q79_selected_alignment_E32_handle_combination_interval as handle
import certify_q79_selected_side_beta_defect_transport as validated


CANDIDATE = ROOT / "candidate_data" / "selected_q79e32primitivehandlebasisintervals.candidate.json"
CERTIFICATE = ROOT / "certificates" / "selected_q79e32primitivehandlebasisintervals.certificate.json"


def load(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def main() -> int:
    candidate = load(CANDIDATE)
    certificate = load(CERTIFICATE)
    packet_path = ROOT / candidate["packet"]
    packet = load(packet_path)
    if candidate["artifact"] != "A209" or packet["artifact"] != "A209":
        raise AssertionError("A209 artifact label changed")
    if sha256(packet_path) != candidate["packet_sha256"]:
        raise AssertionError("A209 packet hash mismatch")
    if sha256(ROOT / candidate["note"]) != candidate["note_sha256"]:
        raise AssertionError("A209 proof-note hash mismatch")
    if sha256(CANDIDATE) != certificate["candidate_sha256"]:
        raise AssertionError("A209 candidate hash mismatch")
    if candidate["closure_claimed"] or certificate["closure_claimed"]:
        raise AssertionError("A209 overclaims carrier closure")

    for path_key, hash_key in (
        ("A208_survivor_queue", "A208_survivor_queue_sha256"),
        ("A131_floating_handle_packet", "A131_floating_handle_packet_sha256"),
        ("A131_orientation_packet", "A131_orientation_packet_sha256"),
        ("A207_handle_interval", "A207_handle_interval_sha256"),
        ("certifier_source", "certifier_source_sha256"),
    ):
        path = ROOT / packet["authority"][path_key]
        if sha256(path) != packet["authority"][hash_key]:
            raise AssertionError(f"A209 authority hash mismatch: {path_key}")
    for relative, digest in packet["authority"]["primitive_column_packets"].items():
        if sha256(ROOT / relative) != digest:
            raise AssertionError(f"A209 primitive-column hash mismatch: {relative}")

    coordinate = packet["coordinate_identity"]
    expected_order = [
        "A:a1",
        "A:b1",
        "A:a2",
        "A:b2",
        "B:a1",
        "B:b1",
        "B:a2",
        "B:b2",
    ]
    if coordinate["primitive_column_order"] != expected_order:
        raise AssertionError("A209 primitive handle order changed")
    primitive = packet["primitive_E32_handle_intervals"]
    if len(primitive) != 8 or [row["label"] for row in primitive] != expected_order:
        raise AssertionError("A209 primitive interval ledger changed")
    primitive_balls = []
    for index, row in enumerate(primitive):
        if row["column_index"] != index:
            raise AssertionError("A209 primitive column index changed")
        ball = validated.interval_from_bounds(row["E32_interval"])
        primitive_balls.append(ball)
        source_radius = float(row["E32_interval_radius_upper"])
        component_radii = (
            validated.upper(ball.real.rad()),
            validated.upper(ball.imag.rad()),
        )
        if any(radius < source_radius for radius in component_radii):
            raise AssertionError("A209 primitive serialization shrank a component radius")
        if max(radius - source_radius for radius in component_radii) > 1.0e-10:
            raise AssertionError("A209 primitive component-radius replay mismatch")
        expected = handle.complex_value(row["A131_floating_center"])
        center = handle.midpoint(ball)
        if abs(abs(center - expected) - row["A131_center_difference"]) > 1.0e-12:
            raise AssertionError("A209 primitive center replay mismatch")
        if row["A131_center_difference"] >= 1.0e-6:
            raise AssertionError("A209 primitive center gate failed")

    a208 = load(ROOT / packet["authority"]["A208_survivor_queue"])
    expected_coordinates = {
        row["candidate_id"]: row["primitive_handle_coordinates"]
        for row in a208["height_four_candidates"]
    }
    combinations = packet["height_four_candidate_handle_combinations"]
    if len(combinations) != 5 or {row["candidate_id"] for row in combinations} != set(expected_coordinates):
        raise AssertionError("A209 survivor combination ledger changed")
    for row in combinations:
        coordinates = [int(value) for value in row["primitive_handle_coordinates"]]
        if coordinates != expected_coordinates[row["candidate_id"]]:
            raise AssertionError("A209 survivor handle coordinates changed")
        replay = acb(0)
        for coefficient, ball in zip(coordinates, primitive_balls):
            replay += acb(coefficient) * ball
        stored = validated.interval_from_bounds(row["E32_interval"])
        if not stored.contains(replay) and not replay.contains(stored):
            stored_center = handle.midpoint(stored)
            replay_center = handle.midpoint(replay)
            if abs(stored_center - replay_center) > (
                validated.radius_upper(stored) + validated.radius_upper(replay)
            ):
                raise AssertionError("A209 survivor interval replay is disjoint")
        if row["A131_center_difference"] >= 5.0e-6:
            raise AssertionError("A209 survivor center gate failed")

    base = packet["rigorous_base_cut_basis"]
    if base["basis_order"] != ["a1", "b1", "a2", "b2"]:
        raise AssertionError("A209 base-cut basis order changed")
    if max(base["basis_center_errors_against_A131"]) >= 1.0e-6:
        raise AssertionError("A209 base-cut orientation gate failed")
    if not packet["A207_independent_cross_check"][
        "primitive_basis_interval_overlaps_direct_A207_interval"
    ]:
        raise AssertionError("A209 direct A207 cross-check failed")
    if packet["scope"]["survivor_E32_zero_decisions_closed"]:
        raise AssertionError("A209 invents survivor decisions")

    print("q79 A209 E32 primitive handle basis interval audit: PASS")
    print("closed: four rigorous base cuts and eight primitive A/B E32 handle intervals")
    print("closed: interval handle combinations for all five A208 height-four rows")
    print("open: thimble aggregation and survivor E32 zero decisions")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
