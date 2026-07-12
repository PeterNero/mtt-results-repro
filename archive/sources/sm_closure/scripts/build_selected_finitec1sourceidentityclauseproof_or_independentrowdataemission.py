"""Build finite C1 source-identity clause proof or independent row data emission.

This targets the most movable clause from the source-identity theorem gate:
finite Weyl trace assembly of sector and Hessian rows.  It proves the formal
measure/assembly part and keeps physical source promotion open.
"""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "candidate_data"
CERTS = ROOT / "certificates"
CORPUS = ROOT / "proof_corpus"

SLUG = "selected_finitec1sourceidentityclauseproof_or_independentrowdataemission"
PACKET_DIR = DATA / SLUG
OUTPUT = DATA / f"{SLUG}.candidate.json"
CLAUSE_PROOF = PACKET_DIR / "finite_weyl_trace_assembly_clause_proof.packet.json"
UPDATED_GATE = PACKET_DIR / "updated_source_identity_clause_gate.packet.json"
ROW_DATA_ATTEMPT = PACKET_DIR / "independent_row_data_emission_attempt.packet.json"
DECISION = PACKET_DIR / "clause_proof_or_row_data_decision.packet.json"
CERT = CERTS / f"{SLUG}_certificate.json"
NOTE = CORPUS / "MTT_Selected_FiniteC1SourceIdentityClauseProof_or_IndependentRowDataEmission_v1.md"

PREVIOUS = DATA / "selected_finitec1sourceidentitytheorem_or_newindependentrows.candidate.json"
THEOREM_GATE = (
    DATA
    / "selected_finitec1sourceidentitytheorem_or_newindependentrows"
    / "selected_finite_c1_source_identity_theorem_gate.packet.json"
)
NEW_ROWS_SCHEMA = (
    DATA
    / "selected_finitec1sourceidentitytheorem_or_newindependentrows"
    / "new_independent_rows_schema.packet.json"
)
TRACE_DERIVATION = (
    DATA
    / "selected_finiteweyl_traceuniqueness_or_physicalboundarysource_derivation"
    / "finite_weyl_trace_uniqueness_derivation.packet.json"
)
FORMAL_110 = (
    DATA
    / "selected_allrowsprovenancepromotion_or_physicalphifinc1actionsource"
    / "formal_110_row_replay_integrated.packet.json"
)
ALL_72 = (
    DATA
    / "selected_firstrowprovenancepromotion_or_allrowsweylexecution"
    / "all_72_exact_weyl_row_execution.packet.json"
)
BASIS = (
    DATA
    / "selected_routeb_selectedbasisindependencefill_or_rowsourcegap"
    / "route_b_selected_basis_independence_fill.packet.json"
)

