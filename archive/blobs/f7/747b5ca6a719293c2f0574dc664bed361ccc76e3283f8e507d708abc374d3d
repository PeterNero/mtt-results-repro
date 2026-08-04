#!/usr/bin/env python3
"""Certify the explicit minimum-degree-nine q79 R-only fiber identity."""

from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "candidate_data" / "q79_Ronly_triple_fiber_min_degree"
PRIME = 101
PARENT_ROWS = (1, 2, 3, 4, 5, 6, 14, 15, 16, 17, 7, 8, 9, 10, 11, 12)
ASSIGNMENTS = {"u0": 1, "u1": 1, "u2": 1, "u3": 1, "v": 1}
Exponent = tuple[int, ...]
Polynomial = dict[Exponent, int]


def require(condition: bool, label: str) -> None:
    if not condition:
        raise AssertionError(label)


def checksum(path: Path) -> dict[str, object]:
    digest = hashlib.sha256()
    with path.open("rb") as stream:
        for block in iter(lambda: stream.read(1 << 20), b""):
            digest.update(block)
    return {
        "path": path.relative_to(ROOT).as_posix(),
        "bytes": path.stat().st_size,
        "sha256": digest.hexdigest(),
    }


def normalized_text(path: Path) -> str:
    return path.read_text(encoding="ascii").replace("\r\n", "\n")


def parse_input(path: Path) -> tuple[tuple[str, ...], int, list[str]]:
    lines = normalized_text(path).splitlines()
    require(len(lines) >= 3, f"nonempty msolve input {path.name}")
    return (
        tuple(lines[0].split(",")),
        int(lines[1]),
        [line.removesuffix(",") for line in lines[2:] if line],
    )


def parse_polynomial(text: str, names: tuple[str, ...]) -> Polynomial:
    positions = {name: index for index, name in enumerate(names)}
    value = text.strip().lstrip("[").rstrip(",]:")
    result: Polynomial = {}
    if value == "0":
        return result
    for raw_term in value.split("+"):
        factors = raw_term.strip().split("*")
        first_is_coefficient = factors[0].isdigit()
        coefficient = int(factors[0]) % PRIME if first_is_coefficient else 1
        exponent = [0] * len(names)
        for factor in factors[1 if first_is_coefficient else 0 :]:
            if "^" in factor:
                name, power = factor.split("^", 1)
                value_power = int(power)
            else:
                name, value_power = factor, 1
            require(name in positions, f"known variable {name}")
            exponent[positions[name]] += value_power
        key = tuple(exponent)
        coefficient = (result.get(key, 0) + coefficient) % PRIME
        if coefficient:
            result[key] = coefficient
        else:
            result.pop(key, None)
    return result


def specialize(
    polynomial: Polynomial, names: tuple[str, ...], target_names: tuple[str, ...]
) -> Polynomial:
    target_positions = tuple(names.index(name) for name in target_names)
    assigned_positions = {
        names.index(name): value for name, value in ASSIGNMENTS.items()
    }
    result: Polynomial = {}
    for exponent, coefficient in polynomial.items():
        for position, value in assigned_positions.items():
            coefficient = coefficient * pow(value, exponent[position], PRIME) % PRIME
        target_exponent = tuple(exponent[position] for position in target_positions)
        coefficient = (result.get(target_exponent, 0) + coefficient) % PRIME
        if coefficient:
            result[target_exponent] = coefficient
        else:
            result.pop(target_exponent, None)
    return result


def homogenize(polynomial: Polynomial) -> Polynomial:
    degree = max(sum(exponent) for exponent in polynomial)
    return {
        exponent + (degree - sum(exponent),): coefficient
        for exponent, coefficient in polynomial.items()
    }


