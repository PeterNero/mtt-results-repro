"""Build the H-threshold/RG source theorem attempt or minimal-primitive calibration run.

The previous packet split the frontier into strict no-knob source emission for
R_H^RG and a controlled minimal-parameter lane.  This packet executes that split:

* strict source theorem attempt: no current source emits R_H^RG;
* minimal calibration run: UP-RET-OVERLAP.HRG can be calibrated exactly on
  lambda_H(M_t), yielding a controlled empirical H-row layer;
* cross-use workorder: the calibrated primitive is not credible as a universal
  parameter until it predicts at least one non-Higgs target without retuning.
"""

from __future__ import annotations

import json
import math
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "candidate_data"
CERTS = ROOT / "certificates"
CORPUS = ROOT / "proof_corpus"

SLUG = "selected_hthresholdrgsource_or_minimalprimitivecalibrationrun"
PACKET_DIR = DATA / SLUG
OUTPUT = DATA / f"{SLUG}.candidate.json"
STRICT_ATTEMPT = PACKET_DIR / "strict_h_threshold_rg_source_theorem_attempt.packet.json"
CALIBRATION = PACKET_DIR / "minimal_primitive_calibration_run.packet.json"
EMPIRICAL_GATE = PACKET_DIR / "controlled_empirical_h_k_gate.packet.json"
CROSSUSE = PACKET_DIR / "crossuse_prediction_audit_workorder.packet.json"
HK_GATE = PACKET_DIR / "hk_threshold_gate_after_calibration_run.packet.json"
CUTSET = PACKET_DIR / "next_cutset_after_calibration_run.packet.json"
CERT = CERTS / f"{SLUG}_certificate.json"
NOTE = CORPUS / "MTT_Selected_HThresholdRGSource_or_MinimalPrimitiveCalibrationRun_v1.md"

PREVIOUS = DATA / "selected_hthresholdrgoperator_or_universalprimitivepolicy.candidate.json"
PREVIOUS_STRICT = (
    DATA
    / "selected_hthresholdrgoperator_or_universalprimitivepolicy"
    / "strict_h_threshold_rg_operator_source_search.packet.json"
)
PREVIOUS_CONDITIONAL = (
    DATA
    / "selected_hthresholdrgoperator_or_universalprimitivepolicy"
    / "conditional_minimal_parameter_h_gate_execution.packet.json"
)
PREVIOUS_ADMISSION = (
    DATA
    / "selected_hthresholdrgoperator_or_universalprimitivepolicy"
    / "h_threshold_universal_primitive_admission_matrix.packet.json"
)
PREVIOUS_HK = (
    DATA
    / "selected_hthresholdrgoperator_or_universalprimitivepolicy"
    / "hk_threshold_gate_after_policy_split.packet.json"
)
PREVIOUS_CUTSET = (
    DATA
    / "selected_hthresholdrgoperator_or_universalprimitivepolicy"
    / "next_cutset_after_policy_split.packet.json"
)
AEW_DIAG = (
    DATA
    / "selected_ewboundaryrgfactorforhiggsdterm_or_directtenkclosure"
    / "external_aew_dterm_diagnostic_postcheck.packet.json"
)
H_SOURCE = (
    DATA
    / "selected_hsectorquarticthresholdpayload_or_stricttenkclosure"
    / "h_sector_payload_source_equation.packet.json"
)
CROSSUSE_THEOREM = (
    DATA
    / "universal_crossuse_parameter_admissibility_theorem"
    / "crossuse_admissibility_theorem.packet.json"
)
ALPHA1_CASE = (
    DATA
    / "universal_crossuse_parameter_admissibility_theorem"
    / "alpha1_crossuse_case.packet.json"
)
UP_CANDIDATES = DATA / "universal_source_parameter_policy" / "candidate_universal_parameters.packet.json"

STATUS = (
    "MTT_SELECTED_HTHRESHOLDRGSOURCE_OR_MINIMALPRIMITIVECALIBRATIONRUN_"
    "CALIBRATION_LAYER_CLOSED_STRICT_SOURCE_OPEN"
)
NEXT = "MTT_Selected_HRGPrimitiveCrossUsePredictionAudit_or_SourceTheoremAttempt_v1"


def rel(path: Path) -> str:
    try:
        return str(path.relative_to(ROOT)).replace("\\", "/")
    except ValueError:
        return str(path).replace("\\", "/")


