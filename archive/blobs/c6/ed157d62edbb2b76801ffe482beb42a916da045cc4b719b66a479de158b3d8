"""Audit Higgs shared-metrology handoff / HRG source reentry theorem gates."""

from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SLUG = "selected_higgssharedmetrologyprimitivehandoff_or_hrgsourcetheoremreentry"
BASE = ROOT / "candidate_data" / SLUG
CANDIDATE = ROOT / "candidate_data" / f"{SLUG}.candidate.json"
CERT = ROOT / "certificates" / f"{SLUG}_certificate.json"
NOTE = ROOT / "proof_corpus" / "MTT_Selected_HiggsSharedMetrologyPrimitiveHandoff_or_HRGSourceTheoremReentry_v1.md"
BUILD = ROOT / "scripts" / f"build_{SLUG}.py"

METROLOGY_HANDOFF = BASE / "higgs_shared_metrology_handoff_theorem.packet.json"
HRG_REENTRY = BASE / "hrg_source_admission_reentry_theorem.packet.json"
ROUTE_MATRIX = BASE / "two_route_frontier_execution_matrix.packet.json"
CUTSET = BASE / "next_cutset_after_handoff_reentry.packet.json"

STATUS = (
    "MTT_SELECTED_HIGGSSHAREDMETROLOGYPRIMITIVEHANDOFF_OR_HRGSOURCETHEOREMREENTRY_"
    "THEOREM_GATES_BUILT_VALUES_OPEN"
)
NEXT = "MTT_Selected_AEWMetrologySlotExecution_or_HRGNonHiggsPredictionSelector_v1"
S_BETA = 0.004701083905943647
HRG = 391.39140285811936
LOG_HRG = 5.969708089616292


def load(path: Path):
    return json.loads(path.read_text(encoding="utf-8"))


def require(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)


