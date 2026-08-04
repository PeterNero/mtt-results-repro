from __future__ import annotations

import argparse
import concurrent.futures
import json
import subprocess
import sys
import threading
import time
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
PERIOD_DIRECTORY = (
    ROOT
    / "candidate_data"
    / "selected_q79covariantperiodbranchcutsetandtightbetatransport"
    / "selected_alignment_thimble_periods"
)
LOG_DIRECTORY = ROOT / "reports" / "q79_selected_E32_remaining_interval_batch"
PRINT_LOCK = threading.Lock()


def load(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def emit(message: str) -> None:
    with PRINT_LOCK:
        print(message, flush=True)


def source_path(index: int) -> Path:
    rows = list(PERIOD_DIRECTORY.glob(f"d{index:03d}_*.thimble_period.candidate.json"))
    if len(rows) != 1:
        raise AssertionError(f"d{index:03d}: expected one source packet, found {len(rows)}")
    return rows[0]


def packet_paths(index: int) -> dict[str, Path]:
    source = load(source_path(index))
    stem = f"d{index:03d}_{source['root_id']}"
    return {
        "source": source_path(index),
        "nodal": PERIOD_DIRECTORY / f"{stem}.nodal_factor.interval.packet.json",
        "tail": PERIOD_DIRECTORY / f"{stem}.E32_tail.interval.packet.json",
        "scan": PERIOD_DIRECTORY / f"{stem}.E32_detour_scan.packet.json",
        "main": PERIOD_DIRECTORY / f"{stem}.E32_main.interval.packet.json",
        "full": PERIOD_DIRECTORY / f"{stem}.E32_full.interval.packet.json",
        "log": LOG_DIRECTORY / f"{stem}.log",
    }


def valid_packet(path: Path, index: int, keys: tuple[str, ...]) -> bool:
    if not path.exists():
        return False
    try:
        packet = load(path)
        if int(packet.get("distinguished_index", packet.get("selected_thimble", {}).get("distinguished_index", -1))) != index:
            return False
        value = packet
        for key in keys:
            value = value[key]
        return value is True
    except (KeyError, TypeError, ValueError, json.JSONDecodeError):
        return False


def append_log(path: Path, text: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("a", encoding="utf-8") as handle:
        handle.write(text)
        if not text.endswith("\n"):
            handle.write("\n")


def run_logged(index: int, stage: str, args: list[str], log_path: Path, timeout: int) -> None:
    command = [sys.executable, *args]
    append_log(log_path, f"\n=== {stage}: {' '.join(command)} ===\n")
    started = time.monotonic()
    result = subprocess.run(
        command,
        cwd=ROOT,
        text=True,
        stdout=subprocess.PIPE,
        stderr=subprocess.STDOUT,
        timeout=timeout,
        check=False,
    )
    append_log(log_path, result.stdout)
    elapsed = time.monotonic() - started
    if result.returncode != 0:
        tail = "\n".join(result.stdout.splitlines()[-12:])
        raise RuntimeError(
            f"d{index:03d} {stage} failed after {elapsed:.1f}s "
            f"with exit {result.returncode}:\n{tail}"
        )
    emit(f"d{index:03d} {stage} PASS ({elapsed:.1f}s)")


def route_scan(index: int, paths: dict[str, Path]) -> dict:
    if paths["scan"].exists():
        packet = load(paths["scan"])
        if int(packet.get("distinguished_index", -1)) == index and packet.get("ranked_routes"):
            emit(f"d{index:03d} route scan REUSED")
            return packet
    command = [
        sys.executable,
        "scripts/scan_q79_selected_alignment_E32_polygonal_detours.py",
        "--distinguished-index",
        str(index),
        "--limit",
        "5",
    ]
    started = time.monotonic()
    result = subprocess.run(
        command,
        cwd=ROOT,
        text=True,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        timeout=300,
        check=False,
    )
    append_log(paths["log"], f"\n=== route scan: {' '.join(command)} ===\n{result.stdout}{result.stderr}")
    if result.returncode != 0:
        raise RuntimeError(f"d{index:03d} route scan failed: {result.stderr.strip()}")
    packet = json.loads(result.stdout)
    if not packet.get("ranked_routes"):
        raise RuntimeError(f"d{index:03d} route scan emitted no certified route")
    paths["scan"].write_text(json.dumps(packet, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    emit(f"d{index:03d} route scan PASS ({time.monotonic() - started:.1f}s)")
    return packet


def certify(index: int) -> dict:
    paths = packet_paths(index)
    paths["log"].parent.mkdir(parents=True, exist_ok=True)
    emit(f"d{index:03d} START")

    if valid_packet(
        paths["nodal"],
        index,
        ("scope", "nodal_quadratic_times_quartic_factor_closed"),
    ):
        emit(f"d{index:03d} nodal REUSED")
    else:
        try:
            run_logged(
                index,
                "nodal",
                [
                    "scripts/certify_q79_selected_alignment_single_E32_thimble_nodal_factor.py",
                    "--distinguished-index",
                    str(index),
                    "--dps",
                    "100",
                ],
                paths["log"],
                300,
            )
        except RuntimeError:
            emit(f"d{index:03d} nodal DEEP-SEED RETRY")
            run_logged(
                index,
                "nodal-deep-seed",
                [
                    "scripts/certify_q79_selected_alignment_single_E32_thimble_nodal_factor_deep_seed.py",
                    "--distinguished-index",
                    str(index),
                    "--dps",
                    "100",
                ],
                paths["log"],
                300,
            )

    if valid_packet(paths["tail"], index, ("scope", "endpoint_tail_interval_closed")):
        emit(f"d{index:03d} tail REUSED")
    else:
        tail_errors = []
        for segments in (384, 768, 1536, 3072, 6144):
            try:
                run_logged(
                    index,
                    f"tail-{segments}",
                    [
                        "scripts/certify_q79_selected_alignment_single_E32_thimble_tail_interval_node_pair.py",
                        "--distinguished-index",
                        str(index),
                        "--outer-segments",
                        str(segments),
                        "--dps",
                        "100",
                    ],
                    paths["log"],
                    900,
                )
                break
            except RuntimeError as error:
                tail_errors.append(str(error))
                emit(f"d{index:03d} tail-{segments} RETRY")
        else:
            raise RuntimeError("\n".join(tail_errors))

    scan = route_scan(index, paths)
    route = scan["ranked_routes"][0]
    if valid_packet(
        paths["main"],
        index,
        ("scope", "main_homogeneous_Gauss_Manin_segment_interval_closed"),
    ):
        emit(f"d{index:03d} main REUSED")
    else:
        run_logged(
            index,
            "main",
            [
                "scripts/certify_q79_selected_alignment_E32_thimble_polygonal_main_interval_tail_reuse_zonotope.py",
                "--distinguished-index",
                str(index),
                "--dps",
                "100",
                "--order",
                "20",
                "--detour-fraction",
                str(route["detour_fraction"]),
                "--detour-offset",
                str(route["detour_offset"]),
                "--return-fraction",
                str(route["return_fraction"]),
            ],
            paths["log"],
            1800,
        )

    if valid_packet(paths["full"], index, ("scope", "single_full_E32_thimble_interval_closed")):
        emit(f"d{index:03d} full REUSED")
    else:
        run_logged(
            index,
            "full",
            [
                "scripts/build_selected_q79_single_E32_thimble_full_interval.py",
                "--distinguished-index",
                str(index),
            ],
            paths["log"],
            300,
        )

    full = load(paths["full"])
    result = {
        "distinguished_index": index,
        "root_id": load(paths["source"])["root_id"],
        "line_chart": load(paths["source"])["line_chart"],
        "route": route,
        "full_radius": full["full_E32_thimble"]["interval_radius_upper"],
        "center_difference": full["full_E32_thimble"]["floating_candidate_center_difference"],
        "fallback_met": full["A134_radius_ledger"]["fallback_met"],
    }
    emit(f"d{index:03d} COMPLETE radius={float(result['full_radius']):.3e}")
    return result


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Certify the remaining selected q79 E32 single-thimble intervals in parallel."
    )
    parser.add_argument("--predecessor", required=True)
    parser.add_argument("--workers", type=int, default=4)
    parser.add_argument("--include-partial", action="store_true")
    parser.add_argument("--indices", help="optional comma-separated override")
    return parser.parse_args()


def main() -> int:
    arguments = parse_args()
    predecessor = load(ROOT / arguments.predecessor)
    if arguments.indices:
        indices = [int(item) for item in arguments.indices.split(",") if item.strip()]
    else:
        indices = [
            int(row["distinguished_index"])
            for chart in ("y", "z")
            for row in predecessor["clearance_ranked_queues"][chart]
        ]
        if arguments.include_partial:
            indices.extend(
                int(row["distinguished_index"])
                for row in predecessor["partial_interval_diagnostics"]
            )
    if not indices:
        emit("no remaining intervals requested")
        return 0
    LOG_DIRECTORY.mkdir(parents=True, exist_ok=True)
    emit(f"batch START rows={len(indices)} workers={arguments.workers} indices={indices}")
    results = []
    failures = []
    with concurrent.futures.ThreadPoolExecutor(max_workers=arguments.workers) as executor:
        future_by_index = {executor.submit(certify, index): index for index in indices}
        for future in concurrent.futures.as_completed(future_by_index):
            index = future_by_index[future]
            try:
                results.append(future.result())
            except Exception as error:
                failures.append({"distinguished_index": index, "error": str(error)})
                emit(f"d{index:03d} FAILED: {error}")
    summary = {
        "schema": "MTTQ79SelectedE32RemainingIntervalBatch.v1",
        "predecessor": arguments.predecessor,
        "requested_indices": indices,
        "workers": arguments.workers,
        "completed": sorted(results, key=lambda row: indices.index(row["distinguished_index"])),
        "failures": sorted(failures, key=lambda row: indices.index(row["distinguished_index"])),
        "all_requested_intervals_closed": not failures and len(results) == len(indices),
    }
    summary_path = PERIOD_DIRECTORY / "selected_alignment_E32_remaining_interval_batch.packet.json"
    summary_path.write_text(json.dumps(summary, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    emit(
        f"batch COMPLETE passed={len(results)} failed={len(failures)} "
        f"summary={summary_path.relative_to(ROOT)}"
    )
    return 1 if failures else 0


if __name__ == "__main__":
    raise SystemExit(main())
