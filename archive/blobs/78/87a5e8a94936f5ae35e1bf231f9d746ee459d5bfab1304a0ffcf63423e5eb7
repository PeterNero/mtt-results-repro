from __future__ import annotations

import argparse
import hashlib
import json
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
DIRECTORY = VALIDATED / "far_residue"
INDEX = 27
EPSILON = 1.0e-3
FAR_SOURCE = VALIDATED / "far_source" / "d027.1em03.json"
CANONICAL_PATHS = generic.paths(INDEX)
MAIN = DIRECTORY / "d027.main.a406m.json"
CHECKPOINT = DIRECTORY / "d027.main.a406m.ckpt.json"
NOTE = ROOT / "proof_corpus" / "MTT_q79HeightFourD027FarCutMainResidue_A406M_v1.md"
FAST_AUDIT = ROOT / "proof_corpus" / "selected_q79fasttaylorruntime_equivalence_audit.py"
ARTIFACT = "A406M"


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
    return {
        "real": format(value.real, ".17g"),
        "imaginary": format(value.imag, ".17g"),
    }


def checkpoint_stamp(arguments: argparse.Namespace) -> dict[str, object]:
    return {
        "A406M_builder_sha256": sha256(Path(__file__).resolve()),
        "A406M_far_source_sha256": sha256(FAR_SOURCE),
        "A406M_fast_runtime_sha256": sha256(Path(fast.__file__).resolve()),
        "A406M_fast_audit_sha256": sha256(FAST_AUDIT),
        "A406M_main_dps": arguments.main_dps,
    }


def verify_checkpoint(arguments: argparse.Namespace) -> None:
    if not CHECKPOINT.exists():
        return
    packet = load(CHECKPOINT)
    for key, expected in checkpoint_stamp(arguments).items():
        if packet.get(key) != expected:
            raise ValueError(f"A406M checkpoint authority is stale: {key}")


