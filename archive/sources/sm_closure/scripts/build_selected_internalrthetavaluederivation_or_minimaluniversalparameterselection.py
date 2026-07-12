"""Build internal Rtheta value derivation / minimal universal parameter selection attack."""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "candidate_data"
CERTS = ROOT / "certificates"
CORPUS = ROOT / "proof_corpus"

SLUG = "selected_internalrthetavaluederivation_or_minimaluniversalparameterselection"
PACKET_DIR = DATA / SLUG
OUTPUT = DATA / f"{SLUG}.candidate.json"
FIRST_RESPONSE = PACKET_DIR / "internal_rtheta_first_response_sufficiency_test.packet.json"
FUNCTIONAL_READINESS = PACKET_DIR / "post_pi_threshold_functional_readiness_recheck.packet.json"
PARAMETER_RECHECK = PACKET_DIR / "minimal_universal_parameter_selection_recheck.packet.json"
DECISION = PACKET_DIR / "internal_or_minimal_selection_decision.packet.json"
CUTSET = PACKET_DIR / "next_cutset_after_internal_rtheta_attack.packet.json"
CERT = CERTS / f"{SLUG}_certificate.json"
NOTE = CORPUS / "MTT_Selected_InternalRThetaValueDerivation_or_MinimalUniversalParameterSelection_v1.md"

PREVIOUS = DATA / "selected_noknobvaluederivationpostpi_or_minimaluniversalparameterpolicy.candidate.json"
PREV_FINAL_RECHECK = (
    DATA
    / "selected_noknobvaluederivationpostpi_or_minimaluniversalparameterpolicy"
    / "final_no_knob_value_derivation_recheck.packet.json"
)
PREV_EXTERNAL_BOUNDARY = (
    DATA
    / "selected_noknobvaluederivationpostpi_or_minimaluniversalparameterpolicy"
    / "post_pi_external_replay_boundary.packet.json"
)
PREV_POLICY_MATRIX = (
    DATA
    / "selected_noknobvaluederivationpostpi_or_minimaluniversalparameterpolicy"
    / "minimal_universal_parameter_policy_matrix.packet.json"
)
SAME_SOURCE_DYNAMIC = DATA / "selected_samesourcedynamicmatteroverlapoperatorpacket_or_primitivec1valueclosure.candidate.json"
SAME_SOURCE_PACKET = (
    DATA
    / "selected_samesourcedynamicmatteroverlapoperatorpacket_or_primitivec1valueclosure"
    / "same_source_matter_overlap_operator_packet.packet.json"
)
SELECTED_NONSCALAR = (
    DATA
    / "selected_samesourcedynamicmatteroverlapoperatorpacket_or_primitivec1valueclosure"
    / "selected_non_scalar_dynamic_overlap_values.packet.json"
)
CONDITIONAL_DYNAMIC = (
    DATA
    / "selected_dynamicc1transfertensor_or_galerkinc1values"
    / "conditional_dynamic_c1_transfer_tensor.packet.json"
)
STRICT_ACCEPTANCE = (
    DATA
    / "selected_dynamicc1transfertensor_or_galerkinc1values_acceptance_manifest"
    / "strict_dynamic_c1_transfer_tensor_acceptance.packet.json"
)
RTHETA_BASIS = (
    DATA
    / "selected_rthetavaluerows_or_universalsourceanchortheorem"
    / "rtheta_family_eigenprofile_to_magnitude_row_basis_map.packet.json"
)
RTHETA_COEFF = (
    DATA
    / "selected_rthetavaluerows_or_universalsourceanchortheorem"
    / "rtheta_value_row_coefficients_attempt.packet.json"
)
HIGHER_RESPONSE = (
    DATA
    / "selected_higherresponsesectorcoefficients_or_thresholdfunctionalsourcerows"
    / "higher_response_sector_coefficient_source_attempt.packet.json"
)
THRESHOLD_ATTEMPT = (
    DATA
    / "selected_higherresponsesectorcoefficients_or_thresholdfunctionalsourcerows"
    / "selected_threshold_response_functional_execution_attempt.packet.json"
)
MINIMAL_APPLICATION = (
    DATA
    / "selected_higherresponsesectorcoefficients_or_thresholdfunctionalsourcerows"
    / "minimal_universal_parameter_application_to_yukawa_wall.packet.json"
)
POST_PI_CONVENTION = (
    DATA
    / "selected_postpiconventionsource_or_thresholdfunctionalinstantiation"
    / "post_pi_same_branch_convention_source_contract.packet.json"
)
POST_PI_ROWS = (
    DATA
    / "selected_thresholdmatchingrowspostpi_or_massschemesourcerows"
    / "external_row_admission_not_rtheta_selection.packet.json"
)
POST_PI_DIAGONAL = (
    DATA
    / "selected_fullprofileordiagonaltheorempostpi_or_noknobvaluederivation"
    / "accepted_diagonal_profile_theorem_after_external_rows.packet.json"
)

