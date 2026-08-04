from __future__ import annotations

import argparse
import concurrent.futures
import hashlib
import json
import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
DATA = (
    ROOT
    / "candidate_data"
    / "selected_q79genus2localroottrajectoryexecution"
)
TRAJECTORY_BATCH = DATA / "local_trajectory_batch.packet.json"
CERTIFIER = ROOT / "scripts" / "certify_q79genus2singlelocal_root_tubes.py"
OUTPUT = DATA / "local_root_tube_batch.packet.json"


def load(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def dump(path: Path, payload: dict) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(payload, indent=2, sort_keys=True) + "\n", encoding="utf-8")


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def trajectory_packet_path(root_id: str) -> Path:
    return DATA / f"{root_id}.trajectory.packet.json"


def full_certificate_path(root_id: str) -> Path:
    return DATA / f"{root_id}.root_tube_certificate.packet.json"


def partial_certificate_path(root_id: str, start: int, stop: int) -> Path:
    return DATA / (
        f"{root_id}.root_tube_certificate.{start}_{stop}.partial.packet.json"
    )


def certificate_matches_trajectory(certificate: dict, root_id: str) -> bool:
    packet_path = trajectory_packet_path(root_id)
    trajectory_packet = load(packet_path)
    trajectory_path = ROOT / trajectory_packet["trajectory"]["path"]
    return (
        certificate["root_id"] == root_id
        and certificate["authority"]["trajectory_packet_sha256"]
        == sha256(packet_path)
        and certificate["authority"]["trajectory_sha256"]
        == sha256(trajectory_path)
        and float(certificate["certificate"]["minimum_Rouche_relative_margin"])
        > 0
        and float(certificate["certificate"]["minimum_pairwise_tube_separation"])
        > 0
    )


def valid_full(root_id: str) -> dict | None:
    path = full_certificate_path(root_id)
    if not path.exists():
        return None
    certificate = load(path)
    if (
        certificate["status"] != "LOCAL_CONTINUOUS_ROOT_TUBES_CLOSED"
        or not certificate["certificate"]["complete"]
        or not certificate_matches_trajectory(certificate, root_id)
    ):
        return None
    return certificate


def valid_partial(root_id: str, start: int, stop: int) -> dict | None:
    path = partial_certificate_path(root_id, start, stop)
    if not path.exists():
        return None
    certificate = load(path)
    row = certificate["certificate"]
    if (
        row["segment_start"] != start
        or row["segments_certified"] != stop - start
        or row["complete"]
        or not certificate_matches_trajectory(certificate, root_id)
    ):
        return None
    return certificate


def run_chunk(
    root_id: str, start: int, stop: int, force: bool
) -> tuple[str, int, int, bool]:
    if not force:
        if start == 0:
            full = valid_full(root_id)
            if full is not None:
                return root_id, 0, full["certificate"]["segments_available"], True
        partial = valid_partial(root_id, start, stop)
        if partial is not None:
            return root_id, start, stop, True
    result = subprocess.run(
        [
            sys.executable,
            str(CERTIFIER),
            "--root-id",
            root_id,
            "--start",
            str(start),
            "--limit",
            str(stop - start),
        ],
        cwd=ROOT,
        capture_output=True,
        text=True,
    )
    if result.returncode != 0:
        raise RuntimeError(
            f"{root_id}[{start}:{stop}] failed\n"
            f"stdout:\n{result.stdout}\nstderr:\n{result.stderr}"
        )
    if stop == load(trajectory_packet_path(root_id))["transport"]["saved_sample_count"] - 1:
        valid = valid_full(root_id) if start == 0 else valid_partial(root_id, start, stop)
    else:
        valid = valid_partial(root_id, start, stop)
    if valid is None:
        raise AssertionError(f"{root_id}[{start}:{stop}] emitted no valid certificate")
    return root_id, start, stop, False


