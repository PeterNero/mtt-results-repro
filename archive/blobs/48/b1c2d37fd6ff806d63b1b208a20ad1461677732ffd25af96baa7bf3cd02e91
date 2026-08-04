from __future__ import annotations

import argparse
import hashlib
import json
import math
import time
from pathlib import Path

import numpy as np
from flint import arb, ctx

import certify_q79_height4_d057_continued_pair_full_residue_interval as adapter
import certify_q79_height4_target_full_residue_interval as generic
import certify_q79_height4_target_main_hessian_interval as main_hessian
import certify_q79_selected_side_beta_defect_transport as validated
import q79_fast_taylor_runtime as fast


ROOT = Path(__file__).resolve().parents[1]
VALIDATED = main_hessian.VALIDATED
DIRECTORY = VALIDATED / "far_residue"
FAR_SOURCE = VALIDATED / "far_source" / "d057.1em03.json"
CANONICAL = VALIDATED / "d057.n3.full8.refined.json"
CANONICAL_NODE = VALIDATED / "d057.n3.node.refined.json"
MAIN = DIRECTORY / "d057.main.a397.json"
CHECKPOINT = DIRECTORY / "d057.main.a397.ckpt.json"
TAIL = DIRECTORY / "d057.tail.a397.json"
FULL = DIRECTORY / "d057.full.a397.json"
NOTE = ROOT / "proof_corpus" / "MTT_q79HeightFourD057FarCutFullResidue_A397_v1.md"
FAST_AUDIT = ROOT / "proof_corpus" / "selected_q79fasttaylorruntime_equivalence_audit.py"
ARTIFACT = "A397"
INDEX = 57
EPSILON = 1.0e-3
CANONICAL_PATHS = generic.paths(INDEX)


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


def far_paths() -> dict[str, Path]:
    return {
        **CANONICAL_PATHS,
        "node": CANONICAL_NODE,
        "main": MAIN,
        "main_checkpoint": CHECKPOINT,
        "tail": TAIL,
        "full": FULL,
    }


def verify_checkpoint_authority(arguments: argparse.Namespace) -> None:
    if not CHECKPOINT.exists():
        return
    checkpoint = load(CHECKPOINT)
    expected = {
        "A397_builder_sha256": sha256(Path(__file__).resolve()),
        "A397_far_source_sha256": sha256(FAR_SOURCE),
        "A397_fast_runtime_sha256": sha256(Path(fast.__file__).resolve()),
        "A397_fast_audit_sha256": sha256(FAST_AUDIT),
        "A397_main_dps": arguments.main_dps,
    }
    for key, value in expected.items():
        if checkpoint.get(key) != value:
            raise ValueError(f"A397 checkpoint authority is stale: {key}")


def execute_main(arguments: argparse.Namespace) -> dict:
    started = time.perf_counter()
    ctx.dps = arguments.main_dps
    source = load(FAR_SOURCE)
    target = source["selected_target"]
    if (
        source.get("artifact") != "A380FS"
        or int(target["distinguished_index"]) != INDEX
        or target["root_id"] != "selected_008"
        or int(target["signed_chain_coefficient"]) != 4
        or float(target["selected_far_cut_epsilon"]) != EPSILON
    ):
        raise AssertionError("A397 far-cut source identity changed")
    system, rank, row = main_hessian.selected_system(INDEX, arguments.main_dps)
    if rank != int(target["A219_contribution_rank"]) or row["root_id"] != target["root_id"]:
        raise AssertionError("A397 selected-system row changed")
    initial_periods = [
        validated.decoded_acb(value)
        for value in source["far_cut_source"]["full_precision_period_balls"]
    ]
    start_packet = source["far_cut_source"]["cutoff_start_binary64"]
    start = complex(float(start_packet["real"]), float(start_packet["imaginary"]))
    verify_checkpoint_authority(arguments)
    original_atomic_dump = validated.atomic_dump

    def stamped_checkpoint(path: Path, value: dict) -> None:
        payload = dict(value)
        if payload.get("schema") == "MTTQ79HeightFourAllRowMainCheckpoint.v1":
            payload.update(
                {
                    "A397_builder_sha256": sha256(Path(__file__).resolve()),
                    "A397_far_source_sha256": sha256(FAR_SOURCE),
                    "A397_fast_runtime_sha256": sha256(Path(fast.__file__).resolve()),
                    "A397_fast_audit_sha256": sha256(FAST_AUDIT),
                    "A397_main_dps": arguments.main_dps,
                }
            )
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
        raise AssertionError("A397 far-cut main orientation disagrees with canonical d057")
    selected_difference = min(plus, minus)
    rejected_difference = max(plus, minus)
    if rejected_difference <= 1000.0 * max(selected_difference, 1.0e-15):
        raise AssertionError("A397 far-cut main orientation is not separated")
    transported = np.asarray(
        [complex_value(value) for value in execution["center"][5:]],
        dtype=np.complex128,
    )
    main_center = -orientation * transported
    payload = {
        "schema": "MTTQ79HeightFourD057FarCutResidueMainInterval.v1",
        "status": "D057_FAR_CUT_ALL_EIGHT_MAIN_RESIDUE_ROWS_INTERVAL_CERTIFIED",
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
            "canonical_d057_orientation_replayed": True,
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
            "A380FS_d057_far_cut_period_source": authority(FAR_SOURCE),
            "canonical_d057_main_orientation": authority(CANONICAL_PATHS["main"]),
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
            "full_d057_period_vector_interval_closed": False,
            "covariant_zero_proved": False,
            "full_SM_closure_proved": False,
        },
    }
    dump(MAIN, payload)
    print(f"wrote {relative(MAIN)}", flush=True)
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


