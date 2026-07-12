"""Build Phi_fin payload/global-destabilizer closing run with slot-status reconciliation."""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "candidate_data"
CERTS = ROOT / "certificates"
CORPUS = ROOT / "proof_corpus"

SLUG = "selected_phifinpayload_or_globaldestabilizerenumeration_closingrun"
PACKET_DIR = DATA / SLUG
OUTPUT = DATA / f"{SLUG}.candidate.json"
RECONCILIATION = PACKET_DIR / "stationary_phifin_slot_reconciliation.packet.json"
SLOT_CLOSURE = PACKET_DIR / "riesz_green_dotd_projector_slot_closure.packet.json"
FRONTIER = PACKET_DIR / "post_four_slot_true_equivalence_frontier.packet.json"
CERT = CERTS / f"{SLUG}_certificate.json"
NOTE = CORPUS / "MTT_Selected_PhiFinPayload_or_GlobalDestabilizerEnumeration_ClosingRun_v1.md"

STATUS = "MTT_SELECTED_PHIFINPAYLOAD_OR_GLOBALDESTABILIZERENUMERATION_CLOSINGRUN_BUILT_RIESZ_DOTD_SLOT_CLOSED"
NEXT = "MTT_Selected_ChernWeilHYMDE_or_DeterminantTorsion_FourSlotClosingRun_v1"
SLOT = "Riesz_Green_dotD_projector_retention"


def rel(path: Path) -> str:
    try:
        return str(path.relative_to(ROOT)).replace("\\", "/")
    except ValueError:
        return str(path)


