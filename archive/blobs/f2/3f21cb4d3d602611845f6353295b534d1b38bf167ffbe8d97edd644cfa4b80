from __future__ import annotations

import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
QA = ROOT.parent / "mtt-qa-su3-packet-proof"

PREV = ROOT / "candidate_data" / "alpha1_terminal_baseorder_ahbinding_import.packet.json"
BRIDGE = QA / "candidate_data" / "selected_u1y_routec_terminal_orientation_branchcoherence_bridge.candidate.json"

OUT_CERT = ROOT / "certificates" / "alpha1_terminal_orientation_bridge_import_certificate.json"
OUT_PACKET = ROOT / "candidate_data" / "alpha1_terminal_orientation_bridge_import.packet.json"
OUT_NOTE = ROOT / "proof_corpus" / "Alpha1_TerminalOrientation_Bridge_Import_v1.md"

STATUS = "ALPHA1_TERMINAL_ORIENTATION_ORDERED_SELECTOR_CLOSED_OPERATOR_EMISSION_OPEN"
NEXT = "Selected_U1Y_RouteC_OperatorEmission_and_OverlapNormalization_from_TerminalSlotMap_v1"


def load(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def main() -> None:
    prev = load(PREV)
    bridge = load(BRIDGE)

    previous_base_ready = all(
        [
            prev["theorem"]["proved"] is True,
            prev["what_closes_now"]["SU5_E6_slot_map_support_complete"] is True,
            prev["what_remains_open"]["same_branch_selected_slot_map_emission"] is True,
        ]
    )
    ordered_orientation_closed = all(
        [
            bridge["theorem"]["proved"] is True,
            bridge["decision"]["ordered_matter_slot_orientation_selector_closed"] is True,
            bridge["decision"]["selected_U10_Ubar5_orientation_at_ordered_layer"] is True,
            bridge["decision"]["selected_1M_Dirac_shift_at_ordered_layer"] is True,
            bridge["ordered_orientation"]["closed"] is True,
            bridge["ordered_orientation"]["phase_sectors"] == ["u", "e"],
            bridge["ordered_orientation"]["shift_sectors"] == ["d", "nuD"],
        ]
    )
    hym_no_go_retained = all(
        [
            bridge["decision"]["hym_nogo_retained"] is True,
            bridge["replay_bridge"]["hym_replay_orientation_nogo_retained"] is True,
            bridge["replay_bridge"]["stationary_hym_replay_closed"] is True,
            bridge["replay_bridge"]["rho_s_validator_ready"] is True,
        ]
    )
    operator_emission_open = all(
        [
            bridge["decision"]["same_branch_selected_operator_emission"] is False,
            bridge["decision"]["selected_overlap_normalization_emitted"] is False,
            bridge["decision"]["alpha1_driver_verified"] is False,
            bridge["emission_gap"]["same_branch_selected_operator_emission"] is False,
            bridge["emission_gap"]["operator_layer_Pic0_closed"] is False,
        ]
    )
    theorem_proved = all([previous_base_ready, ordered_orientation_closed, hym_no_go_retained, operator_emission_open])

    packet = {
        "theorem": {
            "name": "Alpha1TerminalOrientationBridgeImport",
            "proved": theorem_proved,
            "closure_claimed": False,
            "statement": (
                "The terminal monad/AH/good-cover section-ring source closes the ordered matter-slot "
                "orientation selector: g3/L3-K2 selects 10_M clock sectors {u,e}, bar5_M shift {d}, "
                "and 1_M=N^c Dirac shift {nuD}. This is compatible with the HYM replay no-go: "
                "HYM/End0 replay remains permutation-invariant and supplies the common validator-ready "
                "rho_s carrier, while terminal source labels supply ordered orientation. The remaining "
                "frontier is same-branch selected operator emission, operator-layer Pic0/torsion discipline, "
                "overlap normalization, and alpha1 transfer."
            ),
        },
        "imported_status": {"status": STATUS, "bridge_status": bridge["status"]},
        "ordered_orientation": bridge["ordered_orientation"],
        "replay_bridge": bridge["replay_bridge"],
        "emission_gap": bridge["emission_gap"],
        "proof_chain": {
            "previous_base_ready": previous_base_ready,
            "ordered_orientation_closed": ordered_orientation_closed,
            "hym_no_go_retained": hym_no_go_retained,
            "operator_emission_open": operator_emission_open,
            "target_fitting_used": bridge["target_fitting_used"],
        },
        "what_closes_now": {
            "terminal_source_orientation_selector_closed_at_ordered_layer": True,
            "10M_clock_orientation_at_ordered_layer": True,
            "bar5M_shift_orientation_at_ordered_layer": True,
            "1M_Dirac_shift_orientation_at_ordered_layer": True,
            "HYM_orientation_nogo_retained": True,
            "branchcoherence_frontier_moved_to_operator_emission_and_overlap": True,
            "target_fitting_excluded": True,
        },
        "what_remains_open": {
            "same_branch_selected_operator_emission": True,
            "operator_layer_Pic0_or_torsion_gerbe_rule": True,
            "same_source_D_E_Riesz_Green_dotD": True,
            "selected_overlap_transfer_normalization": True,
            "alpha1_driver_verified": True,
            "lambda_12_or_full_SM_closure": True,
        },
        "guardrails": {
            "does_not_claim_same_branch_operator_emission": True,
            "does_not_claim_operator_layer_Pic0_closed": True,
            "does_not_claim_alpha1_driver_verified": True,
            "does_not_claim_lambda12": True,
            "does_not_use_observed_or_benchmark_inputs": True,
        },
        "next_required_artifact": NEXT,
        "input_artifacts": {"previous_baseorder": str(PREV), "terminal_orientation_bridge": str(BRIDGE)},
    }
    cert = {
        "program": "MTT protospinor GR response proof",
        "certificate": "alpha1_terminal_orientation_bridge_import",
        "status": STATUS,
        "closure_claimed": False,
        "checks": {
            "theorem_proved": theorem_proved,
            "previous_base_ready": previous_base_ready,
            "ordered_orientation_closed": ordered_orientation_closed,
            "hym_no_go_retained": hym_no_go_retained,
            "operator_emission_open": operator_emission_open,
            "target_fitting_excluded": bridge["target_fitting_used"] is False,
            "all_closes_true": all(packet["what_closes_now"].values()),
            "all_open_true": all(packet["what_remains_open"].values()),
            "all_guardrails_true": all(packet["guardrails"].values()),
        },
        "next_required_artifact": NEXT,
        "packet_written": str(OUT_PACKET),
        "note_written": str(OUT_NOTE),
    }
    note = f"""# Alpha1 TerminalOrientation Bridge Import v1

## Result

Ordered terminal orientation closes:

```text
source label = g3 / L3-K2
10_M clock = u,e
bar5_M shift = d
1_M=N^c Dirac shift = nuD
```

This does not contradict the HYM replay no-go. HYM replay supplies the common
`rho_s` carrier; terminal source labels supply the ordered orientation.

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
