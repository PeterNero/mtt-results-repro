from __future__ import annotations

import argparse
import json
import shutil
import subprocess
import sys
from pathlib import Path

import certify_q79_height4_target_main_hessian_interval as main_hessian


ROOT = Path(__file__).resolve().parents[1]
HESSIAN = main_hessian.OUTPUT_DIRECTORY
QUEUE = HESSIAN / "queue"
MANIFEST = HESSIAN / "precision.manifest.json"


def load(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def command(*arguments: object) -> None:
    rendered = [str(value) for value in arguments]
    print("$ " + " ".join(rendered), flush=True)
    subprocess.run(rendered, cwd=ROOT, check=True)


def target_fraction(checkpoint: dict) -> float:
    config = checkpoint["configuration"]
    start = main_hessian.complex_value(config["start"])
    endpoint = main_hessian.complex_value(config["endpoint"])
    distance = abs(endpoint - start)
    return float(checkpoint["position"]) / distance


def completed_indices() -> set[int]:
    if not MANIFEST.is_file():
        return set()
    packet = load(MANIFEST)
    return {
        int(row["distinguished_index"])
        for row in packet["targets"]
        if row.get("full_budget_pass", False)
    }


def resumable_stage(index: int, checkpoint: Path, certificate: Path) -> bool:
    try:
        checkpoint_packet = load(checkpoint)
        certificate_packet = load(certificate)
    except (OSError, ValueError, TypeError, json.JSONDecodeError):
        return False
    if checkpoint_packet.get("schema") != "MTTQ79ReverseTargetMainHessianCheckpoint.v1":
        return False
    configuration = checkpoint_packet.get("configuration") or {}
    if int(configuration.get("index", -1)) != index:
        return False
    reanchor = checkpoint_packet.get("affine_chain_basis_reanchor") or {}
    if not reanchor.get(
        "five_coordinate_lift_replaced_by_selected_affine_basis_enclosure", False
    ):
        return False
    expected_authority = {
        "path": main_hessian.relative(certificate),
        "sha256": main_hessian.sha256(certificate),
    }
    if reanchor.get("certificate") != expected_authority:
        return False
    scope = certificate_packet.get("strict_scope") or {}
    reanchor_closed = scope.get("smooth_base_affine_reanchor_closed", False) or scope.get(
        "regular_fiber_affine_reanchor_closed", False
    )
    return bool(
        int(certificate_packet.get("distinguished_index", -1)) == index
        and reanchor_closed
        and scope.get("puncture_at_infinity_coordinate_retained", False)
        and scope.get("integer_coordinates_selected_by_verified_interval_solve", False)
    )


def latest_stage(index: int) -> tuple[int, Path, Path] | None:
    rows: list[tuple[int, Path, Path]] = []
    for checkpoint in QUEUE.glob(f"d{index:03d}.affine.s*.rc.json"):
        stem = checkpoint.name.removesuffix(".rc.json")
        try:
            stage = int(stem.rsplit("s", 1)[1])
        except (IndexError, ValueError):
            continue
        certificate = QUEUE / f"d{index:03d}.affine.s{stage}.json"
        if certificate.is_file() and resumable_stage(index, checkpoint, certificate):
            rows.append((stage, checkpoint, certificate))
    selected = max(rows, default=None, key=lambda row: row[0])
    if selected is not None:
        print(
            f"d{index:03d} selected resumable affine stage s{selected[0]}",
            flush=True,
        )
    return selected


def initialize(index: int, dps: int, order: int) -> tuple[int, Path, Path]:
    paths = main_hessian.target_paths(index)
    initial = QUEUE / f"d{index:03d}.initial.json"
    certificate = QUEUE / f"d{index:03d}.affine.s0.json"
    checkpoint = QUEUE / f"d{index:03d}.affine.s0.rc.json"
    command(
        sys.executable,
        "scripts/build_q79_height4_reverse_initial_checkpoint.py",
        "--index",
        index,
        "--canonical-main",
        paths["canonical_main"],
        "--output",
        initial,
        "--dps",
        dps,
        "--order",
        order,
    )
    command(
        sys.executable,
        "scripts/certify_q79_height4_affine_chain_basis_reanchor.py",
        "--index",
        index,
        "--initial-checkpoint",
        initial,
        "--canonical-main",
        paths["canonical_main"],
        "--output",
        certificate,
        "--reanchored-checkpoint",
        checkpoint,
    )
    return 0, checkpoint, certificate


def advance_target(
    index: int,
    *,
    dps: int,
    order: int,
    stage_steps: int,
    maximum_stages: int,
    restart: bool,
) -> dict:
    paths = main_hessian.target_paths(index)
    output = QUEUE / f"d{index:03d}.affine.mainH.json"
    if restart:
        for path in QUEUE.glob(f"d{index:03d}.*"):
            path.unlink()
        output.unlink(missing_ok=True)

    current = latest_stage(index)
    if current is None:
        current = initialize(index, dps, order)
    stage, checkpoint_path, certificate_path = current

    while not output.is_file():
        if stage >= maximum_stages:
            raise ArithmeticError(
                f"d{index:03d} exceeded {maximum_stages} affine reanchor stages"
            )
        checkpoint = load(checkpoint_path)
        accepted = len(checkpoint["accepted_steps"])
        before = target_fraction(checkpoint)
        command(
            sys.executable,
            "scripts/run_q79_height4_stable_fast_affine_basis_reanchored_main_hessian.py",
            "--index",
            index,
            "--checkpoint",
            checkpoint_path,
            "--reanchor-certificate",
            certificate_path,
            "--canonical-main",
            paths["canonical_main"],
            "--canonical-full",
            paths["canonical_full"],
            "--output",
            output,
            "--maximum-steps",
            accepted + stage_steps,
        )
        if output.is_file():
            break
        checkpoint = load(checkpoint_path)
        after = target_fraction(checkpoint)
        print(
            f"d{index:03d} stage {stage}: fraction {before:.12g} -> {after:.12g}",
            flush=True,
        )
        stage += 1
        next_certificate = QUEUE / f"d{index:03d}.affine.s{stage}.json"
        next_checkpoint = QUEUE / f"d{index:03d}.affine.s{stage}.rc.json"
        note = (
            ROOT
            / "proof_corpus"
            / f"MTT_q79HeightFourD{index:03d}InteriorAffineReanchorS{stage}_A380ABI_v1.md"
        )
        command(
            sys.executable,
            "scripts/certify_q79_height4_interior_affine_chain_basis_reanchor_adaptive.py",
            "--index",
            index,
            "--checkpoint",
            checkpoint_path,
            "--canonical-main",
            paths["canonical_main"],
            "--output",
            next_certificate,
            "--reanchored-checkpoint",
            next_checkpoint,
            "--note",
            note,
        )
        checkpoint_path = next_checkpoint
        certificate_path = next_certificate

    packet = load(output)
    if not packet["strict_scope"]["target_main_Hessian_interval_closed"]:
        raise AssertionError(f"d{index:03d} queue output is not a closed main Hessian")
    shutil.copyfile(output, paths["output"])
    command(
        sys.executable,
        "scripts/build_q79_height4_target_full_hessian_interval.py",
        "--index",
        index,
    )
    command(
        sys.executable,
        "scripts/run_q79_height4_precision_hessian_queue.py",
        "--manifest-only",
    )
    full = load(HESSIAN / f"d{index:03d}.fullH.interval.json")
    manifest = load(MANIFEST)
    row = next(
        value
        for value in manifest["targets"]
        if int(value["distinguished_index"]) == index
    )
    result = {
        "distinguished_index": index,
        "accepted_step_count": packet["summary"]["accepted_step_count"],
        "main_Frobenius_radius": packet["summary"][
            "main_Hessian_product_box_frobenius_radius_upper"
        ],
        "weighted_full_Frobenius_radius": full["summary"][
            "selected_chain_Hessian_product_box_frobenius_radius_upper"
        ],
        "full_budget_pass": bool(row["full_budget_pass"]),
        "manifest_full_budget_count": manifest["counts"]["full_budget"],
        "manifest_remaining_count": manifest["remaining_full_budget_count"],
    }
    print(json.dumps(result, indent=2), flush=True)
    return result


def parser() -> argparse.ArgumentParser:
    value = argparse.ArgumentParser()
    value.add_argument("--indices", type=int, nargs="+")
    value.add_argument("--dps", type=int, default=150)
    value.add_argument("--order", type=int, default=48)
    value.add_argument("--stage-steps", type=int, default=40)
    value.add_argument("--maximum-stages", type=int, default=20)
    value.add_argument("--restart", action="store_true")
    value.add_argument("--keep-going", action="store_true")
    return value


def main() -> int:
    arguments = parser().parse_args()
    if arguments.stage_steps < 1 or arguments.maximum_stages < 1:
        raise ValueError("queue stage counts must be positive")
    manifest = load(MANIFEST)
    selected = arguments.indices or [
        int(row["distinguished_index"])
        for row in manifest["targets"]
        if not row.get("full_budget_pass", False)
    ]
    closed = completed_indices()
    results: list[dict] = []
    failures: list[dict] = []
    for index in selected:
        if index in closed and not arguments.restart:
            print(f"d{index:03d} already passes the full budget", flush=True)
            continue
        try:
            result = advance_target(
                index,
                dps=arguments.dps,
                order=arguments.order,
                stage_steps=arguments.stage_steps,
                maximum_stages=arguments.maximum_stages,
                restart=arguments.restart,
            )
            results.append(result)
            if result["full_budget_pass"]:
                closed.add(index)
            elif not arguments.keep_going:
                raise ArithmeticError(f"d{index:03d} full Hessian misses its budget")
        except Exception as error:
            failures.append(
                {
                    "distinguished_index": index,
                    "error": f"{type(error).__name__}: {error}",
                }
            )
            print(json.dumps(failures[-1], indent=2), flush=True)
            if not arguments.keep_going:
                raise
    print(json.dumps({"closed": results, "failures": failures}, indent=2), flush=True)
    return 1 if failures else 0


if __name__ == "__main__":
    raise SystemExit(main())
