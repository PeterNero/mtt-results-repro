from __future__ import annotations

import argparse
import hashlib
import json
import math
import sys
import time
from argparse import Namespace
from pathlib import Path

import numpy as np
from flint import acb, arb, ctx

import build_q79_height4_target_full_hessian_interval as full_hessian
import certify_q79_height4_rank3_beta_hessian_interval as beta_hessian
import certify_q79_height4_source_derived_far_cut_hessian_interval as far2
import certify_q79_height4_target_main_hessian_interval as main_hessian
import certify_q79_selected_alignment_E32_thimble_polygonal_main_interval as polygonal
import certify_q79_selected_side_beta_defect_transport as validated
import q79_fast_taylor_runtime as fast_taylor
import q79_stable_affine_hessian_runtime as stable_affine


ROOT = Path(__file__).resolve().parents[1]
OUTPUT_DIRECTORY = main_hessian.OUTPUT_DIRECTORY / "detour"
ARTIFACT = "A380D-A382D"
FAST_AUDIT = (
    ROOT / "proof_corpus" / "selected_q79fasttaylorruntime_equivalence_audit.py"
)
STABLE_AUDIT = (
    ROOT / "proof_corpus" / "selected_q79stableaffinehessianruntime_inclusion_audit.py"
)


def load(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def dump(path: Path, value: dict) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(value, indent=2, sort_keys=True) + "\n", encoding="utf-8")


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def relative(path: Path) -> str:
    return str(path.relative_to(ROOT)).replace("\\", "/")


def authority(path: Path) -> dict[str, str]:
    return {"path": relative(path), "sha256": sha256(path)}


def pair(value: complex) -> dict[str, str]:
    return {
        "real": format(float(value.real), ".17g"),
        "imaginary": format(float(value.imag), ".17g"),
    }


def complex_value(value: dict[str, str]) -> complex:
    return complex(float(value["real"]), float(value["imaginary"]))


def paths(index: int, epsilon: float, source_route: str) -> dict[str, Path]:
    if source_route == "far":
        selected = far2.paths(index, epsilon)
    elif source_route == "canonical":
        canonical = main_hessian.tight.canonical_paths(index)
        selected = {
            "thimble": canonical["thimble"],
            "canonical_main": canonical["main"],
            "canonical_tail": canonical["tail"],
            "canonical_full": canonical["full"],
            "ordinary_tail": canonical["tail"],
            "synthetic_main": canonical["main"],
            "tail": far2.tail_hessian.output_paths(index)["output"],
        }
    else:
        raise ValueError(f"unsupported detour source route {source_route!r}")
    stem = f"d{index:03d}"
    return {
        **selected,
        "detour_main": OUTPUT_DIRECTORY / f"{stem}.mainH.json",
        "detour_checkpoint": OUTPUT_DIRECTORY / f"{stem}.checkpoint.json",
        "detour_full": OUTPUT_DIRECTORY / f"{stem}.fullH.json",
        "detour_main_note": ROOT
        / "proof_corpus"
        / f"MTT_q79HeightFourD{index:03d}DetourMainHessian_A380D_v1.md",
        "detour_full_note": ROOT
        / "proof_corpus"
        / f"MTT_q79HeightFourD{index:03d}DetourFullHessian_A382D_v1.md",
    }


def check_authorities(packet: dict, label: str) -> None:
    for name, row in packet.get("authority", {}).items():
        path = ROOT / row["path"]
        if not path.exists() or sha256(path) != row["sha256"]:
            raise AssertionError(f"{label} authority is stale: {name}")