STATUS = "MTT_SELECTED_FINITEC1SOURCEIDENTITY_CLAUSEPROOF_BUILT_TRACEASSEMBLY_CLOSED_SOURCE_OPEN"
NEXT = "MTT_Selected_PhysicalSourcePromotionClauseProof_or_NewIndependentRowPacketFill_v1"


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

    previous = load(PREVIOUS)
    gate = load(THEOREM_GATE)
    rows_schema = load(NEW_ROWS_SCHEMA)
    trace = load(TRACE_DERIVATION)
    formal = load(FORMAL_110)
    all_72 = load(ALL_72)
    basis = load(BASIS)

    trace_assembly_closed = (
        trace["derived_now"]["finite_measure_equals_normalized_trace"] is True
        and trace["derived_now"]["trace_frobenius_pairing_for_finite_quotient"] is True
        and formal["formal_110_rows_executed"] is True
        and formal["row_counts"]["primitive_rows"] == 72
        and formal["row_counts"]["sector_matrix_rows"] == 36
        and formal["row_counts"]["hessian_source_rows"] == 2
        and formal["sector_matrix_rows"]["all_formal_quadrature_emitted"] is True
        and formal["hessian_source_rows"]["all_formal_quadrature_emitted"] is True
    )
    physical_source_promoted = (
        formal["sector_matrix_rows"]["physical_source_promoted"] is True
        and formal["hessian_source_rows"]["physical_source_promoted"] is True
    )

    clause_proof = {
        "schema": "MTTFiniteWeylTraceAssemblyClauseProof.v1",
        "status": "TRACE_MEASURE_AND_FORMAL_ASSEMBLY_PROVED_PHYSICAL_SOURCE_OPEN",
        "clause": "finite_weyl_trace_rule_assembles_sector_and_hessian_rows",
        "proved_subclaim": {
            "finite_measure_equals_normalized_trace": trace["derived_now"]["finite_measure_equals_normalized_trace"],
            "trace_frobenius_pairing_for_finite_quotient": trace["derived_now"][
                "trace_frobenius_pairing_for_finite_quotient"
            ],
            "formal_110_rows_executed": formal["formal_110_rows_executed"],
            "sector_rows_assembled_formally": formal["sector_matrix_rows"]["all_formal_quadrature_emitted"],
            "hessian_source_rows_assembled_formally": formal["hessian_source_rows"][
                "all_formal_quadrature_emitted"
            ],
            "formal_110_max_abs_error": formal["formal_110_max_abs_error"],
            "trace_assembly_closed": trace_assembly_closed,
        },
        "not_proved_subclaim": {
            "sector_rows_physical_source_promoted": formal["sector_matrix_rows"]["physical_source_promoted"],
            "hessian_source_rows_physical_source_promoted": formal["hessian_source_rows"][
                "physical_source_promoted"
            ],
            "full_source_identity_clause_proved": physical_source_promoted,
        },
        "proof_sources": {
            "finite_weyl_trace_uniqueness": rel(TRACE_DERIVATION),
            "formal_110_row_replay": rel(FORMAL_110),
            "all_72_exact_rows_postcheck": rel(ALL_72),
        },
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
    }

    updated_gate = json.loads(json.dumps(gate))
    updated_gate["schema"] = "MTTSelectedFiniteC1SourceIdentityTheoremGateAfterTraceAssemblyClause.v1"
    updated_gate["status"] = "THEOREM_GATE_TRACE_ASSEMBLY_SUBCLAUSE_CLOSED_SOURCE_PROMOTION_OPEN"
    updated_gate["clause_status"]["finite_weyl_trace_rule_assembles_sector_and_hessian_rows"] = {
        "status": "SUBCLAUSE_CLOSED_PHYSICAL_SOURCE_PROMOTION_OPEN",
        "proved": False,
        "route": "B",
        "closed_part": "finite normalized trace/Frobenius measure and formal 36 sector + 2 Hessian/source row assembly",
        "closed_subclaim_source": rel(CLAUSE_PROOF),
        "reason_open": "physical/source promotion of sector and Hessian rows is still false",
        "remaining_open": [
            "sector_rows_physical_source_promoted",
            "hessian_source_rows_physical_source_promoted",
            "same-source b_selected emission",
        ],
    }
    updated_gate["proved_now"] = False
    updated_gate["observed_data_used_as_selector"] = False
    updated_gate["target_fitting_used"] = False

    row_data_attempt = {
        "schema": "MTTIndependentRowDataEmissionAttemptFromCurrentSupport.v1",
        "status": "CURRENT_SUPPORT_FILLS_POSTCHECK_VALUES_NOT_NEW_INDEPENDENT_SOURCE_DATA",
        "required_schema": rel(NEW_ROWS_SCHEMA),
        "basis_source_certificate_available": basis["route_B_independent_execution"][
            "selected_basis_independence_certificate"
        ]["all_sector_sources_verified_by_transport_conjugation"],
        "primitive_rows_available": all_72["row_count"],
        "primitive_values_exact": all_72["exactness_clause_closed_for_all_rows"],
        "primitive_rows_source_independent": all_72[
            "provenance_independent_of_residual_projector_replay_for_all_rows"
        ],
        "sector_rows_available_formally": formal["row_counts"]["sector_matrix_rows"],
        "hessian_rows_available_formally": formal["row_counts"]["hessian_source_rows"],
        "new_independent_row_packet_emitted": False,
        "why_not_emitted": (
            "Current rows are exact and useful as postchecks, but their value source is still the finite Weyl "
            "residual-polynomial/replay lineage rather than a new selected physical or Galerkin source identity."
        ),
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
    }

    decision = {
        "schema": "MTTFiniteC1ClauseProofOrRowDataDecision.v1",
        "status": "TRACE_ASSEMBLY_SUBCLAUSE_CLOSED_FULL_THEOREM_OPEN",
        "source_identity_theorem_proved": False,
        "new_independent_rows_emitted": False,
        "clause_progress": {
            "finite_weyl_trace_measure_and_formal_assembly": "CLOSED",
            "physical_source_promotion_for_assembled_rows": "OPEN",
            "no_residual_projector_replay_as_source": "OPEN",
            "physical_action_restriction_and_boundary": "OPEN",
        },
        "next_required_artifact": NEXT,
        "superset_strategy": {
            "straight_path_progress": "Route B formal measure/assembly subclaim closed from finite Weyl trace uniqueness",
            "combined_path_still_needed": "Route A physical source promotion or new independent selected row source data",
            "locked_target": "selected finite C1 source identity, not measured SM data",
        },
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
    }

    for path, payload in [
        (CLAUSE_PROOF, clause_proof),
        (UPDATED_GATE, updated_gate),
        (ROW_DATA_ATTEMPT, row_data_attempt),
        (DECISION, decision),
    ]:
        write_json(path, payload)

    candidate = {
        "candidate": "MTTSelectedFiniteC1SourceIdentityClauseProofOrIndependentRowDataEmission",
        "status": STATUS,
        "inputs": {
            "previous": rel(PREVIOUS),
            "theorem_gate": rel(THEOREM_GATE),
            "trace_derivation": rel(TRACE_DERIVATION),
            "formal_110_rows": rel(FORMAL_110),
            "all_72_rows": rel(ALL_72),
        },
        "output_packets": {
            "finite_weyl_trace_assembly_clause_proof": rel(CLAUSE_PROOF),
            "updated_source_identity_clause_gate": rel(UPDATED_GATE),
            "independent_row_data_emission_attempt": rel(ROW_DATA_ATTEMPT),
            "decision": rel(DECISION),
        },
        "theorem": {
            "name": "FiniteWeylTraceAssemblySubclauseTheorem",
            "proved": True,
            "statement": (
                "The finite Weyl trace uniqueness theorem and the formal 110-row replay prove the normalized "
                "trace/Frobenius measure and formal assembly of 36 sector rows and 2 Hessian/source rows. "
                "This does not promote the rows as physical/source data."
            ),
        },
        "what_closes_now": {
            "finite_trace_measure_assembly_subclause": True,
            "formal_sector_and_hessian_row_assembly": True,
            "current_support_checked_against_new_row_schema": True,
            "full_clause_boundary_refined": True,
        },
        "what_remains_open": {
            "physical_source_promotion_for_sector_and_hessian_rows": True,
            "no_residual_projector_replay_as_source": True,
            "physical_action_restriction_and_boundary": True,
            "new_independent_selected_row_data": True,
            "unpatched_dynamic_C1_closure": True,
        },
        "closure_claimed": False,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "next_required_artifact": NEXT,
    }

    cert = {
        "certificate": "MTT_Selected_FiniteC1SourceIdentityClauseProof_or_IndependentRowDataEmission_v1",
        "status": STATUS,
        "candidate_path": rel(OUTPUT),
        "note_path": rel(NOTE),
        "trace_assembly_subclause_closed": True,
        "full_source_identity_theorem_proved": False,
        "new_independent_rows_emitted": False,
        "closure_claimed": False,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
    }

    NOTE.write_text(
        "# MTT Selected FiniteC1SourceIdentityClauseProof or IndependentRowDataEmission v1\n\n"
        f"Status: `{STATUS}`.\n\n"
        "This artifact proves the movable subclaim inside the finite-C1 source identity gate: "
        "the selected qutrit Weyl trace uniquely fixes the normalized trace/Frobenius measure, "
        "and that measure formally assembles the `36` sector rows plus `2` Hessian/source rows "
        "inside the existing `110`-row packet.\n\n"
        "It does not promote those rows as physical/source data. The remaining live proof is "
        "physical source promotion or genuinely new independent selected row data with an "
        "independence certificate excluding residual-projector replay.\n\n"
        f"Next artifact: `{NEXT}`.\n",
        encoding="utf-8",
    )
    write_json(OUTPUT, candidate)
    write_json(CERT, cert)

    print(json.dumps({"candidate": rel(OUTPUT), "status": STATUS}, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
