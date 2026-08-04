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
OUTPUT_DIR = ROOT / "candidate_data" / "selected_q79genus2thimbleperiodexecution"
OUTPUT = OUTPUT_DIR / "representative_convergence_audit.packet.json"
REPRESENTATIVES = (1, 12, 38, 43, 45)
VARIATIONS = (
    {
        "id": "smaller_endpoint_cutoff",
        "epsilon": 3.0e-6,
        "dps": 90,
        "rtol": 2.0e-10,
        "atol": 2.0e-13,
        "local_outer_order": None,
    },
    {
        "id": "higher_precision_tighter_ODE",
        "epsilon": 1.0e-5,
        "dps": 120,
        "rtol": 8.0e-11,
        "atol": 8.0e-14,
        "local_outer_order": None,
    },
    {
        "id": "higher_local_quadrature_order",
        "epsilon": 1.0e-5,
        "dps": 90,
        "rtol": 2.0e-10,
        "atol": 2.0e-13,
        "local_outer_order": 96,
    },
)


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
    parser.add_argument("--jobs", type=int, default=4)
    return parser.parse_args()


def baseline_path(index: int) -> Path:
    matches = sorted(OUTPUT_DIR.glob(f"d{index:03d}_*.thimble_period.candidate.json"))
    if len(matches) != 1:
        raise AssertionError(f"expected one baseline packet for d{index:03d}")
    return matches[0]


def execute(case: tuple[int, dict]) -> tuple[int, dict, dict]:
    index, variation = case
    command = [
        sys.executable,
        str(SINGLE),
        "--distinguished-index",
        str(index),
        "--epsilon",
        format(variation["epsilon"], ".17g"),
        "--dps",
        str(variation["dps"]),
        "--rtol",
        format(variation["rtol"], ".17g"),
        "--atol",
        format(variation["atol"], ".17g"),
        "--gauss-manin-chart",
        "t",
        "--no-save",
    ]
    if variation["local_outer_order"] is not None:
        command[-1:-1] = [
            "--local-outer-order",
            str(variation["local_outer_order"]),
        ]
    completed = subprocess.run(
        command,
        cwd=ROOT,
        text=True,
        capture_output=True,
    )
    if completed.returncode != 0:
        raise RuntimeError(
            f"d{index:03d}/{variation['id']} failed:\n"
            f"{completed.stdout}\n{completed.stderr}"
        )
    return index, variation, json.loads(completed.stdout)


def main() -> int:
    args = parse_args()
    started = time.perf_counter()
    engine_hash = sha256(ENGINE)
    baselines = {index: load(baseline_path(index)) for index in REPRESENTATIVES}
    if any(
        packet["authority"]["period_engine_sha256"] != engine_hash
        for packet in baselines.values()
    ):
        raise AssertionError("representative baseline uses stale engine authority")

    cases = [
        (index, variation)
        for index in REPRESENTATIVES
        for variation in VARIATIONS
    ]
    reruns: dict[tuple[int, str], dict] = {}
    with concurrent.futures.ThreadPoolExecutor(max_workers=args.jobs) as pool:
        futures = {pool.submit(execute, case): case for case in cases}
        for future in concurrent.futures.as_completed(futures):
            index, variation, packet = future.result()
            reruns[index, variation["id"]] = packet
            print(f"d{index:03d}/{variation['id']}: computed", flush=True)

    comparisons: list[dict] = []
    absolute_differences: list[float] = []
    scaled_differences: list[float] = []
    for index in REPRESENTATIVES:
        baseline = baselines[index]
        baseline_values = parse_values(baseline)
        scale = max(float(np.max(np.abs(baseline_values))), 1.0)
        for variation in VARIATIONS:
            packet = reruns[index, variation["id"]]
            values = parse_values(packet)
            differences = np.abs(values - baseline_values)
            maximum_absolute = float(np.max(differences))
            maximum_scaled = maximum_absolute / scale
            absolute_differences.append(maximum_absolute)
            scaled_differences.append(maximum_scaled)
            comparisons.append(
                {
                    "distinguished_index": index,
                    "root_id": baseline["root_id"],
                    "variation": variation,
                    "maximum_absolute_difference": format(
                        maximum_absolute, ".17g"
                    ),
                    "maximum_scale_normalized_difference": format(
                        maximum_scaled, ".17g"
                    ),
                    "rowwise_absolute_differences": [
                        format(float(value), ".17g") for value in differences
                    ],
                    "rerun_numerics": packet["execution"]["numerics"],
                }
            )

    maximum_absolute = max(absolute_differences)
    maximum_scaled = max(scaled_differences)
    payload = {
        "schema": "MTTQ79RepresentativeThimblePeriodConvergenceAudit.v1",
        "status": "REPRESENTATIVE_THREE_AXIS_FLOATING_CONVERGENCE_AUDITED_INTERVAL_PROMOTION_OPEN",
        "authority": {
            "period_engine_sha256": engine_hash,
            "single_runner_sha256": sha256(SINGLE),
            "baseline_packet_sha256": {
                str(index): sha256(baseline_path(index))
                for index in REPRESENTATIVES
            },
        },
        "representative_design": {
            "indices": list(REPRESENTATIVES),
            "coverage": "ordinary s_0 chart, s_minus1 chart, and all three formerly stalled/high-condition rays",
            "variation_axes": [variation["id"] for variation in VARIATIONS],
        },
        "comparisons": comparisons,
        "maximum_absolute_difference": format(maximum_absolute, ".17g"),
        "maximum_scale_normalized_difference": format(maximum_scaled, ".17g"),
        "elapsed_seconds": format(time.perf_counter() - started, ".17g"),
        "strict_scope": {
            "representative_columns_audited": len(REPRESENTATIVES),
            "independent_reruns": len(cases),
            "endpoint_cutoff_axis_executed": True,
            "precision_and_ODE_tolerance_axis_executed": True,
            "local_quadrature_order_axis_executed": True,
            "full_90_column_interval_enclosure": False,
            "integral_H2_column_promotion": False,
        },
    }
    dump(OUTPUT, payload)
    print(json.dumps(payload, indent=2, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
