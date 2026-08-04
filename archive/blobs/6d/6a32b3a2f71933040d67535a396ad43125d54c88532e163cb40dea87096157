from __future__ import annotations

import argparse
import hashlib
import json
import math
import time
from pathlib import Path

import numpy as np
from flint import ctx

import certify_q79_height4_target_full_residue_interval as generic
import certify_q79_height4_target_main_hessian_interval as main_hessian
import certify_q79_selected_side_beta_defect_transport as validated
import q79_fast_taylor_runtime as fast


ROOT = Path(__file__).resolve().parents[1]
VALIDATED = main_hessian.VALIDATED
A404 = VALIDATED / "n3.junction_operator_sweep.a404.json"
A413 = VALIDATED / "ol" / "all76.a413.json"
DIRECTORY = VALIDATED / "ol"
FAST_AUDIT = ROOT / "proof_corpus" / "selected_q79fasttaylorruntime_equivalence_audit.py"


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


def resolve(path: str) -> Path:
    return ROOT / Path(path)


def complex_value(value: dict[str, str]) -> complex:
    return complex(float(value["real"]), float(value["imaginary"]))


def encoded_complex(value: complex) -> dict[str, str]:
    return {"real": format(value.real, ".17g"), "imaginary": format(value.imag, ".17g")}


def paths(index: int) -> dict[str, Path]:
    stem = f"d{index:03d}.a414"
    return {
        "checkpoint": DIRECTORY / f"{stem}.ckpt.json",
        "output": DIRECTORY / f"{stem}.json",
        "note": ROOT / "proof_corpus" / f"MTT_q79D{index:03d}A413OuterLeg_A414_v1.md",
    }


