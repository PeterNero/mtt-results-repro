from __future__ import annotations

import hashlib
import json
import math
from pathlib import Path

from flint import acb, acb_mat, arb


ROOT = Path(__file__).resolve().parents[1]
DIRECTORY = (
    ROOT
    / "candidate_data"
    / "selected_q79covariantperiodbranchcutsetandtightbetatransport"
    / "selected_alignment_thimble_periods"
    / "covariant_floating_probe"
    / "validated_transport"
)
MANIFEST = DIRECTORY / "n3.junction_operator_sweep.a404.json"
RUN_DIRECTORY = DIRECTORY / "jop"
PACKET = DIRECTORY / "n3.junction_operator_sweep.a405.json"


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
    outward_radius = math.nextafter(radius + serialization, math.inf)
    return acb(
        arb(format(center.real, ".17g"), format(outward_radius, ".17g")),
        arb(format(center.imag, ".17g"), format(outward_radius, ".17g")),
    )


def main() -> int:
    packet = load(PACKET)
    manifest = load(MANIFEST)
    if packet["artifact"] != "A405":
        raise AssertionError("A405 artifact changed")
    if packet["authority"]["A404_manifest"]["sha256"] != sha256(MANIFEST):
        raise AssertionError("A405 A404 authority is stale")
    waypoints = [complex_value(value) for value in manifest["polygon_sweep"]["waypoints"]]
    entries = manifest["ordered_entry_rows"]
    for column in range(5):
        result_path = RUN_DIRECTORY / f"basis_{column}.a405.json"
        snapshots_path = RUN_DIRECTORY / f"basis_{column}.a405.snapshots.json"
        result = load(result_path)
        snapshots = load(snapshots_path)
        if packet["authority"][f"basis_{column}_result"]["sha256"] != sha256(result_path):
            raise AssertionError(f"A405 basis {column} result is stale")
        if packet["authority"][f"basis_{column}_snapshots"]["sha256"] != sha256(snapshots_path):
            raise AssertionError(f"A405 basis {column} snapshots are stale")
        rows = snapshots["snapshots"]
        if len(rows) != len(entries) + 1:
            raise AssertionError(f"A405 basis {column} snapshot count changed")
        for segment, row in enumerate(rows):
            if int(row["segment_index"]) != segment or len(row["center"]) != 13:
                raise AssertionError(f"A405 basis {column} snapshot {segment} changed")
            radii = [float(value) for value in row["component_radius_uppers"]]
            if len(radii) != 13 or not all(math.isfinite(value) and value >= 0 for value in radii):
                raise AssertionError(f"A405 basis {column} has invalid radii")
        steps = result["validated_transport"]["execution"]["steps"]
        positions = list(waypoints[:-1])
        for step in steps:
            segment = int(step["segment_index"])
            start = complex_value(step["start"])
            end = complex_value(step["end"])
            width = float(step["step"])
            if abs(start - positions[segment]) > 3.0e-14:
                raise AssertionError(f"A405 basis {column} path has a gap")
            direction = waypoints[segment + 1] - waypoints[segment]
            direction /= abs(direction)
            if abs(end - start - width * direction) > 3.0e-14:
                raise AssertionError(f"A405 basis {column} step leaves its chord")
            if int(step["augmented_state_dimension"]) != 13:
                raise AssertionError(f"A405 basis {column} lost its affine frame")
            if not step["homogeneous_thimble_source_terms_omitted_exactly"]:
                raise AssertionError(f"A405 basis {column} used an affine source")
            positions[segment] = end
        for segment, position in enumerate(positions):
            if abs(position - waypoints[segment + 1]) > 3.0e-14:
                raise AssertionError(f"A405 basis {column} misses chord {segment}")

    operators = packet["operators_at_77_entries"]
    if len(operators) != 77:
        raise AssertionError("A405 operator entry count changed")
    maximum = 0.0
    minimum_period_determinant_lower = math.inf
    for index, row in enumerate(operators):
        if int(row["entry_index_zero_based"]) != index:
            raise AssertionError("A405 operators are reordered")
        period = row["period_transport_5_by_5"]
        residue = row["integrated_residue_operator_8_by_5"]
        if len(period) != 5 or any(len(values) != 5 for values in period):
            raise AssertionError("A405 period operator dimensions changed")
        if len(residue) != 8 or any(len(values) != 5 for values in residue):
            raise AssertionError("A405 residue operator dimensions changed")
        period_interval = acb_mat(
            [[interval_entry(value) for value in values] for values in period]
        )
        determinant_lower = float(abs(period_interval.det()).lower())
        if not determinant_lower > 0.0:
            raise AssertionError(f"A405 period operator {index} is not interval-invertible")
        minimum_period_determinant_lower = min(
            minimum_period_determinant_lower, determinant_lower
        )
        for entry in [value for values in [*period, *residue] for value in values]:
            radius = float(entry["component_radius_upper"])
            if not math.isfinite(radius) or radius < 0:
                raise AssertionError("A405 operator radius is invalid")
            maximum = max(maximum, radius)
    if not math.isclose(
        maximum,
        float(packet["summary"]["maximum_operator_component_radius_upper"]),
        rel_tol=2.0e-14,
        abs_tol=0.0,
    ):
        raise AssertionError("A405 maximum radius does not replay")
    scope = packet["strict_scope"]
    if not scope["full_junction_period_and_residue_operator_closed"]:
        raise AssertionError("A405 operator closure flag is false")
    if scope["outer_thimble_transports_to_entries_closed"] or scope["covariant_zero_proved"]:
        raise AssertionError("A405 overclaims the remaining transport")
    print(
        "PASS: A405 independently verifies five complete homogeneous sweeps and "
        "all 77 common-frame 5x5 plus 8x5 operators; minimum determinant lower "
        f"{minimum_period_determinant_lower:.6g}"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
