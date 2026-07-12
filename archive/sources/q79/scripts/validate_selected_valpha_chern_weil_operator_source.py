"""Validate Selected_VAlpha_ChernWeil_Operator_Source.v1.

This is the executable slot named by the V_alpha operator-source critical-path
reduction.  It accepts only a single same-source packet that selects the
rank-two V_alpha source, resolves Pic0, derives the visible Chern-Weil row, and
emits same-branch operator data.

Exit codes:
  0  complete selected source packet
  1  invalid packet or forbidden shortcut
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

SCHEMA = "SelectedVAlphaChernWeilOperatorSource.v1"
TARGET_L = [1, -2, 0]
TARGET_L2 = [2, -4, 0]
TARGET_C2 = [4, 0, 0]
PIC0_RESOLUTIONS = {
    "neutral_character_selected",
    "pic0_quotient_rule",
    "specific_flat_character_selected",
}


def load(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def resolve_path(value: Any, packet_path: Path) -> Path | None:
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


def run_validator(script: str, path: Path) -> tuple[int, list[str]]:
    proc = subprocess.run(
        [sys.executable, str(SCRIPTS / script), str(path)],
        cwd=ROOT,
        text=True,
        stdout=subprocess.PIPE,
        stderr=subprocess.STDOUT,
    )
    return proc.returncode, proc.stdout.strip().splitlines()


def require_true(container: dict[str, Any], key: str, open_items: list[str]) -> None:
    if container.get(key) is not True:
        open_items.append(f"{key} must be true")


def require_false(
    container: dict[str, Any],
    key: str,
    failures: list[str],
    open_items: list[str],
) -> None:
    value = container.get(key)
    if value is True:
        failures.append(f"{key} must be false")
    elif value is not False:
        open_items.append(f"{key} must be false")


def check_packet(packet_path: Path, packet: dict[str, Any]) -> tuple[int, dict[str, Any]]:
    failures: list[str] = []
    open_items: list[str] = []
    subvalidators: dict[str, Any] = {}

    if packet.get("schema") != SCHEMA:
        failures.append(f"schema must be {SCHEMA}")

    identity = packet.get("source_identity", {})
    if not isinstance(identity, dict):
        failures.append("source_identity must be an object")
        identity = {}
    if identity.get("branch_id") != "q79/F,m=1":
        open_items.append("branch_id must be q79/F,m=1")
    for key in ["selected_by_mtt", "no_observed_flavor_inputs", "no_benchmark_flavor_inputs"]:
        require_true(identity, key, open_items)
    if identity.get("fixture_only") is True:
        open_items.append("packet is marked fixture_only")
    elif identity.get("fixture_only") is not False:
        open_items.append("fixture_only must be false")
    if not identity.get("source_certificate"):
        open_items.append("source_certificate missing")

    valpha = packet.get("valpha_extension", {})
    if not isinstance(valpha, dict):
        failures.append("valpha_extension must be an object")
        valpha = {}
    if valpha.get("selected_L") != TARGET_L:
        failures.append("selected_L must be (1,-2,0)")
    if valpha.get("selected_L2") != TARGET_L2:
        failures.append("selected_L2 must be (2,-4,0)")
    if valpha.get("c2_valpha") != TARGET_C2:
        failures.append("c2_valpha must be (4,0,0)")
    if valpha.get("h1_L2") not in {8, "8"}:
        open_items.append("h1_L2 must be 8")
    for key in [
        "rank2_valpha_model_selected",
        "terminal_monad_difference_L3_minus_K2_selector_closed",
        "ordered_source_validator_passes",
        "pic0_selected_or_quotiented",
        "nonzero_ext_class_selected",
        "non_split_stability_or_hym_proved",
    ]:
        require_true(valpha, key, open_items)
    if valpha.get("pic0_resolution") not in PIC0_RESOLUTIONS:
        open_items.append("pic0_resolution must select or quotient Pic0")

    ordered_path = resolve_path(valpha.get("ordered_source_packet"), packet_path)
    if ordered_path is None:
        open_items.append("ordered_source_packet missing")
    else:
        code, output = run_validator("validate_visible_rank2_l2_ordered_source_packet.py", ordered_path)
        subvalidators["ordered_source"] = {
            "path": str(ordered_path),
            "exit_code": code,
            "output_head": output[:10],
        }
        if code != 0:
            open_items.append(f"ordered source validator did not pass (exit {code})")

    support = packet.get("s3_green_schwarz_support", {})
    if not isinstance(support, dict):
        failures.append("s3_green_schwarz_support must be an object")
        support = {}
    for key in [
        "selected_s3_class_restriction_closed",
        "block_projector_retention_closed",
        "visible_gs_curvature_closed",
        "same_source_link_valpha_to_s3_proved",
        "chern_weil_row_derived_from_same_source",
        "visible_gs_source_validator_passes",
    ]:
        require_true(support, key, open_items)

    s3_path = resolve_path(support.get("s3_class_restriction_packet"), packet_path)
    if s3_path is None:
        open_items.append("s3_class_restriction_packet missing")
    else:
        code, output = run_validator("validate_visible_twisted_s3_class_restriction_packet.py", s3_path)
        subvalidators["s3_class_restriction"] = {
            "path": str(s3_path),
            "exit_code": code,
            "output_head": output[:8],
        }
        if code != 0:
            open_items.append(f"S3 class/restriction validator did not pass (exit {code})")

    gs_path = resolve_path(support.get("visible_gs_source_packet"), packet_path)
    if gs_path is None:
        open_items.append("visible_gs_source_packet missing")
    else:
        code, output = run_validator("validate_time_oriented_m1_visible_gs_source.py", gs_path)
        subvalidators["visible_gs_source"] = {
            "path": str(gs_path),
            "exit_code": code,
            "output_head": output[:12],
        }
        if code != 0:
            open_items.append(f"visible GS source validator did not pass (exit {code})")

    execution = packet.get("operator_execution", {})
    if not isinstance(execution, dict):
        failures.append("operator_execution must be an object")
        execution = {}
    for key in [
        "typed_transition_or_rhoE_data_emitted",
        "hym_strominger_or_routec_residual_pass",
        "sector_D_E_packets_pass",
        "reduced_green_packets_pass",
        "dotD_packets_pass",
        "same_branch_derivative_verified",
        "coherent_spectral_projector_retention",
        "selected_source_promotion_validator_passes",
        "primitive_C1_or_Yukawa_contractions",
    ]:
        require_true(execution, key, open_items)

    promotion_path = resolve_path(execution.get("selected_source_promotion_packet"), packet_path)
    if promotion_path is None:
        open_items.append("selected_source_promotion_packet missing")
    else:
        code, output = run_validator("validate_iwasawa_selected_source_promotion.py", promotion_path)
        subvalidators["selected_source_promotion"] = {
            "path": str(promotion_path),
            "exit_code": code,
            "output_head": output[:16],
        }
        if code != 0:
            open_items.append(f"selected-source promotion validator did not pass (exit {code})")

    branch = packet.get("branch_orientation", {})
    if not isinstance(branch, dict):
        failures.append("branch_orientation must be an object")
        branch = {}
    for key in [
        "time_oriented_q79_representative",
        "m1_label_bound_to_q79",
        "antiunitary_conjugate_pair_accounted",
        "cp_even_parity_accounted",
        "orientation_selection_justified_by_source",
    ]:
        require_true(branch, key, open_items)

    shortcuts = packet.get("forbidden_shortcuts", {})
    if isinstance(shortcuts, dict):
        for key in [
            "uses_observed_masses_or_mixings",
            "uses_benchmark_flavor_entries",
            "copies_visible_gs_row_without_source_derivation",
            "uses_routec_smoke_as_selected_operator_data",
            "splices_s3_and_valpha_without_same_source_link",
            "treats_pic0_as_notational_without_rule",
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
        "would_close_selected_valpha_operator_source": exit_code == 0,
    }
    return exit_code, report


def main(argv: list[str]) -> int:
    if len(argv) != 2:
        print("Usage: validate_selected_valpha_chern_weil_operator_source.py PACKET.json")
        return 2
    packet_path = Path(argv[1]).resolve()
    if not packet_path.exists():
        print(f"Packet not found: {packet_path}")
        return 2
    try:
        exit_code, report = check_packet(packet_path, load(packet_path))
    except (OSError, json.JSONDecodeError, ValueError) as exc:
        print(f"INVALID selected V_alpha Chern-Weil operator source packet: {exc}")
        return 1
    print("selected_valpha_chern_weil_operator_source_report=" + json.dumps(report, sort_keys=True))
    return exit_code


if __name__ == "__main__":
    raise SystemExit(main(sys.argv))
