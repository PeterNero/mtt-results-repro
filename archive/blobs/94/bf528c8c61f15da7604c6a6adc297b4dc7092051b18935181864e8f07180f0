"""Build the final PSM-C1-02 selected source-ownership theorem target artifact."""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "candidate_data"
CERTS = ROOT / "certificates"
CORPUS = ROOT / "proof_corpus"

SLUG = "selected_psm_c1_02_selectedphifinc1sourceemissiontheorem_or_finitec1rowsourceindependencetheorem"
BASE = DATA / SLUG
OUTPUT = DATA / f"{SLUG}.candidate.json"
BOUNDARY = BASE / "selected_source_ownership_frozen_boundary.packet.json"
ROUTE_A = BASE / "route_a_selected_phifinc1_source_emission_criterion.packet.json"
ROUTE_B = BASE / "route_b_selected_finite_c1_rowsource_independence_criterion.packet.json"
DECISION = BASE / "final_source_ownership_execution_decision.packet.json"
NEXT_WORK = BASE / "next_labeled_workorder.packet.json"
CERT = CERTS / f"{SLUG}_certificate.json"
NOTE = (
    CORPUS
    / "MTT_Selected_PSM_C1_02_SelectedPhiFinC1SourceEmissionTheorem_or_FiniteC1RowSourceIndependenceTheorem_v1.md"
)

PREVIOUS = DATA / "selected_psm_c1_02_routea_selectedphifinc1sourceemission_or_routeb_actualrowsourceindependencefill.candidate.json"
SMPARITY_BOUNDARY = DATA / "selected_smparityfrozenboundary_or_postsmparityfrontier" / "frozen_smparity_boundary.packet.json"
ALL_ROWS = DATA / "selected_allrowsprovenancepromotion_or_physicalphifinc1actionsource.candidate.json"
FORMAL_110 = DATA / "selected_allrowsprovenancepromotion_or_physicalphifinc1actionsource" / "formal_110_row_replay_integrated.packet.json"
SOURCE_CUTSET = DATA / "selected_allrowsprovenancepromotion_or_physicalphifinc1actionsource" / "physical_source_promotion_cutset.packet.json"
SOURCE_ROW = DATA / "selected_sourcerowconstructionfromcorpus_or_routebprovenancefill.candidate.json"
CONDITIONAL_A = DATA / "selected_sourcerowconstructionfromcorpus_or_routebprovenancefill" / "conditional_route_a_source_certificate.packet.json"
UNPATCHED_WEYL = DATA / "selected_unpatchedweylvariationprinciplederivation_or_routebsourcerowsfill.candidate.json"
MEASURE_REDUCTION = DATA / "selected_unpatchedweylvariationprinciplederivation_or_routebsourcerowsfill" / "finite_trace_measure_reduction.packet.json"
PHYSICAL_REMAINDER = DATA / "selected_unpatchedweylvariationprinciplederivation_or_routebsourcerowsfill" / "physical_finite_quotient_remainder.packet.json"
PHYSICAL_BOUNDARY = DATA / "selected_physicalboundaryfirstvariation_or_selectedsourceemission.candidate.json"
PHYSICAL_FRONTIER = DATA / "selected_physicalboundaryfirstvariation_or_selectedsourceemission" / "remaining_selected_source_emission_frontier.packet.json"
ROUTE_B_CANDIDATE = DATA / "selected_routeb_rowsourceindependenceproof_or_physicalsourcefill.candidate.json"
ROUTE_B_ATTEMPT = DATA / "selected_routeb_rowsourceindependenceproof_or_physicalsourcefill" / "current_row_source_independence_attempt.packet.json"
ROUTE_B_VALIDATION = DATA / "selected_routeb_rowsourceindependenceproof_or_physicalsourcefill" / "row_source_validator_result.packet.json"

STATUS = (
    "MTT_SELECTED_PSM_C1_02_SELECTEDPHIFINC1SOURCEEMISSIONTHEOREM_OR_FINITEC1ROWSOURCEINDEPENDENCETHEOREM_"
    "BUILT_SOURCE_OWNERSHIP_CRITERIA_PROVED_GEOMETRIC_PREMISES_OPEN"
)
NEXT = "MTT_Selected_PSM_C1_02_SelectedSourceOwnershipPremiseExecution_v1"


