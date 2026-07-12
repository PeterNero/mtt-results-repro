"""Build higher-response Rtheta functional / source-anchor theorem artifact."""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "candidate_data"
CERTS = ROOT / "certificates"
CORPUS = ROOT / "proof_corpus"

SLUG = "selected_higherresponserthetafunctional_or_sourceanchortheorem"
PACKET_DIR = DATA / SLUG
OUTPUT = DATA / f"{SLUG}.candidate.json"
PAYLOAD_GAP = PACKET_DIR / "higher_response_source_payload_gap.packet.json"
CONTRACT = PACKET_DIR / "rtheta_higher_response_functional_contract.packet.json"
ANCHOR_RECHECK = PACKET_DIR / "source_anchor_theorem_recheck.packet.json"
DECISION = PACKET_DIR / "higher_response_or_source_anchor_decision.packet.json"
CUTSET = PACKET_DIR / "next_cutset_after_higher_response_contract.packet.json"
CERT = CERTS / f"{SLUG}_certificate.json"
NOTE = CORPUS / "MTT_Selected_HigherResponseRThetaFunctional_or_SourceAnchorTheorem_v1.md"

PREVIOUS = DATA / "selected_internalrthetavaluederivation_or_minimaluniversalparameterselection.candidate.json"
PREV_CUTSET = (
    DATA
    / "selected_internalrthetavaluederivation_or_minimaluniversalparameterselection"
    / "next_cutset_after_internal_rtheta_attack.packet.json"
)
HIGHER_ORDER = DATA / "selected_routec_higherorder_fullresponse_flavor_splitting.candidate.json"
PHIFIN_ALPHA1 = DATA / "selected_phifinalpha1payloadvalues_or_typedbnretardedderivativeexecution.candidate.json"
ALPHA1_PACKET = (
    DATA
    / "selected_phifinalpha1payloadvalues_or_typedbnretardedderivativeexecution"
    / "alpha1_derivative_dotd_execution_packet.packet.json"
)
TYPED_BN_STATUS = (
    DATA
    / "selected_phifinalpha1payloadvalues_or_typedbnretardedderivativeexecution"
    / "typed_bn_retarded_execution_status.packet.json"
)
PRIMITIVE_SELECTOR = DATA / "selected_primitivefibershift_or_typedretardedselector_sourcetheorem.candidate.json"
INTERNAL_ATTACK = (
    DATA
    / "selected_internalrthetavaluederivation_or_minimaluniversalparameterselection"
    / "internal_rtheta_first_response_sufficiency_test.packet.json"
)
POLICY_MATRIX = (
    DATA
    / "selected_noknobvaluederivationpostpi_or_minimaluniversalparameterpolicy"
    / "minimal_universal_parameter_policy_matrix.packet.json"
)

STATUS = (
    "MTT_SELECTED_HIGHERRESPONSERTHETAFUNCTIONAL_OR_SOURCEANCHORTHEOREM_"
    "BUILT_PAYLOAD_SPEC_SOURCE_ANCHOR_OPEN"
)
NEXT = "MTT_Selected_DynamicPhiFinC1PayloadRows_or_HigherResponseExecution_v1"


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
        raise FileNotFoundError("missing higher-response sources: " + ", ".join(missing))


