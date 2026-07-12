"""Audit R_theta threshold rows or profile-convention source closure packet."""

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
BUILDER = ROOT / "scripts" / "build_selected_rtheta_thresholdrows_or_profileconventionsourceclosure.py"

SLUG = "selected_rtheta_thresholdrows_or_profileconventionsourceclosure"
PACKET_DIR = DATA / SLUG
CANDIDATE = DATA / f"{SLUG}.candidate.json"
CERT = CERTS / f"{SLUG}_certificate.json"
NOTE = CORPUS / "MTT_Selected_RThetaThresholdRows_or_ProfileConventionSourceClosure_v1.md"

ORDER = PACKET_DIR / "remaining_value_frontier_dependency_order.packet.json"
PROFILE = PACKET_DIR / "profile_convention_source_recheck.packet.json"
ROWS = PACKET_DIR / "threshold_mass_scheme_source_rows_recheck.packet.json"
EXECUTION = PACKET_DIR / "rtheta_value_execution_readiness_after_ordering.packet.json"
CUTSET = PACKET_DIR / "next_cutset_after_threshold_profile_ordering.packet.json"

STATUS = (
    "MTT_SELECTED_RTHETA_THRESHOLDROWS_OR_PROFILECONVENTIONSOURCECLOSURE_"
    "BUILT_ORDERED_FRONTIER_ROWS_OPEN"
)
NEXT = "MTT_Selected_ValueSourceDerivationObligationKernel_or_ExternalThresholdImportManifest_v1"


