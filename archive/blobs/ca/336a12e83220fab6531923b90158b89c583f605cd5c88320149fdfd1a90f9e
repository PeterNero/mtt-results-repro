#!/usr/bin/env python3
"""Transport an exact fixed-u2 symbolic-u3 basis to its canonical v-line."""

from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path

from flint import nmod_mpoly_ctx

from build_q79_D10_D6_h1_g1_pair_quotient_obstructions import (
    PRIME,
    parse_input,
    parse_polynomial,
)
from verify_q79_Ronly_symbolic_affine_quadratic_exception_D_unit_general import (
    evaluate,
    parse_basis,
    recover_affine_quadratic_quotient,
)


def require(condition: bool, label: str) -> None:
    if not condition:
        raise AssertionError(label)


def checksum(path: Path) -> dict[str, object]:
    return {
        "path": path.as_posix(),
        "bytes": path.stat().st_size,
        "sha256": hashlib.sha256(path.read_bytes()).hexdigest(),
    }


def monic(polynomial):
    coefficient = int(polynomial.leading_coefficient()) % PRIME
    require(coefficient != 0, "nonzero leading coefficient")
    return polynomial * pow(coefficient, -1, PRIME)


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--source-input", type=Path, required=True)
    parser.add_argument("--source-basis", type=Path, required=True)
    parser.add_argument("--target-input", type=Path, required=True)
    parser.add_argument("--target-packet", type=Path, required=True)
    parser.add_argument("--a", type=int, required=True)
    parser.add_argument("--output-basis", type=Path, required=True)
    parser.add_argument("--output-certificate", type=Path, required=True)
    args = parser.parse_args()

    a_value = args.a % PRIME
    require(a_value != 0, "nonzero canonical a")
    inverse_a = pow(a_value, -1, PRIME)
    source_names, source_field, source_texts = parse_input(args.source_input)
    target_names, target_field, target_texts = parse_input(args.target_input)
    require(
        source_field == target_field == PRIME
        and len(source_names) == len(target_names) == 12
        and source_names[:-1] == target_names[:-1]
        and source_names[-1] == "t"
        and target_names[-1] == "v",
        "Laurent coordinate rings",
    )
    require(len(source_texts) == len(target_texts) == 13, "line row counts")

    source_context = nmod_mpoly_ctx.get(
        source_names, ordering="degrevlex", modulus=PRIME
    )
    target_context = nmod_mpoly_ctx.get(
        target_names, ordering="degrevlex", modulus=PRIME
    )
    source_generators = dict(zip(source_names, source_context.gens()))
    target_generators = dict(zip(target_names, target_context.gens()))
    source_rows = [
        parse_polynomial(text, source_context, source_names) for text in source_texts
    ]
    target_rows = [
        parse_polynomial(text, target_context, target_names) for text in target_texts
    ]
    require(
        all("t" not in text for text in source_texts[:12])
        and all("v" not in text for text in target_texts[:12]),
        "R rows are independent of Laurent auxiliaries",
    )
    require(
        source_rows[-1] == source_generators["u3"] * source_generators["t"] - 1,
        "source saturation",
    )
    require(
        target_rows[-1]
        == target_generators["u3"] * target_generators["v"] - a_value,
        "target line relation",
    )

    parsed_names, _, source_basis = parse_basis(
        args.source_basis.read_text(encoding="ascii")
    )
    require(parsed_names == source_names and source_basis, "source reduced basis")
    forward_composition = [
        target_context.constant(inverse_a) * target_generators["v"]
        if name == "t"
        else target_generators[name]
        for name in source_names
    ]
    target_basis = [
        monic(row.compose(*forward_composition, ctx=target_context))
        for row in source_basis
    ]

    inverse_composition = [
        source_context.constant(a_value) * source_generators["t"]
        if name == "v"
        else source_generators[name]
        for name in target_names
    ]
    recovered_source_basis = [
        monic(row.compose(*inverse_composition, ctx=source_context))
        for row in target_basis
    ]
    require(recovered_source_basis == source_basis, "two-sided basis transport")

    output_text = (
        "#Reduced Groebner basis data\n"
        "#---\n"
        "#field characteristic: 101\n"
        "#variable order:       "
        + ", ".join(target_names)
        + "\n"
        "#monomial order:       graded reverse lexicographical\n"
        f"#length of basis:      {len(target_basis)} elements sorted by increasing leading monomials\n"
        "#---\n["
        + ",\n".join(str(row) for row in target_basis)
        + "]:\n"
    )
    args.output_basis.parent.mkdir(parents=True, exist_ok=True)
    args.output_basis.write_text(output_text, encoding="ascii", newline="\n")

    (
        verified_names,
        _,
        algebra,
        values,
        _,
        _,
        associativity_checks,
    ) = recover_affine_quadratic_quotient(output_text)
    require(verified_names == target_names, "transported variable order")
    target_remainders = [
        evaluate(row, target_names, values, algebra) for row in target_rows
    ]
    require(all(value == algebra.zero() for value in target_remainders), "target rows vanish")

    packet = json.loads(args.target_packet.read_text(encoding="utf-8"))
    require(
        packet.get("schema") == "MTTQ79RonlySymbolicVLineInput.v1"
        and packet.get("fixed_coordinates", {}).get("a_equals_v_times_u3") == a_value
        and packet.get("output", {}).get("sha256")
        == checksum(args.target_input)["sha256"],
        "target line packet",
    )
    certificate = {
        "schema": "MTTQ79RonlySymbolicU3ToVGroebnerTransport.v1",
        "date": "2026-07-21",
        "status": "EXACT_DIAGONAL_LAURENT_GROEBNER_BASIS_TRANSPORT",
        "field": "F_101",
        "canonical_a": a_value,
        "coordinate_isomorphism": {
            "forward": f"t -> {inverse_a}*v",
            "inverse": f"v -> {a_value}*t",
            "source_relation": "t*u3-1",
            "target_relation": f"v*u3-{a_value}",
        },
        "artifacts": {
            "source_symbolic_u3_input": checksum(args.source_input),
            "source_exact_reduced_basis": checksum(args.source_basis),
            "target_symbolic_v_input": checksum(args.target_input),
            "target_input_packet": checksum(args.target_packet),
            "transported_exact_reduced_basis": checksum(args.output_basis),
        },
        "quotient": {
            "dimension": algebra.dimension,
            "standard_basis": ["1", *algebra.free_names],
            "reduced_basis_rows": len(target_basis),
            "associativity_basis_triple_checks": associativity_checks,
        },
        "checks": {
            "R_rows_are_independent_of_t_and_v": True,
            "source_saturation_is_exactly_t_times_u3_minus_one": True,
            "target_line_is_exactly_v_times_u3_minus_a": True,
            "forward_coordinate_map_is_invertible": True,
            "inverse_transport_reproduces_every_source_basis_row": True,
            "diagonal_scaling_preserves_the_degrevlex_leading_monomials": True,
            "transported_rows_form_an_affine_quadratic_finite_algebra": True,
            "all_target_line_generators_vanish_in_that_algebra": True,
            "no_solver_result_is_fabricated_by_the_transport": True,
            "no_continuous_fit_parameter_is_added": True,
        },
        "theorem": (
            "The diagonal Laurent isomorphism t=a^(-1)v carries the exact reduced "
            "Groebner basis of the fixed-u2 symbolic-u3 line to an exact reduced "
            "basis of the canonical line v*u3=a. Its inverse v=a*t reproduces the "
            "source basis row by row."
        ),
        "claim_boundary": (
            "This transports an already computed exact basis; it does not classify "
            "the resulting nonunit quotient under omitted y or D rows. That separate "
            "unit test must be performed in the transported finite algebra."
        ),
        "new_continuous_fit_parameters": 0,
    }
    require(all(certificate["checks"].values()), "transport checks")
    args.output_certificate.parent.mkdir(parents=True, exist_ok=True)
    args.output_certificate.write_text(
        json.dumps(certificate, indent=2) + "\n", encoding="utf-8"
    )
    print(certificate["status"])
    print(
        f"dimension={algebra.dimension}; basis={['1', *algebra.free_names]}; "
        f"associativity_checks={associativity_checks}"
    )
    print(args.output_certificate)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
