from __future__ import annotations

import argparse
import json
from pathlib import Path

import numpy as np
from scipy.optimize import Bounds, LinearConstraint, milp


ROOT = Path(__file__).resolve().parents[1]
PERIODS = (
    ROOT
    / "candidate_data"
    / "selected_q79genus2handleandlerayperiodexecution"
    / "full_integral_basis_period_table.packet.json"
)
BETA = (
    ROOT
    / "candidate_data"
    / "selected_q79genus2delignebetaperiodandintegralbranchexecution"
    / "selected_beta_period_vector.floating.packet.json"
)


def load(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def complex_value(value: dict) -> complex:
    return complex(float(value["real"]), float(value["imaginary"]))


def complex_pair(value: complex) -> dict[str, str]:
    return {
        "real": format(float(value.real), ".17g"),
        "imaginary": format(float(value.imag), ".17g"),
    }


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--output", type=Path, required=True)
    parser.add_argument("--coefficient-bound", type=int, default=1)
    parser.add_argument("--time-limit", type=float, default=180.0)
    parser.add_argument("--sparsity-weight", type=float, default=1.0e-10)
    arguments = parser.parse_args()
    if arguments.coefficient_bound < 1:
        raise ValueError("coefficient bound must be positive")

    period_packet = load(PERIODS)
    beta_packet = load(BETA)
    period_matrix = np.asarray(
        [
            [complex_value(value) for value in row]
            for row in period_packet["period_rows"]
        ],
        dtype=np.complex128,
    )
    beta = np.asarray(
        [complex_value(value) for value in beta_packet["production_values"]],
        dtype=np.complex128,
    )
    if period_matrix.shape != (8, 92) or beta.shape != (8,):
        raise AssertionError("unexpected A119/A121 period dimensions")

    real_matrix = np.vstack([period_matrix.real, period_matrix.imag])
    real_beta = np.concatenate([beta.real, beta.imag])
    singular_values = np.linalg.svd(real_matrix, compute_uv=False)
    rank = int(np.linalg.matrix_rank(real_matrix))
    nonzero = np.max(abs(real_matrix), axis=0) > 1.0e-14
    active_indices = np.flatnonzero(nonzero)
    zero_indices = np.flatnonzero(~nonzero)
    active = real_matrix[:, active_indices]
    count = active.shape[1]

    # With a positive sparsity weight, variables are
    # (ell_1,...,ell_n, |ell_1|,...,|ell_n|, t).  The pure residual search
    # omits the 90 auxiliary magnitudes entirely.
    use_sparsity = arguments.sparsity_weight > 0.0
    variable_count = (2 * count + 1) if use_sparsity else (count + 1)
    t_index = variable_count - 1
    objective = np.zeros(variable_count, dtype=np.float64)
    if use_sparsity:
        objective[count : 2 * count] = arguments.sparsity_weight
    objective[t_index] = 1.0
    integrality = np.zeros(variable_count, dtype=np.int8)
    integrality[:count] = 1
    if use_sparsity:
        lower = np.concatenate(
            [
                np.full(
                    count, -arguments.coefficient_bound, dtype=np.float64
                ),
                np.zeros(count + 1, dtype=np.float64),
            ]
        )
        upper = np.concatenate(
            [
                np.full(
                    count, arguments.coefficient_bound, dtype=np.float64
                ),
                np.full(
                    count, arguments.coefficient_bound, dtype=np.float64
                ),
                [np.inf],
            ]
        )
    else:
        lower = np.concatenate(
            [
                np.full(
                    count, -arguments.coefficient_bound, dtype=np.float64
                ),
                [0.0],
            ]
        )
        upper = np.concatenate(
            [
                np.full(
                    count, arguments.coefficient_bound, dtype=np.float64
                ),
                [np.inf],
            ]
        )

    residual_positive = np.zeros((16, variable_count), dtype=np.float64)
    residual_positive[:, :count] = active
    residual_positive[:, t_index] = -1.0
    residual_negative = np.zeros((16, variable_count), dtype=np.float64)
    residual_negative[:, :count] = -active
    residual_negative[:, t_index] = -1.0
    constraint_blocks = [residual_positive, residual_negative]
    constraint_upper_blocks = [real_beta, -real_beta]
    if use_sparsity:
        absolute_positive = np.zeros(
            (count, variable_count), dtype=np.float64
        )
        absolute_positive[:, :count] = np.eye(count)
        absolute_positive[:, count : 2 * count] = -np.eye(count)
        absolute_negative = np.zeros(
            (count, variable_count), dtype=np.float64
        )
        absolute_negative[:, :count] = -np.eye(count)
        absolute_negative[:, count : 2 * count] = -np.eye(count)
        constraint_blocks.extend([absolute_positive, absolute_negative])
        constraint_upper_blocks.append(np.zeros(2 * count, dtype=np.float64))
    constraint_matrix = np.vstack(constraint_blocks)
    constraint_upper = np.concatenate(constraint_upper_blocks)
    result = milp(
        objective,
        integrality=integrality,
        bounds=Bounds(lower, upper),
        constraints=LinearConstraint(
            constraint_matrix,
            np.full(len(constraint_upper), -np.inf),
            constraint_upper,
        ),
        options={
            "time_limit": arguments.time_limit,
            "mip_rel_gap": 1.0e-9,
            "presolve": True,
        },
    )
    if result.x is None:
        raise AssertionError(f"bounded branch search found no incumbent: {result.message}")
    active_ell = np.rint(result.x[:count]).astype(np.int64)
    ell = np.zeros(92, dtype=np.int64)
    ell[active_indices] = active_ell
    residual = beta - period_matrix @ ell
    support = [
        {
            "index_zero_based": int(index),
            "column": period_packet["column_order"][index],
            "coefficient": int(ell[index]),
        }
        for index in np.flatnonzero(ell)
    ]
    packet = {
        "schema": "MTTQ79BoundedIntegralBetaBranchSearch.v1",
        "status": "EXPLORATORY_BOUNDED_INTEGER_BRANCH_CANDIDATE",
        "inputs": {
            "period_table": str(PERIODS.relative_to(ROOT)).replace("\\", "/"),
            "beta_vector": str(BETA.relative_to(ROOT)).replace("\\", "/"),
        },
        "real_period_system": {
            "shape": [16, 92],
            "rank": rank,
            "singular_values": [float(value) for value in singular_values],
            "active_columns": int(count),
            "exact_zero_columns_zero_based": [
                int(value) for value in zero_indices
            ],
        },
        "search": {
            "method": "SciPy-HiGHS bounded MILP",
            "coefficient_bound": arguments.coefficient_bound,
            "time_limit_seconds": arguments.time_limit,
            "sparsity_weight": arguments.sparsity_weight,
            "solver_success": bool(result.success),
            "solver_status": int(result.status),
            "solver_message": result.message,
            "objective": float(result.fun),
            "mip_gap": (
                None
                if getattr(result, "mip_gap", None) is None
                else float(result.mip_gap)
            ),
        },
        "candidate": {
            "ell_Z92": [int(value) for value in ell],
            "support_size": len(support),
            "support": support,
            "residual_z_minus_Pi_ell": [
                complex_pair(value) for value in residual
            ],
            "residual_maximum_absolute_value": float(np.max(abs(residual))),
            "residual_l2_norm": float(np.linalg.norm(residual)),
        },
        "strict_scope": {
            "observed_SM_values_used": False,
            "bounded_floating_search_only": True,
            "exact_Z92_membership_proved": False,
            "small_residual_accepted_as_proof": False,
            "candidate_requires_same_branch_PGL3_continuation_and_exact_certificate": True,
        },
    }
    arguments.output.parent.mkdir(parents=True, exist_ok=True)
    arguments.output.write_text(
        json.dumps(packet, indent=2, sort_keys=True) + "\n",
        encoding="utf-8",
    )
    print(
        json.dumps(
            {
                "rank": rank,
                "active_columns": int(count),
                "solver_success": bool(result.success),
                "solver_status": int(result.status),
                "support_size": len(support),
                "residual_maximum_absolute_value": packet["candidate"][
                    "residual_maximum_absolute_value"
                ],
                "residual_l2_norm": packet["candidate"]["residual_l2_norm"],
            },
            indent=2,
        )
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
