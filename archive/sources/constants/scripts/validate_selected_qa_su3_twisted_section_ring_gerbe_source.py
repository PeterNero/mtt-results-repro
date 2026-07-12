"""Validate a selected Qa/SU3 twisted section-ring/gerbe-source packet.

Exit codes:
  0 complete packet passes implemented structural checks
  1 complete-looking packet fails a structural check
  2 packet is open or incomplete
"""

from __future__ import annotations

import json
import sys
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DEFAULT_PACKET = ROOT / "certificates" / "selected_qa_su3_twisted_section_ring_gerbe_source.template.json"

REQUIRED_IDS = ["F1", "F2", "F3", "F4", "F5", "G1", "G2", "G3", "G4", "G5", "P"]
EXPECTED = {
    "F1": {"charge": [-3, 0, 1], "ab": [-3, 0], "twist": 1},
    "F2": {"charge": [-2, 1, -1], "ab": [-2, 1], "twist": -1},
    "F3": {"charge": [0, -1, 0], "ab": [0, -1], "twist": 0},
    "F4": {"charge": [0, 0, -1], "ab": [0, 0], "twist": -1},
    "F5": {"charge": [1, 1, 1], "ab": [1, 1], "twist": 1},
    "G1": {"charge": [2, 1, -1], "ab": [2, 1], "twist": -1},
    "G2": {"charge": [1, 0, 1], "ab": [1, 0], "twist": 1},
    "G3": {"charge": [-1, 2, 0], "ab": [-1, 2], "twist": 0},
    "G4": {"charge": [-1, 1, 1], "ab": [-1, 1], "twist": 1},
    "G5": {"charge": [-2, 0, -1], "ab": [-2, 0], "twist": -1},
    "P": {"charge": [-1, 1, 0], "ab": [-1, 1], "twist": 0},
}
PAIRS = [("F1", "G1"), ("F2", "G2"), ("F3", "G3"), ("F4", "G4"), ("F5", "G5")]


def incomplete(reason: str) -> int:
    print(f"OPEN: {reason}")
    return 2


def fail(reason: str) -> int:
    print(f"FAIL: {reason}")
    return 1


def ok(message: str) -> int:
    print(f"PASS: {message}")
    return 0


def is_number(value: Any) -> bool:
    return isinstance(value, int | float) and not isinstance(value, bool)


def main(argv: list[str]) -> int:
    path = Path(argv[1]) if len(argv) > 1 else DEFAULT_PACKET
    data = json.loads(path.read_text(encoding="utf-8"))

    if str(data.get("status", "")).startswith("OPEN_"):
        return incomplete("packet status is open")

    selected = data.get("selected_branch", {})
    if selected.get("target_residual_used") is not False:
        return fail("target residual is marked as used")
    if not selected.get("source_certificate") or not selected.get("selection_rule"):
        return incomplete("source certificate or selection rule missing")

    gerbe = data.get("gerbe_source", {})
    if gerbe.get("kind") not in gerbe.get("allowed_kinds", []):
        return incomplete("gerbe source kind missing or unsupported")
    for key in (
        "representative",
        "period_denominator",
        "central_cocycle",
        "selected_by_mtt",
        "fixed_topological_sector",
        "cocycle_checked",
        "nontrivial_twist_checked",
    ):
        value = gerbe.get(key)
        if value is None:
            return incomplete(f"gerbe source missing {key}")
        if key.endswith("checked") or key in ("selected_by_mtt", "fixed_topological_sector"):
            if value is not True:
                return incomplete(f"gerbe source {key} is not certified true")
    if not isinstance(gerbe.get("period_denominator"), int) or gerbe["period_denominator"] <= 1:
        return fail("gerbe period denominator must be a nontrivial integer")

    ab = data.get("ordinary_ab_line_bundle_part", {})
    if ab.get("forbidden_c_as_ordinary_c1") is not True:
        return fail("literal c is being allowed as ordinary c1")
    if not ab.get("factor_model") or ab.get("a_b_c1_realization_checked") is not True:
        return incomplete("ordinary ab factor model is not certified")

    section = data.get("twisted_section_spaces", {})
    spaces = section.get("spaces")
    if not isinstance(spaces, list) or len(spaces) != 11:
        return fail("twisted section-space list must contain eleven spaces")
    by_id = {space.get("id"): space for space in spaces if isinstance(space, dict)}
    if sorted(by_id) != sorted(REQUIRED_IDS):
        return fail("twisted section-space ids do not match required ids")
    for space_id in REQUIRED_IDS:
        space = by_id[space_id]
        expected = EXPECTED[space_id]
        if space.get("charge") != expected["charge"]:
            return fail(f"charge mismatch for {space_id}")
        if space.get("ordinary_ab_charge") != expected["ab"]:
            return fail(f"ordinary ab charge mismatch for {space_id}")
        if space.get("gerbe_c_twist") != expected["twist"]:
            return fail(f"gerbe twist mismatch for {space_id}")
        if not isinstance(space.get("dimension"), int) or space["dimension"] <= 0:
            return incomplete(f"positive dimension missing for {space_id}")
        if not isinstance(space.get("basis"), list) or len(space["basis"]) != space["dimension"]:
            return incomplete(f"basis missing or wrong length for {space_id}")
    if section.get("twisted_equivariance_checked") is not True:
        return incomplete("twisted section equivariance not certified")

    multiplication = data.get("twisted_multiplication", {})
    pair_products = multiplication.get("pair_products")
    if not isinstance(pair_products, dict):
        return incomplete("twisted pair products missing")
    for index, (f_id, g_id) in enumerate(PAIRS, start=1):
        key = f"{f_id}_{g_id}"
        product = pair_products.get(key)
        if not isinstance(product, dict):
            return incomplete(f"product packet missing for {key}")
        if product.get("target") != "P":
            return fail(f"product target mismatch for {key}")
        if product.get("gerbe_twist_sum") != 0:
            return fail(f"gerbe twist does not cancel for {key}")
        if product.get("ordinary_ab_sum") != [-1, 1]:
            return fail(f"ordinary ab product mismatch for {key}")
        if not is_number(product.get("constant")):
            return incomplete(f"numeric multiplication constant missing for {key}")
    if multiplication.get("gerbe_twist_cancellation_checked") is not True:
        return incomplete("gerbe twist cancellation not certified")
    if multiplication.get("product_table_checked") is not True:
        return incomplete("twisted product table not certified")

    admissibility = data.get("admissibility", {})
    for key in (
        "green_schwarz_bianchi_verified",
        "freed_witten_verified",
        "twisted_projector_retention_verified",
        "coherent_spectral_projector_verified",
    ):
        if admissibility.get(key) is not True:
            return incomplete(f"admissibility check {key} is not certified")

    exit_packet = data.get("operator_exit", {})
    if exit_packet.get("kind") not in exit_packet.get("allowed_kinds", []):
        return incomplete("operator exit kind missing or unsupported")
    if exit_packet.get("packet") is None:
        return incomplete("operator exit packet missing")
    if exit_packet.get("finite_part_available") is not True:
        return incomplete("operator finite part unavailable")

    return ok("selected Qa/SU3 twisted section-ring/gerbe-source packet passes implemented checks")


if __name__ == "__main__":
    raise SystemExit(main(sys.argv))
