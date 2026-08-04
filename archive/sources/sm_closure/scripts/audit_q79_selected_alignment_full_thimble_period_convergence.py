from __future__ import annotations

import argparse
import concurrent.futures
import hashlib
import json
import subprocess
import sys
import time
from pathlib import Path

import numpy as np


ROOT = Path(__file__).resolve().parents[1]
DIRECTORY = (
    ROOT
    / "candidate_data"
    / "selected_q79covariantperiodbranchcutsetandtightbetatransport"
)
SINGLE = ROOT / "scripts" / "compute_q79_selected_alignment_single_thimble_period.py"
IDENTITY_ENGINE = ROOT / "scripts" / "q79genus2_period_transport.py"
SELECTED_ADAPTER = ROOT / "scripts" / "q79_selected_alignment_period_transport.py"
FAN = DIRECTORY / "selected_alignment_distinguished_radial_fan.interval.packet.json"
ATLAS = DIRECTORY / "selected_alignment_period_atlas.packet.json"
OUTPUT_DIRECTORY = DIRECTORY / "selected_alignment_thimble_periods"
INTEGRAL_BASIS = (
    ROOT
    / "candidate_data"
    / "selected_q79alignmentintegralh2presentation"
    / "selected_alignment_exact_integral_H2_basis.packet.json"
)
OUTPUT = OUTPUT_DIRECTORY / "selected_alignment_full_90_column_convergence_audit.packet.json"
VARIATION = {
    "epsilon": 3.0e-6,
    "dps": 100,
    "rtol": 8.0e-11,
    "atol": 8.0e-14,
}


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


def parse_values(packet: dict) -> np.ndarray:
    return np.asarray(
        [
            complex(float(value["real"]), float(value["imaginary"]))
            for value in packet["execution"]["period_values"]
        ],
        dtype=np.complex128,
    )


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser()
    parser.add_argument("--jobs", type=int, default=6)
    return parser.parse_args()


def baseline_path(row: dict) -> Path:
    return OUTPUT_DIRECTORY / (
        f"d{row['distinguished_index']:03d}_{row['root_id']}"
        ".thimble_period.candidate.json"
    )


def execute(row: dict, line_chart: str) -> tuple[int, dict]:
    index = int(row["distinguished_index"])
    command = [
        sys.executable,
        str(SINGLE),
        "--distinguished-index",
        str(index),
        "--epsilon",
        format(VARIATION["epsilon"], ".17g"),
        "--dps",
        str(VARIATION["dps"]),
        "--rtol",
        format(VARIATION["rtol"], ".17g"),
        "--atol",
        format(VARIATION["atol"], ".17g"),
        "--gauss-manin-chart",
        "t",
        "--no-save",
    ]
    if line_chart == "z":
        command.extend(["--line-chart", "z"])
    completed = subprocess.run(
        command,
        cwd=ROOT,
        text=True,
        capture_output=True,
    )
    if completed.returncode != 0:
        raise RuntimeError(
            f"d{index:03d} failed:\n{completed.stdout}\n{completed.stderr}"
        )
    return index, json.loads(completed.stdout)


