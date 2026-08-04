"""Audit PSM-C1-02 SI-1d local source-identity integration."""

from __future__ import annotations

import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "candidate_data"
CERTS = ROOT / "certificates"
CORPUS = ROOT / "proof_corpus"

SLUG = "selected_psm_c1_02_localsourceidentityclosure_integration_or_unpatchedkernelexecution"
BASE = DATA / SLUG
CANDIDATE = DATA / f"{SLUG}.candidate.json"
LOCAL_INTEGRATION = BASE / "psm_c1_02_local_source_identity_integration.packet.json"
VALIDATOR_LEDGER = BASE / "unpatched_validator_guardrail_ledger.packet.json"
THEOREM = BASE / "local_source_identity_integration_theorem.packet.json"
NEXT_WORK = BASE / "next_labeled_workorder.packet.json"
CERT = CERTS / f"{SLUG}_certificate.json"
NOTE = CORPUS / "MTT_Selected_PSM_C1_02_LocalSourceIdentityClosure_Integration_or_UnpatchedKernelExecution_v1.md"

STATUS = "MTT_SELECTED_PSM_C1_02_SI1D_LOCAL_SOURCEIDENTITY_INTEGRATED_UNPATCHED_EXECUTION_OPEN"
NEXT = "MTT_Selected_PSM_C1_02_LocalReplayReconciliation_or_UnpatchedKernelExecutionPlan_v1"


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
    local = load(LOCAL_INTEGRATION)
    ledger = load(VALIDATOR_LEDGER)
    theorem = load(THEOREM)
    next_work = load(NEXT_WORK)
    cert = load(CERT)
    note = NOTE.read_text(encoding="utf-8")

    require(candidate["status"] == STATUS, "candidate status mismatch")
    require(candidate["active_label"] == "PSM-C1-02", "active label mismatch")
    require(candidate["active_routes"] == ["SOURCE-IDENTITY/SI-1d"], "active routes mismatch")
    require(candidate["closed_boundary"] == "DONE-PARITY-00", "closed boundary mismatch")
    require(candidate["next_required_artifact"] == NEXT, "next artifact mismatch")
    require(candidate["theorem"]["proved"] is True, "candidate theorem not proved")

    closure = candidate["closure_decision"]
    require(closure["local_source_identity_closed"] is True, "local source identity not closed")
    require(closure["unpatched_source_identity_closed"] is False, "unpatched source identity overclosed")
    require(closure["local_dynamic_C1_closed"] is True, "local dynamic C1 not closed")
    require(closure["current_unpatched_packet_passes"] is False, "current packet overaccepted")
    require(closure["patched_local_axiom_packet_passes_unpatched_validator"] is False, "patched packet overaccepted")
    require(closure["conditional_unpatched_packet_passes_if_theorem_supplied"] is True, "conditional target not preserved")
    require(closure["true_SM_equivalence_closed"] is False, "true SM overclosed")
    require(closure["no_knob_closed"] is False, "no-knob overclosed")
    require(closure["global_closure_claimed"] is False, "global closure overclaimed")

    for key in [
        "SI1d_local_source_identity_integrated",
        "local_chain_audits_imported_and_pass",
        "local_110row_source_identity_validates",
        "local_dynamic_C1_closure_connected",
        "unpatched_validator_guardrails_preserved",
        "superset_paths_constrained_to_locked_target",
    ]:
        require(candidate["what_closes_now"][key] is True, f"achievement missing: {key}")

    require(local["status"] == "LOCAL_SOURCE_IDENTITY_CHAIN_INTEGRATED_FOR_PSM_C1_02", "local integration status mismatch")
    require(local["clause"] == "SI-1d", "local clause mismatch")
    require(local["scientific_status"] == "local-premise source-identity closure for the PSM-C1-02 proof spine", "scientific status mismatch")
    for audit in local["imported_audits"].values():
        require(audit["returncode"] == 0, f"imported audit failed: {audit['audit']}")
    for key, value in local["local_chain"].items():
        require(value is True, f"local chain flag missing: {key}")

    require(ledger["status"] == "UNPATCHED_VALIDATOR_GUARDRAILS_PRESERVED", "ledger status mismatch")
    require(ledger["current_unpatched_packet_passes"] is False, "ledger current packet overaccepted")
    require(ledger["patched_local_axiom_packet_passes_unpatched_validator"] is False, "ledger patched packet overaccepted")
    require(ledger["conditional_unpatched_packet_passes"] is True, "ledger conditional missing")
    require(ledger["current_closed_fields"] == 3, "closed field count mismatch")
    require(ledger["current_open_fields"] == 4, "open field count mismatch")
    require(ledger["dynamic_values_ready"] is True, "dynamic values not ready")
    require(ledger["unpatched_source_rule_proved"] is False, "unpatched source rule overproved")
    require(ledger["honest_galerkin_table_exported"] is False, "honest Galerkin export overclaimed")

    require(theorem["name"] == "PSMC102LocalSourceIdentityIntegrationTheorem", "theorem name mismatch")
    require(theorem["proved"] is True, "theorem should be proved")
    require(theorem["local_source_identity_closed"] is True, "theorem local closure missing")
    require(theorem["unpatched_source_identity_closed"] is False, "theorem unpatched overclosed")
    for value in theorem["does_not_close"].values():
        require(value is True, "does-not-close guard missing")

    require(next_work["primary"]["label"] == "PSM-C1-02 / SOURCE-IDENTITY / SI-1e", "next primary mismatch")
    require(next_work["secondary"]["label"] == "PSM-C1-02 / SOURCE-IDENTITY / SI-1u", "next secondary mismatch")
    require(next_work["next_required_artifact"] == NEXT, "next work artifact mismatch")

    require(cert["status"] == STATUS, "cert status mismatch")
    require(cert["local_source_identity_closed"] is True, "cert local source identity missing")
    require(cert["unpatched_source_identity_closed"] is False, "cert unpatched overclosed")
    require(cert["conditional_unpatched_packet_passes_if_theorem_supplied"] is True, "cert conditional missing")

    require("Status label: `PSM-C1-02 / SOURCE-IDENTITY / SI-1d`" in note, "note label missing")
    require("local-premise source-identity closure" in note, "note local premise guard missing")
    require("They are not knobs" in note, "note superset guard missing")

    for packet in [candidate, local, ledger, theorem, cert]:
        guard(packet)

    print(f"PASS {CANDIDATE.name}: {candidate['status']}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
