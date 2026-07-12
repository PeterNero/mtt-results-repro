"""Build the PSM-C1-02 selected source-ownership premise execution cutset."""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "candidate_data"
CERTS = ROOT / "certificates"
CORPUS = ROOT / "proof_corpus"

SLUG = "selected_psm_c1_02_selectedsourceownershippremiseexecution"
BASE = DATA / SLUG
OUTPUT = DATA / f"{SLUG}.candidate.json"
ROUTE_A = BASE / "route_a_gauge_transport_phifin_trace_execution_attempt.packet.json"
ROUTE_B = BASE / "route_b_independent_row_formula_execution_attempt.packet.json"
DECISION = BASE / "source_ownership_premise_execution_decision.packet.json"
NEXT_WORK = BASE / "next_labeled_workorder.packet.json"
CERT = CERTS / f"{SLUG}_certificate.json"
NOTE = CORPUS / "MTT_Selected_PSM_C1_02_SelectedSourceOwnershipPremiseExecution_v1.md"

PREVIOUS = DATA / "selected_psm_c1_02_selectedphifinc1sourceemissiontheorem_or_finitec1rowsourceindependencetheorem.candidate.json"
FINITE_PHIFIN = DATA / "finite_emission_morphism_phifin.candidate.json"
PHIFIN_BN = DATA / "phifin_bn_modelactive_equivalence_or_minimizer_trace.candidate.json"
HYM_PAYLOAD = DATA / "selected_selectedhymoperatorpayloadpromotion_or_rhoedefulls2execution.candidate.json"
RTHETA_HYM = DATA / "selected_rtheta_pikernel_from_selectedhymconnection_or_bnbasisemission.candidate.json"
HYM_CONNECTION = DATA / "selected_hymconnectionextraction_or_sourceoriginlemma.candidate.json"
STROMINGER_TRACE = DATA / "selected_stromingertracec1firstvariation_or_quadratureexecutionplan.candidate.json"
ROUTE_B_BASIS = DATA / "selected_routeb_selectedbasisindependencefill_or_rowsourcegap.candidate.json"
FIRST_ROW_FORMULA = DATA / "selected_differentiatedphifinc1primitiveoverlap_or_firstrowkernelformulasource.candidate.json"
FIRST_ROW_PACKET = DATA / "selected_differentiatedphifinc1primitiveoverlap_or_firstrowkernelformulasource" / "first_row_kernel_formula_source_packet.packet.json"
ROUTE_B_ROWSOURCE = DATA / "selected_routeb_rowsourceindependenceproof_or_physicalsourcefill.candidate.json"

STATUS = (
    "MTT_SELECTED_PSM_C1_02_SELECTEDSOURCEOWNERSHIPPREMISEEXECUTION_"
    "BUILT_GAUGE_TRANSPORT_TRACE_OR_INDEPENDENT_ROW_EXECUTION_OPEN"
)
NEXT = "MTT_Selected_GaugeTransported_BN_PhiFin_Trace_or_IndependentComplexRowExecution_v1"


def rel(path: Path) -> str:
    return str(path.relative_to(ROOT)).replace("\\", "/")


