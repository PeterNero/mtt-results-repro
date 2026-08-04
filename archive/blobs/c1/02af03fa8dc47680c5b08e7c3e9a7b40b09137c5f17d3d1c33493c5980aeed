from __future__ import annotations

import argparse
import json
import math
from pathlib import Path

import numpy as np
from flint import acb, arb, ctx

import certify_q79_height4_target_main_hessian_interval as base
import q79_fast_taylor_runtime as fast
import q79_stable_affine_hessian_runtime as stable
import run_q79_height4_stable_fast_reverse_target_main_hessian as reverse


ROOT = Path(__file__).resolve().parents[1]
FAST_AUDIT = ROOT / "proof_corpus" / "selected_q79fasttaylorruntime_equivalence_audit.py"
STABLE_AUDIT = (
    ROOT / "proof_corpus" / "selected_q79stableaffinehessianruntime_inclusion_audit.py"
)
ARTIFACT = "A380BD"


def complex_value(value: dict[str, str]) -> complex:
    return complex(float(value["real"]), float(value["imaginary"]))


def authority(path: Path) -> dict[str, str]:
    return {"path": base.relative(path), "sha256": base.sha256(path)}


def decoded_checkpoint(path: Path, schema: str) -> tuple[dict, list[acb], object, list[arb]]:
    packet = base.load(path)
    if packet.get("schema") != schema:
        raise ValueError(f"checkpoint schema changed: {path.name}")
    center = [base.validated.decoded_acb(value) for value in packet["center"]]
    frame = base.validated.LiftErrorFrame(
        fundamental=base.validated.decoded_matrix(packet["lift_fundamental"]),
        coordinate_radii=[arb(value) for value in packet["coordinate_radii"]],
    )
    radii = [arb(value) for value in packet["output_radii"]]
    if len(center) != 77 or len(radii) != 72:
        raise AssertionError("bidirectional checkpoint state dimensions changed")
    return packet, center, frame, radii


def audit_steps(packet: dict, position: float, *, stable_required: bool) -> None:
    cursor = 0.0
    for step in packet["accepted_steps"]:
        start = float(step["start_arclength"])
        end = float(step["end_arclength"])
        width = float(step["step"])
        tolerance = 2.0e-14 * max(1.0, abs(cursor), abs(start), abs(end))
        if abs(start - cursor) > tolerance or abs((end - start) - width) > tolerance:
            raise AssertionError("checkpoint accepted-step chain is not contiguous")
        if not end > start or not width > 0.0:
            raise AssertionError("checkpoint accepted step is not positive")
        if stable_required:
            if step.get("affine_growth_integral_bound") != "A*h*exp(L*h)":
                raise AssertionError("checkpoint does not carry the stable growth majorant")
            if step.get("zero_linear_defect_regularization_by_division") is not False:
                raise AssertionError("checkpoint used forbidden zero-defect division")
        cursor = end
    tolerance = 2.0e-14 * max(1.0, abs(cursor), abs(position))
    if abs(cursor - position) > tolerance:
        raise AssertionError("checkpoint position does not equal its accepted-step endpoint")


def validate_authorities(
    index: int,
    selected_main_path: Path,
    selected_main: dict,
    forward: dict,
    reverse_packet: dict,
) -> None:
    current_main_hash = base.sha256(selected_main_path)
    for name, packet in (("forward", forward), ("reverse", reverse_packet)):
        config = packet["configuration"]
        if int(config["index"]) != index:
            raise AssertionError(f"{name} checkpoint target changed")
        if config["canonical_main_sha256"] != current_main_hash:
            raise AssertionError(f"{name} checkpoint main replay authority is stale")
        if config["A378_sha256"] != base.sha256(base.A378):
            raise AssertionError(f"{name} checkpoint A378 authority is stale")
        if config["selected_root_id"] != selected_main["selected_target"]["root_id"]:
            raise AssertionError(f"{name} checkpoint root identity changed")
    reverse_config = reverse_packet["configuration"]
    required_reverse_hashes = {
        "reverse_builder_source_sha256": Path(reverse.__file__).resolve(),
        "C_backed_Taylor_runtime_sha256": Path(fast.__file__).resolve(),
        "C_backed_Taylor_equivalence_audit_sha256": FAST_AUDIT,
        "stable_affine_Hessian_runtime_sha256": Path(stable.__file__).resolve(),
        "stable_affine_Hessian_inclusion_audit_sha256": STABLE_AUDIT,
    }
    for key, path in required_reverse_hashes.items():
        if reverse_config.get(key) != base.sha256(path):
            raise AssertionError(f"reverse checkpoint authority is stale: {key}")


