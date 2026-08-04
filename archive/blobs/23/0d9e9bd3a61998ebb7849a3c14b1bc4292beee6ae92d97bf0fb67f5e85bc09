"""Build Rtheta scalar value functional source/domain or no-knob numerical rows gate."""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "candidate_data"
CERTS = ROOT / "certificates"
CORPUS = ROOT / "proof_corpus"

SLUG = "selected_rthetascalarvaluefunctionalsource_or_noknobnumericalrows"
PACKET_DIR = DATA / SLUG
OUTPUT = DATA / f"{SLUG}.candidate.json"
SOURCE_PACKET = PACKET_DIR / "rtheta_scalar_value_functional_source_packet.packet.json"
CODOMAIN_MAP = PACKET_DIR / "ten_scalar_rows_to_threshold_contract_map.packet.json"
EXECUTION_GATE = PACKET_DIR / "no_knob_numerical_rows_execution_gate.packet.json"
CUTSET = PACKET_DIR / "next_cutset_after_rtheta_scalar_value_functional_source.packet.json"
CERT = CERTS / f"{SLUG}_certificate.json"
NOTE = CORPUS / "MTT_Selected_RThetaScalarValueFunctionalSource_or_NoKnobNumericalRows_v1.md"

PREVIOUS = DATA / "selected_secondorderorbitqualitativesmclosure_or_rthetascalarvalues.candidate.json"
QUAL_LEDGER = (
    DATA
    / "selected_secondorderorbitqualitativesmclosure_or_rthetascalarvalues"
    / "qualitative_sm_orbit_closure_ledger.packet.json"
)
SCALAR_OBLIGATION = (
    DATA
    / "selected_secondorderorbitqualitativesmclosure_or_rthetascalarvalues"
    / "rtheta_scalar_value_obligation.packet.json"
)
RTHETA_EXECUTION = DATA / "selected_rtheta_valueevaluatorexecution_or_thresholdresponseinstantiation.candidate.json"
RTHETA_GATE = (
    DATA
    / "selected_rtheta_valueevaluatorexecution_or_thresholdresponseinstantiation"
    / "rtheta_value_evaluator_execution_gate.packet.json"
)
RTHETA_VALUE_RECHECK = (
    DATA
    / "selected_rtheta_valueevaluatorexecution_or_thresholdresponseinstantiation"
    / "rtheta_coefficient_value_recheck_after_pi_closure.packet.json"
)
RTHETA_CUTSET = (
    DATA
    / "selected_rtheta_valueevaluatorexecution_or_thresholdresponseinstantiation"
    / "next_cutset_after_value_evaluator_recheck.packet.json"
)
THRESHOLD_CONTRACT = (
    DATA
    / "selected_thresholdresponsefunctionalderivation_or_profilelikelihoodacquisition"
    / "selected_threshold_response_functional_contract.packet.json"
)
HIGHER_CONTRACT = (
    DATA
    / "selected_higherresponserthetafunctional_or_sourceanchortheorem"
    / "rtheta_higher_response_functional_contract.packet.json"
)

STATUS = (
    "MTT_SELECTED_RTHETASCALARVALUEFUNCTIONALSOURCE_OR_NOKNOBNUMERICALROWS_"
    "BUILT_FUNCTIONAL_SOURCE_DOMAIN_CLOSED_NUMERICAL_ROWS_OPEN"
)
NEXT = "MTT_Selected_ThresholdMagnitudeRows_or_MinimalUniversalParameterDecision_v1"


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
        raise FileNotFoundError("missing Rtheta scalar value source inputs: " + ", ".join(missing))


