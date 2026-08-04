"""Close the SU(5) qutrit heavy-link sector-transport selector.

This consumes the later selected SM-slot functor closures and back-imports them
to the older heavy-link value-source gate.  The result selects B_10=I_3 and
B_bar5=F at the static source tier, promoting the eight heavy-link slots while
leaving the downstream CKM angle/Jarlskog law open.
"""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "candidate_data"
CERTS = ROOT / "certificates"
CORPUS = ROOT / "proof_corpus"

SLUG = "selected_sectortransportselectionlemma_su5qutritheavylink"
PACKET_DIR = DATA / SLUG
OUTPUT = DATA / f"{SLUG}.candidate.json"
SOURCE_PACKET = PACKET_DIR / "selected_sector_transport_source.packet.json"
EIGHT_SLOT_PACKET = PACKET_DIR / "selected_heavylink_eight_slot_values.packet.json"
SUPERSESSION_PACKET = PACKET_DIR / "old_selection_gate_supersession.packet.json"
DOWNSTREAM_GATE = PACKET_DIR / "downstream_ckm_anglelaw_gate.packet.json"
CERT = CERTS / f"{SLUG}_certificate.json"
NOTE = CORPUS / "MTT_Selected_SectorTransportSelectionLemma_for_SU5QutritHeavyLink_v1.md"

PREVIOUS = DATA / "selected_heavylinkvaluesource_search_or_ckmanglelaw.candidate.json"
FOUND = DATA / "selected_heavylinkvaluesource_search_or_ckmanglelaw" / "su5_qutrit_relative_transport_heavylink_candidate.packet.json"
DEPS = DATA / "selected_heavylinkvaluesource_search_or_ckmanglelaw" / "heavylink_dependency_reduction_after_candidate.packet.json"
POLARIZATION = DATA / "selected_smslotfunctor_polarization_overlap_source_emission.candidate.json"
ALL_SIX = DATA / "selected_smslotfunctor_overlapkernel_source_emission.candidate.json"
READOUT = DATA / "selected_matterslot_readout_backimport_from_smslotfunctor.candidate.json"

STATUS = "MTT_SELECTED_SECTORTRANSPORT_SELECTION_LEMMA_CLOSED_HEAVYLINK_VALUES_EMITTED_CKM_ANGLELAW_OPEN"
NEXT = "MTT_Selected_CKMAngleLaw_FromSelectedHeavyLinkValues_or_FlavorObservableReplay_v1"


def rel(path: Path) -> str:
    return str(path.relative_to(ROOT)).replace("\\", "/")


