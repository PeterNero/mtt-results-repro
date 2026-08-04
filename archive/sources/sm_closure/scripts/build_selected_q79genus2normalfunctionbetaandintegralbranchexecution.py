from __future__ import annotations

import hashlib
import json
from collections import Counter
from pathlib import Path

import numpy as np
import sympy as sp


ROOT = Path(__file__).resolve().parents[1]
COMPUTE_ENGINE = ROOT / "scripts" / "compute_q79genus2normalfunction.py"
OUT = (
    ROOT
    / "candidate_data"
    / "selected_q79genus2normalfunctionbetaandintegralbranchexecution"
)
PRODUCTION = OUT / "normal_function_handles.production.packet.json"
TIGHT = OUT / "normal_function_handles.tight.packet.json"
FACTORIZATION = (
    ROOT
    / "candidate_data"
    / "selected_q79genus2distinguishedcutsystemandglobalrelation"
    / "global_integral_gauss_manin_factorization.packet.json"
)
PERIOD_TABLE = (
    ROOT
    / "candidate_data"
    / "selected_q79genus2handleandlerayperiodexecution"
    / "full_integral_basis_period_table.packet.json"
)
DIRECT_BATCHES = [
    OUT / "meridians_001_010.production.packet.json",
    OUT / "meridians_011_020.production.packet.json",
    OUT / "meridians_021_030.production.packet.json",
    OUT / "meridians_031_040.production.packet.json",
    OUT / "meridian_041.production.packet.json",
    OUT / "meridian_042.production.packet.json",
    OUT / "meridian_044.production.packet.json",
    OUT / "meridians_046_050.production.packet.json",
    OUT / "meridians_051_060.production.packet.json",
    OUT / "meridians_061_070.production.packet.json",
    OUT / "meridians_071_080.production.packet.json",
    OUT / "meridians_081_090.production.packet.json",
]
AFFINE = OUT / "complete_affine_normal_function_cocycle.packet.json"
CONVERGENCE = OUT / "normal_function_floating_convergence.packet.json"
BETA_OPEN = OUT / "beta_period_and_integral_branch.open.json"
FRONTIER = OUT / "U6_frontier_after_A120.packet.json"
CANDIDATE = (
    ROOT
    / "candidate_data"
    / "selected_q79genus2normalfunctionbetaandintegralbranchexecution.candidate.json"
)
CERTIFICATE = (
    ROOT
    / "certificates"
    / "selected_q79genus2normalfunctionbetaandintegralbranchexecution.certificate.json"
)


STATUS = (
    "MTT_U6_Q79_EXACT_MUMFORD_SOURCE_AND_COMPLETE_SELECTED_INTEGRAL_AFFINE_"
    "NORMAL_FUNCTION_COCYCLE_CLOSED_BETA_PERIOD_BRANCH_OPEN"
)
NEXT = "MTT_Selected_q79GenusTwoDeligneBetaPeriodAndIntegralBranchExecution_v1"


