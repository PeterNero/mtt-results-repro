"""Audit Step 7 common-RG/covariance/observable-suite and final gate boundary."""

from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
SLUG = "selected_step7_commonrgcovarianceobservablesuite_or_finaltruesmequivalencegate"
BUILDER = ROOT / "scripts" / f"build_{SLUG}.py"
DATA = ROOT / "candidate_data" / f"{SLUG}.candidate.json"
PACKET_DIR = ROOT / "candidate_data" / SLUG
POLICY = PACKET_DIR / "step7_policy_suite_closure.packet.json"
STATUS_MATRIX = PACKET_DIR / "step7_must_close_status_matrix.packet.json"
TRUE_GATE = PACKET_DIR / "step7_final_true_equivalence_gate.packet.json"
BOUNDARY = PACKET_DIR / "step7_closure_boundary.packet.json"
HANDOFF = PACKET_DIR / "step7_to_step8_handoff.packet.json"
CERT = ROOT / "certificates" / f"{SLUG}_certificate.json"
NOTE = ROOT / "proof_corpus" / "MTT_Selected_Step7_CommonRGCovarianceObservableSuite_or_FinalTrueSMEquivalenceGate_v1.md"

STATUS = (
    "MTT_SELECTED_STEP7_COMMONRGCOVARIANCEOBSERVABLESUITE_OR_FINALTRUESMEQUIVALENCEGATE_"
    "CLOSED_GATE_CONTRACT_TRUE_EQUIVALENCE_OPEN"
)
NEXT = "MTT_Selected_Step8_PrecisionValueEmission_or_ActualQaSU3OperatorPacketClosure_v1"


