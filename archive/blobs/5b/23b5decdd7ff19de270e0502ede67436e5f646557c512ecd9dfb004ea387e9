from __future__ import annotations

import argparse
import concurrent.futures
import hashlib
import json
import subprocess
import sys
from pathlib import Path

import sympy as sp


ROOT = Path(__file__).resolve().parents[1]
FAN = (
    ROOT
    / "candidate_data"
    / "selected_q79genus2distinguishedcutsystemandglobalrelation"
    / "distinguished_radial_fan.packet.json"
)
OUTPUT = (
    ROOT
    / "candidate_data"
    / "selected_q79genus2distinguishedmeridianexecution"
)
BATCH = OUTPUT / "distinguished_trajectory_batch.packet.json"
WORKER = ROOT / "scripts" / "explore_q79genus2distinguishedmeridiantrajectory.py"
DEFAULT_CHART_ATTEMPTS = [(0.0, 0.0), (-1.0, 0.0), (2.0, 3.0)]
PREFERRED_MINUS_ONE_ROOT_IDS = {"a34", "a75"}
REFINED_STEP_ROOT_IDS = {
    "a01",
    "a04",
    "a06",
    "a08",
    "a19",
    "a27",
    "a37",
    "a50",
    "a60",
    "a61",
    "a67",
    "a70",
    "a74",
    "a78",
    "a83",
    "a85",
}


