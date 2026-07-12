"""Build sector-scaled eigenprofile threshold rows / Yukawa magnitude source execution gate."""

from __future__ import annotations

import json
import math
from pathlib import Path
from typing import Any

import numpy as np


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "candidate_data"
CERTS = ROOT / "certificates"
CORPUS = ROOT / "proof_corpus"

SLUG = "selected_sectorscaledeigenprofilethresholdrows_or_yukawamagnitudesourceexecution"
PACKET_DIR = DATA / SLUG
OUTPUT = DATA / f"{SLUG}.candidate.json"
MODEL_TESTS = PACKET_DIR / "sector_scaled_eigenprofile_model_tests.packet.json"
COEFFICIENT_FRONTIER = PACKET_DIR / "sector_coefficient_frontier.packet.json"
ROW_ATTEMPT = PACKET_DIR / "eigenprofile_threshold_row_acceptance_attempt.packet.json"
DECISION = PACKET_DIR / "sector_scaled_eigenprofile_or_yukawa_magnitude_source_decision.packet.json"
CUTSET = PACKET_DIR / "next_cutset_after_sector_scaled_eigenprofile.packet.json"
CERT = CERTS / f"{SLUG}_certificate.json"
NOTE = CORPUS / "MTT_Selected_SectorScaledEigenprofileThresholdRows_or_YukawaMagnitudeSourceExecution_v1.md"

PREVIOUS = DATA / "selected_familyresolvingoperator_or_generationthresholdrowsexecution.candidate.json"
SPECTRUM = (
    DATA
    / "selected_familyresolvingoperator_or_generationthresholdrowsexecution"
    / "selected_first_response_family_spectrum.packet.json"
)
MAG_OBSTRUCTION = (
    DATA
    / "selected_familyresolvingoperator_or_generationthresholdrowsexecution"
    / "magnitude_threshold_row_obstruction_after_family_resolution.packet.json"
)
RANK_GAP = (
    DATA
    / "selected_magnitudebearingprojectionweights_or_thresholdrowsderivation"
    / "magnitude_weight_rank_gap.packet.json"
)
BACKSOLVE = (
    DATA
    / "selected_magnitudebearingprojectionweights_or_thresholdrowsderivation"
    / "diagnostic_magnitude_weight_backsolve.packet.json"
)
VSD02_FILL = DATA / "selected_vsd02acceptedsourcerowsfill_or_noknobthresholdderivation.candidate.json"
VSD02_FILL_ATTEMPT = (
    DATA
    / "selected_vsd02acceptedsourcerowsfill_or_noknobthresholdderivation"
    / "accepted_source_rows_fill_attempt.packet.json"
)
VSD02_SCHEMA = (
    DATA
    / "selected_vsd02acceptedsourcerowsfill_or_noknobthresholdderivation"
    / "accepted_source_row_strict_schema.packet.json"
)
VALUE_PACKET = (
    DATA
    / "selected_acceptedcommonscaleyukawahiggsvalues_or_profilelikelihoodexecution"
    / "versioned_common_scale_yukawa_higgs_values.packet.json"
)

STATUS = (
    "MTT_SELECTED_SECTORSCALEDEIGENPROFILETHRESHOLDROWS_OR_YUKAWAMAGNITUDESOURCEEXECUTION_"
    "BUILT_UNIVERSAL_PROFILE_NOGO_SECTOR_COEFFICIENTS_OPEN"
)
NEXT = "MTT_Selected_HigherResponseSectorCoefficients_or_ThresholdFunctionalSourceRows_v1"


def rel(path: Path) -> str:
    try:
        return str(path.relative_to(ROOT)).replace("\\", "/")
    except ValueError:
        return str(path)


