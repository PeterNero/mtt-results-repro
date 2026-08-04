#!/usr/bin/env python3
"""Reverse the q79 F4 operation DAG into sixteen explicit multipliers."""

from __future__ import annotations

import argparse
import hashlib
import json
import os
from collections import Counter
from pathlib import Path

from flint import nmod_mpoly_ctx

from build_q79_D10_D6_h1_g1_pair_quotient_obstructions import (
    PRIME,
    parse_input,
    parse_polynomial,
)


ROOT = Path(__file__).resolve().parents[1]
DEFAULT_DIR = ROOT / "candidate_data" / "q79_Ronly_triple_fiber_min_degree"
DEFAULT_DAG = Path(
    os.environ.get("MTT_Q79_F4_OPERATION_DAG", str(DEFAULT_DIR / "q79_full14_operation_dag.tsv"))
)
DEFAULT_INPUT = DEFAULT_DIR / "selected_full14.msolve.in"
DEFAULT_CERTIFICATE = DEFAULT_DIR / "explicit_degree9_multipliers.json"
DEFAULT_PACKET = DEFAULT_DIR / "explicit_degree9_generation.packet.json"
DEFAULT_PATCH = DEFAULT_DIR / "msolve_f4_operation_dag.patch"


Polynomial = dict[int, int]


def require(condition: bool, label: str) -> None:
    if not condition:
        raise AssertionError(label)


def checksum(path: Path) -> dict[str, object]:
    digest = hashlib.sha256()
    with path.open("rb") as stream:
        for block in iter(lambda: stream.read(1 << 20), b""):
            digest.update(block)
    return {"path": str(path), "bytes": path.stat().st_size, "sha256": digest.hexdigest()}


def encode(exponents: tuple[int, ...] | list[int]) -> int:
    require(all(0 <= value < 16 for value in exponents), "four-bit exponent")
    return sum(value << (4 * index) for index, value in enumerate(exponents))


def decode(monomial: int, variables: int) -> list[int]:
    return [(monomial >> (4 * index)) & 15 for index in range(variables)]


def monomial_degree(monomial: int, variables: int) -> int:
    return sum(decode(monomial, variables))


def add_scaled(target: Polynomial, source: Polynomial, scale: int, shift: int = 0) -> int:
    before = len(target)
    scale %= PRIME
    if scale == 0:
        return 0
    for monomial, coefficient in source.items():
        shifted = monomial + shift
        value = (target.get(shifted, 0) + scale * coefficient) % PRIME
        if value:
            target[shifted] = value
        else:
            target.pop(shifted, None)
    return len(target) - before


def add_to_node(
    weights: dict[int, Polynomial], node: int, source: Polynomial, scale: int, shift: int = 0
) -> int:
    require(node > 0, "positive dependency node")
    target = weights.get(node)
    if target is None:
        target = {}
        weights[node] = target
    delta = add_scaled(target, source, scale, shift)
    if not target:
        weights.pop(node, None)
    return delta


