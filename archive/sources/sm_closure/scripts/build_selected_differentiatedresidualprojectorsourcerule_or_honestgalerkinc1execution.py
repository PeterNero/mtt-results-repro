"""Build differentiated residual-projector source rule or honest Galerkin C1 execution gate."""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "candidate_data"
CERTS = ROOT / "certificates"
CORPUS = ROOT / "proof_corpus"

PREVIOUS = DATA / "selected_phifinc1_residualprojectorapplication_or_honestgalerkinexecution_valuefill.candidate.json"
APPLICATION_DECISION = (
    DATA
    / "selected_phifinc1_residualprojectorapplication_or_honestgalerkinexecution_valuefill"
    / "application_or_execution_decision.packet.json"
)
CANONICAL_PROJECTOR = (
    DATA
    / "selected_canonicalresidualprojector_or_honestgalerkinc1_valuefill"
    / "canonical_fixedfiber_residual_projector.packet.json"
)
CANONICAL_CUTSET = (
    DATA
    / "selected_canonicalresidualprojector_or_honestgalerkinc1_valuefill"
    / "projector_or_galerkin_cutset_decision.packet.json"
)
SOURCE_SELECTOR = DATA / "selected_primitivevertex_source_or_basistransport_selectiontheorem.candidate.json"
PRIMITIVE_VALUE_GATE = DATA / "selected_primitiveoverlapcontractions_valueemission_or_honestgalerkinrun.candidate.json"
WEYLPAIR_SOURCE_GATE = DATA / "selected_routec_weylpair_basis_transport_or_vertex_source_theorem.candidate.json"
WEYLPAIR_A_GATE = DATA / "selected_routec_weylpair_aselected_assembly_or_source_proof.candidate.json"
GALERKIN_CONTRACT = (
    DATA
    / "selected_primitiveoverlapcontractions_valueemission_or_honestgalerkinrun"
    / "honest_galerkin_c1_value_run_contract.packet.json"
)

OUTPUT = DATA / "selected_differentiatedresidualprojectorsourcerule_or_honestgalerkinc1execution.candidate.json"
PACKET_DIR = DATA / "selected_differentiatedresidualprojectorsourcerule_or_honestgalerkinc1execution"
SOURCE_RULE_PACKET = PACKET_DIR / "differentiated_residual_projector_source_rule.contract.json"
ROUTE_LADDER_PACKET = PACKET_DIR / "source_rule_or_execution_route_ladder.packet.json"
HONEST_EXECUTION_PACKET = PACKET_DIR / "honest_galerkin_c1_execution_requirement.packet.json"
CERT = CERTS / "selected_differentiatedresidualprojectorsourcerule_or_honestgalerkinc1execution_certificate.json"
NOTE = CORPUS / "MTT_Selected_DifferentiatedResidualProjectorSourceRule_or_HonestGalerkinC1Execution_v1.md"

STATUS = "MTT_SELECTED_DIFFERENTIATEDRESIDUALPROJECTORSOURCERULE_OR_HONESTGALERKINC1EXECUTION_BUILT_SOURCE_RULE_CONTRACT_OPEN"
NEXT = "MTT_Selected_WeylPairSourceEmission_or_HonestGalerkinC1Execution_ValueRun_v1"


def rel(path: Path) -> str:
    try:
        return str(path.relative_to(ROOT)).replace("\\", "/")
    except ValueError:
        return str(path)


