from __future__ import annotations

import argparse
import copy
import hashlib
import json
import sys
from argparse import Namespace
from pathlib import Path

import numpy as np
from flint import acb, ctx

import build_q79_height4_selected_far_cut_period_source as source_builder
import build_q79_height4_target_full_hessian_interval as full_hessian
import certify_q79_height4_dynamic_target_full_residue_interval as dynamic
import certify_q79_height4_target_full_residue_interval as ordinary
import certify_q79_height4_target_main_hessian_interval as main_hessian
import certify_q79_height4_target_tail_hessian_interval as tail_hessian
import certify_q79_height4_target_tail_hessian_quadrature_interval as quadrature
import certify_q79_height4_tight_target_full_residue_interval as tight
import certify_q79_selected_alignment_E32_handle_combination_interval as handle
import certify_q79_selected_side_beta_defect_transport as validated


ROOT = Path(__file__).resolve().parents[1]
OUTPUT_DIRECTORY = main_hessian.OUTPUT_DIRECTORY / "far2"
ARTIFACT = "A380FF-A382FF"


def load(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def dump(path: Path, value: dict) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(value, indent=2, sort_keys=True) + "\n", encoding="utf-8")


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def relative(path: Path) -> str:
    return str(path.relative_to(ROOT)).replace("\\", "/")


def pair(value: complex) -> dict[str, str]:
    return {
        "real": format(float(value.real), ".17g"),
        "imaginary": format(float(value.imag), ".17g"),
    }


def paths(index: int, epsilon: float) -> dict[str, Path]:
    canonical = tight.canonical_paths(index)
    source, _source_note = source_builder.paths(index, epsilon)
    stem = f"d{index:03d}"
    return {
        "thimble": canonical["thimble"],
        "canonical_main": canonical["main"],
        "canonical_tail": canonical["tail"],
        "canonical_full": canonical["full"],
        "source": source,
        "node": OUTPUT_DIRECTORY / f"{stem}.node.json",
        "ordinary_tail": OUTPUT_DIRECTORY / f"{stem}.tail.json",
        "synthetic_main": OUTPUT_DIRECTORY / f"{stem}.main_source.json",
        "main": OUTPUT_DIRECTORY / f"{stem}.mainH.json",
        "main_checkpoint": OUTPUT_DIRECTORY / f"{stem}.mainH.checkpoint.json",
        "tail": OUTPUT_DIRECTORY / f"{stem}.tailH.json",
        "full": OUTPUT_DIRECTORY / f"{stem}.fullH.json",
        "main_note": ROOT
        / "proof_corpus"
        / f"MTT_q79HeightFourD{index:03d}SourceDerivedFarMainHessian_A380FF_v1.md",
        "tail_note": ROOT
        / "proof_corpus"
        / f"MTT_q79HeightFourD{index:03d}SourceDerivedFarTailHessian_A381QFF_v1.md",
        "full_note": ROOT
        / "proof_corpus"
        / f"MTT_q79HeightFourD{index:03d}SourceDerivedFarFullHessian_A382FF_v1.md",
    }


def authority(path: Path) -> dict[str, str]:
    return {"path": relative(path), "sha256": sha256(path)}


def ensure_source(arguments: argparse.Namespace, selected: dict[str, Path]) -> dict:
    if not selected["source"].exists():
        source_builder.execute(
            Namespace(
                index=arguments.index,
                epsilon=arguments.epsilon,
                dps=arguments.dps,
                cut_segments=arguments.cut_segments,
                cut_tolerance=arguments.cut_tolerance,
                maximum_period_radius=arguments.maximum_period_radius,
            )
        )
    source = load(selected["source"])
    if (
        source.get("artifact") != "A380FS"
        or int(source["selected_target"]["distinguished_index"]) != arguments.index
        or float(source["selected_target"]["selected_far_cut_epsilon"])
        != arguments.epsilon
    ):
        raise AssertionError("selected far-cut source identity changed")
    for row in source["authority"].values():
        path = ROOT / row["path"]
        if not path.exists() or sha256(path) != row["sha256"]:
            raise AssertionError("selected far-cut source authority is stale")
    return source


