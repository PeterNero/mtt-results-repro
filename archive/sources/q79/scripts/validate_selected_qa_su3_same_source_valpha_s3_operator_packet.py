"""Validate a selected Qa/SU3 same-source V_alpha/S3 operator packet.

This is the sharper q79-side gate imported from the constants/no-knob repo.
It can only close if one source binds:

* rank-two V_alpha / terminal-monad L3-K2 source data,
* selected S3 / Green-Schwarz visible support,
* typed transition/rhoE and HYM/Route-C operator execution data.

Exit codes:
  0  complete selected same-source V_alpha/S3 operator packet
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

SCHEMA = "SelectedQaSU3SameSourceVAlphaS3OperatorPacket.v1"
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
    if packet.get("status") == "OPEN_SELECTED_QA_SU3_SAME_SOURCE_VALPHA_S3_OPERATOR_PACKET_REQUIRED":
        open_items.append("packet is the open template")

    identity = packet.get("source_identity", {})
    if not isinstance(identity, dict):
        failures.append("source_identity must be an object")
        identity = {}
    for key in [
        "selected_by_mtt",
        "same_source_valpha_s3_operator",
        "no_observed_flavor_inputs",
    ]:
        require_true(identity, key, open_items)
    if identity.get("fixture_only") is True:
        open_items.append("packet is marked fixture_only")
    elif identity.get("fixture_only") is not False:
        open_items.append("fixture_only must be false")
    if not identity.get("source_certificate"):
        open_items.append("source_certificate missing")

    skeleton = packet.get("source_skeleton", {})
    if not isinstance(skeleton, dict):
        failures.append("source_skeleton must be an object")
        skeleton = {}
    if skeleton.get("selected_L") != TARGET_L:
        failures.append("source_skeleton.selected_L must be (1,-2,0)")
    if skeleton.get("selected_L2") != TARGET_L2:
        failures.append("source_skeleton.selected_L2 must be (2,-4,0)")
    if skeleton.get("c2_valpha") != TARGET_C2:
        failures.append("source_skeleton.c2_valpha must be (4,0,0)")
    for key in [
        "rank2_valpha_model_selected",
        "terminal_monad_difference_L3_minus_K2_selector_closed",
        "nonzero_ext_class_selected",
        "non_split_stability_proved",
        "ordered_source_validator_passes",
    ]:
        require_true(skeleton, key, open_items)
    if skeleton.get("pic0_resolution") not in PIC0_RESOLUTIONS:
        open_items.append("Pic0 resolution is not selected or quotiented")

    ordered_path = resolve_path(skeleton.get("ordered_source_packet"), packet_path)
    if ordered_path is None:
        open_items.append("ordered_source_packet missing")
    else:
        code, output = run_validator("validate_visible_rank2_l2_ordered_source_packet.py", ordered_path)
        subvalidators["ordered_source"] = {
            "path": str(ordered_path),
            "exit_code": code,
            "output_head": output.splitlines()[:8],
        }
        if code != 0:
            open_items.append(f"ordered-source validator did not pass (exit {code})")

    merge = packet.get("same_source_merge", {})
    if not isinstance(merge, dict):
        failures.append("same_source_merge must be an object")
        merge = {}
    for key in [
        "selected_s3_green_schwarz_visible_support",
        "same_source_link_valpha_to_s3_proved",
        "chern_weil_row_derived_from_same_source",
        "visible_gs_source_validator_passes",
        "block_projector_retention_closed",
        "coherent_spectral_zero_mode_projectors_closed",
    ]:
        require_true(merge, key, open_items)

    s3_path = resolve_path(merge.get("s3_class_restriction_packet"), packet_path)
    if s3_path is None:
        open_items.append("s3_class_restriction_packet missing")
    else:
        code, output = run_validator("validate_visible_twisted_s3_class_restriction_packet.py", s3_path)
        subvalidators["s3_class_restriction"] = {
            "path": str(s3_path),
            "exit_code": code,
            "output_head": output.splitlines()[:8],
        }
        if code != 0:
            open_items.append(f"S3 class/restriction validator did not pass (exit {code})")

    gs_path = resolve_path(merge.get("visible_green_schwarz_source_packet"), packet_path)
    if gs_path is None:
        open_items.append("visible_green_schwarz_source_packet missing")
    else:
        code, output = run_validator("validate_time_oriented_m1_visible_gs_source.py", gs_path)
        subvalidators["visible_green_schwarz_source"] = {
            "path": str(gs_path),
            "exit_code": code,
            "output_head": output.splitlines()[:12],
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
        "riesz_green_packets_pass",
        "dotD_packets_pass",
        "selected_source_promotion_validator_passes",
        "primitive_C1_or_Yukawa_overlap_contractions",
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
            "output_head": output.splitlines()[:16],
        }
        if code != 0:
            open_items.append(f"selected-source promotion validator did not pass (exit {code})")

    shortcuts = packet.get("forbidden_shortcuts", {})
    if isinstance(shortcuts, dict):
        for key in [
            "splices_valpha_and_s3_without_same_source_link",
            "promotes_inserted_gs_row_to_chern_weil_derivation",
            "uses_routec_smoke_as_selected_operator_data",
            "uses_lifted_flags_as_proof",
            "uses_observed_masses_or_mixings",
            "uses_benchmark_flavor_entries",
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
        "would_close_same_source_valpha_s3_operator_packet": exit_code == 0,
    }
    return exit_code, report


def main(argv: list[str]) -> int:
    if len(argv) != 2:
        print("Usage: validate_selected_qa_su3_same_source_valpha_s3_operator_packet.py PACKET.json")
        return 2
    packet_path = Path(argv[1]).resolve()
    if not packet_path.exists():
        print(f"Packet not found: {packet_path}")
        return 2
    try:
        packet = load(packet_path)
        exit_code, report = classify(packet_path, packet)
    except (OSError, json.JSONDecodeError, ValueError) as exc:
        print(f"INVALID selected Qa/SU3 same-source V_alpha/S3 packet: {exc}")
        return 1
    print("selected_qa_su3_same_source_valpha_s3_report=" + json.dumps(report, sort_keys=True))
    return exit_code


if __name__ == "__main__":
    raise SystemExit(main(sys.argv))