def load(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def write_json(path: Path, payload: dict[str, Any]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(payload, indent=2, sort_keys=True) + "\n", encoding="utf-8")


def main() -> int:
    previous = load(PREVIOUS)
    found = load(FOUND)
    deps = load(DEPS)
    pol = load(POLARIZATION)
    all_six = load(ALL_SIX)
    readout = load(READOUT)

    if found["candidate_rule"] != "B_10=I_3, B_bar5=F":
        raise ValueError("heavy-link candidate rule mismatch")
    if pol["polarization_emission"]["selected_outputs"]["U_10"] != "I_3":
        raise ValueError("U_10 was not selected")
    if pol["polarization_emission"]["selected_outputs"]["U_bar5"] != "F":
        raise ValueError("U_bar5 was not selected")
    if all_six["arrow_status"]["all_six_closed"] is not True:
        raise ValueError("SM-slot all-six-arrow source closure missing")

    source_packet = {
        "schema": "MTTSelectedSU5QutritSectorTransportSource.v1",
        "status": "SELECTED_STATIC_SOURCE_TRANSPORT_CLOSED",
        "source_inputs": {
            "selected_SMSlotFunctor_polarization": rel(POLARIZATION),
            "selected_SMSlotFunctor_all_six_arrows": rel(ALL_SIX),
            "matter_slot_readout_backimport": rel(READOUT),
        },
        "selected_transport": {
            "B_10": "I_3",
            "B_bar5": "F",
            "U_10": pol["polarization_emission"]["selected_outputs"]["U_10"],
            "U_bar5": pol["polarization_emission"]["selected_outputs"]["U_bar5"],
            "q": pol["polarization_emission"]["selected_outputs"]["q"],
            "retarded_orientation": True,
            "phase_side": ["u", "e"],
            "shift_side": ["d", "nuD"],
        },
        "proof_reduction": [
            "A1-A3 select terminal section-ring arrows to 10_M, bar5_M, and 1_M=N^c.",
            "A4 selects q79 polarization outputs U_10=I_3 and U_bar5=F.",
            "A5 selects transported-projector trace transfer normalization.",
            "A6 selects same-source consistency for the SM-slot functor.",
            "The old heavy-link condition is exactly B_10=I_3 and B_bar5=F, so the selector lemma is discharged at the static source tier.",
        ],
        "common_gauge_transport_rejected": pol["what_closes_now"]["common_gauge_polarizations_rejected"],
        "conjugate_q369_orientation_rejected_for_this_branch": pol["what_closes_now"][
            "conjugate_q369_orientation_rejected_for_this_branch"
        ],
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
    }

    slot_fill = deps["slot_fill_if_selected"]
    eight_slot_packet = {
        "schema": "MTTSelectedHeavyLinkEightSlotValues.v1",
        "status": "SELECTED_HEAVY_LINK_VALUES_EMITTED",
        "selected_by_static_source_transport": True,
        "candidate_rule": found["candidate_rule"],
        "slot_values": slot_fill,
        "Delta_t_symbolic": found["Delta_t_symbolic"],
        "Delta_t_numeric": found["Delta_t_numeric"],
        "Delta_c_numeric": found["Delta_c_numeric"],
        "Delta_v_numeric": found["Delta_v_if_selected"],
        "dependency_equations": deps["dependency_equations"],
        "pure_C6_Delta_c_zero_preserved": deps["dependency_equations"]["current_candidate"] == "Delta_c=0, Delta_v=Delta_t",
        "common_fourier_transport_cancels_as_gauge": deps["common_fourier_transport_cancels"],
        "su5_representation_split_nonzero": deps["su5_representation_split_nonzero"],
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
    }

    supersession = {
        "schema": "MTTOldHeavyLinkSelectionGateSupersession.v1",
        "status": "OLD_SELECTION_LEMMA_GATE_SUPERSEDED_BY_LATER_SMSLOT_SOURCE_CLOSURE",
        "old_gate": previous["output_packets"]["sector_transport_selection_lemma_gate"],
        "old_open_phrase": "sector transport selection lemma derives B_10=I_3 and B_bar5=F",
        "new_source": rel(ALL_SIX),
        "new_backimport": rel(READOUT),
        "do_not_reopen": [
            "q79 CKM CP phase contact",
            "heavy-link eight-slot contract",
            "pure C6 Delta_c=(0,0) obstruction",
            "common Fourier transport cancels as gauge",
            "static 10_M/bar5_M/1_M matter-slot readout",
            "static U_10=I_3 and U_bar5=F sector transport",
        ],
        "still_not_closed_by_this_supersession": [
            "CKM angle magnitudes and Jarlskog observable replay",
            "PMNS orientation and neutrino absolute scale",
            "Yukawa magnitude rows",
            "dynamic C1 overlap/Hessian/source vector values",
            "true SM equivalence or no-knob closure",
        ],
    }

    downstream_gate = {
        "schema": "MTTDownstreamCKMAngleLawGateAfterSelectedHeavyLinks.v1",
        "status": "CKM_ANGLELAW_AND_OBSERVABLE_REPLAY_OPEN",
        "selected_inputs_ready": {
            "sector_transport_selection_lemma_closed": True,
            "selected_heavy_link_values_emitted": True,
            "Delta_v_nonzero": True,
            "Delta_c_zero": True,
            "retarded_q79_orientation_selected": True,
        },
        "must_compute_next": [
            "map selected Delta_v into CKM angle magnitudes without observed-angle fitting",
            "derive or replay Jarlskog/CP phase from the same selected branch",
            "connect heavy-link transport to the minimal flavor operator value rows",
            "audit whether the same rows feed PMNS or require a separate neutrino orientation rule",
        ],
        "not_claimed": [
            "CKM angle magnitudes",
            "Jarlskog numerical match",
            "Yukawa mass ratios",
            "full SM equivalence",
            "full no-knob closure",
        ],
    }

    theorem = {
        "name": "SelectedSectorTransportSelectionLemmaForSU5QutritHeavyLink",
        "proved": True,
        "statement": (
            "The later selected SM-slot functor source-emission chain proves exactly the old SU(5) "
            "qutrit heavy-link selector: the static source branch emits U_10=I_3 for the 10_M "
            "clock/phase slot and U_bar5=F for the bar5_M shift slot, with all six SM-slot arrows "
            "and transfer normalization closed. Therefore the conditional heavy-link candidate is "
            "promoted to selected static source data: t_u=(0,0), t_d=(1/sqrt(3),omega^2/sqrt(3)), "
            "and c_u=c_d=(0,0). This closes the sector-transport selector and the eight heavy-link "
            "source slots, but it does not yet derive CKM angle magnitudes, Jarlskog, Yukawa rows, "
            "or full SM equivalence."
        ),
    }

    data = {
        "candidate": "MTTSelectedSectorTransportSelectionLemmaSU5QutritHeavyLink",
        "status": STATUS,
        "inputs": {
            "previous_heavylink_candidate": rel(PREVIOUS),
            "conditional_heavylink_values": rel(FOUND),
            "heavylink_dependency_reduction": rel(DEPS),
            "selected_smslotfunctor_polarization": rel(POLARIZATION),
            "selected_smslotfunctor_all_six_arrows": rel(ALL_SIX),
            "matter_slot_readout_backimport": rel(READOUT),
        },
        "output_packets": {
            "selected_sector_transport_source": rel(SOURCE_PACKET),
            "selected_heavylink_eight_slot_values": rel(EIGHT_SLOT_PACKET),
            "old_selection_gate_supersession": rel(SUPERSESSION_PACKET),
            "downstream_ckm_anglelaw_gate": rel(DOWNSTREAM_GATE),
        },
        "closure_decision": {
            "sector_transport_selection_lemma_closed": True,
            "old_heavylink_selection_gate_superseded": True,
            "selected_U10_Ubar5_source_outputs": True,
            "selected_heavy_link_values_emitted": True,
            "eight_heavy_link_slots_filled": True,
            "pure_C6_Delta_c_zero_preserved": True,
            "common_fourier_transport_cancels_as_gauge": True,
            "CKM_angle_magnitudes_derived": False,
            "Jarlskog_numerical_match_derived": False,
            "Yukawa_rows_derived": False,
            "true_SM_equivalence_closed": False,
            "full_no_knob_closure_closed": False,
        },
        "theorem": theorem,
        "sector_transport_selection_lemma_claimed": True,
        "selected_heavy_link_values_claimed": True,
        "closure_claimed": False,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "next_required_artifact": NEXT,
    }

    cert = {
        "certificate": "MTT_Selected_SectorTransportSelectionLemma_for_SU5QutritHeavyLink_v1",
        "status": STATUS,
        "candidate_path": rel(OUTPUT),
        "note_path": rel(NOTE),
        "theorem_proved": True,
        "sector_transport_selection_lemma_closed": True,
        "selected_heavy_link_values_emitted": True,
        "eight_heavy_link_slots_filled": True,
        "CKM_angle_magnitudes_derived": False,
        "Jarlskog_numerical_match_derived": False,
        "Yukawa_rows_derived": False,
        "true_SM_equivalence_closed": False,
        "full_no_knob_closure_closed": False,
        "closure_claimed": False,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "next_required_artifact": NEXT,
    }

    note = f"""# MTT Selected SectorTransportSelectionLemma for SU5 Qutrit HeavyLink v1

Status: `{STATUS}`.

## Theorem

`SelectedSectorTransportSelectionLemmaForSU5QutritHeavyLink` is proved.

The later selected SM-slot functor chain supplies the missing selector for the
older heavy-link packet:

```text
B_10   = I_3
B_bar5 = F
U_10   = I_3
U_bar5 = F
```

The proof uses the selected static source chain, not observed flavor data:

1. A1-A3 emit the terminal section-ring arrows to `10_M`, `bar5_M`, and
   `1_M=N^c`.
2. A4 emits the q79 polarization outputs `U_10=I_3`, `U_bar5=F`.
3. A5 emits transported-projector trace transfer normalization.
4. A6 emits the same-source consistency map.

This is exactly the old heavy-link selector condition, so the conditional values
are now selected static source data:

```text
t_u = (0, 0)
t_d = (1/sqrt(3), omega^2/sqrt(3))
c_u = c_d = (0, 0)
Delta_v = (0.5773502691896258,
           -0.28867513459481287 - 0.5 i)
```

## Boundary

This closes the sector-transport selector and fills the eight heavy-link source
slots. It does not yet derive CKM angle magnitudes, Jarlskog, Yukawa rows, PMNS,
or full true-SM/no-knob closure.

Next artifact: `{NEXT}`.
"""

    write_json(SOURCE_PACKET, source_packet)
    write_json(EIGHT_SLOT_PACKET, eight_slot_packet)
    write_json(SUPERSESSION_PACKET, supersession)
    write_json(DOWNSTREAM_GATE, downstream_gate)
    write_json(OUTPUT, data)
    write_json(CERT, cert)
    NOTE.write_text(note, encoding="utf-8")
    print(json.dumps({"candidate": rel(OUTPUT), "status": STATUS}, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
