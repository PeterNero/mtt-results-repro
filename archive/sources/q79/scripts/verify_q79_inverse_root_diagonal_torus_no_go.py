#!/usr/bin/env python3
"""Test exact row-semi-invariant diagonal scalings of q79 inverse-root parents."""

from __future__ import annotations

import argparse
import hashlib
import itertools
import json
import math
from pathlib import Path

from flint import nmod_mpoly_ctx
from sympy import Matrix

from build_q79_D10_D6_h1_g1_pair_quotient_obstructions import (
    PRIME,
    parse_input,
    parse_polynomial,
)


def require(condition: bool, label: str) -> None:
    if not condition:
        raise AssertionError(label)


def checksum(path: Path) -> dict[str, object]:
    return {
        "path": str(path),
        "bytes": path.stat().st_size,
        "sha256": hashlib.sha256(path.read_bytes()).hexdigest(),
    }


def rank_mod(matrix: list[list[int]], prime: int) -> int:
    work = [[value % prime for value in row] for row in matrix]
    if not work:
        return 0
    row_index = 0
    for column in range(len(work[0])):
        pivot = next(
            (index for index in range(row_index, len(work)) if work[index][column]),
            None,
        )
        if pivot is None:
            continue
        work[row_index], work[pivot] = work[pivot], work[row_index]
        inverse = pow(work[row_index][column], -1, prime)
        work[row_index] = [value * inverse % prime for value in work[row_index]]
        for index in range(len(work)):
            if index == row_index or work[index][column] == 0:
                continue
            factor = work[index][column]
            work[index] = [
                (left - factor * right) % prime
                for left, right in zip(work[index], work[row_index])
            ]
        row_index += 1
        if row_index == len(work):
            break
    return row_index


def affine_solution_space_mod_prime(
    matrix: list[list[int]], target: list[int], prime: int
) -> tuple[list[int], list[list[int]]] | None:
    require(len(matrix) == len(target), "affine system row count")
    columns = len(matrix[0])
    augmented = [
        [*(value % prime for value in row), target[index] % prime]
        for index, row in enumerate(matrix)
    ]
    rank = 0
    pivots = []
    for column in range(columns):
        pivot = next(
            (index for index in range(rank, len(augmented)) if augmented[index][column]),
            None,
        )
        if pivot is None:
            continue
        augmented[rank], augmented[pivot] = augmented[pivot], augmented[rank]
        inverse = pow(augmented[rank][column], -1, prime)
        augmented[rank] = [value * inverse % prime for value in augmented[rank]]
        for index in range(len(augmented)):
            if index == rank or augmented[index][column] == 0:
                continue
            factor = augmented[index][column]
            augmented[index] = [
                (left - factor * right) % prime
                for left, right in zip(augmented[index], augmented[rank])
            ]
        pivots.append(column)
        rank += 1
    if not all(any(row[:columns]) or row[-1] == 0 for row in augmented):
        return None
    free = [column for column in range(columns) if column not in pivots]
    particular = [0] * columns
    for row_index, pivot in enumerate(pivots):
        particular[pivot] = augmented[row_index][-1]
    basis = []
    for free_column in free:
        vector = [0] * columns
        vector[free_column] = 1
        for row_index, pivot in enumerate(pivots):
            vector[pivot] = -augmented[row_index][free_column] % prime
        basis.append(vector)
    return particular, basis


def enumerate_affine_space(
    particular: list[int], basis: list[list[int]], prime: int
) -> list[list[int]]:
    result = []
    for coefficients in itertools.product(range(prime), repeat=len(basis)):
        vector = list(particular)
        for coefficient, direction in zip(coefficients, basis):
            vector = [
                (left + coefficient * right) % prime
                for left, right in zip(vector, direction)
            ]
        result.append(vector)
    return result


