from __future__ import annotations

import argparse
import json
import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
PROBE = (
    ROOT
    / "candidate_data"
    / "selected_q79covariantperiodbranchcutsetandtightbetatransport"
    / "selected_alignment_thimble_periods"
    / "covariant_floating_probe"
)
BOUNDARY = PROBE / "rank3_complex_PGL3_floating_boundary.packet.json"
VALIDATED = PROBE / "validated_transport"
WORKER = ROOT / "scripts" / "precompute_q79_height4_dynamic_target_main.py"


def load(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def main_is_complete(index: int) -> bool:
    checkpoint = VALIDATED / f"d{index:03d}.n3.main8.refined.checkpoint.json"
    main_packet = VALIDATED / f"d{index:03d}.n3.main8.refined.json"
    if not checkpoint.exists() or not main_packet.exists():
        return False
    return bool(load(checkpoint).get("complete"))


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--from-rank", type=int, default=25)
    parser.add_argument("--through-rank", type=int, default=76)
    parser.add_argument("--cooling-pause-every", type=int, default=20)
    parser.add_argument("--cooling-pause-seconds", type=float, default=2.0)
    arguments = parser.parse_args()
    if not 16 <= arguments.from_rank <= arguments.through_rank <= 76:
        raise ValueError("require 16 <= from-rank <= through-rank <= 76")

    ranked = load(BOUNDARY)["difference_decomposition"][
        "ranked_thimble_contributions"
    ]
    for rank in range(arguments.from_rank, arguments.through_rank + 1):
        row = ranked[rank - 1]
        index = int(row["distinguished_index"])
        artifact = f"A{220 + 2 * rank}"
        if main_is_complete(index):
            print(f"main phase already complete for rank {rank} d{index:03d}", flush=True)
            continue
        print(
            f"\n=== PRECOMPUTE A219 rank {rank}/76: d{index:03d} "
            f"{row['root_id']} ===",
            flush=True,
        )
        subprocess.run(
            [
                sys.executable,
                str(WORKER),
                "--index",
                str(index),
                "--artifact",
                artifact,
                "--phase",
                "main",
                "--cooling-pause-every",
                str(arguments.cooling_pause_every),
                "--cooling-pause-seconds",
                str(arguments.cooling_pause_seconds),
            ],
            cwd=ROOT,
            check=True,
        )
        print(f"precomputed main phase rank {rank}/76", flush=True)
    print("dynamic main-phase precompute queue completed", flush=True)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
