from __future__ import annotations

import argparse
import hashlib
import json
import time
from concurrent.futures import ProcessPoolExecutor, as_completed
from pathlib import Path

import numpy as np
from flint import ctx
import explore_q79_height4_covariant_floating_probe as probe


ROOT = probe.ROOT
BASE_TRIAL = probe.PROBE_DIRECTORY / "tr3_s1d000ep00" / "trial.packet.json"
A212 = probe.PROBE_DIRECTORY / "height4_picard_lefschetz_corrected_newton.packet.json"
PROPOSAL = probe.PROBE_DIRECTORY / "rank4_PL_recentered_step_01.packet.json"


def load(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def dump(path: Path, value: dict) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(value, indent=2, sort_keys=True) + "\n", encoding="utf-8")


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def relative(path: Path) -> str:
    return str(path.relative_to(ROOT)).replace("\\", "/")


def selected_radial_wall_coordinate(centers: dict[str, complex]) -> dict:
    start = 0.25 + 0.25j
    end = centers["selected_039"]
    vector = end - start
    squared_length = vector.real**2 + vector.imag**2
    rows = []
    for real_shift in range(-2, 3):
        for imaginary_shift in range(-2, 3):
            point = centers["selected_038"] + real_shift + 1j * imaginary_shift
            offset = point - start
            parameter = (
                offset.real * vector.real + offset.imag * vector.imag
            ) / squared_length
            if not 0 < parameter < 1:
                continue
            signed = (
                vector.real * offset.imag - vector.imag * offset.real
            ) / abs(vector)
            rows.append(
                {
                    "longitudinal_parameter": float(parameter),
                    "signed_transverse_coordinate": float(signed),
                    "clearance": float(abs(signed)),
                    "deck_shift": [real_shift, imaginary_shift],
                }
            )
    if not rows:
        raise AssertionError("selected radial wall left the interior segment")
    return min(rows, key=lambda row: row["clearance"])


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser()
    parser.add_argument("--workers", type=int, default=4)
    parser.add_argument("--force", action="store_true")
    return parser.parse_args()


