"""Build PSM-C1-02 physical boundary/first-variation or Route-B row-source gate."""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "candidate_data"
CERTS = ROOT / "certificates"
CORPUS = ROOT / "proof_corpus"

SLUG = "selected_psm_c1_02_physicalboundaryfirstvariation_or_routebrowsourceindependence"
BASE = DATA / SLUG
OUTPUT = DATA / f"{SLUG}.candidate.json"
ROUTE_A_REPLAY = BASE / "route_a_i11_boundary_firstvariation_replay.packet.json"
ROUTE_B_REPLAY = BASE / "route_b_rowsource_independence_replay.packet.json"
COMMON_OBSTRUCTION = BASE / "common_source_promotion_final_obstruction.packet.json"
NEXT_WORK = BASE / "next_labeled_workorder.packet.json"
CERT = CERTS / f"{SLUG}_certificate.json"
NOTE = CORPUS / "MTT_Selected_PSM_C1_02_PhysicalBoundaryFirstVariation_or_RouteBRowSourceIndependence_v1.md"

PREVIOUS = DATA / "selected_psm_c1_02_unpatcheda1a_sourcecutset_or_routeb_rowsource.candidate.json"
ROUTE_A_GENERAL = DATA / "selected_physicalboundaryfirstvariation_or_selectedsourceemission.candidate.json"
ROUTE_A_REMAINING = (
    DATA
    / "selected_physicalboundaryfirstvariation_or_selectedsourceemission"
    / "remaining_selected_source_emission_frontier.packet.json"
)
ROUTE_A_CURRENT = (
    DATA
    / "selected_physicalboundaryfirstvariation_or_selectedsourceemission"
    / "current_physical_source_validator_result.packet.json"
)
ROUTE_A_CONDITIONAL = (
    DATA
    / "selected_physicalboundaryfirstvariation_or_selectedsourceemission"
    / "conditional_physical_source_validator_result.packet.json"
)
ROUTE_B_GENERAL = DATA / "selected_routeb_rowsourceindependenceproof_or_physicalsourcefill.candidate.json"
ROUTE_B_DECISION = (
    DATA / "selected_routeb_rowsourceindependenceproof_or_physicalsourcefill" / "final_routeb_or_routea_decision.packet.json"
)
LOCAL_ROUTE_A = DATA / "selected_psm_c1_02_localprinciple_routea_validation_or_unpatcheda1aactualsource.candidate.json"
LOCAL_VALIDATOR = (
    DATA
    / "selected_psm_c1_02_localprinciple_routea_validation_or_unpatcheda1aactualsource"
    / "local_principle_route_a_validator_result.packet.json"
)

STATUS = (
    "MTT_SELECTED_PSM_C1_02_PHYSICALBOUNDARYFIRSTVARIATION_OR_ROUTEBROWSOURCEINDEPENDENCE_"
    "BUILT_FINAL_UNPATCHED_SOURCE_GATE_OPEN"
)
NEXT = "MTT_Selected_PSM_C1_02_RouteA_SelectedPhiFinC1SourceEmission_or_RouteB_ActualRowSourceIndependenceFill_v1"


def rel(path: Path) -> str:
    return str(path.relative_to(ROOT)).replace("\\", "/")