def load(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def packet_path(index: int, root_id: str) -> Path:
    return OUTPUT / f"d{index:03d}_{root_id}.trajectory.packet.json"


def valid_existing(index: int, root_id: str) -> dict | None:
    path = packet_path(index, root_id)
    if not path.exists():
        return None
    packet = load(path)
    if packet.get("root_id") != root_id or packet.get("distinguished_index") != index:
        return None
    if packet["authority"].get("distinguished_fan_sha256") != sha256(FAN):
        return None
    trajectory = packet.get("trajectory")
    if not trajectory:
        return None
    trajectory_path = ROOT / trajectory["path"]
    if not trajectory_path.exists() or sha256(trajectory_path) != trajectory["sha256"]:
        return None
    matrix = sp.Matrix(
        packet["homology"]["integral_picard_lefschetz_matrix_A114_marking"]
    )
    delta = matrix - sp.eye(4)
    if delta.rank() != 1 or delta * delta != sp.zeros(4):
        return None
    permutation = packet["braid"]["final_root_permutation"]
    if sum(value != slot for slot, value in enumerate(permutation)) != 2:
        return None
    return packet


def run_root(
    index: int, root_id: str, step_ratio: float, force: bool
) -> tuple[int, str, dict, bool]:
    existing = None if force else valid_existing(index, root_id)
    if existing is not None:
        return index, root_id, existing, True
    failures: list[str] = []
    chart_attempts = list(DEFAULT_CHART_ATTEMPTS)
    if root_id in PREFERRED_MINUS_ONE_ROOT_IDS:
        chart_attempts = [(-1.0, 0.0), (0.0, 0.0), (2.0, 3.0)]
    for omitted_real, omitted_imag in chart_attempts:
        result = subprocess.run(
            [
                sys.executable,
                str(WORKER),
                "--root-id",
                root_id,
                "--omitted-real",
                format(omitted_real, ".17g"),
                "--omitted-imag",
                format(omitted_imag, ".17g"),
                "--step-ratio",
                format(step_ratio, ".17g"),
            ],
            cwd=ROOT,
            capture_output=True,
            text=True,
        )
        packet = valid_existing(index, root_id) if result.returncode == 0 else None
        if packet is not None:
            return index, root_id, packet, False
        failures.append(
            f"chart=({omitted_real},{omitted_imag}) code={result.returncode}\n"
            f"stdout:\n{result.stdout}\nstderr:\n{result.stderr}"
        )
    raise RuntimeError(f"d{index:03d} {root_id} failed all charts\n" + "\n".join(failures))


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--jobs", type=int, default=4)
    parser.add_argument("--start", type=int, default=0)
    parser.add_argument("--limit", type=int, default=None)
    parser.add_argument("--step-ratio", type=float, default=0.16)
    parser.add_argument("--force", action="store_true")
    args = parser.parse_args()
    fan = load(FAN)
    all_rows = fan["distinguished_positive_meridians"]
    stop = (
        len(all_rows)
        if args.limit is None
        else min(len(all_rows), args.start + args.limit)
    )
    selected = all_rows[args.start:stop]
    if not selected:
        raise AssertionError("empty distinguished-meridian batch")
    OUTPUT.mkdir(parents=True, exist_ok=True)

    with concurrent.futures.ThreadPoolExecutor(max_workers=args.jobs) as executor:
        futures = {
            executor.submit(
                run_root,
                int(row["distinguished_index"]),
                row["root_id"],
                (
                    min(args.step_ratio, 0.08)
                    if row["root_id"] in REFINED_STEP_ROOT_IDS
                    else args.step_ratio
                ),
                args.force,
            ): row
            for row in selected
        }
        for future in concurrent.futures.as_completed(futures):
            index, root_id, packet, reused = future.result()
            print(
                f"d{index:03d} {root_id}: {'reused' if reused else 'computed'} "
                f"chart={packet['branch_chart']['coordinate']} "
                f"samples={packet['transport']['saved_sample_count']} "
                f"word={packet['braid']['raw_length']}",
                flush=True,
            )

    packets = [
        valid_existing(int(row["distinguished_index"]), row["root_id"])
        for row in all_rows
    ]
    complete = [packet for packet in packets if packet is not None]
    payload = {
        "schema": "MTTQ79GenusTwoDistinguishedTrajectoryBatch.v1",
        "status": (
            "ALL_90_DISTINGUISHED_MERIDIAN_TRAJECTORIES_COMPUTED_TUBES_OPEN"
            if len(complete) == 90
            else "PARTIAL_DISTINGUISHED_MERIDIAN_TRAJECTORY_BATCH"
        ),
        "authority": {
            "distinguished_fan_sha256": sha256(FAN),
            "worker_sha256": sha256(WORKER),
        },
        "counts": {
            "distinguished_paths_available": 90,
            "trajectory_packets_complete": len(complete),
            "saved_samples_total": sum(
                packet["transport"]["saved_sample_count"] for packet in complete
            ),
            "root_solves_total": sum(
                packet["transport"]["root_solve_count"] for packet in complete
            ),
            "raw_braid_generators_total": sum(
                packet["braid"]["raw_length"] for packet in complete
            ),
            "branch_charts_used": sorted(
                {packet["branch_chart"]["coordinate"] for packet in complete}
            ),
            "step_to_root_separation_thresholds_used": sorted(
                {
                    packet["transport"]["step_to_root_separation_threshold"]
                    for packet in complete
                }
            ),
        },
        "rows": [
            {
                "distinguished_index": packet["distinguished_index"],
                "root_id": packet["root_id"],
                "packet_path": str(
                    packet_path(
                        packet["distinguished_index"], packet["root_id"]
                    ).relative_to(ROOT)
                ).replace("\\", "/"),
                "packet_sha256": sha256(
                    packet_path(
                        packet["distinguished_index"], packet["root_id"]
                    )
                ),
                "trajectory_path": packet["trajectory"]["path"],
                "trajectory_sha256": packet["trajectory"]["sha256"],
                "branch_chart": packet["branch_chart"]["coordinate"],
                "saved_sample_count": packet["transport"]["saved_sample_count"],
            }
            for packet in complete
        ],
        "strict_scope": {
            "continuous_root_tubes_certified": 0,
            "distinguished_local_matrices_promoted": 0,
            "global_surface_relation_checked": False,
        },
    }
    BATCH.write_text(
        json.dumps(payload, indent=2, sort_keys=True) + "\n", encoding="utf-8"
    )
    print(f"wrote {BATCH}")
    print(json.dumps(payload["counts"], indent=2, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