def load(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def main() -> int:
    PACKET_DIR.mkdir(parents=True, exist_ok=True)

    previous = load(PREVIOUS)
    application_decision = load(APPLICATION_DECISION)
    projector = load(CANONICAL_PROJECTOR)
    canonical_cutset = load(CANONICAL_CUTSET)
    source_selector = load(SOURCE_SELECTOR)
    primitive_value = load(PRIMITIVE_VALUE_GATE)
    weyl_source = load(WEYLPAIR_SOURCE_GATE)
    weyl_a = load(WEYLPAIR_A_GATE)
    galerkin = load(GALERKIN_CONTRACT)

    conditional = canonical_cutset["if_lane_A_application_theorem_is_supplied"]
    selector_packet = source_selector["source_selector_packet"]
    span_obstruction = primitive_value["span_obstruction_summary"]
    source_gate = weyl_source["theorem_gate"]

    source_rule_contract = {
        "schema": "MTTDifferentiatedResidualProjectorSourceRuleContract.v1",
        "status": "SOURCE_RULE_CONTRACT_EMITTED_VALUES_OPEN",
        "rule_name": "SelectedDifferentiatedResidualProjectorSourceRule",
        "formal_statement": (
            "For the selected q79/F,m=1 S3/GS Route-C branch, the differentiated "
            "C1 transfer applies Q_residual to the selected Weyl source packet, or "
            "equivalently emits the same residual R_Z/R_X through a selected "
            "basis-transport, vertex, or Hessian source in the same transported "
            "zero-mode basis and normalization."
        ),
        "already_selected_support": {
            "canonical_Q_residual_available": True,
            "Q_residual_rank": projector["operator_checks"]["residual_projector_rank"],
            "source_selector_promoted": source_selector["promotion_decision"][
                "source_selector_promoted"
            ],
            "primitive_vertex_or_basis_transport_source_selector_promoted": source_selector[
                "promotion_decision"
            ]["selected_primitive_vertex_or_basis_transport_source_promoted"],
            "static_sector_route_selected": selector_packet["selector_components"][
                "static_sector_route"
            ]["selected"],
            "static_trace_transfer_normalization_selected": selector_packet["selector_components"][
                "static_overlap_transfer_normalization"
            ]["selected"],
            "alpha1_dotD_driver_verified": selector_packet["selector_components"][
                "alpha1_dotD_driver"
            ]["alpha1_driver_verified"],
        },
        "why_selector_is_not_enough": {
            "source_selector_is_value_emission": False,
            "primitive_fixed_fiber_span_can_close": span_obstruction[
                "pure_fixed_fiber_span_can_close"
            ],
            "phase_single_sector_residual_norm_sq": span_obstruction[
                "phase_single_sector_residual_norm_sq"
            ],
            "shift_single_sector_residual_norm_sq": span_obstruction[
                "shift_single_sector_residual_norm_sq"
            ],
            "stationary_transport_only_ruled_out": True,
        },
        "exact_conditional_values_if_rule_is_proved": {
            "A_transpose_A": conditional["A_transpose_A"],
            "A_transpose_b": conditional["A_transpose_b"],
            "deltaTheta_C1": conditional["deltaTheta_C1"],
            "rank": conditional["rank"],
            "SM_parity_dynamic_packet_would_close": True,
            "no_knob_flavor_constants_would_close": False,
        },
        "required_emissions": [
            "theorem-derived phase-like Z or I+Z residual/basis-holonomy source",
            "theorem-derived shift-like X or I+X residual/active-vertex source",
            "same transported zero-mode basis and projector normalization",
            "selected Hessian/source vector b_selected or equivalent emitted source coefficients",
            "rank and Gram replay in the fixed 72-real coordinate system",
        ],
        "currently_emitted": {
            "selected_differentiated_residual_projector_source_rule": False,
            "selected_basis_transport_vertex_or_Hessian_values": False,
            "selected_A_selected": False,
            "selected_b_selected": False,
            "selected_deltaTheta_C1": False,
        },
        "observed_data_used": False,
        "target_fitting_used": False,
    }

    route_ladder = {
        "schema": "MTTSourceRuleOrExecutionRouteLadder.v1",
        "status": "ROUTE_LADDER_RANKED_NO_PROMOTION",
        "straight_path": {
            "id": "A_differentiated_residual_projector_rule",
            "description": application_decision["straight_path"],
            "current_status": "OPEN_NEW_SOURCE_RULE_REQUIRED",
            "why_not_closed": (
                "Existing Phi_fin^C1 support proves stationary/source transport and alpha1/dotD, "
                "but not the differentiated residual-projector application."
            ),
        },
        "near_straight_source_path": {
            "id": "B_enriched_weylpair_basis_transport_or_vertex_source",
            "description": "Promote the enriched Weyl-pair basis-transport/vertex packet as same-branch source emission.",
            "current_status": weyl_source["status"],
            "algebraically_sufficient": weyl_source["span_test"]["target_in_span"],
            "conditional_A_rank": weyl_a["locked_solve"]["rank"],
            "conditional_deltaTheta": weyl_a["locked_solve"]["deltaTheta_conditional"],
            "why_not_closed": weyl_a["conditional_operator"]["why_not_selected"],
        },
        "superset_execution_path": {
            "id": "C_honest_selected_Galerkin_C1_execution",
            "description": application_decision["superset_path"],
            "current_status": galerkin["status"],
            "selected_source_verified": galerkin["selected_source_verified"],
            "required_outputs": galerkin["required_outputs"],
        },
        "ruled_out_paths": [
            "stationary transport-only Phi_fin^C1",
            "pure fixed-fiber primitive replay",
            "promoting canonical Q_residual without an application/source rule",
            "using observed SM flavor data or benchmark matrices as selectors",
        ],
        "recommended_next": "B_enriched_weylpair_basis_transport_or_vertex_source",
        "reason": (
            "It is the shortest route with algebraic sufficiency already proved; it "
            "still needs same-branch source emission, but not a new numerical search."
        ),
        "observed_data_used": False,
        "target_fitting_used": False,
    }

    honest_execution = {
        "schema": "MTTHonestGalerkinC1ExecutionRequirement.v1",
        "status": "HONEST_EXECUTION_REQUIREMENT_REEMITTED_VALUES_OPEN",
        "must_fill_template": galerkin["must_fill_template"],
        "required_inputs": galerkin["required_inputs"],
        "required_outputs": galerkin["required_outputs"],
        "acceptance_checks": galerkin["acceptance_checks"],
        "selected_source_verified": galerkin["selected_source_verified"],
        "current_manifest_status": galerkin["current_manifest_status"],
        "would_close_SM_parity_dynamic_packet_if_values_emitted": True,
        "would_close_no_knob_flavor_constants_if_values_emitted": False,
        "observed_flavor_data_forbidden": galerkin["observed_flavor_data_forbidden"],
        "target_fitting_forbidden": galerkin["target_fitting_forbidden"],
    }

    candidate = {
        "candidate": "MTTSelectedDifferentiatedResidualProjectorSourceRuleOrHonestGalerkinC1Execution",
        "status": STATUS,
        "inputs": {
            "previous_application_gate": rel(PREVIOUS),
            "application_decision": rel(APPLICATION_DECISION),
            "canonical_projector": rel(CANONICAL_PROJECTOR),
            "canonical_cutset": rel(CANONICAL_CUTSET),
            "primitive_source_selector": rel(SOURCE_SELECTOR),
            "primitive_value_gate": rel(PRIMITIVE_VALUE_GATE),
            "weylpair_basis_transport_source_gate": rel(WEYLPAIR_SOURCE_GATE),
            "weylpair_A_assembly_gate": rel(WEYLPAIR_A_GATE),
            "honest_galerkin_contract": rel(GALERKIN_CONTRACT),
        },
        "output_packets": {
            "differentiated_residual_projector_source_rule": rel(SOURCE_RULE_PACKET),
            "source_rule_or_execution_route_ladder": rel(ROUTE_LADDER_PACKET),
            "honest_galerkin_c1_execution_requirement": rel(HONEST_EXECUTION_PACKET),
        },
        "what_closes_now": {
            "differentiated_residual_projector_source_rule_formalized": True,
            "selector_vs_value_emission_gap_made_explicit": True,
            "enriched_weylpair_route_ranked_primary": True,
            "honest_Galerkin_execution_requirements_reemitted": True,
            "ruled_out_stationary_and_fixed_fiber_shortcuts": True,
            "observed_constants_excluded_as_selectors": True,
        },
        "what_remains_open": {
            "selected_differentiated_residual_projector_source_rule": True,
            "selected_enriched_weylpair_source_emission": True,
            "selected_basis_transport_vertex_or_Hessian_values": True,
            "honest_selected_Galerkin_C1_execution_values": True,
            "selected_A_selected": True,
            "selected_b_selected": True,
            "selected_deltaTheta_C1": True,
            "SM_parity_dynamic_packet_closure": True,
            "true_SM_equivalence_closure": True,
            "full_no_knob_flavor_closure": True,
        },
        "promotion_decision": {
            "differentiated_residual_projector_source_rule_promoted": False,
            "enriched_weylpair_source_emission_promoted": False,
            "honest_Galerkin_C1_execution_promoted": False,
            "selected_A_selected_promoted": False,
            "selected_b_selected_promoted": False,
            "selected_deltaTheta_C1_promoted": False,
            "SM_parity_dynamic_packet_closed": False,
            "true_SM_equivalence_closed": False,
            "no_knob_flavor_constants_closed": False,
        },
        "observed_data_used": False,
        "target_fitting_used": False,
        "closure_claimed": False,
        "SM_parity_dynamic_packet_closure_claimed": False,
        "true_SM_equivalence_claimed": False,
        "no_knob_closure_claimed": False,
        "next_required_artifact": NEXT,
        "theorem": {
            "name": "DifferentiatedResidualProjectorSourceRuleCutsetTheorem",
            "proved": True,
            "statement": (
                "After canonical Q_residual is constructed, SM-parity dynamic closure is "
                "equivalent to one of three value-emission routes: a selected differentiated "
                "residual-projector source rule, a same-branch enriched Weyl-pair basis-transport/"
                "vertex/Hessian source emitting the residual application, or honest selected "
                "Galerkin C1 execution.  Existing artifacts close the selector and algebraic "
                "sufficiency layers but not selected value emission, so A_selected, b_selected, "
                "and deltaTheta_C1 remain unpromoted."
            ),
        },
    }

    cert = {
        "certificate": "MTT_Selected_DifferentiatedResidualProjectorSourceRule_or_HonestGalerkinC1Execution_v1",
        "status": STATUS,
        "candidate_path": rel(OUTPUT),
        "note_path": rel(NOTE),
        "source_rule_packet_path": rel(SOURCE_RULE_PACKET),
        "route_ladder_packet_path": rel(ROUTE_LADDER_PACKET),
        "honest_execution_packet_path": rel(HONEST_EXECUTION_PACKET),
        "theorem_proved": True,
        "closure_claimed": False,
        "SM_parity_dynamic_packet_closure_claimed": False,
        "true_SM_equivalence_claimed": False,
        "no_knob_closure_claimed": False,
        "observed_data_used": False,
        "target_fitting_used": False,
        "what_closes": candidate["what_closes_now"],
        "what_remains_open": candidate["what_remains_open"],
        "next_required_artifact": NEXT,
    }

    note = f"""# MTT Selected DifferentiatedResidualProjectorSourceRule or HonestGalerkinC1Execution v1

Status: `{STATUS}`.

The next proof object is now formalized.  The selected source selector and the
canonical projector are both in place, but selector data is not value emission.

The three legal routes are:

```text
A. prove selected differentiated Phi_fin^C1 applies Q_residual
B. promote the enriched Weyl-pair basis-transport/vertex/Hessian source
C. run honest selected Galerkin C1 execution
```

Route B is ranked primary because the enriched Weyl-pair packet is already
algebraically sufficient and its conditional solve has rank
`{weyl_a["locked_solve"]["rank"]}` with `deltaTheta={weyl_a["locked_solve"]["deltaTheta_conditional"]}`.

If any legal value-emission route supplies the normal form, the conditional
values are:

```text
A^T A = {conditional["A_transpose_A"]}
A^T b = {conditional["A_transpose_b"]}
deltaTheta_C1 = {conditional["deltaTheta_C1"]}
```

No observed masses, CKM/PMNS values, CP phase, benchmark matrices, or target
residuals are used as selectors.

Next artifact: `{NEXT}`.
"""

    SOURCE_RULE_PACKET.write_text(json.dumps(source_rule_contract, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    ROUTE_LADDER_PACKET.write_text(json.dumps(route_ladder, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    HONEST_EXECUTION_PACKET.write_text(json.dumps(honest_execution, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    OUTPUT.write_text(json.dumps(candidate, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    CERT.write_text(json.dumps(cert, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    NOTE.write_text(note, encoding="utf-8")
    print(json.dumps({"candidate": rel(OUTPUT), "status": STATUS}, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
