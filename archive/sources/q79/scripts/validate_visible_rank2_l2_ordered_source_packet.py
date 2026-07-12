"""Validate a selected ordered integral source packet for visible L^2.

This validator is intentionally stricter than the Appell-Humbert existence
check.  It accepts only a packet that supplies source-level MTT selection of
the ordered integral representative

    L=(1,-2,0),  L^2=(2,-4,0),
    E(g1,g2)=2, E(g3,g4)=-4, E(g5,g6)=0,

and resolves the flat Pic0/semicharacter ambiguity either by selected neutral
holonomy or by an explicit quotient rule.

Exit codes:
  0  complete selected ordered source packet
  1  mathematically invalid or forbidden proxy input
  2  open/incomplete packet
"""

from __future__ import annotations

import json
import sys
from pathlib import Path
from typing import Any


TARGET_L = [1, -2, 0]
TARGET_L2 = [2, -4, 0]
ALLOWED_SELECTED_SOURCE_STATUSES = {
    "VISIBLE_RANK2_L2_ORDERED_SOURCE_SELECTED",
    "VISIBLE_RANK2_L2_ORDERED_SOURCE_SELECTED_PIC0_QUOTIENTED",
}


def target_matrix() -> list[list[int]]:
    matrix = [[0 for _ in range(6)] for _ in range(6)]
    for degree, left, right in [(2, 0, 1), (-4, 2, 3), (0, 4, 5)]:
        matrix[left][right] = degree
        matrix[right][left] = -degree
    return matrix


def load(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def matrix_is_skew(matrix: list[list[Any]]) -> bool:
    if len(matrix) != 6 or any(len(row) != 6 for row in matrix):
        return False
    return all(matrix[i][j] == -matrix[j][i] for i in range(6) for j in range(6))


def classify(packet: dict[str, Any]) -> tuple[int, dict[str, Any]]:
    failures: list[str] = []
    open_items: list[str] = []

    if packet.get("schema") != "VisibleRank2L2OrderedSourcePacket.v1":
        failures.append("wrong schema")

    if packet.get("target", {}).get("L") != TARGET_L:
        failures.append("target L is not (1,-2,0)")
    if packet.get("target", {}).get("L2") != TARGET_L2:
        failures.append("target L^2 is not (2,-4,0)")

    c1_matrix = packet.get("target", {}).get("c1_deck_matrix_order_g1_to_g6")
    if c1_matrix != target_matrix():
        failures.append("ordered c1 matrix is not E12=2,E34=-4,E56=0")
    elif not matrix_is_skew(c1_matrix):
        failures.append("ordered c1 matrix is not skew")

    source = packet.get("source", {})
    if source.get("uses_observed_flavor_inputs") is True:
        failures.append("observed flavor inputs are forbidden")
    if source.get("uses_benchmark_flavor_inputs") is True:
        failures.append("benchmark flavor inputs are forbidden")
    if source.get("fixture_only") is True:
        open_items.append("packet is marked fixture_only")
    if source.get("selected_by_mtt") is not True:
        open_items.append("source.selected_by_mtt is not true")
    if not source.get("source_certificate"):
        open_items.append("source certificate missing")
    if source.get("source_status") not in ALLOWED_SELECTED_SOURCE_STATUSES:
        open_items.append("source status is not a selected ordered-source status")

    automorphy = packet.get("automorphy", {})
    if automorphy.get("cocycle_checked") is not True:
        open_items.append("automorphy cocycle not checked")
    if automorphy.get("ordinary_integral_c1_realized") is not True:
        open_items.append("ordinary integral c1 not realized")
    if automorphy.get("finite_torsion_gerbe_used_as_ordinary_c1") is True:
        failures.append("finite torsion gerbe cannot be used as ordinary c1")

    evidence = packet.get("selection_evidence", {})
    for key in [
        "standard_lattice_or_equivalent_selected",
        "base_factor_order_selected",
        "base_swap_broken_by_source",
        "not_only_finite_mod3_qutrit",
        "not_equal_radius_import",
    ]:
        if evidence.get(key) is not True:
            open_items.append(f"selection evidence missing: {key}")

    pic0 = packet.get("pic0_resolution", {})
    if pic0.get("resolution") not in {
        "neutral_character_selected",
        "pic0_quotient_rule",
        "specific_flat_character_selected",
    }:
        open_items.append("Pic0 resolution rule missing")
    if pic0.get("source_selected_or_quotiented") is not True:
        open_items.append("Pic0 character not selected or quotiented")

    if failures:
        exit_code = 1
        status = "INVALID"
    elif open_items:
        exit_code = 2
        status = "OPEN"
    else:
        exit_code = 0
        status = "PASS"

    report = {
        "status": status,
        "exit_code": exit_code,
        "failures": failures,
        "open_items": open_items,
        "target_matrix": target_matrix(),
        "recognized_selected_statuses": sorted(ALLOWED_SELECTED_SOURCE_STATUSES),
    }
    return exit_code, report


def main(argv: list[str]) -> int:
    if len(argv) != 2:
        print("Usage: validate_visible_rank2_l2_ordered_source_packet.py PACKET.json")
        return 2
    path = Path(argv[1])
    if not path.exists():
        print(f"Packet not found: {path}")
        return 2
    packet = load(path)
    exit_code, report = classify(packet)
    print("visible_rank2_l2_ordered_source_validation_report=" + json.dumps(report, sort_keys=True))
    return exit_code


if __name__ == "__main__":
    raise SystemExit(main(sys.argv))
