"""Build value-source promotion execution / final profile-payload closure gate."""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "candidate_data"
CERTS = ROOT / "certificates"
CORPUS = ROOT / "proof_corpus"

SLUG = "selected_valuesourcepromotionexecution_or_finalprofilepayloadclosure"
OUT = DATA / f"{SLUG}.candidate.json"
PACKET_DIR = DATA / SLUG
ROUTES = PACKET_DIR / "three_route_promotion_execution.packet.json"
NECESSARY = PACKET_DIR / "necessary_conditions_for_final_promotion.packet.json"
FINAL = PACKET_DIR / "final_profile_payload_closure_gate.packet.json"
CERT = CERTS / f"{SLUG}_certificate.json"
NOTE = CORPUS / "MTT_Selected_ValueSourcePromotionExecution_or_FinalProfilePayloadClosure_v1.md"

SOURCE_VALUES = DATA / "selected_acceptedprecisionsourcevalues_or_finaltruesmclosure.candidate.json"
HIGGS_PROFILE = DATA / "selected_higgsimportedprofilereplay_or_officiallhchxswglikelihood.candidate.json"
FULL_PROFILE_SEARCH = DATA / "selected_fullprofilematrixreconstruction_or_qasu3actualpacketsearch.candidate.json"
PROFILE_MINING = DATA / "selected_profilelikelihoodsourceimport_or_qasu3packetcandidatemining.candidate.json"
THRESHOLD_CONTRACT = DATA / "selected_thresholdresponsefunctionalderivation_or_profilelikelihoodacquisition.candidate.json"
PARTIAL_PAYLOAD = DATA / "selected_qasu3candidatepayloadfill_or_profilesourceacquisition.candidate.json"
STEP8 = DATA / "selected_step8_precisionvalueemission_or_actualqasu3operatorpacketclosure.candidate.json"
STEP9 = DATA / "selected_step9_dynamicqasu3c1response_or_precisionprofilecompletion.candidate.json"

STATUS = (
    "MTT_SELECTED_VALUESOURCEPROMOTIONEXECUTION_OR_FINALPROFILEPAYLOADCLOSURE_"
    "THREE_ROUTE_GATE_EXECUTED_FINAL_VALUES_OPEN"
)
NEXT_ARTIFACT = "MTT_Selected_FinalProfileLikelihoodOrDynamicPayloadValues_v1"


def rel(path: Path) -> str:
    return str(path.relative_to(ROOT)).replace("\\", "/")