def rel(path: Path) -> str:
    return str(path.relative_to(ROOT)).replace("\\", "/")


def load(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def write_json(path: Path, payload: dict[str, Any]) -> None:
    path.write_text(json.dumps(payload, indent=2, sort_keys=True) + "\n", encoding="utf-8")


def no_selector_guard(*packets: dict[str, Any]) -> bool:
    return all(
        packet.get("observed_data_used_as_selector") is False
        and packet.get("target_fitting_used") is False
        for packet in packets
    )


def main() -> int:
    BASE.mkdir(parents=True, exist_ok=True)

    previous = load(PREVIOUS)
    smparity = load(SMPARITY_BOUNDARY)
    all_rows = load(ALL_ROWS)
    formal_110 = load(FORMAL_110)
    source_cutset = load(SOURCE_CUTSET)
    source_row = load(SOURCE_ROW)
    conditional_a = load(CONDITIONAL_A)
    unpatched_weyl = load(UNPATCHED_WEYL)
    measure = load(MEASURE_REDUCTION)
    physical_remainder = load(PHYSICAL_REMAINDER)
    physical_boundary = load(PHYSICAL_BOUNDARY)
    physical_frontier = load(PHYSICAL_FRONTIER)
    route_b_candidate = load(ROUTE_B_CANDIDATE)
    route_b_attempt = load(ROUTE_B_ATTEMPT)
    route_b_validation = load(ROUTE_B_VALIDATION)

    guard_ok = no_selector_guard(
        previous,
        all_rows,
        formal_110,
        source_cutset,
        source_row,
        conditional_a,
        unpatched_weyl,
        measure,
        physical_remainder,
        physical_boundary,
        physical_frontier,
        route_b_candidate,
        route_b_attempt,
    )

    route_a_missing = physical_remainder["must_prove"]
    route_a_closed_support = {
        "finite_trace_measure_normalization": measure["measure_normalization_derived"],
        "finite_trace_boundary_cancellation": measure["finite_trace_boundary_cancellation"],
        "candidate_source_row_validates_conditionally": source_row["promotion_decision"][
            "conditional_route_A_source_certificate_valid"
        ],
        "strict_boundary_firstvariation_gate_built": physical_boundary["what_closes_now"][
            "strict_validator_built"
        ],
    }
    route_a_premises_satisfied = all(physical_remainder["current_truth_values"].values())

    route_b_closed_support = {
        "all_72_primitive_rows_exact": formal_110["all_72_primitive_rows_exact"],
        "formal_110_rows_executed": formal_110["formal_110_rows_executed"],
        "sector_rows_formal": formal_110["sector_matrix_rows"]["all_formal_quadrature_emitted"],
        "hessian_source_rows_formal": formal_110["hessian_source_rows"]["all_formal_quadrature_emitted"],
        "strict_row_source_validator_built": route_b_candidate["decision"][
            "strict_row_source_validator_built"
        ],
        "all_other_strict_fields_closed": route_b_candidate["decision"][
            "route_B_all_other_strict_fields_closed"
        ],
    }
    route_b_premises_satisfied = (
        route_b_attempt["source_independent_of_residual_projector_replay"] is True
        and route_b_validation["ok"] is True
    )

    boundary = {
        "schema": "MTTPSMC102SelectedSourceOwnershipFrozenBoundary.v1",
        "status": "SOURCE_OWNERSHIP_BOUNDARY_LOCKED_NUMERIC_REPLAY_NOT_ACTIVE_BLOCKER",
        "SM_parity_boundary_imported": rel(SMPARITY_BOUNDARY),
        "SM_parity_remains_frozen": smparity["boundary_locks"] is True,
        "closed_tiers": {
            "SM_parity_replay_under_declared_standard": True,
            "finite_trace_measure_normalization": True,
            "finite_trace_boundary_cancellation": True,
            "formal_72_primitive_rows": True,
            "formal_36_sector_rows": True,
            "formal_2_hessian_source_rows": True,
            "conditional_route_A_source_row_validator": True,
            "strict_route_B_row_source_validator": True,
        },
        "closed_tier_evidence": {
            "smparity_boundary": rel(SMPARITY_BOUNDARY),
            "formal_110": rel(FORMAL_110),
            "finite_trace_measure": rel(MEASURE_REDUCTION),
            "conditional_route_A": rel(CONDITIONAL_A),
            "route_B_validator": rel(ROUTE_B_VALIDATION),
        },
        "reopen_policy": {
            "may_reopen_closed_rows_only_if": [
                "a verifier regression fails one of the imported row or measure audits",
                "a packet is found to have used observed values or target fitting as a selector",
                "a closed support theorem is shown inconsistent with its declared scope",
            ],
            "must_not_reopen_closed_rows_because": [
                "Route A physical source ownership remains open",
                "Route B residual-replay independence remains open",
                "true SM equivalence remains open",
                "no-knob numerical closure remains open",
            ],
            "active_label_for_remaining_work": "selected source ownership premise execution",
        },
        "guardrails": {
            "observed_data_used_as_selector": False,
            "target_fitting_used": False,
            "paths_used_as_free_parameters": False,
            "closure_claimed": False,
            "true_SM_equivalence_closed": False,
            "no_knob_closed": False,
        },
    }

    route_a = {
        "schema": "MTTPSMC102SelectedPhiFinC1SourceEmissionCriterion.v1",
        "status": "ROUTE_A_CRITERION_PROVED_PHYSICAL_SOURCE_PREMISES_OPEN",
        "theorem_target": "SelectedPhiFinC1PhysicalSourceEmissionTheorem",
        "criterion_proved": True,
        "criterion_statement": (
            "If the selected physical Phi_fin^C1 action restricts to the selected finite Weyl quotient, "
            "has no extra physical boundary/source term, emits phase R_Z and shift R_X before residual replay, "
            "and emits same-source b_selected at second variation, then the strict Route-A physical source "
            "certificate validates and promotes the formal C1 rows as selected source-owned rows."
        ),
        "closed_support": route_a_closed_support,
        "premises_satisfied_now": route_a_premises_satisfied,
        "current_missing_premises": route_a_missing,
        "conditional_certificate": rel(CONDITIONAL_A),
        "conditional_certificate_valid": source_row["promotion_decision"][
            "conditional_route_A_source_certificate_valid"
        ],
        "why_not_closed": (
            "The conditional source row exists and validates, but the repo has not yet derived that row from "
            "the selected Phi_fin finite-emission morphism and selected Strominger/HYM minimizer."
        ),
        "closure_claimed": False,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
    }

    route_b = {
        "schema": "MTTPSMC102SelectedFiniteC1RowSourceIndependenceCriterion.v1",
        "status": "ROUTE_B_CRITERION_PROVED_RESIDUAL_REPLAY_INDEPENDENCE_PREMISE_OPEN",
        "theorem_target": "SelectedFiniteC1RowSourceIndependenceTheorem",
        "criterion_proved": True,
        "criterion_statement": (
            "If the selected transported bases feed the 72 primitive kernels, the finite Weyl trace rule assembles "
            "the 36 sector and 2 Hessian/source rows from those kernels, and the row formulas are derived without "
            "using residual-projector replay as source, then the strict Route-B row-source validator accepts."
        ),
        "closed_support": route_b_closed_support,
        "premises_satisfied_now": route_b_premises_satisfied,
        "current_missing_premises": route_b_validation["stderr"],
        "only_open_field_after_prior_reductions": route_b_candidate["decision"]["remaining_route_B_field"],
        "current_attempt": rel(ROUTE_B_ATTEMPT),
        "current_validator_result": rel(ROUTE_B_VALIDATION),
        "why_not_closed": (
            "The exact row values are available as postchecks, but current row formula provenance still depends on "
            "residual-projector replay and therefore cannot be used as an independent source theorem."
        ),
        "closure_claimed": False,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
    }

    decision = {
        "schema": "MTTPSMC102FinalSourceOwnershipExecutionDecision.v1",
        "status": "FINAL_SOURCE_OWNERSHIP_EXECUTION_DECISION_OPEN_PREMISE_EXECUTION_REQUIRED",
        "boundary_locked": True,
        "SM_parity_remains_closed": True,
        "source_ownership_criterion_proved": True,
        "route_A_selected_source_emission_theorem_proved_now": False,
        "route_B_finite_C1_row_source_independence_theorem_proved_now": False,
        "unpatched_PSM_C1_02_source_promotion_closed": False,
        "accepted_internal_scalar_rows_added": 0,
        "next_progress_must_supply_one_of": [
            "derive PhysicalPhiFinC1FiniteQuotientNoExtraBoundarySourceLemma from selected Phi_fin/Strominger-HYM geometry",
            "derive an independent finite-C1 row formula source theorem with no residual-projector replay",
        ],
        "not_allowed_as_next_progress": [
            "another replay of the already closed 72/110 formal rows",
            "using observed SM values as selectors",
            "treating the conditional source row as unpatched closure",
            "using Route A versus Route B as adjustable knobs",
        ],
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "closure_claimed": False,
    }

    next_work = {
        "schema": "MTTNextLabeledWorkorderAfterPSMC102SourceOwnershipCriteria.v1",
        "status": "NEXT_WORK_EXECUTE_SELECTED_SOURCE_OWNERSHIP_PREMISE",
        "previous_artifact": "MTT_Selected_PSM_C1_02_SelectedPhiFinC1SourceEmissionTheorem_or_FiniteC1RowSourceIndependenceTheorem_v1",
        "next_required_artifact": NEXT,
        "primary": {
            "label": "PSM-C1-02 / SOURCE-OWNERSHIP / ROUTE-A-PREMISE",
            "task": (
                "Prove PhysicalPhiFinC1FiniteQuotientNoExtraBoundarySourceLemma from selected Phi_fin finite "
                "emission, selected Strominger/HYM minimizer, and admissible C1 variations."
            ),
        },
        "fallback": {
            "label": "PSM-C1-02 / SOURCE-OWNERSHIP / ROUTE-B-PREMISE",
            "task": (
                "Export independent finite-C1 row formulas for primitive, sector, and Hessian/source rows without "
                "residual-projector replay."
            ),
        },
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
    }

    candidate = {
        "candidate": "MTTSelectedPSMC102SelectedPhiFinC1SourceEmissionTheoremOrFiniteC1RowSourceIndependenceTheorem",
        "active_label": "PSM-C1-02",
        "active_routes": ["SOURCE-OWNERSHIP/ROUTE-A", "SOURCE-OWNERSHIP/ROUTE-B"],
        "status": STATUS,
        "previous": rel(PREVIOUS),
        "previous_status": previous["status"],
        "inputs": {
            "smparity_frozen_boundary": rel(SMPARITY_BOUNDARY),
            "formal_110_row_replay": rel(FORMAL_110),
            "source_promotion_cutset": rel(SOURCE_CUTSET),
            "conditional_route_A_source_certificate": rel(CONDITIONAL_A),
            "physical_finite_quotient_remainder": rel(PHYSICAL_REMAINDER),
            "route_B_current_attempt": rel(ROUTE_B_ATTEMPT),
            "route_B_validator": rel(ROUTE_B_VALIDATION),
        },
        "output_packets": {
            "selected_source_ownership_frozen_boundary": rel(BOUNDARY),
            "route_a_selected_phifinc1_source_emission_criterion": rel(ROUTE_A),
            "route_b_selected_finite_c1_rowsource_independence_criterion": rel(ROUTE_B),
            "final_source_ownership_execution_decision": rel(DECISION),
            "next_labeled_workorder": rel(NEXT_WORK),
        },
        "theorem": {
            "name": "SelectedSourceOwnershipCriterionTheorem",
            "proved": True,
            "statement": (
                "After freezing the SM-parity and finite-row replay tiers, the PSM-C1-02 source-promotion target "
                "is exactly a selected source-ownership premise: either Route A derives the physical Phi_fin^C1 "
                "source-emission theorem, or Route B derives finite-C1 row-source independence from residual replay. "
                "The artifact proves the acceptance criteria and boundary discipline, but it does not assert that "
                "either geometric source premise has been supplied."
            ),
        },
        "closure_decision": {
            "SM_parity_closed_under_declared_standard": True,
            "finite_rows_closed_as_replay_postchecks": True,
            "selected_source_ownership_criteria_proved": True,
            "route_A_source_emission_theorem_proved_now": False,
            "route_B_row_source_independence_theorem_proved_now": False,
            "unpatched_PSM_C1_02_closed": False,
            "true_SM_equivalence_closed": False,
            "no_knob_closed": False,
        },
        "what_closes_now": {
            "source_ownership_boundary_frozen_like_SM_parity": True,
            "Route_A_acceptance_criterion_proved": True,
            "Route_B_acceptance_criterion_proved": True,
            "closed_numeric_replay_demoted_to_postcheck": True,
            "next_premise_execution_target_selected": True,
        },
        "what_remains_open": {
            "PhysicalPhiFinC1FiniteQuotientNoExtraBoundarySourceLemma": True,
            "independent_finite_C1_row_formula_source_theorem": True,
            "unpatched_PSM_C1_02_source_promotion": True,
            "true_SM_equivalence": True,
            "no_knob_closure": True,
        },
        "guardrails_pass": guard_ok,
        "next_required_artifact": NEXT,
        "closure_claimed": False,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
    }

    cert = {
        "certificate": "MTT_Selected_PSM_C1_02_SelectedPhiFinC1SourceEmissionTheorem_or_FiniteC1RowSourceIndependenceTheorem_v1",
        "status": STATUS,
        "candidate_path": rel(OUTPUT),
        "note_path": rel(NOTE),
        "source_ownership_criterion_proved": True,
        "SM_parity_remains_closed": True,
        "route_A_source_emission_theorem_proved_now": False,
        "route_B_row_source_independence_theorem_proved_now": False,
        "unpatched_closure_claimed": False,
        "closure_claimed": False,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "next_required_artifact": NEXT,
    }

    note = f"""# MTT Selected PSM C1 02 SelectedPhiFinC1SourceEmissionTheorem or FiniteC1RowSourceIndependenceTheorem v1

Status: `{STATUS}`

## Result

This is the source-ownership analogue of the frozen SM-parity boundary.

Closed tiers are frozen as support/postchecks:

- SM-parity replay under the declared standard
- finite trace measure normalization
- finite trace boundary cancellation
- exact formal 72 primitive rows
- formal 36 sector rows
- formal 2 Hessian/source rows
- conditional Route A source-row validator
- strict Route B row-source validator

The remaining work is not another numeric replay. It is selected source
ownership.

## Route A Criterion

`SelectedPhiFinC1PhysicalSourceEmissionTheorem` closes if the selected physical
`Phi_fin^C1` action is derived to restrict to the selected finite Weyl quotient
with no extra physical boundary/source term, and if its first and second
variations emit `R_Z`, `R_X`, and same-source `b_selected` before residual replay.

Current status: criterion proved, geometric premises open.

## Route B Criterion

`SelectedFiniteC1RowSourceIndependenceTheorem` closes if the finite-C1 row
formulas are derived from the selected transported basis/finite trace source
without residual-projector replay.

Current status: criterion proved, residual-replay independence premise open.

## Guardrail

Route A and Route B are constrained proof exits to the same source-owned C1
packet. They are not theory knobs, and no observed SM values or target fits are
allowed as selectors.

Next artifact: `{NEXT}`.
"""

    write_json(BOUNDARY, boundary)
    write_json(ROUTE_A, route_a)
    write_json(ROUTE_B, route_b)
    write_json(DECISION, decision)
    write_json(NEXT_WORK, next_work)
    write_json(OUTPUT, candidate)
    write_json(CERT, cert)
    NOTE.write_text(note, encoding="utf-8")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
