"""Validate the local-premise finite-trace/PhiFin promotion theorem."""

from __future__ import annotations

import json
import sys
from dataclasses import dataclass
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parent
TEXPAPERS = Path(r"C:\Users\nero_\Downloads\TEXPAPERS")
SMP = TEXPAPERS / "mtt-sm-parity-closure"
PREMISE = (
    SMP
    / "candidate_data"
    / "selected_weylvariation_actionprinciple_apply_or_independentkernelexecution"
    / "accepted_local_weylvariation_actionprinciple.packet.json"
)
KERNEL = (
    SMP
    / "candidate_data"
    / "selected_weylvariation_actionprinciple_apply_or_independentkernelexecution"
    / "applied_principle_kernel_closure.packet.json"
)
KERNEL_VALIDATOR = (
    SMP
    / "candidate_data"
    / "selected_weylvariation_actionprinciple_apply_or_independentkernelexecution"
    / "applied_kernel_validator_result.packet.json"
)
EXIT = (
    SMP
    / "candidate_data"
    / "selected_weylvariation_actionprinciple_apply_or_independentkernelexecution"
    / "unpatched_or_independent_kernel_execution_exit.packet.json"
)
PAYLOAD = ROOT / "selected_primitive_kernel_source_payload.local_principle_promoted.json"
THEOREM = ROOT / "Selected_FiniteTraceQuadrature_Equals_PhysicalPhiFinC1Action_LocalPremise_Theorem_v1.md"

sys.path.insert(0, str(ROOT))
from selected_primitive_kernel_source_payload_check import validate_payload  # noqa: E402


@dataclass(frozen=True)
class Gate:
    label: str
    status: str
    detail: str


def load_json(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def read_text(path: Path) -> str:
    return path.read_text(encoding="utf-8", errors="ignore") if path.exists() else ""


def main() -> None:
    premise = load_json(PREMISE)
    kernel = load_json(KERNEL)
    validator = load_json(KERNEL_VALIDATOR)
    exit_packet = load_json(EXIT)
    payload = load_json(PAYLOAD)
    theorem = read_text(THEOREM)
    errors = validate_payload(payload)

    conditional = payload.get("conditional_on_explicit_local_premise", {})
    rows = payload.get("primitive_rows", {})
    gates = [
        Gate("theorem saved", "PASS" if "LOCAL-PREMISE PROVED" in theorem and "UNPATCHED DERIVATION OPEN" in theorem else "FAIL", str(THEOREM)),
        Gate("local premise accepted", "PASS" if premise.get("accepted_as") == "explicit local premise, not unpatched theorem" else "FAIL", premise.get("status", "missing")),
        Gate("applied kernel validator", "PASS" if validator.get("ok") is True and validator.get("exit_code") == 0 else "FAIL", str(validator)),
        Gate("kernel source promotion", "PASS" if kernel.get("promoted_inside_local_spine", {}).get("pre_residual_phase_shift_operator_source") is True else "FAIL", kernel.get("status", "missing")),
        Gate("same-source Hessian", "PASS" if kernel.get("same_source_hessian") is True else "FAIL", "same_source_hessian must be true under local premise"),
        Gate("residual replay excluded", "PASS" if kernel.get("residual_projector_replay_used_as_source") is False else "FAIL", "residual replay not source"),
        Gate("u row promoted", "PASS" if rows.get("u_phase", {}).get("independent_source_emitted") is True else "FAIL", "u:phase"),
        Gate("d row promoted", "PASS" if rows.get("d_shift", {}).get("independent_source_emitted") is True else "FAIL", "d:shift"),
        Gate("strict payload validation", "PASS" if not errors else "FAIL", f"{len(errors)} strict errors"),
        Gate("local premise guard", "PASS" if conditional.get("accepted_as") == "explicit local premise, not unpatched theorem" else "FAIL", "payload carries conditional premise"),
        Gate("unpatched exit retained", "OPEN" if exit_packet.get("unpatched_principle_derived_now") is False else "FAIL", "unpatched derivation remains open"),
        Gate("no target fitting", "PASS" if payload.get("observed_data_used_as_selector") is False and payload.get("target_fitting_used") is False else "FAIL", "observed/target inputs excluded"),
    ]

    print("Local-premise finite-trace/PhiFin promotion check")
    print("=================================================")
    print()
    if errors:
        print("Strict payload errors:")
        for error in errors:
            print(f"  - {error}")
        print()
    width = max(len(g.label) for g in gates)
    status_width = max(len(g.status) for g in gates)
    for gate in gates:
        print(f"{gate.label:{width}s}  {gate.status:{status_width}s}  {gate.detail}")

    failures = [gate for gate in gates if gate.status == "FAIL"]
    if failures:
        raise SystemExit(1)


if __name__ == "__main__":
    main()
