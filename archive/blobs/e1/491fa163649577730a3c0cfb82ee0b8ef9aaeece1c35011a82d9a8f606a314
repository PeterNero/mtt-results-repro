"""Audit selected trace payload or full HYM operator emission artifact."""

from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SLUG = "selected_tracepayload_or_fullhymoperatoremission"
DATA = ROOT / "candidate_data" / f"{SLUG}.candidate.json"
PACKET_DIR = ROOT / "candidate_data" / SLUG
TRACE_RECON = PACKET_DIR / "selected_trace_payload_reconciliation.packet.json"
SLOT_CLOSURE = PACKET_DIR / "transition_rhoe_or_cech_dolbeault_de_slot_closure.packet.json"
FRONTIER = PACKET_DIR / "post_seven_slot_true_equivalence_frontier.packet.json"
CERT = ROOT / "certificates" / f"{SLUG}_certificate.json"
NOTE = ROOT / "proof_corpus" / "MTT_Selected_TracePayload_or_FullHYMOperatorEmission_v1.md"
BUILDER = ROOT / "scripts" / f"build_{SLUG}.py"

STATUS = "MTT_SELECTED_TRACEPAYLOAD_OR_FULLHYMOPERATOREMISSION_BUILT_TRANSITION_SLOT_CLOSED"
NEXT = "MTT_Selected_HeatTorsionResponse_FinalGate_v1"
SLOT = "transition_rhoE_or_Cech_Dolbeault_DE_data"


def load(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def require(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)


def main() -> int:
    subprocess.run([sys.executable, str(BUILDER)], cwd=ROOT, check=True)

    data = load(DATA)
    recon = load(TRACE_RECON)
    slot = load(SLOT_CLOSURE)
    frontier = load(FRONTIER)
    cert = load(CERT)
    note = NOTE.read_text(encoding="utf-8")

    require(data["status"] == STATUS, "candidate status mismatch")
    require(cert["status"] == STATUS, "certificate status mismatch")
    require(data["theorem"]["proved"] is True and cert["theorem_proved"] is True, "theorem flag missing")
    require(data["next_required_artifact"] == NEXT and cert["next_required_artifact"] == NEXT, "next artifact mismatch")

    require(recon["slot"] == SLOT, "reconciled slot mismatch")
    require(recon["slot_closes"] is True, "transition slot should close")
    for key, value in recon["proof_inputs"].items():
        require(value is True, f"proof input false: {key}")
    payload = recon["selected_trace_payload"]
    require(payload["level"] == "selected Phi_fin finite trace D_E/gap layer", "payload level mismatch")
    require(payload["branch"] == {"q": 79, "orientation": "F", "torsion_label_m": 1}, "branch mismatch")
    require(payload["basis_id"] == "F3xF3_gerbe_twisted_fourier_N1_rank3", "basis mismatch")
    require(payload["basis_dimension"] == 27, "basis dimension mismatch")
    require(payload["selected_trace_equality"]["proved"] is True, "trace equality not proved")
    require(payload["selected_gap_lower_bound"] > 0, "gap not positive")

    for no_claim in [
        "full S2 value emission beyond D_E gap layer",
        "selected dotD_alpha1 source identity",
        "primitive C1 response",
        "A_selected or b_selected",
        "finite determinant/heat spectrum/torsion response",
        "Yukawa, CKM, PMNS, or full SM closure",
        "no-knob constants derivation",
    ]:
        require(no_claim in recon["scope"]["does_not_close"], f"missing guard: {no_claim}")

    require(slot["filled_slot"] == SLOT, "slot closure filled wrong slot")
    result = slot["closure_result"]
    require(result["transition_rhoE_or_Cech_Dolbeault_DE_data_closed"] is True, "transition closure missing")
    require(result["determinant_torsion_slot_closed"] is False, "torsion overclosed")
    require(result["full_S2_value_emission_closed"] is False, "full S2 overclosed")
    require(result["selected_dotD_alpha1_source_identity_closed"] is False, "dotD overclosed")
    require(result["actual_dynamic_QaSU3_operator_packet_closed"] is False, "dynamic packet overclosed")
    status = slot["slot_status_after_closure"]
    require(status["required_operator_slot_count"] == 8, "required slot count mismatch")
    require(status["filled_operator_slot_count"] == 7, "filled slot count should be 7")
    require(status["remaining_missing_slot_count"] == 1, "remaining slot count should be 1")
    require(SLOT in status["filled_slots"], "transition slot not filled")
    require(SLOT not in status["missing_slots"], "transition slot still missing")
    require(status["missing_slots"] == ["finite_determinant_heat_spectrum_or_torsion_response"], "wrong remaining slot")

    require(frontier["operator_source_slots_closed"] == 7, "frontier closed count mismatch")
    require(frontier["operator_source_slots_remaining"] == 1, "frontier remaining count mismatch")
    require(frontier["remaining_slots"] == ["finite_determinant_heat_spectrum_or_torsion_response"], "frontier remaining mismatch")
    require(frontier["true_SM_equivalence_closed"] is False, "true equivalence overclosed")
    require(frontier["no_knob_closed"] is False, "no-knob overclosed")

    closure = data["closure_decision"]
    require(closure["operator_source_slots_closed_total"] == 7, "candidate closed count mismatch")
    require(closure["operator_source_slots_remaining"] == 1, "candidate remaining count mismatch")
    require(closure["transition_rhoE_or_Cech_Dolbeault_DE_data_closed"] is True, "candidate transition missing")
    require(closure["finite_determinant_heat_spectrum_or_torsion_response_closed"] is False, "candidate torsion overclosed")
    require(closure["actual_dynamic_QaSU3_operator_packet_closed"] is False, "candidate dynamic overclosed")
    require(data["closure_claimed"] is True, "candidate should claim transition slot closure")
    require(data["what_remains_open"]["finite_determinant_heat_spectrum_or_torsion_response"] is True, "torsion blocker missing")
    require(data["what_remains_open"]["selected_dotD_alpha1_source_identity"] is True, "dotD blocker missing")

    require("This closes:" in note and SLOT in note, "note closure missing")
    require("It does not close full S2 value emission" in note, "note guard missing")
    require("Current count is now seven closed operator-source slots and one open slot" in note, "note count missing")

    for packet in [data, recon, slot, frontier, cert]:
        require(packet.get("observed_data_used_as_selector") is False, "observed selector violation")
        require(packet.get("target_fitting_used") is False, "target fitting violation")

    print(json.dumps({"candidate": str(DATA.relative_to(ROOT)), "status": STATUS}, indent=2))
    print(f"PASS {DATA.name}: {STATUS}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
