"""Validate selected Phi_fin^C1 pre-residual action-kernel theorem packets."""

from __future__ import annotations

import json
import sys
from pathlib import Path
from typing import Any


REQUIRED_FIELDS = [
    "physical_action_equals_c1_defect_functional",
    "admissible_differentiated_variations_fixed",
    "physical_boundary_source_terms_vanish",
    "same_source_rz_rx_bselected_emitted",
]


def load(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def evidence_count(packet: dict[str, Any]) -> int:
    evidence = packet.get("attached_theorem_evidence", [])
    return len(evidence) if isinstance(evidence, list) else 0


def validate(packet: dict[str, Any]) -> tuple[bool, list[str]]:
    errors: list[str] = []
    if packet.get("observed_data_used_as_selector") is not False:
        errors.append("observed_data_used_as_selector must be false")
    if packet.get("target_fitting_used") is not False:
        errors.append("target_fitting_used must be false")
    if packet.get("locked_target_values_used_as_source") is not False:
        errors.append("locked_target_values_used_as_source must be false")
    if packet.get("residual_projector_replay_used_as_source") is not False:
        errors.append("residual_projector_replay_used_as_source must be false")
    if packet.get("free_axiom_patch_used") is not False:
        errors.append("free_axiom_patch_used must be false")
    if packet.get("same_branch") is not True:
        errors.append("same_branch must be true")

    missing = [field for field in REQUIRED_FIELDS if packet.get(field) is not True]
    if missing:
        errors.append("missing action-kernel theorem fields: " + ", ".join(missing))
    if evidence_count(packet) < 4:
        errors.append("at least four theorem evidence entries are required")
    return not errors, errors


def main(argv: list[str]) -> int:
    if len(argv) != 2:
        print("usage: validate_selected_phifinc1_preresidual_action_kernel_theorem.py <packet.json>", file=sys.stderr)
        return 2
    ok, errors = validate(load(Path(argv[1])))
    if ok:
        print(f"PASS {argv[1]}")
        return 0
    for error in errors:
        print(f"ERROR {error}", file=sys.stderr)
    return 1


if __name__ == "__main__":
    raise SystemExit(main(sys.argv))
