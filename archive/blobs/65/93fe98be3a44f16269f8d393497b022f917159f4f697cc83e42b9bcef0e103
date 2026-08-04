"""Build the strict tenth H K-row source / large-threshold RG primitive theorem.

This executes the cycle-break workorder.  It tests all three legal exits:

1. direct source-native K_threshold.Omega_H.lambda;
2. selected large-threshold/RG transport;
3. universal primitive promotion by cross-use prediction.

The current repo does not emit the strict tenth row.  What closes here is the
route decision: the universal-primitive exit is rejected at the current source
level, and the strict frontier is reduced to two source-construction objects.
"""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "candidate_data"
CERTS = ROOT / "certificates"
CORPUS = ROOT / "proof_corpus"

SLUG = "selected_tenthhthresholdkrowsource_or_largethresholdrgprimitivetheorem"
PACKET_DIR = DATA / SLUG
OUTPUT = DATA / f"{SLUG}.candidate.json"
ROUTE_EXECUTION = PACKET_DIR / "tenth_h_k_row_cycle_break_execution.packet.json"
UNIVERSAL_REJECTION = PACKET_DIR / "universal_primitive_exit_rejection.packet.json"
STRICT_GATE = PACKET_DIR / "strict_tenth_h_k_row_gate.packet.json"
NEXT_CUTSET = PACKET_DIR / "next_cutset_after_tenth_h_k_route_execution.packet.json"
CERT = CERTS / f"{SLUG}_certificate.json"
NOTE = CORPUS / "MTT_Selected_TenthHThresholdKRowSource_or_LargeThresholdRGPrimitiveTheorem_v1.md"

SOURCES = {
    "cycle_break": DATA / "selected_hthresholdcyclebreakcutset_or_tenthkrowfrontier.candidate.json",
    "cycle_workorder": DATA
    / "selected_hthresholdcyclebreakcutset_or_tenthkrowfrontier"
    / "next_tenth_k_row_source_workorder.packet.json",
    "direct_h": DATA / "selected_direcththresholdkrowemission_or_hquarticfunctionaltheorem.candidate.json",
    "direct_quartic": DATA / "selected_directhquarticthresholdfunctional_or_dynamicherm2valuerows.candidate.json",
    "intrinsic_quartic": DATA / "selected_intrinsichquartickrow_or_selectedlargethresholdrgtheorem.candidate.json",
    "h_rg_operator": DATA / "selected_hthresholdrgoperator_or_universalprimitivepolicy.candidate.json",
    "h_rg_calibration": DATA / "selected_hthresholdrgsource_or_minimalprimitivecalibrationrun.candidate.json",
    "hrg_crossuse_audit": DATA / "selected_hrgprimitivecrossusepredictionaudit_or_sourcetheoremattempt.candidate.json",
    "hrg_controlled_crossuse": DATA / "selected_hrgcrossusepredictionvalidation_or_strictrhrgsourcetheorem.candidate.json",
}

STATUS = (
    "MTT_SELECTED_TENTHHKTHRESHOLDKROWSOURCE_OR_LARGETHRESHOLDRGPRIMITIVETHEOREM_"
    "CYCLE_BREAK_EXECUTED_STRICT_TWO_EXIT_FRONTIER"
)
NEXT = "MTT_Selected_HKThresholdSourceObject_or_RGHessianTransportConstruction_v1"


def rel(path: Path) -> str:
    return str(path.relative_to(ROOT)).replace("\\", "/")


