from __future__ import annotations

import argparse
import hashlib
import json
import math
import time
from pathlib import Path

import numpy as np
from flint import acb, acb_mat, arb, ctx

import certify_q79_height4_target_main_hessian_interval as base
import q79_fast_taylor_runtime as fast
import q79_stable_affine_hessian_runtime as stable


ROOT = Path(__file__).resolve().parents[1]
FAST_AUDIT = ROOT / "proof_corpus" / "selected_q79fasttaylorruntime_equivalence_audit.py"
STABLE_AUDIT = (
    ROOT / "proof_corpus" / "selected_q79stableaffinehessianruntime_inclusion_audit.py"
)
ARTIFACT = "A380B"


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def relative(path: Path) -> str:
    return str(path.relative_to(ROOT)).replace("\\", "/")


def authority(path: Path) -> dict[str, str]:
    return {"path": relative(path), "sha256": sha256(path)}


def zero_centered_complex_ball(radius: float) -> acb:
    return acb(arb(0, radius), arb(0, radius))


def checkpoint_path(paths: dict[str, Path]) -> Path:
    return paths.get(
        "reverse_checkpoint",
        paths["output"].parent
        / f"r{int(paths['output'].name[1:4]):03d}.ckpt.json",
    )


def note_path(index: int, paths: dict[str, Path]) -> Path:
    return paths.get(
        "reverse_note",
        ROOT
        / "proof_corpus"
        / f"MTT_q79HeightFourD{index:03d}ReverseMainHessianInterval_A380B_v1.md",
    )


def certified_affine_base_state(
    index: int,
    selected_main: dict,
) -> tuple[list[acb], base.validated.LiftErrorFrame, list[arb], dict, Path]:
    source_path = base.tight.canonical_paths(index)["main"]
    source = base.load(source_path)
    if source["selected_target"]["root_id"] != selected_main["selected_target"]["root_id"]:
        raise AssertionError("reverse affine source root identity changed")
    if source["selected_target"].get("line_chart") != selected_main["selected_target"].get(
        "line_chart"
    ):
        raise AssertionError("reverse affine source line chart changed")
    transport = source.get("validated_main_transport", {})
    encoded_center = transport.get("center", [])
    lift_radii = transport.get("lift_radius_uppers", [])
    if len(encoded_center) < 5 or not lift_radii:
        raise AssertionError("ordinary main packet has no certified terminal affine lift")
    radius = max(float(value) for value in lift_radii)
    if not math.isfinite(radius) or radius <= 0.0:
        raise ArithmeticError("ordinary terminal affine-lift radius is invalid")
    periods = [
        acb(str(value["real"]), str(value["imaginary"]))
        for value in encoded_center[:5]
    ]
    identity = acb_mat(5, 5)
    for coordinate in range(5):
        identity[coordinate, coordinate] = acb(1)
    frame = base.validated.LiftErrorFrame(
        fundamental=identity,
        coordinate_radii=[arb(format(radius, ".17g")) for _ in range(5)],
    )
    center = periods + [acb(0) for _ in range(72)]
    return center, frame, [arb(0) for _ in range(72)], {
        "method": (
            "certified five-coordinate terminal affine zonotope from the ordinary "
            "cutoff-to-base transport, reused as initial data for the reverse ODE"
        ),
        "source_path": relative(source_path),
        "source_sha256": sha256(source_path),
        "terminal_affine_center": encoded_center[:5],
        "uniform_component_radius_upper": radius,
        "puncture_lift_coordinates_retained": True,
        "compact_H1_only_initializer_used": False,
    }, source_path


def configuration(
    arguments: argparse.Namespace,
    paths: dict[str, Path],
    selected_main: dict,
    cutoff: complex,
    affine_source: Path,
) -> dict:
    value = base.configuration(arguments, paths, selected_main, cutoff)
    value.update(
        {
            "transport_orientation": "smooth_base_to_selected_cutoff_reverse",
            "start": base.pair(0.0 + 0.0j),
            "endpoint": base.pair(cutoff),
            "certified_affine_base_source_sha256": sha256(affine_source),
            "reverse_builder_source_sha256": sha256(Path(__file__).resolve()),
            "C_backed_Taylor_runtime_sha256": sha256(Path(fast.__file__).resolve()),
            "C_backed_Taylor_equivalence_audit_sha256": sha256(FAST_AUDIT),
            "stable_affine_Hessian_runtime_sha256": sha256(
                Path(stable.__file__).resolve()
            ),
            "stable_affine_Hessian_inclusion_audit_sha256": sha256(STABLE_AUDIT),
        }
    )
    return value


