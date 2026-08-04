from __future__ import annotations

import hashlib
import json
import math
import sys
from pathlib import Path

import numpy as np
from flint import acb, arb

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))

import certify_q79_selected_side_beta_defect_transport as validated


HESSIAN = (
    ROOT
    / "candidate_data"
    / "selected_q79covariantperiodbranchcutsetandtightbetatransport"
    / "selected_alignment_thimble_periods"
    / "covariant_floating_probe"
    / "validated_transport"
    / "hessian"
)
MANIFEST = HESSIAN / "precision.manifest.json"


def load(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def require(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)


def close(left: float, right: float, *, scale: float = 1.0) -> bool:
    return abs(left - right) <= 2.0e-12 * max(scale, abs(left), abs(right))


def complex_value(value: dict[str, str]) -> complex:
    return complex(float(value["real"]), float(value["imaginary"]))


def authority_path(row: dict, label: str) -> Path:
    path = ROOT / row["path"]
    require(path.is_file(), f"{label} authority is absent")
    require(sha256(path) == row.get("sha256"), f"{label} authority is stale")
    return path


def audit_authorities(packet: dict, label: str) -> None:
    for name, row in packet.get("authority", {}).items():
        authority_path(row, f"{label}:{name}")


def audit_bridge_steps(
    steps: list[dict],
    start: float,
    target: float,
    label: str,
) -> None:
    cursor = start
    for index, step in enumerate(steps):
        begin = float(step["start_arclength"])
        end = float(step["end_arclength"])
        width = float(step["step"])
        direction = int(step["direction_sign"])
        require(direction in {-1, 1}, f"{label} bridge direction is not a sign")
        require(close(begin, cursor), f"{label} bridge step {index} is discontinuous")
        require(
            close(end - begin, direction * width),
            f"{label} bridge step {index} width does not replay",
        )
        require(width > 0.0, f"{label} bridge step {index} is nonpositive")
        require(
            step.get("affine_growth_integral_bound") == "A*h*exp(L*h)",
            f"{label} bridge step {index} lost the stable affine majorant",
        )
        require(
            step.get("zero_linear_defect_regularization_by_division") is False,
            f"{label} bridge step {index} used forbidden zero-defect division",
        )
        require(
            step.get("all_returned_bounds_finite") is True,
            f"{label} bridge step {index} has a nonfinite bound",
        )
        cursor = end
    require(close(cursor, target), f"{label} bridge does not end at the meeting point")


def audit_packet(path: Path, packet: dict) -> int:
    index = int(packet["selected_target"]["distinguished_index"])
    label = f"d{index:03d}"
    require(
        packet.get("schema") == "MTTQ79HeightFourTargetMainHessianInterval.v1",
        f"{label} bidirectional main schema changed",
    )
    require(packet.get("artifact") == "A380BD", f"{label} route artifact changed")
    scope = packet["strict_scope"]
    for key in (
        "target_main_Hessian_interval_closed",
        "forward_cutoff_to_meeting_transport_used",
        "reverse_base_to_meeting_transport_used",
        "all_five_meeting_lift_coordinates_overlap",
        "ordinary_main_rows_independently_replayed",
        "same_source_A378_homogeneous_Hessian_rows_used",
    ):
        require(scope.get(key) is True, f"{label} strict scope lost {key}")
    require(scope["observed_SM_values_used"] is False, f"{label} used observed values")
    audit_authorities(packet, label)

    meeting_path = authority_path(packet["authority"]["meeting_certificate"], f"{label}:meeting")
    meeting = load(meeting_path)
    require(
        meeting.get("schema") == "MTTQ79BidirectionalMainHessianMeeting.v1",
        f"{label} meeting schema changed",
    )
    require(int(meeting["distinguished_index"]) == index, f"{label} meeting target changed")
    require(
        meeting["all_five_affine_lift_coordinates_overlap"] is True,
        f"{label} meeting lift overlap reopened",
    )
    audit_authorities(meeting, f"{label}:meeting")
    require(
        packet["execution"]["meeting_certificate"]
        == packet["authority"]["meeting_certificate"],
        f"{label} execution and authority meeting certificates differ",
    )

    forward_position = float(meeting["forward_position"])
    forward_meeting = float(meeting["forward_position_at_meeting"])
    reverse_position = float(meeting["reverse_position_before_bridge"])
    reverse_meeting = float(meeting["reverse_position_at_meeting"])
    forward_config = packet["execution"]["forward_checkpoint_configuration"]
    cutoff = complex_value(forward_config["start"])
    distance = abs(cutoff - complex_value(forward_config["endpoint"]))
    require(close(forward_meeting + reverse_meeting, distance), f"{label} meeting positions do not complement")
    audit_bridge_steps(meeting["forward_bridge_steps"], forward_position, forward_meeting, f"{label}:forward")
    audit_bridge_steps(meeting["reverse_bridge_steps"], reverse_position, reverse_meeting, f"{label}:reverse")

    forward_center = [validated.decoded_acb(value) for value in meeting["forward_center"]]
    reverse_center = [validated.decoded_acb(value) for value in meeting["reverse_center"]]
    require(len(forward_center) == len(reverse_center) == 77, f"{label} meeting state dimension changed")
    forward_frame = validated.LiftErrorFrame(
        fundamental=validated.decoded_matrix(meeting["forward_lift_fundamental"]),
        coordinate_radii=[arb(value) for value in meeting["forward_coordinate_radii"]],
    )
    reverse_frame = validated.LiftErrorFrame(
        fundamental=validated.decoded_matrix(meeting["reverse_lift_fundamental"]),
        coordinate_radii=[arb(value) for value in meeting["reverse_coordinate_radii"]],
    )
    forward_lift_radius = validated.upper(forward_frame.physical_radius())
    reverse_lift_radius = validated.upper(reverse_frame.physical_radius())
    forward_lifts = [
        value + acb(arb(0, forward_lift_radius), arb(0, forward_lift_radius))
        for value in forward_center[:5]
    ]
    reverse_lifts = [
        value + acb(arb(0, reverse_lift_radius), arb(0, reverse_lift_radius))
        for value in reverse_center[:5]
    ]
    replayed_lift_differences = [
        validated.upper(abs(left - right)) for left, right in zip(forward_lifts, reverse_lifts)
    ]
    require(all(left.overlaps(right) for left, right in zip(forward_lifts, reverse_lifts)), f"{label} lift overlap does not replay")
    stored_lift_differences = [float(value) for value in meeting["affine_lift_difference_uppers"]]
    require(len(stored_lift_differences) == 5, f"{label} lift difference count changed")
    for stored, replayed in zip(stored_lift_differences, replayed_lift_differences):
        require(close(stored, replayed), f"{label} lift difference bound does not replay")

    forward_radii = [validated.upper(arb(value)) for value in meeting["forward_output_radii"]]
    reverse_radii = [validated.upper(arb(value)) for value in meeting["reverse_output_radii"]]
    require(len(forward_radii) == len(reverse_radii) == 72, f"{label} output radius dimension changed")
    combined_radii = np.asarray(forward_radii) + np.asarray(reverse_radii)
    canonical_path = authority_path(packet["authority"]["selected_main_replay_interval"], f"{label}:canonical")
    canonical = load(canonical_path)
    orientation = int(canonical["orientation"]["selected_sign"])
    require(orientation in {-1, 1}, f"{label} orientation is not a sign")
    forward_outputs = np.asarray([validated.midpoint(value) for value in forward_center[5:]])
    reverse_outputs = np.asarray([validated.midpoint(value) for value in reverse_center[5:]])
    combined_centers = orientation * (reverse_outputs - forward_outputs)

    rows = packet["main_residue_rows"]
    require(len(rows) == 8, f"{label} ordinary row count changed")
    canonical_centers = np.asarray(
        [complex_value(value) for value in canonical["all_eight_main_residue_rows"]["interval_centers"]]
    )
    canonical_radius = float(
        canonical["all_eight_main_residue_rows"]["common_complex_disk_radius_upper"]
    )
    for row, encoded in enumerate(rows):
        require(int(encoded["residue_index_zero_based"]) == row, f"{label} row order changed")
        center = complex_value(encoded["interval_center"])
        radius = float(encoded["component_radius_upper"])
        require(abs(center - combined_centers[row]) <= 2.0e-12, f"{label} row center does not replay")
        require(close(radius, combined_radii[row]), f"{label} row radius does not replay")
        require(
            abs(center - canonical_centers[row]) <= radius + canonical_radius,
            f"{label} row does not overlap the canonical interval",
        )

    expected_centers = combined_centers[8:].reshape(8, 8).T
    expected_radii = combined_radii[8:].reshape(8, 8).T
    matrix = packet["complex_main_Hessian_8_by_8"]
    require(len(matrix) == 8 and all(len(row) == 8 for row in matrix), f"{label} Hessian shape changed")
    for row in range(8):
        for column in range(8):
            encoded = matrix[row][column]
            center = complex_value(encoded["interval_center"])
            radius = float(encoded["component_radius_upper"])
            require(abs(center - expected_centers[row, column]) <= 2.0e-12, f"{label} Hessian center does not replay")
            require(close(radius, expected_radii[row, column]), f"{label} Hessian radius does not replay")
            require(math.isfinite(radius) and radius >= 0.0, f"{label} Hessian radius is invalid")

    summary = packet["summary"]
    require(int(summary["certified_main_rows"]) == 8, f"{label} summary row count changed")
    require(int(summary["certified_main_Hessian_entries"]) == 64, f"{label} summary Hessian count changed")
    require(close(float(summary["main_Hessian_product_box_frobenius_radius_upper"]), float(np.linalg.norm(expected_radii))), f"{label} Frobenius radius does not replay")
    require(close(float(summary["maximum_main_Hessian_component_radius_upper"]), float(np.max(expected_radii))), f"{label} maximum Hessian radius does not replay")
    require(int(summary["forward_bridge_step_count"]) == len(meeting["forward_bridge_steps"]), f"{label} forward bridge count changed")
    require(int(summary["reverse_bridge_step_count"]) == len(meeting["reverse_bridge_steps"]), f"{label} reverse bridge count changed")
    return index


def main() -> int:
    manifest = load(MANIFEST)
    audited: list[int] = []
    for row in manifest["targets"]:
        if row.get("full_budget_pass") is not True:
            continue
        path = ROOT / row["main_path"]
        if not path.is_file():
            continue
        packet = load(path)
        if packet.get("artifact") == "A380BD":
            audited.append(audit_packet(path, packet))
    require(audited, "no accepted bidirectional main Hessian packet was found")
    print(
        "PASS: independently replayed bidirectional meeting, lift, row, and Hessian "
        f"certificates for {','.join(f'd{index:03d}' for index in audited)}"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
