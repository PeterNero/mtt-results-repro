"""Build higher-response sector coefficients / threshold functional source rows gate."""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "candidate_data"
CERTS = ROOT / "certificates"
CORPUS = ROOT / "proof_corpus"

SLUG = "selected_higherresponsesectorcoefficients_or_thresholdfunctionalsourcerows"
PACKET_DIR = DATA / SLUG
OUTPUT = DATA / f"{SLUG}.candidate.json"
KNOB_APPLICATION = PACKET_DIR / "minimal_universal_parameter_application_to_yukawa_wall.packet.json"
RESPONSE_FUNCTIONAL_ATTEMPT = PACKET_DIR / "selected_threshold_response_functional_execution_attempt.packet.json"
SECTOR_COEFFICIENT_ATTEMPT = PACKET_DIR / "higher_response_sector_coefficient_source_attempt.packet.json"
DECISION = PACKET_DIR / "higher_response_or_threshold_functional_decision.packet.json"
CUTSET = PACKET_DIR / "next_cutset_after_higher_response_attempt.packet.json"
CERT = CERTS / f"{SLUG}_certificate.json"
NOTE = CORPUS / "MTT_Selected_HigherResponseSectorCoefficients_or_ThresholdFunctionalSourceRows_v1.md"

PREVIOUS = DATA / "selected_sectorscaledeigenprofilethresholdrows_or_yukawamagnitudesourceexecution.candidate.json"
MODEL_TESTS = (
    DATA
    / "selected_sectorscaledeigenprofilethresholdrows_or_yukawamagnitudesourceexecution"
    / "sector_scaled_eigenprofile_model_tests.packet.json"
)
COEFFICIENT_FRONTIER = (
    DATA
    / "selected_sectorscaledeigenprofilethresholdrows_or_yukawamagnitudesourceexecution"
    / "sector_coefficient_frontier.packet.json"
)
ROW_ATTEMPT_PREVIOUS = (
    DATA
    / "selected_sectorscaledeigenprofilethresholdrows_or_yukawamagnitudesourceexecution"
    / "eigenprofile_threshold_row_acceptance_attempt.packet.json"
)
UNIVERSAL_POLICY = DATA / "universal_source_parameter_policy.candidate.json"
UNIVERSAL_POLICY_PACKET = DATA / "universal_source_parameter_policy" / "universal_source_parameter_policy.packet.json"
UNIVERSAL_CANDIDATES = DATA / "universal_source_parameter_policy" / "candidate_universal_parameters.packet.json"
UNIVERSAL_GATE_MAPPING = DATA / "universal_source_parameter_policy" / "current_gate_mapping.packet.json"
VSD02_FILL = DATA / "selected_vsd02acceptedsourcerowsfill_or_noknobthresholdderivation.candidate.json"
VSD02_FILL_ATTEMPT = (
    DATA
    / "selected_vsd02acceptedsourcerowsfill_or_noknobthresholdderivation"
    / "accepted_source_rows_fill_attempt.packet.json"
)
VSD02_REDUCTION = (
    DATA
    / "selected_vsd02acceptedsourcerowsfill_or_noknobthresholdderivation"
    / "no_knob_threshold_derivation_reduction.packet.json"
)
VSD02_SCHEMA = (
    DATA
    / "selected_vsd02acceptedsourcerowsfill_or_noknobthresholdderivation"
    / "accepted_source_row_strict_schema.packet.json"
)
RANK_GAP = (
    DATA
    / "selected_magnitudebearingprojectionweights_or_thresholdrowsderivation"
    / "magnitude_weight_rank_gap.packet.json"
)

STATUS = (
    "MTT_SELECTED_HIGHERRESPONSESECTORCOEFFICIENTS_OR_THRESHOLDFUNCTIONALSOURCEROWS_"
    "BUILT_MINIMAL_PARAMETER_POLICY_APPLIED_FUNCTIONAL_OPEN"
)
NEXT = "MTT_Selected_ThresholdFunctionalSourceTheorem_or_MinimalUniversalParameterSelection_v1"


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
        raise FileNotFoundError("missing higher-response/threshold-functional sources: " + ", ".join(missing))