def lift_balls(center: list[acb], frame: object) -> list[acb]:
    radius = base.validated.upper(frame.physical_radius())
    return [value + reverse.zero_centered_complex_ball(radius) for value in center[:5]]


def bridge_checkpoint_to_position(
    *,
    system: object,
    packet: dict,
    label: str,
    center: list[acb],
    frame: object,
    output_radii: list[arb],
    target_position: float,
    maximum_steps: int,
) -> tuple[list[acb], object, list[arb], list[dict], int]:
    config = packet["configuration"]
    start = complex_value(config["start"])
    endpoint = complex_value(config["endpoint"])
    distance = abs(endpoint - start)
    if distance <= 0.0:
        raise ArithmeticError("bidirectional path has zero length")
    direction = (endpoint - start) / distance
    position = float(packet["position"])
    proposed_step = float(packet["proposed_step"])
    minimum_step = float(config["minimum_step"])
    maximum_step = float(config["maximum_step"])
    maximum_lift_correction = float(config["maximum_lift_correction"])
    maximum_output_increment = float(config["maximum_output_increment"])
    maximum_output_radius = float(config["maximum_output_radius"])
    order = int(config["order"])
    bridge_steps: list[dict] = []
    rejected = 0

    while not math.isclose(position, target_position, rel_tol=0.0, abs_tol=2.0e-15):
        if len(bridge_steps) >= maximum_steps:
            raise ArithmeticError("bidirectional bridge exceeded its step budget")
        signed_gap = target_position - position
        step_direction = direction if signed_gap > 0.0 else -direction
        step = min(proposed_step, abs(signed_gap))
        if step < minimum_step:
            raise ArithmeticError("bidirectional bridge requires a smaller step")
        parameter_start = start + direction * position
        try:
            next_center, next_frame, next_radii, diagnostics = (
                base.beta_hessian.validated_affine_hessian_step(
                    system,
                    parameter_start,
                    step_direction,
                    step,
                    center,
                    frame,
                    output_radii,
                    order=order,
                    system_builder=base.build_homogeneous_hessian_system,
                )
            )
            if diagnostics["transformed_lift_correction"] > maximum_lift_correction:
                raise ArithmeticError("bidirectional bridge lift correction exceeds budget")
            if diagnostics["maximum_output_increment_error"] > maximum_output_increment:
                raise ArithmeticError("bidirectional bridge output increment exceeds budget")
            if diagnostics["maximum_output_radius"] > maximum_output_radius:
                raise ArithmeticError("bidirectional bridge output radius exceeds budget")
        except (ArithmeticError, ZeroDivisionError, ValueError):
            rejected += 1
            proposed_step = step / 2.0
            if rejected % 10 == 0:
                print(
                    f"{label} bridge rejections={rejected} "
                    f"position={position:.12g} next={proposed_step:.3e}",
                    flush=True,
                )
            if proposed_step < minimum_step:
                raise
            continue
        old_position = position
        center = next_center
        frame = next_frame
        output_radii = next_radii
        position += math.copysign(step, signed_gap)
        if abs(position - target_position) <= 2.0e-15:
            position = target_position
        bridge_steps.append(
            {
                "path_label": label,
                "start_arclength": old_position,
                "end_arclength": position,
                "step": step,
                "direction_sign": 1 if signed_gap > 0.0 else -1,
                **diagnostics,
            }
        )
        quality = max(
            diagnostics["maximum_reduction_neumann_norm"],
            diagnostics["fundamental_inverse_neumann_norm"],
        )
        proposed_step = min(maximum_step, step * (1.8 if quality < 0.05 else 1.35))
        if len(bridge_steps) % 10 == 0 or position == target_position:
            print(
                f"{label} bridge steps={len(bridge_steps)} "
                f"position={position:.12g} target={target_position:.12g} "
                f"radius={max(base.validated.upper(value) for value in output_radii):.3e}",
                flush=True,
            )
    return center, frame, output_radii, bridge_steps, rejected


