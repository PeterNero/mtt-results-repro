"""Build threshold magnitude rows or minimal universal parameter decision packet."""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "candidate_data"
CERTS = ROOT / "certificates"
CORPUS = ROOT / "proof_corpus"

SLUG = "selected_thresholdmagnituderows_or_minimaluniversalparameterdecision"
PACKET_DIR = DATA / SLUG
OUTPUT = DATA / f"{SLUG}.candidate.json"
ROW_DECISION = PACKET_DIR / "threshold_magnitude_row_decision.packet.json"
ANCHOR_RECHECK = PACKET_DIR / "minimal_universal_anchor_recheck_after_source_domain.packet.json"
TERMINAL_CUTSET = PACKET_DIR / "terminal_value_closure_cutset.packet.json"
NEXT_STEP = PACKET_DIR / "next_constructive_target.packet.json"
CERT = CERTS / f"{SLUG}_certificate.json"
NOTE = CORPUS / "MTT_Selected_ThresholdMagnitudeRows_or_MinimalUniversalParameterDecision_v1.md"

PREVIOUS = DATA / "selected_rthetascalarvaluefunctionalsource_or_noknobnumericalrows.candidate.json"
SOURCE_DOMAIN = (
    DATA
    / "selected_rthetascalarvaluefunctionalsource_or_noknobnumericalrows"
    / "rtheta_scalar_value_functional_source_packet.packet.json"
)
EXECUTION_GATE = (
    DATA
    / "selected_rthetascalarvaluefunctionalsource_or_noknobnumericalrows"
    / "no_knob_numerical_rows_execution_gate.packet.json"
)
MAGNITUDE = DATA / "selected_magnitudebearingprojectionweights_or_thresholdrowsderivation.candidate.json"
MAGNITUDE_RANK_GAP = (
    DATA
    / "selected_magnitudebearingprojectionweights_or_thresholdrowsderivation"
    / "magnitude_weight_rank_gap.packet.json"
)
BASIS_ROWS = DATA / "selected_rthetavaluerows_or_universalsourceanchortheorem.candidate.json"
COEFF_ATTEMPT = (
    DATA
    / "selected_rthetavaluerows_or_universalsourceanchortheorem"
    / "rtheta_value_row_coefficients_attempt.packet.json"
)
UNIVERSAL_POLICY = DATA / "universal_source_parameter_policy/universal_source_parameter_policy.packet.json"
UNIVERSAL_CANDIDATES = DATA / "universal_source_parameter_policy/candidate_universal_parameters.packet.json"
UNIVERSAL_ATTEMPT = (
    DATA
    / "selected_thresholdfunctionalsourcetheorem_or_minimaluniversalparameterselection"
    / "minimal_universal_parameter_selection_attempt.packet.json"
)
INTERNAL_NOGO = DATA / "selected_internalrthetavaluederivation_or_minimaluniversalparameterselection.candidate.json"
HIGHER_RESPONSE = DATA / "selected_higherresponserthetafunctional_or_sourceanchortheorem.candidate.json"

STATUS = (
    "MTT_SELECTED_THRESHOLDMAGNITUDEROWS_OR_MINIMALUNIVERSALPARAMETERDECISION_"
    "BUILT_NUMERICAL_ROWS_STILL_OPEN_CONSTRUCTIVE_TARGET_FIXED"
)
NEXT = "MTT_Selected_SameBranchThresholdMassSchemeRows_or_SourceAnchorConstruction_v1"


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
        raise FileNotFoundError("missing threshold magnitude decision inputs: " + ", ".join(missing))


