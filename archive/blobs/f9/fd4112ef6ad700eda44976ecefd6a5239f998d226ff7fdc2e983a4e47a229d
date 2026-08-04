from __future__ import annotations

import math
import sys
from pathlib import Path

from flint import acb, arb, ctx


ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))

import certify_q79_height4_rank3_beta_hessian_interval as beta_hessian
import certify_q79_height4_target_main_hessian_interval as main_hessian
import certify_q79_selected_side_beta_defect_transport as validated
import q79_fast_taylor_runtime as fast
import q79_stable_affine_hessian_runtime as stable


def require(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)


def main() -> int:
    ctx.dps = 90
    linear = arb(0, "1e-100")
    affine = arb("2e-80")
    step_ball = arb("1e-4")
    growth, forced = stable.exponential_integral_upper_bound(
        linear, affine, step_ball
    )
    require(math.isfinite(validated.upper(growth)), "growth bound is non-finite")
    require(math.isfinite(validated.upper(forced)), "forced bound is non-finite")
    require(
        validated.lower(forced) >= 0.0,
        "stable exponential-integral enclosure is not nonnegative",
    )

    index = 87
    system, _rank, _row = main_hessian.selected_system(index, 90)
    packet = main_hessian.load(main_hessian.target_paths(index)["canonical_main"])
    _node, start = main_hessian.canonical_cutoff_start(packet)
    center, frame, radii, _source = main_hessian.initial_state(system, packet, start)
    direction = -start / abs(start)
    step = 1.0e-6
    fast.install()
    try:
        baseline = stable.ORIGINAL_STEP(
            system,
            start,
            direction,
            step,
            center,
            frame,
            radii,
            order=16,
            system_builder=main_hessian.build_homogeneous_hessian_system,
        )
        candidate = stable.stable_validated_affine_hessian_step(
            system,
            start,
            direction,
            step,
            center,
            frame,
            radii,
            order=16,
            system_builder=main_hessian.build_homogeneous_hessian_system,
        )
    finally:
        fast.uninstall()

    baseline_center, baseline_frame, baseline_radii, baseline_diagnostics = baseline
    stable_center, stable_frame, stable_radii, stable_diagnostics = candidate
    require(
        all(left.overlaps(right) for left, right in zip(baseline_center, stable_center)),
        "stable step changed the endpoint center enclosure",
    )
    require(
        validated.upper(stable_frame.physical_radius())
        >= validated.lower(baseline_frame.physical_radius()),
        "stable lift frame does not include the reference-radius scale",
    )
    require(
        all(
            validated.upper(current) >= validated.lower(reference)
            for current, reference in zip(stable_radii, baseline_radii)
        ),
        "stable output radius falls below a reference output radius",
    )
    require(
        stable_diagnostics["all_returned_bounds_finite"],
        "stable finite gate did not pass",
    )
    require(
        stable_diagnostics["maximum_output_radius"]
        >= baseline_diagnostics["maximum_output_radius"],
        "stable majorant unexpectedly narrowed the reference step",
    )
    print(
        "PASS: A*h*exp(L*h) is finite for a zero-containing L interval and "
        "the stable affine-Hessian step contains the reference finite step"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
