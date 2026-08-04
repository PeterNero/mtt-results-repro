from __future__ import annotations

import argparse
import hashlib
import json
import sys
from argparse import Namespace
from pathlib import Path

from flint import ctx

import build_q79_height4_target_full_hessian_interval as full_hessian
import certify_q79_height4_target_main_hessian_interval as main_hessian
import certify_q79_height4_target_tail_hessian_interval as tail_hessian
import certify_q79_height4_target_tail_hessian_quadrature_interval as quadrature
import certify_q79_height4_tight_target_full_residue_interval as tight


ROOT = Path(__file__).resolve().parents[1]
OUTPUT = main_hessian.OUTPUT_DIRECTORY / "far"
ARTIFACT = "A380F-A382F"


def load(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def dump(path: Path, value: dict) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(value, indent=2, sort_keys=True) + "\n", encoding="utf-8")


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def relative(path: Path) -> str:
    return str(path.relative_to(ROOT)).replace("\\", "/")


def paths(index: int) -> dict[str, Path]:
    ordinary = tight.tight_paths(index)
    stem = f"d{index:03d}.far"
    return {
        "ordinary_main": ordinary["main"],
        "ordinary_tail": ordinary["tail"],
        "ordinary_full": ordinary["full"],
        "main": OUTPUT / f"{stem}.mainH.interval.json",
        "main_checkpoint": OUTPUT / f"{stem}.mainH.checkpoint.json",
        "tail": OUTPUT / f"{stem}.tailH.interval.json",
        "full": OUTPUT / f"{stem}.fullH.interval.json",
        "main_note": ROOT
        / "proof_corpus"
        / f"MTT_q79HeightFourD{index:03d}FarCutMainHessianInterval_A380F_v1.md",
        "tail_note": ROOT
        / "proof_corpus"
        / f"MTT_q79HeightFourD{index:03d}FarCutTailHessianInterval_A381QF_v1.md",
        "full_note": ROOT
        / "proof_corpus"
        / f"MTT_q79HeightFourD{index:03d}FarCutFullHessianInterval_A382F_v1.md",
    }


def adapter_authority() -> dict[str, str]:
    source = Path(__file__).resolve()
    return {"path": relative(source), "sha256": sha256(source)}


def promote_packet(path: Path, artifact: str, route: str) -> dict:
    packet = load(path)
    packet["artifact"] = artifact
    packet["far_cut_route"] = {
        "identity": route,
        "canonical_A373_packets_overwritten": False,
        "adapter_authority": adapter_authority(),
    }
    packet["authority"]["far_cut_adapter"] = adapter_authority()
    dump(path, packet)
    return packet