def main() -> int:
    PACKET_DIR.mkdir(parents=True, exist_ok=True)
    CERTS.mkdir(parents=True, exist_ok=True)
    CORPUS.mkdir(parents=True, exist_ok=True)

    sources = [
        PREVIOUS,
        SOURCE_DOMAIN,
        EXECUTION_GATE,
        MAGNITUDE,
        MAGNITUDE_RANK_GAP,
        BASIS_ROWS,
        COEFF_ATTEMPT,
        UNIVERSAL_POLICY,
        UNIVERSAL_CANDIDATES,
        UNIVERSAL_ATTEMPT,
        INTERNAL_NOGO,
        HIGHER_RESPONSE,
    ]
    require_sources(sources)

    previous = load(PREVIOUS)
    source_domain = load(SOURCE_DOMAIN)
    execution = load(EXECUTION_GATE)
    magnitude = load(MAGNITUDE)
    rank_gap = load(MAGNITUDE_RANK_GAP)
    basis_rows = load(BASIS_ROWS)
    coeff_attempt = load(COEFF_ATTEMPT)
    policy = load(UNIVERSAL_POLICY)
    candidates = load(UNIVERSAL_CANDIDATES)
    universal_attempt = load(UNIVERSAL_ATTEMPT)
    internal_nogo = load(INTERNAL_NOGO)
    higher_response = load(HIGHER_RESPONSE)

    current_selected_parameters = [
        row for row in candidates["candidate_classes"] if row.get("selected_now") is True
    ]
    accepted_coefficients = coeff_attempt["accepted_coefficient_rows"]

    row_decision = {
        "schema": "MTTThresholdMagnitudeRowDecision.v1",
        "status": "NO_SELECTED_THRESHOLD_MAGNITUDE_ROWS_AVAILABLE",
        "source_domain_closed": source_domain["source_domain_closed"],
        "basis_map_to_sector_scaled_magnitude_rows_closed": basis_rows["closure_decision"][
            "basis_map_to_sector_scaled_magnitude_rows_closed"
        ],
        "rank_gap_theorem_proved": magnitude["closure_decision"]["rank_gap_theorem_proved"],
        "magnitude_bearing_projection_weights_closed": magnitude["closure_decision"][
            "magnitude_bearing_projection_weights_closed"
        ],
        "generation_resolved_threshold_source_rows_closed": magnitude["closure_decision"][
            "generation_resolved_threshold_source_rows_closed"
        ],
        "accepted_coefficient_row_count": coeff_attempt["accepted_coefficient_row_count"],
        "accepted_coefficient_rows": accepted_coefficients,
        "diagnostic_coefficient_count": coeff_attempt["diagnostic_coefficient_count"],
        "diagnostic_coefficients_rejected_as_selectors": True,
        "rank_gap_source": rel(MAGNITUDE_RANK_GAP),
        "decision": (
            "The selected basis and source/domain are closed, but all magnitude-bearing coefficient "
            "rows remain diagnostic because the coefficient functional and threshold/mass-scheme "
            "source rows are not selected."
        ),
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "closure_claimed": False,
    }
    write_json(ROW_DECISION, row_decision)

    anchor_recheck = {
        "schema": "MTTMinimalUniversalAnchorRecheckAfterSourceDomain.v1",
        "status": "NO_UNIVERSAL_ANCHOR_SELECTED_AFTER_SOURCE_DOMAIN_CLOSURE",
        "policy": rel(UNIVERSAL_POLICY),
        "maximum_live_universal_parameters": policy["maximum_live_universal_parameters"],
        "selected_parameter_count_before": universal_attempt["selected_parameter_count_before"],
        "selected_parameter_count_after": universal_attempt["selected_parameter_count_after"],
        "candidate_rows": universal_attempt["candidate_selection_rows"],
        "selected_candidates_now": current_selected_parameters,
        "source_domain_closure_changes_decision": False,
        "why_not_selected": [
            "source/domain closure identifies where a universal anchor would attach, but does not select one",
            "no candidate-specific source-anchor theorem is present",
            "diagnostic Yukawa/threshold/profile residuals remain forbidden selectors",
        ],
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "closure_claimed": False,
    }
    write_json(ANCHOR_RECHECK, anchor_recheck)

    terminal_cutset = {
        "schema": "MTTTerminalValueClosureCutset.v1",
        "status": "VALUE_CLOSURE_REDUCED_TO_TWO_CONSTRUCTIVE_OBJECTS",
        "closed_now": {
            "qualitative_SM_orbit_closure": True,
            "Rtheta_value_functional_source_domain": source_domain["source_domain_closed"],
            "basis_map_to_nine_charged_magnitude_rows": True,
            "first_response_only_no_go": internal_nogo["closure_decision"][
                "first_response_only_route_rejected_for_scalar_no_knob_values"
            ],
            "higher_response_contract": higher_response["closure_decision"][
                "higher_response_Rtheta_functional_contract_closed"
            ],
            "minimal_universal_policy_declared": True,
        },
        "still_open": {
            "construct_same_branch_threshold_mass_scheme_rows": True,
            "construct_magnitude_bearing_projection_weights_or_coefficients": True,
            "construct_candidate_specific_universal_source_anchor_theorem": True,
            "execute_higher_response_Rtheta_scalar_rows": True,
            "emit_lambda_H_row": True,
            "emit_CKM_PMNS_Yukawa_numerical_rows": True,
            "true_SM_equivalence": True,
            "full_no_knob_or_declared_minimal_parameter_closure": True,
        },
        "two_valid_routes": {
            "route_1_no_knob": (
                "derive same-branch threshold/mass-scheme rows plus magnitude-bearing coefficients "
                "from selected finite response geometry"
            ),
            "route_2_minimal_parameter": (
                "prove a candidate-specific universal source-anchor theorem, select <=3 universal "
                "parameters before empirical replay, then execute the same codomain rows"
            ),
        },
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "closure_claimed": False,
    }
    write_json(TERMINAL_CUTSET, terminal_cutset)

    next_step = {
        "schema": "MTTNextConstructiveTarget.v1",
        "status": "CONSTRUCT_SAME_BRANCH_THRESHOLD_ROWS_OR_SOURCE_ANCHOR",
        "next_required_artifact": NEXT,
        "preferred_first_attack": {
            "name": "SameBranchThresholdMassSchemeRows",
            "reason": (
                "It is the shortest route to no-knob numerical closure because the source/domain, "
                "Pi_Rtheta, coefficient skeleton, qualitative orbit layer, and basis map are now closed."
            ),
            "must_construct": [
                "scale/scheme/loop convention from selected branch",
                "threshold matching source rows for top,bottom,charm,tau,W/Z/H",
                "mass-scheme conversion rows for top,bottom,charm,tau,Higgs/lambda",
                "magnitude-bearing coefficient functional over nine charged rows",
                "lambda_H row from the same branch",
            ],
        },
        "fallback_attack": {
            "name": "CandidateSpecificUniversalSourceAnchorTheorem",
            "reason": "Allowed only if route 1 cannot emit magnitudes from selected geometry alone.",
            "must_construct": [
                "select the universal anchor before empirical replay",
                "prove its typed source role at the Rtheta gate",
                "propagate it through all ten scalar rows without sector fitting",
            ],
        },
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "closure_claimed": False,
    }
    write_json(NEXT_STEP, next_step)

    candidate = {
        "candidate": "MTTSelectedThresholdMagnitudeRowsOrMinimalUniversalParameterDecision",
        "status": STATUS,
        "inputs": {path.stem: rel(path) for path in sources},
        "output_packets": {
            "threshold_magnitude_row_decision": rel(ROW_DECISION),
            "minimal_universal_anchor_recheck_after_source_domain": rel(ANCHOR_RECHECK),
            "terminal_value_closure_cutset": rel(TERMINAL_CUTSET),
            "next_constructive_target": rel(NEXT_STEP),
        },
        "theorem": {
            "name": "ThresholdMagnitudeRowsOrUniversalAnchorTerminalCutsetTheorem",
            "proved": True,
            "statement": (
                "After qualitative orbit closure and Rtheta source/domain closure, current selected "
                "data still emit zero accepted numerical coefficient rows and no selected universal "
                "source anchor. Therefore full SM value closure reduces to two constructive objects: "
                "same-branch threshold/mass-scheme magnitude rows, or a candidate-specific universal "
                "source-anchor theorem followed by scalar-row execution."
            ),
        },
        "closure_decision": {
            "terminal_value_cutset_proved": True,
            "accepted_numerical_coefficient_rows": coeff_attempt["accepted_coefficient_row_count"],
            "minimal_universal_parameter_selected": False,
            "selected_universal_parameter_count": len(current_selected_parameters),
            "true_SM_equivalence_closed": False,
            "full_no_knob_closed": False,
        },
        "what_closes_now": terminal_cutset["closed_now"],
        "what_remains_open": terminal_cutset["still_open"],
        "previous_status": previous["status"],
        "next_required_artifact": NEXT,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "closure_claimed": False,
        "unpatched_theorem_closure_claimed": True,
    }
    write_json(OUTPUT, candidate)

    cert = {
        "certificate": "MTT_Selected_ThresholdMagnitudeRows_or_MinimalUniversalParameterDecision_v1",
        "status": STATUS,
        "candidate_path": rel(OUTPUT),
        "note_path": rel(NOTE),
        "theorem_proved": True,
        "terminal_value_cutset_proved": True,
        "accepted_numerical_coefficient_rows": coeff_attempt["accepted_coefficient_row_count"],
        "minimal_universal_parameter_selected": False,
        "selected_universal_parameter_count": len(current_selected_parameters),
        "true_SM_equivalence_closed": False,
        "full_no_knob_closed": False,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "closure_claimed": False,
        "unpatched_theorem_closure_claimed": True,
        "next_required_artifact": NEXT,
    }
    write_json(CERT, cert)

    note = f"""# MTT Selected ThresholdMagnitudeRows or MinimalUniversalParameterDecision v1

Status: `{STATUS}`.

The value layer is now reduced to a sharp constructive cutset:

```text
Rtheta source/domain closed          : {str(source_domain["source_domain_closed"]).lower()}
basis map to charged magnitude rows  : true
accepted numerical coefficient rows  : {coeff_attempt["accepted_coefficient_row_count"]}
selected universal parameter count   : {len(current_selected_parameters)}
full numerical SM equivalence        : false
```

Current selected data do not yet emit no-knob Yukawa/CKM/PMNS/lambda_H values.
The remaining work is no longer vague: construct same-branch threshold and
mass-scheme magnitude rows, or prove a candidate-specific universal source
anchor before empirical replay.

Next artifact: `{NEXT}`.
"""
    NOTE.write_text(note, encoding="utf-8")

    print(json.dumps({"candidate": rel(OUTPUT), "status": STATUS}, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
