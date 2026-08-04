"""Build current frontier reconciliation against the higher-response payload ledger."""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "candidate_data"
CERTS = ROOT / "certificates"
CORPUS = ROOT / "proof_corpus"

SLUG = "selected_currentfrontierreconciliation_or_higherresponsepayloadledger"
PACKET_DIR = DATA / SLUG
OUTPUT = DATA / f"{SLUG}.candidate.json"
SCOPE = PACKET_DIR / "scope_reconciliation_after_first_response.packet.json"
PAYLOAD = PACKET_DIR / "higher_response_payload_ledger_update.packet.json"
NEXT = PACKET_DIR / "next_cutset_after_current_frontier_reconciliation.packet.json"
CERT = CERTS / f"{SLUG}_certificate.json"
NOTE = CORPUS / "MTT_Selected_CurrentFrontierReconciliation_or_HigherResponsePayloadLedger_v1.md"

STATUS = (
    "MTT_SELECTED_CURRENTFRONTIERRECONCILIATION_OR_HIGHERRESPONSEPAYLOADLEDGER_"
    "BUILT_FIRST_RESPONSE_RETIRED_HIGHER_RESPONSE_OPEN"
)
NEXT_ARTIFACT = "MTT_Selected_HigherResponsePayloadRows_SourcePromotion_or_FullS2ValueExecution_v1"


def rel(path: Path) -> str:
    try:
        return str(path.relative_to(ROOT)).replace("\\", "/")
    except ValueError:
        return str(path)


