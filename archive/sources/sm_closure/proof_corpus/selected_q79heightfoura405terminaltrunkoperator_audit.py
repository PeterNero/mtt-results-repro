from __future__ import annotations

import hashlib
import json
import math
from pathlib import Path

from flint import acb, acb_mat, arb


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
A405 = VALIDATED / "n3.junction_operator_sweep.a405.json"
RUN_DIRECTORY = VALIDATED / "jop"
PACKET = RUN_DIRECTORY / "trunk.a411.json"


def load(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def encoded_entry(snapshot: dict, row: int) -> dict:
    value = snapshot["center"][row]
    ball = acb(arb(value["real"]), arb(value["imaginary"]))
    center = complex(float(ball.real.mid()), float(ball.imag.mid()))
    return {
        "center": {
            "real": format(center.real, ".17g"),
            "imaginary": format(center.imag, ".17g"),
        },
        "component_radius_upper": float(snapshot["component_radius_uppers"][row]),
    }


def interval_entry(value: dict) -> acb:
    center = complex(
        float(value["center"]["real"]), float(value["center"]["imaginary"])
    )
    radius = float(value["component_radius_upper"])
    serialization = max(math.ulp(center.real), math.ulp(center.imag), 1.0e-300)
    outward = math.nextafter(radius + serialization, math.inf)
    return acb(
        arb(format(center.real, ".17g"), format(outward, ".17g")),
        arb(format(center.imag, ".17g"), format(outward, ".17g")),
    )


def contains_identity(matrix: acb_mat) -> bool:
    return all(
        matrix[row, column].contains(acb(1 if row == column else 0))
        for row in range(matrix.nrows())
        for column in range(matrix.ncols())
    )


def main() -> int:
    packet = load(PACKET)
    manifest = load(A404)
    sweep = load(A405)
    if packet.get("artifact") != "A411":
        raise AssertionError("A411 artifact changed")
    if packet["authority"]["A404_manifest"]["sha256"] != sha256(A404):
        raise AssertionError("A411 A404 authority is stale")
    if packet["authority"]["A405_operator_sweep"]["sha256"] != sha256(A405):
        raise AssertionError("A411 A405 authority is stale")
    if sweep["authority"]["A404_manifest"]["sha256"] != sha256(A404):
        raise AssertionError("A405 no longer binds A404")

    snapshots = []
    for column in range(5):
        path = RUN_DIRECTORY / f"basis_{column}.a405.snapshots.json"
        if packet["authority"][f"basis_{column}_snapshots"]["sha256"] != sha256(path):
            raise AssertionError(f"A411 basis {column} authority is stale")
        terminal = load(path)["snapshots"][-1]
        if terminal["label"] != "terminal_base" or int(terminal["segment_index"]) != 77:
            raise AssertionError(f"A411 basis {column} terminal changed")
        snapshots.append(terminal)

    expected_period = [
        [encoded_entry(snapshots[column], row) for column in range(5)]
        for row in range(5)
    ]
    expected_residue = [
        [encoded_entry(snapshots[column], 5 + row) for column in range(5)]
        for row in range(8)
    ]
    if packet["period_transport_5_by_5"] != expected_period:
        raise AssertionError("A411 period operator does not reconstruct")
    if packet["integrated_residue_operator_8_by_5"] != expected_residue:
        raise AssertionError("A411 residue operator does not reconstruct")
    if packet["terminal_base"] != manifest["polygon_sweep"]["terminal_base"]:
        raise AssertionError("A411 terminal base changed")

    matrix = acb_mat([[interval_entry(value) for value in row] for row in expected_period])
    determinant_lower = float(abs(matrix.det()).lower())
    inverse = matrix.inv()
    if determinant_lower <= 0.0:
        raise AssertionError("A411 period operator is not interval-invertible")
    if not contains_identity(matrix * inverse) or not contains_identity(inverse * matrix):
        raise AssertionError("A411 inverse products miss the identity")
    maximum = max(
        float(value["component_radius_upper"])
        for rows in (expected_period, expected_residue)
        for row in rows
        for value in row
    )
    summary = packet["summary"]
    if not math.isclose(
        determinant_lower,
        float(summary["period_determinant_absolute_lower"]),
        rel_tol=2.0e-14,
    ):
        raise AssertionError("A411 determinant lower bound does not replay")
    if not math.isclose(
        maximum,
        float(summary["maximum_operator_component_radius_upper"]),
        rel_tol=2.0e-14,
    ):
        raise AssertionError("A411 maximum radius does not replay")
    scope = packet["strict_scope"]
    if not scope["common_hub_to_canonical_base_operator_closed"]:
        raise AssertionError("A411 terminal operator closure flag is false")
    if scope["outer_thimble_states_consumed"] or scope["covariant_zero_proved"]:
        raise AssertionError("A411 overclaims its scope")
    print(
        "PASS: A411 independently reconstructs the terminal 5x5 plus 8x5 trunk "
        f"operator; determinant lower {determinant_lower:.6g}"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
