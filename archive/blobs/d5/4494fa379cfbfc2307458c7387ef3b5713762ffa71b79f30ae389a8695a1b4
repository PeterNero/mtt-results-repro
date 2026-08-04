"""Audit CKM source-chain integration after selected heavy-link values."""

from __future__ import annotations

import json
import math
import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SLUG = "selected_ckmanglelaw_fromselectedheavylinks_or_flavorobservablereplay"
BUILDER = ROOT / "scripts" / f"build_{SLUG}.py"
CANDIDATE = ROOT / "candidate_data" / f"{SLUG}.candidate.json"
PACKET_DIR = ROOT / "candidate_data" / SLUG
INTEGRATION = PACKET_DIR / "selected_ckm_source_chain_integration.packet.json"
DELTA_SIGNATURE = PACKET_DIR / "selected_heavylink_delta_signature.packet.json"
POSTCHECK = PACKET_DIR / "q79_phase_jarlskog_observable_postcheck.packet.json"
ANGLE_MAP_GATE = PACKET_DIR / "remaining_ckm_angle_map_gate.packet.json"
CERT = ROOT / "certificates" / f"{SLUG}_certificate.json"
NOTE = ROOT / "proof_corpus" / "MTT_Selected_CKMAngleLaw_FromSelectedHeavyLinkValues_or_FlavorObservableReplay_v1.md"

STATUS = "MTT_SELECTED_CKMANGLELAW_FROM_SELECTEDHEAVYLINKS_CHAIN_TIED_ANGLEMAP_OPEN"
NEXT = "MTT_Selected_DeltaV_to_CKM_AngleMagnitudeMap_or_HonestFlavorObservableExecution_v1"


def load(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def require(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)


def main() -> int:
    subprocess.run([sys.executable, str(BUILDER)], cwd=ROOT, check=True)

    data = load(CANDIDATE)
    integration = load(INTEGRATION)
    delta = load(DELTA_SIGNATURE)
    postcheck = load(POSTCHECK)
    gate = load(ANGLE_MAP_GATE)
    cert = load(CERT)
    note = NOTE.read_text(encoding="utf-8")

    require(data["status"] == STATUS, "candidate status mismatch")
    require(cert["status"] == STATUS, "certificate status mismatch")
    require(data["next_required_artifact"] == NEXT, "candidate next mismatch")
    require(cert["next_required_artifact"] == NEXT, "cert next mismatch")
    require(data["theorem"]["proved"] is True, "theorem not proved")
    require(cert["theorem_proved"] is True, "cert theorem not proved")

    decision = data["closure_decision"]
    require(decision["CKM_source_input_chain_tied"] is True, "source chain not tied")
    require(decision["old_heavy_link_values_open_flag_superseded"] is True, "old flag not superseded")
    require(decision["selected_heavy_link_entry_count"] == 8, "heavy-link count mismatch")
    require(decision["selected_Delta_v_emitted"] is True, "Delta_v not emitted")
    require(decision["leading_CKM_noncommutation_values_closed"] is True, "noncommutation not closed")
    require(decision["q79_phase_contact_closed"] is True, "q79 phase not closed")
    require(decision["q79_observable_postcheck_recomputed"] is True, "postcheck missing")
    for key in [
        "CKM_angle_magnitudes_derived",
        "Jarlskog_source_derived_without_measured_angles",
        "Yukawa_rows_derived",
        "PMNS_orientation_source_values_derived",
        "true_SM_equivalence_closed",
        "full_no_knob_closure_closed",
    ]:
        require(decision[key] is False, f"overclaim: {key}")

    require(integration["status"] == "SELECTED_SOURCE_CHAIN_TIED", "integration status")
    closed = integration["closed_inputs"]
    for key in [
        "policy_operator_CKM_PMNS_bridge",
        "q79_CKM_CP_phase_contact",
        "heavy_link_slot_contract",
        "sector_transport_selection_lemma",
        "selected_heavy_link_values",
        "static_same_orientation_filter",
        "leading_noncommutation_readiness",
    ]:
        require(closed[key] is True, f"integration missing {key}")
    require(integration["newly_closed_by_this_bridge"]["selected_heavy_link_entry_count"] == 8, "integration count")
    require(integration["newly_closed_by_this_bridge"]["leading_noncommutation_values_closed"] is True, "integration noncommutation")
    require(integration["not_closed"]["Delta_v_to_CKM_angle_magnitude_map"] is True, "angle map boundary")
    require(integration["observed_data_used_as_selector"] is False, "observed selector used")
    require(integration["observed_data_used_for_postcheck"] is True, "postcheck flag missing")

    require(delta["status"] == "SELECTED_DELTAV_SIGNATURE_EMITTED", "delta status")
    require(delta["Delta_v_symbolic"] == ["1/sqrt(3)", "omega^2/sqrt(3)"], "delta symbolic")
    require(delta["Delta_c_zero"] is True, "Delta_c not zero")
    require(abs(delta["component_magnitudes"][0] - 1 / math.sqrt(3)) < 1e-12, "first magnitude")
    require(abs(delta["component_magnitudes"][1] - 1 / math.sqrt(3)) < 1e-12, "second magnitude")
    require(abs(delta["norm"] - math.sqrt(2 / 3)) < 1e-12, "norm mismatch")
    require(delta["norm_symbolic"] == "sqrt(2/3)", "norm symbolic")

    require(postcheck["status"] == "OBSERVABLE_POSTCHECK_ONLY_NOT_SELECTOR", "postcheck status")
    require(postcheck["q_mod_448"] == 79, "q mismatch")
    require(abs(postcheck["delta_q79_deg"] - 63.48214285714286) < 1e-12, "delta q79")
    require(abs(postcheck["phase_residual_deg"] - 2.213743629348511) < 1e-12, "phase residual")
    require(abs(postcheck["jarlskog_relative_residual"] - 0.018190645457448397) < 1e-12, "J residual")
    require(postcheck["matches_prior_q79_bridge_residuals"] is True, "prior residual mismatch")
    require(postcheck["observed_data_used_as_selector"] is False, "postcheck selector")
    require(postcheck["observed_data_used_for_postcheck"] is True, "postcheck flag")

    require(gate["status"] == "ANGLE_MAGNITUDE_MAP_OPEN", "gate status")
    for key in ["Delta_v", "q79_phase", "minimal_flavor_policy_operator", "static_matter_slot_source", "leading_noncommutation"]:
        require(gate["selected_inputs_available"][key] is True, f"gate input missing {key}")
    require("A_CKM" in gate["required_next_theorem"], "A_CKM theorem missing")
    require("fit s12,s23,s13 from observed CKM values and call them selected" in gate["forbidden_routes"], "forbidden fit missing")
    require(gate["next_required_artifact"] == NEXT, "gate next mismatch")

    require(data["closure_claimed"] is False, "closure overclaimed")
    require(data["observed_data_used_as_selector"] is False, "observed selector used")
    require(data["observed_data_used_for_postcheck"] is True, "postcheck flag missing")
    require(data["target_fitting_used"] is False, "target fitting used")
    require(cert["closure_claimed"] is False, "cert closure overclaimed")
    require("A_CKM" in note and NEXT in note, "note missing next theorem")
    print(f"PASS {CANDIDATE.name}: {STATUS}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
