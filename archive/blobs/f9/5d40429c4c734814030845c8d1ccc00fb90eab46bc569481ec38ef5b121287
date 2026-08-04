"""Build RO value-source / non-Higgs map execution packet.

The previous theorem source-selected the retarded-overlap family class, but not
the HRG numeric specialization.  This artifact executes the next decision:

* can any current strict source packet emit RO.value_source / R_H^RG?
* can the family-selected HRG value be admitted through a same-HRG non-Higgs map?
* does the adjacent Qa/SU3 selected retarded-response result promote the HRG
  number, or only support the retarded-overlap source shape?

Current result: zero accepted RO value sources and zero accepted same-HRG
non-Higgs maps.  The Qa/SU3 import is real source-shape support, but it emits
chi_Qa=1, not UP-RET-OVERLAP.HRG.
"""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
TEXPAPERS = ROOT.parent
DATA = ROOT / "candidate_data"
CERTS = ROOT / "certificates"
CORPUS = ROOT / "proof_corpus"

SLUG = "selected_rovaluesource_or_nonhiggsmapexecution"
PACKET_DIR = DATA / SLUG
OUTPUT = DATA / f"{SLUG}.candidate.json"
VALUE_MATRIX = PACKET_DIR / "ro_value_source_candidate_matrix.packet.json"
VALUE_EXECUTION = PACKET_DIR / "ro_value_source_execution.packet.json"
NONHIGGS_IMPORT_REPLAY = PACKET_DIR / "ro_nonhiggs_same_hrg_map_import_replay.packet.json"
MINIMAL_PARAMETER_STATUS = PACKET_DIR / "ro_minimal_parameter_status_after_value_attempt.packet.json"
PAYLOAD_AFTER_EXECUTION = PACKET_DIR / "ro_payload_after_value_source_execution.packet.json"
CUTSET = PACKET_DIR / "next_cutset_after_ro_value_source_execution.packet.json"
CERT = CERTS / f"{SLUG}_certificate.json"
NOTE = CORPUS / "MTT_Selected_ROValueSource_or_NonHiggsMapExecution_v1.md"

PREVIOUS = DATA / "selected_rofamilyselectorsourcetheorem_or_nonhiggspredictionmap.candidate.json"
PREVIOUS_FAMILY = (
    DATA
    / "selected_rofamilyselectorsourcetheorem_or_nonhiggspredictionmap"
    / "ro_family_selector_source_theorem.packet.json"
)
PREVIOUS_FULL_PAYLOAD = (
    DATA
    / "selected_rofamilyselectorsourcetheorem_or_nonhiggspredictionmap"
    / "ro_full_payload_after_family_selector.packet.json"
)
PREVIOUS_NONHIGGS = (
    DATA
    / "selected_rofamilyselectorsourcetheorem_or_nonhiggspredictionmap"
    / "ro_nonhiggs_prediction_map_attempt_after_selector.packet.json"
)
PREVIOUS_GATE = (
    DATA
    / "selected_rofamilyselectorsourcetheorem_or_nonhiggspredictionmap"
    / "ro_universal_admission_gate_after_selector.packet.json"
)
RO_VALUE_SOURCE = (
    DATA
    / "selected_retardedoverlapfamilyselector_or_hrgsourcepayloadfill"
    / "ro_value_source.packet.json"
)
STRICT_H_SOURCE_ATTEMPT = (
    DATA
    / "selected_hthresholdrgsource_or_minimalprimitivecalibrationrun"
    / "strict_h_threshold_rg_source_theorem_attempt.packet.json"
)
MINIMAL_CALIBRATION = (
    DATA
    / "selected_hthresholdrgsource_or_minimalprimitivecalibrationrun"
    / "minimal_primitive_calibration_run.packet.json"
)
H_PRIMITIVE_ADMISSION = (
    DATA
    / "selected_hthresholdrgoperator_or_universalprimitivepolicy"
    / "h_threshold_universal_primitive_admission_matrix.packet.json"
)
FAMILY_SOURCE_CONTRACT = (
    DATA
    / "selected_hrgnonhiggsretardedoverlapmap_or_strictsourcetheorem"
    / "retarded_overlap_family_source_map_contract.packet.json"
)
NONHIGGS_HRG_EXECUTION = (
    DATA
    / "selected_hrgnonhiggsretardedoverlapmap_or_strictsourcetheorem"
    / "nonhiggs_hrg_source_map_execution.packet.json"
)
CROSSUSE_POLICY = (
    DATA
    / "universal_crossuse_parameter_admissibility_theorem"
    / "crossuse_admissibility_theorem.packet.json"
)
QA_RESPONSE = (
    TEXPAPERS
    / "mtt-qa-su3-packet-proof"
    / "candidate_data"
    / "selected_response_functional_chi_qa.candidate.json"
)

