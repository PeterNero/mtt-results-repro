"""Build the U1/Y Route-C branch-coherence selector or finite validator replay gate."""

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
    "source_promotion_packet": DATA / "selected_u1y_routec_u10ubar5_1m_sourcepromotion_samebranch_emission.candidate.json",
    "transport_replay": DATA / "selected_u1y_routec_transportclosed_bn_basis_or_symbolic_projector_replay.candidate.json",
    "transport_replay_values": DATA / "selected_u1y_routec_symbolic_transport_projector_replay.values.json",
    "functional_payload": DATA / "selected_u1y_routec_hym_projector_source_payload.functional.json",
    "end0_sector_values": DATA / "selected_u1y_routec_end0_to_sector_functor_source_and_value_packet.values.json",
    "dotd_driver": DATA / "selected_u1y_routec_dotd_alpha1_transport_derivative_and_driver.candidate.json",
    "sm_1m_u10ubar5_gate": SM / "candidate_data" / "selected_1m_dirac_source_or_u10ubar5_polarization.candidate.json",
}

OUTPUT_DATA = DATA / "selected_u1y_routec_branchcoherence_selector_or_finite_validator_replay.candidate.json"
OUTPUT_CERT = CERTS / "selected_u1y_routec_branchcoherence_selector_or_finite_validator_replay_certificate.json"
OUTPUT_NOTE = PROOF / "Selected_U1Y_RouteC_BranchCoherence_Selector_or_FiniteValidatorReplay_v1.md"

STATUS = "U1Y_ROUTEC_BRANCHCOHERENCE_GATE_PARTIAL_REPLAY_CLOSED_MATTERSLOT_SELECTOR_OPEN"
NEXT = "Selected_U1Y_RouteC_MatterSlot_OrientationSelector_from_HYM_FiniteReplay_v1"


