from __future__ import annotations

import argparse
import json
from argparse import Namespace
from pathlib import Path

from flint import ctx

import certify_q79_height4_source_derived_far_cut_hessian_interval as source_cut
import certify_q79_height4_target_main_hessian_interval as base
import q79_fast_taylor_runtime as fast
import q79_stable_affine_hessian_runtime as stable
import run_q79_height4_stable_fast_reverse_target_main_hessian as reverse


ROOT = Path(__file__).resolve().parents[1]


def authority(path: Path) -> dict[str, str]:
    return {"path": reverse.relative(path), "sha256": reverse.sha256(path)}


def parser() -> argparse.ArgumentParser:
    value = argparse.ArgumentParser()
    value.add_argument("--index", type=int, required=True)
    value.add_argument("--epsilon", type=float, required=True)
    value.add_argument("--dps", type=int, default=150)
    value.add_argument("--order", type=int, default=48)
    value.add_argument("--maximum-step", type=float, default=0.02)
    value.add_argument("--minimum-step", type=float, default=1.0e-12)
    value.add_argument("--maximum-steps", type=int, default=50000)
    value.add_argument("--maximum-lift-correction", type=float, default=1.0e-7)
    value.add_argument("--maximum-output-increment", type=float, default=1.0e-5)
    value.add_argument("--maximum-output-radius", type=float, default=0.005)
    value.add_argument("--resume", action="store_true")
    return value


def main() -> int:
    arguments = parser().parse_args()
    if not 1 <= arguments.index <= 90:
        raise ValueError("index must lie in [1,90]")
    ctx.dps = arguments.dps
    selected = source_cut.paths(arguments.index, arguments.epsilon)
    for name in ("source", "ordinary_tail", "synthetic_main", "canonical_full"):
        if not selected[name].is_file():
            raise FileNotFoundError(f"reverse source-derived input is absent: {name}")
    synthetic = source_cut.load(selected["synthetic_main"])
    if float(synthetic["selected_target"]["endpoint_cutoff_epsilon"]) != arguments.epsilon:
        raise AssertionError("reverse source-derived cutoff identity changed")

    prior_paths = base.target_paths

    def local_paths(_index: int) -> dict[str, Path]:
        return {
            "canonical_main": selected["synthetic_main"],
            "canonical_full": selected["canonical_full"],
            "output": selected["main"],
            "checkpoint": selected["main_checkpoint"],
            "note": selected["main_note"],
            "reverse_checkpoint": selected["main"].parent
            / f"r{arguments.index:03d}.ckpt.json",
            "reverse_note": ROOT
            / "proof_corpus"
            / (
                f"MTT_q79HeightFourD{arguments.index:03d}SourceDerivedReverse"
                "MainHessian_A380BFF_v1.md"
            ),
        }

    base.target_paths = local_paths
    fast.install()
    stable.install()
    try:
        reverse.execute(
            Namespace(
                index=arguments.index,
                dps=arguments.dps,
                order=arguments.order,
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
        stable.uninstall()
        fast.uninstall()
        base.target_paths = prior_paths

    packet = json.loads(selected["main"].read_text(encoding="utf-8"))
    packet["artifact"] = "A380BFF"
    packet["source_derived_reverse_route"] = {
        "selected_cutoff_epsilon": arguments.epsilon,
        "A380FS_source": authority(selected["source"]),
        "ordinary_tail_source": authority(selected["ordinary_tail"]),
        "synthetic_main_replay_source": authority(selected["synthetic_main"]),
    }
    packet["authority"]["A380FS_far_cut_source"] = authority(selected["source"])
    packet["authority"]["selected_far_tail_interval"] = authority(
        selected["ordinary_tail"]
    )
    packet["authority"]["source_derived_main_replay"] = authority(
        selected["synthetic_main"]
    )
    packet["authority"]["reverse_source_route_runner"] = authority(
        Path(__file__).resolve()
    )
    packet["strict_scope"]["source_derived_reverse_main_Hessian_interval_closed"] = True
    selected["main"].write_text(
        json.dumps(packet, indent=2, sort_keys=True) + "\n",
        encoding="utf-8",
    )
    print(
        f"promoted {reverse.relative(selected['main'])} as source-derived "
        f"reverse main at epsilon={arguments.epsilon:.1e}"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
