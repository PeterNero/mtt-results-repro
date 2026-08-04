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
SINGLE = ROOT / "scripts" / "compute_q79genus2single_distinguished_thimble_period.py"
ENGINE = ROOT / "scripts" / "q79genus2_period_transport.py"
FAN = (
    ROOT
    / "candidate_data"
    / "selected_q79genus2distinguishedcutsystemandglobalrelation"
    / "distinguished_radial_fan.packet.json"
)
CYCLE_PRESENTATION = (
    ROOT
    / "candidate_data"
    / "selected_q79genus2integralsurfacecyclepresentation"
    / "integral_surface_cycle_presentation.packet.json"
)
OUTPUT_DIR = ROOT / "candidate_data" / "selected_q79genus2thimbleperiodexecution"
OUTPUT = OUTPUT_DIR / "full_90_column_convergence_audit.packet.json"
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


def baseline_path(index: int, root_id: str) -> Path:
    return OUTPUT_DIR / f"d{index:03d}_{root_id}.thimble_period.candidate.json"


def execute(row: dict) -> tuple[int, dict]:
    index = row["distinguished_index"]
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
    args = parse_args()
    started = time.perf_counter()
    fan = load(FAN)
    rows = fan["distinguished_positive_meridians"]
    engine_hash = sha256(ENGINE)
    baselines: dict[int, dict] = {}
    baseline_hashes: list[str] = []
    for row in rows:
        index = row["distinguished_index"]
        path = baseline_path(index, row["root_id"])
        packet = load(path)
        if packet["authority"]["period_engine_sha256"] != engine_hash:
            raise AssertionError(f"stale baseline authority at d{index:03d}")
        baselines[index] = packet
        baseline_hashes.append(sha256(path))

    reruns: dict[int, dict] = {}
    with concurrent.futures.ThreadPoolExecutor(max_workers=args.jobs) as pool:
        futures = {pool.submit(execute, row): row for row in rows}
        for future in concurrent.futures.as_completed(futures):
            index, packet = future.result()
            reruns[index] = packet
            print(f"d{index:03d}: computed", flush=True)

    baseline_primitive = np.column_stack(
        [parse_values(baselines[index]) for index in range(1, 91)]
    )
    rerun_primitive = np.column_stack(
        [parse_values(reruns[index]) for index in range(1, 91)]
    )
    primitive_difference = np.abs(rerun_primitive - baseline_primitive)
    column_rows: list[dict] = []
    for row in rows:
        index = row["distinguished_index"]
        column = primitive_difference[:, index - 1]
        baseline_column = baseline_primitive[:, index - 1]
        scale = max(float(np.max(np.abs(baseline_column))), 1.0)
        maximum_absolute = float(np.max(column))
        column_rows.append(
            {
                "distinguished_index": index,
                "root_id": row["root_id"],
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

    cycle_presentation = load(CYCLE_PRESENTATION)
    kernel = np.asarray(
        cycle_presentation["thimble_boundary_lattice"][
            "closed_thimble_kernel_basis_columns"
        ],
        dtype=np.int64,
    )
    baseline_closed = baseline_primitive @ kernel
    rerun_closed = rerun_primitive @ kernel
    closed_difference = np.abs(rerun_closed - baseline_closed)
    maximum_primitive_absolute = float(np.max(primitive_difference))
    maximum_primitive_scaled = max(
        float(value["maximum_scale_normalized_difference"])
        for value in column_rows
    )
    maximum_closed_absolute = float(np.max(closed_difference))
    maximum_closed_scaled = maximum_closed_absolute / max(
        float(np.max(np.abs(baseline_closed))), 1.0
    )
    thresholds = (1.0e-6, 1.0e-7, 1.0e-8, 1.0e-9)
    payload = {
        "schema": "MTTQ79FullThimblePeriodConvergenceAudit.v1",
        "status": "ALL_NINETY_COLUMNS_TIGHTER_CUTOFF_FLOATING_CONVERGENCE_AUDITED_INTERVAL_PROMOTION_OPEN",
        "authority": {
            "period_engine_sha256": engine_hash,
            "single_runner_sha256": sha256(SINGLE),
            "distinguished_fan_sha256": sha256(FAN),
            "integral_cycle_presentation_sha256": sha256(CYCLE_PRESENTATION),
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
        "closed_thimble_table_comparison": {
            "assembly": "Pi_closed=Pi_primitive*K_90x86",
            "shape": [8, 86],
            "maximum_absolute_difference": format(
                maximum_closed_absolute, ".17g"
            ),
            "maximum_scale_normalized_difference": format(
                maximum_closed_scaled, ".17g"
            ),
        },
        "columns_by_decreasing_scale_normalized_difference": column_rows,
        "elapsed_seconds": format(time.perf_counter() - started, ".17g"),
        "strict_scope": {
            "all_90_columns_independently_rerun": True,
            "all_720_primitive_entries_compared": True,
            "all_688_closed_thimble_entries_compared": True,
            "full_interval_enclosure": False,
            "integral_H2_column_promotion": False,
        },
    }
    dump(OUTPUT, payload)
    print(json.dumps(payload, indent=2, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
