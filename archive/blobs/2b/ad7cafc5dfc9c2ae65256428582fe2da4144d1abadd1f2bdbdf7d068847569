"""Check the selected primitive-kernel source payload for right labels."""

from __future__ import annotations

import json
import sys
from dataclasses import dataclass
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parent
DEFAULT_PAYLOAD = ROOT / "selected_primitive_kernel_source_payload.current_attempt.json"
TOL = 1e-12


@dataclass(frozen=True)
class Gate:
    label: str
    status: str
    detail: str


def read_text(path: Path) -> str:
    return path.read_text(encoding="utf-8", errors="ignore") if path.exists() else ""


def load_json(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def truth(data: dict[str, Any], key: str) -> bool:
    return data.get(key) is True


def falsehood(data: dict[str, Any], key: str) -> bool:
    return data.get(key) is False


def validate_payload(data: dict[str, Any]) -> list[str]:
    errors: list[str] = []
    required_true = [
        "selected_emitted",
        "source_owner_verified",
        "source_independent_of_residual_projector_replay",
        "row_formula_source_theorem_derived",
        "selected_basis_feeds_required_primitive_rows",
        "selected_trace_pairing_verified",
        "finite_normalization_rule_emitted",
    ]
    required_false = [
        "residual_replay_dependency",
        "observed_data_used_as_selector",
        "target_fitting_used",
    ]

    if data.get("schema") != "MTTSelectedPrimitiveKernelSourcePayload.v1":
        errors.append("schema mismatch")
    if not data.get("branch_id"):
        errors.append("branch_id missing")
    for key in required_true:
        if not truth(data, key):
            errors.append(f"{key} must be true")
    for key in required_false:
        if not falsehood(data, key):
            errors.append(f"{key} must be false")
    if data.get("exactness_or_error_certificate") in (None, ""):
        errors.append("exactness_or_error_certificate must be supplied")

    rows = data.get("primitive_rows", {})
    down_row_key = "d_shift" if "d_shift" in rows else "d_phase"
    for row_key in ("u_phase", down_row_key):
        row = rows.get(row_key)
        if not isinstance(row, dict):
            errors.append(f"{row_key} row missing")
            continue
        if row.get("pre_residual") is not True:
            errors.append(f"{row_key}.pre_residual must be true")
        if row.get("independent_source_emitted") is not True:
            errors.append(f"{row_key}.independent_source_emitted must be true")
        if row.get("residual_replay_dependency") is not False:
            errors.append(f"{row_key}.residual_replay_dependency must be false")

    labels = data.get("label_output", {})
    for label in ("S_u_spin", "S_d_dyad", "S_d_nil"):
        item = labels.get(label)
        if not isinstance(item, dict):
            errors.append(f"{label} missing")
            continue
        if item.get("third_complement_trace_reported") is not True:
            errors.append(f"{label}.third_complement_trace_reported must be true")
        residual = item.get("max_abs_trace_residual")
        if not isinstance(residual, (int, float)) or float(residual) >= TOL:
            errors.append(f"{label}.max_abs_trace_residual must be < {TOL:g}")

    forbidden = data.get("forbidden_shortcuts", {})
    for key in ("observed_masses_used", "observed_ckm_entries_used", "target_mass_fitting_used"):
        if forbidden.get(key) is not False:
            errors.append(f"forbidden_shortcuts.{key} must be false")
    if forbidden.get("residual_replay_promoted_as_source") is not False:
        errors.append("forbidden_shortcuts.residual_replay_promoted_as_source must be false")
    return errors


def main() -> None:
    payload_path = Path(sys.argv[1]) if len(sys.argv) > 1 else DEFAULT_PAYLOAD
    payload = load_json(payload_path)
    schema_note = read_text(ROOT / "Selected_Primitive_Kernel_Source_Payload_Schema_v1.md")
    template = read_text(ROOT / "selected_primitive_kernel_source_payload.template.json")
    workorder = read_text(ROOT / "Selected_Primitive_Kernel_Source_Theorem_Workorder_v1.md")
    promotion = read_text(ROOT / "Primitive_C1_Right_Label_Source_Promotion_Theorem_Attempt_v1.md")
    errors = validate_payload(payload)
    expected_rejection = payload_path.resolve() == DEFAULT_PAYLOAD.resolve() or "OPEN" in str(payload.get("status", ""))

    gates = [
        Gate("schema note saved", "PASS" if "MTTSelectedPrimitiveKernelSourcePayload.v1" in schema_note else "FAIL", "payload schema note present"),
        Gate("template saved", "PASS" if "TEMPLATE_FILL_WITH_SOURCE_OWNER_ROWS" in template else "FAIL", "fill template present"),
        Gate("workorder saved", "PASS" if "SelectedMatterSlotChargeAndOverlapNormalizationTheorem" in workorder else "FAIL", "source theorem workorder present"),
        Gate("promotion theorem linked", "PASS" if "CONDITIONAL_PROMOTION_PROVED" in promotion else "FAIL", "conditional theorem available"),
        Gate("payload loaded", "PASS" if payload.get("schema") == "MTTSelectedPrimitiveKernelSourcePayload.v1" else "FAIL", str(payload_path)),
        Gate("strict source validation", "PASS" if not errors else ("EXPECTED-REJECT" if expected_rejection else "FAIL"), f"{len(errors)} strict errors"),
        Gate("current source status", "OPEN" if errors else "CLOSED", "source-owner primitive rows still missing" if errors else "source-owner primitive rows emitted"),
    ]

    print("Selected primitive-kernel source payload check")
    print("==============================================")
    print()
    if errors:
        print("Strict validator errors:")
        for err in errors:
            print(f"  - {err}")
        print()
    width = max(len(g.label) for g in gates)
    status_width = max(len(g.status) for g in gates)
    for gate in gates:
        print(f"{gate.label:{width}s}  {gate.status:{status_width}s}  {gate.detail}")

    hard_failures = [gate for gate in gates if gate.status == "FAIL"]
    if hard_failures:
        raise SystemExit(1)


if __name__ == "__main__":
    main()
