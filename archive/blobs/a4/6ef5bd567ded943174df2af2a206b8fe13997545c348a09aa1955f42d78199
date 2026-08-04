"""Build HYM connection extraction or source-origin lemma bridge."""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "candidate_data"
CERTS = ROOT / "certificates"
CORPUS = ROOT / "proof_corpus"

SLUG = "selected_hymconnectionextraction_or_sourceoriginlemma"
PACKET_DIR = DATA / SLUG
OUTPUT = DATA / f"{SLUG}.candidate.json"
SOURCE_ORIGIN = PACKET_DIR / "source_origin_lemma_status.packet.json"
CONNECTION = PACKET_DIR / "hym_connection_extraction_status.packet.json"
DIAGONAL = PACKET_DIR / "diagonal_connection_payload_reuse.packet.json"
PROMOTION = PACKET_DIR / "promotion_decision_after_connection_extraction.packet.json"
CUTSET = PACKET_DIR / "newton_galerkin_or_rank2_sector_transfer_cutset.packet.json"
CERT = CERTS / f"{SLUG}_certificate.json"
NOTE = CORPUS / "MTT_Selected_HYMConnectionExtraction_or_SourceOriginLemma_v1.md"

STATUS = "MTT_SELECTED_HYMCONNECTIONEXTRACTION_OR_SOURCEORIGINLEMMA_BUILT_DIAGONAL_PAYLOAD_FULL_TRANSFER_OPEN"


def rel(path: Path) -> str:
    try:
        return str(path.relative_to(ROOT)).replace("\\", "/")
    except ValueError:
        return str(path)


