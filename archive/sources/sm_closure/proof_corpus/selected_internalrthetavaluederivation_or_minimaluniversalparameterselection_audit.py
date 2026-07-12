"""Audit internal Rtheta value derivation / minimal universal parameter selection attack."""

from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "candidate_data"
CERTS = ROOT / "certificates"
CORPUS = ROOT / "proof_corpus"
BUILDER = ROOT / "scripts" / "build_selected_internalrthetavaluederivation_or_minimaluniversalparameterselection.py"

SLUG = "selected_internalrthetavaluederivation_or_minimaluniversalparameterselection"
PACKET_DIR = DATA / SLUG
CANDIDATE = DATA / f"{SLUG}.candidate.json"
CERT = CERTS / f"{SLUG}_certificate.json"
NOTE = CORPUS / "MTT_Selected_InternalRThetaValueDerivation_or_MinimalUniversalParameterSelection_v1.md"

FIRST_RESPONSE = PACKET_DIR / "internal_rtheta_first_response_sufficiency_test.packet.json"
FUNCTIONAL_READINESS = PACKET_DIR / "post_pi_threshold_functional_readiness_recheck.packet.json"
PARAMETER_RECHECK = PACKET_DIR / "minimal_universal_parameter_selection_recheck.packet.json"
DECISION = PACKET_DIR / "internal_or_minimal_selection_decision.packet.json"
CUTSET = PACKET_DIR / "next_cutset_after_internal_rtheta_attack.packet.json"

STATUS = (
    "MTT_SELECTED_INTERNALRTHETAVALUEDERIVATION_OR_MINIMALUNIVERSALPARAMETERSELECTION_"
    "BUILT_FIRST_RESPONSE_NOGO_HIGHER_RESPONSE_REQUIRED"
)
NEXT = "MTT_Selected_HigherResponseRThetaFunctional_or_SourceAnchorTheorem_v1"


