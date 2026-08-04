"""Audit the selected SU(5) qutrit heavy-link sector-transport lemma."""

from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SLUG = "selected_sectortransportselectionlemma_su5qutritheavylink"
BUILDER = ROOT / "scripts" / f"build_{SLUG}.py"
CANDIDATE = ROOT / "candidate_data" / f"{SLUG}.candidate.json"
PACKET_DIR = ROOT / "candidate_data" / SLUG
SOURCE_PACKET = PACKET_DIR / "selected_sector_transport_source.packet.json"
EIGHT_SLOT_PACKET = PACKET_DIR / "selected_heavylink_eight_slot_values.packet.json"
SUPERSESSION_PACKET = PACKET_DIR / "old_selection_gate_supersession.packet.json"
DOWNSTREAM_GATE = PACKET_DIR / "downstream_ckm_anglelaw_gate.packet.json"
CERT = ROOT / "certificates" / f"{SLUG}_certificate.json"
NOTE = ROOT / "proof_corpus" / "MTT_Selected_SectorTransportSelectionLemma_for_SU5QutritHeavyLink_v1.md"

STATUS = "MTT_SELECTED_SECTORTRANSPORT_SELECTION_LEMMA_CLOSED_HEAVYLINK_VALUES_EMITTED_CKM_ANGLELAW_OPEN"
NEXT = "MTT_Selected_CKMAngleLaw_FromSelectedHeavyLinkValues_or_FlavorObservableReplay_v1"


def load(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def require(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)


def main() -> int:
    subprocess.run([sys.executable, str(BUILDER)], cwd=ROOT, check=True)

    data = load(CANDIDATE)
    source = load(SOURCE_PACKET)
    slots = load(EIGHT_SLOT_PACKET)
    supersession = load(SUPERSESSION_PACKET)
    downstream = load(DOWNSTREAM_GATE)
    cert = load(CERT)
    note = NOTE.read_text(encoding="utf-8")

    require(data["status"] == STATUS, "candidate status mismatch")
    require(cert["status"] == STATUS, "certificate status mismatch")
    require(data["next_required_artifact"] == NEXT, "candidate next mismatch")
    require(cert["next_required_artifact"] == NEXT, "certificate next mismatch")
    require(data["theorem"]["proved"] is True, "theorem not proved")
    require(cert["theorem_proved"] is True, "certificate theorem not proved")

    decision = data["closure_decision"]
    require(decision["sector_transport_selection_lemma_closed"] is True, "selector not closed")
    require(decision["old_heavylink_selection_gate_superseded"] is True, "old gate not superseded")
    require(decision["selected_U10_Ubar5_source_outputs"] is True, "U outputs not selected")
    require(decision["selected_heavy_link_values_emitted"] is True, "heavy-link values not emitted")
    require(decision["eight_heavy_link_slots_filled"] is True, "eight slots not filled")
    require(decision["CKM_angle_magnitudes_derived"] is False, "CKM angles overderived")
    require(decision["Jarlskog_numerical_match_derived"] is False, "Jarlskog overderived")
    require(decision["Yukawa_rows_derived"] is False, "Yukawa rows overderived")
    require(decision["true_SM_equivalence_closed"] is False, "true SM overclosed")
    require(decision["full_no_knob_closure_closed"] is False, "no-knob overclosed")

    require(source["status"] == "SELECTED_STATIC_SOURCE_TRANSPORT_CLOSED", "source status mismatch")
    selected = source["selected_transport"]
    require(selected["B_10"] == "I_3", "B_10 mismatch")
    require(selected["B_bar5"] == "F", "B_bar5 mismatch")
    require(selected["U_10"] == "I_3", "U_10 mismatch")
    require(selected["U_bar5"] == "F", "U_bar5 mismatch")
    require(selected["q"] == 79, "q mismatch")
    require(selected["phase_side"] == ["u", "e"], "phase side mismatch")
    require(selected["shift_side"] == ["d", "nuD"], "shift side mismatch")
    require(source["common_gauge_transport_rejected"] is True, "common gauge not rejected")
    require(source["conjugate_q369_orientation_rejected_for_this_branch"] is True, "q369 not rejected")
    require(source["observed_data_used_as_selector"] is False, "observed selector used")
    require(source["target_fitting_used"] is False, "target fitting used")

    require(slots["status"] == "SELECTED_HEAVY_LINK_VALUES_EMITTED", "slot status mismatch")
    require(slots["selected_by_static_source_transport"] is True, "slots not selected")
    require(slots["candidate_rule"] == "B_10=I_3, B_bar5=F", "candidate rule mismatch")
    require(slots["slot_values"]["t_u13"] == 0.0 and slots["slot_values"]["t_u23"] == 0.0, "up slots mismatch")
    require(slots["slot_values"]["t_d13"] == 0.5773502691896258, "t_d13 mismatch")
    require(slots["slot_values"]["t_d23"] == [-0.28867513459481287, -0.5], "t_d23 mismatch")
    for key in ["c_u13", "c_u23", "c_d13", "c_d23"]:
        require(slots["slot_values"][key] == 0.0, f"{key} mismatch")
    require(slots["Delta_t_symbolic"] == ["1/sqrt(3)", "omega^2/sqrt(3)"], "Delta symbolic mismatch")
    require(slots["Delta_v_numeric"] == slots["Delta_t_numeric"], "Delta_v mismatch")
    require(slots["pure_C6_Delta_c_zero_preserved"] is True, "Delta_c guard lost")

    require(supersession["status"] == "OLD_SELECTION_LEMMA_GATE_SUPERSEDED_BY_LATER_SMSLOT_SOURCE_CLOSURE", "supersession mismatch")
    for item in [
        "static U_10=I_3 and U_bar5=F sector transport",
        "static 10_M/bar5_M/1_M matter-slot readout",
        "common Fourier transport cancels as gauge",
    ]:
        require(item in supersession["do_not_reopen"], f"missing do-not-reopen item: {item}")

    require(downstream["status"] == "CKM_ANGLELAW_AND_OBSERVABLE_REPLAY_OPEN", "downstream status mismatch")
    require(downstream["selected_inputs_ready"]["sector_transport_selection_lemma_closed"] is True, "downstream selector missing")
    require(downstream["selected_inputs_ready"]["selected_heavy_link_values_emitted"] is True, "downstream values missing")
    require("CKM angle magnitudes" in downstream["not_claimed"], "CKM boundary missing")
    require("Yukawa mass ratios" in downstream["not_claimed"], "Yukawa boundary missing")

    require(data["sector_transport_selection_lemma_claimed"] is True, "selector claim missing")
    require(data["selected_heavy_link_values_claimed"] is True, "values claim missing")
    require(data["closure_claimed"] is False, "full closure overclaimed")
    require(data["observed_data_used_as_selector"] is False, "observed selector used")
    require(data["target_fitting_used"] is False, "target fitting used")
    require(cert["sector_transport_selection_lemma_closed"] is True, "cert selector")
    require(cert["selected_heavy_link_values_emitted"] is True, "cert values")
    require(cert["closure_claimed"] is False, "cert overclaim")
    require("sector-transport selector and fills the eight heavy-link source" in note, "note boundary missing")
    require(NEXT in note, "note next mismatch")

    print(f"PASS {CANDIDATE.name}: {STATUS}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
