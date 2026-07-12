"""Audit selected H/lambda overlap-kernel row or scalar Omega gate."""

from __future__ import annotations

import json
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SLUG = "selected_hlambdaoverlapkernelrow_or_scalaromegaexecutiongate"
DATA = ROOT / "candidate_data" / f"{SLUG}.candidate.json"
PACKET_DIR = ROOT / "candidate_data" / SLUG
STRICT = PACKET_DIR / "strict_hlambda_overlap_kernel_gate.packet.json"
CONTROLLED = PACKET_DIR / "controlled_one_parameter_scalar_gate.packet.json"
TIER = PACKET_DIR / "strict_vs_controlled_tier_separation.packet.json"
CUTSET = PACKET_DIR / "next_cutset_after_hlambda_scalar_gate.packet.json"
CERT = ROOT / "certificates" / f"{SLUG}_certificate.json"
NOTE = ROOT / "proof_corpus" / "MTT_Selected_HLambdaOverlapKernelRow_or_ScalarOmegaExecutionGate_v1.md"
STATUS = "MTT_SELECTED_HLAMBDAOVERLAPKERNELROW_OR_SCALAROMEGAEXECUTIONGATE_STRICT_9OF10_CONTROLLED_ONE_PARAMETER_10OF10_BUILT"
NEXT = "MTT_Selected_HRGPrimitiveCrossUsePredictionAudit_or_StrictHSourceTheorem_v1"