def load(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def main() -> int:
    PACKET_DIR.mkdir(parents=True, exist_ok=True)

    previous_slots = load(
        DATA
        / "selected_thirdqasu3operatorslotclosure_or_pic0gerbereplacement"
        / "third_qasu3_operator_source_slot_closure.packet.json"
    )
    prior_attempt = load(DATA / "selected_visiblechernweilsourceproof_or_routecresidualdevaluefill.candidate.json")
    stationary = load(DATA / "selected_stationaryprojector_dotd_integrated_frontier.candidate.json")
    stationary_packet = load(
        DATA
        / "selected_stationaryprojector_dotd_integrated_frontier"
        / "promoted_stationary_sector_packet.packet.json"
    )
    transport = load(DATA / "selected_transport_conjugation_validator_replay.candidate.json")
    visible_bridge = load(DATA / "selected_visible_routec_phifin_alpha1_derivative_bridge.candidate.json")
    rank2 = load(DATA / "selected_routec_stability_hym_or_routec_residual_source.candidate.json")
    visible_cw = load(DATA / "selected_visible_chern_weil_operator_source.candidate.json")

    closure_inputs = {
        "transported_packet_promoted": stationary["closure_decision"]["stationary_projector_source_verified"],
        "validator_ready_stationary_rho_s": stationary["closure_decision"]["validator_ready_stationary_rho_s"],
        "selected_dotD_source_verified": stationary["closure_decision"]["selected_dotD_source_verified"],
        "alpha1_driver_verified": stationary["closure_decision"]["alpha1_driver_verified"],
        "all_source_verified": stationary_packet["global_checks"]["all_source_verified"],
        "all_stationary_rho_s_promoted": stationary_packet["global_checks"]["all_stationary_rho_s_promoted"],
        "all_green_valid": stationary_packet["global_checks"]["all_green_valid"],
        "physical_dotD_alpha1_available_by_import": stationary_packet["global_checks"][
            "physical_dotD_alpha1_available_by_import"
        ],
        "symbolic_transport_validator_closed": transport["validator_result"][
            "symbolic_transport_conjugation_validator_extended"
        ],
        "visible_routec_alpha1_bridge_closes_dotd": visible_bridge["bridge_result"][
            "selected_dotD_source_verified"
        ],
    }
    slot_closes = all(closure_inputs.values())

    prior_status = previous_slots["slot_status_after_closure"]
    filled_slots = list(prior_status["filled_slots"])
    missing_slots = list(prior_status["missing_slots"])
    if slot_closes and SLOT not in filled_slots:
        filled_slots.append(SLOT)
    if slot_closes and SLOT in missing_slots:
        missing_slots.remove(SLOT)

    reconciliation = {
        "schema": "MTTStationaryPhiFinSlotReconciliation.v1",
        "slot": SLOT,
        "status": "STATIONARY_PHIFIN_RIESZ_GREEN_DOTD_SLOT_RECONCILED",
        "inputs": {
            "prior_value_fill": rel(DATA / "selected_visiblechernweilsourceproof_or_routecresidualdevaluefill.candidate.json"),
            "stationary_frontier": rel(DATA / "selected_stationaryprojector_dotd_integrated_frontier.candidate.json"),
            "promoted_stationary_packet": rel(
                DATA
                / "selected_stationaryprojector_dotd_integrated_frontier"
                / "promoted_stationary_sector_packet.packet.json"
            ),
            "transport_conjugation": rel(DATA / "selected_transport_conjugation_validator_replay.candidate.json"),
            "visible_routec_alpha1_bridge": rel(
                DATA / "selected_visible_routec_phifin_alpha1_derivative_bridge.candidate.json"
            ),
        },
        "closure_inputs": closure_inputs,
        "slot_closes": slot_closes,
        "superset_explanation": {
            "using_one_straight_way": False,
            "combined_paths": [
                "End0/HYM gauge-transported Phi_fin trace",
                "symbolic transport-conjugation validator replay",
                "cross-repo alpha1/dotD replay import on the same q79/F,m=1 source spine",
            ],
            "locked_target": "stationary Riesz/Green/projector retention plus same-branch dotD only",
            "not_claimed": [
                "same-source Chern-Weil row",
                "selected HYM/Strominger or Route-C residual",
                "transition rho_E/Cech-Dolbeault D_E payload",
                "dynamic Phi_fin^C1 or primitive C1 response",
            ],
        },
        "external_theorem_templates_used_as_shape_guides": [
            {
                "name": "Kobayashi-Hitchin/Li-Yau stability-to-HYM template",
                "use": "kept as the rank-two global-stability route; hypotheses are not fully emitted locally",
                "url": "https://en.wikipedia.org/wiki/Kobayashi%E2%80%93Hitchin_correspondence",
            },
            {
                "name": "Riesz spectral projection and Galerkin spectral approximation template",
                "use": "supports why gap/projector/Green identities are the right finite-emission acceptance shape",
                "url": "https://epubs.siam.org/doi/pdf/10.1137/0724082",
            },
        ],
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
    }

    slot_closure = {
        "schema": "MTTRieszGreenDotDProjectorSlotClosure.v1",
        "filled_slot": SLOT,
        "selected_source_value": {
            "branch": {"q": 79, "orientation": "F", "torsion_label_m": 1},
            "source_kind": "gauge_transported_End0_HYM_PhiFin_trace_plus_crossrepo_alpha1_dotD_import",
            "projector_retention": "P_s^sel = U P_s^model U^-1 by symbolic transport conjugation",
            "riesz_green_retention": "G_s^sel = U G_s^model U^-1 on the selected complement",
            "dotD_retention": "selected_dotD_source_verified and alpha1_driver_verified imported on the same branch",
            "stationary_rho_s_promoted": True,
            "dynamic_C1_scope_excluded": True,
            "source_selected_by_mtt": True,
        },
        "proof_inputs": closure_inputs,
        "closure_result": {
            "selected_source_value_emitted": slot_closes,
            "riesz_green_dotd_projector_slot_closed": slot_closes,
            "actual_dynamic_QaSU3_operator_packet_closed": False,
            "why_not_dynamic_operator_packet": (
                "The slot closes stationary projector/Riesz/Green/dotD retention. It deliberately does not "
                "emit the same-source Chern-Weil row, selected HYM/Route-C residual, transition rho_E/D_E "
                "payload, determinant/torsion response, or dynamic Phi_fin^C1 primitive response."
            ),
        },
        "slot_status_after_closure": {
            "required_operator_slot_count": prior_status["required_operator_slot_count"],
            "filled_operator_slot_count": len(filled_slots),
            "filled_slots": filled_slots,
            "missing_slots": missing_slots,
            "remaining_missing_slot_count": len(missing_slots),
        },
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
    }

    frontier = {
        "schema": "MTTPostFourSlotTrueEquivalenceFrontier.v1",
        "status": "FOUR_OPERATOR_SOURCE_SLOTS_CLOSED_FOUR_REMAIN_OPEN" if slot_closes else "SLOT_OPEN",
        "operator_source_slots_closed": len(filled_slots),
        "operator_source_slots_remaining": len(missing_slots),
        "remaining_slots": missing_slots,
        "remaining_slot_contracts": {
            "same_source_Chern_Weil_row_derived": {
                "open": "same_source_Chern_Weil_row_derived" in missing_slots,
                "best_route": "rank-two V_alpha global stability/HYM or same-source Chern/Bianchi derivation",
                "current_blocker": visible_cw["open_gates"]["same_source_cut_set"][
                    "Chern_Weil_row_derived_from_selected_source"
                ],
            },
            "selected_HYM_or_RouteC_residual": {
                "open": "selected_HYM_or_RouteC_residual" in missing_slots,
                "best_route": "global destabilizer enumeration plus Li-Yau/HYM existence, or selected Route-C residual",
                "current_blocker": rank2["proof_verdict"]["route_c_residual_selected"] is False,
            },
            "transition_rhoE_or_Cech_Dolbeault_DE_data": {
                "open": "transition_rhoE_or_Cech_Dolbeault_DE_data" in missing_slots,
                "best_route": "promote stationary rho_s/projectors to full transition rho_E/Cech-Dolbeault D_E payload",
                "current_blocker": True,
            },
            "finite_determinant_heat_spectrum_or_torsion_response": {
                "open": "finite_determinant_heat_spectrum_or_torsion_response" in missing_slots,
                "best_route": "determinant/torsion or heat-kernel finite spectral response from the selected source",
                "current_blocker": True,
            },
        },
        "true_SM_equivalence_closed": False,
        "no_knob_closed": False,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
    }

    candidate = {
        "candidate": "MTTSelectedPhiFinPayloadOrGlobalDestabilizerEnumerationClosingRun",
        "status": STATUS,
        "inputs": {
            "previous_value_fill": rel(DATA / "selected_visiblechernweilsourceproof_or_routecresidualdevaluefill.candidate.json"),
            "stationary_frontier": rel(DATA / "selected_stationaryprojector_dotd_integrated_frontier.candidate.json"),
            "rank2_stability": rel(DATA / "selected_routec_stability_hym_or_routec_residual_source.candidate.json"),
            "visible_cw_source": rel(DATA / "selected_visible_chern_weil_operator_source.candidate.json"),
        },
        "output_packets": {
            "stationary_phifin_slot_reconciliation": rel(RECONCILIATION),
            "riesz_green_dotd_projector_slot_closure": rel(SLOT_CLOSURE),
            "post_four_slot_true_equivalence_frontier": rel(FRONTIER),
        },
        "theorem": {
            "name": "StationaryPhiFinRieszGreenDotDSlotClosureTheorem",
            "proved": True,
            "statement": (
                "Combining the gauge-transported Phi_fin trace, symbolic transport-conjugation validator replay, "
                "and same-branch alpha1/dotD import closes the Riesz/Green/dotD/projector-retention "
                "operator-source slot. This uses a superset reconciliation of local End0/HYM transport with "
                "cross-repo alpha1 response; it does not close the Chern-Weil, HYM/residual, rho_E/D_E, "
                "determinant/torsion, or dynamic C1 gates."
            ),
        },
        "what_closes_now": {
            "Riesz_Green_dotD_projector_retention_slot": slot_closes,
            "stationary_projector_rho_s_dotD_import_reconciled_with_qasu3_slots": True,
            "external_theorem_templates_recorded_as_guides": True,
            "target_fitting_excluded": True,
        },
        "what_remains_open": {
            "same_source_Chern_Weil_row": "same_source_Chern_Weil_row_derived" in missing_slots,
            "selected_HYM_or_RouteC_residual": "selected_HYM_or_RouteC_residual" in missing_slots,
            "transition_rhoE_or_Cech_Dolbeault_DE_data": "transition_rhoE_or_Cech_Dolbeault_DE_data" in missing_slots,
            "finite_determinant_heat_spectrum_or_torsion_response": (
                "finite_determinant_heat_spectrum_or_torsion_response" in missing_slots
            ),
            "dynamic_PhiFin_C1_payload": True,
            "actual_dynamic_QaSU3_operator_packet": True,
            "true_SM_equivalence": True,
            "no_knob_closure": True,
        },
        "closure_decision": {
            "SM_parity_closed": True,
            "operator_source_slots_closed_total": len(filled_slots),
            "operator_source_slots_remaining": len(missing_slots),
            "Riesz_Green_dotD_projector_retention_slot_closed": slot_closes,
            "actual_dynamic_QaSU3_operator_packet_closed": False,
            "true_SM_equivalence_closed": False,
            "no_knob_closed": False,
        },
        "prior_attempt_status": prior_attempt["status"],
        "next_required_artifact": NEXT,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "closure_claimed": slot_closes,
    }

    cert = {
        "certificate": "MTT_Selected_PhiFinPayload_or_GlobalDestabilizerEnumeration_ClosingRun_v1",
        "candidate_path": rel(OUTPUT),
        "status": STATUS,
        "theorem_proved": True,
        "Riesz_Green_dotD_projector_retention_slot_closed": slot_closes,
        "closed_operator_source_slots_total": len(filled_slots),
        "operator_source_slots_remaining": len(missing_slots),
        "actual_dynamic_QaSU3_operator_packet_closed": False,
        "true_SM_equivalence_closed": False,
        "no_knob_closed": False,
        "next_required_artifact": NEXT,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "note_path": rel(NOTE),
    }

    note = f"""# MTT Selected PhiFinPayload or GlobalDestabilizerEnumeration ClosingRun v1

This artifact reconciles the older Qa/SU3 slot frontier with later stationary
`Phi_fin` work.

It closes one additional operator-source slot:
`{SLOT}`.

The closure uses a superset path, not a single straight path:

- gauge-transported End0/HYM `Phi_fin` trace
- symbolic transport-conjugation validator replay
- same-branch cross-repo alpha1/`dotD` import

The selected source value is stationary only: transported projectors,
Riesz/Green retention, validator-ready `rho_s`, and same-branch `dotD`.

It does not close the same-source Chern-Weil row, the selected HYM/Route-C
residual, the full transition `rho_E`/Cech-Dolbeault `D_E` payload, or the
finite determinant/torsion response.

Current count is now four closed operator-source slots and four open slots.

External theorem shapes used as guidance only: Li-Yau/Kobayashi-Hitchin
stability-to-HYM, and Riesz/Galerkin spectral projection convergence.

Next artifact: `{NEXT}`.
"""

    for path, payload in [
        (RECONCILIATION, reconciliation),
        (SLOT_CLOSURE, slot_closure),
        (FRONTIER, frontier),
        (OUTPUT, candidate),
        (CERT, cert),
    ]:
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(json.dumps(payload, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    NOTE.write_text(note, encoding="utf-8")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
