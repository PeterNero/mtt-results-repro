#!/usr/bin/env python3
"""Exact compiler and validator for UST.G3C target-metric certificates."""

from __future__ import annotations

import argparse
import copy
import json
import re
from fractions import Fraction
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parent
DEFAULT_PACKET = ROOT / "state" / "ust_g3c_reference_metric.packet.json"
HEX64 = re.compile(r"^[0-9a-f]{64}$")
GRADES = {"PASS", "FAIL", "PARTIAL", "CONDITIONAL", "OPEN", "NOT_SOURCE"}
SCOPES = {
    "finite_exact_reference",
    "finite_exact_readout",
    "finite_truncation_only",
    "continuum_complete",
}
FIELDS = {"rational_real_symmetric", "rational_complex_realification"}
CONSTRAINT_KINDS = {
    "finite_symmetry_invariance",
    "infinitesimal_invariance",
    "self_adjointness",
    "skew_adjointness",
    "complex_structure_compatibility",
    "metric_binding_intertwiner",
    "general_homogeneous_source_constraint",
}


def require(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)


def q(value: str | int) -> Fraction:
    return Fraction(str(value))


def matrix(values: list[list[str | int]], n: int, label: str) -> list[list[Fraction]]:
    require(len(values) == n, f"{label}: expected {n} rows")
    require(all(len(row) == n for row in values), f"{label}: expected {n} columns")
    return [[q(value) for value in row] for row in values]


def transpose(a: list[list[Fraction]]) -> list[list[Fraction]]:
    return [list(row) for row in zip(*a)]


def symmetric_pairs(n: int) -> list[tuple[int, int]]:
    return [(i, j) for i in range(n) for j in range(i, n)]


def compile_constraint_rows(packet: dict[str, Any]) -> tuple[list[list[Fraction]], list[tuple[int, int]]]:
    n = packet["dimension"]
    pairs = symmetric_pairs(n)
    rows: list[list[Fraction]] = []
    constraint_ids: set[str] = set()

    for constraint in packet["constraints"]:
        require(
            set(constraint) == {"id", "kind", "evidence_grade", "provenance", "terms"},
            f"unexpected fields in constraint: {constraint.get('id', '<missing>')}",
        )
        constraint_id = constraint["id"]
        require(constraint_id not in constraint_ids, f"duplicate constraint id: {constraint_id}")
        constraint_ids.add(constraint_id)
        require(constraint["evidence_grade"] in GRADES, f"bad grade: {constraint_id}")
        require(constraint["kind"] in CONSTRAINT_KINDS, f"bad kind: {constraint_id}")
        require(
            set(constraint["provenance"]) == {"source_hash", "artifact", "locator"},
            f"bad provenance fields: {constraint_id}",
        )
        require(
            all(bool(constraint["provenance"][key]) for key in ("source_hash", "artifact", "locator")),
            f"incomplete provenance: {constraint_id}",
        )
        require(bool(constraint["terms"]), f"empty constraint: {constraint_id}")

        parsed_terms: list[tuple[Fraction, list[list[Fraction]], list[list[Fraction]]]] = []
        for term_index, term in enumerate(constraint["terms"]):
            require(set(term) == {"coefficient", "left", "right"}, f"bad term fields: {constraint_id}")
            coefficient = q(term["coefficient"])
            left = matrix(term["left"], n, f"{constraint_id}.term[{term_index}].left")
            right = matrix(term["right"], n, f"{constraint_id}.term[{term_index}].right")
            parsed_terms.append((coefficient, left, right))

        # For W_{pq}, compute the coefficient of (L^T W R)_{ij} directly.
        # This avoids a dense matrix product for every symmetric basis vector.
        for row_index in range(n):
            for column_index in range(n):
                row: list[Fraction] = []
                for p, q_index in pairs:
                    value = Fraction(0)
                    for coefficient, left, right in parsed_terms:
                        value += coefficient * left[p][row_index] * right[q_index][column_index]
                        if p != q_index:
                            value += coefficient * left[q_index][row_index] * right[p][column_index]
                    row.append(value)
                if any(entry != 0 for entry in row):
                    rows.append(row)

    return rows, pairs


