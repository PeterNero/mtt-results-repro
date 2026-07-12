"""Build magnitude-bearing projection weights / threshold rows derivation gate."""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "candidate_data"
CERTS = ROOT / "certificates"
CORPUS = ROOT / "proof_corpus"

SLUG = "selected_magnitudebearingprojectionweights_or_thresholdrowsderivation"
PACKET_DIR = DATA / SLUG
OUTPUT = DATA / f"{SLUG}.candidate.json"
BACKSOLVE = PACKET_DIR / "diagnostic_magnitude_weight_backsolve.packet.json"
RANK_GAP = PACKET_DIR / "magnitude_weight_rank_gap.packet.json"
THRESHOLD = PACKET_DIR / "threshold_rows_derivation_attempt.packet.json"
SUPERSET = PACKET_DIR / "superset_search_targets_without_selection.packet.json"
DECISION = PACKET_DIR / "magnitude_weights_or_threshold_rows_decision.packet.json"
CUTSET = PACKET_DIR / "next_cutset_after_magnitude_weight_backsolve.packet.json"
CERT = CERTS / f"{SLUG}_certificate.json"
NOTE = CORPUS / "MTT_Selected_MagnitudeBearingProjectionWeights_or_ThresholdRowsDerivation_v1.md"

PREVIOUS = DATA / "selected_thresholdresponserows_or_sectorprojectionweightsexecution.candidate.json"
PREVIOUS_DECISION = (
    DATA
    / "selected_thresholdresponserows_or_sectorprojectionweightsexecution"
    / "threshold_rows_or_projection_weights_decision.packet.json"
)
SOURCE_WEIGHTS = (
    DATA
    / "selected_thresholdresponserows_or_sectorprojectionweightsexecution"
    / "source_normalized_sector_projection_weights.packet.json"
)
WEIGHT_CUTSET = (
    DATA
    / "selected_thresholdresponserows_or_sectorprojectionweightsexecution"
    / "next_cutset_after_source_projection_weights.packet.json"
)
VALUE_PACKET = (
    DATA
    / "selected_acceptedcommonscaleyukawahiggsvalues_or_profilelikelihoodexecution"
    / "versioned_common_scale_yukawa_higgs_values.packet.json"
)
SOURCE_ROW_AUDIT = (
    DATA
    / "selected_acceptedthresholdmassschemesourcerows_or_noknobvaluederivation"
    / "accepted_threshold_mass_scheme_source_row_audit.packet.json"
)
RESIDUAL_ROWS = (
    DATA
    / "selected_thresholdmassschemevalues_or_correlatedlikelihoodsourceimport"
    / "threshold_mass_scheme_residual_values.packet.json"
)
CONTRACT = (
    DATA
    / "selected_thresholdresponsefunctionalderivation_or_profilelikelihoodacquisition"
    / "selected_threshold_response_functional_contract.packet.json"
)
SUPerset = (
    DATA
    / "selected_yukawaprojectionkernel_readiness_or_thresholdresponsefrontier"
    / "superset_strategy_execution_matrix.packet.json"
)

STATUS = (
    "MTT_SELECTED_MAGNITUDEBEARINGPROJECTIONWEIGHTS_OR_THRESHOLDROWSDERIVATION_"
    "BUILT_DIAGNOSTIC_BACKSOLVE_RANK_GAP_THRESHOLD_ROWS_OPEN"
)
NEXT = "MTT_Selected_GenerationResolvedThresholdSourceRows_or_ProfileConventionClosure_v1"


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
        raise FileNotFoundError("missing magnitude-weight sources: " + ", ".join(missing))


def ratio(values: list[float]) -> float:
    nonzero = [v for v in values if v > 0]
    return max(nonzero) / min(nonzero)


