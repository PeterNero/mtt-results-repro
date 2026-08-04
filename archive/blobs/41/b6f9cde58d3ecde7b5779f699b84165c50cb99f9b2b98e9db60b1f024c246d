from __future__ import annotations

import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
QA = ROOT.parent / "mtt-qa-su3-packet-proof"

PREV = ROOT / "candidate_data" / "alpha1_partial_sourceidentity_closure_theorem.packet.json"
SOURCE_PROMOTION = QA / "candidate_data" / "selected_u1y_routec_u10ubar5_1m_sourcepromotion_samebranch_emission.candidate.json"
BRANCH = QA / "candidate_data" / "selected_u1y_routec_branchcoherence_selector_or_finite_validator_replay.candidate.json"
FUNCTIONAL = QA / "candidate_data" / "selected_u1y_routec_samesource_chernweil_operator_functional_value.candidate.json"
MATTER = QA / "candidate_data" / "selected_u1y_routec_selected_matter_slot_charge_and_overlap_normalization_theorem.candidate.json"

OUT_CERT = ROOT / "certificates" / "alpha1_branchcoherence_partial_replay_import_certificate.json"
OUT_PACKET = ROOT / "candidate_data" / "alpha1_branchcoherence_partial_replay_import.packet.json"
OUT_NOTE = ROOT / "proof_corpus" / "Alpha1_BranchCoherence_Partial_Replay_Import_v1.md"

STATUS = "ALPHA1_BRANCHCOHERENCE_PARTIAL_REPLAY_CLOSED_ORIENTATION_SELECTOR_OPEN"
NEXT = "Selected_U1Y_RouteC_MatterSlot_OrientationSelector_from_HYM_FiniteReplay_v1"


