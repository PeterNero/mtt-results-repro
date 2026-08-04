#!/usr/bin/env python3
"""Eliminate the h1/g1 triangular roots inside the exact pair quotient."""

from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path

from flint import nmod_mpoly, nmod_mpoly_ctx


ROOT = Path(__file__).resolve().parent
PRIME = 101
PAIR_NAMES = tuple(f"u{index}" for index in range(8))
FULL_NAMES = ("g2", "g3", "g4", *PAIR_NAMES)
TRIANGULAR_ROWS = (5, 6, 7)
CONSISTENCY_ROWS = (8, 9, 10)
INVERSE_TWO = pow(2, -1, PRIME)


def require(condition: bool, label: str) -> None:
    if not condition:
        raise AssertionError(label)


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def checksum(path: Path) -> dict[str, str]:
    return {"path": str(path), "sha256": sha256(path)}


def normalized_text(path: Path) -> str:
    return path.read_text(encoding="ascii").replace("\r\n", "\n")


def parse_input(path: Path) -> tuple[tuple[str, ...], int, list[str]]:
    lines = normalized_text(path).splitlines()
    return (
        tuple(lines[0].split(",")),
        int(lines[1]),
        [line.removesuffix(",") for line in lines[2:] if line],
    )


def parse_polynomial(
    text: str, context: nmod_mpoly_ctx, names: tuple[str, ...]
) -> nmod_mpoly:
    value = text.strip().lstrip("[").rstrip(",]:")
    positions = {name: index for index, name in enumerate(names)}
    coefficients: dict[tuple[int, ...], int] = {}
    for raw_term in value.split("+"):
        factors = raw_term.strip().split("*")
        first_is_coefficient = factors[0].isdigit()
        coefficient = int(factors[0]) % PRIME if first_is_coefficient else 1
        exponents = [0] * len(names)
        for factor in factors[1 if first_is_coefficient else 0 :]:
            if "^" in factor:
                name, exponent_text = factor.split("^", 1)
                exponent = int(exponent_text)
            else:
                name, exponent = factor, 1
            require(name in positions, f"known variable {name}")
            exponents[positions[name]] += exponent
        monomial = tuple(exponents)
        coefficients[monomial] = (
            coefficients.get(monomial, 0) + coefficient
        ) % PRIME
    return context.from_dict(
        {monomial: coefficient for monomial, coefficient in coefficients.items() if coefficient}
    )


def parse_groebner(
    path: Path, context: nmod_mpoly_ctx
) -> tuple[list[nmod_mpoly], int]:
    lines = normalized_text(path).splitlines()
    require(lines[0] == "#Reduced Groebner basis data", "Groebner header")
    require("#field characteristic: 101" in lines, "Groebner field")
    variable_line = next(line for line in lines if line.startswith("#variable order:"))
    variables = tuple(
        value.strip() for value in variable_line.split(":", 1)[1].split(",")
    )
    require(variables == PAIR_NAMES, "Groebner variable order")
    require(
        any("graded reverse lexicographical" in line for line in lines),
        "Groebner ordering",
    )
    length_line = next(line for line in lines if line.startswith("#length of basis:"))
    basis_length = int(length_line.split(":", 1)[1].split()[0])
    rows = [line for line in lines if line and not line.startswith("#")]
    require(len(rows) == basis_length, "Groebner basis length")
    return [parse_polynomial(row, context, PAIR_NAMES) for row in rows], basis_length


def normal_form(
    polynomial: nmod_mpoly, basis: list[nmod_mpoly]
) -> tuple[nmod_mpoly, int]:
    rounds = 0
    while True:
        before = polynomial
        for divisor in basis:
            polynomial %= divisor
        rounds += 1
        if polynomial == before:
            return polynomial, rounds
        require(rounds <= 20, "normal-form reduction terminates")


def leading_monomial(polynomial: nmod_mpoly) -> tuple[int, ...]:
    require(not polynomial.is_zero(), "nonzero basis polynomial")
    return tuple(int(value) for value in polynomial.monomial(0))


def is_irreducible(
    polynomial: nmod_mpoly, leading_monomials: list[tuple[int, ...]]
) -> bool:
    return all(
        not any(
            all(value >= divisor for value, divisor in zip(monomial, leading))
            for leading in leading_monomials
        )
        for monomial in polynomial.to_dict()
    )


