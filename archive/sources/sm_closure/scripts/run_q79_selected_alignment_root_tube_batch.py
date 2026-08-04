from __future__ import annotations

import argparse
import concurrent.futures
import hashlib
import json
import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
DIRECTORY = (
    ROOT
    / "candidate_data"
    / "selected_q79covariantperiodbranchcutsetandtightbetatransport"
)
MONODROMY_BATCH = DIRECTORY / "selected_alignment_meridian_monodromy_batch.packet.json"
MONODROMY = DIRECTORY / "selected_alignment_meridian_monodromy"
OUTPUT = DIRECTORY / "selected_alignment_continuous_root_tubes"
BATCH = DIRECTORY / "selected_alignment_continuous_root_tube_batch.packet.json"
CERTIFIER = ROOT / "scripts" / "certify_q79_selected_alignment_single_root_tubes.py"


def load(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def dump(path: Path, payload: dict) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(
        json.dumps(payload, indent=2, sort_keys=True) + "\n",
        encoding="utf-8",
    )


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def stem(index: int, root_id: str) -> str:
    return f"d{index:03d}_{root_id}"


def monodromy_path(index: int, root_id: str) -> Path:
    return MONODROMY / f"{stem(index, root_id)}.packet.json"


def full_path(index: int, root_id: str) -> Path:
    return OUTPUT / f"{stem(index, root_id)}.root_tube_certificate.packet.json"


def partial_path(index: int, root_id: str, start: int, stop: int) -> Path:
    return OUTPUT / (
        f"{stem(index, root_id)}.root_tube_certificate."
        f"{start}_{stop}.partial.packet.json"
    )


def certificate_matches(certificate: dict, index: int, root_id: str) -> bool:
    source_path = monodromy_path(index, root_id)
    source = load(source_path)
    trajectory_path = ROOT / source["trajectory"]["path"]
    return (
        certificate["distinguished_index"] == index
        and certificate["root_id"] == root_id
        and certificate["authority"]["monodromy_packet_sha256"]
        == sha256(source_path)
        and certificate["authority"]["trajectory_sha256"]
        == sha256(trajectory_path)
        and float(certificate["certificate"]["minimum_Rouche_relative_margin"])
        > 0
        and float(certificate["certificate"]["minimum_pairwise_tube_separation"])
        > 0
    )


def valid_full(index: int, root_id: str) -> dict | None:
    path = full_path(index, root_id)
    if not path.exists():
        return None
    certificate = load(path)
    if (
        certificate["status"]
        != "SELECTED_ALIGNMENT_CONTINUOUS_ROOT_TUBES_CLOSED"
        or not certificate["certificate"]["complete"]
        or not certificate_matches(certificate, index, root_id)
    ):
        return None
    return certificate


def valid_partial(
    index: int, root_id: str, start: int, stop: int
) -> dict | None:
    path = partial_path(index, root_id, start, stop)
    if not path.exists():
        return None
    certificate = load(path)
    row = certificate["certificate"]
    if (
        row["segment_start"] != start
        or row["segments_certified"] != stop - start
        or row["complete"]
        or not certificate_matches(certificate, index, root_id)
    ):
        return None
    return certificate


def run_chunk(
    index: int,
    root_id: str,
    start: int,
    stop: int,
    available: int,
    force: bool,
) -> tuple[int, str, int, int, bool]:
    if not force:
        if start == 0 and stop == available:
            full = valid_full(index, root_id)
            if full is not None:
                return index, root_id, start, stop, True
        partial = valid_partial(index, root_id, start, stop)
        if partial is not None:
            return index, root_id, start, stop, True
    command = [
        sys.executable,
        str(CERTIFIER),
        "--distinguished-index",
        str(index),
        "--root-id",
        root_id,
        "--start",
        str(start),
        "--limit",
        str(stop - start),
    ]
    result = subprocess.run(
        command,
        cwd=ROOT,
        capture_output=True,
        text=True,
    )
    if result.returncode != 0:
        raise RuntimeError(
            f"{stem(index, root_id)}[{start}:{stop}] failed\n"
            f"stdout:\n{result.stdout}\nstderr:\n{result.stderr}"
        )
    certificate = (
        valid_full(index, root_id)
        if start == 0 and stop == available
        else valid_partial(index, root_id, start, stop)
    )
    if certificate is None:
        raise AssertionError(
            f"{stem(index, root_id)}[{start}:{stop}] emitted no valid certificate"
        )
    return index, root_id, start, stop, False


def aggregate(index: int, root_id: str, available: int) -> dict:
    existing = valid_full(index, root_id)
    if (
        existing is not None
        and existing["certificate"]["segments_certified"] == available
    ):
        return existing

    pattern = f"{stem(index, root_id)}.root_tube_certificate.*_*.partial.packet.json"
    candidates = sorted(
        OUTPUT.glob(pattern),
        key=lambda path: load(path)["certificate"]["segment_start"],
    )
    partials: list[tuple[Path, dict]] = []
    cursor = 0
    for path in candidates:
        certificate = load(path)
        row = certificate["certificate"]
        start = row["segment_start"]
        stop = start + row["segments_certified"]
        if start != cursor or not certificate_matches(certificate, index, root_id):
            continue
        partials.append((path, certificate))
        cursor = stop
        if cursor == available:
            break
    if cursor != available:
        raise AssertionError(
            f"{stem(index, root_id)} partial coverage ends at {cursor}/{available}"
        )

    source_path = monodromy_path(index, root_id)
    source = load(source_path)
    trajectory_path = ROOT / source["trajectory"]["path"]
    payload = {
        "schema": "MTTQ79SelectedAlignmentAggregatedContinuousRootTubeCertificate.v1",
        "status": "SELECTED_ALIGNMENT_CONTINUOUS_ROOT_TUBES_CLOSED",
        "root_id": root_id,
        "distinguished_index": index,
        "authority": {
            "monodromy_packet_sha256": sha256(source_path),
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
                    float(value["certificate"]["minimum_Rouche_relative_margin"])
                    for _, value in partials
                ),
                ".17g",
            ),
            "minimum_pairwise_tube_separation": format(
                min(
                    float(value["certificate"]["minimum_pairwise_tube_separation"])
                    for _, value in partials
                ),
                ".17g",
            ),
            "segments_requiring_certificate_subdivision": sum(
                value["certificate"]["segments_requiring_certificate_subdivision"]
                for _, value in partials
            ),
            "maximum_certificate_subdivision_depth": max(
                value["certificate"]["maximum_certificate_subdivision_depth"]
                for _, value in partials
            ),
            "additional_root_subinterval_certificates": sum(
                value["certificate"]["additional_root_subinterval_certificates"]
                for _, value in partials
            ),
            "partial_certificate_count": len(partials),
        },
        "method": partials[0][1]["method"],
        "acceptance": {
            "continuous_selected_braid_isotopy_certified": True,
            "promotion_ready": True,
        },
    }
    dump(full_path(index, root_id), payload)
    return payload


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--jobs", type=int, default=8)
    parser.add_argument("--chunk-size", type=int, default=4000)
    parser.add_argument("--force", action="store_true")
    arguments = parser.parse_args()
    batch = load(MONODROMY_BATCH)
    if batch["counts"]["monodromy_packets_complete"] != 90:
        raise AssertionError("all selected monodromy packets are required")

    rows: list[tuple[int, str, int]] = []
    for row in batch["rows"]:
        index = int(row["distinguished_index"])
        root_id = row["root_id"]
        packet = load(monodromy_path(index, root_id))
        available = int(packet["transport"]["saved_sample_count"]) - 1
        rows.append((index, root_id, available))

    tasks: list[tuple[int, str, int, int, int]] = []
    for index, root_id, available in rows:
        if not arguments.force and valid_full(index, root_id) is not None:
            continue
        for start in range(0, available, arguments.chunk_size):
            tasks.append(
                (
                    index,
                    root_id,
                    start,
                    min(available, start + arguments.chunk_size),
                    available,
                )
            )

    failures: list[str] = []
    with concurrent.futures.ThreadPoolExecutor(max_workers=arguments.jobs) as executor:
        futures = {
            executor.submit(run_chunk, *task, arguments.force): task
            for task in tasks
        }
        for future in concurrent.futures.as_completed(futures):
            index, root_id, start, stop, _available = futures[future]
            try:
                _, _, _, _, reused = future.result()
                print(
                    f"{stem(index, root_id)}[{start}:{stop}]: "
                    f"{'reused' if reused else 'certified'}",
                    flush=True,
                )
            except Exception as error:
                failures.append(str(error))
                print(
                    f"{stem(index, root_id)}[{start}:{stop}]: FAILED",
                    flush=True,
                )
    if failures:
        raise RuntimeError("\n\n".join(failures))

    output_rows: list[dict] = []
    for index, root_id, available in rows:
        certificate = aggregate(index, root_id, available)
        path = full_path(index, root_id)
        output_rows.append(
            {
                "distinguished_index": index,
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
        "schema": "MTTQ79SelectedAlignmentContinuousRootTubeBatch.v1",
        "status": "ALL_90_SELECTED_ALIGNMENT_CONTINUOUS_ROOT_TUBES_CLOSED",
        "authority": {
            "monodromy_batch_sha256": sha256(MONODROMY_BATCH),
            "certifier_sha256": sha256(CERTIFIER),
        },
        "counts": {
            "selected_meridians": 90,
            "continuous_root_tube_certificates": len(output_rows),
            "segments_certified": sum(row["segments_certified"] for row in output_rows),
        },
        "minimums": {
            "Rouche_relative_margin": format(
                min(float(row["minimum_Rouche_relative_margin"]) for row in output_rows),
                ".17g",
            ),
            "pairwise_tube_separation": format(
                min(float(row["minimum_pairwise_tube_separation"]) for row in output_rows),
                ".17g",
            ),
        },
        "rows": output_rows,
        "acceptance": {
            "all_90_selected_braid_isotopies_certified": True,
            "all_90_selected_matrices_root_tube_promotion_ready": True,
        },
    }
    dump(BATCH, payload)
    print(f"wrote {BATCH.relative_to(ROOT)}")
    print(json.dumps(payload["counts"], indent=2, sort_keys=True))
    print(json.dumps(payload["minimums"], indent=2, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
