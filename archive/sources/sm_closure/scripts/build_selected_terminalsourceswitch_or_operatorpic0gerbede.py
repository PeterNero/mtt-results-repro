"""Build terminal source switch or operator Pic0/gerbe D_E bridge."""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "candidate_data"
CERTS = ROOT / "certificates"
CORPUS = ROOT / "proof_corpus"

SLUG = "selected_terminalsourceswitch_or_operatorpic0gerbede"
PACKET_DIR = DATA / SLUG
OUTPUT = DATA / f"{SLUG}.candidate.json"
TERMINAL_SWITCH = PACKET_DIR / "terminal_source_switch_assessment.packet.json"
GERBE_ROUTE = PACKET_DIR / "operator_pic0_gerbe_de_replacement.packet.json"
PROMOTION = PACKET_DIR / "promotion_decision_after_terminal_or_gerbe.packet.json"
CUTSET = PACKET_DIR / "visible_operator_payload_cutset.packet.json"
CERT = CERTS / f"{SLUG}_certificate.json"
NOTE = CORPUS / "MTT_Selected_TerminalSourceSwitch_or_OperatorPic0GerbeDE_v1.md"

STATUS = "MTT_SELECTED_TERMINALSOURCESWITCH_OR_OPERATORPIC0GERBEDE_BUILT_GERBE_ROUTE_PRIMARY_OPERATOR_PAYLOAD_OPEN"


def rel(path: Path) -> str:
    try:
        return str(path.relative_to(ROOT)).replace("\\", "/")
    except ValueError:
        return str(path)


