#!/usr/bin/env python3
"""Certify D rejection in a general finite q79 Groebner line quotient."""

from __future__ import annotations

import argparse
import hashlib
import json
import re
from collections import deque
from pathlib import Path

from flint import nmod_mpoly_ctx

from build_q79_D10_D6_h1_g1_pair_quotient_obstructions import (
    PRIME,
    parse_input,
    parse_polynomial,
)
from verify_q79_Ronly_symbolic_affine_quadratic_exception_D_unit_general import (
    determinant_mod,
    parse_basis,
    solve_square,
)


ROOT = Path(__file__).resolve().parents[1]
SOLVER_BASELINE = ROOT / "certificates" / "Q79_Ronly_U1_002_Space5_Symbolic_U2_Prefix_v1.json"
R_ROWS = tuple(range(1, 13))
Y_ROWS = tuple(range(14, 18))
D_ROWS = tuple(range(18, 22))


def require(condition: bool, label: str) -> None:
    if not condition:
        raise AssertionError(label)


def checksum(path: Path) -> dict[str, object]:
    resolved = path.resolve()
    try:
        label = resolved.relative_to(ROOT).as_posix()
    except ValueError:
        label = resolved.as_posix()
    return {
        "path": label,
        "bytes": path.stat().st_size,
        "sha256": hashlib.sha256(path.read_bytes()).hexdigest(),
    }


def monomial_key(monomial: tuple[int, ...]) -> tuple[int, tuple[int, ...]]:
    return sum(monomial), tuple(-value for value in reversed(monomial))


def divides(monomial: tuple[int, ...], divisor: tuple[int, ...]) -> bool:
    return all(left >= right for left, right in zip(monomial, divisor))


def monomial_label(names: tuple[str, ...], monomial: tuple[int, ...]) -> str:
    factors = []
    for name, exponent in zip(names, monomial):
        if exponent == 1:
            factors.append(name)
        elif exponent > 1:
            factors.append(f"{name}^{exponent}")
    return "*".join(factors) or "1"


