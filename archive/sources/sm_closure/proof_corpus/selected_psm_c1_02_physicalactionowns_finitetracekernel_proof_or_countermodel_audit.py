"""Audit PSM-C1-02 physical-action finite-trace ownership proof/countermodel."""

from __future__ import annotations

import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "candidate_data"
CERTS = ROOT / "certificates"
CORPUS = ROOT / "proof_corpus"

SLUG = "selected_psm_c1_02_physicalactionowns_finitetracekernel_proof_or_countermodel"
BASE = DATA / SLUG
CANDIDATE = DATA / f"{SLUG}.candidate.json"
DIRECT = BASE / "direct_proof_attempt.packet.json"
COUNTERMODEL = BASE / "support_only_countermodel_import.packet.json"
REMAINING = BASE / "remaining_kernel_theorem.packet.json"
NEXT_WORK = BASE / "next_labeled_workorder.packet.json"
CERT = CERTS / f"{SLUG}_certificate.json"
NOTE = CORPUS / "MTT_Selected_PSM_C1_02_PhysicalActionOwnsFiniteTraceKernel_Proof_or_Countermodel_v1.md"

STATUS = "MTT_SELECTED_PSM_C1_02_PHYSICALACTIONOWNS_FINITETRACEKERNEL_ATTACK_BUILT_COUNTERMODEL_SUPPORT_ONLY_PROOF_BLOCKED"
NEXT = "MTT_Selected_PSM_C1_02_SelectedPhiFinC1PreResidualActionKernelTheorem_Proof_or_LocalPrincipleDecision_v1"


def load(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def require(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)


def main() -> int:
    candidate = load(CANDIDATE)
    direct = load(DIRECT)
    countermodel = load(COUNTERMODEL)
    remaining = load(REMAINING)
    next_work = load(NEXT_WORK)
    cert = load(CERT)
    note = NOTE.read_text(encoding="utf-8")

    require(candidate["status"] == STATUS, "candidate status mismatch")
    require(candidate["active_label"] == "PSM-C1-02", "active label mismatch")
    require(candidate["active_routes"] == ["SOURCE-IDENTITY/SI-1a", "SOURCE-IDENTITY/SI-1b"], "active routes mismatch")
    require(candidate["closed_boundary"] == "DONE-PARITY-00", "closed boundary mismatch")
    require(candidate["next_required_artifact"] == NEXT, "next artifact mismatch")
    require(candidate["closure_claimed"] is False, "candidate overclaims closure")
    require(candidate["observed_data_used_as_selector"] is False, "candidate observed selector")
    require(candidate["target_fitting_used"] is False, "candidate target fitting")
    require(candidate["what_closes_now"]["direct_proof_attempt_completed"] is True, "direct attempt not recorded")
    require(candidate["what_closes_now"]["support_only_countermodel_imported"] is True, "countermodel not imported")
    require(candidate["what_closes_now"]["closed_support_alone_blocked_as_derivation_route"] is True, "support route not blocked")
    require(candidate["what_closes_now"]["remaining_kernel_theorem_identified"] is True, "remaining theorem missing")
    require(candidate["what_remains_open"]["PhysicalActionOwnsFiniteTraceKernel"] is True, "physical action theorem overclosed")
    require(candidate["what_remains_open"]["SelectedFiniteC1SourceIdentityLemma_unpatched"] is True, "source identity lemma overclosed")

    require(direct["target"] == "PhysicalActionOwnsFiniteTraceKernel", "direct target mismatch")
    require(all(direct["closed_subclauses"].values()), "not all route A closed subclauses true")
    require(all(direct["still_required_physical_subclauses"].values()), "not all required physical subclauses marked open")
    require(direct["proof_result"]["physical_action_owns_finite_trace_kernel_proved_now"] is False, "direct proof overclosed")
    require(direct["closure_claimed"] is False, "direct proof claims closure")

    require(countermodel["support_only_countermodel_valid"] is True, "support countermodel invalid")
    require(countermodel["closed_support_not_enough"] is True, "closed support route not blocked")
    require(countermodel["validator_rejects_current_two_exit_packet"] is True, "validator should reject support-only packet")
    require(countermodel["blocks_derivation_from_closed_support_alone"] is True, "support-only derivation not blocked")
    require(all(countermodel["closed_support_facts_true"].values()), "closed support facts should all be true")
    require(all(countermodel["additional_structural_support_true"].values()), "additional structural support should all be true")
    require(not any(countermodel["source_promotion_fields_false"].values()), "source promotion false fields should remain false")
    require(countermodel["closure_claimed"] is False, "countermodel claims closure")

    require(remaining["theorem_name"] == "SelectedPhiFinC1PreResidualActionKernelTheorem", "remaining theorem mismatch")
    require(remaining["proved_now"] is False, "remaining theorem overclosed")
    require(remaining["must_not_be_used_as_free_patch"] is True, "free patch guardrail missing")
    forbidden = " ".join(remaining["forbidden_shortcuts"])
    require("observed SM values" in forbidden, "observed values shortcut missing")
    require("A^T b" in forbidden, "locked target shortcut missing")
    require(remaining["closure_claimed"] is False, "remaining theorem claims closure")

    require(next_work["primary"]["label"] == "PSM-C1-02 / SOURCE-IDENTITY / SI-1c", "next primary label mismatch")
    require(next_work["next_required_artifact"] == NEXT, "next work artifact mismatch")
    require(next_work["superset_strategy"]["paths_used_as_free_parameters"] is False, "superset paths used as knobs")

    require(cert["status"] == STATUS, "cert status mismatch")
    require(cert["physical_action_owns_finite_trace_kernel_proved"] is False, "cert overproves action ownership")
    require(cert["support_only_countermodel_valid"] is True, "cert countermodel invalid")
    require(cert["closed_support_alone_blocked_as_derivation_route"] is True, "cert support route not blocked")
    require(cert["remaining_kernel_theorem"] == "SelectedPhiFinC1PreResidualActionKernelTheorem", "cert remaining theorem mismatch")
    require(cert["closure_claimed"] is False, "cert claims closure")

    require("Status label: `PSM-C1-02 / SOURCE-IDENTITY / SI-1a`" in note, "note SI-1a label missing")
    require("Countermodel label: `PSM-C1-02 / SOURCE-IDENTITY / SI-1b`" in note, "note SI-1b label missing")
    require("SelectedPhiFinC1PreResidualActionKernelTheorem" in note, "note remaining theorem missing")
    require("They are not knobs" in note, "note superset guardrail missing")

    print(f"PASS {CANDIDATE.name}: {candidate['status']}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
