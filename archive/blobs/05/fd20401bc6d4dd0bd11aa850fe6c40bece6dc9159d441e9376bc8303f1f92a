"""Build the post-source dynamic Qa/SU3 or C1 response frontier artifact."""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "candidate_data"
CERTS = ROOT / "certificates"
CORPUS = ROOT / "proof_corpus"

SLUG = "selected_dynamicqasu3_or_c1response_postsourcefrontier"
PACKET_DIR = DATA / SLUG
OUTPUT = DATA / f"{SLUG}.candidate.json"
RECONCILIATION = PACKET_DIR / "postsource_reconciliation.packet.json"
FRONTIER = PACKET_DIR / "dynamic_qasu3_c1_frontier.packet.json"
ROUTES = PACKET_DIR / "three_route_closure_contract.packet.json"
NEXT = PACKET_DIR / "next_executable_workorder.packet.json"
CERT = CERTS / f"{SLUG}_certificate.json"
NOTE = CORPUS / "MTT_Selected_DynamicQaSU3_or_C1Response_PostSourceFrontier_v1.md"

STATUS = "MTT_SELECTED_DYNAMICQASU3_OR_C1RESPONSE_POSTSOURCEFRONTIER_BUILT_VALUES_OPEN"
NEXT_ARTIFACT = "MTT_Selected_SameSourceDynamicPhiFinC1_or_HonestGalerkinExecution_RouteTest_v1"


def rel(path: Path) -> str:
    try:
        return str(path.relative_to(ROOT)).replace("\\", "/")
    except ValueError:
        return str(path)


