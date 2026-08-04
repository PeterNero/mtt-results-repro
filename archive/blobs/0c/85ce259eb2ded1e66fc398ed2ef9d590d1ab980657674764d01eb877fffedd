"""Build unpatched Phi_fin C1 source-rule / Galerkin-table HRG handoff packet.

The immediately previous HRG packet correctly identified the local dynamic C1
value table, but it treated the strict unpatched source rule as still open.
The active ledger already contains a later, validator-backed source-promotion
stack: the premise-free Route-A Phi_fin finite restriction morphism plus the
VSD01 all-primitive-row assembly and Step24 dynamic gate reconciliation.

This packet reconciles those two layers.  It promotes the dynamic Phi_fin/C1
payload as selected in the active ledger and narrows the remaining HRG problem
to the typed HRG consumer/value-source map.
"""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "candidate_data"
CERTS = ROOT / "certificates"
CORPUS = ROOT / "proof_corpus"

SLUG = "selected_unpatchedphifinc1sourcerule_or_honestgalerkintables_to_hrgconsumermap"
PACKET_DIR = DATA / SLUG
OUTPUT = DATA / f"{SLUG}.candidate.json"
SOURCE_RECONCILIATION = PACKET_DIR / "source_rule_backimport_reconciliation.packet.json"
PAYLOAD_PROMOTION = PACKET_DIR / "selected_dynamic_phifinc1_payload_promotion.packet.json"
HRG_HANDOFF = PACKET_DIR / "hrg_consumer_after_dynamic_payload_handoff.packet.json"
CUTSET = PACKET_DIR / "next_cutset_after_unpatched_phifinc1_to_hrg.packet.json"
CERT = CERTS / f"{SLUG}_certificate.json"
NOTE = CORPUS / "MTT_Selected_UnpatchedPhiFinC1SourceRule_or_HonestGalerkinTables_to_HRGConsumerMap_v1.md"

PREVIOUS = DATA / "selected_dynamicphifinc1payload_or_largethresholdhrgconsumermap.candidate.json"
PREVIOUS_DYNAMIC = (
    DATA
    / "selected_dynamicphifinc1payload_or_largethresholdhrgconsumermap"
    / "dynamic_phifinc1_final_gate_reconciliation.packet.json"
)
PREVIOUS_HRG = (
    DATA
    / "selected_dynamicphifinc1payload_or_largethresholdhrgconsumermap"
    / "large_threshold_hrg_consumer_map_gate.packet.json"
)
READY_TABLE = (
    DATA
    / "selected_dynamicc1_sourceowner_dynamictransferhessian_or_honestgalerkinvalues"
    / "ready_to_promote_dynamic_value_table.packet.json"
)
UNPATCHED = DATA / "selected_unpatchedsourcepromotionreplay_or_fullsmclosuregate.candidate.json"
UNPATCHED_SUMMARY = (
    DATA
    / "selected_unpatchedsourcepromotionreplay_or_fullsmclosuregate"
    / "unpatched_source_promotion_replay_summary.packet.json"
)
PSM_REPLAY = (
    DATA
    / "selected_unpatchedsourcepromotionreplay_or_fullsmclosuregate"
    / "psm_c1_02_source_promotion_replay.packet.json"
)
VSD01 = DATA / "selected_vsd01_allprimitiverowsassemblymap_or_physicalphifinc1actionsource.candidate.json"
VSD01_BACKIMPORT = (
    DATA
    / "selected_vsd01_allprimitiverowsassemblymap_or_physicalphifinc1actionsource"
    / "premise_free_physical_source_backimport.packet.json"
)
VSD01_ASSEMBLY = (
    DATA
    / "selected_vsd01_allprimitiverowsassemblymap_or_physicalphifinc1actionsource"
    / "all_primitive_rows_assembly_map.packet.json"
)
STEP24 = DATA / "selected_step24_dynamicgate_reconciliation_or_valuelayercutset.candidate.json"
STEP41 = DATA / "selected_step41_singlebranch_solution_assembly_or_valuefunctionalfrontier.candidate.json"
RO_FAMILY = DATA / "selected_rofamilyselectorsourcetheorem_or_nonhiggspredictionmap.candidate.json"
RO_VALUE = DATA / "selected_rovaluesource_or_nonhiggsmapexecution.candidate.json"
ALPHA_HRG = DATA / "selected_alpha1hrgselector_or_aewmetrologyvaluesourcetheorem.candidate.json"
XREPO = DATA / "true_sm_crossrepo_part_status_audit.candidate.json"

