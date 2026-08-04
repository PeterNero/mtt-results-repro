from __future__ import annotations

import argparse
import hashlib
import json
import time
from pathlib import Path

import numpy as np
from scipy.integrate import solve_ivp

from q79genus2_period_transport import (
    FORM_NAMES,
    Q79GenusTwoGaussManin,
    initial_vanishing_periods,
)
from q79genus2_root_transport import Q79GenusTwoRootTransport, midpoint


ROOT = Path(__file__).resolve().parents[1]
FIBRATION = (
    ROOT
    / "candidate_data"
    / "selected_q79genus2lefschetzperiodreduction"
    / "explicit_genus2_fibration.packet.json"
)
EXPLORATION = (
    ROOT
    / "candidate_data"
    / "selected_q79genus2picardlefschetzmonodromyexecution"
    / "numerical_monodromy_exploration.packet.json"
)
FACTORIZATION = (
    ROOT
    / "candidate_data"
    / "selected_q79genus2distinguishedcutsystemandglobalrelation"
    / "global_integral_gauss_manin_factorization.packet.json"
)
PROMOTED_HANDLES = (
    ROOT
    / "candidate_data"
    / "selected_q79genus2handlemonodromypromotion"
    / "two_promoted_torus_handle_monodromies.packet.json"
)
HANDLE_EXPLORATION = (
    ROOT
    / "candidate_data"
    / "selected_q79genus2handlemonodromycandidate"
    / "handle_monodromy_exploration.packet.json"
)
OUTPUT_DIR = (
    ROOT / "candidate_data" / "selected_q79genus2handleandlerayperiodexecution"
)
DEFAULT_OUTPUT = OUTPUT_DIR / "primitive_handle_periods.production.packet.json"
OMITTED = 2 + 3j
CHAIN_SIGNS = (1, -1, -1, -1, 1)
EXPECTED_CENTRAL_LIFTS = {"A": 1, "B": -1}