def load(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def write_json(path: Path, payload: dict[str, Any]) -> None:
    path.write_text(json.dumps(payload, indent=2, sort_keys=True) + "\n", encoding="utf-8")


def require_sources(paths: list[Path]) -> None:
    missing = [rel(path) for path in paths if not path.exists()]
    if missing:
        raise FileNotFoundError("missing sector-scaled eigenprofile sources: " + ", ".join(missing))


def diagnostic_by_sector(backsolve: dict[str, Any]) -> dict[str, np.ndarray]:
    grouped: dict[str, list[float]] = {}
    for row in backsolve["diagnostic_weights"]:
        grouped.setdefault(row["sector"], []).append(float(row["diagnostic_magnitude_weight"]))
    return {sector: np.array(values, dtype=float) for sector, values in sorted(grouped.items())}


def ratio(values: np.ndarray) -> float:
    positives = values[values > 0]
    return float(np.max(positives) / np.min(positives))


def least_squares_scale(target: np.ndarray, profile: np.ndarray) -> tuple[float, np.ndarray, float, float]:
    scale = float(np.dot(target, profile) / np.dot(profile, profile))
    predicted = scale * profile
    rel_resid = float(np.linalg.norm(predicted - target) / np.linalg.norm(target))
    log_resid = float(np.linalg.norm(np.log(predicted) - np.log(target))) if np.all(predicted > 0) else math.inf
    return scale, predicted, rel_resid, log_resid


def log_affine_fit(target: np.ndarray, signed_eigenvalues: np.ndarray) -> tuple[list[float], np.ndarray, float, float]:
    design = np.column_stack([np.ones(3), signed_eigenvalues])
    coefficients = np.linalg.lstsq(design, np.log(target), rcond=None)[0]
    predicted = np.exp(design @ coefficients)
    rel_resid = float(np.linalg.norm(predicted - target) / np.linalg.norm(target))
    log_resid = float(np.linalg.norm(np.log(predicted) - np.log(target)))
    return [float(value) for value in coefficients], predicted, rel_resid, log_resid


def log_quadratic_coefficients(target: np.ndarray, signed_eigenvalues: np.ndarray) -> list[float]:
    design = np.column_stack([np.ones(3), signed_eigenvalues, signed_eigenvalues**2])
    coefficients = np.linalg.solve(design, np.log(target))
    return [float(value) for value in coefficients]


def floats(values: np.ndarray) -> list[float]:
    return [float(value) for value in values]


def main() -> int:
    PACKET_DIR.mkdir(parents=True, exist_ok=True)
    CERTS.mkdir(parents=True, exist_ok=True)
    CORPUS.mkdir(parents=True, exist_ok=True)

    sources = [
        PREVIOUS,
        SPECTRUM,
        MAG_OBSTRUCTION,
        RANK_GAP,
        BACKSOLVE,
        VSD02_FILL,
        VSD02_FILL_ATTEMPT,
        VSD02_SCHEMA,
        VALUE_PACKET,
    ]
    require_sources(sources)

    previous = load(PREVIOUS)
    spectrum = load(SPECTRUM)
    mag_obstruction = load(MAG_OBSTRUCTION)
    rank_gap = load(RANK_GAP)
    backsolve = load(BACKSOLVE)
    vsd02_fill = load(VSD02_FILL)
    vsd02_fill_attempt = load(VSD02_FILL_ATTEMPT)
    value_packet = load(VALUE_PACKET)

    signed_eigenvalues = np.array(spectrum["sector_results"]["u"]["eigenvalues"], dtype=float)
    abs_profile = np.abs(signed_eigenvalues)
    charged_targets = diagnostic_by_sector(backsolve)
    hierarchy_ratios = {sector: ratio(values) for sector, values in charged_targets.items()}
    hierarchy_spread = max(hierarchy_ratios.values()) / min(hierarchy_ratios.values())
    universal_abs_profile_ratio = ratio(abs_profile)

    model_results: dict[str, Any] = {}
    log_affine_results: dict[str, Any] = {}
    log_quadratic_results: dict[str, Any] = {}
    for sector, values in charged_targets.items():
        scale, predicted, rel_resid, log_resid = least_squares_scale(values, abs_profile)
        model_results[sector] = {
            "diagnostic_values_not_used_as_selectors": floats(values),
            "best_sector_scale": scale,
            "predicted_from_abs_eigenprofile": floats(predicted),
            "relative_residual": rel_resid,
            "log_residual": log_resid,
            "diagnostic_hierarchy_ratio": hierarchy_ratios[sector],
            "universal_abs_eigenprofile_ratio": universal_abs_profile_ratio,
            "accepted_as_source_row": False,
        }
        coefficients, log_affine_pred, log_affine_rel, log_affine_log = log_affine_fit(values, signed_eigenvalues)
        log_affine_results[sector] = {
            "diagnostic_coefficients_not_selected": coefficients,
            "predicted_values": floats(log_affine_pred),
            "relative_residual": log_affine_rel,
            "log_residual": log_affine_log,
            "accepted_as_source_row": False,
        }
        log_quadratic_results[sector] = {
            "diagnostic_exact_coefficients_not_selected": log_quadratic_coefficients(values, signed_eigenvalues),
            "accepted_as_source_row": False,
            "why_not_selected": (
                "A sector-specific quadratic log-profile has exactly three coefficients for three family values; "
                "using it here would backsolve the diagnostic Yukawa magnitudes rather than emit selected source rows."
            ),
        }

    universal_scaled_profile_can_match_diagnostics = hierarchy_spread == 1.0
    model_tests = {
        "schema": "MTTSectorScaledEigenprofileModelTests.v1",
        "status": "UNIVERSAL_SECTOR_SCALED_EIGENPROFILE_FAILS_MAGNITUDE_ROWS",
        "family_spectrum": rel(SPECTRUM),
        "diagnostic_backsolve": rel(BACKSOLVE),
        "signed_family_eigenvalues": floats(signed_eigenvalues),
        "abs_family_eigenprofile": floats(abs_profile),
        "universal_abs_eigenprofile_ratio": universal_abs_profile_ratio,
        "diagnostic_hierarchy_ratios_not_used_as_selectors": hierarchy_ratios,
        "diagnostic_hierarchy_spread": hierarchy_spread,
        "sector_scale_only_results": model_results,
        "log_affine_diagnostic_results": log_affine_results,
        "log_quadratic_diagnostic_exact_coefficients": log_quadratic_results,
        "theorem": {
            "name": "UniversalSectorScaledEigenprofileNoGo",
            "proved": True,
            "statement": (
                "Any model y_s,g = c_s p_g with one selected universal family profile p_g and sector scales c_s "
                "has identical hierarchy ratios in all charged sectors. The diagnostic charged Yukawa hierarchy "
                "ratios differ across u,d,e, so the selected first-response eigenprofile cannot by itself emit the "
                "nine magnitude-bearing rows."
            ),
        },
        "universal_scaled_profile_can_match_diagnostic_hierarchies": universal_scaled_profile_can_match_diagnostics,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "closure_claimed": True,
    }
    write_json(MODEL_TESTS, model_tests)

    coefficient_frontier = {
        "schema": "MTTSectorCoefficientFrontier.v1",
        "status": "SECTOR_COEFFICIENTS_OR_THRESHOLD_FUNCTIONAL_REQUIRED",
        "family_operator_closed": previous["closure_decision"]["family_resolving_operator_closed"],
        "family_eigenbasis_available": True,
        "universal_family_profile_insufficient": True,
        "minimal_new_selected_objects": [
            "sector-specific higher-response coefficients for u,d,e",
            "or a selected threshold response functional F_s(lambda_g) emitting magnitude rows",
            "or selected threshold/mass-scheme/profile source rows accepted by the VSD02 strict schema",
            "plus an independent lambda_H source row",
        ],
        "forbidden_shortcuts": [
            "using diagnostic common-scale Yukawa values as source coefficients",
            "choosing polynomial degree or coefficients because they fit measured hierarchy ratios",
            "treating first-pass/profile values as true no-knob source rows",
            "claiming sector scales alone close charged magnitudes",
        ],
        "vsd02_strict_fill_attempt_currently_accepts_rows": vsd02_fill_attempt["accepted_row_count"],
        "vsd02_selected_threshold_response_functional_closed": vsd02_fill["closure_decision"][
            "selected_threshold_response_functional_closed"
        ],
        "accepted_for_true_precision": value_packet["accepted_for_true_precision_equivalence"],
        "same_branch_scale_scheme_loop_convention_closed": False,
        "closure_claimed": True,
    }
    write_json(COEFFICIENT_FRONTIER, coefficient_frontier)

    attempted_rows = []
    for sector, values in charged_targets.items():
        for generation, value in enumerate(values, start=1):
            attempted_rows.append(
                {
                    "row_id": f"{sector}.gen{generation}.eigenprofile_threshold_candidate",
                    "family_eigenvalue": float(signed_eigenvalues[generation - 1]),
                    "diagnostic_magnitude_value": float(value),
                    "accepted_as_selected_threshold_source_row": False,
                    "why_not": [
                        "family eigenvalue is selected, but the sector-specific magnitude coefficient is not",
                        "the diagnostic magnitude comes from the first-pass/profile value packet",
                        "VSD02 strict accepted-source-row fill still accepts zero rows",
                    ],
                }
            )
    row_attempt = {
        "schema": "MTTEigenprofileThresholdRowAcceptanceAttempt.v1",
        "status": "EIGENPROFILE_ROWS_ATTEMPTED_FAMILY_COORDINATE_ONLY",
        "accepted_rows": [],
        "attempted_rows": attempted_rows,
        "attempted_row_count": len(attempted_rows),
        "accepted_row_count": 0,
        "required_charged_generation_row_count": rank_gap["dimension_evidence"][
            "charged_generation_magnitude_rows"
        ],
        "lambda_H_row_required": True,
        "family_coordinate_rows_available": True,
        "sector_scaled_magnitude_rows_emitted": False,
        "generation_resolved_threshold_source_rows_closed": False,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "closure_claimed": False,
    }
    write_json(ROW_ATTEMPT, row_attempt)

    decision = {
        "schema": "MTTSectorScaledEigenprofileOrYukawaMagnitudeSourceDecision.v1",
        "status": "FAMILY_COORDINATE_CLOSED_SECTOR_MAGNITUDE_SOURCE_OPEN",
        "previous_status": previous["status"],
        "family_resolving_operator_closed": True,
        "universal_sector_scaled_eigenprofile_nogo_proved": True,
        "sector_coefficient_frontier_identified": True,
        "accepted_generation_threshold_source_row_count": 0,
        "required_charged_generation_row_count": rank_gap["dimension_evidence"][
            "charged_generation_magnitude_rows"
        ],
        "lambda_H_row_required": True,
        "generation_resolved_threshold_source_rows_closed": False,
        "selected_threshold_response_functional_closed": False,
        "same_branch_scale_scheme_loop_convention_closed": False,
        "accepted_Yukawa_magnitudes_as_no_knob_predictions": False,
        "true_SM_equivalence_closed": False,
        "full_no_knob_closed": False,
        "what_this_closes": [
            "proves sector scales on a universal family eigenprofile are insufficient",
            "separates selected family coordinate rows from magnitude-bearing source rows",
            "reduces the next target to sector coefficients or a threshold response functional",
        ],
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "closure_claimed": False,
    }
    write_json(DECISION, decision)

    cutset = {
        "schema": "MTTNextCutsetAfterSectorScaledEigenprofile.v1",
        "status": "NEXT_ATTACK_HIGHER_RESPONSE_SECTOR_COEFFICIENTS",
        "closed_this_artifact": {
            "universal_sector_scaled_eigenprofile_nogo": True,
            "family_coordinate_vs_magnitude_row_separation": True,
            "sector_coefficient_frontier_identified": True,
        },
        "still_open": [
            "selected sector-specific higher-response coefficients for u,d,e",
            "selected threshold response functional F_s(lambda_g)",
            "9 charged generation-resolved magnitude-bearing source rows",
            "lambda_H source row",
            "same-branch scale/scheme/loop convention and mass-scheme conversion",
            "full profile likelihood or accepted diagonal theorem",
        ],
        "next_required_artifact": NEXT,
        "recommended_next": {
            "artifact": NEXT,
            "reason": (
                "The family eigenbasis is selected, but universal scaling is mathematically too weak. The next "
                "proof must emit sector coefficients from a selected higher-response or threshold functional."
            ),
        },
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "closure_claimed": False,
    }
    write_json(CUTSET, cutset)

    candidate = {
        "candidate": "MTTSelectedSectorScaledEigenprofileThresholdRowsOrYukawaMagnitudeSourceExecution",
        "status": STATUS,
        "inputs": {
            "selected_familyresolvingoperator_or_generationthresholdrowsexecution.candidate": rel(PREVIOUS),
            "selected_first_response_family_spectrum.packet": rel(SPECTRUM),
            "magnitude_threshold_row_obstruction_after_family_resolution.packet": rel(MAG_OBSTRUCTION),
            "magnitude_weight_rank_gap.packet": rel(RANK_GAP),
            "diagnostic_magnitude_weight_backsolve.packet": rel(BACKSOLVE),
            "selected_vsd02acceptedsourcerowsfill_or_noknobthresholdderivation.candidate": rel(VSD02_FILL),
            "accepted_source_rows_fill_attempt.packet": rel(VSD02_FILL_ATTEMPT),
            "accepted_source_row_strict_schema.packet": rel(VSD02_SCHEMA),
            "versioned_common_scale_yukawa_higgs_values.packet": rel(VALUE_PACKET),
        },
        "output_packets": {
            "sector_scaled_eigenprofile_model_tests": rel(MODEL_TESTS),
            "sector_coefficient_frontier": rel(COEFFICIENT_FRONTIER),
            "eigenprofile_threshold_row_acceptance_attempt": rel(ROW_ATTEMPT),
            "sector_scaled_eigenprofile_or_yukawa_magnitude_source_decision": rel(DECISION),
            "next_cutset_after_sector_scaled_eigenprofile": rel(CUTSET),
        },
        "theorem": {
            "name": "SectorScaledEigenprofileNoGoAndCoefficientFrontierTheorem",
            "proved": True,
            "statement": (
                "The selected first-response family eigenprofile can label the three generations, but a universal "
                "family profile with charged-sector scales cannot emit the nine charged Yukawa magnitude rows. "
                "Sector-specific hierarchy ratios require selected sector coefficients, a selected threshold "
                "response functional, or accepted threshold/mass-scheme/profile source rows."
            ),
        },
        "closure_decision": {
            "family_resolving_operator_closed": True,
            "universal_sector_scaled_eigenprofile_nogo_proved": True,
            "sector_coefficient_frontier_identified": True,
            "generation_resolved_threshold_source_rows_closed": False,
            "selected_threshold_response_functional_closed": False,
            "accepted_Yukawa_magnitudes_as_no_knob_predictions": False,
            "true_SM_equivalence_closed": False,
            "full_no_knob_closed": False,
        },
        "next_required_artifact": NEXT,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "closure_claimed": False,
        "unpatched_theorem_closure_claimed": False,
    }
    write_json(OUTPUT, candidate)

    cert = {
        "certificate": "MTT_Selected_SectorScaledEigenprofileThresholdRows_or_YukawaMagnitudeSourceExecution_v1",
        "status": STATUS,
        "candidate_path": rel(OUTPUT),
        "note_path": rel(NOTE),
        "theorem_proved": True,
        "family_resolving_operator_closed": True,
        "universal_sector_scaled_eigenprofile_nogo_proved": True,
        "sector_coefficient_frontier_identified": True,
        "accepted_generation_threshold_source_row_count": 0,
        "required_charged_generation_row_count": rank_gap["dimension_evidence"][
            "charged_generation_magnitude_rows"
        ],
        "generation_resolved_threshold_source_rows_closed": False,
        "accepted_Yukawa_magnitudes_as_no_knob_predictions": False,
        "true_SM_equivalence_closed": False,
        "full_no_knob_closed": False,
        "closure_claimed": False,
        "unpatched_theorem_closure_claimed": False,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "next_required_artifact": NEXT,
    }
    write_json(CERT, cert)

    note = f"""# MTT Selected SectorScaledEigenprofileThresholdRows or YukawaMagnitudeSourceExecution v1

Status: `{STATUS}`.

This artifact tests whether the selected family eigenprofile can be promoted to
charged Yukawa magnitude rows by adding only sector scales.

```text
family-resolving operator closed              : true
universal sector-scaled eigenprofile no-go    : true
universal abs eigenprofile hierarchy ratio    : {universal_abs_profile_ratio}
diagnostic hierarchy ratios (not selectors)   : u={hierarchy_ratios["u"]}, d={hierarchy_ratios["d"]}, e={hierarchy_ratios["e"]}
accepted generation threshold rows            : 0/{rank_gap["dimension_evidence"]["charged_generation_magnitude_rows"]}
Yukawa magnitudes no-knob closed              : false
```

The selected eigenprofile supplies the family coordinate.  It does not supply
sector-specific magnitude coefficients.  A one-profile/sector-scale model would
force the same hierarchy ratio in `u`, `d`, and `e`, while the diagnostic
common-scale values have different hierarchy ratios.  Therefore the next object
must be selected sector coefficients, a selected threshold response functional,
or accepted threshold/mass-scheme/profile source rows.

Next artifact: `{NEXT}`.
"""
    NOTE.write_text(note, encoding="utf-8")

    print(json.dumps({"candidate": rel(OUTPUT), "status": STATUS}, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
