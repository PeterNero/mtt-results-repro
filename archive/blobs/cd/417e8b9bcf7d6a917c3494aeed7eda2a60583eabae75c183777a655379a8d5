from __future__ import annotations

import argparse
import json
import subprocess
import sys
from argparse import Namespace
from pathlib import Path

import certify_q79_height4_source_derived_far_cut_hessian_interval as far
import certify_q79_height4_target_main_hessian_interval as main_hessian


ROOT = Path(__file__).resolve().parents[1]


def command(*arguments: object) -> None:
    rendered = [str(value) for value in arguments]
    print("$ " + " ".join(rendered), flush=True)
    subprocess.run(rendered, cwd=ROOT, check=True)


def load(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def target_fraction(checkpoint: dict) -> float:
    config = checkpoint["configuration"]
    start = main_hessian.complex_value(config["start"])
    endpoint = main_hessian.complex_value(config["endpoint"])
    return float(checkpoint["position"]) / abs(endpoint - start)


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--index", type=int, required=True)
    parser.add_argument("--epsilon", type=float, default=1.0e-7)
    parser.add_argument("--dps", type=int, default=150)
    parser.add_argument("--order", type=int, default=48)
    parser.add_argument("--stage-steps", type=int, default=20)
    parser.add_argument("--maximum-stages", type=int, default=20)
    parser.add_argument("--maximum-output-radius", type=float, default=0.005)
    arguments = parser.parse_args()
    if arguments.stage_steps < 1 or arguments.maximum_stages < 1:
        raise ValueError("stage counts must be positive")

    selected = far.paths(arguments.index, arguments.epsilon)
    source = far.ensure_source(
        Namespace(
            index=arguments.index,
            epsilon=arguments.epsilon,
            dps=arguments.dps,
            cut_segments=40,
            cut_tolerance=1.0e-50,
            maximum_period_radius=1.0e-35,
        ),
        selected,
    )
    for name in ("synthetic_main", "ordinary_tail", "canonical_full"):
        if not selected[name].is_file():
            raise FileNotFoundError(f"source-derived affine input is absent: {selected[name]}")

    directory = selected["synthetic_main"].parent
    # Keep filenames short enough for atomic ``.tmp`` writes on legacy Windows paths.
    stem = f"c{arguments.index:02d}"
    initial = directory / f"{stem}.i.json"
    # The reverse runner validates the target index from output.name[1:4].
    output = directory / f"d{arguments.index:03d}.m.json"
    certificate = directory / f"{stem}.s0.json"
    checkpoint = directory / f"{stem}.r0.json"
    note = ROOT / "proof_corpus" / (
        f"MTT_q79HeightFourD{arguments.index:03d}CurrentSourceDerivedAffineMainHessian_A380ABR_v1.md"
    )

    command(
        sys.executable,
        "scripts/build_q79_height4_reverse_initial_checkpoint.py",
        "--index",
        arguments.index,
        "--canonical-main",
        selected["synthetic_main"],
        "--output",
        initial,
        "--dps",
        arguments.dps,
        "--order",
        arguments.order,
        "--maximum-step",
        0.02,
        "--minimum-step",
        1.0e-12,
        "--maximum-lift-correction",
        1.0e-7,
        "--maximum-output-increment",
        1.0e-5,
        "--maximum-output-radius",
        arguments.maximum_output_radius,
    )
    command(
        sys.executable,
        "scripts/certify_q79_height4_affine_chain_basis_reanchor.py",
        "--index",
        arguments.index,
        "--initial-checkpoint",
        initial,
        "--canonical-main",
        selected["synthetic_main"],
        "--output",
        certificate,
        "--reanchored-checkpoint",
        checkpoint,
    )

    stage = 0
    while not output.is_file():
        if stage >= arguments.maximum_stages:
            raise ArithmeticError("source-derived affine queue exceeded its reanchor stages")
        packet = load(checkpoint)
        before = target_fraction(packet)
        command(
            sys.executable,
            "scripts/run_q79_height4_stable_fast_affine_basis_reanchored_main_hessian.py",
            "--index",
            arguments.index,
            "--checkpoint",
            checkpoint,
            "--reanchor-certificate",
            certificate,
            "--canonical-main",
            selected["synthetic_main"],
            "--canonical-full",
            selected["canonical_full"],
            "--output",
            output,
            "--note",
            note,
            "--maximum-steps",
            len(packet["accepted_steps"]) + arguments.stage_steps,
        )
        if output.is_file():
            break
        packet = load(checkpoint)
        after = target_fraction(packet)
        print(
            f"d{arguments.index:03d} source-derived stage {stage}: "
            f"fraction {before:.12g} -> {after:.12g}",
            flush=True,
        )
        stage += 1
        certificate = directory / f"{stem}.s{stage}.json"
        next_checkpoint = directory / f"{stem}.r{stage}.json"
        stage_note = ROOT / "proof_corpus" / (
            f"MTT_q79HeightFourD{arguments.index:03d}CurrentSourceDerivedInteriorAffineS{stage}_A380ABI_v1.md"
        )
        command(
            sys.executable,
            "scripts/certify_q79_height4_interior_affine_chain_basis_reanchor_adaptive.py",
            "--index",
            arguments.index,
            "--checkpoint",
            checkpoint,
            "--canonical-main",
            selected["synthetic_main"],
            "--output",
            certificate,
            "--reanchored-checkpoint",
            next_checkpoint,
            "--note",
            stage_note,
        )
        checkpoint = next_checkpoint

    packet = far.promote(
        output,
        artifact="A380ABR",
        source=selected["source"],
        extra_authority={
            "derived_far_main_replay_source": selected["synthetic_main"],
            "selected_far_tail_interval": selected["ordinary_tail"],
            "canonical_full_interval": selected["canonical_full"],
        },
    )
    packet["strict_scope"]["far_main_replayed_from_full_minus_tail_interval"] = True
    far.dump(output, packet)
    print(json.dumps(packet["summary"], indent=2), flush=True)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
