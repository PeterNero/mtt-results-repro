from __future__ import annotations

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
PACKET = VALIDATED / "n3.junction_operator_sweep.a404.json"
A403 = VALIDATED / "n3.common_junction_edge_ledger.a403.json"


def load(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def complex_value(value: dict[str, str]) -> complex:
    return complex(float(value["real"]), float(value["imaginary"]))


def main() -> int:
    packet = load(PACKET)
    ledger = load(A403)
    if packet["artifact"] != "A404" or not packet["theorem"]["proved"]:
        raise AssertionError("A404 theorem packet is not closed")
    if packet["authority"]["A403_common_junction_edge_ledger"]["sha256"] != sha256(A403):
        raise AssertionError("A404 A403 authority is stale")
    if packet["operational_disk"]["exact_radius"] != "1/10":
        raise AssertionError("A404 operational radius changed")
    minimum = float(
        ledger["root_free_junction_disk"][
            "minimum_critical_value_torus_distance_lower"
        ]
    )
    expected_clearance = math.nextafter(minimum - 0.1, -math.inf)
    if not math.isclose(
        float(packet["operational_disk"]["critical_value_clearance_lower"]),
        expected_clearance,
        rel_tol=2.0e-15,
        abs_tol=0.0,
    ):
        raise AssertionError("A404 operational clearance does not replay")

    entries = packet["ordered_entry_rows"]
    thimbles = [row for row in entries if row["kind"] == "selected_thimble_entry"]
    handles = [row for row in entries if row["kind"] == "selected_A_handle_entry"]
    expected_coefficients = {
        int(row["distinguished_index"]): int(row["signed_chain_coefficient"])
        for row in ledger["oriented_edge_ledger"]["selected_thimble_rows"]
    }
    actual_coefficients = {
        int(row["distinguished_index"]): int(row["signed_chain_coefficient"])
        for row in thimbles
    }
    if actual_coefficients != expected_coefficients or len(thimbles) != 76 or len(handles) != 1:
        raise AssertionError("A404 entry inventory does not replay A403")
    angles = [float(row["angle_radians"]) for row in entries]
    if angles != sorted(angles):
        raise AssertionError("A404 entries are not angularly ordered")
    waypoints = [complex_value(value) for value in packet["polygon_sweep"]["waypoints"]]
    if (
        len(waypoints) != len(entries) + 2
        or abs(waypoints[0] - 0.1) > 1.0e-15
        or abs(waypoints[-1]) > 1.0e-15
    ):
        raise AssertionError("A404 polygon endpoints changed")
    if max(abs(value) for value in waypoints) > 0.1 * (1 + 1.0e-14):
        raise AssertionError("A404 polygon left the operational disk")
    lengths = [abs(right - left) for left, right in zip(waypoints, waypoints[1:])]
    if not math.isclose(
        max(lengths),
        float(packet["polygon_sweep"]["maximum_chord_length"]),
        rel_tol=2.0e-15,
        abs_tol=0.0,
    ):
        raise AssertionError("A404 maximum chord does not replay")
    if len(packet["basis_sources"]) != 5:
        raise AssertionError("A404 lost an exact basis source")
    for column, source_row in enumerate(packet["basis_sources"]):
        path = ROOT / source_row["path"]
        if int(source_row["basis_column_zero_based"]) != column or sha256(path) != source_row["sha256"]:
            raise AssertionError(f"A404 basis source {column} is stale")
        source = load(path)
        if int(source["basis_column_zero_based"]) != column:
            raise AssertionError(f"A404 basis source {column} is mislabeled")
    scope = packet["strict_scope"]
    if not scope["finite_operator_sweep_geometry_selected"]:
        raise AssertionError("A404 finite sweep selection flag is false")
    if scope["operator_sweep_executed"] or scope["covariant_zero_proved"]:
        raise AssertionError("A404 overclaims numerical execution")
    print(
        "PASS: A404 independently replays the finite 77-entry polygon and all "
        "five exact homogeneous basis sources inside the root-free subdisk"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