class FiniteGroebnerAlgebra:
    def __init__(self, names: tuple[str, ...], basis) -> None:
        self.names = names
        self.variable_count = len(names)
        self.basis_terms = []
        self.leading_monomials = []
        for row in basis:
            terms = {
                tuple(int(value) for value in monomial): int(coefficient) % PRIME
                for monomial, coefficient in row.to_dict().items()
            }
            require(terms, "nonzero basis row")
            leading = max(terms, key=monomial_key)
            require(
                leading == tuple(int(value) for value in row.monoms()[0])
                and terms[leading] == 1,
                "monic degrevlex leading monomial",
            )
            self.basis_terms.append(terms)
            self.leading_monomials.append(leading)
        require(
            len(set(self.leading_monomials)) == len(self.leading_monomials),
            "unique leading monomials",
        )
        for leading, terms in zip(self.leading_monomials, self.basis_terms):
            for monomial in terms:
                if monomial == leading:
                    continue
                require(
                    not any(divides(monomial, divisor) for divisor in self.leading_monomials),
                    "reduced Groebner tail",
                )

        origin = (0,) * self.variable_count
        standard = {origin}
        queue = deque([origin])
        while queue:
            monomial = queue.popleft()
            for position in range(self.variable_count):
                candidate = list(monomial)
                candidate[position] += 1
                value = tuple(candidate)
                if value in standard or any(
                    divides(value, divisor) for divisor in self.leading_monomials
                ):
                    continue
                standard.add(value)
                queue.append(value)
                require(len(standard) <= 4096, "finite standard-monomial guard")
        self.standard_monomials = tuple(sorted(standard, key=monomial_key))
        self.index = {monomial: index for index, monomial in enumerate(self.standard_monomials)}
        self.dimension = len(self.standard_monomials)
        require(self.dimension > 0, "positive quotient dimension")

        self.products: list[list[tuple[int, ...]]] = [
            [tuple() for _ in range(self.dimension)] for _ in range(self.dimension)
        ]
        for left, left_monomial in enumerate(self.standard_monomials):
            for right in range(left, self.dimension):
                right_monomial = self.standard_monomials[right]
                product = tuple(
                    a + b for a, b in zip(left_monomial, right_monomial)
                )
                value = self.normal_form_terms({product: 1})
                self.products[left][right] = self.products[right][left] = value

    def normal_form_terms(self, source: dict[tuple[int, ...], int]) -> tuple[int, ...]:
        work = {
            monomial: coefficient % PRIME
            for monomial, coefficient in source.items()
            if coefficient % PRIME
        }
        remainder: dict[tuple[int, ...], int] = {}
        while work:
            monomial = max(work, key=monomial_key)
            coefficient = work.pop(monomial) % PRIME
            reducer = next(
                (
                    index
                    for index, leading in enumerate(self.leading_monomials)
                    if divides(monomial, leading)
                ),
                None,
            )
            if reducer is None:
                remainder[monomial] = (
                    remainder.get(monomial, 0) + coefficient
                ) % PRIME
                if remainder[monomial] == 0:
                    del remainder[monomial]
                continue
            leading = self.leading_monomials[reducer]
            shift = tuple(left - right for left, right in zip(monomial, leading))
            for basis_monomial, basis_coefficient in self.basis_terms[reducer].items():
                if basis_monomial == leading:
                    continue
                target = tuple(
                    left + right for left, right in zip(basis_monomial, shift)
                )
                work[target] = (
                    work.get(target, 0) - coefficient * basis_coefficient
                ) % PRIME
                if work[target] == 0:
                    del work[target]
        require(all(monomial in self.index for monomial in remainder), "standard remainder")
        vector = [0] * self.dimension
        for monomial, coefficient in remainder.items():
            vector[self.index[monomial]] = coefficient
        return tuple(vector)

    def normal_form(self, polynomial) -> tuple[int, ...]:
        return self.normal_form_terms({
            tuple(int(value) for value in monomial): int(coefficient) % PRIME
            for monomial, coefficient in polynomial.to_dict().items()
        })

    def zero(self) -> tuple[int, ...]:
        return (0,) * self.dimension

    def one(self) -> tuple[int, ...]:
        return (1, *([0] * (self.dimension - 1)))

    def constant(self, value: int) -> tuple[int, ...]:
        return (value % PRIME, *([0] * (self.dimension - 1)))

    def basis_vector(self, index: int) -> tuple[int, ...]:
        return tuple(int(position == index) for position in range(self.dimension))

    def generator(self, name: str) -> tuple[int, ...]:
        position = self.names.index(name)
        monomial = tuple(int(index == position) for index in range(self.variable_count))
        return self.normal_form_terms({monomial: 1})

    def add(self, left, right) -> tuple[int, ...]:
        return tuple((a + b) % PRIME for a, b in zip(left, right))

    def negative(self, value) -> tuple[int, ...]:
        return tuple(-coefficient % PRIME for coefficient in value)

    def subtract(self, left, right) -> tuple[int, ...]:
        return self.add(left, self.negative(right))

    def scale(self, scalar: int, value) -> tuple[int, ...]:
        return tuple(scalar * coefficient % PRIME for coefficient in value)

    def multiply(self, left, right) -> tuple[int, ...]:
        result = [0] * self.dimension
        for i, a in enumerate(left):
            if a == 0:
                continue
            for j, b in enumerate(right):
                if b == 0:
                    continue
                factor = a * b % PRIME
                result = [
                    (value + factor * coefficient) % PRIME
                    for value, coefficient in zip(result, self.products[i][j])
                ]
        return tuple(result)

    def power(self, value, exponent: int) -> tuple[int, ...]:
        require(exponent >= 0, "nonnegative exponent")
        result = self.one()
        base = value
        while exponent:
            if exponent & 1:
                result = self.multiply(result, base)
            base = self.multiply(base, base)
            exponent >>= 1
        return result

    def inverse_with_determinant(self, value):
        columns = [
            self.multiply(value, self.basis_vector(index))
            for index in range(self.dimension)
        ]
        matrix = [
            [columns[column][row] for column in range(self.dimension)]
            for row in range(self.dimension)
        ]
        determinant = determinant_mod(matrix)
        if determinant == 0:
            return None
        solution = solve_square(matrix, list(self.one()))
        require(solution is not None, "unit linear solve")
        inverse = tuple(solution)
        require(self.multiply(value, inverse) == self.one(), "unit inverse identity")
        return inverse, determinant

    def verify_associativity(self) -> int:
        checks = 0
        basis = [self.basis_vector(index) for index in range(self.dimension)]
        for left in basis:
            for middle in basis:
                for right in basis:
                    require(
                        self.multiply(self.multiply(left, middle), right)
                        == self.multiply(left, self.multiply(middle, right)),
                        "finite quotient associativity",
                    )
                    checks += 1
        return checks

    def verify_buchberger(self) -> dict[str, int]:
        product_criterion = 0
        explicit_reductions = 0
        for left in range(len(self.basis_terms)):
            for right in range(left + 1, len(self.basis_terms)):
                left_leading = self.leading_monomials[left]
                right_leading = self.leading_monomials[right]
                if not any(a and b for a, b in zip(left_leading, right_leading)):
                    product_criterion += 1
                    continue
                least_common_multiple = tuple(
                    max(a, b) for a, b in zip(left_leading, right_leading)
                )
                s_polynomial: dict[tuple[int, ...], int] = {}
                for monomial, coefficient in self.basis_terms[left].items():
                    target = tuple(
                        value + common - leading
                        for value, common, leading in zip(
                            monomial, least_common_multiple, left_leading
                        )
                    )
                    s_polynomial[target] = (
                        s_polynomial.get(target, 0) + coefficient
                    ) % PRIME
                for monomial, coefficient in self.basis_terms[right].items():
                    target = tuple(
                        value + common - leading
                        for value, common, leading in zip(
                            monomial, least_common_multiple, right_leading
                        )
                    )
                    s_polynomial[target] = (
                        s_polynomial.get(target, 0) - coefficient
                    ) % PRIME
                s_polynomial = {
                    monomial: coefficient
                    for monomial, coefficient in s_polynomial.items()
                    if coefficient
                }
                require(
                    self.normal_form_terms(s_polynomial) == self.zero(),
                    "Buchberger S-pair reduction",
                )
                explicit_reductions += 1
        total = product_criterion + explicit_reductions
        require(
            total == len(self.basis_terms) * (len(self.basis_terms) - 1) // 2,
            "complete S-pair accounting",
        )
        return {
            "total_pairs": total,
            "product_criterion_pairs": product_criterion,
            "explicit_zero_reductions": explicit_reductions,
        }

    def multiplication_table_sha256(self) -> str:
        upper = [
            list(self.products[left][right])
            for left in range(self.dimension)
            for right in range(left, self.dimension)
        ]
        payload = json.dumps(upper, separators=(",", ":")).encode("ascii")
        return hashlib.sha256(payload).hexdigest()


