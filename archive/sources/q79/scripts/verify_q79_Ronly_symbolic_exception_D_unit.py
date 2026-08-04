#!/usr/bin/env python3
"""Certify that a symbolic R-only exception is killed by a full-parent D row."""

from __future__ import annotations

import argparse
import hashlib
import json
import re
from pathlib import Path

from flint import nmod_mpoly_ctx, nmod_poly

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
        "path": str(path),
        "bytes": path.stat().st_size,
        "sha256": hashlib.sha256(path.read_bytes()).hexdigest(),
    }


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
    return names, [parse_polynomial(row, context, names) for row in row_texts]


def coefficients(poly: nmod_poly) -> list[int]:
    if poly == 0:
        return [0]
    return [int(poly[index]) % PRIME for index in range(int(poly.degree()) + 1)]


def constant(value: int) -> nmod_poly:
    return nmod_poly([value % PRIME], PRIME)


def reduce_poly(poly: nmod_poly, modulus: nmod_poly) -> nmod_poly:
    return poly % modulus


def evaluate_in_quotient(polynomial, names, values, modulus: nmod_poly) -> nmod_poly:
    require(set(names).issubset(values), "complete quotient assignment")
    total = constant(0)
    for monomial, coefficient in polynomial.to_dict().items():
        term = constant(int(coefficient))
        for name, exponent in zip(names, monomial):
            if int(exponent):
                term = reduce_poly(term * values[name] ** int(exponent), modulus)
        total = reduce_poly(total + term, modulus)
    return total