def execute(arguments: argparse.Namespace) -> dict:
    started = time.perf_counter()
    paths = base.target_paths(arguments.index)
    if not paths["canonical_main"].is_file():
        raise FileNotFoundError("selected main replay source is absent")
    selected_main = base.load(paths["canonical_main"])
    system, rank, row = base.selected_system(arguments.index, arguments.dps)
    chart = base.dynamic.CHART
    smoke = base.smoke_test(system, chart, min(arguments.order, 18))
    if arguments.smoke_only:
        print(json.dumps(smoke, indent=2))
        return {"smoke_test": smoke}

    _node_center, cutoff = base.canonical_cutoff_start(selected_main)
    epsilon = float(selected_main["selected_target"]["endpoint_cutoff_epsilon"])
    start = 0.0 + 0.0j
    distance = abs(cutoff)
    if distance <= 0.0:
        raise ArithmeticError("reverse main path has zero length")
    direction = cutoff / distance
    center0, frame0, radii0, affine_source_info, affine_source = (
        certified_affine_base_state(arguments.index, selected_main)
    )
    config = configuration(arguments, paths, selected_main, cutoff, affine_source)
    checkpoint = checkpoint_path(paths)

    if arguments.resume:
        saved = base.load(checkpoint)
        if saved.get("schema") != "MTTQ79ReverseTargetMainHessianCheckpoint.v1":
            raise ValueError("reverse Hessian checkpoint schema changed")
        if saved.get("configuration") != config:
            raise ValueError("reverse Hessian checkpoint configuration changed")
        center = [base.validated.decoded_acb(value) for value in saved["center"]]
        frame = base.validated.LiftErrorFrame(
            fundamental=base.validated.decoded_matrix(saved["lift_fundamental"]),
            coordinate_radii=[arb(value) for value in saved["coordinate_radii"]],
        )
        output_radii = [arb(value) for value in saved["output_radii"]]
        accepted = saved["accepted_steps"]
        rejected = int(saved["rejected_step_count"])
        minimum_accepted_step = float(saved["minimum_accepted_step"])
        proposed_step = float(saved["proposed_step"])
        position = float(saved["position"])
        print(
            f"resumed reverse d{arguments.index:03d} steps={len(accepted)} "
            f"fraction={position / distance:.12g}",
            flush=True,
        )
    else:
        center = center0
        frame = frame0
        output_radii = radii0
        accepted = []
        rejected = 0
        minimum_accepted_step = math.inf
        proposed_step = min(arguments.maximum_step, distance / 8.0)
        position = 0.0

    def save_checkpoint() -> None:
        base.validated.atomic_dump(
            checkpoint,
            {
                "schema": "MTTQ79ReverseTargetMainHessianCheckpoint.v1",
                "configuration": config,
                "position": format(position, ".17g"),
                "proposed_step": format(proposed_step, ".17g"),
                "center": [base.validated.encoded_acb(value) for value in center],
                "lift_fundamental": base.validated.encoded_matrix(frame.fundamental),
                "coordinate_radii": [str(value) for value in frame.coordinate_radii],
                "output_radii": [str(value) for value in output_radii],
                "accepted_steps": accepted,
                "rejected_step_count": rejected,
                "minimum_accepted_step": format(minimum_accepted_step, ".17g"),
            },
        )

    while position < distance:
        if len(accepted) >= arguments.maximum_steps:
            raise ArithmeticError("reverse target Hessian exceeded step budget")
        step = min(proposed_step, distance - position)
        if step < arguments.minimum_step:
            raise ArithmeticError("reverse target Hessian requires a smaller step")
        parameter_start = start + direction * position
        try:
            next_center, next_frame, next_radii, diagnostics = (
                base.beta_hessian.validated_affine_hessian_step(
                    system,
                    parameter_start,
                    direction,
                    step,
                    center,
                    frame,
                    output_radii,
                    order=arguments.order,
                    system_builder=base.build_homogeneous_hessian_system,
                )
            )
            if diagnostics["transformed_lift_correction"] > arguments.maximum_lift_correction:
                raise ArithmeticError("reverse lift correction exceeds local budget")
            if diagnostics["maximum_output_increment_error"] > arguments.maximum_output_increment:
                raise ArithmeticError("reverse output increment exceeds local budget")
            if diagnostics["maximum_output_radius"] > arguments.maximum_output_radius:
                raise ArithmeticError("reverse output radius exceeds global budget")
        except (ArithmeticError, ZeroDivisionError, ValueError) as error:
            rejected += 1
            proposed_step = step / 2.0
            if rejected % 10 == 0:
                print(
                    f"reverse d{arguments.index:03d} rejections={rejected} "
                    f"fraction={position / distance:.12g} next={proposed_step:.3e} "
                    f"reason={type(error).__name__}: {error}",
                    flush=True,
                )
            if proposed_step < arguments.minimum_step:
                raise
            continue
        center = next_center
        frame = next_frame
        output_radii = next_radii
        position = min(distance, position + step)
        minimum_accepted_step = min(minimum_accepted_step, step)
        accepted.append(
            {
                "start_arclength": position - step,
                "end_arclength": position,
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
        if len(accepted) % 10 == 0 or position == distance:
            save_checkpoint()
        if len(accepted) <= 3 or len(accepted) % 10 == 0 or position == distance:
            print(
                f"reverse d{arguments.index:03d} steps={len(accepted)} "
                f"fraction={position / distance:.12g} "
                f"radius={max(base.validated.upper(value) for value in output_radii):.3e}",
                flush=True,
            )

    direct_center, direct_frame, _direct_radii, direct_source = base.initial_state(
        system, selected_main, cutoff
    )
    reverse_lift_radius = base.validated.upper(frame.physical_radius())
    direct_lift_radius = base.validated.upper(direct_frame.physical_radius())
    reverse_lift_balls = [
        value + zero_centered_complex_ball(reverse_lift_radius)
        for value in center[:5]
    ]
    direct_lift_balls = [
        value + zero_centered_complex_ball(direct_lift_radius)
        for value in direct_center[:5]
    ]
    lift_overlap = [
        reverse.overlaps(direct)
        for reverse, direct in zip(reverse_lift_balls, direct_lift_balls)
    ]
    lift_difference = [
        base.validated.upper(abs(reverse - direct))
        for reverse, direct in zip(reverse_lift_balls, direct_lift_balls)
    ]
    if not all(lift_overlap):
        raise AssertionError("reverse affine lift does not overlap the direct cutoff source")

    orientation = int(selected_main["orientation"]["selected_sign"])
    ordinary_centers = orientation * np.asarray(
        [base.validated.midpoint(value) for value in center[5:13]],
        dtype=np.complex128,
    )
    ordinary_radii = np.asarray(
        [base.validated.upper(value) for value in output_radii[:8]],
        dtype=np.float64,
    )
    hessian = np.empty((8, 8), dtype=np.complex128)
    hessian_radii = np.empty((8, 8), dtype=np.float64)
    for selected_direction in range(8):
        for residue_index in range(8):
            offset = selected_direction * 8 + residue_index
            hessian[residue_index, selected_direction] = orientation * base.validated.midpoint(
                center[13 + offset]
            )
            hessian_radii[residue_index, selected_direction] = base.validated.upper(
                output_radii[8 + offset]
            )

    canonical_centers = np.asarray(
        [
            base.complex_value(value)
            for value in selected_main["all_eight_main_residue_rows"]["interval_centers"]
        ],
        dtype=np.complex128,
    )
    canonical_radius = float(
        selected_main["all_eight_main_residue_rows"]["common_complex_disk_radius_upper"]
    )
    replay_difference = abs(ordinary_centers - canonical_centers)
    replay_overlap = replay_difference <= ordinary_radii + canonical_radius
    if not bool(np.all(replay_overlap)):
        raise AssertionError("reverse ordinary rows do not overlap the selected main packet")

    payload = {
        "schema": "MTTQ79HeightFourTargetMainHessianInterval.v1",
        "status": "TARGET_REVERSE_MAIN_EIGHT_ROWS_AND_COMPLEX_8_BY_8_HESSIAN_INTERVAL_CERTIFIED",
        "artifact": ARTIFACT,
        "selected_target": {
            "distinguished_index": arguments.index,
            "A219_contribution_rank": rank,
            "root_id": row["root_id"],
            "line_chart": chart,
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
            "main_Hessian_product_box_frobenius_radius_upper": float(
                np.linalg.norm(hessian_radii)
            ),
            "all_canonical_main_intervals_overlap": bool(np.all(replay_overlap)),
            "maximum_canonical_main_center_difference": float(np.max(replay_difference)),
            "all_five_direct_cutoff_periods_overlap": all(lift_overlap),
            "maximum_direct_cutoff_lift_difference_upper": max(lift_difference),
            "accepted_step_count": len(accepted),
            "rejected_step_count": rejected,
            "minimum_accepted_step": minimum_accepted_step,
            "elapsed_seconds": time.perf_counter() - started,
        },
        "smoke_test": smoke,
        "initial_period_source": affine_source_info,
        "terminal_direct_cut_source": direct_source,
        "execution": {
            "configuration": config,
            "steps": accepted,
            "checkpoint": relative(checkpoint),
            "checkpoint_sha256": sha256(checkpoint),
            "stable_affine_Hessian_runtime": {
                "installed": True,
                "growth_integral_majorant": "A*h*exp(L*h)",
                "zero_containing_linear_defect_interval_supported": True,
            },
        },
        "authority": {
            "selected_main_replay_interval": authority(paths["canonical_main"]),
            "certified_affine_base_source": authority(affine_source),
            "A378_Hessian_integrand_source": authority(base.A378),
            "triangular_validated_engine": authority(Path(base.beta_hessian.__file__).resolve()),
            "validated_Taylor_engine": authority(Path(base.validated.__file__).resolve()),
            "direct_cut_period_engine": authority(Path(base.handle.__file__).resolve()),
            "cutoff_root_engine": authority(Path(base.pilot.__file__).resolve()),
            "C_backed_Taylor_runtime": authority(Path(fast.__file__).resolve()),
            "C_backed_Taylor_equivalence_audit": authority(FAST_AUDIT),
            "stable_affine_Hessian_runtime": authority(Path(stable.__file__).resolve()),
            "stable_affine_Hessian_inclusion_audit": authority(STABLE_AUDIT),
            "reverse_builder_source": authority(Path(__file__).resolve()),
        },
        "strict_scope": {
            "observed_SM_values_used": False,
            "same_source_A378_homogeneous_Hessian_rows_used": True,
            "certified_five_coordinate_affine_endpoint_source_used": True,
            "compact_H1_only_initializer_used": False,
            "puncture_lift_coordinates_retained": True,
            "reverse_base_to_cutoff_transport_used": True,
            "all_five_terminal_direct_cut_periods_overlap": True,
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
            "splice this reverse-certified main Hessian to the matching A381 tail"
        ),
    }
    base.dump(paths["output"], payload)
    note = note_path(arguments.index, paths)
    note.write_text(
        f"# MTT q79 Height-Four d{arguments.index:03d} Reverse Main Hessian Interval (A380B) v1\n\n"
        "A380B starts from the ordinary packet's certified five-coordinate affine "
        "base enclosure, including its puncture lift, and validates the same "
        "homogeneous A378 system from the smooth base to the selected cutoff. "
        "Negating the accumulated rows recovers the required cutoff-to-base "
        "orientation. All five terminal lift coordinates overlap an independently "
        "recomputed direct-cut source.\n\n"
        f"The product-box Frobenius radius is `{np.linalg.norm(hessian_radii):.12g}`; "
        "all eight ordinary rows overlap the selected main replay packet. No "
        "observed Standard Model value is used.\n",
        encoding="utf-8",
    )
    print(f"wrote {relative(paths['output'])}")
    print(f"wrote {relative(note)}")
    print(json.dumps(payload["summary"], indent=2))
    return payload


def parser() -> argparse.ArgumentParser:
    value = argparse.ArgumentParser()
    value.add_argument("--index", type=int, required=True)
    value.add_argument("--dps", type=int, default=120)
    value.add_argument("--order", type=int, default=48)
    value.add_argument("--maximum-step", type=float, default=0.02)
    value.add_argument("--minimum-step", type=float, default=1.0e-12)
    value.add_argument("--maximum-steps", type=int, default=50000)
    value.add_argument("--maximum-lift-correction", type=float, default=1.0e-7)
    value.add_argument("--maximum-output-increment", type=float, default=1.0e-5)
    value.add_argument("--maximum-output-radius", type=float, default=0.005)
    value.add_argument("--resume", action="store_true")
    value.add_argument("--smoke-only", action="store_true")
    return value


def main() -> int:
    arguments = parser().parse_args()
    if not 1 <= arguments.index <= 90:
        raise ValueError("index must lie in [1,90]")
    ctx.dps = arguments.dps
    fast.install()
    stable.install()
    try:
        execute(arguments)
    finally:
        stable.uninstall()
        fast.uninstall()
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