def main() -> int:
    PACKET_DIR.mkdir(parents=True, exist_ok=True)
    CERTS.mkdir(parents=True, exist_ok=True)
    CORPUS.mkdir(parents=True, exist_ok=True)

    sources = [
        PREVIOUS,
        MODEL_TESTS,
        COEFFICIENT_FRONTIER,
        ROW_ATTEMPT_PREVIOUS,
        UNIVERSAL_POLICY,
        UNIVERSAL_POLICY_PACKET,
        UNIVERSAL_CANDIDATES,
        UNIVERSAL_GATE_MAPPING,
        VSD02_FILL,
        VSD02_FILL_ATTEMPT,
        VSD02_REDUCTION,
        VSD02_SCHEMA,
        RANK_GAP,
    ]
    require_sources(sources)

    previous = load(PREVIOUS)
    model_tests = load(MODEL_TESTS)
    coefficient_frontier = load(COEFFICIENT_FRONTIER)
    row_attempt_previous = load(ROW_ATTEMPT_PREVIOUS)
    universal_policy = load(UNIVERSAL_POLICY)
    universal_policy_packet = load(UNIVERSAL_POLICY_PACKET)
    universal_candidates = load(UNIVERSAL_CANDIDATES)
    universal_gate_mapping = load(UNIVERSAL_GATE_MAPPING)
    vsd02_fill = load(VSD02_FILL)
    vsd02_fill_attempt = load(VSD02_FILL_ATTEMPT)
    vsd02_reduction = load(VSD02_REDUCTION)
    rank_gap = load(RANK_GAP)

    knob_lanes = [
        {
            "lane": "UP-0",
            "parameter_count": 0,
            "interpretation": "strict no-knob closure",
            "currently_closes_yukawa_wall": False,
            "why": "No selected threshold response functional or sector coefficient theorem is emitted yet.",
            "credible_if_next": "derive SelectedThresholdResponseFunctional with no universal parameter.",
        },
        {
            "lane": "UP-1",
            "parameter_count": 1,
            "interpretation": "one universal source anchor",
            "candidate_classes": ["UP-RET-OVERLAP", "UP-ACTION-NORM", "UP-PHASE"],
            "currently_closes_yukawa_wall": False,
            "why": (
                "A single global source anchor may normalize or orient the selected packet, but by policy it cannot "
                "be refit per charged sector; it therefore cannot replace missing sector-specific magnitude rows."
            ),
            "credible_if_next": "select one source-level parameter before replay and propagate it through the threshold functional.",
        },
        {
            "lane": "UP-2",
            "parameter_count": 2,
            "interpretation": "two universal source anchors",
            "candidate_classes": ["UP-RET-OVERLAP", "UP-PHASE", "UP-ACTION-NORM"],
            "currently_closes_yukawa_wall": False,
            "why": (
                "Two global anchors can add normalization plus orientation/phase, but cannot be chosen from the "
                "diagnostic hierarchy residuals and cannot act as per-sector Yukawa sliders."
            ),
            "credible_if_next": "prove both anchors are selected by MTT and replay them without empirical selection.",
        },
        {
            "lane": "UP-3",
            "parameter_count": 3,
            "interpretation": "maximum currently allowed minimal universal parameter realism",
            "candidate_classes": ["UP-RET-OVERLAP", "UP-PHASE", "UP-ACTION-NORM"],
            "currently_closes_yukawa_wall": False,
            "why": (
                "Three universal source anchors would be valuable if selected, but three fitted charged-sector "
                "coefficients would violate the policy because they are sector-specific rather than universal."
            ),
            "credible_if_next": "supply candidate-specific source theorems for all anchors and an accepted replay map.",
        },
    ]

    forbidden_knob_counting = {
        "ordinary_sector_fits_forbidden": True,
        "one_knob_per_charged_sector_forbidden_as_source_proof": True,
        "one_knob_per_generation_forbidden_as_source_proof": True,
        "diagnostic_log_affine_coefficients_are_not_selected": True,
        "diagnostic_log_quadratic_coefficients_are_not_selected": True,
        "reason": (
            "The universal-parameter policy allows only source-level parameters selected before empirical replay. "
            "It does not permit using u,d,e hierarchy residuals to choose sector coefficients."
        ),
    }

    knob_application = {
        "schema": "MTTMinimalUniversalParameterApplicationToYukawaWall.v1",
        "status": "NO_KNOB_PREFERRED_MINIMAL_UNIVERSAL_PARAMETER_LANES_ALLOWED_NOT_SELECTED",
        "universal_policy": rel(UNIVERSAL_POLICY_PACKET),
        "maximum_live_universal_parameters": universal_policy_packet["maximum_live_universal_parameters"],
        "selected_parameter_count_now": universal_policy["selected_parameter_count_now"],
        "policy_tiers": universal_policy_packet["tiers"],
        "candidate_classes_available": universal_candidates["candidate_classes"],
        "gate_mapping_imported": rel(UNIVERSAL_GATE_MAPPING),
        "current_yukawa_wall": rel(PREVIOUS),
        "knob_lanes": knob_lanes,
        "forbidden_knob_counting": forbidden_knob_counting,
        "best_current_statement": (
            "No-knob remains the preferred target. A 1-3 parameter result would be credible only if the parameters "
            "are universal source anchors selected by MTT before replay; no such parameter is selected now."
        ),
        "minimal_universal_parameter_lane_selected_now": False,
        "selected_parameter_count_after_this_artifact": 0,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "closure_claimed": True,
    }
    write_json(KNOB_APPLICATION, knob_application)

    required_functional_outputs = vsd02_reduction["minimal_new_theorem_required"]["must_emit"]
    functional_checks = [
        {
            "required_output": "selected response functional mapping MTT dynamic packet to threshold rows",
            "present_now": False,
            "source": rel(VSD02_REDUCTION),
            "blocking_reason": "VSD02 reduction names this as the missing theorem; no packet emits it.",
        },
        {
            "required_output": "explicit scale/scheme/loop-order convention",
            "present_now": False,
            "source": rel(COEFFICIENT_FRONTIER),
            "blocking_reason": "current profile convention remains first-pass/SM-parity, not true precision.",
        },
        {
            "required_output": "mass-scheme conversion maps",
            "present_now": False,
            "source": rel(VSD02_FILL_ATTEMPT),
            "blocking_reason": "VSD02 strict fill accepts no mass-scheme conversion source rows.",
        },
        {
            "required_output": "threshold covariance response or accepted diagonal limitation theorem",
            "present_now": False,
            "source": rel(VSD02_REDUCTION),
            "blocking_reason": "external likelihood/profile workspace is not imported as a full accepted source.",
        },
        {
            "required_output": "proof no observed values select the response",
            "present_now": True,
            "source": rel(MODEL_TESTS),
            "blocking_reason": "guardrail exists, but the functional itself is absent.",
        },
    ]
    response_functional_attempt = {
        "schema": "MTTSelectedThresholdResponseFunctionalExecutionAttempt.v1",
        "status": "THRESHOLD_RESPONSE_FUNCTIONAL_ATTEMPTED_REQUIRED_OUTPUTS_OPEN",
        "required_outputs_from_vsd02": required_functional_outputs,
        "functional_checks": functional_checks,
        "required_output_count": len(required_functional_outputs),
        "present_required_output_count": sum(1 for item in functional_checks if item["present_now"]),
        "selected_threshold_response_functional_closed": False,
        "accepted_external_likelihood_workspace_closed": vsd02_reduction["external_acquisition_alternative"][
            "full_likelihood_imported_now"
        ],
        "accepted_source_row_count": vsd02_fill_attempt["accepted_row_count"],
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "closure_claimed": False,
    }
    write_json(RESPONSE_FUNCTIONAL_ATTEMPT, response_functional_attempt)

    coefficient_rows = []
    for sector, result in model_tests["log_affine_diagnostic_results"].items():
        coefficient_rows.append(
            {
                "candidate_id": f"{sector}.log_affine_higher_response_coefficients",
                "diagnostic_coefficients": result["diagnostic_coefficients_not_selected"],
                "accepted_as_selected_sector_coefficients": False,
                "why_not": [
                    "coefficients are fitted/backsolved from diagnostic magnitude values",
                    "no selected higher-response operator emits them",
                    "using them as source rows would violate the universal-parameter policy",
                ],
            }
        )
    for sector, result in model_tests["log_quadratic_diagnostic_exact_coefficients"].items():
        coefficient_rows.append(
            {
                "candidate_id": f"{sector}.log_quadratic_exact_higher_response_coefficients",
                "diagnostic_coefficients": result["diagnostic_exact_coefficients_not_selected"],
                "accepted_as_selected_sector_coefficients": False,
                "why_not": [
                    "three coefficients exactly determine three diagnostic values",
                    "no selected threshold functional chooses this polynomial family",
                    "exact diagnostic interpolation is not a no-knob source theorem",
                ],
            }
        )

    sector_coefficient_attempt = {
        "schema": "MTTHigherResponseSectorCoefficientSourceAttempt.v1",
        "status": "DIAGNOSTIC_SECTOR_COEFFICIENTS_REJECTED_SELECTED_SOURCE_ROWS_OPEN",
        "family_coordinate_available": previous["closure_decision"]["family_resolving_operator_closed"],
        "universal_profile_nogo_proved": previous["closure_decision"][
            "universal_sector_scaled_eigenprofile_nogo_proved"
        ],
        "candidate_sector_coefficient_rows": coefficient_rows,
        "candidate_sector_coefficient_row_count": len(coefficient_rows),
        "accepted_sector_coefficient_rows": [],
        "accepted_sector_coefficient_row_count": 0,
        "accepted_generation_threshold_source_row_count": row_attempt_previous["accepted_row_count"],
        "required_charged_generation_row_count": rank_gap["dimension_evidence"][
            "charged_generation_magnitude_rows"
        ],
        "lambda_H_row_required": row_attempt_previous["lambda_H_row_required"],
        "ordinary_sector_knobs_rejected": True,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "closure_claimed": False,
    }
    write_json(SECTOR_COEFFICIENT_ATTEMPT, sector_coefficient_attempt)

    decision = {
        "schema": "MTTHigherResponseOrThresholdFunctionalDecision.v1",
        "status": "MINIMAL_PARAMETER_POLICY_APPLIED_THRESHOLD_FUNCTIONAL_OPEN",
        "previous_status": previous["status"],
        "no_knob_target_preserved": True,
        "minimal_universal_parameter_fallback_allowed": True,
        "maximum_live_universal_parameters": universal_policy_packet["maximum_live_universal_parameters"],
        "selected_universal_parameter_count": 0,
        "family_resolving_operator_closed": previous["closure_decision"]["family_resolving_operator_closed"],
        "universal_sector_scaled_eigenprofile_nogo_proved": previous["closure_decision"][
            "universal_sector_scaled_eigenprofile_nogo_proved"
        ],
        "higher_response_sector_coefficients_closed": False,
        "selected_threshold_response_functional_closed": False,
        "accepted_generation_threshold_source_row_count": row_attempt_previous["accepted_row_count"],
        "required_charged_generation_row_count": rank_gap["dimension_evidence"][
            "charged_generation_magnitude_rows"
        ],
        "generation_resolved_threshold_source_rows_closed": False,
        "accepted_Yukawa_magnitudes_as_no_knob_predictions": False,
        "minimal_parameter_yukawa_closure_closed": False,
        "true_SM_equivalence_closed": False,
        "full_no_knob_closed": False,
        "what_this_closes": [
            "applies the 0-3 universal-parameter policy to the Yukawa wall",
            "rejects fitted sector coefficients as source proof",
            "shows the selected threshold functional remains the minimal honest next theorem",
        ],
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "closure_claimed": False,
    }
    write_json(DECISION, decision)

    cutset = {
        "schema": "MTTNextCutsetAfterHigherResponseAttempt.v1",
        "status": "NEXT_ATTACK_THRESHOLD_FUNCTIONAL_SOURCE_THEOREM_OR_UNIVERSAL_PARAMETER_SELECTION",
        "closed_this_artifact": {
            "minimal_parameter_policy_applied_to_yukawa_wall": True,
            "ordinary_sector_knob_route_rejected": True,
            "threshold_functional_required_outputs_replayed": True,
        },
        "still_open": [
            "selected threshold response functional mapping dynamic packet to threshold rows",
            "selected higher-response sector coefficients not fitted from values",
            "candidate-specific theorem for any 1-3 universal source parameters",
            "9 charged generation-resolved magnitude-bearing source rows",
            "lambda_H source row",
            "true precision scale/scheme/loop and mass-scheme conversion",
        ],
        "next_required_artifact": NEXT,
        "recommended_next": {
            "artifact": NEXT,
            "reason": (
                "The proof has separated no-knob from minimal-parameter realism. The next gate must either "
                "derive the selected threshold functional with zero parameters or select a small universal source "
                "parameter packet before empirical replay."
            ),
        },
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "closure_claimed": False,
    }
    write_json(CUTSET, cutset)

    candidate = {
        "candidate": "MTTSelectedHigherResponseSectorCoefficientsOrThresholdFunctionalSourceRows",
        "status": STATUS,
        "inputs": {
            "selected_sectorscaledeigenprofilethresholdrows_or_yukawamagnitudesourceexecution.candidate": rel(PREVIOUS),
            "sector_scaled_eigenprofile_model_tests.packet": rel(MODEL_TESTS),
            "sector_coefficient_frontier.packet": rel(COEFFICIENT_FRONTIER),
            "eigenprofile_threshold_row_acceptance_attempt.packet": rel(ROW_ATTEMPT_PREVIOUS),
            "universal_source_parameter_policy.candidate": rel(UNIVERSAL_POLICY),
            "universal_source_parameter_policy.packet": rel(UNIVERSAL_POLICY_PACKET),
            "candidate_universal_parameters.packet": rel(UNIVERSAL_CANDIDATES),
            "current_gate_mapping.packet": rel(UNIVERSAL_GATE_MAPPING),
            "selected_vsd02acceptedsourcerowsfill_or_noknobthresholdderivation.candidate": rel(VSD02_FILL),
            "accepted_source_rows_fill_attempt.packet": rel(VSD02_FILL_ATTEMPT),
            "no_knob_threshold_derivation_reduction.packet": rel(VSD02_REDUCTION),
            "accepted_source_row_strict_schema.packet": rel(VSD02_SCHEMA),
            "magnitude_weight_rank_gap.packet": rel(RANK_GAP),
        },
        "output_packets": {
            "minimal_universal_parameter_application_to_yukawa_wall": rel(KNOB_APPLICATION),
            "selected_threshold_response_functional_execution_attempt": rel(RESPONSE_FUNCTIONAL_ATTEMPT),
            "higher_response_sector_coefficient_source_attempt": rel(SECTOR_COEFFICIENT_ATTEMPT),
            "higher_response_or_threshold_functional_decision": rel(DECISION),
            "next_cutset_after_higher_response_attempt": rel(CUTSET),
        },
        "theorem": {
            "name": "MinimalUniversalParameterPolicyAndThresholdFunctionalFrontierTheorem",
            "proved": True,
            "statement": (
                "No-knob closure remains the strongest target, but MTT can coherently admit a 1-3 universal "
                "source-parameter fallback only when those parameters are selected before empirical replay and are "
                "not refit per sector or observable. Applying that policy to the current Yukawa wall rejects "
                "diagnostic sector-coefficient fits and leaves the selected threshold response functional or a "
                "candidate-specific universal-parameter theorem as the next honest closure object."
            ),
        },
        "closure_decision": {
            "no_knob_target_preserved": True,
            "minimal_universal_parameter_fallback_allowed": True,
            "selected_universal_parameter_count": 0,
            "higher_response_sector_coefficients_closed": False,
            "selected_threshold_response_functional_closed": False,
            "generation_resolved_threshold_source_rows_closed": False,
            "accepted_Yukawa_magnitudes_as_no_knob_predictions": False,
            "minimal_parameter_yukawa_closure_closed": False,
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
        "certificate": "MTT_Selected_HigherResponseSectorCoefficients_or_ThresholdFunctionalSourceRows_v1",
        "status": STATUS,
        "candidate_path": rel(OUTPUT),
        "note_path": rel(NOTE),
        "theorem_proved": True,
        "no_knob_target_preserved": True,
        "minimal_universal_parameter_fallback_allowed": True,
        "maximum_live_universal_parameters": universal_policy_packet["maximum_live_universal_parameters"],
        "selected_universal_parameter_count": 0,
        "higher_response_sector_coefficients_closed": False,
        "selected_threshold_response_functional_closed": False,
        "accepted_generation_threshold_source_row_count": row_attempt_previous["accepted_row_count"],
        "required_charged_generation_row_count": rank_gap["dimension_evidence"][
            "charged_generation_magnitude_rows"
        ],
        "accepted_Yukawa_magnitudes_as_no_knob_predictions": False,
        "minimal_parameter_yukawa_closure_closed": False,
        "true_SM_equivalence_closed": False,
        "full_no_knob_closed": False,
        "closure_claimed": False,
        "unpatched_theorem_closure_claimed": False,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "next_required_artifact": NEXT,
    }
    write_json(CERT, cert)

    note = f"""# MTT Selected HigherResponseSectorCoefficients or ThresholdFunctionalSourceRows v1

Status: `{STATUS}`.

This artifact applies the no-knob versus minimal-universal-parameter policy to
the current Yukawa wall.

```text
no-knob target preserved                    : true
minimal universal parameter fallback allowed: true
maximum live universal parameters           : {universal_policy_packet["maximum_live_universal_parameters"]}
selected universal parameters now           : 0
ordinary fitted sector knobs rejected       : true
accepted generation threshold rows          : {row_attempt_previous["accepted_row_count"]}/{rank_gap["dimension_evidence"]["charged_generation_magnitude_rows"]}
Yukawa magnitudes no-knob closed            : false
minimal-parameter Yukawa closure closed     : false
```

A 1-3 parameter universe remains scientifically valuable only if those
parameters are universal source anchors selected by MTT before replay.  The
current diagnostic sector coefficients are not that: they are backsolved from
value packets and remain rejected as source proof.

Next artifact: `{NEXT}`.
"""
    NOTE.write_text(note, encoding="utf-8")

    print(json.dumps({"candidate": rel(OUTPUT), "status": STATUS}, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