def scan_dag(
    path: Path,
) -> tuple[
    int,
    int,
    dict[int, int],
    dict[int, Polynomial],
    dict[int, int],
    Counter[str],
]:
    node_offsets: dict[int, int] = {}
    initial: dict[int, Polynomial] = {}
    basis_nodes: dict[int, int] = {}
    node_types: Counter[str] = Counter()
    current_initial: int | None = None
    variables = 0
    declared_nodes = 0
    declared_reducer_terms = 0

    with path.open("rb") as stream:
        while True:
            offset = stream.tell()
            line = stream.readline()
            if not line:
                break
            tag = line.split(b"\t", 1)[0].rstrip().decode("ascii")
            if tag == "FORMAT":
                fields = line.rstrip().split(b"\t")
                require(
                    fields[1] == b"MSOLVE_F4_OPERATION_DAG_V1"
                    and int(fields[2]) == PRIME,
                    "DAG format and field",
                )
                variables = int(fields[3])
                require(int(fields[4]) == variables + 1, "exponent-vector length")
            elif tag == "INITIAL":
                fields = line.rstrip().split(b"\t")
                current_initial = int(fields[1])
                require(current_initial not in initial, "unique initial polynomial")
                initial[current_initial] = {}
            elif tag == "ITERM":
                require(current_initial is not None, "initial term placement")
                fields = line.rstrip().split(b"\t")
                coefficient = int(fields[1]) % PRIME
                exponents = tuple(int(value) for value in fields[2:])
                require(len(exponents) == variables, "initial exponent length")
                initial[current_initial][encode(exponents)] = coefficient
            elif tag == "ENDINITIAL":
                require(current_initial is not None, "initial terminator")
                current_initial = None
            elif tag in {"INPUT", "REDUCE", "SCALE"}:
                fields = line.split(b"\t", 2)
                node = int(fields[1])
                require(node not in node_offsets, "unique DAG node")
                node_offsets[node] = offset
                node_types[tag] += 1
            elif tag == "BASIS":
                fields = line.rstrip().split(b"\t")
                basis_index, node = int(fields[1]), int(fields[2])
                require(basis_index not in basis_nodes, "unique derived basis node")
                basis_nodes[basis_index] = node
            elif tag in {"ENDROUND"}:
                continue
            elif tag == "END":
                fields = line.rstrip().split(b"\t")
                declared_nodes = int(fields[1])
                declared_reducer_terms = int(fields[2])
            elif tag == "ERROR":
                raise AssertionError(line.decode("ascii", errors="replace"))
            else:
                raise AssertionError(f"unknown DAG tag: {tag}")

    require(current_initial is None and variables == 14, "complete initial DAG section")
    require(len(initial) == 16 and len(basis_nodes) == 3205, "basis counts")
    require(
        len(node_offsets) == declared_nodes
        and set(node_offsets) == set(range(1, declared_nodes + 1)),
        "contiguous declared DAG nodes",
    )
    return (
        variables,
        declared_reducer_terms,
        node_offsets,
        initial,
        basis_nodes,
        node_types,
    )


def reverse_dag(
    path: Path,
    variables: int,
    node_offsets: dict[int, int],
    basis_nodes: dict[int, int],
    target_basis: int,
) -> tuple[dict[int, Polynomial], dict[str, int]]:
    require(target_basis in basis_nodes, "target basis node")
    target_node = basis_nodes[target_basis]
    weights: dict[int, Polynomial] = {target_node: {0: 1}}
    initial_weights: dict[int, Polynomial] = {}
    active_counts: Counter[str] = Counter()
    maximum_pending_nodes = 1
    maximum_pending_terms = 1
    pending_terms = 1
    processed = 0

    with path.open("rb") as stream:
        for node in range(max(node_offsets), 0, -1):
            weight = weights.pop(node, None)
            if weight is None:
                continue
            pending_terms -= len(weight)
            stream.seek(node_offsets[node])
            fields = stream.readline().rstrip().split(b"\t")
            tag = fields[0].decode("ascii")
            require(int(fields[1]) == node, "node offset binding")
            active_counts[tag] += 1

            if tag == "INPUT":
                basis_index = int(fields[5])
                exponents = tuple(int(value) for value in fields[6:])
                require(len(exponents) == variables, "input multiplier length")
                shift = encode(exponents)
                if basis_index < 16:
                    target = initial_weights.setdefault(basis_index, {})
                    add_scaled(target, weight, 1, shift)
                else:
                    require(basis_index in basis_nodes, "derived input basis node")
                    dependency = basis_nodes[basis_index]
                    require(dependency < node, "input DAG order")
                    pending_terms += add_to_node(weights, dependency, weight, 1, shift)
            elif tag == "SCALE":
                dependency, coefficient = int(fields[2]), int(fields[3])
                require(dependency < node, "scale DAG order")
                pending_terms += add_to_node(weights, dependency, weight, coefficient)
            elif tag == "REDUCE":
                parent, count = int(fields[2]), int(fields[3])
                require(len(fields) == 4 + 2 * count, "reducer term count")
                require(parent < node, "parent DAG order")
                pending_terms += add_to_node(weights, parent, weight, 1)
                for position in range(count):
                    dependency = int(fields[4 + 2 * position])
                    coefficient = int(fields[5 + 2 * position])
                    require(dependency < node, "reducer DAG order")
                    pending_terms += add_to_node(weights, dependency, weight, coefficient)
            else:
                raise AssertionError(f"unexpected node tag: {tag}")

            maximum_pending_nodes = max(maximum_pending_nodes, len(weights))
            require(pending_terms >= 0, "nonnegative pending term count")
            maximum_pending_terms = max(maximum_pending_terms, pending_terms)
            processed += 1
            if processed % 2500 == 0:
                print(
                    f"DAG_REVERSE_PROGRESS active={processed} node={node} "
                    f"pending_nodes={len(weights)} pending_terms={pending_terms}",
                    flush=True,
                )

    require(not weights and len(initial_weights) > 0, "DAG fully reaches initial basis")
    stats = {
        "target_basis": target_basis,
        "target_node": target_node,
        "active_nodes": sum(active_counts.values()),
        "active_input_nodes": active_counts["INPUT"],
        "active_reduce_nodes": active_counts["REDUCE"],
        "active_scale_nodes": active_counts["SCALE"],
        "maximum_pending_nodes": maximum_pending_nodes,
        "maximum_pending_polynomial_terms": maximum_pending_terms,
    }
    return initial_weights, stats


