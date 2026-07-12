"""Audit PSM-C1-02 RA-3/RB-5 dynamic source-owner attack."""

from __future__ import annotations

import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "candidate_data"
CERTS = ROOT / "certificates"
CORPUS = ROOT / "proof_corpus"

BASE = DATA / "selected_psm_c1_02_ra3_samesourceemission_or_rb5_dynamicvalueownerfill"
CANDIDATE = DATA / "selected_psm_c1_02_ra3_samesourceemission_or_rb5_dynamicvalueownerfill.candidate.json"
RA3 = BASE / "route_a_ra3_samesource_emission_attack.packet.json"
RB5 = BASE / "route_b_rb5_dynamic_value_owner_fill_attack.packet.json"
REDUCTION = BASE / "four_dynamic_fields_to_single_identity_reduction.packet.json"
NEXT_WORK = BASE / "next_labeled_workorder.packet.json"
CERT = CERTS / "selected_psm_c1_02_ra3_samesourceemission_or_rb5_dynamicvalueownerfill_certificate.json"
NOTE = CORPUS / "MTT_Selected_PSM_C1_02_RouteA_RA3_SameSourceEmission_or_RouteB_RB5_DynamicValueOwnerFill_v1.md"

STATUS = "MTT_SELECTED_PSM_C1_02_RA3_SAMESOURCEEMISSION_OR_RB5_DYNAMICVALUEOWNERFILL_ATTACK_BUILT_REDUCED_TO_SINGLE_IDENTITY_OPEN"
NEXT = "MTT_Selected_PSM_C1_02_SourceIdentityLemma_Derivation_or_ExplicitLocalPrincipleDecision_v1"
OPEN_FIELDS = ["phase_R_Z_source", "shift_R_X_source", "b_selected_source", "sector_row_assembly"]


def load(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def require(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)


def main() -> int:
    candidate = load(CANDIDATE)
    ra3 = load(RA3)
    rb5 = load(RB5)
    reduction = load(REDUCTION)
    next_work = load(NEXT_WORK)
    cert = load(CERT)
    note = NOTE.read_text(encoding="utf-8")

    require(candidate["status"] == STATUS, "candidate status mismatch")
    require(candidate["active_label"] == "PSM-C1-02", "active label mismatch")
    require(candidate["active_routes"] == ["ROUTE-A/RA-3", "ROUTE-B/RB-5"], "active routes mismatch")
    require(candidate["closed_boundary"] == "DONE-PARITY-00", "closed boundary mismatch")
    require(candidate["next_required_artifact"] == NEXT, "next artifact mismatch")
    require(candidate["closure_claimed"] is False, "candidate overclaims closure")
    require(candidate["observed_data_used_as_selector"] is False, "candidate observed selector")
    require(candidate["target_fitting_used"] is False, "candidate target fitting")
    require(candidate["what_closes_now"]["four_dynamic_fields_reduced_to_single_identity"] is True, "single identity reduction missing")
    require(candidate["what_closes_now"]["conditional_source_id_validator_ready"] is True, "validator readiness missing")
    require(candidate["what_remains_open"]["SelectedFiniteC1SourceIdentityLemma_unpatched_derivation"] is True, "source identity should remain open")

    require(ra3["route_label"] == "ROUTE-A", "RA3 route mismatch")
    require(ra3["clause_id"] == "RA-3", "RA3 clause mismatch")
    require(ra3["current_route_A_accepts"] is False, "RA3 overaccepted")
    require(ra3["conditional_source_identity_validator_ready"] is True, "RA3 validator not ready")
    require(ra3["selected_finite_c1_source_identity_derived_now"] is False, "RA3 source identity overderived")
    require(ra3["selected_values_promoted_now"] is False, "RA3 selected values overpromoted")
    require(ra3["free_axiom_patch_used"] is False, "RA3 free axiom used")

    require(rb5["route_label"] == "ROUTE-B", "RB5 route mismatch")
    require(rb5["input_id"] == "RB-5", "RB5 input mismatch")
    require(rb5["current_open_dynamic_fields"] == OPEN_FIELDS, "RB5 open fields mismatch")
    require(rb5["route_B_current_accepts"] is False, "RB5 overaccepted")
    require(rb5["dynamic_fields_promoted_now"] is False, "RB5 dynamic fields overpromoted")
    require(rb5["independent_source_table_promoted_now"] is False, "RB5 table overpromoted")
    require(rb5["normal_form_identity"]["selected_identity_proved_now"] is False, "normal form overproved")
    require(rb5["rb3_support_hessian"]["A_transpose_A"] == [[12.0, 0.0], [0.0, 12.0]], "RB3 Hessian mismatch")

    require(reduction["status"] == "FOUR_DYNAMIC_FIELDS_REDUCED_TO_SELECTED_FINITE_C1_SOURCE_IDENTITY_LEMMA", "reduction status mismatch")
    require(reduction["open_dynamic_fields_before"] == OPEN_FIELDS, "reduction open fields mismatch")
    require(reduction["all_four_still_open_now"] is True, "all four should remain open")
    require(reduction["single_remaining_identity"]["name"] == "SelectedFiniteC1SourceIdentityLemma", "lemma name mismatch")
    require(reduction["single_remaining_identity"]["conditional_validator_would_pass_if_inserted"] is True, "conditional validator mismatch")
    require(reduction["single_remaining_identity"]["derived_or_accepted_now"] is False, "lemma overaccepted")
    require(reduction["if_single_identity_proved_then"]["selected_source_promotion_would_close_for_PSM_C1_02"] is True, "conditional closure missing")
    require(reduction["superset_strategy"]["paths_used_as_knobs"] is False, "paths used as knobs")
    require(reduction["superset_strategy"]["observed_values_used_as_knobs"] is False, "observed values used as knobs")

    require(next_work["primary"]["label"] == "PSM-C1-02 / SOURCE-IDENTITY / SI-1", "next primary mismatch")
    require(next_work["secondary"]["label"] == "PSM-C1-02 / SOURCE-IDENTITY / SI-2", "next secondary mismatch")
    require(next_work["next_required_artifact"] == NEXT, "next work artifact mismatch")

    require(cert["status"] == STATUS, "cert status mismatch")
    require(cert["route_A_RA3_same_source_promoted"] is False, "cert RA3 overpromoted")
    require(cert["route_B_RB5_dynamic_fields_promoted"] is False, "cert RB5 overpromoted")
    require(cert["open_dynamic_fields"] == OPEN_FIELDS, "cert open fields mismatch")
    require(cert["reduced_to_single_identity"] is True, "cert reduction missing")
    require(cert["conditional_source_id_validator_ready"] is True, "cert validator missing")
    require(cert["closure_claimed"] is False, "cert closure overclaimed")

    require("Status label: `PSM-C1-02 / ROUTE-A / RA-3`" in note, "note RA3 label missing")
    require("`PSM-C1-02 / ROUTE-B / RB-5`" in note, "note RB5 label missing")
    require("They are two constrained exits" in note, "note superset guardrail missing")

    print(f"PASS {CANDIDATE.name}: {candidate['status']}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
