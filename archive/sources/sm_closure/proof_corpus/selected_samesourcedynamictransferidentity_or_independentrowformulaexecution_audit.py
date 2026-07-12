"""Audit same-source dynamic transfer identity / independent row formula execution gate."""

from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SLUG = "selected_samesourcedynamictransferidentity_or_independentrowformulaexecution"
DATA = ROOT / "candidate_data" / f"{SLUG}.candidate.json"
PACKET_DIR = ROOT / "candidate_data" / SLUG
IDENTITY = PACKET_DIR / "same_source_dynamic_transfer_identity_current_gate.packet.json"
ROWS = PACKET_DIR / "independent_row_formula_execution_current_gate.packet.json"
EQUIV = PACKET_DIR / "identity_or_rows_equivalence.packet.json"
DECISION = PACKET_DIR / "current_frontier_decision.packet.json"
CERT = ROOT / "certificates" / f"{SLUG}_certificate.json"
NOTE = ROOT / "proof_corpus" / "MTT_Selected_SameSourceDynamicTransferIdentity_or_IndependentRowFormulaExecution_v1.md"
BUILDER = ROOT / "scripts" / "build_selected_samesourcedynamictransferidentity_or_independentrowformulaexecution.py"

STATUS = "MTT_SELECTED_SAMESOURCEDYNAMICTRANSFERIDENTITY_OR_INDEPENDENTROWFORMULAEXECUTION_BUILT_CURRENT_FRONTIER_OPEN"
NEXT = "MTT_Selected_PhiFinC1DynamicTransferIdentityProof_or_FirstIndependentRowFormulaRun_v1"


def require(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)


def load(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def guardrails(payload: dict, label: str) -> None:
    require(payload["observed_data_used_as_selector"] is False, f"{label}: observed selector used")
    require(payload["target_fitting_used"] is False, f"{label}: target fitting used")


def main() -> int:
    subprocess.run([sys.executable, str(BUILDER)], cwd=ROOT, check=True)

    data = load(DATA)
    identity = load(IDENTITY)
    rows = load(ROWS)
    equiv = load(EQUIV)
    decision = load(DECISION)
    cert = load(CERT)
    note = NOTE.read_text(encoding="utf-8")

    require(data["status"] == STATUS, "candidate status mismatch")
    require(cert["status"] == STATUS, "certificate status mismatch")
    require(data["next_required_artifact"] == NEXT, "candidate next mismatch")
    require(cert["next_required_artifact"] == NEXT, "certificate next mismatch")
    require(data["theorem"]["proved"] is True, "theorem not proved")
    require(cert["theorem_proved"] is True, "certificate theorem not proved")
    require("independent primitive row formula" in note, "note misses updated fallback")

    require(identity["status"] == "SAME_SOURCE_DYNAMIC_TRANSFER_IDENTITY_NORMAL_FORM_CURRENT_VALUES_OPEN", "identity status mismatch")
    require(identity["identity_name"] == "SelectedSameSourceDynamicTransferIdentityNormalForm", "identity name mismatch")
    require(len(identity["identity_equations"]) == 7, "identity equation count mismatch")
    require(identity["finite_values_if_identity_proved"]["A_transpose_b"] == [12.0, 12.0], "identity b mismatch")
    require(identity["finite_values_if_identity_proved"]["deltaTheta_C1"] == [1.0, 1.0], "identity delta mismatch")
    require(identity["closed_support"]["static_source_retired"] is True, "static source not retired")
    require(identity["closed_support"]["conditional_dynamic_values_exact"] is True, "conditional values not exact")
    require(identity["can_promote_now"] is False, "identity overpromoted")
    require(all(value is False for value in identity["selected_status"].values()), "identity selected status overfilled")

    require(rows["status"] == "INDEPENDENT_ROW_FORMULA_EXECUTION_CURRENT_GATE_OPEN", "rows status mismatch")
    require(rows["row_count"] == 72, "row count mismatch")
    require(rows["row_count_matches_checklist"] is True, "row checklist mismatch")
    require(all(rows["available_support"].values()), "row support missing")
    require(all(rows["still_missing_for_execution"].values()), "row missing flags not preserved")
    require(all(value is False for value in rows["execution_contract"].values()), "row execution overfilled")
    require(rows["first_row"] == "u:phase:r0c0", "first row mismatch")
    require(rows["all_rows_executed_now"] is False, "rows overexecuted")
    require(rows["locked_target_allowed_only_after_emission"] is True, "oracle guard missing")

    require(equiv["status"] == "CURRENT_FRONTIER_TWO_ROUTE_EQUIVALENCE_BUILT_NEITHER_ROUTE_CLOSED", "equiv status mismatch")
    require(equiv["route_a_identity_if_proved_then"]["unpatched_dynamic_C1_packet_closed"] is True, "Route A implication missing")
    require(equiv["route_b_rows_if_executed_then"]["locked_target_checked_after_emission"] is True, "Route B oracle implication missing")
    require(equiv["shared_guardrails"]["target_replay_is_acceptance_oracle_only"] is True, "shared oracle guard missing")

    require(decision["status"] == "CURRENT_FRONTIER_BUILT_CLOSURE_NOT_CLAIMED", "decision status mismatch")
    require(decision["same_source_dynamic_transfer_identity_closed"] is False, "identity overclosed")
    require(decision["independent_row_formula_execution_closed"] is False, "rows overclosed")
    require(decision["conditional_dynamic_values_exact"] is True, "conditional exactness missing")
    require(decision["unpatched_dynamic_C1_packet_closed"] is False, "dynamic C1 overclosed")
    require(decision["true_SM_equivalence_closed"] is False, "true SM overclosed")
    require(decision["no_knob_closed"] is False, "no-knob overclosed")

    for label, payload in [
        ("candidate", data),
        ("identity", identity),
        ("rows", rows),
        ("equiv", equiv["shared_guardrails"]),
        ("decision", decision),
        ("certificate", cert),
    ]:
        guardrails(payload, label)

    print(f"PASS {DATA.name}: {STATUS}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