def polynomial_record(polynomial: nmod_mpoly) -> dict:
    text = str(polynomial)
    monomials = polynomial.to_dict()
    return {
        "sha256": hashlib.sha256(text.encode("ascii")).hexdigest(),
        "terms": len(monomials),
        "total_degree": int(polynomial.total_degree()),
        "degree_support": sorted({int(sum(monomial)) for monomial in monomials}),
    }


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--space", type=int, choices=(5, 6), required=True)
    args = parser.parse_args()
    space = args.space

    stem = f"space_{space}_h1_g1_forced_low_plus_d_normalized_active"
    active_path = ROOT / "generated_q79_D10_D6_interior_subset_cores" / f"{stem}.msolve.in"
    active_manifest_path = active_path.with_suffix(".manifest.json")
    pair_path = active_path.with_name(f"{stem}_pair5.msolve.in")
    pair_manifest_path = pair_path.with_suffix(".manifest.json")
    groebner_path = active_path.with_name(f"space_{space}_h1_g1_pair5.groebner.out")
    output_path = active_path.with_name(
        f"space_{space}_h1_g1_pair_quotient_obstructions.msolve.in"
    )
    manifest_path = output_path.with_suffix(".manifest.json")

    active_manifest = json.loads(active_manifest_path.read_text(encoding="utf-8"))
    pair_manifest = json.loads(pair_manifest_path.read_text(encoding="utf-8"))
    require(all(active_manifest["checks"].values()), "active transformation checks")
    require(all(pair_manifest["checks"].values()), "pair transformation checks")
    require(active_manifest["output"]["normalized_ascii_sha256"] == hashlib.sha256(normalized_text(active_path).encode("ascii")).hexdigest(), "active hash")
    require(pair_manifest["output"]["normalized_ascii_sha256"] == hashlib.sha256(normalized_text(pair_path).encode("ascii")).hexdigest(), "pair hash")

    full_context = nmod_mpoly_ctx.get(FULL_NAMES, ordering="degrevlex", modulus=PRIME)
    pair_context = nmod_mpoly_ctx.get(PAIR_NAMES, ordering="degrevlex", modulus=PRIME)
    pair_generators = pair_context.gens()
    zero = pair_context.constant(0)

    active_names, active_field, active_texts = parse_input(active_path)
    pair_names, pair_field, pair_texts = parse_input(pair_path)
    require(active_names == FULL_NAMES and active_field == PRIME, "active ring")
    require(pair_names == PAIR_NAMES and pair_field == PRIME, "pair ring")
    require(len(active_texts) == 11 and len(pair_texts) == 5, "equation counts")
    require(pair_texts == active_texts[:5], "five literal pair generators")

    active_polynomials = [
        parse_polynomial(text, full_context, FULL_NAMES) for text in active_texts
    ]
    pair_polynomials = [
        parse_polynomial(text, pair_context, PAIR_NAMES) for text in pair_texts
    ]
    basis, basis_length = parse_groebner(groebner_path, pair_context)
    require(basis_length == 76, "expected pair basis length")
    leading_monomials = [leading_monomial(polynomial) for polynomial in basis]

    pair_reduction_rounds = []
    for polynomial in pair_polynomials:
        remainder, rounds = normal_form(polynomial, basis)
        require(remainder.is_zero(), "pair generator reduces to zero")
        pair_reduction_rounds.append(rounds)

    root_solutions: list[nmod_mpoly] = []
    root_records = []
    triangular_rounds = []
    for row_index, target_position in zip(TRIANGULAR_ROWS, range(3)):
        source_terms = active_polynomials[row_index].to_dict()
        target_terms = [
            (monomial, coefficient)
            for monomial, coefficient in source_terms.items()
            if monomial[target_position]
        ]
        expected_target = tuple(
            1 if index == target_position else 0 for index in range(len(FULL_NAMES))
        )
        require(target_terms == [(expected_target, PRIME - 2)], "constant minus-two pivot")

        zero_target_mapping = [
            *root_solutions,
            *([zero] * (3 - len(root_solutions))),
            *pair_generators,
        ]
        constant_part = active_polynomials[row_index].compose(
            *zero_target_mapping, ctx=pair_context
        )
        constant_remainder, rounds = normal_form(constant_part, basis)
        solution = constant_remainder * INVERSE_TWO
        require(is_irreducible(solution, leading_monomials), "root solution normal form")
        root_solutions.append(solution)
        triangular_rounds.append(rounds)

        solved_mapping = [
            *root_solutions,
            *([zero] * (3 - len(root_solutions))),
            *pair_generators,
        ]
        solved_row = active_polynomials[row_index].compose(
            *solved_mapping, ctx=pair_context
        )
        solved_remainder, _ = normal_form(solved_row, basis)
        require(solved_remainder.is_zero(), "triangular row reconstructs exactly")
        root_records.append(polynomial_record(solution))

    consistency_remainders = []
    consistency_records = []
    consistency_rounds = []
    complete_mapping = [*root_solutions, *pair_generators]
    for row_index in CONSISTENCY_ROWS:
        substituted = active_polynomials[row_index].compose(
            *complete_mapping, ctx=pair_context
        )
        remainder, rounds = normal_form(substituted, basis)
        require(not remainder.is_zero(), "nontrivial consistency obstruction")
        require(is_irreducible(remainder, leading_monomials), "consistency normal form")
        consistency_remainders.append(remainder)
        consistency_records.append(polynomial_record(remainder))
        consistency_rounds.append(rounds)

    output_equations = [*pair_texts, *(str(value) for value in consistency_remainders)]
    output_text = (
        ",".join(PAIR_NAMES)
        + "\n"
        + str(PRIME)
        + "\n"
        + ",\n".join(output_equations)
        + "\n"
    )
    output_path.write_text(output_text, encoding="ascii")

    checks = {
        "active_and_pair_transformation_manifests_pass": True,
        "five_pair_rows_are_literal_active_generators": True,
        "exact_reduced_pair_Groebner_basis_has_76_rows": True,
        "all_five_pair_generators_reduce_to_zero": True,
        "three_root_rows_have_constant_minus_two_pivots": True,
        "all_three_root_solutions_reconstruct_their_rows_modulo_the_pair_ideal": True,
        "all_root_solutions_are_reduced_normal_forms": True,
        "all_three_consistency_obstructions_are_nonzero_reduced_normal_forms": True,
        "output_contains_five_pair_rows_and_three_exact_quotient_obstructions": True,
        "no_denominator_or_field_extension_is_introduced": True,
        "no_continuous_fit_parameter_is_added": True,
    }
    require(all(checks.values()), "quotient-obstruction checks")
    manifest = {
        "schema": "MTTQ79D10D6H1G1PairQuotientObstructions.v1",
        "date": "2026-07-19",
        "status": "EXACT_PAIR_QUOTIENT_REDUCTION_EMITTED",
        "space_index": space,
        "field_characteristic": PRIME,
        "dependencies": {
            "active_input": checksum(active_path),
            "active_manifest": checksum(active_manifest_path),
            "pair_input": checksum(pair_path),
            "pair_manifest": checksum(pair_manifest_path),
            "pair_Groebner_basis": checksum(groebner_path),
            "builder": checksum(Path(__file__).resolve()),
        },
        "pair_Groebner_basis_rows": basis_length,
        "pair_generator_normal_form_rounds": pair_reduction_rounds,
        "root_solutions": root_records,
        "triangular_normal_form_rounds": triangular_rounds,
        "consistency_obstructions": consistency_records,
        "consistency_normal_form_rounds": consistency_rounds,
        "output": {
            "path": str(output_path),
            "normalized_ascii_sha256": hashlib.sha256(output_text.encode("ascii")).hexdigest(),
            "variables": len(PAIR_NAMES),
            "equations": len(output_equations),
            "bytes": len(output_text.encode("ascii")),
        },
        "equivalence": (
            "Modulo the first five pair generators, active rows 5,6,7 have successive "
            "unit pivots -2 in g2,g3,g4. Their displayed quotient normal forms therefore "
            "give the unique root reconstruction. Active rows 8,9,10 vanish after that "
            "reconstruction if and only if the three emitted reduced normal forms vanish. "
            "Thus the eight-variable output and the eleven-variable active core have "
            "isomorphic solution sets over every extension of F_101."
        ),
        "checks": checks,
        "claim_boundary": (
            "This is an exact elimination/input transformation, not an emptiness result. "
            "The emitted eight-equation system still requires an exact solve or no-go certificate."
        ),
    }
    manifest_path.write_text(json.dumps(manifest, indent=2) + "\n", encoding="utf-8")
    print(output_path.name)
    print(manifest_path.name)
    print(f"checks={sum(checks.values())}/{len(checks)}")
    print(
        "obstruction_terms="
        + ",".join(str(row["terms"]) for row in consistency_records)
        + f"; output_bytes={manifest['output']['bytes']}"
    )


if __name__ == "__main__":
    main()
