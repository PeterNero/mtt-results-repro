"""Audit H one-parameter adoption policy or finite-H source construction packet."""

from __future__ import annotations

import json
import math
import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SLUG = "selected_honeparameteradoptionpolicy_or_finitehsourceconstruction"
DATA = ROOT / "candidate_data" / f"{SLUG}.candidate.json"
PACKET_DIR = ROOT / "candidate_data" / SLUG
ADOPTION = PACKET_DIR / "h_one_parameter_adoption_policy.packet.json"
FINITE_H = PACKET_DIR / "strict_finite_h_construction_workorder.packet.json"
STANDARDS = PACKET_DIR / "h_closure_standards_ledger.packet.json"
NEXT_PACKET = PACKET_DIR / "next_execution_target.packet.json"
CERT = ROOT / "certificates" / f"{SLUG}_certificate.json"
NOTE = ROOT / "proof_corpus" / "MTT_Selected_HOneParameterAdoptionPolicy_or_FiniteHSourceConstruction_v1.md"
BUILDER = ROOT / "scripts" / f"build_{SLUG}.py"

STATUS = (
    "MTT_SELECTED_HONEPARAMETERADOPTIONPOLICY_OR_FINITEHSOURCECONSTRUCTION_"
    "POLICY_CLOSED_ONE_PARAMETER_AVAILABLE_STRICT_SOURCE_OPEN"
)
NEXT = "MTT_Selected_HOneParameterExecutionLedger_or_StrictFiniteHSourceRows_v1"


