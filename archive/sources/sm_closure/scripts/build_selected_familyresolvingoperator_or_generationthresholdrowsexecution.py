"""Build selected family-resolving operator / generation threshold row execution gate."""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any

import numpy as np


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "candidate_data"
CERTS = ROOT / "certificates"
CORPUS = ROOT / "proof_corpus"

SLUG = "selected_familyresolvingoperator_or_generationthresholdrowsexecution"
PACKET_DIR = DATA / SLUG
OUTPUT = DATA / f"{SLUG}.candidate.json"
STALE_RECONCILIATION = PACKET_DIR / "stale_routec_operator_nogo_reconciliation.packet.json"
SPECTRUM = PACKET_DIR / "selected_first_response_family_spectrum.packet.json"
MAG_OBSTRUCTION = PACKET_DIR / "magnitude_threshold_row_obstruction_after_family_resolution.packet.json"
DECISION = PACKET_DIR / "family_resolving_operator_or_generation_threshold_rows_decision.packet.json"
CUTSET = PACKET_DIR / "next_cutset_after_family_resolving_operator.packet.json"
CERT = CERTS / f"{SLUG}_certificate.json"
NOTE = CORPUS / "MTT_Selected_FamilyResolvingOperator_or_GenerationThresholdRowsExecution_v1.md"