def load(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def expect(condition: bool, message: str, errors: list[str]) -> None:
    if not condition:
        errors.append(message)


def guard(packet: dict[str, Any], errors: list[str], label: str, *, closure: bool) -> None:
    expect(packet.get("observed_data_used_as_selector") is False, f"{label} observed selector violation", errors)
    expect(packet.get("target_fitting_used") is False, f"{label} target fitting violation", errors)
    expect(packet.get("closure_claimed") is closure, f"{label} closure flag mismatch", errors)


def main() -> int:
    subprocess.run([sys.executable, str(BUILDER)], cwd=ROOT, check=True)

    data = load(DATA)
    cert = load(CERT)
    policy = load(POLICY)
    matrix = load(STATUS_MATRIX)
    true_gate = load(TRUE_GATE)
    boundary = load(BOUNDARY)
    handoff = load(HANDOFF)
    note = NOTE.read_text(encoding="utf-8")
    errors: list[str] = []

    expect(data.get("status") == STATUS, "candidate status mismatch", errors)
    expect(cert.get("status") == STATUS, "certificate status mismatch", errors)
    expect(data.get("next_required_artifact") == NEXT, "candidate next mismatch", errors)
    expect(cert.get("next_required_artifact") == NEXT, "certificate next mismatch", errors)
    expect(data.get("theorem", {}).get("proved") is True, "candidate theorem not proved", errors)
    expect(cert.get("theorem_proved") is True, "certificate theorem not proved", errors)

    guard(data, errors, "candidate", closure=False)
    guard(cert, errors, "certificate", closure=False)
    guard(policy, errors, "policy", closure=True)
    guard(matrix, errors, "matrix", closure=True)
    guard(true_gate, errors, "true gate", closure=True)
    guard(boundary, errors, "boundary", closure=False)
    guard(handoff, errors, "handoff", closure=False)

    for key in [
        "RG_reference_scheme_and_scale_policy",
        "central_value_covariance_tier_policy",
        "minimal_neutrino_oscillation_policy",
        "observable_suite_manifest",
        "precision_empirical_replay_suite_built",
        "tree_QFT_identity_tier_closed",
        "policy_suite_closed_for_step7_contract",
    ]:
        expect(policy.get(key) is True, f"policy row missing: {key}", errors)
    expect(policy.get("full_covariance_profile_values_closed") is False, "full covariance overclosed", errors)
    expect(policy.get("precision_local_QFT_observable_values_closed") is False, "precision QFT values overclosed", errors)

    rows = matrix.get("rows", {})
    expected_rows = [
        "single_common_scale_transport",
        "loop_order_beta_functions_and_thresholds",
        "mass_scheme_unification",
        "Yukawa_running_matrices_at_common_scale",
        "Higgs_lambda_running_at_common_scale",
        "full_CKM_PMNS_covariance_or_profile_likelihood",
        "absolute_neutrino_mass_or_declared_minimal_parity_policy",
        "observable_suite_with_tolerances",
        "selected_SM_packet_final_certificate",
    ]
    expect(set(rows) == set(expected_rows), "Step 7 row set mismatch", errors)
    expect(matrix.get("all_rows_closed_for_step7_contract") is True, "Step 7 contract rows not closed", errors)
    expect(matrix.get("all_rows_closed_for_true_equivalence") is False, "Step 7 true equivalence overclosed", errors)
    for key in expected_rows:
        row = rows.get(key, {})
        expect(row.get("closed_for_step7_contract") is True, f"row not closed for contract: {key}", errors)
        expect(row.get("blocks_true_equivalence") is True, f"row should block true equivalence: {key}", errors)
        expect(str(row.get("true_equivalence_status", "")).startswith("OPEN"), f"row not marked open for true equivalence: {key}", errors)

    expect(true_gate.get("precision_value_table_contract_ready") is True, "precision contract not ready", errors)
    expect(true_gate.get("actual_QaSU3_operator_upgrade_contract_ready") is True, "QaSU3 contract not ready", errors)
    expect(true_gate.get("partial_precision_values_emitted") is True, "partial precision values missing", errors)
    expect(true_gate.get("qasu3_source_payload_filled") is False, "QaSU3 source payload overfilled", errors)
    expect(true_gate.get("true_SM_equivalence_closed") is False, "true gate true equivalence overclosed", errors)
    expect(true_gate.get("full_no_knob_closed") is False, "true gate no-knob overclosed", errors)
    for key in [
        "precision_value_profile_table_with_loop_scheme_covariance_semantics",
        "actual_selected_QaSU3_source_operator_packet",
    ]:
        expect(true_gate.get("true_equivalence_next_routes", {}).get(key) is True, f"next route missing: {key}", errors)
    for key in [
        "actual_QaSU3_operator_packet",
        "full_nonHiggs_covariance_profile",
        "precision_local_QFT_loop_values",
        "published_or_reconstructed_correlated_profile_values",
        "full_no_knob_closure",
    ]:
        expect(true_gate.get("remaining_true_equivalence_blockers", {}).get(key) is True, f"blocker missing: {key}", errors)

    for key in [
        "policy_suite_closed_for_step7_contract",
        "all_step7_rows_closed_for_gate_contract",
        "SM_parity_closed",
        "central_or_firstpass_comparison_tier_closed",
        "precision_value_table_contract_ready",
        "actual_QaSU3_operator_upgrade_contract_ready",
        "step7_closed_for_plan_contract",
    ]:
        expect(boundary.get(key) is True, f"boundary missing: {key}", errors)
    expect(boundary.get("all_step7_rows_closed_for_true_equivalence") is False, "boundary true rows overclosed", errors)
    expect(boundary.get("true_SM_equivalence_closed") is False, "boundary true SM overclosed", errors)
    expect(boundary.get("full_no_knob_closed") is False, "boundary no-knob overclosed", errors)

    expect(handoff.get("completed_step") == 7, "handoff completed step mismatch", errors)
    expect(handoff.get("next_step") == 8, "handoff next step mismatch", errors)
    expect(handoff.get("next_required_artifact") == NEXT, "handoff next mismatch", errors)
    for key in [
        "precision_value_profile_table_with_loop_scheme_covariance_semantics",
        "actual_selected_QaSU3_source_operator_packet",
    ]:
        expect(handoff.get("step8_must_close_one_or_both_routes", {}).get(key) is True, f"handoff route missing: {key}", errors)
    for key in [
        "diagnostic_coefficients",
        "admitted_external_replay_rows",
        "measured_Yukawa_CKM_PMNS_lambdaH_values",
        "profile_residuals",
    ]:
        expect(handoff.get("step8_must_not_use_as_selectors", {}).get(key) is True, f"selector guard missing: {key}", errors)

    decision = data.get("closure_decision", {})
    expect(decision.get("step7_closed_for_plan_contract") is True, "candidate Step 7 closure missing", errors)
    expect(decision.get("all_step7_rows_closed_for_gate_contract") is True, "candidate gate rows not closed", errors)
    expect(decision.get("all_step7_rows_closed_for_true_equivalence") is False, "candidate true rows overclosed", errors)
    expect(decision.get("SM_parity_closed") is True, "candidate SM parity missing", errors)
    expect(decision.get("true_SM_equivalence_closed") is False, "candidate true SM overclosed", errors)
    expect(decision.get("full_no_knob_closed") is False, "candidate no-knob overclosed", errors)
    expect(data.get("step7_contract_closure_claimed") is True, "candidate Step 7 local claim missing", errors)
    expect(data.get("SM_parity_closure_claimed") is True, "candidate SM parity claim missing", errors)
    expect(data.get("true_SM_equivalence_claimed") is False, "candidate true SM claim overclosed", errors)
    expect(data.get("full_no_knob_closure_claimed") is False, "candidate no-knob claim overclosed", errors)

    expect(cert.get("step7_contract_closure_claimed") is True, "certificate Step 7 local claim missing", errors)
    expect(cert.get("all_step7_rows_closed_for_gate_contract") is True, "certificate gate rows not closed", errors)
    expect(cert.get("all_step7_rows_closed_for_true_equivalence") is False, "certificate true rows overclosed", errors)
    expect(cert.get("SM_parity_closure_claimed") is True, "certificate SM parity claim missing", errors)
    expect(cert.get("true_SM_equivalence_claimed") is False, "certificate true SM claim overclosed", errors)
    expect(cert.get("full_no_knob_closure_claimed") is False, "certificate no-knob claim overclosed", errors)

    expect("Step 7 is closed as a gate contract" in note, "note missing Step 7 closure", errors)
    expect("all Step 7 rows closed for contract   : true" in note, "note missing contract closure", errors)
    expect("all Step 7 rows closed for true eq    : false" in note, "note missing true-equivalence guard", errors)
    expect("true SM equivalence closed            : false" in note, "note missing true SM guard", errors)
    expect(NEXT in note, "note missing next artifact", errors)

    if errors:
        print("Step 7 audit FAILED")
        for error in errors:
            print(f"- {error}")
        return 1

    print("Step 7 audit passed")
    print(json.dumps({"candidate": str(DATA.relative_to(ROOT)), "status": STATUS}, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
