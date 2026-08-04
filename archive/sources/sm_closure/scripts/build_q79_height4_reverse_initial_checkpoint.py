from __future__ import annotations

import argparse
import math
from argparse import Namespace
from pathlib import Path

from flint import ctx

import certify_q79_height4_target_main_hessian_interval as base
import run_q79_height4_stable_fast_reverse_target_main_hessian as reverse


def authority(path: Path) -> dict[str, str]:
    return {"path": base.relative(path), "sha256": base.sha256(path)}


def parser() -> argparse.ArgumentParser:
    value = argparse.ArgumentParser()
    value.add_argument("--index", type=int, required=True)
    value.add_argument("--canonical-main", type=Path, required=True)
    value.add_argument("--output", type=Path, required=True)
    value.add_argument("--dps", type=int, default=150)
    value.add_argument("--order", type=int, default=48)
    value.add_argument("--maximum-step", type=float, default=0.02)
    value.add_argument("--minimum-step", type=float, default=1.0e-12)
    value.add_argument("--maximum-lift-correction", type=float, default=1.0e-7)
    value.add_argument("--maximum-output-increment", type=float, default=1.0e-5)
    value.add_argument("--maximum-output-radius", type=float, default=0.005)
    return value


def main() -> int:
    arguments = parser().parse_args()
    arguments.canonical_main = arguments.canonical_main.resolve()
    arguments.output = arguments.output.resolve()
    if not arguments.canonical_main.is_file():
        raise FileNotFoundError("canonical main packet is absent")
    if not 1 <= arguments.index <= 90:
        raise ValueError("index must lie in [1,90]")

    selected_main = base.load(arguments.canonical_main)
    target = selected_main["selected_target"]
    if int(target["distinguished_index"]) != arguments.index:
        raise AssertionError("reverse initializer target identity changed")
    _rank, selected_row, _prior_node = base.tight.configure_selected_target(
        arguments.index
    )
    coefficient = abs(int(selected_row["signed_coefficient"]))
    if coefficient < 1:
        raise AssertionError("selected chain coefficient vanished")

    ctx.dps = arguments.dps
    _node_center, cutoff = base.canonical_cutoff_start(selected_main)
    center, frame, output_radii, source_info, affine_source = (
        reverse.certified_affine_base_state(arguments.index, selected_main)
    )
    paths = base.target_paths(arguments.index)
    paths["canonical_main"] = arguments.canonical_main
    run_arguments = Namespace(
        index=arguments.index,
        dps=arguments.dps,
        order=arguments.order,
        maximum_step=arguments.maximum_step,
        minimum_step=arguments.minimum_step,
        maximum_steps=0,
        maximum_lift_correction=arguments.maximum_lift_correction,
        maximum_output_increment=arguments.maximum_output_increment / coefficient,
        maximum_output_radius=arguments.maximum_output_radius / coefficient,
        resume=False,
        smoke_only=False,
    )
    configuration = reverse.configuration(
        run_arguments,
        paths,
        selected_main,
        cutoff,
        affine_source,
    )
    distance = abs(cutoff)
    if distance <= 0.0:
        raise ArithmeticError("reverse initial path has zero length")

    packet = {
        "schema": "MTTQ79ReverseTargetMainHessianCheckpoint.v1",
        "configuration": configuration,
        "position": "0",
        "proposed_step": format(min(run_arguments.maximum_step, distance / 8.0), ".17g"),
        "center": [base.validated.encoded_acb(value) for value in center],
        "lift_fundamental": base.validated.encoded_matrix(frame.fundamental),
        "coordinate_radii": [str(value) for value in frame.coordinate_radii],
        "output_radii": [str(value) for value in output_radii],
        "accepted_steps": [],
        "rejected_step_count": 0,
        "minimum_accepted_step": format(math.inf, ".17g"),
        "reverse_initial_state_certificate": {
            "status": "CANONICAL_TERMINAL_AFFINE_STATE_REPLAYED_AT_SMOOTH_BASE",
            "initial_period_source": source_info,
            "selected_chain_coefficient_absolute": coefficient,
            "coefficient_scaled_maximum_output_increment": (
                run_arguments.maximum_output_increment
            ),
            "coefficient_scaled_maximum_output_radius": run_arguments.maximum_output_radius,
            "all_72_Hessian_outputs_zero_at_path_origin": all(
                value == 0 for value in output_radii
            ),
            "authority": {
                "ordinary_terminal_affine_source": authority(affine_source),
                "canonical_main": authority(arguments.canonical_main),
                "builder_source": authority(Path(__file__).resolve()),
            },
            "strict_scope": {
                "observed_SM_values_used": False,
                "configuration_derived_from_canonical_target": True,
                "numerical_tolerance_only_scaled_by_preselected_integer_coefficient": True,
                "all_five_affine_period_coordinates_retained": True,
                "puncture_lift_coordinates_retained": True,
                "cycle_or_source_reselected": False,
                "target_main_Hessian_interval_closed": False,
            },
        },
    }
    base.dump(arguments.output, packet)
    print(f"wrote {base.relative(arguments.output)}")
    print(
        f"initial lift radius {base.validated.upper(frame.physical_radius()):.17g}; "
        f"coefficient {coefficient}; output increment "
        f"{run_arguments.maximum_output_increment:.17g}"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
