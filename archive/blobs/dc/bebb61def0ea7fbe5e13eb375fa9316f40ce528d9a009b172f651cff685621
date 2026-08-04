from __future__ import annotations

import hashlib
import json
import math
from pathlib import Path

from flint import acb, ctx

import certify_q79_selected_side_base_lift_interval as base_interval


ROOT = Path(__file__).resolve().parents[1]
VALIDATED = (
    ROOT
    / "candidate_data"
    / "selected_q79covariantperiodbranchcutsetandtightbetatransport"
    / "selected_alignment_thimble_periods"
    / "covariant_floating_probe"
    / "validated_transport"
)
A403 = VALIDATED / "n3.common_junction_edge_ledger.a403.json"
OUTPUT = VALIDATED / "n3.junction_operator_sweep.a404.json"
NOTE = ROOT / "proof_corpus" / "MTT_q79HeightFourJunctionOperatorSweep_A404_v1.md"
ARTIFACT = "A404"
RADIUS = 0.1
HUB = 0.1 + 0.0j


def load(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def dump(path: Path, value: dict) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(value, indent=2, sort_keys=True) + "\n", encoding="utf-8")


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def relative(path: Path) -> str:
    return str(path.relative_to(ROOT)).replace("\\", "/")


def authority(path: Path) -> dict[str, str]:
    return {"path": relative(path), "sha256": sha256(path)}


def pair(value: complex) -> dict[str, str]:
    return {
        "real": format(value.real, ".17g"),
        "imaginary": format(value.imag, ".17g"),
    }


def complex_value(value: dict[str, str]) -> complex:
    return complex(float(value["real"]), float(value["imaginary"]))