def write_node_packet(
    arguments: argparse.Namespace,
    selected: dict[str, Path],
    source: dict,
) -> None:
    canonical = load(selected["canonical_main"])
    packet = {
        "schema": "MTTQ79HeightFourSourceDerivedFarNodeReuse.v1",
        "status": "CANONICAL_CERTIFIED_NODE_REUSED_FOR_SELECTED_FAR_CUT",
        "artifact": "A380FN",
        "selected_target": {
            "distinguished_index": arguments.index,
            "root_id": source["selected_target"]["root_id"],
            "line_chart": source["selected_target"]["line_chart"],
            "endpoint_cutoff_epsilon": arguments.epsilon,
        },
        "certified_node": canonical["certified_node"],
        "authority": {
            "canonical_main_interval": authority(selected["canonical_main"]),
            "A380FS_far_cut_source": authority(selected["source"]),
            "builder_source": authority(Path(__file__).resolve()),
        },
        "strict_scope": {
            "observed_SM_values_used": False,
            "canonical_node_interval_reused": True,
            "node_reselected_or_fitted": False,
        },
    }
    dump(selected["node"], packet)


def ordinary_paths(selected: dict[str, Path]) -> dict[str, Path]:
    return {
        "thimble": selected["thimble"],
        "node": selected["node"],
        "main": selected["synthetic_main"],
        "main_checkpoint": selected["main_checkpoint"],
        "tail": selected["ordinary_tail"],
        "full": selected["canonical_full"],
    }


def build_ordinary_tail(
    arguments: argparse.Namespace,
    selected: dict[str, Path],
    source: dict,
) -> dict:
    write_node_packet(arguments, selected, source)
    prior_paths = ordinary.paths
    prior_target = ordinary.target
    prior_exact = ordinary.main_engine.exact_target_system
    prior_fast_node = ordinary.main_engine.fast_certify_node
    prior_pair_selector = ordinary.nodal.closest_pair
    prior_midpoint = ordinary.nodal.midpoint
    prior_factor_models = ordinary.tail.factor_taylor_models
    prior_direct_cut = ordinary.handle.direct_cut_periods
    source_periods = [
        validated.decoded_acb(value)
        for value in source["far_cut_source"]["full_precision_period_balls"]
    ]
    source_pair = tuple(
        int(value)
        for value in source["selected_target"]["preselected_pair_zero_based"]
    )

    def source_oriented_direct_cut(*args, **kwargs):
        roots = args[0]
        requested_pair = tuple(int(value) for value in args[2])
        if requested_pair != source_pair:
            raise AssertionError("ordinary tail requested a different far-cut pair")
        minimum_root_separation = min(
            validated.lower(abs(roots[left] - roots[right]))
            for left in range(len(roots))
            for right in range(left)
        )
        if minimum_root_separation <= 0.0:
            raise AssertionError("ordinary-tail far-cut root balls overlap")
        diagnostics = dict(source["far_cut_source"]["direct_cut_diagnostics"])
        diagnostics.update(
            {
                "period_source_method": (
                    "consume the exact A380FS arbitrary-precision cutoff-period "
                    "balls; the tail engine separately encloses its endpoint sliver"
                ),
                "requested_pair_zero_based": list(requested_pair),
                "current_root_ball_separation_lower": minimum_root_separation,
                "A380FS_source_sha256": sha256(selected["source"]),
            }
        )
        return [acb(value) for value in source_periods], diagnostics

    tight.configure_selected_target(arguments.index)
    tight.install_target_adapters(arguments.index, dynamic.CHART)
    ordinary.paths = lambda _index: ordinary_paths(selected)
    ordinary.handle.direct_cut_periods = source_oriented_direct_cut
    try:
        dynamic.load_node_for_tail()
        source_start_row = source["far_cut_source"]["cutoff_start_binary64"]
        source_start = validated.exact_acb(
            {
                "real": source_start_row["real"],
                "imaginary": source_start_row["imaginary"],
            }
        )
        epsilon_factor = validated.exact_acb(
            {"real": format(1.0 - arguments.epsilon, ".17g"), "imaginary": "0"}
        )
        def source_midpoint(_value):
            ordinary.nodal.midpoint = prior_midpoint
            return source_start / epsilon_factor

        def factor_models_then_install_source_cutoff(*args, **kwargs):
            value = prior_factor_models(*args, **kwargs)
            ordinary.nodal.midpoint = source_midpoint
            return value

        ordinary.tail.factor_taylor_models = factor_models_then_install_source_cutoff
        ordinary.nodal.closest_pair = lambda _roots: source_pair
        packet = ordinary.execute_tail(
            Namespace(
                index=arguments.index,
                epsilon=arguments.epsilon,
                tail_dps=arguments.dps,
                factor_order=arguments.factor_order,
                node_width=arguments.node_width,
                outer_segments=arguments.ordinary_tail_segments,
                theta_segments=arguments.theta_segments,
            )
        )
    finally:
        ordinary.paths = prior_paths
        ordinary.target = prior_target
        ordinary.main_engine.exact_target_system = prior_exact
        ordinary.main_engine.fast_certify_node = prior_fast_node
        ordinary.nodal.closest_pair = prior_pair_selector
        ordinary.nodal.midpoint = prior_midpoint
        ordinary.tail.factor_taylor_models = prior_factor_models
        ordinary.handle.direct_cut_periods = prior_direct_cut
    packet["artifact"] = "A380FT"
    packet["selected_target"]["line_chart"] = source["selected_target"]["line_chart"]
    packet["source_derived_far_route"] = {
        "selected_far_cut_epsilon": arguments.epsilon,
        "A380FS_source": authority(selected["source"]),
        "adapter": authority(Path(__file__).resolve()),
    }
    packet["authority"]["A380FS_far_cut_source"] = authority(selected["source"])
    packet["authority"]["source_derived_far_adapter"] = authority(
        Path(__file__).resolve()
    )
    packet["strict_scope"][
        "source_derived_far_cutoff_period_source_consumed_exactly"
    ] = True
    dump(selected["ordinary_tail"], packet)
    return packet