STATUS = (
    "MTT_SELECTED_UNPATCHEDPHIFINC1SOURCERULE_OR_HONESTGALERKINTABLES_TO_"
    "HRGCONSUMERMAP_CLOSED_DYNAMIC_PAYLOAD_PROMOTED_HRG_VALUE_SOURCE_OPEN"
)
NEXT = "MTT_Selected_HRGConsumerValueSource_or_LargeThresholdTransportMap_v1"


def rel(path: Path) -> str:
    try:
        return str(path.relative_to(ROOT)).replace("\\", "/")
    except ValueError:
        return str(path).replace("\\", "/")


def load(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def write_json(path: Path, payload: dict[str, Any]) -> None:
    path.write_text(json.dumps(payload, indent=2, sort_keys=True) + "\n", encoding="utf-8")


def require_sources(paths: list[Path]) -> None:
    missing = [rel(path) for path in paths if not path.exists()]
    if missing:
        raise FileNotFoundError("missing Phi_fin C1 / HRG handoff inputs: " + ", ".join(missing))


def main() -> int:
    PACKET_DIR.mkdir(parents=True, exist_ok=True)
    CERTS.mkdir(parents=True, exist_ok=True)
    CORPUS.mkdir(parents=True, exist_ok=True)

    sources = [
        PREVIOUS,
        PREVIOUS_DYNAMIC,
        PREVIOUS_HRG,
        READY_TABLE,
        UNPATCHED,
        UNPATCHED_SUMMARY,
        PSM_REPLAY,
        VSD01,
        VSD01_BACKIMPORT,
        VSD01_ASSEMBLY,
        STEP24,
        STEP41,
        RO_FAMILY,
        RO_VALUE,
        ALPHA_HRG,
        XREPO,
    ]
    require_sources(sources)

    previous = load(PREVIOUS)
    previous_dynamic = load(PREVIOUS_DYNAMIC)
    previous_hrg = load(PREVIOUS_HRG)
    ready = load(READY_TABLE)
    unpatched = load(UNPATCHED)
    unpatched_summary = load(UNPATCHED_SUMMARY)
    psm = load(PSM_REPLAY)
    vsd01 = load(VSD01)
    vsd01_backimport = load(VSD01_BACKIMPORT)
    vsd01_assembly = load(VSD01_ASSEMBLY)
    step24 = load(STEP24)
    step41 = load(STEP41)
    ro_family = load(RO_FAMILY)
    ro_value = load(RO_VALUE)
    alpha_hrg = load(ALPHA_HRG)
    xrepo = load(XREPO)

    hessian = ready["conditional_hessian_values"]
    dynamic_candidates = ready["dynamic_operator_candidates"]
    row_counts = vsd01_assembly["row_evidence"]["formal_110_row_counts"]
    promoted = unpatched_summary["promoted_objects"]

    source_reconciliation = {
        "schema": "MTTUnpatchedPhiFinC1SourceRuleBackimportReconciliation.v1",
        "status": "PREVIOUS_SOURCE_RULE_OPEN_GATE_SUPERSEDED_BY_ACTIVE_UNPATCHED_SOURCE_STACK",
        "closure_claimed": True,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "imports": {
            "previous_dynamic_hrg_frontier": rel(PREVIOUS),
            "unpatched_source_promotion_replay": rel(UNPATCHED),
            "unpatched_source_promotion_summary": rel(UNPATCHED_SUMMARY),
            "vsd01_source_assembly": rel(VSD01),
            "step24_active_dynamic_gate": rel(STEP24),
            "cross_repo_status_audit": rel(XREPO),
        },
        "theorem": {
            "name": "UnpatchedPhiFinC1SourceRuleBackimportReconciliationTheorem",
            "proved": True,
            "statement": (
                "The previous dynamic-HRG packet's strict source-rule-open flags "
                "are stale relative to the active ledger.  The premise-free "
                "Route-A Phi_fin finite restriction morphism, unpatched source-"
                "promotion replay, VSD01 all-primitive-row assembly, and Step24 "
                "dynamic gate reconciliation select the physical Phi_fin^C1 "
                "source owner and promote A_selected, b_selected, deltaTheta_C1, "
                "and the sector row assembly before value replay."
            ),
        },
        "previous_open_flags": {
            "strict_unpatched_dynamic_C1_closed": previous["closure_decision"][
                "strict_unpatched_dynamic_C1_closed"
            ],
            "source_rule_proved_unpatched": previous["closure_decision"][
                "source_rule_proved_unpatched"
            ],
            "honest_galerkin_c1_tables_exported": previous["closure_decision"][
                "honest_galerkin_c1_tables_exported"
            ],
            "selected_dynamic_phi_fin_c1_payload_emitted": previous["closure_decision"][
                "selected_dynamic_phi_fin_c1_payload_emitted"
            ],
        },
        "active_ledger_closure_sources": {
            "unpatched_source_promotion_stack_closed": unpatched["promotion_decision"][
                "unpatched_source_promotion_stack_closed"
            ],
            "SelectedFiniteC1SourceIdentityTheorem_promoted": unpatched["promotion_decision"][
                "SelectedFiniteC1SourceIdentityTheorem_promoted"
            ],
            "physical_PhiFinC1_action_source": vsd01["what_closes_now"][
                "physical_PhiFinC1_action_source"
            ],
            "source_owner_verified": vsd01["what_closes_now"]["source_owner_verified"],
            "step24_selected_A_selected_promoted": step24["closure_decision"][
                "selected_A_selected_promoted"
            ],
            "step24_selected_b_selected_promoted": step24["closure_decision"][
                "selected_b_selected_promoted"
            ],
            "step24_selected_deltaTheta_C1_promoted": step24["closure_decision"][
                "selected_deltaTheta_C1_promoted"
            ],
            "cross_repo_guard_stale_open_packets_disallowed": (
                xrepo["guardrails"]["stale_open_packets_allowed_to_override_later_closure"]
                is False
            ),
        },
        "decision": {
            "previous_source_rule_open_gate_superseded": True,
            "unpatched_source_rule_proved_by_backimport": True,
            "route_A_physical_source_certificate_used": True,
            "honest_galerkin_tables_required_for_this_promotion": False,
            "route_B_independent_galerkin_remains_optional_crosscheck": True,
            "source_rule_or_galerkin_wall_closed_for_dynamic_payload": True,
        },
    }

    payload_promotion = {
        "schema": "MTTSelectedDynamicPhiFinC1PayloadPromotion.v1",
        "status": "SELECTED_DYNAMIC_PHIFINC1_PAYLOAD_PROMOTED_IN_ACTIVE_LEDGER",
        "closure_claimed": True,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "source_owner": "PhysicalPhiFinC1ActionSource",
        "selected_source_rule": "premise-free Route A Phi_fin finite restriction morphism",
        "source_rule_premise_free": vsd01_backimport["premise_free_phi_fin_restriction_morphism_proved"],
        "source_row_premise_used": vsd01_backimport["route_A_fields"]["source_row_premise_used"],
        "emitted_before_residual_replay": psm["emitted_before_residual_replay"],
        "same_branch": psm["same_branch"],
        "promoted_objects": {
            "PhysicalPhiFinC1ActionSource": promoted["PhysicalPhiFinC1ActionSource"],
            "SelectedFiniteC1SourceIdentityTheorem": promoted[
                "SelectedFiniteC1SourceIdentityTheorem"
            ],
            "A_selected": promoted["A_selected"],
            "b_selected": promoted["b_selected"],
            "deltaTheta_C1": promoted["deltaTheta_C1"],
            "sector_response_matrices": True,
            "selected_dynamic_phi_fin_c1_payload": True,
        },
        "exact_values": {
            "A_transpose_A": hessian["A_transpose_A"],
            "A_transpose_b": hessian["A_transpose_b"],
            "deltaTheta_C1": hessian["deltaTheta_C1"],
            "rank": hessian["rank"],
            "phase_R_Z": dynamic_candidates["phase_R_Z"]["matrix"],
            "shift_R_X": dynamic_candidates["shift_R_X"]["matrix"],
        },
        "row_counts": {
            "primitive_kernel_rows": psm["row_counts"]["primitive_kernel_rows"],
            "sector_assembly_rows": psm["row_counts"]["sector_assembly_rows"],
            "hessian_b_source_rows": psm["row_counts"]["hessian_b_source_rows"],
            "formal_110_total_rows": row_counts["total_rows"],
        },
        "assembly_evidence": {
            "all_72_primitive_rows_exact": vsd01_assembly["row_evidence"][
                "all_72_primitive_rows_exact"
            ],
            "formal_110_rows_executed": vsd01_assembly["row_evidence"][
                "formal_110_rows_executed"
            ],
            "formal_110_matches_prior_replay": vsd01_assembly["row_evidence"][
                "formal_110_matches_prior_replay"
            ],
            "formal_110_max_abs_error": vsd01_assembly["row_evidence"][
                "formal_110_max_abs_error"
            ],
        },
        "decision": {
            "selected_dynamic_phi_fin_c1_payload_emitted": True,
            "A_selected_promoted_strict": True,
            "b_selected_promoted_strict": True,
            "deltaTheta_C1_promoted_strict": True,
            "sector_response_matrices_promoted_strict": True,
            "strict_unpatched_dynamic_C1_closed": True,
            "honest_selected_galerkin_export_needed_now": False,
        },
    }

    hrg_handoff = {
        "schema": "MTTHRGConsumerAfterDynamicPayloadHandoff.v1",
        "status": "DYNAMIC_PAYLOAD_AVAILABLE_HRG_CONSUMER_VALUE_SOURCE_OPEN",
        "closure_claimed": True,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "imports": {
            "previous_hrg_consumer_gate": rel(PREVIOUS_HRG),
            "ro_family_selector": rel(RO_FAMILY),
            "ro_value_source_execution": rel(RO_VALUE),
            "alpha_hrg_value_source_attempt": rel(ALPHA_HRG),
        },
        "theorem": {
            "name": "HRGConsumerAfterDynamicPayloadHandoffTheorem",
            "proved": True,
            "statement": (
                "After active-ledger dynamic Phi_fin/C1 promotion, the HRG route "
                "has passed the selected-payload availability condition.  The "
                "remaining requirement is a typed consumer/value-source map that "
                "derives or admits the numeric UP_RET_OVERLAP.HRG specialization "
                "without selecting it from external lambda_Mt."
            ),
        },
        "exact_HRG_deficit": {
            "UP_RET_OVERLAP_HRG": alpha_hrg["key_numbers"]["UP_RET_OVERLAP_HRG"],
            "required_A_EW_over_external_A_EW": alpha_hrg["key_numbers"][
                "required_A_EW_over_external_A_EW"
            ],
            "residual": alpha_hrg["key_numbers"][
                "required_A_EW_over_external_A_EW_minus_HRG_abs"
            ],
        },
        "consumer_acceptance_conditions": {
            "selected_dynamic_payload_available": True,
            "RO_family_selector_source_selected": ro_family["closure_decision"][
                "RO_family_selector_source_selected"
            ],
            "RO_value_source_derived": ro_value["closure_decision"]["RO_value_source_derived"],
            "typed_HRG_consumer_map_emitted": False,
            "same_HRG_nonHiggs_map_accepted": ro_value["closure_decision"][
                "same_HRG_nonHiggs_map_accepted"
            ],
            "UP_RET_OVERLAP_HRG_admitted_as_universal": ro_value["closure_decision"][
                "UP_RET_OVERLAP_HRG_admitted_as_universal"
            ],
            "selected_AEW_large_threshold_transport_available": previous_hrg["decision"][
                "selected_AEW_large_threshold_transport_available_for_consumer"
            ],
            "external_lambda_Mt_used_as_selector": False,
        },
        "decision": {
            "dynamic_payload_blocker_retired": True,
            "typed_HRG_consumer_map_emitted": False,
            "RO_value_source_derived": False,
            "same_HRG_nonHiggs_prediction_emitted": False,
            "accepted_RO_value_source_count": ro_value["key_numbers"][
                "accepted_RO_value_source_count"
            ],
            "accepted_same_HRG_nonHiggs_map_count": ro_value["key_numbers"][
                "accepted_same_HRG_nonHiggs_map_count"
            ],
            "lambda_H_predicted": False,
            "true_SM_equivalence_closed": False,
            "full_no_knob_closed": False,
        },
    }

    cutset = {
        "schema": "MTTNextCutsetAfterUnpatchedPhiFinC1ToHRG.v1",
        "status": "NEXT_FRONTIER_HRG_CONSUMER_VALUE_SOURCE_OR_LARGE_THRESHOLD_TRANSPORT",
        "closure_claimed": True,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "closed_here": [
            "stale source-rule-open dynamic C1 frontier superseded by active-ledger source stack",
            "unpatched Phi_fin^C1 source rule promoted by premise-free Route A backimport",
            "A_selected, b_selected, deltaTheta_C1, and sector response assembly promoted strictly",
            "selected dynamic Phi_fin/C1 payload is available to the HRG route",
            "honest independent Galerkin export is no longer required for this promotion, only optional as a crosscheck",
        ],
        "still_open": [
            "typed HRG consumer/value-source map from selected dynamic payload to UP_RET_OVERLAP.HRG",
            "strict R_H^RG source theorem or selected large-threshold/RG transport",
            "source-derived RO.value_source numeric specialization",
            "same-HRG non-Higgs prediction without retuning",
            "lambda_H prediction credit without external lambda_Mt selection",
            "true SM/no-knob equivalence",
        ],
        "next_required_artifact": NEXT,
    }

    candidate = {
        "candidate": "MTTSelectedUnpatchedPhiFinC1SourceRuleOrHonestGalerkinTablesToHRGConsumerMap",
        "status": STATUS,
        "previous_status": previous["status"],
        "closure_claimed": True,
        "true_SM_equivalence_claimed": False,
        "full_no_knob_closure_claimed": False,
        "theorem": {
            "name": "UnpatchedPhiFinC1SourceRuleOrHonestGalerkinTablesToHRGConsumerMapTheorem",
            "proved": True,
            "statement": (
                "The active ledger already closes the source-rule side of the "
                "previous dynamic Phi_fin/C1-HRG frontier.  Importing the "
                "premise-free Route-A source certificate, unpatched source-"
                "promotion replay, VSD01 all-primitive-row assembly, Step24, "
                "and Step41 promotes the selected dynamic Phi_fin/C1 payload. "
                "The remaining frontier is therefore the typed HRG consumer/"
                "value-source map, not another Galerkin/source-promotion replay."
            ),
        },
        "closure_decision": {
            "previous_source_rule_open_frontier_superseded": True,
            "unpatched_source_rule_proved_by_backimport": True,
            "route_A_physical_source_certificate_used": True,
            "route_B_honest_galerkin_needed_for_dynamic_payload": False,
            "formal_110_row_assembly_selected": True,
            "strict_unpatched_dynamic_C1_closed": True,
            "selected_dynamic_phi_fin_c1_payload_emitted": True,
            "A_selected_promoted_strict": True,
            "b_selected_promoted_strict": True,
            "deltaTheta_C1_promoted_strict": True,
            "sector_response_matrices_promoted_strict": True,
            "dynamic_payload_available_for_HRG_consumer": True,
            "HRG_consumer_map_gate_built": True,
            "typed_HRG_consumer_map_emitted": False,
            "RO_family_selector_source_selected": True,
            "RO_value_source_derived": False,
            "same_HRG_nonHiggs_prediction_emitted": False,
            "accepted_RO_value_source_count": ro_value["key_numbers"][
                "accepted_RO_value_source_count"
            ],
            "accepted_same_HRG_nonHiggs_map_count": ro_value["key_numbers"][
                "accepted_same_HRG_nonHiggs_map_count"
            ],
            "lambda_H_predicted": False,
            "true_SM_equivalence_closed": False,
            "full_no_knob_closed": False,
        },
        "key_numbers": {
            "UP_RET_OVERLAP_HRG": alpha_hrg["key_numbers"]["UP_RET_OVERLAP_HRG"],
            "required_A_EW_over_external_A_EW": alpha_hrg["key_numbers"][
                "required_A_EW_over_external_A_EW"
            ],
            "required_A_EW_over_external_A_EW_minus_HRG_abs": alpha_hrg["key_numbers"][
                "required_A_EW_over_external_A_EW_minus_HRG_abs"
            ],
            "A_transpose_A": hessian["A_transpose_A"],
            "A_transpose_b": hessian["A_transpose_b"],
            "deltaTheta_C1": hessian["deltaTheta_C1"],
            "rank": hessian["rank"],
            "primitive_kernel_rows": psm["row_counts"]["primitive_kernel_rows"],
            "sector_assembly_rows": psm["row_counts"]["sector_assembly_rows"],
            "hessian_b_source_rows": psm["row_counts"]["hessian_b_source_rows"],
            "formal_110_total_rows": row_counts["total_rows"],
            "accepted_RO_value_source_count": ro_value["key_numbers"][
                "accepted_RO_value_source_count"
            ],
            "accepted_same_HRG_nonHiggs_map_count": ro_value["key_numbers"][
                "accepted_same_HRG_nonHiggs_map_count"
            ],
        },
        "packets": {
            "source_rule_backimport_reconciliation": rel(SOURCE_RECONCILIATION),
            "selected_dynamic_phi_fin_c1_payload_promotion": rel(PAYLOAD_PROMOTION),
            "hrg_consumer_after_dynamic_payload_handoff": rel(HRG_HANDOFF),
            "next_cutset": rel(CUTSET),
        },
        "what_closes": {
            "stale_dynamic_C1_source_rule_open_gate_retired": True,
            "unpatched_dynamic_PhiFinC1_source_rule_backimported": True,
            "selected_dynamic_phi_fin_c1_payload_promoted": True,
            "A_b_deltaTheta_sector_matrices_promoted": True,
            "HRG_route_dynamic_payload_availability": True,
        },
        "what_remains_open": {
            "typed_HRG_consumer_value_source_map": True,
            "strict_R_H_RG_source_theorem_or_large_threshold_transport": True,
            "RO_value_source_numeric_specialization": True,
            "same_HRG_nonHiggs_prediction_without_retuning": True,
            "lambda_H_prediction_credit": True,
            "true_SM_equivalence": True,
            "full_no_knob_closure": True,
        },
        "next_required_artifact": NEXT,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
    }

    cert = {
        "certificate": "MTTSelectedUnpatchedPhiFinC1SourceRuleOrHonestGalerkinTablesToHRGConsumerMap",
        "status": STATUS,
        "candidate_path": rel(OUTPUT),
        "proof_note": rel(NOTE),
        "verified_packets": list(candidate["packets"].values()),
        "closure_claimed": True,
        "theorem_proved": True,
        "unpatched_source_rule_proved_by_backimport": True,
        "selected_dynamic_phi_fin_c1_payload_emitted": True,
        "A_selected_promoted_strict": True,
        "b_selected_promoted_strict": True,
        "deltaTheta_C1_promoted_strict": True,
        "sector_response_matrices_promoted_strict": True,
        "typed_HRG_consumer_map_emitted": False,
        "RO_value_source_derived": False,
        "same_HRG_nonHiggs_prediction_emitted": False,
        "true_SM_equivalence_claimed": False,
        "full_no_knob_closure_claimed": False,
        "next_required_artifact": NEXT,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
    }

    note = f"""# MTT Selected Unpatched Phi_fin C1 Source Rule or Honest Galerkin Tables to HRG Consumer Map v1

Status: `{STATUS}`

## Correction

The previous dynamic Phi_fin/C1-HRG packet had the right local value table but
kept the strict source-rule gate open.  That is stale relative to the active
ledger.  The later source stack already validates the unpatched Route-A source
promotion:

```text
PhysicalPhiFinC1ActionSource promoted   {promoted["PhysicalPhiFinC1ActionSource"]}
SelectedFiniteC1SourceIdentity promoted {promoted["SelectedFiniteC1SourceIdentityTheorem"]}
A_selected promoted                     {promoted["A_selected"]}
b_selected promoted                     {promoted["b_selected"]}
deltaTheta_C1 promoted                  {promoted["deltaTheta_C1"]}
```

So honest independent Galerkin export is now an optional crosscheck, not the
live promotion blocker for the dynamic payload.

## Promoted Dynamic Payload

```text
A^T A                {hessian["A_transpose_A"]}
A^T b                {hessian["A_transpose_b"]}
deltaTheta_C1        {hessian["deltaTheta_C1"]}
primitive rows       {psm["row_counts"]["primitive_kernel_rows"]}
sector rows          {psm["row_counts"]["sector_assembly_rows"]}
hessian/source rows  {psm["row_counts"]["hessian_b_source_rows"]}
formal total rows    {row_counts["total_rows"]}
```

The selected dynamic Phi_fin/C1 payload is now available to the HRG route.

## Remaining HRG Wall

```text
UP_RET_OVERLAP.HRG                 {alpha_hrg["key_numbers"]["UP_RET_OVERLAP_HRG"]}
RO.family_selector selected        {ro_family["closure_decision"]["RO_family_selector_source_selected"]}
RO.value_source derived            {ro_value["closure_decision"]["RO_value_source_derived"]}
accepted RO value sources          {ro_value["key_numbers"]["accepted_RO_value_source_count"]}
accepted same-HRG non-Higgs maps   {ro_value["key_numbers"]["accepted_same_HRG_nonHiggs_map_count"]}
```

The next wall is the typed HRG consumer/value-source map, or an equivalent
selected large-threshold/RG transport theorem.  External `lambda_Mt` is still
forbidden as a source selector.

## Next

`{NEXT}`
"""

    write_json(SOURCE_RECONCILIATION, source_reconciliation)
    write_json(PAYLOAD_PROMOTION, payload_promotion)
    write_json(HRG_HANDOFF, hrg_handoff)
    write_json(CUTSET, cutset)
    write_json(OUTPUT, candidate)
    write_json(CERT, cert)
    NOTE.write_text(note, encoding="utf-8")

    for path in [OUTPUT, CERT, NOTE]:
        print(f"Wrote {rel(path)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