def build_detour_geometry(
    arguments: argparse.Namespace,
    main_packet: dict,
) -> tuple[list[complex], dict]:
    node_ball = validated.decoded_acb(main_packet["certified_node"]["parameter_ball"])
    node_center = polygonal.handle.midpoint(node_ball)
    target_w = polygonal.BASE + 1j * node_center
    displacement = target_w - polygonal.BASE
    right = complex(displacement.imag, -displacement.real) / abs(displacement)
    cutoff = polygonal.BASE + (1.0 - arguments.epsilon) * displacement
    path_w = [
        polygonal.BASE,
        polygonal.BASE + arguments.entry_fraction * displacement,
        polygonal.BASE
        + arguments.peak_fraction * displacement
        + arguments.detour_offset * right,
        polygonal.BASE + arguments.return_fraction * displacement,
        cutoff,
    ]
    dual = load(polygonal.DUAL)
    chart = main_packet["selected_target"]["line_chart"]
    z_wall = load(polygonal.Z_WALL) if chart == "z" else None
    geometry = polygonal.certify_detour(
        path_w,
        dual,
        main_packet["selected_target"]["root_id"],
        line_chart=chart,
        z_wall=z_wall,
    )
    parameters = [-1j * (point - polygonal.BASE) for point in reversed(path_w)]
    _node, canonical_start = main_hessian.canonical_cutoff_start(main_packet)
    if abs(parameters[0] - canonical_start) > 5.0e-15:
        raise AssertionError("detour cutoff does not replay the canonical far-cut start")
    parameters[0] = canonical_start
    geometry.update(
        {
            "entry_fraction": arguments.entry_fraction,
            "peak_fraction": arguments.peak_fraction,
            "return_fraction": arguments.return_fraction,
            "detour_signed_right_offset": arguments.detour_offset,
            "points_in_base_to_node_order": [pair(value) for value in path_w],
            "parameters_in_cutoff_to_base_order": [pair(value) for value in parameters],
            "selected_local_detour": True,
        }
    )
    return parameters, geometry


def configuration(
    arguments: argparse.Namespace,
    selected: dict[str, Path],
    main_packet: dict,
    parameters: list[complex],
) -> dict:
    value = {
        "index": arguments.index,
        "epsilon": format(arguments.epsilon, ".17g"),
        "dps": arguments.dps,
        "order": arguments.order,
        "maximum_step": format(arguments.maximum_step, ".17g"),
        "minimum_step": format(arguments.minimum_step, ".17g"),
        "maximum_lift_correction": format(arguments.maximum_lift_correction, ".17g"),
        "maximum_output_increment": format(arguments.maximum_output_increment, ".17g"),
        "maximum_output_radius": format(arguments.maximum_output_radius, ".17g"),
        "entry_fraction": format(arguments.entry_fraction, ".17g"),
        "peak_fraction": format(arguments.peak_fraction, ".17g"),
        "return_fraction": format(arguments.return_fraction, ".17g"),
        "detour_offset": format(arguments.detour_offset, ".17g"),
        "parameters": [pair(value) for value in parameters],
        "derived_far_main_sha256": sha256(selected["synthetic_main"]),
        "source_route": arguments.source_route,
        "A378_sha256": sha256(main_hessian.A378),
        "builder_source_sha256": sha256(Path(__file__).resolve()),
        "selected_root_id": main_packet["selected_target"]["root_id"],
    }
    if arguments.source_route == "far":
        value["A380FS_sha256"] = sha256(selected["source"])
    if arguments.fast:
        value["C_backed_Taylor_runtime_sha256"] = sha256(
            Path(fast_taylor.__file__).resolve()
        )
        value["C_backed_Taylor_equivalence_audit_sha256"] = sha256(FAST_AUDIT)
        value["stable_affine_Hessian_runtime_sha256"] = sha256(
            Path(stable_affine.__file__).resolve()
        )
        value["stable_affine_Hessian_inclusion_audit_sha256"] = sha256(
            STABLE_AUDIT
        )
    return value