def load(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def all_true(values: dict[str, bool]) -> bool:
    return all(values.values())


def main() -> int:
    PACKET_DIR.mkdir(parents=True, exist_ok=True)

    boundary = load(DATA / "selected_smparityfrozenboundary_or_postsmparityfrontier" / "frozen_smparity_boundary.packet.json")
    next_boundary = load(DATA / "selected_smparityfrozenboundary_or_postsmparityfrontier" / "next_work_after_frozen_boundary.packet.json")
    heat_frontier = load(DATA / "selected_heattorsionresponse_finalgate" / "post_eight_slot_true_equivalence_frontier.packet.json")
    heat_cert = load(CERTS / "selected_heattorsionresponse_finalgate_certificate.json")
    static_provenance = load(DATA / "selected_enrichedweylpairsourceprovenance_or_galerkinc1values.candidate.json")
    c1_frontier = load(DATA / "selected_dynamicc1transfertensor_or_galerkinc1values.candidate.json")
    acceptance = load(DATA / "selected_dynamicc1transfertensor_or_galerkinc1values_acceptance_manifest.candidate.json")
    value_cutset = load(DATA / "selected_dynamicc1transfertensor_valueemission_or_honestgalerkinc1run.candidate.json")
    source_map = load(DATA / "selected_primitivec1tensor_hessiansourcemap_or_honestgalerkinc1execution.candidate.json")
    selection_test = load(DATA / "selected_sourcemapselectiontheorem_or_honestgalerkinc1valuerun.candidate.json")
    first_static_qasu3 = load(DATA / "selected_acceptedhiggsdecaycovarianceprofile_or_firstqasu3selectedslotclosure.candidate.json")

    closed_support = {
        "SM_parity_boundary_frozen": boundary["boundary_locks"],
        "finite_operator_source_slots_8_of_8_closed": heat_frontier["source_slot_layer_closed"]
        and heat_frontier["operator_source_slots_closed"] == 8
        and heat_frontier["operator_source_slots_remaining"] == 0,
        "heat_spectrum_pseudodeterminant_response_closed": heat_cert[
            "finite_determinant_heat_spectrum_or_torsion_response_closed"
        ],
        "static_enriched_weylpair_provenance_closed": static_provenance["promotion_decision"][
            "static_enriched_weylpair_source_provenance_promoted"
        ],
        "first_static_QaSU3_route_slot_closed": first_static_qasu3["closure_decision"][
            "first_selected_QaSU3_static_slot_closed"
        ],
        "alpha1_dotD_operator_support_closed_for_frontier": c1_frontier["promotion_decision"][
            "operator_alpha1_support_closed_for_frontier"
        ],
        "strict_72_real_acceptance_manifest_built": acceptance["what_closes_now"][
            "dynamic_C1_acceptance_manifest"
        ],
        "conditional_dynamic_C1_tensor_normal_form_built": c1_frontier["what_closes_now"][
            "conditional_dynamic_C1_transfer_tensor_normal_form_built"
        ],
        "minimal_source_map_candidate_constructed": source_map["promotion_decision"][
            "source_map_candidate_constructed"
        ],
        "value_cutset_identified": value_cutset["what_closes_now"]["minimal_dynamic_value_cutset_identified"],
    }

    open_dynamic_targets = {
        "actual_dynamic_QaSU3_operator_packet": True,
        "selected_differentiated_PhiFinC1_source_map": True,
        "selected_primitive_C1_overlap_contractions": True,
        "selected_A_selected": True,
        "selected_b_selected": True,
        "selected_deltaTheta_C1": True,
        "selected_sector_response_matrices": True,
        "full_S2_value_emission_beyond_DE_gap": True,
        "precision_QFT_observable_functor": True,
        "no_knob_value_derivation": True,
    }

    reconciliation = {
        "schema": "MTTPostSourceFrontierReconciliation.v1",
        "status": "FROZEN_SOURCE_SLOT_LAYER_RECONCILED_WITH_DYNAMIC_VALUE_FRONTIER",
        "closed_support": closed_support,
        "stale_language_retired": {
            "do_not_use": [
                "SM-parity blocker",
                "missing finite source slot",
                "Qa/SU3 source-slot count still below eight",
            ],
            "reason": (
                "The latest frozen boundary and heat/torsion final gate supersede older partial Qa/SU3 "
                "source-slot accounting at the finite source-slot layer. Remaining work is dynamic value "
                "promotion and true-equivalence/no-knob upgrade."
            ),
        },
        "live_open_targets": open_dynamic_targets,
        "guardrails": {
            "SM_parity_reopened": False,
            "finite_source_slots_reopened": False,
            "actual_dynamic_QaSU3_operator_packet_closed": False,
            "selected_C1_response_closed": False,
            "true_SM_equivalence_closed": False,
            "no_knob_closed": False,
            "observed_data_used_as_selector": False,
            "target_fitting_used": False,
        },
    }

    routes = {
        "schema": "MTTDynamicQaSU3C1ThreeRouteClosureContract.v1",
        "status": "THREE_LEGAL_POSTSOURCE_ROUTES_LOCKED_VALUES_OPEN",
        "shared_acceptance_target": {
            "A_selected": "selected 72-real dynamic response operator / Hessian normal matrix",
            "b_selected": "selected source vector or Hessian source vector",
            "deltaTheta_C1": "selected solve; conditional replay currently equals [1,1]",
            "sector_response_matrices": "selected sector matrices with non-scalar dynamic response",
            "actual_dynamic_QaSU3_operator_packet": "dynamic HYM/End0/C1 packet, not just static route labels",
        },
        "routes": [
            {
                "id": "route_A_same_source_dynamic_PhiFinC1",
                "status": "OPEN_PRIMARY",
                "closed_support": [
                    "stationary projector/Riesz/Green support",
                    "alpha1/dotD replay support",
                    "static Weyl Z/X routing",
                    "canonical Q_residual and exact residual Weyl polynomials",
                    "conditional rank-2 normal form",
                ],
                "must_emit": [
                    "selected differentiated Phi_fin^C1 applies Q_residual to phase/shift legs",
                    "same-source b_selected or Hessian source vector",
                    "selected A_selected and sector response matrices",
                ],
                "forbidden_shortcut": "Do not promote the conditional Weyl-pair packet without the physical differentiated source rule.",
            },
            {
                "id": "route_B_honest_selected_Galerkin_C1_execution",
                "status": "OPEN_REPLACEMENT",
                "closed_support": [
                    "strict 72-real acceptance manifest",
                    "honest Galerkin value slots declared",
                    "same target objects as route A",
                ],
                "must_emit": [
                    "selected zero-mode basis and primitive 3x3 terms",
                    "linear response matrices",
                    "b_selected/source vector",
                    "C33/nonzero-family-rank checks",
                ],
                "forbidden_shortcut": "Do not use diagnostic or model-active Galerkin values as selected replacement values.",
            },
            {
                "id": "route_C_superset_bridge",
                "status": "OPEN_BRIDGE",
                "closed_support": [
                    "finite D_E/gap/heat source-slot layer",
                    "typed monad/section-ring static SM-slot data",
                    "HYM/Route-C and visible Chern-Weil support",
                    "external QFT/RG convention layer for replay constraints",
                ],
                "must_emit": [
                    "a theorem that identifies the dynamic HYM/End0/C1 packet with the selected C1 response target",
                    "a bridge proving route A target values or route B replacement values from the same selected branch",
                ],
                "forbidden_shortcut": "Do not combine lanes by fitting observed Yukawa or mixing targets.",
            },
        ],
        "route_closes_now": False,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
    }

    frontier = {
        "schema": "MTTDynamicQaSU3OrC1ResponsePostSourceFrontier.v1",
        "status": "POST_SMPARITY_DYNAMIC_QASU3_C1_FRONTIER_OPEN_VALUES_NOT_EMITTED",
        "starting_point": {
            "SM_parity_closed_frozen": True,
            "finite_operator_source_slot_layer_closed_frozen": True,
            "source_slots_closed": 8,
            "source_slots_remaining": 0,
            "active_tier": "post-SM-parity true-equivalence/no-knob frontier",
        },
        "closed_support": closed_support,
        "open_dynamic_targets": open_dynamic_targets,
        "current_best_reduction": {
            "blocker_type": "dynamic selected value/source promotion",
            "not_blocker_type": "SM-parity replay or finite source-slot assembly",
            "minimal_cutset": [
                "selected differentiated Phi_fin^C1 / primitive tensor source map plus b_selected",
                "or honest selected Galerkin C1 execution emitting replacement values",
                "or same-branch superset bridge from HYM/Route-C/typed source data to the accepted dynamic target",
            ],
        },
        "closure_decision": {
            "postsource_frontier_built": True,
            "actual_dynamic_QaSU3_operator_packet_closed": False,
            "selected_C1_response_closed": False,
            "A_selected_promoted": False,
            "b_selected_promoted": False,
            "deltaTheta_C1_promoted": False,
            "sector_response_matrices_promoted": False,
            "true_SM_equivalence_closed": False,
            "no_knob_closed": False,
        },
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
    }

    next_work = {
        "schema": "MTTNextExecutableDynamicQaSU3C1Workorder.v1",
        "status": "ROUTE_TEST_SELECTED_ROUTE_A_PRIMARY_ROUTE_B_PARALLEL",
        "next_required_artifact": NEXT_ARTIFACT,
        "work_items": [
            {
                "id": "A1_source_rule_test",
                "route": "route_A_same_source_dynamic_PhiFinC1",
                "task": "Test whether existing differentiated Phi_fin^C1 / residual-projector artifacts already imply physical Q_residual application.",
                "success_condition": "selected differentiated source rule emits phase R_Z and shift R_X sources with same-branch b_selected.",
            },
            {
                "id": "B1_galerkin_readiness_test",
                "route": "route_B_honest_selected_Galerkin_C1_execution",
                "task": "Inventory missing basis/quadrature/value rows for an honest selected Galerkin C1 execution.",
                "success_condition": "all zero-mode bases, primitive 3x3 terms, linear response matrices, and b source rows are executable.",
            },
            {
                "id": "C1_superset_bridge_test",
                "route": "route_C_superset_bridge",
                "task": "Check whether HYM/Route-C, typed monad/section-ring, and finite D_E/heat packets identify the same dynamic target.",
                "success_condition": "bridge proves one of route A or route B target emissions without observed target fitting.",
            },
        ],
        "first_action": "build Route A source-rule test with Route B readiness sidecar",
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
    }

    candidate = {
        "candidate": "MTTSelectedDynamicQaSU3OrC1ResponsePostSourceFrontier",
        "status": STATUS,
        "inputs": {
            "frozen_boundary": rel(DATA / "selected_smparityfrozenboundary_or_postsmparityfrontier" / "frozen_smparity_boundary.packet.json"),
            "next_work_after_boundary": rel(DATA / "selected_smparityfrozenboundary_or_postsmparityfrontier" / "next_work_after_frozen_boundary.packet.json"),
            "post_eight_source_frontier": rel(DATA / "selected_heattorsionresponse_finalgate" / "post_eight_slot_true_equivalence_frontier.packet.json"),
            "static_weylpair_provenance": rel(DATA / "selected_enrichedweylpairsourceprovenance_or_galerkinc1values.candidate.json"),
            "dynamic_c1_frontier": rel(DATA / "selected_dynamicc1transfertensor_or_galerkinc1values.candidate.json"),
            "strict_acceptance_manifest": rel(DATA / "selected_dynamicc1transfertensor_or_galerkinc1values_acceptance_manifest.candidate.json"),
            "value_emission_cutset": rel(DATA / "selected_dynamicc1transfertensor_valueemission_or_honestgalerkinc1run.candidate.json"),
            "source_map_candidate": rel(DATA / "selected_primitivec1tensor_hessiansourcemap_or_honestgalerkinc1execution.candidate.json"),
            "source_map_selection_test": rel(DATA / "selected_sourcemapselectiontheorem_or_honestgalerkinc1valuerun.candidate.json"),
        },
        "output_packets": {
            "postsource_reconciliation": rel(RECONCILIATION),
            "dynamic_qasu3_c1_frontier": rel(FRONTIER),
            "three_route_closure_contract": rel(ROUTES),
            "next_executable_workorder": rel(NEXT),
        },
        "theorem": {
            "name": "PostSourceDynamicQaSU3C1FrontierTheorem",
            "proved": all_true(closed_support),
            "statement": (
                "After the frozen SM-parity boundary and eight-of-eight finite source-slot closure, the "
                "remaining active proof object is not SM-parity or finite source-slot assembly. It is dynamic "
                "selected operator/value emission: actual dynamic Qa/SU3, selected differentiated Phi_fin^C1 "
                "or primitive C1 response, A_selected, b_selected, deltaTheta_C1, and sector response matrices. "
                "The legal routes are same-source dynamic Phi_fin^C1, honest selected Galerkin C1 execution, or "
                "a same-branch superset bridge; none closes now."
            ),
        },
        "what_closes_now": {
            "postsource_dynamic_frontier_built": True,
            "stale_source_slot_language_retired": True,
            "three_legal_routes_locked": True,
            "next_executable_workorder_emitted": True,
            "observed_constants_excluded_as_selectors": True,
        },
        "what_remains_open": open_dynamic_targets,
        "closure_decision": frontier["closure_decision"],
        "next_required_artifact": NEXT_ARTIFACT,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "closure_claimed": False,
    }

    cert = {
        "certificate": "MTT_Selected_DynamicQaSU3_or_C1Response_PostSourceFrontier_v1",
        "candidate_path": rel(OUTPUT),
        "status": STATUS,
        "theorem_proved": all_true(closed_support),
        "SM_parity_reopened": False,
        "finite_source_slots_reopened": False,
        "actual_dynamic_QaSU3_operator_packet_closed": False,
        "selected_C1_response_closed": False,
        "true_SM_equivalence_closed": False,
        "no_knob_closed": False,
        "next_required_artifact": NEXT_ARTIFACT,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "note_path": rel(NOTE),
    }

    note = f"""# MTT Selected DynamicQaSU3 or C1Response PostSourceFrontier v1

This is the first post-SM-parity frontier artifact after freezing SM-parity and
closing all eight finite operator-source slots.

Closed support:

- frozen SM-parity boundary
- eight of eight finite operator-source slots
- selected finite `D_E`/gap/heat/pseudodeterminant layer
- static Weyl-pair and SM-slot routing
- alpha1/dotD operator support at the current frontier
- strict 72-real dynamic C1 acceptance target
- minimal primitive/Hessian source-map candidate

Live blocker:

Dynamic selected operator/value emission, not SM-parity replay and not finite
source-slot assembly.

Legal routes:

1. same-source dynamic `Phi_fin^C1` source rule
2. honest selected Galerkin C1 execution
3. same-branch superset bridge from HYM/Route-C, typed source data, and finite
   `D_E`/heat packets into the dynamic target

No route closes here. The point is to make the live target precise and prevent
old source-slot language from reappearing as if SM-parity had regressed.

Next artifact: `{NEXT_ARTIFACT}`.
"""

    for path, payload in [
        (RECONCILIATION, reconciliation),
        (FRONTIER, frontier),
        (ROUTES, routes),
        (NEXT, next_work),
        (OUTPUT, candidate),
        (CERT, cert),
    ]:
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(json.dumps(payload, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    NOTE.write_text(note, encoding="utf-8")
    print(json.dumps({"candidate": rel(OUTPUT), "status": STATUS}, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
