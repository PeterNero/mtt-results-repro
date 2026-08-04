from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path

import numpy as np
from scipy.optimize import Bounds, LinearConstraint, milp

from build_selected_q79_effective_integral_branch_quotient import (
    BETA,
    INTEGRAL_BASIS,
    PERIODS,
    complex_value,
)
from explore_q79_a126_integral_period_branch_lll import realification


ROOT = Path(__file__).resolve().parents[1]
PERIOD_DIRECTORY = (
    ROOT
    / "candidate_data"
    / "selected_q79covariantperiodbranchcutsetandtightbetatransport"
    / "selected_alignment_thimble_periods"
)
A208 = PERIOD_DIRECTORY / "selected_alignment_height4_survivor_queue_and_E32_priority.packet.json"
DEFAULT_OUTPUT = PERIOD_DIRECTORY / "selected_alignment_height4_bounded_milp.exploratory.json"


def load(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def relative(path: Path) -> str:
    return str(path.relative_to(ROOT)).replace("\\", "/")


def vector_id(values: list[int]) -> str:
    canonical = json.dumps(values, separators=(",", ":")).encode("ascii")
    return hashlib.sha256(canonical).hexdigest()[:16]


def complex_pair(value: complex) -> dict[str, str]:
    return {
        "real": format(float(value.real), ".17g"),
        "imaginary": format(float(value.imag), ".17g"),
    }


def optional_float(result, name: str) -> float | None:
    value = getattr(result, name, None)
    return None if value is None else float(value)


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--output", type=Path, default=DEFAULT_OUTPUT)
    parser.add_argument("--coefficient-bound", type=int, default=4)
    parser.add_argument("--time-limit", type=float, default=600.0)
    parser.add_argument("--mip-rel-gap", type=float, default=1.0e-8)
    arguments = parser.parse_args()
    if arguments.coefficient_bound < 1:
        raise ValueError("coefficient bound must be positive")
    if arguments.time_limit <= 0:
        raise ValueError("time limit must be positive")

    period_packet = load(PERIODS)
    beta_packet = load(BETA)
    basis_packet = load(INTEGRAL_BASIS)
    a208 = load(A208)
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
    if np.any(period_matrix[:, 90:] != 0.0):
        raise AssertionError("selected Leray-null columns changed")
    active = period_matrix[:, :90]
    real_matrix = np.vstack([active.real, active.imag])
    real_beta = realification(beta)
    variable_count = 91
    t_index = 90
    objective = np.zeros(variable_count, dtype=np.float64)
    objective[t_index] = 1.0
    integrality = np.zeros(variable_count, dtype=np.int8)
    integrality[:90] = 1
    lower = np.concatenate(
        [
            np.full(90, -arguments.coefficient_bound, dtype=np.float64),
            [0.0],
        ]
    )
    upper = np.concatenate(
        [
            np.full(90, arguments.coefficient_bound, dtype=np.float64),
            [np.inf],
        ]
    )
    positive = np.zeros((16, variable_count), dtype=np.float64)
    positive[:, :90] = real_matrix
    positive[:, t_index] = -1.0
    negative = np.zeros((16, variable_count), dtype=np.float64)
    negative[:, :90] = -real_matrix
    negative[:, t_index] = -1.0
    constraint_matrix = np.vstack([positive, negative])
    constraint_upper = np.concatenate([real_beta, -real_beta])

    result = milp(
        objective,
        integrality=integrality,
        bounds=Bounds(lower, upper),
        constraints=LinearConstraint(
            constraint_matrix,
            np.full(32, -np.inf),
            constraint_upper,
        ),
        options={
            "time_limit": arguments.time_limit,
            "mip_rel_gap": arguments.mip_rel_gap,
            "presolve": True,
        },
    )
    incumbent = None
    if result.x is not None:
        ell = np.rint(result.x[:90]).astype(np.int64)
        residual = beta - active @ ell
        primitive_basis = np.asarray(
            basis_packet["primary_basis"]["basis_columns"], dtype=object
        )
        if primitive_basis.shape != (98, 90):
            raise AssertionError("selected primary basis shape changed")
        primitive = primitive_basis @ np.asarray(ell, dtype=object)
        coordinates = [int(value) for value in ell]
        candidate_id = vector_id(coordinates)
        a208_by_id = {
            row["candidate_id"]: int(row["A132_objective_rank"])
            for row in a208["height_four_candidates"]
        }
        incumbent = {
            "candidate_id": candidate_id,
            "matches_A208_height_four_row": candidate_id in a208_by_id,
            "A208_objective_rank_if_matched": a208_by_id.get(candidate_id),
            "effective_coordinates_Z90": coordinates,
            "coefficient_height": int(np.max(np.abs(ell))),
            "coefficient_l1_norm": int(np.sum(np.abs(ell))),
            "support_size": int(np.count_nonzero(ell)),
            "primitive_thimble_support": int(
                np.count_nonzero(np.asarray(primitive[:90], dtype=object))
            ),
            "primitive_handle_coordinates": [int(value) for value in primitive[90:]],
            "residual_rows": [complex_pair(value) for value in residual],
            "residual_maximum_coordinate_absolute_value": float(
                np.max(np.abs(np.concatenate([residual.real, residual.imag])))
            ),
            "residual_maximum_complex_absolute_value": float(np.max(np.abs(residual))),
            "residual_l2_norm": float(np.linalg.norm(residual)),
            "solver_t": float(result.x[t_index]),
        }

    packet = {
        "schema": "MTTQ79SelectedAlignmentBoundedHeightMILPExploration.v1",
        "status": (
            "BOUNDED_FLOATING_MILP_OPTIMUM_CERTIFIED"
            if result.success and optional_float(result, "mip_gap") == 0.0
            else "BOUNDED_FLOATING_MILP_TIMED_OR_GAPPED_INCUMBENT"
        ),
        "authority": {
            "period_table": relative(PERIODS),
            "period_table_sha256": sha256(PERIODS),
            "beta_packet": relative(BETA),
            "beta_packet_sha256": sha256(BETA),
            "integral_basis": relative(INTEGRAL_BASIS),
            "integral_basis_sha256": sha256(INTEGRAL_BASIS),
            "A208_queue": relative(A208),
            "A208_queue_sha256": sha256(A208),
            "source": relative(Path(__file__)),
            "source_sha256": sha256(Path(__file__)),
        },
        "problem": {
            "real_shape": [16, 90],
            "integer_coordinate_bound": arguments.coefficient_bound,
            "objective": "minimize t subject to |Pi*m-beta|_infinity <= t",
            "height_definition": "maximum absolute effective Z90 coefficient",
        },
        "solver": {
            "name": "SciPy HiGHS MILP",
            "success": bool(result.success),
            "status": int(result.status),
            "message": result.message,
            "time_limit_seconds": arguments.time_limit,
            "requested_mip_relative_gap": arguments.mip_rel_gap,
            "objective": None if result.fun is None else float(result.fun),
            "mip_node_count": optional_float(result, "mip_node_count"),
            "mip_dual_bound": optional_float(result, "mip_dual_bound"),
            "mip_gap": optional_float(result, "mip_gap"),
        },
        "incumbent": incumbent,
        "strict_scope": {
            "observed_SM_values_used": False,
            "same_selected_carrier": True,
            "bounded_all_90_effective_coordinates": True,
            "floating_period_centers_only": True,
            "interval_membership_or_nonmembership_proved": False,
            "covariant_PGL3_zero_or_no_go_proved": False,
            "global_Z90_search_proved": False,
            "zero_MIP_gap_would_only_prove_the_floating_bounded_problem": True,
        },
    }
    output = arguments.output
    if not output.is_absolute():
        output = ROOT / output
    output.parent.mkdir(parents=True, exist_ok=True)
    output.write_text(json.dumps(packet, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    print(f"wrote {relative(output)}")
    print(
        json.dumps(
            {
                "success": packet["solver"]["success"],
                "status": packet["solver"]["status"],
                "mip_gap": packet["solver"]["mip_gap"],
                "incumbent": incumbent,
            },
            indent=2,
        )
    )
    return 0 if incumbent is not None else 1


if __name__ == "__main__":
    raise SystemExit(main())
