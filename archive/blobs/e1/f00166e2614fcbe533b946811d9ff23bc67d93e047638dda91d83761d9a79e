"""Validate a same-source monad/GS/operator fusion packet.

The packet is allowed to close the monad-difference selector only if a single
selected source binds all of the following:

* ordered L3-K2 source selection and Pic0 resolution,
* visible Green-Schwarz row and projector retention,
* selected D_E/Riesz/Green/dotD promotion,
* primitive C1 data for the next flavor stage.

Exit codes:
  0  complete same-source fusion packet
  1  mathematically invalid or forbidden proxy input
  2  open/incomplete packet
"""

from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
SCRIPTS = ROOT / "scripts"

SCHEMA = "SameSourceMonadGSOperatorFusionPacket.v1"
TARGET_L = [1, -2, 0]
TARGET_L2 = [2, -4, 0]
SOURCE_KINDS = {
    "typed_Cech_monad_transition_data",
    "finite_HYM_Strominger_solve",
    "selected_visible_SM_bundle_operator_source",
}
LANE_SELECTORS = {
    "terminal_monad_difference_Li_minus_K2",
    "same_source_DE_response_selects_terminal_monad_difference",
}
PIC0_RESOLUTIONS = {
    "neutral_character_selected",
    "pic0_quotient_rule",
    "specific_flat_character_selected",
}


