"""Audit the strict tenth H K-row / large-threshold RG primitive theorem."""

from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SLUG = "selected_tenthhthresholdkrowsource_or_largethresholdrgprimitivetheorem"
DATA = ROOT / "candidate_data" / f"{SLUG}.candidate.json"
PACKET_DIR = ROOT / "candidate_data" / SLUG
ROUTE_EXECUTION = PACKET_DIR / "tenth_h_k_row_cycle_break_execution.packet.json"
UNIVERSAL_REJECTION = PACKET_DIR / "universal_primitive_exit_rejection.packet.json"
STRICT_GATE = PACKET_DIR / "strict_tenth_h_k_row_gate.packet.json"
NEXT_CUTSET = PACKET_DIR / "next_cutset_after_tenth_h_k_route_execution.packet.json"
CERT = ROOT / "certificates" / f"{SLUG}_certificate.json"
NOTE = ROOT / "proof_corpus" / "MTT_Selected_TenthHThresholdKRowSource_or_LargeThresholdRGPrimitiveTheorem_v1.md"
BUILDER = ROOT / "scripts" / f"build_{SLUG}.py"

STATUS = (
    "MTT_SELECTED_TENTHHKTHRESHOLDKROWSOURCE_OR_LARGETHRESHOLDRGPRIMITIVETHEOREM_"
    "CYCLE_BREAK_EXECUTED_STRICT_TWO_EXIT_FRONTIER"
)
NEXT = "MTT_Selected_HKThresholdSourceObject_or_RGHessianTransportConstruction_v1"


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
    route_execution = load(ROUTE_EXECUTION)
    universal_rejection = load(UNIVERSAL_REJECTION)
    strict_gate = load(STRICT_GATE)
    next_cutset = load(NEXT_CUTSET)
    cert = load(CERT)
    note = NOTE.read_text(encoding="utf-8")

    for label, packet in [
        ("candidate", data),
        ("route execution", route_execution),
        ("universal rejection", universal_rejection),
        ("strict gate", strict_gate),
        ("next cutset", next_cutset),
        ("certificate", cert),
    ]:
        guard(packet, label)

    require(data["status"] == STATUS, "candidate status")
    require(cert["status"] == STATUS, "certificate status")
    require(data["next_required_artifact"] == NEXT, "candidate next")
    require(cert["next_required_artifact"] == NEXT, "certificate next")
    require(data["theorem"]["proved"] is True, "candidate theorem")
    require(cert["theorem_proved"] is True, "certificate theorem")
    require(data["full_no_knob_closure_claimed"] is False, "no-knob overclaim")
    require(data["true_SM_equivalence_claimed"] is False, "true SM overclaim")

    decision = data["closure_decision"]
    require(decision["cycle_break_exits_executed"] is True, "cycle break executed")
    require(decision["universal_primitive_crossuse_rejected_currently"] is True, "universal rejection")
    require(decision["accepted_selected_K_source_row_count"] == 9, "strict K count")
    require(decision["selected_K_threshold_row_count_required"] == 10, "required K count")
    require(decision["remaining_strict_exit_count"] == 2, "remaining strict exits")
    require(decision["controlled_empirical_10_of_10_available"] is True, "controlled availability")
    require(
        decision["controlled_empirical_10_of_10_selected_for_no_knob"] is False,
        "controlled no-knob overclaim",
    )
    for key in [
        "direct_H_K_row_exit_accepted",
        "selected_large_threshold_RG_exit_accepted",
        "universal_primitive_crossuse_exit_accepted",
        "strict_H_K_threshold_row_emitted",
        "strict_Omega_lambda_scalar_execution_closed",
        "full_no_knob_closed",
        "true_SM_equivalence_closed",
    ]:
        require(decision[key] is False, f"decision overclosed {key}")

    require(
        route_execution["status"]
        == "THREE_EXITS_EXECUTED_UNIVERSAL_PRIMITIVE_REJECTED_TWO_STRICT_EXITS_OPEN",
        "route status",
    )
    results = route_execution["route_results"]
    require(set(results) == {"direct_H_K_row", "selected_large_threshold_RG", "universal_primitive_crossuse"}, "route set")
    for route_id, result in results.items():
        require(result["accepted"] is False, f"route accepted {route_id}")
        require(result["reason"], f"route reason {route_id}")

    strict_result = route_execution["strict_result"]
    require(strict_result["accepted_selected_K_source_row_count"] == 9, "route strict count")
    require(strict_result["selected_K_threshold_row_count_required"] == 10, "route required count")
    require(strict_result["strict_H_K_threshold_row_emitted"] is False, "route H row")
    require(strict_result["strict_ten_K_closure"] is False, "route ten K")
    require(strict_result["strict_Omega_lambda_scalar_execution_closed"] is False, "route Omega")

    controlled = route_execution["controlled_result"]
    require(controlled["controlled_empirical_10_of_10_available"] is True, "route controlled")
    require(controlled["controlled_empirical_10_of_10_selected_for_no_knob"] is False, "route controlled no-knob")

    require(
        universal_rejection["status"] == "UP_RET_OVERLAP_HRG_NOT_PROMOTED_ZERO_NONHIGGS_TARGETS",
        "universal rejection status",
    )
    require(universal_rejection["primitive"] == "UP-RET-OVERLAP.HRG", "primitive id")
    support = universal_rejection["controlled_support"]
    require(support["internal_dynamic_C1_crossuse_validated"] is True, "controlled support")
    require(support["same_parameter_reused_without_retuning"] is True, "same parameter")
    strict_rejection = universal_rejection["strict_rejection"]
    require(strict_rejection["accepted_nonhiggs_prediction_target_count"] == 0, "non-Higgs count")
    require(strict_rejection["strict_HRG_source_theorem_emitted"] is False, "strict HRG source")
    require(strict_rejection["UP_RET_OVERLAP_HRG_universal_admitted"] is False, "universal admitted")
    require(strict_rejection["lambda_H_predicted"] is False, "lambda prediction")

    require(strict_gate["status"] == "STRICT_GATE_9_OF_10_TWO_SOURCE_OBJECTS_REMAIN", "strict gate status")
    require(strict_gate["strict_selected_K_rows"] == 9, "gate K count")
    require(strict_gate["required_selected_K_rows"] == 10, "gate required")
    require(strict_gate["missing_row"] == "K_threshold.Omega_H.lambda", "gate missing row")
    require(strict_gate["accepted_exit_count"] == 0, "gate exits")
    require(len(strict_gate["remaining_strict_source_objects"]) == 2, "remaining objects")
    require(strict_gate["strict_ten_K_closure"] is False, "gate ten K")
    require(strict_gate["full_no_knob_closed"] is False, "gate no-knob")
    require(strict_gate["true_SM_equivalence_closed"] is False, "gate true SM")

    require(
        next_cutset["status"] == "NEXT_FRONTIER_DIRECT_HK_SOURCE_OR_RG_HESSIAN_TRANSPORT",
        "next cutset status",
    )
    require(next_cutset["next_required_artifact"] == NEXT, "next cutset artifact")
    for phrase in [
        "cycle-break exits executed",
        "universal primitive promotion rejected at current source level",
        "strict frontier reduced from three exits to two source-construction objects",
    ]:
        require(phrase in next_cutset["closed_here"], f"closed missing {phrase}")
    for phrase in [
        "direct source-native K_threshold.Omega_H.lambda",
        "selected large-threshold/RG transport with R_H^RG, A_EW, mu_match, and same-scheme Omega certificate",
        "strict Omega_H.lambda scalar execution after tenth K row emission",
    ]:
        require(phrase in next_cutset["still_open"], f"open missing {phrase}")
    contract = next_cutset["acceptance_contract"]
    for key in [
        "same_branch_q79_F_m1",
        "source_owned_numeric_or_symbolic_value_required",
        "observed_target_selector_forbidden",
        "conditional_ten_K_theorem_trigger_required",
        "Omega_H_lambda_execution_certificate_required",
    ]:
        require(contract[key] is True, f"contract missing {key}")

    for phrase in [
        "TenthHThresholdKRowSourceOrLargeThresholdRGPrimitiveTheorem",
        "Universal primitive cross-use: rejected currently",
        "Strict selected K rows: `9/10`",
        "Controlled empirical selected for no-knob: `false`",
        NEXT,
    ]:
        require(phrase in note, f"note missing {phrase}")

    print(
        "AUDIT_PASS: tenth H K-row route execution locked; universal primitive rejected; two strict exits remain."
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
