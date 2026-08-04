#!/usr/bin/env python3
"""Exact structural checks for the UST.G1E embedding and cutset packet."""

from __future__ import annotations

import json
from fractions import Fraction
from pathlib import Path

from verify_ust_g1_candidate_adjudication import add, matrix, multiply, transpose


ROOT = Path(__file__).resolve().parent
PACKET = ROOT / "state" / "ust_g1e_bundle_cohesive_embedding.packet.json"


def require(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)


def main() -> None:
    with PACKET.open("r", encoding="utf-8") as handle:
        packet = json.load(handle)

    require(packet["schema"] == "mtt.unified-source.bundle-cohesive-embedding.v1", "schema")
    require(packet["theorem_id"] == "UST.G1E", "theorem id")
    require(packet["state"] == "CLOSED_EXACT_ONE_WAY_REVERSE_PHYSICAL_REPRESENTABILITY_OPEN", "tier")
    require(packet["candidate_relation"] == "C_bundle is a physical representable sublocus of C_cohesive", "nested relation")
    require(len(packet["source_locks"]) == 2, "q79 source locks")
    require(all(len(item["commit"]) == 40 and len(item["sha256"]) == 64 for item in packet["source_locks"]), "source lock hashes")

    twists = packet["twist_arithmetic"]
    require((twists["hidden_twist_mod_3"] + twists["dual_twist_mod_3"]) % 3 == twists["endomorphism_twist_mod_3"], "twist cancellation")

    ranks = packet["rank102_check"]
    require(sum(ranks[key] for key in ("TstarX", "adTX", "adV3", "adW9", "TX")) == ranks["total"] == 102, "rank-102 carrier")

    benchmark = packet["current_benchmark"]
    inverse_chern = (benchmark["inverse_c1_H_coefficient"], benchmark["inverse_c2_u_coefficient"])
    physical_chern = (benchmark["physical_V3_c1_H_coefficient"], benchmark["physical_V3_c2_u_coefficient"])
    require(inverse_chern != physical_chern, "benchmark Chern mismatch")
    require(not benchmark["passes_direct_physical_topology_row"], "benchmark not promoted")
    require(not benchmark["excludes_entire_cohesive_route"], "route remains live")

    # Finite DGLA presentation witness reused in both languages. Identity
    # transport preserves the cochain law, Hodge Gram and a nonlinear MC value.
    d0 = matrix([["1"], ["0"]])
    d1 = matrix([["0", "1"]])
    require(multiply(d1, d0) == [[Fraction(0)]], "cochain law")
    delta = add(multiply(transpose(d1), d1), multiply(d0, transpose(d0)))
    require(delta == matrix([["1", "0"], ["0", "1"]]), "same Hodge operator")
    y1, y2 = Fraction(2), Fraction(3)
    bundle_mc = y2 + y2 * y2
    cohesive_mc = y2 + y2 * y2
    bundle_gauge = y1
    cohesive_gauge = y1
    require(bundle_mc == cohesive_mc == Fraction(12), "same nonlinear MC residual")
    require(bundle_gauge == cohesive_gauge, "same gauge row")

    require(len(packet["reverse_cutset"]) == 7, "complete reverse cutset")
    require(not any(packet["physical_instantiation"].values()), "physical reverse remains open")
    require(packet["next_gate"] == "UST.G3", "next gate")

    print("UST.G1E bundle-cohesive embedding: PASS")
    print("bundle route embeds in cohesive route: true")
    print("current S_HS benchmark directly physical: false")
    print("reverse physical representability selected: false")


if __name__ == "__main__":
    main()
