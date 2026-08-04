"""Validate a selected Qa/SU3 orientation-carrying D_E/dotD source packet.

This gate is the executable version of
SelectedQaSU3OrientationCarryingDEDotDSource.v1.  It accepts a packet only when
one MTT-selected visible source chooses a torsion orientation and supplies the
same-branch finite operator data consumed by the existing D_E, reduced-Green,
and dotD-response validators.

Exit codes:
  0  complete selected orientation-carrying D_E/dotD source packet
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

SCHEMA = "SelectedQaSU3OrientationCarryingDEDotDSource.v1"
ALLOWED_TORSION_LABELS = [1, 2]
GLOBAL_CP_BY_M = {1: 79, 2: 369}
SOURCE_KINDS = {
    "same_source_valpha_s3_operator",
    "selected_route_c_hym_source",
    "selected_visible_bundle",
    "selected_twisted_gerbe",
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


def run_optional_subvalidator(
    packet_path: Path,
    value: Any,
    script: str,
    key: str,
    open_items: list[str],
    subvalidators: dict[str, Any],
) -> None:
    path = resolve_path(value, packet_path)
    if path is None:
        open_items.append(f"{key} packet missing")
        return
    code, output = run_validator(script, path)
    subvalidators[key] = {
        "path": str(path),
        "exit_code": code,
        "output_head": output.splitlines()[:16],
    }
    if code != 0:
        open_items.append(f"{key} validator did not pass (exit {code})")


def classify(packet_path: Path, packet: dict[str, Any]) -> tuple[int, dict[str, Any]]:
    failures: list[str] = []
    open_items: list[str] = []
    subvalidators: dict[str, Any] = {}

    if packet.get("schema") != SCHEMA:
        failures.append(f"schema must be {SCHEMA}")
    if packet.get("status") == "OPEN":
        open_items.append("packet is the open template")

    source = packet.get("source_origin", {})
    if not isinstance(source, dict):
        failures.append("source_origin must be an object")
        source = {}
    if source.get("source_kind") not in SOURCE_KINDS:
        open_items.append("source_kind must be a recognized selected source kind")
    for key in [
        "selected_by_mtt",
        "visible_bundle_or_twisted_gerbe_source",
        "pic0_selected_or_quotiented",
        "freed_witten_and_projector_retention",
    ]:
        require_true(source, key, open_items)
    if resolve_path(source.get("source_certificate"), packet_path) is None:
        open_items.append("source_certificate missing or unresolved")

    branch = packet.get("branch_selection", {})
    if not isinstance(branch, dict):
        failures.append("branch_selection must be an object")
        branch = {}
    if branch.get("allowed_torsion_labels") != ALLOWED_TORSION_LABELS:
        failures.append("allowed_torsion_labels must be [1, 2]")
    if branch.get("do_not_use_observed_cp_sign") is not True:
        failures.append("do_not_use_observed_cp_sign must be true")
    if branch.get("must_bind_m_to_global_cp_label") != {"m=1": 79, "m=2": 369}:
        failures.append("must_bind_m_to_global_cp_label must bind m=1 to 79 and m=2 to 369")
    selected_m = branch.get("selected_torsion_label_m")
    if selected_m not in GLOBAL_CP_BY_M:
        open_items.append("selected_torsion_label_m must be one of [1, 2]")
    else:
        expected_q = GLOBAL_CP_BY_M[selected_m]
        if branch.get("global_cp_label") != expected_q:
            failures.append(f"global_cp_label must be {expected_q} for m={selected_m}")
    require_true(branch, "selection_justified_by_source", open_items)

    operator = packet.get("operator_data", {})
    if not isinstance(operator, dict):
        failures.append("operator_data must be an object")
        operator = {}
    require_true(operator, "same_branch_derivative_verified", open_items)
    run_optional_subvalidator(
        packet_path,
        operator.get("selected_D_E_action"),
        "validate_iwasawa_de_action.py",
        "selected_D_E_action",
        open_items,
        subvalidators,
    )
    run_optional_subvalidator(
        packet_path,
        operator.get("selected_reduced_green"),
        "validate_iwasawa_reduced_green.py",
        "selected_reduced_green",
        open_items,
        subvalidators,
    )
    run_optional_subvalidator(
        packet_path,
        operator.get("selected_dotD_alpha1"),
        "validate_iwasawa_dotd_response.py",
        "selected_dotD_alpha1",
        open_items,
        subvalidators,
    )

    support = packet.get("support_evidence", {})
    if isinstance(support, dict):
        if support.get("finite_s3_class_restriction_passes") is not True:
            open_items.append("finite_s3_class_restriction_passes must be true")
        if support.get("m1_deresponse_stack_coherent_conditionally") is not True:
            open_items.append("m1_deresponse_stack_coherent_conditionally must be true")
    else:
        open_items.append("support_evidence missing")

    guardrails = packet.get("guardrails", {})
    if isinstance(guardrails, dict):
        for key in [
            "uses_observed_cp_sign",
            "uses_observed_masses_or_mixings",
            "uses_benchmark_flavor_entries",
            "uses_lifted_selected_flags_as_proof",
            "claims_full_sm_closure",
        ]:
            require_false(guardrails, key, failures, open_items)
    else:
        open_items.append("guardrails object missing")

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
        "would_close_orientation_carrying_dedotd_source": exit_code == 0,
    }
    return exit_code, report


def main(argv: list[str]) -> int:
    if len(argv) != 2:
        print("Usage: validate_selected_qa_su3_orientation_dedotd_source_packet.py PACKET.json")
        return 2
    packet_path = Path(argv[1]).resolve()
    if not packet_path.exists():
        print(f"Packet not found: {packet_path}")
        return 2
    try:
        packet = load(packet_path)
        exit_code, report = classify(packet_path, packet)
    except (OSError, json.JSONDecodeError, ValueError) as exc:
        print(f"INVALID selected Qa/SU3 orientation D_E/dotD source packet: {exc}")
        return 1
    print("selected_qa_su3_orientation_dedotd_source_report=" + json.dumps(report, sort_keys=True))
    return exit_code


if __name__ == "__main__":
    raise SystemExit(main(sys.argv))
