"""Audit selected_physicalphifinc1actionsource_or_provenanceindependencetheorem."""

from __future__ import annotations

import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "candidate_data" / "selected_physicalphifinc1actionsource_or_provenanceindependencetheorem.candidate.json"
CERT = ROOT / "certificates" / "selected_physicalphifinc1actionsource_or_provenanceindependencetheorem_certificate.json"
PACKET_DIR = ROOT / "candidate_data" / "selected_physicalphifinc1actionsource_or_provenanceindependencetheorem"
CONTRACT = PACKET_DIR / "last_source_theorem_contract.packet.json"
VALIDATOR = PACKET_DIR / "promotion_validator_kernel.packet.json"
DECISION = PACKET_DIR / "current_frontier_decision.packet.json"
NOTE = ROOT / "proof_corpus" / "MTT_Selected_PhysicalPhiFinC1ActionSource_or_ProvenanceIndependenceTheorem_v1.md"


def load(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def require(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)


def main() -> int:
    data = load(DATA)
    cert = load(CERT)
    contract = load(CONTRACT)
    validator = load(VALIDATOR)
    decision = load(DECISION)
    note = NOTE.read_text(encoding="utf-8")

    require(data["status"] == "MTT_SELECTED_PHYSICALPHIFINC1ACTIONSOURCE_OR_PROVENANCEINDEPENDENCETHEOREM_BUILT_LAST_SOURCE_CONTRACT_OPEN", "status mismatch")
    require(data["theorem"]["proved"] is True, "theorem not proved")
    require(contract["formal_computation_layer_closed"]["formal_110_row_replay_closed"] is True, "formal replay not closed")
    require(contract["formal_computation_layer_closed"]["total_rows"] == 110, "total rows mismatch")
    require(contract["route_A_physical_action_source_theorem"]["closed_now"] is False, "route A overclosed")
    require(contract["route_B_provenance_independence_theorem"]["closed_now"] is False, "route B overclosed")
    require(validator["accepted_now"] is False, "validator overaccepted")
    require("using residual-projector replay as independent provenance" in validator["forbidden_shortcuts"], "guardrail missing")
    require(validator["consequent_if_accepted"]["physical_b_selected"] == [12.0, 12.0], "consequent b mismatch")
    require(decision["formal_computation_layer_closed"] is True, "formal layer not closed")
    require(decision["finite_measure_normalization_retired"] is True, "measure not retired")
    require(decision["physical_action_equivalence_theorem_built"] is True, "action equivalence missing")
    require(decision["finite_rows_to_physical_promotion_theorem_conditional"] is True, "conditional promotion missing")
    require(decision["route_A_physical_action_source_closed"] is False, "route A decision overclosed")
    require(decision["route_B_provenance_independence_closed"] is False, "route B decision overclosed")
    require(decision["unpatched_A_selected_promoted"] is False, "A overpromoted")
    require(decision["unpatched_b_selected_promoted"] is False, "b overpromoted")
    require(decision["true_SM_equivalence_closed"] is False, "SM equivalence overclaimed")
    require(decision["no_knob_closed"] is False, "no-knob overclaimed")
    require(cert["last_source_theorem_contract_built"] is True, "cert contract missing")
    require(cert["route_A_physical_action_source_closed"] is False, "cert route A overclosed")
    require(data["observed_data_used_as_selector"] is False, "observed data used")
    require(data["target_fitting_used"] is False, "target fitting used")
    require("No route is promoted" in note, "note missing guardrail")
    print(f"PASS {DATA.name}: {data['status']}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