def load(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def dump(path: Path, value: dict) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(
        json.dumps(value, indent=2, sort_keys=True) + "\n",
        encoding="utf-8",
    )


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def complex_value(value: dict) -> complex:
    return complex(float(value["real"]), float(value["imaginary"]))


def integer_vector(value: sp.Matrix) -> list[int]:
    return [int(entry) for entry in value]


def affine_compose(
    second: tuple[sp.Matrix, sp.Matrix],
    first: tuple[sp.Matrix, sp.Matrix],
) -> tuple[sp.Matrix, sp.Matrix]:
    matrix_second, translation_second = second
    matrix_first, translation_first = first
    return (
        matrix_second * matrix_first,
        matrix_second * translation_first + translation_second,
    )


def affine_inverse(
    pair: tuple[sp.Matrix, sp.Matrix],
) -> tuple[sp.Matrix, sp.Matrix]:
    matrix, translation = pair
    inverse = matrix.inv()
    return inverse, -inverse * translation


def handle_translation(packet: dict, name: str) -> sp.Matrix:
    row = next(item for item in packet["handles"] if item["name"] == name)
    return sp.Matrix(row["selected_integer_translation"])


def main() -> int:
    production = load(PRODUCTION)
    tight = load(TIGHT)
    factorization = load(FACTORIZATION)
    period_table = load(PERIOD_TABLE)
    if not production["exact_mumford_source"]["all_exact_checks_pass"]:
        raise AssertionError("exact Mumford source did not close")
    if period_table["period_matrix_shape"] != [8, 92]:
        raise AssertionError("A119 period table is not 8x92")

    direct_rows: dict[int, dict] = {}
    for path in DIRECT_BATCHES:
        packet = load(path)
        for row in packet["distinguished_meridians"]:
            index = int(row["distinguished_index"])
            if index in direct_rows:
                raise AssertionError(f"duplicate direct meridian {index}")
            direct_rows[index] = row
    direct_indices = sorted(direct_rows)
    relation_indices = [43, 45]
    if direct_indices != [
        index for index in range(1, 91) if index not in relation_indices
    ]:
        raise AssertionError("direct meridian inventory mismatch")

    factors = factorization["factors"]
    matrix_a = sp.Matrix(factorization["handle_actions"]["A"])
    # A119 selected the central period lifts +A and -B.
    matrix_b = -sp.Matrix(factorization["handle_actions"]["B"])
    translation_a = handle_translation(production, "A")
    translation_b = handle_translation(production, "B")
    handle_a = (matrix_a, translation_a)
    handle_b = (matrix_b, translation_b)
    boundary = affine_compose(
        affine_inverse(handle_b),
        affine_compose(
            affine_inverse(handle_a),
            affine_compose(handle_b, handle_a),
        ),
    )

    x43, x45 = sp.symbols("x43 x45", integer=True)
    symbolic_product = (sp.eye(4), sp.zeros(4, 1))
    for index, factor in enumerate(factors, start=1):
        matrix = sp.Matrix(factor["positive_picard_lefschetz_matrix"])
        vanishing = sp.Matrix(
            factor["positive_vanishing_cycle_up_to_sign"]
        )
        if index == 43:
            multiplier = x43
        elif index == 45:
            multiplier = x45
        else:
            multiplier = direct_rows[index][
                "translation_vanishing_cycle_multiplier"
            ]
            if multiplier is None:
                raise AssertionError(f"non-PL direct translation {index}")
        symbolic_product = affine_compose(
            (matrix, multiplier * vanishing), symbolic_product
        )
    if symbolic_product[0] != boundary[0]:
        raise AssertionError("linear surface relation changed")
    equations = list(symbolic_product[1] - boundary[1])
    solutions = sp.solve(equations, (x43, x45), dict=True)
    if solutions != [{x43: 1, x45: 0}]:
        raise AssertionError(f"unexpected affine relation solution {solutions}")
    selected_multipliers = {43: 1, 45: 0}
    selected_multipliers.update(
        {
            index: int(row["translation_vanishing_cycle_multiplier"])
            for index, row in direct_rows.items()
        }
    )

    exact_product = (sp.eye(4), sp.zeros(4, 1))
    rows: list[dict] = []
    for index, factor in enumerate(factors, start=1):
        matrix = sp.Matrix(factor["positive_picard_lefschetz_matrix"])
        vanishing = sp.Matrix(
            factor["positive_vanishing_cycle_up_to_sign"]
        )
        multiplier = selected_multipliers[index]
        translation = multiplier * vanishing
        exact_product = affine_compose(
            (matrix, translation), exact_product
        )
        row = {
            "distinguished_index": index,
            "root_id": factor["root_id"],
            "positive_vanishing_cycle_up_to_sign": integer_vector(vanishing),
            "translation_multiplier": multiplier,
            "integer_translation": integer_vector(translation),
            "selection_route": (
                "exact_affine_surface_relation"
                if index in relation_indices
                else "direct_inhomogeneous_Gauss_Manin_fit"
            ),
        }
        if index in direct_rows:
            row["direct_fitted_homology_coordinates"] = direct_rows[index][
                "fitted_homology_coordinates"
            ]
            row["direct_period_fit_scaled_residual"] = direct_rows[index][
                "period_fit_scaled_residual"
            ]
        rows.append(row)
    if exact_product != boundary:
        raise AssertionError("affine surface relation did not close exactly")

    c_symbols = sp.Matrix(sp.symbols("c0:4"))
    coboundary_equations: list[sp.Expr] = []
    for row, factor in zip(rows, factors):
        matrix = sp.Matrix(factor["positive_picard_lefschetz_matrix"])
        translation = sp.Matrix(row["integer_translation"])
        coboundary_equations.extend(
            list((matrix - sp.eye(4)) * c_symbols - translation)
        )
    coboundary_equations.extend(
        list((matrix_a - sp.eye(4)) * c_symbols - translation_a)
    )
    coboundary_equations.extend(
        list((matrix_b - sp.eye(4)) * c_symbols - translation_b)
    )
    coboundary_solution = sp.linsolve(
        coboundary_equations, list(c_symbols)
    )
    if coboundary_solution != sp.EmptySet:
        raise AssertionError("normal-function cocycle unexpectedly trivial")

    maximum_coordinate_rounding_error = max(
        abs(float(value) - integer)
        for row in direct_rows.values()
        for value, integer in zip(
            row["fitted_homology_coordinates"],
            row["selected_integer_translation"],
        )
    )
    multiplier_counts = Counter(selected_multipliers.values())
    affine = {
        "schema": "MTTQ79CompleteAffineDeltaNormalFunctionCocycle.v1",
        "status": (
            "COMPLETE_SELECTED_INTEGRAL_AFFINE_COCYCLE_AND_EXACT_SURFACE_"
            "RELATION_CLOSED"
        ),
        "homology_basis": ["a1", "b1", "a2", "b2"],
        "exact_mumford_source": production["exact_mumford_source"],
        "physical_handle_lifts": {
            "A": "+A_braid",
            "B": "-B_braid",
            "A_translation": integer_vector(translation_a),
            "B_translation": integer_vector(translation_b),
        },
        "local_rows": rows,
        "direct_rows": len(direct_rows),
        "relation_completed_rows": relation_indices,
        "maximum_direct_coordinate_rounding_error": format(
            maximum_coordinate_rounding_error, ".17g"
        ),
        "translation_multiplier_counts": {
            str(key): value for key, value in sorted(multiplier_counts.items())
        },
        "affine_surface_relation": {
            "path_word": "A*B*A^-1*B^-1=m1*...*m90",
            "left_action_linear_matrix": [
                [int(value) for value in row] for row in boundary[0].tolist()
            ],
            "handle_boundary_translation": integer_vector(boundary[1]),
            "ordered_meridian_translation": integer_vector(exact_product[1]),
            "symbolic_residual_before_solution": [
                str(value) for value in equations
            ],
            "unique_integer_solution": {"m43": 1, "m45": 0},
            "exact_matrix_and_translation_equality": True,
        },
        "cohomology": {
            "all_local_singularity_classes_zero": True,
            "reason": (
                "Every local translation is an integral multiple of the "
                "corresponding Picard-Lefschetz vanishing cycle, hence lies "
                "in image(M_i-I)."
            ),
            "global_integral_coboundary_exists": False,
            "global_cocycle_nontrivial": True,
            "meaning": (
                "The divisor normal function extends admissibly across every "
                "node but represents a genuine global integral Leray class; "
                "one period shift cannot trivialize all 92 generators."
            ),
        },
        "strict_scope": {
            "integer_rows_selected": 90,
            "direct_floating_rows": 88,
            "exact_relation_completed_rows": 2,
            "floating_interval_enclosure": False,
            "Deligne_beta_period_vector_emitted": False,
            "integral_H2_branch_selected": False,
            "beta_C_zero_or_nonzero_decided": False,
        },
    }
    dump(AFFINE, affine)

    production_lift = np.asarray(
        [complex_value(value) for value in production["base_abel_jacobi_lift"]["values"]]
    )
    tight_lift = np.asarray(
        [complex_value(value) for value in tight["base_abel_jacobi_lift"]["values"]]
    )
    handle_differences: dict[str, dict] = {}
    maximum_handle_jump_difference = 0.0
    maximum_relative_period_difference = 0.0
    for name in ["A", "B"]:
        production_row = next(
            row for row in production["handles"] if row["name"] == name
        )
        tight_row = next(
            row for row in tight["handles"] if row["name"] == name
        )
        production_jump = np.asarray(
            [complex_value(value) for value in production_row["physical_jump"]]
        )
        tight_jump = np.asarray(
            [complex_value(value) for value in tight_row["physical_jump"]]
        )
        production_relative = np.asarray(
            [complex_value(value) for value in production_row["relative_periods"]]
        )
        tight_relative = np.asarray(
            [complex_value(value) for value in tight_row["relative_periods"]]
        )
        jump_difference = float(np.max(abs(production_jump - tight_jump)))
        relative_difference = float(
            np.max(abs(production_relative - tight_relative))
        )
        maximum_handle_jump_difference = max(
            maximum_handle_jump_difference, jump_difference
        )
        maximum_relative_period_difference = max(
            maximum_relative_period_difference, relative_difference
        )
        handle_differences[name] = {
            "selected_integer_translation": production_row[
                "selected_integer_translation"
            ],
            "maximum_physical_jump_difference": format(
                jump_difference, ".17g"
            ),
            "maximum_eight_row_relative_period_difference": format(
                relative_difference, ".17g"
            ),
        }
    convergence = {
        "schema": "MTTQ79DeltaNormalFunctionFloatingConvergence.v1",
        "status": "TWO_RUN_HANDLE_NORMAL_FUNCTION_DIFFERENCE_RECORDED",
        "production_tolerances": production["tolerances"],
        "tight_tolerances": tight["tolerances"],
        "maximum_base_lift_absolute_difference": format(
            float(np.max(abs(production_lift - tight_lift))), ".17g"
        ),
        "handles": handle_differences,
        "maximum_handle_jump_absolute_difference": format(
            maximum_handle_jump_difference, ".17g"
        ),
        "maximum_relative_period_absolute_difference": format(
            maximum_relative_period_difference, ".17g"
        ),
        "strict_scope": {
            "two_run_floating_check": True,
            "interval_enclosure": False,
            "rigorous_truncation_bound": False,
        },
    }
    dump(CONVERGENCE, convergence)

    beta_open = {
        "schema": "MTTQ79DeligneBetaPeriodAndIntegralBranchInput.v1",
        "status": "OPEN_ANALYTIC_DELIGNE_PAIRING_AND_INTEGRAL_H2_BRANCH",
        "closed_input": {
            "exact_Mumford_normal_function_source": str(
                AFFINE.relative_to(ROOT)
            ).replace("\\", "/"),
            "complete_affine_monodromy_cocycle": True,
            "normal_function_handle_relative_period_rows": {
                name: next(
                    row["relative_periods"]
                    for row in production["handles"]
                    if row["name"] == name
                )
                for name in ["A", "B"]
            },
            "full_integral_period_table": str(
                PERIOD_TABLE.relative_to(ROOT)
            ).replace("\\", "/"),
        },
        "required_next_derivation": [
            "derive the Deligne/Poincare pairing functional that maps the affine normal-function cocycle to the eight additive beta periods",
            "express the resulting z_8 on the A119 integral H2 basis and solve z=Pi*ell, or certify exact nonmembership",
            "only after a zero branch, differentiate the same source in the eight PGL3 directions and certify the covariant Jacobian",
        ],
        "guard": {
            "affine_monodromy_is_not_itself_z_8": True,
            "global_cocycle_nontrivial_does_not_by_itself_prove_beta_nonzero": True,
            "floating_nearest_lattice_is_not_accepted": True,
        },
    }
    dump(BETA_OPEN, beta_open)

    frontier = {
        "schema": "MTTU6FrontierAfterA120.v1",
        "status": STATUS,
        "exact_Mumford_source_closed": True,
        "normal_function_handle_translations_selected": 2,
        "normal_function_local_translations_selected": 90,
        "direct_local_rows": 88,
        "exact_relation_completed_local_rows": 2,
        "affine_surface_relation_exact": True,
        "local_singularity_classes_zero": 90,
        "global_affine_cocycle_nontrivial": True,
        "normal_function_handle_relative_period_rows_emitted": 16,
        "Deligne_beta_C_period_rows_emitted": 0,
        "integral_period_branch_selected": False,
        "gerbe_zero_or_no_go_executed": False,
        "strict_MTT_source_moduli_removed": 0,
        "U6_strong_CP_closed": False,
        "next_required_artifact": NEXT,
    }
    dump(FRONTIER, frontier)

    authority_paths = [
        PRODUCTION,
        TIGHT,
        FACTORIZATION,
        PERIOD_TABLE,
        *DIRECT_BATCHES,
        COMPUTE_ENGINE,
        Path(__file__),
        AFFINE,
        CONVERGENCE,
        BETA_OPEN,
        FRONTIER,
    ]
    candidate = {
        "schema": (
            "MTTSelectedQ79GenusTwoNormalFunctionBetaAndIntegralBranchExecution.v1"
        ),
        "status": STATUS,
        "proof_artifact": (
            "proof_corpus/MTT_Selected_q79GenusTwoNormalFunctionBetaAndIntegralBranchExecution_v1.md"
        ),
        "authority_hashes": [
            {
                "path": str(path.relative_to(ROOT)).replace("\\", "/"),
                "sha256": sha256(path),
            }
            for path in authority_paths
        ],
        "outputs": {
            "affine_cocycle": str(AFFINE.relative_to(ROOT)).replace("\\", "/"),
            "floating_convergence": str(CONVERGENCE.relative_to(ROOT)).replace("\\", "/"),
            "beta_branch_open": str(BETA_OPEN.relative_to(ROOT)).replace("\\", "/"),
            "frontier": str(FRONTIER.relative_to(ROOT)).replace("\\", "/"),
        },
        "checks": {
            "exact_Mumford_source": True,
            "all_90_local_integral_translations_selected": len(rows) == 90,
            "all_local_translations_are_PL_multiples": all(
                row["translation_multiplier"] is not None for row in rows
            ),
            "affine_surface_relation_exact": exact_product == boundary,
            "global_cocycle_is_not_a_coboundary": (
                coboundary_solution == sp.EmptySet
            ),
            "Deligne_beta_not_invented": (
                frontier["Deligne_beta_C_period_rows_emitted"] == 0
            ),
            "integral_branch_not_invented": not frontier[
                "integral_period_branch_selected"
            ],
        },
        "results": frontier,
        "next_required_artifact": NEXT,
    }
    dump(CANDIDATE, candidate)
    certificate = {
        "certificate": (
            "MTTSelectedQ79GenusTwoNormalFunctionBetaAndIntegralBranchExecution"
        ),
        "status": STATUS,
        "candidate_path": str(CANDIDATE.relative_to(ROOT)).replace("\\", "/"),
        "candidate_sha256": sha256(CANDIDATE),
        "exact_Mumford_source_closed": True,
        "complete_affine_normal_function_cocycle_closed": True,
        "Deligne_beta_period_closed": False,
        "integral_branch_selected": False,
        "full_U6_closed": False,
        "target_fitting_used": False,
        "next_required_artifact": NEXT,
    }
    dump(CERTIFICATE, certificate)
    print(json.dumps(candidate, indent=2, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
