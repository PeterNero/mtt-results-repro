from __future__ import annotations

import argparse
import hashlib
import json
import math
from pathlib import Path

import numpy as np
from flint import acb, acb_mat, arb, ctx

import certify_q79_height4_target_main_hessian_high_order_interval as high_order
import certify_q79_height4_target_main_hessian_interval as base


ROOT = Path(__file__).resolve().parents[1]


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def relative(path: Path) -> str:
    return str(path.relative_to(ROOT)).replace("\\", "/")


def interval_midpoint(value: dict) -> complex:
    real = (float(value["real"]["lower"]) + float(value["real"]["upper"])) / 2.0
    imaginary = (
        float(value["imaginary"]["lower"])
        + float(value["imaginary"]["upper"])
    ) / 2.0
    return complex(real, imaginary)


def stored_interval_radius(value: dict) -> float:
    return max(
        (float(value["real"]["upper"]) - float(value["real"]["lower"])) / 2.0,
        (
            float(value["imaginary"]["upper"])
            - float(value["imaginary"]["lower"])
        )
        / 2.0,
    )


def parser() -> argparse.ArgumentParser:
    value = base.parser()
    value.add_argument("--cut-tolerance", type=float, default=1.0e-50)
    value.add_argument("--cut-segments", type=int, default=0)
    return value


def main() -> int:
    arguments = parser().parse_args()
    if not 1 <= arguments.index <= 90:
        raise ValueError("index must lie in [1,90]")
    ctx.dps = arguments.dps
    paths = base.target_paths(arguments.index)
    main_packet = base.load(paths["canonical_main"])
    system, _rank, _row = base.selected_system(arguments.index, arguments.dps)
    node_ball = base.validated.decoded_acb(
        main_packet["certified_node"]["parameter_ball"]
    )
    node_center = base.validated.SelectedQ79IntervalSystem.midpoint_acb(node_ball)
    epsilon = float(main_packet["selected_target"]["endpoint_cutoff_epsilon"])
    start_ball = node_center * acb(format(1.0 - epsilon, ".17g"))
    start = base.validated.midpoint(start_ball)
    roots, leading = base.main_engine.pilot.roots_at(system, complex(start))
    pair, pair_diagnostics = base.main_engine.pilot.closest_pair(roots)
    expected_pair = tuple(
        int(value)
        for value in main_packet["selected_target"][
            "near_node_colliding_pair_zero_based"
        ]
    )
    if tuple(pair) != expected_pair:
        raise AssertionError("recomputed cutoff colliding pair changed")
    segments = arguments.cut_segments or int(
        main_packet["near_node_direct_cycle_interval"]["theta_segments"]
    )
    initial_periods, cut_diagnostics = base.main_engine.handle.direct_cut_periods(
        roots,
        leading,
        pair,
        segments=segments,
        tolerance=arguments.cut_tolerance,
    )
    stored = np.asarray(
        [
            interval_midpoint(value)
            for value in main_packet["near_node_direct_cycle_interval"][
                "initial_period_intervals"
            ]
        ],
        dtype=np.complex128,
    )
    recomputed = np.asarray(
        [base.validated.midpoint(value) for value in initial_periods],
        dtype=np.complex128,
    )
    plus = float(np.max(abs(recomputed - stored)))
    minus = float(np.max(abs(-recomputed - stored)))
    orientation = 1 if plus <= minus else -1
    selected_difference = min(plus, minus)
    rejected_difference = max(plus, minus)
    if rejected_difference <= 1000.0 * max(selected_difference, 1.0e-15):
        raise AssertionError("recomputed cutoff-cycle orientation is not separated")
    initial_periods = [acb(orientation) * value for value in initial_periods]
    recomputed_radius = max(
        base.validated.radius_upper(value) for value in initial_periods
    )
    stored_radius = max(
        stored_interval_radius(value)
        for value in main_packet["near_node_direct_cycle_interval"][
            "initial_period_intervals"
        ]
    )
    if not recomputed_radius < stored_radius:
        raise AssertionError("recomputed cutoff periods did not tighten JSON bounds")

    def recomputed_initial_state(
        _main_packet: dict,
    ) -> tuple[list[acb], base.validated.LiftErrorFrame, list[arb]]:
        center = [
            base.validated.SelectedQ79IntervalSystem.midpoint_acb(value)
            for value in initial_periods
        ] + [acb(0) for _ in range(72)]
        fundamental = acb_mat(5, 5)
        for index in range(5):
            fundamental[index, index] = acb(1)
        frame = base.validated.LiftErrorFrame(
            fundamental=fundamental,
            coordinate_radii=[value.rad().upper() for value in initial_periods],
        )
        return center, frame, [arb(0) for _ in range(72)]

    original_initial_state = base.initial_state
    original_smoke_gate = base.coefficient_difference
    base.initial_state = recomputed_initial_state
    if arguments.order >= 12:
        base.coefficient_difference = high_order.coefficient_overlap_gate
    try:
        payload = base.execute(arguments)
    finally:
        base.initial_state = original_initial_state
        base.coefficient_difference = original_smoke_gate
    if arguments.smoke_only:
        return 0

    payload["artifact"] = "A380R"
    payload["recomputed_cutoff_initialization"] = {
        "method": "same selected direct-cut cycle recomputed before transport",
        "colliding_pair_zero_based": list(pair),
        "pair_diagnostics": pair_diagnostics,
        "theta_segments": segments,
        "cut_tolerance": arguments.cut_tolerance,
        "orientation_sign_against_canonical_packet": orientation,
        "selected_center_difference": selected_difference,
        "opposite_center_difference": rejected_difference,
        "maximum_recomputed_component_radius_upper": recomputed_radius,
        "maximum_stored_JSON_component_radius_upper": stored_radius,
        "stored_to_recomputed_radius_ratio_lower": stored_radius
        / recomputed_radius,
        "cut_diagnostics": cut_diagnostics,
    }
    payload["authority"]["recomputed_cutoff_initializer"] = {
        "path": relative(Path(__file__).resolve()),
        "sha256": sha256(Path(__file__).resolve()),
    }
    payload["strict_scope"][
        "same_source_cutoff_periods_recomputed_without_JSON_width"
    ] = True
    if arguments.order >= 12:
        payload["strict_scope"][
            "high_order_smoke_interval_overlap_adapter_used"
        ] = True
    base.dump(paths["output"], payload)
    with paths["note"].open("a", encoding="utf-8") as note:
        note.write(
            "\nA380R recomputed the same selected cutoff direct-cycle periods "
            "in Arb before transport instead of reloading their 17-digit JSON "
            "display bounds. The selected pair and orientation replay exactly; "
            f"the maximum initial radius tightened by a factor greater than "
            f"`{stored_radius / recomputed_radius:.12g}`.\n"
        )
    print(f"promoted {relative(paths['output'])} with A380R authority")
    print(
        json.dumps(
            {
                "stored_radius": stored_radius,
                "recomputed_radius": recomputed_radius,
                "radius_reduction_factor": stored_radius / recomputed_radius,
            },
            indent=2,
        )
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
