from __future__ import annotations

import concurrent.futures
import json
import subprocess
import sys
import time
from pathlib import Path

import certify_q79_selected_alignment_E32_primitive_handle_basis_intervals as basis
import certify_q79_selected_alignment_E32_survivor_direct_handle_interval as direct


ROOT = Path(__file__).resolve().parents[1]
SUMMARY = basis.PERIOD_DIRECTORY / "selected_alignment_E32_survivor_direct_handle_batch.packet.json"
LOG_DIRECTORY = ROOT / "reports" / "q79_selected_E32_survivor_direct_handle_batch"
TASKS = [(2, "A"), (3, "A"), (4, "A"), (5, "A"), (3, "B")]


def candidate_id(rank: int) -> str:
    packet = basis.load(basis.A208)
    rows = [
        row
        for row in packet["height_four_candidates"]
        if int(row["A132_objective_rank"]) == rank
    ]
    if len(rows) != 1:
        raise AssertionError("A208 survivor rank is not unique")
    return rows[0]["candidate_id"]


def certify(task: tuple[int, str]) -> dict:
    rank, handle_name = task
    output = direct.output_path(rank, handle_name, candidate_id(rank))
    if output.exists():
        packet = basis.load(output)
        if packet.get("scope", {}).get(
            "candidate_specific_direct_handle_E32_interval_closed"
        ):
            return {
                "rank": rank,
                "handle": handle_name,
                "status": "REUSED",
                "radius": packet["direct_handle_interval"][
                    "E32_uniform_component_radius_upper"
                ],
            }
    command = [
        sys.executable,
        "scripts/certify_q79_selected_alignment_E32_survivor_direct_handle_interval.py",
        "--rank",
        str(rank),
        "--handle",
        handle_name,
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
    (LOG_DIRECTORY / f"rank{rank}_{handle_name}.log").write_text(
        result.stdout, encoding="utf-8"
    )
    if result.returncode != 0:
        raise RuntimeError(
            f"rank {rank} {handle_name} failed with exit {result.returncode}"
        )
    packet = basis.load(output)
    return {
        "rank": rank,
        "handle": handle_name,
        "status": "CERTIFIED",
        "wall_seconds": time.monotonic() - started,
        "radius": packet["direct_handle_interval"][
            "E32_uniform_component_radius_upper"
        ],
    }


def main() -> int:
    results = []
    failures = []
    with concurrent.futures.ThreadPoolExecutor(max_workers=4) as executor:
        futures = {executor.submit(certify, task): task for task in TASKS}
        for future in concurrent.futures.as_completed(futures):
            task = futures[future]
            try:
                row = future.result()
                results.append(row)
                print(
                    f"rank {row['rank']} {row['handle']} PASS "
                    f"radius={float(row['radius']):.3e}",
                    flush=True,
                )
            except Exception as error:
                failures.append(
                    {"rank": task[0], "handle": task[1], "error": str(error)}
                )
                print(f"rank {task[0]} {task[1]} FAILED: {error}", flush=True)
    packet = {
        "schema": "MTTQ79SelectedAlignmentE32SurvivorDirectHandleBatch.v1",
        "tasks": [{"rank": rank, "handle": name} for rank, name in TASKS],
        "completed": sorted(results, key=lambda row: (row["rank"], row["handle"])),
        "failures": sorted(failures, key=lambda row: (row["rank"], row["handle"])),
        "all_five_direct_handle_tasks_closed": not failures and len(results) == 5,
    }
    SUMMARY.write_text(json.dumps(packet, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    print(f"batch COMPLETE passed={len(results)} failed={len(failures)}", flush=True)
    return 1 if failures else 0


if __name__ == "__main__":
    raise SystemExit(main())
