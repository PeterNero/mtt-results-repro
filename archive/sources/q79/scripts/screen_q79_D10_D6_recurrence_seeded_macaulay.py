#!/usr/bin/env python3
"""Test bounded affine Nullstellensatz membership on one mirror u1 fiber.

The ten inverse-root recurrence rows are inserted before the eleven terminal
rows.  Sparse Gaussian elimination is exact over F_101 and uses the proved
root-block monomial order, so the calculation does not expand the recursive
root normal forms into the carrier variables.
"""

from __future__ import annotations

import argparse
import hashlib
import json
import time
from array import array
from collections import defaultdict
from dataclasses import dataclass
from pathlib import Path

from flint import nmod_mpoly_ctx

from build_q79_D10_D6_h1_g1_pair_quotient_obstructions import (
    PRIME,
    parse_input,
    parse_polynomial,
)


RECURRENCE_PARENT_ROWS = (1, 2, 3, 4, 5, 6, 14, 15, 16, 17)
TERMINAL_PARENT_ROWS = (7, 8, 9, 10, 11, 12, 13, 18, 19, 20, 21)


def require(condition: bool, label: str) -> None:
    if not condition:
        raise AssertionError(label)


def compositions(total: int, parts: int):
    """Yield exponent tuples of fixed total degree without materializing them."""

    if parts == 1:
        yield (total,)
        return
    for first in range(total + 1):
        for tail in compositions(total - first, parts - 1):
            yield (first,) + tail


def monomials_through(variable_count: int, degree: int) -> list[tuple[int, ...]]:
    return [
        exponent
        for total in range(degree + 1)
        for exponent in compositions(total, variable_count)
    ]


def add_exponents(left: tuple[int, ...], right: tuple[int, ...]) -> tuple[int, ...]:
    return tuple(a + b for a, b in zip(left, right))


@dataclass(frozen=True)
class PackedRow:
    columns: array
    coefficients: array

    @classmethod
    def from_dict(cls, row: dict[int, int]) -> "PackedRow":
        items = sorted(row.items(), reverse=True)
        return cls(
            columns=array("I", (column for column, _ in items)),
            coefficients=array("B", (coefficient for _, coefficient in items)),
        )

    def __len__(self) -> int:
        return len(self.columns)


def sparse_axpy(target: dict[int, int], factor: int, source: PackedRow) -> None:
    """Set target <- target - factor*source over F_101 in place."""

    if not factor:
        return
    for column, coefficient in zip(source.columns, source.coefficients):
        value = (target.get(column, 0) - factor * coefficient) % PRIME
        if value:
            target[column] = value
        else:
            target.pop(column, None)


def sparse_scale(row: dict[int, int], factor: int) -> None:
    for column in tuple(row):
        row[column] = row[column] * factor % PRIME


def polynomial_dict(polynomial) -> dict[tuple[int, ...], int]:
    return {
        tuple(int(value) for value in exponent): int(coefficient) % PRIME
        for exponent, coefficient in polynomial.to_dict().items()
        if int(coefficient) % PRIME
    }


@dataclass(frozen=True)
class SourceRow:
    stage: str
    parent_row: int
    multiplier: tuple[int, ...]
    polynomial: dict[tuple[int, ...], int]


def checksum(path: Path) -> dict[str, str]:
    return {"path": str(path), "sha256": hashlib.sha256(path.read_bytes()).hexdigest()}


