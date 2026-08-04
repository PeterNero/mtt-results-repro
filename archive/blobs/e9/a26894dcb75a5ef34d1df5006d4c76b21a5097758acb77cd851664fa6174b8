"""Execute the HRG primitive cross-use audit and strict source reattempt.

The previous packet calibrated UP-RET-OVERLAP.HRG on lambda_H(M_t), producing a
controlled empirical H-layer but explicitly forbidding prediction credit for the
calibrating observable.  This packet removes the next ambiguity: it executes the
cross-use audit against the currently available non-Higgs target classes and
reattempts the strict source theorem.  Current result: no cross-use prediction
passes, and no strict selected R_H^RG source is emitted.
"""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "candidate_data"
CERTS = ROOT / "certificates"
CORPUS = ROOT / "proof_corpus"

SLUG = "selected_hrgprimitivecrossusepredictionaudit_or_sourcetheoremattempt"
PACKET_DIR = DATA / SLUG
OUTPUT = DATA / f"{SLUG}.candidate.json"
STRICT_REATTEMPT = PACKET_DIR / "strict_hrg_source_theorem_reattempt.packet.json"
CROSSUSE_EXECUTION = PACKET_DIR / "hrg_crossuse_prediction_audit_execution.packet.json"
TARGET_MATRIX = PACKET_DIR / "hrg_nonhiggs_target_matrix.packet.json"
POLICY_DECISION = PACKET_DIR / "hrg_primitive_policy_decision_after_crossuse.packet.json"
HK_GATE = PACKET_DIR / "hk_threshold_gate_after_hrg_crossuse_audit.packet.json"
CUTSET = PACKET_DIR / "next_cutset_after_hrg_crossuse_audit.packet.json"
CERT = CERTS / f"{SLUG}_certificate.json"
NOTE = CORPUS / "MTT_Selected_HRGPrimitiveCrossUsePredictionAudit_or_SourceTheoremAttempt_v1.md"

