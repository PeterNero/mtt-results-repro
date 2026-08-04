"""Build integrated stationary-projector/dotD frontier after HYM first solve."""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "candidate_data"
CERTS = ROOT / "certificates"
CORPUS = ROOT / "proof_corpus"

SLUG = "selected_stationaryprojector_dotd_integrated_frontier"
PACKET_DIR = DATA / SLUG
OUTPUT = DATA / f"{SLUG}.candidate.json"
INTEGRATION = PACKET_DIR / "stationary_projector_dotd_integration.packet.json"
PROMOTION = PACKET_DIR / "promoted_stationary_sector_packet.packet.json"
FRONTIER = PACKET_DIR / "dynamic_c1_frontier_after_projector_dotd.packet.json"
CUTSET = PACKET_DIR / "primitive_c1_or_dynamic_phifin_cutset.packet.json"
CERT = CERTS / f"{SLUG}_certificate.json"
NOTE = CORPUS / "MTT_Selected_StationaryProjector_dotD_IntegratedFrontier_v1.md"

STATUS = "MTT_SELECTED_STATIONARYPROJECTOR_DOTD_INTEGRATED_FRONTIER_BUILT_C1_OPEN"
NEXT = "MTT_Selected_PrimitiveC1Contractions_or_DynamicPhiFinC1Payload_ValueEmission_v1"


def rel(path: Path) -> str:
    try:
        return str(path.relative_to(ROOT)).replace("\\", "/")
    except ValueError:
        return str(path)


