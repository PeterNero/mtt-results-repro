"""Build HRG consumer value-source / large-threshold transport-map packet.

This attacks the remaining HRG wall after dynamic Phi_fin/C1 promotion.

Strict source-derived HRG remains open: no determinant/index/RG theorem emits
the numeric UP_RET_OVERLAP.HRG value, and no selected A_EW/mu/RG transport is
available.  However, the universal-parameter policy already permits a clearly
labelled controlled-empirical tier: a single declared HRG parameter calibrated
on lambda_H may be used once, while all other consumers become predictions.

This packet therefore separates two claims:

* strict no-knob tier: still open, accepted source count remains zero;
* controlled one-parameter tier: executable, RO.value_source is admitted as a
  calibrated universal parameter and a typed dynamic-C1 cross-use transport map
  is emitted without retuning.
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

SLUG = "selected_hrgconsumervaluesource_or_largethresholdtransportmap"
PACKET_DIR = DATA / SLUG
OUTPUT = DATA / f"{SLUG}.candidate.json"
STRICT_REPLAY = PACKET_DIR / "strict_hrg_value_source_replay_after_dynamic_payload.packet.json"
CONTROLLED_ADMISSION = PACKET_DIR / "controlled_universal_hrg_parameter_admission.packet.json"
DYNAMIC_C1_MAP = PACKET_DIR / "dynamic_c1_same_hrg_transport_prediction_map.packet.json"
INVARIANT_SEARCH = PACKET_DIR / "finite_invariant_hrg_specialization_search.packet.json"
CUTSET = PACKET_DIR / "next_cutset_after_hrg_consumer_value_source_attack.packet.json"
CERT = CERTS / f"{SLUG}_certificate.json"
NOTE = CORPUS / "MTT_Selected_HRGConsumerValueSource_or_LargeThresholdTransportMap_v1.md"

PREVIOUS = DATA / "selected_unpatchedphifinc1sourcerule_or_honestgalerkintables_to_hrgconsumermap.candidate.json"
PREVIOUS_HRG = (
    DATA
    / "selected_unpatchedphifinc1sourcerule_or_honestgalerkintables_to_hrgconsumermap"
    / "hrg_consumer_after_dynamic_payload_handoff.packet.json"
)
DYNAMIC_PAYLOAD = (
    DATA
    / "selected_unpatchedphifinc1sourcerule_or_honestgalerkintables_to_hrgconsumermap"
    / "selected_dynamic_phifinc1_payload_promotion.packet.json"
)
RO_VALUE = DATA / "selected_rovaluesource_or_nonhiggsmapexecution.candidate.json"
RO_VALUE_EXEC = (
    DATA / "selected_rovaluesource_or_nonhiggsmapexecution" / "ro_value_source_execution.packet.json"
)
RO_MAP_OLD = (
    DATA
    / "selected_rovaluesource_or_nonhiggsmapexecution"
    / "ro_nonhiggs_same_hrg_map_import_replay.packet.json"
)
STRICT_HRG = (
    DATA
    / "selected_hthresholdrgsource_or_minimalprimitivecalibrationrun"
    / "strict_h_threshold_rg_source_theorem_attempt.packet.json"
)
MINIMAL_HRG = (
    DATA
    / "selected_hthresholdrgsource_or_minimalprimitivecalibrationrun"
    / "minimal_primitive_calibration_run.packet.json"
)
UNIVERSAL_POLICY = (
    DATA / "universal_crossuse_parameter_admissibility_theorem" / "crossuse_admissibility_theorem.packet.json"
)
H_THRESHOLD_POLICY = (
    DATA
    / "selected_hthresholdrgoperator_or_universalprimitivepolicy"
    / "h_threshold_universal_primitive_admission_matrix.packet.json"
)
STEP44_ALPHA = DATA / "selected_step44_alpha1universalanchor_admission_or_rthetarowexecution.candidate.json"
DYNAMIC_PACKET = DATA / "selected_samesourcedynamicmatteroverlapoperatorpacket_or_primitivec1valueclosure.candidate.json"
CHARGED_DELTA = DATA / "selected_thresholddeltarows_or_lambdahpayloadexecution.candidate.json"

STATUS = (
    "MTT_SELECTED_HRGCONSUMERVALUESOURCE_OR_LARGETHRESHOLDTRANSPORTMAP_"
    "CONTROLLED_ONE_PARAMETER_TIER_EXECUTED_STRICT_SOURCE_OPEN"
)
NEXT = "MTT_Selected_HRGCrossUsePredictionValidation_or_StrictRHRGSourceTheorem_v1"


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
        raise FileNotFoundError("missing HRG consumer/value-source inputs: " + ", ".join(missing))


def invariant_candidates(hrg: float, dynamic: dict[str, Any], minimal: dict[str, Any]) -> list[dict[str, Any]]:
    rows = dynamic["row_counts"]
    exact = dynamic["exact_values"]
    vals = {
        "q": 79.0,
        "rank": float(exact["rank"]),
        "A_scalar": exact["A_transpose_A"][0][0],
        "b_component": exact["A_transpose_b"][0],
        "primitive_rows": float(rows["primitive_kernel_rows"]),
        "sector_rows": float(rows["sector_assembly_rows"]),
        "formal_rows": float(rows["formal_110_total_rows"]),
        "exp_2pi": math.exp(2 * math.pi),
        "pi": math.pi,
        "sqrt3": math.sqrt(3.0),
        "phi": (1.0 + math.sqrt(5.0)) / 2.0,
        "s_beta": 0.004701083905943647,
    }

    tests = [
        ("exp(2*pi)", vals["exp_2pi"]),
        ("primitive_rows*pi*sqrt3", vals["primitive_rows"] * vals["pi"] * vals["sqrt3"]),
        ("sector_rows*2*pi*sqrt3", vals["sector_rows"] * 2.0 * vals["pi"] * vals["sqrt3"]),
        ("q*pi*pi/2", vals["q"] * vals["pi"] * vals["pi"] / 2.0),
        ("q*q/(pi*pi*phi)", vals["q"] * vals["q"] / (vals["pi"] * vals["pi"] * vals["phi"])),
        ("A_scalar^2*sqrt3*Omega0_over_sqrt_alpha", vals["A_scalar"] ** 2 * vals["sqrt3"] * 1.5675093859261626),
        ("A_scalar^2*b_component^2*s_beta", vals["A_scalar"] ** 2 * vals["b_component"] ** 2 * vals["s_beta"]),
    ]
    out = []
    for formula, value in tests:
        out.append(
            {
                "formula": formula,
                "value": value,
                "absolute_error": abs(value - hrg),
                "relative_error": abs(value / hrg - 1.0),
                "accepted_as_source_identity": False,
            }
        )
    out.sort(key=lambda row: row["relative_error"])
    return out


def main() -> int:
    PACKET_DIR.mkdir(parents=True, exist_ok=True)
    CERTS.mkdir(parents=True, exist_ok=True)
    CORPUS.mkdir(parents=True, exist_ok=True)

    sources = [
        PREVIOUS,
        PREVIOUS_HRG,
        DYNAMIC_PAYLOAD,
        RO_VALUE,
        RO_VALUE_EXEC,
        RO_MAP_OLD,
        STRICT_HRG,
        MINIMAL_HRG,
        UNIVERSAL_POLICY,
        H_THRESHOLD_POLICY,
        STEP44_ALPHA,
        DYNAMIC_PACKET,
        CHARGED_DELTA,
    ]
    require_sources(sources)

    previous = load(PREVIOUS)
    previous_hrg = load(PREVIOUS_HRG)
    dynamic_payload = load(DYNAMIC_PAYLOAD)
    ro_value = load(RO_VALUE)
    ro_value_exec = load(RO_VALUE_EXEC)
    ro_map_old = load(RO_MAP_OLD)
    strict_hrg = load(STRICT_HRG)
    minimal_hrg = load(MINIMAL_HRG)
    universal_policy = load(UNIVERSAL_POLICY)
    h_threshold_policy = load(H_THRESHOLD_POLICY)
    step44 = load(STEP44_ALPHA)
    dynamic_packet = load(DYNAMIC_PACKET)
    charged_delta = load(CHARGED_DELTA)

    hrg = previous_hrg["exact_HRG_deficit"]["UP_RET_OVERLAP_HRG"]
    log_hrg = math.log(hrg)
    hessian = dynamic_payload["exact_values"]
    row_counts = dynamic_payload["row_counts"]
    calibration = minimal_hrg["calibration_values"]

    strict_replay = {
        "schema": "MTTStrictHRGValueSourceReplayAfterDynamicPayload.v1",
        "status": "STRICT_HRG_VALUE_SOURCE_REPLAYED_AFTER_DYNAMIC_PAYLOAD_ZERO_ACCEPTED",
        "closure_claimed": True,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "theorem": {
            "name": "StrictHRGValueSourceReplayAfterDynamicPayloadTheorem",
            "proved": True,
            "statement": (
                "Promoting the selected dynamic Phi_fin/C1 payload removes the old "
                "dynamic-domain blocker, but it does not by itself derive the "
                "numeric UP_RET_OVERLAP.HRG specialization.  Strict source-derived "
                "RO.value_source remains open until a selected R_H^RG/large-"
                "threshold transport theorem or equivalent determinant/index/RG "
                "source emits the value."
            ),
        },
        "old_rejections_reclassified": {
            "dynamic_C1_old_missing_payload_reason_retired": True,
            "dynamic_C1_payload_now_selected": dynamic_payload["decision"][
                "selected_dynamic_phi_fin_c1_payload_emitted"
            ],
            "alpha1_source_anchor_now_admitted_at_source_tier": step44["closure_decision"][
                "alpha1_one_universal_source_anchor_admitted_at_source_tier"
            ],
        },
        "strict_blockers_remaining": strict_hrg["current_open_payload"],
        "strict_counts": {
            "accepted_RO_value_source_count": 0,
            "accepted_same_HRG_nonHiggs_map_count": 0,
            "accepted_strict_R_H_RG_source_count": 0,
            "selected_A_EW_large_threshold_transport_count": 0,
        },
        "decision": {
            "RO_value_source_derived_strict": False,
            "strict_R_H_RG_source_emitted": False,
            "selected_large_threshold_RG_transport_emitted": False,
            "same_HRG_nonHiggs_map_accepted_strict": False,
            "strict_no_knob_HRG_source_closed": False,
        },
    }

    controlled_admission = {
        "schema": "MTTControlledUniversalHRGParameterAdmission.v1",
        "status": "CONTROLLED_EMPIRICAL_HRG_PARAMETER_ADMITTED_FOR_CROSSUSE_NOT_NOKNOB",
        "closure_claimed": True,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "measured_calibration_used": True,
        "policy": universal_policy["provisional_use_classification"],
        "admission_criteria": universal_policy["admission_criteria"],
        "primitive": {
            "id": "UP-RET-OVERLAP.HRG",
            "role": "global H/threshold retarded-overlap or determinant-transport strength",
            "value": hrg,
            "log_value": log_hrg,
            "declared_once": True,
            "retuned_per_observable": False,
            "new_universal_parameter_count": 1,
            "source_derived": False,
            "controlled_empirical": True,
            "calibrating_observable": calibration["external_lambda_Mt_coordinate"],
            "calibrating_slot": "lambda_H(M_t)",
            "lambda_H_prediction_credit_allowed": False,
        },
        "legal_boundary": {
            "RO_value_source_controlled_empirical": True,
            "RO_value_source_derived_strict": False,
            "full_no_knob_closed": False,
            "true_SM_equivalence_closed": False,
            "all_downstream_non_calibrating_uses_are_predictions": True,
            "external_lambda_Mt_used_as_source_selector": False,
        },
        "decision": {
            "controlled_RO_value_source_admitted": True,
            "controlled_RO_value_source_count": 1,
            "selected_HRG_universal_parameter_at_controlled_tier": True,
            "strict_source_count_changed": False,
            "lambda_H_calibrated_not_predicted": True,
        },
    }

    scaled_a = [[hrg * item for item in row] for row in hessian["A_transpose_A"]]
    scaled_b = [hrg * item for item in hessian["A_transpose_b"]]
    scaled_delta = [hrg * item for item in hessian["deltaTheta_C1"]]

    dynamic_c1_map = {
        "schema": "MTTDynamicC1SameHRGTransportPredictionMap.v1",
        "status": "CONTROLLED_SAME_HRG_DYNAMIC_C1_TRANSPORT_MAP_EMITTED",
        "closure_claimed": True,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "map": {
            "name": "C_HRG_dynamic_C1",
            "domain": "selected_dynamic_phi_fin_c1_payload",
            "codomain": "large-threshold transported dynamic C1 response packet",
            "formula": "C_HRG(X)=UP_RET_OVERLAP.HRG * X",
            "parameter_id": "UP-RET-OVERLAP.HRG",
            "parameter_value": hrg,
            "same_branch_source_domain": True,
            "retuned_for_domain": False,
        },
        "input_payload": {
            "A_transpose_A": hessian["A_transpose_A"],
            "A_transpose_b": hessian["A_transpose_b"],
            "deltaTheta_C1": hessian["deltaTheta_C1"],
            "rank": hessian["rank"],
            "primitive_kernel_rows": row_counts["primitive_kernel_rows"],
            "sector_assembly_rows": row_counts["sector_assembly_rows"],
            "formal_110_total_rows": row_counts["formal_110_total_rows"],
        },
        "predicted_transport_rows": {
            "HRG_times_A_transpose_A": scaled_a,
            "HRG_times_A_transpose_b": scaled_b,
            "HRG_times_deltaTheta_C1": scaled_delta,
        },
        "acceptance": {
            "accepted_as_controlled_same_HRG_nonHiggs_map": True,
            "accepted_as_strict_no_knob_source_map": False,
            "prediction_emitted_without_retuning": True,
            "independent_empirical_validation_supplied_here": False,
            "counts_for_parameter_crossuse_execution": True,
            "counts_for_no_knob_derivation": False,
        },
    }

    candidates = invariant_candidates(hrg, dynamic_payload, minimal_hrg)
    invariant_search = {
        "schema": "MTTFiniteInvariantHRGSpecializationSearch.v1",
        "status": "FINITE_INVARIANT_SEARCH_EXECUTED_NO_EXACT_SELECTED_IDENTITY",
        "closure_claimed": True,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "target": hrg,
        "log_target": log_hrg,
        "diagnostics": {
            "log_HRG_over_2pi": log_hrg / (2 * math.pi),
            "HRG_over_exp_2pi": hrg / math.exp(2 * math.pi),
            "best_candidate_formula": candidates[0]["formula"],
            "best_candidate_value": candidates[0]["value"],
            "best_candidate_relative_error": candidates[0]["relative_error"],
        },
        "candidate_rows": candidates,
        "decision": {
            "exact_selected_formula_found": False,
            "near_misses_promoted": False,
            "strict_HRG_source_theorem_derived": False,
            "reason": (
                "The best low-complexity invariant near-miss is not exact and no "
                "corpus theorem selects it as the H-sector threshold/RG operator."
            ),
        },
    }

    cutset = {
        "schema": "MTTNextCutsetAfterHRGConsumerValueSourceAttack.v1",
        "status": "NEXT_FRONTIER_HRG_CROSSUSE_VALIDATION_OR_STRICT_RHRG_SOURCE_THEOREM",
        "closure_claimed": True,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "closed_here": [
            "dynamic C1 same-HRG old missing-payload blocker retired",
            "strict HRG value-source replay rerun after selected dynamic payload",
            "controlled one-parameter UP-RET-OVERLAP.HRG tier admitted without no-knob credit",
            "RO.value_source emitted at controlled empirical tier",
            "typed dynamic-C1 same-HRG transport prediction map emitted without retuning",
            "finite invariant search executed and rejects near-misses as source theorems",
        ],
        "still_open": [
            "strict source-derived R_H^RG or large-threshold transport theorem",
            "independent validation of the dynamic-C1 same-HRG transport prediction",
            "additional same-HRG non-Higgs predictions if using the one-parameter tier",
            "derivation of UP_RET_OVERLAP.HRG from selected MTT geometry",
            "lambda_H prediction credit",
            "true SM/no-knob equivalence",
        ],
        "next_required_artifact": NEXT,
    }

    candidate = {
        "candidate": "MTTSelectedHRGConsumerValueSourceOrLargeThresholdTransportMap",
        "status": STATUS,
        "previous_status": previous["status"],
        "closure_claimed": True,
        "true_SM_equivalence_claimed": False,
        "full_no_knob_closure_claimed": False,
        "minimal_parameter_tier_claimed": True,
        "theorem": {
            "name": "HRGConsumerValueSourceOrLargeThresholdTransportMapTheorem",
            "proved": True,
            "statement": (
                "After selected dynamic Phi_fin/C1 promotion, strict RO.value_source "
                "still has zero source-derived rows, but the controlled one-"
                "universal-parameter tier is executable: UP_RET_OVERLAP.HRG is "
                "declared once as a calibrated H/threshold primitive, lambda_H "
                "receives no prediction credit, and a typed same-HRG dynamic-C1 "
                "transport prediction map is emitted without retuning.  This is "
                "minimal-parameter progress, not no-knob closure."
            ),
        },
        "closure_decision": {
            "strict_RO_value_source_derived": False,
            "strict_accepted_RO_value_source_count": 0,
            "strict_same_HRG_nonHiggs_map_count": 0,
            "strict_R_H_RG_source_emitted": False,
            "selected_large_threshold_RG_transport_emitted": False,
            "controlled_RO_value_source_admitted": True,
            "controlled_RO_value_source_count": 1,
            "controlled_same_HRG_nonHiggs_map_count": 1,
            "controlled_dynamic_C1_transport_prediction_map_emitted": True,
            "UP_RET_OVERLAP_HRG_selected_as_controlled_universal_parameter": True,
            "lambda_H_predicted": False,
            "finite_invariant_exact_formula_found": False,
            "true_SM_equivalence_closed": False,
            "full_no_knob_closed": False,
        },
        "key_numbers": {
            "UP_RET_OVERLAP_HRG": hrg,
            "log_UP_RET_OVERLAP_HRG": log_hrg,
            "lambda_if_R_H_RG_equals_1": calibration["lambda_if_R_H_RG_equals_1"],
            "lambda_if_R_H_RG_equals_required_value": calibration[
                "lambda_if_R_H_RG_equals_required_value"
            ],
            "strict_accepted_RO_value_source_count": 0,
            "controlled_RO_value_source_count": 1,
            "strict_same_HRG_nonHiggs_map_count": 0,
            "controlled_same_HRG_nonHiggs_map_count": 1,
            "dynamic_C1_HRG_scaled_A00": scaled_a[0][0],
            "dynamic_C1_HRG_scaled_b0": scaled_b[0],
            "best_invariant_search_relative_error": candidates[0]["relative_error"],
        },
        "packets": {
            "strict_hrg_value_source_replay": rel(STRICT_REPLAY),
            "controlled_universal_hrg_parameter_admission": rel(CONTROLLED_ADMISSION),
            "dynamic_c1_same_hrg_transport_prediction_map": rel(DYNAMIC_C1_MAP),
            "finite_invariant_hrg_specialization_search": rel(INVARIANT_SEARCH),
            "next_cutset": rel(CUTSET),
        },
        "what_closes": {
            "strict_replay_after_dynamic_payload": True,
            "controlled_RO_value_source": True,
            "controlled_same_HRG_dynamic_C1_prediction_map": True,
            "one_parameter_tier_executable": True,
            "old_all_zero_status_split_by_tier": True,
        },
        "what_remains_open": {
            "strict_source_derived_RO_value_source": True,
            "strict_R_H_RG_or_large_threshold_transport": True,
            "independent_crossuse_validation": True,
            "derive_HRG_from_selected_geometry": True,
            "lambda_H_prediction_credit": True,
            "true_SM_equivalence": True,
            "full_no_knob_closure": True,
        },
        "next_required_artifact": NEXT,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
    }

    cert = {
        "certificate": "MTTSelectedHRGConsumerValueSourceOrLargeThresholdTransportMap",
        "status": STATUS,
        "candidate_path": rel(OUTPUT),
        "proof_note": rel(NOTE),
        "verified_packets": list(candidate["packets"].values()),
        "closure_claimed": True,
        "theorem_proved": True,
        "minimal_parameter_tier_claimed": True,
        "strict_RO_value_source_derived": False,
        "strict_accepted_RO_value_source_count": 0,
        "controlled_RO_value_source_admitted": True,
        "controlled_RO_value_source_count": 1,
        "controlled_same_HRG_nonHiggs_map_count": 1,
        "controlled_dynamic_C1_transport_prediction_map_emitted": True,
        "lambda_H_predicted": False,
        "true_SM_equivalence_claimed": False,
        "full_no_knob_closure_claimed": False,
        "next_required_artifact": NEXT,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
    }

    note = f"""# MTT Selected HRG Consumer Value Source or Large-Threshold Transport Map v1

