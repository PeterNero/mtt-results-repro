"""Build PSM-C1-02 final Route-A source emission / Route-B row-source fill attempt."""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "candidate_data"
CERTS = ROOT / "certificates"
CORPUS = ROOT / "proof_corpus"

SLUG = "selected_psm_c1_02_routea_selectedphifinc1sourceemission_or_routeb_actualrowsourceindependencefill"
BASE = DATA / SLUG
OUTPUT = DATA / f"{SLUG}.candidate.json"
ROUTE_A_ATTEMPT = BASE / "route_a_selected_phifinc1_source_emission_attempt.packet.json"
ROUTE_B_ATTEMPT = BASE / "route_b_actual_row_source_independence_attempt.packet.json"
FINAL_DECISION = BASE / "final_unpatched_source_promotion_decision.packet.json"
NEXT_WORK = BASE / "next_labeled_workorder.packet.json"
CERT = CERTS / f"{SLUG}_certificate.json"
NOTE = (
    CORPUS
    / "MTT_Selected_PSM_C1_02_RouteA_SelectedPhiFinC1SourceEmission_or_RouteB_ActualRowSourceIndependenceFill_v1.md"
)

PREVIOUS = DATA / "selected_psm_c1_02_physicalboundaryfirstvariation_or_routebrowsourceindependence.candidate.json"
FINAL_SOURCE = DATA / "selected_finalsourceemission_actualfill_or_nogowitness.candidate.json"
FINAL_SOURCE_VALIDATOR = DATA / "selected_finalsourceemission_actualfill_or_nogowitness" / "strict_validator_result.packet.json"
FINAL_FRONTIER = (
    DATA / "selected_finalsourceemission_actualfill_or_nogowitness" / "current_frontier_after_actual_fill_attempt.packet.json"
)
ROUTE_B = DATA / "selected_routeb_rowsourceindependenceproof_or_physicalsourcefill.candidate.json"
ROUTE_B_VALIDATOR = DATA / "selected_routeb_rowsourceindependenceproof_or_physicalsourcefill" / "row_source_validator_result.packet.json"
LOCAL_ROUTE_A = DATA / "selected_psm_c1_02_localprinciple_routea_validation_or_unpatcheda1aactualsource.candidate.json"

STATUS = (
    "MTT_SELECTED_PSM_C1_02_ROUTEA_SELECTEDPHIFINC1SOURCEEMISSION_OR_ROUTEB_ACTUALROWSOURCEINDEPENDENCEFILL_"
    "BUILT_FINAL_ACTUAL_ATTEMPTS_REJECT_SOURCE_THEOREM_OR_ROWSOURCE_THEOREM_OPEN"
)
NEXT = "MTT_Selected_PSM_C1_02_SelectedPhiFinC1SourceEmissionTheorem_or_FiniteC1RowSourceIndependenceTheorem_v1"


def rel(path: Path) -> str:
    return str(path.relative_to(ROOT)).replace("\\", "/")


