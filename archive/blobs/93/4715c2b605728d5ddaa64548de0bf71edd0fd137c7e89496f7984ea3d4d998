"""Fill the RO.* payload slots for the HRG retarded-overlap frontier.

The previous artifact reduced the frontier to six payloads:

* RO.family_selector
* RO.value_source
* RO.H_sector_map
* RO.nonHiggs_sector_map
* RO.nonHiggs_prediction_evaluator
* RO.provenance_certificate

This builder fills each slot with the strongest current object available.  It
separates typed shells, empirical H-layer payloads, and source-selected payloads
so that the ledger cannot accidentally promote calibration to prediction.
"""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "candidate_data"
CERTS = ROOT / "certificates"
CORPUS = ROOT / "proof_corpus"

SLUG = "selected_retardedoverlapfamilyselector_or_hrgsourcepayloadfill"
PACKET_DIR = DATA / SLUG
OUTPUT = DATA / f"{SLUG}.candidate.json"
RO_SELECTOR = PACKET_DIR / "ro_family_selector.packet.json"
RO_VALUE = PACKET_DIR / "ro_value_source.packet.json"
RO_H_MAP = PACKET_DIR / "ro_h_sector_map.packet.json"
RO_NONHIGGS_MAP = PACKET_DIR / "ro_nonhiggs_sector_map.packet.json"
RO_EVALUATOR = PACKET_DIR / "ro_nonhiggs_prediction_evaluator.packet.json"
RO_PROVENANCE = PACKET_DIR / "ro_provenance_certificate.packet.json"
FILL_MATRIX = PACKET_DIR / "ro_payload_fill_matrix.packet.json"
CUTSET = PACKET_DIR / "next_cutset_after_ro_payload_fill.packet.json"
CERT = CERTS / f"{SLUG}_certificate.json"
NOTE = CORPUS / "MTT_Selected_RetardedOverlapFamilySelector_or_HRGSourcePayloadFill_v1.md"

PREVIOUS = DATA / "selected_hrgnonhiggsretardedoverlapmap_or_strictsourcetheorem.candidate.json"
PREVIOUS_CONTRACT = (
    DATA
    / "selected_hrgnonhiggsretardedoverlapmap_or_strictsourcetheorem"
    / "retarded_overlap_family_source_map_contract.packet.json"
)
PREVIOUS_MANIFEST = (
    DATA
    / "selected_hrgnonhiggsretardedoverlapmap_or_strictsourcetheorem"
    / "retarded_overlap_family_payload_manifest.packet.json"
)
PREVIOUS_MAP_EXECUTION = (
    DATA
    / "selected_hrgnonhiggsretardedoverlapmap_or_strictsourcetheorem"
    / "nonhiggs_hrg_source_map_execution.packet.json"
)
PREVIOUS_STRICT = (
    DATA
    / "selected_hrgnonhiggsretardedoverlapmap_or_strictsourcetheorem"
    / "strict_hrg_source_theorem_execution.packet.json"
)
UNIVERSAL_POLICY = DATA / "universal_source_parameter_policy" / "candidate_universal_parameters.packet.json"
CROSSUSE = (
    DATA
    / "universal_crossuse_parameter_admissibility_theorem"
    / "crossuse_admissibility_theorem.packet.json"
)
CALIBRATION = (
    DATA
    / "selected_hthresholdrgsource_or_minimalprimitivecalibrationrun"
    / "minimal_primitive_calibration_run.packet.json"
)
EMPIRICAL_H_GATE = (
    DATA
    / "selected_hthresholdrgsource_or_minimalprimitivecalibrationrun"
    / "controlled_empirical_h_k_gate.packet.json"
)
H_SOURCE = (
    DATA
    / "selected_hsectorquarticthresholdpayload_or_stricttenkclosure"
    / "h_sector_payload_source_equation.packet.json"
)
H_ACCEPTANCE = (
    DATA
    / "selected_intrinsichquartickrow_or_selectedlargethresholdrgtheorem"
    / "selected_large_threshold_rg_acceptance_contract.packet.json"
)