def execute(arguments: argparse.Namespace) -> dict:
    ctx.dps = arguments.main_dps
    started = time.perf_counter()
    source = load(FAR_SOURCE)
    target = source["selected_target"]
    expected = {
        "distinguished_index": INDEX,
        "root_id": "selected_011",
        "A219_contribution_rank": 15,
        "signed_chain_coefficient": -2,
        "selected_far_cut_epsilon": EPSILON,
    }
    if source.get("artifact") != "A380FS":
        raise AssertionError("A406M source is not A380FS")
    for key, value in expected.items():
        actual = target[key]
        if isinstance(value, float):
            actual = float(actual)
        elif isinstance(value, int):
            actual = int(actual)
        if actual != value:
            raise AssertionError(f"A406M selected target changed: {key}")
    for label, entry in source["authority"].items():
        path = ROOT / entry["path"]
        if not path.is_file() or sha256(path) != entry["sha256"]:
            raise AssertionError(f"A406M source authority stale: {label}")

    system, rank, row = main_hessian.selected_system(INDEX, arguments.main_dps)
    if rank != int(target["A219_contribution_rank"]) or row["root_id"] != target["root_id"]:
        raise AssertionError("A406M selected-system row changed")
    initial_periods = [
        validated.decoded_acb(value)
        for value in source["far_cut_source"]["full_precision_period_balls"]
    ]
    start_row = source["far_cut_source"]["cutoff_start_binary64"]
    start = complex(float(start_row["real"]), float(start_row["imaginary"]))
    verify_checkpoint(arguments)
    original_atomic_dump = validated.atomic_dump

    def stamped_checkpoint(path: Path, value: dict) -> None:
        payload = dict(value)
        if payload.get("schema") == "MTTQ79HeightFourAllRowMainCheckpoint.v1":
            payload.update(checkpoint_stamp(arguments))
        original_atomic_dump(path, payload)

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
            endpoint=0.0 + 0.0j,
            order=arguments.order,
            maximum_step=arguments.maximum_step,
            initial_step=min(arguments.initial_step, abs(start)),
            minimum_step=arguments.minimum_step,
            maximum_lift_correction=arguments.maximum_lift_correction,
            maximum_integral_radius=arguments.maximum_integral_radius,
            cooling_pause_every=arguments.cooling_pause_every,
            cooling_pause_seconds=arguments.cooling_pause_seconds,
        )
    finally:
        fast.uninstall()
        validated.atomic_dump = original_atomic_dump

    canonical_main = load(CANONICAL_PATHS["main"])
    expected_orientation = int(canonical_main["orientation"]["selected_sign"])
    base_center = np.asarray(
        [complex_value(value) for value in execution["center"][:5]],
        dtype=np.complex128,
    )
    thimble = load(CANONICAL_PATHS["thimble"])
    floating_base = np.asarray(
        [complex_value(value) for value in thimble["base_fiber_propagated_periods"]],
        dtype=np.complex128,
    )
    plus = float(np.max(abs(base_center - floating_base)))
    minus = float(np.max(abs(-base_center - floating_base)))
    orientation = 1 if plus <= minus else -1
    if orientation != expected_orientation:
        raise AssertionError("A406M orientation disagrees with canonical d027")
    selected_difference = min(plus, minus)
    rejected_difference = max(plus, minus)
    if rejected_difference <= 1000.0 * max(selected_difference, 1.0e-15):
        raise AssertionError("A406M orientation is not separated")
    transported = np.asarray(
        [complex_value(value) for value in execution["center"][5:]],
        dtype=np.complex128,
    )
    main_center = -orientation * transported
    payload = {
        "schema": "MTTQ79HeightFourD027FarCutResidueMainInterval.v1",
        "status": "D027_FAR_CUT_ALL_EIGHT_MAIN_RESIDUE_ROWS_INTERVAL_CERTIFIED",
        "artifact": ARTIFACT,
        "selected_target": {
            "distinguished_index": INDEX,
            "root_id": target["root_id"],
            "line_chart": target["line_chart"],
            "A219_contribution_rank": rank,
            "signed_chain_coefficient": int(target["signed_chain_coefficient"]),
            "endpoint_cutoff_epsilon": EPSILON,
            "near_node_colliding_pair_zero_based": target["preselected_pair_zero_based"],
        },
        "validated_main_transport": execution,
        "orientation": {
            "selected_sign": orientation,
            "selected_base_center_maximum_difference": selected_difference,
            "opposite_base_center_maximum_difference": rejected_difference,
            "canonical_d027_orientation_replayed": True,
        },
        "all_eight_main_residue_rows": {
            "interval_centers": [encoded_complex(value) for value in main_center],
            "residue_coordinate_radius_uppers": execution[
                "residue_coordinate_radius_uppers"
            ],
            "maximum_radius_upper": execution["uniform_integral_radius_upper"],
        },
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
            "A380FS_d027_far_cut_period_source": authority(FAR_SOURCE),
            "canonical_d027_main_orientation": authority(CANONICAL_PATHS["main"]),
            "n3_target_cache": authority(CANONICAL_PATHS["thimble"]),
            "completed_transport_checkpoint": authority(CHECKPOINT),
            "validated_main_engine": authority(Path(generic.__file__).resolve()),
            "selected_system_engine": authority(Path(main_hessian.__file__).resolve()),
            "C_backed_Taylor_runtime": authority(Path(fast.__file__).resolve()),
            "C_backed_Taylor_equivalence_audit": authority(FAST_AUDIT),
            "builder_source": authority(Path(__file__).resolve()),
        },
        "strict_scope": {
            "observed_SM_values_used": False,
            "far_cut_period_source_consumed": True,
            "all_eight_far_cut_main_rows_interval_closed": True,
            "matching_far_cut_tail_interval_closed": False,
            "full_d027_period_vector_interval_closed": False,
            "covariant_zero_proved": False,
            "full_SM_closure_proved": False,
        },
        "next_required_artifact": (
            "certify the selected d027 epsilon-1e-3 endpoint tail with the "
            "quantitative Hensel/Frobenius engine"
        ),
    }
    dump(MAIN, payload)
    NOTE.write_text(
        "# MTT q79 Height-Four d027 Far-Cut Main Residue (A406M) v1\n\n"
        "A406M transports the audited A380FS d027 cutoff-period balls to the "
        "base on the exact selected n3 system. It closes all eight main residue "
        "rows and replays the independently stored canonical orientation.\n\n"
        f"The maximum main-row radius is `{execution['uniform_integral_radius_upper']:.12g}`. "
        "The matching endpoint tail and full d027 splice remain separate gates.\n",
        encoding="utf-8",
    )
    print(f"wrote {relative(MAIN)}")
    print(
        json.dumps(
            {
                "maximum_main_radius": execution["uniform_integral_radius_upper"],
                "accepted_steps": execution["accepted_step_count"],
                "rejected_steps": execution["rejected_step_count"],
                "orientation": orientation,
            },
            indent=2,
        ),
        flush=True,
    )
    return payload


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--main-dps", type=int, default=100)
    parser.add_argument("--order", type=int, default=32)
    parser.add_argument("--initial-step", type=float, default=1.0e-4)
    parser.add_argument("--maximum-step", type=float, default=0.003)
    parser.add_argument("--minimum-step", type=float, default=1.0e-12)
    parser.add_argument("--maximum-lift-correction", type=float, default=1.0e-10)
    parser.add_argument("--maximum-integral-radius", type=float, default=1.0e-4)
    parser.add_argument("--cooling-pause-every", type=int, default=20)
    parser.add_argument("--cooling-pause-seconds", type=float, default=0.0)
    parser.add_argument("--restart", action="store_true")
    arguments = parser.parse_args()
    if arguments.main_dps < 90 or arguments.order < 24:
        raise ValueError("A406M requires at least 90 digits and Taylor order 24")
    if arguments.restart and CHECKPOINT.exists():
        CHECKPOINT.unlink()
    DIRECTORY.mkdir(parents=True, exist_ok=True)
    generic.set_below_normal_priority()
    execute(arguments)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
