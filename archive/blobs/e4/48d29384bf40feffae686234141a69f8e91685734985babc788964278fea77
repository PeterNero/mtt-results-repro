"""Audit Higgs production covariance profile or dynamic Qa/SU3 operator slot closure."""

from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SLUG = "selected_higgsproductioncovarianceprofile_or_dynamicqasu3operatorslotclosure"
DATA = ROOT / "candidate_data" / f"{SLUG}.candidate.json"
PACKET_DIR = ROOT / "candidate_data" / SLUG
PRODUCTION = PACKET_DIR / "higgs_production_covariance_profile_acquisition.packet.json"
SLOT = PACKET_DIR / "qasu3_operator_source_slot_closure.packet.json"
DECISION = PACKET_DIR / "true_equivalence_decision_after_production_or_operator_slot.packet.json"
CERT = ROOT / "certificates" / f"{SLUG}_certificate.json"
NOTE = ROOT / "proof_corpus" / "MTT_Selected_HiggsProductionCovarianceProfile_or_DynamicQaSU3OperatorSlotClosure_v1.md"
BUILDER = ROOT / "scripts" / f"build_{SLUG}.py"

STATUS = (
    "MTT_SELECTED_HIGGSPRODUCTIONCOVARIANCEPROFILE_OR_DYNAMICQASU3OPERATORSLOTCLOSURE_"
    "BUILT_PRODUCTION_OPEN_ONE_OPERATOR_SOURCE_SLOT_CLOSED"
)
NEXT = "MTT_Selected_HiggsProductionProfileImport_or_SecondQaSU3OperatorSlotClosure_v1"
FILLED_SLOT = "selected_source_status_for_L3_minus_K2_or_enlarged_visible_source"


def load(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def require(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)


def main() -> int:
    subprocess.run([sys.executable, str(BUILDER)], cwd=ROOT, check=True)

    data = load(DATA)
    production = load(PRODUCTION)
    slot = load(SLOT)
    decision = load(DECISION)
    cert = load(CERT)
    note = NOTE.read_text(encoding="utf-8")

    require(data["status"] == STATUS, "candidate status mismatch")
    require(cert["status"] == STATUS, "certificate status mismatch")
    require(data["theorem"]["proved"] is True and cert["theorem_proved"] is True, "theorem flag missing")
    require(data["next_required_artifact"] == NEXT and cert["next_required_artifact"] == NEXT, "next artifact mismatch")

    available = production["available_now"]
    require(available["accepted_Higgs_decay_covariance_profile"] is True, "decay profile not retained")
    require(available["imported_decay_profile_replay_closed"] is True, "decay replay not retained")
    require(available["official_LHCHXSWG_likelihood_imported"] is False, "official likelihood overclaimed")
    require(available["production_covariance_profile_rows_present"] is False, "production rows overclaimed")
    require(available["coupling_modifier_covariance_profile_present"] is False, "coupling profile overclaimed")
    require(production["decision"]["production_covariance_profile_closed"] is False, "production profile overclosed")
    require(production["decision"]["production_profile_acquisition_manifest_built"] is True, "production manifest missing")
    require(production["acquisition_standard"]["accepted_decay_profile_is_not_reused_as_production_profile"] is True, "decay/production guard missing")

    require(slot["filled_slot"] == FILLED_SLOT, "filled slot mismatch")
    value = slot["selected_source_value"]
    require(value["selected_source_label"] == "g3 / L3-K2", "selected source label mismatch")
    require(value["selected_L"] == [1, -2, 0], "selected L mismatch")
    require(value["selected_L2"] == [2, -4, 0], "selected L2 mismatch")
    require(value["selected_c2"] == [4, 0, 0], "selected c2 mismatch")
    require(value["status"] == "UNCONDITIONAL_IN_PATCHED_PROOF_SPINE", "terminal source status mismatch")
    for key, closed in slot["proof_inputs"].items():
        require(closed is True, f"slot proof input not closed: {key}")
    slot_status = slot["slot_status_after_closure"]
    require(slot_status["required_operator_slot_count"] == 8, "slot count mismatch")
    require(slot_status["filled_operator_slot_count"] == 1, "filled slot count mismatch")
    require(slot_status["filled_slots"] == [FILLED_SLOT], "filled slot list mismatch")
    require(slot_status["remaining_missing_slot_count"] == 7, "remaining slot count mismatch")
    require(FILLED_SLOT not in slot_status["missing_slots"], "filled slot still missing")
    closure = slot["closure_result"]
    require(closure["operator_source_slot_closed"] is True, "operator source slot not closed")
    require(closure["selected_source_value_emitted"] is True, "selected source value not emitted")
    require(closure["actual_dynamic_QaSU3_operator_packet_closed"] is False, "dynamic packet overclosed")

    require(decision["status"] == "PRODUCTION_PROFILE_OPEN_ONE_QASU3_OPERATOR_SOURCE_SLOT_CLOSED", "decision status mismatch")
    require(decision["route_A"]["production_covariance_profile_closed"] is False, "decision route A overclosed")
    require(decision["route_B"]["operator_source_slots_closed"] == 1, "decision route B slot count mismatch")
    require(decision["route_B"]["operator_source_slots_remaining"] == 7, "decision remaining slot mismatch")
    require(decision["route_B"]["actual_dynamic_QaSU3_operator_packet_closed"] is False, "decision dynamic overclosed")
    require(decision["SM_parity_closed"] is True, "SM parity reopened")
    require(decision["true_SM_equivalence_closed"] is False, "true equivalence overclosed")
    require(decision["no_knob_closed"] is False, "no-knob overclosed")

    closure_decision = data["closure_decision"]
    require(closure_decision["production_covariance_profile_closed"] is False, "candidate production overclosed")
    require(closure_decision["first_QaSU3_operator_source_slot_closed"] is True, "candidate slot closure missing")
    require(closure_decision["actual_dynamic_QaSU3_operator_packet_closed"] is False, "candidate dynamic overclosed")
    require(closure_decision["true_SM_equivalence_closed"] is False, "candidate true equivalence overclosed")
    require(data["what_closes_now"]["selected_L3_minus_K2_operator_source_slot"] is True, "slot close flag missing")
    require(data["what_closes_now"]["qasu3_operator_cutset_reduced_to_seven_slots"] is True, "cutset reduction missing")
    require(data["what_remains_open"]["operator_layer_Pic0_or_physical_quotient"] is True, "Pic0 gate missing")
    require(data["what_remains_open"]["actual_dynamic_QaSU3_operator_packet"] is True, "dynamic gate missing")
    require(data["closure_claimed"] is False, "candidate incorrectly claims full closure")
    require("does not close Higgs production/coupling covariance" in note, "note missing production guard")
    require("reduces the operator cutset from eight slots to seven" in note, "note missing slot reduction")

    for packet in [data, production, slot, decision, cert]:
        require(packet.get("observed_data_used_as_selector") is False, "observed selector violation")
        require(packet.get("target_fitting_used") is False, "target fitting violation")

    print(json.dumps({"candidate": str(DATA.relative_to(ROOT)), "status": STATUS}, indent=2))
    print(f"PASS {DATA.name}: {STATUS}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