def execute_tail(arguments: argparse.Namespace) -> dict:
    original_paths = generic.paths
    original_pilot_pair = generic.pilot.closest_pair
    original_nodal_pair = generic.nodal.closest_pair
    node = load(CANONICAL_NODE)
    adapter.NODE_ROOT_BALL = validated.decoded_acb(
        node["certified_node"]["double_root_ball"]
    )
    adapter.install_pair_selectors()

    def selected_paths(index: int) -> dict[str, Path]:
        if index != INDEX:
            raise ValueError("A397 path adapter is frozen to d057")
        return far_paths()

    generic.paths = selected_paths
    try:
        payload = generic.execute_tail(arguments)
    finally:
        generic.paths = original_paths
        generic.pilot.closest_pair = original_pilot_pair
        generic.nodal.closest_pair = original_nodal_pair
    payload["artifact"] = ARTIFACT
    payload["status"] = "D057_FAR_CUT_ALL_EIGHT_NODE_TO_CUTOFF_TAILS_INTERVAL_CERTIFIED"
    payload["authority"]["A380FS_d057_far_cut_period_source"] = authority(FAR_SOURCE)
    payload["authority"]["d057_continued_pair_adapter"] = authority(
        Path(adapter.__file__).resolve()
    )
    payload["authority"]["A397_builder_source"] = authority(Path(__file__).resolve())
    payload["strict_scope"]["selected_far_cut_epsilon_used"] = True
    payload["strict_scope"]["certified_nodal_pair_selector_consumed"] = True
    payload["strict_scope"]["instantaneous_closest_pair_rule_used"] = False
    dump(TAIL, payload)
    return payload