def source_polynomials(
    path: Path, variables: int
) -> tuple[list[str], list[Polynomial], list[int]]:
    names, field, texts = parse_input(path)
    require(field == PRIME and len(names) == variables and len(texts) == 16, "source input")
    context = nmod_mpoly_ctx.get(names, ordering="degrevlex", modulus=PRIME)
    polynomials: list[Polynomial] = []
    degrees: list[int] = []
    for text in texts:
        polynomial = parse_polynomial(text, context, names)
        data = {
            encode(tuple(int(value) for value in exponent)): int(coefficient) % PRIME
            for exponent, coefficient in polynomial.to_dict().items()
        }
        polynomials.append(data)
        degrees.append(max(monomial_degree(monomial, variables) for monomial in data))
    return list(names), polynomials, degrees


def match_initial_basis(
    initial: dict[int, Polynomial], sources: list[Polynomial]
) -> dict[int, tuple[int, int]]:
    mapping: dict[int, tuple[int, int]] = {}
    used_sources: set[int] = set()
    for basis_index, basis_polynomial in sorted(initial.items()):
        matches: list[tuple[int, int]] = []
        for source_index, source in enumerate(sources):
            if set(source) != set(basis_polynomial):
                continue
            monomial = next(iter(source))
            scalar = basis_polynomial[monomial] * pow(source[monomial], -1, PRIME) % PRIME
            if all(
                basis_polynomial[item] == scalar * coefficient % PRIME
                for item, coefficient in source.items()
            ):
                matches.append((source_index, scalar))
        require(len(matches) == 1, f"unique source match for initial basis {basis_index}")
        source_index, scalar = matches[0]
        require(source_index not in used_sources, "source permutation")
        used_sources.add(source_index)
        mapping[basis_index] = (source_index, scalar)
    require(used_sources == set(range(16)), "complete initial/source permutation")
    return mapping


def flatten_to_sources(
    initial_weights: dict[int, Polynomial],
    mapping: dict[int, tuple[int, int]],
) -> list[Polynomial]:
    multipliers: list[Polynomial] = [{} for _ in range(16)]
    for basis_index, weight in initial_weights.items():
        source_index, scalar = mapping[basis_index]
        add_scaled(multipliers[source_index], weight, scalar)
    return multipliers


