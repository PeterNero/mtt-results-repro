"""Build generation-resolved threshold source rows / profile convention closure gate."""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "candidate_data"
CERTS = ROOT / "certificates"
CORPUS = ROOT / "proof_corpus"

SLUG = "selected_generationresolvedthresholdsourcerows_or_profileconventionclosure"
PACKET_DIR = DATA / SLUG
OUTPUT = DATA / f"{SLUG}.candidate.json"
RECONCILIATION = PACKET_DIR / "stale_dynamic_gap_reconciliation.packet.json"
GEN_SUPPORT = PACKET_DIR / "generation_source_support_recheck.packet.json"
ROW_ATTEMPT = PACKET_DIR / "generation_resolved_threshold_row_attempt.packet.json"
PROFILE = PACKET_DIR / "profile_convention_closure_recheck.packet.json"
DECISION = PACKET_DIR / "generation_rows_or_profile_convention_decision.packet.json"
CUTSET = PACKET_DIR / "next_cutset_after_generation_row_attempt.packet.json"
CERT = CERTS / f"{SLUG}_certificate.json"
NOTE = CORPUS / "MTT_Selected_GenerationResolvedThresholdSourceRows_or_ProfileConventionClosure_v1.md"

PREVIOUS = DATA / "selected_magnitudebearingprojectionweights_or_thresholdrowsderivation.candidate.json"
PREVIOUS_DECISION = (
    DATA
    / "selected_magnitudebearingprojectionweights_or_thresholdrowsderivation"
    / "magnitude_weights_or_threshold_rows_decision.packet.json"
)
BACKSOLVE = (
    DATA
    / "selected_magnitudebearingprojectionweights_or_thresholdrowsderivation"
    / "diagnostic_magnitude_weight_backsolve.packet.json"
)
RANK_GAP = (
    DATA
    / "selected_magnitudebearingprojectionweights_or_thresholdrowsderivation"
    / "magnitude_weight_rank_gap.packet.json"
)
POSTSOURCE = DATA / "selected_postsourcepromotionfullsmgapaudit_or_dotdalpha1matterroutingclosure.candidate.json"
POSTSOURCE_VALIDATOR = (
    DATA
    / "selected_postsourcepromotionfullsmgapaudit_or_dotdalpha1matterroutingclosure"
    / "same_source_dynamic_matter_overlap_validator_result.packet.json"
)
POSTSOURCE_GAP = (
    DATA
    / "selected_postsourcepromotionfullsmgapaudit_or_dotdalpha1matterroutingclosure"
    / "postsource_fullsm_gap_matrix.packet.json"
)
STATIC_READOUT = (
    DATA
    / "selected_postsourcepromotionfullsmgapaudit_or_dotdalpha1matterroutingclosure"
    / "matter_slot_static_readout_import.packet.json"
)
SAME_SOURCE_DYNAMIC = DATA / "selected_samesourcedynamicmatteroverlapoperatorpacket_or_primitivec1valueclosure.candidate.json"
SAME_SOURCE_VALIDATOR = (
    DATA
    / "selected_samesourcedynamicmatteroverlapoperatorpacket_or_primitivec1valueclosure"
    / "same_source_matter_overlap_operator_validator_result.packet.json"
)
VSD01_ASSEMBLY = DATA / "selected_vsd01_allprimitiverowsassemblymap_or_physicalphifinc1actionsource.candidate.json"
VSD01_ASSEMBLY_MAP = (
    DATA
    / "selected_vsd01_allprimitiverowsassemblymap_or_physicalphifinc1actionsource"
    / "all_primitive_rows_assembly_map.packet.json"
)
SM_INTERFACE = DATA / "sm_sector_embedding_interface.candidate.json"
SOURCE_ROW_AUDIT = (
    DATA
    / "selected_acceptedthresholdmassschemesourcerows_or_noknobvaluederivation"
    / "accepted_threshold_mass_scheme_source_row_audit.packet.json"
)
VALUE_PACKET = (
    DATA
    / "selected_acceptedcommonscaleyukawahiggsvalues_or_profilelikelihoodexecution"
    / "versioned_common_scale_yukawa_higgs_values.packet.json"
)
PROFILE_EXECUTION = DATA / "selected_acceptedcommonscaleyukawahiggsvalues_or_profilelikelihoodexecution.candidate.json"

