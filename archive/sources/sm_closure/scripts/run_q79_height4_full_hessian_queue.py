from __future__ import annotations

import argparse
import hashlib
import json
import math
import os
import subprocess
import sys
from pathlib import Path

import build_q79_height4_target_full_hessian_interval as full_hessian
import certify_q79_height4_target_main_hessian_interval as main_hessian
import certify_q79_height4_target_tail_hessian_interval as tail_hessian
import run_q79_height4_tail_hessian_queue as tail_queue


ROOT = Path(__file__).resolve().parents[1]
PREFIX = main_hessian.VALIDATED / "n3.certified76.recomposition.json"
MANIFEST = main_hessian.OUTPUT_DIRECTORY / "fullH.manifest.json"
FAR_ADAPTER = ROOT / "scripts" / "certify_q79_height4_far_cut_target_hessian_interval.py"
FAR_DIRECTORY = main_hessian.OUTPUT_DIRECTORY / "far"


def load(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def dump(path: Path, value: dict) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    temporary = path.with_name(f"{path.name}.{os.getpid()}.tmp")
    temporary.write_text(
        json.dumps(value, indent=2, sort_keys=True) + "\n", encoding="utf-8"
    )
    temporary.replace(path)


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def relative(path: Path) -> str:
    return str(path.relative_to(ROOT)).replace("\\", "/")


def finite_summary(packet: dict, keys: tuple[str, ...]) -> bool:
    summary = packet.get("summary", {})
    return all(
        math.isfinite(float(summary.get(key, math.nan)))
        and float(summary.get(key, math.nan)) >= 0.0
        for key in keys
    )


def authorities_current(packet: dict) -> bool:
    authority = packet.get("authority", {})
    if not authority:
        return False
    for value in authority.values():
        path_value = value.get("path")
        expected = value.get("sha256")
        if not path_value or not expected:
            return False
        path = ROOT / path_value
        if not path.exists() or sha256(path) != expected:
            return False
    return True


def far_paths(index: int) -> dict[str, Path]:
    stem = f"d{index:03d}.far"
    return {
        "main": FAR_DIRECTORY / f"{stem}.mainH.interval.json",
        "tail": FAR_DIRECTORY / f"{stem}.tailH.interval.json",
        "full": FAR_DIRECTORY / f"{stem}.fullH.interval.json",
        "ordinary_main": main_hessian.tight.tight_paths(index)["main"],
        "ordinary_tail": main_hessian.tight.tight_paths(index)["tail"],
        "ordinary_full": main_hessian.tight.tight_paths(index)["full"],
    }


def valid_far(index: int) -> bool:
    selected = far_paths(index)
    if not all(selected[name].exists() for name in ("main", "tail", "full")):
        return False
    try:
        main_packet = load(selected["main"])
        tail_packet = load(selected["tail"])
        full_packet = load(selected["full"])
    except (OSError, json.JSONDecodeError):
        return False
    full_authority = full_packet.get("authority", {})
    return bool(
        main_packet.get("artifact") == "A380F"
        and tail_packet.get("artifact") == "A381QF"
        and full_packet.get("artifact") == "A382F"
        and full_packet.get("schema")
        == "MTTQ79HeightFourTargetFullHessianInterval.v1"
        and int(full_packet.get("selected_target", {}).get("distinguished_index", -1))
        == index
        and full_packet.get("strict_scope", {}).get(
            "target_full_Hessian_interval_closed", False
        )
        is True
        and full_authority.get("A380_main_Hessian", {}).get("sha256")
        == sha256(selected["main"])
        and full_authority.get("A381_tail_Hessian", {}).get("sha256")
        == sha256(selected["tail"])
        and authorities_current(main_packet)
        and authorities_current(tail_packet)
        and authorities_current(full_packet)
        and finite_summary(
            full_packet,
            (
                "maximum_full_row_component_radius_upper",
                "maximum_full_Hessian_component_radius_upper",
                "full_Hessian_product_box_frobenius_radius_upper",
            ),
        )
    )


def far_prerequisites_exist(index: int) -> bool:
    selected = far_paths(index)
    return all(
        selected[name].exists()
        for name in ("ordinary_main", "ordinary_tail", "ordinary_full")
    )


def valid_main(index: int) -> bool:
    path = main_hessian.target_paths(index)["output"]
    if not path.exists():
        return False
    try:
        packet = load(path)
    except (OSError, json.JSONDecodeError):
        return False
    authority = packet.get("authority", {})
    scope = packet.get("strict_scope", {})
    initial_source = packet.get("initial_period_source", {})
    return bool(
        packet.get("schema") == "MTTQ79HeightFourTargetMainHessianInterval.v1"
        and packet.get("artifact") == "A380"
        and scope.get("target_main_Hessian_interval_closed", False) is True
        and scope.get("canonical_cutoff_start_rounding_replayed", False) is True
        and scope.get("full_precision_direct_cut_periods_recomputed", False) is True
        and initial_source.get(
            "canonical_display_intervals_overlap_all_five", False
        )
        is True
        and math.isfinite(
            float(
                initial_source.get(
                    "maximum_full_precision_period_radius_upper", math.nan
                )
            )
        )
        and int(packet.get("selected_target", {}).get("distinguished_index", -1))
        == index
        and authority.get("builder_source", {}).get("sha256")
        == sha256(Path(main_hessian.__file__).resolve())
        and authority.get("A378_Hessian_integrand_source", {}).get("sha256")
        == sha256(main_hessian.A378)
        and authority.get("direct_cut_period_engine", {}).get("sha256")
        == sha256(Path(main_hessian.handle.__file__).resolve())
        and authority.get("cutoff_root_engine", {}).get("sha256")
        == sha256(Path(main_hessian.pilot.__file__).resolve())
        and finite_summary(
            packet,
            (
                "maximum_main_row_component_radius_upper",
                "maximum_main_Hessian_component_radius_upper",
                "main_Hessian_product_box_frobenius_radius_upper",
            ),
        )
    )


def valid_full(index: int) -> bool:
    selected = full_hessian.paths(index)
    path = selected["output"]
    if (
        not valid_main(index)
        or not tail_queue.valid_completed_output(index)
        or not path.exists()
        or not selected["main"].exists()
        or not selected["tail"].exists()
    ):
        return False
    try:
        packet = load(path)
    except (OSError, json.JSONDecodeError):
        return False
    authority = packet.get("authority", {})
    return bool(
        packet.get("schema") == "MTTQ79HeightFourTargetFullHessianInterval.v1"
        and packet.get("artifact") == "A382"
        and packet.get("strict_scope", {}).get(
            "target_full_Hessian_interval_closed", False
        )
        is True
        and int(packet.get("selected_target", {}).get("distinguished_index", -1))
        == index
        and authority.get("builder_source", {}).get("sha256")
        == sha256(Path(full_hessian.__file__).resolve())
        and authority.get("A380_main_Hessian", {}).get("sha256")
        == sha256(selected["main"])
        and authority.get("A381_tail_Hessian", {}).get("sha256")
        == sha256(selected["tail"])
        and finite_summary(
            packet,
            (
                "maximum_full_row_component_radius_upper",
                "maximum_full_Hessian_component_radius_upper",
                "full_Hessian_product_box_frobenius_radius_upper",
            ),
        )
    )


def compatible_checkpoint(
    index: int,
    arguments: argparse.Namespace,
    order: int,
) -> bool:
    path = main_hessian.target_paths(index)["checkpoint"]
    if not path.exists():
        return False
    try:
        checkpoint = load(path)
    except (OSError, json.JSONDecodeError):
        return False
    configuration = checkpoint.get("configuration", {})
    canonical_main = main_hessian.target_paths(index)["canonical_main"]
    if not canonical_main.exists():
        return False
    return bool(
        checkpoint.get("schema") == "MTTQ79TargetMainHessianCheckpoint.v1"
        and configuration.get("index") == index
        and configuration.get("dps") == arguments.dps
        and configuration.get("order") == order
        and configuration.get("maximum_step")
        == format(arguments.maximum_step, ".17g")
        and configuration.get("minimum_step")
        == format(arguments.minimum_step, ".17g")
        and configuration.get("maximum_lift_correction")
        == format(arguments.maximum_lift_correction, ".17g")
        and configuration.get("maximum_output_increment")
        == format(arguments.maximum_output_increment, ".17g")
        and configuration.get("maximum_output_radius")
        == format(arguments.maximum_output_radius, ".17g")
        and configuration.get("canonical_main_sha256") == sha256(canonical_main)
        and configuration.get("builder_source_sha256")
        == sha256(Path(main_hessian.__file__).resolve())
        and configuration.get("A378_sha256") == sha256(main_hessian.A378)
        and configuration.get("triangular_engine_sha256")
        == sha256(Path(main_hessian.beta_hessian.__file__).resolve())
        and configuration.get("validated_engine_sha256")
        == sha256(Path(main_hessian.validated.__file__).resolve())
        and configuration.get("direct_cut_period_engine_sha256")
        == sha256(Path(main_hessian.handle.__file__).resolve())
        and configuration.get("cutoff_root_engine_sha256")
        == sha256(Path(main_hessian.pilot.__file__).resolve())
        and configuration.get("cutoff_start_rounding_convention")
        == "canonical ordinary handle.midpoint replay"
    )


def write_manifest(inventory: list[dict], arguments: argparse.Namespace) -> None:
    rows = []
    for item in inventory:
        index = int(item["distinguished_index"])
        main_path = main_hessian.target_paths(index)["output"]
        tail_path = tail_hessian.output_paths(index)["output"]
        full_path = full_hessian.paths(index)["output"]
        main_complete = valid_main(index)
        tail_complete = tail_queue.valid_completed_output(index)
        standard_full_complete = valid_full(index)
        far_complete = valid_far(index)
        full_complete = standard_full_complete or far_complete
        selected_full_path = far_paths(index)["full"] if far_complete else full_path
        rows.append(
            {
                "A219_profile_priority_rank": int(item["A219_profile_priority_rank"]),
                "distinguished_index": index,
                "main_complete": main_complete,
                "tail_complete": tail_complete,
                "full_complete": full_complete,
                "full_route": (
                    "standard"
                    if standard_full_complete
                    else "far"
                    if far_complete
                    else "open"
                ),
                "main_output": relative(main_path),
                "tail_output": relative(tail_path),
                "full_output": relative(selected_full_path),
                **(
                    {"main_sha256": sha256(main_path)} if main_complete else {}
                ),
                **(
                    {"tail_sha256": sha256(tail_path)} if tail_complete else {}
                ),
                **(
                    {
                        "full_sha256": sha256(selected_full_path)
                    }
                    if full_complete
                    else {}
                ),
            }
        )
    counts = {
        name: sum(bool(row[f"{name}_complete"]) for row in rows)
        for name in ("main", "tail", "full")
    }
    dump(
        MANIFEST,
        {
            "schema": "MTTQ79HeightFourFullHessianQueueManifest.v1",
            "status": (
                "ALL_76_FULL_HESSIANS_CERTIFIED"
                if counts["full"] == 76
                else "FULL_HESSIAN_QUEUE_IN_PROGRESS"
            ),
            "configuration": {
                "dps": arguments.dps,
                "order": arguments.order,
                "retry_orders": [
                    int(value.strip())
                    for value in arguments.retry_orders.split(",")
                    if value.strip()
                ],
                "maximum_step": arguments.maximum_step,
                "minimum_step": arguments.minimum_step,
                "maximum_steps": arguments.maximum_steps,
                "maximum_lift_correction": arguments.maximum_lift_correction,
                "maximum_output_increment": arguments.maximum_output_increment,
                "maximum_output_radius": arguments.maximum_output_radius,
                "start_rank": arguments.start_rank,
                "end_rank": arguments.end_rank,
            },
            "certified_counts": counts,
            "remaining_full_count": 76 - counts["full"],
            "targets": rows,
            "authority": {
                "A373_prefix": {"path": relative(PREFIX), "sha256": sha256(PREFIX)},
                "A380_builder": {
                    "path": relative(Path(main_hessian.__file__).resolve()),
                    "sha256": sha256(Path(main_hessian.__file__).resolve()),
                },
                "A380_direct_cut_period_engine": {
                    "path": relative(Path(main_hessian.handle.__file__).resolve()),
                    "sha256": sha256(Path(main_hessian.handle.__file__).resolve()),
                },
                "A380_cutoff_root_engine": {
                    "path": relative(Path(main_hessian.pilot.__file__).resolve()),
                    "sha256": sha256(Path(main_hessian.pilot.__file__).resolve()),
                },
                "A381_queue": {
                    "path": relative(Path(tail_queue.__file__).resolve()),
                    "sha256": sha256(Path(tail_queue.__file__).resolve()),
                },
                "A382_builder": {
                    "path": relative(Path(full_hessian.__file__).resolve()),
                    "sha256": sha256(Path(full_hessian.__file__).resolve()),
                },
                "A380F_A382F_far_cut_adapter": {
                    "path": relative(FAR_ADAPTER),
                    "sha256": sha256(FAR_ADAPTER),
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
    parser.add_argument("--retry-orders", default="12,16,20,24,28")
    parser.add_argument("--maximum-step", type=float, default=0.003)
    parser.add_argument("--minimum-step", type=float, default=1.0e-10)
    parser.add_argument("--maximum-steps", type=int, default=50000)
    parser.add_argument("--maximum-lift-correction", type=float, default=1.0e-6)
    parser.add_argument("--maximum-output-increment", type=float, default=2.0e-3)
    parser.add_argument("--maximum-output-radius", type=float, default=0.25)
    parser.add_argument("--resume", action="store_true")
    parser.add_argument("--reverse", action="store_true")
    parser.add_argument("--main-only", action="store_true")
    parser.add_argument("--full-only", action="store_true")
    parser.add_argument("--manifest-only", action="store_true")
    arguments = parser.parse_args()
    if not 1 <= arguments.start_rank <= arguments.end_rank <= 76:
        raise ValueError("require 1 <= start rank <= end rank <= 76")
    if arguments.main_only and arguments.full_only:
        raise ValueError("--main-only and --full-only are mutually exclusive")
    retry_orders = [
        int(value.strip())
        for value in arguments.retry_orders.split(",")
        if value.strip()
    ]
    if any(order < 2 for order in retry_orders):
        raise ValueError("retry orders must be at least 2")

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
        if valid_far(index):
            print(
                f"fullH rank={rank}/76 d{index:03d} far full certified",
                flush=True,
            )
            continue
        if not arguments.full_only and not valid_main(index):
            orders = [arguments.order] + [
                order for order in retry_orders if order > arguments.order
            ]
            for attempt, order in enumerate(orders, start=1):
                command = [
                    sys.executable,
                    str(Path(main_hessian.__file__).resolve()),
                    "--index",
                    str(index),
                    "--dps",
                    str(arguments.dps),
                    "--order",
                    str(order),
                    "--maximum-step",
                    str(arguments.maximum_step),
                    "--minimum-step",
                    str(arguments.minimum_step),
                    "--maximum-steps",
                    str(arguments.maximum_steps),
                    "--maximum-lift-correction",
                    str(arguments.maximum_lift_correction),
                    "--maximum-output-increment",
                    str(arguments.maximum_output_increment),
                    "--maximum-output-radius",
                    str(arguments.maximum_output_radius),
                ]
                if (
                    attempt == 1
                    and arguments.resume
                    and compatible_checkpoint(index, arguments, order)
                ):
                    command.append("--resume")
                print(
                    f"fullH rank={rank}/76 d{index:03d} main starting "
                    f"order={order} attempt={attempt}/{len(orders)}",
                    flush=True,
                )
                result = subprocess.run(command, cwd=ROOT, check=False)
                if result.returncode == 0 and valid_main(index):
                    break
                print(
                    f"fullH rank={rank}/76 d{index:03d} order={order} failed; "
                    "advancing retry ladder",
                    flush=True,
                )
            if not valid_main(index) and far_prerequisites_exist(index):
                print(
                    f"fullH rank={rank}/76 d{index:03d} standard main failed; "
                    "starting certified far-cut fallback",
                    flush=True,
                )
                result = subprocess.run(
                    [
                        sys.executable,
                        str(FAR_ADAPTER),
                        "--index",
                        str(index),
                        "--phase",
                        "all",
                        "--dps",
                        str(max(arguments.dps, 100)),
                        "--main-order",
                        str(arguments.order),
                        "--maximum-step",
                        str(arguments.maximum_step),
                        "--minimum-step",
                        str(arguments.minimum_step),
                        "--maximum-steps",
                        str(arguments.maximum_steps),
                        "--maximum-lift-correction",
                        str(arguments.maximum_lift_correction),
                        "--maximum-output-increment",
                        str(arguments.maximum_output_increment),
                        "--maximum-output-radius",
                        str(arguments.maximum_output_radius),
                    ],
                    cwd=ROOT,
                    check=False,
                )
                if result.returncode == 0 and valid_far(index):
                    write_manifest(inventory, arguments)
                    continue
            if not valid_main(index):
                raise AssertionError(f"d{index:03d} main failed post-run validation")
            write_manifest(inventory, arguments)
        elif valid_main(index):
            print(f"fullH rank={rank}/76 d{index:03d} main certified", flush=True)

        if arguments.main_only:
            continue
        if not tail_queue.valid_completed_output(index):
            print(
                f"fullH rank={rank}/76 d{index:03d} tail absent; splice deferred",
                flush=True,
            )
            continue
        if not valid_full(index):
            print(f"fullH rank={rank}/76 d{index:03d} splice starting", flush=True)
            subprocess.run(
                [
                    sys.executable,
                    str(Path(full_hessian.__file__).resolve()),
                    "--index",
                    str(index),
                ],
                cwd=ROOT,
                check=True,
            )
            if not valid_full(index):
                raise AssertionError(f"d{index:03d} full failed post-run validation")
            write_manifest(inventory, arguments)
        else:
            print(f"fullH rank={rank}/76 d{index:03d} full certified", flush=True)

    write_manifest(inventory, arguments)
    manifest = load(MANIFEST)
    counts = manifest["certified_counts"]
    print(
        f"fullH queue main={counts['main']}/76 tail={counts['tail']}/76 "
        f"full={counts['full']}/76",
        flush=True,
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