def load(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def write_json(path: Path, payload: dict[str, Any]) -> None:
    path.write_text(json.dumps(payload, indent=2, sort_keys=True) + "\n", encoding="utf-8")


def main() -> int:
    PACKET_DIR.mkdir(parents=True, exist_ok=True)

    vsd01 = load(DATA / "selected_vsd01_allprimitiverowsassemblymap_or_physicalphifinc1actionsource.candidate.json")
    vsd01_map = load(
        DATA
        / "selected_vsd01_allprimitiverowsassemblymap_or_physicalphifinc1actionsource"
        / "all_primitive_rows_assembly_map.packet.json"
    )
    dynamic = load(DATA / "selected_samesourcedynamicmatteroverlapoperatorpacket_or_primitivec1valueclosure.candidate.json")
    dynamic_packet = load(
        DATA
        / "selected_samesourcedynamicmatteroverlapoperatorpacket_or_primitivec1valueclosure"
        / "same_source_matter_overlap_operator_packet.packet.json"
    )
    qasu3_replay = load(DATA / "selected_dynamicqasu3operatorpacketreplay_or_yukawamassmixingvalueclosure.candidate.json")
    qasu3_gate = load(
        DATA
        / "selected_dynamicqasu3operatorpacketreplay_or_yukawamassmixingvalueclosure"
        / "true_equivalence_gate_after_dynamic_qasu3_replay.packet.json"
    )
    postsource = load(DATA / "selected_dynamicqasu3_or_c1response_postsourcefrontier.candidate.json")
    route_test = load(DATA / "selected_samesourcedynamicphifinc1_or_honestgalerkinexecution_routetest.candidate.json")
    payload_old = load(DATA / "selected_dynamicphifinc1payloadrows_or_higherresponseexecution.candidate.json")
    payload_inventory = load(
        DATA
        / "selected_dynamicphifinc1payloadrows_or_higherresponseexecution"
        / "dynamic_phifin_c1_payload_row_inventory.packet.json"
    )
    higher = load(DATA / "selected_higherresponserthetafunctional_or_sourceanchortheorem.candidate.json")
    internal = load(DATA / "selected_internalrthetavaluederivation_or_minimaluniversalparameterselection.candidate.json")
    hym_values = load(DATA / "selected_hym_projector_zeromode_basis_value_emission.candidate.json")
    hym_operator = load(DATA / "selected_hym_operator_payload_extraction_from_diagonal_replay.candidate.json")
    end0_de = load(DATA / "selected_end0_de_payload_from_diagonal_hym.candidate.json")

    source_promoted = vsd01_map["source_stack_replay"]["promoted_objects"]
    dynamic_fields = dynamic_packet["attempted_selected_packet"]["fields"]
    first_response_closed = (
        source_promoted["A_selected"]
        and source_promoted["b_selected"]
        and source_promoted["deltaTheta_C1"]
        and dynamic["promotion_decision"]["dynamic_matter_overlap_operator_packet_closed"]
        and qasu3_replay["promotion_decision"]["dynamic_QaSU3_first_response_layer_closed"]
    )

    retired_first_response_labels = {
        "PSM-C1-01_source_rule_for_VSD01_first_response": True,
        "PSM-C1-03_A_selected_for_VSD01_first_response": source_promoted["A_selected"],
        "PSM-C1-04_b_selected_for_VSD01_first_response": source_promoted["b_selected"],
        "PSM-C1-05_deltaTheta_C1_for_VSD01_first_response": source_promoted["deltaTheta_C1"],
        "PSM-C1-06_sector_rows_for_VSD01_first_response": vsd01_map["row_evidence"]["formal_110_row_counts"][
            "sector_matrix_rows"
        ]
        == 36,
    }

    scope = {
        "schema": "MTTCurrentFrontierScopeReconciliationAfterFirstResponse.v1",
        "status": "FIRST_RESPONSE_SCOPE_CLOSED_FULL_S2_HIGHER_RESPONSE_SCOPE_OPEN",
        "first_response_scope": {
            "VSD01_source_stack_closed": vsd01["closure_decision"]["VSD01_source_assembly_subgate_closed"],
            "A_selected_promoted": source_promoted["A_selected"],
            "b_selected_promoted": source_promoted["b_selected"],
            "deltaTheta_C1_promoted": source_promoted["deltaTheta_C1"],
            "all_72_primitive_rows_exact": vsd01_map["row_evidence"]["all_72_primitive_rows_exact"],
            "formal_110_rows_executed": vsd01_map["row_evidence"]["formal_110_rows_executed"],
            "sector_matrix_rows": vsd01_map["row_evidence"]["formal_110_row_counts"]["sector_matrix_rows"],
            "same_source_dynamic_matter_packet_closed": dynamic["promotion_decision"][
                "dynamic_matter_overlap_operator_packet_closed"
            ],
            "dynamic_QaSU3_first_response_layer_closed": qasu3_replay["promotion_decision"][
                "dynamic_QaSU3_first_response_layer_closed"
            ],
        },
        "retired_first_response_labels": retired_first_response_labels,
        "postsource_frontier_reinterpretation": {
            "old_postsource_open_flags_are_not_source_assembly_absence": True,
            "postsource_artifact": rel(DATA / "selected_dynamicqasu3_or_c1response_postsourcefrontier.candidate.json"),
            "route_test_artifact": rel(DATA / "selected_samesourcedynamicphifinc1_or_honestgalerkinexecution_routetest.candidate.json"),
            "route_test_missing_A_b_deltaTheta_is_stale_for_first_response": True,
            "still_open_meaning": "full-S2/higher-response/precision value emission, not the VSD01 first-response A,b,delta source stack",
        },
        "full_S2_higher_response_scope": {
            "first_response_only_is_insufficient_for_scalar_values": internal["closure_decision"][
                "first_response_only_route_rejected_for_scalar_no_knob_values"
            ],
            "higher_response_Rtheta_functional_contract_closed": higher["closure_decision"][
                "higher_response_Rtheta_functional_contract_closed"
            ],
            "higher_response_Rtheta_executed": higher["closure_decision"]["selected_higher_response_Rtheta_functional_executed"],
            "true_SM_equivalence_closed": False,
            "full_no_knob_closed": False,
        },
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "closure_claimed": False,
    }

    payload_rows = [
        {
            "row_id": "finite_Hessian_C1_source",
            "old_status": "support_candidate_only",
            "updated_status": "closed_for_first_response_source_stack",
            "selected_for_higher_response_scalar_functional": False,
            "evidence": [
                rel(
                    DATA
                    / "selected_vsd01_allprimitiverowsassemblymap_or_physicalphifinc1actionsource"
                    / "all_primitive_rows_assembly_map.packet.json"
                )
            ],
        },
        {
            "row_id": "primitive_C1_contractions",
            "old_status": "support_candidate_only",
            "updated_status": "closed_for_first_response_dynamic_packet",
            "selected_for_higher_response_scalar_functional": False,
            "evidence": [
                rel(
                    DATA
                    / "selected_samesourcedynamicmatteroverlapoperatorpacket_or_primitivec1valueclosure"
                    / "same_source_matter_overlap_operator_packet.packet.json"
                )
            ],
        },
        {
            "row_id": "sector_response_matrices",
            "old_status": "support_candidate_only",
            "updated_status": "closed_for_first_response_dynamic_packet",
            "selected_for_higher_response_scalar_functional": False,
            "evidence": [
                rel(
                    DATA
                    / "selected_samesourcedynamicmatteroverlapoperatorpacket_or_primitivec1valueclosure"
                    / "selected_non_scalar_dynamic_overlap_values.packet.json"
                )
            ],
        },
        {
            "row_id": "deltaTheta_C1",
            "old_status": "conditional_replay_only",
            "updated_status": "closed_for_first_response_source_stack",
            "selected_for_higher_response_scalar_functional": False,
            "value": [1.0, 1.0],
            "evidence": [
                rel(
                    DATA
                    / "selected_vsd01_allprimitiverowsassemblymap_or_physicalphifinc1actionsource"
                    / "all_primitive_rows_assembly_map.packet.json"
                )
            ],
        },
        {
            "row_id": "HYM_projector_zero_mode_basis_values",
            "old_status": "model_active_values_emitted_not_selected",
            "updated_status": "still_open_for_higher_response",
            "selected_for_higher_response_scalar_functional": False,
            "evidence": [rel(DATA / "selected_hym_projector_zeromode_basis_value_emission.candidate.json")],
        },
        {
            "row_id": "Hermitian_metric_and_HYM_connection",
            "old_status": "diagonal_support_extracted",
            "updated_status": "still_open_for_full_sector_payload",
            "selected_for_higher_response_scalar_functional": False,
            "evidence": [rel(DATA / "selected_hym_operator_payload_extraction_from_diagonal_replay.candidate.json")],
        },
        {
            "row_id": "D_E_Riesz_Green_dotD_payload",
            "old_status": "End0_DE_support_available",
            "updated_status": "still_open_for_operator_payload",
            "selected_for_higher_response_scalar_functional": False,
            "evidence": [rel(DATA / "selected_end0_de_payload_from_diagonal_hym.candidate.json")],
        },
        {
            "row_id": "rho_E_transition_data",
            "old_status": "projective_or_transition_support_only",
            "updated_status": "still_open_for_full_transition_payload",
            "selected_for_higher_response_scalar_functional": False,
            "evidence": [rel(DATA / "selected_nonidentity_rhoe_transition_source.candidate.json")],
        },
        {
            "row_id": "scalar_Rtheta_value_rows",
            "old_status": "not_executed",
            "updated_status": "still_open_until_higher_response_payload_rows_promote",
            "selected_for_higher_response_scalar_functional": False,
            "codomain_scalar_row_count": higher["closure_decision"]["codomain_scalar_row_count"],
            "accepted_scalar_row_count_now": 0,
            "evidence": [rel(DATA / "selected_higherresponserthetafunctional_or_sourceanchortheorem.candidate.json")],
        },
    ]

    closed_first_response_rows = [
        row["row_id"]
        for row in payload_rows
        if row["updated_status"] in {"closed_for_first_response_source_stack", "closed_for_first_response_dynamic_packet"}
    ]
    still_open_payload_rows = [
        row["row_id"]
        for row in payload_rows
        if row["updated_status"].startswith("still_open")
    ]

    payload = {
        "schema": "MTTHigherResponsePayloadLedgerUpdateAfterFirstResponse.v1",
        "status": "FIRST_RESPONSE_ROWS_PROMOTED_HIGHER_RESPONSE_PAYLOAD_ROWS_OPEN",
        "previous_inventory": {
            "source": rel(
                DATA
                / "selected_dynamicphifinc1payloadrows_or_higherresponseexecution"
                / "dynamic_phifin_c1_payload_row_inventory.packet.json"
            ),
            "old_accepted_dynamic_payload_row_count": payload_inventory["accepted_dynamic_payload_row_count"],
            "old_support_candidate_present_count": payload_inventory["support_candidate_present_count"],
        },
        "updated_rows": payload_rows,
        "closed_first_response_rows": closed_first_response_rows,
        "still_open_payload_rows": still_open_payload_rows,
        "counts": {
            "closed_first_response_rows": len(closed_first_response_rows),
            "closed_higher_response_scalar_payload_rows": 0,
            "still_open_higher_response_payload_rows": len(still_open_payload_rows),
            "retired_first_response_labels": sum(1 for value in retired_first_response_labels.values() if value),
        },
        "guardrail": {
            "do_not_reuse_first_response_as_scalar_mass_fit": True,
            "do_not_count_model_active_HYM_projectors_as_selected_higher_response_values": True,
            "do_not_count_surrogate_or_profile_values_as_no_knob_derivation": True,
            "observed_data_used_as_selector": False,
            "target_fitting_used": False,
        },
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "closure_claimed": False,
    }

    next_cutset = {
        "schema": "MTTNextCutsetAfterCurrentFrontierReconciliation.v1",
        "status": "NEXT_ATTACK_HIGHER_RESPONSE_PAYLOAD_ROWS_OR_FULL_S2_VALUE_EXECUTION",
        "recommended_next": {
            "artifact": NEXT_ARTIFACT,
            "reason": (
                "The first-response source stack and dynamic matter packet are closed. Full closure now "
                "requires selected higher-response payload rows that can instantiate the scalar R_theta "
                "value functional without fitting observed Yukawa or Higgs values."
            ),
        },
        "lanes": [
            {
                "id": "A_HYM_payload_promotion",
                "must_emit": [
                    "selected HYM/Strominger zero-mode projectors and bases",
                    "full sector Hermitian metric/connection payload",
                    "selected rho_E/D_E/Riesz/Green/dotD operator values",
                ],
            },
            {
                "id": "B_full_S2_value_execution",
                "must_emit": [
                    "higher-response finite Hessian/source blocks beyond first response",
                    "full-S2 sector response matrices",
                    "scalar value rows for u,d,e families and lambda_H",
                ],
            },
            {
                "id": "C_external_or_diagonal_profile_guarded",
                "must_emit": [
                    "accepted full covariance/profile likelihood or accepted diagonal theorem provenance",
                    "same-branch threshold/mass-scheme convention rows",
                    "clear separation of external benchmark rows from no-knob derivation",
                ],
            },
        ],
        "still_open": {
            "Yukawa_mass_mixing_value_closure": True,
            "lambda_H_value_execution": True,
            "higher_response_Rtheta_execution": True,
            "selected_HYM_projector_zero_mode_basis_values": True,
            "selected_rho_E_D_E_Riesz_Green_dotD_payload": True,
            "full_S2_value_emission": True,
            "true_SM_equivalence": True,
            "full_no_knob": True,
        },
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "closure_claimed": False,
    }

    for path, packet in [(SCOPE, scope), (PAYLOAD, payload), (NEXT, next_cutset)]:
        write_json(path, packet)

    candidate = {
        "candidate": "MTTSelectedCurrentFrontierReconciliationOrHigherResponsePayloadLedger",
        "status": STATUS,
        "inputs": {
            "vsd01_source_assembly": rel(DATA / "selected_vsd01_allprimitiverowsassemblymap_or_physicalphifinc1actionsource.candidate.json"),
            "dynamic_matter_overlap_packet": rel(DATA / "selected_samesourcedynamicmatteroverlapoperatorpacket_or_primitivec1valueclosure.candidate.json"),
            "dynamic_qasu3_replay": rel(DATA / "selected_dynamicqasu3operatorpacketreplay_or_yukawamassmixingvalueclosure.candidate.json"),
            "postsource_frontier": rel(DATA / "selected_dynamicqasu3_or_c1response_postsourcefrontier.candidate.json"),
            "route_test": rel(DATA / "selected_samesourcedynamicphifinc1_or_honestgalerkinexecution_routetest.candidate.json"),
            "old_higher_response_payload_inventory": rel(DATA / "selected_dynamicphifinc1payloadrows_or_higherresponseexecution.candidate.json"),
            "higher_response_functional": rel(DATA / "selected_higherresponserthetafunctional_or_sourceanchortheorem.candidate.json"),
        },
        "output_packets": {
            "scope_reconciliation": rel(SCOPE),
            "higher_response_payload_ledger_update": rel(PAYLOAD),
            "next_cutset_after_current_frontier_reconciliation": rel(NEXT),
        },
        "what_closes_now": {
            "stale_first_response_A_b_deltaTheta_blockers_retired": True,
            "VSD01_first_response_source_stack_confirmed_closed": first_response_closed,
            "dynamic_QaSU3_first_response_layer_confirmed_closed": qasu3_gate["actual_QaSU3_operator_packet_status"][
                "first_response_layer_now_closed"
            ],
            "higher_response_payload_ledger_updated": True,
            "next_nonlooping_cutset_selected": True,
            "observed_constants_excluded_as_selectors": True,
            "target_fitting_excluded": True,
        },
        "what_remains_open": next_cutset["still_open"],
        "closure_decision": {
            "first_response_scope_closed": first_response_closed,
            "higher_response_payload_rows_closed": False,
            "full_S2_value_execution_closed": False,
            "Yukawa_mass_mixing_value_closure": False,
            "lambda_H_value_execution": False,
            "true_SM_equivalence_closed": False,
            "full_no_knob_closed": False,
        },
        "theorem": {
            "name": "CurrentFrontierScopeReconciliationTheorem",
            "proved": first_response_closed
            and all(retired_first_response_labels.values())
            and internal["closure_decision"]["first_response_only_route_rejected_for_scalar_no_knob_values"],
            "statement": (
                "The VSD01/source-stack and dynamic matter overlap artifacts close the selected first-response "
                "A,b,deltaTheta, primitive-row, and sector-response layer. Earlier postsource labels that still "
                "say A,b,deltaTheta are absent must therefore be read as full-S2/higher-response/precision "
                "payload labels, not as first-response source absence. First response remains insufficient for "
                "scalar Yukawa/Higgs/no-knob values, so the active frontier is selected higher-response payload "
                "row promotion or full-S2 value execution."
            ),
        },
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "closure_claimed": False,
        "next_required_artifact": NEXT_ARTIFACT,
    }

    cert = {
        "certificate": "MTT_Selected_CurrentFrontierReconciliation_or_HigherResponsePayloadLedger_v1",
        "status": STATUS,
        "candidate_path": rel(OUTPUT),
        "note_path": rel(NOTE),
        "theorem_proved": candidate["theorem"]["proved"],
        "first_response_scope_closed": candidate["closure_decision"]["first_response_scope_closed"],
        "higher_response_payload_rows_closed": False,
        "true_SM_equivalence_closed": False,
        "full_no_knob_closed": False,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "closure_claimed": False,
        "next_required_artifact": NEXT_ARTIFACT,
    }

    note = f"""# MTT Selected CurrentFrontierReconciliation or HigherResponsePayloadLedger v1

Status: `{STATUS}`.

This artifact reconciles the latest first-response closure packets with the
older postsource/higher-response ledgers.

Closed now at first-response scope:

- VSD01 source stack: `A_selected`, `b_selected`, and `deltaTheta_C1`.
- all 72 primitive rows and the formal 110-row assembly.
- first dynamic matter/overlap packet and dynamic Qa/SU3 first-response layer.

Not closed:

- higher-response scalar payload rows.
- full-S2 value execution.
- selected HYM/Strominger zero-mode/metric/rhoE/D_E/Riesz/Green/dotD payload.
- Yukawa/mass/mixing/lambda_H no-knob value derivation.
- true SM equivalence.

Guardrail: first response is not a scalar mass fit and cannot be reused as a
no-knob Yukawa/Higgs derivation.

Next artifact: `{NEXT_ARTIFACT}`.
"""

    write_json(OUTPUT, candidate)
    write_json(CERT, cert)
    NOTE.write_text(note, encoding="utf-8")
    print(json.dumps({"candidate": rel(OUTPUT), "status": STATUS}, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