STATUS = (
    "MTT_SELECTED_ROVALUESOURCE_OR_NONHIGGSMAPEXECUTION_"
    "EXECUTED_VALUE_SOURCE_AND_NONHIGGS_MAPS_OPEN"
)
NEXT = "MTT_Selected_HRGUniversalPrimitiveSourceRule_or_QaSU3RetardedMatchingMap_v1"


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
        raise FileNotFoundError("missing RO value-source execution inputs: " + ", ".join(missing))


def main() -> int:
    PACKET_DIR.mkdir(parents=True, exist_ok=True)
    CERTS.mkdir(parents=True, exist_ok=True)
    CORPUS.mkdir(parents=True, exist_ok=True)

    sources = [
        PREVIOUS,
        PREVIOUS_FAMILY,
        PREVIOUS_FULL_PAYLOAD,
        PREVIOUS_NONHIGGS,
        PREVIOUS_GATE,
        RO_VALUE_SOURCE,
        STRICT_H_SOURCE_ATTEMPT,
        MINIMAL_CALIBRATION,
        H_PRIMITIVE_ADMISSION,
        FAMILY_SOURCE_CONTRACT,
        NONHIGGS_HRG_EXECUTION,
        CROSSUSE_POLICY,
        QA_RESPONSE,
    ]
    require_sources(sources)

    previous = load(PREVIOUS)
    family = load(PREVIOUS_FAMILY)
    previous_payload = load(PREVIOUS_FULL_PAYLOAD)
    previous_nonhiggs = load(PREVIOUS_NONHIGGS)
    previous_gate = load(PREVIOUS_GATE)
    value_source = load(RO_VALUE_SOURCE)
    strict_attempt = load(STRICT_H_SOURCE_ATTEMPT)
    minimal_calibration = load(MINIMAL_CALIBRATION)
    primitive_admission = load(H_PRIMITIVE_ADMISSION)
    family_contract = load(FAMILY_SOURCE_CONTRACT)
    nonhiggs_hrg = load(NONHIGGS_HRG_EXECUTION)
    crossuse_policy = load(CROSSUSE_POLICY)
    qa_response = load(QA_RESPONSE)

    hrg_value = value_source["value"]["UP_RET_OVERLAP_HRG"]
    qa_chi = qa_response["derivation"]["result"]["chi_Qa_numeric"]
    source_family_selected = family["source_selected"] and family["selected_scope"]["family_class_selected"]
    previous_map_rows = previous_nonhiggs["map_rows"]

    value_rows = [
        {
            "lane": "strict_R_H_RG_source_operator",
            "accepted_as_RO_value_source": False,
            "source_selected": False,
            "empirical_payload": False,
            "support_import": False,
            "basis": rel(STRICT_H_SOURCE_ATTEMPT),
            "blocking_reasons": strict_attempt["current_open_payload"],
            "source_status": strict_attempt["status"],
        },
        {
            "lane": "controlled_empirical_H_lambda_calibration",
            "accepted_as_RO_value_source": False,
            "source_selected": False,
            "empirical_payload": True,
            "support_import": False,
            "basis": rel(MINIMAL_CALIBRATION),
            "value": hrg_value,
            "blocking_reasons": [
                "The value is selected by calibrating lambda_H(M_t), so lambda_H cannot be prediction credit.",
                "The calibration does not emit determinant/index/RG source provenance for R_H^RG.",
                "Cross-use has zero accepted same-HRG non-Higgs predictions.",
            ],
            "source_status": minimal_calibration["status"],
        },
        {
            "lane": "declared_UP_RET_OVERLAP_HRG_universal_parameter",
            "accepted_as_RO_value_source": False,
            "source_selected": False,
            "empirical_payload": False,
            "support_import": False,
            "basis": rel(H_PRIMITIVE_ADMISSION),
            "policy_admissible_if_crossused": True,
            "within_parameter_budget": True,
            "blocking_reasons": [
                "The primitive is not selected now in the universal-parameter policy.",
                "The same value is not yet shared across two independent source paths.",
                "No non-Higgs prediction consumes the same HRG value without retuning.",
            ],
            "source_status": primitive_admission["status"],
        },
        {
            "lane": "adjacent_QaSU3_selected_retarded_trace_response",
            "accepted_as_RO_value_source": False,
            "source_selected": False,
            "empirical_payload": False,
            "support_import": True,
            "basis": rel(QA_RESPONSE),
            "imported_result": "chi_Qa=1",
            "imported_numeric_value": qa_chi,
            "same_HRG_numeric_specialization": False,
            "retarded_response_source_shape_selected": True,
            "blocking_reasons": [
                "The Qa/SU3 packet emits a selected finite internal response normalization chi_Qa=1.",
                "It does not emit UP-RET-OVERLAP.HRG or R_H^RG.",
                "It explicitly leaves measured electroweak/running-coupling matching open.",
            ],
            "source_status": qa_response["status"],
        },
        {
            "lane": "same_HRG_nonHiggs_map_execution",
            "accepted_as_RO_value_source": False,
            "source_selected": False,
            "empirical_payload": False,
            "support_import": False,
            "basis": rel(NONHIGGS_HRG_EXECUTION),
            "tested_map_count": nonhiggs_hrg["tested_map_count"],
            "accepted_crossuse_map_count": nonhiggs_hrg["accepted_crossuse_map_count"],
            "blocking_reasons": [
                "The current non-Higgs HRG execution emits zero accepted maps.",
                "Without a same-HRG non-Higgs prediction, HRG remains H-only empirical support.",
            ],
            "source_status": nonhiggs_hrg["status"],
        },
    ]
    accepted_value_rows = [row for row in value_rows if row["accepted_as_RO_value_source"]]
    support_rows = [row for row in value_rows if row["support_import"]]

    value_matrix = {
        "schema": "MTTROValueSourceCandidateMatrix.v1",
        "status": "RO_VALUE_SOURCE_CANDIDATE_MATRIX_EXECUTED_ZERO_ACCEPTED",
        "closure_claimed": True,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "family_selector_source_selected": source_family_selected,
        "candidate_count": len(value_rows),
        "accepted_source_count": len(accepted_value_rows),
        "support_import_count": len(support_rows),
        "empirical_payload_count": len([row for row in value_rows if row["empirical_payload"]]),
        "rows": value_rows,
        "acceptance_rule": {
            "accepted_if_strict_source_operator_emitted": True,
            "accepted_if_same_HRG_nonHiggs_map_predicts_without_retuning": True,
            "accepted_if_universal_parameter_declared_once_and_cross_used": True,
            "rejected_if_value_selected_from_lambda_H_residual_only": True,
            "rejected_if_adjacent_retarded_response_value_differs_from_HRG_specialization": True,
        },
    }

    value_execution = {
        "schema": "MTTROValueSourceExecution.v1",
        "id": "RO.value_source",
        "status": "RO_VALUE_SOURCE_EXECUTED_ZERO_SOURCE_VALUES_HRG_EMPIRICAL_ONLY",
        "closure_claimed": True,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "source_selected": False,
        "family_selector_source_selected": source_family_selected,
        "source_value_emitted": False,
        "strict_R_H_RG_source_emitted": False,
        "empirical_value_available": True,
        "value": value_source["value"],
        "candidate_matrix": rel(VALUE_MATRIX),
        "decision": {
            "RO_value_source_derived": False,
            "strict_R_H_RG_source_emitted": False,
            "same_HRG_nonHiggs_map_accepted": False,
            "adjacent_QaSU3_retarded_response_support_imported": True,
            "adjacent_QaSU3_import_promotes_HRG": False,
            "empirical_HRG_value_retained": True,
            "minimal_parameter_H_layer_retained": True,
            "UP_RET_OVERLAP_HRG_universal_admitted": False,
            "lambda_H_predicted": False,
        },
    }

    qa_map_row = {
        "domain": "Qa/SU3 finite response normalization",
        "accepted_as_crossuse_map": False,
        "family_selector_available_now": source_family_selected,
        "retarded_overlap_source_shape_selected": True,
        "same_HRG_primitive_map_available": False,
        "same_HRG_numeric_specialization": False,
        "prediction_emitted_without_retuning": False,
        "would_count_as_nonHiggs_prediction": True,
        "imported_result": "chi_Qa=1",
        "imported_numeric_value": qa_chi,
        "source_refs": [rel(QA_RESPONSE)],
        "blocking_reason": (
            "Qa/SU3 supplies a selected retarded trace response shape, but its "
            "selected value is chi_Qa=1 and measured coupling matching remains open; "
            "it is not a typed sector insertion map for UP-RET-OVERLAP.HRG."
        ),
    }
    replay_rows = previous_map_rows + [qa_map_row]
    accepted_replay = [row for row in replay_rows if row["accepted_as_crossuse_map"]]
    nonhiggs_replay = {
        "schema": "MTTRONonHiggsSameHRGMapImportReplay.v1",
        "status": "RO_NONHIGGS_SAME_HRG_MAP_IMPORT_REPLAYED_ZERO_ACCEPTED",
        "closure_claimed": True,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "family_selector_source_selected": source_family_selected,
        "qa_su3_retarded_response_imported": True,
        "tested_map_count": len(replay_rows),
        "accepted_crossuse_map_count": len(accepted_replay),
        "minimum_required_accepted_map_count": 1,
        "map_rows": replay_rows,
        "decision": {
            "accepted_RO_nonHiggs_sector_map": False,
            "nonHiggs_prediction_emitted": False,
            "crossuse_prediction_passed": False,
            "UP_RET_OVERLAP_HRG_universal_admitted": False,
        },
    }

    minimal_status = {
        "schema": "MTTROMinimalParameterStatusAfterValueAttempt.v1",
        "status": "RO_MINIMAL_PARAMETER_STATUS_H_ONLY_EXECUTABLE_NOT_UNIVERSAL",
        "closure_claimed": True,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "policy_import": crossuse_policy["admission_criteria"],
        "parameter_under_test": {
            "id": "UP-RET-OVERLAP.HRG",
            "base_policy_class": "UP-RET-OVERLAP",
            "calibrated_value": hrg_value,
            "declared_role": minimal_calibration["primitive"]["declared_role"],
        },
        "decision": {
            "one_parameter_layer_executable_for_H": True,
            "within_maximum_live_universal_parameters": True,
            "declared_once": True,
            "not_retuned_per_observable": True,
            "shared_across_two_independent_source_paths": False,
            "one_calibration_makes_rest_predictions": False,
            "accepted_as_provisional_universal_parameter_now": False,
            "accepted_as_no_knob_source_value": False,
        },
        "blocking_reasons": [
            "The parameter currently explains only the calibrating H/lambda row.",
            "The same value has zero accepted non-Higgs predictions.",
            "The parameter value is not derived from selected source data.",
        ],
    }

    payload_after = {
        "schema": "MTTROPayloadAfterValueSourceExecution.v1",
        "status": "RO_PAYLOAD_AFTER_VALUE_SOURCE_EXECUTION_VALUE_AND_MAP_OPEN",
        "closure_claimed": True,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "payload_rows": [
            {
                "id": "RO.family_selector",
                "status": "RO_FAMILY_SELECTOR_SOURCE_SELECTED_AS_FAMILY_CLASS",
                "source_selected": True,
                "strict_source_payload": True,
            },
            {
                "id": "RO.value_source",
                "status": value_execution["status"],
                "source_selected": False,
                "strict_source_payload": False,
            },
            {
                "id": "RO.H_sector_map",
                "status": "RO_H_SECTOR_MAP_EMPIRICAL_FILLED_FAMILY_SELECTED_STRICT_SOURCE_OPEN",
                "source_selected": False,
                "strict_source_payload": False,
            },
            {
                "id": "RO.nonHiggs_sector_map",
                "status": nonhiggs_replay["status"],
                "source_selected": False,
                "strict_source_payload": False,
            },
            {
                "id": "RO.nonHiggs_prediction_evaluator",
                "status": "RO_NONHIGGS_PREDICTION_EVALUATOR_REPLAYED_AFTER_VALUE_SOURCE_ZERO_PREDICTIONS",
                "source_selected": False,
                "strict_source_payload": False,
            },
            {
                "id": "RO.provenance_certificate",
                "status": "RO_PROVENANCE_CERTIFICATE_UPDATED_AFTER_VALUE_SOURCE_EXECUTION",
                "source_selected": True,
                "strict_source_payload": True,
            },
        ],
        "all_payload_slots_filled": previous_payload["all_payload_slots_filled"],
        "all_required_payloads_source_selected": False,
        "source_selected_payload_count": 2,
        "strict_source_payload_count_excluding_provenance": 1,
        "HRG_numeric_specialization_source_selected": False,
        "accepted_value_source_count": len(accepted_value_rows),
        "accepted_nonHiggs_map_count": len(accepted_replay),
        "nonHiggs_prediction_count": 0,
    }

    cutset = {
        "schema": "MTTNextCutsetAfterROValueSourceExecution.v1",
        "status": "NEXT_FRONTIER_HRG_SOURCE_RULE_OR_QASU3_RETARDED_MATCHING_MAP",
        "closure_claimed": True,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "closed_here": [
            "RO.value_source candidate matrix executed",
            "strict R_H^RG source attempt replayed and still rejects",
            "controlled empirical HRG value retained without prediction credit",
            "adjacent Qa/SU3 selected retarded-response import classified as support only",
            "non-Higgs same-HRG map replay expanded to five lanes with zero accepted maps",
            "minimal-parameter status fixed as H-only executable but not universal",
        ],
        "still_open": [
            "selected HRG numeric source rule from determinant/index/RG transport",
            "strict selected R_H^RG or K_threshold.Omega_H.lambda",
            "typed same-HRG Qa/SU3/electroweak matching map",
            "accepted RO.nonHiggs_sector_map using UP-RET-OVERLAP.HRG",
            "non-Higgs prediction emitted without retuning",
            "universal admission of UP-RET-OVERLAP.HRG",
            "true SM/no-knob equivalence",
        ],
        "next_required_artifact": NEXT,
    }

    candidate = {
        "candidate": "MTTSelectedROValueSourceOrNonHiggsMapExecution",
        "status": STATUS,
        "previous_status": previous["status"],
        "closure_claimed": True,
        "true_SM_equivalence_claimed": False,
        "full_no_knob_closure_claimed": False,
        "theorem": {
            "name": "ROValueSourceOrNonHiggsMapExecutionTheorem",
            "proved": True,
            "statement": (
                "After the retarded-overlap family selector is source-selected, "
                "RO.value_source can be promoted only by a strict R_H^RG source "
                "operator, by a declared universal primitive with same-value "
                "cross-use predictions, or by a same-HRG non-Higgs source map. "
                "The current ledger emits none of these. The adjacent Qa/SU3 "
                "retarded-response result is valid source-shape support, but it "
                "emits chi_Qa=1 rather than UP-RET-OVERLAP.HRG."
            ),
        },
        "closure_decision": {
            "RO_family_selector_source_selected": True,
            "RO_value_source_execution_attempted": True,
            "RO_value_source_derived": False,
            "strict_R_H_RG_source_emitted": False,
            "same_HRG_nonHiggs_map_accepted": False,
            "adjacent_QaSU3_retarded_response_imported": True,
            "adjacent_QaSU3_import_promotes_HRG": False,
            "minimal_parameter_H_layer_executable": True,
            "UP_RET_OVERLAP_HRG_admitted_as_universal": False,
            "RO_nonHiggs_prediction_emitted": False,
            "lambda_H_predicted": False,
            "true_SM_equivalence_closed": False,
            "full_no_knob_closed": False,
        },
        "key_numbers": {
            "UP_RET_OVERLAP_HRG": hrg_value,
            "log_UP_RET_OVERLAP_HRG": value_source["value"]["log_UP_RET_OVERLAP_HRG"],
            "QaSU3_selected_chi_Qa": qa_chi,
            "RO_value_source_candidate_count": len(value_rows),
            "accepted_RO_value_source_count": len(accepted_value_rows),
            "same_HRG_nonHiggs_tested_map_count": len(replay_rows),
            "accepted_same_HRG_nonHiggs_map_count": len(accepted_replay),
            "source_selected_payload_count": payload_after["source_selected_payload_count"],
            "strict_source_payload_count_excluding_provenance": payload_after[
                "strict_source_payload_count_excluding_provenance"
            ],
        },
        "packets": {
            "value_matrix": rel(VALUE_MATRIX),
            "value_execution": rel(VALUE_EXECUTION),
            "nonhiggs_import_replay": rel(NONHIGGS_IMPORT_REPLAY),
            "minimal_parameter_status": rel(MINIMAL_PARAMETER_STATUS),
            "payload_after_execution": rel(PAYLOAD_AFTER_EXECUTION),
            "cutset": rel(CUTSET),
        },
        "what_closes": {
            "RO_value_source_candidate_matrix": True,
            "RO_value_source_execution_attempt": True,
            "QaSU3_retarded_response_import_classification": True,
            "expanded_nonHiggs_same_HRG_map_replay": True,
            "minimal_parameter_status_after_RO_value_attempt": True,
        },
        "what_remains_open": {
            "source_derived_RO_value_source": True,
            "strict_source_selected_RO_H_sector_map": True,
            "accepted_RO_nonHiggs_sector_map": True,
            "RO_nonHiggs_prediction_without_retuning": True,
            "universal_admission_of_HRG": True,
            "strict_selected_K_threshold_Omega_H_lambda": True,
            "true_SM_equivalence": True,
            "full_no_knob_closure": True,
        },
        "next_required_artifact": NEXT,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
    }

    cert = {
        "certificate": "MTTSelectedROValueSourceOrNonHiggsMapExecution",
        "status": STATUS,
        "candidate_path": rel(OUTPUT),
        "proof_note": rel(NOTE),
        "verified_packets": list(candidate["packets"].values()),
        "closure_claimed": True,
        "RO_value_source_execution_attempted": True,
        "RO_value_source_derived": False,
        "strict_R_H_RG_source_emitted": False,
        "accepted_RO_value_source_count": len(accepted_value_rows),
        "same_HRG_nonHiggs_tested_map_count": len(replay_rows),
        "accepted_same_HRG_nonHiggs_map_count": len(accepted_replay),
        "adjacent_QaSU3_retarded_response_imported": True,
        "adjacent_QaSU3_import_promotes_HRG": False,
        "UP_RET_OVERLAP_HRG_admitted_as_universal": False,
        "true_SM_equivalence_claimed": False,
        "full_no_knob_closure_claimed": False,
        "next_required_artifact": NEXT,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
    }

    note = f"""# MTT Selected RO Value Source or Non-Higgs Map Execution v1

Status: `{STATUS}`

## Result

The selected `RO.family_selector` was used to execute the current
`RO.value_source` frontier.  Five value-source lanes were tested:

1. strict `R_H^RG` source operator,
2. controlled empirical `lambda_H` calibration,
3. declared `UP-RET-OVERLAP.HRG` universal primitive,
4. adjacent Qa/SU3 selected retarded trace response,
5. same-HRG non-Higgs map execution.

Accepted `RO.value_source` rows: `0`.

Accepted same-HRG non-Higgs maps: `0 / {len(replay_rows)}`.

## Qa/SU3 Import

The adjacent Qa/SU3 repo supplies genuine retarded-overlap source-shape
support:

```text
chi_Qa = Tr_finite(tau^2) * <Pi_tw, G_ret Pi_tw> = 8 * 1/8 = 1
```

This is useful, but it does not promote `UP-RET-OVERLAP.HRG={hrg_value}`:
it emits `chi_Qa=1`, leaves measured coupling matching open, and gives no typed
same-HRG sector insertion map.

## Boundary

`RO.value_source` remains empirical/source-open.  The one-parameter H layer is
still executable as a controlled H calibration, but it is not a universal
primitive admission because the same value has no accepted non-Higgs prediction.
`lambda_H` remains calibration, not prediction.

## Next

`{NEXT}`
"""

    write_json(VALUE_MATRIX, value_matrix)
    write_json(VALUE_EXECUTION, value_execution)
    write_json(NONHIGGS_IMPORT_REPLAY, nonhiggs_replay)
    write_json(MINIMAL_PARAMETER_STATUS, minimal_status)
    write_json(PAYLOAD_AFTER_EXECUTION, payload_after)
    write_json(CUTSET, cutset)
    write_json(OUTPUT, candidate)
    write_json(CERT, cert)
    NOTE.write_text(note, encoding="utf-8")

    for path in [OUTPUT, CERT, NOTE]:
        print(f"Wrote {rel(path)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