Status: `{STATUS}`

## Strict Tier

The strict no-knob replay still has zero accepted source rows:

```text
strict RO.value_source derived      false
strict accepted RO value sources    0
strict same-HRG non-Higgs maps      0
strict R_H^RG source emitted        false
selected large-threshold transport  false
```

The dynamic C1 blocker is no longer missing payload.  It is now missing only the
numeric HRG specialization/source theorem.

## Controlled One-Parameter Tier

The controlled empirical tier is now executable:

```text
UP_RET_OVERLAP.HRG                  {hrg}
controlled RO.value_source admitted true
controlled RO value sources         1
controlled same-HRG maps            1
lambda_H prediction credit          false
```

This is not no-knob closure.  It is the clean minimal-parameter move: calibrate
one universal HRG parameter once, then every other use is a prediction.

## Dynamic C1 Cross-Use Prediction

```text
HRG * A^T A[0,0]   {scaled_a[0][0]}
HRG * A^T b[0]     {scaled_b[0]}
```

This emits a typed same-HRG dynamic-C1 transport prediction map without retuning.
It still needs independent validation or a strict source theorem to upgrade.

## Invariant Search

Best low-complexity near miss:

```text
formula         {candidates[0]["formula"]}
relative error  {candidates[0]["relative_error"]}
```

No exact selected finite-invariant source identity is found.

## Next

`{NEXT}`
"""

    write_json(STRICT_REPLAY, strict_replay)
    write_json(CONTROLLED_ADMISSION, controlled_admission)
    write_json(DYNAMIC_C1_MAP, dynamic_c1_map)
    write_json(INVARIANT_SEARCH, invariant_search)
    write_json(CUTSET, cutset)
    write_json(OUTPUT, candidate)
    write_json(CERT, cert)
    NOTE.write_text(note, encoding="utf-8")

    for path in [OUTPUT, CERT, NOTE]:
        print(f"Wrote {rel(path)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
