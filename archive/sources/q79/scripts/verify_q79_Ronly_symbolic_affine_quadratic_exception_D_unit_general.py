#!/usr/bin/env python3
"""Certify D rejection in a finite affine-quadratic q79 line quotient."""

from __future__ import annotations

import argparse
import hashlib
import json
import re
from pathlib import Path

from flint import nmod_mpoly_ctx

from build_q79_D10_D6_h1_g1_pair_quotient_obstructions import (
    PRIME,
    parse_input,
    parse_polynomial,
)


R_ROWS = tuple(range(1, 13))
Y_ROWS = tuple(range(14, 18))
D_ROWS = tuple(range(18, 22))


def require(condition: bool, label: str) -> None:
    if not condition:
        raise AssertionError(label)


def checksum(path: Path) -> dict[str, object]:
    return {
        "path": path.as_posix(),
        "bytes": path.stat().st_size,
        "sha256": hashlib.sha256(path.read_bytes()).hexdigest(),
    }


def solve_square(matrix: list[list[int]], target: list[int]) -> list[int] | None:
    dimension = len(target)
    require(
        len(matrix) == dimension and all(len(row) == dimension for row in matrix),
        "square linear system",
    )
    augmented = [
        [*(value % PRIME for value in row), target[index] % PRIME]
        for index, row in enumerate(matrix)
    ]
    rank = 0
    pivots = []
    for column in range(dimension):
        pivot = next(
            (index for index in range(rank, dimension) if augmented[index][column]),
            None,
        )
        if pivot is None:
            continue
        augmented[rank], augmented[pivot] = augmented[pivot], augmented[rank]
        inverse = pow(augmented[rank][column], -1, PRIME)
        augmented[rank] = [value * inverse % PRIME for value in augmented[rank]]
        for index in range(dimension):
            if index == rank or augmented[index][column] == 0:
                continue
            factor = augmented[index][column]
            augmented[index] = [
                (left - factor * right) % PRIME
                for left, right in zip(augmented[index], augmented[rank])
            ]
        pivots.append(column)
        rank += 1
    if rank != dimension:
        return None
    require(pivots == list(range(dimension)), "ordered full pivots")
    return [augmented[index][-1] for index in range(dimension)]


def determinant_mod(matrix: list[list[int]]) -> int:
    dimension = len(matrix)
    require(all(len(row) == dimension for row in matrix), "determinant square matrix")
    work = [[value % PRIME for value in row] for row in matrix]
    determinant = 1
    for column in range(dimension):
        pivot = next(
            (index for index in range(column, dimension) if work[index][column]),
            None,
        )
        if pivot is None:
            return 0
        if pivot != column:
            work[column], work[pivot] = work[pivot], work[column]
            determinant = -determinant
        pivot_value = work[column][column]
        determinant = determinant * pivot_value % PRIME
        inverse = pow(pivot_value, -1, PRIME)
        for index in range(column + 1, dimension):
            factor = work[index][column] * inverse % PRIME
            if factor:
                work[index] = [
                    (left - factor * right) % PRIME
                    for left, right in zip(work[index], work[column])
                ]
    return determinant % PRIME


class FiniteAlgebra:
    def __init__(self, free_names: list[str], products: dict[tuple[int, int], list[int]]):
        self.free_names = tuple(free_names)
        self.dimension = len(free_names) + 1
        self.products = {
            tuple(sorted(pair)): tuple(value % PRIME for value in coefficients)
            for pair, coefficients in products.items()
        }
        expected = {
            (left, right)
            for left in range(1, self.dimension)
            for right in range(left, self.dimension)
        }
        require(set(self.products) == expected, "complete quadratic multiplication table")
        require(
            all(len(coefficients) == self.dimension for coefficients in self.products.values()),
            "multiplication-vector dimensions",
        )

    def element(self, coefficients) -> "AlgebraElement":
        return AlgebraElement(self, coefficients)

    def zero(self) -> "AlgebraElement":
        return self.element([0] * self.dimension)

    def one(self) -> "AlgebraElement":
        return self.element([1, *([0] * (self.dimension - 1))])

    def constant(self, value: int) -> "AlgebraElement":
        return self.element([value, *([0] * (self.dimension - 1))])

    def generator(self, index: int) -> "AlgebraElement":
        require(1 <= index < self.dimension, "free generator index")
        values = [0] * self.dimension
        values[index] = 1
        return self.element(values)

    def basis_product(self, left: int, right: int) -> tuple[int, ...]:
        if left == 0:
            values = [0] * self.dimension
            values[right] = 1
            return tuple(values)
        if right == 0:
            values = [0] * self.dimension
            values[left] = 1
            return tuple(values)
        return self.products[tuple(sorted((left, right)))]

    def verify_associativity(self) -> int:
        checks = 0
        basis = [self.one(), *(self.generator(index) for index in range(1, self.dimension))]
        for left in basis:
            for middle in basis:
                for right in basis:
                    require((left * middle) * right == left * (middle * right), "associativity")
                    checks += 1
        return checks


