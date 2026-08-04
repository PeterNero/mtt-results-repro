from __future__ import annotations

import argparse
import hashlib
import json
import math
from pathlib import Path

from flint import acb, acb_mat, arb, ctx

import certify_q79_height4_d087_full_residue_main_interval as n3_engine
import certify_q79_selected_side_beta_defect_transport as validated
import q79_fast_taylor_runtime as fast
import run_q79_augmented_beta_transport as augmented


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
# Keep atomic checkpoint names below the legacy Windows MAX_PATH boundary.
RUN_DIRECTORY = DIRECTORY / "jop"
OUTPUT = DIRECTORY / "n3.junction_operator_sweep.a405.json"
NOTE = ROOT / "proof_corpus" / "MTT_q79HeightFourJunctionOperatorSweeps_A405_v1.md"
FAST_AUDIT = ROOT / "proof_corpus" / "selected_q79fasttaylorruntime_equivalence_audit.py"
ARTIFACT = "A405"


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


def complex_value(value: dict[str, str]) -> complex:
    return complex(float(value["real"]), float(value["imaginary"]))


def paths(column: int) -> dict[str, Path]:
    return {
        "checkpoint": RUN_DIRECTORY / f"basis_{column}.a405.ckpt.json",
        "snapshots": RUN_DIRECTORY / f"basis_{column}.a405.snapshots.json",
        "result": RUN_DIRECTORY / f"basis_{column}.a405.json",
    }


def source_path(manifest: dict, column: int) -> Path:
    row = manifest["basis_sources"][column]
    if int(row["basis_column_zero_based"]) != column:
        raise AssertionError("A404 basis sources are reordered")
    path = ROOT / row["path"]
    if sha256(path) != row["sha256"]:
        raise AssertionError(f"A404 basis source {column} is stale")
    return path


def initial_state(source: Path) -> tuple[list[acb], validated.LiftErrorFrame]:
    packet = load(source)
    balls = [
        validated.interval_from_bounds(value) for value in packet["y_chart_base_lift"]
    ]
    center = [validated.SelectedQ79IntervalSystem.midpoint_acb(value) for value in balls]
    center.extend(acb(0) for _ in range(8))
    fundamental = acb_mat(5, 5)
    for index in range(5):
        fundamental[index, index] = acb(1)
    frame = validated.LiftErrorFrame(
        fundamental=fundamental,
        coordinate_radii=[value.rad().upper() for value in balls],
    )
    return center, frame


def install_augmented_homogeneous_engine():
    originals = {
        "base_lift": validated.BASE_LIFT,
        "build": validated.build_taylor_system,
        "step": validated.validated_flow_step,
        "generator": validated.LiftErrorFrame.physical_generator_matrix,
        "radius": validated.LiftErrorFrame.physical_radius,
    }
    validated.build_taylor_system = n3_engine.build_thimble_taylor_system
    validated.validated_flow_step = augmented.augmented_validated_flow_step
    validated.LiftErrorFrame.physical_generator_matrix = augmented.dynamic_generator_matrix
    validated.LiftErrorFrame.physical_radius = augmented.dynamic_physical_radius
    return originals


def restore_engine(originals: dict) -> None:
    validated.BASE_LIFT = originals["base_lift"]
    validated.build_taylor_system = originals["build"]
    validated.validated_flow_step = originals["step"]
    validated.LiftErrorFrame.physical_generator_matrix = originals["generator"]
    validated.LiftErrorFrame.physical_radius = originals["radius"]


def smoke(
    system: validated.SelectedQ79IntervalSystem,
    manifest: dict,
    column: int,
    order: int,
) -> dict:
    source = source_path(manifest, column)
    center, frame = initial_state(source)
    waypoints = [complex_value(value) for value in manifest["polygon_sweep"]["waypoints"]]
    displacement = waypoints[1] - waypoints[0]
    direction = displacement / abs(displacement)
    step = min(1.0e-4, abs(displacement))
    originals = install_augmented_homogeneous_engine()
    try:
        endpoint, output_frame, output_radius, diagnostics = (
            augmented.augmented_validated_flow_step(
                system,
                waypoints[0],
                direction,
                step,
                center,
                frame,
                arb(0),
                order=order,
            )
        )
    finally:
        restore_engine(originals)
    if len(endpoint) != 13 or output_frame.fundamental.nrows() != 13:
        raise AssertionError("A405 smoke step lost the 13-state frame")
    return {
        "basis_column_zero_based": column,
        "step": step,
        "order": order,
        "output_residue_radius_upper": validated.upper(output_radius),
        "output_state_radius_upper": validated.upper(
            augmented.dynamic_physical_radius(output_frame)
        ),
        "linear_defect_bound": diagnostics["linear_defect_bound"],
        "affine_defect_bound": diagnostics["affine_defect_bound"],
        "homogeneous_source_terms_omitted_exactly": diagnostics[
            "homogeneous_thimble_source_terms_omitted_exactly"
        ],
        "all_returned_bounds_finite": diagnostics["all_returned_bounds_finite"],
    }