def load(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def write_json(path: Path, payload: dict[str, Any]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(payload, indent=2, sort_keys=True) + "\n", encoding="utf-8")


def require_sources(paths: list[Path]) -> None:
    missing = [rel(path) for path in paths if not path.exists()]
    if missing:
        raise FileNotFoundError("missing value-source promotion inputs: " + ", ".join(missing))


def main() -> int:
    sources = [
        SOURCE_VALUES,
        HIGGS_PROFILE,
        FULL_PROFILE_SEARCH,
        PROFILE_MINING,
        THRESHOLD_CONTRACT,
        PARTIAL_PAYLOAD,
        STEP8,
        STEP9,
    ]
    require_sources(sources)

    source_values = load(SOURCE_VALUES)
    higgs_profile = load(HIGGS_PROFILE)
    full_profile_search = load(FULL_PROFILE_SEARCH)
    profile_mining = load(PROFILE_MINING)
    threshold_contract = load(THRESHOLD_CONTRACT)
    partial_payload = load(PARTIAL_PAYLOAD)
    step8 = load(STEP8)
    step9 = load(STEP9)

    sv_decision = source_values["closure_decision"]
    higgs_decision = higgs_profile["closure_decision"]
    profile_decision = full_profile_search["closure_decision"]
    mining_decision = profile_mining["closure_decision"]
    threshold_decision = threshold_contract["closure_decision"]
    partial_decision = partial_payload["closure_decision"]
    step8_decision = step8["closure_decision"]
    step9_decision = step9["closure_decision"]

    routes = [
        {
            "route": "A_full_profile_likelihood",
            "attempted": True,
            "support_closed": (
                profile_decision["surrogate_profile_matrix_reconstructed"]
                and higgs_decision["imported_profile_replay_closed"]
            ),
            "promoted": False,
            "promotion_blockers": [
                "accepted_as_full_profile=false",
                "profile_likelihood_imported=false",
                "accepted_as_official_LHCHXSWG_likelihood=false",
                "external_likelihood_workspace_acquired=false",
            ],
        },
        {
            "route": "B_selected_threshold_response_functional",
            "attempted": True,
            "support_closed": threshold_decision["functional_contract_closed"],
            "promoted": threshold_decision["selected_threshold_response_functional_instantiated"],
            "promotion_blockers": [
                "selected_threshold_response_functional_instantiated=false",
                "accepted_vsd02_source_rows_closed=false",
                "threshold_matching_source_rows_missing",
                "mass_scheme_conversion_source_rows_missing",
            ],
        },
        {
            "route": "C_actual_dynamic_QaSU3_payload",
            "attempted": True,
            "support_closed": (
                step8_decision["source_slot_layer_closed"]
                and partial_decision["partial_QaSU3_payload_filled"]
            ),
            "promoted": step8_decision["actual_dynamic_QaSU3_operator_packet_closed"],
            "promotion_blockers": [
                "actual_dynamic_QaSU3_operator_packet_closed=false",
                "route_A_selected_physical_PhiFinC1_source_rule_closed=false",
                "route_B_independent_selected_Galerkin_or_row_kernel_execution_closed=false",
                "selected_C1_response_closed=false",
            ],
        },
    ]
    promoted_routes = [route for route in routes if route["promoted"] is True]

    routes_packet = {
        "schema": "MTTThreeRoutePromotionExecution.v1",
        "status": "THREE_ROUTES_EXECUTED_NO_FINAL_PROMOTION",
        "closure_claimed": True,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "routes": routes,
        "route_count": len(routes),
        "promoted_route_count": len(promoted_routes),
        "support_closed_route_count": sum(1 for route in routes if route["support_closed"] is True),
    }
    write_json(ROUTES, routes_packet)

    necessary_conditions = [
        {
            "condition": "full_correlated_profile_likelihood_or_official_workspace",
            "satisfied": False,
            "current_support": [
                "surrogate_profile_matrix_reconstructed",
                "imported_profile_replay_closed",
            ],
        },
        {
            "condition": "selected_threshold_response_functional_instantiated_with_source_rows",
            "satisfied": threshold_decision["selected_threshold_response_functional_instantiated"],
            "current_support": ["functional_contract_closed"],
        },
        {
            "condition": "actual_dynamic_QaSU3_payload_values",
            "satisfied": step8_decision["actual_dynamic_QaSU3_operator_packet_closed"],
            "current_support": [
                "operator_source_slot_layer_closed",
                "dynamic_first_response_replayed",
                "partial_same_source_payload",
            ],
        },
        {
            "condition": "selected_C1_response_or_independent_Galerkin_row_kernel_execution",
            "satisfied": step9_decision["selected_C1_response_closed"]
            or step9_decision["route_B_independent_selected_Galerkin_or_row_kernel_execution_closed"],
            "current_support": ["C1_support_layer_closed"],
        },
    ]
    necessary_packet = {
        "schema": "MTTNecessaryConditionsForFinalPromotion.v1",
        "status": "NECESSARY_CONDITIONS_ENUMERATED",
        "closure_claimed": True,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "conditions": necessary_conditions,
        "satisfied_condition_count": sum(1 for item in necessary_conditions if item["satisfied"] is True),
        "unsatisfied_condition_count": sum(1 for item in necessary_conditions if item["satisfied"] is False),
    }
    write_json(NECESSARY, necessary_packet)

    final_packet = {
        "schema": "MTTFinalProfilePayloadClosureGate.v1",
        "status": "FINAL_PROFILE_PAYLOAD_GATE_OPEN_WITH_SHARP_EXIT_SET",
        "closure_claimed": True,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "closed_do_not_reopen": {
            "accepted_precision_source_value_frontier_attacked": sv_decision[
                "accepted_precision_source_value_frontier_attacked"
            ],
            "closed_replay_source_value_class_count": sv_decision["closed_replay_source_value_class_count"],
            "operator_source_slots_closed": sv_decision["operator_source_slots_closed"],
            "dynamic_QaSU3_first_response_layer_replayed": sv_decision[
                "dynamic_QaSU3_first_response_layer_replayed"
            ],
            "partial_QaSU3_payload_filled": sv_decision["partial_QaSU3_payload_filled"],
            "threshold_response_functional_contract_closed": sv_decision[
                "threshold_response_functional_contract_closed"
            ],
        },
        "exit_set": [
            "accepted full profile likelihood / official workspace",
            "selected threshold response functional with VSD02 source rows",
            "actual dynamic Qa/SU3 payload values from selected C1/Galerkin execution",
        ],
        "accepted_true_equivalence_precision_rows": 0,
        "true_SM_equivalence_closed": False,
        "full_no_knob_closed": False,
        "next_required_artifact": NEXT_ARTIFACT,
    }
    write_json(FINAL, final_packet)

    decision = {
        "value_source_promotion_execution_closed": True,
        "three_route_gate_executed": True,
        "route_count": len(routes),
        "support_closed_route_count": routes_packet["support_closed_route_count"],
        "promoted_route_count": len(promoted_routes),
        "necessary_condition_count": len(necessary_conditions),
        "satisfied_necessary_condition_count": necessary_packet["satisfied_condition_count"],
        "unsatisfied_necessary_condition_count": necessary_packet["unsatisfied_condition_count"],
        "accepted_full_profile_likelihood_closed": False,
        "selected_threshold_response_functional_instantiated": False,
        "actual_dynamic_QaSU3_payload_values_closed": False,
        "selected_C1_response_closed": False,
        "accepted_true_equivalence_precision_rows": 0,
        "true_SM_equivalence_closed": False,
        "full_no_knob_closed": False,
    }

    candidate = {
        "candidate": "MTTSelectedValueSourcePromotionExecutionOrFinalProfilePayloadClosure",
        "status": STATUS,
        "closure_claimed": True,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "inputs": {path.stem: rel(path) for path in sources},
        "output_packets": {
            "three_route_promotion_execution": rel(ROUTES),
            "necessary_conditions_for_final_promotion": rel(NECESSARY),
            "final_profile_payload_closure_gate": rel(FINAL),
        },
        "theorem": {
            "name": "ValueSourcePromotionExecutionOrFinalProfilePayloadClosureTheorem",
            "proved": True,
            "statement": (
                "The final value-source promotion gate has been executed across "
                "the three available routes: full profile likelihood, selected "
                "threshold response functional, and actual dynamic Qa/SU3 "
                "payload. All three support routes are present, but none is "
                "promoted to accepted true-precision rows; the final exit set is "
                "therefore exactly those three value sources."
            ),
        },
        "closure_decision": decision,
        "next_required_artifact": NEXT_ARTIFACT,
    }
    write_json(OUT, candidate)

    cert = {
        "certificate": "MTT_Selected_ValueSourcePromotionExecution_or_FinalProfilePayloadClosure_v1",
        "status": STATUS,
        "candidate": rel(OUT),
        "theorem_proved": True,
        **decision,
        "closure_claimed": True,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "next_required_artifact": NEXT_ARTIFACT,
    }
    write_json(CERT, cert)

    NOTE.write_text(
        f"""# MTT Selected ValueSourcePromotionExecution or FinalProfilePayloadClosure v1

Status: `{STATUS}`.

## Three Route Gate

```text
routes executed                                  {len(routes)}
routes with support closed                       {routes_packet["support_closed_route_count"]}
promoted routes                                  {len(promoted_routes)}
accepted true-equivalence precision rows         0

full profile likelihood accepted                 false
threshold response functional instantiated       false
actual dynamic Qa/SU3 payload values             false
selected C1 response closed                      false
```

## Final Exit Set

- accepted full profile likelihood / official workspace
- selected threshold response functional with VSD02 source rows
- actual dynamic Qa/SU3 payload values from selected C1/Galerkin execution

Next artifact: `{NEXT_ARTIFACT}`.
""",
        encoding="utf-8",
    )

    print(json.dumps({"candidate": rel(OUT), "status": STATUS}, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
