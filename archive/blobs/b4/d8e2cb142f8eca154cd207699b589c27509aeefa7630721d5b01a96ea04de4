"""Audit PSM-C1-02 SI-1c action-kernel theorem/local-principle decision."""

from __future__ import annotations

import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "candidate_data"
CERTS = ROOT / "certificates"
CORPUS = ROOT / "proof_corpus"

SLUG = "selected_psm_c1_02_selectedphifinc1_preresidualactionkernel_theorem_or_localprincipledecision"
BASE = DATA / SLUG
CANDIDATE = DATA / f"{SLUG}.candidate.json"
UNPATCHED = BASE / "unpatched_theorem_derivation_attempt.packet.json"
LOCAL = BASE / "local_principle_kernel_closure_import.packet.json"
DECISION = BASE / "si1c_decision.packet.json"
NEXT_WORK = BASE / "next_labeled_workorder.packet.json"
CERT = CERTS / f"{SLUG}_certificate.json"
NOTE = CORPUS / "MTT_Selected_PSM_C1_02_SelectedPhiFinC1PreResidualActionKernelTheorem_Proof_or_LocalPrincipleDecision_v1.md"

STATUS = "MTT_SELECTED_PSM_C1_02_SI1C_LOCAL_PHIFINC1_PRERESIDUAL_ACTION_KERNEL_CLOSED_UNPATCHED_THEOREM_OPEN"
NEXT = "MTT_Selected_PSM_C1_02_LocalSourceIdentityClosure_Integration_or_UnpatchedKernelExecution_v1"


def load(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def require(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)


def guard(packet: dict) -> None:
    require(packet.get("observed_data_used_as_selector") is False, "observed selector violation")
    require(packet.get("target_fitting_used") is False, "target fitting violation")
    require(packet.get("closure_claimed") is False, "closure overclaim")


def main() -> int:
    candidate = load(CANDIDATE)
    unpatched = load(UNPATCHED)
    local = load(LOCAL)
    decision = load(DECISION)
    next_work = load(NEXT_WORK)
    cert = load(CERT)
    note = NOTE.read_text(encoding="utf-8")

    require(candidate["status"] == STATUS, "candidate status mismatch")
    require(candidate["active_label"] == "PSM-C1-02", "active label mismatch")
    require(candidate["active_routes"] == ["SOURCE-IDENTITY/SI-1c"], "active routes mismatch")
    require(candidate["closed_boundary"] == "DONE-PARITY-00", "closed boundary mismatch")
    require(candidate["next_required_artifact"] == NEXT, "next artifact mismatch")
    require(candidate["theorem"]["proved"] is True, "local theorem should be proved")
    require(candidate["what_closes_now"]["local_pre_residual_action_kernel_closed"] is True, "local kernel not closed")
    require(candidate["what_closes_now"]["strict_kernel_validator_ok"] is True, "validator not ok")
    require(candidate["what_closes_now"]["unpatched_exit_preserved"] is True, "unpatched exit not preserved")
    require(candidate["what_remains_open"]["unpatched_SelectedPhiFinC1PreResidualActionKernelTheorem"] is True, "unpatched theorem overclosed")
    require(candidate["what_remains_open"]["unpatched_SelectedFiniteC1SourceIdentityLemma"] is True, "unpatched source identity overclosed")

    require(unpatched["clause"] == "SI-1c", "unpatched clause mismatch")
    require(unpatched["theorem_name"] == "SelectedPhiFinC1PreResidualActionKernelTheorem", "unpatched theorem mismatch")
    require(unpatched["unpatched_theorem_derived_now"] is False, "unpatched theorem overderived")
    require(len(unpatched["why_not_derived"]) >= 3, "unpatched reason list too short")

    require(local["local_principle_accepted"] is True, "local principle not accepted")
    require(local["accepted_as"] == "explicit local premise, not unpatched theorem", "local accepted_as guard mismatch")
    require(local["strict_kernel_validator_ok"] is True, "strict validator not ok")
    require(local["strict_kernel_closed_under_local_principle"] is True, "local kernel not closed")
    require(local["audit_ok"] is True, "imported existing audit did not pass")
    for value in local["promoted_inside_local_spine"].values():
        require(value is True, "local promoted field missing")
    for value in local["does_not_close"].values():
        require(value is True, "does-not-close guard missing")

    require(decision["status"] == "LOCAL_PRINCIPLE_CLOSES_SI1C_KERNEL_UNPATCHED_THEOREM_REMAINS_OPEN", "decision status mismatch")
    require(decision["unpatched_theorem_derived_now"] is False, "decision overderives theorem")
    require(decision["local_principle_accepted"] is True, "decision local principle not accepted")
    require(decision["local_pre_residual_action_kernel_closed"] is True, "decision local kernel not closed")
    require(decision["source_identity_lemma_status"] == "CLOSED_ONLY_RELATIVE_TO_ACCEPTED_LOCAL_WEYLVARIATION_ACTION_PRINCIPLE", "local source identity status mismatch")
    require(decision["unpatched_source_identity_lemma_status"] == "OPEN", "unpatched source identity should remain open")
    require(decision["superset_strategy"]["paths_used_as_free_parameters"] is False, "superset paths used as knobs")

    require(next_work["primary"]["label"] == "PSM-C1-02 / SOURCE-IDENTITY / SI-1d", "next primary label mismatch")
    require(next_work["secondary"]["label"] == "PSM-C1-02 / SOURCE-IDENTITY / SI-1u", "next secondary label mismatch")
    require(next_work["next_required_artifact"] == NEXT, "next work artifact mismatch")

    require(cert["status"] == STATUS, "cert status mismatch")
    require(cert["local_principle_accepted"] is True, "cert local principle missing")
    require(cert["strict_kernel_validator_ok"] is True, "cert validator not ok")
    require(cert["local_pre_residual_action_kernel_closed"] is True, "cert local kernel not closed")
    require(cert["unpatched_theorem_derived_now"] is False, "cert overderives unpatched theorem")

    require("Status label: `PSM-C1-02 / SOURCE-IDENTITY / SI-1c`" in note, "note label missing")
    require("local-premise closure" in note, "note local-premise guard missing")
    require("They are not knobs" in note, "note superset guard missing")

    for packet in [candidate, unpatched, local, decision, cert]:
        guard(packet)

    print(f"PASS {CANDIDATE.name}: {candidate['status']}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
