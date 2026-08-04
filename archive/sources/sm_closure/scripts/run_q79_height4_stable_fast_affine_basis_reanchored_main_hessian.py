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
    value.add_argument("--checkpoint", type=Path, required=True)
    value.add_argument("--reanchor-certificate", type=Path, required=True)
    value.add_argument("--canonical-main", type=Path, required=True)
    value.add_argument("--canonical-full", type=Path)
    value.add_argument("--output", type=Path, required=True)
    value.add_argument("--note", type=Path)
    value.add_argument("--maximum-steps", type=int, default=50000)
    return value


def main() -> int:
    arguments = parser().parse_args()
    for name in (
        "checkpoint",
        "reanchor_certificate",
        "canonical_main",
        "canonical_full",
        "output",
        "note",
    ):
        path = getattr(arguments, name)
        if path is not None:
            setattr(arguments, name, path.resolve())
    for path in (
        arguments.checkpoint,
        arguments.reanchor_certificate,
        arguments.canonical_main,
    ):
        if not path.is_file():
            raise FileNotFoundError(f"affine-basis continuation input is absent: {path}")

    checkpoint = base.load(arguments.checkpoint)
    if checkpoint.get("schema") != "MTTQ79ReverseTargetMainHessianCheckpoint.v1":
        raise ValueError("affine-basis continuation requires a reverse checkpoint")
    config = checkpoint["configuration"]
    if int(config["index"]) != arguments.index:
        raise AssertionError("affine-basis continuation target changed")
    reanchor = checkpoint.get("affine_chain_basis_reanchor")
    if not reanchor or not reanchor.get(
        "five_coordinate_lift_replaced_by_selected_affine_basis_enclosure", False
    ):
        raise AssertionError("checkpoint lacks the selected affine-basis reanchor")
    if reanchor["certificate"] != authority(arguments.reanchor_certificate):
        raise AssertionError("affine-basis reanchor authority changed")
    certificate = base.load(arguments.reanchor_certificate)
    scope = certificate["strict_scope"]
    reanchor_closed = scope.get("smooth_base_affine_reanchor_closed", False) or scope.get(
        "regular_fiber_affine_reanchor_closed", False
    )
    if (
        int(certificate["distinguished_index"]) != arguments.index
        or not reanchor_closed
        or not scope["puncture_at_infinity_coordinate_retained"]
        or not scope["integer_coordinates_selected_by_verified_interval_solve"]
    ):
        raise AssertionError("affine-basis reanchor is not promotion ready")
    if config["canonical_main_sha256"] != base.sha256(arguments.canonical_main):
        raise AssertionError("affine-basis canonical-main authority is stale")

    ordinary_paths = base.target_paths(arguments.index)
    selected = {
        **ordinary_paths,
        "checkpoint": arguments.checkpoint,
        "reverse_checkpoint": arguments.checkpoint,
        "canonical_main": arguments.canonical_main,
        "canonical_full": arguments.canonical_full or ordinary_paths["canonical_full"],
        "output": arguments.output,
        "note": arguments.note
        or ROOT
        / "proof_corpus"
        / f"MTT_q79HeightFourD{arguments.index:03d}AffineBasisMainHessian_A380ABR_v1.md",
        "reverse_note": arguments.note
        or ROOT
        / "proof_corpus"
        / f"MTT_q79HeightFourD{arguments.index:03d}AffineBasisMainHessian_A380ABR_v1.md",
    }
    if not selected["canonical_full"].is_file():
        raise FileNotFoundError("affine-basis continuation lacks canonical full packet")

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
        try:
            packet = reverse.execute(run_arguments)
        except ArithmeticError as error:
            if str(error) == "reverse target Hessian exceeded step budget":
                paused = base.load(arguments.checkpoint)
                paused["affine_chain_basis_reanchor"] = {
                    "certificate": authority(arguments.reanchor_certificate),
                    "same_position_outputs_and_output_radii_retained": True,
                    "five_coordinate_lift_replaced_by_selected_affine_basis_enclosure": True,
                    "provenance_restored_after_checkpoint_write": True,
                }
                base.dump(arguments.checkpoint, paused)
                print(
                    f"staged pause after {arguments.maximum_steps} accepted steps; "
                    f"checkpoint retained at {base.relative(arguments.checkpoint)}"
                )
                return 0
            raise
    finally:
        stable.uninstall()
        fast.uninstall()
        base.configuration = prior_configuration
        base.target_paths = prior_paths

    packet["artifact"] = "A380ABR"
    packet["affine_chain_basis_reanchor"] = authority(
        arguments.reanchor_certificate
    )
    packet["authority"]["affine_basis_reanchored_continuation_runner"] = authority(
        Path(__file__).resolve()
    )
    packet["authority"]["affine_chain_basis_reanchor"] = authority(
        arguments.reanchor_certificate
    )
    packet["strict_scope"]["smooth_base_affine_basis_reanchor_used"] = True
    packet["strict_scope"]["puncture_at_infinity_coordinate_retained"] = True
    packet["strict_scope"]["selected_affine_integer_coordinates_used"] = True
    base.dump(selected["output"], packet)
    print(f"promoted {base.relative(selected['output'])} from affine H1 basis")
    print(json.dumps(packet["summary"], indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