def load(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def write_json(path: Path, payload: dict[str, Any]) -> None:
    path.write_text(json.dumps(payload, indent=2, sort_keys=True) + "\n", encoding="utf-8")


def guard_ok(packet: dict[str, Any]) -> bool:
    return packet.get("observed_data_used_as_selector", False) is False and packet.get("target_fitting_used", False) is False


def main() -> int:
    BASE.mkdir(parents=True, exist_ok=True)

    previous = load(PREVIOUS)
    finite_phifin = load(FINITE_PHIFIN)
    phifin_bn = load(PHIFIN_BN)
    hym_payload = load(HYM_PAYLOAD)
    rtheta_hym = load(RTHETA_HYM)
    hym_connection = load(HYM_CONNECTION)
    strominger_trace = load(STROMINGER_TRACE)
    route_b_basis = load(ROUTE_B_BASIS)
    first_row_formula = load(FIRST_ROW_FORMULA)
    first_row_packet = load(FIRST_ROW_PACKET)
    route_b_rowsource = load(ROUTE_B_ROWSOURCE)

    selected_flags = finite_phifin["phifin_schema"]["selected_flags"]
    selected_payload_closed = finite_phifin["obstruction"]["selected_payload_closed"]
    gauge_repair = phifin_bn["gauge_transport_repair"]
    route_b_promotion = first_row_formula["promotion_decision"]

    route_a = {
        "schema": "MTTPSMC102RouteAGaugeTransportPhiFinTraceExecutionAttempt.v1",
        "status": "ROUTE_A_GAUGE_TRANSPORT_PHIFIN_TRACE_EXECUTION_ATTEMPT_OPEN",
        "route": "SelectedPhiFinC1PhysicalSourceEmissionTheorem",
        "support_closed": {
            "finite_phifin_codomain_schema_built": all(finite_phifin["phifin_schema"]["shape_gates"].values()),
            "diagonal_End0_operator_payload_closed": hym_payload["closure_decision"][
                "diagonal_End0_operator_payload_closed"
            ],
            "selected_HYM_connection_subgate_closed": rtheta_hym["closure_decision"][
                "selected_HYM_connection_subgate_closed"
            ],
            "selected_diagonal_rank2_payload_imported": hym_connection["closure_decision"][
                "diagonal_rank2_payload_imported"
            ],
            "untransported_BN_equivalence_rejected": phifin_bn["promotion_decision"][
                "exact_model_active_equivalence_rejected"
            ],
            "gauge_transport_repair_identified": phifin_bn["what_closes_now"][
                "gauge_transport_repair_identified"
            ],
            "strominger_first_variation_plan_built": strominger_trace["what_closes_now"][
                "I11_first_variation_certificate_schema_built"
            ],
        },
        "current_execution": {
            "Phi_fin_selected_payload_closed": selected_payload_closed,
            "Phi_fin_selected_flags": selected_flags,
            "selected_minimizer_trace_emitted": phifin_bn["promotion_decision"][
                "selected_minimizer_trace_emitted"
            ],
            "selected_source_flags_may_be_flipped_now": phifin_bn["promotion_decision"][
                "selected_source_flags_may_be_flipped_now"
            ],
            "route_A_premise_closed_now": False,
        },
        "next_required_construction": {
            "name": gauge_repair["name"],
            "transport": gauge_repair["required_transport"],
            "must_emit": gauge_repair["must_emit_next"],
        },
        "why_not_closed": (
            "The selected HYM connection is present, but current Phi_fin still has open selected flags and no "
            "gauge-transported minimizer trace. The untransported BN equality route is explicitly rejected."
        ),
        "closure_claimed": False,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
    }

    route_b = {
        "schema": "MTTPSMC102RouteBIndependentRowFormulaExecutionAttempt.v1",
        "status": "ROUTE_B_INDEPENDENT_ROW_FORMULA_EXECUTION_ATTEMPT_OPEN",
        "route": "SelectedFiniteC1RowSourceIndependenceTheorem",
        "support_closed": {
            "selected_basis_independence_clause": route_b_basis["what_closes_now"][
                "route_B_selected_basis_independent_of_residual_projector"
            ],
            "differentiated_primitive_overlap_formula_source": first_row_formula["what_closes_now"][
                "differentiated_primitive_overlap_formula_source_specified"
            ],
            "finite_trace_pairing_source": first_row_formula["what_closes_now"][
                "finite_trace_frobenius_pairing_source_attached"
            ],
            "first_row_formula_source_specified": first_row_formula["what_closes_now"][
                "first_row_kernel_formula_source_specified"
            ],
            "route_B_all_other_strict_fields_closed": route_b_rowsource["decision"][
                "route_B_all_other_strict_fields_closed"
            ],
        },
        "current_execution": {
            "computed_independent_complex_entries": route_b_promotion[
                "closed_kernel_clauses_for_first_row"
            ]["computed_independent_complex_entries"],
            "exactness_or_error_bound_certificate": route_b_promotion[
                "closed_kernel_clauses_for_first_row"
            ]["exactness_or_error_bound_certificate"],
            "provenance_independent_of_residual_projector_replay": route_b_promotion[
                "closed_kernel_clauses_for_first_row"
            ]["provenance_independent_of_residual_projector_replay"],
            "first_row_packet": rel(FIRST_ROW_PACKET),
            "first_row_formula_status": first_row_packet.get("status", "UNKNOWN"),
            "route_B_premise_closed_now": False,
        },
        "next_required_construction": {
            "name": "IndependentComplexRowExecution",
            "must_emit": [
                "computed independent complex entries for the first primitive row, then all 72 rows",
                "exactness proof or numerical error-bound certificate",
                "provenance independent of residual-projector replay",
                "lift from primitive rows to 36 sector and 2 Hessian/source rows",
            ],
        },
        "why_not_closed": (
            "Formula and trace pairing are sourced, but no independent complex entry execution, exactness certificate, "
            "or residual-replay-independent provenance is emitted."
        ),
        "closure_claimed": False,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
    }

    decision = {
        "schema": "MTTPSMC102SelectedSourceOwnershipPremiseExecutionDecision.v1",
        "status": "PREMISE_EXECUTION_REDUCED_TO_GAUGE_TRANSPORT_TRACE_OR_INDEPENDENT_COMPLEX_ROWS",
        "SM_parity_remains_closed": True,
        "previous_source_ownership_criterion_proved": previous["closure_decision"][
            "selected_source_ownership_criteria_proved"
        ],
        "Route_A_currently_closes": False,
        "Route_B_currently_closes": False,
        "unpatched_PSM_C1_02_source_promotion_closed": False,
        "strongest_new_information": [
            "Route A cannot use untransported BN/model-active equality; selected HYM du makes that false.",
            "Route A's legal repair is the gauge-transported BN Phi_fin trace U=exp(-u ad(T3)).",
            "Route B has selected basis/formula/pairing source but lacks independent complex values, exactness, and provenance.",
        ],
        "best_next_artifact": NEXT,
        "no_reopen_closed_boundary": True,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "closure_claimed": False,
    }

    next_work = {
        "schema": "MTTNextLabeledWorkorderAfterPSMC102PremiseExecution.v1",
        "status": "NEXT_WORK_BUILD_GAUGE_TRANSPORT_TRACE_OR_EXECUTE_INDEPENDENT_ROWS",
        "previous_artifact": "MTT_Selected_PSM_C1_02_SelectedSourceOwnershipPremiseExecution_v1",
        "next_required_artifact": NEXT,
        "primary": {
            "label": "PSM-C1-02 / SOURCE-OWNERSHIP / ROUTE-A-GAUGE-TRANSPORT",
            "task": (
                "Construct U=exp(-u ad(T3)), transport the BN basis/projectors into the selected HYM connection, "
                "prove D_selected(U psi)=U d psi on retained End0 lanes, and emit selected Phi_fin trace flags."
            ),
        },
        "fallback": {
            "label": "PSM-C1-02 / SOURCE-OWNERSHIP / ROUTE-B-INDEPENDENT-ROWS",
            "task": (
                "Compute independent complex primitive row contractions with exactness/error certificates and no "
                "residual-projector replay lineage."
            ),
        },
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
    }

    guardrails_pass = all(
        guard_ok(packet)
        for packet in [
            previous,
            finite_phifin,
            phifin_bn,
            hym_payload,
            rtheta_hym,
            hym_connection,
            strominger_trace,
            route_b_basis,
            first_row_formula,
            route_b_rowsource,
        ]
    )

    candidate = {
        "candidate": "MTTSelectedPSMC102SelectedSourceOwnershipPremiseExecution",
        "active_label": "PSM-C1-02",
        "status": STATUS,
        "previous": rel(PREVIOUS),
        "previous_status": previous["status"],
        "inputs": {
            "finite_emission_morphism_phifin": rel(FINITE_PHIFIN),
            "phifin_bn_modelactive_equivalence_or_minimizer_trace": rel(PHIFIN_BN),
            "selected_hym_operator_payload_promotion": rel(HYM_PAYLOAD),
            "rtheta_hym_connection_subgate": rel(RTHETA_HYM),
            "hym_connection_extraction": rel(HYM_CONNECTION),
            "strominger_trace_c1_firstvariation_plan": rel(STROMINGER_TRACE),
            "route_b_basis_independence": rel(ROUTE_B_BASIS),
            "first_row_formula_source": rel(FIRST_ROW_FORMULA),
            "route_b_row_source_independence": rel(ROUTE_B_ROWSOURCE),
        },
        "output_packets": {
            "route_a_gauge_transport_phifin_trace_execution_attempt": rel(ROUTE_A),
            "route_b_independent_row_formula_execution_attempt": rel(ROUTE_B),
            "source_ownership_premise_execution_decision": rel(DECISION),
            "next_labeled_workorder": rel(NEXT_WORK),
        },
        "theorem": {
            "name": "SelectedSourceOwnershipPremiseExecutionCutsetTheorem",
            "proved": True,
            "statement": (
                "Given the source-ownership criterion, the current HYM/Strominger and finite-row corpus does not close "
                "either exit yet. Route A is reduced to a gauge-transported BN Phi_fin trace because untransported BN "
                "equality is false for nonzero du ad(T3). Route B is reduced to independent complex row execution with "
                "exactness and residual-replay-independent provenance."
            ),
        },
        "closure_decision": {
            "SM_parity_closed_under_declared_standard": True,
            "Route_A_gauge_transport_trace_required": True,
            "Route_B_independent_complex_rows_required": True,
            "Route_A_closed_now": False,
            "Route_B_closed_now": False,
            "unpatched_PSM_C1_02_closed": False,
            "true_SM_equivalence_closed": False,
            "no_knob_closed": False,
        },
        "what_closes_now": {
            "untransported_BN_shortcut_rejected_for_source_ownership": True,
            "gauge_transport_trace_promoted_to_primary_next_target": True,
            "independent_row_formula_execution_promoted_to_fallback_next_target": True,
            "closed_SM_parity_and_formal_row_boundaries_preserved": True,
        },
        "what_remains_open": {
            "SelectedGaugeTransportedBNPhiFinTrace": True,
            "IndependentComplexRowExecution": True,
            "unpatched_PSM_C1_02_source_promotion": True,
            "true_SM_equivalence": True,
            "no_knob_closure": True,
        },
        "guardrails_pass": guardrails_pass,
        "next_required_artifact": NEXT,
        "closure_claimed": False,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
    }

    cert = {
        "certificate": "MTT_Selected_PSM_C1_02_SelectedSourceOwnershipPremiseExecution_v1",
        "status": STATUS,
        "candidate_path": rel(OUTPUT),
        "note_path": rel(NOTE),
        "Route_A_gauge_transport_trace_required": True,
        "Route_B_independent_complex_rows_required": True,
        "Route_A_closed_now": False,
        "Route_B_closed_now": False,
        "unpatched_closure_claimed": False,
        "closure_claimed": False,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "next_required_artifact": NEXT,
    }

    note = f"""# MTT Selected PSM C1 02 SelectedSourceOwnershipPremiseExecution v1

Status: `{STATUS}`

## Result

The source-ownership premise was attacked from both sides.

Route A does not close by copying the untransported `B_N`/model-active packet.
The existing no-go shows the selected HYM connection has nonzero `du ad(T3)`,
so the legal repair is a gauge-transported trace:

`U = exp(-u ad(T3))`.

Route B also does not close yet. It has selected basis independence, primitive
formula source, and finite trace pairing source, but it still lacks independent
complex row execution, exactness/error certificates, and provenance independent
of residual-projector replay.

## Best Next Target

`{NEXT}`

Primary path: construct the gauge-transported `Phi_fin` trace and emit selected
source flags. Fallback path: perform independent complex row execution by computing row contractions with
certified exactness and no residual replay lineage.

No SM-parity boundary is reopened, and no observed SM values are used as
selectors.
"""

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
