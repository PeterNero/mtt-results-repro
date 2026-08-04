from __future__ import annotations

import argparse
import hashlib
import json
import math
import subprocess
import sys
from pathlib import Path

import certify_q79_height4_target_tail_hessian_interval as target
import certify_q79_height4_target_tail_hessian_quadrature_interval as quadrature


ROOT = Path(__file__).resolve().parents[1]
PREFIX = target.VALIDATED / "n3.certified76.recomposition.json"
MANIFEST = target.OUTPUT_DIRECTORY / "tailH.manifest.json"
SOURCE_DERIVED_FAR_ADAPTER = (
    ROOT / "scripts" / "certify_q79_height4_source_derived_far_cut_hessian_interval.py"
)


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
    output = target.output_paths(index)["output"]
    if not output.exists():
        return False
    try:
        packet = load(output)
    except (OSError, json.JSONDecodeError):
        return False
    scope = packet.get("strict_scope", {})
    authority = packet.get("authority", {}).get("builder_source", {})
    artifact = packet.get("artifact")
    summary = packet.get("summary", {})
    finite_summary = all(
        math.isfinite(float(summary.get(key, math.nan)))
        and float(summary.get(key, math.nan)) >= 0.0
        for key in (
            "maximum_tail_row_component_radius_upper",
            "maximum_tail_Hessian_component_radius_upper",
            "tail_Hessian_product_box_frobenius_radius_upper",
        )
    )
    expected_builder = {
        "A381": Path(target.__file__).resolve(),
        "A381Q": Path(quadrature.__file__).resolve(),
        "A381QFF": Path(quadrature.__file__).resolve(),
    }.get(artifact)
    source_route_current = True
    if artifact == "A381QFF":
        adapter = packet.get("authority", {}).get("source_derived_far_adapter", {})
        far_source = packet.get("authority", {}).get("A380FS_far_cut_source", {})
        route = packet.get("source_derived_far_route", {})
        source_route_current = bool(
            SOURCE_DERIVED_FAR_ADAPTER.is_file()
            and adapter
            == {
                "path": relative(SOURCE_DERIVED_FAR_ADAPTER),
                "sha256": sha256(SOURCE_DERIVED_FAR_ADAPTER),
            }
            and route.get("adapter") == adapter
            and route.get("A380FS_source") == far_source
            and packet.get("authority", {}).get("selected_far_tail_interval")
            and packet.get("authority", {}).get("derived_far_main_replay_source")
        )
    return bool(
        packet.get("schema")
        in {
            "MTTQ79HeightFourTargetTailHessianInterval.v1",
            "MTTQ79HeightFourTargetTailHessianQuadratureInterval.v1",
        }
        and (
            scope.get("target_tail_Hessian_interval_closed", False) is True
            or scope.get("target_Frobenius_tail_Hessian_interval_closed", False)
            is True
        )
        and int(packet.get("selected_target", {}).get("distinguished_index", -1))
        == index
        and expected_builder is not None
        and authority.get("sha256") == sha256(expected_builder)
        and source_route_current
        and finite_summary
    )


def write_manifest(inventory: list[dict], arguments: argparse.Namespace) -> None:
    rows = []
    for item in inventory:
        index = int(item["distinguished_index"])
        output = target.output_paths(index)["output"]
        complete = valid_completed_output(index)
        row = {
            "A219_profile_priority_rank": int(item["A219_profile_priority_rank"]),
            "distinguished_index": index,
            "complete": complete,
            "output": relative(output),
        }
        if complete:
            packet = load(output)
            row.update(
                {
                    "output_sha256": sha256(output),
                    "maximum_tail_Hessian_component_radius_upper": packet[
                        "summary"
                    ]["maximum_tail_Hessian_component_radius_upper"],
                }
            )
        rows.append(row)
    completed = sum(row["complete"] for row in rows)
    dump(
        MANIFEST,
        {
            "schema": "MTTQ79HeightFourTailHessianQueueManifest.v1",
            "status": (
                "ALL_76_TAIL_HESSIANS_CERTIFIED"
                if completed == 76
                else "TAIL_HESSIAN_QUEUE_IN_PROGRESS"
            ),
            "configuration": {
                "dps": arguments.dps,
                "order": arguments.order,
                "series_terms": arguments.series_terms,
                "outer_segments": arguments.outer_segments,
                "theta_segments": arguments.theta_segments,
                "node_width": arguments.node_width,
                "start_rank": arguments.start_rank,
                "end_rank": arguments.end_rank,
            },
            "completed_count": completed,
            "remaining_count": 76 - completed,
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
                "quadrature_target_builder": {
                    "path": relative(Path(quadrature.__file__).resolve()),
                    "sha256": sha256(Path(quadrature.__file__).resolve()),
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
    parser.add_argument("--start-rank", type=int, default=1)
    parser.add_argument("--end-rank", type=int, default=76)
    parser.add_argument("--dps", type=int, default=90)
    parser.add_argument("--order", type=int, default=20)
    parser.add_argument("--series-terms", type=int, default=8)
    parser.add_argument("--outer-segments", type=int, default=64)
    parser.add_argument("--theta-segments", type=int, default=64)
    parser.add_argument("--node-width", type=float, default=1.0e-10)
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
        print(f"wrote {relative(MANIFEST)}")
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
            print(f"tailH rank={rank}/76 d{index:03d} already certified", flush=True)
            continue
        canonical = target.output_paths(index)
        if not canonical["main"].exists() or not canonical["tail"].exists():
            print(
                f"tailH rank={rank}/76 d{index:03d} canonical aliases absent; deferred",
                flush=True,
            )
            continue
        command = [
            sys.executable,
            str(Path(quadrature.__file__).resolve()),
            "--index",
            str(index),
            "--dps",
            str(arguments.dps),
            "--order",
            str(arguments.order),
            "--series-terms",
            str(arguments.series_terms),
            "--outer-segments",
            str(arguments.outer_segments),
            "--theta-segments",
            str(arguments.theta_segments),
            "--node-width",
            str(arguments.node_width),
        ]
        print(f"tailH rank={rank}/76 d{index:03d} starting", flush=True)
        subprocess.run(command, cwd=ROOT, check=True)
        if not valid_completed_output(index):
            raise AssertionError(f"d{index:03d} output failed post-run validation")
        write_manifest(inventory, arguments)
        print(f"tailH rank={rank}/76 d{index:03d} certified", flush=True)
    write_manifest(inventory, arguments)
    manifest = load(MANIFEST)
    print(
        f"tailH queue complete={manifest['completed_count']}/76 "
        f"remaining={manifest['remaining_count']}",
        flush=True,
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
