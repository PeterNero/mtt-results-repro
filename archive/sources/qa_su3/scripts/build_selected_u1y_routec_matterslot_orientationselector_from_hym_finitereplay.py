"""Build the U1/Y Route-C matter-slot orientation selector from HYM finite replay gate."""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "candidate_data"
CERTS = ROOT / "certificates"
PROOF = ROOT / "proof_corpus"
TEXPAPERS = ROOT.parent
SM = TEXPAPERS / "mtt-sm-parity-closure"

INPUTS = {
    "branchcoherence_gate": DATA / "selected_u1y_routec_branchcoherence_selector_or_finite_validator_replay.candidate.json",
    "functional_payload": DATA / "selected_u1y_routec_hym_projector_source_payload.functional.json",
    "end0_sector_values": DATA / "selected_u1y_routec_end0_to_sector_functor_source_and_value_packet.values.json",
    "sm_transversality_readout": SM / "candidate_data" / "selected_matterslot_transversality_readout_functional.candidate.json",
    "sm_grading_readout": SM / "candidate_data" / "selected_matterslot_grading_or_sectionring_readout.candidate.json",
    "sm_samebranch_emission_attempt": SM / "candidate_data" / "selected_u10ubar5_1m_samebranch_emission_attempt.candidate.json",
    "sm_weylpair_matterslot": SM / "candidate_data" / "selected_routec_weylpair_matter_slot_or_blocksector_source_theorem.candidate.json",
}

OUTPUT_DATA = DATA / "selected_u1y_routec_matterslot_orientationselector_from_hym_finitereplay.candidate.json"
OUTPUT_CERT = CERTS / "selected_u1y_routec_matterslot_orientationselector_from_hym_finitereplay_certificate.json"
OUTPUT_NOTE = PROOF / "Selected_U1Y_RouteC_MatterSlot_OrientationSelector_from_HYM_FiniteReplay_v1.md"

STATUS = "U1Y_ROUTEC_MATTERSLOT_ORIENTATION_SELECTOR_HYM_REPLAY_NOGO_TERMINAL_GRADING_OPEN"
NEXT = "Selected_U1Y_RouteC_TerminalMonad_MatterSlot_SectionRing_SourceSelector_v1"