def add_product(residual: Polynomial, left: Polynomial, right: Polynomial) -> None:
    for left_exponent, left_coefficient in left.items():
        for right_exponent, right_coefficient in right.items():
            exponent = tuple(
                a + b for a, b in zip(left_exponent, right_exponent, strict=True)
            )
            coefficient = (
                residual.get(exponent, 0) + left_coefficient * right_coefficient
            ) % PRIME
            if coefficient:
                residual[exponent] = coefficient
            else:
                residual.pop(exponent, None)


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--parent", type=Path, default=DATA / "parent_space5_class1_inverse_root.msolve.in")
    parser.add_argument("--selected", type=Path, default=DATA / "selected_full14.msolve.in")
    parser.add_argument("--multipliers", type=Path, default=DATA / "explicit_degree9_multipliers.json")
    parser.add_argument("--homogeneous", type=Path, default=DATA / "homogeneous_D8_D9.msolve.in")
    parser.add_argument("--normal-forms", type=Path, default=DATA / "homogeneous_D8_D9.msolve.out")
    parser.add_argument("--generation-packet", type=Path, default=DATA / "explicit_degree9_generation.packet.json")
    parser.add_argument("--tail-patch", type=Path, default=DATA / "msolve_f4_tail_dump.patch")
    parser.add_argument("--ancestry-patch", type=Path, default=DATA / "msolve_f4_ancestry_dump.patch")
    parser.add_argument("--provenance-patch", type=Path, default=DATA / "msolve_f4_provenance_degree.patch")
    parser.add_argument("--operation-patch", type=Path, default=DATA / "msolve_f4_operation_dag.patch")
    parser.add_argument("--output", type=Path, default=ROOT / "certificates" / "Q79_Ronly_Triple_Fiber_Explicit_Minimum_Degree9_v2.json")
    args = parser.parse_args()

    required = (
        args.parent,
        args.selected,
        args.multipliers,
        args.homogeneous,
        args.normal_forms,
        args.generation_packet,
        args.tail_patch,
        args.ancestry_patch,
        args.provenance_patch,
        args.operation_patch,
    )
    for path in required:
        require(path.is_file(), f"required file: {path}")

    parent_names, parent_field, parent_texts = parse_input(args.parent)
    selected_names, selected_field, selected_texts = parse_input(args.selected)
    require(parent_field == selected_field == PRIME, "common field F_101")
    require(len(parent_names) == 19 and len(parent_texts) == 22, "parent dimensions")
    require(len(selected_names) == 14 and len(selected_texts) == 16, "selected dimensions")
    require(
        selected_names == tuple(name for name in parent_names if name not in ASSIGNMENTS),
        "selected variable order",
    )
    parent = [parse_polynomial(text, parent_names) for text in parent_texts]
    selected = [parse_polynomial(text, selected_names) for text in selected_texts]
    specialized = [specialize(polynomial, parent_names, selected_names) for polynomial in parent]
    require(not specialized[0] and not specialized[13], "endpoint equations vanish")
    require(
        [specialized[index] for index in PARENT_ROWS] == selected,
        "sixteen rows are exact parent specializations",
    )

    homogeneous_names, homogeneous_field, homogeneous_texts = parse_input(args.homogeneous)
    require(
        homogeneous_field == PRIME
        and homogeneous_names == selected_names + ("t",)
        and len(homogeneous_texts) == 18,
        "homogeneous input shape",
    )
    homogeneous_rows = [
        parse_polynomial(text, homogeneous_names) for text in homogeneous_texts
    ]
    require(homogeneous_rows[:16] == [homogenize(row) for row in selected], "exact row homogenization")
    t8 = (0,) * 14 + (8,)
    t9 = (0,) * 14 + (9,)
    require(homogeneous_rows[16:] == [{t8: 1}, {t9: 1}], "t8 and t9 targets")
    require("".join(normalized_text(args.normal_forms).split()) == "[1*t^8,0]:", "exact normal forms")

    explicit = json.loads(args.multipliers.read_text(encoding="utf-8"))
    require(explicit.get("schema") == "MTTQ79RonlyExplicitDegree9Multipliers.v1", "multiplier schema")
    require(explicit.get("field") == "F_101" and explicit.get("variables") == list(selected_names), "multiplier domain")
    require(explicit.get("source_input_sha256") == checksum(args.selected)["sha256"], "multiplier source binding")
    multiplier_rows = explicit.get("multipliers")
    require(isinstance(multiplier_rows, list) and len(multiplier_rows) == 16, "sixteen multipliers")
    residual: Polynomial = {}
    term_counts: list[int] = []
    product_degrees: list[int] = []
    for index, (payload, source) in enumerate(zip(multiplier_rows, selected, strict=True)):
        source_degree = max(sum(exponent) for exponent in source)
        require(payload.get("source_row_zero_based") == index, f"multiplier row {index}")
        require(payload.get("source_degree") == source_degree, f"source degree {index}")
        multiplier: Polynomial = {}
        for term in payload.get("terms", []):
            require(isinstance(term, list) and len(term) == 15, f"term width {index}")
            coefficient, exponent = term[0], tuple(term[1:])
            require(
                isinstance(coefficient, int)
                and 0 < coefficient < PRIME
                and all(isinstance(value, int) and value >= 0 for value in exponent),
                f"term domain {index}",
            )
            require(exponent not in multiplier, f"unique monomial {index}")
            multiplier[exponent] = coefficient
        require(multiplier, f"nonempty multiplier {index}")
        product_degree = max(sum(exponent) for exponent in multiplier) + source_degree
        require(payload.get("maximum_product_degree") == product_degree, f"product degree {index}")
        term_counts.append(len(multiplier))
        product_degrees.append(product_degree)
        add_product(residual, multiplier, source)
    require(residual == {(0,) * 14: 1}, "sum_i q_i f_i equals one")
    require(max(product_degrees) == 9, "explicit degree-nine upper bound")

    generation = json.loads(args.generation_packet.read_text(encoding="utf-8"))
    require(generation.get("status") == "EXACT_EXPLICIT_SIXTEEN_ROW_DEGREE_9_UNIT_CERTIFICATE", "generation status")
    require(generation["files"]["source_input"]["sha256"] == checksum(args.selected)["sha256"], "generation source binding")
    require(generation["files"]["explicit_multipliers"]["sha256"] == checksum(args.multipliers)["sha256"], "generation payload binding")
    require(generation["files"]["operation_DAG_patch"]["sha256"] == checksum(args.operation_patch)["sha256"], "operation patch binding")
    require(
        generation["DAG"]["declared_nodes"] == 45786
        and generation["DAG"]["declared_reducer_terms"] == 15217730
        and generation["DAG"]["target_basis"] == 3220
        and generation["DAG"]["target_node"] == 44140,
        "generation DAG dimensions",
    )

    files = {
        "parent_input": checksum(args.parent),
        "selected_sixteen_row_input": checksum(args.selected),
        "explicit_multipliers": checksum(args.multipliers),
        "homogeneous_membership_input": checksum(args.homogeneous),
        "normal_form_output": checksum(args.normal_forms),
        "generation_packet": checksum(args.generation_packet),
        "F4_tail_patch": checksum(args.tail_patch),
        "F4_ancestry_patch": checksum(args.ancestry_patch),
        "F4_provenance_degree_patch": checksum(args.provenance_patch),
        "operation_DAG_patch": checksum(args.operation_patch),
    }
    packet = {
        "schema": "MTTQ79RonlyTripleFiberExplicitMinimumDegree9.v2",
        "date": "2026-07-20",
        "status": "EXACT_EXPLICIT_MINIMUM_DEGREE_9_R_ONLY_TRIPLE_FIBER_CERTIFICATE",
        "field": "F_101",
        "fiber": {
            "space": 5,
            "scalar_square_class_representative": 1,
            "u1": 1,
            "a_equals_v_times_u3": 1,
            "v": 1,
            "forced_assignments": ASSIGNMENTS,
        },
        "selected_rows": {
            "parent_rows_in_certificate_order": list(PARENT_ROWS),
            "recurrence_parent_rows": list(PARENT_ROWS[:10]),
            "R_terminal_parent_rows": list(PARENT_ROWS[10:]),
            "D_terminal_rows_used": [],
        },
        "files": files,
        "parent_specialization": {
            "parent_variables": len(parent_names),
            "selected_variables": len(selected_names),
            "selected_rows": len(selected),
            "endpoint_parent_rows_vanishing": [0, 13],
            "exact_rowwise_match": True,
        },
        "explicit_identity": {
            "identity": "sum_i q_i*f_i=1 in F_101[h1,...,u7]",
            "multiplier_term_counts": term_counts,
            "total_multiplier_terms": sum(term_counts),
            "maximum_product_degrees": product_degrees,
            "global_maximum_product_degree": max(product_degrees),
            "computed_residual": "1",
        },
        "minimum_degree_theorem": {
            "homogeneous_ideal": "J=<f_1^h,...,f_16^h>",
            "normal_forms": {"NF_J(t^8)": "t^8", "NF_J(t^9)": "0"},
            "minimum_maximum_product_total_degree": 9,
            "argument": (
                "Because J is homogeneous, t^D belongs to J exactly when the affine "
                "identity has multipliers with deg(q_i)+deg(f_i)<=D. The nonzero "
                "normal form of t^8 excludes degree at most 8; the explicit identity "
                "and zero normal form of t^9 establish degree 9. Any lower degree "
                "would imply t^8 in J after multiplication by a power of t."
            ),
        },
        "generation_provenance": {
            "method": "one-thread patched official msolve F4 operation DAG, reversed once to the initial generators",
            "msolve_release": "0.10.1",
            "patch_application_order": [
                "msolve_f4_tail_dump.patch",
                "msolve_f4_ancestry_dump.patch",
                "msolve_f4_provenance_degree.patch",
                "msolve_f4_operation_dag.patch",
            ],
            "DAG_sha256": generation["files"]["operation_DAG"]["sha256"],
            "DAG_bytes": generation["files"]["operation_DAG"]["bytes"],
            "declared_nodes": generation["DAG"]["declared_nodes"],
            "declared_reducer_terms": generation["DAG"]["declared_reducer_terms"],
            "independent_verification_requires_DAG": False,
        },
        "checks": {
            "selected_rows_are_exact_parent_specializations": True,
            "all_sixteen_homogenizations_are_recomputed": True,
            "normal_form_of_t8_is_nonzero": True,
            "normal_form_of_t9_is_zero": True,
            "explicit_sum_qi_fi_equals_one_mod_101": True,
            "certificate_degree_nine_is_minimal": True,
            "D_terminal_rows_are_not_used": True,
            "complete_F4_instrumentation_patch_stack_is_packaged": True,
            "no_continuous_fit_parameter_is_added": True,
        },
        "claim_boundary": (
            "This exact theorem applies to one displayed finite-field R-only triple "
            "fiber. It does not classify the other scalar triples or mirror charts, "
            "nor promote the finite-field obstruction to selected physical HYM/QG data."
        ),
        "new_continuous_fit_parameters": 0,
    }
    require(all(packet["checks"].values()), "all closure checks")
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(packet, indent=2) + "\n", encoding="utf-8", newline="\n")
    print("Q79_RONLY_EXPLICIT_MINIMUM_DEGREE9_PASS")
    print(f"multiplier_terms={sum(term_counts)} residual_terms={len(residual)}")
    print(args.output)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
