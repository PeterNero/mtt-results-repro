from __future__ import annotations

import argparse
import hashlib
import json
import time
from pathlib import Path

from q79genus2_period_transport import (
    SELECTED_LOCAL_DIRECT_CUTOFFS,
    SELECTED_LOCAL_OUTER_ORDERS,
    execute_thimble_period,
    load_json,
)


ROOT = Path(__file__).resolve().parents[1]
FIBRATION = (
    ROOT
    / "candidate_data"
    / "selected_q79genus2lefschetzperiodreduction"
    / "explicit_genus2_fibration.packet.json"
)
EXPLORATION = (
    ROOT
    / "candidate_data"
    / "selected_q79genus2picardlefschetzmonodromyexecution"
    / "numerical_monodromy_exploration.packet.json"
)
FAN = (
    ROOT
    / "candidate_data"
    / "selected_q79genus2distinguishedcutsystemandglobalrelation"
    / "distinguished_radial_fan.packet.json"
)
TRAJECTORY_DIR = (
    ROOT / "candidate_data" / "selected_q79genus2distinguishedmeridianexecution"
)
OUTPUT_DIR = ROOT / "candidate_data" / "selected_q79genus2thimbleperiodexecution"


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def packet_complex(value: dict) -> complex:
    return complex(float(value["real"]), float(value["imaginary"]))


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser()
    parser.add_argument("--distinguished-index", type=int, required=True)
    parser.add_argument("--epsilon", type=float, default=1.0e-5)
    parser.add_argument("--inner-order", type=int, default=160)
    parser.add_argument("--dps", type=int, default=70)
    parser.add_argument("--root-step-ratio", type=float, default=0.12)
    parser.add_argument("--rtol", type=float, default=2.0e-10)
    parser.add_argument("--atol", type=float, default=2.0e-13)
    parser.add_argument(
        "--gauss-manin-chart",
        choices=("t", "frozen_reciprocal"),
        default="t",
    )
    parser.add_argument("--local-direct-cutoff", type=float)
    parser.add_argument("--local-outer-order", type=int)
    parser.add_argument("--tail-outer-order", type=int, default=24)
    parser.add_argument("--no-save", action="store_true")
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    if not 1 <= args.distinguished_index <= 90:
        raise ValueError("distinguished index must lie in 1,...,90")
    started = time.perf_counter()
    fan = load_json(FAN)
    exploration = load_json(EXPLORATION)
    row = next(
        item
        for item in fan["distinguished_positive_meridians"]
        if item["distinguished_index"] == args.distinguished_index
    )
    stem = f"d{args.distinguished_index:03d}_{row['root_id']}"
    trajectory_packet_path = TRAJECTORY_DIR / f"{stem}.trajectory.packet.json"
    trajectory_packet = load_json(trajectory_packet_path)
    trajectory_path = ROOT / trajectory_packet["trajectory"]["path"]
    chart = trajectory_packet["branch_chart"]["coordinate"]
    if chart == "s_0=1/t":
        omitted = 0j
    elif chart == "s_minus1=1/(t+1)":
        omitted = -1 + 0j
    else:
        raise AssertionError(f"unsupported frozen branch chart: {chart}")

    execution = execute_thimble_period(
        fibration_path=FIBRATION,
        homology_convention=exploration["homology_convention"],
        trajectory_path=trajectory_path,
        trajectory_packet=trajectory_packet,
        critical_center=packet_complex(row["canonical_lift"]),
        omitted=omitted,
        epsilon=args.epsilon,
        inner_order=args.inner_order,
        dps=args.dps,
        root_step_ratio=args.root_step_ratio,
        rtol=args.rtol,
        atol=args.atol,
        gauss_manin_chart=args.gauss_manin_chart,
        local_direct_cutoff=(
            args.local_direct_cutoff
            if args.local_direct_cutoff is not None
            else SELECTED_LOCAL_DIRECT_CUTOFFS.get(args.distinguished_index, 0.0)
        ),
        local_outer_order=(
            args.local_outer_order
            if args.local_outer_order is not None
            else SELECTED_LOCAL_OUTER_ORDERS.get(args.distinguished_index, 32)
        ),
        tail_outer_order=args.tail_outer_order,
    )
    packet = {
        "schema": "MTTQ79SingleDistinguishedThimblePeriodCandidate.v1",
        "status": "PICARD_FUCHS_THIMBLE_PERIOD_CANDIDATE_COMPUTED_INTERVAL_PROMOTION_OPEN",
        "distinguished_index": args.distinguished_index,
        "root_id": row["root_id"],
        "branch_chart": chart,
        "critical_center": row["canonical_lift"],
        "authority": {
            "fibration_sha256": sha256(FIBRATION),
            "distinguished_fan_sha256": sha256(FAN),
            "trajectory_packet_sha256": sha256(trajectory_packet_path),
            "trajectory_npz_sha256": sha256(trajectory_path),
            "period_engine_sha256": sha256(
                ROOT / "scripts" / "q79genus2_period_transport.py"
            ),
        },
        "execution": execution,
        "elapsed_seconds": format(time.perf_counter() - started, ".17g"),
    }
    if not args.no_save:
        OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
        output = OUTPUT_DIR / f"{stem}.thimble_period.candidate.json"
        output.write_text(
            json.dumps(packet, indent=2, sort_keys=True) + "\n",
            encoding="utf-8",
        )
        print(f"wrote {output}")
    print(json.dumps(packet, indent=2, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