def dump_bridge_cache(
    path: Path,
    *,
    index: int,
    label: str,
    input_path: Path,
    target_position: float,
    center: list[acb],
    frame: object,
    output_radii: list[arb],
    bridge_steps: list[dict],
    rejected: int,
) -> None:
    base.dump(
        path,
        {
            "schema": "MTTQ79BidirectionalMainHessianBridgeCache.v1",
            "distinguished_index": index,
            "path_label": label,
            "target_position": format(target_position, ".17g"),
            "center": [base.validated.encoded_acb(value) for value in center],
            "lift_fundamental": base.validated.encoded_matrix(frame.fundamental),
            "coordinate_radii": [str(value) for value in frame.coordinate_radii],
            "output_radii": [str(value) for value in output_radii],
            "bridge_steps": bridge_steps,
            "bridge_rejection_count": rejected,
            "authority": {
                "input_checkpoint": authority(input_path),
                "builder_source": authority(Path(__file__).resolve()),
            },
        },
    )
    print(f"wrote {base.relative(path)}", flush=True)


def load_bridge_cache(
    path: Path,
    *,
    index: int,
    label: str,
    input_path: Path,
    target_position: float,
) -> tuple[list[acb], object, list[arb], list[dict], int] | None:
    if not path.is_file():
        return None
    packet = base.load(path)
    if packet.get("schema") != "MTTQ79BidirectionalMainHessianBridgeCache.v1":
        return None
    if int(packet.get("distinguished_index", -1)) != index:
        return None
    if packet.get("path_label") != label:
        return None
    if abs(float(packet["target_position"]) - target_position) > 2.0e-15:
        return None
    if packet["authority"].get("input_checkpoint") != authority(input_path):
        return None
    if packet["authority"].get("builder_source") != authority(Path(__file__).resolve()):
        return None
    center = [base.validated.decoded_acb(value) for value in packet["center"]]
    frame = base.validated.LiftErrorFrame(
        fundamental=base.validated.decoded_matrix(packet["lift_fundamental"]),
        coordinate_radii=[arb(value) for value in packet["coordinate_radii"]],
    )
    output_radii = [arb(value) for value in packet["output_radii"]]
    if len(center) != 77 or len(output_radii) != 72:
        raise AssertionError("bidirectional bridge cache state dimensions changed")
    print(f"resumed {label} bridge from {base.relative(path)}", flush=True)
    return (
        center,
        frame,
        output_radii,
        packet["bridge_steps"],
        int(packet["bridge_rejection_count"]),
    )


def parser() -> argparse.ArgumentParser:
    value = argparse.ArgumentParser()
    value.add_argument("--index", type=int, required=True)
    value.add_argument("--forward-checkpoint", type=Path)
    value.add_argument("--reverse-checkpoint", type=Path)
    value.add_argument("--output", type=Path)
    value.add_argument("--note", type=Path)
    value.add_argument("--forward-bridge-cache", type=Path)
    value.add_argument("--reverse-bridge-cache", type=Path)
    value.add_argument("--maximum-bridge-steps", type=int, default=1000)
    return value