def load(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def expect(condition: bool, message: str, errors: list[str]) -> None:
    if not condition:
        errors.append(message)


def main() -> int:
    subprocess.run([sys.executable, str(BUILDER)], cwd=ROOT, check=True)

    candidate = load(CANDIDATE)
    cert = load(CERT)
    order = load(ORDER)
    profile = load(PROFILE)
    rows = load(ROWS)
    execution = load(EXECUTION)
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
        order.get("status") == "REMAINING_VALUE_FRONTIER_HAS_ORDERED_INTERDEPENDENT_GATES",
        "order status mismatch",
        errors,
    )
    expect(order.get("obvious_order_exists") is True, "order theorem missing", errors)
    expect(order.get("but_gates_are_interlinked") is True, "interlink theorem missing", errors)
    for key in [
        "Pi_Rtheta",
        "selected_dynamic_operator_source_owner",
        "coefficient_functional_domain",
        "source_normalized_projection_weights",
        "generation_structure_support",
    ]:
        expect(order["closed_prerequisites"].get(key) is True, f"closed prerequisite missing: {key}", errors)
    layers = {item["id"]: item for item in order.get("ordered_remaining_layers", [])}
    expect(layers["same_branch_scale_scheme_loop_convention"]["layer"] == 1, "convention layer mismatch", errors)
    expect(layers["full_profile_likelihood_or_accepted_diagonal_theorem"]["layer"] == 1, "profile layer mismatch", errors)
    expect(layers["threshold_matching_source_rows"]["layer"] == 2, "threshold rows layer mismatch", errors)
    expect(layers["mass_scheme_conversion_source_rows"]["layer"] == 2, "mass rows layer mismatch", errors)
    expect(layers["no_knob_value_derivation"]["layer"] == 3, "no-knob layer mismatch", errors)

    expect(
        profile.get("status") == "FIRSTPASS_PROFILE_AVAILABLE_TRUE_SOURCE_CONVENTION_OPEN",
        "profile status mismatch",
        errors,
    )
    expect(profile.get("firstpass_profile_layer_closed") is True, "firstpass profile support missing", errors)
    for key in [
        "same_branch_scale_scheme_loop_convention_closed",
        "full_profile_likelihood_closed",
        "full_covariance_profile_closed",
        "accepted_for_true_precision_equivalence",
        "closure_claimed",
    ]:
        expect(profile.get(key) is False, f"profile overclosed: {key}", errors)

    expect(rows.get("status") == "SOURCE_ROW_AUDIT_NONE_ACCEPTED_ROWS_OPEN", "rows status mismatch", errors)
    expect(rows.get("candidate_source_row_count") == 6, "candidate row count mismatch", errors)
    expect(rows.get("support_present_count") >= 5, "support row count too low", errors)
    expect(rows.get("promotable_count") == 0, "rows overpromoted", errors)
    expect(rows.get("accepted_threshold_matching_source_rows") == [], "threshold rows overclosed", errors)
    expect(rows.get("accepted_mass_scheme_conversion_source_rows") == [], "mass rows overclosed", errors)
    expect(rows.get("accepted_source_rows_present") is False, "accepted rows overclaimed", errors)
    expect(rows.get("residual_rows_finite_but_downstream") is True, "residual guard missing", errors)
    expect(rows.get("closure_claimed") is False, "rows closure overclaimed", errors)

    expect(
        execution.get("status") == "VALUE_EXECUTION_ORDERED_BUT_STILL_BLOCKED",
        "execution status mismatch",
        errors,
    )
    expect(execution.get("ordered_dependency_graph_closed") is True, "execution missing order graph", errors)
    for key in [
        "selected_threshold_response_functional_instantiated",
        "selected_value_evaluator_closed",
        "accepted_lambda_H_value",
        "closure_claimed",
    ]:
        expect(execution.get(key) is False, f"execution overclosed: {key}", errors)
    expect(execution.get("accepted_coefficient_value_count") == 0, "execution accepted coefficients", errors)
    expected_open = [
        "same_branch_scale_scheme_loop_convention",
        "threshold_matching_source_rows",
        "mass_scheme_conversion_source_rows",
        "no_knob_value_derivation",
        "full_profile_likelihood_or_accepted_diagonal_theorem",
    ]
    expect(execution.get("blocking_failures") == expected_open, "execution blocker list mismatch", errors)

    expect(
        cutset.get("status") == "NEXT_ATTACK_VALUE_SOURCE_OBLIGATION_OR_EXTERNAL_THRESHOLD_IMPORT",
        "cutset status mismatch",
        errors,
    )
    expect(cutset.get("recommended_next", {}).get("artifact") == NEXT, "cutset next mismatch", errors)
    expect(cutset.get("closed_now", {}).get("remaining_value_frontier_dependency_order") is True, "cutset missing order closure", errors)
    expect(cutset.get("still_open") == expected_open, "cutset open list mismatch", errors)
    expect(cutset.get("closure_claimed") is False, "cutset overclaimed", errors)

    closure = candidate.get("closure_decision", {})
    expect(closure.get("ordered_dependency_graph_closed") is True, "candidate missing order closure", errors)
    expect(closure.get("generation_structure_support_closed") is True, "candidate generation support missing", errors)
    for key in [
        "same_branch_scale_scheme_loop_convention_closed",
        "threshold_matching_source_rows_closed",
        "mass_scheme_conversion_source_rows_closed",
        "no_knob_value_derivation_closed",
        "full_profile_likelihood_or_accepted_diagonal_theorem_closed",
        "selected_threshold_response_functional_instantiated",
        "selected_value_evaluator_closed",
        "accepted_lambda_H_value",
        "true_SM_equivalence_closed",
        "full_no_knob_closed",
    ]:
        expect(closure.get(key) is False, f"candidate closure overclosed: {key}", errors)
    expect(closure.get("accepted_coefficient_value_count") == 0, "candidate accepted coefficients", errors)
    expect(candidate.get("theorem", {}).get("proved") is True, "candidate theorem not proved", errors)
    expect(cert.get("theorem_proved") is True, "certificate theorem missing", errors)
    expect(cert.get("ordered_dependency_graph_closed") is True, "cert order closure missing", errors)
    expect(cert.get("selected_threshold_response_functional_instantiated") is False, "cert threshold overclosed", errors)
    expect(cert.get("accepted_coefficient_value_count") == 0, "cert accepted coefficients", errors)

    expect("ordered dependency graph closed               : true" in note, "note missing order closure", errors)
    expect("threshold matching source rows                : false" in note, "note missing threshold guard", errors)
    expect("mass-scheme conversion source rows            : false" in note, "note missing mass guard", errors)
    expect("accepted coefficient values                    : 0" in note, "note missing zero-value guard", errors)

    if errors:
        print("RTheta threshold/profile ordering audit FAILED")
        for error in errors:
            print(f"- {error}")
        return 1

    print("RTheta threshold/profile ordering audit passed")
    print(json.dumps({"candidate": str(CANDIDATE.relative_to(ROOT)), "status": STATUS}, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
