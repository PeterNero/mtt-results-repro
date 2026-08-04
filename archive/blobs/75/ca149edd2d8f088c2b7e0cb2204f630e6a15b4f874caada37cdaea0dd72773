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
INDEX = 57
EPSILON = 1.0e-3
SOURCE = VALIDATED / "far_source" / "d057.1em03.json"
A404 = VALIDATED / "n3.junction_operator_sweep.a404.json"
CANONICAL_MAIN = VALIDATED / "d057.n3.main8.refined.json"
DIRECTORY = VALIDATED / "ol"
CHECKPOINT = DIRECTORY / "d057.a409o.ckpt.json"
OUTPUT = DIRECTORY / "d057.a409o.json"
NOTE = ROOT / "proof_corpus" / "MTT_q79HeightFourD057OuterLegToA404_A409O_v1.md"
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


def complex_value(value: dict[str, str]) -> complex:
    return complex(float(value["real"]), float(value["imaginary"]))


def encoded_complex(value: complex) -> dict[str, str]:
    return {"real": format(value.real, ".17g"), "imaginary": format(value.imag, ".17g")}


def checkpoint_stamp(arguments: argparse.Namespace, endpoint: complex) -> dict[str, object]:
    return {
        "A409O_builder_sha256": sha256(Path(__file__).resolve()),
        "A409O_A380FS_sha256": sha256(SOURCE),
        "A409O_A404_sha256": sha256(A404),
        "A409O_fast_runtime_sha256": sha256(Path(fast.__file__).resolve()),
        "A409O_fast_audit_sha256": sha256(FAST_AUDIT),
        "A409O_main_dps": arguments.main_dps,
        "A409O_entry": encoded_complex(endpoint),
    }


def selected_entry(manifest: dict) -> tuple[int, dict, complex]:
    matches = [
        (position, row)
        for position, row in enumerate(manifest["ordered_entry_rows"])
        if row.get("kind") == "selected_thimble_entry"
        and int(row["distinguished_index"]) == INDEX
    ]
    if len(matches) != 1:
        raise AssertionError("A409O did not find one d057 A404 entry")
    position, row = matches[0]
    return position, row, complex_value(row["point"])


