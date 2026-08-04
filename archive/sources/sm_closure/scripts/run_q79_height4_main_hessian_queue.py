from __future__ import annotations

import argparse
import hashlib
import json
import subprocess
import sys
from pathlib import Path

import certify_q79_height4_target_main_hessian_interval as target


ROOT = Path(__file__).resolve().parents[1]
PREFIX = target.VALIDATED / "n3.certified76.recomposition.json"


def load(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def dump(path: Path, value: dict) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(value, indent=2, sort_keys=True) + "\n", encoding="utf-8")


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def relative(path: Path) -> str:
    return str(path.relative_to(ROOT)).replace("\\", "/")


def valid_completed_output(index: int) -> bool:
    output = target.target_paths(index)["output"]
    if not output.exists():
        return False
    try:
        packet = load(output)
    except (OSError, json.JSONDecodeError):
        return False
    authority = packet.get("authority", {}).get("builder_source", {})
    return bool(
        packet.get("schema") == "MTTQ79HeightFourTargetMainHessianInterval.v1"
        and packet.get("strict_scope", {}).get("target_main_Hessian_interval_closed")
        is True
        and int(packet.get("selected_target", {}).get("distinguished_index", -1))
        == index
        and authority.get("sha256") == sha256(Path(target.__file__).resolve())
    )


def valid_resume_checkpoint(index: int, arguments: argparse.Namespace) -> bool:
    checkpoint = target.target_paths(index)["checkpoint"]
    if not checkpoint.exists():
        return False
    try:
        packet = load(checkpoint)
    except (OSError, json.JSONDecodeError):
        return False
    config = packet.get("configuration", {})
    return bool(
        packet.get("schema") == "MTTQ79TargetMainHessianCheckpoint.v1"
        and int(config.get("index", -1)) == index
        and int(config.get("dps", -1)) == arguments.dps
        and int(config.get("order", -1)) == arguments.order
        and config.get("builder_source_sha256")
        == sha256(Path(target.__file__).resolve())
        and config.get("A378_sha256") == sha256(target.A378)
    )


def manifest_path(arguments: argparse.Namespace) -> Path:
    direction = ".reverse" if arguments.reverse else ""
    return target.OUTPUT_DIRECTORY / (
        f"mainH.manifest.r{arguments.start_rank:02d}-{arguments.end_rank:02d}"
        f"{direction}.json"
    )


def write_manifest(inventory: list[dict], arguments: argparse.Namespace) -> None:
    rows = []
    for item in inventory:
        rank = int(item["A219_profile_priority_rank"])
        if not arguments.start_rank <= rank <= arguments.end_rank:
            continue
        index = int(item["distinguished_index"])
        paths = target.target_paths(index)
        complete = valid_completed_output(index)
        row = {
            "A219_profile_priority_rank": rank,
            "distinguished_index": index,
            "complete": complete,
            "resumable_checkpoint": valid_resume_checkpoint(index, arguments),
            "output": relative(paths["output"]),
            "checkpoint": relative(paths["checkpoint"]),
        }
        if complete:
            packet = load(paths["output"])
            row.update(
                {
                    "output_sha256": sha256(paths["output"]),
                    "maximum_main_Hessian_component_radius_upper": packet[
                        "summary"
                    ]["maximum_main_Hessian_component_radius_upper"],
                }
            )
        rows.append(row)
    completed = sum(row["complete"] for row in rows)
    manifest = manifest_path(arguments)
    dump(
        manifest,
        {
            "schema": "MTTQ79HeightFourMainHessianQueueManifest.v1",
            "status": (
                "SELECTED_MAIN_HESSIAN_RANGE_CERTIFIED"
                if completed == len(rows)
                else "MAIN_HESSIAN_QUEUE_IN_PROGRESS"
            ),
            "configuration": {
                "dps": arguments.dps,
                "order": arguments.order,
                "maximum_step": arguments.maximum_step,
                "start_rank": arguments.start_rank,
                "end_rank": arguments.end_rank,
                "reverse": arguments.reverse,
            },
            "selected_count": len(rows),
            "completed_count": completed,
            "remaining_count": len(rows) - completed,
            "targets": rows,
            "authority": {
                "A373_prefix": {
                    "path": relative(PREFIX),
                    "sha256": sha256(PREFIX),
                },
                "target_builder": {
                    "path": relative(Path(target.__file__).resolve()),
                    "sha256": sha256(Path(target.__file__).resolve()),
                },
                "queue_source": {
                    "path": relative(Path(__file__).resolve()),
                    "sha256": sha256(Path(__file__).resolve()),
                },
            },
        },
    )


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--start-rank", type=int, required=True)
    parser.add_argument("--end-rank", type=int, required=True)
    parser.add_argument("--dps", type=int, default=90)
    parser.add_argument("--order", type=int, default=8)
    parser.add_argument("--maximum-step", type=float, default=0.003)
    parser.add_argument("--reverse", action="store_true")
    parser.add_argument("--manifest-only", action="store_true")
    arguments = parser.parse_args()
    if not 1 <= arguments.start_rank <= arguments.end_rank <= 76:
        raise ValueError("require 1 <= start rank <= end rank <= 76")
    prefix = load(PREFIX)
    inventory = prefix["certified_targets_in_A219_priority_order"]
    if len(inventory) != 76:
        raise AssertionError("A373 target inventory is not 76 rows")
    write_manifest(inventory, arguments)
    if arguments.manifest_only:
        print(f"wrote {relative(manifest_path(arguments))}")
        return 0

    selected = [
        row
        for row in inventory
        if arguments.start_rank
        <= int(row["A219_profile_priority_rank"])
        <= arguments.end_rank
    ]
    if arguments.reverse:
        selected.reverse()
    for row in selected:
        rank = int(row["A219_profile_priority_rank"])
        index = int(row["distinguished_index"])
        if valid_completed_output(index):
            print(f"mainH rank={rank}/76 d{index:03d} already certified", flush=True)
            continue
        paths = target.target_paths(index)
        if not paths["canonical_main"].exists():
            raise FileNotFoundError(
                f"d{index:03d} canonical main interval is absent"
            )
        command = [
            sys.executable,
            str(Path(target.__file__).resolve()),
            "--index",
            str(index),
            "--dps",
            str(arguments.dps),
            "--order",
            str(arguments.order),
            "--maximum-step",
            str(arguments.maximum_step),
        ]
        if valid_resume_checkpoint(index, arguments):
            command.append("--resume")
            mode = "resuming"
        else:
            mode = "starting"
        print(f"mainH rank={rank}/76 d{index:03d} {mode}", flush=True)
        subprocess.run(command, cwd=ROOT, check=True)
        if not valid_completed_output(index):
            raise AssertionError(f"d{index:03d} output failed post-run validation")
        write_manifest(inventory, arguments)
        print(f"mainH rank={rank}/76 d{index:03d} certified", flush=True)
    write_manifest(inventory, arguments)
    manifest = load(manifest_path(arguments))
    print(
        f"mainH range complete={manifest['completed_count']}/"
        f"{manifest['selected_count']} remaining={manifest['remaining_count']}",
        flush=True,
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