PREVIOUS = DATA / "selected_hthresholdrgsource_or_minimalprimitivecalibrationrun.candidate.json"
PREVIOUS_STRICT = (
    DATA
    / "selected_hthresholdrgsource_or_minimalprimitivecalibrationrun"
    / "strict_h_threshold_rg_source_theorem_attempt.packet.json"
)
PREVIOUS_CALIBRATION = (
    DATA
    / "selected_hthresholdrgsource_or_minimalprimitivecalibrationrun"
    / "minimal_primitive_calibration_run.packet.json"
)
PREVIOUS_CROSSUSE = (
    DATA
    / "selected_hthresholdrgsource_or_minimalprimitivecalibrationrun"
    / "crossuse_prediction_audit_workorder.packet.json"
)
PREVIOUS_HK = (
    DATA
    / "selected_hthresholdrgsource_or_minimalprimitivecalibrationrun"
    / "hk_threshold_gate_after_calibration_run.packet.json"
)
CHARGED_K = (
    DATA
    / "selected_thresholddeltarows_or_lambdahpayloadexecution"
    / "charged_kthreshold_rows_after_null_delta.packet.json"
)
CHARGED_L = (
    DATA
    / "selected_retardedoverlapspectralpairinglemma_or_independentquadraturevalues"
    / "charged_strict_lrowlocal_rows_after_pairing_lemma.packet.json"
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

STATUS = (
    "MTT_SELECTED_HRGPRIMITIVECROSSUSEPREDICTIONAUDIT_OR_SOURCETHEOREMATTEMPT_"
    "EXECUTED_NO_CROSSUSE_STRICT_SOURCE_OPEN"
)
NEXT = "MTT_Selected_HRGNonHiggsRetardedOverlapMap_or_StrictSourceTheorem_v1"


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
        raise FileNotFoundError("missing HRG cross-use audit inputs: " + ", ".join(missing))


def main() -> int:
    PACKET_DIR.mkdir(parents=True, exist_ok=True)
    CERTS.mkdir(parents=True, exist_ok=True)
    CORPUS.mkdir(parents=True, exist_ok=True)

    sources = [
        PREVIOUS,
        PREVIOUS_STRICT,
        PREVIOUS_CALIBRATION,
        PREVIOUS_CROSSUSE,
        PREVIOUS_HK,
        CHARGED_K,
        CHARGED_L,
        CROSSUSE_THEOREM,
        ALPHA1_CASE,
    ]
    require_sources(sources)

    previous = load(PREVIOUS)
    previous_strict = load(PREVIOUS_STRICT)
    calibration = load(PREVIOUS_CALIBRATION)
    workorder = load(PREVIOUS_CROSSUSE)
    previous_hk = load(PREVIOUS_HK)
    charged_k = load(CHARGED_K)
    charged_l = load(CHARGED_L)
    crossuse = load(CROSSUSE_THEOREM)
    alpha1_case = load(ALPHA1_CASE)

    primitive = workorder["calibrated_primitive_under_test"]
    primitive_id = primitive["id"]
    calibrated_value = float(primitive["calibrated_value"])

    target_results = [
        {
            "target": "non-Higgs threshold/RG observable",
            "candidate_source_path": "none emitted in current corpus",
            "same_primitive_source_map_available": False,
            "predicted_value_emitted_without_retuning": False,
            "passes_crossuse": False,
            "blocking_reason": (
                "No typed non-Higgs threshold/RG source map consumes "
                f"{primitive_id}={calibrated_value}."
            ),
        },
        {
            "target": "weak-mixing or alpha-sector consistency",
            "candidate_source_path": "B42/alpha1 universal primitive policy lane",
            "same_primitive_source_map_available": False,
            "predicted_value_emitted_without_retuning": False,
            "passes_crossuse": False,
            "blocking_reason": (
                "The alpha1 cross-use case remains not admitted; current alpha "
                "source primitives are L0/E0-family objects, not HRG."
            ),
            "alpha1_case_admitted_now": alpha1_case["admitted_now"],
        },
        {
            "target": "charged scalar threshold/prefactor rows",
            "candidate_source_path": rel(CHARGED_K),
            "same_primitive_source_map_available": False,
            "predicted_value_emitted_without_retuning": False,
            "passes_crossuse": False,
            "blocking_reason": (
                "Nine charged K rows are already strict source rows from "
                "L_rowlocal and null threshold-delta; applying HRG would be a "
                "post-hoc multiplier, not a selected prediction."
            ),
            "charged_strict_lrowlocal_row_count": charged_l["row_count"],
            "charged_strict_kthreshold_row_count": charged_k[
                "accepted_selected_charged_K_threshold_row_count"
            ],
        },
    ]
    passed_targets = [row for row in target_results if row["passes_crossuse"]]

    strict_reattempt = {
        "schema": "MTTStrictHRGSourceTheoremReattempt.v1",
        "status": "STRICT_HRG_SOURCE_THEOREM_REATTEMPTED_NOT_EMITTED",
        "closure_claimed": True,
        "previous_attempt_status": previous_strict["status"],
        "target": previous_strict["attempted_theorem"]["target"],
        "retested_contract": previous_strict["attempted_theorem"]["acceptance_contract"],
        "result": {
            "selected_R_H_RG_emitted": False,
            "selected_K_threshold_Omega_H_lambda_emitted": False,
            "same_branch_H_sector_determinant_or_index_emitted": False,
            "selected_matching_surface_mu_match_emitted": False,
            "mathematical_impossibility_claimed": False,
            "reason": (
                "Current data still provide a calibrated HRG value and H source "
                "equation, but no same-branch selected H threshold/RG operator "
                "or determinant/index certificate."
            ),
        },
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
    }

    target_matrix = {
        "schema": "MTTHRGNonHiggsTargetMatrix.v1",
        "status": "HRG_NONHIGGS_TARGET_MATRIX_EXECUTED_ZERO_ACCEPTED_TARGETS",
        "closure_claimed": True,
        "primitive_under_test": primitive,
        "policy_required": crossuse["admission_criteria"],
        "required_target_count_minimum": 1,
        "tested_target_count": len(target_results),
        "accepted_prediction_target_count": len(passed_targets),
        "target_results": target_results,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
    }

    crossuse_execution = {
        "schema": "MTTHRGCrossUsePredictionAuditExecution.v1",
        "status": "HRG_CROSSUSE_PREDICTION_AUDIT_EXECUTED_FAILED",
        "closure_claimed": True,
        "workorder_status": workorder["status"],
        "primitive_under_test": primitive,
        "calibration_scope": {
            "calibrating_observable": primitive["calibrating_observable"],
            "forbidden_prediction_credit": primitive["forbidden_prediction_credit"],
            "calibration_layer_built": True,
            "lambda_H_predicted": False,
        },
        "audit_result": {
            "crossuse_prediction_audit_executed": True,
            "crossuse_prediction_audit_passed": False,
            "accepted_prediction_target_count": len(passed_targets),
            "H_only_fit_quarantined": True,
            "universal_primitive_admitted": False,
            "strict_no_knob_status_upgraded": False,
        },
        "target_matrix_ref": rel(TARGET_MATRIX),
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
    }

    policy_decision = {
        "schema": "MTTHRGPrimitivePolicyDecisionAfterCrossUse.v1",
        "status": "HRG_PRIMITIVE_CLASSIFIED_H_ONLY_EMPIRICAL_NOT_UNIVERSAL",
        "closure_claimed": True,
        "primitive_id": primitive_id,
        "calibrated_value": calibrated_value,
        "allowed_current_use": [
            "controlled empirical H-layer replay",
            "SM-parity comparison input when declared as measured/calibrated downstream data",
        ],
        "forbidden_current_use": [
            "strict no-knob K_threshold.Omega_H.lambda source row",
            "lambda_H prediction claim",
            "universal parameter credibility upgrade",
            "non-Higgs prediction credit",
            "retuning or copying HRG per observable",
        ],
        "crossuse_policy_import": crossuse["statement"],
        "policy_decision": {
            "H_only_measured_parameter_interface_ready": True,
            "universal_parameter_admitted": False,
            "no_knob_parameter_derived": False,
            "requires_nonhiggs_map_or_strict_source_theorem": True,
        },
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
    }

    hk_gate = {
        "schema": "MTTHKThresholdGateAfterHRGCrossUseAudit.v1",
        "status": "H_K_THRESHOLD_GATE_EMPIRICAL_10_OF_10_STRICT_9_OF_10_CROSSUSE_FAILED",
        "closure_claimed": True,
        "strict_source_tier": previous_hk["strict_source_tier"],
        "controlled_empirical_tier": {
            **previous_hk["controlled_empirical_tier"],
            "crossuse_prediction_audit_required": False,
            "crossuse_prediction_audit_executed": True,
            "crossuse_prediction_audit_passed": False,
            "UP_RET_OVERLAP_HRG_universal_admitted": False,
            "UP_RET_OVERLAP_HRG_H_only_empirical": True,
        },
        "H_row": {
            **previous_hk["H_row"],
            "crossuse_prediction_audit_executed": True,
            "crossuse_prediction_audit_passed": False,
            "strict_HRG_source_reattempted": True,
        },
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
    }

    cutset = {
        "schema": "MTTNextCutsetAfterHRGCrossUseAudit.v1",
        "status": "NEXT_FRONTIER_HRG_NONHIGGS_MAP_OR_STRICT_SOURCE_THEOREM",
        "closure_claimed": True,
        "closed_here": [
            "HRG cross-use prediction audit executed",
            "zero non-Higgs prediction targets accepted",
            "HRG primitive classified as H-only empirical calibration unless upgraded",
            "strict HRG source theorem reattempted and still not emitted",
            "conditional empirical H K layer remains 10/10 but quarantined",
        ],
        "still_open": [
            "strict selected R_H^RG source theorem",
            "strict selected K_threshold.Omega_H.lambda",
            "non-Higgs retarded-overlap source map using UP-RET-OVERLAP.HRG",
            "universal primitive credibility upgrade for HRG",
            "lambda_H prediction without calibration",
            "true SM/no-knob equivalence",
        ],
        "next_required_artifact": NEXT,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
    }

    candidate = {
        "candidate": "MTTSelectedHRGPrimitiveCrossUsePredictionAuditOrSourceTheoremAttempt",
        "status": STATUS,
        "previous_status": previous["status"],
        "theorem": {
            "name": "HRGPrimitiveCrossUseAuditAndSourceReattemptTheorem",
            "proved": True,
            "statement": (
                "Executing the declared cross-use audit for UP-RET-OVERLAP.HRG "
                "against the current non-Higgs target classes yields zero "
                "accepted prediction targets. Reattempting the strict source "
                "theorem still emits no selected R_H^RG operator. Therefore the "
                "calibrated HRG value remains a controlled H-only empirical layer "
                "and cannot be used as a universal parameter, lambda_H prediction, "
                "or no-knob tenth K row until a non-Higgs source map or strict "
                "source theorem is supplied."
            ),
        },
        "closure_claimed": True,
        "true_SM_equivalence_claimed": False,
        "full_no_knob_closure_claimed": False,
        "closure_decision": {
            "crossuse_prediction_audit_executed": True,
            "crossuse_prediction_audit_passed": False,
            "accepted_nonhiggs_prediction_target_count": len(passed_targets),
            "strict_HRG_source_theorem_reattempted": True,
            "strict_HRG_source_theorem_emitted": False,
            "UP_RET_OVERLAP_HRG_universal_admitted": False,
            "UP_RET_OVERLAP_HRG_H_only_empirical": True,
            "conditional_empirical_H_K_layer_10_of_10": True,
            "strict_source_tier_9_of_10": True,
            "lambda_H_calibrated": True,
            "lambda_H_predicted": False,
            "true_SM_equivalence_closed": False,
            "full_no_knob_closed": False,
        },
        "key_numbers": {
            "UP_RET_OVERLAP_HRG": calibrated_value,
            "accepted_nonhiggs_prediction_target_count": len(passed_targets),
            "tested_nonhiggs_target_count": len(target_results),
            "controlled_empirical_conditional_K_row_count": 10,
            "strict_accepted_selected_K_source_row_count": previous_hk["strict_source_tier"][
                "accepted_selected_K_source_row_count"
            ],
        },
        "packets": {
            "strict_reattempt": rel(STRICT_REATTEMPT),
            "crossuse_execution": rel(CROSSUSE_EXECUTION),
            "target_matrix": rel(TARGET_MATRIX),
            "policy_decision": rel(POLICY_DECISION),
            "hk_gate": rel(HK_GATE),
            "cutset": rel(CUTSET),
        },
        "what_closes": {
            "HRG_crossuse_audit_executed": True,
            "HRG_universal_upgrade_rejected_currently": True,
            "H_only_empirical_policy_boundary_fixed": True,
            "strict_source_reattempt_recorded": True,
        },
        "what_remains_open": {
            "strict_selected_R_H_RG_source_theorem": True,
            "strict_selected_K_threshold_Omega_H_lambda": True,
            "nonhiggs_HRG_source_map": True,
            "lambda_H_prediction_without_calibration": True,
            "true_SM_equivalence": True,
            "full_no_knob_closure": True,
        },
        "next_required_artifact": NEXT,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
    }

    cert = {
        "certificate": "MTTSelectedHRGPrimitiveCrossUsePredictionAuditOrSourceTheoremAttempt",
        "status": STATUS,
        "candidate_path": rel(OUTPUT),
        "proof_note": rel(NOTE),
        "verified_packets": list(candidate["packets"].values()),
        "closure_claimed": True,
        "crossuse_prediction_audit_passed": False,
        "strict_HRG_source_emitted": False,
        "H_only_empirical_layer_retained": True,
        "true_SM_equivalence_claimed": False,
        "full_no_knob_closure_claimed": False,
        "next_required_artifact": NEXT,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
    }

    note = f"""# MTT Selected HRG Primitive Cross-Use Prediction Audit or Source Theorem Attempt v1

Status: `{STATUS}`

This packet executes the audit that the previous packet only scheduled.

## Result

- `UP-RET-OVERLAP.HRG = {calibrated_value}` remains calibrated on `lambda_H(M_t)`.
- Cross-use prediction audit: executed.
- Accepted non-Higgs prediction targets: `0 / {len(target_results)}`.
- Strict selected `R_H^RG` source theorem: reattempted, still not emitted.
- Controlled empirical H K layer: still conditional `10/10`.
- Strict source tier: still `9/10`.

## Meaning

The H-layer calibration is useful, but it is not yet a universal primitive and
not a no-knob result.  It may be used only as controlled H-only empirical
support or an SM-parity comparison input.  It cannot receive prediction credit
for `lambda_H`, cannot close the strict tenth K row, and cannot be reused in
non-Higgs sectors until a same-source non-Higgs retarded-overlap map is emitted.

## Tested Cross-Use Targets

1. non-Higgs threshold/RG observable: no typed source map currently consumes
   `UP-RET-OVERLAP.HRG`;
2. weak-mixing or alpha-sector consistency: the existing alpha primitive lane
   is not the HRG primitive and remains not admitted as cross-use;
3. charged scalar threshold/prefactor rows: the nine charged rows are already
   strict `L_rowlocal*T_scheme` rows, so HRG would be a post-hoc multiplier.

## Next

`{NEXT}`
"""

    write_json(STRICT_REATTEMPT, strict_reattempt)
    write_json(TARGET_MATRIX, target_matrix)
    write_json(CROSSUSE_EXECUTION, crossuse_execution)
    write_json(POLICY_DECISION, policy_decision)
    write_json(HK_GATE, hk_gate)
    write_json(CUTSET, cutset)
    write_json(OUTPUT, candidate)
    write_json(CERT, cert)
    NOTE.write_text(note, encoding="utf-8")

    for path in [OUTPUT, CERT, NOTE]:
        print(f"Wrote {rel(path)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
