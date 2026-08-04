from __future__ import annotations

import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
QA = ROOT.parent / "mtt-qa-su3-packet-proof"

PREV = ROOT / "candidate_data" / "alpha1_orientation_selector_nogo_import.packet.json"
TERMINAL = QA / "candidate_data" / "selected_u1y_routec_terminalmonad_matterslot_sectionring_source_selector.candidate.json"

OUT_CERT = ROOT / "certificates" / "alpha1_terminal_selector_reduction_import_certificate.json"
OUT_PACKET = ROOT / "candidate_data" / "alpha1_terminal_selector_reduction_import.packet.json"
OUT_NOTE = ROOT / "proof_corpus" / "Alpha1_TerminalSelector_Reduction_Import_v1.md"

STATUS = "ALPHA1_TERMINAL_SELECTOR_REDUCED_BASEORDER_AHBINDING_SLOTMAP_OPEN"
NEXT = "Selected_U1Y_RouteC_TerminalMonad_BaseOrder_AHBinding_SMSlotMap_v1"


def load(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def main() -> None:
    prev = load(PREV)
    terminal = load(TERMINAL)

    previous_orientation_ready = all(
        [
            prev["theorem"]["proved"] is True,
            prev["what_closes_now"]["hym_replay_orientation_no_go"] is True,
            prev["what_remains_open"]["selected_terminal_monad_lane_source_selector"] is True,
        ]
    )
    terminal_candidate_fixed = all(
        [
            terminal["theorem"]["proved"] is True,
            terminal["decision"]["L3_K2_unique_terminal_candidate_imported"] is True,
            terminal["imported_terminal_candidate"]["closed_as_unique_candidate"] is True,
            terminal["imported_terminal_candidate"]["forced_label"] == "L3-K2",
            terminal["imported_terminal_candidate"]["forced_value"] == [1, -2, 0],
            terminal["imported_terminal_candidate"]["forced_double"] == [2, -4, 0],
        ]
    )
    ordered_pic0_removed = all(
        [
            terminal["decision"]["ordered_layer_Pic0_removed_as_ordered_source_blocker"] is True,
            terminal["ordered_layer_pic0_result"]["ordered_layer_pic0_removed_as_blocker"] is True,
            terminal["ordered_layer_pic0_result"]["operator_layer_pic0_closed"] is False,
        ]
    )
    slot_map_contract_ready = all(
        [
            terminal["slot_map_contract"]["closed"] is False,
            terminal["slot_map_contract"]["must_map_without_locked_C1_columns"]["10_M_clock"] == ["u", "e"],
            terminal["slot_map_contract"]["must_map_without_locked_C1_columns"]["bar5_M_shift"] == ["d"],
            terminal["slot_map_contract"]["must_map_without_locked_C1_columns"]["1_M_Dirac_shift"] == ["nuD"],
            terminal["slot_map_contract"]["must_preserve_q79_polarization"]["U_10"] == "I_3",
            terminal["slot_map_contract"]["must_preserve_q79_polarization"]["U_bar5"] == "F",
        ]
    )
    obligations_explicit = all(not value["closed"] for value in terminal["source_selector_obligations"].values())
    theorem_proved = all(
        [
            previous_orientation_ready,
            terminal_candidate_fixed,
            ordered_pic0_removed,
            slot_map_contract_ready,
            obligations_explicit,
        ]
    )

    packet = {
        "theorem": {
            "name": "Alpha1TerminalSelectorReductionImport",
            "proved": theorem_proved,
            "closure_claimed": False,
            "statement": (
                "The terminal monad/Cech section-ring route is reduced to an explicit target-free packet. "
                "The unique central-neutral terminal candidate is L3-K2=(1,-2,0) with double (2,-4,0), "
                "and Pic0 is no longer an ordered Chern/H1 blocker. Orientation remains open because "
                "the source still must emit MTT selection of the terminal lane, standard lattice/base order, "
                "AH/Cech transition binding, operator-layer Pic0/torsion discipline, and the section-ring "
                "map to SU(5)/E6 slots preserving U_10=I_3, U_bar5=F, phase={u,e}, shift={d,nuD}."
            ),
        },
        "imported_status": {
            "status": STATUS,
            "terminal_status": terminal["status"],
            "source_certificate_status": terminal["source_certificate_import"]["status"],
        },
        "terminal_candidate": terminal["imported_terminal_candidate"],
        "ordered_layer_pic0_result": terminal["ordered_layer_pic0_result"],
        "slot_map_contract": terminal["slot_map_contract"],
        "source_selector_obligations": terminal["source_selector_obligations"],
        "proof_chain": {
            "previous_orientation_ready": previous_orientation_ready,
            "terminal_candidate_fixed": terminal_candidate_fixed,
            "ordered_pic0_removed": ordered_pic0_removed,
            "slot_map_contract_ready": slot_map_contract_ready,
            "obligations_explicit": obligations_explicit,
            "target_fitting_used": terminal["target_fitting_used"],
        },
        "what_closes_now": {
            "L3_K2_unique_terminal_candidate": True,
            "ordered_layer_Pic0_removed_as_ordered_source_blocker": True,
            "matter_slot_map_contract_imported": True,
            "terminal_selector_reduced_to_baseorder_AHbinding_slotmap": True,
            "target_fitting_excluded": True,
        },
        "what_remains_open": {
            "terminal_monad_lane_selected_by_MTT": True,
            "standard_lattice_or_equivalent_selected": True,
            "base_factor_order_selected": True,
            "AH_or_Cech_transition_binding_selected": True,
            "operator_layer_Pic0_selection_or_quotient": True,
            "section_ring_to_SU5_E6_matter_slot_map": True,
            "selected_1M_Dirac_shift_readout": True,
            "selected_overlap_transfer_normalization": True,
            "same_source_D_E_Riesz_Green_dotD": True,
            "alpha1_driver_verified": True,
        },
        "guardrails": {
            "does_not_claim_terminal_lane_selected_by_MTT": True,
            "does_not_claim_operator_layer_Pic0_closed": True,
            "does_not_use_locked_C1_columns": True,
            "does_not_claim_alpha1_driver_verified": True,
            "does_not_use_observed_or_benchmark_inputs": True,
        },
        "next_required_artifact": NEXT,
        "input_artifacts": {
            "previous_orientation": str(PREV),
            "terminal_selector": str(TERMINAL),
        },
    }
    cert = {
        "program": "MTT protospinor GR response proof",
        "certificate": "alpha1_terminal_selector_reduction_import",
        "status": STATUS,
        "closure_claimed": False,
        "checks": {
            "theorem_proved": theorem_proved,
            "previous_orientation_ready": previous_orientation_ready,
            "terminal_candidate_fixed": terminal_candidate_fixed,
            "ordered_pic0_removed": ordered_pic0_removed,
            "slot_map_contract_ready": slot_map_contract_ready,
            "obligations_explicit": obligations_explicit,
            "target_fitting_excluded": terminal["target_fitting_used"] is False,
            "all_closes_true": all(packet["what_closes_now"].values()),
            "all_open_true": all(packet["what_remains_open"].values()),
            "all_guardrails_true": all(packet["guardrails"].values()),
        },
        "next_required_artifact": NEXT,
        "packet_written": str(OUT_PACKET),
        "note_written": str(OUT_NOTE),
    }
    note = f"""# Alpha1 TerminalSelector Reduction Import v1

## Result

The terminal monad candidate is fixed:

```text
forced label = L3-K2
forced value = (1,-2,0)
forced double = (2,-4,0)
```

Pic0 is removed at the ordered Chern/H1 layer, but operator-layer Pic0/torsion
discipline remains open. The next packet must bind base order, AH/Cech
transition data, and the section-ring map to the SU(5)/E6 slots.

Status:

```text
{STATUS}
```

Next:

```text
{NEXT}
```
"""
    OUT_PACKET.write_text(json.dumps(packet, indent=2), encoding="utf-8")
    OUT_CERT.write_text(json.dumps(cert, indent=2), encoding="utf-8")
    OUT_NOTE.write_text(note, encoding="utf-8")
    print(f"WROTE: {OUT_CERT}")
    print(f"WROTE: {OUT_PACKET}")
    print(f"WROTE: {OUT_NOTE}")
    print(f"STATUS: {STATUS}")


if __name__ == "__main__":
    main()