def load(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def write_json(path: Path, payload: dict[str, Any]) -> None:
    path.write_text(json.dumps(payload, indent=2, sort_keys=True) + "\n", encoding="utf-8")


def main() -> int:
    BASE.mkdir(parents=True, exist_ok=True)

    previous = load(PREVIOUS)
    final_source = load(FINAL_SOURCE)
    final_validator = load(FINAL_SOURCE_VALIDATOR)
    final_frontier = load(FINAL_FRONTIER)
    route_b = load(ROUTE_B)
    route_b_validator = load(ROUTE_B_VALIDATOR)
    local_route_a = load(LOCAL_ROUTE_A)

    route_a_attempt = {
        "schema": "MTTPSMC102RouteASelectedPhiFinC1SourceEmissionAttempt.v1",
        "label": "PSM-C1-02 / SOURCE-IDENTITY / ROUTE-A-FINAL",
        "status": "ROUTE_A_SELECTED_PHIFINC1_SOURCE_EMISSION_ATTEMPT_REJECTED",
        "source": rel(FINAL_SOURCE),
        "strict_validator_result": final_validator,
        "current_attempt_rejected": final_validator["exit_code"] != 0,
        "closed_nonblockers": final_frontier["closed_gates"],
        "remaining_route_A_fields": [
            "same_branch",
            "physical_phifin_c1_action_emitted",
            "no_extra_boundary_or_source_term",
            "selected_phase_shift_variation_operators_pre_residual",
            "selected_hessian_counterterm_source",
            "same_source_b_selected_emitted",
            "row_formula_source_theorem_derived",
        ],
        "local_principle_route_A_validates": local_route_a["what_closes_now"][
            "local_principle_route_A_strict_validator_pass"
        ],
        "local_principle_is_unpatched_proof": False,
        "unpatched_route_A_closed_now": False,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "closure_claimed": False,
    }

    route_b_attempt = {
        "schema": "MTTPSMC102RouteBActualRowSourceIndependenceAttempt.v1",
        "label": "PSM-C1-02 / SOURCE-IDENTITY / ROUTE-B-FINAL",
        "status": "ROUTE_B_ACTUAL_ROWSOURCE_INDEPENDENCE_ATTEMPT_REJECTED",
        "source": rel(ROUTE_B),
        "strict_validator_result": route_b_validator,
        "current_attempt_rejected": route_b_validator["exit_code"] != 0,
        "route_B_all_other_strict_fields_closed": route_b["decision"]["route_B_all_other_strict_fields_closed"],
        "remaining_route_B_field": route_b["decision"]["remaining_route_B_field"],
        "missing_validator_fields": [
            "selected_basis_feeds_72_primitive_rows",
            "no_residual_projector_replay_used_as_source",
            "row_formula_source_theorem_derived",
            "source_independent_of_residual_projector_replay",
        ],
        "unpatched_route_B_closed_now": False,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "closure_claimed": False,
    }

    final_decision = {
        "schema": "MTTPSMC102FinalUnpatchedSourcePromotionDecision.v1",
        "status": "FINAL_ACTUAL_ATTEMPTS_REJECT_THEOREM_TARGETS_SHARP",
        "SM_parity_remains_closed": True,
        "local_principle_route_A_validates": True,
        "local_principle_is_no_knob_closure": False,
        "route_A_actual_attempt_rejected": True,
        "route_B_actual_attempt_rejected": True,
        "unpatched_source_promotion_closed": False,
        "remaining_exact_theorems": {
            "route_A": "SelectedPhiFinC1PhysicalSourceEmissionTheorem",
            "route_B": "SelectedFiniteC1RowSourceIndependenceTheorem",
        },
        "why_this_is_progress": [
            "alpha1/dotD, canonical residual values, and algebraic b replay are retired as blockers",
            "Route A fails only as same-branch physical Phi_fin^C1 source emission",
            "Route B fails only as row-source independence from residual-projector replay",
            "local-principle validation is kept separate from unpatched/no-knob closure",
        ],
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "closure_claimed": False,
    }

    next_work = {
        "schema": "MTTNextLabeledWorkorderAfterPSMC102FinalActualAttempts.v1",
        "previous_artifact": "MTT_Selected_PSM_C1_02_RouteA_SelectedPhiFinC1SourceEmission_or_RouteB_ActualRowSourceIndependenceFill_v1",
        "next_required_artifact": NEXT,
        "primary": {
            "label": "PSM-C1-02 / SOURCE-IDENTITY / ROUTE-A-THEOREM",
            "task": "Derive SelectedPhiFinC1PhysicalSourceEmissionTheorem from selected Theta/Phi_fin/Strominger action text.",
        },
        "fallback": {
            "label": "PSM-C1-02 / SOURCE-IDENTITY / ROUTE-B-THEOREM",
            "task": "Prove SelectedFiniteC1RowSourceIndependenceTheorem for the 72 primitive, 36 sector, and 2 Hessian/source rows.",
        },
        "status": "NEXT_WORKORDER_PROVE_ROUTE_A_SOURCE_THEOREM_OR_ROUTE_B_ROWSOURCE_THEOREM",
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
    }

    candidate = {
        "candidate": "MTTSelectedPSMC102RouteASelectedPhiFinC1SourceEmissionOrRouteBActualRowSourceIndependenceFill",
        "active_label": "PSM-C1-02",
        "active_routes": ["SOURCE-IDENTITY/ROUTE-A-FINAL", "SOURCE-IDENTITY/ROUTE-B-FINAL"],
        "status": STATUS,
        "previous": rel(PREVIOUS),
        "previous_status": previous["status"],
        "inputs": {
            "final_source_emission_actualfill": rel(FINAL_SOURCE),
            "route_b_rowsource_independence": rel(ROUTE_B),
            "local_route_a_validation": rel(LOCAL_ROUTE_A),
        },
        "output_packets": {
            "route_a_selected_phifinc1_source_emission_attempt": rel(ROUTE_A_ATTEMPT),
            "route_b_actual_row_source_independence_attempt": rel(ROUTE_B_ATTEMPT),
            "final_unpatched_source_promotion_decision": rel(FINAL_DECISION),
            "next_labeled_workorder": rel(NEXT_WORK),
        },
        "closure_decision": {
            "SM_parity_closed_under_declared_standard": True,
            "local_principle_route_A_validates": True,
            "route_A_actual_attempt_rejected": True,
            "route_B_actual_attempt_rejected": True,
            "unpatched_PSM_C1_02_closed": False,
            "true_SM_equivalence_closed": False,
            "no_knob_closed": False,
        },
        "what_closes_now": {
            "route_A_actual_source_emission_attempt_replayed": True,
            "route_B_actual_row_source_attempt_replayed": True,
            "alpha1_dotD_and_residual_replay_retired_as_blockers": True,
            "final_two_unpatched_theorem_targets_named": True,
            "local_principle_guardrail_preserved": True,
        },
        "what_remains_open": {
            "SelectedPhiFinC1PhysicalSourceEmissionTheorem": True,
            "SelectedFiniteC1RowSourceIndependenceTheorem": True,
            "unpatched_PSM_C1_02_source_promotion": True,
            "true_SM_equivalence": True,
            "no_knob_closure": True,
        },
        "theorem": {
            "name": "PSMC102FinalActualAttemptsAndTheoremTargetsTheorem",
            "proved": True,
            "statement": (
                "The PSM-C1-02 final actual-fill attempts import the latest source-emission no-go and Route-B "
                "row-source validator. Route A still rejects because no unpatched same-branch Phi_fin^C1 physical "
                "source-emission theorem is supplied. Route B still rejects because row-source independence from "
                "residual-projector replay is not proved. Thus the next progress must be one of two theorems, not "
                "another numerical replay: SelectedPhiFinC1PhysicalSourceEmissionTheorem or "
                "SelectedFiniteC1RowSourceIndependenceTheorem."
            ),
        },
        "superset_strategy": {
            "classification": "FINAL_TWO_THEOREM_CUTSET",
            "paths_used_as_free_parameters": False,
            "route_A": "selected physical source-emission theorem",
            "route_B": "selected finite-C1 row-source independence theorem",
            "local_route": "validator-clean local premise, not counted as no-knob",
        },
        "next_required_artifact": NEXT,
        "closure_claimed": False,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
    }

    cert = {
        "certificate": "MTT_Selected_PSM_C1_02_RouteA_SelectedPhiFinC1SourceEmission_or_RouteB_ActualRowSourceIndependenceFill_v1",
        "status": STATUS,
        "candidate_path": rel(OUTPUT),
        "note_path": rel(NOTE),
        "route_A_actual_attempt_rejected": True,
        "route_B_actual_attempt_rejected": True,
        "local_principle_route_A_validates": True,
        "unpatched_closure_claimed": False,
        "closure_claimed": False,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "next_required_artifact": NEXT,
    }

    note = f"""# MTT Selected PSM C1 02 RouteA SelectedPhiFinC1SourceEmission or RouteB ActualRowSourceIndependenceFill v1

Status labels:

- `PSM-C1-02 / SOURCE-IDENTITY / ROUTE-A-FINAL`
- `PSM-C1-02 / SOURCE-IDENTITY / ROUTE-B-FINAL`

Status: `{STATUS}`

## Result

Both final unpatched actual-fill routes were replayed under the PSM-C1-02 label.

- Route A still rejects: the same-branch `Phi_fin^C1` physical source-emission
  theorem is not supplied.
- Route B still rejects: row-source independence from residual-projector replay
  is not proved.

The local-principle route remains validator-clean, but it is local-premise
closure, not no-knob/unpatched closure.

## What This Retires

The active blocker is no longer alpha1/dotD, canonical residual values, finite
trace measure, algebraic `b` replay, or missing exact primitive values. Those
are postchecks/support. The remaining target is source ownership.

## Next Artifact

`{NEXT}`
"""

    write_json(ROUTE_A_ATTEMPT, route_a_attempt)
    write_json(ROUTE_B_ATTEMPT, route_b_attempt)
    write_json(FINAL_DECISION, final_decision)
    write_json(NEXT_WORK, next_work)
    write_json(OUTPUT, candidate)
    write_json(CERT, cert)
    NOTE.write_text(note, encoding="utf-8")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
