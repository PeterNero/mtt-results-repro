from __future__ import annotations

import json
import math
import sys
from pathlib import Path

from flint import acb, ctx


ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))

import certify_q79_height4_target_main_hessian_interval as main_hessian
import certify_q79_selected_side_beta_defect_transport as validated


def load(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def require(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)


def independent_canonical_start(packet: dict) -> tuple[complex, complex]:
    node = validated.decoded_acb(packet["certified_node"]["parameter_ball"])
    node_center = complex(float(node.real.mid()), float(node.imag.mid()))
    epsilon = float(packet["selected_target"]["endpoint_cutoff_epsilon"])
    start_ball = node_center * acb(format(1.0 - epsilon, ".17g"))
    start = complex(float(start_ball.real.mid()), float(start_ball.imag.mid()))
    return node_center, start


def check_target(index: int, expected_chart: str) -> dict:
    packet = load(main_hessian.target_paths(index)["canonical_main"])
    system, _rank, _row = main_hessian.selected_system(index, 90)
    require(system.line_chart == expected_chart, f"d{index:03d} chart changed")

    expected_node, expected_start = independent_canonical_start(packet)
    node, start = main_hessian.canonical_cutoff_start(packet)
    require(node == expected_node, f"d{index:03d} node midpoint replay changed")
    require(start == expected_start, f"d{index:03d} cutoff start replay changed")

    center, frame, output_radii, source = main_hessian.initial_state(
        system, packet, start
    )
    require(len(center) == 77, f"d{index:03d} initial state width changed")
    require(len(frame.coordinate_radii) == 5, f"d{index:03d} frame width changed")
    require(len(output_radii) == 72, f"d{index:03d} output width changed")
    require(
        source["canonical_display_intervals_overlap_all_five"] is True,
        f"d{index:03d} current-source periods left the ordinary certificate",
    )
    require(
        all(source["canonical_display_overlap_by_period"]),
        f"d{index:03d} lost a cutoff-period overlap",
    )
    radius = float(source["maximum_full_precision_period_radius_upper"])
    require(math.isfinite(radius), f"d{index:03d} initializer radius is nonfinite")
    require(0.0 < radius < 1.0e-35, f"d{index:03d} initializer lost Arb precision")
    require(
        len(source["full_precision_period_balls"]) == 5,
        f"d{index:03d} full-precision period inventory changed",
    )
    require(
        source["canonical_pair_zero_based"]
        == packet["selected_target"]["near_node_colliding_pair_zero_based"],
        f"d{index:03d} cutoff pair changed",
    )
    require(
        float(source["minimum_cutoff_root_ball_separation_lower"]) > 0.0,
        f"d{index:03d} cutoff roots are not separated",
    )
    return {
        "index": index,
        "chart": expected_chart,
        "maximum_period_radius": radius,
        "maximum_display_difference": float(
            source["maximum_canonical_display_interval_difference_upper"]
        ),
    }


def main() -> int:
    ctx.dps = 90
    rows = [check_target(87, "y"), check_target(65, "z")]
    print(
        "PASS: canonical cutoff rounding and full-precision direct-cut initializers "
        f"replay on y/z representatives {rows}"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