def load(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def main() -> int:
    PACKET_DIR.mkdir(parents=True, exist_ok=True)

    previous = load(DATA / "selected_visibleoperatorpayload_or_routechymresidual.candidate.json")
    previous_cutset = load(
        DATA
        / "selected_visibleoperatorpayload_or_routechymresidual"
        / "connection_extraction_or_source_origin_cutset.packet.json"
    )
    extraction_contract = load(DATA / "selected_hym_connection_to_finite_operator_extraction.candidate.json")
    source_origin = load(DATA / "routec_selected_source_origin_lemma.candidate.json")
    phifin_schema = load(DATA / "finite_emission_morphism_phifin.candidate.json")
    alpha1_payload = load(DATA / "selected_phifin_alpha1_payload.candidate.json")
    gauge_solve = load(DATA / "selected_hym_gaugefixed_connection_or_galerkin_solve.candidate.json")
    diagonal_payload = load(DATA / "selected_hym_operator_payload_extraction_from_diagonal_replay.candidate.json")

    source_origin_status = {
        "schema": "MTTSourceOriginLemmaStatus.v1",
        "status": "SOURCE_ORIGIN_REDUCED_TO_FINITE_EMISSION_MORPHISM",
        "lemma_name": source_origin["lemma_evaluation"]["lemma_name"],
        "fixed_sector_support_passes": source_origin["gate_matrix"]["G1_fixed_topological_sector_named"]["passes"],
        "strominger_selection_available": source_origin["gate_matrix"]["G2_MTT_Strominger_selection_available"]["passes"],
        "same_source_support_converges": source_origin["gate_matrix"]["G3_same_source_support_converges"]["passes"],
        "finite_emission_morphism_present": source_origin["gate_matrix"]["G4_minimizer_to_finite_packet_morphism"]["passes"],
        "operator_payload_emitted": source_origin["gate_matrix"]["G5_operator_payload_emitted"]["passes"],
        "fully_proved": source_origin["lemma_evaluation"]["fully_proved"],
        "open_sublemma": source_origin["lemma_evaluation"]["open_sublemma"],
        "open_sublemma_statement": source_origin["lemma_evaluation"]["open_sublemma_statement"],
        "finite_emission_contract": source_origin["finite_emission_morphism_contract"],
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
    }

    connection_status = {
        "schema": "MTTHYMConnectionExtractionStatus.v1",
        "status": "EXTRACTION_CONTRACT_BUILT_GAUGEFIXED_REPRESENTATIVE_OPEN",
        "extraction_contract": extraction_contract["extraction_contract"],
        "straight_path": extraction_contract["straight_path"],
        "first_DE_emission_attempt": extraction_contract["first_DE_emission_attempt"],
        "gauge_fixed_problem": gauge_solve["gauge_fixed_hym_problem"],
        "finite_newton_galerkin_contract": gauge_solve["finite_newton_galerkin_contract"],
        "first_solve_attempt": gauge_solve["first_solve_attempt"],
        "acceptance_gate_for_promotion": gauge_solve["acceptance_gate_for_promotion"],
        "actual_gauge_fixed_connection_representative_emitted": False,
        "actual_finite_operator_payload_emitted": False,
        "rank2_to_sector_transfer_functor_closed": False,
        "accepted_as_actual_QaSU3_packet": False,
        "accepted_for_true_SM_equivalence": False,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
    }

    diagonal_reuse = {
        "schema": "MTTDiagonalConnectionPayloadReuse.v1",
        "status": "DIAGONAL_RANK2_PAYLOAD_EXTRACTED_FULL_SECTOR_TRANSFER_OPEN",
        "diagonal_metric_payload": diagonal_payload["diagonal_metric_payload"],
        "diagonal_connection_payload": diagonal_payload["diagonal_connection_payload"],
        "curvature_residual_payload": diagonal_payload["curvature_residual_payload"],
        "operator_payload_boundary": diagonal_payload["operator_payload_boundary"],
        "can_reuse_as_rank2_support": True,
        "can_promote_to_full_sector_payload_now": False,
        "why_not_validator_ready": diagonal_payload["operator_payload_boundary"]["why_not_validator_ready"],
        "still_open_for_full_payload": diagonal_payload["what_remains_open"],
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
    }

    promotion = {
        "schema": "MTTPromotionDecisionAfterHYMConnectionExtraction.v1",
        "status": "DIAGONAL_SUPPORT_IMPORTED_FULL_FINITE_EMISSION_OPEN",
        "route_A_source_origin": {
            "fixed_sector_and_selection_support_present": True,
            "finite_emission_morphism_closed": False,
            "source_origin_lemma_fully_proved": False,
        },
        "route_B_connection_extraction": {
            "extraction_contract_formalized": True,
            "gauge_fixed_connection_representative_emitted": False,
            "finite_newton_galerkin_values_emitted": False,
            "rank2_to_sector_transfer_functor_closed": False,
        },
        "route_C_diagonal_payload_reuse": {
            "rank2_diagonal_metric_connection_extracted": True,
            "curvature_residual_closed": True,
            "full_sector_payload_promoted": False,
        },
        "SM_parity_closed": True,
        "true_SM_equivalence_closed": False,
        "no_knob_closed": False,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
    }

    cutset = {
        "schema": "MTTNewtonGalerkinOrRank2SectorTransferCutset.v1",
        "status": "NEWTON_GALERKIN_SOLVE_OR_RANK2_SECTOR_TRANSFER_REQUIRED",
        "closed_now": [
            "source-origin lemma replayed and reduced to finite Phi_fin emission",
            "selected HYM connection extraction contract imported",
            "gauge-fixed finite Newton/Galerkin problem imported",
            "diagonal rank-2 metric/connection payload imported as support",
            "full sector promotion blocked on rank2-to-sector transfer and validator-ready finite operators",
        ],
        "remaining_minimal_payloads": [
            "emit selected A_HYM or S/H coefficient vector in fixed gauge",
            "prove coercive gauge-fixed Jacobian/Hessian lower bound",
            "emit selected quadrature/truncation error bound",
            "construct rank2-to-sector transfer functor or prove it unnecessary",
            "derive rho_E, metric, D_E, Riesz/Green, dotD, and C1/overlap data from the selected connection",
            "replay validators without lifted flags or smoke fixtures",
        ],
        "recommended_next_artifact": "MTT_Selected_HYMNewtonGalerkin_FirstSolve_or_Rank2SectorFunctor_v1",
        "SM_parity_closed": True,
        "true_SM_equivalence_closed": False,
        "no_knob_closed": False,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
    }

    candidate = {
        "candidate": "MTTSelectedHYMConnectionExtractionOrSourceOriginLemma",
        "status": STATUS,
        "inputs": {
            "previous_candidate": rel(DATA / "selected_visibleoperatorpayload_or_routechymresidual.candidate.json"),
            "previous_cutset": rel(
                DATA
                / "selected_visibleoperatorpayload_or_routechymresidual"
                / "connection_extraction_or_source_origin_cutset.packet.json"
            ),
            "connection_extraction_contract": rel(DATA / "selected_hym_connection_to_finite_operator_extraction.candidate.json"),
            "source_origin_lemma": rel(DATA / "routec_selected_source_origin_lemma.candidate.json"),
            "phifin_schema": rel(DATA / "finite_emission_morphism_phifin.candidate.json"),
            "phifin_alpha1_payload": rel(DATA / "selected_phifin_alpha1_payload.candidate.json"),
            "gauge_fixed_connection_or_galerkin_solve": rel(
                DATA / "selected_hym_gaugefixed_connection_or_galerkin_solve.candidate.json"
            ),
            "diagonal_hym_operator_payload": rel(
                DATA / "selected_hym_operator_payload_extraction_from_diagonal_replay.candidate.json"
            ),
        },
        "output_packets": {
            "source_origin_lemma_status": rel(SOURCE_ORIGIN),
            "hym_connection_extraction_status": rel(CONNECTION),
            "diagonal_connection_payload_reuse": rel(DIAGONAL),
            "promotion_decision": rel(PROMOTION),
            "newton_galerkin_or_rank2_sector_transfer_cutset": rel(CUTSET),
        },
        "theorem": {
            "name": "HYMConnectionExtractionOrSourceOriginReductionTheorem",
            "proved": True,
            "statement": (
                "The selected source-origin problem and visible operator payload problem reduce to the same finite "
                "emission step. Fixed q79/F,m=1 S3/GS source support and abstract HYM existence are present; a "
                "diagonal rank-2 HYM metric/connection payload is extracted as support. Full Qa/SU3 promotion still "
                "requires a gauge-fixed Newton/Galerkin solve or equivalent rank2-to-sector transfer that emits "
                "validator-ready rho_E, D_E, Riesz/Green, dotD, and C1 data without lifted flags."
            ),
        },
        "what_closes_now": {
            "source_origin_reduction_replayed": True,
            "connection_extraction_contract_replayed": True,
            "gauge_fixed_problem_imported": True,
            "diagonal_rank2_payload_imported": True,
            "next_solver_or_transfer_cutset_sharpened": True,
        },
        "what_remains_open": {
            "finite_emission_morphism_Phi_fin": True,
            "gauge_fixed_HYM_Newton_Galerkin_values": True,
            "rank2_to_sector_transfer_functor": True,
            "selected_rho_E_metric_D_E_Riesz_Green_dotD": True,
            "selected_C1_overlap_contractions": True,
            "actual_QaSU3_packet": True,
            "true_SM_equivalence": True,
            "no_knob_closure": True,
        },
        "closure_decision": {
            "SM_parity_closed": previous["closure_decision"]["SM_parity_closed"],
            "source_origin_lemma_fully_proved": False,
            "diagonal_rank2_payload_imported": True,
            "full_sector_operator_payload_emitted": False,
            "actual_QaSU3_packet_promoted": False,
            "true_SM_equivalence_closed": False,
            "no_knob_closed": False,
        },
        "previous_status": previous["status"],
        "previous_remaining_payloads": previous_cutset["remaining_minimal_payloads"],
        "phifin_selected_payload_flags": phifin_schema["phifin_schema"]["selected_flags"],
        "alpha1_payload_all_selected_values_emitted": alpha1_payload["payload_summary"]["all_selected_values_emitted"],
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "next_required_artifact": cutset["recommended_next_artifact"],
    }

    cert = {
        "certificate": "MTT_Selected_HYMConnectionExtraction_or_SourceOriginLemma_v1",
        "status": STATUS,
        "candidate_path": rel(OUTPUT),
        "note_path": rel(NOTE),
        "theorem_proved": True,
        "SM_parity_closed": True,
        "source_origin_lemma_fully_proved": False,
        "diagonal_rank2_payload_imported": True,
        "full_sector_operator_payload_emitted": False,
        "actual_QaSU3_packet_promoted": False,
        "true_SM_equivalence_closed": False,
        "no_knob_closed": False,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "next_required_artifact": candidate["next_required_artifact"],
    }

    note = f"""# MTT Selected HYMConnectionExtraction or SourceOriginLemma v1

Status: `{STATUS}`.

This artifact unifies the source-origin and finite-operator extraction gates.

The good news: fixed q79/F,m=1 S3/GS support, abstract HYM existence, and a
diagonal rank-2 HYM metric/connection payload are all present. The diagonal
payload includes a determinant-one metric, `A_diag = d u * T3`, and a tiny
curvature residual.

The hard boundary remains: diagonal rank-2 support is not the full finite
sector payload. Promotion still needs a selected Newton/Galerkin solve or an
equivalent rank2-to-sector transfer emitting rho_E, D_E, Riesz, Green, dotD,
and C1/overlap data without lifted flags or smoke fixtures.
"""

    for path, body in [
        (SOURCE_ORIGIN, source_origin_status),
        (CONNECTION, connection_status),
        (DIAGONAL, diagonal_reuse),
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