def checkpoint_stamp(arguments: argparse.Namespace, source: Path, endpoint: complex) -> dict[str, object]:
    return {
        "A414_builder_sha256": sha256(Path(__file__).resolve()),
        "A414_A413_sha256": sha256(A413),
        "A414_source_sha256": sha256(source),
        "A414_A404_sha256": sha256(A404),
        "A414_fast_runtime_sha256": sha256(Path(fast.__file__).resolve()),
        "A414_fast_audit_sha256": sha256(FAST_AUDIT),
        "A414_main_dps": arguments.main_dps,
        "A414_entry": encoded_complex(endpoint),
    }


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--index", type=int, required=True)
    parser.add_argument("--main-dps", type=int, default=100)
    parser.add_argument("--order", type=int, default=32)
    parser.add_argument("--initial-step", type=float, default=1.0e-4)
    parser.add_argument("--maximum-step", type=float, default=0.003)
    parser.add_argument("--minimum-step", type=float, default=1.0e-12)
    parser.add_argument("--maximum-lift-correction", type=float, default=1.0e-10)
    parser.add_argument("--maximum-integral-radius", type=float, default=1.0e-4)
    parser.add_argument("--restart", action="store_true")
    arguments = parser.parse_args()
    if arguments.main_dps < 90 or arguments.order < 24:
        raise ValueError("A414 requires at least 90 digits and Taylor order 24")
    ctx.dps = arguments.main_dps
    generic.set_below_normal_priority()
    started = time.perf_counter()
    source_manifest = load(A413)
    junction_manifest = load(A404)
    matches = [
        row for row in source_manifest["target_rows"]
        if int(row["distinguished_index"]) == arguments.index
    ]
    if len(matches) != 1:
        raise ValueError(f"A414 index {arguments.index} is not in the A413 support")
    contract = matches[0]
    source_path = resolve(contract["authority"]["canonical_main"]["path"])
    source = load(source_path)
    if contract["authority"]["canonical_main"]["sha256"] != sha256(source_path):
        raise AssertionError("A414 A413 source authority is stale")
    entries = [
        (position, row)
        for position, row in enumerate(junction_manifest["ordered_entry_rows"])
        if row.get("kind") == "selected_thimble_entry"
        and int(row["distinguished_index"]) == arguments.index
    ]
    if len(entries) != 1:
        raise AssertionError("A414 did not find one A404 entry")
    entry_index, entry = entries[0]
    endpoint = complex_value(entry["point"])
    system, rank, selected_row = main_hessian.selected_system(arguments.index, arguments.main_dps)
    target = source["selected_target"]
    if selected_row["root_id"] != target["root_id"] or contract["root_id"] != target["root_id"]:
        raise AssertionError("A414 selected target root changed")
    if contract["line_chart"] != target["line_chart"]:
        raise AssertionError("A414 selected target chart changed")
    _node, start = main_hessian.canonical_cutoff_start(source)
    if abs(start - complex_value(contract["cutoff_start"])) > 3.0e-14:
        raise AssertionError("A414 cutoff start differs from A413")
    normalized_cross = abs(start.real * endpoint.imag - start.imag * endpoint.real) / (abs(start) * abs(endpoint))
    radial_ratio = start / endpoint
    if normalized_cross > 3.0e-14 or radial_ratio.real <= 1.0 or abs(radial_ratio.imag) > 3.0e-13:
        raise AssertionError("A414 selected segment is not the A413 radial leg")
    _hessian_seed, _frame, _output_radii, source_diagnostics = main_hessian.initial_state(
        system, source, start
    )
    initial_periods = [
        validated.decoded_acb(value)
        for value in source_diagnostics["full_precision_period_balls"]
    ]
    if len(initial_periods) != 5:
        raise AssertionError("A414 source did not emit five full-precision period balls")
    run_paths = paths(arguments.index)
    if arguments.restart and run_paths["checkpoint"].exists():
        run_paths["checkpoint"].unlink()
    stamp = checkpoint_stamp(arguments, source_path, endpoint)
    if run_paths["checkpoint"].exists():
        checkpoint = load(run_paths["checkpoint"])
        for key, expected in stamp.items():
            if checkpoint.get(key) != expected:
                raise ValueError(f"A414 checkpoint authority stale: {key}")

    original_atomic_dump = validated.atomic_dump

    def stamped_checkpoint(path: Path, value: dict) -> None:
        payload = dict(value)
        if payload.get("schema") == "MTTQ79HeightFourAllRowMainCheckpoint.v1":
            payload.update(stamp)
        original_atomic_dump(path, payload)

    DIRECTORY.mkdir(parents=True, exist_ok=True)
    validated.atomic_dump = stamped_checkpoint
    fast.install()
    try:
        execution = generic.execute_main_transport_resumable(
            system,
            initial_periods,
            index=arguments.index,
            root_id=target["root_id"],
            checkpoint_path=run_paths["checkpoint"],
            start=start,
            endpoint=endpoint,
            order=arguments.order,
            maximum_step=arguments.maximum_step,
            initial_step=min(arguments.initial_step, abs(start - endpoint)),
            minimum_step=arguments.minimum_step,
            maximum_lift_correction=arguments.maximum_lift_correction,
            maximum_integral_radius=arguments.maximum_integral_radius,
            cooling_pause_every=20,
            cooling_pause_seconds=0.0,
        )
    finally:
        fast.uninstall()
        validated.atomic_dump = original_atomic_dump

    transport_orientation = int(source["orientation"]["selected_sign"])
    cycle_orientation = int(contract["canonical_cycle_to_floating_orientation_sign"])
    raw_periods = np.asarray(
        [complex_value(value) for value in execution["center"][:5]], dtype=np.complex128
    )
    raw_residues = np.asarray(
        [complex_value(value) for value in execution["center"][5:]], dtype=np.complex128
    )
    floating_periods = transport_orientation * raw_periods
    floating_residues = -transport_orientation * raw_residues
    a130_periods = cycle_orientation * floating_periods
    a130_residues = cycle_orientation * floating_residues
    payload = {
        "schema": "MTTQ79HeightFourA413OuterLeg.v1",
        "status": "ONE_A413_NATIVE_OUTER_LEG_AFFINE_TRANSPORT_CERTIFIED",
        "artifact": "A414",
        "selected_target": {
            "distinguished_index": arguments.index,
            "root_id": target["root_id"],
            "line_chart": target["line_chart"],
            "A219_contribution_rank": rank,
            "transport_orientation_sign": transport_orientation,
            "canonical_cycle_to_floating_orientation_sign": cycle_orientation,
            "A130_raw_chain_coefficient": int(contract["A130_raw_chain_coefficient"]),
            "endpoint_floating_chain_coefficient": int(contract["endpoint_floating_chain_coefficient"]),
            "Picard_Lefschetz_wall_delta": int(contract["Picard_Lefschetz_wall_delta"]),
        },
        "A404_entry": {
            "entry_index_zero_based": entry_index,
            "label": entry["label"],
            "point": entry["point"],
            "operational_radius": abs(endpoint),
        },
        "cutoff_source_diagnostics": source_diagnostics,
        "validated_outer_main_transport": execution,
        "floating_oriented_entry_period_centers": [encoded_complex(value) for value in floating_periods],
        "floating_oriented_outer_main_residue_centers": [encoded_complex(value) for value in floating_residues],
        "A130_oriented_entry_period_centers": [encoded_complex(value) for value in a130_periods],
        "A130_oriented_outer_main_residue_centers": [encoded_complex(value) for value in a130_residues],
        "residue_coordinate_radius_uppers": execution["residue_coordinate_radius_uppers"],
        "numerics": {
            "main_dps": arguments.main_dps,
            "Taylor_order": arguments.order,
            "initial_step": arguments.initial_step,
            "maximum_step": arguments.maximum_step,
            "minimum_step": arguments.minimum_step,
            "maximum_lift_correction": arguments.maximum_lift_correction,
            "maximum_integral_radius": arguments.maximum_integral_radius,
            "elapsed_seconds": time.perf_counter() - started,
        },
        "authority": {
            "A413_source_manifest": authority(A413),
            "A413_canonical_main_source": authority(source_path),
            "A404_common_junction_manifest": authority(A404),
            "completed_correlated_row_checkpoint": authority(run_paths["checkpoint"]),
            "validated_main_engine": authority(Path(generic.__file__).resolve()),
            "selected_system_engine": authority(Path(main_hessian.__file__).resolve()),
            "C_backed_Taylor_runtime": authority(Path(fast.__file__).resolve()),
            "C_backed_Taylor_equivalence_audit": authority(FAST_AUDIT),
            "builder_source": authority(Path(__file__).resolve()),
        },
        "strict_scope": {
            "observed_SM_values_used": False,
            "same_A413_native_cutoff_source_used": True,
            "same_A404_radial_entry_used": True,
            "full_correlated_checkpoint_frames_retained": True,
            "outer_main_leg_to_common_entry_closed": True,
            "A130_to_floating_orientation_reconciled": True,
            "A410_y_from_z_transition_required": target["line_chart"] == "z",
            "A410_y_from_z_transition_applied": False,
            "matching_local_tail_attached": False,
            "A405_entry_operator_applied": False,
            "integer_chain_combination_at_hub_closed": False,
            "full_correlation_preserving_path_execution_closed": False,
            "interval_Newton_existence_and_uniqueness_closed": False,
            "covariant_zero_proved": False,
            "full_SM_closure_proved": False,
        },
        "next_required_artifact": (
            "attach the A413 local tail, apply A410 for native-z, then apply the "
            "A405/A409T reverse entry operator to the retained affine frames"
        ),
    }
    dump(run_paths["output"], payload)
    run_paths["note"].write_text(
        f"# MTT q79 d{arguments.index:03d} A413 Outer Leg (A414) v1\n\n"
        f"A414 transports the certified native-{target['line_chart']} cutoff source "
        "to its exact A404 radial entry while retaining all eight affine checkpoint "
        "frames. Both floating-oriented and raw-A130-oriented centers are emitted.\n\n"
        f"The maximum outer-main residue radius is "
        f"`{execution['uniform_integral_radius_upper']:.12g}`. Tail splicing, chart "
        "conversion when required, reverse entry application, and the hub sum remain open.\n",
        encoding="utf-8",
    )
    print(f"wrote {relative(run_paths['output'])}", flush=True)
    print(
        json.dumps(
            {
                "index": arguments.index,
                "line_chart": target["line_chart"],
                "accepted_steps": execution["accepted_step_count"],
                "rejected_steps": execution["rejected_step_count"],
                "maximum_outer_main_radius": execution["uniform_integral_radius_upper"],
                "entry_index_zero_based": entry_index,
            },
            indent=2,
        ),
        flush=True,
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