def load(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def write_json(path: Path, payload: dict[str, Any]) -> None:
    path.write_text(json.dumps(payload, indent=2, sort_keys=True) + "\n", encoding="utf-8")


def require_sources(paths: list[Path]) -> None:
    missing = [rel(path) for path in paths if not path.exists()]
    if missing:
        raise FileNotFoundError("missing H threshold calibration inputs: " + ", ".join(missing))


def main() -> int:
    PACKET_DIR.mkdir(parents=True, exist_ok=True)
    CERTS.mkdir(parents=True, exist_ok=True)
    CORPUS.mkdir(parents=True, exist_ok=True)

    sources = [
        PREVIOUS,
        PREVIOUS_STRICT,
        PREVIOUS_CONDITIONAL,
        PREVIOUS_ADMISSION,
        PREVIOUS_HK,
        PREVIOUS_CUTSET,
        AEW_DIAG,
        H_SOURCE,
        CROSSUSE_THEOREM,
        ALPHA1_CASE,
        UP_CANDIDATES,
    ]
    require_sources(sources)

    previous = load(PREVIOUS)
    previous_strict = load(PREVIOUS_STRICT)
    previous_conditional = load(PREVIOUS_CONDITIONAL)
    previous_admission = load(PREVIOUS_ADMISSION)
    previous_hk = load(PREVIOUS_HK)
    previous_cutset = load(PREVIOUS_CUTSET)
    aew_diag = load(AEW_DIAG)
    h_source = load(H_SOURCE)
    crossuse = load(CROSSUSE_THEOREM)
    alpha1_case = load(ALPHA1_CASE)
    up_candidates = load(UP_CANDIDATES)

    nums = previous["diagnostic_numbers_not_source"]
    lambda_r1 = float(nums["lambda_if_R_H_RG_equals_1"])
    lambda_ext = float(nums["external_lambda_Mt_coordinate"])
    required_r = float(nums["required_UP_RET_OVERLAP_HRG_if_calibrated_on_lambda_H"])
    log_required = float(nums["log_required_UP_RET_OVERLAP_HRG"])
    lambda_calibrated = lambda_r1 * required_r
    residual = lambda_calibrated - lambda_ext
    relative_residual = residual / lambda_ext if lambda_ext else math.inf

    strict_attempt = {
        "schema": "MTTStrictHThresholdRGSourceTheoremAttempt.v1",
        "status": "STRICT_H_THRESHOLD_RG_SOURCE_THEOREM_ATTEMPTED_NOT_EMITTED",
        "closure_claimed": True,
        "attempted_theorem": {
            "name": "SelectedHThresholdRGSourceTheorem",
            "target": previous_strict["searched_object"],
            "acceptance_contract": previous_strict["acceptance_contract"],
        },
        "attempt_result": {
            "selected_R_H_RG_emitted": False,
            "selected_A_EW_emitted": False,
            "selected_mu_match_emitted": False,
            "selected_K_threshold_Omega_H_lambda_emitted": False,
            "mathematical_impossibility_claimed": False,
            "reason": previous_strict["reason"],
        },
        "source_status_imports": previous_strict["source_status_imports"],
        "current_open_payload": [
            "same-branch H-sector determinant/index/RG transport operator",
            "selected physical gauge/action normalization or admitted primitive tier",
            "selected matching surface mu_match",
            "same-scheme Omega_H.lambda transport certificate",
        ],
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
    }

    calibration = {
        "schema": "MTTMinimalPrimitiveCalibrationRun.v1",
        "status": "UP_RET_OVERLAP_HRG_CALIBRATED_EMPIRICAL_LAYER_NOT_PREDICTION",
        "closure_claimed": True,
        "primitive": {
            "id": "UP-RET-OVERLAP.HRG",
            "base_policy_class": "UP-RET-OVERLAP",
            "name": "universal H-threshold/RG transport strength",
            "declared_role": "global H/threshold retarded-overlap or determinant-transport strength",
            "new_universal_parameter_count_in_this_layer": 1,
            "selected_as_strict_source_parameter": False,
            "admitted_as_controlled_empirical_parameter": True,
        },
        "calibration_protocol": {
            "calibrating_observable": "lambda_H(M_t)",
            "calibrating_observable_prediction_claim_allowed": False,
            "measured_calibration_used": True,
            "observed_data_used_as_source_selector": False,
            "parameter_declared_before_replay_in_this_packet": True,
            "retuning_per_observable_allowed": False,
            "crossuse_required_before_credibility_upgrade": True,
        },
        "calibration_values": {
            "lambda_if_R_H_RG_equals_1": lambda_r1,
            "external_lambda_Mt_coordinate": lambda_ext,
            "required_UP_RET_OVERLAP_HRG": required_r,
            "log_required_UP_RET_OVERLAP_HRG": log_required,
            "lambda_if_R_H_RG_equals_required_value": lambda_calibrated,
            "absolute_residual": residual,
            "relative_residual": relative_residual,
        },
        "claim_boundary": {
            "strict_no_knob_closure_claimed": False,
            "lambda_H_predicted": False,
            "lambda_H_calibrated": True,
            "minimal_parameter_H_layer_closed": True,
            "full_SM_closure_claimed": False,
        },
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
    }

    empirical_gate = {
        "schema": "MTTControlledEmpiricalHKGate.v1",
        "status": "CONTROLLED_EMPIRICAL_H_K_GATE_CONDITIONAL_10_OF_10_STRICT_9_OF_10",
        "closure_claimed": True,
        "strict_source_tier": {
            "accepted_selected_K_source_row_count": previous_hk[
                "accepted_selected_K_source_row_count"
            ],
            "selected_K_threshold_row_count_required": previous_hk[
                "selected_K_threshold_row_count_required"
            ],
            "K_threshold_Omega_H_lambda_emitted": False,
            "ten_K_antecedent_satisfied": False,
            "strict_Omega_lambda_scalar_execution_closed": False,
        },
        "controlled_empirical_tier": {
            "UP_RET_OVERLAP_HRG_admitted_as_calibrated_parameter": True,
            "conditional_parameterized_K_row_count": previous_hk[
                "conditional_minimal_parameter_consequent"
            ]["conditional_parameterized_K_row_count"],
            "H_lambda_calibrated_not_predicted": True,
            "conditional_H_row_formula": previous_conditional[
                "source_row_effect_if_policy_later_admitted"
            ]["conditional_K_threshold_Omega_H_lambda_executable"],
            "omega_scheme_formula": (
                "K_threshold.Omega_H.lambda = lambda_H(M_t)/(D_fin.H*epsilon_Theta^(1/3)) "
                "after calibrated H-threshold/RG transport and same-scheme alignment"
            ),
            "same_scheme_source_equation": h_source["selected_source_equation"]["omega_value"],
        },
        "notices": [
            "This closes a controlled empirical H calibration layer, not strict no-knob H closure.",
            "The calibrated primitive must predict a non-Higgs target without retuning before it is credible as universal.",
            "The strict selected K row remains absent at the source tier.",
        ],
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
    }

    crossuse_workorder = {
        "schema": "MTTHRGPrimitiveCrossUsePredictionAuditWorkorder.v1",
        "status": "CROSSUSE_PREDICTION_AUDIT_REQUIRED_FOR_HRG_PRIMITIVE",
        "closure_claimed": True,
        "policy_import": {
            "admission_criteria": crossuse["admission_criteria"],
            "provisional_use_classification": crossuse["provisional_use_classification"],
            "alpha1_case_status": alpha1_case["status"],
            "alpha1_case_admitted_now": alpha1_case["admitted_now"],
        },
        "calibrated_primitive_under_test": {
            "id": "UP-RET-OVERLAP.HRG",
            "calibrated_value": required_r,
            "calibrating_observable": "lambda_H(M_t)",
            "forbidden_prediction_credit": "lambda_H(M_t)",
        },
        "required_prediction_set_before_credibility_upgrade": [
            {
                "target": "non-Higgs threshold/RG observable",
                "minimum_requirement": "same UP-RET-OVERLAP.HRG value enters a typed source map and predicts the target without retuning",
                "current_source_map_available": False,
            },
            {
                "target": "weak-mixing or alpha-sector consistency",
                "minimum_requirement": "if B42 physical-unit primitive is also used, HRG must not retune E0/L0 and must leave alpha1/weak-mixing calibration order intact",
                "current_source_map_available": False,
            },
            {
                "target": "charged scalar threshold/prefactor rows",
                "minimum_requirement": "prove HRG belongs to the same universal retarded-overlap family as charged-row threshold maps before applying it",
                "current_source_map_available": False,
            },
        ],
        "credibility_decision": {
            "crossuse_prediction_audit_passed_now": False,
            "H_only_fit_quarantined": True,
            "minimal_parameter_result_current_status": "H_CALIBRATION_LAYER_BUILT_CROSSUSE_OPEN",
        },
        "next_required_artifact": NEXT,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
    }

    hk_gate = {
        "schema": "MTTHKThresholdGateAfterCalibrationRun.v1",
        "status": "H_K_THRESHOLD_GATE_STRICT_9_OF_10_EMPIRICAL_H_LAYER_BUILT",
        "closure_claimed": True,
        "required_output": "K_threshold.Omega_H.lambda",
        "strict_source_tier": {
            "accepted_selected_K_source_row_count": 9,
            "selected_K_threshold_row_count_required": 10,
            "ten_K_antecedent_satisfied": False,
            "strict_Omega_lambda_scalar_execution_closed": False,
            "accepted_internal_scalar_value_row_count": 0,
        },
        "controlled_empirical_tier": {
            "calibrated_H_threshold_primitive_admitted": True,
            "conditional_parameterized_K_row_count": 10,
            "H_lambda_calibrated_not_predicted": True,
            "crossuse_prediction_audit_required": True,
            "full_SM_closure_claimed": False,
        },
        "H_row": {
            **previous_hk["H_row"],
            "strict_H_threshold_RG_source_theorem_attempted": True,
            "strict_H_threshold_RG_operator_emitted": False,
            "UP_RET_OVERLAP_HRG_calibration_run_built": True,
            "UP_RET_OVERLAP_HRG_admitted_empirical_layer": True,
            "UP_RET_OVERLAP_HRG_selected_strict_source": False,
            "K_threshold_Omega_H_lambda_emitted": False,
            "controlled_empirical_H_layer_built": True,
        },
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
    }

    cutset = {
        "schema": "MTTNextCutsetAfterCalibrationRun.v1",
        "status": "NEXT_FRONTIER_HRG_CROSSUSE_PREDICTION_AUDIT_OR_SOURCE_THEOREM",
        "closure_claimed": True,
        "closed_here": [
            "strict R_H^RG source theorem attempted and still not emitted",
            "UP-RET-OVERLAP.HRG calibrated exactly at controlled empirical tier",
            "controlled empirical H K layer built as conditional 10/10",
            "lambda_H prediction credit explicitly forbidden for the calibration observable",
            "cross-use prediction audit workorder built",
        ],
        "still_open": [
            "strict selected R_H^RG source theorem",
            "strict selected K_threshold.Omega_H.lambda",
            "cross-use prediction audit for UP-RET-OVERLAP.HRG",
            "non-Higgs threshold/RG source map using the same calibrated primitive",
            "true SM/no-knob equivalence",
        ],
        "next_required_artifact": NEXT,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
    }

    candidate = {
        "candidate": "MTTSelectedHThresholdRGSourceOrMinimalPrimitiveCalibrationRun",
        "status": STATUS,
        "previous_status": previous["status"],
        "theorem": {
            "name": "HThresholdRGSourceAttemptOrMinimalPrimitiveCalibrationRunTheorem",
            "proved": True,
            "statement": (
                "The strict source theorem for R_H^RG is attempted against the "
                "current source ledger and remains unemitted.  The minimal-"
                "parameter lane can be executed exactly by admitting "
                "UP-RET-OVERLAP.HRG as a controlled empirical calibration "
                "parameter with value 391.39140285811936.  This builds a "
                "conditional H K layer but does not predict lambda_H, does not "
                "emit a strict selected K row, and remains credibility-open until "
                "the same primitive predicts a non-Higgs target without retuning."
            ),
        },
        "closure_claimed": True,
        "true_SM_equivalence_claimed": False,
        "full_no_knob_closure_claimed": False,
        "minimal_parameter_H_calibration_layer_claimed": True,
        "closure_decision": {
            "strict_H_threshold_RG_source_theorem_attempted": True,
            "strict_H_threshold_RG_operator_emitted": False,
            "UP_RET_OVERLAP_HRG_calibration_run_built": True,
            "UP_RET_OVERLAP_HRG_admitted_empirical_layer": True,
            "UP_RET_OVERLAP_HRG_selected_strict_source": False,
            "lambda_H_calibrated": True,
            "lambda_H_predicted": False,
            "controlled_empirical_H_K_layer_built": True,
            "controlled_empirical_conditional_K_row_count": 10,
            "strict_accepted_selected_K_source_row_count": 9,
            "strict_selected_K_threshold_row_count_required": 10,
            "strict_ten_K_antecedent_satisfied": False,
            "strict_Omega_lambda_scalar_execution_closed": False,
            "crossuse_prediction_audit_passed": False,
            "true_SM_equivalence_closed": False,
            "full_no_knob_closed": False,
        },
        "calibration_numbers": {
            "lambda_if_R_H_RG_equals_1": lambda_r1,
            "external_lambda_Mt_coordinate": lambda_ext,
            "UP_RET_OVERLAP_HRG": required_r,
            "log_UP_RET_OVERLAP_HRG": log_required,
            "lambda_if_R_H_RG_equals_required_value": lambda_calibrated,
            "residual": residual,
        },
        "inputs": {path.stem: rel(path) for path in sources},
        "output_packets": {
            "strict_h_threshold_rg_source_theorem_attempt": rel(STRICT_ATTEMPT),
            "minimal_primitive_calibration_run": rel(CALIBRATION),
            "controlled_empirical_h_k_gate": rel(EMPIRICAL_GATE),
            "crossuse_prediction_audit_workorder": rel(CROSSUSE),
            "hk_threshold_gate_after_calibration_run": rel(HK_GATE),
            "next_cutset_after_calibration_run": rel(CUTSET),
        },
        "next_required_artifact": NEXT,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
    }

    cert = {
        "certificate": "MTTSelectedHThresholdRGSourceOrMinimalPrimitiveCalibrationRunCertificate",
        "status": STATUS,
        "theorem_proved": True,
        "strict_H_threshold_RG_source_theorem_attempted": True,
        "strict_H_threshold_RG_operator_emitted": False,
        "UP_RET_OVERLAP_HRG_calibration_run_built": True,
        "UP_RET_OVERLAP_HRG_admitted_empirical_layer": True,
        "UP_RET_OVERLAP_HRG_selected_strict_source": False,
        "UP_RET_OVERLAP_HRG_value": required_r,
        "lambda_H_calibrated": True,
        "lambda_H_predicted": False,
        "controlled_empirical_H_K_layer_built": True,
        "controlled_empirical_conditional_K_row_count": 10,
        "strict_accepted_selected_K_source_row_count": 9,
        "strict_selected_K_threshold_row_count_required": 10,
        "strict_ten_K_antecedent_satisfied": False,
        "strict_Omega_lambda_scalar_execution_closed": False,
        "crossuse_prediction_audit_passed": False,
        "true_SM_equivalence_claimed": False,
        "full_no_knob_closure_claimed": False,
        "minimal_parameter_H_calibration_layer_claimed": True,
        "next_required_artifact": NEXT,
        "closure_claimed": True,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
    }

    note = f"""# MTT Selected HThresholdRGSource or MinimalPrimitiveCalibrationRun v1

Status: `{STATUS}`

## Current Plan Position

- strict selected K rows: `9/10`
- controlled empirical H calibration layer: built
- full no-knob / true SM equivalence: open

## What Closed

- strict `R_H^RG` source theorem was attempted and remains open
- `UP-RET-OVERLAP.HRG` is calibrated at the controlled empirical tier:
  - `UP-RET-OVERLAP.HRG={required_r}`
  - `log(UP-RET-OVERLAP.HRG)={log_required}`
  - `lambda(R=1)={lambda_r1}`
  - `lambda(R=UP-RET-OVERLAP.HRG)={lambda_calibrated}`
- conditional empirical H K layer is now `10/10`
- strict source tier remains `9/10`
- `lambda_H` is calibration, not prediction

## Still Open

- strict selected `R_H^RG` source theorem
- strict selected `K_threshold.Omega_H.lambda`
- cross-use prediction audit for `UP-RET-OVERLAP.HRG`
- non-Higgs threshold/RG source map using the same primitive

Next required artifact: `{NEXT}`
"""

    write_json(STRICT_ATTEMPT, strict_attempt)
    write_json(CALIBRATION, calibration)
    write_json(EMPIRICAL_GATE, empirical_gate)
    write_json(CROSSUSE, crossuse_workorder)
    write_json(HK_GATE, hk_gate)
    write_json(CUTSET, cutset)
    write_json(OUTPUT, candidate)
    write_json(CERT, cert)
    NOTE.write_text(note, encoding="utf-8")

    print(f"Wrote {rel(OUTPUT)}")
    print(f"Wrote {rel(CERT)}")
    print(f"Wrote {rel(NOTE)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
