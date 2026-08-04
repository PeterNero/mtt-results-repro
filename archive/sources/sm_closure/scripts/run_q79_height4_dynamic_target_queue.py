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
VALIDATED = PROBE / "validated_transport"
BOUNDARY = PROBE / "rank3_complex_PGL3_floating_boundary.packet.json"
CURRENT = VALIDATED / "n3.certified.current.recomposition.json"
MANIFEST = VALIDATED / "n3.dynamic_targets.manifest.json"
TARGET_RUNNER = ROOT / "scripts" / "certify_q79_height4_dynamic_target_full_residue_interval.py"
PREFIX_BUILDER = ROOT / "scripts" / "build_q79_height4_dynamic_certified_prefix_recomposition.py"
TARGET_AUDIT = ROOT / "proof_corpus" / "selected_q79heightfourdynamictargetmanifest_audit.py"
PREFIX_AUDIT = ROOT / "proof_corpus" / "selected_q79heightfourdynamiccertifiedprefixrecomposition_audit.py"


def load(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def run(command: list[str]) -> None:
    print("RUN:", " ".join(command), flush=True)
    subprocess.run(command, cwd=ROOT, check=True)


def certified_rank() -> int:
    if not CURRENT.exists():
        return 15
    return int(load(CURRENT)["certified_A219_priority_prefix_length"])


def target_already_certified(rank: int, index: int) -> bool:
    if not MANIFEST.exists():
        return False
    manifest = load(MANIFEST)
    matches = [
        row
        for row in manifest["targets_in_A219_priority_order"]
        if int(row["A219_priority_rank"]) == rank
        and int(row["distinguished_index"]) == index
    ]
    if len(matches) != 1:
        return False
    return (ROOT / matches[0]["full_interval_path"]).exists()


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--through-rank", type=int, default=76)
    parser.add_argument("--cooling-pause-every", type=int, default=20)
    parser.add_argument("--cooling-pause-seconds", type=float, default=2.0)
    arguments = parser.parse_args()
    if not 16 <= arguments.through_rank <= 76:
        raise ValueError("--through-rank must lie in 16..76")

    ranked = load(BOUNDARY)["difference_decomposition"][
        "ranked_thimble_contributions"
    ]
    start = certified_rank() + 1
    if start > arguments.through_rank:
        print(
            f"dynamic queue already certified through rank {certified_rank()}",
            flush=True,
        )
        return 0
    for rank in range(start, arguments.through_rank + 1):
        row = ranked[rank - 1]
        index = int(row["distinguished_index"])
        artifact = f"A{220 + 2 * rank}"
        print(
            f"\n=== A219 rank {rank}/76: d{index:03d} {row['root_id']} "
            f"coefficient {int(row['signed_coefficient']):+d} ===",
            flush=True,
        )
        if not target_already_certified(rank, index):
            run(
                [
                    sys.executable,
                    str(TARGET_RUNNER),
                    "--index",
                    str(index),
                    "--artifact",
                    artifact,
                    "--phase",
                    "all",
                    "--cooling-pause-every",
                    str(arguments.cooling_pause_every),
                    "--cooling-pause-seconds",
                    str(arguments.cooling_pause_seconds),
                ]
            )
        else:
            print("target interval already present and manifest-listed", flush=True)
        run([sys.executable, str(PREFIX_BUILDER), "--rank", str(rank)])
        run([sys.executable, str(TARGET_AUDIT)])
        run([sys.executable, str(PREFIX_AUDIT)])
        print(f"completed and audited dynamic prefix rank {rank}/76", flush=True)
    print("dynamic target queue completed", flush=True)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
