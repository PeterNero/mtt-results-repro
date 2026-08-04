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
OUTPUT = RUN_DIRECTORY / "trunk.a411.json"
NOTE = ROOT / "proof_corpus" / "MTT_q79HeightFourA405TerminalTrunkOperator_A411_v1.md"


def load(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def authority(path: Path) -> dict[str, str]:
    return {"path": str(path.relative_to(ROOT)).replace("\\", "/"), "sha256": sha256(path)}


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
    for row in range(matrix.nrows()):
        for column in range(matrix.ncols()):
            expected = acb(1 if row == column else 0)
            if not matrix[row, column].contains(expected):
                return False
    return True


def main() -> int:
    manifest = load(A404)
    sweep = load(A405)
    if manifest.get("artifact") != "A404" or sweep.get("artifact") != "A405":
        raise AssertionError("A411 requires A404 and A405")
    if not sweep["strict_scope"]["full_junction_period_and_residue_operator_closed"]:
        raise AssertionError("A411 requires the audited A405 operator sweep")
    if sweep["authority"]["A404_manifest"]["sha256"] != sha256(A404):
        raise AssertionError("A411 A404 authority is stale")

    snapshots = []
    for column in range(5):
        path = RUN_DIRECTORY / f"basis_{column}.a405.snapshots.json"
        if sweep["authority"][f"basis_{column}_snapshots"]["sha256"] != sha256(path):
            raise AssertionError(f"A411 basis {column} authority is stale")
        rows = load(path)["snapshots"]
        if len(rows) != 78:
            raise AssertionError(f"A411 basis {column} snapshot count changed")
        terminal = rows[-1]
        if (
            terminal["label"] != "terminal_base"
            or int(terminal["segment_index"]) != 77
            or int(terminal["waypoint_index"]) != 78
        ):
            raise AssertionError(f"A411 basis {column} terminal snapshot changed")
        snapshots.append(terminal)

    period = [
        [encoded_entry(snapshots[column], row) for column in range(5)]
        for row in range(5)
    ]
    residue = [
        [encoded_entry(snapshots[column], 5 + row) for column in range(5)]
        for row in range(8)
    ]
    matrix = acb_mat([[interval_entry(value) for value in row] for row in period])
    determinant_lower = float(abs(matrix.det()).lower())
    if determinant_lower <= 0.0:
        raise AssertionError("A411 terminal period operator is not interval-invertible")
    inverse = matrix.inv()
    if not contains_identity(matrix * inverse) or not contains_identity(inverse * matrix):
        raise AssertionError("A411 terminal inverse products miss the identity")
    maximum_radius = max(
        float(value["component_radius_upper"])
        for rows in (period, residue)
        for row in rows
        for value in row
    )

    payload = {
        "schema": "MTTQ79HeightFourA405TerminalTrunkOperator.v1",
        "status": "COMMON_HUB_TO_CANONICAL_BASE_TERMINAL_OPERATOR_CERTIFIED",
        "artifact": "A411",
        "terminal_base": manifest["polygon_sweep"]["terminal_base"],
        "period_transport_5_by_5": period,
        "integrated_residue_operator_8_by_5": residue,
        "summary": {
            "period_operator_entries": 25,
            "integrated_residue_operator_entries": 40,
            "maximum_operator_component_radius_upper": maximum_radius,
            "period_determinant_absolute_lower": determinant_lower,
            "both_inverse_products_contain_identity": True,
        },
        "authority": {
            "A404_manifest": authority(A404),
            "A405_operator_sweep": authority(A405),
            **{
                f"basis_{column}_snapshots": authority(
                    RUN_DIRECTORY / f"basis_{column}.a405.snapshots.json"
                )
                for column in range(5)
            },
            "builder_source": authority(Path(__file__).resolve()),
        },
        "strict_scope": {
            "observed_SM_values_used": False,
            "all_five_terminal_basis_snapshots_consumed": True,
            "common_hub_to_canonical_base_operator_closed": True,
            "terminal_period_operator_interval_invertible": True,
            "outer_thimble_states_consumed": False,
            "full_correlation_preserving_path_execution_closed": False,
            "interval_Newton_existence_and_uniqueness_closed": False,
            "covariant_zero_proved": False,
            "full_SM_closure_proved": False,
        },
        "next_required_artifact": (
            "compose A409O with the d057 A405 reverse entry map and this terminal "
            "trunk, then compare the resulting base residue with A397"
        ),
    }
    OUTPUT.parent.mkdir(parents=True, exist_ok=True)
    NOTE.parent.mkdir(parents=True, exist_ok=True)
    OUTPUT.write_text(json.dumps(payload, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    NOTE.write_text(
        "# MTT q79 Height-Four A405 Terminal Trunk Operator (A411) v1\n\n"
        "A411 extracts the terminal common-hub-to-base homogeneous operator from "
        "the five already certified A405 basis snapshots. The interval 5-by-5 "
        "period block is nonsingular and both computed inverse products contain "
        "the identity.\n\n"
        f"The determinant absolute lower bound is `{determinant_lower:.12g}` and "
        f"the maximum component radius is `{maximum_radius:.12g}`. Outer states, "
        "the hub sum, Newton inclusion, and the covariant zero remain open.\n",
        encoding="utf-8",
    )
    print(f"wrote {OUTPUT.relative_to(ROOT)}")
    print(f"wrote {NOTE.relative_to(ROOT)}")
    print(json.dumps(payload["summary"], indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