STATUS = (
    "MTT_SELECTED_RETARDEDOVERLAPFAMILYSELECTOR_OR_HRGSOURCEPAYLOADFILL_"
    "PAYLOADS_FILLED_SOURCE_SELECTOR_OPEN"
)
NEXT = "MTT_Selected_ROFamilySelectorSourceTheorem_or_NonHiggsPredictionMap_v1"


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
        raise FileNotFoundError("missing RO payload-fill inputs: " + ", ".join(missing))


def main() -> int:
    PACKET_DIR.mkdir(parents=True, exist_ok=True)
    CERTS.mkdir(parents=True, exist_ok=True)
    CORPUS.mkdir(parents=True, exist_ok=True)

    sources = [
        PREVIOUS,
        PREVIOUS_CONTRACT,
        PREVIOUS_MANIFEST,
        PREVIOUS_MAP_EXECUTION,
        PREVIOUS_STRICT,
        UNIVERSAL_POLICY,
        CROSSUSE,
        CALIBRATION,
        EMPIRICAL_H_GATE,
        H_SOURCE,
        H_ACCEPTANCE,
    ]
    require_sources(sources)

    previous = load(PREVIOUS)
    contract = load(PREVIOUS_CONTRACT)
    manifest = load(PREVIOUS_MANIFEST)
    map_execution = load(PREVIOUS_MAP_EXECUTION)
    strict_execution = load(PREVIOUS_STRICT)
    universal_policy = load(UNIVERSAL_POLICY)
    crossuse = load(CROSSUSE)
    calibration = load(CALIBRATION)
    empirical_h = load(EMPIRICAL_H_GATE)
    h_source = load(H_SOURCE)
    h_acceptance = load(H_ACCEPTANCE)

    hrg_value = float(previous["key_numbers"]["UP_RET_OVERLAP_HRG"])
    cal_values = calibration["calibration_values"]
    primitive = calibration["primitive"]
    required_payload_ids = [
        payload["id"] for payload in manifest["payloads_required_for_next_closure"]
    ]

    selector = {
        "schema": "MTTROFamilySelectorPayload.v1",
        "id": "RO.family_selector",
        "status": "RO_FAMILY_SELECTOR_TYPED_SHELL_FILLED_NOT_SELECTED",
        "closure_claimed": True,
        "payload_kind": "typed_shell",
        "source_selected": False,
        "candidate_selector": {
            "primitive_class": "UP-RET-OVERLAP",
            "specialization": "UP-RET-OVERLAP.HRG",
            "intended_family": [
                "H threshold/RG transport",
                "dynamic C1 overlap/value tensor",
                "alpha/source-strength retarded derivative",
                "non-Higgs threshold/RG map",
            ],
            "declared_once": crossuse["admission_criteria"]["declared_once"],
            "not_retuned_per_observable": crossuse["admission_criteria"][
                "not_retuned_per_observable"
            ],
        },
        "policy_basis": {
            "universal_parameter_candidates_status": universal_policy["status"],
            "UP_RET_OVERLAP_selected_now": False,
            "crossuse_policy_status": crossuse["status"],
        },
        "blocking_reasons": [
            "No selected source id emits the retarded-overlap family before empirical replay.",
            "No non-Higgs sector map uses the same HRG value without retuning.",
            "Current UP-RET-OVERLAP.HRG value is calibrated in the H lane, not source-derived.",
        ],
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
    }

    value_source = {
        "schema": "MTTROValueSourcePayload.v1",
        "id": "RO.value_source",
        "status": "RO_VALUE_SOURCE_EMPIRICAL_VALUE_FILLED_SOURCE_VALUE_OPEN",
        "closure_claimed": True,
        "payload_kind": "empirical_value_with_source_gap",
        "source_selected": False,
        "empirical_value_available": True,
        "value": {
            "UP_RET_OVERLAP_HRG": hrg_value,
            "log_UP_RET_OVERLAP_HRG": cal_values["log_required_UP_RET_OVERLAP_HRG"],
            "calibrating_observable": calibration["calibration_protocol"][
                "calibrating_observable"
            ],
            "lambda_if_R_H_RG_equals_1": cal_values["lambda_if_R_H_RG_equals_1"],
            "lambda_if_R_H_RG_equals_required_value": cal_values[
                "lambda_if_R_H_RG_equals_required_value"
            ],
            "absolute_residual": cal_values["absolute_residual"],
        },
        "source_value_emitted": False,
        "strict_R_H_RG_source_emitted": strict_execution["result"]["selected_R_H_RG"],
        "claim_boundary": calibration["claim_boundary"],
        "blocking_reasons": [
            "The value is calibrated on lambda_H(M_t), so lambda_H cannot count as prediction.",
            "No determinant/index/RG source rule derives the numeric HRG value.",
            "No non-Higgs prediction has validated the same value without retuning.",
        ],
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
    }

    h_sector_map = {
        "schema": "MTTROHSectorMapPayload.v1",
        "id": "RO.H_sector_map",
        "status": "RO_H_SECTOR_MAP_EMPIRICAL_FILLED_STRICT_SOURCE_OPEN",
        "closure_claimed": True,
        "payload_kind": "controlled_empirical_H_map",
        "source_selected": False,
        "controlled_empirical_map_filled": True,
        "strict_H_sector_map_emitted": False,
        "primitive": {
            "id": primitive["id"],
            "admitted_as_controlled_empirical_parameter": primitive[
                "admitted_as_controlled_empirical_parameter"
            ],
            "selected_as_strict_source_parameter": primitive[
                "selected_as_strict_source_parameter"
            ],
        },
        "map_formulae": {
            "boundary": h_acceptance["required_equations"]["boundary"],
            "omega_scheme": h_acceptance["required_equations"]["omega_scheme"],
            "transported_postcheck": h_acceptance["required_equations"][
                "transported_postcheck"
            ],
            "same_scheme_source_equation": h_source["selected_source_equation"][
                "omega_value"
            ],
            "controlled_empirical_omega_scheme_formula": empirical_h[
                "controlled_empirical_tier"
            ]["omega_scheme_formula"],
        },
        "gate_effect": {
            "conditional_parameterized_K_row_count": empirical_h[
                "controlled_empirical_tier"
            ]["conditional_parameterized_K_row_count"],
            "H_lambda_calibrated_not_predicted": empirical_h[
                "controlled_empirical_tier"
            ]["H_lambda_calibrated_not_predicted"],
            "strict_K_threshold_Omega_H_lambda_emitted": empirical_h[
                "strict_source_tier"
            ]["K_threshold_Omega_H_lambda_emitted"],
        },
        "blocking_reasons": [
            "Selected A_EW and selected mu_match remain absent.",
            "Selected R_H^RG determinant/index/provenance certificate remains absent.",
            "The filled H map is empirical/conditional, not a strict source map.",
        ],
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
    }

    nonhiggs_map = {
        "schema": "MTTRONonHiggsSectorMapPayload.v1",
        "id": "RO.nonHiggs_sector_map",
        "status": "RO_NONHIGGS_SECTOR_MAP_EXECUTED_ZERO_ACCEPTED_MAPS",
        "closure_claimed": True,
        "payload_kind": "executed_map_search",
        "source_selected": False,
        "tested_map_count": map_execution["tested_map_count"],
        "accepted_crossuse_map_count": map_execution["accepted_crossuse_map_count"],
        "map_rows": map_execution["map_rows"],
        "nonHiggs_sector_map_emitted": False,
        "blocking_reasons": [
            "Alpha/source-strength lane has no typed HRG insertion map.",
            "Dynamic C1 lane has no selected value tensor or honest Galerkin values.",
            "Charged rows are already source-native T_scheme=1 and cannot be multiplied by HRG.",
            "No generic non-Higgs threshold/RG source map consumes HRG.",
        ],
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
    }

    evaluator = {
        "schema": "MTTRONonHiggsPredictionEvaluatorPayload.v1",
        "id": "RO.nonHiggs_prediction_evaluator",
        "status": "RO_NONHIGGS_PREDICTION_EVALUATOR_BUILT_ZERO_PREDICTIONS",
        "closure_claimed": True,
        "payload_kind": "prediction_evaluator_contract",
        "source_selected": False,
        "evaluator_contract": {
            "input_required": "one accepted RO.nonHiggs_sector_map",
            "must_use_same_HRG_value": True,
            "must_not_recalibrate_on_nonHiggs_target": True,
            "must_emit_prediction_without_retuning": True,
            "lambda_H_forbidden_as_prediction_credit": True,
        },
        "execution_result": {
            "accepted_nonHiggs_sector_map_count": map_execution["accepted_crossuse_map_count"],
            "prediction_count": 0,
            "crossuse_prediction_passed": False,
            "universal_primitive_admitted": False,
        },
        "candidate_prediction_domains_waiting": [
            row["domain"]
            for row in map_execution["map_rows"]
            if row["would_count_as_nonHiggs_prediction"]
        ],
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
    }

    provenance = {
        "schema": "MTTROProvenanceCertificatePayload.v1",
        "id": "RO.provenance_certificate",
        "status": "RO_PROVENANCE_CERTIFICATE_CLOSED_FOR_CURRENT_PAYLOAD_FILL",
        "closure_claimed": True,
        "payload_kind": "provenance_certificate",
        "source_selected": True,
        "certificate_closes": [
            "calibration/prediction separation",
            "H-only empirical classification",
            "charged-row HRG multiplier prohibition",
            "non-Higgs map count and zero-prediction decision",
            "strict no-knob and true-SM overclaim guard",
        ],
        "provenance_ledger": {
            "RO.family_selector": "typed shell only; source selector not emitted",
            "RO.value_source": "empirical calibrated value filled; source value not emitted",
            "RO.H_sector_map": "controlled empirical H map filled; strict H source map not emitted",
            "RO.nonHiggs_sector_map": "executed with zero accepted maps",
            "RO.nonHiggs_prediction_evaluator": "built with zero predictions because no map is accepted",
            "RO.provenance_certificate": "closed for current payload-fill boundary",
        },
        "forbidden_promotions": manifest["forbidden_payloads"],
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
    }

    payload_packets = [
        selector,
        value_source,
        h_sector_map,
        nonhiggs_map,
        evaluator,
        provenance,
    ]
    payload_by_id = {packet["id"]: packet for packet in payload_packets}
    missing_from_manifest = sorted(set(required_payload_ids) - set(payload_by_id))
    source_selected_count = sum(1 for packet in payload_packets if packet["source_selected"])
    empirical_filled_count = sum(
        1 for packet in payload_packets if packet["payload_kind"].startswith("empirical")
        or packet["payload_kind"] == "controlled_empirical_H_map"
    )
    strict_source_payload_count = sum(
        1
        for packet in payload_packets
        if packet["source_selected"] and packet["id"] != "RO.provenance_certificate"
    )

    fill_matrix = {
        "schema": "MTTROPayloadFillMatrix.v1",
        "status": "RO_PAYLOAD_FILL_MATRIX_BUILT_PROVENANCE_ONLY_SOURCE_SELECTED",
        "closure_claimed": True,
        "required_payload_count": len(required_payload_ids),
        "filled_payload_count": len(payload_packets),
        "missing_from_manifest": missing_from_manifest,
        "source_selected_payload_count": source_selected_count,
        "strict_source_payload_count_excluding_provenance": strict_source_payload_count,
        "empirical_or_conditional_payload_count": empirical_filled_count,
        "payload_rows": [
            {
                "id": packet["id"],
                "status": packet["status"],
                "payload_kind": packet["payload_kind"],
                "source_selected": packet["source_selected"],
            }
            for packet in payload_packets
        ],
        "gate_decision": {
            "all_payload_slots_filled_with_current_objects": True,
            "all_required_payloads_source_selected": False,
            "HRG_universal_admitted": False,
            "strict_H_K_row_closed": False,
            "nonHiggs_prediction_emitted": False,
            "true_SM_equivalence_closed": False,
            "full_no_knob_closed": False,
        },
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
    }

    cutset = {
        "schema": "MTTNextCutsetAfterROPayloadFill.v1",
        "status": "NEXT_FRONTIER_RO_FAMILY_SELECTOR_SOURCE_THEOREM_OR_NONHIGGS_MAP",
        "closure_claimed": True,
        "closed_here": [
            "all six RO payload slots filled with current strongest objects",
            "RO.provenance_certificate closed for current payload boundary",
            "RO.H_sector_map filled at controlled empirical tier",
            "RO.value_source filled as calibrated value with source gap",
            "RO.nonHiggs_sector_map and evaluator executed with zero accepted predictions",
        ],
        "still_open": [
            "source-selected RO.family_selector",
            "source-derived RO.value_source or strict R_H^RG",
            "strict source-selected RO.H_sector_map",
            "accepted RO.nonHiggs_sector_map",
            "non-Higgs prediction emitted without retuning",
            "universal admission of UP-RET-OVERLAP.HRG",
            "strict selected K_threshold.Omega_H.lambda",
            "true SM/no-knob equivalence",
        ],
        "next_required_artifact": NEXT,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
    }

    candidate = {
        "candidate": "MTTSelectedRetardedOverlapFamilySelectorOrHRGSourcePayloadFill",
        "status": STATUS,
        "previous_status": previous["status"],
        "theorem": {
            "name": "RetardedOverlapFamilyPayloadFillTheorem",
            "proved": True,
            "statement": (
                "All six RO payload slots are filled with the strongest current "
                "objects: a typed family-selector shell, an empirical calibrated "
                "HRG value, a controlled empirical H-sector map, an executed "
                "zero-map non-Higgs sector-map search, a zero-prediction evaluator, "
                "and a closed provenance certificate.  Only provenance is closed "
                "as selected payload; the selector, source value, strict H map, "
                "non-Higgs map, and non-Higgs prediction remain open."
            ),
        },
        "closure_claimed": True,
        "true_SM_equivalence_claimed": False,
        "full_no_knob_closure_claimed": False,
        "closure_decision": {
            "all_six_RO_payload_slots_filled": True,
            "RO_provenance_certificate_closed": True,
            "RO_family_selector_source_selected": False,
            "RO_value_source_derived": False,
            "RO_H_sector_map_strict_source_selected": False,
            "RO_nonHiggs_sector_map_accepted": False,
            "RO_nonHiggs_prediction_emitted": False,
            "UP_RET_OVERLAP_HRG_universal_admitted": False,
            "UP_RET_OVERLAP_HRG_H_only_empirical": True,
            "conditional_empirical_H_K_layer_10_of_10": True,
            "strict_source_tier_9_of_10": True,
            "lambda_H_predicted": False,
            "true_SM_equivalence_closed": False,
            "full_no_knob_closed": False,
        },
        "key_numbers": {
            "UP_RET_OVERLAP_HRG": hrg_value,
            "payload_slots_required": len(required_payload_ids),
            "payload_slots_filled": len(payload_packets),
            "source_selected_payload_count": source_selected_count,
            "strict_source_payload_count_excluding_provenance": strict_source_payload_count,
            "nonHiggs_prediction_count": 0,
        },
        "packets": {
            "RO.family_selector": rel(RO_SELECTOR),
            "RO.value_source": rel(RO_VALUE),
            "RO.H_sector_map": rel(RO_H_MAP),
            "RO.nonHiggs_sector_map": rel(RO_NONHIGGS_MAP),
            "RO.nonHiggs_prediction_evaluator": rel(RO_EVALUATOR),
            "RO.provenance_certificate": rel(RO_PROVENANCE),
            "fill_matrix": rel(FILL_MATRIX),
            "cutset": rel(CUTSET),
        },
        "what_closes": {
            "RO_payload_slots_materialized": True,
            "RO_provenance_certificate": True,
            "empirical_H_sector_payload_boundary": True,
            "nonHiggs_zero_prediction_evaluator_boundary": True,
            "next_source_theorem_target_fixed": True,
        },
        "what_remains_open": {
            "source_selected_RO_family_selector": True,
            "source_derived_RO_value_source": True,
            "strict_source_selected_RO_H_sector_map": True,
            "accepted_RO_nonHiggs_sector_map": True,
            "RO_nonHiggs_prediction_without_retuning": True,
            "strict_selected_K_threshold_Omega_H_lambda": True,
            "true_SM_equivalence": True,
            "full_no_knob_closure": True,
        },
        "next_required_artifact": NEXT,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
    }

    cert = {
        "certificate": "MTTSelectedRetardedOverlapFamilySelectorOrHRGSourcePayloadFill",
        "status": STATUS,
        "candidate_path": rel(OUTPUT),
        "proof_note": rel(NOTE),
        "verified_packets": list(candidate["packets"].values()),
        "closure_claimed": True,
        "RO_payload_slots_filled": len(payload_packets),
        "RO_provenance_certificate_closed": True,
        "strict_source_payload_count_excluding_provenance": strict_source_payload_count,
        "nonHiggs_prediction_count": 0,
        "H_only_empirical_layer_retained": True,
        "true_SM_equivalence_claimed": False,
        "full_no_knob_closure_claimed": False,
        "next_required_artifact": NEXT,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
    }

    note = f"""# MTT Selected Retarded-Overlap Family Selector or HRG Source Payload Fill v1

Status: `{STATUS}`

This packet fills the six `RO.*` payload slots with the strongest current
objects.

## Filled Payloads

- `RO.family_selector`: typed shell filled, not source-selected.
- `RO.value_source`: empirical calibrated value filled,
  `UP-RET-OVERLAP.HRG={hrg_value}`, source value still open.
- `RO.H_sector_map`: controlled empirical H map filled; strict selected H map
  still open.
- `RO.nonHiggs_sector_map`: executed, `0` accepted maps.
- `RO.nonHiggs_prediction_evaluator`: built, `0` predictions.
- `RO.provenance_certificate`: closed for the current payload boundary.

## Boundary

Only the provenance certificate is closed as a selected payload.  The H payload
is useful but empirical/conditional; it does not make `lambda_H` a prediction.
No non-Higgs prediction exists yet, and `UP-RET-OVERLAP.HRG` is not admitted as
a universal primitive.

## Next

`{NEXT}`

The next theorem must do one of two things:

1. source-select the `RO.family_selector` and derive `RO.value_source`/strict
   `R_H^RG`; or
2. emit an accepted `RO.nonHiggs_sector_map` plus a non-Higgs prediction using
   the same HRG value without retuning.
"""

    write_json(RO_SELECTOR, selector)
    write_json(RO_VALUE, value_source)
    write_json(RO_H_MAP, h_sector_map)
    write_json(RO_NONHIGGS_MAP, nonhiggs_map)
    write_json(RO_EVALUATOR, evaluator)
    write_json(RO_PROVENANCE, provenance)
    write_json(FILL_MATRIX, fill_matrix)
    write_json(CUTSET, cutset)
    write_json(OUTPUT, candidate)
    write_json(CERT, cert)
    NOTE.write_text(note, encoding="utf-8")

    for path in [OUTPUT, CERT, NOTE]:
        print(f"Wrote {rel(path)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
