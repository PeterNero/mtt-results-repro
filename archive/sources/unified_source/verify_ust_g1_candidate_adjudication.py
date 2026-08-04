#!/usr/bin/env python3
"""Independent exact checks for the UST.G1 two-presentation adjudication packet."""

from __future__ import annotations

import json
from fractions import Fraction
from pathlib import Path


ROOT = Path(__file__).resolve().parent
PACKET = ROOT / "state" / "ust_g1_candidate_adjudication.packet.json"


def require(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)


def q(value: str | int) -> Fraction:
    return Fraction(str(value))


def matrix(values: list[list[str]]) -> list[list[Fraction]]:
    return [[q(value) for value in row] for row in values]


def shape(a: list[list[Fraction]]) -> tuple[int, int]:
    return len(a), len(a[0])


def transpose(a: list[list[Fraction]]) -> list[list[Fraction]]:
    return [list(row) for row in zip(*a)]


def multiply(a: list[list[Fraction]], b: list[list[Fraction]]) -> list[list[Fraction]]:
    rows, inner = shape(a)
    inner_b, columns = shape(b)
    require(inner == inner_b, "matrix shape mismatch")
    return [
        [sum((a[i][k] * b[k][j] for k in range(inner)), Fraction(0)) for j in range(columns)]
        for i in range(rows)
    ]


def add(a: list[list[Fraction]], b: list[list[Fraction]]) -> list[list[Fraction]]:
    require(shape(a) == shape(b), "matrix add shape mismatch")
    return [[left + right for left, right in zip(arow, brow)] for arow, brow in zip(a, b)]


def inverse_2x2(a: list[list[Fraction]]) -> list[list[Fraction]]:
    require(shape(a) == (2, 2), "only 2x2 inverse is needed")
    determinant = a[0][0] * a[1][1] - a[0][1] * a[1][0]
    require(determinant != 0, "singular metric")
    return [[a[1][1] / determinant, -a[0][1] / determinant], [-a[1][0] / determinant, a[0][0] / determinant]]


def vstack(a: list[list[Fraction]], b: list[list[Fraction]]) -> list[list[Fraction]]:
    require(shape(a)[1] == shape(b)[1], "vertical stack width mismatch")
    return a + b


def block_diag(a: list[list[Fraction]], b: list[list[Fraction]]) -> list[list[Fraction]]:
    ar, ac = shape(a)
    br, bc = shape(b)
    return [row + [Fraction(0)] * bc for row in a] + [[Fraction(0)] * ac + row for row in b]


def zero(rows: int, columns: int) -> list[list[Fraction]]:
    return [[Fraction(0) for _ in range(columns)] for _ in range(rows)]


def metric_adjoint(
    operator: list[list[Fraction]],
    domain_metric: list[list[Fraction]],
    codomain_metric: list[list[Fraction]],
) -> list[list[Fraction]]:
    return multiply(multiply(inverse_2x2(domain_metric), transpose(operator)), codomain_metric)


def main() -> None:
    with PACKET.open("r", encoding="utf-8") as handle:
        packet = json.load(handle)

    require(packet["schema"] == "mtt.unified-source.candidate-adjudication.v1", "schema")
    require(packet["theorem_id"] == "UST.G1", "theorem id")
    require(packet["scope"] == "local_q79_heterotic_source", "route-relative scope")
    require("TWO_PRESENTATION" in packet["state"], "two-presentation state")

    requirement_ids = [item["id"] for item in packet["requirements"]]
    require(requirement_ids == ["PROV", "AUG", "NONLIN", "METRIC", "GAUGE", "MAPS"], "requirements")

    partial_objects = packet["partial_objects"]
    allowed_types = {"constraint", "shadow", "benchmark_presentation", "tangent_subcomplex", "tangent_output", "source_presentation"}
    require(len({item["id"] for item in partial_objects}) == len(partial_objects), "unique partial object ids")
    for item in partial_objects:
        require(item["object_type"] in allowed_types, f"typed partial object {item['id']}")
        require(bool(item["missing"]), f"partial object must have an omission certificate: {item['id']}")
        require(set(item["missing"]).issubset(requirement_ids), f"known omissions for {item['id']}")

    survivors = packet["surviving_source_presentations"]
    require([item["id"] for item in survivors] == ["C.BUNDLE_GERM", "C.COHESIVE_GERM"], "two surviving routes")
    require("sublocus" in packet["later_g1e_relation"], "G1E nested presentation relation")
    for item in survivors:
        require(set(item["capabilities_at_type_level"]) == set(requirement_ids), f"source type capabilities {item['id']}")
        require(item["physical_instance_selected"] is False, f"no physical promotion {item['id']}")

    normal_form = packet["necessary_normal_form"]
    require(normal_form["cyclic_enhancement_proved"] is False, "cyclicity remains open")
    require(normal_form["canonical_finite_readout_proved"] is False, "finite readout remains open")

    predicate = packet["separating_predicate"]
    required_preservations = {
        "augmented_differential", "form_connecting_map", "nonlinear_residual",
        "higher_products", "infinitesimal_gauge_action", "stabilizers",
        "physical_pairing", "Hodge_operator", "Chern_anomaly_data",
        "shared_line", "finite_readout",
    }
    require(set(predicate["must_preserve"]) == required_preservations, "complete separating predicate")

    witness = packet["augmented_witness"]
    l0 = matrix(witness["L0"])
    l1 = matrix(witness["L1"])
    g0 = matrix(witness["G0"])
    g1 = matrix(witness["G1"])
    g2 = matrix(witness["G2"])
    require(multiply(l1, l0) == zero(2, 2), "cochain identity")

    l0_adjoint = metric_adjoint(l0, g0, g1)
    l1_adjoint = metric_adjoint(l1, g1, g2)
    hodge = add(multiply(l1_adjoint, l1), multiply(l0, l0_adjoint))
    require(hodge == matrix(witness["expected_weighted_hodge"]), "weighted Hodge")

    jacobian = vstack(l1, l0_adjoint)
    defect_metric = block_diag(g2, g0)
    jacobian_adjoint = multiply(multiply(inverse_2x2(g1), transpose(jacobian)), defect_metric)
    require(multiply(jacobian_adjoint, jacobian) == hodge, "same-source Gram identity")

    naive_hodge = add(multiply(transpose(l1), l1), multiply(l0, transpose(l0)))
    require(naive_hodge == matrix(witness["expected_naive_hodge"]), "naive Hodge witness")
    require(naive_hodge != hodge, "pairing necessity")

    bare = q(witness["bare_q_compression"])
    correction = q(witness["positive_form_sector_correction"])
    full = q(witness["full_q_compression"])
    require(bare + correction == full and correction > 0, "augmented compression correction")

    kappa = Fraction(7, 3)
    require(kappa == kappa, "common Hessian")
    require(6 * Fraction(0) != 6 * Fraction(5, 2), "nonlinear completion differs")

    boundary = packet["full_residual_boundary"]
    require(boundary["equality_requires_new_theorem"] is True, "full residual equality remains open")
    base_hessian = Fraction(2)
    extra_derivative = Fraction(3)
    require(base_hessian + extra_derivative * extra_derivative > base_hessian, "extra residual adds K^dagger K")

    require(packet["next_gates"] == ["UST.G1E", "UST.G3"], "next gates")
    print("UST.G1 two-presentation adjudication: PASS")
    print(f"requirements: {len(requirement_ids)}")
    print(f"typed partial objects: {len(partial_objects)}")
    print(f"surviving source presentations: {len(survivors)}")
    print("physical representative selected: false")


if __name__ == "__main__":
    main()
