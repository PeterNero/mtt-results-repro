from __future__ import annotations

import argparse
import json
from argparse import Namespace
from pathlib import Path

from flint import ctx

import certify_q79_height4_target_main_hessian_interval as base
import q79_fast_taylor_runtime as fast
import q79_stable_affine_hessian_runtime as stable
import run_q79_height4_stable_fast_reverse_target_main_hessian as reverse


ROOT = Path(__file__).resolve().parents[1]


def authority(path: Path) -> dict[str, str]:
    return {"path": base.relative(path), "sha256": base.sha256(path)}


def parser() -> argparse.ArgumentParser:
    value = argparse.ArgumentParser()
    value.add_argument("--index", type=int, required=True)
    value.add_argument("--direction", choices=("forward", "reverse"), required=True)
    value.add_argument("--checkpoint", type=Path, required=True)
    value.add_argument("--reanchor-certificate", type=Path, action="append", required=True)
    value.add_argument("--canonical-main", type=Path)
    value.add_argument("--canonical-full", type=Path)
    value.add_argument("--output", type=Path)
    value.add_argument("--note", type=Path)
    value.add_argument("--maximum-steps", type=int, default=50000)
    return value


def main() -> int:
    arguments = parser().parse_args()
    arguments.checkpoint = arguments.checkpoint.resolve()
    arguments.reanchor_certificate = [
        path.resolve() for path in arguments.reanchor_certificate
    ]
    for name in ("canonical_main", "canonical_full", "output", "note"):
        path = getattr(arguments, name)
        if path is not None:
            setattr(arguments, name, path.resolve())
    for path in [arguments.checkpoint, *arguments.reanchor_certificate]:
        if not path.is_file():
            raise FileNotFoundError(f"reanchored continuation input is absent: {path}")

    checkpoint = base.load(arguments.checkpoint)
    expected_schema = (
        "MTTQ79TargetMainHessianCheckpoint.v1"
        if arguments.direction == "forward"
        else "MTTQ79ReverseTargetMainHessianCheckpoint.v1"
    )
    if checkpoint.get("schema") != expected_schema:
        raise ValueError("checkpoint direction/schema mismatch")
    config = checkpoint["configuration"]
    if int(config["index"]) != arguments.index:
        raise AssertionError("reanchored checkpoint target changed")
    reanchor = checkpoint.get("direct_period_reanchor")
    if not reanchor or not reanchor.get(
        "five_coordinate_lift_replaced_by_unique_overlapping_direct_enclosure", False
    ):
        raise AssertionError("checkpoint does not carry a certified direct-period reanchor")
    latest_certificate = arguments.reanchor_certificate[-1]
    if reanchor["certificate"] != authority(latest_certificate):
        raise AssertionError("checkpoint reanchor certificate authority changed")
    for certificate_path in arguments.reanchor_certificate:
        certificate = base.load(certificate_path)
        if not certificate["strict_scope"]["interior_direct_period_reanchor_closed"]:
            raise AssertionError("reanchor history contains an open certificate")
        if int(certificate["distinguished_index"]) != arguments.index:
            raise AssertionError("reanchor history target changed")

    ordinary_paths = base.target_paths(arguments.index)
    selected = {
        **ordinary_paths,
        "checkpoint": arguments.checkpoint,
        "reverse_checkpoint": arguments.checkpoint,
        "canonical_main": arguments.canonical_main or ordinary_paths["canonical_main"],
        "canonical_full": arguments.canonical_full or ordinary_paths["canonical_full"],
        "output": arguments.output or ordinary_paths["output"],
        "note": arguments.note
        or ROOT
        / "proof_corpus"
        / f"MTT_q79HeightFourD{arguments.index:03d}ReanchoredMainHessian_A380DRF_v1.md",
        "reverse_note": arguments.note
        or ROOT
        / "proof_corpus"
        / f"MTT_q79HeightFourD{arguments.index:03d}ReanchoredReverseMainHessian_A380DRR_v1.md",
    }
    for name in ("canonical_main", "canonical_full"):
        if not selected[name].is_file():
            raise FileNotFoundError(f"reanchored continuation lacks {name}")
    if config["canonical_main_sha256"] != base.sha256(selected["canonical_main"]):
        raise AssertionError("reanchored continuation canonical-main authority is stale")

    run_arguments = Namespace(
        index=arguments.index,
        dps=int(config["dps"]),
        order=int(config["order"]),
        maximum_step=float(config["maximum_step"]),
        minimum_step=float(config["minimum_step"]),
        maximum_steps=arguments.maximum_steps,
        maximum_lift_correction=float(config["maximum_lift_correction"]),
        maximum_output_increment=float(config["maximum_output_increment"]),
        maximum_output_radius=float(config["maximum_output_radius"]),
        resume=True,
        smoke_only=False,
    )
    ctx.dps = run_arguments.dps
    prior_paths = base.target_paths
    prior_configuration = base.configuration

    def accelerated_configuration(*args, **kwargs) -> dict:
        value = prior_configuration(*args, **kwargs)
        value["C_backed_Taylor_runtime_sha256"] = base.sha256(
            Path(fast.__file__).resolve()
        )
        value["C_backed_Taylor_equivalence_audit_sha256"] = base.sha256(
            reverse.FAST_AUDIT
        )
        value["stable_affine_Hessian_runtime_sha256"] = base.sha256(
            Path(stable.__file__).resolve()
        )
        value["stable_affine_Hessian_inclusion_audit_sha256"] = base.sha256(
            reverse.STABLE_AUDIT
        )
        return value

    base.target_paths = lambda _index: selected
    base.configuration = accelerated_configuration
    fast.install()
    stable.install()
    try:
        if arguments.direction == "forward":
            packet = base.execute(run_arguments)
        else:
            packet = reverse.execute(run_arguments)
    finally:
        stable.uninstall()
        fast.uninstall()
        base.configuration = prior_configuration
        base.target_paths = prior_paths

    packet["artifact"] = "A380DRF" if arguments.direction == "forward" else "A380DRR"
    packet["direct_period_reanchor_history"] = [
        authority(path) for path in arguments.reanchor_certificate
    ]
    packet["authority"]["reanchored_continuation_runner"] = authority(
        Path(__file__).resolve()
    )
    for index, path in enumerate(arguments.reanchor_certificate, start=1):
        packet["authority"][f"direct_period_reanchor_{index:03d}"] = authority(path)
    packet["strict_scope"]["interior_direct_period_reanchor_used"] = True
    packet["strict_scope"]["all_reanchor_sources_same_selected_branch"] = True
    base.dump(selected["output"], packet)
    print(
        f"promoted {base.relative(selected['output'])} after "
        f"{len(arguments.reanchor_certificate)} certified direct-period reanchor(s)"
    )
    print(json.dumps(packet["summary"], indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