def execute_main(arguments: argparse.Namespace, selected: dict[str, Path]) -> dict:
    started = time.perf_counter()
    main_packet = load(selected["synthetic_main"])
    check_authorities(main_packet, "derived far main")
    if arguments.source_route == "far":
        source_packet = load(selected["source"])
        check_authorities(source_packet, "selected far-cut source")
    if int(main_packet["selected_target"]["distinguished_index"]) != arguments.index:
        raise AssertionError("detour target identity changed")
    system, rank, row = main_hessian.selected_system(arguments.index, arguments.dps)
    chart = main_hessian.dynamic.CHART
    smoke = main_hessian.smoke_test(system, chart, min(arguments.order, 18))
    parameters, geometry = build_detour_geometry(arguments, main_packet)
    config = configuration(arguments, selected, main_packet, parameters)
    initial_center, initial_frame, initial_radii, initial_period_source = (
        main_hessian.initial_state(system, main_packet, parameters[0])
    )

    lengths = [abs(end - start) for start, end in zip(parameters, parameters[1:])]
    total_length = sum(lengths)
    if min(lengths) <= 0.0:
        raise AssertionError("detour has a zero-length segment")

    center = initial_center
    frame = initial_frame
    output_radii = initial_radii
    accepted: list[dict] = []
    rejected = 0
    minimum_accepted_step = math.inf
    starting_segment = 0
    starting_position = 0.0
    node_center, _start = main_hessian.canonical_cutoff_start(main_packet)
    proposed_step = min(arguments.maximum_step, abs(node_center - parameters[0]) / 4.0)

    if arguments.resume:
        checkpoint = load(selected["detour_checkpoint"])
        if checkpoint.get("schema") != "MTTQ79DetourMainHessianCheckpoint.v1":
            raise ValueError("detour checkpoint schema changed")
        if checkpoint.get("configuration") != config:
            raise ValueError("detour checkpoint configuration changed")
        center = [validated.decoded_acb(value) for value in checkpoint["center"]]
        frame = validated.LiftErrorFrame(
            fundamental=validated.decoded_matrix(checkpoint["lift_fundamental"]),
            coordinate_radii=[arb(value) for value in checkpoint["coordinate_radii"]],
        )
        output_radii = [arb(value) for value in checkpoint["output_radii"]]
        accepted = checkpoint["accepted_steps"]
        rejected = int(checkpoint["rejected_step_count"])
        minimum_accepted_step = float(checkpoint["minimum_accepted_step"])
        proposed_step = float(checkpoint["proposed_step"])
        starting_segment = int(checkpoint["segment_index"])
        starting_position = float(checkpoint["segment_position"])
        print(
            f"resumed d{arguments.index:03d} detour Hessian steps={len(accepted)} "
            f"segment={starting_segment + 1}/4",
            flush=True,
        )

    segment_index = starting_segment
    segment_position = starting_position

    def save_checkpoint() -> None:
        validated.atomic_dump(
            selected["detour_checkpoint"],
            {
                "schema": "MTTQ79DetourMainHessianCheckpoint.v1",
                "configuration": config,
                "segment_index": segment_index,
                "segment_position": format(segment_position, ".17g"),
                "proposed_step": format(proposed_step, ".17g"),
                "center": [validated.encoded_acb(value) for value in center],
                "lift_fundamental": validated.encoded_matrix(frame.fundamental),
                "coordinate_radii": [str(value) for value in frame.coordinate_radii],
                "output_radii": [str(value) for value in output_radii],
                "accepted_steps": accepted,
                "rejected_step_count": rejected,
                "minimum_accepted_step": format(minimum_accepted_step, ".17g"),
            },
        )

    for segment_index in range(starting_segment, len(lengths)):
        start = parameters[segment_index]
        endpoint = parameters[segment_index + 1]
        distance = lengths[segment_index]
        direction = (endpoint - start) / distance
        segment_position = starting_position if segment_index == starting_segment else 0.0
        if segment_index > starting_segment:
            proposed_step = min(proposed_step, arguments.maximum_step / 4.0)
        covered = sum(lengths[:segment_index])
        while segment_position < distance:
            if len(accepted) >= arguments.maximum_steps:
                raise ArithmeticError("detour Hessian transport exceeded step budget")
            step = min(proposed_step, distance - segment_position)
            if step < arguments.minimum_step:
                raise ArithmeticError("detour Hessian transport requires a smaller step")
            parameter_start = start + direction * segment_position
            try:
                next_center, next_frame, next_radii, diagnostics = (
                    beta_hessian.validated_affine_hessian_step(
                        system,
                        parameter_start,
                        direction,
                        step,
                        center,
                        frame,
                        output_radii,
                        order=arguments.order,
                        system_builder=main_hessian.build_homogeneous_hessian_system,
                    )
                )
                if diagnostics["transformed_lift_correction"] > arguments.maximum_lift_correction:
                    raise ArithmeticError("lift correction exceeds local budget")
                if diagnostics["maximum_output_increment_error"] > arguments.maximum_output_increment:
                    raise ArithmeticError("output increment exceeds local budget")
                if diagnostics["maximum_output_radius"] > arguments.maximum_output_radius:
                    raise ArithmeticError("output radius exceeds global budget")
            except (ArithmeticError, ZeroDivisionError, ValueError) as error:
                rejected += 1
                proposed_step = step / 2.0
                if rejected % 10 == 0:
                    print(
                        f"d{arguments.index:03d} detour rejections={rejected} "
                        f"segment={segment_index + 1}/4 "
                        f"fraction={(covered + segment_position) / total_length:.12g} "
                        f"next={proposed_step:.3e} reason={type(error).__name__}: {error}",
                        flush=True,
                    )
                if proposed_step < arguments.minimum_step:
                    raise
                continue
            center = next_center
            frame = next_frame
            output_radii = next_radii
            segment_position = min(distance, segment_position + step)
            minimum_accepted_step = min(minimum_accepted_step, step)
            accepted.append(
                {
                    "segment_index": segment_index,
                    "start_arclength": covered + segment_position - step,
                    "end_arclength": covered + segment_position,
                    "step": step,
                    **diagnostics,
                }
            )
            quality = max(
                diagnostics["maximum_reduction_neumann_norm"],
                diagnostics["fundamental_inverse_neumann_norm"],
            )
            proposed_step = min(
                arguments.maximum_step,
                step * (1.8 if quality < 0.05 else 1.35),
            )
            if len(accepted) % 10 == 0 or segment_position == distance:
                save_checkpoint()
            if len(accepted) <= 3 or len(accepted) % 10 == 0 or segment_position == distance:
                print(
                    f"d{arguments.index:03d} detour steps={len(accepted)} "
                    f"segment={segment_index + 1}/4 "
                    f"fraction={(covered + segment_position) / total_length:.12g} "
                    f"radius={max(validated.upper(value) for value in output_radii):.3e}",
                    flush=True,
                )
        starting_position = 0.0

    orientation = int(main_packet["orientation"]["selected_sign"])
    ordinary_centers = -orientation * np.asarray(
        [validated.midpoint(value) for value in center[5:13]], dtype=np.complex128
    )
    ordinary_radii = np.asarray(
        [validated.upper(value) for value in output_radii[:8]], dtype=np.float64
    )
    hessian = np.empty((8, 8), dtype=np.complex128)
    hessian_radii = np.empty((8, 8), dtype=np.float64)
    for selected_direction in range(8):
        for residue_index in range(8):
            offset = selected_direction * 8 + residue_index
            hessian[residue_index, selected_direction] = -orientation * validated.midpoint(
                center[13 + offset]
            )
            hessian_radii[residue_index, selected_direction] = validated.upper(
                output_radii[8 + offset]
            )

    expected = main_packet["all_eight_main_residue_rows"]
    canonical_centers = np.asarray(
        [complex_value(value) for value in expected["interval_centers"]],
        dtype=np.complex128,
    )
    canonical_radii = np.asarray(
        expected.get(
            "per_row_derived_radius_uppers",
            [expected["common_complex_disk_radius_upper"]] * 8,
        ),
        dtype=np.float64,
    )
    replay_difference = abs(ordinary_centers - canonical_centers)
    replay_overlap = replay_difference <= ordinary_radii + canonical_radii
    if not bool(np.all(replay_overlap)):
        raise AssertionError("detour ordinary rows do not overlap the selected far main")

    payload = {
        "schema": "MTTQ79HeightFourTargetMainHessianInterval.v1",
        "status": "TARGET_DETOUR_MAIN_EIGHT_ROWS_AND_COMPLEX_8_BY_8_HESSIAN_INTERVAL_CERTIFIED",
        "artifact": "A380D",
        "selected_target": {
            "distinguished_index": arguments.index,
            "A219_contribution_rank": rank,
            "root_id": row["root_id"],
            "line_chart": chart,
            "signed_chain_coefficient": int(row["signed_coefficient"]),
            "orientation_sign": orientation,
            "endpoint_cutoff_epsilon": arguments.epsilon,
        },
        "polygonal_homotopy": geometry,
        "main_residue_rows": [
            {
                "residue_index_zero_based": index,
                "interval_center": pair(ordinary_centers[index]),
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
                    "interval_center": pair(hessian[row_index, column_index]),
                    "component_radius_upper": float(hessian_radii[row_index, column_index]),
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
            "main_Hessian_product_box_frobenius_radius_upper": float(np.linalg.norm(hessian_radii)),
            "all_canonical_main_intervals_overlap": bool(np.all(replay_overlap)),
            "maximum_canonical_main_center_difference": float(np.max(replay_difference)),
            "accepted_step_count": len(accepted),
            "rejected_step_count": rejected,
            "minimum_accepted_step": minimum_accepted_step,
            "elapsed_seconds": time.perf_counter() - started,
        },
        "smoke_test": smoke,
        "initial_period_source": initial_period_source,
        "execution": {
            "configuration": config,
            "steps": accepted,
            "checkpoint": relative(selected["detour_checkpoint"]),
            "checkpoint_sha256": sha256(selected["detour_checkpoint"]),
        },
        "authority": {
            "derived_far_main_replay_source": authority(selected["synthetic_main"]),
            "certified_dual_discriminant": authority(polygonal.DUAL),
            "A378_Hessian_integrand_source": authority(main_hessian.A378),
            "triangular_validated_engine": authority(Path(beta_hessian.__file__).resolve()),
            "validated_Taylor_engine": authority(Path(validated.__file__).resolve()),
            "direct_cut_period_engine": authority(Path(main_hessian.handle.__file__).resolve()),
            "cutoff_root_engine": authority(Path(main_hessian.pilot.__file__).resolve()),
            "polygonal_homotopy_engine": authority(Path(polygonal.__file__).resolve()),
            "builder_source": authority(Path(__file__).resolve()),
        },
        "strict_scope": {
            "observed_SM_values_used": False,
            "same_source_A378_homogeneous_Hessian_rows_used": True,
            "full_precision_direct_cut_periods_recomputed": True,
            "relative_homotopy_to_selected_radial_path_closed": True,
            "detour_wall_clearance_certified": True,
            "ordinary_main_rows_independently_replayed": True,
            "target_main_Hessian_interval_closed": True,
            "target_full_Hessian_interval_closed": False,
            "interval_Newton_existence_and_uniqueness_closed": False,
            "covariant_zero_proved": False,
            "full_SM_closure_proved": False,
        },
        "next_required_artifact": "splice the matching selected far-tail Hessian interval",
    }
    if arguments.source_route == "far":
        payload["authority"]["A380FS_far_cut_source"] = authority(
            selected["source"]
        )
        payload["strict_scope"]["selected_far_cut_source_used"] = True
    else:
        payload["strict_scope"]["canonical_cutoff_source_used"] = True
    if chart == "z":
        payload["authority"]["selected_z_chart_wall"] = authority(polygonal.Z_WALL)
    if arguments.fast:
        payload["execution"]["C_backed_Taylor_runtime"] = {
            "installed": True,
            "equivalence_gate": relative(FAST_AUDIT),
        }
        payload["authority"]["C_backed_Taylor_runtime"] = authority(
            Path(fast_taylor.__file__).resolve()
        )
        payload["authority"]["C_backed_Taylor_equivalence_audit"] = authority(
            FAST_AUDIT
        )
        payload["execution"]["stable_affine_Hessian_runtime"] = {
            "installed": True,
            "growth_integral_majorant": "A*h*exp(L*h)",
            "zero_containing_linear_defect_interval_supported": True,
            "inclusion_gate": relative(STABLE_AUDIT),
        }
        payload["authority"]["stable_affine_Hessian_runtime"] = authority(
            Path(stable_affine.__file__).resolve()
        )
        payload["authority"]["stable_affine_Hessian_inclusion_audit"] = authority(
            STABLE_AUDIT
        )
        payload["strict_scope"][
            "C_backed_polynomial_acceleration_equivalence_audited"
        ] = True
        payload["strict_scope"][
            "zero_defect_regular_affine_growth_bound_audited"
        ] = True
        payload["strict_scope"]["all_step_bounds_finite"] = True
    dump(selected["detour_main"], payload)
    selected["detour_main_note"].write_text(
        f"# MTT q79 Height-Four d{arguments.index:03d} Detour Main Hessian (A380D) v1\n\n"
        "This packet executes A378 on a certified polygonal path in the same relative "
        "homotopy class as the selected radial thimble. The detour changes numerical "
        "conditioning only; it does not change the cycle, branch, or source periods.\n\n"
        f"The certified other-critical-value clearance is "
        f"`{geometry['other_critical_ball_clearance_lower']:.12g}` and the Hessian "
        f"product-box Frobenius radius is `{np.linalg.norm(hessian_radii):.12g}`.\n",
        encoding="utf-8",
    )
    print(f"wrote {relative(selected['detour_main'])}")
    print(json.dumps(payload["summary"], indent=2))
    return payload


def execute_full(arguments: argparse.Namespace, selected: dict[str, Path]) -> dict:
    if not selected["detour_main"].exists() or not selected["tail"].exists():
        raise FileNotFoundError("detour main and selected far-tail Hessians are required")
    prior = full_hessian.paths

    def local_paths(_index: int) -> dict[str, Path]:
        return {
            "main": selected["detour_main"],
            "tail": selected["tail"],
            "canonical_full": selected["canonical_full"],
            "output": selected["detour_full"],
            "note": selected["detour_full_note"],
        }

    full_hessian.paths = local_paths
    prior_argv = sys.argv
    try:
        sys.argv = [str(Path(full_hessian.__file__).resolve()), "--index", str(arguments.index)]
        full_hessian.main()
    finally:
        sys.argv = prior_argv
        full_hessian.paths = prior
    packet = load(selected["detour_full"])
    packet["artifact"] = "A382D"
    packet["authority"]["A380D_detour_builder"] = authority(Path(__file__).resolve())
    if arguments.source_route == "far":
        packet["authority"]["A380FS_far_cut_source"] = authority(
            selected["source"]
        )
    packet["authority"]["derived_far_main_replay_source"] = authority(
        selected["synthetic_main"]
    )
    packet["strict_scope"]["certified_relative_homotopy_detour_used"] = True
    packet["strict_scope"]["target_full_Hessian_interval_closed"] = True
    dump(selected["detour_full"], packet)
    return packet


def parser() -> argparse.ArgumentParser:
    value = argparse.ArgumentParser()
    value.add_argument("--index", type=int, default=34)
    value.add_argument("--phase", choices=("main", "tail-hessian", "full", "all"), default="all")
    value.add_argument("--source-route", choices=("canonical", "far"), default="canonical")
    value.add_argument("--epsilon", type=float)
    value.add_argument("--dps", type=int, default=110)
    value.add_argument("--order", type=int, default=36)
    value.add_argument("--tail-order", type=int, default=24)
    value.add_argument("--tail-seed-segments", type=int, default=64)
    value.add_argument("--theta-segments", type=int, default=32)
    value.add_argument("--node-width", type=float, default=1.0e-10)
    value.add_argument("--series-terms", type=int, default=10)
    value.add_argument("--entry-fraction", type=float, default=0.94)
    value.add_argument("--peak-fraction", type=float, default=0.994)
    value.add_argument("--return-fraction", type=float, default=0.998)
    value.add_argument("--detour-offset", type=float, default=-0.002)
    value.add_argument("--maximum-step", type=float, default=0.01)
    value.add_argument("--minimum-step", type=float, default=1.0e-12)
    value.add_argument("--maximum-steps", type=int, default=50000)
    value.add_argument("--maximum-lift-correction", type=float, default=1.0e-6)
    value.add_argument("--maximum-output-increment", type=float, default=2.0e-4)
    value.add_argument("--maximum-output-radius", type=float, default=0.03)
    value.add_argument("--resume", action="store_true")
    value.add_argument("--fast", action="store_true")
    return value


def main() -> int:
    arguments = parser().parse_args()
    if arguments.epsilon is None:
        if arguments.source_route == "canonical":
            canonical = load(main_hessian.tight.canonical_paths(arguments.index)["main"])
            arguments.epsilon = float(
                canonical["selected_target"]["endpoint_cutoff_epsilon"]
            )
        else:
            arguments.epsilon = 1.0e-3
    if not 0.0 < arguments.epsilon < 0.01:
        raise ValueError("epsilon must lie in (0,0.01)")
    if not 0.0 < arguments.entry_fraction < arguments.peak_fraction < arguments.return_fraction < 1.0 - arguments.epsilon:
        raise ValueError("detour fractions must be ordered before the cutoff")
    ctx.dps = arguments.dps
    selected = paths(arguments.index, arguments.epsilon, arguments.source_route)
    required = ["ordinary_tail", "synthetic_main", "canonical_full"]
    if arguments.source_route == "far":
        required.append("source")
    for name in required:
        if not selected[name].exists():
            raise FileNotFoundError(f"required selected far-route input is absent: {name}")
    if arguments.phase in {"main", "all"}:
        try:
            if arguments.fast:
                fast_taylor.install()
                stable_affine.install()
            execute_main(arguments, selected)
        finally:
            if arguments.fast:
                stable_affine.uninstall()
                fast_taylor.uninstall()
    if arguments.phase in {"tail-hessian", "all"}:
        tail_arguments = Namespace(
            index=arguments.index,
            dps=arguments.dps,
            order=arguments.tail_order,
            outer_segments=arguments.tail_seed_segments,
            theta_segments=arguments.theta_segments,
            node_width=arguments.node_width,
            series_terms=arguments.series_terms,
        )
        if arguments.source_route == "far":
            far2.run_tail_hessian(
                Namespace(
                    index=arguments.index,
                    dps=arguments.dps,
                    tail_order=arguments.tail_order,
                    tail_seed_segments=arguments.tail_seed_segments,
                    theta_segments=arguments.theta_segments,
                    node_width=arguments.node_width,
                    series_terms=arguments.series_terms,
                ),
                selected,
            )
        else:
            far2.quadrature.execute(tail_arguments)
    if arguments.phase in {"full", "all"}:
        execute_full(arguments, selected)
    print(f"{ARTIFACT}: d{arguments.index:03d} phase={arguments.phase} complete")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
