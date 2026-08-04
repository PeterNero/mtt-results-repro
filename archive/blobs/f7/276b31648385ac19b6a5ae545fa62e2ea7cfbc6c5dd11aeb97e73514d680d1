"""Audit current PSM-C1-02 import of gauge-transported Phi_fin source closure."""

from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "candidate_data"
SLUG = "selected_psm_c1_02_gaugetransportedphifintrace_import_or_fullsmgap"
BASE = DATA / SLUG
CANDIDATE = DATA / f"{SLUG}.candidate.json"
IMPORT_VALIDATION = BASE / "transport_closed_phifin_import_validation.packet.json"
SOURCE_PROMOTION = BASE / "current_psm_c1_02_source_promotion_reconciliation.packet.json"
FULL_SM_GAP = BASE / "post_source_promotion_fullsm_gap.packet.json"
NEXT_WORK = BASE / "next_labeled_workorder.packet.json"
CERT = ROOT / "certificates" / f"{SLUG}_certificate.json"
NOTE = ROOT / "proof_corpus" / "MTT_Selected_PSM_C1_02_GaugeTransportedPhiFinTraceImport_or_FullSMGap_v1.md"
BUILD = ROOT / "scripts" / "build_selected_psm_c1_02_gaugetransportedphifintrace_import_or_fullsmgap.py"

STATUS = "MTT_SELECTED_PSM_C1_02_GAUGETRANSPORTEDPHIFINTRACE_IMPORT_BUILT_SOURCE_PROMOTION_CLOSED_FULLSM_OPEN"
NEXT = "MTT_Selected_PostSourcePromotionFullSMGapAudit_or_DotDAlpha1MatterRoutingClosure_v1"


def load(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def require(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)


def main() -> int:
    proc = subprocess.run(
        [sys.executable, str(BUILD)],
        cwd=ROOT,
        text=True,
        stdout=subprocess.PIPE,
        stderr=subprocess.STDOUT,
        check=False,
    )
    if proc.returncode != 0:
        print(proc.stdout)
        return 1

    candidate = load(CANDIDATE)
    import_validation = load(IMPORT_VALIDATION)
    source_promotion = load(SOURCE_PROMOTION)
    full_sm_gap = load(FULL_SM_GAP)
    next_work = load(NEXT_WORK)
    cert = load(CERT)
    note = NOTE.read_text(encoding="utf-8")

    require(candidate["status"] == STATUS, "candidate status mismatch")
    require(candidate["theorem"]["proved"] is True, "theorem not proved")
    require(candidate["closure_decision"]["PSM_C1_02_unpatched_source_promotion_closed"] is True, "PSM not closed")
    require(candidate["closure_decision"]["A_selected_promoted"] is True, "A not promoted")
    require(candidate["closure_decision"]["b_selected_promoted"] is True, "b not promoted")
    require(candidate["closure_decision"]["deltaTheta_C1_promoted"] is True, "deltaTheta not promoted")
    require(candidate["closure_decision"]["Route_A_transport_closed_import_validates"] is True, "Route A import failed")
    require(candidate["closure_decision"]["Route_B_independent_rows_required_for_PSM_closure"] is False, "Route B incorrectly required")
    require(candidate["closure_decision"]["true_SM_equivalence_closed"] is False, "true SM overclosed")
    require(candidate["closure_decision"]["full_SM_no_knob_closed"] is False, "no-knob overclosed")

    require(import_validation["transport_source_closes"]["premise_free_phi_fin_restriction_morphism"] is True, "morphism missing")
    require(import_validation["transport_source_closes"]["premise_free_route_A_physical_source_certificate"] is True, "source cert missing")
    require(import_validation["transport_source_closes"]["raw_27mode_replay_not_used"] is True, "raw replay guard missing")
    require(import_validation["narrowed_route_A_replay"]["validator_passes"] is True, "narrowed validator failed")
    require(import_validation["narrowed_route_A_replay"]["route_A_all_fields_true"] is True, "Route A fields not true")
    require(import_validation["narrowed_route_A_replay"]["same_branch_evidence_count"] >= 6, "insufficient evidence")
    require(import_validation["psm_replay"]["validator_passes"] is True, "PSM validator failed")

    require(source_promotion["unpatched_PSM_C1_02_source_promotion_closed"] is True, "source promotion not closed")
    require(source_promotion["free_axiom_patch_used"] is False, "free axiom patch used")
    require(source_promotion["locked_target_values_used_as_source"] is False, "locked target used as source")
    require(source_promotion["raw_27mode_replay_claimed"] is False, "raw 27 mode overclaimed")
    require(source_promotion["symbolic_transport_quotient_used"] is True, "symbolic quotient not used")

    require(full_sm_gap["source_stack_closed"] is True, "full gate missing source stack")
    require(full_sm_gap["true_SM_equivalence_closed"] is False, "full gap true SM overclosed")
    require(full_sm_gap["full_SM_no_knob_closed"] is False, "full gap no-knob overclosed")
    require("PSM-C1-02 unpatched source promotion" in full_sm_gap["not_remaining"], "closed gate not retired")
    require(next_work["next_required_artifact"] == NEXT, "next mismatch")
    require(cert["status"] == STATUS, "cert status mismatch")
    require(cert["PSM_C1_02_unpatched_source_promotion_closed"] is True, "cert PSM not closed")
    require("This is not true SM equivalence" in note, "note missing full SM guardrail")

    for packet in [candidate, import_validation, source_promotion, full_sm_gap, cert]:
        require(packet.get("observed_data_used_as_selector") is False, "observed selector violation")
        require(packet.get("target_fitting_used") is False, "target fitting violation")

    print(f"PASS {CANDIDATE.name}: {candidate['status']}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