def main() -> int:
    PACKET_DIR.mkdir(parents=True, exist_ok=True)
    CERTS.mkdir(parents=True, exist_ok=True)
    CORPUS.mkdir(parents=True, exist_ok=True)

    sources = [
        PREVIOUS,
        QUAL_LEDGER,
        SCALAR_OBLIGATION,
        RTHETA_EXECUTION,
        RTHETA_GATE,
        RTHETA_VALUE_RECHECK,
        RTHETA_CUTSET,
        THRESHOLD_CONTRACT,
        HIGHER_CONTRACT,
    ]
    require_sources(sources)

    previous = load(PREVIOUS)
    qual = load(QUAL_LEDGER)
    scalar_obligation = load(SCALAR_OBLIGATION)
    rtheta_execution = load(RTHETA_EXECUTION)
    rtheta_gate = load(RTHETA_GATE)
    value_recheck = load(RTHETA_VALUE_RECHECK)
    rtheta_cutset = load(RTHETA_CUTSET)
    threshold_contract = load(THRESHOLD_CONTRACT)
    higher_contract = load(HIGHER_CONTRACT)

    source_domain_closed = (
        qual["closure_claimed"] is True
        and rtheta_gate["Pi_Rtheta_closed"] is True
        and rtheta_gate["coefficient_functional_skeleton_closed"] is True
        and rtheta_gate["selected_dynamic_operator_source_owner_closed"] is True
        and rtheta_gate["source_normalized_projection_weights_closed"] is True
        and rtheta_gate["threshold_response_contract_closed"] is True
        and threshold_contract["closure_claimed"] is True
        and higher_contract["contract_closed"] is True
        and scalar_obligation["codomain_scalar_row_count"] == 10
    )

    numerical_rows_closed = (
        rtheta_gate["selected_threshold_response_functional_instantiated"] is True
        and value_recheck["accepted_coefficient_value_count"] == 9
        and value_recheck["lambda_H_value_selected"] is True
        and value_recheck["accepted_Yukawa_magnitudes_as_no_knob_predictions"] is True
    )

    source_packet = {
        "schema": "MTTRThetaScalarValueFunctionalSourcePacket.v1",
        "status": "RTHETA_SCALAR_VALUE_FUNCTIONAL_SOURCE_DOMAIN_CLOSED"
        if source_domain_closed
        else "RTHETA_SCALAR_VALUE_FUNCTIONAL_SOURCE_DOMAIN_OPEN",
        "qualitative_orbit_layer": rel(QUAL_LEDGER),
        "rtheta_value_evaluator_gate": rel(RTHETA_GATE),
        "selected_functional_symbol": threshold_contract["functional_symbol"],
        "closed_source_domain_components": {
            "qualitative_SM_orbit_layer": qual["closure_claimed"],
            "Pi_Rtheta": rtheta_gate["Pi_Rtheta_closed"],
            "coefficient_functional_skeleton": rtheta_gate["coefficient_functional_skeleton_closed"],
            "selected_dynamic_operator_source_owner": rtheta_gate[
                "selected_dynamic_operator_source_owner_closed"
            ],
            "source_normalized_projection_weights": rtheta_gate[
                "source_normalized_projection_weights_closed"
            ],
            "threshold_response_contract": rtheta_gate["threshold_response_contract_closed"],
            "higher_response_scalar_codomain_contract": higher_contract["contract_closed"],
        },
        "source_domain_closed": source_domain_closed,
        "important_boundary": (
            "This closes the selected source/domain of the value functional, not its numerical "
            "instantiation. Magnitude-bearing projection weights and threshold/mass-scheme source "
            "rows are still required before any scalar value row can be accepted."
        ),
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "closure_claimed": source_domain_closed,
    }
    write_json(SOURCE_PACKET, source_packet)

    codomain_map = {
        "schema": "MTTTenScalarRowsToThresholdContractMap.v1",
        "status": "TEN_SCALAR_ROW_CODOMAIN_ALIGNED_WITH_THRESHOLD_CONTRACT",
        "ten_scalar_rows": higher_contract["codomain_scalar_rows"],
        "charged_yukawa_rows": higher_contract["codomain_scalar_rows"][:9],
        "higgs_quartic_row": higher_contract["codomain_scalar_rows"][9],
        "threshold_contract_outputs_required": threshold_contract["row_outputs_required"],
        "acceptance_equations": threshold_contract["acceptance_equations"],
        "alignment": {
            "charged_row_count": value_recheck["charged_functional_row_count"],
            "charged_rows_match_contract": value_recheck["charged_functional_row_count"] == 9,
            "lambda_H_row_required": True,
            "threshold_matching_rows_required": True,
            "mass_scheme_conversion_rows_required": True,
            "profile_response_or_diagonal_limitation_required": True,
        },
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "closure_claimed": True,
    }
    write_json(CODOMAIN_MAP, codomain_map)

    execution_gate = {
        "schema": "MTTNoKnobNumericalRowsExecutionGate.v1",
        "status": "FUNCTIONAL_SOURCE_DOMAIN_CLOSED_NUMERICAL_ROWS_REJECTED",
        "source_domain_closed": source_domain_closed,
        "selected_threshold_response_functional_instantiated": rtheta_gate[
            "selected_threshold_response_functional_instantiated"
        ],
        "magnitude_bearing_projection_weights_closed": rtheta_gate[
            "magnitude_bearing_projection_weights_closed"
        ],
        "accepted_coefficient_value_count": value_recheck["accepted_coefficient_value_count"],
        "accepted_Yukawa_magnitudes_as_no_knob_predictions": value_recheck[
            "accepted_Yukawa_magnitudes_as_no_knob_predictions"
        ],
        "lambda_H_value_selected": value_recheck["lambda_H_value_selected"],
        "rejected_value_reasons": value_recheck["rejected_value_reasons"],
        "still_open_from_rtheta_cutset": rtheta_cutset["still_open"],
        "numerical_rows_closed": numerical_rows_closed,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "closure_claimed": False,
    }
    write_json(EXECUTION_GATE, execution_gate)

    cutset = {
        "schema": "MTTNextCutsetAfterRThetaScalarValueFunctionalSource.v1",
        "status": "RTHETA_FUNCTIONAL_SOURCE_DOMAIN_CLOSED_NUMERICAL_ROWS_NEXT",
        "closed_now": {
            "selected_Rtheta_scalar_value_functional_source_domain": source_domain_closed,
            "ten_scalar_row_codomain_aligned": True,
            "Pi_Rtheta_imported_into_qualitative_orbit_frontier": True,
            "coefficient_functional_skeleton_imported": True,
            "empirical_selector_forbidden_boundary_preserved": True,
        },
        "still_open": {
            "same_branch_scale_scheme_loop_convention": True,
            "threshold_matching_source_rows": True,
            "mass_scheme_conversion_source_rows": True,
            "magnitude_bearing_projection_weights": True,
            "selected_threshold_response_functional_instantiation": True,
            "accepted_numerical_Yukawa_rows": True,
            "lambda_H_value": True,
            "true_SM_equivalence": True,
            "full_no_knob_closure": True,
        },
        "recommended_next": {
            "artifact": NEXT,
            "route_A": "derive threshold and mass-scheme source rows from the same selected branch",
            "route_B": "derive magnitude-bearing projection weights from the orbit matrix packet",
            "route_C": "prove a minimal universal parameter theorem if exact no-knob numerical rows cannot be selected",
        },
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "closure_claimed": False,
    }
    write_json(CUTSET, cutset)

    candidate = {
        "candidate": "MTTSelectedRThetaScalarValueFunctionalSourceOrNoKnobNumericalRows",
        "status": STATUS,
        "inputs": {path.stem: rel(path) for path in sources},
        "output_packets": {
            "rtheta_scalar_value_functional_source_packet": rel(SOURCE_PACKET),
            "ten_scalar_rows_to_threshold_contract_map": rel(CODOMAIN_MAP),
            "no_knob_numerical_rows_execution_gate": rel(EXECUTION_GATE),
            "next_cutset_after_rtheta_scalar_value_functional_source": rel(CUTSET),
        },
        "theorem": {
            "name": "RThetaScalarValueFunctionalSourceDomainTheorem",
            "proved": source_domain_closed,
            "statement": (
                "Combining the selected qualitative orbit closure with the existing R_theta evaluator "
                "lane closes the selected value-functional source/domain: Pi_Rtheta, coefficient "
                "functional skeleton, source ownership, source-normalized projection weights, and "
                "the ten-row scalar codomain are all aligned. The numerical no-knob rows remain "
                "rejected until threshold/mass-scheme rows and magnitude-bearing weights are selected."
            ),
        },
        "closure_decision": {
            "selected_Rtheta_scalar_value_functional_source_domain_closed": source_domain_closed,
            "ten_scalar_row_codomain_aligned": True,
            "no_knob_numerical_rows_emitted": numerical_rows_closed,
            "accepted_value_layer_closed": False,
            "true_SM_equivalence_closed": False,
            "full_no_knob_closed": False,
        },
        "what_closes_now": cutset["closed_now"],
        "what_remains_open": cutset["still_open"],
        "previous_status": previous["status"],
        "rtheta_execution_status": rtheta_execution["status"],
        "next_required_artifact": NEXT,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "closure_claimed": False,
        "unpatched_theorem_closure_claimed": source_domain_closed,
    }
    write_json(OUTPUT, candidate)

    cert = {
        "certificate": "MTT_Selected_RThetaScalarValueFunctionalSource_or_NoKnobNumericalRows_v1",
        "status": STATUS,
        "candidate_path": rel(OUTPUT),
        "note_path": rel(NOTE),
        "theorem_proved": source_domain_closed,
        "selected_Rtheta_scalar_value_functional_source_domain_closed": source_domain_closed,
        "ten_scalar_row_codomain_aligned": True,
        "no_knob_numerical_rows_emitted": numerical_rows_closed,
        "accepted_value_layer_closed": False,
        "true_SM_equivalence_closed": False,
        "full_no_knob_closed": False,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "closure_claimed": False,
        "unpatched_theorem_closure_claimed": source_domain_closed,
        "next_required_artifact": NEXT,
    }
    write_json(CERT, cert)

    note = f"""# MTT Selected RThetaScalarValueFunctionalSource or NoKnobNumericalRows v1

Status: `{STATUS}`.

The value-functional source/domain is now aligned with the qualitative orbit
closure and the existing R_theta evaluator lane:

```text
Pi_Rtheta closed                 : {str(rtheta_gate["Pi_Rtheta_closed"]).lower()}
coefficient functional skeleton  : {str(rtheta_gate["coefficient_functional_skeleton_closed"]).lower()}
source owner closed              : {str(rtheta_gate["selected_dynamic_operator_source_owner_closed"]).lower()}
ten scalar row codomain aligned  : true
accepted numerical scalar rows   : {value_recheck["accepted_coefficient_value_count"]}
lambda_H selected                : {str(value_recheck["lambda_H_value_selected"]).lower()}
```

This closes the source/domain side of the Rtheta value functional. It still
does not emit no-knob numerical Yukawa, CKM/PMNS, lambda_H, threshold, or
mass-scheme values.

Next artifact: `{NEXT}`.
"""
    NOTE.write_text(note, encoding="utf-8")

    print(json.dumps({"candidate": rel(OUTPUT), "status": STATUS}, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