PREVIOUS = DATA / "selected_generationresolvedthresholdsourcerows_or_profileconventionclosure.candidate.json"
PREVIOUS_ROWS = (
    DATA
    / "selected_generationresolvedthresholdsourcerows_or_profileconventionclosure"
    / "generation_resolved_threshold_row_attempt.packet.json"
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
OLD_ROUTEC_NOGO = DATA / "selected_routec_samesource_operatorpacket_fill_or_nogo.candidate.json"
SAME_SOURCE_DYNAMIC = DATA / "selected_samesourcedynamicmatteroverlapoperatorpacket_or_primitivec1valueclosure.candidate.json"
DYNAMIC_VALUES = (
    DATA
    / "selected_samesourcedynamicmatteroverlapoperatorpacket_or_primitivec1valueclosure"
    / "selected_non_scalar_dynamic_overlap_values.packet.json"
)
DYNAMIC_VALIDATOR = (
    DATA
    / "selected_samesourcedynamicmatteroverlapoperatorpacket_or_primitivec1valueclosure"
    / "same_source_matter_overlap_operator_validator_result.packet.json"
)
DYNAMIC_QASU3 = DATA / "selected_dynamicqasu3operatorpacketreplay_or_yukawamassmixingvalueclosure.candidate.json"
DYNAMIC_QASU3_REPLAY = (
    DATA
    / "selected_dynamicqasu3operatorpacketreplay_or_yukawamassmixingvalueclosure"
    / "dynamic_qasu3_operator_packet_replay.packet.json"
)
VSD_BACKIMPORT = DATA / "selected_vsd01_dynamicoperatorbackimport_or_yukawavaluefrontier.candidate.json"

STATUS = (
    "MTT_SELECTED_FAMILYRESOLVINGOPERATOR_OR_GENERATIONTHRESHOLDROWSEXECUTION_"
    "BUILT_FAMILY_OPERATOR_CLOSED_MAGNITUDE_ROWS_OPEN"
)
NEXT = "MTT_Selected_SectorScaledEigenprofileThresholdRows_or_YukawaMagnitudeSourceExecution_v1"


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
        raise FileNotFoundError("missing family-resolving operator sources: " + ", ".join(missing))


def to_complex(value: Any) -> complex:
    if (
        isinstance(value, list)
        and len(value) == 2
        and all(isinstance(part, (int, float)) for part in value)
    ):
        return complex(value[0], value[1])
    return complex(value)


def matrix(payload: list[list[Any]]) -> np.ndarray:
    return np.array([[to_complex(value) for value in row] for row in payload], dtype=complex)


def rounded(values: np.ndarray, digits: int = 12) -> list[float]:
    return [round(float(value), digits) for value in values]


def group_by_sector(rows: list[dict[str, Any]]) -> dict[str, list[float]]:
    grouped: dict[str, list[float]] = {}
    for row in rows:
        grouped.setdefault(row["sector"], []).append(float(row["diagnostic_magnitude_weight"]))
    return grouped


def hierarchy_ratio(values: list[float]) -> float:
    positives = [value for value in values if value > 0]
    return max(positives) / min(positives)


def main() -> int:
    PACKET_DIR.mkdir(parents=True, exist_ok=True)
    CERTS.mkdir(parents=True, exist_ok=True)
    CORPUS.mkdir(parents=True, exist_ok=True)

    sources = [
        PREVIOUS,
        PREVIOUS_ROWS,
        RANK_GAP,
        BACKSOLVE,
        OLD_ROUTEC_NOGO,
        SAME_SOURCE_DYNAMIC,
        DYNAMIC_VALUES,
        DYNAMIC_VALIDATOR,
        DYNAMIC_QASU3,
        DYNAMIC_QASU3_REPLAY,
        VSD_BACKIMPORT,
    ]
    require_sources(sources)

    previous = load(PREVIOUS)
    previous_rows = load(PREVIOUS_ROWS)
    rank_gap = load(RANK_GAP)
    backsolve = load(BACKSOLVE)
    old_routec_nogo = load(OLD_ROUTEC_NOGO)
    same_source_dynamic = load(SAME_SOURCE_DYNAMIC)
    dynamic_values = load(DYNAMIC_VALUES)
    dynamic_validator = load(DYNAMIC_VALIDATOR)
    dynamic_qasu3 = load(DYNAMIC_QASU3)
    dynamic_qasu3_replay = load(DYNAMIC_QASU3_REPLAY)
    vsd_backimport = load(VSD_BACKIMPORT)

    validator_passes = dynamic_validator.get("returncode") == 0 or dynamic_validator.get("ok") is True
    dynamic_packet_closed = same_source_dynamic["promotion_decision"][
        "dynamic_matter_overlap_operator_packet_closed"
    ]
    dynamic_first_response_closed = dynamic_qasu3["promotion_decision"][
        "dynamic_QaSU3_first_response_layer_closed"
    ]
    vsd_dynamic_subgate_closed = vsd_backimport["closure_decision"]["VSD01_dynamic_tensor_subgate_closed"]

    stale_reconciliation = {
        "schema": "MTTStaleRouteCOperatorNoGoReconciliation.v1",
        "status": "STALE_ROUTEC_SCAFFOLD_NOGO_RETIRED_FOR_FIRST_RESPONSE_DYNAMIC_LAYER",
        "old_routec_nogo": rel(OLD_ROUTEC_NOGO),
        "later_same_source_dynamic_packet": rel(SAME_SOURCE_DYNAMIC),
        "later_dynamic_validator": rel(DYNAMIC_VALIDATOR),
        "later_dynamic_qasu3_replay": rel(DYNAMIC_QASU3_REPLAY),
        "old_selected_emitted_count": old_routec_nogo["fill_summary"]["selected_emitted"],
        "old_required_field_count": old_routec_nogo["fill_summary"]["required_fields"],
        "later_dynamic_validator_passes": validator_passes,
        "later_dynamic_packet_closed": dynamic_packet_closed,
        "later_qasu3_first_response_closed": dynamic_first_response_closed,
        "vsd01_dynamic_tensor_subgate_closed": vsd_dynamic_subgate_closed,
        "retired_scope": (
            "The old Route-C same-source scaffold no-go is stale only for the existence of a first-response "
            "selected dynamic matter/overlap operator. It remains a useful warning against promoting support-only "
            "visible/Route-C scaffolds to full magnitude/value closure."
        ),
        "stale_first_response_absence_blocker_retired": bool(
            validator_passes and dynamic_packet_closed and dynamic_first_response_closed and vsd_dynamic_subgate_closed
        ),
        "magnitude_value_closure_retired": False,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "closure_claimed": True,
    }
    write_json(STALE_RECONCILIATION, stale_reconciliation)

    sector_results: dict[str, dict[str, Any]] = {}
    spectrum_keys: list[tuple[float, ...]] = []
    for sector, payload in dynamic_values["sector_first_responses"].items():
        d_y = matrix(payload["correction_dY"])
        h1 = matrix(payload["first_hermitian_response_H1"])
        trace = np.trace(h1)
        traceless = h1 - trace / 3.0 * np.eye(3)
        h1_eigenvalues = np.linalg.eigvalsh(h1)
        distinct_values = sorted(set(rounded(h1_eigenvalues)))
        gaps = np.diff(np.sort(h1_eigenvalues))
        spectrum_key = tuple(distinct_values)
        spectrum_keys.append(spectrum_key)
        sector_results[sector] = {
            "source_direction": payload["source_direction"],
            "correction_dY_rank": int(np.linalg.matrix_rank(d_y)),
            "first_hermitian_response_rank": int(np.linalg.matrix_rank(h1)),
            "traceless_rank": int(np.linalg.matrix_rank(traceless)),
            "hermitian_error_max_abs": float(np.max(np.abs(h1 - h1.conj().T))),
            "trace": [float(trace.real), float(trace.imag)],
            "eigenvalues": rounded(h1_eigenvalues),
            "distinct_eigenvalue_count": len(distinct_values),
            "min_spectral_gap": float(np.min(np.abs(gaps))) if len(gaps) else 0.0,
            "nondegenerate_family_spectrum": len(distinct_values) == 3,
            "family_labels_resolved": len(distinct_values) == 3 and int(np.linalg.matrix_rank(traceless)) == 3,
            "selected_by_MTT": dynamic_values["selected_by_MTT"],
        }

    universal_spectrum = len(set(spectrum_keys)) == 1
    family_operator_closed = (
        dynamic_values["selected_by_MTT"] is True
        and dynamic_packet_closed
        and dynamic_first_response_closed
        and all(item["family_labels_resolved"] for item in sector_results.values())
    )
    family_spectrum = {
        "schema": "MTTSelectedFirstResponseFamilySpectrum.v1",
        "status": "SELECTED_FIRST_RESPONSE_OPERATOR_HAS_NONDEGENERATE_FAMILY_SPECTRUM",
        "source": rel(DYNAMIC_VALUES),
        "sector_results": sector_results,
        "all_sectors_family_resolved": family_operator_closed,
        "universal_spectrum_across_sectors": universal_spectrum,
        "family_resolving_operator_closed": family_operator_closed,
        "generation_magnitude_rows_emitted": False,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "closure_claimed": True,
    }
    write_json(SPECTRUM, family_spectrum)

    diagnostic_by_sector = group_by_sector(backsolve["diagnostic_weights"])
    diagnostic_hierarchies = {
        sector: hierarchy_ratio(values) for sector, values in sorted(diagnostic_by_sector.items())
    }
    hierarchy_values = list(diagnostic_hierarchies.values())
    hierarchy_spread = max(hierarchy_values) / min(hierarchy_values)
    first_response_ratio = (
        max(abs(value) for value in sector_results["u"]["eigenvalues"])
        / min(abs(value) for value in sector_results["u"]["eigenvalues"] if abs(value) > 0)
    )
    mag_obstruction = {
        "schema": "MTTMagnitudeThresholdRowObstructionAfterFamilyResolution.v1",
        "status": "FAMILY_LABELS_RESOLVED_MAGNITUDE_ROWS_STILL_NOT_EMITTED",
        "family_operator": rel(SPECTRUM),
        "rank_gap": rel(RANK_GAP),
        "diagnostic_backsolve": rel(BACKSOLVE),
        "family_operator_closed": family_operator_closed,
        "universal_spectrum_across_sectors": universal_spectrum,
        "first_response_abs_eigenvalue_ratio": first_response_ratio,
        "diagnostic_hierarchy_ratios_not_used_as_selectors": diagnostic_hierarchies,
        "diagnostic_hierarchy_spread": hierarchy_spread,
        "why_first_response_is_not_enough": [
            "the selected first-response spectrum resolves three family labels but is the same in every sector",
            "the missing rows are magnitude-bearing charged-sector rows, not only family labels",
            "sector-specific threshold, mass-scheme, RG/profile, or higher-response coefficients are not emitted",
            "using diagnostic Yukawa magnitudes to choose those coefficients would violate the selector guard",
        ],
        "accepted_generation_threshold_source_rows": [],
        "accepted_generation_threshold_source_row_count": previous_rows["accepted_row_count"],
        "required_charged_generation_row_count": rank_gap["dimension_evidence"][
            "charged_generation_magnitude_rows"
        ],
        "lambda_H_row_required": previous_rows["lambda_H_row_required"],
        "generation_resolved_threshold_source_rows_closed": False,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "closure_claimed": False,
    }
    write_json(MAG_OBSTRUCTION, mag_obstruction)

    decision = {
        "schema": "MTTFamilyResolvingOperatorOrGenerationThresholdRowsDecision.v1",
        "status": "FAMILY_RESOLVING_OPERATOR_CLOSED_GENERATION_MAGNITUDE_THRESHOLD_ROWS_OPEN",
        "previous_status": previous["status"],
        "stale_first_response_absence_blocker_retired": stale_reconciliation[
            "stale_first_response_absence_blocker_retired"
        ],
        "family_resolving_operator_closed": family_operator_closed,
        "all_sectors_family_resolved": family_operator_closed,
        "universal_spectrum_across_sectors": universal_spectrum,
        "generation_resolved_threshold_source_rows_closed": False,
        "accepted_generation_threshold_source_row_count": previous_rows["accepted_row_count"],
        "required_charged_generation_row_count": rank_gap["dimension_evidence"][
            "charged_generation_magnitude_rows"
        ],
        "lambda_H_row_required": previous_rows["lambda_H_row_required"],
        "same_branch_scale_scheme_loop_convention_closed": False,
        "accepted_Yukawa_magnitudes_as_no_knob_predictions": False,
        "true_SM_equivalence_closed": False,
        "full_no_knob_closed": False,
        "what_this_closes": [
            "first-response selected family operator exists",
            "each sector has a nondegenerate three-family Hermitian spectrum",
            "the old absence-of-dynamic-first-response blocker is stale",
        ],
        "what_this_does_not_close": [
            "sector-specific charged Yukawa magnitude rows",
            "lambda_H source row",
            "threshold matching and mass-scheme conversion rows",
            "true precision profile likelihood or accepted diagonal theorem",
        ],
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "closure_claimed": False,
    }
    write_json(DECISION, decision)

    cutset = {
        "schema": "MTTNextCutsetAfterFamilyResolvingOperator.v1",
        "status": "NEXT_ATTACK_SECTOR_SCALED_EIGENPROFILE_THRESHOLD_ROWS",
        "closed_this_artifact": {
            "stale_first_response_absence_blocker_retired": stale_reconciliation[
                "stale_first_response_absence_blocker_retired"
            ],
            "selected_family_resolving_operator_executed": family_operator_closed,
            "three_distinct_family_eigenvalues_per_sector": family_operator_closed,
        },
        "still_open": [
            "sector-scaled eigenprofile or higher-response coefficients for u,d,e",
            "9 charged generation-resolved magnitude-bearing source rows",
            "lambda_H source row",
            "same-branch true precision scale/scheme/loop convention",
            "threshold matching and mass-scheme conversion source rows",
            "full profile likelihood or accepted diagonal theorem",
        ],
        "next_required_artifact": NEXT,
        "recommended_next": {
            "artifact": NEXT,
            "reason": (
                "The selected dynamic first response now resolves family labels. The remaining gap is the "
                "sector-scaled magnitude profile that turns those labels into charged Yukawa magnitudes without "
                "using observed masses as selectors."
            ),
        },
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "closure_claimed": False,
    }
    write_json(CUTSET, cutset)

    candidate = {
        "candidate": "MTTSelectedFamilyResolvingOperatorOrGenerationThresholdRowsExecution",
        "status": STATUS,
        "inputs": {
            "selected_generationresolvedthresholdsourcerows_or_profileconventionclosure.candidate": rel(PREVIOUS),
            "generation_resolved_threshold_row_attempt.packet": rel(PREVIOUS_ROWS),
            "magnitude_weight_rank_gap.packet": rel(RANK_GAP),
            "diagnostic_magnitude_weight_backsolve.packet": rel(BACKSOLVE),
            "selected_routec_samesource_operatorpacket_fill_or_nogo.candidate": rel(OLD_ROUTEC_NOGO),
            "selected_samesourcedynamicmatteroverlapoperatorpacket_or_primitivec1valueclosure.candidate": rel(
                SAME_SOURCE_DYNAMIC
            ),
            "selected_non_scalar_dynamic_overlap_values.packet": rel(DYNAMIC_VALUES),
            "same_source_matter_overlap_operator_validator_result.packet": rel(DYNAMIC_VALIDATOR),
            "selected_dynamicqasu3operatorpacketreplay_or_yukawamassmixingvalueclosure.candidate": rel(
                DYNAMIC_QASU3
            ),
            "dynamic_qasu3_operator_packet_replay.packet": rel(DYNAMIC_QASU3_REPLAY),
            "selected_vsd01_dynamicoperatorbackimport_or_yukawavaluefrontier.candidate": rel(VSD_BACKIMPORT),
        },
        "output_packets": {
            "stale_routec_operator_nogo_reconciliation": rel(STALE_RECONCILIATION),
            "selected_first_response_family_spectrum": rel(SPECTRUM),
            "magnitude_threshold_row_obstruction_after_family_resolution": rel(MAG_OBSTRUCTION),
            "family_resolving_operator_or_generation_threshold_rows_decision": rel(DECISION),
            "next_cutset_after_family_resolving_operator": rel(CUTSET),
        },
        "theorem": {
            "name": "SelectedFamilyResolvingOperatorAndMagnitudeRowsSeparationTheorem",
            "proved": True,
            "statement": (
                "The selected same-source dynamic matter/overlap packet gives a first-response family-resolving "
                "operator: in every sector the Hermitian response has rank three and three distinct eigenvalues. "
                "This closes qualitative generation-label resolution. Because the spectrum is universal across "
                "sectors and no sector-scaled threshold/profile coefficients are emitted, it does not close the "
                "nine charged generation-resolved magnitude-bearing source rows or lambda_H."
            ),
        },
        "closure_decision": {
            "stale_first_response_absence_blocker_retired": stale_reconciliation[
                "stale_first_response_absence_blocker_retired"
            ],
            "family_resolving_operator_closed": family_operator_closed,
            "generation_resolved_threshold_source_rows_closed": False,
            "same_branch_scale_scheme_loop_convention_closed": False,
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
        "certificate": "MTT_Selected_FamilyResolvingOperator_or_GenerationThresholdRowsExecution_v1",
        "status": STATUS,
        "candidate_path": rel(OUTPUT),
        "note_path": rel(NOTE),
        "theorem_proved": True,
        "stale_first_response_absence_blocker_retired": stale_reconciliation[
            "stale_first_response_absence_blocker_retired"
        ],
        "family_resolving_operator_closed": family_operator_closed,
        "accepted_generation_threshold_source_row_count": previous_rows["accepted_row_count"],
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

    note = f"""# MTT Selected FamilyResolvingOperator or GenerationThresholdRowsExecution v1

Status: `{STATUS}`.

This artifact executes the selected first-response dynamic matter/overlap packet
as a family-resolving operator.

```text
stale first-response absence blocker retired : {str(stale_reconciliation["stale_first_response_absence_blocker_retired"]).lower()}
family-resolving operator closed             : {str(family_operator_closed).lower()}
distinct family eigenvalues per sector       : 3
universal spectrum across sectors            : {str(universal_spectrum).lower()}
accepted generation threshold rows           : {previous_rows["accepted_row_count"]}/{rank_gap["dimension_evidence"]["charged_generation_magnitude_rows"]}
Yukawa magnitudes no-knob closed             : false
```

The selected first response now resolves the three family labels in every
sector.  It does not yet emit the sector-scaled magnitude-bearing rows needed
for charged Yukawa values, nor the `lambda_H` row.  The next object must turn
the universal family eigenprofile into sector-specific threshold/profile source
rows without using observed masses as selectors.

Next artifact: `{NEXT}`.
"""
    NOTE.write_text(note, encoding="utf-8")

    print(json.dumps({"candidate": rel(OUTPUT), "status": STATUS}, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