def load(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def require(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)


def guard(packet: dict, label: str) -> None:
    require(packet.get("closure_claimed") is True, f"{label} closure flag")
    require(packet.get("observed_data_used_as_selector") is False, f"{label} observed selector")
    require(packet.get("target_fitting_used") is False, f"{label} target fitting")


def main() -> int:
    subprocess.run([sys.executable, str(BUILDER)], cwd=ROOT, check=True)

    data = load(DATA)
    adoption = load(ADOPTION)
    finite_h = load(FINITE_H)
    standards = load(STANDARDS)
    next_packet = load(NEXT_PACKET)
    cert = load(CERT)
    note = NOTE.read_text(encoding="utf-8")

    for label, packet in [
        ("candidate", data),
        ("adoption", adoption),
        ("finite_h", finite_h),
        ("standards", standards),
        ("next", next_packet),
        ("certificate", cert),
    ]:
        guard(packet, label)

    require(data["status"] == STATUS, "candidate status")
    require(cert["status"] == STATUS, "certificate status")
    require(data["next_required_artifact"] == NEXT, "candidate next")
    require(cert["next_required_artifact"] == NEXT, "certificate next")
    require(data["theorem"]["proved"] is True, "theorem")
    require(cert["theorem_proved"] is True, "certificate theorem")
    require(data["full_no_knob_closure_claimed"] is False, "no-knob overclaim")
    require(data["true_SM_equivalence_claimed"] is False, "true SM overclaim")

    parameter = adoption["parameter"]
    require(parameter["id"] == "UP-RET-OVERLAP.HRG", "parameter id")
    require(parameter["new_parameter_count"] == 1, "parameter count")
    require(parameter["value"] > 0, "parameter positive")
    require(math.isclose(parameter["derived_N_H"], parameter["value"] ** 2, abs_tol=1e-9), "N_H")

    rule = adoption["admission_rule"]
    require(rule["allowed_as_minimal_H_parameter"] is True, "minimal allowed")
    for key in [
        "allowed_as_strict_no_knob_source",
        "allowed_as_lambda_H_prediction",
        "allowed_as_true_SM_no_knob_closure",
    ]:
        require(rule[key] is False, f"adoption overclaims {key}")
    for key in [
        "must_be_declared_before_replay",
        "must_be_counted_in_parameter_budget",
        "must_not_be_retuned_per_observable",
    ]:
        require(rule[key] is True, f"adoption guard {key}")

    conditional = adoption["conditional_result_if_adopted"]
    require(conditional["conditional_H_K_rows"] == 10, "conditional H K rows")
    require(conditional["strict_K_rows_without_adoption"] == 9, "strict K rows")
    require(conditional["minimal_parameter_H_layer_closed"] is True, "minimal H closed")
    require(conditional["lambda_H_calibrated"] is True, "lambda calibrated")
    require(conditional["lambda_H_predicted"] is False, "lambda predicted")

    counts = finite_h["accepted_now"]
    for key in [
        "accepted_strict_source_route_count",
        "accepted_value_row_count",
        "accepted_final_certificate_count",
        "accepted_direct_radial_hessian_value_rows",
        "same_source_connection_values_accepted",
    ]:
        require(counts[key] == 0, f"finite-H count {key}")
    require(len(finite_h["required_source_objects"]) == 4, "required source objects")
    require("controlled finite-H action exact second variation" in finite_h["already_promoted_support"], "controlled support")
    require(finite_h["strict_no_knob_source_closed"] is False, "finite-H overclosed")
    for phrase in [
        "controlled UP-RET-OVERLAP.HRG as strict r_H",
        "lambda_H target inversion",
        "same-source labels without connection values",
        "internal dynamic-C1 cross-use as non-Higgs prediction",
    ]:
        require(phrase in finite_h["must_not_use"], f"must not use {phrase}")

    ledger = standards["standards"]
    require(ledger["strict_no_knob_H_closure"]["closed"] is False, "strict standard")
    require(ledger["strict_no_knob_H_closure"]["parameter_count"] == 0, "strict parameter count")
    require(ledger["minimal_one_parameter_H_closure"]["available"] is True, "minimal available")
    require(ledger["minimal_one_parameter_H_closure"]["closed_if_policy_adopted"] is True, "minimal if adopted")
    require(ledger["minimal_one_parameter_H_closure"]["parameter_count"] == 1, "minimal count")
    require(ledger["true_SM_no_knob_equivalence"]["closed"] is False, "true SM standard")
    require(standards["general_policy_import"]["acceptable_parameter_count_range_if_source_selected"] == [1, 2, 3], "general range")

    require(next_packet["next_required_artifact"] == NEXT, "next packet")
    require(next_packet["status"] == "NEXT_EXECUTE_ADOPTION_LEDGER_OR_STRICT_SOURCE_ROWS", "next status")

    decision = data["closure_decision"]
    require(decision["H_one_parameter_policy_closed"] is True, "policy closed")
    require(decision["H_one_parameter_available_if_explicitly_adopted"] is True, "parameter available")
    require(decision["H_one_parameter_adopted_now"] is False, "adopted too early")
    require(decision["H_one_parameter_count_if_adopted"] == 1, "decision count")
    require(decision["conditional_H_K_rows_if_adopted"] == 10, "decision K")
    require(decision["strict_finite_H_source_workorder_built"] is True, "workorder")
    for key in [
        "strict_finite_H_source_closed",
        "lambda_H_predicted",
        "full_no_knob_closed",
        "true_SM_equivalence_closed",
    ]:
        require(decision[key] is False, f"decision overclosed {key}")
    require(decision["strict_value_rows_accepted"] == 0, "strict rows")
    require(decision["accepted_nonhiggs_HRG_prediction_targets"] == 0, "non-Higgs HRG")

    for phrase in [
        "HOneParameterAdoptionPolicyOrFiniteHSourceConstructionTheorem",
        "minimal one-parameter H closure: available if explicitly adopted",
        "parameter count if adopted: `1`",
        "conditional H K rows if adopted: `10/10`",
        "cannot be called no-knob closure",
        NEXT,
    ]:
        require(phrase in note, f"note missing {phrase}")

    print(
        "AUDIT_PASS: H one-parameter policy is closed as available/not adopted; "
        "strict finite-H source construction remains open."
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
