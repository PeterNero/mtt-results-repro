"""Build integrated post-source frontier / higher-response value gate.

This artifact reconciles the source-promotion replay, stationary/dotD
frontier, VSD-01 first-response closure, and the newer higher-response payload
ledgers.  Its job is to prevent scope drift: source/dotD closure is real at the
first-response/source-stack level, but it is not a no-knob Yukawa/Higgs value
derivation.
"""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "candidate_data"
CERTS = ROOT / "certificates"
CORPUS = ROOT / "proof_corpus"

SLUG = "selected_integratedpostsourcefrontier_or_higherresponsevaluegate"
BASE = DATA / SLUG
OUTPUT = DATA / f"{SLUG}.candidate.json"
SOURCE_SCOPE = BASE / "source_scope_reconciliation.packet.json"
VALUE_FRONTIER = BASE / "postsource_value_frontier.packet.json"
NEXT_CUTSET = BASE / "nonlooping_next_value_cutset.packet.json"
CERT = CERTS / f"{SLUG}_certificate.json"
NOTE = CORPUS / "MTT_Selected_IntegratedPostSourceFrontier_or_HigherResponseValueGate_v1.md"

STATUS = (
    "MTT_SELECTED_INTEGRATEDPOSTSOURCEFRONTIER_OR_HIGHERRESPONSEVALUEGATE_BUILT_"
    "SOURCE_DOTD_RETIRED_VALUE_CLOSURE_OPEN"
)
NEXT = "MTT_Selected_HigherOrderFullResponseMatrices_or_SecondOrderFlavorLift_v1"


INPUTS = {
    "source_promotion_replay": DATA / "selected_unpatchedsourcepromotionreplay_or_fullsmclosuregate.candidate.json",
    "stationary_dotd_frontier": DATA / "selected_stationaryprojector_dotd_integrated_frontier.candidate.json",
    "current_frontier": DATA / "selected_currentfrontierreconciliation_or_higherresponsepayloadledger.candidate.json",
    "higher_response_payload": DATA / "selected_higherresponsepayloadrows_sourcepromotion_or_fulls2valueexecution.candidate.json",
    "selected_hym_payload": DATA / "selected_selectedhymoperatorpayloadpromotion_or_rhoedefulls2execution.candidate.json",
    "transport_validator": DATA / "selected_transport_conjugation_validator_replay.candidate.json",
    "gauge_transported_trace": DATA / "selected_gauge_transported_bn_phifin_trace.candidate.json",
    "vsd01_dynamic": DATA / "selected_vsd01_dynamicoperatorbackimport_or_yukawavaluefrontier.candidate.json",
    "postsource_observable": DATA / "selected_postsourceformal110_observableaudit_or_fullsmgap.candidate.json",
    "yukawa_value_audit": DATA / "selected_yukawamagnitudergclosure_or_finaltruesmequivalenceaudit.candidate.json",
    "vsd02_threshold": DATA / "selected_vsd02thresholdresponserule_or_externallikelihoodimport.candidate.json",
}


def rel(path: Path) -> str:
    return str(path.relative_to(ROOT)).replace("\\", "/")


