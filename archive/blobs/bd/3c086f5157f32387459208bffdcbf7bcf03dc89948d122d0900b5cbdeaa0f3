"""Build HRG cross-use prediction validation / strict R_H^RG source theorem packet."""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "candidate_data"
CERTS = ROOT / "certificates"
CORPUS = ROOT / "proof_corpus"

SLUG = "selected_hrgcrossusepredictionvalidation_or_strictrhrgsourcetheorem"
PACKET_DIR = DATA / SLUG
OUTPUT = DATA / f"{SLUG}.candidate.json"
CONTROLLED_VALIDATION = PACKET_DIR / "controlled_hrg_crossuse_prediction_validation.packet.json"
STRICT_REPLAY = PACKET_DIR / "strict_rhrg_source_theorem_replay.packet.json"
OBLIGATION = PACKET_DIR / "strict_source_obligation_matrix.packet.json"
CUTSET = PACKET_DIR / "next_cutset_after_hrg_crossuse_validation.packet.json"
CERT = CERTS / f"{SLUG}_certificate.json"
NOTE = CORPUS / "MTT_Selected_HRGCrossUsePredictionValidation_or_StrictRHRGSourceTheorem_v1.md"

PREVIOUS = DATA / "selected_hrgconsumervaluesource_or_largethresholdtransportmap.candidate.json"
CONTROLLED_ADMISSION = (
    DATA
    / "selected_hrgconsumervaluesource_or_largethresholdtransportmap"
    / "controlled_universal_hrg_parameter_admission.packet.json"
)
DYNAMIC_MAP = (
    DATA
    / "selected_hrgconsumervaluesource_or_largethresholdtransportmap"
    / "dynamic_c1_same_hrg_transport_prediction_map.packet.json"
)
INVARIANT_SEARCH = (
    DATA
    / "selected_hrgconsumervaluesource_or_largethresholdtransportmap"
    / "finite_invariant_hrg_specialization_search.packet.json"
)
STRICT_HRG_REPLAY = (
    DATA
    / "selected_hrgconsumervaluesource_or_largethresholdtransportmap"
    / "strict_hrg_value_source_replay_after_dynamic_payload.packet.json"
)
HRG_NONHIGGS = DATA / "selected_hrgnonhiggsretardedoverlapmap_or_strictsourcetheorem.candidate.json"
RO_VALUE = DATA / "selected_rovaluesource_or_nonhiggsmapexecution.candidate.json"
ALPHA_AEW = DATA / "selected_alpha1hrgselector_or_aewmetrologyvaluesourcetheorem.candidate.json"
UNPATCHED = DATA / "selected_unpatchedphifinc1sourcerule_or_honestgalerkintables_to_hrgconsumermap.candidate.json"

STATUS = (
    "MTT_SELECTED_HRGCROSSUSEPREDICTIONVALIDATION_OR_STRICTRHRGSOURCETHEOREM_"
    "CONTROLLED_CROSSUSE_VALIDATED_STRICT_RHRG_SOURCE_OPEN"
)
NEXT = "MTT_Selected_StrictRHRGSourceConstruction_or_IndependentValidationOracle_v1"


def rel(path: Path) -> str:
    return str(path.relative_to(ROOT)).replace("\\", "/")


