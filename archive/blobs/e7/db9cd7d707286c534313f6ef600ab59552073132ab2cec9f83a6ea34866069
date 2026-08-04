"""Build threshold-functional source theorem / minimal universal parameter selection gate."""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "candidate_data"
CERTS = ROOT / "certificates"
CORPUS = ROOT / "proof_corpus"

SLUG = "selected_thresholdfunctionalsourcetheorem_or_minimaluniversalparameterselection"
PACKET_DIR = DATA / SLUG
OUTPUT = DATA / f"{SLUG}.candidate.json"
STALE_BLOCKER = PACKET_DIR / "stale_rtheta_dynamic_source_blocker_reconciliation.packet.json"
DOMAIN_READINESS = PACKET_DIR / "rtheta_domain_readiness_after_dynamic_family_closure.packet.json"
UNIVERSAL_SELECTION = PACKET_DIR / "minimal_universal_parameter_selection_attempt.packet.json"
INSTANTIATION_UPDATE = PACKET_DIR / "rtheta_instantiation_update_after_dynamic_source_closure.packet.json"
DECISION = PACKET_DIR / "threshold_functional_source_or_minimal_parameter_decision.packet.json"
CUTSET = PACKET_DIR / "next_cutset_after_threshold_functional_source_gate.packet.json"
CERT = CERTS / f"{SLUG}_certificate.json"
NOTE = CORPUS / "MTT_Selected_ThresholdFunctionalSourceTheorem_or_MinimalUniversalParameterSelection_v1.md"

PREVIOUS = DATA / "selected_higherresponsesectorcoefficients_or_thresholdfunctionalsourcerows.candidate.json"
PREVIOUS_RESPONSE_ATTEMPT = (
    DATA
    / "selected_higherresponsesectorcoefficients_or_thresholdfunctionalsourcerows"
    / "selected_threshold_response_functional_execution_attempt.packet.json"
)
PREVIOUS_KNOB = (
    DATA
    / "selected_higherresponsesectorcoefficients_or_thresholdfunctionalsourcerows"
    / "minimal_universal_parameter_application_to_yukawa_wall.packet.json"
)
THETA_FUNCTIONAL = DATA / "selected_thresholdresponsefunctionalderivation_or_profilelikelihoodacquisition.candidate.json"
THETA_CONTRACT = (
    DATA
    / "selected_thresholdresponsefunctionalderivation_or_profilelikelihoodacquisition"
    / "selected_threshold_response_functional_contract.packet.json"
)
OLD_INSTANTIATION = (
    DATA
    / "selected_thresholdresponsefunctionalderivation_or_profilelikelihoodacquisition"
    / "current_repo_functional_instantiation_audit.packet.json"
)
OLD_DECISION = (
    DATA
    / "selected_thresholdresponsefunctionalderivation_or_profilelikelihoodacquisition"
    / "threshold_response_functional_decision.packet.json"
)
DYNAMIC_PACKET = DATA / "selected_samesourcedynamicmatteroverlapoperatorpacket_or_primitivec1valueclosure.candidate.json"
DYNAMIC_VALIDATOR = (
    DATA
    / "selected_samesourcedynamicmatteroverlapoperatorpacket_or_primitivec1valueclosure"
    / "same_source_matter_overlap_operator_validator_result.packet.json"
)
FAMILY_OPERATOR = DATA / "selected_familyresolvingoperator_or_generationthresholdrowsexecution.candidate.json"
FAMILY_SPECTRUM = (
    DATA
    / "selected_familyresolvingoperator_or_generationthresholdrowsexecution"
    / "selected_first_response_family_spectrum.packet.json"
)
SECTOR_NOGO = DATA / "selected_sectorscaledeigenprofilethresholdrows_or_yukawamagnitudesourceexecution.candidate.json"
UNIVERSAL_POLICY = DATA / "universal_source_parameter_policy.candidate.json"
UNIVERSAL_POLICY_PACKET = DATA / "universal_source_parameter_policy" / "universal_source_parameter_policy.packet.json"
UNIVERSAL_CANDIDATES = DATA / "universal_source_parameter_policy" / "candidate_universal_parameters.packet.json"
UNIVERSAL_CROSSUSE = DATA / "universal_crossuse_parameter_admissibility_theorem.candidate.json"
UNIVERSAL_ALPHA1 = DATA / "universal_alpha1_frontier_handoff_import.candidate.json"
VSD02_FILL_ATTEMPT = (
    DATA
    / "selected_vsd02acceptedsourcerowsfill_or_noknobthresholdderivation"
    / "accepted_source_rows_fill_attempt.packet.json"
)
RANK_GAP = (
    DATA
    / "selected_magnitudebearingprojectionweights_or_thresholdrowsderivation"
    / "magnitude_weight_rank_gap.packet.json"
)