def snapshot_from_checkpoint(
    checkpoint: dict,
    *,
    segment: int,
    label: str,
) -> dict:
    frame = validated.LiftErrorFrame(
        fundamental=validated.decoded_matrix(checkpoint["lift_fundamental"]),
        coordinate_radii=[arb(value) for value in checkpoint["coordinate_radii"]],
    )
    radii = augmented.component_radii(frame)
    return {
        "segment_index": segment,
        "waypoint_index": segment + 1,
        "label": label,
        "center": checkpoint["center"],
        "component_radius_uppers": [validated.upper(value) for value in radii],
        "lift_fundamental": checkpoint["lift_fundamental"],
        "coordinate_radii": checkpoint["coordinate_radii"],
        "beta_radius": checkpoint["beta_radius"],
    }


def execute_basis(
    system: validated.SelectedQ79IntervalSystem,
    manifest: dict,
    column: int,
    arguments: argparse.Namespace,
    smoke_packet: dict,
) -> dict:
    source = source_path(manifest, column)
    selected_paths = paths(column)
    RUN_DIRECTORY.mkdir(parents=True, exist_ok=True)
    checkpoint_path = selected_paths["checkpoint"]
    snapshot_path = selected_paths["snapshots"]
    result_path = selected_paths["result"]
    manifest_hash = sha256(MANIFEST)
    source_hash = sha256(source)
    builder_hash = sha256(Path(__file__).resolve())
    if result_path.exists() and not arguments.restart:
        result = load(result_path)
        authority_rows = result.get("authority", {})
        if (
            authority_rows.get("A404_manifest", {}).get("sha256") == manifest_hash
            and authority_rows.get("basis_source", {}).get("sha256") == source_hash
            and authority_rows.get("builder_source", {}).get("sha256") == builder_hash
        ):
            print(f"basis {column} already complete with current authority", flush=True)
            return result
    if arguments.restart:
        for path in selected_paths.values():
            if path.exists():
                path.unlink()
    if checkpoint_path.exists():
        checkpoint = load(checkpoint_path)
        for key, expected in {
            "A405_manifest_sha256": manifest_hash,
            "A405_source_sha256": source_hash,
            "A405_builder_sha256": builder_hash,
        }.items():
            if checkpoint.get(key) != expected:
                raise ValueError(f"A405 basis {column} checkpoint is stale: {key}")

    waypoints = [complex_value(value) for value in manifest["polygon_sweep"]["waypoints"]]
    entry_labels = [row["label"] for row in manifest["ordered_entry_rows"]]
    segment_labels = [*entry_labels, "terminal_base"]
    if len(segment_labels) != len(waypoints) - 1:
        raise AssertionError("A404 segment labels do not match its path")
    snapshots = {}
    if snapshot_path.exists() and not arguments.restart:
        prior = load(snapshot_path)
        if (
            prior.get("A404_manifest_sha256") != manifest_hash
            or prior.get("basis_source_sha256") != source_hash
        ):
            raise ValueError(f"A405 basis {column} snapshot authority is stale")
        snapshots = {
            int(row["segment_index"]): row for row in prior.get("snapshots", [])
        }

    source_fingerprint = source_hash[:16]
    path_name = (
        f"A405 n3 homogeneous junction basis={column} dps={arguments.dps} "
        f"source={source_fingerprint} builder={builder_hash[:16]}"
    )
    original_atomic_dump = validated.atomic_dump

    def stamped_dump(path: Path, value: dict) -> None:
        path.parent.mkdir(parents=True, exist_ok=True)
        payload = dict(value)
        if path == checkpoint_path:
            payload.update(
                {
                    "A405_manifest_sha256": manifest_hash,
                    "A405_source_sha256": source_hash,
                    "A405_builder_sha256": builder_hash,
                    "A405_basis_column_zero_based": column,
                }
            )
        original_atomic_dump(path, payload)
        if path != checkpoint_path:
            return
        segment = int(payload["segment_index"])
        position = float(payload["segment_position"])
        length = abs(waypoints[segment + 1] - waypoints[segment])
        if not math.isclose(position, length, rel_tol=2.0e-13, abs_tol=2.0e-15):
            return
        snapshots[segment] = snapshot_from_checkpoint(
            payload,
            segment=segment,
            label=segment_labels[segment],
        )
        original_atomic_dump(
            snapshot_path,
            {
                "schema": "MTTQ79HeightFourJunctionBasisSnapshots.v1",
                "artifact": ARTIFACT,
                "basis_column_zero_based": column,
                "A404_manifest_sha256": manifest_hash,
                "basis_source_sha256": source_hash,
                "builder_source_sha256": builder_hash,
                "snapshots": [snapshots[index] for index in sorted(snapshots)],
            },
        )

    originals = install_augmented_homogeneous_engine()
    validated.BASE_LIFT = source
    validated.atomic_dump = stamped_dump
    fast.install()
    try:
        transport = validated.execute_validated_path(
            system,
            waypoints=waypoints,
            path_name=path_name,
            order=arguments.order,
            initial_step=arguments.initial_step,
            minimum_step=arguments.minimum_step,
            maximum_steps=arguments.maximum_steps,
            checkpoint_path=checkpoint_path,
            resume=checkpoint_path.exists(),
        )
    finally:
        fast.uninstall()
        validated.atomic_dump = original_atomic_dump
        restore_engine(originals)
    if set(snapshots) != set(range(len(segment_labels))):
        raise AssertionError(f"A405 basis {column} did not emit every segment snapshot")
    result = {
        "schema": "MTTQ79HeightFourJunctionBasisSweep.v1",
        "status": "ONE_EXACT_HOMOGENEOUS_JUNCTION_BASIS_SWEEP_EXECUTED",
        "artifact": ARTIFACT,
        "basis_column_zero_based": column,
        "smoke_test": smoke_packet,
        "validated_transport": transport,
        "snapshot_count": len(snapshots),
        "entry_snapshot_count": len(entry_labels),
        "authority": {
            "A404_manifest": authority(MANIFEST),
            "basis_source": authority(source),
            "completed_checkpoint": authority(checkpoint_path),
            "snapshot_packet": authority(snapshot_path),
            "n3_exact_fibration": authority(n3_engine.FIBRATION),
            "homogeneous_taylor_system": authority(Path(n3_engine.__file__).resolve()),
            "augmented_affine_transport": authority(Path(augmented.__file__).resolve()),
            "C_backed_Taylor_runtime": authority(Path(fast.__file__).resolve()),
            "C_backed_Taylor_equivalence_audit": authority(FAST_AUDIT),
            "builder_source": authority(Path(__file__).resolve()),
        },
        "strict_scope": {
            "observed_SM_values_used": False,
            "exact_homogeneous_basis_source_consumed": True,
            "all_77_entry_snapshots_emitted": len(entry_labels) == 77,
            "terminal_base_snapshot_emitted": True,
            "single_basis_sweep_executed": True,
            "all_five_basis_sweeps_executed": False,
            "full_junction_operator_closed": False,
            "covariant_zero_proved": False,
            "full_SM_closure_proved": False,
        },
    }
    dump(result_path, result)
    print(f"wrote {relative(result_path)}", flush=True)
    return result


