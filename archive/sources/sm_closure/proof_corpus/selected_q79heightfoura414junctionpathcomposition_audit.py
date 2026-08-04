from __future__ import annotations

import argparse
import hashlib
import json
import math
import sys
from pathlib import Path

from flint import acb, acb_mat, arb, ctx


ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))

import certify_q79_height4_target_full_residue_interval as generic
import certify_q79_selected_side_base_lift_interval as serializer
import certify_q79_selected_side_beta_defect_transport as validated


VALIDATED = (
    ROOT
    / "candidate_data"
    / "selected_q79covariantperiodbranchcutsetandtightbetatransport"
    / "selected_alignment_thimble_periods"
    / "covariant_floating_probe"
    / "validated_transport"
)
A405 = VALIDATED / "n3.junction_operator_sweep.a405.json"
A409T = VALIDATED / "n3.junction_reverse_composition.a409t.json"
A410 = VALIDATED / "pt" / "a410.json"
A411 = VALIDATED / "jop" / "trunk.a411.json"
A413 = VALIDATED / "ol" / "all76.a413.json"


def load(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def complex_value(value: dict[str, str]) -> complex:
    return complex(float(value["real"]), float(value["imaginary"]))


def interval_entry(value: dict) -> acb:
    center = complex_value(value["center"])
    radius = float(value["component_radius_upper"])
    serialization = max(math.ulp(center.real), math.ulp(center.imag), 1.0e-300)
    outward = math.nextafter(radius + serialization, math.inf)
    return acb(
        arb(format(center.real, ".17g"), format(outward, ".17g")),
        arb(format(center.imag, ".17g"), format(outward, ".17g")),
    )


def interval_matrix(rows: list[list[dict]]) -> acb_mat:
    return acb_mat([[interval_entry(value) for value in row] for row in rows])


def column(values: list[acb]) -> acb_mat:
    result = acb_mat(len(values), 1)
    for row, value in enumerate(values):
        result[row, 0] = value
    return result


def chart_block(transition: acb_mat | None) -> acb_mat:
    result = acb_mat(6, 6)
    if transition is None:
        for row in range(5):
            result[row, row] = acb(1)
    else:
        for row in range(5):
            for col in range(5):
                result[row, col] = transition[row, col]
    result[5, 5] = acb(1)
    return result


def reverse_block(period: acb_mat, residue: acb_mat, residue_row: int) -> acb_mat:
    inverse = period.inv()
    coupling = residue * inverse
    result = acb_mat(6, 6)
    for row in range(5):
        for col in range(5):
            result[row, col] = inverse[row, col]
    for col in range(5):
        result[5, col] = coupling[residue_row, col]
    result[5, 5] = acb(1)
    return result


def forward_block(period: acb_mat, residue: acb_mat, residue_row: int) -> acb_mat:
    result = acb_mat(6, 6)
    for row in range(5):
        for col in range(5):
            result[row, col] = period[row, col]
    for col in range(5):
        result[5, col] = -residue[residue_row, col]
    result[5, 5] = acb(1)
    return result


def component_radius(center: acb_mat, generator: acb_mat) -> float:
    generator_radius = sum((abs(generator[5, col]) for col in range(6)), arb(0))
    return validated.radius_upper(center[5, 0]) + validated.upper(generator_radius)


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--index", type=int, required=True)
    arguments = parser.parse_args()
    ctx.dps = 120
    packet_path = VALIDATED / "ol" / f"d{arguments.index:03d}.a415.json"
    outer_path = VALIDATED / "ol" / f"d{arguments.index:03d}.a414.json"
    checkpoint_path = VALIDATED / "ol" / f"d{arguments.index:03d}.a414.ckpt.json"
    packet = load(packet_path)
    outer = load(outer_path)
    checkpoint = load(checkpoint_path)
    source_manifest = load(A413)
    sweep = load(A405)
    transitions = load(A410)
    trunk = load(A411)
    if packet.get("artifact") != "A415":
        raise AssertionError("A415 artifact changed")
    if packet["composition"].get("residue_sign_bridge") != "r_phys=-q":
        raise AssertionError("A415 residue sign bridge changed")
    fixed = {
        "A405_entry_operators": A405,
        "A409T_reverse_composition_theorem": A409T,
        "A410_native_z_transitions": A410,
        "A411_terminal_trunk": A411,
        "A413_source_manifest": A413,
        "A414_outer_leg": outer_path,
        "A414_correlated_checkpoint": checkpoint_path,
    }
    for label, path in fixed.items():
        if packet["authority"][label]["sha256"] != sha256(path):
            raise AssertionError(f"A415 authority is stale: {label}")
    contract = next(
        row for row in source_manifest["target_rows"]
        if int(row["distinguished_index"]) == arguments.index
    )
    tail_path = ROOT / Path(contract["authority"]["canonical_tail"]["path"])
    full_path = ROOT / Path(contract["authority"]["canonical_full"]["path"])
    if packet["authority"]["canonical_local_tail"]["sha256"] != sha256(tail_path):
        raise AssertionError("A415 canonical tail authority is stale")
    if packet["authority"]["canonical_full_residue"]["sha256"] != sha256(full_path):
        raise AssertionError("A415 canonical full authority is stale")
    tail = load(tail_path)
    canonical = load(full_path)
    operator = next(
        row for row in sweep["operators_at_77_entries"]
        if row["entry"].get("kind") == "selected_thimble_entry"
        and int(row["entry"]["distinguished_index"]) == arguments.index
    )
    entry_period = interval_matrix(operator["period_transport_5_by_5"])
    entry_residue = interval_matrix(operator["integrated_residue_operator_8_by_5"])
    trunk_period = interval_matrix(trunk["period_transport_5_by_5"])
    trunk_residue = interval_matrix(trunk["integrated_residue_operator_8_by_5"])
    transition_row = next(
        (row for row in transitions["native_z_entry_transitions"] if int(row["distinguished_index"]) == arguments.index),
        None,
    )
    transition = None
    if transition_row is not None:
        transition = acb_mat(
            [
                [validated.interval_from_bounds(value["interval_bounds"]) for value in row]
                for row in transition_row["y_periods_from_z_periods_5_by_5"]
            ]
        )
    chart = chart_block(transition)
    orientation = int(outer["selected_target"]["transport_orientation_sign"])
    tail_intervals = tail["all_eight_endpoint_tails"]["intervals"]
    canonical_rows = canonical["residue_rows"]
    radii = []
    differences = []
    margins = []
    for residue_row in range(8):
        raw_center = [validated.decoded_acb(value) for value in checkpoint["centers"][residue_row]]
        frame = generic.decoded_frame(checkpoint["frames"][residue_row])
        raw_generator = frame.physical_generator_matrix()
        selected_center = [orientation * value for value in raw_center[:5]] + [-orientation * raw_center[5]]
        selected_generator = acb_mat(6, 6)
        for row in range(6):
            sign = orientation if row < 5 else -orientation
            for col in range(6):
                selected_generator[row, col] = sign * raw_generator[row, col]
        selected_center[5] += orientation * validated.interval_from_bounds(tail_intervals[residue_row])
        common_center = chart * column(selected_center)
        common_generator = chart * selected_generator
        reverse = reverse_block(entry_period, entry_residue, residue_row)
        hub_center = reverse * common_center
        hub_generator = reverse * common_generator
        forward = forward_block(trunk_period, trunk_residue, residue_row)
        base_center = forward * hub_center
        base_generator = forward * hub_generator
        radius = component_radius(base_center, base_generator)
        center = validated.midpoint(base_center[5, 0])
        expected = complex_value(canonical_rows[residue_row]["full_interval_center"])
        expected_radius = float(canonical_rows[residue_row]["full_interval_radius_upper"])
        difference = abs(center - expected)
        margin = radius + expected_radius - difference
        if margin < 0.0:
            raise AssertionError(f"A415 row {residue_row} no longer overlaps canonical")
        stored = packet["residue_rows"][residue_row]
        serialized_generators = {
            "common_y_entry_affine_generator_6_by_6": common_generator,
            "hub_affine_generator_6_by_6": hub_generator,
            "base_affine_generator_6_by_6": base_generator,
        }
        for label, matrix in serialized_generators.items():
            encoded = stored.get(label)
            if not isinstance(encoded, list) or len(encoded) != 6 or any(
                not isinstance(row, list) or len(row) != 6 for row in encoded
            ):
                raise AssertionError(f"A415 row {residue_row} lost {label}")
            for matrix_row in range(6):
                for matrix_col in range(6):
                    if encoded[matrix_row][matrix_col]["interval_bounds"] != serializer.complex_interval(
                        matrix[matrix_row, matrix_col]
                    ):
                        raise AssertionError(
                            f"A415 row {residue_row} {label} does not replay"
                        )
        checks = (
            (radius, float(stored["base_residue_total_radius_upper"])),
            (difference, float(stored["base_to_canonical_center_difference"])),
            (margin, float(stored["overlap_margin"])),
        )
        if any(not math.isclose(left, right, rel_tol=2.0e-13, abs_tol=1.0e-30) for left, right in checks):
            raise AssertionError(f"A415 row {residue_row} diagnostics do not replay")
        radii.append(radius)
        differences.append(difference)
        margins.append(margin)
    summary = packet["summary"]
    summary_checks = (
        (max(radii), float(summary["maximum_base_residue_radius_upper"])),
        (max(differences), float(summary["maximum_base_to_canonical_center_difference"])),
        (min(margins), float(summary["minimum_canonical_overlap_margin"])),
    )
    if any(not math.isclose(left, right, rel_tol=2.0e-13, abs_tol=1.0e-30) for left, right in summary_checks):
        raise AssertionError("A415 summary does not replay")
    scope = packet["strict_scope"]
    if not scope["single_target_alternate_path_composition_closed"] or not scope["independent_canonical_full_residue_crosscheck_closed"]:
        raise AssertionError("A415 closure flags are false")
    if not scope["entry_hub_and_base_affine_generators_serialized"]:
        raise AssertionError("A415 affine-generator payload flag is false")
    if scope["all_76_outer_thimble_paths_closed"] or scope["covariant_zero_proved"]:
        raise AssertionError("A415 overclaims the frontier")
    print(
        f"PASS: A415 d{arguments.index:03d} native-{contract['line_chart']} full "
        f"junction path; minimum canonical overlap {min(margins):.6g}"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