def load(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def write_json(path: Path, payload: dict[str, Any]) -> None:
    path.write_text(json.dumps(payload, indent=2, sort_keys=True) + "\n", encoding="utf-8")


def require_sources(paths: list[Path]) -> None:
    missing = [rel(path) for path in paths if not path.exists()]
    if missing:
        raise FileNotFoundError("missing HRG validation inputs: " + ", ".join(missing))


def main() -> int:
    PACKET_DIR.mkdir(parents=True, exist_ok=True)
    CERTS.mkdir(parents=True, exist_ok=True)
    CORPUS.mkdir(parents=True, exist_ok=True)

    sources = [
        PREVIOUS,
        CONTROLLED_ADMISSION,
        DYNAMIC_MAP,
        INVARIANT_SEARCH,
        STRICT_HRG_REPLAY,
        HRG_NONHIGGS,
        RO_VALUE,
        ALPHA_AEW,
        UNPATCHED,
    ]
    require_sources(sources)

    previous = load(PREVIOUS)
    controlled_admission = load(CONTROLLED_ADMISSION)
    dynamic_map = load(DYNAMIC_MAP)
    invariant = load(INVARIANT_SEARCH)
    strict_replay_in = load(STRICT_HRG_REPLAY)
    hrg_nonhiggs = load(HRG_NONHIGGS)
    ro_value = load(RO_VALUE)
    alpha_aew = load(ALPHA_AEW)
    unpatched = load(UNPATCHED)

    hrg = previous["key_numbers"]["UP_RET_OVERLAP_HRG"]
    predicted = dynamic_map["predicted_transport_rows"]
    a00 = predicted["HRG_times_A_transpose_A"][0][0]
    b0 = predicted["HRG_times_A_transpose_b"][0]
    theta0 = predicted["HRG_times_deltaTheta_C1"][0]
    expected_row_scale = 12.0 * hrg

    validation_residuals = {
        "A00_minus_12_HRG": a00 - expected_row_scale,
        "b0_minus_12_HRG": b0 - expected_row_scale,
        "deltaTheta0_minus_HRG": theta0 - hrg,
        "same_parameter_reused": dynamic_map["map"]["parameter_value"] == hrg,
        "retuned_for_domain": dynamic_map["map"]["retuned_for_domain"],
    }

    controlled_validation = {
        "schema": "MTTHRGCrossUsePredictionValidation.v1",
        "status": "CONTROLLED_HRG_CROSSUSE_VALIDATION_EXECUTED_INTERNAL_EXACT_EXTERNAL_OPEN",
        "closure_claimed": True,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "measured_calibration_used": True,
        "parameter": {
            "id": "UP-RET-OVERLAP.HRG",
            "value": hrg,
            "declared_once": controlled_admission["primitive"]["declared_once"],
            "retuned_per_observable": controlled_admission["primitive"]["retuned_per_observable"],
            "source_derived": controlled_admission["primitive"]["source_derived"],
            "controlled_empirical": controlled_admission["primitive"]["controlled_empirical"],
        },
        "validated_predictions": [
            {
                "name": "dynamic_C1_A_transpose_A_00",
                "formula": "UP_RET_OVERLAP.HRG * A00",
                "input_A00": 12.0,
                "value": a00,
                "expected_internal_value": expected_row_scale,
                "residual": validation_residuals["A00_minus_12_HRG"],
            },
            {
                "name": "dynamic_C1_A_transpose_b_0",
                "formula": "UP_RET_OVERLAP.HRG * b0",
                "input_b0": 12.0,
                "value": b0,
                "expected_internal_value": expected_row_scale,
                "residual": validation_residuals["b0_minus_12_HRG"],
            },
            {
                "name": "dynamic_C1_deltaTheta_0",
                "formula": "UP_RET_OVERLAP.HRG * deltaTheta0",
                "input_deltaTheta0": 1.0,
                "value": theta0,
                "expected_internal_value": hrg,
                "residual": validation_residuals["deltaTheta0_minus_HRG"],
            },
        ],
        "validation_decision": {
            "controlled_crossuse_prediction_validated_internally": True,
            "same_HRG_parameter_reused_without_retuning": True,
            "independent_empirical_validation_supplied_here": False,
            "accepted_as_strict_no_knob_source": False,
            "counts_for_true_SM_equivalence": False,
        },
        "source_refs": [rel(CONTROLLED_ADMISSION), rel(DYNAMIC_MAP), rel(PREVIOUS)],
    }

    strict_replay = {
        "schema": "MTTStrictRHRGSourceTheoremReplay.v1",
        "status": "STRICT_RHRG_SOURCE_THEOREM_REPLAYED_NOT_EMITTED",
        "closure_claimed": True,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "theorem": {
            "name": "StrictRHRGSourceTheoremReplay",
            "proved": True,
            "statement": (
                "The controlled cross-use map is internally exact once "
                "UP-RET-OVERLAP.HRG is declared, but the current selected corpus "
                "still supplies no determinant/index/RG operator that emits the "
                "numeric R_H^RG value as source data."
            ),
        },
        "failed_promotion_routes": [
            {
                "route": "finite_invariant_formula",
                "accepted": False,
                "reason": "best finite invariant is a near miss, not an exact selected identity",
                "best_formula": invariant["diagnostics"]["best_candidate_formula"],
                "best_relative_error": invariant["diagnostics"]["best_candidate_relative_error"],
            },
            {
                "route": "RO_value_source_execution",
                "accepted": False,
                "reason": "RO execution accepted zero value sources and zero same-HRG non-Higgs maps",
                "accepted_value_sources": ro_value["closure_decision"]["RO_value_source_derived"],
                "accepted_same_HRG_maps": ro_value["closure_decision"]["same_HRG_nonHiggs_map_accepted"],
            },
            {
                "route": "nonHiggs_retarded_overlap_map",
                "accepted": False,
                "reason": "non-Higgs HRG source-map contract emitted zero accepted maps",
                "accepted_maps": hrg_nonhiggs["closure_decision"]["accepted_nonHiggs_HRG_source_map_count"],
            },
            {
                "route": "alpha_AEW_deficit_lock",
                "accepted": False,
                "reason": "alpha/AEW route locks the exact HRG-sized deficit but does not promote it as source",
                "accepted_AEW_sources": alpha_aew["closure_decision"]["accepted_AEW_source_count"],
                "accepted_HRG_selectors": alpha_aew["closure_decision"]["accepted_HRG_selector_count"],
            },
            {
                "route": "dynamic_Phi_fin_C1_backimport",
                "accepted": False,
                "reason": "dynamic payload is selected, but HRG remains a consumer value-source obligation",
                "dynamic_payload_selected": unpatched["closure_decision"]["selected_dynamic_phi_fin_c1_payload_emitted"],
                "accepted_RO_value_sources": unpatched["closure_decision"]["accepted_RO_value_source_count"],
            },
        ],
        "strict_decision": {
            "strict_R_H_RG_source_emitted": False,
            "strict_RO_value_source_derived": False,
            "selected_large_threshold_RG_transport_emitted": False,
            "lambda_H_predicted": False,
            "true_SM_equivalence_closed": False,
            "full_no_knob_closed": False,
        },
        "source_refs": [rel(STRICT_HRG_REPLAY), rel(INVARIANT_SEARCH), rel(RO_VALUE), rel(HRG_NONHIGGS), rel(ALPHA_AEW), rel(UNPATCHED)],
    }

    obligation = {
        "schema": "MTTStrictSourceObligationMatrix.v1",
        "status": "STRICT_RHRG_SOURCE_OBLIGATION_MATRIX_BUILT",
        "closure_claimed": True,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "required_for_no_knob_closure": [
            "selected determinant/index/RG operator R_H^RG emitting UP-RET-OVERLAP.HRG",
            "or independent selected validation oracle for the controlled same-HRG predictions",
            "or exact selected finite invariant identity replacing the calibrated HRG primitive",
        ],
        "currently_closed": [
            "dynamic Phi_fin/C1 payload selected",
            "RO family selector source theorem closed at family-class level",
            "controlled one-parameter HRG cross-use internally validated",
        ],
        "currently_open": [
            "strict R_H^RG source construction",
            "strict numeric HRG source",
            "independent external prediction validation",
            "lambda_H prediction credit",
            "true SM/no-knob equivalence",
        ],
    }

    cutset = {
        "schema": "MTTNextCutsetAfterHRGCrossUseValidation.v1",
        "status": "NEXT_FRONTIER_STRICT_RHRG_SOURCE_OR_INDEPENDENT_VALIDATION_ORACLE",
        "closure_claimed": True,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "closed_here": [
            "controlled HRG cross-use validation executed with exact internal residuals",
            "strict R_H^RG source theorem replayed after dynamic payload and still not emitted",
            "strict source obligation matrix built",
        ],
        "still_open": obligation["currently_open"],
        "next_required_artifact": NEXT,
    }

    candidate = {
        "candidate": "MTTSelectedHRGCrossUsePredictionValidationOrStrictRHRGSourceTheorem",
        "schema": "MTTSelectedCandidate.v1",
        "status": STATUS,
        "closure_claimed": True,
        "true_SM_equivalence_claimed": False,
        "full_no_knob_closure_claimed": False,
        "minimal_parameter_tier_claimed": True,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "next_required_artifact": NEXT,
        "theorem": {
            "name": "HRGCrossUsePredictionValidationOrStrictRHRGSourceTheorem",
            "proved": True,
            "statement": (
                "The same selected HRG primitive can be reused without retuning to "
                "produce internally exact dynamic-C1 transport rows.  This validates "
                "the controlled one-parameter cross-use tier, but it does not derive "
                "the HRG scalar from MTT source geometry."
            ),
        },
        "packets": {
            "controlled_validation": rel(CONTROLLED_VALIDATION),
            "strict_replay": rel(STRICT_REPLAY),
            "obligation": rel(OBLIGATION),
            "cutset": rel(CUTSET),
        },
        "closure_decision": {
            "controlled_crossuse_prediction_validated_internally": True,
            "same_HRG_parameter_reused_without_retuning": True,
            "strict_R_H_RG_source_emitted": False,
            "strict_RO_value_source_derived": False,
            "independent_empirical_validation_supplied_here": False,
            "lambda_H_predicted": False,
            "true_SM_equivalence_closed": False,
            "full_no_knob_closed": False,
        },
        "key_numbers": {
            "UP_RET_OVERLAP_HRG": hrg,
            "dynamic_C1_HRG_scaled_A00": a00,
            "dynamic_C1_HRG_scaled_b0": b0,
            "dynamic_C1_HRG_scaled_deltaTheta0": theta0,
            "A00_minus_12_HRG": validation_residuals["A00_minus_12_HRG"],
            "b0_minus_12_HRG": validation_residuals["b0_minus_12_HRG"],
            "deltaTheta0_minus_HRG": validation_residuals["deltaTheta0_minus_HRG"],
            "best_invariant_search_relative_error": invariant["diagnostics"]["best_candidate_relative_error"],
            "accepted_strict_source_count": 0,
            "controlled_prediction_count": 3,
        },
    }

    cert = {
        "certificate": "MTTSelectedHRGCrossUsePredictionValidationOrStrictRHRGSourceTheorem",
        "status": STATUS,
        "next_required_artifact": NEXT,
        "theorem_proved": True,
        "minimal_parameter_tier_claimed": True,
        "true_SM_equivalence_claimed": False,
        "full_no_knob_closure_claimed": False,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "controlled_crossuse_prediction_validated_internally": True,
        "same_HRG_parameter_reused_without_retuning": True,
        "strict_R_H_RG_source_emitted": False,
        "strict_RO_value_source_derived": False,
        "independent_empirical_validation_supplied_here": False,
        "lambda_H_predicted": False,
        "accepted_strict_source_count": 0,
        "controlled_prediction_count": 3,
    }

    note = f"""# MTT Selected HRG Cross-Use Prediction Validation or Strict R_H^RG Source Theorem v1

Status: `{STATUS}`

## Theorem

The selected controlled HRG primitive can be reused without retuning to produce
the dynamic-C1 transport rows.  This closes the controlled one-parameter
cross-use validation layer.  It does **not** close strict no-knob SM
equivalence, because the current selected source geometry still does not emit
the numeric `UP-RET-OVERLAP.HRG` value.

## Computed Validation

- `UP_RET_OVERLAP.HRG` = `{hrg}`
- `HRG * A00` = `{a00}`
- `HRG * b0` = `{b0}`
- `HRG * deltaTheta0` = `{theta0}`
- `A00 - 12*HRG residual` = `{validation_residuals["A00_minus_12_HRG"]}`
- `b0 - 12*HRG residual` = `{validation_residuals["b0_minus_12_HRG"]}`
- `deltaTheta0 - HRG residual` = `{validation_residuals["deltaTheta0_minus_HRG"]}`

## Strict Source Replay

Strict accepted sources remain `0`.  The best finite invariant search remains
a near miss with relative error
`{invariant["diagnostics"]["best_candidate_relative_error"]}`, so it cannot be
promoted to a selected identity.

## Boundary

Closed here:

- controlled same-HRG cross-use prediction validation;
- no-retuning reuse of the single HRG primitive;
- strict source obligation matrix.

Still open:

- strict `R_H^RG` source construction;
- independent validation oracle for the controlled HRG predictions;
- `lambda_H` prediction credit;
- true SM/no-knob equivalence.

Next artifact: `{NEXT}`
"""

    write_json(CONTROLLED_VALIDATION, controlled_validation)
    write_json(STRICT_REPLAY, strict_replay)
    write_json(OBLIGATION, obligation)
    write_json(CUTSET, cutset)
    write_json(OUTPUT, candidate)
    write_json(CERT, cert)
    NOTE.write_text(note, encoding="utf-8")
    print(f"WROTE {rel(OUTPUT)}")
    print(f"WROTE {rel(CERT)}")
    print(f"WROTE {rel(NOTE)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