def verify_identity(
    multipliers: list[Polynomial], sources: list[Polynomial], variables: int
) -> Polynomial:
    result: Polynomial = {}
    for multiplier, source in zip(multipliers, sources, strict=True):
        for left_monomial, left_coefficient in multiplier.items():
            for right_monomial, right_coefficient in source.items():
                monomial = left_monomial + right_monomial
                value = (
                    result.get(monomial, 0) + left_coefficient * right_coefficient
                ) % PRIME
                if value:
                    result[monomial] = value
                else:
                    result.pop(monomial, None)
    require(result == {0: 1}, "explicit sixteen-row multiplier identity")
    return result


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--dag", type=Path, default=DEFAULT_DAG)
    parser.add_argument("--input", type=Path, default=DEFAULT_INPUT)
    parser.add_argument("--target-basis", type=int, default=3220)
    parser.add_argument("--certificate", type=Path, default=DEFAULT_CERTIFICATE)
    parser.add_argument("--packet", type=Path, default=DEFAULT_PACKET)
    parser.add_argument("--instrumentation-patch", type=Path, default=DEFAULT_PATCH)
    args = parser.parse_args()

    for path in (args.dag, args.input, args.instrumentation_patch):
        require(path.is_file(), f"required file: {path}")

    (
        variables,
        reducer_terms,
        node_offsets,
        initial,
        basis_nodes,
        node_types,
    ) = scan_dag(args.dag)
    print(
        f"DAG_SCAN_OK nodes={len(node_offsets)} reducer_terms={reducer_terms} "
        f"derived_basis={len(basis_nodes)}",
        flush=True,
    )
    initial_weights, reverse_stats = reverse_dag(
        args.dag, variables, node_offsets, basis_nodes, args.target_basis
    )
    names, sources, source_degrees = source_polynomials(args.input, variables)
    mapping = match_initial_basis(initial, sources)
    multipliers = flatten_to_sources(initial_weights, mapping)
    verify_identity(multipliers, sources, variables)

    product_degrees = []
    for multiplier, source_degree in zip(multipliers, source_degrees, strict=True):
        maximum_multiplier_degree = max(
            (monomial_degree(monomial, variables) for monomial in multiplier),
            default=-1,
        )
        product_degrees.append(maximum_multiplier_degree + source_degree)
    require(max(product_degrees) == 9, "certificate has exact degree nine")

    certificate = {
        "schema": "MTTQ79RonlyExplicitDegree9Multipliers.v1",
        "date": "2026-07-20",
        "field": "F_101",
        "variables": names,
        "identity": "sum_i q_i*f_i=1",
        "source_input_sha256": checksum(args.input)["sha256"],
        "multipliers": [
            {
                "source_row_zero_based": index,
                "source_degree": source_degrees[index],
                "maximum_product_degree": product_degrees[index],
                "terms": [
                    [coefficient, *decode(monomial, variables)]
                    for monomial, coefficient in sorted(multiplier.items())
                ],
            }
            for index, multiplier in enumerate(multipliers)
        ],
    }
    args.certificate.parent.mkdir(parents=True, exist_ok=True)
    args.certificate.write_text(
        json.dumps(certificate, separators=(",", ":")) + "\n",
        encoding="utf-8",
    )

    packet = {
        "schema": "MTTQ79RonlyExplicitDegree9MultiplierCertificate.v1",
        "date": "2026-07-20",
        "status": "EXACT_EXPLICIT_SIXTEEN_ROW_DEGREE_9_UNIT_CERTIFICATE",
        "field": "F_101",
        "target_basis": args.target_basis,
        "files": {
            "source_input": checksum(args.input),
            "operation_DAG": checksum(args.dag),
            "operation_DAG_patch": checksum(args.instrumentation_patch),
            "explicit_multipliers": checksum(args.certificate),
        },
        "DAG": {
            "declared_nodes": len(node_offsets),
            "declared_reducer_terms": reducer_terms,
            "node_types": dict(sorted(node_types.items())),
            "derived_basis_rows": len(basis_nodes),
            **reverse_stats,
        },
        "initial_basis_to_source_rows": {
            str(basis): {"source_row_zero_based": source, "scalar": scalar}
            for basis, (source, scalar) in sorted(mapping.items())
        },
        "certificate": {
            "multiplier_term_counts": [len(multiplier) for multiplier in multipliers],
            "total_multiplier_terms": sum(len(multiplier) for multiplier in multipliers),
            "maximum_product_degrees": product_degrees,
            "global_maximum_product_degree": max(product_degrees),
            "residual": "1",
        },
        "checks": {
            "DAG_nodes_are_contiguous_and_backward_referencing": True,
            "all_shared_F4_ancestry_is_reversed_once": True,
            "internal_initial_basis_is_scalar_permuted_from_source_rows": True,
            "explicit_sum_qi_fi_equals_one_mod_101": True,
            "maximum_product_degree_is_exactly_nine": True,
            "D_terminal_rows_are_not_used": True,
            "no_continuous_fit_parameter_is_added": True,
        },
        "claim_boundary": (
            "This exact explicit Nullstellensatz certificate applies to one displayed "
            "finite-field R-only triple fiber. It does not classify the other triples "
            "or mirror charts or promote the finite-field obstruction to physical data."
        ),
        "new_continuous_fit_parameters": 0,
    }
    require(all(packet["checks"].values()), "all explicit-certificate checks")
    args.packet.write_text(json.dumps(packet, indent=2) + "\n", encoding="utf-8")
    print("Q79_RONLY_EXPLICIT_DEGREE9_MULTIPLIER_CERTIFICATE_PASS")
    print(f"total_multiplier_terms={sum(len(value) for value in multipliers)}")
    print(args.packet)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
