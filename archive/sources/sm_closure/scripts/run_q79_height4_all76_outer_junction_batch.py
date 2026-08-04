from __future__ import annotations

import argparse
import hashlib
import json
import os
import platform
import subprocess
import sys
import time
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
VALIDATED = (
    ROOT
    / "candidate_data"
    / "selected_q79covariantperiodbranchcutsetandtightbetatransport"
    / "selected_alignment_thimble_periods"
    / "covariant_floating_probe"
    / "validated_transport"
)
DIRECTORY = VALIDATED / "ol"
A413 = DIRECTORY / "all76.a413.json"
A412 = DIRECTORY / "d057.a412.json"
OUTER_BUILDER = ROOT / "scripts" / "run_q79_height4_outer_leg_from_a413.py"
OUTER_AUDIT = ROOT / "proof_corpus" / "selected_q79heightfoura413outerleg_audit.py"
COMPOSER = ROOT / "scripts" / "build_q79_height4_a414_junction_path_composition.py"
COMPOSITION_AUDIT = (
    ROOT / "proof_corpus" / "selected_q79heightfoura414junctionpathcomposition_audit.py"
)
A412_AUDIT = ROOT / "proof_corpus" / "selected_q79d057fulljunctionpathcomposition_audit.py"
# Keep the atomic temporary path below the legacy Windows MAX_PATH boundary.
CHECKPOINT = DIRECTORY / "b416.json"


