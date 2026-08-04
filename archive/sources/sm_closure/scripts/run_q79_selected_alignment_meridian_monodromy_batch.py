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
DIRECTORY = (
    ROOT
    / "candidate_data"
    / "selected_q79covariantperiodbranchcutsetandtightbetatransport"
)
FAN = DIRECTORY / "selected_alignment_distinguished_radial_fan.interval.packet.json"
OUTPUT = DIRECTORY / "selected_alignment_meridian_monodromy"
BATCH = DIRECTORY / "selected_alignment_meridian_monodromy_batch.packet.json"
WORKER = ROOT / "scripts" / "compute_q79_selected_alignment_single_meridian_monodromy.py"
ROOT_TRANSPORT = ROOT / "scripts" / "q79_selected_alignment_genus2_root_transport.py"
COMMON_BRANCH_CHART = "s=1/(t-(2+3i))"


def load(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def packet_path(index: int, root_id: str) -> Path:
    return OUTPUT / f"d{index:03d}_{root_id}.packet.json"


def valid_existing(index: int, root_id: str) -> dict | None:
    path = packet_path(index, root_id)
    if not path.exists():
        return None
    packet = load(path)
    if packet.get("root_id") != root_id or packet.get("distinguished_index") != index:
        return None
    if packet["authority"].get("fan_sha256") != sha256(FAN):
        return None
    if packet["branch_chart"].get("coordinate") != COMMON_BRANCH_CHART:
        return None
    if packet["transport"].get("circle_scale") != "0.10000000000000001":
        return None
    trajectory = packet.get("trajectory")
    if trajectory is None:
        return None
    trajectory_path = ROOT / trajectory["path"]
    if (
        not trajectory_path.exists()
        or sha256(trajectory_path) != trajectory.get("sha256")
    ):
        return None
    expected_samples = packet["transport"]["saved_sample_count"]
    if trajectory.get("array_schema") != {
        "w": [expected_samples],
        "roots": [expected_samples, 6],
        "root_radius_uppers": [expected_samples, 6],
    }:
        return None
    matrix = sp.Matrix(packet["homology"]["integral_picard_lefschetz_matrix"])
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
    result = subprocess.run(
        [
            sys.executable,
            str(WORKER),
            "--root-id",
            root_id,
            "--step-ratio",
            format(step_ratio, ".17g"),
            "--circle-scale",
            "0.1",
        ],
        cwd=ROOT,
        capture_output=True,
        text=True,
    )
    packet = valid_existing(index, root_id) if result.returncode == 0 else None
    if packet is None:
        raise RuntimeError(
            f"d{index:03d} {root_id} failed code={result.returncode}\n"
            f"stdout:\n{result.stdout}\nstderr:\n{result.stderr}"
        )
    return index, root_id, packet, False


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--jobs", type=int, default=4)
    parser.add_argument("--step-ratio", type=float, default=0.14)
    parser.add_argument("--force", action="store_true")
    arguments = parser.parse_args()
    fan = load(FAN)
    rows = fan["distinguished_positive_meridians"]
    if len(rows) != 90:
        raise AssertionError("selected fan path count changed")
    OUTPUT.mkdir(parents=True, exist_ok=True)

    with concurrent.futures.ThreadPoolExecutor(max_workers=arguments.jobs) as executor:
        futures = {
            executor.submit(
                run_root,
                int(row["distinguished_index"]),
                row["root_id"],
                arguments.step_ratio,
                arguments.force,
            ): row
            for row in rows
        }
        for future in concurrent.futures.as_completed(futures):
            index, root_id, packet, reused = future.result()
            print(
                f"d{index:03d} {root_id}: "
                f"{'reused' if reused else 'computed'} "
                f"samples={packet['transport']['saved_sample_count']} "
                f"word={packet['braid']['raw_length']}",
                flush=True,
            )

    packets = [
        valid_existing(int(row["distinguished_index"]), row["root_id"])
        for row in rows
    ]
    if any(packet is None for packet in packets):
        raise AssertionError("selected meridian batch is incomplete")
    complete = [packet for packet in packets if packet is not None]
    matrix_classes: dict[str, int] = {}
    for packet in complete:
        key = json.dumps(
            packet["homology"]["integral_picard_lefschetz_matrix"],
            separators=(",", ":"),
        )
        matrix_classes[key] = matrix_classes.get(key, 0) + 1

    payload = {
        "schema": "MTTQ79SelectedAlignmentMeridianMonodromyBatch.v1",
        "status": "ALL_90_SELECTED_ALIGNMENT_POINTWISE_MONODROMIES_COMPUTED",
        "authority": {
            "fan_sha256": sha256(FAN),
            "worker_sha256": sha256(WORKER),
            "selected_root_transport_sha256": sha256(ROOT_TRANSPORT),
        },
        "common_branch_chart": COMMON_BRANCH_CHART,
        "counts": {
            "distinguished_paths": len(rows),
            "monodromy_packets_complete": len(complete),
            "saved_samples_total": sum(
                packet["transport"]["saved_sample_count"] for packet in complete
            ),
            "root_solves_total": sum(
                packet["transport"]["root_solve_count"] for packet in complete
            ),
            "raw_braid_generators_total": sum(
                packet["braid"]["raw_length"] for packet in complete
            ),
            "distinct_integral_PL_matrices": len(matrix_classes),
        },
        "integral_PL_matrix_multiplicities": [
            {"matrix": json.loads(key), "multiplicity": multiplicity}
            for key, multiplicity in sorted(matrix_classes.items())
        ],
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
                    packet_path(packet["distinguished_index"], packet["root_id"])
                ),
                "trajectory_path": packet["trajectory"]["path"],
                "trajectory_sha256": packet["trajectory"]["sha256"],
                "matrix": packet["homology"][
                    "integral_picard_lefschetz_matrix"
                ],
                "final_root_permutation": packet["braid"][
                    "final_root_permutation"
                ],
            }
            for packet in complete
        ],
        "strict_scope": {
            "pointwise_root_balls_certified": 90,
            "continuous_root_tubes_certified": 0,
            "local_monodromy_matrices_promoted": 0,
            "global_surface_relation_checked": False,
            "period_columns_emitted": 0,
            "observed_SM_values_used": False,
        },
    }
    BATCH.write_text(
        json.dumps(payload, indent=2, sort_keys=True) + "\n",
        encoding="utf-8",
    )
    print(f"wrote {BATCH.relative_to(ROOT)}")
    print(json.dumps(payload["counts"], indent=2, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