def main() -> int:
    arguments = parse_args()
    ctx.dps = 100
    started = time.perf_counter()
    base_trial = load(BASE_TRIAL)
    a212 = load(A212)
    proposal = load(PROPOSAL)
    if a212["continuation_rule"]["selected_integer_coefficient"] != 1:
        raise AssertionError("A212 PL jump coefficient changed")
    if (
        proposal["candidate_rank"] != 4
        or proposal["selected_scale"] != 1.0
        or proposal["summary"]["crossing_count"] != 0
    ):
        raise AssertionError("rank-4 proposal is not the chamber-safe full step")
    delta = np.asarray(proposal["selected_step"], dtype=np.float64)
    tag = "tr4_PL_three_wall_step01"
    output_directory = probe.PROBE_DIRECTORY / tag
    output = output_directory / "trial.packet.json"
    if output.exists() and not arguments.force:
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
    base_alignment = probe.complex_matrix(proposal["base_alignment"])
    alignment = probe.complex_matrix(proposal["target_alignment"])
    output_directory.mkdir(parents=True, exist_ok=True)
    y_path = output_directory / "fy.packet.json"
    z_path = output_directory / "fz.packet.json"
    dump(y_path, probe.build_point_fibration(alignment, "y"))
    dump(z_path, probe.build_point_fibration(alignment, "z"))
    centers, critical_diagnostics = probe.continued_critical_centers(alignment)
    radial_wall = selected_radial_wall_coordinate(centers)
    if radial_wall["signed_transverse_coordinate"] >= 0:
        raise AssertionError("PL-recentered probe returned to the pre-wall chamber")
    preflight = {
        "schema": "MTTQ79CovariantPLRank4TrialPreflight.v1",
        "candidate_rank": 4,
        "proposal": relative(PROPOSAL),
        "executed_step": [float(value) for value in delta],
        "executed_step_maximum_absolute_coordinate": float(np.max(abs(delta))),
        "critical_continuation": critical_diagnostics,
        "selected_039_selected_038_radial_wall": radial_wall,
        "elapsed_seconds": time.perf_counter() - started,
    }
    dump(output_directory / "preflight.packet.json", preflight)
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
        probe.central_alignment()
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
    center_rows = {
        row["candidate_id"]: row
        for row in next(
            trial
            for trial in a212["corrected_trials"]
            if float(trial["scale"]) == 1.0
        )["candidate_rows"]
    }
    crossing_period = probe.complex_vector(thimbles[65]["period_values"])
    candidate_rows = []
    for candidate in candidates:
        raw_period = np.zeros(8, dtype=np.complex128)
        coefficients = {}
        for chain_row in candidate["primitive_thimble_chain"]:
            index = int(chain_row["distinguished_index"])
            coefficients[index] = int(chain_row["coefficient"])
            value = probe.complex_vector(thimbles[index]["period_values"])
            raw_period += coefficients[index] * column_signs[index - 1] * value
        raw_period += handles @ np.asarray(
            candidate["primitive_handle_coordinates"], dtype=np.float64
        )
        period_correction = coefficients.get(64, 0) * column_signs[63] * crossing_period
        corrected_period = raw_period + period_correction
        raw_residual = anchored_beta - raw_period
        corrected_residual = anchored_beta - corrected_period
        center_residual = probe.complex_vector(
            center_rows[candidate["candidate_id"]]["PL_corrected_residual"]
        )
        row = {
                "candidate_id": candidate["candidate_id"],
                "A132_objective_rank": candidate["A132_objective_rank"],
                "primitive_d064_coefficient": coefficients.get(64, 0),
                "raw_moving_period": probe.encoded_complex_vector(raw_period),
                "PL_period_correction": probe.encoded_complex_vector(period_correction),
                "PL_corrected_moving_period": probe.encoded_complex_vector(corrected_period),
                "raw_residual": probe.encoded_complex_vector(raw_residual),
                "PL_corrected_residual": probe.encoded_complex_vector(corrected_residual),
                "PL_corrected_residual_l2_norm": float(np.linalg.norm(corrected_residual)),
                "PL_corrected_residual_maximum_absolute_value": float(
                    np.max(abs(corrected_residual))
                ),
                "base_PL_corrected_residual": probe.encoded_complex_vector(center_residual),
                "change_from_base_PL_corrected_residual_l2_norm": float(
                    np.linalg.norm(corrected_residual - center_residual)
                ),
        }
        candidate_rows.append(row)
    selected_trial = next(
        row
        for row in candidate_rows
        if int(row["A132_objective_rank"]) == 4
    )
    predicted_residual = probe.complex_vector(
        proposal["selected_predicted_residual"]
    )
    actual_residual = probe.complex_vector(
        selected_trial["PL_corrected_residual"]
    )
    base_residual = probe.complex_vector(
        selected_trial["base_PL_corrected_residual"]
    )
    packet = {
        "schema": "MTTQ79HeightFourCovariantPLRank4Trial.v1",
        "status": "SAME_SOURCE_PL_RANK4_NONLINEAR_TRIAL_EXECUTED",
        "tag": tag,
        "candidate_rank_used_for_step": 4,
        "proposal": relative(PROPOSAL),
        "executed_step": [float(value) for value in delta],
        "executed_step_maximum_absolute_coordinate": float(np.max(abs(delta))),
        "base_alignment": probe.encoded_complex_matrix(base_alignment),
        "alignment": probe.encoded_complex_matrix(alignment),
        "critical_continuation": critical_diagnostics,
        "selected_039_selected_038_radial_wall": radial_wall,
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
        "candidate_residuals": candidate_rows,
        "summary": {
            "selected_candidate_rank": 4,
            "selected_base_PL_corrected_residual_l2_norm": float(np.linalg.norm(base_residual)),
            "selected_actual_PL_corrected_residual_l2_norm": selected_trial[
                "PL_corrected_residual_l2_norm"
            ],
            "selected_predicted_PL_corrected_residual_l2_norm": float(
                np.linalg.norm(predicted_residual)
            ),
            "selected_actual_reduction_factor_from_base": float(
                np.linalg.norm(actual_residual) / np.linalg.norm(base_residual)
            ),
            "selected_model_error_l2_norm": float(
                np.linalg.norm(actual_residual - predicted_residual)
            ),
            "selected_radial_wall_signed_coordinate": radial_wall[
                "signed_transverse_coordinate"
            ],
            "elapsed_seconds": time.perf_counter() - started,
        },
        "authority": {
            "base_trial": relative(BASE_TRIAL),
            "base_trial_sha256": sha256(BASE_TRIAL),
            "A212": relative(A212),
            "A212_sha256": sha256(A212),
            "proposal": relative(PROPOSAL),
            "proposal_sha256": sha256(PROPOSAL),
            "probe_engine_source": relative(Path(probe.__file__).resolve()),
            "probe_engine_source_sha256": sha256(Path(probe.__file__).resolve()),
            "runner_source": relative(Path(__file__)),
            "runner_source_sha256": sha256(Path(__file__)),
        },
        "strict_scope": {
            "same_source_nonlinear_trial": True,
            "PL_corrected_candidate_periods": True,
            "same_fixed_handle_chamber": True,
            "same_post_selected_039_selected_038_radial_chamber": True,
            "sampled_three_wall_preflight_passed": True,
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
