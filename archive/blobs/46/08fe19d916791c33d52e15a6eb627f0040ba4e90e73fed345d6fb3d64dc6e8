"""Validate a selected Qa/SU3 Iwasawa monad-map augmentation packet.

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
DEFAULT_PACKET = ROOT / "certificates" / "source_augmentation_iwasawa_monad_maps.template.json"

REQUIRED_IDS = ["F1", "F2", "F3", "F4", "F5", "G1", "G2", "G3", "G4", "G5", "P"]
EXPECTED_CHARGES = {
    "F1": [-3, 0, 1],
    "F2": [-2, 1, -1],
    "F3": [0, -1, 0],
    "F4": [0, 0, -1],
    "F5": [1, 1, 1],
    "G1": [2, 1, -1],
    "G2": [1, 0, 1],
    "G3": [-1, 2, 0],
    "G4": [-1, 1, 1],
    "G5": [-2, 0, -1],
    "P": [-1, 1, 0],
}


def incomplete(reason: str) -> int:
    print(f"OPEN: {reason}")
    return 2


def fail(reason: str) -> int:
    print(f"FAIL: {reason}")
    return 1


def ok(message: str) -> int:
    print(f"PASS: {message}")
    return 0


def is_number(x: Any) -> bool:
    return isinstance(x, int | float) and not isinstance(x, bool)


def is_vector(value: Any, length: int) -> bool:
    return isinstance(value, list) and len(value) == length and all(is_number(x) for x in value)


def dot_product_sum(products: dict[str, Any], f: list[float], g: list[float]) -> float | None:
    total = 0.0
    for i in range(5):
        key = f"{i + 1}"
        value = products.get(key)
        if not is_number(value):
            return None
        total += float(value) * float(f[i]) * float(g[i])
    return total


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

    geometry = data.get("geometry", {})
    for key in ("complex_coordinate_action", "lattice_generators", "left_or_right_quotient_convention"):
        if geometry.get(key) is None:
            return incomplete(f"geometry missing {key}")

    automorphy = data.get("automorphy", {})
    if automorphy.get("flat_character_only") is True:
        return fail("flat-character-only automorphy cannot realize nonzero charges")
    for key in ("charge_to_factor_map", "cocycle_checked", "multiplicative_charge_law_checked", "c1_charge_realization_checked"):
        if key == "charge_to_factor_map":
            if automorphy.get(key) is None:
                return incomplete("charge_to_factor_map missing")
        elif automorphy.get(key) is not True:
            return incomplete(f"automorphy check {key} is not certified true")

    section_spaces = data.get("section_spaces", {})
    spaces = section_spaces.get("spaces")
    if not isinstance(spaces, list) or len(spaces) != 11:
        return fail("section space list must contain eleven spaces")
    by_id = {space.get("id"): space for space in spaces if isinstance(space, dict)}
    if sorted(by_id) != sorted(REQUIRED_IDS):
        return fail("section space ids do not match required ids")
    for space_id in REQUIRED_IDS:
        space = by_id[space_id]
        if space.get("charge") != EXPECTED_CHARGES[space_id]:
            return fail(f"charge mismatch for {space_id}")
        if not isinstance(space.get("dimension"), int) or space["dimension"] <= 0:
            return incomplete(f"nonzero dimension missing for {space_id}")
        if not isinstance(space.get("basis"), list) or len(space["basis"]) != space["dimension"]:
            return incomplete(f"basis missing or wrong length for {space_id}")
    if section_spaces.get("section_equivariance_checked") is not True:
        return incomplete("section equivariance not certified")

    multiplication = data.get("multiplication", {})
    products = multiplication.get("product_constants")
    if not isinstance(products, dict):
        return incomplete("product constants missing")
    if multiplication.get("product_table_checked") is not True:
        return incomplete("product table not certified")

    maps = data.get("monad_maps", {})
    f = maps.get("f_coefficients")
    g = maps.get("g_coefficients")
    if not is_vector(f, 5) or not is_vector(g, 5):
        return incomplete("f/g coefficient vectors missing")
    total = dot_product_sum(products, f, g)
    if total is None:
        return incomplete("product constants must contain numeric keys 1..5")
    if abs(total) > 1e-9:
        return fail("g*f scalar relation is nonzero")
    for key in ("g_f_zero_checked", "locally_free_checked", "stable_or_hym_source_checked"):
        if maps.get(key) is not True:
            return incomplete(f"monad map check {key} is not certified true")

    exit_packet = data.get("operator_exit", {})
    if exit_packet.get("kind") not in exit_packet.get("allowed_kinds", []):
        return incomplete("operator exit kind missing or unsupported")
    if exit_packet.get("packet") is None:
        return incomplete("operator exit packet missing")
    if exit_packet.get("finite_part_available") is not True:
        return incomplete("operator finite part unavailable")

    return ok("selected Qa/SU3 Iwasawa monad-map augmentation packet passes implemented checks")


if __name__ == "__main__":
    raise SystemExit(main(sys.argv))
