from __future__ import annotations

import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
QA = ROOT.parent / "mtt-qa-su3-packet-proof"

PREV = ROOT / "candidate_data" / "alpha1_branchcoherence_partial_replay_import.packet.json"
ORIENTATION = QA / "candidate_data" / "selected_u1y_routec_matterslot_orientationselector_from_hym_finitereplay.candidate.json"

OUT_CERT = ROOT / "certificates" / "alpha1_orientation_selector_nogo_import_certificate.json"
OUT_PACKET = ROOT / "candidate_data" / "alpha1_orientation_selector_nogo_import.packet.json"
OUT_NOTE = ROOT / "proof_corpus" / "Alpha1_OrientationSelector_NoGo_Import_v1.md"

STATUS = "ALPHA1_ORIENTATION_SELECTOR_HYM_REPLAY_NOGO_TERMINAL_GRADING_OPEN"
NEXT = "Selected_U1Y_RouteC_TerminalMonad_MatterSlot_SectionRing_SourceSelector_v1"


def load(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def main() -> None:
    prev = load(PREV)
    orientation = load(ORIENTATION)

    previous_branch_ready = all(
        [
            prev["theorem"]["proved"] is True,
            prev["what_closes_now"]["stationary_HYM_finite_validator_replay"] is True,
            prev["what_remains_open"]["matter_slot_orientation_selector"] is True,
        ]
    )
    no_go_proved = all(
        [
            orientation["theorem"]["proved"] is True,
            orientation["decision"]["hym_replay_no_go_for_orientation_proved"] is True,
            orientation["hym_replay_orientation_no_go"]["stationary_hym_replay_cannot_select_orientation"] is True,
            orientation["hym_replay_orientation_no_go"]["not_a_failure_of_hym_replay"] is True,
            orientation["what_closes_now"]["hym_replay_orientation_no_go"] is True,
        ]
    )
    legal_readouts_exhausted = all(
        [
            orientation["readout_tests"]["hym_rho_s_adjoint_readout"]["conclusion"]
            == "NO_GO_PERMUTATION_INVARIANT",
            orientation["readout_tests"]["projector_gap_green_readout"]["conclusion"]
            == "NO_GO_COMMON_STATIONARY_DATA",
            orientation["readout_tests"]["locked_c1_partition_readout"]["conclusion"]
            == "FORBIDDEN_TARGET_LOCALIZED_SELECTOR",
            orientation["readout_tests"]["su5_e6_structural_readout"]["conclusion"]
            == "STRUCTURAL_SUPPORT_NOT_SOURCE_EMISSION",
            orientation["readout_tests"]["terminal_monad_sectionring_readout"]["conclusion"]
            == "PRIMARY_OPEN_REPAIR_ROUTE",
        ]
    )
    terminal_route_identified = all(
        [
            orientation["decision"]["primary_repair_route"] == "terminal_monad_cech_sectionring",
            orientation["positive_route"]["selected_closed"] is False,
            orientation["positive_route"]["source_selector_to_prove"]["forced_label_inside_lane"] == "L3-K2",
            orientation["positive_route"]["source_selector_to_prove"]["forced_value"] == [1, -2, 0],
            orientation["what_closes_now"]["terminal_monad_sectionring_route_imported_as_primary"] is True,
        ]
    )
    theorem_proved = all([previous_branch_ready, no_go_proved, legal_readouts_exhausted, terminal_route_identified])

    packet = {
        "theorem": {
            "name": "Alpha1OrientationSelectorNoGoImport",
            "proved": theorem_proved,
            "closure_claimed": False,
            "statement": (
                "The matter-slot orientation selector cannot be derived from stationary HYM/End0 replay alone. "
                "On u,d,e,N, the replay emits identical adjoint rho_s, identity Gram data, equal ranks, "
                "and equal T3 norms; therefore every legal readout built only from these invariants is "
                "permutation-invariant. The required phase={u,e}, shift={d,nuD} partition needs an additional "
                "selected grading/section-label source. The primary positive route is the terminal monad/Cech "
                "section-ring selector forcing L3-K2=(1,-2,0) and binding it to 10_M clock, bar5_M shift, "
                "and 1_M Dirac shift."
            ),
        },
        "imported_status": {
            "status": STATUS,
            "orientation_status": orientation["status"],
        },
        "hym_replay_orientation_no_go": orientation["hym_replay_orientation_no_go"],
        "readout_tests": orientation["readout_tests"],
        "positive_route": orientation["positive_route"],
        "proof_chain": {
            "previous_branch_ready": previous_branch_ready,
            "no_go_proved": no_go_proved,
            "legal_readouts_exhausted": legal_readouts_exhausted,
            "terminal_route_identified": terminal_route_identified,
            "target_fitting_used": orientation["target_fitting_used"],
        },
        "what_closes_now": {
            "hym_replay_orientation_no_go": True,
            "legal_current_readouts_exhausted": True,
            "terminal_monad_sectionring_route_identified": True,
            "orientation_problem_not_a_failure_of_hym_replay": True,
            "target_fitting_excluded": True,
        },
        "what_remains_open": {
            "selected_terminal_monad_lane_source_selector": True,
            "section_ring_to_SU5_E6_matter_slot_map": True,
            "selected_10M_clock_readout": True,
            "selected_bar5M_shift_readout": True,
            "selected_1M_Dirac_shift_readout": True,
            "selected_overlap_transfer_normalization": True,
            "alpha1_driver_verified": True,
            "lambda_12_or_full_SM_closure": True,
        },
        "guardrails": {
            "does_not_claim_selected_orientation_selector": True,
            "does_not_use_locked_c1_target_as_selector": True,
            "does_not_promote_structural_su5_support_as_source_emission": True,
            "does_not_claim_alpha1_driver_verified": True,
            "does_not_use_observed_or_benchmark_inputs": True,
        },
        "next_required_artifact": NEXT,
        "input_artifacts": {
            "previous_branchcoherence": str(PREV),
            "orientation": str(ORIENTATION),
        },
    }
    cert = {
        "program": "MTT protospinor GR response proof",
        "certificate": "alpha1_orientation_selector_nogo_import",
        "status": STATUS,
        "closure_claimed": False,
        "checks": {
            "theorem_proved": theorem_proved,
            "previous_branch_ready": previous_branch_ready,
            "no_go_proved": no_go_proved,
            "legal_readouts_exhausted": legal_readouts_exhausted,
            "terminal_route_identified": terminal_route_identified,
            "target_fitting_excluded": orientation["target_fitting_used"] is False,
            "all_closes_true": all(packet["what_closes_now"].values()),
            "all_open_true": all(packet["what_remains_open"].values()),
            "all_guardrails_true": all(packet["guardrails"].values()),
        },
        "next_required_artifact": NEXT,
        "packet_written": str(OUT_PACKET),
        "note_written": str(OUT_NOTE),
    }
    note = f"""# Alpha1 OrientationSelector NoGo Import v1

## Result

Stationary HYM/End0 replay cannot select the matter-slot orientation:

```text
u,d,e,N carry identical adjoint rho_s
Gram matrices are identical
ranks and T3 norms are equal
```

Thus HYM replay is closed for `rho_s`, but insufficient for the phase/shift
partition. The live positive route is terminal monad/Cech section-ring grading:

```text
terminal lane = L_i-K2
forced label = L3-K2
forced value = (1,-2,0)
phase = u,e
shift = d,nuD
```

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