def rref(rows: list[list[Fraction]], columns: int) -> tuple[list[list[Fraction]], list[int]]:
    work = [row[:] for row in rows if any(entry != 0 for entry in row)]
    pivot_columns: list[int] = []
    pivot_row = 0

    for column in range(columns):
        candidate = next((index for index in range(pivot_row, len(work)) if work[index][column] != 0), None)
        if candidate is None:
            continue
        work[pivot_row], work[candidate] = work[candidate], work[pivot_row]
        divisor = work[pivot_row][column]
        work[pivot_row] = [entry / divisor for entry in work[pivot_row]]
        for row_index in range(len(work)):
            if row_index == pivot_row:
                continue
            factor = work[row_index][column]
            if factor != 0:
                work[row_index] = [
                    entry - factor * pivot_entry
                    for entry, pivot_entry in zip(work[row_index], work[pivot_row])
                ]
        pivot_columns.append(column)
        pivot_row += 1
        if pivot_row == len(work):
            break

    return work, pivot_columns


def nullspace_basis(rows: list[list[Fraction]], columns: int) -> list[list[Fraction]]:
    reduced, pivots = rref(rows, columns)
    free_columns = [column for column in range(columns) if column not in pivots]
    basis: list[list[Fraction]] = []
    for free_column in free_columns:
        vector = [Fraction(0) for _ in range(columns)]
        vector[free_column] = Fraction(1)
        for row_index, pivot_column in enumerate(pivots):
            vector[pivot_column] = -reduced[row_index][free_column]
        basis.append(vector)
    return basis


def symmetric_vector(a: list[list[Fraction]], pairs: list[tuple[int, int]]) -> list[Fraction]:
    return [a[i][j] for i, j in pairs]


def determinant(a: list[list[Fraction]]) -> Fraction:
    n = len(a)
    work = [row[:] for row in a]
    result = Fraction(1)
    sign = Fraction(1)
    for column in range(n):
        pivot = next((row for row in range(column, n) if work[row][column] != 0), None)
        if pivot is None:
            return Fraction(0)
        if pivot != column:
            work[column], work[pivot] = work[pivot], work[column]
            sign = -sign
        pivot_value = work[column][column]
        result *= pivot_value
        for row in range(column + 1, n):
            factor = work[row][column] / pivot_value
            for entry in range(column + 1, n):
                work[row][entry] -= factor * work[column][entry]
    return sign * result


def is_positive_definite(a: list[list[Fraction]]) -> bool:
    return all(determinant([row[:size] for row in a[:size]]) > 0 for size in range(1, len(a) + 1))