def load(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def resolve_path(value: Any, packet_path: Path, label: str) -> Path | None:
    if not isinstance(value, str) or not value:
        return None
    raw = Path(value)
    candidates = [raw] if raw.is_absolute() else [
        (packet_path.parent / raw).resolve(),
        (ROOT / raw).resolve(),
    ]
    for candidate in candidates:
        if candidate.exists():
            return candidate
    return None


def run_validator(script: str, path: Path) -> tuple[int, str]:
    proc = subprocess.run(
        [sys.executable, str(SCRIPTS / script), str(path)],
        cwd=ROOT,
        text=True,
        stdout=subprocess.PIPE,
        stderr=subprocess.STDOUT,
    )
    return proc.returncode, proc.stdout.strip()


def require_true(container: dict[str, Any], key: str, open_items: list[str]) -> None:
    if container.get(key) is not True:
        open_items.append(f"{key} must be true")


def require_false(container: dict[str, Any], key: str, failures: list[str], open_items: list[str]) -> None:
    value = container.get(key)
    if value is True:
        failures.append(f"{key} must be false")
    elif value is not False:
        open_items.append(f"{key} must be false")


def classify(packet_path: Path, packet: dict[str, Any]) -> tuple[int, dict[str, Any]]:
    failures: list[str] = []
    open_items: list[str] = []
    subvalidators: dict[str, Any] = {}

    if packet.get("schema") != SCHEMA:
        failures.append(f"schema must be {SCHEMA}")
    if packet.get("status") == "OPEN_SAME_SOURCE_MONAD_GS_OPERATOR_FUSION_REQUIRED":
        open_items.append("packet is the open template")

    source = packet.get("source_identity", {})
    if not isinstance(source, dict):
        failures.append("source_identity must be an object")
        source = {}
    if source.get("source_kind") not in SOURCE_KINDS:
        open_items.append("source_kind must be a selected allowed source kind")
    require_true(source, "selected_by_mtt", open_items)
    require_true(source, "no_observed_flavor_inputs", open_items)
    require_true(source, "same_source_for_ordered_L_pic0_GS_and_DE", open_items)
    if source.get("fixture_only") is True:
        open_items.append("packet is marked fixture_only")
    elif source.get("fixture_only") is not False:
        open_items.append("fixture_only must be false")
    require_false(source, "uses_execution_ii_benchmarks", failures, open_items)
    if not source.get("source_certificate"):
        open_items.append("source_certificate missing")

    ordered = packet.get("ordered_source", {})
    if not isinstance(ordered, dict):
        failures.append("ordered_source must be an object")
        ordered = {}
    if ordered.get("selected_L") != TARGET_L:
        failures.append("selected_L must be (1,-2,0)")
    if ordered.get("selected_L2") != TARGET_L2:
        failures.append("selected_L2 must be (2,-4,0)")
    if ordered.get("source_lane_selector") not in LANE_SELECTORS:
        open_items.append("source_lane_selector is not closed")
    for key in [
        "standard_lattice_or_equivalent_selected",
        "base_factor_order_selected",
        "base_swap_broken_by_source",
        "ordered_source_validator_passes",
    ]:
        require_true(ordered, key, open_items)
    if ordered.get("pic0_resolution") not in PIC0_RESOLUTIONS:
        open_items.append("Pic0 resolution is not selected or quotiented")

    ordered_path = resolve_path(
        ordered.get("visible_rank2_l2_ordered_source_packet"),
        packet_path,
        "ordered_source.visible_rank2_l2_ordered_source_packet",
    )
    if ordered_path is None:
        open_items.append("visible_rank2_l2_ordered_source_packet missing")
    else:
        code, output = run_validator("validate_visible_rank2_l2_ordered_source_packet.py", ordered_path)
        subvalidators["ordered_source"] = {
            "path": str(ordered_path),
            "exit_code": code,
            "output_head": output.splitlines()[:8],
        }
        if code != 0:
            open_items.append(f"ordered-source validator did not pass (exit {code})")

    gs = packet.get("green_schwarz_and_gerbe", {})
    if not isinstance(gs, dict):
        failures.append("green_schwarz_and_gerbe must be an object")
        gs = {}
    for key in [
        "time_oriented_m1_representative_used",
        "antiunitary_q369_retained",
        "visible_green_schwarz_row_derived_from_same_source",
        "freed_witten_or_cycle_restrictions_verified_if_used",
        "projector_retention_verified",
    ]:
        require_true(gs, key, open_items)

    op = packet.get("operator_response", {})
    if not isinstance(op, dict):
        failures.append("operator_response must be an object")
        op = {}
    for key in [
        "route_c_residuals_pass",
        "de_action_pass",
        "riesz_gap_pass",
        "reduced_green_pass",
        "dotd_response_pass",
        "selected_dotD_source_verified",
        "primitive_C1_contractions",
    ]:
        require_true(op, key, open_items)

    promotion_path = resolve_path(
        op.get("iwasawa_selected_source_promotion_packet"),
        packet_path,
        "operator_response.iwasawa_selected_source_promotion_packet",
    )
    if promotion_path is None:
        open_items.append("iwasawa_selected_source_promotion_packet missing")
    else:
        code, output = run_validator("validate_iwasawa_selected_source_promotion.py", promotion_path)
        subvalidators["selected_source_promotion"] = {
            "path": str(promotion_path),
            "exit_code": code,
            "output_head": output.splitlines()[:16],
        }
        if code != 0:
            open_items.append(f"selected-source promotion validator did not pass (exit {code})")

    shortcuts = packet.get("forbidden_shortcuts", {})
    if isinstance(shortcuts, dict):
        for key in [
            "uses_lifted_flags_as_proof",
            "uses_observed_masses_or_mixings",
            "uses_benchmark_flavor_entries",
            "combines_separate_sources_without_same_source_certificate",
            "treats_curvature_only_gs_as_operator_source",
        ]:
            require_false(shortcuts, key, failures, open_items)
    else:
        open_items.append("forbidden_shortcuts guardrail object missing")

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
        "schema": SCHEMA,
        "status": status,
        "exit_code": exit_code,
        "failures": failures,
        "open_items": open_items,
        "subvalidators": subvalidators,
        "would_close_selected_monad_difference_source": exit_code == 0,
    }
    return exit_code, report


def main(argv: list[str]) -> int:
    if len(argv) != 2:
        print("Usage: validate_same_source_monad_gs_operator_fusion_packet.py PACKET.json")
        return 2
    packet_path = Path(argv[1]).resolve()
    if not packet_path.exists():
        print(f"Packet not found: {packet_path}")
        return 2
    try:
        packet = load(packet_path)
        exit_code, report = classify(packet_path, packet)
    except (OSError, json.JSONDecodeError, ValueError) as exc:
        print(f"INVALID same-source fusion packet: {exc}")
        return 1
    print("same_source_monad_gs_operator_fusion_report=" + json.dumps(report, sort_keys=True))
    return exit_code


if __name__ == "__main__":
    raise SystemExit(main(sys.argv))