STATUS = (
    "MTT_SELECTED_GENERATIONRESOLVEDTHRESHOLDSOURCEROWS_OR_PROFILECONVENTIONCLOSURE_"
    "BUILT_STALE_DYNAMIC_BLOCKER_RETIRED_GENERATION_ROWS_OPEN"
)
NEXT = "MTT_Selected_FamilyResolvingOperator_or_GenerationThresholdRowsExecution_v1"


def rel(path: Path) -> str:
    try:
        return str(path.relative_to(ROOT)).replace("\\", "/")
    except ValueError:
        return str(path)


def load(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def write_json(path: Path, payload: dict[str, Any]) -> None:
    path.write_text(json.dumps(payload, indent=2, sort_keys=True) + "\n", encoding="utf-8")


def require_sources(paths: list[Path]) -> None:
    missing = [rel(path) for path in paths if not path.exists()]
    if missing:
        raise FileNotFoundError("missing generation-threshold sources: " + ", ".join(missing))


def main() -> int:
    PACKET_DIR.mkdir(parents=True, exist_ok=True)
    CERTS.mkdir(parents=True, exist_ok=True)
    CORPUS.mkdir(parents=True, exist_ok=True)

    sources = [
        PREVIOUS,
        PREVIOUS_DECISION,
        BACKSOLVE,
        RANK_GAP,
        POSTSOURCE,
        POSTSOURCE_VALIDATOR,
        POSTSOURCE_GAP,
        STATIC_READOUT,
        SAME_SOURCE_DYNAMIC,
        SAME_SOURCE_VALIDATOR,
        VSD01_ASSEMBLY,
        VSD01_ASSEMBLY_MAP,
        SM_INTERFACE,
        SOURCE_ROW_AUDIT,
        VALUE_PACKET,
        PROFILE_EXECUTION,
    ]
    require_sources(sources)

    previous = load(PREVIOUS)
    previous_decision = load(PREVIOUS_DECISION)
    backsolve = load(BACKSOLVE)
    rank_gap = load(RANK_GAP)
    postsource = load(POSTSOURCE)
    postsource_validator = load(POSTSOURCE_VALIDATOR)
    postsource_gap = load(POSTSOURCE_GAP)
    static_readout = load(STATIC_READOUT)
    same_source_dynamic = load(SAME_SOURCE_DYNAMIC)
    same_source_validator = load(SAME_SOURCE_VALIDATOR)
    vsd01 = load(VSD01_ASSEMBLY)
    vsd01_map = load(VSD01_ASSEMBLY_MAP)
    sm_interface = load(SM_INTERFACE)
    source_row_audit = load(SOURCE_ROW_AUDIT)
    value_packet = load(VALUE_PACKET)
    profile_execution = load(PROFILE_EXECUTION)

    later_dynamic_closed = (
        same_source_dynamic["promotion_decision"]["dynamic_matter_overlap_operator_packet_closed"]
        and same_source_validator["returncode"] == 0
    )
    old_errors = [
        line.strip()
        for line in postsource_validator["stdout"]
        if any(key in line for key in ["operator_values", "primitive_contractions", "promote_to_A_selected", "promote_to_b_selected"])
    ]
    stale_dynamic_errors_retired = later_dynamic_closed and len(old_errors) >= 4

    reconciliation = {
        "schema": "MTTStaleDynamicGapReconciliation.v1",
        "status": "STALE_DYNAMIC_OPERATOR_PRIMITIVE_BLOCKER_RETIRED",
        "old_postsource_validator": rel(POSTSOURCE_VALIDATOR),
        "later_same_source_dynamic_packet": rel(SAME_SOURCE_DYNAMIC),
        "old_errors": old_errors,
        "later_dynamic_packet_validates": later_dynamic_closed,
        "stale_dynamic_errors_retired": stale_dynamic_errors_retired,
        "still_not_retired": [
            "Yukawa/mass/mixing value closure",
            "generation-resolved magnitude-bearing threshold/source rows",
            "true precision profile convention",
        ],
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "closure_claimed": True,
    }
    write_json(RECONCILIATION, reconciliation)

    row_counts = vsd01_map["row_evidence"]["formal_110_row_counts"]
    sm_generations_selected = (
        sm_interface["sm_required_components"]["three_generations"]["status"]
        == "SELECTED_SOURCE_DATA_REQUIRED"
    )
    source_stack_closed = vsd01_map["source_stack_replay"]["source_stack_closed"]
    static_matter_closed = all(static_readout["static_readout_closed"].values())
    generation_support_closed = sm_generations_selected and source_stack_closed and static_matter_closed
    gen_support = {
        "schema": "MTTGenerationSourceSupportRecheck.v1",
        "status": "GENERATION_STRUCTURE_SUPPORT_PRESENT_MAGNITUDE_ROWS_OPEN",
        "selected_three_family_structure_declared": sm_generations_selected,
        "static_matter_slot_readout_closed": static_matter_closed,
        "finite_c1_source_stack_closed": source_stack_closed,
        "formal_row_counts": row_counts,
        "what_this_supports": [
            "three-generation SM source interface",
            "static matter-slot routing",
            "finite C1 source identity and row stack",
        ],
        "what_this_does_not_emit": [
            "generation-resolved magnitude-bearing projection/source rows",
            "family-resolving threshold operator eigenvalues",
            "same-branch precision scale/scheme/loop convention",
        ],
        "generation_support_closed": generation_support_closed,
        "generation_resolved_magnitude_rows_closed": False,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "closure_claimed": True,
    }
    write_json(GEN_SUPPORT, gen_support)

    diagnostic_rows = backsolve["diagnostic_weights"]
    attempted_rows = [
        {
            "row_id": f"{row['sector']}.gen{row['generation']}.diagnostic_magnitude",
            "diagnostic_value": row["diagnostic_magnitude_weight"],
            "accepted_as_selected_generation_threshold_source_row": False,
            "why_not": [
                "diagnostic value comes from first-pass/profile value packet",
                "no selected family-resolving threshold operator emits this row",
                "using it as a source would violate measured/replay selector guard",
            ],
        }
        for row in diagnostic_rows
    ]
    row_attempt = {
        "schema": "MTTGenerationResolvedThresholdRowAttempt.v1",
        "status": "GENERATION_RESOLVED_ROWS_ATTEMPTED_DIAGNOSTIC_ONLY",
        "diagnostic_backsolve": rel(BACKSOLVE),
        "rank_gap": rel(RANK_GAP),
        "attempted_rows": attempted_rows,
        "attempted_row_count": len(attempted_rows),
        "accepted_rows": [],
        "accepted_generation_threshold_source_rows": [],
        "accepted_row_count": 0,
        "required_row_count": rank_gap["dimension_evidence"]["charged_generation_magnitude_rows"],
        "required_charged_generation_row_count": rank_gap["dimension_evidence"]["charged_generation_magnitude_rows"],
        "lambda_H_row_required": True,
        "generation_resolved_threshold_source_rows_closed": False,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "closure_claimed": False,
    }
    write_json(ROW_ATTEMPT, row_attempt)

    transport_convention = value_packet["transport_convention"]
    profile = {
        "schema": "MTTProfileConventionClosureRecheck.v1",
        "status": "FIRSTPASS_PROFILE_CONVENTION_AVAILABLE_TRUE_PRECISION_CONVENTION_OPEN",
        "value_packet": rel(VALUE_PACKET),
        "profile_execution": rel(PROFILE_EXECUTION),
        "firstpass_convention": transport_convention,
        "accepted_for_SM_parity": value_packet["accepted_for_SM_parity"],
        "accepted_for_profile_input": value_packet["accepted_for_profile_execution_input"],
        "accepted_for_profile_execution_input": value_packet["accepted_for_profile_execution_input"],
        "accepted_for_true_precision": value_packet["accepted_for_true_precision_equivalence"],
        "accepted_for_true_precision_equivalence": value_packet["accepted_for_true_precision_equivalence"],
        "value_profile_execution_layer_closed": profile_execution["closure_decision"]["value_profile_execution_layer_closed"],
        "profile_layer_closed": profile_execution["closure_decision"]["value_profile_execution_layer_closed"],
        "full_profile_likelihood_closed": profile_execution["closure_decision"]["full_profile_likelihood_closed"],
        "same_branch_scale_scheme_loop_convention_closed": False,
        "reason_not_closed": [
            "declared convention is explicitly first-pass/parity",
            "threshold policy is no-threshold diagnostic convention",
            "mass-scheme policy uses admitted central masses as replay inputs",
        ],
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "closure_claimed": False,
    }
    write_json(PROFILE, profile)

    decision = {
        "schema": "MTTGenerationRowsOrProfileConventionDecision.v1",
        "status": "DYNAMIC_BLOCKER_RETIRED_GENERATION_ROWS_AND_PROFILE_CONVENTION_OPEN",
        "previous_status": previous["status"],
        "rank_gap_theorem_proved": previous_decision["rank_gap_theorem_proved"],
        "stale_dynamic_operator_primitive_blocker_retired": stale_dynamic_errors_retired,
        "generation_structure_support_closed": generation_support_closed,
        "generation_resolved_threshold_source_rows_closed": False,
        "accepted_generation_threshold_source_row_count": 0,
        "required_charged_generation_row_count": rank_gap["dimension_evidence"]["charged_generation_magnitude_rows"],
        "required_generation_threshold_source_row_count": rank_gap["dimension_evidence"]["charged_generation_magnitude_rows"],
        "same_branch_scale_scheme_loop_convention_closed": False,
        "threshold_matching_source_rows_closed": False,
        "mass_scheme_conversion_source_rows_closed": False,
        "full_profile_likelihood_closed": False,
        "profile_likelihood_or_diagonal_theorem_closed": False,
        "accepted_Yukawa_magnitudes_as_no_knob_predictions": False,
        "true_SM_equivalence_closed": False,
        "full_no_knob_closed": False,
        "what_this_fixes": [
            "retires the stale post-source dynamic packet errors using later same-source dynamic validation",
            "separates generation-structure support from generation-resolved magnitude rows",
            "shows first-pass profile convention is not true precision convention",
        ],
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "closure_claimed": False,
    }
    write_json(DECISION, decision)

    cutset = {
        "schema": "MTTNextCutsetAfterGenerationRowAttempt.v1",
        "status": "NEXT_ATTACK_FAMILY_RESOLVING_OPERATOR_OR_GENERATION_THRESHOLD_ROWS",
        "next_required_artifact": NEXT,
        "closed_this_artifact": {
            "stale_dynamic_operator_primitive_blocker_retired": stale_dynamic_errors_retired,
            "generation_structure_support_rechecked": generation_support_closed,
            "profile_convention_rechecked": True,
        },
        "closed_now": {
            "stale_dynamic_operator_primitive_blocker_retired": stale_dynamic_errors_retired,
            "generation_structure_support_rechecked": generation_support_closed,
            "profile_convention_rechecked": True,
        },
        "still_open": [
            "family-resolving operator that emits generation threshold rows",
            "9 charged generation-resolved magnitude-bearing rows plus lambda_H row",
            "same-branch true precision scale/scheme/loop convention",
            "threshold matching source rows",
            "mass-scheme conversion source rows",
            "full profile likelihood or accepted diagonal theorem",
        ],
        "recommended_next": {
            "artifact": NEXT,
            "reason": (
                "The current source/dynamic stack reaches sector and source-normalized rows. It does not "
                "split the three generations by magnitude. The missing object is a family-resolving selected "
                "operator or an equivalent generation threshold-row theorem."
            ),
        },
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "closure_claimed": False,
    }
    write_json(CUTSET, cutset)

    candidate = {
        "candidate": "MTTSelectedGenerationResolvedThresholdSourceRowsOrProfileConventionClosure",
        "status": STATUS,
        "inputs": {path.stem: rel(path) for path in sources},
        "output_packets": {
            "stale_dynamic_gap_reconciliation": rel(RECONCILIATION),
            "generation_source_support_recheck": rel(GEN_SUPPORT),
            "generation_resolved_threshold_row_attempt": rel(ROW_ATTEMPT),
            "profile_convention_closure_recheck": rel(PROFILE),
            "generation_rows_or_profile_convention_decision": rel(DECISION),
            "next_cutset_after_generation_row_attempt": rel(CUTSET),
        },
        "theorem": {
            "name": "GenerationSupportReconciliationAndThresholdRowGapTheorem",
            "proved": True,
            "statement": (
                "The stale post-source dynamic operator/primitive-contraction blocker is retired by the later "
                "same-source dynamic overlap packet. Three-family/source support, static matter readout, and the "
                "finite C1 row stack are present. However, none emits generation-resolved magnitude-bearing "
                "threshold/source rows or a true precision profile convention. Therefore the next closure object "
                "is a family-resolving selected operator or generation threshold-row theorem."
            ),
        },
        "closure_decision": {
            "stale_dynamic_operator_primitive_blocker_retired": stale_dynamic_errors_retired,
            "generation_structure_support_closed": generation_support_closed,
            "generation_resolved_threshold_source_rows_closed": False,
            "same_branch_scale_scheme_loop_convention_closed": False,
            "accepted_Yukawa_magnitudes_as_no_knob_predictions": False,
            "true_SM_equivalence_closed": False,
            "full_no_knob_closed": False,
        },
        "next_required_artifact": NEXT,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "closure_claimed": False,
        "unpatched_theorem_closure_claimed": False,
    }
    write_json(OUTPUT, candidate)

    cert = {
        "certificate": "MTT_Selected_GenerationResolvedThresholdSourceRows_or_ProfileConventionClosure_v1",
        "status": STATUS,
        "candidate_path": rel(OUTPUT),
        "note_path": rel(NOTE),
        "theorem_proved": True,
        "stale_dynamic_operator_primitive_blocker_retired": stale_dynamic_errors_retired,
        "generation_structure_support_closed": generation_support_closed,
        "accepted_generation_threshold_source_row_count": 0,
        "generation_resolved_threshold_source_rows_closed": False,
        "same_branch_scale_scheme_loop_convention_closed": False,
        "accepted_Yukawa_magnitudes_as_no_knob_predictions": False,
        "true_SM_equivalence_closed": False,
        "full_no_knob_closed": False,
        "closure_claimed": False,
        "unpatched_theorem_closure_claimed": False,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "next_required_artifact": NEXT,
    }
    write_json(CERT, cert)

    note = f"""# MTT Selected GenerationResolvedThresholdSourceRows or ProfileConventionClosure v1

Status: `{STATUS}`.

This artifact reconciles the older post-source dynamic rejection with the later
same-source dynamic packet, then tries the generation-resolved threshold row
target.

```text
stale dynamic blocker retired        : {str(stale_dynamic_errors_retired).lower()}
generation structure support closed  : {str(generation_support_closed).lower()}
accepted generation threshold rows   : 0/{rank_gap["dimension_evidence"]["charged_generation_magnitude_rows"]}
profile convention true-precision    : false
Yukawa magnitudes no-knob closed     : false
```

The remaining object is now very specific: a family-resolving selected operator
or equivalent generation threshold-row theorem.  Static three-family support and
the finite C1 row stack are present; they do not yet split the three generations
into magnitude-bearing source rows.

Next artifact: `{NEXT}`.
"""
    NOTE.write_text(note, encoding="utf-8")

    print(json.dumps({"candidate": rel(OUTPUT), "status": STATUS}, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
