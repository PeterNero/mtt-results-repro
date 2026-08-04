from __future__ import annotations

import argparse
import copy
import json
from pathlib import Path

from flint import acb, acb_mat, arb

import certify_q79_height4_target_main_hessian_interval as base


def authority(path: Path) -> dict[str, str]:
    return {"path": base.relative(path), "sha256": base.sha256(path)}


def parser() -> argparse.ArgumentParser:
    value = argparse.ArgumentParser()
    value.add_argument("--index", type=int, required=True)
    value.add_argument("--checkpoint", type=Path, required=True)
    value.add_argument("--output", type=Path, required=True)
    value.add_argument("--reframed-checkpoint", type=Path, required=True)
    return value


def main() -> int:
    arguments = parser().parse_args()
    arguments.checkpoint = arguments.checkpoint.resolve()
    arguments.output = arguments.output.resolve()
    arguments.reframed_checkpoint = arguments.reframed_checkpoint.resolve()
    packet = base.load(arguments.checkpoint)
    if packet.get("schema") not in {
        "MTTQ79TargetMainHessianCheckpoint.v1",
        "MTTQ79ReverseTargetMainHessianCheckpoint.v1",
    }:
        raise ValueError("unsupported Hessian checkpoint schema")
    if int(packet["configuration"]["index"]) != arguments.index:
        raise AssertionError("affine reframe target changed")
    frame = base.validated.LiftErrorFrame(
        fundamental=base.validated.decoded_matrix(packet["lift_fundamental"]),
        coordinate_radii=[arb(value) for value in packet["coordinate_radii"]],
    )
    old_physical_radius = base.validated.upper(frame.physical_radius())
    coordinate_bounds = []
    for row in range(5):
        bound = arb(0)
        for column in range(5):
            bound += abs(frame.fundamental[row, column]) * frame.coordinate_radii[column]
        coordinate_bounds.append(bound)
    new_physical_radius = max(base.validated.upper(value) for value in coordinate_bounds)
    if new_physical_radius > old_physical_radius * (1.0 + 1.0e-12):
        raise AssertionError("coordinate-box hull exceeds the recorded physical radius")

    certificate = {
        "schema": "MTTQ79HeightFourCheckpointAffineBoxReframe.v1",
        "status": "FIVE_COORDINATE_AFFINE_ZONOTOPE_REFRAMED_BY_IDENTITY_BOX_HULL",
        "artifact": "A380RB",
        "distinguished_index": arguments.index,
        "checkpoint_schema": packet["schema"],
        "path_position": packet["position"],
        "coordinate_box_radius_uppers": [
            base.validated.upper(value) for value in coordinate_bounds
        ],
        "old_physical_radius_upper": old_physical_radius,
        "new_physical_radius_upper": new_physical_radius,
        "inclusion_identity": "|F e|_i <= sum_j |F_ij| r_j",
        "same_center_outputs_and_output_radii_retained": True,
        "authority": {
            "input_checkpoint": authority(arguments.checkpoint),
            "builder_source": authority(Path(__file__).resolve()),
        },
        "strict_scope": {
            "observed_SM_values_used": False,
            "five_coordinate_affine_lift_retained": True,
            "puncture_lift_coordinates_retained": True,
            "old_affine_zonotope_contained_in_new_identity_box": True,
            "cycle_or_source_reselected": False,
            "affine_box_reframe_closed": True,
            "target_main_Hessian_interval_closed": False,
            "full_SM_closure_proved": False,
        },
    }
    base.dump(arguments.output, certificate)

    reframed = copy.deepcopy(packet)
    identity = acb_mat(5, 5)
    for index in range(5):
        identity[index, index] = acb(1)
    reframed["lift_fundamental"] = base.validated.encoded_matrix(identity)
    reframed["coordinate_radii"] = [str(value) for value in coordinate_bounds]
    reframed["affine_box_reframe"] = {
        "certificate": authority(arguments.output),
        "same_center_outputs_and_output_radii_retained": True,
        "old_affine_zonotope_contained_in_new_identity_box": True,
    }
    base.dump(arguments.reframed_checkpoint, reframed)
    print(f"wrote {base.relative(arguments.output)}")
    print(f"wrote {base.relative(arguments.reframed_checkpoint)}")
    print(json.dumps({
        "old_physical_radius_upper": old_physical_radius,
        "new_physical_radius_upper": new_physical_radius,
        "maximum_coordinate_box_radius_upper": new_physical_radius,
    }, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
