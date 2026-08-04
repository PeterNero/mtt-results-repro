from __future__ import annotations

import argparse
import concurrent.futures
import hashlib
import json
import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
PATHS = (
    ROOT
    / "candidate_data"
    / "selected_q79genus2basedpathsystemandmonodromycandidate"
    / "certified_based_meridian_and_handle_paths.packet.json"
)
OUTPUT = (
    ROOT
    / "candidate_data"
    / "selected_q79genus2localroottrajectoryexecution"
)
BATCH = OUTPUT / "local_trajectory_batch.packet.json"
WORKER = ROOT / "scripts" / "explore_q79genus2localmonodromytrajectory.py"


def load(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


FALLBACK_ROOT_IDS = {"a34", "a41"}


def valid_existing(root_id: str) -> dict | None:
    packet_path = OUTPUT / f"{root_id}.trajectory.packet.json"
    if not packet_path.exists():
        return None
    packet = load(packet_path)
    trajectory = packet.get("trajectory")
    if not trajectory:
        return None
    trajectory_path = ROOT / trajectory["path"]
    if not trajectory_path.exists() or sha256(trajectory_path) != trajectory["sha256"]:
        return None
    if not packet["homology"]["matches_A113_candidate_matrix"]:
        return None
    expected_fragment = "(-1.0+0.0i)" if root_id in FALLBACK_ROOT_IDS else "(0.0+0.0i)"
    if expected_fragment not in packet["branch_chart"]["coordinate"]:
        return None
    if not packet["authority"].get("branch_chart_transition_sha256"):
        return None
    return packet


def run_root(root_id: str, step_ratio: float, force: bool) -> tuple[str, dict, bool]:
    existing = None if force else valid_existing(root_id)
    if existing is not None:
        return root_id, existing, True
    omitted_real = "-1" if root_id in FALLBACK_ROOT_IDS else "0"
    result = subprocess.run(
        [
            sys.executable,
            str(WORKER),
            "--root-id",
            root_id,
            "--omitted-real",
            omitted_real,
            "--omitted-imag",
            "0",
            "--step-ratio",
            format(step_ratio, ".17g"),
        ],
        cwd=ROOT,
        capture_output=True,
        text=True,
    )
    if result.returncode != 0:
        raise RuntimeError(
            f"{root_id} failed\nstdout:\n{result.stdout}\nstderr:\n{result.stderr}"
        )
    packet = valid_existing(root_id)
    if packet is None:
        raise AssertionError(f"{root_id} did not emit a valid trajectory packet")
    return root_id, packet, False


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--jobs", type=int, default=4)
    parser.add_argument("--start", type=int, default=0)
    parser.add_argument("--limit", type=int, default=None)
    parser.add_argument("--step-ratio", type=float, default=0.16)
    parser.add_argument("--force", action="store_true")
    args = parser.parse_args()
    paths = load(PATHS)
    root_ids = [row["root_id"] for row in paths["positive_based_meridians"]]
    stop = len(root_ids) if args.limit is None else min(len(root_ids), args.start + args.limit)
    selected = root_ids[args.start:stop]
    if not selected:
        raise AssertionError("empty root-id batch")
    OUTPUT.mkdir(parents=True, exist_ok=True)

    completed: dict[str, dict] = {}
    with concurrent.futures.ThreadPoolExecutor(max_workers=args.jobs) as executor:
        futures = {
            executor.submit(run_root, root_id, args.step_ratio, args.force): root_id
            for root_id in selected
        }
        for future in concurrent.futures.as_completed(futures):
            root_id, packet, reused = future.result()
            completed[root_id] = packet
            print(
                f"{root_id}: {'reused' if reused else 'computed'} "
                f"samples={packet['transport']['saved_sample_count']} "
                f"solves={packet['transport']['root_solve_count']} "
                f"word={packet['braid']['raw_length']}",
                flush=True,
            )

    all_packets = [valid_existing(root_id) for root_id in root_ids]
    complete_packets = [packet for packet in all_packets if packet is not None]
    payload = {
        "schema": "MTTQ79GenusTwoLocalTrajectoryBatch.v1",
        "status": (
            "ALL_90_ZERO_CHART_LOCAL_TRAJECTORIES_COMPUTED_TUBES_OPEN"
            if len(complete_packets) == 90
            else "PARTIAL_ZERO_CHART_LOCAL_TRAJECTORY_BATCH"
        ),
        "authority": {
            "paths_sha256": sha256(PATHS),
            "worker_sha256": sha256(WORKER),
        },
        "branch_chart": {
            "primary_coordinate": "s_0=1/t for 88 paths",
            "fallback_coordinate": "s_minus1=1/(t+1) for a34 and a41",
            "marking_transport": "M_old=P^(-1)*M_target*P",
            "step_to_root_separation_thresholds_used": sorted(
                {
                    packet["transport"]["step_to_root_separation_threshold"]
                    for packet in complete_packets
                }
            ),
        },
        "counts": {
            "root_ids_available": 90,
            "trajectory_packets_complete": len(complete_packets),
            "A113_matrix_matches": sum(
                packet["homology"]["matches_A113_candidate_matrix"]
                for packet in complete_packets
            ),
            "saved_samples_total": sum(
                packet["transport"]["saved_sample_count"]
                for packet in complete_packets
            ),
            "root_solves_total": sum(
                packet["transport"]["root_solve_count"]
                for packet in complete_packets
            ),
            "raw_braid_generators_total": sum(
                packet["braid"]["raw_length"] for packet in complete_packets
            ),
        },
        "rows": [
            {
                "root_id": packet["root_id"],
                "packet_path": str(
                    (OUTPUT / f"{packet['root_id']}.trajectory.packet.json").relative_to(ROOT)
                ).replace("\\", "/"),
                "packet_sha256": sha256(
                    OUTPUT / f"{packet['root_id']}.trajectory.packet.json"
                ),
                "trajectory_path": packet["trajectory"]["path"],
                "trajectory_sha256": packet["trajectory"]["sha256"],
                "saved_sample_count": packet["transport"]["saved_sample_count"],
                "step_to_root_separation_threshold": packet["transport"][
                    "step_to_root_separation_threshold"
                ],
                "branch_coordinate": packet["branch_chart"]["coordinate"],
                "A113_matrix_match": packet["homology"][
                    "matches_A113_candidate_matrix"
                ],
            }
            for packet in complete_packets
        ],
        "strict_scope": {
            "continuous_local_root_tubes_certified": 0,
            "local_matrices_promoted": 0,
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