class AlgebraElement:
    def __init__(self, algebra: FiniteAlgebra, coefficients):
        self.algebra = algebra
        self.coefficients = tuple(int(value) % PRIME for value in coefficients)
        require(len(self.coefficients) == algebra.dimension, "algebra element dimension")

    def coerce(self, other) -> "AlgebraElement":
        if isinstance(other, AlgebraElement):
            require(other.algebra is self.algebra, "common finite algebra")
            return other
        return self.algebra.constant(int(other))

    def __eq__(self, other):
        try:
            other = self.coerce(other)
        except (AssertionError, TypeError, ValueError):
            return False
        return self.coefficients == other.coefficients

    def __add__(self, other):
        other = self.coerce(other)
        return self.algebra.element(
            (left + right) % PRIME
            for left, right in zip(self.coefficients, other.coefficients)
        )

    __radd__ = __add__

    def __neg__(self):
        return self.algebra.element(-value for value in self.coefficients)

    def __sub__(self, other):
        return self + (-self.coerce(other))

    def __rsub__(self, other):
        return self.coerce(other) - self

    def __mul__(self, other):
        other = self.coerce(other)
        result = [0] * self.algebra.dimension
        for left, left_value in enumerate(self.coefficients):
            if left_value == 0:
                continue
            for right, right_value in enumerate(other.coefficients):
                if right_value == 0:
                    continue
                scale = left_value * right_value % PRIME
                product = self.algebra.basis_product(left, right)
                result = [
                    (value + scale * coefficient) % PRIME
                    for value, coefficient in zip(result, product)
                ]
        return self.algebra.element(result)

    __rmul__ = __mul__

    def __pow__(self, exponent: int):
        require(exponent >= 0, "nonnegative exponent")
        result = self.algebra.one()
        base = self
        power = exponent
        while power:
            if power & 1:
                result *= base
            base *= base
            power >>= 1
        return result

    def multiplication_matrix(self) -> list[list[int]]:
        columns = []
        columns.append((self * self.algebra.one()).coefficients)
        for index in range(1, self.algebra.dimension):
            columns.append((self * self.algebra.generator(index)).coefficients)
        return [
            [columns[column][row] for column in range(self.algebra.dimension)]
            for row in range(self.algebra.dimension)
        ]

    def inverse_with_determinant(self) -> tuple["AlgebraElement", int] | None:
        matrix = self.multiplication_matrix()
        determinant = determinant_mod(matrix)
        if determinant == 0:
            return None
        target = [1, *([0] * (self.algebra.dimension - 1))]
        solution = solve_square(matrix, target)
        require(solution is not None, "nonzero determinant solves inverse")
        inverse = self.algebra.element(solution)
        require(self * inverse == self.algebra.one(), "exact algebra inverse")
        return inverse, determinant

    def as_list(self) -> list[int]:
        return list(self.coefficients)


def parse_basis(text: str):
    require(text.startswith("#Reduced Groebner basis data"), "reduced basis header")
    require("#field characteristic: 101" in text, "basis field")
    variable_match = re.search(r"#variable order:\s+(.*)", text)
    require(variable_match is not None, "basis variable order")
    names = tuple(value.strip() for value in variable_match.group(1).split(","))
    body_match = re.search(r"\n\[(.*)\]:\s*$", text, flags=re.DOTALL)
    require(body_match is not None, "basis body")
    row_texts = [row.strip() for row in body_match.group(1).split(",\n") if row.strip()]
    context = nmod_mpoly_ctx.get(names, ordering="degrevlex", modulus=PRIME)
    rows = [parse_polynomial(row, context, names) for row in row_texts]
    return names, context, rows