def execute_full() -> dict:
    main = load(MAIN)
    tail = load(TAIL)
    canonical = load(CANONICAL)
    thimble = load(CANONICAL_PATHS["thimble"])
    orientation = int(main["orientation"]["selected_sign"])
    coefficient = int(main["selected_target"]["signed_chain_coefficient"])
    main_centers = np.asarray(
        [
            complex_value(value)
            for value in main["all_eight_main_residue_rows"]["interval_centers"]
        ],
        dtype=np.complex128,
    )
    tail_centers = np.asarray(
        [
            complex_value(value)
            for value in tail["all_eight_endpoint_tails"]["interval_centers"]
        ],
        dtype=np.complex128,
    )
    main_radii = np.asarray(
        main["validated_main_transport"]["residue_coordinate_radius_uppers"],
        dtype=np.float64,
    )
    tail_radii = np.asarray(
        tail["all_eight_endpoint_tails"]["interval_radius_uppers"],
        dtype=np.float64,
    )
    floating = np.asarray(
        [complex_value(value) for value in thimble["period_values"]],
        dtype=np.complex128,
    )
    full_centers = main_centers + orientation * tail_centers
    full_radii = main_radii + tail_radii
    differences = abs(floating - full_centers)
    if not bool(np.all(differences <= full_radii)):
        raise AssertionError("d057 floating values left the A397 far-cut intervals")
    canonical_maximum = float(canonical["summary"]["maximum_full_interval_radius_upper"])
    far_maximum = float(np.max(full_radii))
    if not far_maximum < canonical_maximum:
        raise AssertionError("A397 far-cut d057 interval does not tighten A246")
    rows = []
    for index in range(8):
        rows.append(
            {
                "residue_index_zero_based": index,
                "full_interval_center": encoded_complex(full_centers[index]),
                "full_interval_radius_upper": float(full_radii[index]),
                "selected_chain_contribution_center": encoded_complex(
                    coefficient * full_centers[index]
                ),
                "selected_chain_contribution_radius_upper": float(
                    abs(coefficient) * full_radii[index]
                ),
                "floating_value_diagnostic_only": encoded_complex(floating[index]),
                "floating_to_interval_center_distance": float(differences[index]),
                "floating_value_contained": True,
                "containment_margin": float(full_radii[index] - differences[index]),
            }
        )
    chain_radii = abs(coefficient) * full_radii
    payload = {
        "schema": "MTTQ79HeightFourD057FarCutFullResidueInterval.v1",
        "status": "D057_FAR_CUT_FULL_EIGHT_ROW_CHAIN_CONTRIBUTION_INTERVAL_CERTIFIED",
        "artifact": ARTIFACT,
        "selected_target": {
            **main["selected_target"],
            "orientation_sign": orientation,
        },
        "residue_rows": rows,
        "summary": {
            "certified_rows": 8,
            "maximum_full_interval_radius_upper": far_maximum,
            "maximum_chain_coordinate_radius_upper": float(np.max(chain_radii)),
            "selected_chain_product_disk_l2_radius_upper": float(
                np.linalg.norm(chain_radii)
            ),
            "maximum_floating_center_difference": float(np.max(differences)),
            "minimum_floating_containment_margin": float(
                np.min(full_radii - differences)
            ),
            "canonical_A246_maximum_full_interval_radius_upper": canonical_maximum,
            "A246_to_A397_maximum_radius_tightening_factor": (
                canonical_maximum / far_maximum
            ),
            "all_floating_values_contained": True,
        },
        "authority": {
            "A380FS_d057_far_cut_period_source": authority(FAR_SOURCE),
            "far_cut_main": authority(MAIN),
            "far_cut_tail": authority(TAIL),
            "canonical_A246_d057_interval": authority(CANONICAL),
            "n3_target_cache": authority(CANONICAL_PATHS["thimble"]),
            "A219_chain_coefficient": authority(generic.BOUNDARY),
            "builder_source": authority(Path(__file__).resolve()),
        },
        "strict_scope": {
            "observed_SM_values_used": False,
            "far_cut_period_source_interval_closed": True,
            "all_eight_far_cut_main_rows_interval_closed": True,
            "all_eight_matching_tail_rows_interval_closed": True,
            "orientation_splice_closed": True,
            "full_period_vector_interval_closed": True,
            "selected_chain_contribution_interval_closed": True,
            "strictly_tighter_than_canonical_A246": True,
            "floating_values_used_as_bounds": False,
            "full_76_target_chain_recomposition_updated": False,
            "coupled_beta_period_residual_transport_closed": False,
            "interval_Newton_existence_and_uniqueness_closed": False,
            "covariant_zero_proved": False,
            "full_SM_closure_proved": False,
        },
        "next_required_artifact": (
            "replace the canonical d057 row in the 76-target chain recomposition, "
            "then apply the same far-cut strategy to the next dominant targets"
        ),
    }
    dump(FULL, payload)
    NOTE.write_text(
        "# MTT q79 Height-Four d057 Far-Cut Full Residue (A397) v1\n\n"
        "A397 restarts the selected d057 period transport from the independently "
        "certified A380FS source at `epsilon=10^-3`, splices the matching "
        "continued-pair tail, and replays all eight floating diagnostics.\n\n"
        f"The maximum full-row radius falls from `{canonical_maximum:.12g}` in "
        f"A246 to `{far_maximum:.12g}`, a factor "
        f"`{canonical_maximum / far_maximum:.12g}`.\n\n"
        "This closes only the tighter d057 contribution. The 76-target chain "
        "recomposition, coupled beta-period enclosure, polydisk Krawczyk theorem, "
        "covariant zero, and full SM closure remain open.\n",
        encoding="utf-8",
    )
    print(f"wrote {relative(FULL)}", flush=True)
    print(f"wrote {relative(NOTE)}", flush=True)
    print(json.dumps(payload["summary"], indent=2), flush=True)
    return payload


def parser() -> argparse.ArgumentParser:
    value = argparse.ArgumentParser()
    value.add_argument("--phase", choices=("main", "tail", "full", "all"), default="all")
    value.add_argument("--main-dps", type=int, default=100)
    value.add_argument("--order", type=int, default=32)
    value.add_argument("--initial-step", type=float, default=1.0e-4)
    value.add_argument("--maximum-step", type=float, default=0.003)
    value.add_argument("--minimum-step", type=float, default=1.0e-12)
    value.add_argument("--maximum-lift-correction", type=float, default=1.0e-10)
    value.add_argument("--maximum-integral-radius", type=float, default=1.0e-4)
    value.add_argument("--tail-dps", type=int, default=100)
    value.add_argument("--node-width", type=float, default=1.0e-10)
    value.add_argument("--outer-segments", type=int, default=9600)
    value.add_argument("--theta-segments", type=int, default=32)
    value.add_argument("--factor-order", type=int, default=32)
    value.add_argument("--cooling-pause-every", type=int, default=20)
    value.add_argument("--cooling-pause-seconds", type=float, default=0.0)
    value.add_argument("--restart", action="store_true")
    return value


def main() -> int:
    arguments = parser().parse_args()
    arguments.index = INDEX
    arguments.epsilon = EPSILON
    if arguments.main_dps < 90 or arguments.order < 24:
        raise ValueError("A397 requires at least 90 digits and Taylor order 24")
    if not 0.0 < arguments.node_width < EPSILON:
        raise ValueError("A397 requires 0 < node width < epsilon")
    if arguments.restart and CHECKPOINT.exists():
        CHECKPOINT.unlink()
    DIRECTORY.mkdir(parents=True, exist_ok=True)
    generic.set_below_normal_priority()
    if arguments.phase in {"main", "all"}:
        execute_main(arguments)
    if arguments.phase in {"tail", "all"}:
        execute_tail(arguments)
    if arguments.phase in {"full", "all"}:
        execute_full()
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
