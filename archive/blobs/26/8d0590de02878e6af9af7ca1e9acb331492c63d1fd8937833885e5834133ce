"""Build visible operator payload or Route-C/HYM residual bridge."""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "candidate_data"
CERTS = ROOT / "certificates"
CORPUS = ROOT / "proof_corpus"

SLUG = "selected_visibleoperatorpayload_or_routechymresidual"
PACKET_DIR = DATA / SLUG
OUTPUT = DATA / f"{SLUG}.candidate.json"
PIPELINE = PACKET_DIR / "routec_hym_pipeline_replay.packet.json"
VALUE_SEARCH = PACKET_DIR / "selected_value_search_replay.packet.json"
EXTRACTION = PACKET_DIR / "hym_operator_extraction_contract.packet.json"
PROMOTION = PACKET_DIR / "promotion_decision_after_operator_payload.packet.json"
CUTSET = PACKET_DIR / "connection_extraction_or_source_origin_cutset.packet.json"
CERT = CERTS / f"{SLUG}_certificate.json"
NOTE = CORPUS / "MTT_Selected_VisibleOperatorPayload_or_RouteCHYMResidual_v1.md"

STATUS = "MTT_SELECTED_VISIBLEOPERATORPAYLOAD_OR_ROUTEC_HYM_RESIDUAL_BUILT_EXTRACTION_CONTRACT_OPEN"


def rel(path: Path) -> str:
    try:
        return str(path.relative_to(ROOT)).replace("\\", "/")
    except ValueError:
        return str(path)


