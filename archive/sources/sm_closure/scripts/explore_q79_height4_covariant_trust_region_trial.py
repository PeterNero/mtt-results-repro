from __future__ import annotations

import argparse
import hashlib
import json
import time
from concurrent.futures import ProcessPoolExecutor, as_completed
from pathlib import Path

import numpy as np
from flint import ctx
from scipy.linalg import expm

import explore_q79_height4_covariant_floating_probe as probe


ROOT = probe.ROOT
JACOBIAN = (
    probe.PROBE_DIRECTORY / "height4_covariant_floating_jacobian.packet.json"
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


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser()
    parser.add_argument("--rank", type=int, choices=(2, 3, 4, 5), default=4)
    parser.add_argument("--scale", type=float, required=True)
    parser.add_argument("--workers", type=int, default=4)
    parser.add_argument("--force", action="store_true")
    parser.add_argument("--critical-only", action="store_true")
    return parser.parse_args()


def scale_tag(value: float) -> str:
    return format(value, ".3e").replace("+", "p").replace("-", "m").replace(".", "d")


def main() -> int:
    arguments = parse_args()
    if not 0 < arguments.scale <= 1:
        raise ValueError("scale must lie in (0,1]")
    ctx.dps = 100
    started = time.perf_counter()
    jacobian_packet = load(JACOBIAN)
    if not jacobian_packet["strict_scope"]["all_eight_directions_executed"]:
        raise AssertionError("the full eight-direction floating Jacobian is unavailable")
    selected = next(
        row
        for row in jacobian_packet["candidate_Jacobians"]
        if int(row["A132_objective_rank"]) == arguments.rank
    )
    full_step = np.asarray(
        selected["local_least_squares_step_on_available_directions"],
        dtype=np.float64,
    )
    delta = arguments.scale * full_step
    tag = f"tr{arguments.rank}_s{scale_tag(arguments.scale)}"
    output_directory = probe.PROBE_DIRECTORY / tag
    output = output_directory / "trial.packet.json"
    if output.exists() and not arguments.force and not arguments.critical_only:
        print(f"cached {relative(output)}")
        print(json.dumps(load(output)["summary"], indent=2))
        return 0

    a208 = load(probe.A208)
    candidates = a208["height_four_candidates"][1:]
    support = sorted(
        {
            int(row["distinguished_index"])
            for candidate in candidates
            for row in candidate["primitive_thimble_chain"]
        }
    )
    orientation = load(probe.ORIENTATION)
    support = sorted(
        set(support)
        | {int(value) for value in orientation["unimodular_pivot_indices_one_based"]}
    )
    evaluator = probe.PGL3BetaEvaluator()
    tangent = sum(
        (
            delta[index] * evaluator.generators[index]
            for index in range(8)
        ),
        np.zeros((3, 3), dtype=np.complex128),
    )
    base_alignment = probe.central_alignment()
    alignment = base_alignment @ expm(tangent)
    output_directory.mkdir(parents=True, exist_ok=True)
    y_path = output_directory / "fy.packet.json"
    z_path = output_directory / "fz.packet.json"
    dump(y_path, probe.build_point_fibration(alignment, "y"))
    dump(z_path, probe.build_point_fibration(alignment, "z"))
    centers, critical_diagnostics = probe.continued_critical_centers(alignment)
    preflight = {
        "schema": "MTTQ79CovariantTrustRegionPreflight.v1",
        "candidate_rank": arguments.rank,
        "scale": arguments.scale,
        "full_step": [float(value) for value in full_step],
        "scaled_step": [float(value) for value in delta],
        "scaled_step_maximum_absolute_coordinate": float(np.max(abs(delta))),
        "critical_continuation": critical_diagnostics,
        "elapsed_seconds": time.perf_counter() - started,
    }
    dump(output_directory / "preflight.packet.json", preflight)
    if arguments.critical_only:
        print(json.dumps(preflight, indent=2))
        return 0
    crossed_handles = [
        name
        for name, row in critical_diagnostics[
            "fixed_handle_path_wall_diagnostics"
        ].items()
        if not row["same_fixed_handle_chamber"]
    ]
    if crossed_handles:
        raise AssertionError(
            "trust-region step crosses fixed handle wall(s): "
            + ", ".join(crossed_handles)
        )

    fan_by_index = {
        int(row["distinguished_index"]): row
        for row in load(probe.FAN)["distinguished_positive_meridians"]
    }
    cache_directory = output_directory / "thimbles"
    cache_directory.mkdir(parents=True, exist_ok=True)
    thimbles: dict[int, dict] = {}
    tasks = []
    for index in support:
        fan_row = fan_by_index[index]
        cache = cache_directory / f"t{index:03d}.json"
        expected_center = centers[fan_row["root_id"]]
        if cache.exists() and not arguments.force:
            cached = load(cache)
            cached_center = probe.complex_value(cached["critical_center"])
            if (
                cached.get("cache_algorithm") == probe.THIMBLE_CACHE_ALGORITHM
                and abs(cached_center - expected_center) <= 1.0e-14
            ):
                thimbles[index] = cached
                continue
        tasks.append(
            {
                "distinguished_index": index,
                "root_id": fan_row["root_id"],
                "central_packet_path": str(
                    probe.central_period_path(index, fan_row["root_id"])
                ),
                "critical_center": [expected_center.real, expected_center.imag],
                "y_fibration": str(y_path),
                "z_fibration": str(z_path),
            }
        )
    if tasks:
        with ProcessPoolExecutor(max_workers=arguments.workers) as executor:
            futures = {
                executor.submit(probe.thimble_worker, task): task for task in tasks
            }
            for completed, future in enumerate(as_completed(futures), start=1):
                row = future.result()
                index = int(row["distinguished_index"])
                thimbles[index] = row
                dump(cache_directory / f"t{index:03d}.json", row)
                print(f"[{completed}/{len(tasks)}] continued d{index:03d}", flush=True)

    factorization = load(probe.FACTORIZATION)
    vectors = np.asarray(
        [
            row["positive_vanishing_cycle_up_to_sign"]
            for row in factorization["factors"]
        ],
        dtype=np.int64,
    ).T
    pivots = np.asarray(
        [
            int(value) - 1
            for value in orientation["unimodular_pivot_indices_one_based"]
        ],
        dtype=np.int64,
    )
    homology = load(probe.HOMOLOGY)["homology_convention"]
    y_to_z = probe.moving_y_to_z_transition(y_path, alignment, homology)
    pivot_columns = []
    for index in pivots:
        row = thimbles[int(index) + 1]
        values = probe.complex_vector(row["base_fiber_propagated_periods"])
        if row["line_chart"] == "z":
            values = np.linalg.solve(y_to_z, values)
        pivot_columns.append(values)
    pivot_periods = np.column_stack(pivot_columns)
    pivot_signs = np.asarray(orientation["pivot_signs"], dtype=np.int64)
    marked_basis = (pivot_periods * pivot_signs[np.newaxis, :]) @ np.linalg.inv(
        vectors[:, pivots]
    )
    actions = {
        name: np.asarray(factorization["handle_actions"][name], dtype=np.int64)
        for name in ("A", "B")
    }
    central_lifts = {
        name: int(value)
        for name, value in load(probe.CENTRAL_LIFTS)["selected_lifts"].items()
    }
    handle_blocks = []
    handle_rows = []
    for name, displacement in (("A", 1 + 0j), ("B", 1j)):
        block, diagnostics = probe.execute_moving_handle(
            name,
            displacement,
            actions[name],
            central_lifts[name],
            marked_basis,
            homology,
            y_path,
        )
        handle_blocks.append(block)
        handle_rows.append(diagnostics)
    handles = np.hstack(handle_blocks)

    center_floating_beta, wound_reference, anchor_packet = probe.beta_anchor(
        base_alignment
    )
    perturbed_floating_beta, beta_diagnostics = evaluator.evaluate(
        alignment,
        line_chart="y",
        base_lift_source_chart="z",
        rtol=2.0e-9,
        atol=2.0e-11,
        winding_reference=wound_reference,
    )
    certified_beta, certified_beta_path = probe.selected_certified_beta()
    anchored_beta = certified_beta + perturbed_floating_beta - center_floating_beta
    column_signs = np.asarray(orientation["column_signs"], dtype=np.int64)
    jacobian_by_id = {
        row["candidate_id"]: row for row in jacobian_packet["candidate_Jacobians"]
    }
    candidate_rows = []
    for candidate in candidates:
        period = np.zeros(8, dtype=np.complex128)
        for row in candidate["primitive_thimble_chain"]:
            index = int(row["distinguished_index"])
            value = probe.complex_vector(thimbles[index]["period_values"])
            period += int(row["coefficient"]) * column_signs[index - 1] * value
        period += handles @ np.asarray(
            candidate["primitive_handle_coordinates"], dtype=np.float64
        )
        residual = anchored_beta - period
        jacobian_row = jacobian_by_id[candidate["candidate_id"]]
        center = probe.complex_vector(jacobian_row["center_residual"])
        jacobian = np.asarray(
            [
                [probe.complex_value(value) for value in row]
                for row in jacobian_row["covariant_residual_Jacobian_8_by_k"]
            ],
            dtype=np.complex128,
        )
        linearized = center + jacobian @ delta
        candidate_rows.append(
            {
                "candidate_id": candidate["candidate_id"],
                "A132_objective_rank": candidate["A132_objective_rank"],
                "actual_residual": probe.encoded_complex_vector(residual),
                "actual_residual_l2_norm": float(np.linalg.norm(residual)),
                "actual_residual_maximum_absolute_value": float(
                    np.max(abs(residual))
                ),
                "linearized_residual": probe.encoded_complex_vector(linearized),
                "linearized_residual_l2_norm": float(np.linalg.norm(linearized)),
                "linearized_residual_maximum_absolute_value": float(
                    np.max(abs(linearized))
                ),
                "nonlinear_model_error_l2_norm": float(
                    np.linalg.norm(residual - linearized)
                ),
                "center_residual_l2_norm": float(np.linalg.norm(center)),
                "actual_reduction_factor": float(
                    np.linalg.norm(residual) / np.linalg.norm(center)
                ),
            }
        )
    selected_trial = next(
        row
        for row in candidate_rows
        if int(row["A132_objective_rank"]) == arguments.rank
    )
    packet = {
        "schema": "MTTQ79HeightFourCovariantTrustRegionTrial.v1",
        "status": "SAME_SOURCE_NONLINEAR_TRUST_REGION_TRIAL_EXECUTED",
        "candidate_rank_used_for_step": arguments.rank,
        "scale": arguments.scale,
        "full_least_squares_step": [float(value) for value in full_step],
        "executed_step": [float(value) for value in delta],
        "executed_step_maximum_absolute_coordinate": float(np.max(abs(delta))),
        "alignment": probe.encoded_complex_matrix(alignment),
        "critical_continuation": critical_diagnostics,
        "moving_handles": {
            "diagnostics": handle_rows,
            "primitive_handle_period_matrix": probe.encoded_complex_matrix(handles),
        },
        "moving_beta": {
            "branch_route": probe.BETA_BRANCH_ROUTE,
            "center_anchor_difference": anchor_packet[
                "floating_to_certified_maximum_absolute_difference"
            ],
            "certified_beta_path": relative(certified_beta_path),
            "diagnostics": beta_diagnostics,
        },
        "candidate_trials": candidate_rows,
        "summary": {
            "selected_candidate_rank": arguments.rank,
            "selected_center_residual_l2_norm": selected_trial[
                "center_residual_l2_norm"
            ],
            "selected_actual_residual_l2_norm": selected_trial[
                "actual_residual_l2_norm"
            ],
            "selected_linearized_residual_l2_norm": selected_trial[
                "linearized_residual_l2_norm"
            ],
            "selected_actual_reduction_factor": selected_trial[
                "actual_reduction_factor"
            ],
            "selected_nonlinear_model_error_l2_norm": selected_trial[
                "nonlinear_model_error_l2_norm"
            ],
            "elapsed_seconds": time.perf_counter() - started,
        },
        "authority": {
            "Jacobian": relative(JACOBIAN),
            "Jacobian_sha256": sha256(JACOBIAN),
            "probe_engine_source": relative(Path(probe.__file__).resolve()),
            "probe_engine_source_sha256": sha256(Path(probe.__file__).resolve()),
            "runner_source": relative(Path(__file__)),
            "runner_source_sha256": sha256(Path(__file__)),
        },
        "strict_scope": {
            "same_source_nonlinear_trial": True,
            "same_fixed_handle_chamber": True,
            "floating_only": True,
            "interval_zero_certificate": False,
            "covariant_zero_proved": False,
            "observed_SM_values_used": False,
        },
    }
    dump(output, packet)
    print(f"wrote {relative(output)}")
    print(json.dumps(packet["summary"], indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