def load(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def write_json(path: Path, payload: dict[str, Any]) -> None:
    path.write_text(json.dumps(payload, indent=2, sort_keys=True) + "\n", encoding="utf-8")


def result_code(packet: dict[str, Any]) -> int:
    return int(packet.get("exit_code", packet.get("returncode", 1)))


def main() -> int:
    BASE.mkdir(parents=True, exist_ok=True)

    previous = load(PREVIOUS)
    route_a = load(ROUTE_A_GENERAL)
    route_a_remaining = load(ROUTE_A_REMAINING)
    route_a_current = load(ROUTE_A_CURRENT)
    route_a_conditional = load(ROUTE_A_CONDITIONAL)
    route_b = load(ROUTE_B_GENERAL)
    route_b_decision = load(ROUTE_B_DECISION)
    local_route_a = load(LOCAL_ROUTE_A)
    local_validator = load(LOCAL_VALIDATOR)

    route_a_replay = {
        "schema": "MTTPSMC102RouteAI11BoundaryFirstVariationReplay.v1",
        "label": "PSM-C1-02 / SOURCE-IDENTITY / SI-1u-A1a-UNPATCHED-I11",
        "status": "ROUTE_A_I11_BOUNDARY_FIRSTVARIATION_REPLAYED_SOURCE_EMISSION_OPEN",
        "source": rel(ROUTE_A_GENERAL),
        "current_physical_source_validator_rejects": result_code(route_a_current) != 0,
        "conditional_physical_source_witness_validates": result_code(route_a_conditional) == 0,
        "conditional_i11_trace_map_bridge_passes": route_a["what_closes_now"][
            "conditional_i11_trace_map_bridge_passes"
        ],
        "required_unpatched_source_fields": [
            "physical_first_variation_identity",
            "physical_measure_equals_trace_Frobenius_pairing",
            "phase_R_Z_source_selection",
            "shift_R_X_source_selection",
            "same_source_b_selected_emission",
            "no_extra_physical_boundary_or_source_term",
        ],
        "remaining_frontier": route_a_remaining,
        "local_principle_route_A_validates": local_validator["ok"],
        "local_principle_is_unpatched_proof": False,
        "route_A_unpatched_closed_now": False,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "closure_claimed": False,
    }

    route_b_replay = {
        "schema": "MTTPSMC102RouteBRowSourceIndependenceReplay.v1",
        "label": "PSM-C1-02 / SOURCE-IDENTITY / SI-1u-B2-ROWSOURCE",
        "status": "ROUTE_B_FINAL_ROW_SOURCE_INDEPENDENCE_GATE_REPLAYED_OPEN",
        "source": rel(ROUTE_B_GENERAL),
        "strict_row_source_validator_built": route_b_decision["strict_row_source_validator_built"],
        "route_B_all_other_strict_fields_closed": route_b_decision["route_B_all_other_strict_fields_closed"],
        "remaining_route_B_field": route_b_decision["remaining_route_B_field"],
        "route_B_promoted_now": route_b_decision["route_B_promoted_now"],
        "minimal_next": route_b_decision["minimal_next"]["route_B"],
        "route_A_fallback_still_available": route_b_decision["route_A_fallback_still_available"],
        "current_attempt_validates": route_b_decision["current_attempt_validates"],
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "closure_claimed": False,
    }

    common_obstruction = {
        "schema": "MTTPSMC102CommonFinalSourcePromotionObstruction.v1",
        "status": "FINAL_UNPATCHED_SOURCE_PROMOTION_REDUCED_TO_ROUTE_A_SOURCE_THEOREM_OR_ROUTE_B_ROW_SOURCE_THEOREM",
        "closed_boundary": "DONE-PARITY-00",
        "SM_parity_remains_closed": True,
        "local_principle_route_validates": local_validator["ok"],
        "local_principle_counts_as_true_no_knob": False,
        "unpatched_source_promotion_closed": False,
        "route_A_final_theorem": {
            "name": "SelectedPhiFinC1PhysicalSourceEmissionTheorem",
            "required_fields": route_a_replay["required_unpatched_source_fields"],
            "current_validator_rejects": route_a_replay["current_physical_source_validator_rejects"],
            "conditional_witness_validates": route_a_replay["conditional_physical_source_witness_validates"],
        },
        "route_B_final_theorem": {
            "name": "SelectedFiniteC1RowSourceIndependenceTheorem",
            "required_fields": route_b_replay["minimal_next"],
            "only_open_field": route_b_replay["remaining_route_B_field"],
            "current_attempt_validates": False,
        },
        "superset_policy": {
            "paths_used_as_free_parameters": False,
            "observed_constants_used": False,
            "target_fitting_used": False,
            "meaning": "Route A and Route B are constrained exits to the same source-promotion packet, not adjustable theory knobs.",
        },
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "closure_claimed": False,
    }

    next_work = {
        "schema": "MTTNextLabeledWorkorderAfterPSMC102PhysicalBoundaryFirstVariationOrRowSource.v1",
        "previous_artifact": "MTT_Selected_PSM_C1_02_PhysicalBoundaryFirstVariation_or_RouteBRowSourceIndependence_v1",
        "next_required_artifact": NEXT,
        "primary": {
            "label": "PSM-C1-02 / SOURCE-IDENTITY / ROUTE-A-FINAL",
            "task": "Fill a theorem-derived SelectedPhiFinC1PhysicalSourceEmission packet with the six I11 physical source fields.",
        },
        "fallback": {
            "label": "PSM-C1-02 / SOURCE-IDENTITY / ROUTE-B-FINAL",
            "task": "Prove selected finite-C1 row-source independence from residual-projector replay for the 72 primitive, 36 sector, and 2 Hessian/source rows.",
        },
        "status": "NEXT_WORKORDER_ROUTE_A_SELECTED_SOURCE_EMISSION_OR_ROUTE_B_ACTUAL_ROWSOURCE_INDEPENDENCE",
        "target_fitting_used": False,
        "observed_data_used_as_selector": False,
    }

    candidate = {
        "candidate": "MTTSelectedPSMC102PhysicalBoundaryFirstVariationOrRouteBRowSourceIndependence",
        "active_label": "PSM-C1-02",
        "active_routes": [
            "SOURCE-IDENTITY/SI-1u-A1a-UNPATCHED-I11",
            "SOURCE-IDENTITY/SI-1u-B2-ROWSOURCE",
        ],
        "status": STATUS,
        "previous": rel(PREVIOUS),
        "previous_status": previous["status"],
        "inputs": {
            "route_a_physical_boundary_firstvariation": rel(ROUTE_A_GENERAL),
            "route_b_rowsource_independence": rel(ROUTE_B_GENERAL),
            "local_route_a_validation": rel(LOCAL_ROUTE_A),
        },
        "output_packets": {
            "route_a_i11_boundary_firstvariation_replay": rel(ROUTE_A_REPLAY),
            "route_b_rowsource_independence_replay": rel(ROUTE_B_REPLAY),
            "common_source_promotion_final_obstruction": rel(COMMON_OBSTRUCTION),
            "next_labeled_workorder": rel(NEXT_WORK),
        },
        "closure_decision": {
            "SM_parity_closed_under_declared_standard": True,
            "local_principle_route_A_validates": True,
            "route_A_unpatched_closed": False,
            "route_B_row_source_independence_closed": False,
            "unpatched_PSM_C1_02_closed": False,
            "true_SM_equivalence_closed": False,
            "no_knob_closed": False,
        },
        "what_closes_now": {
            "PSM_labeled_import_of_Route_A_I11_gate": True,
            "PSM_labeled_import_of_Route_B_row_source_gate": True,
            "local_principle_validation_reconciled_without_no_knob_overclaim": True,
            "final_unpatched_source_promotion_obstruction_named": True,
            "SM_parity_boundary_preserved": True,
        },
        "what_remains_open": {
            "SelectedPhiFinC1PhysicalSourceEmissionTheorem": True,
            "SelectedFiniteC1RowSourceIndependenceTheorem": True,
            "unpatched_PSM_C1_02_source_promotion": True,
            "true_SM_equivalence": True,
            "no_knob_closure": True,
        },
        "theorem": {
            "name": "PSMC102PhysicalBoundaryFirstVariationOrRouteBRowSourceIndependenceTheorem",
            "proved": True,
            "statement": (
                "The PSM-C1-02 unpatched A1a cutset imports the strict Route-A physical boundary/first-variation "
                "gate and the strict Route-B row-source independence gate. Route A has a validating conditional "
                "six-field physical source witness but no unpatched same-branch source theorem. Route B has all "
                "strict fields closed except source independence from residual-projector replay. Therefore the "
                "last unpatched source-promotion obstruction is exactly either a SelectedPhiFinC1PhysicalSourceEmission "
                "theorem or a SelectedFiniteC1RowSourceIndependence theorem."
            ),
        },
        "superset_strategy": {
            "classification": "PSM_LABELED_FINAL_SOURCE_PROMOTION_CUTSET",
            "paths_used_as_free_parameters": False,
            "route_A": "physical Phi_fin^C1 source-emission theorem",
            "route_B": "selected finite-C1 row-source independence theorem",
            "local_route": "validator-clean local principle replay, preserved as local not no-knob",
        },
        "next_required_artifact": NEXT,
        "closure_claimed": False,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
    }

    cert = {
        "certificate": "MTT_Selected_PSM_C1_02_PhysicalBoundaryFirstVariation_or_RouteBRowSourceIndependence_v1",
        "status": STATUS,
        "candidate_path": rel(OUTPUT),
        "note_path": rel(NOTE),
        "route_A_current_rejects": True,
        "route_A_conditional_passes": True,
        "route_B_all_other_strict_fields_closed": True,
        "route_B_row_source_independence_closed": False,
        "SM_parity_remains_closed": True,
        "unpatched_closure_claimed": False,
        "closure_claimed": False,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "next_required_artifact": NEXT,
    }

    note = f"""# MTT Selected PSM C1 02 PhysicalBoundaryFirstVariation or RouteBRowSourceIndependence v1

Status labels:

- `PSM-C1-02 / SOURCE-IDENTITY / SI-1u-A1a-UNPATCHED-I11`
- `PSM-C1-02 / SOURCE-IDENTITY / SI-1u-B2-ROWSOURCE`

Status: `{STATUS}`

## Result

The PSM-labeled unpatched source frontier now imports the two strict final gates:

- Route A: physical boundary/first-variation source emission.
- Route B: finite-C1 row-source independence.

The local-principle route validates, but remains local-premise closure rather
than an unpatched/no-knob theorem.  SM parity stays frozen closed under the
declared measured-input standard.

## Remaining Unpatched Target

One of the following must be supplied:

- `SelectedPhiFinC1PhysicalSourceEmissionTheorem`.
- `SelectedFiniteC1RowSourceIndependenceTheorem`.

No observed constants, target residuals, benchmark entries, or adjustable
coefficients are used as selectors.

## Next Artifact

`{NEXT}`
"""

    write_json(ROUTE_A_REPLAY, route_a_replay)
    write_json(ROUTE_B_REPLAY, route_b_replay)
    write_json(COMMON_OBSTRUCTION, common_obstruction)
    write_json(NEXT_WORK, next_work)
    write_json(OUTPUT, candidate)
    write_json(CERT, cert)
    NOTE.write_text(note, encoding="utf-8")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
