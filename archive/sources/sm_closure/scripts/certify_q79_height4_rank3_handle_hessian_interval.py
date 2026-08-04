from __future__ import annotations

import argparse
import hashlib
import json
import math
import time
from pathlib import Path

import numpy as np
from flint import acb, acb_mat, arb, ctx

import certify_q79_height4_rank3_beta_hessian_interval as beta_hessian
import certify_q79_height4_rank3_handle_combination_interval as handle
import certify_q79_height4_target_main_hessian_interval as main_hessian
import certify_q79_selected_side_beta_defect_transport as validated


ROOT = Path(__file__).resolve().parents[1]
VALIDATED = handle.PROBE / "validated_transport"
A374 = handle.OUTPUT
A378 = main_hessian.A378
OUTPUT = VALIDATED / "n3.rank3.handle_hessian.interval.json"
CHECKPOINT_A = VALIDATED / "n3.handleA.hessian.checkpoint.json"
CHECKPOINT_B = VALIDATED / "n3.handleB.hessian.checkpoint.json"
NOTE = ROOT / "proof_corpus" / "MTT_q79HeightFourRank3HandleHessianInterval_A383_v1.md"
ARTIFACT = "A383"


def load(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def dump(path: Path, value: dict) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(value, indent=2, sort_keys=True) + "\n", encoding="utf-8")


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def relative(path: Path) -> str:
    return str(path.relative_to(ROOT)).replace("\\", "/")


def pair(value: complex) -> dict[str, str]:
    return {
        "real": format(float(value.real), ".17g"),
        "imaginary": format(float(value.imag), ".17g"),
    }


def complex_value(value: dict[str, str]) -> complex:
    return complex(float(value["real"]), float(value["imaginary"]))


def initial_state(
    initial_periods: list[acb],
) -> tuple[list[acb], validated.LiftErrorFrame, list[arb]]:
    center = [
        validated.SelectedQ79IntervalSystem.midpoint_acb(value)
        for value in initial_periods
    ] + [acb(0) for _ in range(72)]
    fundamental = acb_mat(5, 5)
    for index in range(5):
        fundamental[index, index] = acb(1)
    frame = validated.LiftErrorFrame(
        fundamental=fundamental,
        coordinate_radii=[value.rad().upper() for value in initial_periods],
    )
    return center, frame, [arb(0) for _ in range(72)]


def configuration(
    arguments: argparse.Namespace,
    *,
    label: str,
    endpoint: complex,
    initial_periods: list[acb],
) -> dict:
    return {
        "label": label,
        "endpoint": pair(endpoint),
        "dps": arguments.dps,
        "order": arguments.order,
        "initial_step": format(arguments.initial_step, ".17g"),
        "minimum_step": format(arguments.minimum_step, ".17g"),
        "maximum_lift_correction": format(
            arguments.maximum_lift_correction, ".17g"
        ),
        "maximum_output_increment": format(
            arguments.maximum_output_increment, ".17g"
        ),
        "maximum_output_radius": format(arguments.maximum_output_radius, ".17g"),
        "initial_periods": [validated.encoded_acb(value) for value in initial_periods],
        "A374_sha256": sha256(A374),
        "A378_sha256": sha256(A378),
        "homogeneous_hessian_builder_sha256": sha256(
            Path(main_hessian.__file__).resolve()
        ),
        "validated_step_engine_sha256": sha256(
            Path(beta_hessian.__file__).resolve()
        ),
        "builder_source_sha256": sha256(Path(__file__).resolve()),
    }