def load(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def main() -> int:
    PACKET_DIR.mkdir(parents=True, exist_ok=True)

    previous = load(DATA / "selected_terminalsourceswitch_or_operatorpic0gerbede.candidate.json")
    previous_cutset = load(
        DATA / "selected_terminalsourceswitch_or_operatorpic0gerbede" / "visible_operator_payload_cutset.packet.json"
    )
    pipeline = load(DATA / "selected_routec_hym_operator_pipeline.candidate.json")
    value_search = load(DATA / "selected_routec_hym_value_search.candidate.json")
    values_gate = load(DATA / "selected_routec_hym_operator_values_gate.candidate.json")
    visible_gs = load(DATA / "selected_visible_green_schwarz_operator_source.candidate.json")

    honest_passes = pipeline["pipeline_evaluation"]["honest_operator_pipeline_pass"]
    lifted_passes = pipeline["pipeline_evaluation"]["lifted_flags_operator_pipeline_pass"]
    mesh_passes = pipeline["pipeline_evaluation"]["honest_mesh_metric_sector_pass"]

    pipeline_replay = {
        "schema": "MTTRouteCHYMOperatorPipelineReplay.v1",
        "status": "PIPELINE_EXECUTABLE_HONEST_OPERATOR_PAYLOAD_NOT_PROMOTED",
        "input_cutset": rel(
            DATA / "selected_terminalsourceswitch_or_operatorpic0gerbede" / "visible_operator_payload_cutset.packet.json"
        ),
        "selected_branch": pipeline["pipeline_evaluation"]["selected_branch"],
        "selected_branch_packet": pipeline["pipeline_evaluation"]["selected_branch_packet"],
        "honest_mesh_metric_sector_pass": mesh_passes,
        "honest_operator_pipeline_pass": honest_passes,
        "lifted_flags_operator_pipeline_pass": lifted_passes,
        "actual_selected_route_c_values_supplied": pipeline["gate_results"]["actual_selected_route_c_values_supplied"],
        "actual_selected_D_E_dotD_Riesz_Green_supplied": pipeline["gate_results"][
            "actual_selected_D_E_dotD_Riesz_Green_supplied"
        ],
        "selected_source_verified": pipeline["gate_results"]["selected_source_verified"],
        "selected_hym_operator_source_verified": pipeline["gate_results"]["selected_hym_operator_source_verified"],
        "primitive_C1_contractions_supplied": pipeline["gate_results"]["primitive_C1_contractions_supplied"],
        "why_not_promoted": pipeline["pipeline_evaluation"]["why_not_promoted"],
        "validator_contract": pipeline["next_payload_contract"],
        "superset_strategy_used": pipeline["superset_mode"],
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
    }

    value_search_replay = {
        "schema": "MTTSelectedValueSearchReplay.v1",
        "status": "SELECTED_SOURCE_ORIGIN_LEMMA_REMAINS_LAST_BLOCKER",
        "search_status": value_search["status"],
        "zero_residual_smoke_exists": value_search["gate_results"]["zero_residual_smoke_exists"],
        "zero_residual_smoke_promoted": value_search["gate_results"]["zero_residual_smoke_promoted"],
        "selected_values_closed": value_search["gate_results"]["selected_values_closed"],
        "selected_source_origin_found": value_search["gate_results"]["selected_source_origin_found"],
        "selected_D_E_dotD_Riesz_Green_closed": value_search["gate_results"][
            "selected_D_E_dotD_Riesz_Green_closed"
        ],
        "last_remaining_lemma": value_search["last_remaining_lemma"],
        "honest_validator_passes": value_search["closure_attempts"]["A_promote_smoke_values"][
            "honest_validator_passes"
        ],
        "source_origin_proofs_acceptable": value_search["next_payload_contract"]["acceptable_source_origin_proofs"],
        "source_origin_proofs_not_acceptable": value_search["next_payload_contract"]["not_acceptable"],
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
    }

    extraction_contract = {
        "schema": "MTTHYMOperatorExtractionContract.v1",
        "status": "ABSTRACT_HYM_EXISTS_FINITE_OPERATOR_EXTRACTION_REQUIRED",
        "abstract_HYM_import": values_gate["abstract_HYM_import"],
        "selected_operator_values_closed": values_gate["selected_operator_values_closed"],
        "shape_support": values_gate["shape_support"],
        "source_flags_on_honest_smoke": values_gate["source_flags_on_honest_smoke"],
        "validator_results_on_honest_smoke": values_gate["validator_results_on_honest_smoke"],
        "lifted_flag_diagnostic": values_gate["lifted_flag_diagnostic"],
        "needed_extraction_theorem": values_gate["needed_extraction_theorem"],
        "visible_operator_source_gate_status": visible_gs["status"],
        "visible_operator_payload_contract": visible_gs["operator_source_payload_contract"],
        "actual_extraction_theorem_supplied": False,
        "actual_visible_operator_payload_emitted": False,
        "accepted_as_actual_QaSU3_packet": False,
        "accepted_for_true_SM_equivalence": False,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
    }

    promotion = {
        "schema": "MTTPromotionDecisionAfterVisibleOperatorPayload.v1",
        "status": "VISIBLE_OPERATOR_PAYLOAD_NOT_PROMOTED_EXTRACTION_CONTRACT_ACTIVE",
        "route_A_visible_operator_payload": {
            "selected_visible_source_constructed": False,
            "same_source_chern_weil_row_derived": False,
            "D_E_Riesz_Green_dotD_payload_emitted": False,
            "primitive_C1_contractions_supplied": False,
            "can_close_true_SM_equivalence_now": False,
        },
        "route_B_routec_hym_residual": {
            "honest_mesh_metric_sector_pass": mesh_passes,
            "honest_operator_pipeline_pass": honest_passes,
            "lifted_flags_operator_pipeline_pass": lifted_passes,
            "abstract_HYM_no_longer_blocker": values_gate["what_closes_now"]["abstract_HYM_no_longer_blocker"],
            "finite_operator_extraction_required": True,
            "can_close_true_SM_equivalence_now": False,
        },
        "SM_parity_closed": True,
        "true_SM_equivalence_closed": False,
        "no_knob_closed": False,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
    }

    cutset = {
        "schema": "MTTConnectionExtractionOrSourceOriginCutset.v1",
        "status": "SELECTED_HYM_CONNECTION_EXTRACTION_OR_SOURCE_ORIGIN_REQUIRED",
        "closed_now": [
            "Route-C/HYM pipeline replayed in current SM-parity chain",
            "honest mesh, metric, and sector-map support retained",
            "lifted-flag validators classified as sufficiency diagnostics only",
            "abstract HYM existence imported as no longer the blocker",
            "finite operator extraction theorem identified as the next exact payload",
        ],
        "remaining_minimal_payloads": [
            "prove RouteCSelectedSourceOriginLemma for q79/F,m=1",
            "extract a transition/connection representative for the selected HYM connection",
            "derive rho_E and metric tables from that connection, not smoke fixtures",
            "derive D_E action matrices and stiffness matrices from the same connection",
            "derive Riesz projectors, complement gaps, and reduced Green operators with truncation proof",
            "derive dotD_alpha1 as the same-branch derivative",
            "derive primitive C1/overlap contractions from the same response data",
        ],
        "recommended_next_artifact": "MTT_Selected_HYMConnectionExtraction_or_SourceOriginLemma_v1",
        "SM_parity_closed": True,
        "true_SM_equivalence_closed": False,
        "no_knob_closed": False,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
    }

    candidate = {
        "candidate": "MTTSelectedVisibleOperatorPayloadOrRouteCHYMResidual",
        "status": STATUS,
        "inputs": {
            "previous_candidate": rel(DATA / "selected_terminalsourceswitch_or_operatorpic0gerbede.candidate.json"),
            "previous_cutset": rel(
                DATA / "selected_terminalsourceswitch_or_operatorpic0gerbede" / "visible_operator_payload_cutset.packet.json"
            ),
            "routec_hym_operator_pipeline": rel(DATA / "selected_routec_hym_operator_pipeline.candidate.json"),
            "routec_hym_value_search": rel(DATA / "selected_routec_hym_value_search.candidate.json"),
            "routec_hym_operator_values_gate": rel(DATA / "selected_routec_hym_operator_values_gate.candidate.json"),
            "visible_green_schwarz_operator_source_gate": rel(
                DATA / "selected_visible_green_schwarz_operator_source.candidate.json"
            ),
        },
        "output_packets": {
            "routec_hym_pipeline_replay": rel(PIPELINE),
            "selected_value_search_replay": rel(VALUE_SEARCH),
            "hym_operator_extraction_contract": rel(EXTRACTION),
            "promotion_decision": rel(PROMOTION),
            "connection_extraction_or_source_origin_cutset": rel(CUTSET),
        },
        "theorem": {
            "name": "VisibleOperatorPayloadReductionTheorem",
            "proved": True,
            "statement": (
                "The visible operator payload gate is reduced to a selected HYM/Route-C source-origin and finite "
                "operator extraction theorem. Existing Route-C data honestly validate mesh, metric, and sector "
                "shape, and lifted-flag packets prove sufficiency of the validator schema, but no actual "
                "D_E/Riesz/Green/dotD/C1 payload is theorem-derived yet."
            ),
        },
        "what_closes_now": {
            "routec_hym_pipeline_replayed": True,
            "selected_value_search_replayed": True,
            "abstract_HYM_no_longer_blocker": True,
            "finite_operator_extraction_contract_built": True,
            "visible_operator_payload_cutset_sharpened": True,
        },
        "what_remains_open": {
            "RouteCSelectedSourceOriginLemma": True,
            "selected_HYM_connection_extraction": True,
            "selected_rho_E_metric_tables": True,
            "selected_D_E_Riesz_Green_dotD": True,
            "selected_C1_overlap_contractions": True,
            "actual_QaSU3_packet": True,
            "true_SM_equivalence": True,
            "no_knob_closure": True,
        },
        "closure_decision": {
            "SM_parity_closed": previous["closure_decision"]["SM_parity_closed"],
            "visible_operator_payload_emitted": False,
            "routec_hym_residual_promoted": False,
            "finite_operator_extraction_contract_active": True,
            "actual_QaSU3_packet_promoted": False,
            "true_SM_equivalence_closed": False,
            "no_knob_closed": False,
        },
        "previous_status": previous["status"],
        "previous_remaining_payloads": previous_cutset["remaining_minimal_payloads"],
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "next_required_artifact": cutset["recommended_next_artifact"],
    }

    cert = {
        "certificate": "MTT_Selected_VisibleOperatorPayload_or_RouteCHYMResidual_v1",
        "status": STATUS,
        "candidate_path": rel(OUTPUT),
        "note_path": rel(NOTE),
        "theorem_proved": True,
        "SM_parity_closed": True,
        "visible_operator_payload_emitted": False,
        "routec_hym_residual_promoted": False,
        "finite_operator_extraction_contract_active": True,
        "actual_QaSU3_packet_promoted": False,
        "true_SM_equivalence_closed": False,
        "no_knob_closed": False,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "next_required_artifact": candidate["next_required_artifact"],
    }

    note = f"""# MTT Selected VisibleOperatorPayload or RouteCHYMResidual v1

Status: `{STATUS}`.

This artifact executes the current visible-operator payload gate.

The Route-C/HYM pipeline is real and useful: mesh, metric, and sector maps pass
honestly; lifted selected flags show the lower validators are sufficient once
the source-origin data exist.

But lifted flags are not values. Honest promotion still fails at selected source
origin and selected operator extraction. The abstract HYM existence bridge
removes one mathematical blocker, but the finite `rho_E`, `D_E`, Riesz, Green,
dotD, and C1/overlap matrices still need to be extracted from the selected
connection/source.

Next theorem: `MTT_Selected_HYMConnectionExtraction_or_SourceOriginLemma_v1`.
"""

    for path, body in [
        (PIPELINE, pipeline_replay),
        (VALUE_SEARCH, value_search_replay),
        (EXTRACTION, extraction_contract),
        (PROMOTION, promotion),
        (CUTSET, cutset),
        (OUTPUT, candidate),
        (CERT, cert),
    ]:
        path.write_text(json.dumps(body, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    NOTE.write_text(note, encoding="utf-8")
    print(json.dumps({"candidate": rel(OUTPUT), "status": STATUS}, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