def main() -> int:
    proc = subprocess.run([sys.executable, str(BUILD)], cwd=ROOT, text=True, capture_output=True)
    if proc.returncode:
        print(proc.stdout)
        print(proc.stderr)
        return proc.returncode

    candidate = load(CANDIDATE)
    cert = load(CERT)
    metrology = load(METROLOGY_HANDOFF)
    hrg = load(HRG_REENTRY)
    route_matrix = load(ROUTE_MATRIX)
    cutset = load(CUTSET)
    note = NOTE.read_text(encoding="utf-8")

    require(candidate["status"] == STATUS, "candidate status")
    require(candidate["next_required_artifact"] == NEXT, "candidate next")
    require(candidate["closure_claimed"] is True, "candidate closure")
    require(candidate["true_SM_equivalence_claimed"] is False, "true SM overclaim")
    require(candidate["full_no_knob_closure_claimed"] is False, "no-knob overclaim")
    require(candidate["observed_data_used_as_selector"] is False, "observed selector")
    require(candidate["target_fitting_used"] is False, "target fitting")
    require(len(candidate["theorems"]) == 2, "two theorems")
    require(
        candidate["theorems"][0]["name"] == "HiggsSharedMetrologyPrimitiveHandoffDomainTheorem",
        "metrology theorem name",
    )
    require(candidate["theorems"][0]["proved"] is True, "metrology theorem proved")
    require(
        candidate["theorems"][1]["name"] == "HRGSourceAdmissionReentryPredicateTheorem",
        "HRG theorem name",
    )
    require(candidate["theorems"][1]["proved"] is True, "HRG theorem proved")

    decision = candidate["closure_decision"]
    for key in [
        "higgs_metrology_handoff_domain_closed",
        "HRG_source_admission_predicate_closed",
        "A_EW_slot_legal_for_UP_ABS_SCALE",
        "mu_match_slot_legal_for_UP_ABS_SCALE",
        "threshold_RG_scheme_slot_legal_for_UP_ABS_SCALE",
        "RO_family_selector_selected",
    ]:
        require(decision[key] is True, f"decision true {key}")
    for key in [
        "UP_ABS_SCALE_closes_HRG_now",
        "selected_A_EW_value_emitted_now",
        "selected_mu_match_value_emitted_now",
        "selected_threshold_RG_transport_emitted_now",
        "K_threshold_Omega_H_lambda_emitted_now",
        "RO_value_source_selected",
        "strict_R_H_RG_source_emitted",
        "same_HRG_nonHiggs_map_accepted",
        "UP_RET_OVERLAP_HRG_universal_admitted",
        "current_HRG_reentry_gate_satisfied",
        "true_SM_equivalence_closed",
        "full_no_knob_closed",
    ]:
        require(decision[key] is False, f"decision false {key}")

    nums = candidate["key_numbers"]
    require(abs(nums["s_beta"] - S_BETA) < 1e-18, "s_beta")
    require(abs(nums["UP_RET_OVERLAP_HRG"] - HRG) < 1e-12, "HRG")
    require(abs(nums["log_UP_RET_OVERLAP_HRG"] - LOG_HRG) < 1e-12, "log HRG")
    require(nums["allowed_metrology_slot_count"] == 3, "metrology slot count")
    require(nums["selected_metrology_value_slot_count_now"] == 0, "selected slot count")
    require(nums["strict_H_K_rows"] == 9, "strict H rows")
    require(nums["required_H_K_rows"] == 10, "required H rows")
    require(nums["controlled_empirical_conditional_K_rows"] == 10, "empirical H rows")
    require(nums["accepted_HRG_nonHiggs_map_count"] == 0, "HRG non-Higgs count")

    require(cert["status"] == STATUS, "cert status")
    require(cert["next_required_artifact"] == NEXT, "cert next")
    for key in [
        "higgs_metrology_handoff_domain_closed",
        "HRG_source_admission_predicate_closed",
        "A_EW_slot_legal_for_UP_ABS_SCALE",
        "mu_match_slot_legal_for_UP_ABS_SCALE",
        "threshold_RG_scheme_slot_legal_for_UP_ABS_SCALE",
        "RO_family_selector_selected",
    ]:
        require(cert[key] is True, f"cert true {key}")
    for key in [
        "UP_ABS_SCALE_closes_HRG_now",
        "selected_A_EW_value_emitted_now",
        "selected_mu_match_value_emitted_now",
        "selected_threshold_RG_transport_emitted_now",
        "K_threshold_Omega_H_lambda_emitted_now",
        "RO_value_source_selected",
        "strict_R_H_RG_source_emitted",
        "same_HRG_nonHiggs_map_accepted",
        "UP_RET_OVERLAP_HRG_universal_admitted",
        "current_HRG_reentry_gate_satisfied",
        "true_SM_equivalence_claimed",
        "full_no_knob_closure_claimed",
        "observed_data_used_as_selector",
        "target_fitting_used",
    ]:
        require(cert[key] is False, f"cert false {key}")

    require(metrology["status"] == "HIGGS_SHARED_METROLOGY_HANDOFF_THEOREM_BUILT_VALUES_OPEN", "metrology status")
    require(metrology["theorem"]["proved"] is True, "metrology theorem")
    require(metrology["selected_inputs"]["s_beta_selected"] is True, "s_beta selected")
    require(abs(metrology["selected_inputs"]["s_beta"] - S_BETA) < 1e-18, "metrology s_beta")
    require(metrology["slot_counts"]["allowed_metrology_slot_count"] == 3, "allowed slots")
    require(metrology["slot_counts"]["selected_metrology_value_slot_count_now"] == 0, "selected slots")
    require(metrology["slot_counts"]["prohibited_silent_merge_slot_count"] == 3, "prohibited slots")
    for row in metrology["allowed_metrology_slots"]:
        require(row["may_receive_UP_ABS_SCALE"] is True, f"allowed slot {row['slot']}")
        require(row["source_selected_now"] is False, f"slot selected {row['slot']}")
        require(row["emits_H_K_row_now"] is False, f"slot emits H row {row['slot']}")
    for row in metrology["prohibited_metrology_slots"]:
        require(row["may_receive_UP_ABS_SCALE"] is False, f"prohibited slot {row['slot']}")
    met_decision = metrology["decision"]
    require(met_decision["higgs_metrology_handoff_domain_closed"] is True, "met decision closed")
    require(met_decision["UP_ABS_SCALE_closes_HRG_now"] is False, "met closes HRG")
    require(met_decision["lambda_H_prediction_credit_from_metrology_now"] is False, "met lambda credit")

    require(hrg["status"] == "HRG_SOURCE_ADMISSION_REENTRY_PREDICATE_BUILT_NOT_SATISFIED", "HRG status")
    require(hrg["theorem"]["proved"] is True, "HRG theorem")
    predicate = hrg["admission_predicate"]
    require(predicate["strict_source_lane"]["satisfied_now"] is False, "strict lane")
    require(predicate["universal_parameter_lane"]["satisfied_now"] is False, "universal lane")
    require(predicate["family_class_lane"]["satisfied_now"] is False, "family lane")
    require(predicate["family_class_lane"]["family_selector_selected_now"] is True, "family selected")
    require(predicate["family_class_lane"]["numeric_value_source_selected_now"] is False, "numeric source")
    value_status = hrg["current_value_status"]
    require(abs(value_status["UP_RET_OVERLAP_HRG"] - HRG) < 1e-12, "HRG value")
    require(value_status["empirical_value_available"] is True, "empirical value")
    require(value_status["lambda_H_calibrated"] is True, "lambda calibrated")
    require(value_status["lambda_H_predicted"] is False, "lambda predicted")
    require(value_status["strict_source_selected_now"] is False, "strict source")
    require(value_status["nonHiggs_accepted_crossuse_map_count"] == 0, "crossuse maps")
    hrg_decision = hrg["decision"]
    require(hrg_decision["HRG_source_admission_predicate_closed"] is True, "HRG predicate")
    require(hrg_decision["RO_family_selector_selected"] is True, "HRG family")
    for key in [
        "RO_value_source_selected",
        "strict_R_H_RG_source_emitted",
        "UP_RET_OVERLAP_HRG_universal_admitted",
        "same_HRG_nonHiggs_map_accepted",
        "nonHiggs_prediction_passed",
        "lambda_H_prediction_credit_allowed",
        "current_HRG_reentry_gate_satisfied",
    ]:
        require(hrg_decision[key] is False, f"HRG false {key}")

    require(route_matrix["status"] == "TWO_ROUTE_FRONTIER_EXECUTION_MATRIX_BUILT", "route status")
    require(len(route_matrix["route_rows"]) == 4, "route count")
    for row in route_matrix["route_rows"]:
        require(row["theorem_gate_built"] is True, f"route theorem {row['route']}")
        require(row["value_source_ready_now"] is False, f"route ready {row['route']}")
    require(route_matrix["decision"]["theorem_gates_built"] is True, "route gates")
    require(route_matrix["decision"]["selected_value_route_closed_now"] is False, "route closed")
    require(route_matrix["decision"]["loop_back_to_silent_HRG_metrology_identity_allowed"] is False, "route loop")

    require(cutset["status"] == "NEXT_FRONTIER_AEW_METROLOGY_SLOT_EXECUTION_OR_HRG_NONHIGGS_SELECTOR", "cutset")
    require(cutset["next_required_artifact"] == NEXT, "cutset next")
    for phrase in [
        "Higgs shared-metrology handoff domain theorem built",
        "HRG source/admission reentry predicate built",
        "next execution matrix reduced to metrology-slot execution or HRG non-Higgs prediction selector",
    ]:
        require(phrase in cutset["closed_here"], f"closed missing {phrase}")
    for phrase in [
        "selected A_EW value",
        "selected mu_match value",
        "selected threshold/RG transport into Omega/lambda_H scheme",
        "same-value non-Higgs prediction map for UP-RET-OVERLAP.HRG",
        "true SM/no-knob equivalence",
    ]:
        require(phrase in cutset["still_open"], f"open missing {phrase}")

    for phrase in [
        "Higgs Shared Metrology Handoff Domain Theorem",
        "HRG Source Admission Reentry Predicate Theorem",
        "RO.family_selector selected   true",
        "RO.value_source selected      false",
        NEXT,
    ]:
        require(phrase in note, f"note missing {phrase}")

    print(
        "AUDIT_PASS: Higgs metrology handoff and HRG reentry predicates are built; "
        "A_EW/mu/RG values and HRG non-Higgs prediction remain open."
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
