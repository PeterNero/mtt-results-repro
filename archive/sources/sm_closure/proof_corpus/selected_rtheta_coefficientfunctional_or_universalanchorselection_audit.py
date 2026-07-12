"""Audit R_theta coefficient-functional readiness / universal-anchor selection gate."""

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
BUILDER = ROOT / "scripts" / "build_selected_rtheta_coefficientfunctional_or_universalanchorselection.py"

SLUG = "selected_rtheta_coefficientfunctional_or_universalanchorselection"
PACKET_DIR = DATA / SLUG
CANDIDATE = DATA / f"{SLUG}.candidate.json"
CERT = CERTS / f"{SLUG}_certificate.json"
NOTE = CORPUS / "MTT_Selected_RThetaCoefficientFunctional_or_UniversalAnchorSelection_v1.md"

FUNCTIONAL = PACKET_DIR / "rtheta_coefficient_functional_skeleton.packet.json"
EVALUATOR_GATE = PACKET_DIR / "rtheta_value_evaluator_provenance_gate.packet.json"
DOMAIN_UPDATE = PACKET_DIR / "rtheta_domain_readiness_after_coefficient_functional.packet.json"
UNIVERSAL = PACKET_DIR / "universal_anchor_selection_attempt.packet.json"
DECISION = PACKET_DIR / "coefficient_functional_readiness_decision.packet.json"
CUTSET = PACKET_DIR / "next_cutset_after_coefficient_functional_readiness.packet.json"

STATUS = (
    "MTT_SELECTED_RTHETA_COEFFICIENTFUNCTIONAL_OR_UNIVERSALANCHORSELECTION_"
    "BUILT_FUNCTIONAL_READINESS_CLOSED_VALUES_OPEN"
)
NEXT = "MTT_Selected_RThetaValueEvaluatorSourceProvenance_or_SelectedRouteCClosure_v1"


