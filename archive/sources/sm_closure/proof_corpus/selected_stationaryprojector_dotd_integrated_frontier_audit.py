"""Audit integrated stationary-projector/dotD frontier."""

from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SLUG = "selected_stationaryprojector_dotd_integrated_frontier"
DATA = ROOT / "candidate_data" / f"{SLUG}.candidate.json"
PACKET_DIR = ROOT / "candidate_data" / SLUG
INTEGRATION = PACKET_DIR / "stationary_projector_dotd_integration.packet.json"
PROMOTION = PACKET_DIR / "promoted_stationary_sector_packet.packet.json"
FRONTIER = PACKET_DIR / "dynamic_c1_frontier_after_projector_dotd.packet.json"
CUTSET = PACKET_DIR / "primitive_c1_or_dynamic_phifin_cutset.packet.json"
CERT = ROOT / "certificates" / f"{SLUG}_certificate.json"
NOTE = ROOT / "proof_corpus" / "MTT_Selected_StationaryProjector_dotD_IntegratedFrontier_v1.md"
BUILDER = ROOT / "scripts" / "build_selected_stationaryprojector_dotd_integrated_frontier.py"

STATUS = "MTT_SELECTED_STATIONARYPROJECTOR_DOTD_INTEGRATED_FRONTIER_BUILT_C1_OPEN"
NEXT = "MTT_Selected_PrimitiveC1Contractions_or_DynamicPhiFinC1Payload_ValueEmission_v1"


def require(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)


