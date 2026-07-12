"""Audit transition-payload or heat-torsion response one-gate attack."""

from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SLUG = "selected_transitionpayload_or_heattorsionresponse_onegateattack"
DATA = ROOT / "candidate_data" / f"{SLUG}.candidate.json"
PACKET_DIR = ROOT / "candidate_data" / SLUG
TRANSITION_ATTACK = PACKET_DIR / "selected_transition_payload_attack.packet.json"
PROMOTION_CONTRACT = PACKET_DIR / "transition_payload_promotion_contract.open.json"
HEAT_DEPENDENCY = PACKET_DIR / "heat_torsion_dependency_on_transition_payload.packet.json"
FRONTIER = PACKET_DIR / "one_gate_attack_frontier.packet.json"
CERT = ROOT / "certificates" / f"{SLUG}_certificate.json"
NOTE = ROOT / "proof_corpus" / "MTT_Selected_TransitionPayload_or_HeatTorsionResponse_OneGateAttack_v1.md"
BUILDER = ROOT / "scripts" / f"build_{SLUG}.py"

STATUS = "MTT_SELECTED_TRANSITIONPAYLOAD_OR_HEATTORSIONRESPONSE_ONEGATEATTACK_BUILT_TRANSITION_PAYLOAD_OPEN"
NEXT = "MTT_Selected_TracePayload_or_FullHYMOperatorEmission_v1"


def load(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def require(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)


def main() -> int:
    subprocess.run([sys.executable, str(BUILDER)], cwd=ROOT, check=True)

    data = load(DATA)
    attack = load(TRANSITION_ATTACK)
    contract = load(PROMOTION_CONTRACT)
    heat = load(HEAT_DEPENDENCY)
    frontier = load(FRONTIER)
    cert = load(CERT)
    note = NOTE.read_text(encoding="utf-8")

    require(data["status"] == STATUS, "candidate status mismatch")
    require(cert["status"] == STATUS, "certificate status mismatch")
    require(data["theorem"]["proved"] is True and cert["theorem_proved"] is True, "theorem flag missing")
    require(data["next_required_artifact"] == NEXT and cert["next_required_artifact"] == NEXT, "next artifact mismatch")

    support = attack["support"]
    require(support["prior_has_transition_as_primary_next"] is True, "primary transition support missing")
    require(support["two_gate_transition_slot_open"] is True, "transition was unexpectedly closed")
    require(support["finite_values_shape_complete"] is True, "finite value shapes missing")
    require(support["local_same_source_formula_ready"] is True, "local same-source formula missing")
    require(support["q79_gap_layer_proved"] is True, "q79 gap layer not proved")
    require(support["q79_gap_layer_scope_only"] is True, "q79 scope should remain gap-only")
    require(support["typed_witness_payload_specified"] is True, "typed witness contract missing")
    require(attack["slot_closes"] is False, "transition slot overclosed")
    require("diagnostic/model-active values" in attack["why_not_closed"], "diagnostic guard missing")

    routes = attack["route_status"]
    for route_name in ["finite_trace_identification", "full_HYM_Newton_replay", "typed_monad_Cech_payload"]:
        require(route_name in routes, f"route missing: {route_name}")
        require(routes[route_name]["closed"] is False, f"route overclosed: {route_name}")
        require(len(routes[route_name]["missing"]) > 0, f"route missing-list empty: {route_name}")

    for key in [
        "selected_trace_equality",
        "selected_gap_error_certificate",
        "honest_replay_without_lifted_flags",
    ]:
        require(attack["open_cutset"][key] is True, f"cutset missing: {key}")

    require(contract["status"] == "OPEN", "contract should be open")
    for route_name in ["finite_trace_identification", "full_HYM_Newton_replay", "typed_monad_Cech_payload"]:
        require(route_name in contract["must_emit_one_of"], f"contract route missing: {route_name}")
    for forbidden in [
        "selected flags added by diagnostic lift",
        "observed masses, CKM magnitudes, or benchmark Yukawa entries",
        "identity rho_E smoke",
        "canonical model-active operator relabeled as selected without a trace theorem",
    ]:
        require(forbidden in contract["must_not_use"], f"forbidden input missing: {forbidden}")
    require("selected nonidentity rho_E or selected transition/Cech tables" in contract["common_validator_outputs"], "rho_E output missing")
    require("honest replay without diagnostic selected-flag lifts" in contract["common_validator_outputs"], "honest replay output missing")

    require(heat["slot_closes"] is False, "heat/torsion slot overclosed")
    require(heat["dependency"]["transition_payload_needed_first"] is True, "heat dependency missing")
    require("selected operator and finite basis" in heat["dependency"]["reason"], "heat dependency reason weak")

    require(frontier["operator_source_slots_closed"] == 6, "frontier closed count changed")
    require(frontier["operator_source_slots_remaining"] == 2, "frontier remaining count changed")
    require(frontier["transition_slot_closes"] is False, "frontier transition overclosed")
    require(frontier["determinant_torsion_slot_closes"] is False, "frontier heat overclosed")
    require(frontier["best_next_artifact"] == NEXT, "frontier next mismatch")
    require(frontier["true_SM_equivalence_closed"] is False, "true equivalence overclosed")

    closure = data["closure_decision"]
    require(closure["operator_source_slots_closed_total"] == 6, "candidate closed count changed")
    require(closure["operator_source_slots_remaining"] == 2, "candidate remaining count changed")
    require(closure["transition_rhoE_or_Cech_Dolbeault_DE_data_closed"] is False, "candidate transition overclosed")
    require(closure["finite_determinant_heat_spectrum_or_torsion_response_closed"] is False, "candidate heat overclosed")
    require(data["closure_claimed"] is False, "candidate should not claim closure")
    require(data["what_closes_now"]["promotion_contract_emitted"] is True, "contract flag missing")
    require(data["what_remains_open"]["selected_trace_equality"] is True, "selected trace blocker missing")
    require(data["what_remains_open"]["rhoE_selected_by_mtt"] is True, "rhoE blocker missing")

    require("The result is not a closure" in note, "note no-close statement missing")
    require("finite trace identification" in note, "note route missing")
    require("honest replay without diagnostic lifted selected flags" in note, "note honest replay guard missing")
    require("Current count remains six closed operator-source slots and two open slots" in note, "note count missing")

    for packet in [data, attack, contract, heat, frontier, cert]:
        require(packet.get("observed_data_used_as_selector") is False, "observed selector violation")
        require(packet.get("target_fitting_used") is False, "target fitting violation")

    print(json.dumps({"candidate": str(DATA.relative_to(ROOT)), "status": STATUS}, indent=2))
    print(f"PASS {DATA.name}: {STATUS}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