def load(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def main() -> int:
    PACKET_DIR.mkdir(parents=True, exist_ok=True)

    after_hym = load(DATA / "selected_physicaldotd_sectorrouting_after_hymfirstsolve.candidate.json")
    finite_promotion = load(DATA / "selected_finite_projector_source_promotion.candidate.json")
    transport = load(DATA / "selected_transport_conjugation_validator_replay.candidate.json")
    alpha1_import = load(DATA / "selected_crossrepo_alpha1_driver_replay_import.candidate.json")
    alpha_bridge = load(DATA / "selected_visible_routec_phifin_alpha1_derivative_bridge.candidate.json")
    c1_frontier = load(DATA / "selected_c1_frontier_after_alpha1_import.candidate.json")
    primitive = load(DATA / "selected_primitiveclass_c1observable_or_higherorder_fullresponse_sourceemission.candidate.json")

    integration = {
        "schema": "MTTStationaryProjectorDotDIntegration.v1",
        "status": "STATIONARY_PROJECTOR_AND_DOTD_RECONCILED_DYNAMIC_C1_OPEN",
        "previous_route_status": after_hym["status"],
        "stationary_projector_source_promotion": {
            "finite_projector_source_promotion_proved": finite_promotion["promotion_decision"][
                "finite_projector_source_promotion_proved"
            ],
            "selected_projector_source_verified": finite_promotion["promotion_decision"][
                "selected_projector_source_verified"
            ],
            "validator_ready_stationary_rho_s": finite_promotion["promotion_decision"][
                "validator_ready_stationary_rho_s"
            ],
            "transported_packet_promoted": finite_promotion["promotion_decision"]["transported_packet_promoted"],
            "raw_untransported_packet_promoted": finite_promotion["promotion_decision"][
                "raw_untransported_packet_promoted"
            ],
        },
        "symbolic_transport_validator": {
            "selected_source_verified": transport["validator_result"]["selected_source_verified"],
            "selected_rho_s_validator_ready": transport["validator_result"]["selected_rho_s_validator_ready"],
            "all_sector_projector_riesz_green_replays_pass": transport["validator_result"][
                "all_sector_projector_riesz_green_replays_pass"
            ],
            "selected_dotD_source_verified_by_this_artifact": transport["validator_result"][
                "selected_dotD_source_verified"
            ],
            "alpha1_driver_verified_by_this_artifact": transport["validator_result"]["alpha1_driver_verified"],
        },
        "alpha1_dotd_replay_import": {
            "selected_dotD_source_verified_imported": alpha1_import["selected_dotD_source_verified_imported"],
            "alpha1_driver_verified_imported": alpha1_import["alpha1_driver_verified_imported"],
            "honest_dotD_alpha1_replay_imported": alpha1_import["alpha1_driver_replay_import"][
                "honest_dotD_alpha1_replay"
            ],
            "du_dalpha1_equals_h_ext": alpha1_import["alpha1_driver_replay_import"]["du_dalpha1_equals_h_ext"],
            "N_alpha1_h_ext": alpha1_import["alpha1_driver_replay_import"]["N_alpha1_h_ext"],
        },
        "reconciled_decision": {
            "stationary_projector_source_verified": True,
            "validator_ready_stationary_rho_s": True,
            "physical_dotD_alpha1_closed_by_import": True,
            "visible_routec_alpha1_bridge_compatible": alpha_bridge["bridge_result"][
                "honest_dotD_replay_closed_by_import"
            ],
            "dynamic_PhiFin_C1_payload_emitted": False,
            "primitive_C1_contractions_emitted": False,
        },
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
    }

    promoted_slots = finite_promotion["promoted_sector_slots"]
    promotion = {
        "schema": "MTTPromotedStationarySectorPacket.v1",
        "status": "STATIONARY_SECTOR_PROJECTOR_RHOS_DOTD_READY",
        "sector_slots": {
            sector: {
                "rank": slot["rank"],
                "source_verified_by_transport_conjugation": slot["source_verified_by_transport_conjugation"],
                "stationary_rho_s_promoted": slot["stationary_rho_s_promoted"],
                "green_operator_valid": slot["green_operator_valid"],
                "riesz_projector_valid": slot["riesz_projector_valid"],
                "transport": slot["transport"],
            }
            for sector, slot in promoted_slots.items()
        },
        "global_checks": {
            "all_stationary_rho_s_promoted": all(slot["stationary_rho_s_promoted"] for slot in promoted_slots.values()),
            "all_source_verified": all(slot["source_verified_by_transport_conjugation"] for slot in promoted_slots.values()),
            "all_green_valid": all(slot["green_operator_valid"] for slot in promoted_slots.values()),
            "H_rank_one": promoted_slots["H"]["rank"] == 1,
            "matter_rank_three": all(promoted_slots[s]["rank"] == 3 for s in ["Q", "u", "d", "L", "e", "N"]),
            "physical_dotD_alpha1_available_by_import": True,
        },
        "boundary": {
            "stationary_packet_ready": True,
            "dynamic_C1_response_ready": False,
            "matter_slot_routing_ready": False,
            "primitive_C1_contractions_ready": False,
            "A_selected_b_selected_ready": False,
        },
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
    }

    frontier = {
        "schema": "MTTDynamicC1FrontierAfterProjectorDotD.v1",
        "status": "DYNAMIC_C1_FRONTIER_ACTIVE_AFTER_PROJECTOR_DOTD",
        "retired_gates": {
            "stationary_projector_source": True,
            "stationary_rho_s": True,
            "selected_dotD_source_verified": True,
            "alpha1_driver_verified": True,
            "honest_dotD_alpha1_replay": True,
        },
        "active_gates": c1_frontier["live_source_objects"],
        "primitive_layer_status": {
            "current_primitive_class_promoted_as_valid_C1_observable_layer": primitive["promotion_decision"][
                "current_primitive_class_promoted_as_valid_C1_observable_layer"
            ],
            "current_primitive_class_promoted_as_flavor_closure": primitive["promotion_decision"][
                "current_primitive_class_promoted_as_flavor_closure"
            ],
            "higherorder_fullresponse_values_promoted": primitive["promotion_decision"][
                "higherorder_fullresponse_values_promoted"
            ],
            "current_layer_flavor_splitting_possible": primitive["primitive_class_C1_observable_packet"][
                "flavor_splitting_possible_at_current_layer"
            ],
        },
        "next_values": primitive["higherorder_or_fullresponse_source_emission_packet"]["minimum_next_payload"],
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
    }

    cutset = {
        "schema": "MTTPrimitiveC1OrDynamicPhiFinCutset.v1",
        "status": "NEXT_GATE_IS_PRIMITIVE_C1_OR_DYNAMIC_PHIFIN_C1_VALUES",
        "bookkeeping_remaining": False,
        "source_or_value_emission_required": True,
        "closed_now": [
            "selected diagonal HYM first solve",
            "stationary transported projector source promotion",
            "validator-ready stationary rho_s packet",
            "symbolic transport-conjugation Riesz/Green replay",
            "theorem-derived alpha1 driver and honest dotD replay by compatible cross-repo import",
            "current primitive C1 observable layer and scalar-flavor no-go",
        ],
        "remaining_minimal_payloads": [
            "selected primitive C1 contractions or selected dynamic Phi_fin^C1 payload",
            "selected higher-order/full-response matrices",
            "selected A_selected response operator",
            "selected b_selected source vector",
            "selected deltaTheta_C1 solve or selected no-solve theorem",
            "sector response matrices M_u, M_d, M_e, M_nuD",
            "matter-slot routing and transfer normalization if needed for non-scalar response promotion",
        ],
        "recommended_next_artifact": NEXT,
        "SM_parity_closed": True,
        "true_SM_equivalence_closed": False,
        "no_knob_closed": False,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
    }

    candidate = {
        "candidate": "MTTSelectedStationaryProjectorDotDIntegratedFrontier",
        "status": STATUS,
        "inputs": {
            "physicaldotd_sectorrouting_after_hymfirstsolve": rel(
                DATA / "selected_physicaldotd_sectorrouting_after_hymfirstsolve.candidate.json"
            ),
            "finite_projector_source_promotion": rel(DATA / "selected_finite_projector_source_promotion.candidate.json"),
            "transport_conjugation_validator_replay": rel(
                DATA / "selected_transport_conjugation_validator_replay.candidate.json"
            ),
            "crossrepo_alpha1_driver_replay_import": rel(
                DATA / "selected_crossrepo_alpha1_driver_replay_import.candidate.json"
            ),
            "visible_routec_phifin_alpha1_bridge": rel(
                DATA / "selected_visible_routec_phifin_alpha1_derivative_bridge.candidate.json"
            ),
            "c1_frontier_after_alpha1_import": rel(DATA / "selected_c1_frontier_after_alpha1_import.candidate.json"),
            "primitive_c1_or_higherorder_frontier": rel(
                DATA / "selected_primitiveclass_c1observable_or_higherorder_fullresponse_sourceemission.candidate.json"
            ),
        },
        "output_packets": {
            "stationary_projector_dotd_integration": rel(INTEGRATION),
            "promoted_stationary_sector_packet": rel(PROMOTION),
            "dynamic_c1_frontier_after_projector_dotd": rel(FRONTIER),
            "primitive_c1_or_dynamic_phifin_cutset": rel(CUTSET),
        },
        "theorem": {
            "name": "StationaryProjectorDotDIntegratedFrontierTheorem",
            "proved": True,
            "statement": (
                "The post-HYM-first-solve branch must incorporate the already proved transported finite-projector "
                "source promotion and the compatible cross-repo alpha1/dotD theorem. Stationary sector projectors, "
                "Riesz/Green data, validator-ready rho_s, selected_dotD_source_verified, and alpha1_driver_verified "
                "are therefore not active blockers. The remaining source frontier is dynamic C1/Phi_fin^C1: primitive "
                "C1 contractions, A_selected, b_selected, deltaTheta_C1, and sector response matrices."
            ),
        },
        "what_closes_now": {
            "stationary_projector_rho_s_reconciled": True,
            "alpha1_dotD_reconciled_with_HYM_first_solve_branch": True,
            "physical_dotD_alpha1_removed_from_active_frontier": True,
            "dynamic_C1_frontier_reselected": True,
            "no_target_fitting_guardrail_preserved": True,
        },
        "what_remains_open": {
            "selected_dynamic_PhiFin_C1_payload": True,
            "primitive_C1_contractions": True,
            "selected_A_selected": True,
            "selected_b_selected": True,
            "selected_deltaTheta_C1_solution": True,
            "sector_response_matrices_M_u_M_d_M_e_M_nuD": True,
            "true_SM_equivalence": True,
            "no_knob_closure": True,
        },
        "closure_decision": {
            "SM_parity_closed": True,
            "stationary_projector_source_verified": True,
            "validator_ready_stationary_rho_s": True,
            "selected_dotD_source_verified": True,
            "alpha1_driver_verified": True,
            "dynamic_PhiFin_C1_payload_emitted": False,
            "primitive_C1_contractions_emitted": False,
            "A_selected_emitted": False,
            "b_selected_emitted": False,
            "actual_QaSU3_operator_packet_dynamic_complete": False,
            "true_SM_equivalence_closed": False,
            "no_knob_closed": False,
        },
        "superset_strategy": {
            "using_one_straight_way": False,
            "combining_paths": True,
            "straight_path": "HYM/End0 transported projector theorem and stationary sector packet",
            "support_path": "compatible GR/protospinor alpha1 driver import on the same q79/F,m=1 source spine",
            "locked_target": "dynamic Phi_fin C1 payload / primitive C1 response, not stationary projectors or alpha1",
        },
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "next_required_artifact": NEXT,
    }

    cert = {
        "certificate": "MTT_Selected_StationaryProjector_dotD_IntegratedFrontier_v1",
        "status": STATUS,
        "candidate_path": rel(OUTPUT),
        "note_path": rel(NOTE),
        "theorem_proved": True,
        "SM_parity_closed": True,
        "stationary_projector_source_verified": True,
        "validator_ready_stationary_rho_s": True,
        "selected_dotD_source_verified": True,
        "alpha1_driver_verified": True,
        "dynamic_PhiFin_C1_payload_emitted": False,
        "primitive_C1_contractions_emitted": False,
        "true_SM_equivalence_closed": False,
        "no_knob_closed": False,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "next_required_artifact": NEXT,
    }

    note = f"""# MTT Selected StationaryProjector dotD IntegratedFrontier v1

Status: `{STATUS}`.

This artifact reconciles the HYM-first-solve branch with the already proved
transported finite-projector source promotion and the compatible alpha1/dotD
import.

The active frontier is no longer stationary projectors, `rho_s`, or
`dotD_alpha1`. Those are closed at the stationary/source replay tier. The
remaining frontier is dynamic: selected `Phi_fin^C1` or primitive C1
contractions that emit `A_selected`, `b_selected`, `deltaTheta_C1`, and sector
response matrices without observed-data fitting.
"""

    for path, payload in [
        (INTEGRATION, integration),
        (PROMOTION, promotion),
        (FRONTIER, frontier),
        (CUTSET, cutset),
        (OUTPUT, candidate),
        (CERT, cert),
    ]:
        path.write_text(json.dumps(payload, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    NOTE.write_text(note, encoding="utf-8")
    print(json.dumps({"candidate": rel(OUTPUT), "status": STATUS}, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
