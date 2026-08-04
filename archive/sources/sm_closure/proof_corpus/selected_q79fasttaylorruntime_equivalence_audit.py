from __future__ import annotations

import math
import sys
import time
from pathlib import Path

from flint import acb, arb, ctx


ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))

import certify_q79_height4_rank3_beta_hessian_interval as beta_hessian
import certify_q79_height4_target_main_hessian_interval as main_hessian
import certify_q79_selected_side_beta_defect_transport as validated
import q79_fast_taylor_runtime as fast


TM = validated.TaylorModel


def require(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)


def model(seed: int, order: int, radius: arb) -> TM:
    coefficients = [
        acb(
            format(math.sin(seed + index) / (index + 1), ".17g"),
            format(math.cos(2 * seed + index) / (index + 2), ".17g"),
        )
        for index in range(order + 1)
    ]
    return TM(coefficients, radius, arb("1e-40"))


def main() -> int:
    ctx.dps = 80
    fast.uninstall()
    order = 14
    radius = arb("0.013")
    for seed in range(1, 7):
        left = model(seed, order, radius)
        right = model(seed + 11, order, radius)
        ordinary = fast.ORIGINAL_MULTIPLY(left, right)
        accelerated = fast.multiply(left, right)
        require(
            all(
                current.overlaps(reference)
                for current, reference in zip(
                    accelerated.coefficients, ordinary.coefficients
                )
            ),
            "accelerated product coefficients do not overlap the reference",
        )
        require(
            validated.upper(accelerated.absolute_bound())
            <= validated.upper(ordinary.absolute_bound()) * (1.0 + 1.0e-14),
            "accelerated product bound is wider than the reference",
        )

    index = 87
    system, _rank, _row = main_hessian.selected_system(index, 80)
    packet = main_hessian.load(main_hessian.target_paths(index)["canonical_main"])
    _node, start = main_hessian.canonical_cutoff_start(packet)
    center, frame, radii, _source = main_hessian.initial_state(system, packet, start)
    step = 1.0e-6
    direction = -start / abs(start)

    baseline_started = time.perf_counter()
    baseline = beta_hessian.validated_affine_hessian_step(
        system,
        start,
        direction,
        step,
        center,
        frame,
        radii,
        order=14,
        system_builder=main_hessian.build_homogeneous_hessian_system,
    )
    baseline_elapsed = time.perf_counter() - baseline_started

    center, frame, radii, _source = main_hessian.initial_state(system, packet, start)
    try:
        fast.install()
        accelerated_started = time.perf_counter()
        accelerated = beta_hessian.validated_affine_hessian_step(
            system,
            start,
            direction,
            step,
            center,
            frame,
            radii,
            order=14,
            system_builder=main_hessian.build_homogeneous_hessian_system,
        )
        accelerated_elapsed = time.perf_counter() - accelerated_started
    finally:
        fast.uninstall()

    baseline_center, baseline_frame, baseline_radii, baseline_diagnostics = baseline
    fast_center, fast_frame, fast_radii, fast_diagnostics = accelerated
    require(len(baseline_center) == len(fast_center) == 77, "step state size changed")
    lift_center_difference = max(
        validated.upper(abs(left - right))
        for left, right in zip(baseline_center[:5], fast_center[:5])
    )
    lift_radius_sum = validated.upper(
        baseline_frame.physical_radius() + fast_frame.physical_radius()
    )
    require(
        lift_center_difference <= lift_radius_sum,
        "accelerated lift-center displacement exceeds the combined lift radii",
    )
    require(
        all(
            validated.upper(abs(baseline_center[5 + index] - fast_center[5 + index]))
            <= validated.upper(baseline_radii[index] + fast_radii[index])
            for index in range(72)
        ),
        "accelerated output-center displacement exceeds combined output radii",
    )
    require(
        all(
            float(fast_radii[index].upper())
            <= float(baseline_radii[index].upper()) * (1.0 + 1.0e-10) + 1.0e-70
            for index in range(72)
        ),
        "accelerated output radius exceeds the reference step radius",
    )
    fundamental_difference = max(
        validated.upper(
            abs(
                fast_frame.fundamental[row, column]
                - baseline_frame.fundamental[row, column]
            )
        )
        for row in range(5)
        for column in range(5)
    )
    require(
        fundamental_difference <= 1.0e-30,
        "accelerated lift fundamental differs from the reference by "
        f"{fundamental_difference:.6e}",
    )
    require(
        fast_diagnostics["maximum_output_radius"]
        <= baseline_diagnostics["maximum_output_radius"] * (1.0 + 1.0e-10),
        "accelerated maximum output radius exceeds the reference",
    )
    require(accelerated_elapsed > 0.0 and baseline_elapsed > 0.0, "invalid timing")
    print(
        "PASS: C-backed acb_poly Taylor products and output recurrences overlap "
        "the reference engine; one-step wall-time speedup "
        f"{baseline_elapsed / accelerated_elapsed:.3f}x "
        f"({baseline_elapsed:.3f}s -> {accelerated_elapsed:.3f}s)"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
