from __future__ import annotations

import hashlib
import json
import sys
from pathlib import Path

from flint import acb, ctx


ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))

import build_q79_height4_selected_far_cut_period_source as source_builder
import certify_q79_height4_target_main_hessian_interval as main_hessian
import certify_q79_selected_alignment_E32_handle_combination_interval as handle
import certify_q79_selected_alignment_single_E32_thimble_main_interval as pilot
import certify_q79_selected_side_beta_defect_transport as validated


PACKET = main_hessian.VALIDATED / "far_source" / "d087.1em03.json"


def load(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def require(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)


def main() -> int:
    ctx.dps = 100
    packet = load(PACKET)
    require(
        packet["schema"] == "MTTQ79HeightFourSelectedFarCutPeriodSource.v1",
        "A380FS schema changed",
    )
    require(packet["artifact"] == "A380FS", "A380FS artifact changed")
    target = packet["selected_target"]
    require(int(target["distinguished_index"]) == 87, "A380FS target changed")
    require(target["line_chart"] == "y", "A380FS chart changed")
    require(
        float(target["selected_far_cut_epsilon"]) == 1.0e-3,
        "A380FS far cutoff changed",
    )

    canonical_path = main_hessian.target_paths(87)["canonical_main"]
    canonical = load(canonical_path)
    system, _rank, _row = main_hessian.selected_system(87, 100)
    node = validated.decoded_acb(canonical["certified_node"]["parameter_ball"])
    node_center = handle.midpoint(node)
    epsilon = float(target["selected_far_cut_epsilon"])
    start = handle.midpoint(node_center * acb(format(1.0 - epsilon, ".17g")))
    encoded_start = packet["far_cut_source"]["cutoff_start_binary64"]
    require(
        float(start.real).hex() == encoded_start["real_binary64_hex"],
        "A380FS real cutoff coordinate changed",
    )
    require(
        float(start.imag).hex() == encoded_start["imaginary_binary64_hex"],
        "A380FS imaginary cutoff coordinate changed",
    )

    roots, leading = pilot.roots_at(system, start)
    cut_pair = tuple(int(value) for value in target["preselected_pair_zero_based"])
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
    require(len(stored) == 5, "A380FS period count changed")
    require(
        all(left.overlaps(right) for left, right in zip(replay, stored)),
        "A380FS direct-cut replay lost a full-precision period overlap",
    )
    radius = max(validated.radius_upper(value) for value in stored)
    require(radius < 1.0e-35, "A380FS period source is too wide")
    require(
        float(packet["far_cut_source"]["maximum_period_radius_upper"]) >= radius,
        "A380FS serialized source radius is underreported",
    )

    for label, authority in packet["authority"].items():
        path = ROOT / authority["path"]
        require(path.exists(), f"A380FS authority missing: {label}")
        require(sha256(path) == authority["sha256"], f"A380FS authority stale: {label}")
    scope = packet["strict_scope"]
    require(scope["far_cut_period_source_interval_closed"] is True, "A380FS open")
    require(scope["observed_SM_values_used"] is False, "observed values entered A380FS")
    require(
        scope["far_cut_main_Hessian_interval_closed"] is False,
        "A380FS overpromotes the main Hessian",
    )
    print(
        "PASS: d087 A380FS replays five selected far-cut Arb periods with "
        f"maximum radius {radius:.6e}"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
