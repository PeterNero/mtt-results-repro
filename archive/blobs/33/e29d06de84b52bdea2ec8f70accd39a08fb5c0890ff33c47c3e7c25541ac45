from __future__ import annotations

import argparse
import concurrent.futures
import json
import subprocess
import sys
import time
from pathlib import Path

import certify_q79_selected_alignment_E32_primitive_handle_column_interval as column


ROOT = Path(__file__).resolve().parents[1]
SUMMARY = column.PERIOD_DIRECTORY / "selected_alignment_E32_primitive_handle_batch.packet.json"
LOG_DIRECTORY = ROOT / "reports" / "q79_selected_E32_primitive_handle_batch"


def certify(index: int) -> dict:
    output = column.partial_path(index)
    if output.exists():
        packet = json.loads(output.read_text(encoding="utf-8"))
        if packet.get("scope", {}).get("single_primitive_handle_E32_interval_closed"):
            return {
                "column_index": index,
                "label": packet["label"],
                "status": "REUSED",
                "radius": packet["primitive_E32_handle_interval"][
                    "E32_interval_radius_upper"
                ],
            }
    command = [
        sys.executable,
        "scripts/certify_q79_selected_alignment_E32_primitive_handle_column_interval.py",
        "--column-index",
        str(index),
    ]
    started = time.monotonic()
    result = subprocess.run(
        command,
        cwd=ROOT,
        text=True,
        stdout=subprocess.PIPE,
        stderr=subprocess.STDOUT,
        timeout=7200,
        check=False,
    )
    LOG_DIRECTORY.mkdir(parents=True, exist_ok=True)
    (LOG_DIRECTORY / f"column_{index:02d}.log").write_text(
        result.stdout, encoding="utf-8"
    )
    if result.returncode != 0:
        raise RuntimeError(f"column {index} failed with exit {result.returncode}")
    packet = json.loads(output.read_text(encoding="utf-8"))
    return {
        "column_index": index,
        "label": packet["label"],
        "status": "CERTIFIED",
        "wall_seconds": time.monotonic() - started,
        "radius": packet["primitive_E32_handle_interval"][
            "E32_interval_radius_upper"
        ],
    }


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--workers", type=int, default=4)
    arguments = parser.parse_args()
    results = []
    failures = []
    with concurrent.futures.ThreadPoolExecutor(max_workers=arguments.workers) as executor:
        futures = {executor.submit(certify, index): index for index in range(8)}
        for future in concurrent.futures.as_completed(futures):
            index = futures[future]
            try:
                row = future.result()
                results.append(row)
                print(
                    f"column {index} {row['label']} PASS radius={float(row['radius']):.3e}",
                    flush=True,
                )
            except Exception as error:
                failures.append({"column_index": index, "error": str(error)})
                print(f"column {index} FAILED: {error}", flush=True)
    packet = {
        "schema": "MTTQ79SelectedAlignmentE32PrimitiveHandleBatch.v1",
        "workers": arguments.workers,
        "completed": sorted(results, key=lambda row: row["column_index"]),
        "failures": sorted(failures, key=lambda row: row["column_index"]),
        "all_eight_primitive_handle_columns_closed": not failures and len(results) == 8,
    }
    SUMMARY.write_text(json.dumps(packet, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    print(
        f"batch COMPLETE passed={len(results)} failed={len(failures)}",
        flush=True,
    )
    return 1 if failures else 0


if __name__ == "__main__":
    raise SystemExit(main())