def encoded_entry(value: acb, radius: float) -> dict:
    return {
        "center": {
            "real": format(float(value.real.mid()), ".17g"),
            "imaginary": format(float(value.imag.mid()), ".17g"),
        },
        "component_radius_upper": radius,
    }


def aggregate(manifest: dict, results: list[dict]) -> dict:
    entry_rows = manifest["ordered_entry_rows"]
    snapshots_by_column = []
    for column in range(5):
        packet = load(paths(column)["snapshots"])
        snapshots = packet["snapshots"]
        if len(snapshots) != len(entry_rows) + 1:
            raise AssertionError(f"A405 basis {column} snapshot count changed")
        snapshots_by_column.append(snapshots)
    operators = []
    maximum_radius = 0.0
    for entry_index, entry in enumerate(entry_rows):
        period_rows = []
        residue_rows = []
        for row in range(5):
            period_row = []
            for column in range(5):
                snapshot = snapshots_by_column[column][entry_index]
                value = validated.decoded_acb(snapshot["center"][row])
                radius = float(snapshot["component_radius_uppers"][row])
                maximum_radius = max(maximum_radius, radius)
                period_row.append(encoded_entry(value, radius))
            period_rows.append(period_row)
        for row in range(8):
            residue_row = []
            for column in range(5):
                snapshot = snapshots_by_column[column][entry_index]
                value = validated.decoded_acb(snapshot["center"][5 + row])
                radius = float(snapshot["component_radius_uppers"][5 + row])
                maximum_radius = max(maximum_radius, radius)
                residue_row.append(encoded_entry(value, radius))
            residue_rows.append(residue_row)
        operators.append(
            {
                "entry_index_zero_based": entry_index,
                "entry": entry,
                "period_transport_5_by_5": period_rows,
                "integrated_residue_operator_8_by_5": residue_rows,
            }
        )
    payload = {
        "schema": "MTTQ79HeightFourJunctionOperatorSweeps.v1",
        "status": "ALL_FIVE_COMMON_FRAME_JUNCTION_OPERATOR_SWEEPS_EXECUTED",
        "artifact": ARTIFACT,
        "operators_at_77_entries": operators,
        "summary": {
            "completed_basis_sweeps": len(results),
            "entry_operator_count": len(operators),
            "period_operator_entries": len(operators) * 25,
            "integrated_residue_operator_entries": len(operators) * 40,
            "maximum_operator_component_radius_upper": maximum_radius,
        },
        "authority": {
            "A404_manifest": authority(MANIFEST),
            **{
                f"basis_{column}_result": authority(paths(column)["result"])
                for column in range(5)
            },
            **{
                f"basis_{column}_snapshots": authority(paths(column)["snapshots"])
                for column in range(5)
            },
            "builder_source": authority(Path(__file__).resolve()),
        },
        "strict_scope": {
            "observed_SM_values_used": False,
            "all_five_basis_sweeps_executed": True,
            "all_385_entry_basis_snapshots_closed": True,
            "full_junction_period_and_residue_operator_closed": True,
            "outer_thimble_transports_to_entries_closed": False,
            "integer_chain_combination_at_hub_closed": False,
            "full_correlation_preserving_path_execution_closed": False,
            "interval_Newton_existence_and_uniqueness_closed": False,
            "covariant_zero_proved": False,
            "full_SM_closure_proved": False,
        },
        "next_required_artifact": (
            "execute the 76 outer thimble legs to their A404 entries and apply "
            "these common-frame operators before the A403 zero-trunk reduction"
        ),
    }
    dump(OUTPUT, payload)
    NOTE.write_text(
        "# MTT q79 Height-Four Junction Operator Sweeps (A405) v1\n\n"
        "A405 executes the five exact homogeneous basis sources along the A404 "
        "common polygon and emits the full 5x5 period plus 8x5 integrated-residue "
        "operator at all 77 selected entries.\n\n"
        f"The maximum operator component radius is `{maximum_radius:.12g}`. "
        "The 76 outer thimble legs and their integer combination at the hub "
        "remain open, so this packet does not prove the covariant zero.\n",
        encoding="utf-8",
    )
    print(f"wrote {relative(OUTPUT)}", flush=True)
    return payload


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--dps", type=int, default=110)
    parser.add_argument("--order", type=int, default=40)
    parser.add_argument("--initial-step", type=float, default=0.004)
    parser.add_argument("--minimum-step", type=float, default=1.0e-12)
    parser.add_argument("--maximum-steps", type=int, default=100000)
    parser.add_argument("--basis-column", type=int, action="append")
    parser.add_argument("--restart", action="store_true")
    parser.add_argument("--smoke-only", action="store_true")
    arguments = parser.parse_args()
    if arguments.dps < 80 or arguments.order < 24:
        raise ValueError("A405 requires at least 80 digits and Taylor order 24")
    columns = arguments.basis_column or list(range(5))
    if any(column not in range(5) for column in columns) or len(set(columns)) != len(columns):
        raise ValueError("A405 basis columns must be distinct values from 0 through 4")
    ctx.dps = arguments.dps
    manifest = load(MANIFEST)
    if not manifest["strict_scope"]["finite_operator_sweep_geometry_selected"]:
        raise AssertionError("A404 sweep geometry is unavailable")
    system = n3_engine.exact_target_system(arguments.dps)
    smoke_packets = {
        column: smoke(system, manifest, column, min(arguments.order, 30))
        for column in columns
    }
    if arguments.smoke_only:
        print(json.dumps(list(smoke_packets.values()), indent=2))
        return 0
    RUN_DIRECTORY.mkdir(parents=True, exist_ok=True)
    results = [
        execute_basis(system, manifest, column, arguments, smoke_packets[column])
        for column in columns
    ]
    if set(columns) == set(range(5)):
        payload = aggregate(manifest, results)
        print(json.dumps(payload["summary"], indent=2), flush=True)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