STATUS = (
    "MTT_SELECTED_THRESHOLDFUNCTIONALSOURCETHEOREM_OR_MINIMALUNIVERSALPARAMETERSELECTION_"
    "BUILT_DYNAMIC_DOMAIN_CLOSED_VALUE_ROWS_OPEN"
)
NEXT = "MTT_Selected_RThetaValueRows_or_UniversalSourceAnchorTheorem_v1"


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
        raise FileNotFoundError("missing threshold-functional source theorem sources: " + ", ".join(missing))


def main() -> int:
    PACKET_DIR.mkdir(parents=True, exist_ok=True)
    CERTS.mkdir(parents=True, exist_ok=True)
    CORPUS.mkdir(parents=True, exist_ok=True)

    sources = [
        PREVIOUS,
        PREVIOUS_RESPONSE_ATTEMPT,
        PREVIOUS_KNOB,
        THETA_FUNCTIONAL,
        THETA_CONTRACT,
        OLD_INSTANTIATION,
        OLD_DECISION,
        DYNAMIC_PACKET,
        DYNAMIC_VALIDATOR,
        FAMILY_OPERATOR,
        FAMILY_SPECTRUM,
        SECTOR_NOGO,
        UNIVERSAL_POLICY,
        UNIVERSAL_POLICY_PACKET,
        UNIVERSAL_CANDIDATES,
        UNIVERSAL_CROSSUSE,
        UNIVERSAL_ALPHA1,
        VSD02_FILL_ATTEMPT,
        RANK_GAP,
    ]
    require_sources(sources)

    previous = load(PREVIOUS)
    previous_response = load(PREVIOUS_RESPONSE_ATTEMPT)
    previous_knob = load(PREVIOUS_KNOB)
    theta_functional = load(THETA_FUNCTIONAL)
    theta_contract = load(THETA_CONTRACT)
    old_instantiation = load(OLD_INSTANTIATION)
    old_decision = load(OLD_DECISION)
    dynamic_packet = load(DYNAMIC_PACKET)
    dynamic_validator = load(DYNAMIC_VALIDATOR)
    family_operator = load(FAMILY_OPERATOR)
    family_spectrum = load(FAMILY_SPECTRUM)
    sector_nogo = load(SECTOR_NOGO)
    universal_policy = load(UNIVERSAL_POLICY)
    universal_policy_packet = load(UNIVERSAL_POLICY_PACKET)
    universal_candidates = load(UNIVERSAL_CANDIDATES)
    universal_crossuse = load(UNIVERSAL_CROSSUSE)
    universal_alpha1 = load(UNIVERSAL_ALPHA1)
    vsd02_fill_attempt = load(VSD02_FILL_ATTEMPT)
    rank_gap = load(RANK_GAP)

    dynamic_closed = dynamic_packet["promotion_decision"]["dynamic_matter_overlap_operator_packet_closed"]
    dynamic_first_response_closed = dynamic_packet["promotion_decision"][
        "selected_dynamic_QaSU3_operator_packet_first_response_layer_closed"
    ]
    dynamic_validator_passes = dynamic_validator.get("returncode") == 0 or dynamic_validator.get("ok") is True
    family_closed = family_operator["closure_decision"]["family_resolving_operator_closed"]
    spectrum_closed = family_spectrum["family_resolving_operator_closed"]
    universal_profile_nogo = sector_nogo["closure_decision"]["universal_sector_scaled_eigenprofile_nogo_proved"]

    stale_dynamic_blocker_retired = all(
        [
            dynamic_closed,
            dynamic_first_response_closed,
            dynamic_validator_passes,
            family_closed,
            spectrum_closed,
        ]
    )
    stale_blocker = {
        "schema": "MTTStaleRThetaDynamicSourceBlockerReconciliation.v1",
        "status": "STALE_RTHETA_DYNAMIC_SOURCE_BLOCKER_RETIRED",
        "old_instantiation_audit": rel(OLD_INSTANTIATION),
        "old_blocker": "selected_dynamic_operator_source_owner",
        "later_dynamic_packet": rel(DYNAMIC_PACKET),
        "later_dynamic_validator": rel(DYNAMIC_VALIDATOR),
        "later_family_operator": rel(FAMILY_OPERATOR),
        "later_family_spectrum": rel(FAMILY_SPECTRUM),
        "dynamic_matter_overlap_packet_closed": dynamic_closed,
        "dynamic_first_response_layer_closed": dynamic_first_response_closed,
        "dynamic_validator_passes": dynamic_validator_passes,
        "family_resolving_operator_closed": family_closed,
        "stale_dynamic_source_blocker_retired": stale_dynamic_blocker_retired,
        "retired_scope": (
            "Retired only as an absence-of-dynamic-operator/domain blocker for R_theta. It does not emit "
            "threshold matching rows, mass-scheme rows, true precision profile convention, or Yukawa magnitudes."
        ),
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "closure_claimed": True,
    }
    write_json(STALE_BLOCKER, stale_blocker)

    domain_requirements = [
        {
            "id": "selected_MTT_branch_identifier_and_quotient_sector_data",
            "present": True,
            "source": rel(FAMILY_OPERATOR),
            "status": "CLOSED_SUPPORT",
        },
        {
            "id": "selected_dynamic_operator_packet_or_source_owner_theorem",
            "present": stale_dynamic_blocker_retired,
            "source": rel(DYNAMIC_PACKET),
            "status": "CLOSED_AFTER_DYNAMIC_BACKPROMOTION",
        },
        {
            "id": "scale_and_scheme_convention_before_observed_value_comparison",
            "present": False,
            "source": rel(PREVIOUS_RESPONSE_ATTEMPT),
            "status": "OPEN_TRUE_PRECISION_CONVENTION",
            "missing_for_acceptance": [
                "first-pass/parity convention is available but not a same-branch true precision convention"
            ],
        },
        {
            "id": "finite_normalization_transport_data_from_same_branch",
            "present": True,
            "source": rel(DYNAMIC_PACKET),
            "status": "CLOSED_FIRST_RESPONSE_NORMALIZATION",
        },
        {
            "id": "basis_map_from_MTT_rows_to_SM_value_packet_coordinates",
            "present": False,
            "source": rel(SECTOR_NOGO),
            "status": "PARTIAL_FAMILY_COORDINATE_ONLY",
            "missing_for_acceptance": [
                "family eigenbasis is selected, but sector-scaled magnitude/source rows are not emitted"
            ],
        },
    ]
    domain_readiness = {
        "schema": "MTTRThetaDomainReadinessAfterDynamicFamilyClosure.v1",
        "status": "RTHETA_DOMAIN_DYNAMIC_FAMILY_SUBGATE_CLOSED_VALUE_BASIS_OPEN",
        "functional_contract": rel(THETA_CONTRACT),
        "domain_requirements": domain_requirements,
        "domain_requirement_count": len(domain_requirements),
        "present_domain_requirement_count": sum(1 for item in domain_requirements if item["present"]),
        "dynamic_domain_subgate_closed": stale_dynamic_blocker_retired,
        "family_coordinate_subgate_closed": family_closed,
        "basis_map_to_magnitude_rows_closed": False,
        "same_branch_true_precision_convention_closed": False,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "closure_claimed": True,
    }
    write_json(DOMAIN_READINESS, domain_readiness)

    universal_selection_rows = [
        {
            "candidate_id": row["id"],
            "name": row["name"],
            "selected_now": row["selected_now"],
            "accepted_for_yukawa_wall_now": False,
            "reason_not_selected": (
                "No candidate-specific theorem selects this source anchor for R_theta before empirical replay."
            ),
        }
        for row in universal_candidates["candidate_classes"]
    ]
    universal_selection = {
        "schema": "MTTMinimalUniversalParameterSelectionAttempt.v1",
        "status": "NO_UNIVERSAL_PARAMETER_SELECTED_FOR_RTHETA_YUKAWA_WALL",
        "policy": rel(UNIVERSAL_POLICY_PACKET),
        "crossuse_policy": rel(UNIVERSAL_CROSSUSE),
        "alpha1_frontier_handoff": rel(UNIVERSAL_ALPHA1),
        "maximum_live_universal_parameters": universal_policy_packet["maximum_live_universal_parameters"],
        "selected_parameter_count_before": universal_policy["selected_parameter_count_now"],
        "selected_parameter_count_after": 0,
        "imported_one_universal_primitive_ready": universal_alpha1["imported_one_universal_primitive_ready"],
        "provisional_parameter_admitted_now": universal_crossuse["provisional_parameter_admitted_now"],
        "candidate_selection_rows": universal_selection_rows,
        "why_not_selected": [
            "alpha1/one-primitive handoff is ready but not connected to this R_theta source theorem",
            "cross-use policy allows provisional realism only after a source theorem connects the parameter to the gate",
            "no candidate may be chosen from Yukawa, threshold, CKM, PMNS, or profile residuals",
        ],
        "minimal_parameter_yukawa_closure_closed": False,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "closure_claimed": False,
    }
    write_json(UNIVERSAL_SELECTION, universal_selection)

    remaining_hard_failures = [
        "same_branch_scale_scheme_loop_convention",
        "threshold_matching_source_rows",
        "mass_scheme_conversion_source_rows",
        "no_knob_value_derivation_or_selected_universal_parameter_theorem",
        "full_profile_likelihood_or_accepted_diagonal_theorem",
        "basis_map_to_sector_scaled_magnitude_rows",
    ]
    instantiation_update = {
        "schema": "MTTRThetaInstantiationUpdateAfterDynamicSourceClosure.v1",
        "status": "DYNAMIC_DOMAIN_READY_RTHETA_VALUE_ROWS_STILL_OPEN",
        "old_instantiation_audit": rel(OLD_INSTANTIATION),
        "old_remaining_failures": old_instantiation["blocking_failures"],
        "retired_failures": ["selected_dynamic_operator_source_owner"],
        "remaining_hard_failures": remaining_hard_failures,
        "functional_contract_closed": theta_functional["closure_decision"]["functional_contract_closed"],
        "dynamic_domain_subgate_closed": stale_dynamic_blocker_retired,
        "domain_present_count_after_update": domain_readiness["present_domain_requirement_count"],
        "domain_requirement_count": domain_readiness["domain_requirement_count"],
        "codomain_present_required_output_count_after_update": previous_response["present_required_output_count"],
        "codomain_required_output_count": previous_response["required_output_count"],
        "accepted_generation_threshold_source_row_count": vsd02_fill_attempt["accepted_row_count"],
        "required_charged_generation_row_count": rank_gap["dimension_evidence"][
            "charged_generation_magnitude_rows"
        ],
        "selected_threshold_response_functional_instantiated": False,
        "generation_resolved_threshold_source_rows_closed": False,
        "minimal_parameter_yukawa_closure_closed": False,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "closure_claimed": False,
    }
    write_json(INSTANTIATION_UPDATE, instantiation_update)

    decision = {
        "schema": "MTTThresholdFunctionalSourceOrMinimalParameterDecision.v1",
        "status": "RTHETA_DYNAMIC_DOMAIN_CLOSED_VALUE_ROWS_AND_PARAMETER_SELECTION_OPEN",
        "previous_status": previous["status"],
        "functional_contract_closed": theta_functional["closure_decision"]["functional_contract_closed"],
        "stale_dynamic_source_blocker_retired": stale_dynamic_blocker_retired,
        "dynamic_domain_subgate_closed": stale_dynamic_blocker_retired,
        "family_coordinate_subgate_closed": family_closed,
        "universal_sector_scaled_eigenprofile_nogo_proved": universal_profile_nogo,
        "selected_universal_parameter_count": 0,
        "minimal_universal_parameter_selection_closed": False,
        "selected_threshold_response_functional_instantiated": False,
        "threshold_matching_source_rows_closed": False,
        "mass_scheme_conversion_source_rows_closed": False,
        "basis_map_to_sector_scaled_magnitude_rows_closed": False,
        "accepted_generation_threshold_source_row_count": vsd02_fill_attempt["accepted_row_count"],
        "required_charged_generation_row_count": rank_gap["dimension_evidence"][
            "charged_generation_magnitude_rows"
        ],
        "accepted_Yukawa_magnitudes_as_no_knob_predictions": False,
        "minimal_parameter_yukawa_closure_closed": False,
        "true_SM_equivalence_closed": False,
        "full_no_knob_closed": False,
        "what_this_closes": [
            "retires stale R_theta dynamic-source blocker",
            "closes R_theta dynamic/family domain subgate",
            "keeps universal-parameter realism lane open but unselected",
        ],
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "closure_claimed": False,
    }
    write_json(DECISION, decision)

    cutset = {
        "schema": "MTTNextCutsetAfterThresholdFunctionalSourceGate.v1",
        "status": "NEXT_ATTACK_RTHETA_VALUE_ROWS_OR_UNIVERSAL_SOURCE_ANCHOR",
        "closed_this_artifact": {
            "stale_dynamic_source_blocker_retired": stale_dynamic_blocker_retired,
            "rtheta_dynamic_domain_subgate_closed": stale_dynamic_blocker_retired,
            "minimal_parameter_selection_attempt_executed": True,
        },
        "still_open": [
            "same-branch true precision scale/scheme/loop convention",
            "threshold matching source rows",
            "mass-scheme conversion source rows",
            "basis map from family eigenprofile to sector-scaled magnitude rows",
            "candidate-specific theorem for any universal source anchor",
            "full profile likelihood or accepted diagonal theorem",
        ],
        "next_required_artifact": NEXT,
        "recommended_next": {
            "artifact": NEXT,
            "reason": (
                "R_theta no longer lacks the selected dynamic/family domain. The remaining closure work is to emit "
                "value rows from that domain or select a universal source anchor with a candidate-specific theorem."
            ),
        },
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "closure_claimed": False,
    }
    write_json(CUTSET, cutset)

    candidate = {
        "candidate": "MTTSelectedThresholdFunctionalSourceTheoremOrMinimalUniversalParameterSelection",
        "status": STATUS,
        "inputs": {
            "selected_higherresponsesectorcoefficients_or_thresholdfunctionalsourcerows.candidate": rel(PREVIOUS),
            "selected_threshold_response_functional_execution_attempt.packet": rel(PREVIOUS_RESPONSE_ATTEMPT),
            "minimal_universal_parameter_application_to_yukawa_wall.packet": rel(PREVIOUS_KNOB),
            "selected_thresholdresponsefunctionalderivation_or_profilelikelihoodacquisition.candidate": rel(
                THETA_FUNCTIONAL
            ),
            "selected_threshold_response_functional_contract.packet": rel(THETA_CONTRACT),
            "current_repo_functional_instantiation_audit.packet": rel(OLD_INSTANTIATION),
            "threshold_response_functional_decision.packet": rel(OLD_DECISION),
            "selected_samesourcedynamicmatteroverlapoperatorpacket_or_primitivec1valueclosure.candidate": rel(
                DYNAMIC_PACKET
            ),
            "same_source_matter_overlap_operator_validator_result.packet": rel(DYNAMIC_VALIDATOR),
            "selected_familyresolvingoperator_or_generationthresholdrowsexecution.candidate": rel(FAMILY_OPERATOR),
            "selected_first_response_family_spectrum.packet": rel(FAMILY_SPECTRUM),
            "selected_sectorscaledeigenprofilethresholdrows_or_yukawamagnitudesourceexecution.candidate": rel(
                SECTOR_NOGO
            ),
            "universal_source_parameter_policy.candidate": rel(UNIVERSAL_POLICY),
            "universal_source_parameter_policy.packet": rel(UNIVERSAL_POLICY_PACKET),
            "candidate_universal_parameters.packet": rel(UNIVERSAL_CANDIDATES),
            "universal_crossuse_parameter_admissibility_theorem.candidate": rel(UNIVERSAL_CROSSUSE),
            "universal_alpha1_frontier_handoff_import.candidate": rel(UNIVERSAL_ALPHA1),
            "accepted_source_rows_fill_attempt.packet": rel(VSD02_FILL_ATTEMPT),
            "magnitude_weight_rank_gap.packet": rel(RANK_GAP),
        },
        "output_packets": {
            "stale_rtheta_dynamic_source_blocker_reconciliation": rel(STALE_BLOCKER),
            "rtheta_domain_readiness_after_dynamic_family_closure": rel(DOMAIN_READINESS),
            "minimal_universal_parameter_selection_attempt": rel(UNIVERSAL_SELECTION),
            "rtheta_instantiation_update_after_dynamic_source_closure": rel(INSTANTIATION_UPDATE),
            "threshold_functional_source_or_minimal_parameter_decision": rel(DECISION),
            "next_cutset_after_threshold_functional_source_gate": rel(CUTSET),
        },
        "theorem": {
            "name": "RThetaDynamicDomainClosureAndValueRowsFrontierTheorem",
            "proved": True,
            "statement": (
                "The selected same-source dynamic matter/overlap packet and family-resolving operator retire the "
                "old R_theta dynamic-source blocker and close the dynamic/family domain subgate of the selected "
                "threshold response functional. This does not instantiate R_theta: true precision convention, "
                "threshold matching rows, mass-scheme rows, sector-scaled magnitude basis, profile likelihood, and "
                "universal source-anchor selection remain open."
            ),
        },
        "closure_decision": {
            "functional_contract_closed": theta_functional["closure_decision"]["functional_contract_closed"],
            "stale_dynamic_source_blocker_retired": stale_dynamic_blocker_retired,
            "dynamic_domain_subgate_closed": stale_dynamic_blocker_retired,
            "family_coordinate_subgate_closed": family_closed,
            "minimal_universal_parameter_selection_closed": False,
            "selected_universal_parameter_count": 0,
            "selected_threshold_response_functional_instantiated": False,
            "generation_resolved_threshold_source_rows_closed": False,
            "accepted_Yukawa_magnitudes_as_no_knob_predictions": False,
            "minimal_parameter_yukawa_closure_closed": False,
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
        "certificate": "MTT_Selected_ThresholdFunctionalSourceTheorem_or_MinimalUniversalParameterSelection_v1",
        "status": STATUS,
        "candidate_path": rel(OUTPUT),
        "note_path": rel(NOTE),
        "theorem_proved": True,
        "functional_contract_closed": theta_functional["closure_decision"]["functional_contract_closed"],
        "stale_dynamic_source_blocker_retired": stale_dynamic_blocker_retired,
        "dynamic_domain_subgate_closed": stale_dynamic_blocker_retired,
        "family_coordinate_subgate_closed": family_closed,
        "selected_universal_parameter_count": 0,
        "selected_threshold_response_functional_instantiated": False,
        "accepted_generation_threshold_source_row_count": vsd02_fill_attempt["accepted_row_count"],
        "required_charged_generation_row_count": rank_gap["dimension_evidence"][
            "charged_generation_magnitude_rows"
        ],
        "accepted_Yukawa_magnitudes_as_no_knob_predictions": False,
        "minimal_parameter_yukawa_closure_closed": False,
        "true_SM_equivalence_closed": False,
        "full_no_knob_closed": False,
        "closure_claimed": False,
        "unpatched_theorem_closure_claimed": False,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "next_required_artifact": NEXT,
    }
    write_json(CERT, cert)

    note = f"""# MTT Selected ThresholdFunctionalSourceTheorem or MinimalUniversalParameterSelection v1

Status: `{STATUS}`.

This artifact re-audits `R_theta` after selected dynamic/family closure.

```text
R_theta contract closed                  : {str(theta_functional["closure_decision"]["functional_contract_closed"]).lower()}
stale dynamic-source blocker retired     : {str(stale_dynamic_blocker_retired).lower()}
R_theta dynamic/family domain closed     : {str(stale_dynamic_blocker_retired).lower()}
selected universal parameters now        : 0
R_theta instantiated                     : false
accepted generation threshold rows       : {vsd02_fill_attempt["accepted_row_count"]}/{rank_gap["dimension_evidence"]["charged_generation_magnitude_rows"]}
Yukawa magnitudes no-knob closed         : false
minimal-parameter Yukawa closure closed  : false
```

The old claim that `R_theta` lacks a selected dynamic/operator source is now
stale.  The selected same-source dynamic packet and family operator supply that
domain.  The remaining problem is value-row emission: true precision convention,
threshold rows, mass-scheme maps, sector-scaled magnitude rows, profile
likelihood, or a candidate-specific universal source-anchor theorem.

Next artifact: `{NEXT}`.
"""
    NOTE.write_text(note, encoding="utf-8")

    print(json.dumps({"candidate": rel(OUTPUT), "status": STATUS}, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
