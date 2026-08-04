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
PRIMITIVE_TABLE = OUTPUT_DIRECTORY / "selected_alignment_primitive_thimble_period_table.packet.json"
BATCH = OUTPUT_DIRECTORY / "selected_alignment_thimble_period_batch.packet.json"


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


def decode_complex(value: dict[str, str]) -> complex:
    return complex(float(value["real"]), float(value["imaginary"]))


def encode_complex(value: complex) -> dict[str, str]:
    return {
        "real": format(value.real, ".17g"),
        "imaginary": format(value.imag, ".17g"),
    }


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser()
    parser.add_argument("--jobs", type=int, default=4)
    parser.add_argument("--force", action="store_true")
    parser.add_argument("--epsilon", type=float, default=1.0e-5)
    parser.add_argument("--inner-order", type=int, default=160)
    parser.add_argument("--dps", type=int, default=70)
    parser.add_argument("--root-step-ratio", type=float, default=0.12)
    parser.add_argument("--rtol", type=float, default=2.0e-10)
    parser.add_argument("--atol", type=float, default=2.0e-13)
    return parser.parse_args()


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
    if set(selected_charts) != set(range(1, 91)):
        raise AssertionError("selected period atlas is incomplete")
    OUTPUT_DIRECTORY.mkdir(parents=True, exist_ok=True)

    def output_path(row: dict) -> Path:
        return OUTPUT_DIRECTORY / (
            f"d{row['distinguished_index']:03d}_{row['root_id']}"
            ".thimble_period.candidate.json"
        )

    def run(row: dict) -> tuple[int, str]:
        output = output_path(row)
        if output.exists() and not arguments.force:
            return int(row["distinguished_index"]), "cached"
        command = [
            sys.executable,
            str(SINGLE),
            "--distinguished-index",
            str(row["distinguished_index"]),
            "--epsilon",
            format(arguments.epsilon, ".17g"),
            "--inner-order",
            str(arguments.inner_order),
            "--dps",
            str(arguments.dps),
            "--root-step-ratio",
            format(arguments.root_step_ratio, ".17g"),
            "--rtol",
            format(arguments.rtol, ".17g"),
            "--atol",
            format(arguments.atol, ".17g"),
        ]
        completed = subprocess.run(
            command,
            cwd=ROOT,
            text=True,
            capture_output=True,
        )
        if completed.returncode != 0:
            raise RuntimeError(
                f"d{row['distinguished_index']:03d} failed:\n"
                f"{completed.stdout}\n{completed.stderr}"
            )
        return int(row["distinguished_index"]), "computed"

    statuses: dict[int, str] = {}
    with concurrent.futures.ThreadPoolExecutor(
        max_workers=arguments.jobs
    ) as pool:
        futures = {pool.submit(run, row): row for row in rows}
        for future in concurrent.futures.as_completed(futures):
            index, status = future.result()
            statuses[index] = status
            print(f"d{index:03d}: {status}", flush=True)

    for chart_row in rows:
        index = int(chart_row["distinguished_index"])
        selected_chart = selected_charts[index]
        chart_path = output_path(chart_row)
        chart_packet = load(chart_path)
        if chart_packet.get("line_chart", "y") == selected_chart:
            continue
        command = [
            sys.executable,
            str(SINGLE),
            "--distinguished-index",
            str(index),
            "--line-chart",
            selected_chart,
            "--epsilon",
            format(arguments.epsilon, ".17g"),
            "--inner-order",
            str(arguments.inner_order),
            "--dps",
            str(arguments.dps),
            "--root-step-ratio",
            format(arguments.root_step_ratio, ".17g"),
            "--rtol",
            format(arguments.rtol, ".17g"),
            "--atol",
            format(arguments.atol, ".17g"),
        ]
        completed = subprocess.run(
            command,
            cwd=ROOT,
            text=True,
            capture_output=True,
        )
        if completed.returncode != 0:
            raise RuntimeError(
                f"d{index:03d} {selected_chart}-chart repair failed:\n"
                f"{completed.stdout}\n{completed.stderr}"
            )
        statuses[index] = f"computed_atlas_{selected_chart}"
        print(
            f"d{index:03d}: recomputed in selected {selected_chart} line chart",
            flush=True,
        )

    packets = [load(output_path(row)) for row in rows]
    if [packet["distinguished_index"] for packet in packets] != list(
        range(1, 91)
    ):
        raise AssertionError("selected period packet order")
    adapter_hash = sha256(SELECTED_ADAPTER)
    engine_hash = sha256(IDENTITY_ENGINE)
    for packet in packets:
        if (
            packet["authority"]["selected_period_adapter_sha256"]
            != adapter_hash
            or packet["authority"]["unchanged_identity_period_engine_sha256"]
            != engine_hash
        ):
            raise AssertionError("mixed or stale selected period authority")

    form_names = packets[0]["execution"]["form_names"]
    primitive = np.asarray(
        [
            [
                decode_complex(value)
                for value in packet["execution"]["period_values"]
            ]
            for packet in packets
        ],
        dtype=np.complex128,
    ).T
    if primitive.shape != (8, 90):
        raise AssertionError("selected primitive period table shape")
    primitive_payload = {
        "schema": "MTTQ79SelectedAlignmentPrimitiveThimblePeriodTable.v1",
        "status": "SELECTED_ALIGNMENT_EIGHT_BY_NINETY_FLOATING_PERIOD_TABLE_COMPUTED",
        "form_names": form_names,
        "column_distinguished_indices": list(range(1, 91)),
        "column_root_ids": [packet["root_id"] for packet in packets],
        "period_rows": [
            [encode_complex(value) for value in row] for row in primitive
        ],
        "maximum_absolute_entry": format(
            float(np.max(np.abs(primitive))), ".17g"
        ),
        "strict_scope": {
            "same_selected_carrier_as_A127_beta": True,
            "floating_candidate_entries": 720,
            "independent_tighter_rerun_entries": 0,
            "interval_certified_entries": 0,
            "observed_SM_values_used": False,
        },
    }
    dump(PRIMITIVE_TABLE, primitive_payload)

    numerics = [packet["execution"]["numerics"] for packet in packets]
    batch = {
        "schema": "MTTQ79SelectedAlignmentThimblePeriodBatch.v1",
        "status": "ALL_NINETY_SELECTED_ALIGNMENT_THIMBLE_PERIOD_CANDIDATES_COMPUTED",
        "counts": {
            "computed_this_run": sum(
                value.startswith("computed") for value in statuses.values()
            ),
            "cached_this_run": sum(
                value == "cached" for value in statuses.values()
            ),
            "complete_period_packets": len(packets),
            "projective_z_chart_columns": sum(
                packet.get("line_chart", "y") == "z" for packet in packets
            ),
            "primitive_complex_entries": int(primitive.size),
            "high_precision_Gauss_Manin_connection_evaluations": sum(
                int(row["high_precision_Gauss_Manin_connection_evaluations"])
                for row in numerics
            ),
        },
        "authority": {
            "single_runner_sha256": sha256(SINGLE),
            "unchanged_identity_period_engine_sha256": engine_hash,
            "selected_period_adapter_sha256": adapter_hash,
            "distinguished_fan_sha256": sha256(FAN),
            "selected_period_atlas_sha256": sha256(ATLAS),
            "ordered_single_packet_hashes_sha256": hashlib.sha256(
                "".join(sha256(output_path(row)) for row in rows).encode(
                    "ascii"
                )
            ).hexdigest(),
        },
        "maximums": {
            "Gauss_Manin_reduction_condition_number": format(
                max(
                    float(row["maximum_reduction_condition_number"])
                    for row in numerics
                ),
                ".17g",
            ),
            "equilibrated_Gauss_Manin_reduction_condition_number": format(
                max(
                    float(
                        row[
                            "maximum_equilibrated_reduction_condition_number"
                        ]
                    )
                    for row in numerics
                ),
                ".17g",
            ),
            "Gauss_Manin_reduction_relative_residual": format(
                max(
                    float(row["maximum_reduction_relative_residual"])
                    for row in numerics
                ),
                ".17g",
            ),
            "high_precision_solution_ball_radius": format(
                max(
                    float(row["maximum_high_precision_solution_radius"])
                    for row in numerics
                ),
                ".17g",
            ),
            "ODE_function_evaluations": max(
                int(row["ODE_function_evaluations"]) for row in numerics
            ),
        },
        "minimums": {
            "initial_other_root_normalized_clearance": format(
                min(
                    float(row["initial_other_root_normalized_clearance"])
                    for row in numerics
                ),
                ".17g",
            ),
            "endpoint_tail_other_root_normalized_clearance": format(
                min(
                    float(
                        row[
                            "endpoint_tail_minimum_other_root_normalized_clearance"
                        ]
                    )
                    for row in numerics
                ),
                ".17g",
            ),
        },
        "output": {
            "primitive_table": str(PRIMITIVE_TABLE.relative_to(ROOT)).replace(
                "\\", "/"
            ),
            "primitive_table_sha256": sha256(PRIMITIVE_TABLE),
        },
        "elapsed_seconds": format(time.perf_counter() - started, ".17g"),
        "strict_scope": {
            "all_90_selected_carrier_columns_computed": True,
            "A123_projective_chart_covariance_consumed": True,
            "all_line_charts_selected_by_period_independent_geometry": True,
            "full_tighter_rerun_required": True,
            "selected_handle_periods_computed": False,
            "rank_92_table_assembled": False,
            "integral_branch_selected": False,
        },
    }
    dump(BATCH, batch)
    print(json.dumps(batch, indent=2, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