def aggregate_root(root_id: str, available: int) -> dict:
    existing = valid_full(root_id)
    if existing is not None and existing["certificate"]["segments_certified"] == available:
        return existing

    partial_paths = sorted(
        DATA.glob(f"{root_id}.root_tube_certificate.*_*.partial.packet.json"),
        key=lambda path: load(path)["certificate"]["segment_start"],
    )
    partials: list[tuple[Path, dict]] = []
    cursor = 0
    for path in partial_paths:
        certificate = load(path)
        row = certificate["certificate"]
        start = row["segment_start"]
        stop = start + row["segments_certified"]
        if start != cursor or not certificate_matches_trajectory(certificate, root_id):
            continue
        partials.append((path, certificate))
        cursor = stop
        if cursor == available:
            break
    if cursor != available:
        raise AssertionError(f"{root_id} partial tube coverage ends at {cursor}/{available}")

    packet_path = trajectory_packet_path(root_id)
    trajectory_packet = load(packet_path)
    trajectory_path = ROOT / trajectory_packet["trajectory"]["path"]
    payload = {
        "schema": "MTTQ79GenusTwoAggregatedLocalContinuousRootTubeCertificate.v1",
        "status": "LOCAL_CONTINUOUS_ROOT_TUBES_CLOSED",
        "root_id": root_id,
        "authority": {
            "trajectory_packet_sha256": sha256(packet_path),
            "trajectory_sha256": sha256(trajectory_path),
            "certifier_sha256": sha256(CERTIFIER),
            "partial_certificates": [
                {
                    "path": str(path.relative_to(ROOT)).replace("\\", "/"),
                    "sha256": sha256(path),
                }
                for path, _ in partials
            ],
        },
        "branch_chart": partials[0][1]["branch_chart"],
        "certificate": {
            "segments_available": available,
            "segment_start": 0,
            "segments_certified": available,
            "complete": True,
            "minimum_Rouche_relative_margin": format(
                min(
                    float(certificate["certificate"]["minimum_Rouche_relative_margin"])
                    for _, certificate in partials
                ),
                ".17g",
            ),
            "minimum_pairwise_tube_separation": format(
                min(
                    float(certificate["certificate"]["minimum_pairwise_tube_separation"])
                    for _, certificate in partials
                ),
                ".17g",
            ),
            "segments_requiring_certificate_subdivision": sum(
                certificate["certificate"]["segments_requiring_certificate_subdivision"]
                for _, certificate in partials
            ),
            "maximum_certificate_subdivision_depth": max(
                certificate["certificate"]["maximum_certificate_subdivision_depth"]
                for _, certificate in partials
            ),
            "additional_root_subinterval_certificates": sum(
                certificate["certificate"]["additional_root_subinterval_certificates"]
                for _, certificate in partials
            ),
            "partial_certificate_count": len(partials),
        },
        "method": partials[0][1]["method"],
        "acceptance": {
            "continuous_local_braid_isotopy_certified": True,
            "promotion_ready": True,
        },
    }
    dump(full_certificate_path(root_id), payload)
    return payload


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--jobs", type=int, default=8)
    parser.add_argument("--chunk-size", type=int, default=4000)
    parser.add_argument("--force", action="store_true")
    args = parser.parse_args()
    trajectory_batch = load(TRAJECTORY_BATCH)
    if trajectory_batch["counts"]["trajectory_packets_complete"] != 90:
        raise AssertionError("all 90 local trajectories are required")

    available_by_root = {
        row["root_id"]: load(trajectory_packet_path(row["root_id"]))["transport"][
            "saved_sample_count"
        ]
        - 1
        for row in trajectory_batch["rows"]
    }
    tasks: list[tuple[str, int, int]] = []
    for root_id, available in available_by_root.items():
        if not args.force and valid_full(root_id) is not None:
            continue
        for start in range(0, available, args.chunk_size):
            tasks.append((root_id, start, min(available, start + args.chunk_size)))

    failures: list[str] = []
    with concurrent.futures.ThreadPoolExecutor(max_workers=args.jobs) as executor:
        futures = {
            executor.submit(run_chunk, root_id, start, stop, args.force): (
                root_id,
                start,
                stop,
            )
            for root_id, start, stop in tasks
        }
        for future in concurrent.futures.as_completed(futures):
            root_id, start, stop = futures[future]
            try:
                _, _, _, reused = future.result()
                print(
                    f"{root_id}[{start}:{stop}]: "
                    f"{'reused' if reused else 'certified'}",
                    flush=True,
                )
            except Exception as error:
                failures.append(str(error))
                print(f"{root_id}[{start}:{stop}]: FAILED", flush=True)
    if failures:
        raise RuntimeError("\n\n".join(failures))

    rows: list[dict] = []
    for root_id, available in available_by_root.items():
        certificate = aggregate_root(root_id, available)
        path = full_certificate_path(root_id)
        rows.append(
            {
                "root_id": root_id,
                "certificate_path": str(path.relative_to(ROOT)).replace("\\", "/"),
                "certificate_sha256": sha256(path),
                "segments_certified": certificate["certificate"]["segments_certified"],
                "minimum_Rouche_relative_margin": certificate["certificate"][
                    "minimum_Rouche_relative_margin"
                ],
                "minimum_pairwise_tube_separation": certificate["certificate"][
                    "minimum_pairwise_tube_separation"
                ],
            }
        )

    payload = {
        "schema": "MTTQ79GenusTwoLocalRootTubeBatch.v1",
        "status": "ALL_90_LOCAL_CONTINUOUS_ROOT_TUBES_CLOSED",
        "authority": {
            "trajectory_batch_sha256": sha256(TRAJECTORY_BATCH),
            "certifier_sha256": sha256(CERTIFIER),
        },
        "counts": {
            "local_meridians": len(rows),
            "continuous_root_tube_certificates": len(rows),
            "segments_certified": sum(row["segments_certified"] for row in rows),
            "promotion_ready_local_matrices": len(rows),
        },
        "minimums": {
            "Rouche_relative_margin": format(
                min(float(row["minimum_Rouche_relative_margin"]) for row in rows),
                ".17g",
            ),
            "pairwise_tube_separation": format(
                min(float(row["minimum_pairwise_tube_separation"]) for row in rows),
                ".17g",
            ),
        },
        "rows": rows,
        "acceptance": {
            "all_90_continuous_local_braid_isotopies_certified": True,
            "all_90_local_matrices_root_tube_promotion_ready": True,
        },
    }
    dump(OUTPUT, payload)
    print(f"wrote {OUTPUT}")
    print(json.dumps(payload["counts"], indent=2, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