def load(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def guardrails(payload: dict, label: str) -> None:
    require(payload["observed_data_used_as_selector"] is False, f"{label}: observed selector used")
    require(payload["target_fitting_used"] is False, f"{label}: target fitting used")


def main() -> int:
    subprocess.run([sys.executable, str(BUILDER)], cwd=ROOT, check=True)

    data = load(DATA)
    integration = load(INTEGRATION)
    promotion = load(PROMOTION)
    frontier = load(FRONTIER)
    cutset = load(CUTSET)
    cert = load(CERT)
    note = NOTE.read_text(encoding="utf-8")

    require(data["status"] == STATUS, "candidate status mismatch")
    require(cert["status"] == STATUS, "certificate status mismatch")
    require(data["theorem"]["proved"] is True, "candidate theorem not proved")
    require(cert["theorem_proved"] is True, "certificate theorem not proved")
    require(data["next_required_artifact"] == NEXT, "candidate next artifact mismatch")
    require(cert["next_required_artifact"] == NEXT, "certificate next artifact mismatch")
    require("active frontier is no longer stationary projectors" in note, "note misses active-frontier shift")

    stationary = integration["stationary_projector_source_promotion"]
    require(stationary["finite_projector_source_promotion_proved"] is True, "projector theorem not imported")
    require(stationary["selected_projector_source_verified"] is True, "selected projector source not verified")
    require(stationary["validator_ready_stationary_rho_s"] is True, "stationary rho_s not validator-ready")
    require(stationary["transported_packet_promoted"] is True, "transported packet not promoted")
    require(stationary["raw_untransported_packet_promoted"] is False, "raw packet overpromoted")

    transport = integration["symbolic_transport_validator"]
    require(transport["selected_source_verified"] is True, "transport source not verified")
    require(transport["selected_rho_s_validator_ready"] is True, "transport rho_s not ready")
    require(transport["all_sector_projector_riesz_green_replays_pass"] is True, "transport replays fail")
    require(
        transport["selected_dotD_source_verified_by_this_artifact"] is False,
        "transport artifact overclaims dotD",
    )
    require(
        transport["alpha1_driver_verified_by_this_artifact"] is False,
        "transport artifact overclaims alpha1",
    )

    alpha = integration["alpha1_dotd_replay_import"]
    require(alpha["selected_dotD_source_verified_imported"] is True, "dotD import missing")
    require(alpha["alpha1_driver_verified_imported"] is True, "alpha1 import missing")
    require(alpha["honest_dotD_alpha1_replay_imported"] is True, "honest dotD replay missing")
    require(alpha["du_dalpha1_equals_h_ext"] is True, "du/dalpha1 import mismatch")
    require(alpha["N_alpha1_h_ext"] == 1.0, "alpha1 normalization mismatch")

    decision = integration["reconciled_decision"]
    require(decision["stationary_projector_source_verified"] is True, "stationary source not reconciled")
    require(decision["validator_ready_stationary_rho_s"] is True, "rho_s not reconciled")
    require(decision["physical_dotD_alpha1_closed_by_import"] is True, "dotD not closed by import")
    require(decision["dynamic_PhiFin_C1_payload_emitted"] is False, "dynamic PhiFin overclaimed")
    require(decision["primitive_C1_contractions_emitted"] is False, "primitive C1 overclaimed")

    global_checks = promotion["global_checks"]
    require(global_checks["all_stationary_rho_s_promoted"] is True, "not all rho_s promoted")
    require(global_checks["all_source_verified"] is True, "not all sources verified")
    require(global_checks["all_green_valid"] is True, "not all Green operators valid")
    require(global_checks["H_rank_one"] is True, "H rank mismatch")
    require(global_checks["matter_rank_three"] is True, "matter rank mismatch")
    require(global_checks["physical_dotD_alpha1_available_by_import"] is True, "physical dotD import unavailable")

    boundary = promotion["boundary"]
    require(boundary["stationary_packet_ready"] is True, "stationary packet not ready")
    require(boundary["dynamic_C1_response_ready"] is False, "dynamic response overclaimed")
    require(boundary["matter_slot_routing_ready"] is False, "matter routing overclaimed")
    require(boundary["primitive_C1_contractions_ready"] is False, "primitive contractions overclaimed")
    require(boundary["A_selected_b_selected_ready"] is False, "A/b overclaimed")

    retired = frontier["retired_gates"]
    for key in [
        "stationary_projector_source",
        "stationary_rho_s",
        "selected_dotD_source_verified",
        "alpha1_driver_verified",
        "honest_dotD_alpha1_replay",
    ]:
        require(retired[key] is True, f"retired gate not closed: {key}")

    primitive = frontier["primitive_layer_status"]
    require(
        primitive["current_primitive_class_promoted_as_valid_C1_observable_layer"] is True,
        "primitive observable layer not retained",
    )
    require(
        primitive["current_primitive_class_promoted_as_flavor_closure"] is False,
        "primitive flavor closure overclaimed",
    )
    require(primitive["higherorder_fullresponse_values_promoted"] is False, "higher response overclaimed")
    require(primitive["current_layer_flavor_splitting_possible"] is False, "flavor splitting overclaimed")

    require(cutset["recommended_next_artifact"] == NEXT, "cutset next artifact mismatch")
    require(cutset["bookkeeping_remaining"] is False, "bookkeeping still marked remaining")
    require(cutset["source_or_value_emission_required"] is True, "source/value requirement missing")
    require(cutset["true_SM_equivalence_closed"] is False, "true SM equivalence overclaimed")
    require(cutset["no_knob_closed"] is False, "no-knob overclaimed")
    required_payloads = [
        "selected primitive C1 contractions or selected dynamic Phi_fin^C1 payload",
        "selected A_selected response operator",
        "selected b_selected source vector",
        "selected deltaTheta_C1 solve or selected no-solve theorem",
        "sector response matrices M_u, M_d, M_e, M_nuD",
    ]
    remaining = "\n".join(cutset["remaining_minimal_payloads"])
    for item in required_payloads:
        require(item in remaining, f"cutset missing payload: {item}")

    closure = data["closure_decision"]
    require(closure["stationary_projector_source_verified"] is True, "closure source flag missing")
    require(closure["validator_ready_stationary_rho_s"] is True, "closure rho_s flag missing")
    require(closure["selected_dotD_source_verified"] is True, "closure dotD flag missing")
    require(closure["alpha1_driver_verified"] is True, "closure alpha1 flag missing")
    require(closure["dynamic_PhiFin_C1_payload_emitted"] is False, "closure dynamic PhiFin overclaimed")
    require(closure["primitive_C1_contractions_emitted"] is False, "closure primitive C1 overclaimed")
    require(closure["A_selected_emitted"] is False, "closure A_selected overclaimed")
    require(closure["b_selected_emitted"] is False, "closure b_selected overclaimed")
    require(
        closure["actual_QaSU3_operator_packet_dynamic_complete"] is False,
        "actual Qa/SU3 dynamic packet overclaimed",
    )
    require(closure["true_SM_equivalence_closed"] is False, "true SM equivalence overclaimed")
    require(closure["no_knob_closed"] is False, "no-knob overclaimed")

    for label, payload in [
        ("candidate", data),
        ("integration", integration),
        ("promotion", promotion),
        ("frontier", frontier),
        ("cutset", cutset),
        ("certificate", cert),
    ]:
        guardrails(payload, label)

    print(f"PASS {DATA.name}: {STATUS}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
