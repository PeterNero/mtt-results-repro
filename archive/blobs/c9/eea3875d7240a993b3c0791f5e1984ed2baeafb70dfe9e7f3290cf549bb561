from __future__ import annotations

import argparse
import math
from argparse import Namespace
from pathlib import Path

import certify_q79_height4_target_main_hessian_interval as base
import run_q79_height4_stable_fast_reverse_target_main_hessian as reverse


def authority(path: Path) -> dict[str, str]:
    return {"path": base.relative(path), "sha256": base.sha256(path)}


def parser() -> argparse.ArgumentParser:
    value = argparse.ArgumentParser()
    value.add_argument("--index", type=int, required=True)
    value.add_argument("--canonical-main", type=Path, required=True)
    value.add_argument("--reference-checkpoint", type=Path, required=True)
    value.add_argument("--output", type=Path, required=True)
    return value


def main() -> int:
    arguments = parser().parse_args()
    arguments.canonical_main = arguments.canonical_main.resolve()
    arguments.reference_checkpoint = arguments.reference_checkpoint.resolve()
    arguments.output = arguments.output.resolve()
    for path in (arguments.canonical_main, arguments.reference_checkpoint):
        if not path.is_file():
            raise FileNotFoundError(f"reverse initial-state input is absent: {path}")

    reference = base.load(arguments.reference_checkpoint)
    if reference.get("schema") != "MTTQ79ReverseTargetMainHessianCheckpoint.v1":
        raise ValueError("reference checkpoint is not a reverse Hessian checkpoint")
    reference_config = reference["configuration"]
    if int(reference_config["index"]) != arguments.index:
        raise AssertionError("reverse initial-state target changed")
    if reference_config["canonical_main_sha256"] != base.sha256(
        arguments.canonical_main
    ):
        raise AssertionError("reference checkpoint canonical-main authority is stale")

    selected_main = base.load(arguments.canonical_main)
    _node_center, cutoff = base.canonical_cutoff_start(selected_main)
    center, frame, output_radii, source_info, affine_source = (
        reverse.certified_affine_base_state(arguments.index, selected_main)
    )
    paths = base.target_paths(arguments.index)
    paths["canonical_main"] = arguments.canonical_main
    run_arguments = Namespace(
        index=arguments.index,
        dps=int(reference_config["dps"]),
        order=int(reference_config["order"]),
        maximum_step=float(reference_config["maximum_step"]),
        minimum_step=float(reference_config["minimum_step"]),
        maximum_steps=0,
        maximum_lift_correction=float(reference_config["maximum_lift_correction"]),
        maximum_output_increment=float(reference_config["maximum_output_increment"]),
        maximum_output_radius=float(reference_config["maximum_output_radius"]),
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
    replayed_endpoint = base.complex_value(configuration["endpoint"])
    reference_endpoint = base.complex_value(reference_config["endpoint"])
    endpoint_rounding_difference = abs(replayed_endpoint - reference_endpoint)
    if endpoint_rounding_difference > 4.0e-16 * max(1.0, abs(reference_endpoint)):
        raise AssertionError("reverse endpoint differs beyond binary64 replay rounding")
    configuration["endpoint"] = reference_config["endpoint"]
    if configuration != reference_config:
        raise AssertionError("replayed reverse configuration differs from reference")

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
            "status": "CERTIFIED_ORDINARY_TERMINAL_AFFINE_STATE_REPLAYED_AT_SMOOTH_BASE",
            "initial_period_source": source_info,
            "all_72_Hessian_outputs_zero_at_path_origin": all(
                value == 0 for value in output_radii
            ),
            "authority": {
                "ordinary_terminal_affine_source": authority(affine_source),
                "canonical_main": authority(arguments.canonical_main),
                "reference_reverse_checkpoint": authority(
                    arguments.reference_checkpoint
                ),
                "builder_source": authority(Path(__file__).resolve()),
            },
            "strict_scope": {
                "observed_SM_values_used": False,
                "reverse_configuration_exactly_replayed": True,
                "reference_endpoint_rounding_replayed": True,
                "endpoint_rounding_difference": endpoint_rounding_difference,
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
        "initial lift radius "
        f"{base.validated.upper(frame.physical_radius()):.17g}"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