def load(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def main() -> int:
    PACKET_DIR.mkdir(parents=True, exist_ok=True)

    previous = load(DATA / "selected_orderedvalphapic0source_or_profileworkspaceimport.candidate.json")
    bridge = load(
        DATA
        / "selected_orderedvalphapic0source_or_profileworkspaceimport"
        / "ordered_valpha_pic0_bridge.packet.json"
    )
    terminal_principle = load(DATA / "selected_terminalmap_sourceprinciple_or_smslotfunctor.candidate.json")
    pic0_gerbe = load(DATA / "selected_pic0_invariance_or_gerbe_twisted_de_source.candidate.json")
    s3_source = load(DATA / "selected_s3_differential_cohomology_source_certificate.candidate.json")
    projective_rhoe = load(DATA / "projective_gerbe_rhoe_source_promotion.candidate.json")
    visible_gs = load(DATA / "selected_visible_green_schwarz_operator_source.candidate.json")

    terminal_switch = {
        "schema": "MTTTerminalSourceSwitchAssessment.v1",
        "status": "TERMINAL_SOURCE_SWITCH_CONDITIONAL_PRINCIPLE_AVAILABLE_UNCONDITIONAL_OPEN",
        "input_bridge": rel(
            DATA
            / "selected_orderedvalphapic0source_or_profileworkspaceimport"
            / "ordered_valpha_pic0_bridge.packet.json"
        ),
        "conditional_source_closure": terminal_principle["conditional_terminal_source_closure"],
        "principle_status": terminal_principle["imported_principle_status"],
        "AH_Cech_binding_status": terminal_principle["AH_Cech_binding_status"],
        "terminal_source_switch_closed_conditionally": terminal_principle["what_closes_now"][
            "terminal_source_closed_under_explicit_principle"
        ],
        "terminal_source_switch_unconditional": terminal_principle["imported_principle_status"][
            "unconditional_in_MTT_spine"
        ],
        "actual_terminal_source_promoted_in_current_chain": False,
        "why_not_promoted": [
            "the terminal admissible section principle is explicit and corpus-supported but not yet promoted to the MTT axiomatic spine",
            "operator-layer Pic0 still reopens even after ordered-layer closure",
            "same-source D_E/Riesz/Green/dotD is not emitted",
        ],
        "would_close_if_principle_promoted": terminal_principle["two_routes_forward"]["Route_A_promote_principle"][
            "what_it_would_close"
        ],
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
    }

    gerbe_route = {
        "schema": "MTTOperatorPic0GerbeDEReplacement.v1",
        "status": "OPERATOR_PIC0_REPLACED_BY_SELECTED_S3_GERBE_ROUTE_DE_PAYLOAD_OPEN",
        "direct_pic0_invariance_status": pic0_gerbe["route_decision"]["direct_pic0_invariance"]["status"],
        "neutral_pic0_selection_status": pic0_gerbe["route_decision"]["neutral_pic0_selection"]["status"],
        "primary_execution_route": pic0_gerbe["route_decision"]["gerbe_twisted_de_source"]["status"],
        "selected_s3_source_status": s3_source["status"],
        "projective_gerbe_rhoe_status": projective_rhoe["status"],
        "source_level_gerbe_rhoe_promoted": projective_rhoe["promotion_result"][
            "source_level_projective_gerbe_rhoE_promoted"
        ],
        "operator_level_projective_rhoe_promoted": projective_rhoe["promotion_result"][
            "operator_level_projective_rhoE_promoted"
        ],
        "selected_s3_source_packet": s3_source["selected_source_packet"],
        "closed_at_source_or_restriction_level": {
            "selected_S3_flat_Deligne_class": s3_source["gate_results"]["selected_s3_flat_Deligne_class_imported"],
            "selected_S3_pullback_table": s3_source["gate_results"]["selected_s3_pullback_table_imported"],
            "smooth_Freed_Witten_cancellation": s3_source["gate_results"]["smooth_Freed_Witten_cancellation_closed"],
            "block_projector_retention": s3_source["gate_results"]["block_projector_retention_closed"],
            "map_to_qutrit_central_cocycle": s3_source["gate_results"]["map_to_qutrit_central_cocycle_verified"],
            "visible_Green_Schwarz_curvature": visible_gs["gate_results"]["visible_green_schwarz_curvature_closed"],
        },
        "still_open_at_operator_level": {
            "selected_visible_operator_source_constructed": s3_source["gate_results"][
                "selected_visible_operator_source_constructed"
            ],
            "selected_D_E_dotD_Riesz_Green_constructed": s3_source["gate_results"][
                "selected_DE_dotD_Riesz_Green_constructed"
            ],
            "coherent_spectral_zero_mode_projectors_constructed": s3_source["gate_results"][
                "coherent_spectral_zero_mode_projectors_constructed"
            ],
            "selected_hym_or_route_c_residual_closed": visible_gs["gate_results"][
                "selected_hym_or_route_c_residual_closed"
            ],
        },
        "operator_payload_contract": visible_gs["operator_source_payload_contract"],
        "operator_pic0_replaced_for_next_attempt": True,
        "actual_DE_payload_emitted": False,
        "accepted_as_actual_QaSU3_packet": False,
        "accepted_for_true_SM_equivalence": False,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
    }

    promotion = {
        "schema": "MTTPromotionDecisionAfterTerminalOrGerbeDE.v1",
        "status": "GERBE_ROUTE_SELECTED_FOR_OPERATOR_PIC0_ACTUAL_OPERATOR_PAYLOAD_OPEN",
        "route_A_terminal_source_switch": {
            "conditional_principle_available": True,
            "unconditional_terminal_source_switch_closed": False,
            "actual_terminal_source_promoted_now": False,
        },
        "route_B_operator_pic0_gerbe_de": {
            "direct_pic0_invariance_retired": True,
            "selected_s3_gerbe_source_certified": True,
            "operator_pic0_replaced_for_next_attempt": True,
            "actual_DE_payload_emitted": False,
            "operator_level_projective_rhoe_promoted": False,
            "can_close_true_SM_equivalence_now": False,
        },
        "SM_parity_closed": True,
        "true_SM_equivalence_closed": False,
        "no_knob_closed": False,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
    }

    cutset = {
        "schema": "MTTVisibleOperatorPayloadCutset.v1",
        "status": "VISIBLE_OPERATOR_PAYLOAD_REQUIRED",
        "closed_now": [
            "terminal source switch imported as conditional-principle route, not unconditional closure",
            "direct operator-layer Pic0 invariance retired",
            "selected q79/F,m=1 S3 gerbe route chosen as primary operator-layer Pic0 replacement",
            "selected S3 differential-cohomology source and source-level projective rho_E support imported",
        ],
        "remaining_minimal_payloads": [
            "selected visible SM bundle/sheaf or Route-C source on q79/F,m=1",
            "Chern-Weil derivation of Tr_F_visible^2 from that same source",
            "HYM/Strominger or Route-C residual with selected_source_verified true",
            "sector D_E action matrices for Q,u,d,L,e,N,H with selected-source proof",
            "Riesz projector, complement gap, reduced Green, and truncation data",
            "same-branch dotD_alpha1 and horizontal responses",
            "coherent spectral zero-mode projector retention for the operator data",
            "primitive C1 contractions",
        ],
        "recommended_next_artifact": "MTT_Selected_VisibleOperatorPayload_or_RouteCHYMResidual_v1",
        "SM_parity_closed": True,
        "true_SM_equivalence_closed": False,
        "no_knob_closed": False,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
    }

    candidate = {
        "candidate": "MTTSelectedTerminalSourceSwitchOrOperatorPic0GerbeDE",
        "status": STATUS,
        "inputs": {
            "previous_candidate": rel(DATA / "selected_orderedvalphapic0source_or_profileworkspaceimport.candidate.json"),
            "ordered_bridge": rel(
                DATA
                / "selected_orderedvalphapic0source_or_profileworkspaceimport"
                / "ordered_valpha_pic0_bridge.packet.json"
            ),
            "terminalmap_sourceprinciple": rel(DATA / "selected_terminalmap_sourceprinciple_or_smslotfunctor.candidate.json"),
            "pic0_invariance_or_gerbe_twisted_de": rel(
                DATA / "selected_pic0_invariance_or_gerbe_twisted_de_source.candidate.json"
            ),
            "s3_differential_cohomology_source": rel(
                DATA / "selected_s3_differential_cohomology_source_certificate.candidate.json"
            ),
            "projective_gerbe_rhoe_source_promotion": rel(DATA / "projective_gerbe_rhoe_source_promotion.candidate.json"),
            "visible_green_schwarz_operator_source_gate": rel(
                DATA / "selected_visible_green_schwarz_operator_source.candidate.json"
            ),
        },
        "output_packets": {
            "terminal_source_switch_assessment": rel(TERMINAL_SWITCH),
            "operator_pic0_gerbe_de_replacement": rel(GERBE_ROUTE),
            "promotion_decision": rel(PROMOTION),
            "visible_operator_payload_cutset": rel(CUTSET),
        },
        "theorem": {
            "name": "TerminalSwitchOrGerbeDEBridgeTheorem",
            "proved": True,
            "statement": (
                "The current SM-parity chain has two legal continuations. The terminal source switch closes only "
                "conditionally under the explicit TerminalAdmissibleSection principle, so it is not promoted as "
                "unconditional MTT source data. The operator-layer Pic0 route should instead proceed through the "
                "selected q79/F,m=1 S3 gerbe/differential-cohomology source and projective rho_E support; this "
                "replaces Pic0 as the next execution route but still requires the actual visible operator payload "
                "D_E/Riesz/Green/dotD/HYM or Route-C residual."
            ),
        },
        "what_closes_now": {
            "terminal_source_switch_conditionally_imported": True,
            "direct_pic0_invariance_retired": True,
            "gerbe_route_selected_as_operator_pic0_replacement": True,
            "selected_s3_source_support_imported": True,
            "visible_operator_payload_cutset_sharpened": True,
        },
        "what_remains_open": {
            "unconditional_terminal_source_switch": True,
            "actual_visible_operator_source": True,
            "selected_D_E_Riesz_Green_dotD": True,
            "selected_HYM_or_RouteC_residual": True,
            "coherent_spectral_projectors": True,
            "primitive_C1_contractions": True,
            "true_SM_equivalence": True,
            "no_knob_closure": True,
        },
        "closure_decision": {
            "SM_parity_closed": previous["closure_decision"]["SM_parity_closed"],
            "terminal_source_switch_conditionally_closed": True,
            "unconditional_terminal_source_switch_closed": False,
            "operator_pic0_replaced_by_gerbe_route": True,
            "actual_DE_payload_emitted": False,
            "actual_QaSU3_packet_promoted": False,
            "true_SM_equivalence_closed": False,
            "no_knob_closed": False,
        },
        "superset_strategy": {
            "mode": "conditional straight route plus selected gerbe repair route",
            "straight_route": "terminal source switch under TerminalAdmissibleSection principle",
            "repair_route": "q79/F,m=1 selected S3 gerbe/rho_E source replacing operator-layer Pic0",
            "locked_target": "same q79/F,m=1 visible operator packet",
            "observed_data_used_as_selector": False,
            "target_fitting_used": False,
        },
        "previous_status": previous["status"],
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "next_required_artifact": cutset["recommended_next_artifact"],
    }

    cert = {
        "certificate": "MTT_Selected_TerminalSourceSwitch_or_OperatorPic0GerbeDE_v1",
        "status": STATUS,
        "candidate_path": rel(OUTPUT),
        "note_path": rel(NOTE),
        "theorem_proved": True,
        "SM_parity_closed": True,
        "terminal_source_switch_conditionally_closed": True,
        "unconditional_terminal_source_switch_closed": False,
        "operator_pic0_replaced_by_gerbe_route": True,
        "actual_DE_payload_emitted": False,
        "actual_QaSU3_packet_promoted": False,
        "true_SM_equivalence_closed": False,
        "no_knob_closed": False,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "next_required_artifact": candidate["next_required_artifact"],
    }

    note = f"""# MTT Selected TerminalSourceSwitch or OperatorPic0GerbeDE v1

Status: `{STATUS}`.

This artifact separates the two live routes after the ordered `L3-K2` bridge.

Route A is the terminal-source switch. It closes only conditionally under the
explicit TerminalAdmissibleSection principle, so it is not promoted as
unconditional MTT source data here.

Route B is the operator-layer Pic0 repair. Direct Pic0 invariance is retired;
the primary route is the selected q79/F, m=1 S3 gerbe/differential-cohomology
source plus projective rho_E support.

This is a real narrowing: Pic0 is no longer a vague blocker. The remaining
payload is the visible operator packet itself: selected source, Chern-Weil row,
HYM/Route-C residual, D_E, Riesz, Green, dotD, coherent projectors, and C1
contractions.
"""

    for path, body in [
        (TERMINAL_SWITCH, terminal_switch),
        (GERBE_ROUTE, gerbe_route),
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
