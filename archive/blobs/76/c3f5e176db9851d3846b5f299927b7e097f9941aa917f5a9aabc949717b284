from __future__ import annotations

import hashlib
import json
import math
import sys
from pathlib import Path

from flint import acb, acb_mat, arb, ctx


ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))

import certify_q79_height4_target_full_residue_interval as generic
import certify_q79_selected_side_beta_defect_transport as validated


VALIDATED = (
    ROOT
    / "candidate_data"
    / "selected_q79covariantperiodbranchcutsetandtightbetatransport"
    / "selected_alignment_thimble_periods"
    / "covariant_floating_probe"
    / "validated_transport"
)
A397F = VALIDATED / "far_residue" / "d057.tail_frobenius.a397f.json"
A397 = VALIDATED / "far_residue" / "d057.full.a397.json"
A405 = VALIDATED / "n3.junction_operator_sweep.a405.json"
A409T = VALIDATED / "n3.junction_reverse_composition.a409t.json"
A409O = VALIDATED / "ol" / "d057.a409o.json"
CHECKPOINT = VALIDATED / "ol" / "d057.a409o.ckpt.json"
A411 = VALIDATED / "jop" / "trunk.a411.json"
A413 = VALIDATED / "ol" / "all76.a413.json"
PACKET = VALIDATED / "ol" / "d057.a412.json"


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


def block_reverse(period: acb_mat, residue: acb_mat, residue_row: int) -> acb_mat:
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


def block_forward(period: acb_mat, residue: acb_mat, residue_row: int) -> acb_mat:
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
    ctx.dps = 120
    packet = load(PACKET)
    outer = load(A409O)
    checkpoint = load(CHECKPOINT)
    tail = load(A397F)
    canonical = load(A397)
    sweep = load(A405)
    trunk = load(A411)
    if packet.get("artifact") != "A412":
        raise AssertionError("A412 artifact changed")
    if packet["composition"].get("residue_sign_bridge") != "r_phys=-q":
        raise AssertionError("A412 residue sign bridge changed")
    authorities = {
        "A397F_local_tail": A397F,
        "A397_canonical_full_residue": A397,
        "A405_entry_operators": A405,
        "A409T_reverse_composition_theorem": A409T,
        "A409O_outer_leg": A409O,
        "A409O_correlated_checkpoint": CHECKPOINT,
        "A411_terminal_trunk": A411,
        "A413_source_and_orientation_manifest": A413,
    }
    for label, path in authorities.items():
        if packet["authority"][label]["sha256"] != sha256(path):
            raise AssertionError(f"A412 authority is stale: {label}")

    operator = next(
        row for row in sweep["operators_at_77_entries"] if row["entry"]["label"] == "d057"
    )
    entry_period = interval_matrix(operator["period_transport_5_by_5"])
    entry_residue = interval_matrix(operator["integrated_residue_operator_8_by_5"])
    trunk_period = interval_matrix(trunk["period_transport_5_by_5"])
    trunk_residue = interval_matrix(trunk["integrated_residue_operator_8_by_5"])
    orientation = int(outer["selected_target"]["orientation_sign"])
    tail_rows = tail["all_eight_endpoint_tails"]["rows"]
    canonical_rows = canonical["residue_rows"]
    replay_radii = []
    replay_differences = []
    replay_margins = []
    for residue_row in range(8):
        raw_center = [validated.decoded_acb(value) for value in checkpoint["centers"][residue_row]]
        frame = generic.decoded_frame(checkpoint["frames"][residue_row])
        raw_generator = frame.physical_generator_matrix()
        selected_center = [orientation * value for value in raw_center[:5]] + [
            -orientation * raw_center[5]
        ]
        selected_generator = acb_mat(6, 6)
        for row in range(6):
            sign = orientation if row < 5 else -orientation
            for col in range(6):
                selected_generator[row, col] = sign * raw_generator[row, col]
        selected_center[5] += orientation * validated.interval_from_bounds(
            tail_rows[residue_row]["interval_bounds"]
        )
        reverse = block_reverse(entry_period, entry_residue, residue_row)
        hub_center = reverse * column(selected_center)
        hub_generator = reverse * selected_generator
        forward = block_forward(trunk_period, trunk_residue, residue_row)
        base_center = forward * hub_center
        base_generator = forward * hub_generator
        radius = component_radius(base_center, base_generator)
        center = validated.midpoint(base_center[5, 0])
        expected = complex_value(canonical_rows[residue_row]["full_interval_center"])
        expected_radius = float(canonical_rows[residue_row]["full_interval_radius_upper"])
        difference = abs(center - expected)
        margin = radius + expected_radius - difference
        if margin < 0.0:
            raise AssertionError(f"A412 row {residue_row} no longer overlaps A397")
        stored = packet["residue_rows"][residue_row]
        if not math.isclose(radius, float(stored["base_residue_total_radius_upper"]), rel_tol=2.0e-13):
            raise AssertionError(f"A412 row {residue_row} radius does not replay")
        if not math.isclose(difference, float(stored["base_to_canonical_center_difference"]), rel_tol=2.0e-13, abs_tol=1.0e-30):
            raise AssertionError(f"A412 row {residue_row} center difference does not replay")
        if not math.isclose(margin, float(stored["overlap_margin"]), rel_tol=2.0e-13, abs_tol=1.0e-30):
            raise AssertionError(f"A412 row {residue_row} margin does not replay")
        replay_radii.append(radius)
        replay_differences.append(difference)
        replay_margins.append(margin)

    summary = packet["summary"]
    checks = (
        (max(replay_radii), float(summary["maximum_base_residue_radius_upper"])),
        (max(replay_differences), float(summary["maximum_base_to_A397_center_difference"])),
        (min(replay_margins), float(summary["minimum_A397_overlap_margin"])),
    )
    if any(not math.isclose(left, right, rel_tol=2.0e-13, abs_tol=1.0e-30) for left, right in checks):
        raise AssertionError("A412 summary does not replay")
    scope = packet["strict_scope"]
    if not scope["single_d057_alternate_path_composition_closed"]:
        raise AssertionError("A412 pilot closure flag is false")
    if scope["all_76_outer_thimble_paths_closed"] or scope["covariant_zero_proved"]:
        raise AssertionError("A412 overclaims the remaining frontier")
    print(
        "PASS: A412 independently recomposes the d057 alternate junction path; "
        f"minimum A397 overlap margin {min(replay_margins):.6g}"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
