"""Build finite C1 source-identity theorem gate or new independent rows schema."""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "candidate_data"
CERTS = ROOT / "certificates"
CORPUS = ROOT / "proof_corpus"

SLUG = "selected_finitec1sourceidentitytheorem_or_newindependentrows"
PACKET_DIR = DATA / SLUG
OUTPUT = DATA / f"{SLUG}.candidate.json"
THEOREM_GATE = PACKET_DIR / "selected_finite_c1_source_identity_theorem_gate.packet.json"
ANCESTOR_RECONCILIATION = PACKET_DIR / "ancestor_lemma_reconciliation.packet.json"
NEW_ROWS_SCHEMA = PACKET_DIR / "new_independent_rows_schema.packet.json"
DECISION = PACKET_DIR / "source_identity_or_new_rows_decision.packet.json"
CERT = CERTS / f"{SLUG}_certificate.json"
NOTE = CORPUS / "MTT_Selected_FiniteC1SourceIdentityTheorem_or_NewIndependentRows_v1.md"

PREVIOUS = DATA / "selected_unpatchedweylprincipleproof_or_independentkernelrowsfirstrun.candidate.json"
CUTSET = (
    DATA
    / "selected_unpatchedweylprincipleproof_or_independentkernelrowsfirstrun"
    / "shared_source_theorem_cutset.packet.json"
)
MINIMAL_LEMMA = (
    DATA
    / "selected_sourcetheorem_push_attempt_or_minimalnewlemma"
    / "minimal_selected_finitec1_source_promotion_lemma.packet.json"
)
COUNTERMODEL = DATA / "selected_minimalfinitec1sourcepromotionlemma_proof_or_countermodel.candidate.json"
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
ROUTE_A = (
    DATA
    / "selected_unpatchedweylprincipleproof_or_independentkernelrowsfirstrun"
    / "route_a_unpatched_weyl_principle_reaudit.packet.json"
)
ROUTE_B = (
    DATA
    / "selected_unpatchedweylprincipleproof_or_independentkernelrowsfirstrun"
    / "route_b_independent_kernel_rows_first_run.packet.json"
)
BASIS = (
    DATA
    / "selected_routeb_selectedbasisindependencefill_or_rowsourcegap"
    / "route_b_selected_basis_independence_fill.packet.json"
)

