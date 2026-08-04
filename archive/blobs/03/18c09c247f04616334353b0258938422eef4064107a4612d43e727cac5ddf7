from __future__ import annotations

import hashlib
import json
import sys
from pathlib import Path

from flint import acb, ctx


ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))

import certify_q79_height4_target_main_hessian_interval as main_hessian
import certify_q79_selected_alignment_E32_handle_combination_interval as handle
import certify_q79_selected_alignment_single_E32_thimble_main_interval as pilot
import certify_q79_selected_side_beta_defect_transport as validated


INDICES = (57, 27, 82, 17, 4)
EPSILON = 1.0e-3


def load(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def require(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)


def audit_target(index: int) -> dict[str, float | int | str]:
    packet_path = (
        main_hessian.VALIDATED / "far_source" / f"d{index:03d}.1em03.json"
    )
    packet = load(packet_path)
    require(
        packet["schema"] == "MTTQ79HeightFourSelectedFarCutPeriodSource.v1",
        f"d{index:03d} A380FS schema changed",
    )
    require(packet["artifact"] == "A380FS", f"d{index:03d} artifact changed")

    target = packet["selected_target"]
    require(
        int(target["distinguished_index"]) == index,
        f"d{index:03d} target changed",
    )
    require(
        float(target["selected_far_cut_epsilon"]) == EPSILON,
        f"d{index:03d} far cutoff changed",
    )

    canonical_path = main_hessian.target_paths(index)["canonical_main"]
    canonical = load(canonical_path)
    system, rank, row = main_hessian.selected_system(index, 100)
    canonical_target = canonical["selected_target"]
    require(
        int(target["A219_contribution_rank"]) == rank,
        f"d{index:03d} contribution rank changed",
    )
    require(target["root_id"] == row["root_id"], f"d{index:03d} root changed")
    require(target["line_chart"] == system.line_chart, f"d{index:03d} chart changed")
    require(
        int(target["signed_chain_coefficient"]) == int(row["signed_coefficient"]),
        f"d{index:03d} signed coefficient changed",
    )
    cut_pair = tuple(int(value) for value in target["preselected_pair_zero_based"])
    require(
        cut_pair
        == tuple(
            int(value)
            for value in canonical_target["near_node_colliding_pair_zero_based"]
        ),
        f"d{index:03d} selected pair changed",
    )

    node = validated.decoded_acb(canonical["certified_node"]["parameter_ball"])
    node_center = handle.midpoint(node)
    start = handle.midpoint(node_center * acb(format(1.0 - EPSILON, ".17g")))
    encoded_start = packet["far_cut_source"]["cutoff_start_binary64"]
    require(
        float(start.real).hex() == encoded_start["real_binary64_hex"],
        f"d{index:03d} real cutoff coordinate changed",
    )
    require(
        float(start.imag).hex() == encoded_start["imaginary_binary64_hex"],
        f"d{index:03d} imaginary cutoff coordinate changed",
    )

    roots, leading = pilot.roots_at(system, start)
    minimum_separation = min(
        validated.lower(abs(roots[left] - roots[right]))
        for left in range(len(roots))
        for right in range(left)
    )
    require(minimum_separation > 0.0, f"d{index:03d} root balls overlap")
    replay, _diagnostics = handle.direct_cut_periods(
        roots,
        leading,
        cut_pair,
        segments=int(packet["numerics"]["cut_segments"]),
        tolerance=float(packet["numerics"]["cut_tolerance"]),
    )
    stored = [
        validated.decoded_acb(value)
        for value in packet["far_cut_source"]["full_precision_period_balls"]
    ]
    require(len(stored) == 5, f"d{index:03d} period count changed")
    require(
        all(left.overlaps(right) for left, right in zip(replay, stored)),
        f"d{index:03d} direct-cut replay lost a full-precision overlap",
    )
    radius = max(validated.radius_upper(value) for value in stored)
    require(radius < 1.0e-35, f"d{index:03d} source is too wide")
    require(
        float(packet["far_cut_source"]["maximum_period_radius_upper"]) >= radius,
        f"d{index:03d} source radius is underreported",
    )
    require(
        float(packet["far_cut_source"]["minimum_root_ball_separation_lower"])
        <= minimum_separation,
        f"d{index:03d} root separation is overreported",
    )

    for label, authority in packet["authority"].items():
        path = ROOT / authority["path"]
        require(path.exists(), f"d{index:03d} authority missing: {label}")
        require(
            sha256(path) == authority["sha256"],
            f"d{index:03d} authority stale: {label}",
        )
    scope = packet["strict_scope"]
    require(scope["far_cut_period_source_interval_closed"], f"d{index:03d} source open")
    require(
        not scope["far_cut_main_Hessian_interval_closed"],
        f"d{index:03d} source overclaims transport",
    )
    require(
        not scope["interval_Newton_existence_and_uniqueness_closed"],
        f"d{index:03d} source overclaims Newton",
    )
    require(not scope["observed_SM_values_used"], f"SM data entered d{index:03d}")
    return {
        "index": index,
        "chart": system.line_chart,
        "rank": rank,
        "radius": radius,
        "minimum_root_separation": minimum_separation,
    }


def main() -> int:
    ctx.dps = 100
    rows = [audit_target(index) for index in INDICES]
    print("PASS: independently replayed the five ranked A380FS far-cut sources")
    print(json.dumps(rows, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