def load(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def relative(path: Path) -> str:
    return str(path.relative_to(ROOT)).replace("\\", "/")


def atomic_dump(path: Path, value: dict) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    temporary = path.with_suffix(path.suffix + ".tmp")
    temporary.write_text(json.dumps(value, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    os.replace(temporary, path)


def parse_indices(value: str) -> list[int]:
    if not value.strip():
        return []
    indices = [int(item.strip()) for item in value.split(",") if item.strip()]
    if len(indices) != len(set(indices)):
        raise ValueError("batch indices must be unique")
    return indices


def run(command: list[str], *, allow_failure: bool = False) -> bool:
    print(f"RUN {json.dumps(command)}", flush=True)
    result = subprocess.run(command, cwd=ROOT, check=False)
    if result.returncode and not allow_failure:
        raise subprocess.CalledProcessError(result.returncode, command)
    return result.returncode == 0


def target_paths(index: int) -> dict[str, Path]:
    return {
        "outer": DIRECTORY / f"d{index:03d}.a414.json",
        "outer_checkpoint": DIRECTORY / f"d{index:03d}.a414.ckpt.json",
        "composition": DIRECTORY / f"d{index:03d}.a415.json",
    }


def target_is_current(index: int) -> bool:
    paths = target_paths(index)
    if not all(path.is_file() for path in paths.values()):
        return False
    return run(
        [sys.executable, str(OUTER_AUDIT), "--index", str(index)],
        allow_failure=True,
    ) and run(
        [sys.executable, str(COMPOSITION_AUDIT), "--index", str(index)],
        allow_failure=True,
    )


def configuration(arguments: argparse.Namespace) -> dict:
    authorities = {
        "A413": A413,
        "outer_builder": OUTER_BUILDER,
        "outer_audit": OUTER_AUDIT,
        "composer": COMPOSER,
        "composition_audit": COMPOSITION_AUDIT,
        "A412_audit": A412_AUDIT,
        "batch_source": Path(__file__).resolve(),
    }
    return {
        "authorities": {
            label: {"path": relative(path), "sha256": sha256(path)}
            for label, path in authorities.items()
        },
        "main_dps": arguments.main_dps,
        "order": arguments.order,
        "initial_step": arguments.initial_step,
        "maximum_step": arguments.maximum_step,
        "minimum_step": arguments.minimum_step,
        "maximum_lift_correction": arguments.maximum_lift_correction,
        "maximum_integral_radius": arguments.maximum_integral_radius,
        "python": sys.version,
        "platform": platform.platform(),
    }


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--indices", default="")
    parser.add_argument("--limit", type=int, default=0)
    parser.add_argument("--main-dps", type=int, default=100)
    parser.add_argument("--order", type=int, default=32)
    parser.add_argument("--initial-step", type=float, default=1.0e-4)
    parser.add_argument("--maximum-step", type=float, default=0.003)
    parser.add_argument("--minimum-step", type=float, default=1.0e-12)
    parser.add_argument("--maximum-lift-correction", type=float, default=1.0e-10)
    parser.add_argument("--maximum-integral-radius", type=float, default=1.0e-4)
    parser.add_argument("--restart-targets", default="")
    parser.add_argument("--restart-batch", action="store_true")
    arguments = parser.parse_args()
    if arguments.limit < 0:
        raise ValueError("--limit must be nonnegative")

    manifest = load(A413)
    rows = manifest["target_rows"]
    supported = {int(row["distinguished_index"]): row for row in rows}
    if len(supported) != 76:
        raise AssertionError("A413 support is no longer 76 targets")
    requested = parse_indices(arguments.indices)
    if requested:
        missing = sorted(set(requested) - set(supported))
        if missing:
            raise ValueError(f"indices are outside A413 support: {missing}")
        ordered = [supported[index] for index in requested]
    else:
        ordered = sorted(
            rows,
            key=lambda row: (
                float(row["outward_radial_ratio"]),
                int(row["distinguished_index"]),
            ),
        )
    if arguments.limit:
        ordered = ordered[: arguments.limit]
    restart_targets = set(parse_indices(arguments.restart_targets))

    config = configuration(arguments)
    if arguments.restart_batch and CHECKPOINT.exists():
        CHECKPOINT.unlink()
    if CHECKPOINT.exists():
        progress = load(CHECKPOINT)
        if progress.get("configuration") != config:
            raise ValueError("all-76 batch checkpoint configuration or authority changed")
        progress["requested_indices"] = sorted(
            set(int(value) for value in progress.get("requested_indices", []))
            | {int(row["distinguished_index"]) for row in ordered}
        )
        progress["status"] = "RUNNING_NOT_A_THEOREM_CERTIFICATE"
        progress.pop("finished_unix", None)
    else:
        progress = {
            "schema": "MTTQ79HeightFourAll76OuterJunctionBatchCheckpoint.v1",
            "status": "RUNNING_NOT_A_THEOREM_CERTIFICATE",
            "configuration": config,
            "started_unix": time.time(),
            "requested_indices": [int(row["distinguished_index"]) for row in ordered],
            "completed": {},
        }
    progress.setdefault("invocations", []).append(
        {
            "started_unix": time.time(),
            "indices": [int(row["distinguished_index"]) for row in ordered],
        }
    )
    atomic_dump(CHECKPOINT, progress)

    completed = progress["completed"]
    for position, contract in enumerate(ordered, start=1):
        index = int(contract["distinguished_index"])
        key = f"d{index:03d}"
        print(
            f"TARGET {position}/{len(ordered)} {key} native-{contract['line_chart']} "
            f"radial_ratio={float(contract['outward_radial_ratio']):.12g}",
            flush=True,
        )
        if index == 57:
            if not A412.is_file():
                raise FileNotFoundError("the separately certified d057 A412 packet is missing")
            run([sys.executable, str(A412_AUDIT)])
            packet = load(A412)
            completed[key] = {
                "artifact": "A412",
                "path": relative(A412),
                "sha256": sha256(A412),
                "summary": packet["summary"],
                "verified": True,
            }
            progress["last_completed_index"] = index
            atomic_dump(CHECKPOINT, progress)
            continue

        if index not in restart_targets and target_is_current(index):
            print(f"SKIP {key}: current A414/A415 audits pass", flush=True)
        else:
            command = [
                sys.executable,
                str(OUTER_BUILDER),
                "--index",
                str(index),
                "--main-dps",
                str(arguments.main_dps),
                "--order",
                str(arguments.order),
                "--initial-step",
                format(arguments.initial_step, ".17g"),
                "--maximum-step",
                format(arguments.maximum_step, ".17g"),
                "--minimum-step",
                format(arguments.minimum_step, ".17g"),
                "--maximum-lift-correction",
                format(arguments.maximum_lift_correction, ".17g"),
                "--maximum-integral-radius",
                format(arguments.maximum_integral_radius, ".17g"),
            ]
            if index in restart_targets:
                command.append("--restart")
            run(command)
            run([sys.executable, str(OUTER_AUDIT), "--index", str(index)])
            run([sys.executable, str(COMPOSER), "--index", str(index)])
            run([sys.executable, str(COMPOSITION_AUDIT), "--index", str(index)])

        paths = target_paths(index)
        outer = load(paths["outer"])
        composition = load(paths["composition"])
        completed[key] = {
            "artifact": "A415",
            "outer_path": relative(paths["outer"]),
            "outer_sha256": sha256(paths["outer"]),
            "outer_checkpoint_path": relative(paths["outer_checkpoint"]),
            "outer_checkpoint_sha256": sha256(paths["outer_checkpoint"]),
            "composition_path": relative(paths["composition"]),
            "composition_sha256": sha256(paths["composition"]),
            "outer_summary": {
                "accepted_steps": outer["validated_outer_main_transport"]["accepted_step_count"],
                "rejected_steps": outer["validated_outer_main_transport"]["rejected_step_count"],
                "maximum_radius": outer["validated_outer_main_transport"]["uniform_integral_radius_upper"],
            },
            "composition_summary": composition["summary"],
            "verified": True,
        }
        progress["last_completed_index"] = index
        progress["completed_count"] = len(completed)
        atomic_dump(CHECKPOINT, progress)

    progress["finished_unix"] = time.time()
    progress["completed_count"] = len(completed)
    progress["status"] = (
        "ALL_76_EXECUTIONS_AUDITED_PENDING_AGGREGATE_FINALIZER"
        if len(completed) == 76
        else "REQUESTED_SUBSET_EXECUTED_AND_AUDITED"
    )
    atomic_dump(CHECKPOINT, progress)
    print(
        json.dumps(
            {
                "checkpoint": relative(CHECKPOINT),
                "completed_count": len(completed),
                "status": progress["status"],
            },
            indent=2,
        ),
        flush=True,
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