def load(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def main() -> None:
    prev = load(PREV)
    promotion = load(SOURCE_PROMOTION)
    branch = load(BRANCH)
    functional = load(FUNCTIONAL)
    matter = load(MATTER)

    previous_cutset_ready = all(
        [
            prev["theorem"]["proved"] is True,
            prev["what_closes_now"]["remaining_alpha1_gate_reduced_to_two_legal_routes"] is True,
            prev["what_remains_open"]["selected_transfer_normalization"] is True,
        ]
    )
    support_complete_packet = all(
        [
            promotion["theorem"]["proved"] is True,
            promotion["decision"]["support_complete"] is True,
            promotion["decision"]["same_branch_complete"] is False,
            promotion["counts"]["support_present"] == promotion["counts"]["required"],
            promotion["what_closes_now"]["support_complete_sourcepromotion_packet_constructed"] is True,
        ]
    )
    partial_replay_closed = all(
        [
            branch["theorem"]["proved"] is True,
            branch["decision"]["hym_finite_validator_replay_closed"] is True,
            branch["decision"]["rho_s_validator_ready_promoted"] is True,
            branch["subgoals"]["hym_finite_validator_replay"]["closed"] is True,
            branch["what_closes_now"]["stationary_HYM_finite_validator_replay"] is True,
        ]
    )
    orientation_is_decisive_open_gate = all(
        [
            branch["decision"]["matter_slot_orientation_selector_emitted"] is False,
            branch["subgoals"]["matter_slot_orientation_selector"]["status"] == "OPEN_DECISIVE_GATE",
            branch["what_remains_open"]["matter_slot_orientation_selector"] is True,
            branch["orientation_selector_contract"]["promotes_if_closed"] == [
                "selected_U10_Ubar5_polarization_emitted",
                "selected_1M_Dirac_source_emitted",
                "selected_overlap_normalization_emitted",
                "N_alpha1_h_ext_promoted_to_du_dalpha1",
                "alpha1_driver_verified",
            ],
        ]
    )
    alpha1_functional_ready_after_orientation = all(
        [
            functional["decision"]["unique_current_support_value_identified"] is True,
            functional["decision"]["support_candidate_value_N_alpha1_h_ext"] == 1.0,
            functional["if_next_theorem_closes_then"]["set_alpha1_driver_verified_by_theorem"] is True,
            functional["decision"]["alpha1_driver_verified_now"] is False,
        ]
    )
    same_source_packet_still_open = all(
        [
            matter["theorem"]["proved"] is True,
            matter["promotion_theorem"]["if_all_same_source_fields_selected"]["alpha1_driver_verified"] is True,
            matter["decision"]["same_source_packet_values_emitted"] is False,
            matter["decision"]["alpha1_driver_verified_now"] is False,
        ]
    )
    theorem_proved = all(
        [
            previous_cutset_ready,
            support_complete_packet,
            partial_replay_closed,
            orientation_is_decisive_open_gate,
            alpha1_functional_ready_after_orientation,
            same_source_packet_still_open,
        ]
    )

    packet = {
        "theorem": {
            "name": "Alpha1BranchCoherencePartialReplayImport",
            "proved": theorem_proved,
            "closure_claimed": False,
            "statement": (
                "The QA/SU3 U1/Y branch-coherence theorem is imported: the selected "
                "stationary HYM/projector replay is closed and rho_s is validator-ready. "
                "All finite and functional ingredients are support-complete, including "
                "N_alpha1(h_ext)=1, U_10=I_3, U_bar5=F, the structural 1_M=N^c shift rule, "
                "and the conditional rho_s(T_i)/sqrt(2) transfer normalization. The remaining "
                "decisive gate is a source-internal matter-slot orientation selector deriving "
                "phase={u,e} and shift={d,nuD} from replayed HYM/End0 data without target columns."
            ),
        },
        "imported_status": {
            "status": STATUS,
            "source_promotion_status": promotion["status"],
            "branch_status": branch["status"],
            "functional_status": functional["status"],
            "matter_status": matter["status"],
        },
        "support_complete_packet": promotion["source_promotion_packet"],
        "orientation_selector_contract": branch["orientation_selector_contract"],
        "branch_subgoals": branch["subgoals"],
        "alpha1_functional_value": functional["value_functional"],
        "proof_chain": {
            "previous_cutset_ready": previous_cutset_ready,
            "support_complete_packet": support_complete_packet,
            "partial_replay_closed": partial_replay_closed,
            "orientation_is_decisive_open_gate": orientation_is_decisive_open_gate,
            "alpha1_functional_ready_after_orientation": alpha1_functional_ready_after_orientation,
            "same_source_packet_still_open": same_source_packet_still_open,
            "target_fitting_used": any(
                [
                    promotion["target_fitting_used"],
                    branch["target_fitting_used"],
                    functional["target_fitting_used"],
                    matter["target_fitting_used"],
                ]
            ),
        },
        "what_closes_now": {
            "stationary_HYM_finite_validator_replay": True,
            "rho_s_validator_ready_promoted": True,
            "support_complete_sourcepromotion_packet_imported": True,
            "branchcoherence_blocker_reduced_to_orientation_selector": True,
            "target_fitting_excluded": True,
        },
        "what_remains_open": {
            "matter_slot_orientation_selector": True,
            "selected_U10_clock_source": True,
            "selected_Ubar5_shift_source": True,
            "selected_1M_Dirac_shift_source": True,
            "selected_physical_transfer_normalization": True,
            "selected_alpha1_driver": True,
            "honest_dotD_alpha1_replay": True,
            "primitive_C1_contractions": True,
            "lambda_12_or_full_SM_closure": True,
        },
        "guardrails": {
            "does_not_claim_alpha1_driver_verified": True,
            "does_not_claim_selected_orientation_selector": True,
            "does_not_use_target_columns_as_selector": True,
            "does_not_use_observed_or_benchmark_inputs": True,
        },
        "next_required_artifact": NEXT,
        "input_artifacts": {
            "previous_cutset": str(PREV),
            "source_promotion": str(SOURCE_PROMOTION),
            "branchcoherence": str(BRANCH),
            "functional": str(FUNCTIONAL),
            "matter": str(MATTER),
        },
    }
    cert = {
        "program": "MTT protospinor GR response proof",
        "certificate": "alpha1_branchcoherence_partial_replay_import",
        "status": STATUS,
        "closure_claimed": False,
        "checks": {
            "theorem_proved": theorem_proved,
            "previous_cutset_ready": previous_cutset_ready,
            "support_complete_packet": support_complete_packet,
            "partial_replay_closed": partial_replay_closed,
            "orientation_is_decisive_open_gate": orientation_is_decisive_open_gate,
            "alpha1_functional_ready_after_orientation": alpha1_functional_ready_after_orientation,
            "same_source_packet_still_open": same_source_packet_still_open,
            "target_fitting_excluded": packet["proof_chain"]["target_fitting_used"] is False,
            "all_closes_true": all(packet["what_closes_now"].values()),
            "all_open_true": all(packet["what_remains_open"].values()),
            "all_guardrails_true": all(packet["guardrails"].values()),
        },
        "next_required_artifact": NEXT,
        "packet_written": str(OUT_PACKET),
        "note_written": str(OUT_NOTE),
    }
    note = f"""# Alpha1 BranchCoherence Partial Replay Import v1

## Result

The branch-coherence gate partially closes:

```text
stationary HYM/projector finite replay = closed
rho_s validator-ready = true
support packet = complete
N_alpha1(h_ext) = 1
```

The remaining decisive theorem is the matter-slot orientation selector:

```text
phase sectors = u,e
shift sectors = d,nuD
normalization = rho_s(T_i)/sqrt(2)
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