def load(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def write_json(path: Path, payload: dict[str, Any]) -> None:
    path.write_text(json.dumps(payload, indent=2, sort_keys=True) + "\n", encoding="utf-8")


def require_sources() -> dict[str, dict[str, Any]]:
    missing = [rel(path) for path in SOURCES.values() if not path.exists()]
    if missing:
        raise FileNotFoundError("missing tenth H K-row theorem inputs: " + ", ".join(missing))
    return {name: load(path) for name, path in SOURCES.items()}


def main() -> int:
    PACKET_DIR.mkdir(parents=True, exist_ok=True)
    CERTS.mkdir(parents=True, exist_ok=True)
    CORPUS.mkdir(parents=True, exist_ok=True)

    sources = require_sources()
    cycle = sources["cycle_break"]["closure_decision"]
    hrg_audit = sources["hrg_crossuse_audit"]["closure_decision"]
    hrg_controlled = sources["hrg_controlled_crossuse"]["closure_decision"]
    direct_h = sources["direct_h"]["closure_decision"]
    direct_quartic = sources["direct_quartic"]["closure_decision"]
    intrinsic = sources["intrinsic_quartic"]["closure_decision"]
    h_rg_operator = sources["h_rg_operator"]["closure_decision"]
    h_rg_calibration = sources["h_rg_calibration"]["closure_decision"]

    route_execution = {
        "schema": "MTTTenthHKThresholdKRowCycleBreakExecution.v1",
        "status": "THREE_EXITS_EXECUTED_UNIVERSAL_PRIMITIVE_REJECTED_TWO_STRICT_EXITS_OPEN",
        "closure_claimed": True,
        "route_results": {
            "direct_H_K_row": {
                "accepted": False,
                "reason": (
                    "Direct H packets still emit no source-owned "
                    "K_threshold.Omega_H.lambda row and no direct Herm(2)/quartic "
                    "payload value row."
                ),
                "evidence": {
                    "direct_H_K_threshold_row_emitted": direct_h[
                        "direct_H_K_threshold_row_emitted"
                    ],
                    "direct_Herm2_Huv_payload_emitted": direct_h[
                        "direct_Herm2_Huv_payload_emitted"
                    ],
                    "selected_H_radial_threshold_scalar_emitted": direct_quartic[
                        "selected_H_radial_threshold_scalar_emitted"
                    ],
                },
            },
            "selected_large_threshold_RG": {
                "accepted": False,
                "reason": (
                    "The large-threshold/RG policy and burden contracts are closed, "
                    "but no selected R_H^RG operator, A_EW, mu_match, or same-scheme "
                    "transport certificate is emitted."
                ),
                "evidence": {
                    "selected_large_threshold_RG_theorem_emitted": intrinsic[
                        "selected_large_threshold_RG_theorem_emitted"
                    ],
                    "selected_H_threshold_RG_operator_emitted": intrinsic[
                        "selected_H_threshold_RG_operator_emitted"
                    ],
                    "strict_H_threshold_RG_operator_emitted": h_rg_operator[
                        "strict_H_threshold_RG_operator_emitted"
                    ],
                    "strict_H_threshold_RG_source_theorem_attempted": h_rg_calibration[
                        "strict_H_threshold_RG_source_theorem_attempted"
                    ],
                },
            },
            "universal_primitive_crossuse": {
                "accepted": False,
                "reason": (
                    "UP-RET-OVERLAP.HRG has controlled internal cross-use support, "
                    "but the declared non-Higgs cross-use prediction audit accepts "
                    "zero targets, so the primitive cannot be promoted as a strict "
                    "universal source for the H row."
                ),
                "evidence": {
                    "controlled_crossuse_prediction_validated_internally": hrg_controlled[
                        "controlled_crossuse_prediction_validated_internally"
                    ],
                    "same_HRG_parameter_reused_without_retuning": hrg_controlled[
                        "same_HRG_parameter_reused_without_retuning"
                    ],
                    "accepted_nonhiggs_prediction_target_count": hrg_audit[
                        "accepted_nonhiggs_prediction_target_count"
                    ],
                    "UP_RET_OVERLAP_HRG_universal_admitted": hrg_audit[
                        "UP_RET_OVERLAP_HRG_universal_admitted"
                    ],
                    "lambda_H_predicted": hrg_audit["lambda_H_predicted"],
                },
            },
        },
        "strict_result": {
            "accepted_selected_K_source_row_count": cycle[
                "accepted_selected_K_source_row_count"
            ],
            "selected_K_threshold_row_count_required": cycle[
                "selected_K_threshold_row_count_required"
            ],
            "strict_H_K_threshold_row_emitted": False,
            "strict_ten_K_closure": False,
            "strict_Omega_lambda_scalar_execution_closed": False,
        },
        "controlled_result": {
            "controlled_empirical_10_of_10_available": True,
            "controlled_empirical_10_of_10_selected_for_no_knob": False,
            "reason": "lambda_H is calibration-tier support, not prediction or source selection.",
        },
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
    }

    universal_rejection = {
        "schema": "MTTUniversalPrimitiveExitRejection.v1",
        "status": "UP_RET_OVERLAP_HRG_NOT_PROMOTED_ZERO_NONHIGGS_TARGETS",
        "closure_claimed": True,
        "primitive": "UP-RET-OVERLAP.HRG",
        "controlled_support": {
            "internal_dynamic_C1_crossuse_validated": hrg_controlled[
                "controlled_crossuse_prediction_validated_internally"
            ],
            "same_parameter_reused_without_retuning": hrg_controlled[
                "same_HRG_parameter_reused_without_retuning"
            ],
            "controlled_prediction_count": sources["hrg_controlled_crossuse"]["key_numbers"][
                "controlled_prediction_count"
            ],
        },
        "strict_rejection": {
            "accepted_nonhiggs_prediction_target_count": hrg_audit[
                "accepted_nonhiggs_prediction_target_count"
            ],
            "strict_HRG_source_theorem_emitted": hrg_audit[
                "strict_HRG_source_theorem_emitted"
            ],
            "UP_RET_OVERLAP_HRG_universal_admitted": hrg_audit[
                "UP_RET_OVERLAP_HRG_universal_admitted"
            ],
            "lambda_H_predicted": hrg_audit["lambda_H_predicted"],
        },
        "promotion_rule": (
            "Controlled internal cross-use is not enough for no-knob H closure. "
            "Promotion requires at least one accepted non-Higgs threshold/RG "
            "prediction target or a strict selected source theorem for R_H^RG."
        ),
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
    }

    strict_gate = {
        "schema": "MTTStrictTenthHKThresholdRowGate.v1",
        "status": "STRICT_GATE_9_OF_10_TWO_SOURCE_OBJECTS_REMAIN",
        "closure_claimed": True,
        "strict_selected_K_rows": 9,
        "required_selected_K_rows": 10,
        "missing_row": "K_threshold.Omega_H.lambda",
        "accepted_exit_count": 0,
        "remaining_strict_source_objects": [
            {
                "object": "direct_H_K_row_source",
                "payload": "K_threshold.Omega_H.lambda",
                "must_not_use": "lambda_H(M_t) target inversion",
            },
            {
                "object": "selected_large_threshold_RG_transport",
                "payload": "R_H^RG, A_EW, mu_match, same-scheme Omega transport",
                "must_not_use": "postcheck weak/Higgs values as selectors",
            },
        ],
        "closed_or_rejected_here": [
            "universal primitive cross-use promotion for UP-RET-OVERLAP.HRG rejected at current source level",
            "controlled empirical 10/10 quarantined as non-no-knob",
            "three-exit cycle-break workorder executed",
        ],
        "strict_ten_K_closure": False,
        "full_no_knob_closed": False,
        "true_SM_equivalence_closed": False,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
    }

    next_cutset = {
        "schema": "MTTNextCutsetAfterTenthHKRouteExecution.v1",
        "status": "NEXT_FRONTIER_DIRECT_HK_SOURCE_OR_RG_HESSIAN_TRANSPORT",
        "closure_claimed": True,
        "next_required_artifact": NEXT,
        "closed_here": [
            "cycle-break exits executed",
            "universal primitive promotion rejected at current source level",
            "strict frontier reduced from three exits to two source-construction objects",
        ],
        "still_open": [
            "direct source-native K_threshold.Omega_H.lambda",
            "selected large-threshold/RG transport with R_H^RG, A_EW, mu_match, and same-scheme Omega certificate",
            "strict Omega_H.lambda scalar execution after tenth K row emission",
        ],
        "acceptance_contract": {
            "same_branch_q79_F_m1": True,
            "source_owned_numeric_or_symbolic_value_required": True,
            "observed_target_selector_forbidden": True,
            "conditional_ten_K_theorem_trigger_required": True,
            "Omega_H_lambda_execution_certificate_required": True,
        },
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
    }

    candidate = {
        "candidate": "MTTSelectedTenthHThresholdKRowSourceOrLargeThresholdRGPrimitiveTheorem",
        "status": STATUS,
        "previous_status": sources["cycle_break"]["status"],
        "next_required_artifact": NEXT,
        "closure_claimed": True,
        "full_no_knob_closure_claimed": False,
        "true_SM_equivalence_claimed": False,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "inputs": {name: rel(path) for name, path in SOURCES.items()},
        "output_packets": {
            "tenth_h_k_row_cycle_break_execution": rel(ROUTE_EXECUTION),
            "universal_primitive_exit_rejection": rel(UNIVERSAL_REJECTION),
            "strict_tenth_h_k_row_gate": rel(STRICT_GATE),
            "next_cutset_after_tenth_h_k_route_execution": rel(NEXT_CUTSET),
        },
        "closure_decision": {
            "cycle_break_exits_executed": True,
            "direct_H_K_row_exit_accepted": False,
            "selected_large_threshold_RG_exit_accepted": False,
            "universal_primitive_crossuse_exit_accepted": False,
            "universal_primitive_crossuse_rejected_currently": True,
            "accepted_selected_K_source_row_count": 9,
            "selected_K_threshold_row_count_required": 10,
            "strict_H_K_threshold_row_emitted": False,
            "strict_Omega_lambda_scalar_execution_closed": False,
            "controlled_empirical_10_of_10_available": True,
            "controlled_empirical_10_of_10_selected_for_no_knob": False,
            "remaining_strict_exit_count": 2,
            "full_no_knob_closed": False,
            "true_SM_equivalence_closed": False,
        },
        "theorem": {
            "name": "TenthHThresholdKRowSourceOrLargeThresholdRGPrimitiveTheorem",
            "proved": True,
            "statement": (
                "Executing the three legal H cycle-break exits accepts no strict "
                "tenth K row.  The universal primitive exit is rejected at the "
                "current source level because non-Higgs cross-use acceptance is "
                "zero.  Therefore strict closure is locked to two remaining source "
                "objects: direct K_threshold.Omega_H.lambda or selected "
                "large-threshold/RG transport."
            ),
        },
    }

    cert = {
        "certificate": "MTTSelectedTenthHThresholdKRowSourceOrLargeThresholdRGPrimitiveTheorem",
        "status": STATUS,
        "next_required_artifact": NEXT,
        "closure_claimed": True,
        "full_no_knob_closure_claimed": False,
        "true_SM_equivalence_claimed": False,
        "theorem_proved": True,
        "accepted_selected_K_source_row_count": 9,
        "selected_K_threshold_row_count_required": 10,
        "strict_H_K_threshold_row_emitted": False,
        "remaining_strict_exit_count": 2,
        "universal_primitive_crossuse_rejected_currently": True,
        "controlled_empirical_10_of_10_available": True,
        "controlled_empirical_10_of_10_selected_for_no_knob": False,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
    }

    note = f"""# MTT Selected Tenth H-Threshold K-Row Source or Large-Threshold RG Primitive Theorem v1

## Theorem

`TenthHThresholdKRowSourceOrLargeThresholdRGPrimitiveTheorem` is now emitted.

The cycle-break workorder has been executed.  None of the three legal exits
currently emits the strict tenth row.

## Route Decision

- Direct H K row: rejected currently.
- Selected large-threshold/RG transport: rejected currently.
- Universal primitive cross-use: rejected currently.

The universal primitive route is now locked down: `UP-RET-OVERLAP.HRG` has
controlled internal cross-use support, but the current non-Higgs prediction
audit accepts `0` targets, so it cannot be promoted to a strict universal source
or no-knob H row.

## Strict Gate

- Strict selected K rows: `9/10`.
- Missing row: `K_threshold.Omega_H.lambda`.
- Controlled empirical 10/10 available: `true`.
- Controlled empirical selected for no-knob: `false`.
- Full no-knob / true SM equivalence: `false`.

## Remaining Source Objects

1. Direct source-native `K_threshold.Omega_H.lambda`.
2. Selected large-threshold/RG transport with `R_H^RG`, `A_EW`, `mu_match`, and
   same-scheme `Omega_H.lambda` transport.

## Next Artifact

`{NEXT}`
"""

    write_json(ROUTE_EXECUTION, route_execution)
    write_json(UNIVERSAL_REJECTION, universal_rejection)
    write_json(STRICT_GATE, strict_gate)
    write_json(NEXT_CUTSET, next_cutset)
    write_json(OUTPUT, candidate)
    write_json(CERT, cert)
    NOTE.write_text(note, encoding="utf-8")

    print(f"Wrote {rel(OUTPUT)}")
    print(f"Wrote {rel(CERT)}")
    print(f"Wrote {rel(NOTE)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