def emit_transpose_sms(
    path: Path,
    rhs_path: Path,
    source_descriptors: list[SourceRow],
    rank_by_exponent: dict[tuple[int, ...], int],
    monomial_count: int,
) -> int:
    """Emit A^T x=e_const in LinBox sparse matrix-stream format."""

    path.parent.mkdir(parents=True, exist_ok=True)
    nonzeros = 0
    chunk: list[str] = []
    with path.open("w", encoding="ascii", newline="\n") as stream:
        stream.write(f"{monomial_count} {len(source_descriptors)} M\n")
        for source_id, descriptor in enumerate(source_descriptors, start=1):
            for exponent, coefficient in descriptor.polynomial.items():
                target = add_exponents(exponent, descriptor.multiplier)
                row = rank_by_exponent[target] + 1
                chunk.append(f"{row} {source_id} {coefficient}\n")
                nonzeros += 1
                if len(chunk) == 50_000:
                    stream.write("".join(chunk))
                    chunk.clear()
        if chunk:
            stream.write("".join(chunk))
        stream.write("0 0 0\n")
    with rhs_path.open("w", encoding="ascii", newline="\n") as stream:
        stream.write("1\n")
        for _ in range(monomial_count - 1):
            stream.write("0\n")
    return nonzeros


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--input", type=Path, required=True)
    parser.add_argument("--u1", type=int, default=1)
    parser.add_argument("--degree", type=int, choices=(3, 4, 5, 6), default=5)
    parser.add_argument("--track-certificate", action="store_true")
    parser.add_argument("--max-basis-nnz", type=int, default=2_500_000)
    parser.add_argument("--max-row-nnz", type=int, default=150_000)
    parser.add_argument("--max-provenance-nnz", type=int, default=2_500_000)
    parser.add_argument("--progress-every", type=int, default=250)
    parser.add_argument("--emit-transpose-sms", type=Path)
    parser.add_argument("--emit-only", action="store_true")
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()

    started = time.perf_counter()
    names, field, texts = parse_input(args.input)
    require(field == PRIME and len(names) == 19 and len(texts) == 22, "inverse-root input")
    require(
        set(RECURRENCE_PARENT_ROWS).isdisjoint(TERMINAL_PARENT_ROWS)
        and set(RECURRENCE_PARENT_ROWS).union(TERMINAL_PARENT_ROWS) == set(range(1, 22)),
        "row partition",
    )
    u1 = args.u1 % PRIME
    require(u1 != 0, "u1 is nonzero")
    u0 = pow(u1, -2, PRIME)

    source_context = nmod_mpoly_ctx.get(names, ordering="degrevlex", modulus=PRIME)
    source_rows = [parse_polynomial(text, source_context, names) for text in texts]
    target_names = tuple(name for name in names if name not in {"u0", "u1"})
    target_context = nmod_mpoly_ctx.get(
        target_names, ordering="degrevlex", modulus=PRIME
    )
    target_generators = dict(zip(target_names, target_context.gens()))
    composition = [
        target_context.constant(u0)
        if name == "u0"
        else target_context.constant(u1)
        if name == "u1"
        else target_generators[name]
        for name in names
    ]
    rows = [row.compose(*composition, ctx=target_context) for row in source_rows]
    require(rows[0] == target_context.constant(0), "r endpoint vanishes on fiber")

    variable_count = len(target_names)
    require(variable_count == 17, "seventeen fiber variables")
    positions = {name: index for index, name in enumerate(target_names)}
    root_order = [
        *[f"h{index}" for index in range(6, 0, -1)],
        *[f"y{index}" for index in range(4, 0, -1)],
    ]
    root_positions = [positions[name] for name in root_order]
    carrier_positions = [
        index for index, name in enumerate(target_names) if name not in set(root_order)
    ]

    def order_key(exponent: tuple[int, ...]) -> tuple[int, ...]:
        # Lex on the reverse root block, then degree-reverse-lex on the carrier block.
        carrier_degree = sum(exponent[index] for index in carrier_positions)
        return (
            *(exponent[index] for index in root_positions),
            carrier_degree,
            *(-exponent[index] for index in reversed(carrier_positions)),
        )

    all_monomials = monomials_through(variable_count, args.degree)
    all_monomials.sort(key=order_key)
    rank_by_exponent = {exponent: rank for rank, exponent in enumerate(all_monomials)}
    zero_exponent = (0,) * variable_count
    require(rank_by_exponent[zero_exponent] == 0, "constant is least monomial")

    row_polynomials = {index: polynomial_dict(rows[index]) for index in range(1, 22)}
    row_degrees = {
        index: max(sum(exponent) for exponent in polynomial)
        for index, polynomial in row_polynomials.items()
    }
    require(
        all(1 <= row_degrees[index] <= 3 for index in range(1, 13))
        and max(row_degrees[index] for index in range(1, 13)) == 3,
        "r rows have total degree at most three",
    )
    require(
        all(row_degrees[index] == 5 for index in range(13, 22)),
        "d rows have total degree five",
    )

    base_recurrence: list[SourceRow] = []
    recurrence_multiples: list[SourceRow] = []
    base_terminal: list[SourceRow] = []
    terminal_multiples: list[SourceRow] = []
    for stage, parent_rows, base_target, multiple_target in (
        ("recurrence", RECURRENCE_PARENT_ROWS, base_recurrence, recurrence_multiples),
        ("terminal", TERMINAL_PARENT_ROWS, base_terminal, terminal_multiples),
    ):
        for parent_row in parent_rows:
            multiplier_degree = args.degree - row_degrees[parent_row]
            if multiplier_degree < 0:
                continue
            multipliers = monomials_through(variable_count, multiplier_degree)
            multipliers.sort(key=lambda exponent: rank_by_exponent[exponent], reverse=True)
            for multiplier in multipliers:
                source = SourceRow(
                    stage=stage,
                    parent_row=parent_row,
                    multiplier=multiplier,
                    polynomial=row_polynomials[parent_row],
                )
                if multiplier == zero_exponent:
                    base_target.append(source)
                else:
                    multiple_target.append(source)
    source_descriptors = [
        *base_recurrence,
        *recurrence_multiples,
        *base_terminal,
        *terminal_multiples,
    ]

    sms_emission = None
    if args.emit_transpose_sms is not None:
        rhs_path = args.emit_transpose_sms.with_suffix(
            args.emit_transpose_sms.suffix + ".rhs"
        )
        nonzeros = emit_transpose_sms(
            args.emit_transpose_sms,
            rhs_path,
            source_descriptors,
            rank_by_exponent,
            len(all_monomials),
        )
        sms_emission = {
            "orientation": "transpose_macaulay_operator_A_transpose",
            "equation": "A_transpose*x=e_constant",
            "matrix": checksum(args.emit_transpose_sms),
            "right_hand_side": checksum(rhs_path),
            "rows": len(all_monomials),
            "columns": len(source_descriptors),
            "nonzeros": nonzeros,
        }
        print(
            f"emitted SMS transpose {len(all_monomials)}x{len(source_descriptors)} "
            f"with {nonzeros} nonzeros",
            flush=True,
        )
    require(not args.emit_only or sms_emission is not None, "emit-only requires SMS output")
    if args.emit_only:
        elapsed = time.perf_counter() - started
        packet = {
            "schema": "MTTQ79D10D6RecurrenceSeededAffineMacaulaySMS.v1",
            "date": "2026-07-20",
            "status": "EXACT_SPARSE_TRANSPOSE_MACAULAY_OPERATOR_EMITTED",
            "input": checksum(args.input),
            "field": "F_101",
            "fiber": {"u1": u1, "forced_u0": u0},
            "variables": list(target_names),
            "maximum_product_total_degree": args.degree,
            "row_partition": {
                "recurrence_parent_rows": list(RECURRENCE_PARENT_ROWS),
                "terminal_parent_rows": list(TERMINAL_PARENT_ROWS),
            },
            "operator": sms_emission,
            "elapsed_seconds": elapsed,
            "checks": {
                "constant_is_the_first_ordered_monomial": rank_by_exponent[zero_exponent] == 0,
                "all_generator_multiples_are_emitted": sms_emission["columns"]
                == len(source_descriptors),
                "right_hand_side_is_the_affine_unit_vector": True,
                "no_continuous_fit_parameter_is_added": True,
            },
            "claim_boundary": (
                "This is an exact sparse operator export, not a rank or unit-ideal result. "
                "Any returned solution must be checked against this hash-bound operator."
            ),
        }
        args.output.parent.mkdir(parents=True, exist_ok=True)
        args.output.write_text(json.dumps(packet, indent=2) + "\n", encoding="utf-8")
        print(f"status={packet['status']}; elapsed={elapsed:.3f}s")
        print(args.output)
        return

    basis: dict[int, PackedRow] = {}
    provenance_basis: dict[int, PackedRow] = {}
    stage_stats = {
        "recurrence": {"processed": 0, "rank_increments": 0},
        "terminal": {"processed": 0, "rank_increments": 0},
    }
    source_metadata: list[dict] = []
    basis_nnz = 0
    provenance_nnz = 0
    maximum_row_nnz = 0
    reductions = 0
    unit_provenance: dict[int, int] | None = None
    resource_limit: str | None = None

    for source_id, descriptor in enumerate(source_descriptors):
        source_metadata.append(
            {
                "stage": descriptor.stage,
                "parent_row": descriptor.parent_row,
                "multiplier": descriptor.multiplier,
            }
        )
        row: dict[int, int] = {}
        for exponent, coefficient in descriptor.polynomial.items():
            target_exponent = add_exponents(exponent, descriptor.multiplier)
            column = rank_by_exponent[target_exponent]
            row[column] = (row.get(column, 0) + coefficient) % PRIME
        row = {column: value for column, value in row.items() if value}
        provenance = {source_id: 1} if args.track_certificate else None
        stage_stats[descriptor.stage]["processed"] += 1

        while row:
            pivot = max(row)
            if pivot not in basis:
                inverse = pow(row[pivot], -1, PRIME)
                sparse_scale(row, inverse)
                if provenance is not None:
                    sparse_scale(provenance, inverse)
                basis[pivot] = PackedRow.from_dict(row)
                basis_nnz += len(row)
                if provenance is not None:
                    provenance_basis[pivot] = PackedRow.from_dict(provenance)
                    provenance_nnz += len(provenance)
                stage_stats[descriptor.stage]["rank_increments"] += 1
                maximum_row_nnz = max(maximum_row_nnz, len(row))
                if pivot == 0:
                    require(row == {0: 1}, "constant pivot is a unit row")
                    unit_provenance = provenance
                break
            factor = row[pivot]
            sparse_axpy(row, factor, basis[pivot])
            if provenance is not None:
                sparse_axpy(provenance, factor, provenance_basis[pivot])
            reductions += 1
            if len(row) > args.max_row_nnz:
                resource_limit = "MAX_ROW_NNZ"
                break
            if provenance is not None and len(provenance) > args.max_provenance_nnz:
                resource_limit = "MAX_PROVENANCE_NNZ"
                break
        if resource_limit or unit_provenance is not None or (0 in basis and not args.track_certificate):
            break
        if basis_nnz > args.max_basis_nnz:
            resource_limit = "MAX_BASIS_NNZ"
            break
        if provenance_nnz > args.max_provenance_nnz:
            resource_limit = "MAX_PROVENANCE_NNZ"
            break
        if args.progress_every and (source_id + 1) % args.progress_every == 0:
            print(
                f"rows={source_id + 1}/{len(source_descriptors)} rank={len(basis)} "
                f"basis_nnz={basis_nnz} max_row={maximum_row_nnz}",
                flush=True,
            )

    constant_in_span = 0 in basis
    fully_processed = (
        not resource_limit
        and (constant_in_span or sum(row["processed"] for row in stage_stats.values()) == len(source_descriptors))
    )
    certificate = None
    if constant_in_span and args.track_certificate:
        require(unit_provenance is not None, "tracked unit provenance")
        multipliers_by_parent: dict[int, dict[tuple[int, ...], int]] = defaultdict(dict)
        identity: dict[tuple[int, ...], int] = {}
        for source_id, coefficient in unit_provenance.items():
            metadata = source_metadata[source_id]
            parent_row = int(metadata["parent_row"])
            multiplier = tuple(int(value) for value in metadata["multiplier"])
            previous = multipliers_by_parent[parent_row].get(multiplier, 0)
            multipliers_by_parent[parent_row][multiplier] = (previous + coefficient) % PRIME
            for exponent, polynomial_coefficient in row_polynomials[parent_row].items():
                target = add_exponents(exponent, multiplier)
                value = (identity.get(target, 0) + coefficient * polynomial_coefficient) % PRIME
                if value:
                    identity[target] = value
                else:
                    identity.pop(target, None)
        multipliers_by_parent = defaultdict(
            dict,
            {
                parent: {exponent: value for exponent, value in multiplier.items() if value}
                for parent, multiplier in multipliers_by_parent.items()
            },
        )
        require(identity == {zero_exponent: 1}, "direct sparse certificate identity")
        certificate_rows = []
        digest = hashlib.sha256()
        for parent_row in sorted(multipliers_by_parent):
            terms = [
                {"coefficient": coefficient, "exponents": list(exponent)}
                for exponent, coefficient in sorted(multipliers_by_parent[parent_row].items())
            ]
            encoded = json.dumps([parent_row, terms], separators=(",", ":"), sort_keys=True)
            digest.update(encoded.encode("ascii"))
            certificate_rows.append({"parent_row": parent_row, "multiplier_terms": terms})
        certificate = {
            "identity": "sum(q_i*f_i)=1 in F_101[target_names]",
            "rows": certificate_rows,
            "nonzero_generated_row_coefficients": len(unit_provenance),
            "sha256": digest.hexdigest(),
            "direct_sparse_identity_verified": True,
        }

    elapsed = time.perf_counter() - started
    status = (
        "EXACT_BOUNDED_NULLSTELLENSATZ_CERTIFICATE"
        if constant_in_span and (not args.track_certificate or certificate is not None)
        else "EXACT_NO_UNIT_IN_TRUNCATED_ROW_SPAN"
        if fully_processed
        else "RESOURCE_LIMIT_INCONCLUSIVE"
    )
    checks = {
        "inverse_root_parent_has_19_variables_and_22_rows": len(names) == 19 and len(texts) == 22,
        "nonzero_u1_fiber_forces_u0_equals_u1_inverse_square": u0 * u1 * u1 % PRIME == 1,
        "fiber_has_17_variables_and_21_nonzero_parent_rows": variable_count == 17,
        "ten_recurrence_and_eleven_terminal_rows_partition_the_fiber": True,
        "root_block_order_matches_the_proved_recurrence_basis": root_order
        == ["h6", "h5", "h4", "h3", "h2", "h1", "y4", "y3", "y2", "y1"],
        "all_arithmetic_is_exact_over_F101": True,
        "unit_claim_has_direct_certificate_when_requested": (
            not constant_in_span or not args.track_certificate or certificate is not None
        ),
        "no_timeout_or_resource_limit_is_promoted": status != "EXACT_BOUNDED_NULLSTELLENSATZ_CERTIFICATE"
        or resource_limit is None,
        "no_continuous_fit_parameter_is_added": True,
    }
    require(all(checks.values()), "output checks")
    packet = {
        "schema": "MTTQ79D10D6RecurrenceSeededAffineMacaulayScreen.v1",
        "date": "2026-07-20",
        "status": status,
        "input": checksum(args.input),
        "field": "F_101",
        "fiber": {"u1": u1, "forced_u0": u0},
        "variables": list(target_names),
        "monomial_order": {
            "root_block_lex": root_order,
            "carrier_block": [target_names[index] for index in carrier_positions],
            "carrier_order": "degree_reverse_lexicographic",
        },
        "row_partition": {
            "recurrence_parent_rows": list(RECURRENCE_PARENT_ROWS),
            "terminal_parent_rows": list(TERMINAL_PARENT_ROWS),
        },
        "truncation": {
            "maximum_product_total_degree": args.degree,
            "columns_monomials_of_degree_at_most_D": len(all_monomials),
            "planned_generator_multiples": len(source_descriptors),
            "processed_generator_multiples": sum(
                row["processed"] for row in stage_stats.values()
            ),
            "fully_processed_or_unit_found": fully_processed,
        },
        "exact_linear_algebra": {
            "rank": len(basis),
            "constant_in_row_span": constant_in_span,
            "basis_nnz": basis_nnz,
            "maximum_basis_row_nnz": maximum_row_nnz,
            "row_reductions": reductions,
            "stage_statistics": stage_stats,
            "resource_limit": resource_limit,
            "certificate_tracking": args.track_certificate,
            "provenance_nnz": provenance_nnz if args.track_certificate else None,
        },
        "certificate": certificate,
        "sparse_operator_emission": sms_emission,
        "elapsed_seconds": elapsed,
        "checks": checks,
        "claim_boundary": (
            "A directly verified unit certificate excludes this exact u1 fiber. A fully "
            "processed deficient degree-D span proves only that no certificate exists in "
            "this standard bounded Macaulay space. A resource limit is inconclusive. No "
            "single-fiber result classifies the complete 100-fiber chart."
        ),
        "new_continuous_fit_parameters": 0,
    }
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(packet, indent=2) + "\n", encoding="utf-8")
    print(
        f"status={status}; degree={args.degree}; rows={sum(row['processed'] for row in stage_stats.values())}/"
        f"{len(source_descriptors)}; rank={len(basis)}; basis_nnz={basis_nnz}; "
        f"elapsed={elapsed:.3f}s"
    )
    print(args.output)


if __name__ == "__main__":
    main()
