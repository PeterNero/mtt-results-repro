from __future__ import annotations

import hashlib
import json
from pathlib import Path

from flint import acb, acb_mat, arb, ctx

import certify_q79_height4_dynamic_target_full_residue_interval as dynamic
import certify_q79_height4_target_main_hessian_interval as main_hessian
import certify_q79_height4_tight_target_full_residue_interval as tight
import certify_q79_selected_side_beta_defect_transport as validated


ROOT = Path(__file__).resolve().parents[1]
OUTPUT = main_hessian.VALIDATED / "n3.batched_taylor_solve.selfcheck.json"
NOTE = ROOT / "proof_corpus" / "MTT_q79HeightFourBatchedTaylorSolveSelfcheck_A380S_v1.md"
ARTIFACT = "A380S"


TM = validated.TaylorModel


def dump(path: Path, value: dict) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(value, indent=2, sort_keys=True) + "\n", encoding="utf-8")


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def relative(path: Path) -> str:
    return str(path.relative_to(ROOT)).replace("\\", "/")


def reduction_system(
    system: validated.SelectedQ79IntervalSystem,
    order: int,
) -> tuple[list[list[TM]], list[list[TM]]]:
    radius = arb("1e-5")
    a_value, b_value, _elliptic_residual, _elliptic_remainder = (
        validated.validated_ab_taylor_models(
            system, 0.0 + 0.0j, 1.0 + 0.0j, radius, order
        )
    )
    one = a_value.constant(1, order, radius)
    zero = a_value.constant(0, order, radius)
    elliptic = [a_value, b_value, one]
    elliptic_w = [
        acb(2) * system.period_length * b_value,
        system.period_length * (acb(3) * a_value**2 - 1),
        zero,
    ]
    line = validated.tm_matrix_vector(system.alignment, elliptic)
    line_derivatives = [validated.tm_matrix_vector(system.alignment, elliptic_w)]
    line_derivatives.extend(
        validated.tm_matrix_vector(
            system.alignment * system.generators[selected_direction], elliptic
        )
        for selected_direction in range(8)
    )
    f_coefficients, f_derivatives = (
        main_hessian.aligned_tm_coefficients_and_derivatives_batch(
            system.evaluator.tables["F6"],
            line,
            line_derivatives,
            chart=system.line_chart,
        )
    )
    prototype = f_coefficients[0]
    zero = main_hessian.beta_hessian.tm_zero(prototype)
    polynomial_derivative = [
        index * f_coefficients[index] for index in range(1, 7)
    ]
    reduction = [[zero for _ in range(11)] for _ in range(11)]
    targets = [[zero for _ in range(45)] for _ in range(11)]
    half = acb("0.5")
    for power in range(6):
        if power:
            for index, coefficient in enumerate(f_coefficients):
                reduction[index + power - 1][power] += power * coefficient
        for index, coefficient in enumerate(polynomial_derivative):
            reduction[index + power][power] -= half * coefficient
    for power in range(5):
        for index, coefficient in enumerate(f_coefficients):
            reduction[index + power][6 + power] += coefficient
    for derivative_index, f_derivative in enumerate(f_derivatives):
        offset = 5 * derivative_index
        for power in range(5):
            for index, coefficient in enumerate(f_derivative):
                targets[index + power][offset + power] -= half * coefficient
    return reduction, targets


def center_polynomial(value: TM) -> TM:
    return TM(
        [
            validated.SelectedQ79IntervalSystem.midpoint_acb(coefficient)
            for coefficient in value.coefficients
        ],
        value.radius,
        arb(0),
    )