def build_synthetic_main(
    arguments: argparse.Namespace,
    selected: dict[str, Path],
    source: dict,
    ordinary_tail_packet: dict,
) -> dict:
    canonical_main = load(selected["canonical_main"])
    canonical_full = load(selected["canonical_full"])
    orientation = int(canonical_full["selected_target"]["orientation_sign"])
    if orientation not in {-1, 1}:
        raise AssertionError("canonical full orientation is not a sign")
    full_centers = np.asarray(
        [
            complex(
                float(row["full_interval_center"]["real"]),
                float(row["full_interval_center"]["imaginary"]),
            )
            for row in canonical_full["residue_rows"]
        ],
        dtype=np.complex128,
    )
    full_radii = np.asarray(
        [float(row["full_interval_radius_upper"]) for row in canonical_full["residue_rows"]],
        dtype=np.float64,
    )
    tail_rows = ordinary_tail_packet["all_eight_endpoint_tails"]
    tail_centers = np.asarray(
        [
            complex(float(row["real"]), float(row["imaginary"]))
            for row in tail_rows["interval_centers"]
        ],
        dtype=np.complex128,
    )
    tail_radii = np.asarray(tail_rows["interval_radius_uppers"], dtype=np.float64)
    expected_centers = full_centers - orientation * tail_centers
    expected_radii = full_radii + tail_radii
    source_periods = [
        validated.decoded_acb(value)
        for value in source["far_cut_source"]["full_precision_period_balls"]
    ]
    packet = {
        "schema": "MTTQ79HeightFourSourceDerivedFarMainReplayInterval.v1",
        "status": "FAR_MAIN_REPLAY_INTERVAL_DERIVED_FROM_CANONICAL_FULL_MINUS_FAR_TAIL",
        "artifact": "A380FM",
        "selected_target": {
            **copy.deepcopy(canonical_main["selected_target"]),
            "endpoint_cutoff_epsilon": arguments.epsilon,
            "near_node_colliding_pair_zero_based": source["selected_target"][
                "preselected_pair_zero_based"
            ],
        },
        "certified_node": canonical_main["certified_node"],
        "near_node_direct_cycle_interval": {
            **source["far_cut_source"]["direct_cut_diagnostics"],
            "initial_period_intervals": [
                handle.complex_interval(value) for value in source_periods
            ],
        },
        "orientation": {
            "selected_sign": orientation,
            "source": "canonical full thimble orientation",
        },
        "all_eight_main_residue_rows": {
            "interval_centers": [pair(value) for value in expected_centers],
            "common_complex_disk_radius_upper": float(np.max(expected_radii)),
            "per_row_derived_radius_uppers": expected_radii.tolist(),
            "derivation": "canonical full interval minus oriented selected far-tail interval",
        },
        "numerics": {
            "dps": arguments.dps,
            "cut_segments": int(source["numerics"]["cut_segments"]),
            "cut_tolerance": float(source["numerics"]["cut_tolerance"]),
        },
        "authority": {
            "canonical_main_node_and_orientation": authority(selected["canonical_main"]),
            "canonical_full_interval": authority(selected["canonical_full"]),
            "selected_far_tail_interval": authority(selected["ordinary_tail"]),
            "A380FS_far_cut_source": authority(selected["source"]),
            "builder_source": authority(Path(__file__).resolve()),
        },
        "strict_scope": {
            "observed_SM_values_used": False,
            "expected_far_main_interval_derived_by_interval_subtraction": True,
            "canonical_full_and_selected_far_tail_independent_of_far_main_transport": True,
            "far_main_Hessian_interval_closed": False,
        },
    }
    dump(selected["synthetic_main"], packet)
    return packet