def execute_path(
    system: validated.SelectedQ79IntervalSystem,
    initial_periods: list[acb],
    *,
    endpoint: complex,
    label: str,
    checkpoint_path: Path,
    arguments: argparse.Namespace,
) -> dict:
    started = time.perf_counter()
    if abs(endpoint) != 1.0:
        raise AssertionError("selected handle endpoint must have unit path length")
    config = configuration(
        arguments,
        label=label,
        endpoint=endpoint,
        initial_periods=initial_periods,
    )
    if arguments.resume and checkpoint_path.exists():
        checkpoint = load(checkpoint_path)
        if checkpoint.get("schema") != "MTTQ79Rank3HandleHessianCheckpoint.v1":
            raise ValueError(f"stale handle-Hessian checkpoint {checkpoint_path.name}")
        if checkpoint.get("configuration") != config:
            raise ValueError(f"handle-Hessian configuration changed for {label}")
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
        position = float(checkpoint["position"])
        print(
            f"resumed {label} Hessian steps={len(accepted)} position={position:.12g}",
            flush=True,
        )
    else:
        center, frame, output_radii = initial_state(initial_periods)
        accepted = []
        rejected = 0
        minimum_accepted_step = math.inf
        proposed_step = arguments.initial_step
        position = 0.0

    def save_checkpoint() -> None:
        validated.atomic_dump(
            checkpoint_path,
            {
                "schema": "MTTQ79Rank3HandleHessianCheckpoint.v1",
                "configuration": config,
                "position": format(position, ".17g"),
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

    while position < 1.0:
        if len(accepted) >= arguments.maximum_steps:
            raise ArithmeticError(f"{label} Hessian exceeded step budget")
        step = min(proposed_step, 1.0 - position)
        if step < arguments.minimum_step:
            raise ArithmeticError(f"{label} Hessian requires a smaller step")
        start = endpoint * position
        try:
            next_center, next_frame, next_radii, diagnostics = (
                beta_hessian.validated_affine_hessian_step(
                    system,
                    start,
                    endpoint,
                    step,
                    center,
                    frame,
                    output_radii,
                    order=arguments.order,
                    system_builder=main_hessian.build_homogeneous_hessian_system,
                )
            )
            if (
                diagnostics["transformed_lift_correction"]
                > arguments.maximum_lift_correction
            ):
                raise ArithmeticError("lift correction exceeds local budget")
            if (
                diagnostics["maximum_output_increment_error"]
                > arguments.maximum_output_increment
            ):
                raise ArithmeticError("output increment exceeds local budget")
            if diagnostics["maximum_output_radius"] > arguments.maximum_output_radius:
                raise ArithmeticError("output radius exceeds global budget")
        except (ArithmeticError, ZeroDivisionError, ValueError) as error:
            rejected += 1
            proposed_step = step / 2.0
            if rejected % 10 == 0:
                print(
                    f"{label} Hessian rejections={rejected} position={position:.12g} "
                    f"next={proposed_step:.3e} reason={type(error).__name__}: {error}",
                    flush=True,
                )
            if proposed_step < arguments.minimum_step:
                raise
            continue
        center = next_center
        frame = next_frame
        output_radii = next_radii
        position = min(1.0, position + step)
        minimum_accepted_step = min(minimum_accepted_step, step)
        accepted.append(
            {
                "start_position": position - step,
                "end_position": position,
                "step": step,
                **diagnostics,
            }
        )
        quality = max(
            diagnostics["maximum_reduction_neumann_norm"],
            diagnostics["fundamental_inverse_neumann_norm"],
        )
        proposed_step = min(
            arguments.initial_step,
            step * (1.5 if quality < 0.25 else 1.15),
        )
        if len(accepted) % 10 == 0 or position == 1.0:
            save_checkpoint()
        if len(accepted) <= 3 or len(accepted) % 10 == 0 or position == 1.0:
            print(
                f"{label} Hessian steps={len(accepted)} position={position:.12g} "
                f"radius={max(validated.upper(value) for value in output_radii):.3e}",
                flush=True,
            )

    ordinary_centers = np.asarray(
        [validated.midpoint(value) for value in center[5:13]],
        dtype=np.complex128,
    )
    ordinary_radii = np.asarray(
        [validated.upper(value) for value in output_radii[:8]],
        dtype=np.float64,
    )
    hessian_centers = np.empty((8, 8), dtype=np.complex128)
    hessian_radii = np.empty((8, 8), dtype=np.float64)
    for column in range(8):
        for row in range(8):
            offset = column * 8 + row
            hessian_centers[row, column] = validated.midpoint(center[13 + offset])
            hessian_radii[row, column] = validated.upper(output_radii[8 + offset])
    return {
        "label": label,
        "endpoint": pair(endpoint),
        "ordinary_centers": ordinary_centers,
        "ordinary_radii": ordinary_radii,
        "hessian_centers": hessian_centers,
        "hessian_radii": hessian_radii,
        "accepted_steps": accepted,
        "accepted_step_count": len(accepted),
        "rejected_step_count": rejected,
        "minimum_accepted_step": minimum_accepted_step,
        "maximum_output_radius": float(np.max(hessian_radii)),
        "elapsed_seconds": time.perf_counter() - started,
        "checkpoint": relative(checkpoint_path),
        "checkpoint_sha256": sha256(checkpoint_path),
    }


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--dps", type=int, default=90)
    parser.add_argument("--order", type=int, default=20)
    parser.add_argument("--initial-step", type=float, default=0.006)
    parser.add_argument("--minimum-step", type=float, default=1.0e-10)
    parser.add_argument("--maximum-steps", type=int, default=50000)
    parser.add_argument("--maximum-lift-correction", type=float, default=1.0e-6)
    parser.add_argument("--maximum-output-increment", type=float, default=2.0e-3)
    parser.add_argument("--maximum-output-radius", type=float, default=0.25)
    parser.add_argument("--cut-segments", type=int, default=12)
    parser.add_argument("--cut-tolerance", type=float, default=1.0e-28)
    parser.add_argument("--resume", action="store_true")
    parser.add_argument("--smoke-only", action="store_true")
    arguments = parser.parse_args()
    ctx.dps = arguments.dps

    a374 = load(A374)
    coordinates = [
        int(value)
        for value in a374["selected_rank3_chain"]["primitive_handle_coordinates"]
    ]
    if coordinates != handle.EXPECTED_COORDINATES:
        raise AssertionError("A374 handle coordinates changed")
    system = handle.n3_engine.exact_target_system(arguments.dps)
    smoke = main_hessian.smoke_test(system, system.line_chart, min(arguments.order, 18))
    if arguments.smoke_only:
        print(json.dumps(smoke, indent=2))
        return 0
    basis, basis_diagnostics = handle.oriented_n3_base_cycles(
        system,
        cut_segments=arguments.cut_segments,
        cut_tolerance=arguments.cut_tolerance,
    )
    a_initial = handle.combine_basis(basis, coordinates[:4])
    b_initial = handle.combine_basis(basis, coordinates[4:])
    a_path = execute_path(
        system,
        a_initial,
        endpoint=-1j,
        label="n3 rank-3 A-handle combination",
        checkpoint_path=CHECKPOINT_A,
        arguments=arguments,
    )
    b_path = execute_path(
        system,
        b_initial,
        endpoint=1 + 0j,
        label="n3 rank-3 B-handle combination",
        checkpoint_path=CHECKPOINT_B,
        arguments=arguments,
    )

    ordinary_centers = a_path["ordinary_centers"] + b_path["ordinary_centers"]
    ordinary_radii = a_path["ordinary_radii"] + b_path["ordinary_radii"]
    hessian_centers = a_path["hessian_centers"] + b_path["hessian_centers"]
    hessian_radii = a_path["hessian_radii"] + b_path["hessian_radii"]
    reference_centers = np.asarray(
        [
            complex_value(row["interval_center"])
            for row in a374["all_eight_handle_rows"]
        ],
        dtype=np.complex128,
    )
    reference_radii = np.asarray(
        [
            float(row["uniform_component_radius_upper"])
            for row in a374["all_eight_handle_rows"]
        ],
        dtype=np.float64,
    )
    differences = abs(ordinary_centers - reference_centers)
    overlap = differences <= ordinary_radii + reference_radii
    if not bool(np.all(overlap)):
        raise AssertionError("handle-Hessian ordinary rows do not overlap A374")

    payload = {
        "schema": "MTTQ79HeightFourRank3HandleHessianInterval.v1",
        "status": "N3_RANK3_HANDLE_COMPLEX_8_BY_8_HESSIAN_INTERVAL_CERTIFIED",
        "artifact": ARTIFACT,
        "selected_rank3_chain": {
            **a374["selected_rank3_chain"],
            "Hessian_identity": "D H_n3 = D transport_A + D transport_B",
        },
        "rigorous_base_cut_basis": basis_diagnostics,
        "handle_rows": [
            {
                "residue_index_zero_based": row,
                "interval_center": pair(ordinary_centers[row]),
                "component_radius_upper": float(ordinary_radii[row]),
                "A374_center_difference": float(differences[row]),
                "A374_intervals_overlap": bool(overlap[row]),
            }
            for row in range(8)
        ],
        "complex_handle_Hessian_8_by_8": [
            [
                {
                    "row_zero_based": row,
                    "column_zero_based": column,
                    "interval_center": pair(hessian_centers[row, column]),
                    "component_radius_upper": float(hessian_radii[row, column]),
                }
                for column in range(8)
            ]
            for row in range(8)
        ],
        "path_executions": {
            "A": {
                key: value
                for key, value in a_path.items()
                if key not in {
                    "ordinary_centers",
                    "ordinary_radii",
                    "hessian_centers",
                    "hessian_radii",
                }
            },
            "B": {
                key: value
                for key, value in b_path.items()
                if key not in {
                    "ordinary_centers",
                    "ordinary_radii",
                    "hessian_centers",
                    "hessian_radii",
                }
            },
        },
        "summary": {
            "certified_handle_rows": 8,
            "certified_handle_Hessian_entries": 64,
            "maximum_handle_row_component_radius_upper": float(np.max(ordinary_radii)),
            "maximum_handle_Hessian_component_radius_upper": float(np.max(hessian_radii)),
            "handle_Hessian_product_box_frobenius_radius_upper": float(
                np.linalg.norm(hessian_radii)
            ),
            "all_A374_handle_intervals_overlap": bool(np.all(overlap)),
            "maximum_A374_center_difference": float(np.max(differences)),
        },
        "smoke_test": smoke,
        "authority": {
            name: {"path": relative(path), "sha256": sha256(path)}
            for name, path in {
                "A374_handle_combination": A374,
                "A378_Hessian_integrand_source": A378,
                "A380_homogeneous_Hessian_engine": Path(main_hessian.__file__).resolve(),
                "A379_validated_Hessian_step": Path(beta_hessian.__file__).resolve(),
                "A_path_checkpoint": CHECKPOINT_A,
                "B_path_checkpoint": CHECKPOINT_B,
                "builder_source": Path(__file__).resolve(),
            }.items()
        },
        "strict_scope": {
            "observed_SM_values_used": False,
            "selected_handle_coordinates_inherited_before_Hessian_execution": True,
            "same_source_A378_homogeneous_Hessian_rows_used": True,
            "ordinary_handle_rows_independently_replayed": True,
            "rank3_handle_Hessian_interval_closed": True,
            "full_76_target_chain_Hessian_interval_closed": False,
            "full_residual_interval_Jacobian_closed": False,
            "interval_Newton_existence_and_uniqueness_closed": False,
            "covariant_zero_proved": False,
            "full_SM_closure_proved": False,
        },
        "next_required_artifact": (
            "combine A383 with A379, the 76 selected target Hessians, and the "
            "preselected Picard-Lefschetz correction"
        ),
    }
    dump(OUTPUT, payload)
    NOTE.write_text(
        "# MTT q79 Height-Four Rank-3 Handle Hessian Interval (A383) v1\n\n"
        "A383 differentiates the two A374 homogeneous handle transports using "
        "the same A378 covariant source rows as the target Hessians. The fixed "
        "rank-3 handle coordinates are inherited before execution.\n\n"
        f"All 64 complex entries are certified; the product-box Frobenius radius "
        f"is `{np.linalg.norm(hessian_radii):.12g}`. The eight ordinary rows "
        "independently overlap A374.\n",
        encoding="utf-8",
    )
    print(f"wrote {relative(OUTPUT)}")
    print(f"wrote {relative(NOTE)}")
    print(json.dumps(payload["summary"], indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
