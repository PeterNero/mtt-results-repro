#!/usr/bin/env python3
"""Exact finite witnesses for the UST.G2 full-residual Hodge theorem."""

from __future__ import annotations

import json
from fractions import Fraction
from pathlib import Path

from verify_ust_g1_candidate_adjudication import (
    add,
    block_diag,
    inverse_2x2,
    matrix,
    metric_adjoint,
    multiply,
    q,
    transpose,
    vstack,
)


ROOT = Path(__file__).resolve().parent
G1_PACKET = ROOT / "state" / "ust_g1_candidate_adjudication.packet.json"
PACKET = ROOT / "state" / "ust_g2_full_residual_hodge.packet.json"


def require(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)


def main() -> None:
    with G1_PACKET.open("r", encoding="utf-8") as handle:
        g1_packet = json.load(handle)
    with PACKET.open("r", encoding="utf-8") as handle:
        packet = json.load(handle)

    require(packet["schema"] == "mtt.unified-source.full-residual-hodge.v1", "schema")
    require(packet["theorem_id"] == "UST.G2", "theorem id")
    require(packet["state"] == "CLOSED_EXACT_UNIVERSAL_PHYSICAL_K_OPEN", "proof tier")

    base = g1_packet["augmented_witness"]
    l0 = matrix(base["L0"])
    l1 = matrix(base["L1"])
    g0 = matrix(base["G0"])
    g1 = matrix(base["G1"])
    g2 = matrix(base["G2"])
    l0_adjoint = metric_adjoint(l0, g0, g1)
    l1_adjoint = metric_adjoint(l1, g1, g2)
    delta_y = add(multiply(l1_adjoint, l1), multiply(l0, l0_adjoint))

    witness = packet["weighted_witness"]
    k = matrix(witness["extra_K"])
    k_adjoint = metric_adjoint(k, g1, [[Fraction(1)]])
    k_gram = multiply(k_adjoint, k)
    full = add(delta_y, k_gram)
    require(k_adjoint == matrix(witness["expected_K_adjoint"]), "weighted K adjoint")
    require(k_gram == matrix(witness["expected_K_gram"]), "positive K Gram")
    require(full == matrix(witness["expected_full_hessian"]), "full weighted Hessian")

    # Directly check that stacking the base and extra rows gives the same Gram.
    base_jacobian = vstack(l1, l0_adjoint)
    full_jacobian = vstack(base_jacobian, k)
    full_target_metric = block_diag(block_diag(g2, g0), [[Fraction(1)]])
    full_adjoint = multiply(multiply(inverse_2x2(g1), transpose(full_jacobian)), full_target_metric)
    require(multiply(full_adjoint, full_jacobian) == full, "stacked full-residual Gram")

    scalar = packet["general_metric_scalar_witness"]
    j = q(scalar["J"])
    kval = q(scalar["K"])
    w0 = q(scalar["W0"])
    cross = q(scalar["C"])
    wr = q(scalar["WR"])
    general_hessian = j * w0 * j + j * cross * kval + kval * cross * j + kval * wr * kval
    require(general_hessian == q(scalar["expected_hessian"]), "general target metric formula")

    # Kernel intersection witness: Delta=diag(0,2), K=[1,0]. Their kernels
    # are span(e1) and span(e2), while Delta + K^T K = diag(1,2) is invertible.
    delta_example = [[Fraction(0), Fraction(0)], [Fraction(0), Fraction(2)]]
    k_example = [[Fraction(1), Fraction(0)]]
    k_example_gram = multiply(transpose(k_example), k_example)
    full_example = add(delta_example, k_example_gram)
    e1 = [[Fraction(1)], [Fraction(0)]]
    e2 = [[Fraction(0)], [Fraction(1)]]
    require(multiply(delta_example, e1) == [[Fraction(0)], [Fraction(0)]], "Delta kernel basis")
    require(multiply(k_example, e2) == [[Fraction(0)]], "K kernel basis")
    require(multiply(k_example, e1) != [[Fraction(0)]], "kernel intersection is trivial")
    require(full_example == [[Fraction(1), Fraction(0)], [Fraction(0), Fraction(2)]], "full kernel witness")
    require(full_example[0][0] * full_example[1][1] - full_example[0][1] * full_example[1][0] != 0, "full operator invertible")

    identity = [[Fraction(1), Fraction(0)], [Fraction(0), Fraction(1)]]
    two_identity = [[Fraction(2), Fraction(0)], [Fraction(0), Fraction(2)]]
    absorption_full = add(identity, multiply(transpose(two_identity), two_identity))
    five_identity = [[Fraction(5), Fraction(0)], [Fraction(0), Fraction(5)]]
    require(absorption_full == five_identity, "exact scale absorption witness")

    physical = packet["physical_instantiation"]
    require(not any(physical.values()), "no physical instantiation promoted")
    require(packet["next_gate"] == "UST.G1E", "next gate")
    print("UST.G2 full-residual Hodge theorem: PASS")
    print("universal decomposition: Delta_Y + K^dagger K")
    print("physical K selected: false")


if __name__ == "__main__":
    main()