def kernel_mod4(matrix: list[list[int]]) -> list[list[int]]:
    homogeneous = affine_solution_space_mod_prime(matrix, [0] * len(matrix), 2)
    require(homogeneous is not None, "homogeneous mod-2 system")
    zero, kernel_mod2 = homogeneous
    reductions = enumerate_affine_space(zero, kernel_mod2, 2)
    lifts = set()
    for reduction in reductions:
        products = [sum(left * right for left, right in zip(row, reduction)) for row in matrix]
        require(all(value % 2 == 0 for value in products), "mod-2 kernel reduction")
        target = [-(value // 2) % 2 for value in products]
        correction_space = affine_solution_space_mod_prime(matrix, target, 2)
        if correction_space is None:
            continue
        particular, directions = correction_space
        for correction in enumerate_affine_space(particular, directions, 2):
            lift = tuple(
                (residue + 2 * value) % 4
                for residue, value in zip(reduction, correction)
            )
            require(
                all(sum(left * right for left, right in zip(row, lift)) % 4 == 0 for row in matrix),
                "valid mod-4 lift",
            )
            lifts.add(lift)
    return [list(value) for value in sorted(lifts)]


def exponent_constraints(rows) -> list[list[int]]:
    constraints = []
    for row in rows:
        monomials = sorted(tuple(int(value) for value in monomial) for monomial in row.to_dict())
        require(monomials, "nonzero parent row")
        reference = monomials[0]
        constraints.extend(
            [left - right for left, right in zip(monomial, reference)]
            for monomial in monomials[1:]
        )
    return constraints


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--input", type=Path, action="append", required=True)
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()
    require(len(args.input) == 4, "four inverse-root parents")

    charts = []
    support_hashes = set()
    for path in args.input:
        names, field, texts = parse_input(path)
        require(field == PRIME and len(names) == 19 and len(texts) == 22, "parent shape")
        context = nmod_mpoly_ctx.get(names, ordering="degrevlex", modulus=PRIME)
        rows = [parse_polynomial(text, context, names) for text in texts]
        constraints = exponent_constraints(rows)
        require(all(len(row) == len(names) for row in constraints), "weight constraints")
        rational_rank = int(Matrix(constraints).rank())
        rank_2 = rank_mod(constraints, 2)
        rank_5 = rank_mod(constraints, 5)
        weights_mod4 = kernel_mod4(constraints)
        weights_mod100 = [
            [25 * value % 100 for value in vector] for vector in weights_mod4
        ]
        require(
            all(
                all(
                    sum(left * right for left, right in zip(row, vector)) % 100 == 0
                    for row in constraints
                )
                for vector in weights_mod100
            ),
            "CRT-lifted mod-100 kernels",
        )
        u1_index = names.index("u1")
        u1_exponents = sorted({vector[u1_index] for vector in weights_mod100})
        u1_orders = sorted({100 // math.gcd(value, 100) for value in u1_exponents})
        v_index = names.index("v")
        exact_sign_kernel = {
            tuple(vector) for vector in weights_mod100
        } == {
            tuple([0] * len(names)),
            tuple(50 if index == v_index else 0 for index in range(len(names))),
        }
        support_text = "\n".join(
            ",".join(map(str, sorted(polynomial.to_dict()))) for polynomial in rows
        )
        support_hash = hashlib.sha256(support_text.encode("ascii")).hexdigest()
        support_hashes.add(support_hash)
        charts.append(
            {
                "input": checksum(path),
                "variables": names,
                "parent_rows": len(rows),
                "exponent_difference_constraints": len(constraints),
                "monomial_support_sha256": support_hash,
                "rank_over_Q": rational_rank,
                "nullity_over_Q": len(names) - rational_rank,
                "rank_mod_2": rank_2,
                "nullity_mod_2": len(names) - rank_2,
                "rank_mod_5": rank_5,
                "nullity_mod_5": len(names) - rank_5,
                "weight_kernel_mod_4": weights_mod4,
                "weight_kernel_mod_100": weights_mod100,
                "u1_exponents_mod_100": u1_exponents,
                "u1_character_orders": u1_orders,
                "maximum_u1_orbit_size": max(u1_orders),
                "can_normalize_all_100_nonzero_u1_values": max(u1_orders) == 100,
                "exact_finite_diagonal_symmetry_is_v_sign": exact_sign_kernel,
            }
        )

    for row in charts:
        print(
            f"diagnostic {Path(row['input']['path']).name}: "
            f"{row['rank_over_Q']}/{row['rank_mod_2']}/{row['rank_mod_5']}"
        )
    require(len(support_hashes) in {1, 2}, "at most two mirror-space monomial supports")
    require(
        all(
            row["rank_over_Q"] == 19
            and row["rank_mod_2"] == 18
            and row["rank_mod_5"] == 19
            and row["exact_finite_diagonal_symmetry_is_v_sign"]
            and not row["can_normalize_all_100_nonzero_u1_values"]
            for row in charts
        ),
        "continuous and transitive finite diagonal normalization no-go",
    )
    checks = {
        "all_four_inverse_root_parent_presentations_are_checked": True,
        "every_monomial_exponent_difference_is_included": True,
        "the_weight_constraint_matrix_has_full_rank_over_Q": True,
        "the_weight_constraint_matrix_has_one_residual_direction_mod_2": True,
        "the_weight_constraint_matrix_has_full_rank_mod_5": True,
        "the_complete_mod_4_kernel_is_lifted_exactly": True,
        "the_complete_mod_100_kernel_follows_by_CRT_with_zero_mod_25_component": True,
        "the_only_finite_diagonal_weights_are_identity_and_v_sign": True,
        "u1_is_fixed_by_the_complete_rowwise_diagonal_symmetry": True,
        "u1_cannot_be_normalized_through_all_F101_star_by_a_rowwise_diagonal_action": True,
        "nonlinear_or_generator_mixing_transports_are_not_excluded": True,
        "no_continuous_fit_parameter_is_added": True,
    }
    result = {
        "schema": "MTTQ79InverseRootDiagonalTorusNoGo.v1",
        "date": "2026-07-20",
        "status": "EXACT_ROWWISE_DIAGONAL_TRANSITIVE_U1_NORMALIZATION_NO_GO",
        "field": "F_101",
        "charts": charts,
        "checks": checks,
        "theorem": (
            "For each inverse-root parent, requiring every displayed generator to be "
            "semi-invariant under a diagonal variable scaling gives a full-rank "
            "19-column exponent-difference system over Q and F_5, with one residual "
            "direction over F_2. Exact lifting through mod 4 and CRT gives precisely "
            "two weights mod 100: the identity and weight 50 on v alone. Thus the "
            "complete rowwise diagonal symmetry is v -> +/-v, while u1 is fixed. "
            "No such action can move any u1 != 1 to the computed u1=1 slice."
        ),
        "claim_boundary": (
            "This rules out only diagonal actions for which each displayed parent row "
            "is individually semi-invariant. It does not rule out nonlinear triangular "
            "transport, coordinate changes that mix generators, or a different source "
            "presentation. It is a route-elimination theorem, not chart closure."
        ),
        "next_target": (
            "Use nonlinear triangular transport with an independently verified ideal "
            "intertwiner, or continue the checkpointed finite cover."
        ),
        "new_continuous_fit_parameters": 0,
    }
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
    print(result["status"])
    for row in charts:
        print(
            f"{Path(row['input']['path']).name}: constraints="
            f"{row['exponent_difference_constraints']} ranks="
            f"{row['rank_over_Q']}/{row['rank_mod_2']}/{row['rank_mod_5']}"
        )
    print(args.output)


if __name__ == "__main__":
    main()
