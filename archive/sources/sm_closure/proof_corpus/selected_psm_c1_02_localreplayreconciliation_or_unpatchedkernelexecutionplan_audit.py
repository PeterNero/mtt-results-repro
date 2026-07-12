"""Audit PSM-C1-02 SI-1e local replay reconciliation."""

from __future__ import annotations

import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "candidate_data"
CERTS = ROOT / "certificates"
CORPUS = ROOT / "proof_corpus"

SLUG = "selected_psm_c1_02_localreplayreconciliation_or_unpatchedkernelexecutionplan"
BASE = DATA / SLUG
CANDIDATE = DATA / f"{SLUG}.candidate.json"
RECONCILIATION = BASE / "psm_c1_02_local_replay_reconciliation.packet.json"
STATUS_TABLE = BASE / "local_vs_unpatched_status_table.packet.json"
UNPATCHED_PLAN = BASE / "unpatched_kernel_execution_plan.packet.json"
NEXT_WORK = BASE / "next_labeled_workorder.packet.json"
CERT = CERTS / f"{SLUG}_certificate.json"
NOTE = CORPUS / "MTT_Selected_PSM_C1_02_LocalReplayReconciliation_or_UnpatchedKernelExecutionPlan_v1.md"

STATUS = "MTT_SELECTED_PSM_C1_02_SI1E_LOCAL_REPLAY_RECONCILED_UNPATCHED_PLAN_EMITTED"
NEXT = "MTT_Selected_PSM_C1_02_UnpatchedKernelExecutionPlan_or_HonestGalerkinExport_v1"


def load(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def require(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)


def guard(packet: dict) -> None:
    require(packet.get("observed_data_used_as_selector") is False, "observed selector violation")
    require(packet.get("target_fitting_used") is False, "target fitting violation")
    require(packet.get("closure_claimed") is False, "global closure overclaim")


def main() -> int:
    candidate = load(CANDIDATE)
    reconciliation = load(RECONCILIATION)
    table = load(STATUS_TABLE)
    plan = load(UNPATCHED_PLAN)
    next_work = load(NEXT_WORK)
    cert = load(CERT)
    note = NOTE.read_text(encoding="utf-8")

    require(candidate["status"] == STATUS, "candidate status mismatch")
    require(candidate["active_label"] == "PSM-C1-02", "active label mismatch")
    require(candidate["active_routes"] == ["SOURCE-IDENTITY/SI-1e", "SOURCE-IDENTITY/SI-1u"], "routes mismatch")
    require(candidate["closed_boundary"] == "DONE-PARITY-00", "closed boundary mismatch")
    require(candidate["next_required_artifact"] == NEXT, "next artifact mismatch")
    require(candidate["theorem"]["proved"] is True, "theorem missing")
    require(candidate["closure_decision"]["SM_parity_closed_under_declared_standard"] is True, "SM parity should remain closed")
    require(candidate["closure_decision"]["local_source_identity_closed"] is True, "local source identity not closed")
    require(candidate["closure_decision"]["unpatched_source_identity_closed"] is False, "unpatched source identity overclosed")
    require(candidate["closure_decision"]["true_SM_equivalence_closed"] is False, "true equivalence overclosed")
    require(candidate["closure_decision"]["no_knob_closed"] is False, "no-knob overclosed")
    require(candidate["closure_decision"]["global_closure_claimed"] is False, "global closure overclaimed")

    for key in [
        "SI1e_local_replay_reconciled",
        "local_vs_unpatched_status_table_emitted",
        "unpatched_kernel_execution_plan_emitted",
        "SM_parity_not_reopened",
        "guardrails_preserved",
    ]:
        require(candidate["what_closes_now"][key] is True, f"achievement missing: {key}")

    require(reconciliation["status"] == "LOCAL_REPLAY_RECONCILED_WITH_FINAL_PARITY_LAYER", "reconciliation status mismatch")
    require(reconciliation["final_replay_audit"]["returncode"] == 0, "final replay audit failed")
    rec = reconciliation["reconciliation"]
    require(rec["local_source_identity_closed"] is True, "rec local source identity missing")
    require(rec["local_dynamic_C1_closed"] is True, "rec local dynamic missing")
    require(rec["patched_source_identity_available_in_final_replay"] is True, "rec source identity final replay missing")
    require(rec["SM_parity_closed_under_declared_standard_retained"] is True, "rec SM parity not retained")
    require(rec["true_SM_equivalence_closed"] is False, "rec true equivalence overclosed")
    require(rec["no_knob_closed"] is False, "rec no-knob overclosed")

    require(table["status"] == "LOCAL_CLOSED_UNPATCHED_OPEN_TABLE_EMITTED", "table status mismatch")
    require(len(table["rows"]) == 5, "table row count mismatch")
    require(table["validator_guardrails"]["current_unpatched_packet_passes"] is False, "table current overaccepted")
    require(table["validator_guardrails"]["patched_local_axiom_packet_passes_unpatched_validator"] is False, "table patch overaccepted")
    require(table["validator_guardrails"]["conditional_unpatched_packet_passes"] is True, "table conditional missing")

    require(plan["status"] == "UNPATCHED_KERNEL_EXECUTION_PLAN_EMITTED", "plan status mismatch")
    require(plan["goal"] == "Make the conditional unpatched source-promotion packet pass without local premises.", "plan goal mismatch")
    require(plan["route_A"]["label"] == "PSM-C1-02 / SOURCE-IDENTITY / SI-1u-A", "route A label mismatch")
    require(plan["route_B"]["label"] == "PSM-C1-02 / SOURCE-IDENTITY / SI-1u-B", "route B label mismatch")
    require(len(plan["route_A"]["must_close"]) == 5, "route A must-close count mismatch")
    require(len(plan["route_B"]["must_export"]) == 5, "route B must-export count mismatch")
    require("free_axiom_patch_used=false" in plan["success_condition"], "success condition missing unpatched flag")
    require("renaming a local principle as an unpatched theorem" in plan["forbidden_shortcuts"], "forbidden shortcut missing")

    require(next_work["primary"]["label"] == "PSM-C1-02 / SOURCE-IDENTITY / SI-1u-B", "next primary mismatch")
    require(next_work["secondary"]["label"] == "PSM-C1-02 / SOURCE-IDENTITY / SI-1u-A", "next secondary mismatch")
    require(next_work["next_required_artifact"] == NEXT, "next work artifact mismatch")

    require(cert["status"] == STATUS, "cert status mismatch")
    require(cert["SM_parity_closed_under_declared_standard"] is True, "cert SM parity missing")
    require(cert["local_source_identity_closed"] is True, "cert local closure missing")
    require(cert["unpatched_source_identity_closed"] is False, "cert unpatched overclosed")
    require(cert["true_SM_equivalence_closed"] is False, "cert true equivalence overclosed")
    require(cert["no_knob_closed"] is False, "cert no-knob overclosed")

    require("Status label: `PSM-C1-02 / SOURCE-IDENTITY / SI-1e`" in note, "note SI-1e label missing")
    require("Unpatched route label: `PSM-C1-02 / SOURCE-IDENTITY / SI-1u`" in note, "note SI-1u label missing")
    require("They are not knobs" in note, "note superset guard missing")

    for packet in [candidate, reconciliation, table, plan, cert]:
        guard(packet)

    print(f"PASS {CANDIDATE.name}: {candidate['status']}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
