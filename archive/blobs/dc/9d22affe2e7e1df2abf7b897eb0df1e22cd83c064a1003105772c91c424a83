"""Build Route-A/Route-B test for PSM-C1-01 post-SM-parity work."""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "candidate_data"
CERTS = ROOT / "certificates"
CORPUS = ROOT / "proof_corpus"

SLUG = "selected_samesourcedynamicphifinc1_or_honestgalerkinexecution_routetest"
PACKET_DIR = DATA / SLUG
OUTPUT = DATA / f"{SLUG}.candidate.json"
ROUTE_A = PACKET_DIR / "route_a_psm_c1_01_source_rule_test.packet.json"
ROUTE_B = PACKET_DIR / "route_b_honest_galerkin_readiness_sidecar.packet.json"
LABEL_STATUS = PACKET_DIR / "label_status_after_route_test.packet.json"
NEXT = PACKET_DIR / "next_labeled_workorder.packet.json"
CERT = CERTS / f"{SLUG}_certificate.json"
NOTE = CORPUS / "MTT_Selected_SameSourceDynamicPhiFinC1_or_HonestGalerkinExecution_RouteTest_v1.md"

STATUS = "MTT_SELECTED_SAMESOURCEDYNAMICPHIFINC1_OR_HONESTGALERKINEXECUTION_ROUTETEST_BUILT_PSM_C1_01_OPEN"
NEXT_ARTIFACT = "MTT_Selected_PSM_C1_01_SourceRuleEmission_or_PSM_C1_04_bSelectedSidecar_v1"


def rel(path: Path) -> str:
    try:
        return str(path.relative_to(ROOT)).replace("\\", "/")
    except ValueError:
        return str(path)