def main() -> int:
    parser = argparse.ArgumentParser()
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
        raise ValueError("A409O requires at least 90 digits and Taylor order 24")
    ctx.dps = arguments.main_dps
    generic.set_below_normal_priority()
    started = time.perf_counter()
    source = load(SOURCE)
    manifest = load(A404)
    canonical_main = load(CANONICAL_MAIN)
    target = source["selected_target"]
    if (
        source.get("artifact") != "A380FS"
        or int(target["distinguished_index"]) != INDEX
        or target["root_id"] != "selected_008"
        or target["line_chart"] != "y"
        or int(target["signed_chain_coefficient"]) != 4
        or float(target["selected_far_cut_epsilon"]) != EPSILON
    ):
        raise AssertionError("A409O far-cut source changed")
    if manifest.get("artifact") != "A404" or not manifest["theorem"]["proved"]:
        raise AssertionError("A409O junction manifest is unavailable")
    entry_index, entry_row, endpoint = selected_entry(manifest)
    if not math.isclose(abs(endpoint), 0.1, rel_tol=2.0e-15, abs_tol=2.0e-15):
        raise AssertionError("A409O entry left the selected operational circle")
    if int(entry_row["signed_chain_coefficient"]) != int(target["signed_chain_coefficient"]):
        raise AssertionError("A409O chain coefficient differs from A404")

    system, rank, row = main_hessian.selected_system(INDEX, arguments.main_dps)
    if rank != int(target["A219_contribution_rank"]) or row["root_id"] != target["root_id"]:
        raise AssertionError("A409O selected n3 system changed")
    initial_periods = [
        validated.decoded_acb(value)
        for value in source["far_cut_source"]["full_precision_period_balls"]
    ]
    start = complex_value(source["far_cut_source"]["cutoff_start_binary64"])
    cross = abs(start.real * endpoint.imag - start.imag * endpoint.real)
    if cross > 2.0e-15 * abs(start) * abs(endpoint) or (start / endpoint).real <= 1.0:
        raise AssertionError("A409O outer segment is not the selected outward radial leg")
    if arguments.restart and CHECKPOINT.exists():
        CHECKPOINT.unlink()
    stamp = checkpoint_stamp(arguments, endpoint)
    if CHECKPOINT.exists():
        checkpoint = load(CHECKPOINT)
        for key, expected in stamp.items():
            if checkpoint.get(key) != expected:
                raise ValueError(f"A409O checkpoint authority stale: {key}")

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
            index=INDEX,
            root_id=target["root_id"],
            checkpoint_path=CHECKPOINT,
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

    orientation = int(canonical_main["orientation"]["selected_sign"])
    raw_periods = np.asarray(
        [complex_value(value) for value in execution["center"][:5]],
        dtype=np.complex128,
    )
    raw_residues = np.asarray(
        [complex_value(value) for value in execution["center"][5:]],
        dtype=np.complex128,
    )
    selected_periods = orientation * raw_periods
    selected_main_residues = -orientation * raw_residues
    payload = {
        "schema": "MTTQ79HeightFourD057OuterLegToA404.v1",
        "status": "D057_FAR_CUT_TO_COMMON_JUNCTION_ENTRY_MAIN_LEG_CERTIFIED",
        "artifact": "A409O",
        "selected_target": {
            "distinguished_index": INDEX,
            "root_id": target["root_id"],
            "line_chart": "y",
            "A219_contribution_rank": rank,
            "signed_chain_coefficient": int(target["signed_chain_coefficient"]),
            "endpoint_cutoff_epsilon": EPSILON,
            "orientation_sign": orientation,
        },
        "A404_entry": {
            "entry_index_zero_based": entry_index,
            "label": entry_row["label"],
            "point": entry_row["point"],
            "operational_radius": abs(endpoint),
        },
        "validated_outer_main_transport": execution,
        "selected_entry_period_centers": [encoded_complex(value) for value in selected_periods],
        "selected_outer_main_residue_centers": [
            encoded_complex(value) for value in selected_main_residues
        ],
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
            "A380FS_d057_far_cut_source": authority(SOURCE),
            "A404_common_junction_manifest": authority(A404),
            "canonical_d057_orientation": authority(CANONICAL_MAIN),
            "completed_correlated_row_checkpoint": authority(CHECKPOINT),
            "validated_main_engine": authority(Path(generic.__file__).resolve()),
            "selected_system_engine": authority(Path(main_hessian.__file__).resolve()),
            "C_backed_Taylor_runtime": authority(Path(fast.__file__).resolve()),
            "C_backed_Taylor_equivalence_audit": authority(FAST_AUDIT),
            "builder_source": authority(Path(__file__).resolve()),
        },
        "strict_scope": {
            "observed_SM_values_used": False,
            "same_selected_d057_far_cut_source_used": True,
            "same_A404_radial_entry_used": True,
            "full_correlated_checkpoint_frames_retained": True,
            "outer_main_leg_to_common_entry_closed": True,
            "matching_local_Frobenius_tail_attached": False,
            "A405_entry_operator_applied": False,
            "integer_chain_combination_at_hub_closed": False,
            "full_correlation_preserving_path_execution_closed": False,
            "interval_Newton_existence_and_uniqueness_closed": False,
            "covariant_zero_proved": False,
            "full_SM_closure_proved": False,
        },
        "next_required_artifact": (
            "attach A397F to this outer main leg, then apply the audited A405 d057 "
            "entry operator while retaining the checkpoint error frames"
        ),
    }
    dump(OUTPUT, payload)
    NOTE.write_text(
        "# MTT q79 Height-Four d057 Outer Leg to A404 (A409O) v1\n\n"
        "A409O transports the A380FS d057 cutoff period to its selected A404 "
        "radius-1/10 radial entry and retains the completed rowwise affine frames. "
        "The local Frobenius tail and A405 entry-to-hub operator remain separate.\n\n"
        f"The maximum outer-main residue radius is "
        f"`{execution['uniform_integral_radius_upper']:.12g}`.\n",
        encoding="utf-8",
    )
    print(f"wrote {relative(OUTPUT)}", flush=True)
    print(
        json.dumps(
            {
                "accepted_steps": execution["accepted_step_count"],
                "rejected_steps": execution["rejected_step_count"],
                "maximum_outer_main_radius": execution["uniform_integral_radius_upper"],
                "entry_index_zero_based": entry_index,
                "orientation": orientation,
            },
            indent=2,
        ),
        flush=True,
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