def chart_check(
    system: validated.SelectedQ79IntervalSystem,
    order: int,
) -> dict:
    reduction, targets = reduction_system(system, order)
    solved, neumann, solve_error = main_hessian.tm_matrix_solve_batched(
        reduction, targets
    )
    candidate = [
        [center_polynomial(value) for value in row]
        for row in solved
    ]
    matrix_coefficients = validated.tm_matrix_coefficients(reduction)
    target_coefficients = validated.tm_matrix_coefficients(targets)
    candidate_coefficients = validated.tm_matrix_coefficients(candidate)
    residual_coefficients = []
    for degree in range(2 * order + 1):
        if degree <= order:
            residual = main_hessian.acb_matrix_copy(target_coefficients[degree])
        else:
            residual = acb_mat(len(reduction), len(targets[0]))
        for matrix_degree in range(max(0, degree - order), min(order, degree) + 1):
            candidate_degree = degree - matrix_degree
            residual -= (
                matrix_coefficients[matrix_degree]
                * candidate_coefficients[candidate_degree]
            )
        residual_coefficients.append(residual)

    powers = [arb(1)]
    for _degree in range(2 * order):
        powers.append(powers[-1] * candidate[0][0].radius)
    candidate_bounds = [
        [
            candidate[row][column].polynomial_absolute_bound()
            for column in range(len(targets[0]))
        ]
        for row in range(len(reduction))
    ]
    inverse_norm, independent_neumann = validated.tm_verified_inverse_bound(
        reduction
    )
    required_corrections = []
    assigned_corrections = []
    for column in range(len(targets[0])):
        row_bounds = []
        for row in range(len(reduction)):
            bound = targets[row][column].remainder
            for degree, coefficients in enumerate(residual_coefficients):
                bound += abs(coefficients[row, column]) * powers[degree]
            for inner in range(len(reduction)):
                bound += (
                    reduction[row][inner].remainder
                    * candidate_bounds[inner][column]
                )
            row_bounds.append(bound)
        residual_norm = max(row_bounds, key=validated.upper)
        required = validated.upper(inverse_norm * residual_norm)
        assigned = min(
            validated.upper(solved[row][column].remainder)
            for row in range(len(reduction))
        )
        required_corrections.append(required)
        assigned_corrections.append(assigned)
    all_covered = all(
        assigned >= required
        for assigned, required in zip(assigned_corrections, required_corrections)
    )
    if not all_covered:
        raise AssertionError(
            f"{system.line_chart}-chart coefficient residual exceeds the "
            "assigned correction: required="
            f"{max(required_corrections):.6e}, assigned="
            f"{min(assigned_corrections):.6e}"
        )
    generic, generic_neumann, generic_error = validated.tm_matrix_solve(
        reduction, targets
    )
    maximum_center_coefficient_difference = max(
        validated.upper(
            abs(
                solved[row][column].coefficients[degree]
                - generic[row][column].coefficients[degree]
            )
        )
        for row in range(len(reduction))
        for column in range(len(targets[0]))
        for degree in range(order + 1)
    )
    if maximum_center_coefficient_difference >= 1.0e-50:
        raise AssertionError("batched and generic center recurrences disagree")
    return {
        "line_chart": system.line_chart,
        "Taylor_order": order,
        "right_hand_side_count": 9,
        "target_column_count": 45,
        "fast_solver_Neumann_norm": neumann,
        "independent_Neumann_norm": independent_neumann,
        "generic_solver_Neumann_norm": generic_neumann,
        "generic_solver_maximum_error": generic_error,
        "maximum_generic_center_coefficient_difference": (
            maximum_center_coefficient_difference
        ),
        "fast_solver_maximum_error": solve_error,
        "independent_maximum_required_correction": max(required_corrections),
        "minimum_assigned_correction": min(assigned_corrections),
        "minimum_assigned_minus_required_margin": min(
            assigned - required
            for assigned, required in zip(
                assigned_corrections, required_corrections
            )
        ),
        "all_45_independent_residual_corrections_covered": True,
    }


def main() -> int:
    ctx.dps = 90
    order = 6
    systems = [
        dynamic.z_helper.exact_z_system(90),
        tight.ORIGINAL_EXACT_TARGET_SYSTEM(90),
    ]
    checks = [chart_check(system, order) for system in systems]
    payload = {
        "schema": "MTTQ79HeightFourBatchedTaylorSolveSelfcheck.v1",
        "status": "BATCHED_TAYLOR_SOLVE_INDEPENDENT_RESIDUAL_COVERAGE_CERTIFIED",
        "artifact": ARTIFACT,
        "chart_checks": checks,
        "summary": {
            "certified_charts": len(checks),
            "certified_right_hand_sides_per_chart": 9,
            "certified_target_columns_per_chart": 45,
            "all_independent_residual_corrections_covered": all(
                row["all_45_independent_residual_corrections_covered"]
                for row in checks
            ),
            "minimum_coverage_margin": min(
                row["minimum_assigned_minus_required_margin"] for row in checks
            ),
        },
        "authority": {
            name: {"path": relative(path), "sha256": sha256(path)}
            for name, path in {
                "A380_main_Hessian_builder": Path(main_hessian.__file__).resolve(),
                "validated_Taylor_engine": Path(validated.__file__).resolve(),
                "selfcheck_source": Path(__file__).resolve(),
            }.items()
        },
        "strict_scope": {
            "observed_SM_values_used": False,
            "both_selected_line_charts_checked": True,
            "independent_degree_2N_coefficient_residual_used": True,
            "generic_solver_center_recurrence_replayed": True,
            "batched_solver_residual_coverage_closed": True,
            "full_76_target_chain_Hessian_interval_closed": False,
            "interval_Newton_existence_and_uniqueness_closed": False,
            "full_SM_closure_proved": False,
        },
    }
    dump(OUTPUT, payload)
    NOTE.write_text(
        "# MTT q79 Height-Four Batched Taylor Solve Selfcheck (A380S) v1\n\n"
        "A380S independently convolves the selected Taylor reduction matrix "
        "with the center-polynomial candidate through degree `2N`, then adds "
        "the target and reduction-model remainders before applying the verified "
        "inverse bound. It also replays the center recurrence with the established "
        "generic solver. All 45 right-hand-side columns are enclosed in both "
        "selected line charts.\n\n"
        f"The minimum assigned-minus-required correction margin is "
        f"`{payload['summary']['minimum_coverage_margin']:.12g}`. No observed "
        "Standard Model datum enters this implementation certificate.\n",
        encoding="utf-8",
    )
    print(f"wrote {relative(OUTPUT)}")
    print(f"wrote {relative(NOTE)}")
    print(json.dumps(payload["summary"], indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
