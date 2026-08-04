"""Audit PSM-C1-02 source-identity lemma derivation attempt."""

from __future__ import annotations

import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "candidate_data"
CERTS = ROOT / "certificates"
CORPUS = ROOT / "proof_corpus"

BASE = DATA / "selected_psm_c1_02_sourceidentitylemma_derivation_attempt"
CANDIDATE = DATA / "selected_psm_c1_02_sourceidentitylemma_derivation_attempt.candidate.json"
MATRIX = BASE / "source_identity_subclaim_derivation_matrix.packet.json"
OBSTRUCTION = BASE / "single_surviving_obstruction.packet.json"
EXTERNAL = BASE / "external_methodology_support.packet.json"
NEXT_WORK = BASE / "next_labeled_workorder.packet.json"
CERT = CERTS / "selected_psm_c1_02_sourceidentitylemma_derivation_attempt_certificate.json"
NOTE = CORPUS / "MTT_Selected_PSM_C1_02_SourceIdentityLemma_DerivationAttempt_v1.md"

STATUS = "MTT_SELECTED_PSM_C1_02_SOURCEIDENTITYLEMMA_DERIVATION_ATTEMPT_BUILT_REDUCED_TO_ACTION_OWNERSHIP_OPEN"
NEXT = "MTT_Selected_PSM_C1_02_PhysicalActionOwnsFiniteTraceKernel_Proof_or_Countermodel_v1"


def load(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def require(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)


def main() -> int:
    candidate = load(CANDIDATE)
    matrix = load(MATRIX)
    obstruction = load(OBSTRUCTION)
    external = load(EXTERNAL)
    next_work = load(NEXT_WORK)
    cert = load(CERT)
    note = NOTE.read_text(encoding="utf-8")

    require(candidate["status"] == STATUS, "candidate status mismatch")
    require(candidate["active_label"] == "PSM-C1-02", "active label mismatch")
    require(candidate["active_routes"] == ["SOURCE-IDENTITY/SI-1"], "active route mismatch")
    require(candidate["closed_boundary"] == "DONE-PARITY-00", "closed boundary mismatch")
    require(candidate["next_required_artifact"] == NEXT, "next artifact mismatch")
    require(candidate["closure_claimed"] is False, "candidate overclaims closure")
    require(candidate["observed_data_used_as_selector"] is False, "candidate observed selector")
    require(candidate["target_fitting_used"] is False, "candidate target fitting")
    require(candidate["what_closes_now"]["SI1_derivation_attempt_completed"] is True, "SI1 attempt missing")
    require(candidate["what_closes_now"]["single_surviving_obstruction_identified"] is True, "single obstruction missing")
    require(candidate["what_remains_open"]["PhysicalActionOwnsFiniteTraceKernel"] is True, "physical action obstruction should remain")
    require(candidate["what_remains_open"]["SelectedFiniteC1SourceIdentityLemma_unpatched"] is True, "lemma should remain open")
    require(candidate["subclaim_counts"]["derived_now"] == 2, "derived subclaim count mismatch")
    require(candidate["subclaim_counts"]["total"] == 7, "total subclaim count mismatch")

    subclaims = matrix["subclaims"]
    require(matrix["status"] == "SUBCLAIMS_AUDITED_LEMMA_UNPATCHED_OPEN", "matrix status mismatch")
    require(matrix["derived_count"] == 2, "matrix derived count mismatch")
    require(subclaims["admissible_c1_variation_space"]["derived_now"] is True, "variation space should be derived")
    require(subclaims["postcheck_independence_guard"]["derived_now"] is True, "independence guard should be derived")
    require(subclaims["selected_branch_restricts_Phi_fin_C1_to_finite_qutrit_weyl_quotient"]["derived_now"] is False, "action restriction overderived")
    require(subclaims["normalized_trace_frobenius_pairing_as_finite_source_measure"]["physical_source_measure_closed"] is False, "physical measure overclosed")
    require(subclaims["pre_residual_phase_shift_variations_emit_R_Z_R_X"]["derived_now"] is False, "R_Z/R_X overderived")
    require(subclaims["same_source_second_variation_emits_b_selected"]["derived_now"] is False, "b_selected overderived")

    require(obstruction["obstruction_name"] == "PhysicalActionOwnsFiniteTraceKernel", "obstruction mismatch")
    require(obstruction["status"] == "SINGLE_SURVIVING_OBSTRUCTION_IS_PHYSICAL_ACTION_OWNERSHIP", "obstruction status mismatch")
    require(obstruction["observed_data_used_as_selector"] is False, "obstruction observed selector")

    require(external["status"] == "EXTERNAL_SUPPORT_CLASSIFIED_AS_METHOD_ONLY_NOT_SOURCE_PROOF", "external status mismatch")
    require(all(ref["used_as_mtt_source_proof"] is False for ref in external["references"]), "external proof overclaimed")

    require(next_work["primary"]["label"] == "PSM-C1-02 / SOURCE-IDENTITY / SI-1a", "next primary mismatch")
    require(next_work["secondary"]["label"] == "PSM-C1-02 / SOURCE-IDENTITY / SI-1b", "next secondary mismatch")
    require(next_work["next_required_artifact"] == NEXT, "next work artifact mismatch")

    require(cert["status"] == STATUS, "cert status mismatch")
    require(cert["lemma_derived_unpatched"] is False, "cert lemma overderived")
    require(cert["single_surviving_obstruction"] == "PhysicalActionOwnsFiniteTraceKernel", "cert obstruction mismatch")
    require(cert["derived_subclaim_count"] == 2, "cert derived count mismatch")
    require(cert["closure_claimed"] is False, "cert closure overclaimed")

    require("Status label: `PSM-C1-02 / SOURCE-IDENTITY / SI-1`" in note, "note label missing")
    require("PhysicalActionOwnsFiniteTraceKernel" in note, "note obstruction missing")
    require("They are not knobs" in note, "note superset guardrail missing")

    print(f"PASS {CANDIDATE.name}: {candidate['status']}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