def promote(
    path: Path,
    *,
    artifact: str,
    source: Path,
    extra_authority: dict[str, Path],
) -> dict:
    packet = load(path)
    packet["artifact"] = artifact
    packet["source_derived_far_route"] = {
        "A380FS_source": authority(source),
        "adapter": authority(Path(__file__).resolve()),
    }
    packet["authority"]["A380FS_far_cut_source"] = authority(source)
    packet["authority"]["source_derived_far_adapter"] = authority(
        Path(__file__).resolve()
    )
    for name, authority_path in extra_authority.items():
        packet["authority"][name] = authority(authority_path)
    dump(path, packet)
    return packet


def run_main_hessian(
    arguments: argparse.Namespace,
    selected: dict[str, Path],
) -> dict:
    prior = main_hessian.target_paths

    def local_paths(_index: int) -> dict[str, Path]:
        return {
            "canonical_main": selected["synthetic_main"],
            "canonical_full": selected["canonical_full"],
            "output": selected["main"],
            "checkpoint": selected["main_checkpoint"],
            "note": selected["main_note"],
        }

    main_hessian.target_paths = local_paths
    try:
        main_hessian.execute(
            Namespace(
                index=arguments.index,
                dps=arguments.dps,
                order=arguments.main_order,
                maximum_step=arguments.maximum_step,
                minimum_step=arguments.minimum_step,
                maximum_steps=arguments.maximum_steps,
                maximum_lift_correction=arguments.maximum_lift_correction,
                maximum_output_increment=arguments.maximum_output_increment,
                maximum_output_radius=arguments.maximum_output_radius,
                resume=arguments.resume,
                smoke_only=False,
            )
        )
    finally:
        main_hessian.target_paths = prior
    packet = promote(
        selected["main"],
        artifact="A380FF",
        source=selected["source"],
        extra_authority={
            "derived_far_main_replay_source": selected["synthetic_main"],
            "selected_far_tail_interval": selected["ordinary_tail"],
            "canonical_full_interval": selected["canonical_full"],
        },
    )
    packet["strict_scope"]["far_main_replayed_from_full_minus_tail_interval"] = True
    dump(selected["main"], packet)
    return packet


def run_tail_hessian(
    arguments: argparse.Namespace,
    selected: dict[str, Path],
) -> dict:
    prior = tail_hessian.output_paths

    def local_paths(_index: int) -> dict[str, Path]:
        return {
            "main": selected["synthetic_main"],
            "tail": selected["ordinary_tail"],
            "output": selected["tail"],
            "note": selected["tail_note"],
        }

    tail_hessian.output_paths = local_paths
    try:
        quadrature.execute(
            Namespace(
                index=arguments.index,
                dps=arguments.dps,
                order=arguments.tail_order,
                outer_segments=arguments.tail_seed_segments,
                theta_segments=arguments.theta_segments,
                node_width=arguments.node_width,
                series_terms=arguments.series_terms,
            )
        )
    finally:
        tail_hessian.output_paths = prior
    return promote(
        selected["tail"],
        artifact="A381QFF",
        source=selected["source"],
        extra_authority={
            "selected_far_tail_interval": selected["ordinary_tail"],
            "derived_far_main_replay_source": selected["synthetic_main"],
        },
    )