def load(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def expect(condition: bool, message: str, errors: list[str]) -> None:
    if not condition:
        errors.append(message)


def main() -> int:
    subprocess.run([sys.executable, str(BUILDER)], cwd=ROOT, check=True)

    candidate = load(CANDIDATE)
    cert = load(CERT)
    functional = load(FUNCTIONAL)
    evaluator = load(EVALUATOR_GATE)
    domain = load(DOMAIN_UPDATE)
    universal = load(UNIVERSAL)
    decision = load(DECISION)
    cutset = load(CUTSET)
    note = NOTE.read_text(encoding="utf-8")

    errors: list[str] = []

    expect(candidate.get("status") == STATUS, "candidate status mismatch", errors)
    expect(cert.get("status") == STATUS, "certificate status mismatch", errors)
    expect(candidate.get("next_required_artifact") == NEXT, "candidate next mismatch", errors)
    expect(cert.get("next_required_artifact") == NEXT, "certificate next mismatch", errors)
    for key in [
        "closure_claimed",
        "unpatched_theorem_closure_claimed",
        "observed_data_used_as_selector",
        "target_fitting_used",
    ]:
        expect(candidate.get(key) is False, f"candidate guardrail overclaimed: {key}", errors)

    expect(
        functional.get("status") == "COEFFICIENT_FUNCTIONAL_SKELETON_CLOSED_VALUES_OPEN",
        "functional status mismatch",
        errors,
    )
    expect(functional.get("functional_symbol") == "R_theta", "functional symbol mismatch", errors)
    expect(functional.get("coefficient_functional_readiness_closed") is True, "functional readiness not closed", errors)
    expect(functional.get("charged_functional_row_count") == 9, "wrong charged functional row count", errors)
    expect(functional.get("required_charged_functional_row_count") == 9, "wrong required charged row count", errors)
    expect(functional.get("coefficient_values_selected") is False, "coefficient values overselected", errors)
    expect(
        functional.get("generation_resolved_threshold_source_rows_closed") is False,
        "generation rows overclosed",
        errors,
    )
    expect(functional.get("closure_claimed") is True, "functional local closure should hold", errors)
    domain_components = functional.get("domain_components_closed", {})
    expect(all(domain_components.values()), "all functional domain components should be closed", errors)
    for row in functional.get("charged_functional_rows", []):
        expect(row.get("domain_basis_row_selected") is True, f"{row.get('row_id')} basis not selected", errors)
        expect(row.get("coefficient_value_selected") is False, f"{row.get('row_id')} value overselected", errors)
        expect(row.get("accepted_as_magnitude_value_row") is False, f"{row.get('row_id')} magnitude overaccepted", errors)
        expect("Eval_Rtheta" in row.get("functional_formula_skeleton", ""), f"{row.get('row_id')} formula skeleton missing", errors)
        expect(row.get("value_evaluator_required") == "SelectedRouteCValueEvaluator", f"{row.get('row_id')} evaluator mismatch", errors)

    expect(
        evaluator.get("status") == "VALUE_EVALUATOR_PROVENANCE_OPEN_FORMAL_LIFT_REJECTED_AS_PROOF",
        "evaluator gate status mismatch",
        errors,
    )
    expect(evaluator.get("readiness_present_count") == 4, "Route-C readiness count should remain 4", errors)
    expect(evaluator.get("readiness_required_count") == 7, "Route-C required count should be 7", errors)
    expect(evaluator.get("formal_lift_lower_validators_all_pass") is True, "formal-lift lower validators should pass", errors)
    expect(evaluator.get("formal_lift_promotion_passes") is True, "formal-lift promotion diagnostic should pass", errors)
    for key in [
        "formal_lift_accepted_as_proof",
        "proof_promotion_allowed",
        "honest_selected_source_verified",
        "Pi_Rtheta_closed",
        "selected_value_evaluator_closed",
        "accepted_lambda_H_value",
        "closure_claimed",
    ]:
        expect(evaluator.get(key) is False, f"evaluator overclosed: {key}", errors)
    expect(evaluator.get("accepted_coefficient_value_count") == 0, "evaluator accepted coefficient values", errors)

    expect(
        domain.get("status") == "RTHETA_DOMAIN_READINESS_FULL_VALUES_AND_CODOMAIN_OPEN",
        "domain status mismatch",
        errors,
    )
    expect(domain.get("domain_present_count_before_update") == 4, "domain before count mismatch", errors)
    expect(domain.get("domain_present_count_after_update") == 5, "domain after count mismatch", errors)
    expect(domain.get("domain_requirement_count") == 5, "domain requirement count mismatch", errors)
    expect(domain.get("domain_readiness_closed") is True, "domain readiness not closed", errors)
    expect(domain.get("coefficient_functional_readiness_closed") is True, "coefficient functional readiness not recorded", errors)
    expect(domain.get("codomain_present_required_output_count_after_update") == 1, "codomain count overchanged", errors)
    expect(domain.get("codomain_required_output_count") == 5, "codomain requirement mismatch", errors)
    for key in [
        "coefficient_values_selected",
        "selected_threshold_response_functional_instantiated",
        "generation_resolved_threshold_source_rows_closed",
        "accepted_Yukawa_magnitudes_as_no_knob_predictions",
        "minimal_parameter_yukawa_closure_closed",
        "closure_claimed",
    ]:
        expect(domain.get(key) is False, f"domain overclosed: {key}", errors)
    expect(domain.get("new_frontier_is_evaluator_not_domain") is True, "frontier should move to evaluator", errors)

    expect(
        universal.get("status") == "UNIVERSAL_ANCHOR_NOT_SELECTED_FUNCTIONAL_READINESS_PREFERRED",
        "universal status mismatch",
        errors,
    )
    expect(universal.get("selected_universal_parameter_count") == 0, "universal parameter overselected", errors)
    expect(universal.get("universal_anchor_selected") is False, "universal anchor overselected", errors)
    expect(universal.get("closure_claimed") is False, "universal overclaimed", errors)

    expect(
        decision.get("status") == "RTHETA_READINESS_CLOSED_VALUE_EVALUATOR_SOURCE_PROVENANCE_OPEN",
        "decision status mismatch",
        errors,
    )
    expect(decision.get("functional_domain_readiness_closed") is True, "decision domain not closed", errors)
    expect(decision.get("coefficient_functional_skeleton_closed") is True, "decision skeleton not closed", errors)
    expect(decision.get("charged_functional_row_count") == 9, "decision charged row count mismatch", errors)
    expect(decision.get("threshold_mass_scheme_slot_count") == 10, "decision threshold slot count mismatch", errors)
    expect(decision.get("row_coefficient_slot_manifest_closed") is True, "decision manifest not closed", errors)
    expect(decision.get("accepted_coefficient_value_count") == 0, "decision accepted values overzero", errors)
    for key in [
        "value_evaluator_source_provenance_closed",
        "lambda_H_value_selected",
        "selected_threshold_response_functional_instantiated",
        "true_SM_equivalence_closed",
        "full_no_knob_closed",
        "closure_claimed",
    ]:
        expect(decision.get(key) is False, f"decision overclosed: {key}", errors)
    expect(len(decision.get("minimal_next_actions", [])) == 4, "decision next-action count mismatch", errors)

    expect(
        cutset.get("status") == "NEXT_ATTACK_VALUE_EVALUATOR_SOURCE_PROVENANCE_OR_SELECTED_ROUTEC_CLOSURE",
        "cutset status mismatch",
        errors,
    )
    for value in cutset.get("closed_now", {}).values():
        expect(value is True, "all cutset local closures should be true", errors)
    expect(cutset.get("recommended_next", {}).get("artifact") == NEXT, "cutset next mismatch", errors)
    expect(cutset.get("closure_claimed") is False, "cutset overclaimed", errors)

    closure = candidate.get("closure_decision", {})
    expect(closure.get("domain_readiness_closed") is True, "candidate domain not closed", errors)
    expect(closure.get("domain_present_count_after_update") == 5, "candidate domain count mismatch", errors)
    expect(closure.get("coefficient_functional_skeleton_closed") is True, "candidate skeleton not closed", errors)
    expect(closure.get("charged_functional_row_count") == 9, "candidate row count mismatch", errors)
    expect(closure.get("accepted_coefficient_value_count") == 0, "candidate accepted values overzero", errors)
    for key in [
        "value_evaluator_source_provenance_closed",
        "selected_threshold_response_functional_instantiated",
        "generation_resolved_threshold_source_rows_closed",
        "accepted_Yukawa_magnitudes_as_no_knob_predictions",
        "minimal_parameter_yukawa_closure_closed",
        "true_SM_equivalence_closed",
        "full_no_knob_closed",
    ]:
        expect(closure.get(key) is False, f"candidate closure overclosed: {key}", errors)
    expect(candidate.get("theorem", {}).get("proved") is True, "candidate theorem not proved", errors)
    expect(cert.get("theorem_proved") is True, "certificate theorem not recorded", errors)
    expect(cert.get("domain_present_count_after_update") == 5, "certificate domain count mismatch", errors)
    expect(cert.get("accepted_coefficient_value_count") == 0, "certificate accepted value mismatch", errors)

    expect("R_theta domain readiness closed        : true" in note, "note missing domain closure", errors)
    expect("domain readiness rows present          : 5/5" in note, "note missing 5/5 line", errors)
    expect("accepted coefficient values            : 0" in note, "note missing zero values guard", errors)
    expect("value evaluator provenance closed      : false" in note, "note missing evaluator guard", errors)

    if errors:
        print("RTheta coefficient-functional readiness audit FAILED")
        for error in errors:
            print(f"- {error}")
        return 1

    print("RTheta coefficient-functional readiness audit passed")
    print(json.dumps({"candidate": str(CANDIDATE.relative_to(ROOT)), "status": STATUS}, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