STATUS = "MTT_SELECTED_FINITEC1SOURCEIDENTITYTHEOREM_OR_NEWINDEPENDENTROWS_BUILT_THEOREM_OPEN"
NEXT = "MTT_Selected_FiniteC1SourceIdentityClauseProof_or_IndependentRowDataEmission_v1"


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
    cutset = load(CUTSET)
    lemma = load(MINIMAL_LEMMA)
    countermodel = load(COUNTERMODEL)
    formal = load(FORMAL_110)
    all_72 = load(ALL_72)
    route_a = load(ROUTE_A)
    route_b = load(ROUTE_B)
    basis = load(BASIS)

    theorem_clauses = {
        "physical_action_restriction_to_selected_finite_weyl_quotient": {
            "status": "OPEN",
            "proved": False,
            "route": "A",
            "current_support": route_a["closed_support"],
            "reason_open": "closed finite Weyl support does not select the physical Phi_fin^C1 action restriction",
        },
        "no_extra_physical_boundary_or_source_term": {
            "status": "OPEN",
            "proved": False,
            "route": "A",
            "reason_open": "boundary cancellation is algebraic/formal, not yet promoted as physical dynamic-trace boundary theorem",
        },
        "same_source_R_Z_R_X_b_selected_emission": {
            "status": "OPEN",
            "proved": False,
            "route": "A/B",
            "reason_open": "R_Z/R_X and b_selected are exact values, but same-source physical/source emission remains unproved",
        },
        "selected_transported_bases_feed_all_72_primitive_row_kernels": {
            "status": "PARTIAL",
            "proved": False,
            "route": "B",
            "support": rel(BASIS),
            "closed_part": "stationary selected projectors and ordered bases are transport-conjugation verified",
            "reason_open": "dynamic row-kernel values still inherit residual-lineage provenance",
        },
        "finite_weyl_trace_rule_assembles_sector_and_hessian_rows": {
            "status": "PARTIAL",
            "proved": False,
            "route": "B",
            "support": rel(FORMAL_110),
            "closed_part": "formal 36 sector rows and 2 Hessian/source rows are integrated",
            "reason_open": "formal integration is not physical/source promotion",
        },
        "no_residual_projector_replay_as_source_provenance": {
            "status": "OPEN",
            "proved": False,
            "route": "B",
            "support": rel(ALL_72),
            "reason_open": "all 72 rows are exact, but provenance_independent_of_residual_projector_replay_for_all_rows is false",
        },
    }
    all_clauses_proved = all(item["proved"] is True for item in theorem_clauses.values())

    theorem_gate = {
        "schema": "MTTSelectedFiniteC1SourceIdentityTheoremGate.v1",
        "status": "THEOREM_GATE_BUILT_CLAUSES_OPEN",
        "theorem_name": cutset["theorem_name"],
        "statement": cutset["statement"],
        "required_clauses": cutset["required_clauses"],
        "clause_status": theorem_clauses,
        "proved_now": all_clauses_proved,
        "would_promote_if_proved": {
            "route_A_unpatched_weyl_principle": True,
            "route_B_row_source_independence": True,
            "A_selected": True,
            "b_selected": True,
            "deltaTheta_C1": True,
            "sector_response_matrices": True,
        },
        "current_route_A_accepts": route_a["route_A_accepts"],
        "current_route_B_accepts": route_b["route_B_accepts"],
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
    }

    ancestor_reconciliation = {
        "schema": "MTTFiniteC1SourceIdentityAncestorReconciliation.v1",
        "status": "SOURCE_IDENTITY_STRICTLY_STRENGTHENS_PRIOR_MINIMAL_LEMMA",
        "prior_lemma": lemma["lemma_name"],
        "prior_lemma_status": lemma["status"],
        "prior_lemma_sufficient_for_route_B": lemma["sufficient_for_strict_validator"],
        "new_theorem": cutset["theorem_name"],
        "relation": {
            "new_theorem_implies_prior_route_B_lemma": True,
            "prior_route_B_lemma_does_not_imply_route_A_physical_action_clauses": True,
            "closed_support_alone_countermodel_already_exists": True,
            "countermodel_source": rel(COUNTERMODEL),
        },
        "countermodel_summary": {
            "full_minimal_lemma_proved": countermodel["full_minimal_lemma_proved"],
            "next_required_artifact": countermodel["next_required_artifact"],
        },
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
    }

    new_rows_schema = {
        "schema": "MTTNewIndependentFiniteC1RowsEmissionSchema.v1",
        "status": "NEW_INDEPENDENT_ROWS_SCHEMA_BUILT_VALUES_NOT_EMITTED",
        "purpose": "Define what would count as genuinely new independent selected row data if the source-identity theorem is not proved.",
        "required_packet_fields": {
            "selected_source_identity": {
                "required": True,
                "description": "name of selected physical/Galerkin source producing row kernels before residual projection",
            },
            "basis_source_certificate": {
                "required": True,
                "current_support_available": basis["route_B_independent_execution"]["selected_basis_independence_certificate"][
                    "all_sector_sources_verified_by_transport_conjugation"
                ],
            },
            "primitive_rows": {
                "required_count": 72,
                "must_include": ["row_id", "sector", "response", "coordinate", "exact_value_or_interval", "source_integral_or_formula"],
                "must_not_use": "R_Z/R_X residual-projector replay as source provenance",
            },
            "sector_rows": {
                "required_count": 36,
                "must_include": ["sector", "coordinate", "assembly_formula", "source_rows"],
            },
            "hessian_source_rows": {
                "required_count": 2,
                "must_include": ["response", "hessian_entry", "b_selected_entry", "same_source_derivation"],
            },
            "exactness_or_error_certificate": {
                "required": True,
                "must_bound": "all entries tightly enough to decide rank, A^T A, A^T b, and deltaTheta_C1",
            },
            "independence_certificate": {
                "required": True,
                "must_exclude": [
                    "residual-projector replay as row source",
                    "locked target values as source",
                    "observed SM masses/mixings/thresholds as selectors",
                    "benchmark matrices as selected operator data",
                ],
            },
        },
        "current_values_reusable_as_postchecks": {
            "formal_110_rows_executed": formal["formal_110_rows_executed"],
            "formal_110_max_abs_error": formal["formal_110_max_abs_error"],
            "all_72_values_exact": all_72["exactness_clause_closed_for_all_rows"],
            "all_72_source_independence": all_72["provenance_independent_of_residual_projector_replay_for_all_rows"],
        },
        "emitted_now": False,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
    }

    decision = {
        "schema": "MTTFiniteC1SourceIdentityOrNewRowsDecision.v1",
        "status": "THEOREM_NOT_PROVED_NEW_ROWS_NOT_EMITTED_NEXT_CLAUSE_PROOF",
        "source_identity_theorem_proved": False,
        "new_independent_rows_emitted": False,
        "unpatched_dynamic_C1_closed": False,
        "true_SM_equivalence_without_local_premise": False,
        "no_knob_closed": False,
        "next_required_artifact": NEXT,
        "best_next_work": {
            "primary": "prove one clause of SelectedFiniteC1SourceIdentityTheorem, starting with physical action restriction or no-residual-replay provenance",
            "fallback": "emit a new independent row packet satisfying the schema in this artifact",
        },
        "superset_strategy": {
            "paths_combined": ["Route A physical action", "Route B finite row-kernel execution"],
            "locked_target": "selected finite C1 source identity",
            "not_used": "measured SM data or benchmark target fitting",
        },
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
    }

    for path, payload in [
        (THEOREM_GATE, theorem_gate),
        (ANCESTOR_RECONCILIATION, ancestor_reconciliation),
        (NEW_ROWS_SCHEMA, new_rows_schema),
        (DECISION, decision),
    ]:
        write_json(path, payload)

    candidate = {
        "candidate": "MTTSelectedFiniteC1SourceIdentityTheoremOrNewIndependentRows",
        "status": STATUS,
        "inputs": {
            "previous_cutset": rel(CUTSET),
            "prior_minimal_lemma": rel(MINIMAL_LEMMA),
            "prior_countermodel": rel(COUNTERMODEL),
            "formal_110_rows": rel(FORMAL_110),
            "all_72_rows": rel(ALL_72),
        },
        "output_packets": {
            "theorem_gate": rel(THEOREM_GATE),
            "ancestor_lemma_reconciliation": rel(ANCESTOR_RECONCILIATION),
            "new_independent_rows_schema": rel(NEW_ROWS_SCHEMA),
            "decision": rel(DECISION),
        },
        "theorem": {
            "name": "FiniteC1SourceIdentityGateAndRowsAlternativeTheorem",
            "proved": True,
            "statement": (
                "The selected finite C1 source identity is the strict common theorem behind Route A and Route B. "
                "It strengthens the earlier Route-B source-promotion lemma by adding the physical action and boundary clauses. "
                "Current support does not prove it; a valid alternative must emit genuinely new independent selected row data."
            ),
        },
        "what_closes_now": {
            "source_identity_clause_gate_built": True,
            "prior_minimal_lemma_reconciled": True,
            "new_independent_rows_schema_built": True,
            "next_clause_proof_target_selected": True,
        },
        "what_remains_open": {
            "SelectedFiniteC1SourceIdentityTheorem": True,
            "new_independent_selected_row_data": True,
            "unpatched_dynamic_C1_closure": True,
            "true_SM_equivalence_without_local_premise": True,
            "no_knob_flavor_constants": True,
        },
        "closure_claimed": False,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "next_required_artifact": NEXT,
    }

    cert = {
        "certificate": "MTT_Selected_FiniteC1SourceIdentityTheorem_or_NewIndependentRows_v1",
        "status": STATUS,
        "candidate_path": rel(OUTPUT),
        "note_path": rel(NOTE),
        "source_identity_theorem_proved": False,
        "new_independent_rows_emitted": False,
        "closure_claimed": False,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
    }

    NOTE.write_text(
        "# MTT Selected FiniteC1SourceIdentityTheorem or NewIndependentRows v1\n\n"
        f"Status: `{STATUS}`.\n\n"
        "This artifact turns the shared cutset into a strict theorem gate. The new "
        "`SelectedFiniteC1SourceIdentityTheorem` is stronger than the older Route-B "
        "`SelectedFiniteC1SourcePromotionLemma`: it must also prove the physical "
        "Phi_fin action restriction and no-extra-boundary/source clauses.\n\n"
        "Current support does not prove the theorem. The alternative is now also strict: "
        "emit genuinely new independent selected finite C1 row data with 72 primitive rows, "
        "36 sector rows, 2 Hessian/source rows, exactness/error certificates, and an "
        "independence certificate excluding residual-projector replay and observed-data selection.\n\n"
        f"Next artifact: `{NEXT}`.\n",
        encoding="utf-8",
    )
    write_json(OUTPUT, candidate)
    write_json(CERT, cert)

    print(json.dumps({"candidate": rel(OUTPUT), "status": STATUS}, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
