"""Check the current unpatched Weyl-variation no-go/reduction."""

from __future__ import annotations

import json
from dataclasses import dataclass
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parent
TEXPAPERS = Path(r"C:\Users\nero_\Downloads\TEXPAPERS")
SMP = TEXPAPERS / "mtt-sm-parity-closure"

COUNTERMODEL = (
    SMP
    / "candidate_data"
    / "selected_minimalfinitec1sourcepromotionlemma_proof_or_countermodel"
    / "closed_support_not_enough_countermodel.packet.json"
)
COUNTERMODEL_VALIDATOR = (
    SMP
    / "candidate_data"
    / "selected_minimalfinitec1sourcepromotionlemma_proof_or_countermodel"
    / "countermodel_validator_result.packet.json"
)
LOCAL_GATE = SMP / "candidate_data" / "selected_psm_c1_02_selectedfinitec1_variationalbridge_or_sourcepromotionlemma.candidate.json"
BRIDGE = (
    SMP
    / "candidate_data"
    / "selected_psm_c1_02_variationalprojectionbridge_or_rowsource"
    / "selected_variational_projection_bridge_theorem.packet.json"
)
NOTE = ROOT / "Unpatched_WeylVariation_Principle_Current_NoGo_and_Minimal_Bridge_v1.md"


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
    countermodel = load_json(COUNTERMODEL)
    validator = load_json(COUNTERMODEL_VALIDATOR)
    local_gate = load_json(LOCAL_GATE)
    bridge = load_json(BRIDGE)
    note = read_text(NOTE)

    support_true = countermodel.get("closed_support_facts_true", {})
    source_false = countermodel.get("source_promotion_fields_false", {})
    gates = [
        Gate("note saved", "PASS" if "SUPPORT-ONLY PROOF REFUTED" in note else "FAIL", str(NOTE)),
        Gate("local source promotion", "CLOSED" if local_gate.get("local_premise_closure_claimed") is True else "FAIL", local_gate.get("status", "missing")),
        Gate("unpatched gate", "OPEN" if local_gate.get("what_remains_open", {}).get("unpatched_SelectedWeylVariationActionPrinciple_derivation") is True else "FAIL", "unpatched derivation still open"),
        Gate("countermodel support facts", "PASS" if all(support_true.values()) else "FAIL", "all closed support facts true"),
        Gate("countermodel source fields", "PASS" if all(value is False for value in source_false.values()) else "FAIL", "all source-promotion fields false"),
        Gate("countermodel validator", "EXPECTED-REJECT" if validator.get("returncode") == 1 else "FAIL", "strict validator rejects support-only packet"),
        Gate("bridge theorem target", "OPEN" if bridge.get("proved_now") is False and bridge.get("closure_claimed") is False else "FAIL", bridge.get("status", "missing")),
        Gate("observed data excluded", "PASS" if not countermodel.get("observed_data_used_as_selector") and not local_gate.get("observed_data_used_as_selector") else "FAIL", "no observed selector"),
        Gate("target fitting excluded", "PASS" if not countermodel.get("target_fitting_used") and not local_gate.get("target_fitting_used") else "FAIL", "no target fitting"),
    ]

    print("Unpatched Weyl-variation current no-go/reduction check")
    print("======================================================")
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