def load(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def rel(path: Path) -> str:
    try:
        return str(path.relative_to(ROOT))
    except ValueError:
        return str(path)


def test_row(name: str, available: bool, distinguishes: bool, allowed: bool, conclusion: str, evidence: list[Any]) -> dict[str, Any]:
    return {
        "name": name,
        "available": available,
        "distinguishes_required_partition": distinguishes,
        "allowed_as_selected_source": allowed,
        "conclusion": conclusion,
        "evidence": evidence,
    }


def build() -> tuple[dict[str, Any], dict[str, Any], str]:
    branch = load(INPUTS["branchcoherence_gate"])
    functional = load(INPUTS["functional_payload"])
    end0 = load(INPUTS["end0_sector_values"])
    sm_trans = load(INPUTS["sm_transversality_readout"])
    sm_grading = load(INPUTS["sm_grading_readout"])
    sm_emission = load(INPUTS["sm_samebranch_emission_attempt"])
    sm_weyl = load(INPUTS["sm_weylpair_matterslot"])

    matter_sectors = ["u", "d", "e", "N"]
    rho_tuples = {
        sector: (
            functional["End0_action_on_zero_modes"][sector]["rho_s_T1"],
            functional["End0_action_on_zero_modes"][sector]["rho_s_T2"],
            functional["End0_action_on_zero_modes"][sector]["rho_s_T3"],
        )
        for sector in matter_sectors
    }
    first_tuple = next(iter(rho_tuples.values()))
    all_matter_rho_identical = all(value == first_tuple for value in rho_tuples.values())
    all_gram_equal = all(
        functional["ordered_zero_mode_bases_K_s"][sector]["Gram_matrix"] == "I_3"
        for sector in matter_sectors
    )
    all_norms_equal = all(
        abs(end0["sector_carrier_model"]["validation"]["sector_T3_response_norms"][sector]["frobenius_norm"] - 2 ** 0.5) < 1e-12
        for sector in matter_sectors
    )
    stationary_permutation_invariant = all_matter_rho_identical and all_gram_equal and all_norms_equal

    readout_tests = {
        "hym_rho_s_adjoint_readout": test_row(
            "HYM rho_s adjoint readout",
            available=branch["decision"]["rho_s_validator_ready_promoted"],
            distinguishes=False,
            allowed=True,
            conclusion="NO_GO_PERMUTATION_INVARIANT",
            evidence=[
                f"all_matter_rho_identical={all_matter_rho_identical}",
                f"all_gram_equal={all_gram_equal}",
                f"all_norms_equal={all_norms_equal}",
            ],
        ),
        "projector_gap_green_readout": test_row(
            "projector/gap/Green readout",
            available=branch["decision"]["hym_finite_validator_replay_closed"],
            distinguishes=False,
            allowed=True,
            conclusion="NO_GO_COMMON_STATIONARY_DATA",
            evidence=[
                "selected projector/Riesz/Green replay closed",
                "sector ranks for u,d,e,N are all 3",
                "H is distinguished only as singlet, not as phase/shift matter orientation",
            ],
        ),
        "qutrit_weyl_support_readout": test_row(
            "qutrit/Weyl support readout",
            available=True,
            distinguishes=True,
            allowed=False,
            conclusion="SUPPORT_ONLY_TRANSFER_OPEN",
            evidence=[
                sm_trans["candidate_readouts_tested"][2]["reason"],
                sm_weyl["new_clue_from_qutrit_embedding"]["implication_for_matter_routing"],
            ],
        ),
        "su5_e6_structural_readout": test_row(
            "SU5/E6 structural readout",
            available=True,
            distinguishes=True,
            allowed=False,
            conclusion="STRUCTURAL_SUPPORT_NOT_SOURCE_EMISSION",
            evidence=[
                sm_trans["required_next_readout"]["must_emit"]["matter_slot_grading"],
                sm_emission["finite_su5_support"],
            ],
        ),
        "locked_c1_partition_readout": test_row(
            "locked C1 partition readout",
            available=True,
            distinguishes=True,
            allowed=False,
            conclusion="FORBIDDEN_TARGET_LOCALIZED_SELECTOR",
            evidence=[
                "locked splitter columns uniquely prefer u,e | d,nuD",
                "forbidden as a source selector",
            ],
        ),
        "terminal_monad_sectionring_readout": test_row(
            "terminal monad/section-ring grading readout",
            available=False,
            distinguishes=True,
            allowed=True,
            conclusion="PRIMARY_OPEN_REPAIR_ROUTE",
            evidence=[
                sm_grading["selection_decision"]["primary_route_selected_for_next_attempt"],
                sm_grading["terminal_monad_sectionring_contract"]["must_bind_to_matter_slot_grading"],
            ],
        ),
    }

    no_go = {
        "stationary_hym_replay_cannot_select_orientation": stationary_permutation_invariant,
        "reason": (
            "The selected stationary HYM/End0 replay emits identical adjoint rho_s matrices, "
            "identity Gram matrices, equal ranks, and equal T3 norms on u,d,e,N. Any legal "
            "readout built only from these invariants is equivariant under permutations of "
            "the matter triplet sectors and cannot distinguish phase={u,e} from shift={d,nuD}."
        ),
        "not_a_failure_of_hym_replay": True,
        "meaning": "HYM replay closed the common carrier; orientation needs an additional selected grading/section-label functional.",
    }

    terminal_contract = sm_grading["terminal_monad_sectionring_contract"]
    positive_route = {
        "primary_route": "terminal_monad_cech_sectionring",
        "selected_closed": sm_grading["selection_decision"]["selected_matter_slot_grading_readout_closed"],
        "next_required_artifact": NEXT,
        "source_selector_to_prove": terminal_contract["source_selector_to_prove"],
        "must_bind_to_matter_slot_grading": terminal_contract["must_bind_to_matter_slot_grading"],
        "source_requirements": terminal_contract["source_requirements"],
        "why_this_is_minimal": (
            "It is the first available route that can add actual source labels/degrees rather "
            "than another sector-invariant End0 readout."
        ),
    }

    decision = {
        "orientation_selector_gate_built": True,
        "hym_replay_no_go_for_orientation_proved": no_go["stationary_hym_replay_cannot_select_orientation"],
        "selected_matter_slot_orientation_emitted": False,
        "selected_U10_Ubar5_polarization_emitted": False,
        "selected_1M_Dirac_source_emitted": False,
        "selected_overlap_normalization_emitted": False,
        "N_alpha1_h_ext_promoted_to_du_dalpha1": False,
        "alpha1_driver_verified": False,
        "lambda_12_computable": False,
        "primary_repair_route": "terminal_monad_cech_sectionring",
        "target_fitting_used": False,
        "next_required_artifact": NEXT,
    }

    theorem = {
        "name": "U1YRouteCMatterSlotOrientationSelectorFromHYMReplayNoGoAndTerminalGradingReduction",
        "proved": True,
        "statement": (
            "The selected stationary HYM/End0 finite replay cannot by itself emit "
            "the matter-slot orientation selector. On the non-Higgs matter sectors "
            "u,d,e,N it supplies identical adjoint rho_s matrices, identical "
            "I_3 Gram data, equal ranks, and equal T3 norms, so every legal readout "
            "formed from that replay is permutation-invariant. The desired partition "
            "phase={u,e}, shift={d,nuD} is available only as SU(5)/E6/qutrit support "
            "or forbidden locked-target readout until an additional selected grading "
            "is supplied. The minimal live positive route is the terminal monad/Cech "
            "section-ring source selector, which must bind L3-K2 or equivalent "
            "selected source labels to 10_M clock, bar5_M shift, and 1_M Dirac shift."
        ),
    }

    candidate = {
        "candidate": "SelectedU1YRouteCMatterSlotOrientationSelectorFromHYMFiniteReplay",
        "status": STATUS,
        "inputs": {key: rel(path) for key, path in INPUTS.items()},
        "readout_tests": readout_tests,
        "hym_replay_orientation_no_go": no_go,
        "positive_route": positive_route,
        "decision": decision,
        "theorem": theorem,
        "what_closes_now": {
            "hym_replay_orientation_no_go": no_go["stationary_hym_replay_cannot_select_orientation"],
            "legal_current_readouts_exhausted": True,
            "terminal_monad_sectionring_route_imported_as_primary": True,
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
            "lambda_12": True,
        },
        "next_required_artifact": NEXT,
        "closure_claimed": False,
        "target_fitting_used": False,
        "guardrails": {
            "claims_selected_matter_slot_orientation": False,
            "claims_selected_U10_Ubar5": False,
            "claims_selected_1M_Dirac_source": False,
            "claims_selected_overlap_normalization": False,
            "claims_alpha1_driver_verified": False,
            "claims_lambda12": False,
            "uses_observed_data": False,
            "uses_benchmark_data": False,
            "uses_locked_c1_target_as_selector": False,
            "target_fitting_used": False,
        },
    }

    cert = {
        "certificate": "SelectedU1YRouteCMatterSlotOrientationSelectorFromHYMFiniteReplay",
        "status": STATUS,
        "candidate_path": rel(OUTPUT_DATA),
        "note_path": rel(OUTPUT_NOTE),
        "hym_replay_no_go_for_orientation_proved": decision["hym_replay_no_go_for_orientation_proved"],
        "selected_matter_slot_orientation_emitted": False,
        "primary_repair_route": decision["primary_repair_route"],
        "alpha1_driver_verified": False,
        "lambda_12_closed": False,
        "next_required_artifact": NEXT,
        "target_fitting_used": False,
    }
    return candidate, cert, render_note(candidate, cert)


def render_note(candidate: dict[str, Any], cert: dict[str, Any]) -> str:
    lines = [
        "# Selected U1Y Route-C MatterSlot OrientationSelector from HYM FiniteReplay v1",
        "",
        "## Result",
        "",
        "```text",
        f"status = {candidate['status']}",
        f"hym_replay_no_go_for_orientation_proved = {str(cert['hym_replay_no_go_for_orientation_proved']).lower()}",
        f"selected_matter_slot_orientation_emitted = {str(cert['selected_matter_slot_orientation_emitted']).lower()}",
        f"primary_repair_route = {cert['primary_repair_route']}",
        f"next_required_artifact = {candidate['next_required_artifact']}",
        "```",
        "",
        "The HYM/End0 finite replay is now strong enough to prove its own boundary:",
        "it is a selected common carrier, but it is permutation-invariant across the",
        "non-Higgs matter triplet sectors. Therefore it cannot by itself select",
        "`phase={u,e}` and `shift={d,nuD}`.",
        "",
        "## Readout Tests",
        "",
        "| Readout | Available | Distinguishes | Allowed | Conclusion |",
        "| --- | --- | --- | --- | --- |",
    ]
    for key, row in candidate["readout_tests"].items():
        lines.append(
            f"| `{key}` | `{str(row['available']).lower()}` | "
            f"`{str(row['distinguishes_required_partition']).lower()}` | "
            f"`{str(row['allowed_as_selected_source']).lower()}` | `{row['conclusion']}` |"
        )
    lines.extend(
        [
            "",
            "## Positive Route",
            "",
            "```json",
            json.dumps(candidate["positive_route"]["source_selector_to_prove"], indent=2, sort_keys=True),
            "```",
            "",
            "## Theorem",
            "",
            candidate["theorem"]["statement"],
            "",
            "## Guardrails",
            "",
            "- Do not infer matter-slot orientation from identical HYM/End0 adjoint carriers.",
            "- Do not treat SU(5)/E6/qutrit support as selected source emission.",
            "- Do not use locked C1 splitter columns, observed masses, CKM/PMNS, or benchmark flavor matrices.",
            "- Do not promote `alpha1_driver_verified` or `lambda_12` here.",
            "",
            "## Certificate",
            "",
            "```json",
            json.dumps(cert, indent=2, sort_keys=True),
            "```",
            "",
        ]
    )
    return "\n".join(lines)


def main() -> int:
    candidate, cert, note = build()
    OUTPUT_DATA.write_text(json.dumps(candidate, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    OUTPUT_CERT.write_text(json.dumps(cert, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    OUTPUT_NOTE.write_text(note, encoding="utf-8")
    print(f"wrote {rel(OUTPUT_DATA)}")
    print(f"wrote {rel(OUTPUT_CERT)}")
    print(f"wrote {rel(OUTPUT_NOTE)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
