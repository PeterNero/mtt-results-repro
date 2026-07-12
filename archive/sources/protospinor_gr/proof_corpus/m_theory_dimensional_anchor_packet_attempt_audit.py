from __future__ import annotations

import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
CERT = ROOT / "certificates" / "m_theory_dimensional_anchor_packet_attempt_certificate.json"


def require(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)


def main() -> None:
    cert = json.loads(CERT.read_text(encoding="utf-8"))
    packet = json.loads(Path(cert["packet_written"]).read_text(encoding="utf-8"))
    note = Path(cert["note_written"]).read_text(encoding="utf-8")
    tests = cert["closure_tests"]
    promotion = cert["promotion"]
    guards = cert["guardrails"]

    require(cert["status"] == "MTHEORY_ANCHOR_PACKET_FILLED_STRUCTURAL_VALUE_OPEN", "unexpected packet attempt status")
    require(tests["anchor_packet_gate_ready"] is True, "packet gate must be ready")
    require(tests["m_theory_slot_identified"] is True, "M-theory slot must be identified")
    require(tests["same_branch_alignment_claimed"] is True, "same branch alignment should be recorded")
    require(tests["forbidden_inputs_absent"] is True, "forbidden inputs must be absent")
    require(tests["dimensionful_value_present"] is False, "dimensionful value must remain open")
    require(tests["selected_by_mtt"] is False, "source must not be marked selected")
    require(tests["alpha_phys_value_present"] is False, "alpha value must remain open")
    require(promotion["packet_promotes_to_closed_anchor"] is False, "packet must not promote")

    require(packet["status"] == "ATTEMPT_FILLED_STRUCTURAL_SLOT_VALUE_OPEN", "packet status changed")
    require(packet["dimensionful_quantity"]["value"] is None, "packet must not include a value")
    require(packet["source_certification"]["selected_by_mtt"] is False, "packet must not mark source selected")
    require(packet["source_certification"]["computed_before_target_comparison"] is False, "packet must not claim pre-target computation")
    require(packet["map_to_alpha_phys"]["alpha_phys_value"] is None, "packet must not contain alpha")
    require(packet["forbidden_inputs_absent"]["observed_Newton_or_Planck"] is True, "Newton/Planck input must be absent")
    require(packet["forbidden_inputs_absent"]["observed_particle_masses_or_TeV_calibration"] is True, "TeV calibration must be absent")

    require(guards["claims_alpha_phys_closed"] is False, "must not close alpha")
    require(guards["claims_physical_Newton_or_Planck"] is False, "must not claim Newton/Planck")
    require(guards["uses_observed_target_backsolve"] is False, "must not backsolve")
    require(guards["uses_Theta_5TeV_as_prediction"] is False, "must not use Theta 5 TeV")
    require(guards["uses_unit_convention_as_prediction"] is False, "must not use unit convention")

    require("structural packet, not a closed physical anchor" in note, "note must state nonpromotion")
    print("AUDIT_PASS: M-theory anchor packet fills the structural slot but cannot promote without a selected dimensionful modal-gap value")


if __name__ == "__main__":
    main()