def run_main(arguments: argparse.Namespace, selected: dict[str, Path]) -> dict:
    original = main_hessian.target_paths

    def far_paths(_index: int) -> dict[str, Path]:
        return {
            "canonical_main": selected["ordinary_main"],
            "canonical_full": selected["ordinary_full"],
            "output": selected["main"],
            "checkpoint": selected["main_checkpoint"],
            "note": selected["main_note"],
        }

    main_hessian.target_paths = far_paths
    try:
        packet = main_hessian.execute(
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
        main_hessian.target_paths = original
    packet = promote_packet(
        selected["main"],
        "A380F",
        "same A380 transport from an independently certified farther cutoff",
    )
    selected["main_note"].write_text(
        f"# MTT q79 Height-Four d{arguments.index:03d} Far-Cut Main Hessian (A380F) v1\n\n"
        "A380F runs the unchanged A380 same-source Hessian transport from the "
        "independently certified tight/far ordinary cutoff packet. The canonical "
        "A373 packet is retained unchanged.\n\n"
        f"The selected cutoff is `{packet['selected_target']['endpoint_cutoff_epsilon']}` "
        f"and the maximum Hessian component radius is "
        f"`{packet['summary']['maximum_main_Hessian_component_radius_upper']:.12g}`.\n",
        encoding="utf-8",
    )
    return packet


def run_tail(arguments: argparse.Namespace, selected: dict[str, Path]) -> dict:
    original = tail_hessian.output_paths

    def far_paths(_index: int) -> dict[str, Path]:
        return {
            "main": selected["ordinary_main"],
            "tail": selected["ordinary_tail"],
            "output": selected["tail"],
            "note": selected["tail_note"],
        }

    tail_hessian.output_paths = far_paths
    try:
        quadrature.execute(
            Namespace(
                index=arguments.index,
                dps=arguments.dps,
                order=arguments.tail_order,
                outer_segments=arguments.outer_segments,
                theta_segments=arguments.theta_segments,
                node_width=arguments.node_width,
                series_terms=arguments.series_terms,
            )
        )
    finally:
        tail_hessian.output_paths = original
    packet = promote_packet(
        selected["tail"],
        "A381QF",
        "differentiated A135 quadrature on the matching farther endpoint tail",
    )
    selected["tail_note"].write_text(
        f"# MTT q79 Height-Four d{arguments.index:03d} Far-Cut Tail Hessian (A381QF) v1\n\n"
        "A381QF differentiates the matching tight/far A135 radial/theta tail "
        "certificate. It uses the same cutoff as A380F and leaves the canonical "
        "A373 packet unchanged.\n\n"
        f"The maximum Hessian component radius is "
        f"`{packet['summary']['maximum_tail_Hessian_component_radius_upper']:.12g}`.\n",
        encoding="utf-8",
    )
    return packet


def run_full(arguments: argparse.Namespace, selected: dict[str, Path]) -> dict:
    original = full_hessian.paths

    def far_paths(_index: int) -> dict[str, Path]:
        return {
            "main": selected["main"],
            "tail": selected["tail"],
            "canonical_full": selected["ordinary_full"],
            "output": selected["full"],
            "note": selected["full_note"],
        }

    full_hessian.paths = far_paths
    prior_argv = sys.argv
    try:
        sys.argv = [str(Path(full_hessian.__file__).resolve()), "--index", str(arguments.index)]
        full_hessian.main()
    finally:
        sys.argv = prior_argv
        full_hessian.paths = original
    packet = promote_packet(
        selected["full"],
        "A382F",
        "oriented splice of matching farther-cut A380F and A381QF packets",
    )
    selected["full_note"].write_text(
        f"# MTT q79 Height-Four d{arguments.index:03d} Far-Cut Full Hessian (A382F) v1\n\n"
        "A382F splices the matching far-cut main and tail Hessians with the "
        "preselected thimble orientation and independently replays the far-cut "
        "ordinary full interval.\n\n"
        f"The maximum full-Hessian component radius is "
        f"`{packet['summary']['maximum_full_Hessian_component_radius_upper']:.12g}`.\n",
        encoding="utf-8",
    )
    return packet


def parser() -> argparse.ArgumentParser:
    value = argparse.ArgumentParser()
    value.add_argument("--index", type=int, required=True)
    value.add_argument("--phase", choices=("main", "tail", "full", "all"), default="all")
    value.add_argument("--dps", type=int, default=100)
    value.add_argument("--main-order", type=int, default=20)
    value.add_argument("--tail-order", type=int, default=24)
    value.add_argument("--maximum-step", type=float, default=0.003)
    value.add_argument("--minimum-step", type=float, default=1.0e-10)
    value.add_argument("--maximum-steps", type=int, default=50000)
    value.add_argument("--maximum-lift-correction", type=float, default=1.0e-6)
    value.add_argument("--maximum-output-increment", type=float, default=2.0e-3)
    value.add_argument("--maximum-output-radius", type=float, default=0.25)
    value.add_argument("--outer-segments", type=int, default=64)
    value.add_argument("--theta-segments", type=int, default=64)
    value.add_argument("--node-width", type=float, default=1.0e-10)
    value.add_argument("--series-terms", type=int, default=10)
    value.add_argument("--resume", action="store_true")
    return value


def main() -> int:
    arguments = parser().parse_args()
    if not 1 <= arguments.index <= 90:
        raise ValueError("index must lie in [1,90]")
    ctx.dps = arguments.dps
    selected = paths(arguments.index)
    required = {
        "main": ("ordinary_main",),
        "tail": ("ordinary_main", "ordinary_tail"),
        "full": ("ordinary_full", "main", "tail"),
        "all": ("ordinary_main", "ordinary_tail", "ordinary_full"),
    }[arguments.phase]
    for name in required:
        if not selected[name].exists():
            raise FileNotFoundError(selected[name])
    if arguments.phase in {"main", "all"}:
        run_main(arguments, selected)
    if arguments.phase in {"tail", "all"}:
        run_tail(arguments, selected)
    if arguments.phase in {"full", "all"}:
        run_full(arguments, selected)
    print(f"{ARTIFACT}: d{arguments.index:03d} phase={arguments.phase} complete")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