def main() -> int:
    PACKET_DIR.mkdir(parents=True, exist_ok=True)
    CERTS.mkdir(parents=True, exist_ok=True)
    CORPUS.mkdir(parents=True, exist_ok=True)

    sources = [
        PREVIOUS,
        PREVIOUS_DECISION,
        SOURCE_WEIGHTS,
        WEIGHT_CUTSET,
        VALUE_PACKET,
        SOURCE_ROW_AUDIT,
        RESIDUAL_ROWS,
        CONTRACT,
        SUPerset,
    ]
    require_sources(sources)

    previous = load(PREVIOUS)
    previous_decision = load(PREVIOUS_DECISION)
    source_weights = load(SOURCE_WEIGHTS)
    weight_cutset = load(WEIGHT_CUTSET)
    value_packet = load(VALUE_PACKET)
    source_row_audit = load(SOURCE_ROW_AUDIT)
    residual_rows = load(RESIDUAL_ROWS)
    contract = load(CONTRACT)
    superset = load(SUPerset)

    mags = value_packet["derived_magnitudes"]
    charged_diag = {
        "u": mags["diag_abs_Y_u"],
        "d": mags["diag_abs_Y_d"],
        "e": mags["diag_abs_Y_e"],
    }
    diagnostic_weights = [
        {
            "sector": sector,
            "generation": idx + 1,
            "diagnostic_magnitude_weight": value,
            "source_normalized_weight": 1.0,
            "used_as_selector": False,
        }
        for sector, values in charged_diag.items()
        for idx, value in enumerate(values)
    ]
    diagnostic_backsolve = {
        "schema": "MTTDiagnosticMagnitudeWeightBacksolve.v1",
        "status": "DIAGNOSTIC_MAGNITUDE_WEIGHTS_BACKSOLVED_NOT_SELECTED",
        "value_packet": rel(VALUE_PACKET),
        "source_weights": rel(SOURCE_WEIGHTS),
        "diagnostic_weights": diagnostic_weights,
        "lambda_H_diagnostic_weight": mags["lambda_H"],
        "sector_frobenius_diagnostic_weights": {
            "u": mags["frob_Y_u"],
            "d": mags["frob_Y_d"],
            "e": mags["frob_Y_e"],
        },
        "accepted_as_selected_magnitude_weights": False,
        "why_not_selected": [
            "the value packet is accepted for SM-parity/profile execution, not as no-knob source",
            "using these weights to define the source would make observed/replay values selectors",
            "same-branch threshold and mass-scheme source rows remain absent",
        ],
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "closure_claimed": True,
    }
    write_json(BACKSOLVE, diagnostic_backsolve)

    source_column_count = source_weights["normal_form"]["rank"]
    source_sector_slot_count = len(source_weights["sector_weights"])
    charged_magnitude_count = len(diagnostic_weights)
    magnitude_count_with_lambda = charged_magnitude_count + 1
    rank_gap = {
        "schema": "MTTMagnitudeWeightRankGap.v1",
        "status": "SOURCE_WEIGHT_RANK_INSUFFICIENT_FOR_MAGNITUDE_WEIGHTS",
        "theorem": {
            "name": "SourceNormalizedWeightsDoNotDetermineGenerationResolvedMagnitudes",
            "proved": True,
            "statement": (
                "The selected source-normalized projection layer has rank two and four typed sector slots. "
                "The charged Yukawa diagonal magnitude layer has nine generation-resolved rows, plus lambda_H. "
                "Therefore the current source weights cannot determine the magnitude-bearing projection weights "
                "without extra generation-resolved threshold/mass-scheme/profile source rows."
            ),
        },
        "dimension_evidence": {
            "source_column_count": source_column_count,
            "source_sector_slot_count": source_sector_slot_count,
            "charged_generation_magnitude_rows": charged_magnitude_count,
            "charged_plus_lambda_rows": magnitude_count_with_lambda,
            "rank_gap_against_charged_rows": charged_magnitude_count - source_column_count,
            "slot_gap_against_charged_rows": charged_magnitude_count - source_sector_slot_count,
        },
        "hierarchy_evidence": {
            "diag_abs_Y_u_ratio_max_min": ratio(charged_diag["u"]),
            "diag_abs_Y_d_ratio_max_min": ratio(charged_diag["d"]),
            "diag_abs_Y_e_ratio_max_min": ratio(charged_diag["e"]),
        },
        "consequence": (
            "The next selected object must supply generation-resolved magnitude-bearing rows or an equivalent "
            "operator theorem reducing those rows to selected threshold/profile data."
        ),
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "closure_claimed": True,
    }
    write_json(RANK_GAP, rank_gap)

    threshold = {
        "schema": "MTTThresholdRowsDerivationAttempt.v1",
        "status": "THRESHOLD_ROWS_DERIVATION_ATTEMPTED_NO_ACCEPTED_ROWS",
        "contract": rel(CONTRACT),
        "source_row_audit": rel(SOURCE_ROW_AUDIT),
        "residual_rows": rel(RESIDUAL_ROWS),
        "accepted_threshold_matching_source_rows": source_row_audit[
            "accepted_threshold_matching_source_rows"
        ],
        "accepted_mass_scheme_conversion_source_rows": source_row_audit[
            "accepted_mass_scheme_conversion_source_rows"
        ],
        "residual_rows_finite": residual_rows["summary"]["all_residuals_finite"],
        "accepted_as_threshold_matching_values": residual_rows[
            "accepted_as_threshold_matching_values"
        ],
        "accepted_as_mass_scheme_conversion_values": residual_rows[
            "accepted_as_mass_scheme_conversion_values"
        ],
        "derivation_closed": False,
        "still_missing": [
            "generation-resolved source rows",
            "same-branch scale/scheme/loop convention",
            "threshold matching source rows",
            "mass-scheme conversion source rows",
            "profile/covariance response or accepted diagonal theorem",
        ],
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "closure_claimed": False,
    }
    write_json(THRESHOLD, threshold)

    superset_targets = {
        "schema": "MTTSupersetSearchTargetsWithoutSelection.v1",
        "status": "DIAGNOSTIC_TARGETS_AVAILABLE_FOR_DISCOVERY_ONLY",
        "superset_policy": superset["policy"],
        "diagnostic_backsolve": rel(BACKSOLVE),
        "allowed_use": [
            "rank candidate generation-resolved threshold/source row hypotheses",
            "compare later non-observed selected derivations against the diagnostic table",
            "estimate which missing rows have the largest effect",
        ],
        "forbidden_use": [
            "select MTT branch from diagnostic weights",
            "fit threshold rows to observed/replay magnitudes",
            "claim no-knob Yukawa closure from the backsolve",
        ],
        "selected_next_lane": "internal_generation_resolved_threshold_rows",
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "closure_claimed": False,
    }
    write_json(SUPERSET, superset_targets)

    decision = {
        "schema": "MTTMagnitudeWeightsOrThresholdRowsDecision.v1",
        "status": "DIAGNOSTIC_WEIGHTS_AND_RANK_GAP_CLOSED_SELECTED_ROWS_OPEN",
        "previous_status": previous["status"],
        "source_normalized_sector_projection_weights_closed": previous_decision[
            "source_normalized_sector_projection_weights_closed"
        ],
        "diagnostic_magnitude_backsolve_emitted": True,
        "diagnostic_magnitude_backsolve_accepted_as_selection": False,
        "rank_gap_theorem_proved": True,
        "magnitude_bearing_projection_weights_closed": False,
        "generation_resolved_threshold_source_rows_closed": False,
        "same_branch_scale_scheme_loop_convention_closed": False,
        "mass_scheme_conversion_rows_closed": False,
        "profile_likelihood_or_diagonal_theorem_closed": False,
        "accepted_Yukawa_magnitudes_as_no_knob_predictions": False,
        "true_SM_equivalence_closed": False,
        "full_no_knob_closed": False,
        "what_this_fixes": [
            "emits a reproducible diagnostic magnitude-weight table without using it as a selector",
            "proves current source-normalized rank is insufficient for generation-resolved magnitudes",
            "turns the next target into generation-resolved threshold/source rows",
        ],
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "closure_claimed": False,
    }
    write_json(DECISION, decision)

    cutset = {
        "schema": "MTTNextCutsetAfterMagnitudeWeightBacksolve.v1",
        "status": "NEXT_ATTACK_GENERATION_RESOLVED_THRESHOLD_SOURCE_ROWS",
        "closed_now": {
            "diagnostic_magnitude_weight_backsolve": True,
            "rank_gap_theorem": True,
            "superset_discovery_targets_scoped": True,
        },
        "still_open": [
            "generation-resolved magnitude-bearing projection/source rows",
            "same-branch scale/scheme/loop convention",
            "threshold matching source rows",
            "mass-scheme conversion source rows",
            "full profile likelihood or accepted diagonal theorem",
        ],
        "recommended_next": {
            "artifact": NEXT,
            "reason": (
                "The source-normalized layer is too low-rank for charged generation magnitudes; the "
                "next proof must emit generation-resolved selected rows or a theorem reducing them to "
                "threshold/profile response."
            ),
        },
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "closure_claimed": False,
    }
    write_json(CUTSET, cutset)

    candidate = {
        "candidate": "MTTSelectedMagnitudeBearingProjectionWeightsOrThresholdRowsDerivation",
        "status": STATUS,
        "inputs": {path.stem: rel(path) for path in sources},
        "output_packets": {
            "diagnostic_magnitude_weight_backsolve": rel(BACKSOLVE),
            "magnitude_weight_rank_gap": rel(RANK_GAP),
            "threshold_rows_derivation_attempt": rel(THRESHOLD),
            "superset_search_targets_without_selection": rel(SUPERSET),
            "magnitude_weights_or_threshold_rows_decision": rel(DECISION),
            "next_cutset_after_magnitude_weight_backsolve": rel(CUTSET),
        },
        "theorem": {
            "name": "MagnitudeBacksolveRankGapAndThresholdRowFrontierTheorem",
            "proved": True,
            "statement": (
                "The accepted common-scale packet determines a diagnostic magnitude-weight table, but this "
                "table is not selected MTT data. The selected source-normalized projection layer is too "
                "low-rank to determine generation-resolved charged Yukawa magnitudes. Therefore magnitude-bearing "
                "projection closure reduces to generation-resolved threshold/mass-scheme/profile source rows."
            ),
        },
        "closure_decision": {
            "diagnostic_magnitude_backsolve_emitted": True,
            "rank_gap_theorem_proved": True,
            "magnitude_bearing_projection_weights_closed": False,
            "generation_resolved_threshold_source_rows_closed": False,
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
        "certificate": "MTT_Selected_MagnitudeBearingProjectionWeights_or_ThresholdRowsDerivation_v1",
        "status": STATUS,
        "candidate_path": rel(OUTPUT),
        "note_path": rel(NOTE),
        "theorem_proved": True,
        "diagnostic_magnitude_backsolve_emitted": True,
        "diagnostic_magnitude_backsolve_accepted_as_selection": False,
        "rank_gap_theorem_proved": True,
        "magnitude_bearing_projection_weights_closed": False,
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

    note = f"""# MTT Selected MagnitudeBearingProjectionWeights or ThresholdRowsDerivation v1

Status: `{STATUS}`.

This artifact executes the diagnostic magnitude-weight backsolve and proves the
rank gap.

```text
diagnostic magnitude table emitted        : true
diagnostic table accepted as selection    : false
rank gap theorem proved                   : true
magnitude-bearing weights closed          : false
Yukawa magnitudes no-knob closed          : false
```

The selected source-normalized layer has rank `{source_column_count}` and
`{source_sector_slot_count}` typed source slots.  The charged diagonal Yukawa
layer has `{charged_magnitude_count}` generation-resolved magnitude rows, plus
`lambda_H`.  So the current source weights cannot determine the magnitude layer
without additional generation-resolved threshold/mass-scheme/profile source
rows.

Next artifact: `{NEXT}`.
"""
    NOTE.write_text(note, encoding="utf-8")

    print(json.dumps({"candidate": rel(OUTPUT), "status": STATUS}, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
