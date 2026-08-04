#!/usr/bin/env python3
"""Build an exact bounded Nullstellensatz certificate on one triple endpoint fiber."""

from __future__ import annotations

import argparse
import hashlib
import json
import time
from collections import defaultdict
from pathlib import Path

from flint import nmod_mpoly_ctx

from build_q79_D10_D6_h1_g1_pair_quotient_obstructions import (
    PRIME,
    parse_input,
    parse_polynomial,
)
from screen_q79_D10_D6_recurrence_seeded_macaulay import (
    PackedRow,
    SourceRow,
    add_exponents,
    checksum,
    emit_transpose_sms,
    monomials_through,
    polynomial_dict,
    sparse_axpy,
    sparse_scale,
)


RECURRENCE_PARENT_ROWS = (1, 2, 3, 4, 5, 6, 14, 15, 16, 17)
TERMINAL_PARENT_ROWS = (7, 8, 9, 10, 11, 12, 18, 19, 20, 21)


def require(condition: bool, label: str) -> None:
    if not condition:
        raise AssertionError(label)


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--input", type=Path, required=True)
    parser.add_argument("--scalar-class", type=int, choices=(1, 2), required=True)
    parser.add_argument("--u1", type=int, default=1)
    parser.add_argument("--a", type=int, default=1)
    parser.add_argument("--v", type=int, default=1)
    parser.add_argument(
        "--terminal-parent-rows",
        default=",".join(str(value) for value in TERMINAL_PARENT_ROWS),
    )
    parser.add_argument("--degree", type=int, choices=(3, 4, 5, 6, 7, 8), default=6)
    parser.add_argument("--track-certificate", action="store_true")
    parser.add_argument("--max-basis-nnz", type=int, default=20_000_000)
    parser.add_argument("--max-row-nnz", type=int, default=100_000)
    parser.add_argument("--max-provenance-nnz", type=int, default=20_000_000)
    parser.add_argument("--progress-every", type=int, default=1000)
    parser.add_argument("--emit-transpose-sms", type=Path)
    parser.add_argument("--emit-only", action="store_true")
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()
    terminal_parent_rows = tuple(
        int(value) for value in args.terminal_parent_rows.split(",") if value
    )
    require(
        bool(terminal_parent_rows)
        and len(set(terminal_parent_rows)) == len(terminal_parent_rows)
        and set(terminal_parent_rows).issubset(TERMINAL_PARENT_ROWS),
        "selected terminal parent rows",
    )

    started = time.perf_counter()
    names, field, texts = parse_input(args.input)
    require(field == PRIME and len(names) == 19 and len(texts) == 22, "inverse-root parent")
    u1 = args.u1 % PRIME
    a_value = args.a % PRIME
    v_value = args.v % PRIME
    require(u1 and a_value and v_value, "nonzero triple")
    u0 = pow(u1, -2, PRIME)
    u2 = args.scalar_class * pow(a_value, -2, PRIME) % PRIME
    u3 = a_value * pow(v_value, -1, PRIME) % PRIME
    assignments = {"u0": u0, "u1": u1, "u2": u2, "u3": u3, "v": v_value}

    source_context = nmod_mpoly_ctx.get(names, ordering="degrevlex", modulus=PRIME)
    source_rows = [parse_polynomial(text, source_context, names) for text in texts]
    source_generator = dict(zip(names, source_context.gens()))
    require(source_rows[0] == source_generator["u0"] * source_generator["u1"] ** 2 - 1, "r endpoint")
    require(
        source_rows[13]
        == source_generator["v"] ** 2
        * source_generator["u2"]
        * source_generator["u3"] ** 2
        - args.scalar_class,
        "d endpoint",
    )
    target_names = tuple(name for name in names if name not in assignments)
    target_context = nmod_mpoly_ctx.get(target_names, ordering="degrevlex", modulus=PRIME)
    target_generator = dict(zip(target_names, target_context.gens()))
    composition = [
        target_context.constant(assignments[name])
        if name in assignments
        else target_generator[name]
        for name in names
    ]
    rows = [row.compose(*composition, ctx=target_context) for row in source_rows]
    require(rows[0] == rows[13] == target_context.constant(0), "both endpoints vanish")
    require(len(target_names) == 14, "fourteen variables")
    require(
        set(RECURRENCE_PARENT_ROWS).isdisjoint(terminal_parent_rows),
        "active-row partition",
    )

    variable_count = len(target_names)
    positions = {name: index for index, name in enumerate(target_names)}
    root_order = [
        *[f"h{index}" for index in range(6, 0, -1)],
        *[f"y{index}" for index in range(4, 0, -1)],
    ]
    root_positions = [positions[name] for name in root_order]
    carrier_positions = [
        index for index, name in enumerate(target_names) if name not in set(root_order)
    ]
    require(
        [target_names[index] for index in carrier_positions] == ["u4", "u5", "u6", "u7"],
        "four free carrier coordinates",
    )

    def order_key(exponent: tuple[int, ...]) -> tuple[int, ...]:
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
    require(rank_by_exponent[zero_exponent] == 0, "constant least")

    parent_rows = (*RECURRENCE_PARENT_ROWS, *terminal_parent_rows)
    row_polynomials = {index: polynomial_dict(rows[index]) for index in parent_rows}
    row_degrees = {
        index: max(sum(exponent) for exponent in polynomial)
        for index, polynomial in row_polynomials.items()
    }
    require(max(row_degrees.values()) <= 3, "all fiber rows are cubic or lower")

    base_recurrence: list[SourceRow] = []
    recurrence_multiples: list[SourceRow] = []
    base_terminal: list[SourceRow] = []
    terminal_multiples: list[SourceRow] = []
    for stage, indices, bases, multiples in (
        ("recurrence", RECURRENCE_PARENT_ROWS, base_recurrence, recurrence_multiples),
        ("terminal", terminal_parent_rows, base_terminal, terminal_multiples),
    ):
        for parent_row in indices:
            maximum_multiplier_degree = args.degree - row_degrees[parent_row]
            if maximum_multiplier_degree < 0:
                continue
            multiplier_rows = monomials_through(variable_count, maximum_multiplier_degree)
            multiplier_rows.sort(
                key=lambda exponent: rank_by_exponent[exponent], reverse=True
            )
            for multiplier in multiplier_rows:
                descriptor = SourceRow(stage, parent_row, multiplier, row_polynomials[parent_row])
                (bases if multiplier == zero_exponent else multiples).append(descriptor)
    descriptors = [
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
            descriptors,
            rank_by_exponent,
            len(all_monomials),
        )
        sms_emission = {
            "orientation": "transpose_macaulay_operator_A_transpose",
            "equation": "A_transpose*x=e_constant",
            "matrix": checksum(args.emit_transpose_sms),
            "right_hand_side": checksum(rhs_path),
            "rows": len(all_monomials),
            "columns": len(descriptors),
            "nonzeros": nonzeros,
        }
        print(
            f"emitted SMS transpose {len(all_monomials)}x{len(descriptors)} "
            f"with {nonzeros} nonzeros",
            flush=True,
        )
    require(not args.emit_only or sms_emission is not None, "emit-only requires SMS")
    if args.emit_only:
        elapsed = time.perf_counter() - started
        packet = {
            "schema": "MTTQ79D10D6TripleEndpointMacaulaySMS.v1",
            "date": "2026-07-20",
            "status": "EXACT_TRIPLE_FIBER_SPARSE_TRANSPOSE_EMITTED",
            "input": checksum(args.input),
            "field": "F_101",
            "scalar_square_class_representative": args.scalar_class,
            "fiber": {
                "u1": u1,
                "a_equals_v_times_u3": a_value,
                "v": v_value,
                "forced_u0": u0,
                "forced_u2": u2,
                "forced_u3": u3,
            },
            "variables": list(target_names),
            "row_partition": {
                "recurrence_parent_rows": list(RECURRENCE_PARENT_ROWS),
                "terminal_parent_rows": list(terminal_parent_rows),
            },
            "maximum_product_total_degree": args.degree,
            "operator": sms_emission,
            "elapsed_seconds": elapsed,
            "checks": {
                "both_endpoints_vanish": True,
                "all_selected_active_rows_are_included": len(parent_rows)
                == len(RECURRENCE_PARENT_ROWS) + len(terminal_parent_rows),
                "constant_is_the_first_ordered_monomial": rank_by_exponent[zero_exponent] == 0,
                "right_hand_side_is_the_affine_unit_vector": True,
                "no_continuous_fit_parameter_is_added": True,
            },
            "claim_boundary": (
                "Exact sparse operator export only. A solution vector must be independently "
                "multiplied through this hash-bound matrix before it is a certificate."
            ),
        }
        args.output.parent.mkdir(parents=True, exist_ok=True)
        args.output.write_text(json.dumps(packet, indent=2) + "\n", encoding="utf-8")
        print(f"status={packet['status']}; elapsed={elapsed:.3f}s")
        print(args.output)
        return

    basis: dict[int, PackedRow] = {}
    provenance_basis: dict[int, PackedRow] = {}
    source_metadata: list[dict] = []
    stage_stats = {
        "recurrence": {"processed": 0, "rank_increments": 0, "zero_reductions": 0},
        "terminal": {"processed": 0, "rank_increments": 0, "zero_reductions": 0},
    }
    basis_nnz = 0
    provenance_nnz = 0
    maximum_row_nnz = 0
    reductions = 0
    resource_limit = None
    unit_provenance: dict[int, int] | None = None

    for source_id, descriptor in enumerate(descriptors):
        source_metadata.append(
            {
                "stage": descriptor.stage,
                "parent_row": descriptor.parent_row,
                "multiplier": descriptor.multiplier,
            }
        )
        row: dict[int, int] = {}
        for exponent, coefficient in descriptor.polynomial.items():
            target = add_exponents(exponent, descriptor.multiplier)
            column = rank_by_exponent[target]
            row[column] = (row.get(column, 0) + coefficient) % PRIME
        row = {column: coefficient for column, coefficient in row.items() if coefficient}
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
                    require(row == {0: 1}, "unit row")
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
        if not row and resource_limit is None:
            stage_stats[descriptor.stage]["zero_reductions"] += 1
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
                f"rows={source_id + 1}/{len(descriptors)} rank={len(basis)} "
                f"basis_nnz={basis_nnz} provenance_nnz={provenance_nnz}",
                flush=True,
            )

    constant_in_span = 0 in basis
    certificate = None
    if constant_in_span and args.track_certificate:
        require(unit_provenance is not None, "unit provenance")
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
        require(identity == {zero_exponent: 1}, "direct certificate identity")
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
            "identity": "sum(q_i*f_i)=1 in F_101[h1,...,h6,y1,...,y4,u4,...,u7]",
            "rows": certificate_rows,
            "nonzero_generated_row_coefficients": len(unit_provenance),
            "total_multiplier_terms": sum(len(row["multiplier_terms"]) for row in certificate_rows),
            "sha256": digest.hexdigest(),
            "direct_sparse_identity_verified": True,
        }

    elapsed = time.perf_counter() - started
    processed = sum(row["processed"] for row in stage_stats.values())
    fully_processed = resource_limit is None and (
        constant_in_span or processed == len(descriptors)
    )
    status = (
        "EXACT_TRIPLE_FIBER_NULLSTELLENSATZ_CERTIFICATE"
        if constant_in_span and (not args.track_certificate or certificate is not None)
        else "EXACT_NO_UNIT_IN_TRUNCATED_TRIPLE_FIBER_SPAN"
        if fully_processed
        else "RESOURCE_LIMIT_INCONCLUSIVE"
    )
    checks = {
        "both_endpoint_rows_vanish_exactly": rows[0] == rows[13] == target_context.constant(0),
        "triple_fiber_has_14_variables_and_selected_rows": len(target_names) == 14
        and len(parent_rows) == len(RECURRENCE_PARENT_ROWS) + len(terminal_parent_rows),
        "every_active_row_has_degree_at_most_three": max(row_degrees.values()) <= 3,
        "constant_is_least_monomial": rank_by_exponent[zero_exponent] == 0,
        "unit_has_direct_multiplier_certificate_when_requested": not constant_in_span
        or not args.track_certificate
        or certificate is not None,
        "no_resource_limit_is_promoted": status
        != "EXACT_TRIPLE_FIBER_NULLSTELLENSATZ_CERTIFICATE"
        or resource_limit is None,
        "no_continuous_fit_parameter_is_added": True,
    }
    require(all(checks.values()), "certificate checks")
    packet = {
        "schema": "MTTQ79D10D6TripleEndpointMacaulayCertificate.v1",
        "date": "2026-07-20",
        "status": status,
        "input": checksum(args.input),
        "field": "F_101",
        "scalar_square_class_representative": args.scalar_class,
        "fiber": {
            "u1": u1,
            "a_equals_v_times_u3": a_value,
            "v": v_value,
            "forced_u0": u0,
            "forced_u2": u2,
            "forced_u3": u3,
        },
        "variables": list(target_names),
        "row_partition": {
            "recurrence_parent_rows": list(RECURRENCE_PARENT_ROWS),
            "terminal_parent_rows": list(terminal_parent_rows),
        },
        "maximum_product_total_degree": args.degree,
        "planned_generator_multiples": len(descriptors),
        "processed_generator_multiples": processed,
        "columns_monomials_of_degree_at_most_D": len(all_monomials),
        "exact_linear_algebra": {
            "rank": len(basis),
            "constant_in_row_span": constant_in_span,
            "basis_nnz": basis_nnz,
            "provenance_nnz": provenance_nnz if args.track_certificate else None,
            "maximum_basis_row_nnz": maximum_row_nnz,
            "row_reductions": reductions,
            "stage_statistics": stage_stats,
            "resource_limit": resource_limit,
        },
        "certificate": certificate,
        "sparse_operator_emission": sms_emission,
        "elapsed_seconds": elapsed,
        "checks": checks,
        "claim_boundary": (
            "A direct multiplier identity excludes exactly this nonzero triple fiber. "
            "It does not classify the remaining endpoint fibers without an exhaustive "
            "cover or a proved orbit/parameter theorem."
        ),
        "new_continuous_fit_parameters": 0,
    }
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(packet, indent=2) + "\n", encoding="utf-8")
    print(
        f"status={status}; rows={processed}/{len(descriptors)} rank={len(basis)} "
        f"basis_nnz={basis_nnz} provenance_nnz={provenance_nnz}; elapsed={elapsed:.3f}s"
    )
    print(args.output)


if __name__ == "__main__":
    main()