def main() -> int:
    PACKET_DIR.mkdir(parents=True, exist_ok=True)
    CERTS.mkdir(parents=True, exist_ok=True)
    CORPUS.mkdir(parents=True, exist_ok=True)

    sources = [
        PREVIOUS,
        PREV_CUTSET,
        HIGHER_ORDER,
        PHIFIN_ALPHA1,
        ALPHA1_PACKET,
        TYPED_BN_STATUS,
        PRIMITIVE_SELECTOR,
        INTERNAL_ATTACK,
        POLICY_MATRIX,
    ]
    require_sources(sources)

    previous = load(PREVIOUS)
    prev_cutset = load(PREV_CUTSET)
    higher_order = load(HIGHER_ORDER)
    phifin_alpha1 = load(PHIFIN_ALPHA1)
    alpha1_packet = load(ALPHA1_PACKET)
    typed_bn_status = load(TYPED_BN_STATUS)
    primitive_selector = load(PRIMITIVE_SELECTOR)
    internal_attack = load(INTERNAL_ATTACK)
    policy_matrix = load(POLICY_MATRIX)

    lane_a_payload = alpha1_packet["lane_A_visible_routec_source_identity"]["phi_fin_payload"]
    open_payload_flags = lane_a_payload["open_payload_flags"]
    higher_required = higher_order["path_B_full_response_criterion"]["required_outputs"]
    higher_missing = higher_order["path_A_higher_order_criterion"]["why_values_unavailable"][
        "alpha1_missing_selected_operator_data"
    ]

    payload_gap = {
        "schema": "MTTHigherResponseSourcePayloadGap.v1",
        "status": "DYNAMIC_PHIFIN_C1_PAYLOAD_ROWS_MISSING_HIGHER_RESPONSE_NOT_EXECUTABLE",
        "higher_order_source": rel(HIGHER_ORDER),
        "phifin_alpha1_packet_source": rel(ALPHA1_PACKET),
        "current_layer_no_go_proved": higher_order["current_layer_no_go"]["proved"],
        "current_values_available": higher_order["path_B_full_response_criterion"][
            "current_values_available"
        ],
        "open_payload_flags": open_payload_flags,
        "open_payload_flag_count": len(open_payload_flags),
        "required_full_response_outputs": higher_required,
        "missing_selected_operator_data": higher_missing,
        "typed_bn_retarded_derivative_closed": phifin_alpha1["closure_decision"][
            "typed_bn_retarded_derivative_closed"
        ],
        "phi_fin_dynamic_c1_payload_closed": phifin_alpha1["closure_decision"][
            "phi_fin_dynamic_c1_payload_closed"
        ],
        "primitive_fiber_class_quotient_selected": primitive_selector[
            "fiber_class_quotient_selected_claimed"
        ],
        "absolute_matrix_representative_selected": primitive_selector[
            "observable_class_payload"
        ]["selected_matrix_representative"],
        "selected_higher_response_payload_rows_emitted": False,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "closure_claimed": False,
    }
    write_json(PAYLOAD_GAP, payload_gap)

    scalar_rows = [
        "theta_coeff.u.gen1",
        "theta_coeff.u.gen2",
        "theta_coeff.u.gen3",
        "theta_coeff.d.gen1",
        "theta_coeff.d.gen2",
        "theta_coeff.d.gen3",
        "theta_coeff.e.gen1",
        "theta_coeff.e.gen2",
        "theta_coeff.e.gen3",
        "lambda_H",
    ]
    contract = {
        "schema": "MTTRThetaHigherResponseFunctionalContract.v1",
        "status": "HIGHER_RESPONSE_RTHETA_FUNCTIONAL_CONTRACT_BUILT_EXECUTION_OPEN",
        "contract_closed": True,
        "domain_requirements": [
            "selected zero-mode bases for Q,u,d,L,e,N,H",
            "selected Hermitian metric and L2 Gram-Schmidt rule",
            "selected Riesz/Green operator",
            "selected finite Hessian C1 source blocks",
            "selected rho_E transition data and sector projectors",
            "selected dotD_alpha1 and selected deltaTheta_C1",
            "primitive C1 contractions and sector response matrices M_u,M_d,M_e,M_nuD",
        ],
        "codomain_scalar_rows": scalar_rows,
        "codomain_scalar_row_count": len(scalar_rows),
        "acceptance_tests_after_execution": {
            "mass_hierarchy": "nonzero traceless Hermitian correction in each charged sector",
            "CKM": "nonzero commutator norm between selected u and d Hermitian corrections",
            "PMNS": "nonzero commutator norm between selected e and nuD Hermitian corrections",
            "CP": "nonzero selected complex CP-odd invariant",
            "lambda_H": "same-branch Higgs/quartic row emitted with the scalar rows",
            "no_target_selector": "observed masses, CKM, PMNS, CP, Higgs, or profile residuals do not choose the functional or rows",
        },
        "execution_inputs_available_now": False,
        "selected_functional_executed": False,
        "accepted_scalar_row_count_now": 0,
        "why_contract_matters": [
            "it converts the vague no-knob wall into a finite row-emission target",
            "it prevents first-response qualitative matrices from being mistaken for scalar value rows",
            "it states the exact tests required before Yukawa/mass/mixing closure can be claimed",
        ],
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "closure_claimed": False,
    }
    write_json(CONTRACT, contract)

    anchor_recheck = {
        "schema": "MTTSourceAnchorTheoremRecheck.v1",
        "status": "SOURCE_ANCHOR_THEOREM_NOT_SELECTED",
        "policy_matrix_source": rel(POLICY_MATRIX),
        "typed_bn_status_source": rel(TYPED_BN_STATUS),
        "selected_universal_parameter_count": policy_matrix["selected_universal_parameter_count"],
        "maximum_live_universal_parameters": policy_matrix["maximum_live_universal_parameters"],
        "candidate_specific_source_theorem_present": policy_matrix[
            "candidate_specific_source_theorem_present"
        ],
        "typed_retarded_derivative_emitted": typed_bn_status["typed_retarded_derivative_emitted"],
        "selected_primitive_response_emitted": typed_bn_status["selected_primitive_response_emitted"],
        "retarded_source_selector_selected": primitive_selector["typed_retarded_selector"]["selected"],
        "source_anchor_theorem_closed": False,
        "why_not_closed": [
            "the primitive fiber theorem selects a current-observable quotient class only, not full operator matrices",
            "the typed retarded derivative remains support-only and does not emit a selected source selector",
            "the universal parameter policy has zero selected universal parameters",
        ],
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "closure_claimed": False,
    }
    write_json(ANCHOR_RECHECK, anchor_recheck)

    decision = {
        "schema": "MTTHigherResponseOrSourceAnchorDecision.v1",
        "status": "CONTRACT_BUILT_EXECUTION_AND_SOURCE_ANCHOR_OPEN",
        "higher_response_contract_closed": True,
        "higher_response_payload_rows_emitted": False,
        "selected_higher_response_Rtheta_functional_executed": False,
        "source_anchor_theorem_closed": False,
        "selected_universal_parameter_count": policy_matrix["selected_universal_parameter_count"],
        "first_response_only_route_rejected": prev_cutset["closed_now"][
            "first_response_only_route_rejected_for_scalar_no_knob_values"
        ],
        "dynamic_first_response_rank": internal_attack["dynamic_normal_form_rank"],
        "scalar_target_slot_count": internal_attack["scalar_target_slot_count"],
        "no_knob_value_derivation_closed": False,
        "true_SM_equivalence_closed": False,
        "full_no_knob_closed": False,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "closure_claimed": False,
    }
    write_json(DECISION, decision)

    cutset = {
        "schema": "MTTNextCutsetAfterHigherResponseContract.v1",
        "status": "NEXT_ATTACK_DYNAMIC_PHIFIN_C1_PAYLOAD_ROWS_OR_HIGHER_RESPONSE_EXECUTION",
        "closed_now": {
            "higher_response_payload_gap_imported": True,
            "higher_response_Rtheta_functional_contract_built": True,
            "source_anchor_rechecked_not_selected": True,
            "ten_scalar_row_target_fixed": True,
            "first_response_no_go_preserved": True,
        },
        "still_open": {
            "selected_dynamic_PhiFin_C1_payload_rows": True,
            "selected_zero_mode_bases": True,
            "selected_Hermitian_metric_and_Riesz_Green": True,
            "selected_finite_Hessian_C1_source_blocks": True,
            "selected_rho_E_transition_data": True,
            "selected_sector_projectors": True,
            "selected_dotD_alpha1_and_deltaTheta_C1": True,
            "primitive_C1_contractions": True,
            "sector_response_matrices": True,
            "higher_response_Rtheta_execution": True,
            "candidate_specific_universal_source_anchor_theorem": True,
            "Yukawa_mass_mixing_value_closure": True,
            "true_SM_equivalence": True,
            "full_no_knob": True,
        },
        "recommended_next": {
            "artifact": NEXT,
            "route_A": "emit the dynamic Phi_fin/C1 payload rows and run the higher-response contract",
            "route_B": "prove a typed retarded/source-anchor theorem that supplies the same missing payload rows",
            "route_C": "publish the current result as a precise no-go frontier if no payload source exists",
        },
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "closure_claimed": False,
    }
    write_json(CUTSET, cutset)

    candidate = {
        "candidate": "MTTSelectedHigherResponseRThetaFunctionalOrSourceAnchorTheorem",
        "status": STATUS,
        "inputs": {path.stem: rel(path) for path in sources},
        "output_packets": {
            "higher_response_source_payload_gap": rel(PAYLOAD_GAP),
            "rtheta_higher_response_functional_contract": rel(CONTRACT),
            "source_anchor_theorem_recheck": rel(ANCHOR_RECHECK),
            "higher_response_or_source_anchor_decision": rel(DECISION),
            "next_cutset_after_higher_response_contract": rel(CUTSET),
        },
        "theorem": {
            "name": "HigherResponseFunctionalContractAndSourceAnchorGapTheorem",
            "proved": True,
            "statement": (
                "After the first-response no-go, the correct no-knob target is a selected higher-response "
                "Rtheta functional with ten scalar output rows. The current corpus supplies the contract and "
                "acceptance tests, but not the dynamic Phi_fin/C1 payload rows or a source-selected universal "
                "anchor theorem. Therefore the next proof step is payload emission/execution, not another "
                "external replay or diagnostic coefficient fit."
            ),
        },
        "what_closes_now": cutset["closed_now"],
        "what_remains_open": cutset["still_open"],
        "closure_decision": {
            "higher_response_Rtheta_functional_contract_closed": True,
            "codomain_scalar_row_count": len(scalar_rows),
            "higher_response_payload_rows_emitted": False,
            "selected_higher_response_Rtheta_functional_executed": False,
            "source_anchor_theorem_closed": False,
            "selected_universal_parameter_count": policy_matrix["selected_universal_parameter_count"],
            "accepted_scalar_row_count_now": 0,
            "no_knob_value_derivation_closed": False,
            "true_SM_equivalence_closed": False,
            "full_no_knob_closed": False,
        },
        "previous_status": previous["status"],
        "next_required_artifact": NEXT,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "closure_claimed": False,
        "unpatched_theorem_closure_claimed": False,
    }
    write_json(OUTPUT, candidate)

    cert = {
        "certificate": "MTT_Selected_HigherResponseRThetaFunctional_or_SourceAnchorTheorem_v1",
        "status": STATUS,
        "candidate_path": rel(OUTPUT),
        "note_path": rel(NOTE),
        "theorem_proved": True,
        "higher_response_Rtheta_functional_contract_closed": True,
        "codomain_scalar_row_count": len(scalar_rows),
        "higher_response_payload_rows_emitted": False,
        "selected_higher_response_Rtheta_functional_executed": False,
        "source_anchor_theorem_closed": False,
        "selected_universal_parameter_count": policy_matrix["selected_universal_parameter_count"],
        "accepted_scalar_row_count_now": 0,
        "no_knob_value_derivation_closed": False,
        "true_SM_equivalence_closed": False,
        "full_no_knob_closed": False,
        "next_required_artifact": NEXT,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "closure_claimed": False,
        "unpatched_theorem_closure_claimed": False,
    }
    write_json(CERT, cert)

    note = f"""# MTT Selected HigherResponseRThetaFunctional or SourceAnchorTheorem v1

Status: `{STATUS}`.

The functional target is now finite and explicit.

```text
higher-response contract closed        : true
scalar output rows                     : {len(scalar_rows)}
dynamic Phi_fin/C1 payload emitted     : false
source-anchor theorem closed           : false
selected universal parameters          : {policy_matrix["selected_universal_parameter_count"]}
no-knob value derivation closed        : false
true SM equivalence                    : false
```

The next proof is an execution proof, not another replay proof: emit the
selected dynamic `Phi_fin/C1` payload rows and run the higher-response
functional, or prove a selected source-anchor theorem that supplies the same
payload without fitting observed rows.

Next artifact: `{NEXT}`.
"""
    NOTE.write_text(note, encoding="utf-8")

    print(json.dumps({"candidate": rel(OUTPUT), "status": STATUS}, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