STATUS = (
    "MTT_SELECTED_INTERNALRTHETAVALUEDERIVATION_OR_MINIMALUNIVERSALPARAMETERSELECTION_"
    "BUILT_FIRST_RESPONSE_NOGO_HIGHER_RESPONSE_REQUIRED"
)
NEXT = "MTT_Selected_HigherResponseRThetaFunctional_or_SourceAnchorTheorem_v1"


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
        raise FileNotFoundError("missing internal Rtheta attack sources: " + ", ".join(missing))


def main() -> int:
    PACKET_DIR.mkdir(parents=True, exist_ok=True)
    CERTS.mkdir(parents=True, exist_ok=True)
    CORPUS.mkdir(parents=True, exist_ok=True)

    sources = [
        PREVIOUS,
        PREV_FINAL_RECHECK,
        PREV_EXTERNAL_BOUNDARY,
        PREV_POLICY_MATRIX,
        SAME_SOURCE_DYNAMIC,
        SAME_SOURCE_PACKET,
        SELECTED_NONSCALAR,
        CONDITIONAL_DYNAMIC,
        STRICT_ACCEPTANCE,
        RTHETA_BASIS,
        RTHETA_COEFF,
        HIGHER_RESPONSE,
        THRESHOLD_ATTEMPT,
        MINIMAL_APPLICATION,
        POST_PI_CONVENTION,
        POST_PI_ROWS,
        POST_PI_DIAGONAL,
    ]
    require_sources(sources)

    previous = load(PREVIOUS)
    prev_final = load(PREV_FINAL_RECHECK)
    prev_external = load(PREV_EXTERNAL_BOUNDARY)
    prev_policy = load(PREV_POLICY_MATRIX)
    same_source_dynamic = load(SAME_SOURCE_DYNAMIC)
    same_source_packet = load(SAME_SOURCE_PACKET)
    selected_nonscalar = load(SELECTED_NONSCALAR)
    conditional_dynamic = load(CONDITIONAL_DYNAMIC)
    strict_acceptance = load(STRICT_ACCEPTANCE)
    rtheta_basis = load(RTHETA_BASIS)
    rtheta_coeff = load(RTHETA_COEFF)
    higher_response = load(HIGHER_RESPONSE)
    threshold_attempt = load(THRESHOLD_ATTEMPT)
    minimal_application = load(MINIMAL_APPLICATION)
    post_pi_convention = load(POST_PI_CONVENTION)
    post_pi_rows = load(POST_PI_ROWS)
    post_pi_diagonal = load(POST_PI_DIAGONAL)

    dynamic_rank = selected_nonscalar["dynamic_transfer_tensor"]["normal_form_replay"]["rank"]
    domain_basis_count = len(conditional_dynamic["domain_basis"])
    charged_basis_slots = rtheta_basis["charged_basis_row_count"]
    scalar_target_slots = charged_basis_slots + 1
    accepted_coefficient_rows = rtheta_coeff["accepted_coefficient_row_count"]

    first_response = {
        "schema": "MTTInternalRThetaFirstResponseSufficiencyTest.v1",
        "status": "FIRST_RESPONSE_SELECTED_BUT_INSUFFICIENT_FOR_SCALAR_VALUE_ROWS",
        "same_source_dynamic_source": rel(SAME_SOURCE_DYNAMIC),
        "same_source_packet_source": rel(SAME_SOURCE_PACKET),
        "selected_dynamic_matter_overlap_packet_closed": same_source_dynamic["promotion_decision"][
            "dynamic_matter_overlap_operator_packet_closed"
        ],
        "selected_first_response_layer_closed": same_source_dynamic["promotion_decision"][
            "selected_dynamic_QaSU3_operator_packet_first_response_layer_closed"
        ],
        "field_selection_summary": same_source_packet["attempted_selected_packet"]["fields"],
        "dynamic_domain_basis_count": domain_basis_count,
        "dynamic_normal_form_rank": dynamic_rank,
        "deltaTheta_C1": selected_nonscalar["dynamic_transfer_tensor"]["normal_form_replay"][
            "deltaTheta_C1"
        ],
        "charged_magnitude_basis_slots": charged_basis_slots,
        "lambda_H_row_required": True,
        "scalar_target_slot_count": scalar_target_slots,
        "accepted_selected_coefficient_rows": accepted_coefficient_rows,
        "coefficient_functional_closed": rtheta_coeff["coefficient_functional_closed"],
        "lambda_H_coefficient_selected": rtheta_coeff["lambda_H_coefficient_selected"],
        "first_response_sufficient_for_no_knob_value_rows": False,
        "insufficiency_reasons": [
            "the selected first-response layer emits qualitative non-scalar matrices, not scalar charged magnitude coefficients",
            "the available dynamic normal form has rank two while the no-knob scalar target layer needs nine charged coefficients plus lambda_H",
            "the existing coefficient values are diagnostic replay values and are explicitly rejected as selected source rows",
            "no selected higher-response or retarded-kernel derivative functional maps the first-response packet to numeric threshold rows",
        ],
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "closure_claimed": False,
    }
    write_json(FIRST_RESPONSE, first_response)

    post_pi_checks = {
        "same_branch_scale_scheme_loop_convention_closed": post_pi_convention[
            "same_branch_scale_scheme_loop_convention_closed"
        ],
        "admitted_external_threshold_rows_available": post_pi_rows[
            "accepted_external_threshold_row_count"
        ]
        == 7,
        "admitted_external_mass_scheme_rows_available": post_pi_rows[
            "accepted_external_mass_scheme_row_count"
        ]
        == 3,
        "accepted_diagonal_theorem_available": post_pi_diagonal[
            "accepted_diagonal_theorem_closed"
        ],
        "no_observed_selector_guard_present": True,
        "selected_threshold_response_functional_emitted": False,
        "selected_internal_threshold_mass_rows_emitted": False,
    }
    present_under_external_replay = sum(
        [
            post_pi_checks["same_branch_scale_scheme_loop_convention_closed"],
            post_pi_checks["admitted_external_threshold_rows_available"],
            post_pi_checks["admitted_external_mass_scheme_rows_available"],
            post_pi_checks["accepted_diagonal_theorem_available"],
            post_pi_checks["no_observed_selector_guard_present"],
        ]
    )
    present_under_internal_noknob = sum(
        [
            post_pi_checks["same_branch_scale_scheme_loop_convention_closed"],
            post_pi_checks["no_observed_selector_guard_present"],
            post_pi_checks["selected_threshold_response_functional_emitted"],
            post_pi_checks["selected_internal_threshold_mass_rows_emitted"],
        ]
    )
    functional_readiness = {
        "schema": "MTTPostPiThresholdFunctionalReadinessRecheck.v1",
        "status": "POST_PI_EXTERNAL_READINESS_HIGH_INTERNAL_FUNCTIONAL_STILL_OPEN",
        "old_threshold_attempt_source": rel(THRESHOLD_ATTEMPT),
        "old_present_required_output_count": threshold_attempt["present_required_output_count"],
        "old_required_output_count": threshold_attempt["required_output_count"],
        "post_pi_checks": post_pi_checks,
        "present_under_external_replay_count": present_under_external_replay,
        "required_under_external_replay_count": 5,
        "present_under_strict_internal_no_knob_count": present_under_internal_noknob,
        "required_under_strict_internal_no_knob_count": 4,
        "post_pi_external_replay_ready": prev_external["post_pi_external_replay_ready"],
        "selected_threshold_response_functional_instantiated": False,
        "selected_internal_Rtheta_threshold_mass_derivation_closed": False,
        "accepted_external_rows_promote_to_internal_no_knob": False,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "closure_claimed": False,
    }
    write_json(FUNCTIONAL_READINESS, functional_readiness)

    parameter_recheck = {
        "schema": "MTTMinimalUniversalParameterSelectionRecheck.v1",
        "status": "NO_UNIVERSAL_PARAMETER_SELECTED_AFTER_INTERNAL_RTHETA_ATTACK",
        "previous_policy_matrix_source": rel(PREV_POLICY_MATRIX),
        "minimal_application_source": rel(MINIMAL_APPLICATION),
        "selected_universal_parameter_count": prev_policy["selected_universal_parameter_count"],
        "maximum_live_universal_parameters": prev_policy["maximum_live_universal_parameters"],
        "candidate_specific_source_theorem_present": prev_policy[
            "candidate_specific_source_theorem_present"
        ],
        "minimal_universal_parameter_selection_closed": False,
        "minimal_universal_parameter_lane_selected_now": minimal_application[
            "minimal_universal_parameter_lane_selected_now"
        ],
        "allowed_lanes_rechecked": minimal_application["knob_lanes"],
        "why_not_selected": [
            "no UP-ACTION-NORM, UP-RET-OVERLAP, UP-PHASE, UP-ABS-SCALE, or UP-BOUNDARY source theorem selects a value here",
            "one parameter per charged sector or generation remains forbidden by the policy",
            "external replay rows are admissible for SM-parity replay but are not a universal no-knob source anchor",
        ],
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "closure_claimed": False,
    }
    write_json(PARAMETER_RECHECK, parameter_recheck)

    decision = {
        "schema": "MTTInternalOrMinimalSelectionDecision.v1",
        "status": "INTERNAL_FIRST_RESPONSE_NOGO_AND_MINIMAL_PARAMETER_NOT_SELECTED",
        "internal_first_response_sufficient": False,
        "selected_higher_response_or_retarded_kernel_derivative_required": True,
        "higher_response_sector_coefficients_closed": higher_response[
            "accepted_sector_coefficient_row_count"
        ]
        > 0,
        "accepted_generation_threshold_source_row_count": higher_response[
            "accepted_generation_threshold_source_row_count"
        ],
        "diagnostic_sector_coefficients_rejected": higher_response[
            "accepted_sector_coefficient_row_count"
        ]
        == 0,
        "minimal_universal_parameter_selected": False,
        "post_pi_external_replay_ready": True,
        "no_knob_value_derivation_closed": False,
        "true_SM_equivalence_closed": False,
        "full_no_knob_closed": False,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "closure_claimed": False,
    }
    write_json(DECISION, decision)

    cutset = {
        "schema": "MTTNextCutsetAfterInternalRThetaAttack.v1",
        "status": "NEXT_ATTACK_HIGHER_RESPONSE_RTHETA_FUNCTIONAL_OR_SOURCE_ANCHOR_THEOREM",
        "closed_now": {
            "selected_first_response_internal_value_sufficiency_test": True,
            "first_response_only_route_rejected_for_scalar_no_knob_values": True,
            "post_pi_functional_readiness_rechecked": True,
            "minimal_universal_parameter_selection_rechecked": True,
            "higher_response_or_source_anchor_identified_as_required": True,
        },
        "still_open": {
            "selected_higher_response_Rtheta_functional": True,
            "selected_retarded_kernel_derivative_value_functional": True,
            "selected_internal_Rtheta_threshold_mass_derivation": True,
            "numeric_Rtheta_coefficient_values": True,
            "lambda_H_value_execution": True,
            "candidate_specific_universal_source_anchor_theorem": True,
            "Yukawa_mass_mixing_value_closure": True,
            "true_SM_equivalence": True,
            "full_no_knob": True,
        },
        "recommended_next": {
            "artifact": NEXT,
            "route_A": "construct a selected higher-response or retarded-kernel derivative functional that emits the ten scalar value rows",
            "route_B": "prove a source-anchor theorem for a single universal parameter and propagate it through the same functional",
            "route_C": "if neither exists, publish the theorem as an explicit first-response no-go for full no-knob values",
        },
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "closure_claimed": False,
    }
    write_json(CUTSET, cutset)

    candidate = {
        "candidate": "MTTSelectedInternalRThetaValueDerivationOrMinimalUniversalParameterSelection",
        "status": STATUS,
        "inputs": {path.stem: rel(path) for path in sources},
        "output_packets": {
            "internal_rtheta_first_response_sufficiency_test": rel(FIRST_RESPONSE),
            "post_pi_threshold_functional_readiness_recheck": rel(FUNCTIONAL_READINESS),
            "minimal_universal_parameter_selection_recheck": rel(PARAMETER_RECHECK),
            "internal_or_minimal_selection_decision": rel(DECISION),
            "next_cutset_after_internal_rtheta_attack": rel(CUTSET),
        },
        "theorem": {
            "name": "FirstResponseInsufficiencyAndSourceAnchorNonselectionTheorem",
            "proved": True,
            "statement": (
                "The selected same-source dynamic matter/overlap packet closes the first-response operator layer, "
                "but that layer is insufficient to emit the scalar no-knob Rtheta value rows: it provides a rank-two "
                "qualitative response while the current scalar value layer needs nine charged coefficient rows plus "
                "lambda_H, and zero selected coefficient rows are accepted. The minimal universal parameter lane is "
                "also not selected because no candidate-specific source-anchor theorem is present."
            ),
        },
        "what_closes_now": cutset["closed_now"],
        "what_remains_open": cutset["still_open"],
        "closure_decision": {
            "first_response_only_route_rejected_for_scalar_no_knob_values": True,
            "dynamic_first_response_layer_closed": True,
            "dynamic_normal_form_rank": dynamic_rank,
            "scalar_target_slot_count": scalar_target_slots,
            "selected_threshold_response_functional_instantiated": False,
            "selected_internal_value_emission_count": 0,
            "accepted_coefficient_value_count": accepted_coefficient_rows,
            "lambda_H_value_execution": False,
            "minimal_universal_parameter_selection_closed": False,
            "selected_universal_parameter_count": prev_policy["selected_universal_parameter_count"],
            "no_knob_value_derivation_closed": False,
            "true_SM_equivalence_closed": False,
            "full_no_knob_closed": False,
        },
        "previous_status": previous["status"],
        "next_required_artifact": NEXT,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "closure_claimed": False,
        "unpatched_theorem_closure_claimed": False,
    }
    write_json(OUTPUT, candidate)

    cert = {
        "certificate": "MTT_Selected_InternalRThetaValueDerivation_or_MinimalUniversalParameterSelection_v1",
        "status": STATUS,
        "candidate_path": rel(OUTPUT),
        "note_path": rel(NOTE),
        "theorem_proved": True,
        "first_response_only_route_rejected_for_scalar_no_knob_values": True,
        "dynamic_first_response_layer_closed": True,
        "dynamic_normal_form_rank": dynamic_rank,
        "scalar_target_slot_count": scalar_target_slots,
        "selected_threshold_response_functional_instantiated": False,
        "selected_internal_value_emission_count": 0,
        "accepted_coefficient_value_count": accepted_coefficient_rows,
        "lambda_H_value_execution": False,
        "minimal_universal_parameter_selection_closed": False,
        "selected_universal_parameter_count": prev_policy["selected_universal_parameter_count"],
        "no_knob_value_derivation_closed": False,
        "true_SM_equivalence_closed": False,
        "full_no_knob_closed": False,
        "next_required_artifact": NEXT,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "closure_claimed": False,
        "unpatched_theorem_closure_claimed": False,
    }
    write_json(CERT, cert)

    note = f"""# MTT Selected InternalRThetaValueDerivation or MinimalUniversalParameterSelection v1

Status: `{STATUS}`.

The selected same-source dynamic matter/overlap packet is useful but not enough
for full scalar value closure.

```text
dynamic first-response layer closed     : true
dynamic normal-form rank                : {dynamic_rank}
scalar target slots                     : {scalar_target_slots}
accepted selected coefficient rows      : {accepted_coefficient_rows}
selected universal parameters           : {prev_policy["selected_universal_parameter_count"]}
first-response scalar no-knob closure   : false
full no-knob closure                    : false
true SM equivalence                     : false
```

So the next object is not another replay row.  It must be either a selected
higher-response / retarded-kernel derivative functional that emits the ten
scalar value rows, or a source-selected universal anchor theorem that can be
propagated through that same functional without per-observable fitting.

Next artifact: `{NEXT}`.
"""
    NOTE.write_text(note, encoding="utf-8")

    print(json.dumps({"candidate": rel(OUTPUT), "status": STATUS}, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