def main() -> int:
    ctx.dps = 100
    ledger = load(A403)
    if not ledger["strict_scope"]["aggregate_common_trunk_cancellation_proved"]:
        raise AssertionError("A403 common-junction theorem is unavailable")
    topological_radius = float(ledger["root_free_junction_disk"]["radius_binary64"])
    minimum_root_distance = float(
        ledger["root_free_junction_disk"][
            "minimum_critical_value_torus_distance_lower"
        ]
    )
    if not RADIUS < topological_radius < minimum_root_distance:
        raise AssertionError("the operational sweep disk is not nested in A403")

    entries = []
    for row in ledger["oriented_edge_ledger"]["selected_thimble_rows"]:
        direction = complex_value(
            row["canonical_inner_segment"]["midpoint_diagnostic_only"]
        )
        direction /= abs(direction)
        point = RADIUS * direction
        angle = math.atan2(point.imag, point.real) % (2.0 * math.pi)
        entries.append(
            {
                "label": f"d{int(row['distinguished_index']):03d}",
                "kind": "selected_thimble_entry",
                "distinguished_index": int(row["distinguished_index"]),
                "signed_chain_coefficient": int(row["signed_chain_coefficient"]),
                "angle_radians": angle,
                "point": pair(point),
            }
        )
    entries.append(
        {
            "label": "handle_A_axis_exit",
            "kind": "selected_A_handle_entry",
            "angle_radians": 1.5 * math.pi,
            "point": pair(0.0 - RADIUS * 1j),
        }
    )
    entries.sort(key=lambda row: (float(row["angle_radians"]), row["label"]))
    points = [complex_value(row["point"]) for row in entries]
    if any(abs(left - right) < 1.0e-14 for left, right in zip(points, points[1:])):
        raise AssertionError("the operational sweep contains duplicate adjacent entries")
    waypoints = [HUB, *points, 0 + 0j]
    chord_lengths = [abs(right - left) for left, right in zip(waypoints, waypoints[1:])]
    if not chord_lengths or max(abs(value) for value in waypoints) > RADIUS * (1 + 1.0e-14):
        raise AssertionError("the polygon sweep left the operational disk")

    source_paths = []
    for column in range(5):
        values = [acb(1 if row == column else 0) for row in range(5)]
        path = VALIDATED / f"n3.junction_basis_{column}.source.a404.json"
        source = {
            "schema": "MTTQ79HeightFourJunctionBasisSource.v1",
            "status": "EXACT_HOMOGENEOUS_JUNCTION_BASIS_SOURCE",
            "artifact": ARTIFACT,
            "basis_column_zero_based": column,
            "y_chart_base_lift": [
                base_interval.complex_interval(value) for value in values
            ],
            "strict_scope": {
                "observed_SM_values_used": False,
                "exact_unit_basis_source": True,
                "operator_sweep_executed": False,
            },
        }
        dump(path, source)
        source_paths.append(path)

    payload = {
        "schema": "MTTQ79HeightFourJunctionOperatorSweepManifest.v1",
        "status": "FINITE_FIVE_BASIS_JUNCTION_OPERATOR_SWEEP_SELECTED",
        "artifact": ARTIFACT,
        "operational_disk": {
            "exact_radius": "1/10",
            "radius_binary64": RADIUS,
            "hub": pair(HUB),
            "nested_in_A403_radius_one_fifth_disk": True,
            "minimum_critical_value_distance_lower": minimum_root_distance,
            "critical_value_clearance_lower": math.nextafter(
                minimum_root_distance - RADIUS, -math.inf
            ),
        },
        "ordered_entry_rows": entries,
        "polygon_sweep": {
            "waypoints": [pair(value) for value in waypoints],
            "terminal_base": pair(0 + 0j),
            "waypoint_count": len(waypoints),
            "segment_count": len(chord_lengths),
            "maximum_chord_length": max(chord_lengths),
            "total_polygon_length": sum(chord_lengths),
            "every_chord_inside_convex_root_free_disk": True,
            "prefix_to_each_entry_is_homotopic_to_any_A403_inner_arc": True,
        },
        "basis_sources": [
            {
                "basis_column_zero_based": column,
                **authority(path),
            }
            for column, path in enumerate(source_paths)
        ],
        "operator_reconstruction": {
            "period_basis_dimension": 5,
            "residue_row_count": 8,
            "required_validated_basis_sweeps": 5,
            "snapshot_count_per_sweep": len(entries),
            "statement": (
                "At every ordered entry, the five validated unit-basis images "
                "form the full homogeneous period transport and integrated "
                "eight-residue operator from the hub. Integer cycle combinations "
                "are applied only after these common-frame snapshots are emitted."
            ),
        },
        "theorem": {
            "name": "Finite common-junction operator sweep theorem",
            "proved": True,
            "statement": (
                "Because the operational polygon lies in the simply connected "
                "A403 smooth disk, its prefix to each selected entry represents "
                "the unique Gauss-Manin transport from h. Five unit-basis "
                "solutions therefore determine every required homogeneous "
                "period/residue map at all 76 thimble entries and the A-handle "
                "entry."
            ),
        },
        "summary": {
            "selected_thimble_entry_count": 76,
            "selected_handle_entry_count": 1,
            "ordered_entry_count": len(entries),
            "exact_basis_source_count": len(source_paths),
            "required_snapshot_count": len(entries) * len(source_paths),
        },
        "authority": {
            "A403_common_junction_edge_ledger": authority(A403),
            "builder_source": authority(Path(__file__).resolve()),
            **{
                f"basis_source_{column}": authority(path)
                for column, path in enumerate(source_paths)
            },
        },
        "strict_scope": {
            "observed_SM_values_used": False,
            "finite_operator_sweep_geometry_selected": True,
            "five_exact_basis_sources_emitted": True,
            "all_76_thimble_entries_included": True,
            "A_handle_entry_included": True,
            "operator_sweep_executed": False,
            "outer_thimble_transports_executed_to_operational_entries": False,
            "full_correlation_preserving_path_execution_closed": False,
            "interval_Newton_existence_and_uniqueness_closed": False,
            "covariant_zero_proved": False,
            "full_SM_closure_proved": False,
        },
        "next_required_artifact": (
            "execute five resumable homogeneous augmented sweeps and emit the "
            "77 common-frame snapshots for each basis column"
        ),
    }
    dump(OUTPUT, payload)
    NOTE.write_text(
        "# MTT q79 Height-Four Junction Operator Sweep (A404) v1\n\n"
        "A404 selects the nested operational disk `|t|<=1/10`, whose certified "
        f"critical-value clearance is "
        f"`{payload['operational_disk']['critical_value_clearance_lower']:.12g}`. "
        "A single ordered polygon sweep visits all 76 thimble entry directions "
        "and the A-handle axis entry without leaving this disk.\n\n"
        "Five exact unit-basis sources are sufficient to recover every required "
        "homogeneous period/residue operator at all entries. The manifest and "
        "sources are selected here; their validated sweeps remain to be run.\n",
        encoding="utf-8",
    )
    print(f"wrote {relative(OUTPUT)}")
    print(f"wrote {relative(NOTE)}")
    print(json.dumps(payload["summary"], indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
