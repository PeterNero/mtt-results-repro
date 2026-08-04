from __future__ import annotations

import hashlib
import json
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))

import certify_q79_height4_target_main_hessian_interval as main_hessian
import certify_q79_height4_tight_target_full_residue_interval as tight
import certify_q79_selected_side_beta_defect_transport as validated


PACKET = main_hessian.VALIDATED / "far_source" / "d046.1em03.json"
TIGHT_MAIN = tight.tight_paths(46)["main"]


def load(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def require(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)


def main() -> int:
    packet = load(PACKET)
    ordinary = load(TIGHT_MAIN)
    require(
        packet["schema"] == "MTTQ79HeightFourSelectedFarCutPeriodSource.v1",
        "d046 A380FS schema changed",
    )
    require(packet["artifact"] == "A380FS", "d046 A380FS artifact changed")
    target = packet["selected_target"]
    require(int(target["distinguished_index"]) == 46, "d046 A380FS target changed")
    require(target["line_chart"] == "z", "d046 A380FS chart changed")
    require(
        float(target["selected_far_cut_epsilon"])
        == float(ordinary["selected_target"]["endpoint_cutoff_epsilon"]),
        "d046 far-source and tight ordinary cutoffs differ",
    )
    source_periods = [
        validated.decoded_acb(value)
        for value in packet["far_cut_source"]["full_precision_period_balls"]
    ]
    ordinary_periods = [
        validated.interval_from_bounds(value)
        for value in ordinary["near_node_direct_cycle_interval"][
            "initial_period_intervals"
        ]
    ]
    require(
        len(source_periods) == len(ordinary_periods) == 5,
        "d046 far-source period count changed",
    )
    require(
        all(left.overlaps(right) for left, right in zip(source_periods, ordinary_periods)),
        "d046 selected far source does not overlap the independent tight source",
    )
    require(
        float(packet["far_cut_source"]["maximum_period_radius_upper"]) < 1.0e-35,
        "d046 far source lost full precision",
    )
    for label, authority in packet["authority"].items():
        path = ROOT / authority["path"]
        require(path.exists(), f"d046 A380FS authority missing: {label}")
        require(
            sha256(path) == authority["sha256"],
            f"d046 A380FS authority stale: {label}",
        )
    require(
        packet["strict_scope"]["far_cut_period_source_interval_closed"] is True,
        "d046 A380FS source is open",
    )
    print(
        "PASS: z-chart d046 A380FS overlaps all five independently certified "
        "tight/far ordinary period balls"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