def evaluate(polynomial, names, values, algebra: FiniteGroebnerAlgebra):
    require(set(names).issubset(values), "complete quotient assignment")
    result = algebra.zero()
    for monomial, coefficient in polynomial.to_dict().items():
        term = algebra.constant(int(coefficient))
        for name, exponent in zip(names, monomial):
            if int(exponent):
                term = algebra.multiply(term, algebra.power(values[name], int(exponent)))
        result = algebra.add(result, term)
    return result


def validate_solver_log(path: Path) -> None:
    text = path.read_text(encoding="utf-8").replace("\r\n", "\n")
    required = (
        r"field characteristic\s+101",
        r"monomial order\s+DRL",
        r"#threads\s+1",
        r"reduce gb\s+1",
        r"#invalid equations\s+0",
        r"msolve overall time",
    )
    require(all(re.search(pattern, text) for pattern in required), "exact solver log")


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--parent", type=Path, required=True)
    parser.add_argument("--family-packet", type=Path, required=True)
    parser.add_argument("--source-input", type=Path, required=True)
    parser.add_argument("--basis-output", type=Path, required=True)
    parser.add_argument("--basis-log", type=Path, required=True)
    parser.add_argument("--space", type=int, choices=(5, 6), required=True)
    parser.add_argument("--u1", type=int, required=True)
    parser.add_argument("--u2", type=int, required=True)
    parser.add_argument("--scalar-class", type=int, choices=(1, 2), required=True)
    parser.add_argument("--a", type=int, required=True)
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()

    u1 = args.u1 % PRIME
    u2 = args.u2 % PRIME
    scalar_class = args.scalar_class % PRIME
    a_value = args.a % PRIME
    require(u1 and u2 and a_value, "nonzero selected coordinates")
    u0 = pow(u1, -2, PRIME)
    require(
        u2 == scalar_class * pow(a_value, -2, PRIME) % PRIME,
        "canonical u2/class/a relation",
    )

    family = json.loads(args.family_packet.read_text(encoding="utf-8"))
    require(
        family.get("status") == "EXACT_100_NONZERO_U2_SYMBOLIC_INPUTS_EMITTED"
        and family.get("space_index") == args.space
        and family.get("fixed_u1") == u1,
        "symbolic family",
    )
    record = family["records"][u2 - 1]
    require(
        record.get("u2") == u2
        and record.get("input", {}).get("sha256") == checksum(args.source_input)["sha256"],
        "family line binding",
    )

    baseline = json.loads(SOLVER_BASELINE.read_text(encoding="utf-8"))
    provenance = baseline.get("solver_provenance", {})
    require(
        provenance.get("engine") == "msolve 0.10.1"
        and provenance.get("binary_sha256")
        == "a4c2beb9a7d186394af6bb21e235f76e3bfb3d0e6fdf872c27b517b8a6e87e13",
        "solver provenance",
    )
    validate_solver_log(args.basis_log)

    line_names, line_field, line_texts = parse_input(args.source_input)
    require(
        line_field == PRIME and len(line_names) == 12 and line_names[-1] == "t"
        and len(line_texts) == 13,
        "source symbolic line",
    )
    line_context = nmod_mpoly_ctx.get(line_names, ordering="degrevlex", modulus=PRIME)
    line_rows = [parse_polynomial(text, line_context, line_names) for text in line_texts]
    line_generators = dict(zip(line_names, line_context.gens()))
    require(
        line_rows[-1] == line_generators["u3"] * line_generators["t"] - 1,
        "source Laurent saturation",
    )

    basis_names, _, basis_rows = parse_basis(args.basis_output.read_text(encoding="ascii"))
    require(basis_names == line_names and basis_rows, "basis variable order")
    algebra = FiniteGroebnerAlgebra(line_names, basis_rows)
    buchberger = algebra.verify_buchberger()
    line_values = {name: algebra.generator(name) for name in line_names}
    line_remainders = [algebra.normal_form(row) for row in line_rows]
    require(all(value == algebra.zero() for value in line_remainders), "line rows vanish")
    associativity_checks = algebra.verify_associativity()

    parent_names, parent_field, parent_texts = parse_input(args.parent)
    require(
        parent_field == PRIME and len(parent_names) == 19 and len(parent_texts) == 22,
        "parent input",
    )
    parent_context = nmod_mpoly_ctx.get(parent_names, ordering="degrevlex", modulus=PRIME)
    parent_rows = [parse_polynomial(text, parent_context, parent_names) for text in parent_texts]
    parent_generators = dict(zip(parent_names, parent_context.gens()))
    require(
        parent_rows[0] == parent_generators["u0"] * parent_generators["u1"] ** 2 - 1
        and parent_rows[13]
        == parent_generators["v"] ** 2
        * parent_generators["u2"]
        * parent_generators["u3"] ** 2
        - scalar_class,
        "selected parent endpoints",
    )

    composition = []
    assignments = {"u0": u0, "u1": u1, "u2": u2}
    for name in parent_names:
        if name in assignments:
            composition.append(line_context.constant(assignments[name]))
        elif name in line_generators:
            composition.append(line_generators[name])
        else:
            composition.append(line_context.constant(0))
    restricted_R = [
        parent_rows[index].compose(*composition, ctx=line_context) for index in R_ROWS
    ]
    require(restricted_R == line_rows[:12], "same-source parent R restriction")

    parent_values = {name: line_values[name] for name in line_names if name != "t"}
    parent_values.update({
        "u0": algebra.constant(u0),
        "u1": algebra.constant(u1),
        "u2": algebra.constant(u2),
        "v": algebra.scale(a_value, line_values["t"]),
    })
    require(
        algebra.multiply(parent_values["v"], parent_values["u3"])
        == algebra.constant(a_value),
        "two-sided Laurent coordinate relation",
    )

    reconstructed_y = {}
    for y_number, row_index in enumerate(Y_ROWS, start=1):
        name = f"y{y_number}"
        future = {f"y{index}": algebra.zero() for index in range(y_number, 5)}
        trial = parent_values | future
        trial[name] = algebra.zero()
        constant = evaluate(parent_rows[row_index], parent_names, trial, algebra)
        trial[name] = algebra.one()
        coefficient = algebra.subtract(
            evaluate(parent_rows[row_index], parent_names, trial, algebra), constant
        )
        inverse_data = algebra.inverse_with_determinant(coefficient)
        require(inverse_data is not None, f"unit {name} pivot")
        inverse, determinant = inverse_data
        value = algebra.negative(algebra.multiply(inverse, constant))
        parent_values[name] = value
        reconstructed_y[name] = {
            "pivot_coefficients": list(coefficient),
            "pivot_multiplication_determinant": determinant,
            "pivot_inverse_coefficients": list(inverse),
            "value_coefficients": list(value),
        }
    require(set(parent_values) == set(parent_names), "complete parent assignment")

    parent_remainders = [
        evaluate(row, parent_names, parent_values, algebra) for row in parent_rows
    ]
    require(
        all(parent_remainders[index] == algebra.zero() for index in (0, *R_ROWS, 13, *Y_ROWS)),
        "exact parent R/y lift",
    )
    D_data = {}
    unit_witness = None
    for row_index in D_ROWS:
        remainder = parent_remainders[row_index]
        inverse_data = algebra.inverse_with_determinant(remainder)
        D_data[str(row_index)] = {
            "remainder_coefficients": list(remainder),
            "multiplication_determinant": 0 if inverse_data is None else inverse_data[1],
            "is_unit": inverse_data is not None,
        }
        if inverse_data is not None and unit_witness is None:
            inverse, determinant = inverse_data
            product = algebra.multiply(remainder, inverse)
            require(product == algebra.one(), "D unit product")
            unit_witness = {
                "parent_row": row_index,
                "D_remainder_coefficients": list(remainder),
                "D_multiplication_determinant": determinant,
                "D_inverse_coefficients": list(inverse),
                "product_coefficients": list(product),
            }
    require(unit_witness is not None, "one selected D terminal is a unit")

    checks = {
        "parent_family_input_basis_log_and_solver_provenance_are_hash_bound": True,
        "family_line_has_the_selected_u1_u2_coordinates": True,
        "parent_R_rows_restrict_exactly_to_the_symbolic_line_rows": True,
        "solver_basis_is_monic_reduced_and_zero_dimensional": True,
        "all_Buchberger_pairs_pass_by_the_product_criterion_or_exact_zero_reduction": True,
        "standard_monomials_are_enumerated_from_the_leading_ideal": True,
        "all_symbolic_line_rows_reduce_to_zero": True,
        "the_t_to_v_Laurent_coordinate_map_is_exact_and_invertible": True,
        "the_finite_multiplication_table_is_commutative_and_associative": True,
        "all_four_y_coordinates_reconstruct_by_exact_unit_pivots": True,
        "both_endpoints_all_R_rows_and_all_y_rows_vanish": True,
        "one_selected_D_terminal_has_nonzero_multiplication_determinant": True,
        "the_displayed_D_inverse_multiplies_to_one": True,
        "the_unit_identity_survives_every_field_extension": True,
        "no_locality_reducedness_or_point_count_is_assumed": True,
        "no_continuous_fit_parameter_is_added": True,
    }
    require(all(checks.values()), "finite Groebner quotient checks")
    result = {
        "schema": "MTTQ79RonlySymbolicFiniteGroebnerExceptionDUnit.v1",
        "date": "2026-07-21",
        "status": "EXACT_R_ONLY_FINITE_GROEBNER_LINE_REJECTED_SCHEME_THEORETICALLY_BY_D",
        "field": "F_101",
        "space_index": args.space,
        "scalar_square_class_representative": scalar_class,
        "fixed_coordinates": {
            "u1": u1,
            "a_equals_v_times_u3": a_value,
            "selected_u0": u0,
            "selected_u2": u2,
        },
        "coordinate_isomorphism": {
            "source_relation": "t*u3-1",
            "parent_assignment": f"v={a_value}*t",
            "canonical_relation": f"v*u3-{a_value}",
            "inverse_assignment": f"t={pow(a_value, -1, PRIME)}*v",
        },
        "artifacts": {
            "parent_input": checksum(args.parent),
            "symbolic_family": checksum(args.family_packet),
            "symbolic_input": checksum(args.source_input),
            "exact_reduced_basis_output": checksum(args.basis_output),
            "solver_log": checksum(args.basis_log),
            "solver_provenance_baseline": checksum(SOLVER_BASELINE),
        },
        "solver_provenance": provenance,
        "quotient_algebra": {
            "dimension": algebra.dimension,
            "reduced_basis_rows": len(basis_rows),
            "standard_basis": [
                monomial_label(line_names, monomial)
                for monomial in algebra.standard_monomials
            ],
            "standard_monomial_exponents": [
                list(monomial) for monomial in algebra.standard_monomials
            ],
            "leading_monomial_count": len(algebra.leading_monomials),
            "Buchberger_pair_certificate": buchberger,
            "basis_product_rows": algebra.dimension * (algebra.dimension + 1) // 2,
            "basis_product_table_sha256": algebra.multiplication_table_sha256(),
            "associativity_basis_triple_checks": associativity_checks,
            "reconstructed_y_rows": reconstructed_y,
            "locality_or_reducedness_claim": "NOT_NEEDED_AND_NOT_ASSERTED",
        },
        "symbolic_line_row_remainders": [list(value) for value in line_remainders],
        "parent_row_remainders": [list(value) for value in parent_remainders],
        "D_terminal_data": D_data,
        "unit_witness": unit_witness,
        "checks": checks,
        "theorem": (
            "The exact reduced Groebner basis presents the entire selected R-only "
            f"line as a finite {algebra.dimension}-dimensional commutative associative "
            "F_101-algebra. The same parent R rows restrict to the line, the y chain "
            "lifts by exact units, and a selected D terminal has an explicit inverse. "
            "Hence the full R/y/D line ideal is unit over F_101 and every extension."
        ),
        "claim_boundary": (
            "This closes exactly the displayed fixed-u1, fixed-u2 symbolic line. It "
            "does not classify another line, another u1 value, characteristic zero, "
            "either mirror zero-zero chart, or physical HYM/QG data."
        ),
        "new_continuous_fit_parameters": 0,
    }
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
    print(result["status"])
    print(
        f"dimension={algebra.dimension}; basis_rows={len(basis_rows)}; "
        f"associativity_checks={associativity_checks}; "
        f"D_row={unit_witness['parent_row']}; "
        f"det={unit_witness['D_multiplication_determinant']}"
    )
    print(args.output)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