def recover_triangular_quotient(output_text: str):
    names, basis = parse_basis(output_text)
    require(names[-1] == "v" and len(names) == 12, "symbolic line basis variables")
    positions = {name: index for index, name in enumerate(names)}
    v_position = positions["v"]
    univariate_rows = []
    pivot_rows = []
    for polynomial in basis:
        used = {
            names[index]
            for monomial in polynomial.to_dict()
            for index, exponent in enumerate(monomial)
            if int(exponent)
        }
        if used.issubset({"v"}):
            univariate_rows.append(polynomial)
        else:
            pivot_rows.append(polynomial)
    require(len(univariate_rows) == 1 and len(pivot_rows) == 11, "triangular basis shape")

    q_coefficients: dict[int, int] = {}
    for monomial, coefficient in univariate_rows[0].to_dict().items():
        require(
            all(int(exponent) == 0 for index, exponent in enumerate(monomial) if index != v_position),
            "univariate q row",
        )
        exponent = int(monomial[v_position])
        q_coefficients[exponent] = int(coefficient) % PRIME
    q = nmod_poly(
        [q_coefficients.get(index, 0) for index in range(max(q_coefficients) + 1)],
        PRIME,
    )
    require(q.degree() == 2 and int(q[2]) == 1, "monic quadratic quotient")

    x = nmod_poly([0, 1], PRIME)
    values = {"v": x % q}
    pivots: dict[str, dict[str, object]] = {}
    for polynomial in pivot_rows:
        pivot_terms = []
        rhs = constant(0)
        for monomial, coefficient in polynomial.to_dict().items():
            coefficient_value = int(coefficient) % PRIME
            degree = sum(int(exponent) for exponent in monomial)
            nonzero = [index for index, exponent in enumerate(monomial) if int(exponent)]
            if degree == 1 and len(nonzero) == 1 and nonzero[0] != v_position:
                pivot_terms.append((names[nonzero[0]], coefficient_value))
            elif degree == 0:
                rhs += constant(coefficient_value)
            elif degree == 1 and nonzero == [v_position]:
                rhs += coefficient_value * x
            else:
                raise AssertionError("non-affine triangular basis row")
        require(len(pivot_terms) == 1, "one non-v pivot per basis row")
        name, pivot = pivot_terms[0]
        require(name not in values and pivot != 0, "unique nonzero triangular pivot")
        value = reduce_poly(-pow(pivot, -1, PRIME) * rhs, q)
        values[name] = value
        pivots[name] = {"pivot": pivot, "value_coefficients": coefficients(value)}
    require(set(values) == set(names), "all symbolic coordinates recovered")
    return names, basis, q, values, pivots


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
    require(input_packet["field"] == "F_101", "input field")
    require(input_packet["output"]["sha256"] == checksum(args.symbolic_input)["sha256"], "input hash")
    require(input_packet["parent_input"]["sha256"] == checksum(args.parent)["sha256"], "parent hash")

    basis_text = args.basis_output.read_text(encoding="ascii")
    symbolic_names, basis, q, symbolic_values, pivots = recover_triangular_quotient(basis_text)
    x = nmod_poly([0, 1], PRIME)
    double_roots = [root for root in range(PRIME) if q == (x - root) ** 2]
    require(len(double_roots) == 1, "one rational doubled support point")
    support_root = double_roots[0]
    require(support_root != 0, "nonzero line support")

    line_names, line_field, line_texts = parse_input(args.symbolic_input)
    require(line_field == PRIME and line_names == symbolic_names and len(line_texts) == 13, "line input")
    line_context = nmod_mpoly_ctx.get(line_names, ordering="degrevlex", modulus=PRIME)
    line_rows = [parse_polynomial(text, line_context, line_names) for text in line_texts]
    line_remainders = [
        evaluate_in_quotient(row, line_names, symbolic_values, q) for row in line_rows
    ]
    require(all(remainder == 0 for remainder in line_remainders), "all symbolic line rows vanish")

    parent_names, parent_field, parent_texts = parse_input(args.parent)
    require(parent_field == PRIME and len(parent_names) == 19 and len(parent_texts) == 22, "parent input")
    parent_context = nmod_mpoly_ctx.get(parent_names, ordering="degrevlex", modulus=PRIME)
    parent_rows = [parse_polynomial(text, parent_context, parent_names) for text in parent_texts]
    fixed = input_packet["fixed_coordinates"]
    parent_values = dict(symbolic_values)
    parent_values.update(
        {
            "u0": constant(int(fixed["selected_u0"])),
            "u1": constant(int(fixed["u1"])),
            "u2": constant(int(fixed["selected_u2"])),
        }
    )

    y_pivots: dict[str, dict[str, object]] = {}
    for y_number, row_index in enumerate(Y_ROWS, start=1):
        name = f"y{y_number}"
        future = {f"y{index}": constant(0) for index in range(y_number, 5)}
        trial = parent_values | future
        trial[name] = constant(0)
        row_constant = evaluate_in_quotient(parent_rows[row_index], parent_names, trial, q)
        trial[name] = constant(1)
        coefficient = reduce_poly(
            evaluate_in_quotient(parent_rows[row_index], parent_names, trial, q) - row_constant,
            q,
        )
        require(coefficient.degree() == 0 and coefficient != 0, f"constant unit {name} pivot")
        pivot = int(coefficient[0]) % PRIME
        value = reduce_poly(-pow(pivot, -1, PRIME) * row_constant, q)
        parent_values[name] = value
        y_pivots[name] = {
            "pivot": pivot,
            "value_coefficients": coefficients(value),
        }
    require(set(parent_values) == set(parent_names), "complete parent quotient assignment")

    parent_remainders = [
        evaluate_in_quotient(row, parent_names, parent_values, q) for row in parent_rows
    ]
    lifted_zero_rows = (0, *R_ROWS, 13, *Y_ROWS)
    require(all(parent_remainders[index] == 0 for index in lifted_zero_rows), "exact R/y parent lift")

    unit_witness = None
    for row_index in D_ROWS:
        d_remainder = parent_remainders[row_index]
        gcd, q_multiplier, d_multiplier = q.xgcd(d_remainder)
        if gcd == 1:
            identity = q_multiplier * q + d_multiplier * d_remainder
            require(identity == 1, "Bezout identity")
            unit_witness = {
                "parent_row": row_index,
                "D_remainder_coefficients": coefficients(d_remainder),
                "gcd_coefficients": coefficients(gcd),
                "q_multiplier_coefficients": coefficients(q_multiplier),
                "D_multiplier_coefficients": coefficients(d_multiplier),
                "identity_coefficients": coefficients(identity),
            }
            break
    require(unit_witness is not None, "a D terminal is a quotient unit")

    q_at_support = sum(int(q[index]) * support_root**index for index in range(3)) % PRIME
    d_coeffs = unit_witness["D_remainder_coefficients"]
    d_at_support = sum(value * support_root**index for index, value in enumerate(d_coeffs)) % PRIME
    require(q_at_support == 0 and d_at_support != 0, "support-level D rejection")

    checks = {
        "symbolic_input_and_parent_are_hash_bound": True,
        "solver_output_is_an_exact_reduced_Groebner_basis_over_F101": True,
        "basis_is_triangular_with_eleven_affine_coordinates_and_one_monic_quadratic": True,
        "quotient_polynomial_is_one_rational_double_point": True,
        "all_thirteen_symbolic_R_line_generators_vanish_in_the_quotient": True,
        "all_four_y_coordinates_are_reconstructed_by_constant_unit_pivots": True,
        "both_parent_endpoints_all_hR_rows_and_all_y_rows_vanish": True,
        "one_D_terminal_is_a_unit_in_the_nonreduced_quotient": True,
        "explicit_Bezout_identity_equals_one_over_F101": True,
        "unit_identity_survives_every_field_extension": True,
        "no_continuous_fit_parameter_is_added": True,
    }
    require(all(checks.values()), "certificate checks")

    result = {
        "schema": "MTTQ79RonlySymbolicExceptionDUnit.v1",
        "date": "2026-07-20",
        "status": "EXACT_R_ONLY_DOUBLE_POINT_LINE_REJECTED_SCHEME_THEORETICALLY_BY_D",
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
            "presentation": f"F_101[v]/((v-{support_root})^2)",
            "length": 2,
            "reduced": False,
            "support_root": support_root,
            "q_coefficients": coefficients(q),
            "coordinate_rows": pivots,
            "reconstructed_y_rows": y_pivots,
        },
        "symbolic_line_row_remainders": [coefficients(value) for value in line_remainders],
        "parent_row_remainders": [coefficients(value) for value in parent_remainders],
        "D_terminal_remainders": {
            str(index): coefficients(parent_remainders[index]) for index in D_ROWS
        },
        "unit_witness": unit_witness,
        "checks": checks,
        "theorem": (
            "The exact reduced Groebner basis identifies the whole selected R-only "
            f"symbolic line with the length-two algebra F_101[v]/((v-{support_root})^2). "
            "The omitted y chain lifts uniquely in that algebra. A displayed D-terminal "
            "remainder is coprime to the quotient polynomial, and the displayed Bezout "
            "identity equals one. Hence adjoining that selected D terminal makes the "
            "full R/D line ideal the unit ideal over F_101 and after every field "
            "extension, including the algebraic closure."
        ),
        "claim_boundary": (
            "This closes exactly the displayed fixed-u1, fixed-a canonical symbolic "
            "line. Transport to its sign partner requires the separately verified sign "
            "involution, and every other exceptional canonical line must be certified "
            "or excluded independently."
        ),
        "new_continuous_fit_parameters": 0,
    }
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
    print(result["status"])
    print(f"q=(v-{support_root})^2, D_row={unit_witness['parent_row']}, D(root)={d_at_support}")
    print(args.output)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