def run_full_hessian(arguments: argparse.Namespace, selected: dict[str, Path]) -> dict:
    prior = full_hessian.paths

    def local_paths(_index: int) -> dict[str, Path]:
        return {
            "main": selected["main"],
            "tail": selected["tail"],
            "canonical_full": selected["canonical_full"],
            "output": selected["full"],
            "note": selected["full_note"],
        }

    full_hessian.paths = local_paths
    prior_argv = sys.argv
    try:
        sys.argv = [str(Path(full_hessian.__file__).resolve()), "--index", str(arguments.index)]
        full_hessian.main()
    finally:
        sys.argv = prior_argv
        full_hessian.paths = prior
    packet = promote(
        selected["full"],
        artifact="A382FF",
        source=selected["source"],
        extra_authority={
            "selected_far_tail_interval": selected["ordinary_tail"],
            "derived_far_main_replay_source": selected["synthetic_main"],
            "canonical_full_interval_direct": selected["canonical_full"],
        },
    )
    packet["strict_scope"]["source_derived_far_full_Hessian_interval_closed"] = True
    dump(selected["full"], packet)
    return packet


def parser() -> argparse.ArgumentParser:
    value = argparse.ArgumentParser()
    value.add_argument("--index", type=int, required=True)
    value.add_argument(
        "--phase",
        choices=("tail", "main", "tail-hessian", "full", "all"),
        default="all",
    )
    value.add_argument("--epsilon", type=float, default=1.0e-3)
    value.add_argument("--dps", type=int, default=100)
    value.add_argument("--cut-segments", type=int, default=40)
    value.add_argument("--cut-tolerance", type=float, default=1.0e-50)
    value.add_argument("--maximum-period-radius", type=float, default=1.0e-35)
    value.add_argument("--factor-order", type=int, default=32)
    value.add_argument("--ordinary-tail-segments", type=int, default=9600)
    value.add_argument("--tail-seed-segments", type=int, default=64)
    value.add_argument("--theta-segments", type=int, default=32)
    value.add_argument("--node-width", type=float, default=1.0e-10)
    value.add_argument("--series-terms", type=int, default=10)
    value.add_argument("--main-order", type=int, default=20)
    value.add_argument("--tail-order", type=int, default=24)
    value.add_argument("--maximum-step", type=float, default=0.003)
    value.add_argument("--minimum-step", type=float, default=1.0e-10)
    value.add_argument("--maximum-steps", type=int, default=50000)
    value.add_argument("--maximum-lift-correction", type=float, default=1.0e-6)
    value.add_argument("--maximum-output-increment", type=float, default=2.0e-3)
    value.add_argument("--maximum-output-radius", type=float, default=0.25)
    value.add_argument("--resume", action="store_true")
    return value


def main() -> int:
    arguments = parser().parse_args()
    if not 1 <= arguments.index <= 90:
        raise ValueError("index must lie in [1,90]")
    if not 0.0 < arguments.node_width < arguments.epsilon < 0.01:
        raise ValueError("require 0 < node width < far-cut epsilon < 0.01")
    ctx.dps = arguments.dps
    selected = paths(arguments.index, arguments.epsilon)
    source = ensure_source(arguments, selected)

    if arguments.phase in {"tail", "all"}:
        ordinary_tail_packet = build_ordinary_tail(arguments, selected, source)
        build_synthetic_main(arguments, selected, source, ordinary_tail_packet)
    if arguments.phase in {"main", "tail-hessian", "full"}:
        if not selected["ordinary_tail"].exists():
            raise FileNotFoundError("source-derived far ordinary tail is absent")
        if not selected["synthetic_main"].exists():
            build_synthetic_main(
                arguments, selected, source, load(selected["ordinary_tail"])
            )
    if arguments.phase in {"main", "all"}:
        run_main_hessian(arguments, selected)
    if arguments.phase in {"tail-hessian", "all"}:
        run_tail_hessian(arguments, selected)
    if arguments.phase in {"full", "all"}:
        for name in ("main", "tail"):
            if not selected[name].exists():
                raise FileNotFoundError(f"source-derived far {name} Hessian is absent")
        run_full_hessian(arguments, selected)
    print(f"{ARTIFACT}: d{arguments.index:03d} phase={arguments.phase} complete")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