def main() -> int:
    arguments = parser().parse_args()
    if not 1 <= arguments.index <= 90:
        raise ValueError("index must lie in [1,90]")
    paths = base.target_paths(arguments.index)
    selected_main_path = paths["canonical_main"].resolve()
    forward_path = (arguments.forward_checkpoint or paths["checkpoint"]).resolve()
    reverse_path = (
        arguments.reverse_checkpoint or reverse.checkpoint_path(paths)
    ).resolve()
    output_path = (arguments.output or paths["output"]).resolve()
    note_path = (arguments.note or (
        ROOT
        / "proof_corpus"
        / f"MTT_q79HeightFourD{arguments.index:03d}BidirectionalMainHessianInterval_A380BD_v1.md"
    )).resolve()
    forward_cache_path = (
        arguments.forward_bridge_cache
        or output_path.with_name(f"d{arguments.index:03d}.forward.bridge.cache.json")
    ).resolve()
    reverse_cache_path = (
        arguments.reverse_bridge_cache
        or output_path.with_name(f"d{arguments.index:03d}.reverse.bridge.cache.json")
    ).resolve()
    for path in (selected_main_path, forward_path, reverse_path):
        if not path.is_file():
            raise FileNotFoundError(f"bidirectional input is absent: {path}")

    selected_main = base.load(selected_main_path)
    forward_packet, forward_center, forward_frame, forward_radii = decoded_checkpoint(
        forward_path, "MTTQ79TargetMainHessianCheckpoint.v1"
    )
    reverse_packet, reverse_center, reverse_frame, reverse_radii = decoded_checkpoint(
        reverse_path, "MTTQ79ReverseTargetMainHessianCheckpoint.v1"
    )
    validate_authorities(
        arguments.index,
        selected_main_path,
        selected_main,
        forward_packet,
        reverse_packet,
    )
    forward_position = float(forward_packet["position"])
    reverse_position = float(reverse_packet["position"])
    audit_steps(forward_packet, forward_position, stable_required=True)
    audit_steps(reverse_packet, reverse_position, stable_required=True)

    forward_config = forward_packet["configuration"]
    reverse_config = reverse_packet["configuration"]
    cutoff = complex_value(forward_config["start"])
    reverse_cutoff = complex_value(reverse_config["endpoint"])
    distance = abs(cutoff)
    if abs(cutoff - reverse_cutoff) > 2.0e-14 * max(1.0, distance):
        raise AssertionError("forward and reverse cutoff parameters differ")
    if abs(float(reverse_config["dps"]) - float(forward_config["dps"])) > 50:
        raise AssertionError("forward and reverse precision settings are incompatible")
    reverse_side_position = reverse_position
    forward_side_position_in_reverse_coordinates = distance - forward_position
    target_reverse_position = (
        reverse_side_position + forward_side_position_in_reverse_coordinates
    ) / 2.0
    target_forward_position = distance - target_reverse_position
    if not (
        0.0 <= target_reverse_position <= distance
        and 0.0 <= target_forward_position <= distance
    ):
        raise AssertionError("bidirectional meeting point lies outside the selected path")

    dps = max(int(forward_config["dps"]), int(reverse_config["dps"]))
    ctx.dps = dps
    system, rank, row = base.selected_system(arguments.index, dps)
    fast.install()
    stable.install()
    try:
        forward_cached = load_bridge_cache(
            forward_cache_path,
            index=arguments.index,
            label="forward",
            input_path=forward_path,
            target_position=target_forward_position,
        )
        if forward_cached is None:
            forward_cached = bridge_checkpoint_to_position(
                system=system,
                packet=forward_packet,
                label="forward",
                center=forward_center,
                frame=forward_frame,
                output_radii=forward_radii,
                target_position=target_forward_position,
                maximum_steps=arguments.maximum_bridge_steps,
            )
            dump_bridge_cache(
                forward_cache_path,
                index=arguments.index,
                label="forward",
                input_path=forward_path,
                target_position=target_forward_position,
                center=forward_cached[0],
                frame=forward_cached[1],
                output_radii=forward_cached[2],
                bridge_steps=forward_cached[3],
                rejected=forward_cached[4],
            )
        (
            forward_center,
            forward_frame,
            forward_radii,
            forward_bridge_steps,
            forward_bridge_rejections,
        ) = forward_cached

        reverse_cached = load_bridge_cache(
            reverse_cache_path,
            index=arguments.index,
            label="reverse",
            input_path=reverse_path,
            target_position=target_reverse_position,
        )
        if reverse_cached is None:
            reverse_cached = bridge_checkpoint_to_position(
                system=system,
                packet=reverse_packet,
                label="reverse",
                center=reverse_center,
                frame=reverse_frame,
                output_radii=reverse_radii,
                target_position=target_reverse_position,
                maximum_steps=arguments.maximum_bridge_steps,
            )
            dump_bridge_cache(
                reverse_cache_path,
                index=arguments.index,
                label="reverse",
                input_path=reverse_path,
                target_position=target_reverse_position,
                center=reverse_cached[0],
                frame=reverse_cached[1],
                output_radii=reverse_cached[2],
                bridge_steps=reverse_cached[3],
                rejected=reverse_cached[4],
            )
        (
            reverse_center,
            reverse_frame,
            reverse_radii,
            reverse_bridge_steps,
            reverse_bridge_rejections,
        ) = reverse_cached
    finally:
        stable.uninstall()
        fast.uninstall()

    forward_direction = -cutoff / distance
    meeting_parameter = cutoff + forward_direction * target_forward_position
    reverse_direction = cutoff / distance
    reverse_meeting_parameter = reverse_direction * target_reverse_position
    parameter_difference = abs(reverse_meeting_parameter - meeting_parameter)
    if parameter_difference > 3.0e-14 * max(1.0, distance):
        raise AssertionError("forward and reverse meeting parameters do not coincide")

    forward_lift_balls = lift_balls(forward_center, forward_frame)
    reverse_lift_balls = lift_balls(reverse_center, reverse_frame)
    lift_overlap = [
        forward.overlaps(backward)
        for forward, backward in zip(forward_lift_balls, reverse_lift_balls)
    ]
    lift_differences = [
        base.validated.upper(abs(forward - backward))
        for forward, backward in zip(forward_lift_balls, reverse_lift_balls)
    ]
    if not all(lift_overlap):
        raise AssertionError("bidirectional affine lifts do not overlap at the meeting point")

    orientation = int(selected_main["orientation"]["selected_sign"])
    forward_outputs = np.asarray(
        [base.validated.midpoint(value) for value in forward_center[5:]],
        dtype=np.complex128,
    )
    reverse_outputs = np.asarray(
        [base.validated.midpoint(value) for value in reverse_center[5:]],
        dtype=np.complex128,
    )
    output_centers = orientation * (reverse_outputs - forward_outputs)
    output_radius_values = np.asarray(
        [
            base.validated.upper(forward_radius) + base.validated.upper(reverse_radius)
            for forward_radius, reverse_radius in zip(forward_radii, reverse_radii)
        ],
        dtype=np.float64,
    )
    ordinary_centers = output_centers[:8]
    ordinary_radii = output_radius_values[:8]
    hessian = output_centers[8:].reshape(8, 8).T
    hessian_radii = output_radius_values[8:].reshape(8, 8).T

    canonical_centers = np.asarray(
        [
            base.complex_value(value)
            for value in selected_main["all_eight_main_residue_rows"]["interval_centers"]
        ],
        dtype=np.complex128,
    )
    canonical_radius = float(
        selected_main["all_eight_main_residue_rows"][
            "common_complex_disk_radius_upper"
        ]
    )
    replay_difference = abs(ordinary_centers - canonical_centers)
    replay_overlap = replay_difference <= ordinary_radii + canonical_radius
    if not bool(np.all(replay_overlap)):
        raise AssertionError("bidirectional ordinary rows do not overlap the canonical main packet")

    meeting_path = output_path.with_name(
        f"d{arguments.index:03d}.bidirectional.meeting.json"
    )
    meeting_packet = {
        "schema": "MTTQ79BidirectionalMainHessianMeeting.v1",
        "distinguished_index": arguments.index,
        "forward_position": format(forward_position, ".17g"),
        "forward_position_at_meeting": format(target_forward_position, ".17g"),
        "reverse_position_before_bridge": format(reverse_position, ".17g"),
        "reverse_position_at_meeting": format(target_reverse_position, ".17g"),
        "meeting_parameter": base.pair(meeting_parameter),
        "parameter_center_difference": parameter_difference,
        "forward_center": [base.validated.encoded_acb(value) for value in forward_center],
        "forward_lift_fundamental": base.validated.encoded_matrix(forward_frame.fundamental),
        "forward_coordinate_radii": [str(value) for value in forward_frame.coordinate_radii],
        "forward_output_radii": [str(value) for value in forward_radii],
        "reverse_center": [base.validated.encoded_acb(value) for value in reverse_center],
        "reverse_lift_fundamental": base.validated.encoded_matrix(reverse_frame.fundamental),
        "reverse_coordinate_radii": [str(value) for value in reverse_frame.coordinate_radii],
        "reverse_output_radii": [str(value) for value in reverse_radii],
        "forward_bridge_steps": forward_bridge_steps,
        "forward_bridge_rejection_count": forward_bridge_rejections,
        "reverse_bridge_steps": reverse_bridge_steps,
        "reverse_bridge_rejection_count": reverse_bridge_rejections,
        "all_five_affine_lift_coordinates_overlap": all(lift_overlap),
        "affine_lift_difference_uppers": lift_differences,
        "authority": {
            "forward_checkpoint": authority(forward_path),
            "reverse_checkpoint": authority(reverse_path),
            "builder_source": authority(Path(__file__).resolve()),
        },
    }
    base.dump(meeting_path, meeting_packet)

    epsilon = float(selected_main["selected_target"]["endpoint_cutoff_epsilon"])
    payload = {
        "schema": "MTTQ79HeightFourTargetMainHessianInterval.v1",
        "status": "TARGET_BIDIRECTIONAL_MAIN_EIGHT_ROWS_AND_COMPLEX_8_BY_8_HESSIAN_INTERVAL_CERTIFIED",
        "artifact": ARTIFACT,
        "selected_target": {
            "distinguished_index": arguments.index,
            "A219_contribution_rank": rank,
            "root_id": row["root_id"],
            "line_chart": base.dynamic.CHART,
            "signed_chain_coefficient": int(row["signed_coefficient"]),
            "orientation_sign": orientation,
            "endpoint_cutoff_epsilon": epsilon,
        },
        "main_residue_rows": [
            {
                "residue_index_zero_based": index,
                "interval_center": base.pair(ordinary_centers[index]),
                "component_radius_upper": float(ordinary_radii[index]),
                "canonical_center_difference": float(replay_difference[index]),
                "canonical_intervals_overlap": bool(replay_overlap[index]),
            }
            for index in range(8)
        ],
        "complex_main_Hessian_8_by_8": [
            [
                {
                    "row_zero_based": row_index,
                    "column_zero_based": column_index,
                    "interval_center": base.pair(hessian[row_index, column_index]),
                    "component_radius_upper": float(
                        hessian_radii[row_index, column_index]
                    ),
                }
                for column_index in range(8)
            ]
            for row_index in range(8)
        ],
        "summary": {
            "certified_main_rows": 8,
            "certified_main_Hessian_entries": 64,
            "maximum_main_row_component_radius_upper": float(np.max(ordinary_radii)),
            "maximum_main_Hessian_component_radius_upper": float(np.max(hessian_radii)),
            "main_Hessian_product_box_frobenius_radius_upper": float(
                np.linalg.norm(hessian_radii)
            ),
            "all_canonical_main_intervals_overlap": bool(np.all(replay_overlap)),
            "maximum_canonical_main_center_difference": float(np.max(replay_difference)),
            "all_five_meeting_lift_coordinates_overlap": all(lift_overlap),
            "maximum_meeting_lift_difference_upper": max(lift_differences),
            "forward_fraction_before_bridge": forward_position / distance,
            "forward_fraction_at_meeting": target_forward_position / distance,
            "reverse_fraction_before_bridge": reverse_position / distance,
            "reverse_fraction_at_meeting": target_reverse_position / distance,
            "forward_bridge_step_count": len(forward_bridge_steps),
            "forward_bridge_rejection_count": forward_bridge_rejections,
            "reverse_bridge_step_count": len(reverse_bridge_steps),
            "reverse_bridge_rejection_count": reverse_bridge_rejections,
        },
        "execution": {
            "identity": "Pi_main=orientation*(Pi_base_to_meeting-Pi_cutoff_to_meeting)",
            "forward_checkpoint_configuration": forward_config,
            "reverse_checkpoint_configuration": reverse_config,
            "meeting_certificate": authority(meeting_path),
        },
        "authority": {
            "selected_main_replay_interval": authority(selected_main_path),
            "forward_checkpoint": authority(forward_path),
            "reverse_checkpoint": authority(reverse_path),
            "meeting_certificate": authority(meeting_path),
            "A378_Hessian_integrand_source": authority(base.A378),
            "triangular_validated_engine": authority(Path(base.beta_hessian.__file__).resolve()),
            "validated_Taylor_engine": authority(Path(base.validated.__file__).resolve()),
            "C_backed_Taylor_runtime": authority(Path(fast.__file__).resolve()),
            "C_backed_Taylor_equivalence_audit": authority(FAST_AUDIT),
            "stable_affine_Hessian_runtime": authority(Path(stable.__file__).resolve()),
            "stable_affine_Hessian_inclusion_audit": authority(STABLE_AUDIT),
            "forward_builder_source": authority(Path(base.__file__).resolve()),
            "reverse_builder_source": authority(Path(reverse.__file__).resolve()),
            "bidirectional_builder_source": authority(Path(__file__).resolve()),
        },
        "strict_scope": {
            "observed_SM_values_used": False,
            "same_source_A378_homogeneous_Hessian_rows_used": True,
            "forward_cutoff_to_meeting_transport_used": True,
            "reverse_base_to_meeting_transport_used": True,
            "all_five_meeting_lift_coordinates_overlap": True,
            "ordinary_main_rows_independently_replayed": True,
            "target_main_Hessian_interval_closed": True,
            "target_Frobenius_tail_Hessian_interval_closed": False,
            "target_full_Hessian_interval_closed": False,
            "full_76_target_chain_Hessian_interval_closed": False,
            "interval_Newton_existence_and_uniqueness_closed": False,
            "covariant_zero_proved": False,
            "full_SM_closure_proved": False,
        },
        "next_required_artifact": (
            "splice this bidirectionally certified main Hessian to the matching A381 tail"
        ),
    }
    base.dump(output_path, payload)
    note_path.write_text(
        f"# MTT q79 Height-Four d{arguments.index:03d} Bidirectional Main Hessian Interval (A380BD) v1\n\n"
        "A380BD joins the certified cutoff-to-meeting and base-to-meeting A378 "
        "transports at one interior parameter. All five affine lift coordinates "
        "overlap there. The ordinary and Hessian rows use the exact identity "
        "`Pi_main=orientation*(Pi_base_to_meeting-Pi_cutoff_to_meeting)`.\n\n"
        f"The product-box Frobenius radius is `{np.linalg.norm(hessian_radii):.12g}`. "
        "All eight ordinary rows overlap the canonical selected main packet, and "
        "no observed Standard Model value is used.\n",
        encoding="utf-8",
    )
    print(f"wrote {base.relative(output_path)}")
    print(f"wrote {base.relative(meeting_path)}")
    print(f"wrote {base.relative(note_path)}")
    print(json.dumps(payload["summary"], indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
