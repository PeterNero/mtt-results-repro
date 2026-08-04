from __future__ import annotations

import argparse
import hashlib
import json
import math
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
VALIDATED = (
    ROOT
    / "candidate_data"
    / "selected_q79covariantperiodbranchcutsetandtightbetatransport"
    / "selected_alignment_thimble_periods"
    / "covariant_floating_probe"
    / "validated_transport"
)
A404 = VALIDATED / "n3.junction_operator_sweep.a404.json"
A413 = VALIDATED / "ol" / "all76.a413.json"


def load(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def complex_value(value: dict[str, str]) -> complex:
    return complex(float(value["real"]), float(value["imaginary"]))


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--index", type=int, required=True)
    arguments = parser.parse_args()
    output = VALIDATED / "ol" / f"d{arguments.index:03d}.a414.json"
    checkpoint_path = VALIDATED / "ol" / f"d{arguments.index:03d}.a414.ckpt.json"
    packet = load(output)
    checkpoint = load(checkpoint_path)
    source_manifest = load(A413)
    junction = load(A404)
    if packet.get("artifact") != "A414":
        raise AssertionError("A414 artifact changed")
    if packet["authority"]["A413_source_manifest"]["sha256"] != sha256(A413):
        raise AssertionError("A414 A413 authority is stale")
    if packet["authority"]["A404_common_junction_manifest"]["sha256"] != sha256(A404):
        raise AssertionError("A414 A404 authority is stale")
    if packet["authority"]["completed_correlated_row_checkpoint"]["sha256"] != sha256(checkpoint_path):
        raise AssertionError("A414 checkpoint authority is stale")
    contract = next(
        row for row in source_manifest["target_rows"]
        if int(row["distinguished_index"]) == arguments.index
    )
    target = packet["selected_target"]
    if int(target["distinguished_index"]) != arguments.index or target["root_id"] != contract["root_id"]:
        raise AssertionError("A414 selected target changed")
    if int(target["A130_raw_chain_coefficient"]) != int(contract["A130_raw_chain_coefficient"]):
        raise AssertionError("A414 raw coefficient changed")
    if int(target["endpoint_floating_chain_coefficient"]) != int(contract["endpoint_floating_chain_coefficient"]):
        raise AssertionError("A414 floating coefficient changed")
    if int(target["canonical_cycle_to_floating_orientation_sign"]) != int(contract["canonical_cycle_to_floating_orientation_sign"]):
        raise AssertionError("A414 cycle orientation changed")
    if not checkpoint.get("complete") or len(checkpoint["centers"]) != 8 or len(checkpoint["frames"]) != 8:
        raise AssertionError("A414 checkpoint is incomplete")
    endpoint = complex_value(packet["A404_entry"]["point"])
    if checkpoint["configuration"]["endpoint"] != packet["A404_entry"]["point"]:
        raise AssertionError("A414 checkpoint endpoint changed")
    start = complex_value(checkpoint["configuration"]["start"])
    ratio = start / endpoint
    cross = abs(start.real * endpoint.imag - start.imag * endpoint.real) / (abs(start) * abs(endpoint))
    if cross > 3.0e-14 or ratio.real <= 1.0 or abs(ratio.imag) > 3.0e-13:
        raise AssertionError("A414 radial geometry changed")
    execution = packet["validated_outer_main_transport"]
    if int(execution["accepted_step_count"]) != len(execution["steps"]):
        raise AssertionError("A414 accepted-step count changed")
    total_step = sum(float(row["step"]) for row in execution["steps"])
    if not math.isclose(total_step, float(execution["path_length"]), rel_tol=2.0e-13, abs_tol=1.0e-14):
        raise AssertionError("A414 path length does not replay")
    if len(packet["floating_oriented_entry_period_centers"]) != 5 or len(packet["A130_oriented_entry_period_centers"]) != 5:
        raise AssertionError("A414 period dimensions changed")
    if len(packet["floating_oriented_outer_main_residue_centers"]) != 8 or len(packet["A130_oriented_outer_main_residue_centers"]) != 8:
        raise AssertionError("A414 residue dimensions changed")
    orientation = int(target["canonical_cycle_to_floating_orientation_sign"])
    for floating, raw in zip(
        packet["floating_oriented_entry_period_centers"],
        packet["A130_oriented_entry_period_centers"],
    ):
        if abs(orientation * complex_value(floating) - complex_value(raw)) > 3.0e-14:
            raise AssertionError("A414 A130 period orientation does not replay")
    scope = packet["strict_scope"]
    if not scope["outer_main_leg_to_common_entry_closed"] or not scope["A130_to_floating_orientation_reconciled"]:
        raise AssertionError("A414 closure flags are false")
    if scope["A405_entry_operator_applied"] or scope["covariant_zero_proved"]:
        raise AssertionError("A414 overclaims the frontier")
    if (target["line_chart"] == "z") != scope["A410_y_from_z_transition_required"]:
        raise AssertionError("A414 chart-transition flag changed")
    print(
        f"PASS: A414 d{arguments.index:03d} native-{target['line_chart']} outer leg "
        f"has {execution['accepted_step_count']} certified steps"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