def load(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def main() -> int:
    PACKET_DIR.mkdir(parents=True, exist_ok=True)

    labels = load(DATA / "selected_postsmparity_workbreakdown_labels" / "canonical_work_labels.packet.json")
    matrix = load(DATA / "selected_postsmparity_workbreakdown_labels" / "remaining_work_status_matrix.packet.json")
    postsource = load(DATA / "selected_dynamicqasu3_or_c1response_postsourcefrontier" / "dynamic_qasu3_c1_frontier.packet.json")
    route_contract = load(DATA / "selected_dynamicqasu3_or_c1response_postsourcefrontier" / "three_route_closure_contract.packet.json")
    selection_test = load(DATA / "selected_sourcemapselectiontheorem_or_honestgalerkinc1valuerun" / "source_map_selection_theorem_test.packet.json")
    obligation = load(DATA / "selected_primitivec1tensor_hessiansourcemap_or_honestgalerkinc1execution" / "source_map_selection_obligation_kernel.packet.json")
    source_rule_contract = load(DATA / "selected_differentiatedresidualprojectorsourcerule_or_honestgalerkinc1execution" / "differentiated_residual_projector_source_rule.contract.json")
    galerkin_req = load(DATA / "selected_differentiatedresidualprojectorsourcerule_or_honestgalerkinc1execution" / "honest_galerkin_c1_execution_requirement.packet.json")
    galerkin_slots = load(DATA / "selected_primitivec1tensor_hessiansourcemap_or_honestgalerkinc1execution" / "honest_galerkin_execution_value_slots.packet.json")
    primitive_manifest = load(DATA / "selected_routec_strominger_galerkin_solve" / "c1_primitive_contractions.candidate.json")
    projector_application = load(DATA / "selected_phifinc1_residualprojectorapplication_or_honestgalerkinexecution_valuefill.candidate.json")

    active_label_ok = matrix["current_active_label"] == "PSM-C1-01" and matrix["current_active_route"] == "ROUTE-A"
    route_a_contract = next(route for route in route_contract["routes"] if route["id"] == "route_A_same_source_dynamic_PhiFinC1")
    route_b_contract = next(route for route in route_contract["routes"] if route["id"] == "route_B_honest_selected_Galerkin_C1_execution")

    route_a_support = {
        "active_label_is_PSM_C1_01": active_label_ok,
        "route_A_is_primary": route_a_contract["status"] == "OPEN_PRIMARY",
        "canonical_projector_available": source_rule_contract["already_selected_support"]["canonical_Q_residual_available"],
        "Q_residual_rank_six": source_rule_contract["already_selected_support"]["Q_residual_rank"] == 6,
        "static_sector_route_selected": source_rule_contract["already_selected_support"]["static_sector_route_selected"],
        "alpha1_dotD_driver_verified": source_rule_contract["already_selected_support"]["alpha1_dotD_driver_verified"],
        "source_selector_promoted": source_rule_contract["already_selected_support"]["source_selector_promoted"],
        "exact_conditional_rank_two_replay": source_rule_contract["exact_conditional_values_if_rule_is_proved"]["rank"] == 2
        and source_rule_contract["exact_conditional_values_if_rule_is_proved"]["deltaTheta_C1"] == [1.0, 1.0],
        "stationary_transport_only_ruled_out": source_rule_contract["why_selector_is_not_enough"]["stationary_transport_only_ruled_out"],
        "projector_application_guardrail_blocks_shortcut": not projector_application["promotion_decision"][
            "PhiFinC1_projector_application_promoted"
        ],
    }

    route_a_missing = {
        "PSM-C1-01_selected_differentiated_source_rule": not source_rule_contract["currently_emitted"][
            "selected_differentiated_residual_projector_source_rule"
        ],
        "PSM-C1-04_selected_b_selected": not source_rule_contract["currently_emitted"]["selected_b_selected"],
        "PSM-C1-03_selected_A_selected": not source_rule_contract["currently_emitted"]["selected_A_selected"],
        "PSM-C1-05_selected_deltaTheta_C1": not source_rule_contract["currently_emitted"]["selected_deltaTheta_C1"],
        "PSM-C1-06_sector_response_matrices": obligation["strict_acceptance_field_status"][
            "sector_response_matrices"
        ]
        == "NOT_EMITTED_BY_SELECTED_VALUE_SOURCE",
    }
    route_a_closes_psm_c1_01 = False

    route_a = {
        "schema": "MTTRouteAPSMC101SourceRuleTest.v1",
        "status": "ROUTE_A_TESTED_SOURCE_RULE_STILL_OPEN",
        "active_label": "PSM-C1-01",
        "active_route": "ROUTE-A",
        "support_passed": route_a_support,
        "missing_for_closure": route_a_missing,
        "current_result": {
            "PSM-C1-01_closed": route_a_closes_psm_c1_01,
            "source_rule_contract_exists": True,
            "physical_differentiated_application_promoted": False,
            "phase_R_Z_selected_now": selection_test["selection_attempt"]["phase_R_Z_selected_now"],
            "shift_R_X_selected_now": selection_test["selection_attempt"]["shift_R_X_selected_now"],
            "b_source_emitted_now": selection_test["selection_attempt"]["b_source_emitted_now"],
            "conditional_values_if_rule_proved": source_rule_contract["exact_conditional_values_if_rule_is_proved"],
        },
        "next_needed_emissions": source_rule_contract["required_emissions"],
        "no_overclaim_reason": selection_test["why_selection_is_not_yet_proved"],
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
    }

    route_b_support = {
        "route_B_exists": route_b_contract["status"] == "OPEN_REPLACEMENT",
        "strict_72_real_target_available": galerkin_slots["strict_coordinate_target"]["total_real_coordinates"] == 72,
        "manifest_records_missing_primitive_contractions": primitive_manifest["status"]
        == "OPEN_C1_PRIMITIVE_CONTRACTIONS_MISSING",
        "selected_source_not_verified_yet": primitive_manifest["selected_source_verified"] is False,
        "would_close_dynamic_packet_if_emitted": galerkin_req["would_close_SM_parity_dynamic_packet_if_values_emitted"],
        "observed_flavor_data_forbidden": galerkin_req["observed_flavor_data_forbidden"],
    }
    route_b_required_outputs = galerkin_req["required_outputs"]
    route_b_missing_inputs = {
        key: value is None for key, value in galerkin_req["required_inputs"].items()
    }
    route_b_ready_now = False
    route_b = {
        "schema": "MTTRouteBHonestGalerkinReadinessSidecar.v1",
        "status": "ROUTE_B_READINESS_SIDECAR_BUILT_VALUES_NOT_READY",
        "active_route": "ROUTE-B",
        "support_passed": route_b_support,
        "required_outputs": route_b_required_outputs,
        "missing_selected_inputs": route_b_missing_inputs,
        "readiness_decision": {
            "ready_to_execute_selected_value_run_now": route_b_ready_now,
            "can_replace_route_A_now": False,
            "reason": "The execution contract is precise, but selected zero-mode bases, primitive vertices, basis transport corrections, Hessian counterterms, Gram-Schmidt rule, and source verification are absent.",
        },
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
    }

    labels_after = [
        {
            "id": "PSM-C1-01",
            "status_before": "OPEN_PRIMARY",
            "status_after": "OPEN_PRIMARY_REDUCED_TO_SOURCE_RULE_EMISSION",
            "route": "ROUTE-A",
            "result": "source rule contract and exact conditional replay exist; physical differentiated application is not promoted",
        },
        {
            "id": "PSM-C1-04",
            "status_before": "OPEN_PRIMARY",
            "status_after": "OPEN_PRIMARY_SIDECAR_REQUIRED",
            "route": "ROUTE-A/ROUTE-B",
            "result": "b_selected/source vector is the paired emission required before PSM-C1-05 can be selected",
        },
        {
            "id": "PSM-C1-03",
            "status_before": "OPEN",
            "status_after": "OPEN_DEPENDS_ON_PSM-C1-01_AND_PSM-C1-04",
            "route": "ROUTE-A/ROUTE-B/ROUTE-C",
            "result": "conditional A^T A=12I is available, but A_selected remains unpromoted",
        },
        {
            "id": "PSM-C1-05",
            "status_before": "OPEN_DEPENDS_ON_PSM-C1-03_PSM-C1-04",
            "status_after": "OPEN_CONDITIONAL_VALUE_1_1_NOT_SELECTED",
            "route": "ROUTE-A/ROUTE-B",
            "result": "conditional deltaTheta_C1=[1,1] remains a replay value only",
        },
        {
            "id": "PSM-C1-06",
            "status_before": "OPEN",
            "status_after": "OPEN_REQUIRES_SECTOR_MATRICES_AFTER_SOURCE_VECTOR",
            "route": "ROUTE-A/ROUTE-B/ROUTE-C",
            "result": "sector response matrices are not emitted by selected value source",
        },
    ]

    label_status = {
        "schema": "MTTLabelStatusAfterRouteTest.v1",
        "status": "PSM_C1_01_TESTED_REMAINS_OPEN_LABELS_REFINED",
        "closed_labels_preserved": ["DONE-PARITY-00", "DONE-SOURCE-00", "DONE-DYN-SUPPORT-00"],
        "label_status_after_route_test": labels_after,
        "still_open_labels": [
            "PSM-DYN-01",
            "PSM-C1-01",
            "PSM-C1-02",
            "PSM-C1-03",
            "PSM-C1-04",
            "PSM-C1-05",
            "PSM-C1-06",
            "PSM-S2-01",
            "PSM-QFT-01",
            "PSM-NK-01",
        ],
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
    }

    next_work = {
        "schema": "MTTNextLabeledWorkorderAfterRouteTest.v1",
        "status": "NEXT_WORK_PSM_C1_01_SOURCE_RULE_EMISSION_WITH_PSM_C1_04_SIDECAR",
        "next_required_artifact": NEXT_ARTIFACT,
        "primary_label": "PSM-C1-01",
        "sidecar_label": "PSM-C1-04",
        "primary_route": "ROUTE-A",
        "parallel_route": "ROUTE-B",
        "work_items": [
            {
                "id": "A1a",
                "label": "PSM-C1-01",
                "route": "ROUTE-A",
                "task": "Search for or derive the physical differentiated Phi_fin^C1 source rule applying Q_residual to selected phase/shift legs.",
                "success_condition": "phase_R_Z_selected_now and shift_R_X_selected_now become true without target fitting.",
            },
            {
                "id": "A1b",
                "label": "PSM-C1-04",
                "route": "ROUTE-A",
                "task": "Emit same-source b_selected or Hessian source vector in the fixed 72-real normalization.",
                "success_condition": "b_source_emitted_now becomes true and A^T b is theorem-derived.",
            },
            {
                "id": "B1a",
                "label": "PSM-C1-02",
                "route": "ROUTE-B",
                "task": "Prepare honest Galerkin value run rows: zero-mode bases, primitive 3x3 terms, linear response matrices, and C33/nonzero-family-rank tests.",
                "success_condition": "selected_source_verified becomes true and required outputs are emitted.",
            },
        ],
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
    }

    theorem_proved = (
        active_label_ok
        and all(route_a_support.values())
        and all(route_a_missing.values())
        and all(route_b_support.values())
        and all(route_b_missing_inputs.values())
        and not route_a_closes_psm_c1_01
        and not route_b_ready_now
    )

    candidate = {
        "candidate": "MTTSelectedSameSourceDynamicPhiFinC1OrHonestGalerkinExecutionRouteTest",
        "status": STATUS,
        "inputs": {
            "workbreakdown_matrix": rel(DATA / "selected_postsmparity_workbreakdown_labels" / "remaining_work_status_matrix.packet.json"),
            "route_label_map": rel(DATA / "selected_postsmparity_workbreakdown_labels" / "route_label_map.packet.json"),
            "postsource_frontier": rel(DATA / "selected_dynamicqasu3_or_c1response_postsourcefrontier" / "dynamic_qasu3_c1_frontier.packet.json"),
            "source_map_selection_test": rel(DATA / "selected_sourcemapselectiontheorem_or_honestgalerkinc1valuerun" / "source_map_selection_theorem_test.packet.json"),
            "source_rule_contract": rel(DATA / "selected_differentiatedresidualprojectorsourcerule_or_honestgalerkinc1execution" / "differentiated_residual_projector_source_rule.contract.json"),
            "honest_galerkin_requirement": rel(DATA / "selected_differentiatedresidualprojectorsourcerule_or_honestgalerkinc1execution" / "honest_galerkin_c1_execution_requirement.packet.json"),
        },
        "output_packets": {
            "route_a_psm_c1_01_source_rule_test": rel(ROUTE_A),
            "route_b_honest_galerkin_readiness_sidecar": rel(ROUTE_B),
            "label_status_after_route_test": rel(LABEL_STATUS),
            "next_labeled_workorder": rel(NEXT),
        },
        "theorem": {
            "name": "SameSourceDynamicPhiFinC1RouteTestTheorem",
            "proved": theorem_proved,
            "statement": (
                "For active label PSM-C1-01 on ROUTE-A, the same-source dynamic Phi_fin^C1 source-rule "
                "contract is exact and conditionally sufficient, but current artifacts do not promote the "
                "physical differentiated application of Q_residual, phase/shift residual sources, or b_selected. "
                "ROUTE-B is a valid replacement lane with a fixed 72-real target, but it is not ready because "
                "selected Galerkin inputs and primitive contraction rows remain absent."
            ),
        },
        "what_closes_now": {
            "PSM_C1_01_route_test_completed": True,
            "ROUTE_A_source_rule_gap_sharpened": True,
            "ROUTE_B_readiness_sidecar_built": True,
            "next_labeled_workorder_emitted": True,
        },
        "what_remains_open": {
            "PSM-C1-01": True,
            "PSM-C1-04": True,
            "PSM-C1-03": True,
            "PSM-C1-05": True,
            "PSM-C1-02": True,
            "PSM-C1-06": True,
            "PSM-DYN-01": True,
            "PSM-S2-01": True,
            "PSM-QFT-01": True,
            "PSM-NK-01": True,
        },
        "closure_decision": {
            "PSM-C1-01_closed": False,
            "PSM-C1-04_closed": False,
            "ROUTE_A_closes_now": False,
            "ROUTE_B_ready_now": False,
            "selected_C1_response_closed": False,
            "actual_dynamic_QaSU3_operator_packet_closed": False,
            "true_SM_equivalence_closed": False,
            "no_knob_closed": False,
        },
        "next_required_artifact": NEXT_ARTIFACT,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "closure_claimed": False,
    }

    cert = {
        "certificate": "MTT_Selected_SameSourceDynamicPhiFinC1_or_HonestGalerkinExecution_RouteTest_v1",
        "candidate_path": rel(OUTPUT),
        "status": STATUS,
        "theorem_proved": theorem_proved,
        "active_label": "PSM-C1-01",
        "active_route": "ROUTE-A",
        "sidecar_label": "PSM-C1-04",
        "PSM_C1_01_closed": False,
        "ROUTE_B_ready_now": False,
        "next_required_artifact": NEXT_ARTIFACT,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "note_path": rel(NOTE),
    }

    note = f"""# MTT Selected SameSourceDynamicPhiFinC1 or HonestGalerkinExecution RouteTest v1

Active label: `PSM-C1-01`.

Active route: `ROUTE-A`.

Sidecar label: `PSM-C1-04`.

This artifact tests whether the same-source dynamic `Phi_fin^C1` source rule
already closes `PSM-C1-01`. It does not.

What is now sharp:

- the source-rule contract exists
- canonical `Q_residual` support is selected
- exact conditional replay gives rank 2 and `deltaTheta_C1=[1,1]`
- stationary transport and fixed-fiber shortcuts are ruled out
- physical differentiated application, phase/shift residual sources, and
  `b_selected` are not emitted

`ROUTE-B` remains a valid replacement lane, but it is not ready: selected
zero-mode bases, primitive 3x3 terms, linear response matrices, and
C33/nonzero-family-rank rows are still missing.

Next labels:

- primary: `PSM-C1-01`
- sidecar: `PSM-C1-04`
- replacement readiness: `PSM-C1-02` through `ROUTE-B`

Next artifact: `{NEXT_ARTIFACT}`.
"""

    for path, payload in [
        (ROUTE_A, route_a),
        (ROUTE_B, route_b),
        (LABEL_STATUS, label_status),
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
