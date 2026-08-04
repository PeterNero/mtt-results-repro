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
PRIMITIVE_TABLE = OUTPUT_DIR / "primitive_thimble_period_candidate_table.packet.json"
CLOSED_TABLE = OUTPUT_DIR / "closed_thimble_period_candidate_table.packet.json"
BATCH = OUTPUT_DIR / "distinguished_thimble_period_batch.packet.json"


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


def parse_complex(value: dict) -> complex:
    return complex(float(value["real"]), float(value["imaginary"]))


def packet_complex(value: complex) -> dict[str, str]:
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
    args = parse_args()
    started = time.perf_counter()
    fan = load(FAN)
    rows = fan["distinguished_positive_meridians"]
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

    def output_path(row: dict) -> Path:
        return OUTPUT_DIR / (
            f"d{row['distinguished_index']:03d}_{row['root_id']}"
            ".thimble_period.candidate.json"
        )

    def run(row: dict) -> tuple[int, str]:
        output = output_path(row)
        if output.exists() and not args.force:
            return row["distinguished_index"], "cached"
        command = [
            sys.executable,
            str(SINGLE),
            "--distinguished-index",
            str(row["distinguished_index"]),
            "--epsilon",
            format(args.epsilon, ".17g"),
            "--inner-order",
            str(args.inner_order),
            "--dps",
            str(args.dps),
            "--root-step-ratio",
            format(args.root_step_ratio, ".17g"),
            "--rtol",
            format(args.rtol, ".17g"),
            "--atol",
            format(args.atol, ".17g"),
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
        return row["distinguished_index"], "computed"

    statuses: dict[int, str] = {}
    with concurrent.futures.ThreadPoolExecutor(max_workers=args.jobs) as pool:
        futures = {pool.submit(run, row): row for row in rows}
        for future in concurrent.futures.as_completed(futures):
            index, status = future.result()
            statuses[index] = status
            print(f"d{index:03d}: {status}", flush=True)

    packets = [load(output_path(row)) for row in rows]
    if [packet["distinguished_index"] for packet in packets] != list(range(1, 91)):
        raise AssertionError("period packet order")
    if any(
        not packet["execution"]["strict_scope"][
            "Picard_Fuchs_continuation_executed"
        ]
        for packet in packets
    ):
        raise AssertionError("missing Picard-Fuchs execution")
    engine_hash = sha256(ENGINE)
    if any(
        packet["authority"]["period_engine_sha256"] != engine_hash
        for packet in packets
    ):
        raise AssertionError("mixed or stale period-engine authority")

    form_names = packets[0]["execution"]["form_names"]
    primitive = np.asarray(
        [
            [
                parse_complex(value)
                for value in packet["execution"]["period_values"]
            ]
            for packet in packets
        ],
        dtype=np.complex128,
    ).T
    if primitive.shape != (8, 90):
        raise AssertionError("primitive table shape")
    primitive_payload = {
        "schema": "MTTQ79PrimitiveThimblePeriodCandidateTable.v1",
        "status": "EIGHT_BY_NINETY_PICARD_FUCHS_THIMBLE_CANDIDATE_COMPUTED_INTERVAL_PROMOTION_OPEN",
        "form_names": form_names,
        "column_distinguished_indices": list(range(1, 91)),
        "column_root_ids": [packet["root_id"] for packet in packets],
        "period_rows": [
            [packet_complex(value) for value in row] for row in primitive
        ],
        "orientation_scope": "Independent sign reversal of a primitive thimble column is an integral basis change; the frozen convention is the endpoint-transposition root-label order.",
        "strict_scope": {
            "floating_candidate_entries": 720,
            "interval_certified_entries": 0,
            "integral_H2_columns_promoted": 0,
        },
    }
    dump(PRIMITIVE_TABLE, primitive_payload)

    cycle_presentation = load(CYCLE_PRESENTATION)
    kernel = np.asarray(
        cycle_presentation["thimble_boundary_lattice"][
            "closed_thimble_kernel_basis_columns"
        ],
        dtype=np.int64,
    )
    closed = primitive @ kernel
    if closed.shape != (8, 86):
        raise AssertionError("closed-thimble table shape")
    closed_payload = {
        "schema": "MTTQ79ClosedThimblePeriodCandidateTable.v1",
        "status": "EIGHT_BY_EIGHTY_SIX_CLOSED_THIMBLE_CANDIDATE_COMPUTED_INTERVAL_PROMOTION_OPEN",
        "form_names": form_names,
        "kernel_basis_sha256": hashlib.sha256(kernel.tobytes()).hexdigest(),
        "period_rows": [
            [packet_complex(value) for value in row] for row in closed
        ],
        "assembly": "Pi_closed=T_8x90*K_90x86",
        "maximum_absolute_entry": format(float(np.max(np.abs(closed))), ".17g"),
        "strict_scope": {
            "floating_candidate_entries": 688,
            "interval_certified_entries": 0,
            "closed_integral_columns_promoted": 0,
        },
    }
    dump(CLOSED_TABLE, closed_payload)

    numerics = [packet["execution"]["numerics"] for packet in packets]
    batch = {
        "schema": "MTTQ79DistinguishedThimblePeriodBatch.v1",
        "status": "ALL_NINETY_THIMBLE_PERIOD_CANDIDATES_COMPUTED_INTERVAL_PROMOTION_OPEN",
        "counts": {
            "computed_this_run": sum(value == "computed" for value in statuses.values()),
            "cached_this_run": sum(value == "cached" for value in statuses.values()),
            "complete_period_packets": len(packets),
            "primitive_complex_entries": int(primitive.size),
            "closed_thimble_complex_entries": int(closed.size),
            "high_precision_Gauss_Manin_connection_evaluations": sum(
                int(row["high_precision_Gauss_Manin_connection_evaluations"])
                for row in numerics
            ),
            "desingularized_local_direct_columns": sum(
                float(row["local_direct_cutoff"]) > 0 for row in numerics
            ),
        },
        "authority": {
            "period_engine_sha256": engine_hash,
            "distinguished_fan_sha256": sha256(FAN),
            "integral_cycle_presentation_sha256": sha256(CYCLE_PRESENTATION),
        },
        "maximums": {
            "Gauss_Manin_reduction_condition_number": format(
                max(float(row["maximum_reduction_condition_number"]) for row in numerics),
                ".17g",
            ),
            "Gauss_Manin_reduction_relative_residual": format(
                max(float(row["maximum_reduction_relative_residual"]) for row in numerics),
                ".17g",
            ),
            "equilibrated_Gauss_Manin_reduction_condition_number": format(
                max(
                    float(row["maximum_equilibrated_reduction_condition_number"])
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
            "root_transport_solve_count": max(
                int(row["root_transport_solve_count"]) for row in numerics
            ),
        },
        "minimums": {
            "initial_other_root_normalized_clearance": format(
                min(float(row["initial_other_root_normalized_clearance"]) for row in numerics),
                ".17g",
            ),
            "local_direct_other_root_normalized_clearance": format(
                min(
                    float(row["local_direct_minimum_other_root_normalized_clearance"])
                    for row in numerics
                    if float(row["local_direct_cutoff"]) > 0
                ),
                ".17g",
            ),
            "endpoint_tail_other_root_normalized_clearance": format(
                min(
                    float(row["endpoint_tail_minimum_other_root_normalized_clearance"])
                    for row in numerics
                ),
                ".17g",
            ),
        },
        "outputs": {
            "primitive_table": str(PRIMITIVE_TABLE.relative_to(ROOT)).replace("\\", "/"),
            "primitive_table_sha256": sha256(PRIMITIVE_TABLE),
            "closed_table": str(CLOSED_TABLE.relative_to(ROOT)).replace("\\", "/"),
            "closed_table_sha256": sha256(CLOSED_TABLE),
        },
        "elapsed_seconds": format(time.perf_counter() - started, ".17g"),
        "strict_scope": {
            "all_90_Picard_Fuchs_candidates_computed": True,
            "representative_convergence_audit_required": True,
            "interval_promotion_closed": False,
            "handle_periods_computed": False,
            "Leray_edge_periods_computed": False,
            "integral_branch_selected": False,
        },
    }
    dump(BATCH, batch)
    print(json.dumps(batch, indent=2, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