def load(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def require(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)


def main() -> int:
    data = load(DATA)
    strict = load(STRICT)
    controlled = load(CONTROLLED)
    tier = load(TIER)
    cutset = load(CUTSET)
    cert = load(CERT)
    note = NOTE.read_text(encoding="utf-8")

    require(data["status"] == STATUS, "candidate status mismatch")
    require(cert["status"] == STATUS, "certificate status mismatch")
    require(data["closure_claimed"] is True, "closure flag missing")
    require(data["full_no_knob_closure_claimed"] is False, "no-knob overclaimed")
    require(data["true_SM_equivalence_claimed"] is False, "true SM overclaimed")
    require(data["observed_data_used_as_selector"] is False, "observed selector")
    require(data["target_fitting_used"] is False, "target fitting")
    require(data["next_required_artifact"] == NEXT, "candidate next")
    require(cert["next_required_artifact"] == NEXT, "cert next")

    decision = data["closure_decision"]
    require(decision["strict_selected_charged_overlap_row_count"] == 9, "charged count")
    require(decision["strict_selected_K_source_row_count"] == 9, "strict K count")
    require(decision["strict_selected_K_source_row_count_required"] == 10, "required K count")
    require(decision["strict_selected_H_lambda_overlap_kernel_row_emitted"] is False, "H row overemitted")
    require(decision["strict_selected_K_threshold_Omega_H_lambda_emitted"] is False, "H K overemitted")
    require(decision["strict_Omega_lambda_scalar_execution_closed"] is False, "strict scalar overclosed")
    require(decision["controlled_one_parameter_H_layer_built"] is True, "controlled layer missing")
    require(decision["controlled_parameter_id"] == "UP-RET-OVERLAP.HRG", "controlled id")
    require(decision["controlled_parameterized_K_row_count"] == 10, "controlled K count")
    require(decision["lambda_H_calibrated"] is True, "lambda calibration missing")
    require(decision["lambda_H_predicted"] is False, "lambda prediction overclaimed")
    require(decision["crossuse_prediction_audit_passed"] is False, "crossuse overclaimed")
    require(decision["full_no_knob_closed"] is False, "full no-knob overclosed")
    require(decision["true_SM_equivalence_closed"] is False, "true SM overclosed")

    require(strict["status"] == "STRICT_HLAMBDA_OVERLAP_KERNEL_ROW_STILL_OPEN_AFTER_CHARGED_ROWS", "strict status")
    require(strict["strict_selected_charged_overlap_row_count"] == 9, "strict charged rows")
    require(strict["strict_selected_K_source_row_count"] == 9, "strict K rows")
    require(strict["strict_selected_K_source_row_count_required"] == 10, "strict required")
    require(strict["selected_H_lambda_overlap_kernel_row_emitted"] is False, "strict H row")
    require(strict["selected_K_threshold_Omega_H_lambda_emitted"] is False, "strict H K")
    require(strict["accepted_internal_scalar_value_row_count"] == 0, "strict scalar rows")
    require(strict["strict_Omega_lambda_scalar_execution_closed"] is False, "strict scalar closure")
    require(strict["strict_no_knob_closure_claimed"] is False, "strict no-knob")

    require(
        controlled["status"] == "CONTROLLED_ONE_PARAMETER_H_LAYER_BUILDS_PARAMETERIZED_10OF10_NOT_NOKNOB",
        "controlled status",
    )
    require(controlled["controlled_empirical_tier_available"] is True, "controlled available")
    require(controlled["minimal_parameter_H_calibration_layer_claimed"] is True, "minimal layer")
    require(controlled["primitive_id"] == "UP-RET-OVERLAP.HRG", "primitive id")
    require(controlled["new_universal_parameter_count"] == 1, "parameter count")
    require(controlled["calibrating_observable"] == "lambda_H(M_t)", "calibrating observable")
    require(controlled["lambda_H_calibrated"] is True, "lambda calibrated")
    require(controlled["lambda_H_predicted"] is False, "lambda predicted")
    require(controlled["conditional_parameterized_K_row_count"] == 10, "controlled K")
    require(controlled["strict_no_knob_claim_allowed"] is False, "controlled no-knob")
    require(controlled["true_SM_equivalence_claimed"] is False, "controlled true SM")
    require(controlled["crossuse_prediction_audit_required"] is True, "crossuse required")
    require(controlled["crossuse_prediction_audit_passed"] is False, "crossuse passed")
    require("(1.193869931683266) / D_fin.H" in controlled["controlled_empirical_H_K_symbolic"], "H symbolic")

    require(tier["status"] == "STRICT_AND_CONTROLLED_HLAMBDA_TIERS_SEPARATED", "tier status")
    require(tier["strict_tier"]["selected_K_rows"] == 9, "tier strict rows")
    require(tier["strict_tier"]["required_K_rows"] == 10, "tier strict required")
    require(tier["strict_tier"]["H_lambda_row_selected"] is False, "tier H row")
    require(tier["strict_tier"]["scalar_execution_closed"] is False, "tier scalar")
    require(tier["controlled_one_parameter_tier"]["declared_parameter_count"] == 1, "tier params")
    require(tier["controlled_one_parameter_tier"]["conditional_K_rows"] == 10, "tier controlled K")
    require(tier["controlled_one_parameter_tier"]["lambda_H_is_calibration"] is True, "tier calibration")
    require(tier["controlled_one_parameter_tier"]["lambda_H_prediction_credit_allowed"] is False, "tier prediction")
    require(len(tier["credibility_upgrade_requirements"]) >= 3, "tier requirements")

    require(cutset["next_required_artifact"] == NEXT, "cutset next")
    for phrase in [
        "strict H/lambda gate reconciled after nine charged overlap rows",
        "controlled one-parameter H layer imported into current frontier",
        "parameterized controlled 10/10 K gate recorded separately from strict no-knob tier",
        "lambda_H calibration/prediction boundary locked",
    ]:
        require(phrase in cutset["closed_here"], f"closed missing {phrase}")
    for phrase in [
        "strict selected H/lambda overlap-kernel row",
        "strict selected R_H^RG or H quartic/threshold source theorem",
        "cross-use prediction audit for UP-RET-OVERLAP.HRG",
        "non-Higgs threshold/RG prediction using the same calibrated primitive",
        "strict Omega/lambda_H scalar execution",
        "true SM equivalence",
    ]:
        require(phrase in cutset["still_open"], f"open missing {phrase}")

    for phrase in [
        "selected charged overlap-kernel rows: `9`",
        "selected strict `K_threshold` rows: `9`",
        "required `K_threshold` rows: `10`",
        "controlled `K_threshold` count: `10`",
        "`lambda_H` is calibration, not prediction: `true`",
        "(1.193869931683266) / D_fin.H",
        NEXT,
    ]:
        require(phrase in note, f"note missing {phrase}")

    print(f"PASS {DATA.name}: {STATUS}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
