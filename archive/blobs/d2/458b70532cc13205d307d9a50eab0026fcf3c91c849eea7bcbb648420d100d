"""Audit the heavy-link value source search import."""

from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "candidate_data"
CERTS = ROOT / "certificates"
CORPUS = ROOT / "proof_corpus"
BUILDER = ROOT / "scripts" / "build_selected_heavylinkvaluesource_search_or_ckmanglelaw.py"

SLUG = "selected_heavylinkvaluesource_search_or_ckmanglelaw"
PACKET_DIR = DATA / SLUG
CANDIDATE = DATA / f"{SLUG}.candidate.json"
CERT = CERTS / f"{SLUG}_certificate.json"
NOTE = CORPUS / "MTT_Selected_HeavyLinkValueSourceSearch_or_SelectedCKMAngleLaw_v1.md"
FOUND = PACKET_DIR / "su5_qutrit_relative_transport_heavylink_candidate.packet.json"
DEPENDENCIES = PACKET_DIR / "heavylink_dependency_reduction_after_candidate.packet.json"
SELECTION_GATE = PACKET_DIR / "sector_transport_selection_lemma_gate.packet.json"
NEXT_PACKET = PACKET_DIR / "next_sector_transport_selection_lemma.packet.json"

STATUS = "MTT_SELECTED_HEAVYLINKVALUESOURCE_SEARCH_FOUND_SU5_QUTRIT_CONDITIONAL_VALUES_SELECTION_LEMMA_OPEN"
NEXT = "MTT_Selected_SectorTransportSelectionLemma_for_SU5QutritHeavyLink_v1"


def load(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def require(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)


def main() -> int:
    subprocess.run([sys.executable, str(BUILDER)], cwd=ROOT, check=True)

    candidate = load(CANDIDATE)
    cert = load(CERT)
    found = load(FOUND)
    deps = load(DEPENDENCIES)
    gate = load(SELECTION_GATE)
    next_packet = load(NEXT_PACKET)
    note = NOTE.read_text(encoding="utf-8")

    require(candidate["status"] == STATUS, "candidate status mismatch")
    require(cert["status"] == STATUS, "cert status mismatch")
    require(candidate["next_required_artifact"] == NEXT, "candidate next mismatch")
    require(cert["next_required_artifact"] == NEXT, "cert next mismatch")
    require(next_packet["next_required_artifact"] == NEXT, "next packet mismatch")
    require(candidate["theorem"]["proved"] is True, "candidate theorem not proved")
    require(cert["theorem_proved"] is True, "cert theorem not proved")

    for payload in [candidate, cert, found, deps, gate, next_packet]:
        require(payload["closure_claimed"] is True, "closure boundary missing")
        require(payload["observed_data_used_as_selector"] is False, "observed selector used")
        require(payload["target_fitting_used"] is False, "target fitting used")

    decision = candidate["closure_decision"]
    require(decision["exact_conditional_heavy_link_values_found"] is True, "candidate not found")
    require(decision["candidate_rule_B10_I_Bbar5_F"] is True, "rule not recorded")
    require(decision["conditional_Delta_v_nonzero"] is True, "Delta_v not nonzero")
    require(decision["pure_C6_Delta_c_zero_preserved"] is True, "C6 obstruction not preserved")
    require(decision["common_fourier_transport_cancels_as_gauge"] is True, "gauge guard missing")
    require(decision["selected_heavy_link_values_emitted"] is False, "selected values overemitted")
    require(decision["sector_transport_selection_lemma_closed"] is False, "selection lemma overclosed")
    require(decision["CKM_angle_magnitudes_derived"] is False, "CKM angles overderived")
    require(decision["true_SM_equivalence_closed"] is False, "true SM overclosed")

    require(found["candidate_rule"] == "B_10=I_3, B_bar5=F", "found rule")
    require(found["up_heavy_links_13_23"] == [0.0, 0.0], "up links")
    require(found["Delta_t_symbolic"] == ["1/sqrt(3)", "omega^2/sqrt(3)"], "symbolic Delta")
    require(abs(found["Delta_t_numeric"][0] - 0.5773502691896258) < 1e-12, "Delta first")
    require(found["Delta_t_numeric"][1] == [-0.28867513459481287, -0.5], "Delta second")
    require(found["Delta_v_if_selected"] == found["Delta_t_numeric"], "Delta_v")
    require(found["leading_heavy_link_gate_if_selected"] is True, "leading gate")
    require(found["selected_by_MTT"] is False, "found overselected")
    require(found["uses_observed_flavor_data"] is False, "observed flavor used")

    slot_fill = deps["slot_fill_if_selected"]
    require(slot_fill["t_u13"] == 0.0 and slot_fill["t_u23"] == 0.0, "t_u fill")
    require(slot_fill["t_d13"] == found["Delta_t_numeric"][0], "t_d13")
    require(slot_fill["t_d23"] == found["Delta_t_numeric"][1], "t_d23")
    for key in ["c_u13", "c_u23", "c_d13", "c_d23"]:
        require(slot_fill[key] == 0.0, f"{key} should be zero")
    require(deps["dependency_equations"]["current_candidate"] == "Delta_c=0, Delta_v=Delta_t", "dependency")
    require(deps["common_fourier_transport_cancels"] is True, "common gauge")
    require(deps["su5_representation_split_nonzero"] is True, "split nonzero")

    require(gate["candidate_values_found"] is True, "gate candidate")
    require(gate["selected_heavy_link_values_emitted"] is False, "gate selected")
    require("relative qutrit Fourier transport" in gate["required_lemma"], "required lemma")
    require(gate["still_open"]["MTT_selection_of_B10_Bbar5_transport"] is True, "selection open")
    require(gate["still_open"]["CKM_angle_magnitudes_and_Jarlskog_value"] is True, "CKM open")

    for item in [
        "q79 CKM CP phase contact",
        "heavy-link eight-slot contract",
        "pure C6 Delta_c=(0,0) obstruction",
        "common Fourier transport cancels as gauge",
    ]:
        require(item in next_packet["do_not_reopen"], f"non-reopen missing: {item}")
    for item in [
        "B_10=I_3 selected for 10_M family slot",
        "B_bar5=F selected for bar5_M family slot, or conjugate convention",
        "relative transport is source-owned zero-mode/bundle data",
        "normalization needed before CKM angles/Jarlskog are claimed",
    ]:
        require(item in next_packet["prove_next"], f"prove-next missing: {item}")

    require(cert["exact_conditional_heavy_link_values_found"] is True, "cert found")
    require(cert["selected_heavy_link_values_emitted"] is False, "cert selected")
    require(cert["sector_transport_selection_lemma_closed"] is False, "cert lemma")
    require(cert["CKM_angle_magnitudes_derived"] is False, "cert CKM")
    require(cert["true_SM_equivalence_closed"] is False, "cert true SM")

    require("B_10 = I_3" in note, "note B10")
    require("B_bar5 = F" in note, "note Bbar5")
    require("not selected MTT data yet" in note, "note boundary")
    require(NEXT in note, "note next")

    print("Heavy-link value source search audit passed")
    print(json.dumps({"candidate": str(CANDIDATE.relative_to(ROOT)), "status": STATUS}, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