def load(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def expect(condition: bool, message: str, errors: list[str]) -> None:
    if not condition:
        errors.append(message)


def guard(packet: dict[str, Any], errors: list[str], label: str) -> None:
    expect(packet.get("observed_data_used_as_selector") is False, f"{label} observed selector violation", errors)
    expect(packet.get("target_fitting_used") is False, f"{label} target fitting violation", errors)
    expect(packet.get("closure_claimed") is False, f"{label} overclaimed closure", errors)


def main() -> int:
    subprocess.run([sys.executable, str(BUILDER)], cwd=ROOT, check=True)

    candidate = load(CANDIDATE)
    cert = load(CERT)
    first_response = load(FIRST_RESPONSE)
    functional = load(FUNCTIONAL_READINESS)
    parameter = load(PARAMETER_RECHECK)
    decision = load(DECISION)
    cutset = load(CUTSET)
    note = NOTE.read_text(encoding="utf-8")

    errors: list[str] = []

    expect(candidate.get("status") == STATUS, "candidate status mismatch", errors)
    expect(cert.get("status") == STATUS, "certificate status mismatch", errors)
    expect(candidate.get("next_required_artifact") == NEXT, "candidate next mismatch", errors)
    expect(cert.get("next_required_artifact") == NEXT, "certificate next mismatch", errors)
    expect(candidate.get("theorem", {}).get("proved") is True, "candidate theorem not proved", errors)
    expect(cert.get("theorem_proved") is True, "certificate theorem missing", errors)

    for label, packet in [
        ("candidate", candidate),
        ("certificate", cert),
        ("first_response", first_response),
        ("functional", functional),
        ("parameter", parameter),
        ("decision", decision),
        ("cutset", cutset),
    ]:
        guard(packet, errors, label)

    expect(
        first_response.get("status") == "FIRST_RESPONSE_SELECTED_BUT_INSUFFICIENT_FOR_SCALAR_VALUE_ROWS",
        "first-response status mismatch",
        errors,
    )
    expect(first_response.get("selected_dynamic_matter_overlap_packet_closed") is True, "dynamic packet not closed", errors)
    expect(first_response.get("selected_first_response_layer_closed") is True, "first response not closed", errors)
    expect(first_response.get("dynamic_domain_basis_count") == 2, "dynamic basis count mismatch", errors)
    expect(first_response.get("dynamic_normal_form_rank") == 2, "dynamic rank mismatch", errors)
    expect(first_response.get("deltaTheta_C1") == [1.0, 1.0], "deltaTheta mismatch", errors)
    expect(first_response.get("charged_magnitude_basis_slots") == 9, "charged basis slot count mismatch", errors)
    expect(first_response.get("lambda_H_row_required") is True, "lambda_H row not required", errors)
    expect(first_response.get("scalar_target_slot_count") == 10, "scalar target slot count mismatch", errors)
    expect(first_response.get("accepted_selected_coefficient_rows") == 0, "selected coefficient rows overclaimed", errors)
    expect(first_response.get("coefficient_functional_closed") is False, "coefficient functional overclosed", errors)
    expect(first_response.get("lambda_H_coefficient_selected") is False, "lambda_H coefficient overclosed", errors)
    expect(first_response.get("first_response_sufficient_for_no_knob_value_rows") is False, "first response overaccepted", errors)
    expect(len(first_response.get("insufficiency_reasons", [])) >= 4, "insufficiency reasons incomplete", errors)

    expect(
        functional.get("status") == "POST_PI_EXTERNAL_READINESS_HIGH_INTERNAL_FUNCTIONAL_STILL_OPEN",
        "functional readiness status mismatch",
        errors,
    )
    expect(functional.get("old_present_required_output_count") == 1, "old readiness present mismatch", errors)
    expect(functional.get("old_required_output_count") == 5, "old readiness requirement mismatch", errors)
    checks = functional.get("post_pi_checks", {})
    for key in [
        "same_branch_scale_scheme_loop_convention_closed",
        "admitted_external_threshold_rows_available",
        "admitted_external_mass_scheme_rows_available",
        "accepted_diagonal_theorem_available",
        "no_observed_selector_guard_present",
    ]:
        expect(checks.get(key) is True, f"post-Pi check missing: {key}", errors)
    for key in [
        "selected_threshold_response_functional_emitted",
        "selected_internal_threshold_mass_rows_emitted",
    ]:
        expect(checks.get(key) is False, f"post-Pi internal check overclosed: {key}", errors)
    expect(functional.get("present_under_external_replay_count") == 5, "external replay readiness count mismatch", errors)
    expect(functional.get("required_under_external_replay_count") == 5, "external replay requirement mismatch", errors)
    expect(functional.get("present_under_strict_internal_no_knob_count") == 2, "internal no-knob readiness count mismatch", errors)
    expect(functional.get("required_under_strict_internal_no_knob_count") == 4, "internal no-knob requirement mismatch", errors)
    expect(functional.get("post_pi_external_replay_ready") is True, "post-Pi external replay not ready", errors)
    expect(functional.get("selected_threshold_response_functional_instantiated") is False, "threshold functional overclosed", errors)
    expect(functional.get("accepted_external_rows_promote_to_internal_no_knob") is False, "external rows promoted to no-knob", errors)

    expect(
        parameter.get("status") == "NO_UNIVERSAL_PARAMETER_SELECTED_AFTER_INTERNAL_RTHETA_ATTACK",
        "parameter status mismatch",
        errors,
    )
    expect(parameter.get("selected_universal_parameter_count") == 0, "selected parameter overclaimed", errors)
    expect(parameter.get("maximum_live_universal_parameters") == 3, "max universal parameter mismatch", errors)
    expect(parameter.get("candidate_specific_source_theorem_present") is False, "source theorem overclaimed", errors)
    expect(parameter.get("minimal_universal_parameter_selection_closed") is False, "minimal parameter overclosed", errors)
    expect(parameter.get("minimal_universal_parameter_lane_selected_now") is False, "minimal lane overselected", errors)
    expect(len(parameter.get("allowed_lanes_rechecked", [])) == 4, "lane recheck count mismatch", errors)

    expect(
        decision.get("status") == "INTERNAL_FIRST_RESPONSE_NOGO_AND_MINIMAL_PARAMETER_NOT_SELECTED",
        "decision status mismatch",
        errors,
    )
    expect(decision.get("internal_first_response_sufficient") is False, "decision overaccepts first response", errors)
    expect(decision.get("selected_higher_response_or_retarded_kernel_derivative_required") is True, "higher response not required", errors)
    expect(decision.get("higher_response_sector_coefficients_closed") is False, "higher response overclosed", errors)
    expect(decision.get("accepted_generation_threshold_source_row_count") == 0, "generation rows overaccepted", errors)
    expect(decision.get("diagnostic_sector_coefficients_rejected") is True, "diagnostic coefficients not rejected", errors)
    expect(decision.get("minimal_universal_parameter_selected") is False, "minimal parameter selected", errors)
    expect(decision.get("post_pi_external_replay_ready") is True, "external replay lost", errors)
    for key in ["no_knob_value_derivation_closed", "true_SM_equivalence_closed", "full_no_knob_closed"]:
        expect(decision.get(key) is False, f"decision overclosed: {key}", errors)

    expect(
        cutset.get("status") == "NEXT_ATTACK_HIGHER_RESPONSE_RTHETA_FUNCTIONAL_OR_SOURCE_ANCHOR_THEOREM",
        "cutset status mismatch",
        errors,
    )
    closed = cutset.get("closed_now", {})
    for key in [
        "selected_first_response_internal_value_sufficiency_test",
        "first_response_only_route_rejected_for_scalar_no_knob_values",
        "post_pi_functional_readiness_rechecked",
        "minimal_universal_parameter_selection_rechecked",
        "higher_response_or_source_anchor_identified_as_required",
    ]:
        expect(closed.get(key) is True, f"cutset closure missing: {key}", errors)
    still = cutset.get("still_open", {})
    for key in [
        "selected_higher_response_Rtheta_functional",
        "selected_retarded_kernel_derivative_value_functional",
        "selected_internal_Rtheta_threshold_mass_derivation",
        "numeric_Rtheta_coefficient_values",
        "lambda_H_value_execution",
        "candidate_specific_universal_source_anchor_theorem",
        "Yukawa_mass_mixing_value_closure",
        "true_SM_equivalence",
        "full_no_knob",
    ]:
        expect(still.get(key) is True, f"cutset overclosed: {key}", errors)
    expect(cutset.get("recommended_next", {}).get("artifact") == NEXT, "cutset next mismatch", errors)

    closure = candidate.get("closure_decision", {})
    expect(closure.get("first_response_only_route_rejected_for_scalar_no_knob_values") is True, "candidate no-go missing", errors)
    expect(closure.get("dynamic_first_response_layer_closed") is True, "candidate dynamic layer missing", errors)
    expect(closure.get("dynamic_normal_form_rank") == 2, "candidate dynamic rank mismatch", errors)
    expect(closure.get("scalar_target_slot_count") == 10, "candidate scalar target mismatch", errors)
    expect(closure.get("selected_internal_value_emission_count") == 0, "candidate value emissions overclaimed", errors)
    expect(closure.get("accepted_coefficient_value_count") == 0, "candidate coefficient rows overclaimed", errors)
    expect(closure.get("selected_universal_parameter_count") == 0, "candidate universal parameter overclaimed", errors)
    for key in [
        "selected_threshold_response_functional_instantiated",
        "lambda_H_value_execution",
        "minimal_universal_parameter_selection_closed",
        "no_knob_value_derivation_closed",
        "true_SM_equivalence_closed",
        "full_no_knob_closed",
    ]:
        expect(closure.get(key) is False, f"candidate overclosed: {key}", errors)
        expect(cert.get(key) is False, f"certificate overclosed: {key}", errors)

    expect("dynamic first-response layer closed     : true" in note, "note missing dynamic layer", errors)
    expect("dynamic normal-form rank                : 2" in note, "note missing rank", errors)
    expect("scalar target slots                     : 10" in note, "note missing scalar slots", errors)
    expect("accepted selected coefficient rows      : 0" in note, "note missing coefficient count", errors)
    expect("selected universal parameters           : 0" in note, "note missing universal parameter count", errors)
    expect("first-response scalar no-knob closure   : false" in note, "note missing no-go guard", errors)
    expect("full no-knob closure                    : false" in note, "note missing no-knob guard", errors)
    expect("true SM equivalence                     : false" in note, "note missing true SM guard", errors)

    if errors:
        print("Internal Rtheta/minimal-parameter audit FAILED")
        for error in errors:
            print(f"- {error}")
        return 1

    print("Internal Rtheta/minimal-parameter audit passed")
    print(json.dumps({"candidate": str(CANDIDATE.relative_to(ROOT)), "status": STATUS}, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