def load(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def dump(path: Path, payload: dict) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(
        json.dumps(payload, indent=2, sort_keys=True) + "\n",
        encoding="utf-8",
    )


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def complex_pair(value: complex) -> dict[str, str]:
    return {
        "real": format(value.real, ".17g"),
        "imaginary": format(value.imag, ".17g"),
    }


def complex_matrix(matrix: np.ndarray) -> list[list[dict[str, str]]]:
    return [
        [complex_pair(complex(matrix[row, column])) for column in range(matrix.shape[1])]
        for row in range(matrix.shape[0])
    ]


def marked_base_periods(
    homology: dict, *, inner_order: int, dps: int
) -> tuple[np.ndarray, dict]:
    transport = Q79GenusTwoRootTransport(
        FIBRATION,
        homology,
        omitted=OMITTED,
        dps=dps,
    )
    a_ball, b_ball = transport.ab_at(transport.base)
    leading = midpoint(
        transport.coefficient_at(
            transport.coefficient_terms[0], a_ball, b_ball
        )
    )
    direct = []
    clearances = []
    for index in range(5):
        periods, clearance = initial_vanishing_periods(
            transport.base_roots,
            (index, index + 1),
            leading,
            OMITTED,
            inner_order,
            "t",
        )
        direct.append(periods)
        clearances.append(clearance)
    signed = np.asarray(
        [sign * periods for sign, periods in zip(CHAIN_SIGNS, direct)],
        dtype=np.complex128,
    ).T
    basis = np.column_stack(
        [
            signed[:, 0],
            signed[:, 1],
            signed[:, 0] + signed[:, 2],
            signed[:, 3],
        ]
    )
    holomorphic = basis[:2, :]
    a_periods = holomorphic[:, [0, 2]]
    b_periods = holomorphic[:, [1, 3]]
    riemann = np.linalg.solve(a_periods, b_periods)
    relation = signed[:2, 0] + signed[:2, 2] + signed[:2, 4]
    relation_scaled = float(
        np.linalg.norm(relation)
        / max(np.linalg.norm(signed[:2, :]), np.finfo(float).tiny)
    )
    symmetry_error = float(np.max(np.abs(riemann - riemann.T)))
    imaginary_eigenvalues = np.linalg.eigvalsh(riemann.imag)
    if relation_scaled >= 1.0e-10:
        raise AssertionError("marked chain relation failed")
    if symmetry_error >= 1.0e-10:
        raise AssertionError("Riemann matrix is not symmetric")
    if float(np.min(imaginary_eigenvalues)) <= 0:
        raise AssertionError("Riemann matrix imaginary part is not positive")
    return basis, {
        "basis": ["a1", "b1", "a2", "b2"],
        "adjacent_chain_signs": list(CHAIN_SIGNS),
        "chain_vector_identification": [
            "c1=a1",
            "c2=b1",
            "c3=-a1+a2",
            "c4=b2",
            "c5=-a2",
        ],
        "holomorphic_chain_relation_scaled_residual": format(
            relation_scaled, ".17g"
        ),
        "minimum_direct_chord_clearance": format(
            min(clearances), ".17g"
        ),
        "base_holomorphic_period_matrix": complex_matrix(holomorphic),
        "normalized_Riemann_matrix": complex_matrix(riemann),
        "Riemann_symmetry_error": format(symmetry_error, ".17g"),
        "Riemann_imaginary_eigenvalues": [
            format(float(value), ".17g") for value in imaginary_eigenvalues
        ],
    }


def execute_handle(
    name: str,
    displacement: complex,
    action: np.ndarray,
    initial_periods: np.ndarray,
    homology: dict,
    *,
    dps: int,
    rtol: float,
    atol: float,
) -> tuple[np.ndarray, dict]:
    transport = Q79GenusTwoRootTransport(
        FIBRATION,
        homology,
        omitted=OMITTED,
        dps=dps,
    )
    gauss_manin = Q79GenusTwoGaussManin(
        FIBRATION,
        transport,
        coordinate="t",
        omitted=OMITTED,
    )
    initial_state = np.concatenate(
        [
            initial_periods.reshape(-1),
            np.zeros((8, 4), dtype=np.complex128).reshape(-1),
        ]
    )

    def differential(parameter: float, state: np.ndarray) -> np.ndarray:
        periods = state[:20].reshape(5, 4)
        w_value = transport.base + parameter * displacement
        connection, a_value, b_value = gauss_manin.connection(w_value)
        period_derivative = displacement * connection @ periods
        integral_derivative = np.column_stack(
            [
                gauss_manin.period_length
                * displacement
                * gauss_manin.residue_rows(
                    periods[:, column], a_value, b_value
                )
                for column in range(4)
            ]
        )
        return np.concatenate(
            [period_derivative.reshape(-1), integral_derivative.reshape(-1)]
        )

    solution = solve_ivp(
        differential,
        (0.0, 1.0),
        initial_state,
        method="DOP853",
        rtol=rtol,
        atol=atol,
    )
    if not solution.success:
        raise AssertionError(solution.message)
    endpoint_periods = solution.y[:20, -1].reshape(5, 4)
    handle_integrals = solution.y[20:, -1].reshape(8, 4)
    initial_holomorphic = initial_periods[:2, :]
    endpoint_holomorphic = endpoint_periods[:2, :]
    predicted = initial_holomorphic @ action
    positive_error = float(
        np.linalg.norm(endpoint_holomorphic - predicted)
        / max(np.linalg.norm(endpoint_holomorphic), np.linalg.norm(predicted))
    )
    negative_error = float(
        np.linalg.norm(endpoint_holomorphic + predicted)
        / max(np.linalg.norm(endpoint_holomorphic), np.linalg.norm(predicted))
    )
    central_lift = 1 if positive_error <= negative_error else -1
    selected_error = min(positive_error, negative_error)
    if central_lift != EXPECTED_CENTRAL_LIFTS[name]:
        raise AssertionError(f"unexpected {name} central lift")
    if selected_error >= 5.0e-7:
        raise AssertionError(f"{name} endpoint monodromy residual")
    return handle_integrals, {
        "name": name,
        "base_path": (
            "w(s)=(1+i)/4+s"
            if name == "A"
            else "w(s)=(1+i)/4+i*s"
        ),
        "primitive_fiber_cycle_order": ["a1", "b1", "a2", "b2"],
        "period_values": complex_matrix(handle_integrals),
        "endpoint_holomorphic_periods": complex_matrix(endpoint_holomorphic),
        "promoted_braid_action": action.astype(int).tolist(),
        "period_selected_central_lift": central_lift,
        "period_selected_action": (central_lift * action).astype(int).tolist(),
        "positive_lift_scaled_residual": format(positive_error, ".17g"),
        "negative_lift_scaled_residual": format(negative_error, ".17g"),
        "selected_lift_scaled_residual": format(selected_error, ".17g"),
        "numerics": {
            "working_decimal_digits": dps,
            "ODE_method": "DOP853",
            "ODE_rtol": format(rtol, ".17g"),
            "ODE_atol": format(atol, ".17g"),
            "ODE_function_evaluations": solution.nfev,
            "Gauss_Manin_coordinate": "t",
            "Gauss_Manin_connection_evaluations": gauss_manin.connection_evaluation_count,
            "high_precision_Gauss_Manin_connection_evaluations": gauss_manin.high_precision_connection_evaluation_count,
            "maximum_reduction_condition_number": format(
                gauss_manin.maximum_reduction_condition_number, ".17g"
            ),
            "maximum_equilibrated_reduction_condition_number": format(
                gauss_manin.maximum_equilibrated_reduction_condition_number,
                ".17g",
            ),
            "maximum_reduction_relative_residual": format(
                gauss_manin.maximum_reduction_relative_residual, ".17g"
            ),
        },
    }


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser()
    parser.add_argument("--inner-order", type=int, default=384)
    parser.add_argument("--dps", type=int, default=90)
    parser.add_argument("--rtol", type=float, default=2.0e-10)
    parser.add_argument("--atol", type=float, default=2.0e-13)
    parser.add_argument("--output", type=Path, default=DEFAULT_OUTPUT)
    parser.add_argument("--no-save", action="store_true")
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    started = time.perf_counter()
    exploration = load(EXPLORATION)
    factorization = load(FACTORIZATION)
    handle_exploration = load(HANDLE_EXPLORATION)
    homology = exploration["homology_convention"]
    initial_periods, marking = marked_base_periods(
        homology,
        inner_order=args.inner_order,
        dps=args.dps,
    )
    actions = {
        name: np.asarray(
            factorization["handle_actions"][name], dtype=np.int64
        )
        for name in ("A", "B")
    }
    handle_rows = []
    handle_blocks = []
    for name, displacement in (("A", 1 + 0j), ("B", 1j)):
        block, row = execute_handle(
            name,
            displacement,
            actions[name],
            initial_periods,
            homology,
            dps=args.dps,
            rtol=args.rtol,
            atol=args.atol,
        )
        handle_blocks.append(block)
        handle_rows.append(row)
    primitive = np.hstack(handle_blocks)
    trajectory_hashes = {
        row["name"]: row["trajectory"]["sha256"]
        for row in handle_exploration["handles"]
    }
    payload = {
        "schema": "MTTQ79PrimitiveHandlePeriodExecution.v1",
        "status": "EIGHT_PRIMITIVE_HANDLE_CYLINDER_PERIODS_EXECUTED_CENTRAL_LIFT_SELECTED",
        "authority": {
            "fibration_sha256": sha256(FIBRATION),
            "numerical_monodromy_exploration_sha256": sha256(EXPLORATION),
            "global_factorization_sha256": sha256(FACTORIZATION),
            "promoted_handles_sha256": sha256(PROMOTED_HANDLES),
            "handle_exploration_sha256": sha256(HANDLE_EXPLORATION),
            "handle_trajectory_sha256": trajectory_hashes,
            "period_engine_sha256": sha256(
                ROOT / "scripts" / "q79genus2_period_transport.py"
            ),
            "runner_sha256": sha256(Path(__file__).resolve()),
        },
        "marking": marking,
        "forms": FORM_NAMES,
        "primitive_column_order": [
            "A:a1",
            "A:b1",
            "A:a2",
            "A:b2",
            "B:a1",
            "B:b1",
            "B:a2",
            "B:b2",
        ],
        "primitive_handle_period_matrix": complex_matrix(primitive),
        "handles": handle_rows,
        "central_lift_result": {
            "A": 1,
            "B": -1,
            "interpretation": "The root braid fixes the Sp(4,Z) action only up to the central hyperelliptic deck lift. Independent holomorphic period continuation selects +M_A and -M_B in the frozen marking.",
            "commutator_unchanged": True,
        },
        "execution": {
            "inner_Gauss_Legendre_order": args.inner_order,
            "working_decimal_digits": args.dps,
            "ODE_rtol": format(args.rtol, ".17g"),
            "ODE_atol": format(args.atol, ".17g"),
            "elapsed_seconds": format(time.perf_counter() - started, ".17g"),
        },
        "strict_scope": {
            "primitive_handle_cylinders_executed": 8,
            "closed_integral_H2_basis_assembled": False,
            "floating_convergence_only": True,
            "interval_enclosure": False,
        },
    }
    if not args.no_save:
        output = args.output
        if not output.is_absolute():
            output = ROOT / output
        dump(output, payload)
        print(f"wrote {output}")
    print(json.dumps(payload, indent=2, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
