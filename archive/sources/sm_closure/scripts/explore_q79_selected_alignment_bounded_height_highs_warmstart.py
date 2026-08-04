from __future__ import annotations

import argparse
import json
import math
from pathlib import Path

import highspy
import numpy as np

import explore_q79_selected_alignment_bounded_height_milp as base
from build_selected_q79_effective_integral_branch_quotient import (
    BETA,
    INTEGRAL_BASIS,
    PERIODS,
    complex_value,
)
from explore_q79_a126_integral_period_branch_lll import realification


ROOT = base.ROOT
PERIOD_DIRECTORY = base.PERIOD_DIRECTORY
A208 = base.A208
DEFAULT_OUTPUT = PERIOD_DIRECTORY / (
    "selected_alignment_height4_bounded_highs_warmstart.exploratory.json"
)


def finite_or_none(value: float) -> float | None:
    return float(value) if math.isfinite(float(value)) else None


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--output", type=Path, default=DEFAULT_OUTPUT)
    parser.add_argument("--coefficient-bound", type=int, default=4)
    parser.add_argument("--time-limit", type=float, default=900.0)
    parser.add_argument("--mip-rel-gap", type=float, default=1.0e-8)
    parser.add_argument("--threads", type=int, default=2)
    arguments = parser.parse_args()
    if arguments.coefficient_bound != 4:
        raise ValueError("the current A208 warm start has effective height four")

    period_packet = base.load(PERIODS)
    beta_packet = base.load(BETA)
    basis_packet = base.load(INTEGRAL_BASIS)
    a208 = base.load(A208)
    period_matrix = np.asarray(
        [
            [complex_value(value) for value in row]
            for row in period_packet["period_matrix_rows"]
        ],
        dtype=np.complex128,
    )
    beta = np.asarray(
        [complex_value(value) for value in beta_packet["tight_endpoint"]["beta_center"]],
        dtype=np.complex128,
    )
    if period_matrix.shape != (8, 92) or beta.shape != (8,):
        raise AssertionError("selected period/beta dimensions changed")
    active = period_matrix[:, :90]
    real_matrix = np.vstack([active.real, active.imag])
    real_beta = realification(beta)

    warm_rows = []
    for row in a208["height_four_candidates"]:
        ell = np.asarray(row["effective_coordinates_Z90"], dtype=np.int64)
        residual = beta - active @ ell
        warm_rows.append(
            {
                "row": row,
                "ell": ell,
                "residual": residual,
                "t": float(
                    np.max(np.abs(np.concatenate([residual.real, residual.imag])))
                ),
            }
        )
    warm = min(warm_rows, key=lambda item: item["t"])
    warm_t = warm["t"]

    highs = highspy.Highs()
    highs.setOptionValue("output_flag", False)
    highs.setOptionValue("time_limit", arguments.time_limit)
    highs.setOptionValue("mip_rel_gap", arguments.mip_rel_gap)
    highs.setOptionValue("threads", arguments.threads)
    highs.setOptionValue("random_seed", 0)
    integers = highs.addVariables(
        90,
        lb=-arguments.coefficient_bound,
        ub=arguments.coefficient_bound,
        type=highspy.HighsVarType.kInteger,
        name_prefix="m",
        out_array=True,
    )
    t_variable = highs.addVariable(
        lb=0.0,
        ub=math.nextafter(warm_t, math.inf),
        obj=1.0,
        name="t",
    )
    for index in range(16):
        expression = highs.qsum(
            real_matrix[index, column] * integers[column]
            for column in range(90)
        ) - real_beta[index]
        highs.addConstr(expression <= t_variable, name=f"upper_{index}")
        highs.addConstr(expression >= -t_variable, name=f"lower_{index}")

    warm_values = np.concatenate([warm["ell"].astype(np.float64), [warm_t]])
    warm_status = highs.setSolution(
        91,
        np.arange(91, dtype=np.int32),
        warm_values,
    )
    run_status = highs.run()
    model_status = highs.getModelStatus()
    model_status_text = highs.modelStatusToString(model_status)
    info = highs.getInfo()
    solution = highs.getSolution()
    incumbent = None
    if solution.value_valid and len(solution.col_value) == 91:
        ell = np.rint(np.asarray(solution.col_value[:90])).astype(np.int64)
        residual = beta - active @ ell
        coordinates = [int(value) for value in ell]
        candidate_id = base.vector_id(coordinates)
        a208_by_id = {
            row["candidate_id"]: int(row["A132_objective_rank"])
            for row in a208["height_four_candidates"]
        }
        primitive_basis = np.asarray(
            basis_packet["primary_basis"]["basis_columns"], dtype=object
        )
        primitive = primitive_basis @ np.asarray(ell, dtype=object)
        incumbent = {
            "candidate_id": candidate_id,
            "matches_A208_height_four_row": candidate_id in a208_by_id,
            "A208_objective_rank_if_matched": a208_by_id.get(candidate_id),
            "improves_warm_start": float(info.objective_function_value) < warm_t,
            "effective_coordinates_Z90": coordinates,
            "coefficient_height": int(np.max(np.abs(ell))),
            "coefficient_l1_norm": int(np.sum(np.abs(ell))),
            "support_size": int(np.count_nonzero(ell)),
            "primitive_thimble_support": int(
                np.count_nonzero(np.asarray(primitive[:90], dtype=object))
            ),
            "primitive_handle_coordinates": [int(value) for value in primitive[90:]],
            "residual_rows": [base.complex_pair(value) for value in residual],
            "residual_maximum_coordinate_absolute_value": float(
                np.max(np.abs(np.concatenate([residual.real, residual.imag])))
            ),
            "residual_maximum_complex_absolute_value": float(np.max(np.abs(residual))),
            "residual_l2_norm": float(np.linalg.norm(residual)),
            "solver_objective": float(info.objective_function_value),
        }

    packet = {
        "schema": "MTTQ79SelectedAlignmentBoundedHeightHighsWarmStartExploration.v1",
        "status": (
            "BOUNDED_FLOATING_HIGHS_OPTIMUM_CERTIFIED"
            if model_status == highspy.HighsModelStatus.kOptimal
            else "BOUNDED_FLOATING_HIGHS_WARM_STARTED_SEARCH_INCOMPLETE"
        ),
        "authority": {
            "period_table": base.relative(PERIODS),
            "period_table_sha256": base.sha256(PERIODS),
            "beta_packet": base.relative(BETA),
            "beta_packet_sha256": base.sha256(BETA),
            "integral_basis": base.relative(INTEGRAL_BASIS),
            "integral_basis_sha256": base.sha256(INTEGRAL_BASIS),
            "A208_queue": base.relative(A208),
            "A208_queue_sha256": base.sha256(A208),
            "source": base.relative(Path(__file__)),
            "source_sha256": base.sha256(Path(__file__)),
        },
        "problem": {
            "real_shape": [16, 90],
            "integer_coordinate_bound": arguments.coefficient_bound,
            "objective": "minimize t subject to |Pi*m-beta|_infinity <= t",
            "objective_upper_cutoff": math.nextafter(warm_t, math.inf),
        },
        "warm_start": {
            "set_solution_status": str(warm_status),
            "candidate_id": warm["row"]["candidate_id"],
            "A132_objective_rank": warm["row"]["A132_objective_rank"],
            "component_infinity_residual": warm_t,
            "complex_infinity_residual": float(np.max(np.abs(warm["residual"]))),
        },
        "solver": {
            "name": "highspy HiGHS",
            "version": highspy.HIGHS_VERSION_MAJOR
            + highspy.HIGHS_VERSION_MINOR / 100
            + highspy.HIGHS_VERSION_PATCH / 10000,
            "run_status": str(run_status),
            "model_status": str(model_status),
            "model_status_text": model_status_text,
            "time_limit_seconds": arguments.time_limit,
            "threads": arguments.threads,
            "objective": finite_or_none(info.objective_function_value),
            "mip_node_count": int(info.mip_node_count),
            "mip_dual_bound": finite_or_none(info.mip_dual_bound),
            "mip_gap": finite_or_none(info.mip_gap),
        },
        "incumbent": incumbent,
        "strict_scope": {
            "observed_SM_values_used": False,
            "same_selected_carrier": True,
            "bounded_all_90_effective_coordinates": True,
            "known_A208_incumbent_injected": True,
            "floating_period_centers_only": True,
            "interval_membership_or_nonmembership_proved": False,
            "covariant_PGL3_zero_or_no_go_proved": False,
            "global_Z90_search_proved": False,
            "optimal_status_would_only_prove_the_floating_bounded_problem": True,
        },
    }
    output = arguments.output
    if not output.is_absolute():
        output = ROOT / output
    output.parent.mkdir(parents=True, exist_ok=True)
    output.write_text(json.dumps(packet, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    print(f"wrote {base.relative(output)}")
    print(
        json.dumps(
            {
                "model_status": model_status_text,
                "warm_t": warm_t,
                "objective": packet["solver"]["objective"],
                "mip_dual_bound": packet["solver"]["mip_dual_bound"],
                "mip_gap": packet["solver"]["mip_gap"],
                "incumbent_id": None if incumbent is None else incumbent["candidate_id"],
                "improves_warm_start": (
                    None if incumbent is None else incumbent["improves_warm_start"]
                ),
            },
            indent=2,
        )
    )
    return 0 if incumbent is not None else 1


if __name__ == "__main__":
    raise SystemExit(main())