def main() -> int:
    arguments = parse_args()
    if arguments.jobs < 1:
        raise ValueError("jobs must be positive")
    started = time.perf_counter()
    rows = load(FAN)["distinguished_positive_meridians"]
    atlas = load(ATLAS)
    selected_charts = {
        int(row["distinguished_index"]): row["selected_line_chart"]
        for row in atlas["rows"]
    }
    adapter_hash = sha256(SELECTED_ADAPTER)
    engine_hash = sha256(IDENTITY_ENGINE)
    baselines: dict[int, dict] = {}
    baseline_hashes: list[str] = []
    for row in rows:
        index = int(row["distinguished_index"])
        path = baseline_path(row)
        packet = load(path)
        authority = packet["authority"]
        if (
            authority["selected_period_adapter_sha256"] != adapter_hash
            or authority["unchanged_identity_period_engine_sha256"]
            != engine_hash
        ):
            raise AssertionError(f"stale baseline authority at d{index:03d}")
        expected_chart = selected_charts[index]
        if packet.get("line_chart", "y") != expected_chart:
            raise AssertionError(f"wrong selected line chart at d{index:03d}")
        baselines[index] = packet
        baseline_hashes.append(sha256(path))

    reruns: dict[int, dict] = {}
    with concurrent.futures.ThreadPoolExecutor(
        max_workers=arguments.jobs
    ) as pool:
        futures = {
            pool.submit(
                execute,
                row,
                selected_charts[int(row["distinguished_index"])],
            ): row
            for row in rows
        }
        for future in concurrent.futures.as_completed(futures):
            index, packet = future.result()
            reruns[index] = packet
            print(f"d{index:03d}: tighter rerun computed", flush=True)

    baseline_primitive = np.column_stack(
        [parse_values(baselines[index]) for index in range(1, 91)]
    )
    rerun_primitive = np.column_stack(
        [parse_values(reruns[index]) for index in range(1, 91)]
    )
    primitive_difference = np.abs(rerun_primitive - baseline_primitive)
    column_rows: list[dict] = []
    for row in rows:
        index = int(row["distinguished_index"])
        column = primitive_difference[:, index - 1]
        baseline_column = baseline_primitive[:, index - 1]
        scale = max(float(np.max(np.abs(baseline_column))), 1.0)
        maximum_absolute = float(np.max(column))
        column_rows.append(
            {
                "distinguished_index": index,
                "root_id": row["root_id"],
                "line_chart": reruns[index].get("line_chart", "y"),
                "maximum_absolute_difference": format(
                    maximum_absolute, ".17g"
                ),
                "maximum_scale_normalized_difference": format(
                    maximum_absolute / scale, ".17g"
                ),
                "rowwise_absolute_differences": [
                    format(float(value), ".17g") for value in column
                ],
                "rerun_numerics": reruns[index]["execution"]["numerics"],
            }
        )
    column_rows.sort(
        key=lambda value: float(value["maximum_scale_normalized_difference"]),
        reverse=True,
    )

    integral_basis = load(INTEGRAL_BASIS)
    primary_basis = np.asarray(
        integral_basis["primary_basis"]["basis_columns"], dtype=np.int64
    )
    if primary_basis.shape != (98, 90):
        raise AssertionError("selected integral primary basis shape changed")
    thimble_projection = primary_basis[:90, :]
    baseline_primary_thimble_part = baseline_primitive @ thimble_projection
    rerun_primary_thimble_part = rerun_primitive @ thimble_projection
    primary_difference = np.abs(
        rerun_primary_thimble_part - baseline_primary_thimble_part
    )

    maximum_primitive_absolute = float(np.max(primitive_difference))
    maximum_primitive_scaled = max(
        float(value["maximum_scale_normalized_difference"])
        for value in column_rows
    )
    maximum_primary_absolute = float(np.max(primary_difference))
    maximum_primary_scaled = maximum_primary_absolute / max(
        float(np.max(np.abs(baseline_primary_thimble_part))), 1.0
    )
    thresholds = (1.0e-6, 1.0e-7, 1.0e-8, 1.0e-9)
    payload = {
        "schema": "MTTQ79SelectedAlignmentFullThimblePeriodConvergenceAudit.v1",
        "status": "ALL_NINETY_SELECTED_COLUMNS_TIGHTER_CUTOFF_FLOATING_CONVERGENCE_AUDITED",
        "authority": {
            "unchanged_identity_period_engine_sha256": engine_hash,
            "selected_period_adapter_sha256": adapter_hash,
            "single_runner_sha256": sha256(SINGLE),
            "distinguished_fan_sha256": sha256(FAN),
            "selected_period_atlas_sha256": sha256(ATLAS),
            "selected_integral_H2_basis_sha256": sha256(INTEGRAL_BASIS),
            "ordered_baseline_packet_hashes_sha256": hashlib.sha256(
                "".join(baseline_hashes).encode("ascii")
            ).hexdigest(),
        },
        "variation": VARIATION,
        "primitive_table_comparison": {
            "shape": [8, 90],
            "maximum_absolute_difference": format(
                maximum_primitive_absolute, ".17g"
            ),
            "maximum_scale_normalized_difference": format(
                maximum_primitive_scaled, ".17g"
            ),
            "columns_exceeding_scale_normalized_threshold": {
                format(threshold, ".1e"): sum(
                    float(row["maximum_scale_normalized_difference"])
                    > threshold
                    for row in column_rows
                )
                for threshold in thresholds
            },
        },
        "A130_primary_basis_thimble_part_comparison": {
            "assembly": "Pi_primary_thimble=Pi_primitive*U_thimble_90x90",
            "shape": [8, 90],
            "maximum_absolute_difference": format(
                maximum_primary_absolute, ".17g"
            ),
            "maximum_scale_normalized_difference": format(
                maximum_primary_scaled, ".17g"
            ),
        },
        "columns_by_decreasing_scale_normalized_difference": column_rows,
        "elapsed_seconds": format(time.perf_counter() - started, ".17g"),
        "strict_scope": {
            "all_90_selected_columns_independently_rerun": True,
            "all_720_primitive_entries_compared": True,
            "A123_projective_atlas_selected_without_period_values": True,
            "A130_primary_basis_projection_compared": True,
            "full_interval_enclosure": False,
            "selected_handle_periods_included": False,
            "rank_92_period_table_promoted": False,
        },
    }
    dump(OUTPUT, payload)
    print(json.dumps(payload, indent=2, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