def validate_packet(packet: dict[str, Any]) -> dict[str, Any]:
    required = {
        "schema", "candidate_id", "source_orbit_id", "source_hash", "scope",
        "evidence_grade", "field_representation", "dimension",
        "complete_physical_target", "continuum_completeness_certificate",
        "constraints", "positive_witness", "claimed_solution_space_dimension",
        "empirical_inputs", "physical_promotion_requested",
    }
    require(set(packet) == required, "missing or unexpected packet fields")
    require(packet["schema"] == "mtt.unified-source.target-metric-certificate.v1", "schema")
    require(packet["scope"] in SCOPES, "scope")
    require(packet["evidence_grade"] in GRADES, "evidence grade")
    require(packet["field_representation"] in FIELDS, "field representation")
    require(isinstance(packet["dimension"], int) and packet["dimension"] > 0, "dimension")
    require(isinstance(packet["constraints"], list), "constraints")
    require(isinstance(packet["empirical_inputs"], list), "empirical inputs")
    require(
        set(packet["continuum_completeness_certificate"]) == {"state", "source_hash", "artifact", "locator"},
        "continuum completeness fields",
    )

    rows, pairs = compile_constraint_rows(packet)
    basis = nullspace_basis(rows, len(pairs))
    solution_dimension = len(basis)
    require(
        packet["claimed_solution_space_dimension"] == solution_dimension,
        f"claimed metric-cone dimension {packet['claimed_solution_space_dimension']} != exact {solution_dimension}",
    )

    witness = matrix(packet["positive_witness"], packet["dimension"], "positive_witness")
    require(witness == transpose(witness), "positive witness must be symmetric")
    witness_vector = symmetric_vector(witness, pairs)
    require(
        all(sum((coefficient * value for coefficient, value in zip(row, witness_vector)), Fraction(0)) == 0 for row in rows),
        "positive witness violates source constraints",
    )
    positive_witness = is_positive_definite(witness)
    require(positive_witness, "witness is not positive definite")

    unique_positive_ray = solution_dimension == 1
    same_source = all(
        constraint["evidence_grade"] == "PASS"
        and constraint["provenance"]["source_hash"] == packet["source_hash"]
        for constraint in packet["constraints"]
    )
    continuum = packet["continuum_completeness_certificate"]
    continuum_complete = (
        packet["scope"] == "continuum_complete"
        and continuum["state"] == "PASS"
        and continuum["source_hash"] == packet["source_hash"]
    )
    complex_structure_present = (
        packet["field_representation"] == "rational_real_symmetric"
        or any(item["kind"] == "complex_structure_compatibility" for item in packet["constraints"])
    )
    promotion_conditions = {
        "top_level_pass": packet["evidence_grade"] == "PASS",
        "source_hash_is_sha256": bool(HEX64.fullmatch(packet["source_hash"])),
        "same_source_constraints_pass": same_source,
        "complete_physical_target": packet["complete_physical_target"] is True,
        "continuum_complete": continuum_complete,
        "complex_structure_present_when_required": complex_structure_present,
        "unique_positive_ray": unique_positive_ray,
        "no_empirical_metric_inputs": packet["empirical_inputs"] == [],
    }
    physically_selected = all(promotion_conditions.values())
    if packet["physical_promotion_requested"]:
        failed = [name for name, passed in promotion_conditions.items() if not passed]
        require(not failed, "physical promotion requested with failed conditions: " + ", ".join(failed))

    return {
        "equation_count": len(rows),
        "symmetric_variable_count": len(pairs),
        "solution_space_dimension": solution_dimension,
        "relative_metric_directions_after_common_scale": solution_dimension - 1,
        "positive_witness": positive_witness,
        "unique_positive_ray": unique_positive_ray,
        "same_source": same_source,
        "physically_selected": physically_selected,
        "promotion_conditions": promotion_conditions,
    }


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--candidate", type=Path, default=DEFAULT_PACKET)
    args = parser.parse_args()
    packet = json.loads(args.candidate.read_text(encoding="utf-8"))
    result = validate_packet(packet)

    if packet["candidate_id"] == "UST.G3C.REFERENCE.SIGNED_PERMUTATION":
        reduced_packet = dict(packet)
        reduced_packet["constraints"] = packet["constraints"][:2]
        reduced_packet["claimed_solution_space_dimension"] = 3
        reduced_result = validate_packet(reduced_packet)
        require(reduced_result["solution_space_dimension"] == 3, "disconnected signed axes retain three rays")

        spliced_packet = copy.deepcopy(packet)
        spliced_packet["constraints"][0]["provenance"]["source_hash"] = "REFERENCE.OTHER.ORBIT"
        require(not validate_packet(spliced_packet)["same_source"], "source splicing must be detected")

        false_promotion = copy.deepcopy(packet)
        false_promotion["physical_promotion_requested"] = True
        try:
            validate_packet(false_promotion)
        except AssertionError as error:
            require("physical promotion requested" in str(error), "unexpected false-promotion failure")
        else:
            raise AssertionError("finite reference must not promote as a physical continuum metric")

    print("UST.G3C target-metric certificate: PASS")
    print(f"candidate: {packet['candidate_id']}")
    print(f"symmetric variables: {result['symmetric_variable_count']}")
    print(f"exact constraint rank: {result['symmetric_variable_count'] - result['solution_space_dimension']}")
    print(f"solution-space dimension: {result['solution_space_dimension']}")
    print(f"unique positive ray: {str(result['unique_positive_ray']).lower()}")
    print(f"physical relative metric selected: {str(result['physically_selected']).lower()}")


if __name__ == "__main__":
    main()
