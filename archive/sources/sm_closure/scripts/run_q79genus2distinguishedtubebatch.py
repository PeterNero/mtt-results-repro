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
    / "selected_q79genus2distinguishedmeridianexecution"
)
TRAJECTORY_BATCH = DATA / "distinguished_trajectory_batch.packet.json"
CERTIFIER = ROOT / "scripts" / "certify_q79genus2singlelocal_root_tubes.py"
OUTPUT = DATA / "distinguished_root_tube_batch.packet.json"


def load(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def stem(index: int, root_id: str) -> str:
    return f"d{index:03d}_{root_id}"


def trajectory_packet_path(index: int, root_id: str) -> Path:
    return DATA / f"{stem(index, root_id)}.trajectory.packet.json"


def certificate_path(index: int, root_id: str) -> Path:
    return DATA / f"{stem(index, root_id)}.root_tube_certificate.packet.json"


def valid_certificate(index: int, root_id: str) -> dict | None:
    path = certificate_path(index, root_id)
    packet_path = trajectory_packet_path(index, root_id)
    if not path.exists() or not packet_path.exists():
        return None
    certificate = load(path)
    trajectory_packet = load(packet_path)
    trajectory_path = ROOT / trajectory_packet["trajectory"]["path"]
    row = certificate.get("certificate", {})
    if (
        certificate.get("status")
        != "DISTINGUISHED_CONTINUOUS_ROOT_TUBES_CLOSED"
        or certificate.get("distinguished_index") != index
        or certificate.get("root_id") != root_id
        or not row.get("complete")
        or certificate["authority"].get("trajectory_packet_sha256")
        != sha256(packet_path)
        or certificate["authority"].get("trajectory_sha256")
        != sha256(trajectory_path)
        or float(row.get("minimum_Rouche_relative_margin", -1)) <= 0
        or float(row.get("minimum_pairwise_tube_separation", -1)) <= 0
    ):
        return None
    return certificate


def run_root(
    index: int, root_id: str, force: bool
) -> tuple[int, str, dict, bool]:
    existing = None if force else valid_certificate(index, root_id)
    if existing is not None:
        return index, root_id, existing, True
    result = subprocess.run(
        [
            sys.executable,
            str(CERTIFIER),
            "--root-id",
            root_id,
            "--distinguished-index",
            str(index),
        ],
        cwd=ROOT,
        capture_output=True,
        text=True,
    )
    if result.returncode != 0:
        raise RuntimeError(
            f"d{index:03d} {root_id} failed\n"
            f"stdout:\n{result.stdout}\nstderr:\n{result.stderr}"
        )
    certificate = valid_certificate(index, root_id)
    if certificate is None:
        raise AssertionError(f"d{index:03d} {root_id} emitted no valid certificate")
    return index, root_id, certificate, False


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--jobs", type=int, default=8)
    parser.add_argument("--force", action="store_true")
    args = parser.parse_args()
    trajectory_batch = load(TRAJECTORY_BATCH)
    if trajectory_batch["counts"]["trajectory_packets_complete"] != 90:
        raise AssertionError("all 90 distinguished trajectories are required")
    trajectory_rows = trajectory_batch["rows"]

    failures: list[str] = []
    with concurrent.futures.ThreadPoolExecutor(max_workers=args.jobs) as executor:
        futures = {
            executor.submit(
                run_root,
                int(row["distinguished_index"]),
                row["root_id"],
                args.force,
            ): row
            for row in trajectory_rows
        }
        for future in concurrent.futures.as_completed(futures):
            row = futures[future]
            index = int(row["distinguished_index"])
            root_id = row["root_id"]
            try:
                _, _, certificate, reused = future.result()
                print(
                    f"d{index:03d} {root_id}: "
                    f"{'reused' if reused else 'certified'} "
                    f"segments={certificate['certificate']['segments_certified']}",
                    flush=True,
                )
            except Exception as error:
                failures.append(str(error))
                print(f"d{index:03d} {root_id}: FAILED", flush=True)
    if failures:
        raise RuntimeError("\n\n".join(failures))

    rows: list[dict] = []
    for trajectory_row in trajectory_rows:
        index = int(trajectory_row["distinguished_index"])
        root_id = trajectory_row["root_id"]
        certificate = valid_certificate(index, root_id)
        if certificate is None:
            raise AssertionError(f"missing certificate d{index:03d} {root_id}")
        path = certificate_path(index, root_id)
        rows.append(
            {
                "distinguished_index": index,
                "root_id": root_id,
                "certificate_path": str(path.relative_to(ROOT)).replace("\\", "/"),
                "certificate_sha256": sha256(path),
                "segments_certified": certificate["certificate"][
                    "segments_certified"
                ],
                "minimum_Rouche_relative_margin": certificate["certificate"][
                    "minimum_Rouche_relative_margin"
                ],
                "minimum_pairwise_tube_separation": certificate["certificate"][
                    "minimum_pairwise_tube_separation"
                ],
            }
        )

    payload = {
        "schema": "MTTQ79GenusTwoDistinguishedRootTubeBatch.v1",
        "status": "ALL_90_DISTINGUISHED_CONTINUOUS_ROOT_TUBES_CLOSED",
        "authority": {
            "trajectory_batch_sha256": sha256(TRAJECTORY_BATCH),
            "certifier_sha256": sha256(CERTIFIER),
        },
        "counts": {
            "distinguished_meridians": len(rows),
            "continuous_root_tube_certificates": len(rows),
            "segments_certified": sum(row["segments_certified"] for row in rows),
            "promotion_ready_distinguished_matrices": len(rows),
        },
        "minimums": {
            "Rouche_relative_margin": format(
                min(
                    float(row["minimum_Rouche_relative_margin"])
                    for row in rows
                ),
                ".17g",
            ),
            "pairwise_tube_separation": format(
                min(
                    float(row["minimum_pairwise_tube_separation"])
                    for row in rows
                ),
                ".17g",
            ),
        },
        "rows": rows,
        "acceptance": {
            "all_90_distinguished_braid_isotopies_certified": True,
            "all_90_distinguished_matrices_root_tube_promotion_ready": True,
        },
    }
    OUTPUT.write_text(
        json.dumps(payload, indent=2, sort_keys=True) + "\n", encoding="utf-8"
    )
    print(f"wrote {OUTPUT}")
    print(json.dumps(payload["counts"], indent=2, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