def load(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def rel(path: Path) -> str:
    try:
        return str(path.relative_to(ROOT))
    except ValueError:
        return str(path)


def subgoal(
    *,
    required: str,
    status: str,
    closed: bool,
    evidence: list[Any],
    blocker: str,
) -> dict[str, Any]:
    return {
        "required": required,
        "status": status,
        "closed": closed,
        "evidence": evidence,
        "blocker": blocker,
    }


def build() -> tuple[dict[str, Any], dict[str, Any], str]:
    source = load(INPUTS["source_promotion_packet"])
    transport = load(INPUTS["transport_replay"])
    replay_values = load(INPUTS["transport_replay_values"])
    functional = load(INPUTS["functional_payload"])
    end0 = load(INPUTS["end0_sector_values"])
    dotd = load(INPUTS["dotd_driver"])
    sm_gate = load(INPUTS["sm_1m_u10ubar5_gate"])

    t_decision = transport["decision"]
    replay_result = replay_values["validator_result"]
    route_a = sm_gate["route_A_SU5_E6_polarization"]
    promotion_contract = sm_gate["same_branch_promotion_contract"]["must_emit"]

    hym_replay_closed = (
        t_decision["projector_riesz_green_replay_closed"]
        and t_decision["selected_projector_source_verified"]
        and t_decision["selected_rho_s_validator_ready"]
        and replay_result["selected_source_verified"]
        and replay_result["selected_rho_s_validator_ready"]
    )
    all_functional_same_source = all(
        row["same_source_action"] and row["functional_selected_rho_s"]
        for row in functional["End0_action_on_zero_modes"].values()
    )
    all_sector_gram_identity = all(
        row["Gram_matrix"] in {"I_3", "I_1"}
        for row in functional["ordered_zero_mode_bases_K_s"].values()
    )
    end0_norms_ready = all(
        row["zero_response"] or abs(row["frobenius_norm"] - 2 ** 0.5) < 1e-12
        for row in end0["sector_carrier_model"]["validation"]["sector_T3_response_norms"].values()
    )

    subgoals = {
        "hym_finite_validator_replay": subgoal(
            required="selected HYM/projector rho_s, projectors, Riesz, Green replay in the selected transport frame",
            status="CLOSED",
            closed=hym_replay_closed and all_functional_same_source,
            evidence=[
                transport["status"],
                f"gauge_frame_residual_l2={t_decision['gauge_frame_residual_l2']}",
                f"selected_rho_s_validator_ready={t_decision['selected_rho_s_validator_ready']}",
            ],
            blocker="none for stationary rho_s/projector replay; dotD derivative remains separate",
        ),
        "sector_gram_normalization_ready": subgoal(
            required="selected invariant sector Gram fixes rho_s(T_i)/sqrt(2) after replayed rho_s",
            status="CONDITIONAL_READY",
            closed=False,
            evidence=[
                f"all_sector_gram_identity={all_sector_gram_identity}",
                f"end0_norms_ready={end0_norms_ready}",
                source["source_promotion_packet"]["overlap_transfer_normalization"]["value"],
            ],
            blocker="physical transfer normalization still needs the matter-slot orientation selector to identify which replayed sectors carry phase versus shift.",
        ),
        "q79_finite_polarization_support": subgoal(
            required="finite q79 packet U_10=I_3, U_bar5=F, selected route u,e | d,nuD",
            status="SUPPORT_ONLY",
            closed=False,
            evidence=[
                route_a["finite_packet"],
                promotion_contract["selected_sector_route"],
                f"support_closed={route_a['support_closed']}",
            ],
            blocker="the finite polarization remains an imported support packet until the HYM replay emits the same matter-slot orientation.",
        ),
        "one_M_dirac_shift_support": subgoal(
            required="1_M=N^c emitted as the same selected shift-side source as d and nuD",
            status="SUPPORT_ONLY",
            closed=False,
            evidence=[
                "1_M=N^c",
                promotion_contract["selected_ordered_matter_slot_packet"],
                promotion_contract["selected_sector_route"],
            ],
            blocker="HYM replay has sector N as an adjoint carrier, but no source theorem orients it as 1_M Dirac shift.",
        ),
        "matter_slot_orientation_selector": subgoal(
            required="derive phase={u,e} and shift={d,nuD} from replayed HYM/End0 data without target columns",
            status="OPEN_DECISIVE_GATE",
            closed=False,
            evidence=[
                end0["matter_routing"]["reason"],
                f"structural_su5_e6_support_present={end0['matter_routing']['structural_su5_e6_support_present']}",
            ],
            blocker="End0 replay supplies sector blocks but not the Weyl phase/shift orientation selector.",
        ),
        "alpha1_driver_promotion": subgoal(
            required="promote N_alpha1(h_ext)=1 to du/dalpha1=h_ext and run honest dotD replay",
            status="OPEN_AFTER_ORIENTATION",
            closed=False,
            evidence=[
                dotd["status"],
                f"projector_riesz_green_replay_closed={t_decision['projector_riesz_green_replay_closed']}",
            ],
            blocker="requires selected matter-slot orientation plus physical transfer normalization.",
        ),
    }

    counts = {
        "required": len(subgoals),
        "closed": sum(1 for row in subgoals.values() if row["closed"]),
        "conditional_ready": sum(1 for row in subgoals.values() if row["status"] == "CONDITIONAL_READY"),
        "support_only": sum(1 for row in subgoals.values() if row["status"] == "SUPPORT_ONLY"),
        "open": sum(1 for row in subgoals.values() if row["closed"] is False),
    }

    orientation_selector_contract = {
        "must_not_use": [
            "observed masses or CKM data",
            "benchmark Yukawa matrices",
            "locked splitter target columns as source selectors",
            "diagnostic selected-source flag lifts",
        ],
        "must_emit": {
            "orientation_rule": "source-internal rule distinguishing clock/phase sectors from shift sectors",
            "phase_sectors": ["u", "e"],
            "shift_sectors": ["d", "nuD"],
            "one_M_rule": "N/1_M = N^c belongs to Dirac shift side",
            "finite_packet_match": {"U_10": "I_3", "U_bar5": "F"},
            "normalization": "rho_s(T_i)/sqrt(2) in the selected oriented matter slots",
        },
        "promotes_if_closed": [
            "selected_U10_Ubar5_polarization_emitted",
            "selected_1M_Dirac_source_emitted",
            "selected_overlap_normalization_emitted",
            "N_alpha1_h_ext_promoted_to_du_dalpha1",
            "alpha1_driver_verified",
        ],
    }

    decision = {
        "branchcoherence_gate_built": True,
        "hym_finite_validator_replay_closed": subgoals["hym_finite_validator_replay"]["closed"],
        "rho_s_validator_ready_promoted": subgoals["hym_finite_validator_replay"]["closed"],
        "q79_finite_polarization_selected": False,
        "matter_slot_orientation_selector_emitted": False,
        "selected_U10_Ubar5_polarization_emitted": False,
        "selected_1M_Dirac_source_emitted": False,
        "selected_overlap_normalization_emitted": False,
        "N_alpha1_h_ext_promoted_to_du_dalpha1": False,
        "alpha1_driver_verified": False,
        "lambda_12_computable": False,
        "target_fitting_used": False,
        "next_required_artifact": NEXT,
    }

    theorem = {
        "name": "U1YRouteCBranchCoherenceFiniteReplayPartialClosureTheorem",
        "proved": True,
        "statement": (
            "The branch-coherence gate partially closes: exact symbolic transport "
            "conjugation promotes the selected HYM/projector stationary replay, so "
            "rho_s, sector projectors, Riesz, and Green are validator-ready in the "
            "selected transport frame. This removes the finite replay blocker for "
            "rho_s. It does not select the q79 matter-slot orientation: U_10=I_3, "
            "U_bar5=F, the 1_M=N^c shift rule, and rho_s(T_i)/sqrt(2) remain "
            "support/conditional until a source-internal orientation selector "
            "derives phase={u,e} and shift={d,nuD} from the replayed HYM/End0 data."
        ),
    }

    candidate = {
        "candidate": "SelectedU1YRouteCBranchCoherenceSelectorOrFiniteValidatorReplay",
        "status": STATUS,
        "inputs": {key: rel(path) for key, path in INPUTS.items()},
        "subgoals": subgoals,
        "counts": counts,
        "orientation_selector_contract": orientation_selector_contract,
        "decision": decision,
        "theorem": theorem,
        "what_closes_now": {
            "stationary_HYM_finite_validator_replay": decision["hym_finite_validator_replay_closed"],
            "rho_s_validator_ready_promoted": decision["rho_s_validator_ready_promoted"],
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
            "lambda_12": True,
        },
        "next_required_artifact": NEXT,
        "closure_claimed": False,
        "target_fitting_used": False,
        "guardrails": {
            "claims_full_branch_coherence": False,
            "claims_selected_U10_Ubar5": False,
            "claims_selected_1M_Dirac_source": False,
            "claims_selected_overlap_normalization": False,
            "claims_alpha1_driver_verified": False,
            "claims_lambda12": False,
            "uses_observed_data": False,
            "uses_benchmark_data": False,
            "target_fitting_used": False,
        },
    }

    cert = {
        "certificate": "SelectedU1YRouteCBranchCoherenceSelectorOrFiniteValidatorReplay",
        "status": STATUS,
        "candidate_path": rel(OUTPUT_DATA),
        "note_path": rel(OUTPUT_NOTE),
        "subgoals_closed": counts["closed"],
        "required_subgoals": counts["required"],
        "hym_finite_validator_replay_closed": decision["hym_finite_validator_replay_closed"],
        "rho_s_validator_ready_promoted": decision["rho_s_validator_ready_promoted"],
        "matter_slot_orientation_selector_emitted": False,
        "alpha1_driver_verified": False,
        "lambda_12_closed": False,
        "next_required_artifact": NEXT,
        "target_fitting_used": False,
    }
    return candidate, cert, render_note(candidate, cert)


def render_note(candidate: dict[str, Any], cert: dict[str, Any]) -> str:
    lines = [
        "# Selected U1Y Route-C BranchCoherence Selector or FiniteValidatorReplay v1",
        "",
        "## Result",
        "",
        "```text",
        f"status = {candidate['status']}",
        f"subgoals_closed = {cert['subgoals_closed']} / {cert['required_subgoals']}",
        f"hym_finite_validator_replay_closed = {str(cert['hym_finite_validator_replay_closed']).lower()}",
        f"rho_s_validator_ready_promoted = {str(cert['rho_s_validator_ready_promoted']).lower()}",
        f"matter_slot_orientation_selector_emitted = {str(cert['matter_slot_orientation_selector_emitted']).lower()}",
        f"next_required_artifact = {candidate['next_required_artifact']}",
        "```",
        "",
        "The stationary HYM/projector replay side is now closed in the symbolic",
        "transport frame. The remaining blocker is no longer generic finite replay;",
        "it is the source-internal orientation selector that must identify the",
        "replayed sectors with the q79 finite matter-slot packet.",
        "",
        "## Subgoals",
        "",
        "| Subgoal | Status | Closed | Blocker |",
        "| --- | --- | --- | --- |",
    ]
    for key, row in candidate["subgoals"].items():
        lines.append(
            f"| `{key}` | `{row['status']}` | `{str(row['closed']).lower()}` | {row['blocker']} |"
        )
    lines.extend(
        [
            "",
            "## Orientation Selector Contract",
            "",
            "```json",
            json.dumps(candidate["orientation_selector_contract"]["must_emit"], indent=2, sort_keys=True),
            "```",
            "",
            "## Theorem",
            "",
            candidate["theorem"]["statement"],
            "",
            "## Guardrails",
            "",
            "- Do not treat the closed HYM stationary replay as selected matter-slot orientation.",
            "- Do not promote `U_10=I_3`, `U_bar5=F`, or `1_M=N^c` until the orientation selector emits.",
            "- Do not promote `N_alpha1(h_ext)=1` to `du/dalpha1=h_ext` until physical transfer normalization emits.",
            "- Do not use observed or benchmark data.",
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