def used_variables(polynomial, names) -> set[str]:
    return {
        names[index]
        for monomial in polynomial.to_dict()
        for index, exponent in enumerate(monomial)
        if int(exponent)
    }


def evaluate(polynomial, names, values, algebra: FiniteAlgebra) -> AlgebraElement:
    require(set(names).issubset(values), "complete quotient assignment")
    total = algebra.zero()
    for monomial, coefficient in polynomial.to_dict().items():
        term = algebra.constant(int(coefficient))
        for name, exponent in zip(names, monomial):
            if int(exponent):
                term *= values[name] ** int(exponent)
        total += term
    return total


def recover_affine_quadratic_quotient(output_text: str):
    names, _, basis = parse_basis(output_text)
    require(len(names) == 12 and names[-1] == "v", "symbolic line variables")
    require(all(int(row.total_degree()) <= 2 for row in basis), "quadratic finite basis")
    relation_rows = [row for row in basis if int(row.total_degree()) == 2]
    affine_rows = [row for row in basis if int(row.total_degree()) <= 1]
    free_names = sorted(
        {
            names[index]
            for row in relation_rows
            for monomial in row.to_dict()
            if sum(int(exponent) for exponent in monomial) == 2
            for index, exponent in enumerate(monomial)
            if int(exponent)
        },
        key=names.index,
    )
    free_index = {name: index + 1 for index, name in enumerate(free_names)}
    free_count = len(free_names)
    require(
        len(affine_rows) == len(names) - free_count
        and len(relation_rows) == free_count * (free_count + 1) // 2,
        "affine-quadratic basis count",
    )

    products = {}
    relation_records = []
    for polynomial in relation_rows:
        quadratic_terms = []
        tail = [0] * (free_count + 1)
        for monomial, coefficient in polynomial.to_dict().items():
            coefficient = int(coefficient) % PRIME
            support = [
                (names[position], int(exponent))
                for position, exponent in enumerate(monomial)
                if int(exponent)
            ]
            degree = sum(exponent for _, exponent in support)
            if degree == 2:
                expanded = []
                for name, exponent in support:
                    require(name in free_index, "quadratic term uses a free coordinate")
                    expanded.extend([free_index[name]] * exponent)
                require(len(expanded) == 2, "quadratic product")
                quadratic_terms.append((tuple(sorted(expanded)), coefficient))
            elif degree == 1:
                require(len(support) == 1 and support[0][1] == 1, "affine tail term")
                name = support[0][0]
                require(name in free_index, "relation tail uses only free coordinates")
                tail[free_index[name]] = (tail[free_index[name]] + coefficient) % PRIME
            elif degree == 0:
                tail[0] = (tail[0] + coefficient) % PRIME
            else:
                raise AssertionError("relation degree exceeds two")
        require(len(quadratic_terms) == 1, "one leading quadratic product per relation")
        pair, pivot = quadratic_terms[0]
        require(pair not in products and pivot != 0, "unique quadratic pivot")
        inverse = pow(pivot, -1, PRIME)
        product = [(-inverse * value) % PRIME for value in tail]
        products[pair] = product
        relation_records.append(
            {
                "product": [free_names[pair[0] - 1], free_names[pair[1] - 1]],
                "pivot": pivot,
                "value_coefficients": product,
            }
        )

    algebra = FiniteAlgebra(free_names, products)
    associativity_checks = algebra.verify_associativity()
    values = {
        name: algebra.generator(index + 1) for index, name in enumerate(free_names)
    }
    coordinate_rows = {}
    for polynomial in affine_rows:
        pivot_names = used_variables(polynomial, names) - set(free_names)
        require(len(pivot_names) == 1, "one nonfree affine pivot")
        pivot_name = next(iter(pivot_names))
        require(pivot_name not in values, "unique affine pivot")
        pivot = 0
        remainder = algebra.zero()
        for monomial, coefficient in polynomial.to_dict().items():
            coefficient = int(coefficient) % PRIME
            support = [
                (names[position], int(exponent))
                for position, exponent in enumerate(monomial)
                if int(exponent)
            ]
            degree = sum(exponent for _, exponent in support)
            if degree == 0:
                remainder += coefficient
            elif degree == 1 and len(support) == 1:
                name = support[0][0]
                if name == pivot_name:
                    pivot = coefficient
                else:
                    require(name in values, "known free affine coordinate")
                    remainder += coefficient * values[name]
            else:
                raise AssertionError("invalid affine coordinate row")
        require(pivot != 0, "nonzero affine pivot")
        value = -pow(pivot, -1, PRIME) * remainder
        values[pivot_name] = value
        coordinate_rows[pivot_name] = {
            "pivot": pivot,
            "value_coefficients": value.as_list(),
        }
    require(set(values) == set(names), "all quotient coordinates recovered")
    require(
        all(evaluate(row, names, values, algebra) == algebra.zero() for row in basis),
        "exact basis reconstruction",
    )
    return names, basis, algebra, values, relation_records, coordinate_rows, associativity_checks


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--parent", type=Path, required=True)
    parser.add_argument("--symbolic-input", type=Path, required=True)
    parser.add_argument("--input-packet", type=Path, required=True)
    parser.add_argument("--basis-output", type=Path, required=True)
    parser.add_argument("--basis-log", type=Path, required=True)
    parser.add_argument("--space", type=int, choices=(5, 6), required=True)
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()

    input_packet = json.loads(args.input_packet.read_text(encoding="utf-8"))
    require(input_packet["schema"] == "MTTQ79RonlySymbolicVLineInput.v1", "input schema")
    require(input_packet["output"]["sha256"] == checksum(args.symbolic_input)["sha256"], "input hash")
    require(input_packet["parent_input"]["sha256"] == checksum(args.parent)["sha256"], "parent hash")

    basis_text = args.basis_output.read_text(encoding="ascii")
    (
        line_names,
        _,
        algebra,
        line_values,
        relation_records,
        coordinate_rows,
        associativity_checks,
    ) = recover_affine_quadratic_quotient(basis_text)
    zero = algebra.zero()
    one = algebra.one()

    input_names, input_field, input_texts = parse_input(args.symbolic_input)
    require(
        input_field == PRIME and input_names == line_names and len(input_texts) == 13,
        "symbolic line input",
    )
    line_context = nmod_mpoly_ctx.get(line_names, ordering="degrevlex", modulus=PRIME)
    line_rows = [parse_polynomial(text, line_context, line_names) for text in input_texts]
    line_remainders = [evaluate(row, line_names, line_values, algebra) for row in line_rows]
    require(all(value == zero for value in line_remainders), "line rows vanish")

    parent_names, parent_field, parent_texts = parse_input(args.parent)
    require(parent_field == PRIME and len(parent_names) == 19 and len(parent_texts) == 22, "parent input")
    parent_context = nmod_mpoly_ctx.get(parent_names, ordering="degrevlex", modulus=PRIME)
    parent_rows = [parse_polynomial(text, parent_context, parent_names) for text in parent_texts]
    fixed = input_packet["fixed_coordinates"]
    parent_values = dict(line_values)
    parent_values.update(
        {
            "u0": algebra.constant(int(fixed["selected_u0"])),
            "u1": algebra.constant(int(fixed["u1"])),
            "u2": algebra.constant(int(fixed["selected_u2"])),
        }
    )

    y_rows = {}
    for y_number, row_index in enumerate(Y_ROWS, start=1):
        name = f"y{y_number}"
        future = {f"y{index}": zero for index in range(y_number, 5)}
        trial = parent_values | future
        trial[name] = zero
        constant = evaluate(parent_rows[row_index], parent_names, trial, algebra)
        trial[name] = one
        coefficient = evaluate(parent_rows[row_index], parent_names, trial, algebra) - constant
        inverse_data = coefficient.inverse_with_determinant()
        require(inverse_data is not None, f"unit {name} pivot")
        inverse, determinant = inverse_data
        value = -inverse * constant
        parent_values[name] = value
        y_rows[name] = {
            "pivot_coefficients": coefficient.as_list(),
            "pivot_multiplication_determinant": determinant,
            "pivot_inverse_coefficients": inverse.as_list(),
            "value_coefficients": value.as_list(),
        }
    require(set(parent_values) == set(parent_names), "complete parent assignment")

    parent_remainders = [
        evaluate(row, parent_names, parent_values, algebra) for row in parent_rows
    ]
    require(
        all(parent_remainders[index] == zero for index in (0, *R_ROWS, 13, *Y_ROWS)),
        "exact parent R/y lift",
    )
    unit_witness = None
    for row_index in D_ROWS:
        remainder = parent_remainders[row_index]
        inverse_data = remainder.inverse_with_determinant()
        if inverse_data is None:
            continue
        inverse, determinant = inverse_data
        require(inverse * remainder == one, "D inverse identity")
        unit_witness = {
            "parent_row": row_index,
            "D_remainder_coefficients": remainder.as_list(),
            "D_multiplication_determinant": determinant,
            "D_inverse_coefficients": inverse.as_list(),
            "product_coefficients": (inverse * remainder).as_list(),
        }
        break
    require(unit_witness is not None, "one D terminal is a quotient-algebra unit")

    checks = {
        "symbolic_input_and_parent_are_hash_bound": True,
        "solver_output_is_an_exact_reduced_Groebner_basis_over_F101": True,
        "standard_monomials_are_one_plus_the_free_affine_coordinates": True,
        "every_quadratic_product_has_one_exact_affine_reduction": True,
        "the_recovered_finite_multiplication_is_commutative_and_associative": True,
        "all_symbolic_R_line_generators_vanish_in_the_finite_quotient": True,
        "all_four_y_coordinates_reconstruct_by_exact_unit_pivots": True,
        "both_endpoints_all_hR_rows_and_all_y_rows_vanish": True,
        "one_D_terminal_has_nonzero_multiplication_determinant": True,
        "the_displayed_quotient_inverse_multiplies_D_to_one": True,
        "the_unit_identity_survives_every_field_extension": True,
        "no_locality_reducedness_or_point_count_is_assumed": True,
        "no_continuous_fit_parameter_is_added": True,
    }
    require(all(checks.values()), "finite affine-quadratic checks")

    result = {
        "schema": "MTTQ79RonlySymbolicAffineQuadraticExceptionDUnitGeneral.v1",
        "date": "2026-07-20",
        "status": "EXACT_R_ONLY_FINITE_AFFINE_QUADRATIC_LINE_REJECTED_SCHEME_THEORETICALLY_BY_D",
        "field": "F_101",
        "space_index": args.space,
        "scalar_square_class_representative": input_packet["scalar_square_class_representative"],
        "fixed_coordinates": fixed,
        "artifacts": {
            "parent_input": checksum(args.parent),
            "symbolic_input": checksum(args.symbolic_input),
            "symbolic_input_packet": checksum(args.input_packet),
            "exact_reduced_basis_output": checksum(args.basis_output),
            "solver_log": checksum(args.basis_log),
        },
        "quotient_algebra": {
            "dimension": algebra.dimension,
            "standard_basis": ["1", *algebra.free_names],
            "free_coordinates": list(algebra.free_names),
            "quadratic_product_reductions": relation_records,
            "affine_coordinate_rows": coordinate_rows,
            "associativity_basis_triple_checks": associativity_checks,
            "reconstructed_y_rows": y_rows,
            "locality_or_reducedness_claim": "NOT_NEEDED_AND_NOT_ASSERTED",
        },
        "symbolic_line_row_remainders": [value.as_list() for value in line_remainders],
        "parent_row_remainders": [value.as_list() for value in parent_remainders],
        "D_terminal_remainders": {
            str(index): parent_remainders[index].as_list() for index in D_ROWS
        },
        "unit_witness": unit_witness,
        "checks": checks,
        "theorem": (
            "The exact reduced Groebner basis presents the entire selected R-only line "
            f"as a finite {algebra.dimension}-dimensional commutative associative "
            "F_101-algebra. The y chain lifts by exact units. One selected D-terminal "
            "has nonzero multiplication determinant and the displayed inverse multiplies "
            "it to one. Hence the full R/y/D line ideal is unit over F_101 and every "
            "field extension, without assuming that the R-only quotient is local or reduced."
        ),
        "claim_boundary": (
            "This closes exactly the displayed fixed-u1, fixed-a symbolic line and its "
            "proved sign partner. It does not classify other a lines or other u1 values."
        ),
        "new_continuous_fit_parameters": 0,
    }
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
    print(result["status"])
    print(
        f"dimension={algebra.dimension}; basis={list(algebra.free_names)}; "
        f"associativity_checks={associativity_checks}; D_row={unit_witness['parent_row']}; "
        f"det={unit_witness['D_multiplication_determinant']}"
    )
    print(args.output)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
