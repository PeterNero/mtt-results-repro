from __future__ import annotations

import hashlib
import json
from pathlib import Path

from flint import ctx

import certify_q79_height4_target_main_hessian_interval as base


ROOT = Path(__file__).resolve().parents[1]


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def relative(path: Path) -> str:
    return str(path.relative_to(ROOT)).replace("\\", "/")


def coefficient_overlap_gate(left: base.TM, right: base.TM) -> float:
    radius = base.validated.upper(left.radius)
    center_difference = 0.0
    coefficient_uncertainty = 0.0
    power = 1.0
    for left_value, right_value in zip(left.coefficients, right.coefficients):
        center_difference += abs(
            base.validated.midpoint(left_value)
            - base.validated.midpoint(right_value)
        ) * power
        coefficient_uncertainty += (
            base.validated.radius_upper(left_value)
            + base.validated.radius_upper(right_value)
        ) * power
        power *= radius
    uncertainty = (
        coefficient_uncertainty
        + base.validated.upper(left.remainder)
        + base.validated.upper(right.remainder)
    )
    return 0.0 if center_difference <= uncertainty else float("inf")


def main() -> int:
    arguments = base.parser().parse_args()
    if arguments.order < 12:
        raise ValueError("the high-order adapter requires Taylor order at least 12")
    if not 1 <= arguments.index <= 90:
        raise ValueError("index must lie in [1,90]")
    ctx.dps = arguments.dps
    a378 = base.load(base.A378)
    if not a378["strict_scope"][
        "all_64_homogeneous_period_hessian_integrand_rows_derived"
    ]:
        raise AssertionError("high-order transport requires A378")

    original_gate = base.coefficient_difference
    base.coefficient_difference = coefficient_overlap_gate
    try:
        payload = base.execute(arguments)
    finally:
        base.coefficient_difference = original_gate
    if arguments.smoke_only:
        return 0

    paths = base.target_paths(arguments.index)
    payload["artifact"] = "A380H"
    payload["smoke_test"][
        "ordinary_main_system_coefficient_intervals_all_overlap"
    ] = True
    payload["authority"]["high_order_interval_overlap_adapter"] = {
        "path": relative(Path(__file__).resolve()),
        "sha256": sha256(Path(__file__).resolve()),
    }
    payload["strict_scope"][
        "high_order_smoke_interval_overlap_adapter_used"
    ] = True
    base.dump(paths["output"], payload)
    with paths["note"].open("a", encoding="utf-8") as note:
        note.write(
            "\nThe order-12+ execution used A380H's coefficientwise interval-"
            "overlap smoke gate. This replaces no transport equation or error "
            "bound; it records the rigorous overlap of differently associated "
            "Taylor coefficient balls.\n"
        )
    print(f"promoted {relative(paths['output'])} with A380H authority")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
