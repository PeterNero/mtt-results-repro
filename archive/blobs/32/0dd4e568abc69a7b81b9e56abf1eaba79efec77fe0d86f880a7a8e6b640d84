#!/usr/bin/env python3
"""Exact finite checks for the UST.G3B common-scale quotient theorem."""

from __future__ import annotations

import json
from fractions import Fraction
from pathlib import Path

from verify_ust_g1_candidate_adjudication import add, matrix, multiply


ROOT = Path(__file__).resolve().parent
PACKET = ROOT / "state" / "ust_g3b_scale_orbit.packet.json"
LOCK = ROOT / "state" / "upstream-lock.json"


def require(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)


def scale(a: list[list[Fraction]], value: Fraction) -> list[list[Fraction]]:
    return [[value * entry for entry in row] for row in a]


def main() -> None:
    packet = json.loads(PACKET.read_text(encoding="utf-8"))
    lock = json.loads(LOCK.read_text(encoding="utf-8"))
    require(packet["schema"] == "mtt.unified-source.scale-orbit.v1", "schema")
    require(packet["theorem_id"] == "UST.G3B", "theorem id")
    require(packet["state"] == "CLOSED_EXACT_COMMON_SCALE_PHYSICAL_NORMALIZATION_OPEN", "tier")

    closure = next(item for item in lock["repositories"] if item["id"] == "closure-dynamics")
    sources = {item["path"]: item.get("sha256") for item in closure["sources"]}
    source = packet["source_lock"]
    require(sources.get(source["path"]) == source["sha256"], "locked Hodge-scale theorem")

    lam = Fraction(7)
    h = matrix([["0", "0", "0"], ["0", "2", "0"], ["0", "0", "5"]])
    h_lam = scale(h, lam)
    require(h_lam == matrix([["0", "0", "0"], ["0", "14", "0"], ["0", "0", "35"]]), "uniform spectrum scaling")

    p0 = matrix([["1", "0", "0"], ["0", "0", "0"], ["0", "0", "0"]])
    require(multiply(h, p0) == multiply(h_lam, p0) == matrix([["0", "0", "0"], ["0", "0", "0"], ["0", "0", "0"]]), "same harmonic projector")
    require(Fraction(5, 2) == Fraction(35, 14), "positive spectral ratio")

    green = matrix([["0", "0", "0"], ["0", "1/2", "0"], ["0", "0", "1/5"]])
    green_lam = matrix([["0", "0", "0"], ["0", "1/14", "0"], ["0", "0", "1/35"]])
    require(green_lam == scale(green, Fraction(1, 7)), "Green inverse scaling")
    require(multiply(h_lam, green_lam) == matrix([["0", "0", "0"], ["0", "1", "0"], ["0", "0", "1"]]), "reduced inverse")

    # Newton correction: (lambda H)^-1 (lambda g) = H^-1 g.
    h_pos_inv = matrix([["1/2", "0"], ["0", "1/5"]])
    h_lam_pos_inv = matrix([["1/14", "0"], ["0", "1/35"]])
    gradient = matrix([["4"], ["15"]])
    gradient_lam = scale(gradient, lam)
    require(multiply(h_pos_inv, gradient) == multiply(h_lam_pos_inv, gradient_lam) == matrix([["2"], ["3"]]), "Newton scale invariance")

    # The UST.G2 correction scales with the same common target weight.
    delta = matrix([["2", "0"], ["0", "3"]])
    k_gram = matrix([["1", "1"], ["1", "1"]])
    full = add(delta, k_gram)
    require(add(scale(delta, lam), scale(k_gram, lam)) == scale(full, lam), "full residual common scaling")

    # Independent sector weights are not a common ray.
    relative = add(scale(delta, Fraction(2)), scale(k_gram, Fraction(3)))
    require(relative != scale(full, Fraction(2)), "relative weights alter shape")
    require(relative != scale(full, Fraction(3)), "relative weights are not one ray")

    trace_full = sum(full[i][i] for i in range(2))
    trace_scaled = sum(scale(full, lam)[i][i] for i in range(2))
    normalized = scale(full, Fraction(1, 1) / trace_full)
    normalized_scaled = scale(scale(full, lam), Fraction(1, 1) / trace_scaled)
    require(normalized == normalized_scaled, "normalized finite operator")

    ledger = packet["parameter_ledger"]
    require(ledger["dimensionless_Hodge_shape_parameters_after_relative_selection"] == 0, "zero relative shape parameters after selection")
    require(ledger["maximum_common_positive_normalization_rays"] == 1, "one positive ray")
    require(not any(packet["physical_instantiation"].values()), "physical normalization remains open")

    print("UST.G3B scale-orbit theorem: PASS")
    print("dimensionless Hodge-shape parameters after relative selection: 0")
    print("maximum common positive normalization rays: 1")
    print("physical absolute scale selected: false")


if __name__ == "__main__":
    main()