def load(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def write_json(path: Path, payload: dict[str, Any]) -> None:
    path.write_text(json.dumps(payload, indent=2, sort_keys=True) + "\n", encoding="utf-8")


def require_inputs() -> None:
    missing = [rel(path) for path in INPUTS.values() if not path.exists()]
    if missing:
        raise FileNotFoundError("missing integrated frontier inputs: " + ", ".join(missing))


def main() -> int:
    BASE.mkdir(parents=True, exist_ok=True)
    CERTS.mkdir(parents=True, exist_ok=True)
    CORPUS.mkdir(parents=True, exist_ok=True)
    require_inputs()

    packets = {name: load(path) for name, path in INPUTS.items()}

    source = packets["source_promotion_replay"]
    stationary = packets["stationary_dotd_frontier"]
    current = packets["current_frontier"]
    higher = packets["higher_response_payload"]
    hym = packets["selected_hym_payload"]
    transport = packets["transport_validator"]
    trace = packets["gauge_transported_trace"]
    vsd01 = packets["vsd01_dynamic"]
    observable = packets["postsource_observable"]
    yukawa = packets["yukawa_value_audit"]
    vsd02 = packets["vsd02_threshold"]

    source_stack_closed = source["promotion_decision"]["unpatched_source_promotion_stack_closed"]
    first_response_closed = current["closure_decision"]["first_response_scope_closed"]
    dotd_closed = (
        stationary["closure_decision"]["alpha1_driver_verified"]
        and stationary["closure_decision"]["selected_dotD_source_verified"]
        and higher["closure_decision"]["dotD_alpha1_payload_closed"]
    )
    stationary_rho_closed = transport["promotion_decision"]["rho_candidate_promoted_to_validator_ready_sector_rho_s_packet"]
    trace_closed_functionally = trace["promotion_decision"]["functional_selected_trace_proved"]
    diagonal_hym_closed = hym["closure_decision"]["diagonal_End0_operator_payload_closed"]
    vsd01_dynamic_closed = vsd01["closure_decision"]["VSD01_dynamic_tensor_subgate_closed"]

    source_scope = {
        "schema": "MTTIntegratedSourceScopeReconciliation.v1",
        "status": "FIRST_RESPONSE_SOURCE_AND_DOTD_RETIRED_VALUE_SCOPE_OPEN",
        "closed_source_scope": {
            "unpatched_source_promotion_replay_stack": source_stack_closed,
            "VSD01_first_response_source_scope": first_response_closed,
            "VSD01_dynamic_tensor_subgate": vsd01_dynamic_closed,
            "stationary_rho_s_transport_validator": stationary_rho_closed,
            "same_branch_dotD_alpha1": dotd_closed,
            "gauge_transported_functional_Phi_fin_trace": trace_closed_functionally,
            "diagonal_End0_HYM_operator_payload": diagonal_hym_closed,
        },
        "scope_guardrails": {
            "source_stack_is_not_yukawa_value_fit": True,
            "first_response_is_not_full_S2_value_execution": True,
            "formal_110_rows_are_not_accepted_mass_or_threshold_rows": True,
            "explicit_local_or_patched_source_principles_are_not_needed_to_reopen_first_response": True,
        },
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "closure_claimed": False,
    }

    postsource_value_frontier = {
        "schema": "MTTPostSourceHigherResponseValueFrontier.v1",
        "status": "POSTSOURCE_VALUE_CLOSURE_OPEN_AFTER_SOURCE_DOTD_RETIREMENT",
        "closed_now": {
            "source_stack": source_stack_closed,
            "stationary_projector_dotd": dotd_closed,
            "VSD01_first_response_dynamic_operator_layer": vsd01_dynamic_closed,
            "formal_110_observable_layer_audited": observable["closure_decision"]["formal_110_first_response_audited"],
            "first_non_scalar_family_splitting_detected": observable["closure_decision"]["first_non_scalar_family_splitting"],
        },
        "still_open": {
            "higher_order_full_response_matrices": True,
            "selected_second_order_physical_matrices": True,
            "higher_response_Rtheta_execution": current["closure_decision"]["higher_response_payload_rows_closed"] is False,
            "full_S2_value_execution": current["closure_decision"]["full_S2_value_execution_closed"] is False,
            "accepted_Yukawa_Higgs_value_rows": yukawa["promotion_decision"]["accepted_Yukawa_magnitudes_closed"] is False,
            "threshold_matching_and_mass_scheme_rows": vsd02["closure_decision"]["accepted_threshold_response_rule_closed"] is False,
            "covariance_profile_likelihood_or_no_knob_replacement": True,
            "true_SM_equivalence": True,
            "full_no_knob": True,
        },
        "why_not_closed": [
            "The first post-source layer is non-scalar but still twofold-degenerate and CP-even at the audited layer.",
            "No accepted common-scale Yukawa/Higgs rows are derived or imported as source rows.",
            "Threshold and mass-scheme rows are classified but not accepted or no-knob derived.",
            "Higher-order/full-response matrices have not been emitted from the selected branch.",
        ],
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "closure_claimed": False,
    }

    next_cutset = {
        "schema": "MTTNonLoopingNextValueCutset.v1",
        "status": "NEXT_VALUE_CUTSET_SELECTED",
        "primary_internal_route": {
            "artifact": NEXT,
            "goal": (
                "Emit selected higher-order/full-response matrices from the same branch, then "
                "test whether they break the remaining twofold degeneracy and produce nonzero CP-odd "
                "flavor invariants before any external threshold import."
            ),
        },
        "parallel_precision_route": {
            "artifact": "MTT_Selected_VSD02AcceptedSourceRowsFill_or_NoKnobThresholdDerivation_v1",
            "goal": (
                "Either derive accepted threshold/mass-scheme rows internally or import an external "
                "profile-likelihood source as an explicitly external precision layer, not as a no-knob selector."
            ),
        },
        "forbidden_reentries": [
            "re-proving A_selected, b_selected, deltaTheta_C1 for VSD01 first response",
            "reopening alpha1/dotD as the active blocker",
            "using observed masses, CKM/PMNS, lambda_H, or threshold values as selectors",
            "counting formal 110-row replay as accepted Yukawa/Higgs magnitude closure",
        ],
        "success_criteria_for_next_gate": [
            "emit actual selected higher-response matrices",
            "show whether CP-odd invariant becomes nonzero",
            "derive or reject three distinct family masses at the same source scope",
            "connect the value rows to VSD02 threshold/mass-scheme conventions without proxy fitting",
        ],
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "closure_claimed": False,
    }

    write_json(SOURCE_SCOPE, source_scope)
    write_json(VALUE_FRONTIER, postsource_value_frontier)
    write_json(NEXT_CUTSET, next_cutset)

    candidate = {
        "candidate": "MTTSelectedIntegratedPostSourceFrontierOrHigherResponseValueGate",
        "status": STATUS,
        "inputs": {name: rel(path) for name, path in INPUTS.items()},
        "output_packets": {
            "source_scope_reconciliation": rel(SOURCE_SCOPE),
            "postsource_value_frontier": rel(VALUE_FRONTIER),
            "nonlooping_next_value_cutset": rel(NEXT_CUTSET),
        },
        "what_closes_now": {
            "source_scope_contradiction_resolved": True,
            "source_stack_not_reopened_as_value_blocker": True,
            "alpha1_dotD_not_reopened_as_value_blocker": True,
            "first_response_vs_higher_response_scope_separated": True,
            "next_nonlooping_value_cutset_selected": True,
        },
        "what_remains_open": {
            "higher_order_full_response_matrices": True,
            "selected_second_order_physical_matrices": True,
            "accepted_Yukawa_Higgs_value_rows": True,
            "threshold_matching_and_mass_scheme_rows": True,
            "covariance_profile_or_no_knob_replacement": True,
            "true_SM_equivalence": True,
            "full_no_knob": True,
        },
        "closure_decision": {
            "source_stack_closed_for_first_response": source_stack_closed and first_response_closed,
            "dotD_alpha1_retired": dotd_closed,
            "stationary_operator_payload_closed_enough_for_first_response": stationary_rho_closed and diagonal_hym_closed,
            "higher_response_value_closure": False,
            "accepted_Yukawa_Higgs_value_closure": False,
            "threshold_response_closure": False,
            "true_SM_equivalence_closed": False,
            "full_no_knob_closed": False,
        },
        "theorem": {
            "name": "IntegratedPostSourceFrontierScopeTheorem",
            "proved": True,
            "statement": (
                "After importing the source-promotion replay, transport/rho_s replay, same-branch dotD closure, "
                "and VSD01 first-response dynamic tensor closure, the remaining active SM-closure problem is not "
                "source promotion or alpha1. It is value closure: higher-order/full-response matrices, Rtheta and "
                "threshold/mass-scheme rows, and accepted Yukawa/Higgs value rows without observed-data selection."
            ),
        },
        "next_required_artifact": NEXT,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "closure_claimed": False,
    }

    cert = {
        "certificate": "MTT_Selected_IntegratedPostSourceFrontier_or_HigherResponseValueGate_v1",
        "status": STATUS,
        "candidate_path": rel(OUTPUT),
        "note_path": rel(NOTE),
        "source_stack_closed_for_first_response": candidate["closure_decision"]["source_stack_closed_for_first_response"],
        "dotD_alpha1_retired": dotd_closed,
        "higher_response_value_closure": False,
        "true_SM_equivalence_closed": False,
        "full_no_knob_closed": False,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "closure_claimed": False,
        "next_required_artifact": NEXT,
    }

    note = f"""# MTT Selected IntegratedPostSourceFrontier or HigherResponseValueGate v1

Status: `{STATUS}`.

## Closed Scope

The apparent source-frontier conflict is resolved by scope.  The replay/source
stack closes the VSD01 first-response source gate and the first dynamic operator
layer.  The same-branch `dotD alpha1`, transported stationary `rho_s`, and
diagonal End0/HYM support are also retired as active first-response blockers.

## Open Scope

This does not close no-knob SM values.  Still open:

- higher-order/full-response matrices,
- selected second-order physical matrix promotion,
- nonzero CP-odd flavor invariant and realistic family splitting,
- accepted Yukawa/Higgs value rows,
- threshold/mass-scheme/covariance rows or an explicit external precision layer.

## Guardrail

Do not re-enter through `A_selected`, `b_selected`, `deltaTheta_C1`, or alpha1.
Those are not the active wall.  The active wall is value emission and precision
source ownership after the first-response layer.

Next artifact: `{NEXT}`.
"""

    write_json(OUTPUT, candidate)
    write_json(CERT, cert)
    NOTE.write_text(note, encoding="utf-8")
    print(f"built {rel(OUTPUT)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
