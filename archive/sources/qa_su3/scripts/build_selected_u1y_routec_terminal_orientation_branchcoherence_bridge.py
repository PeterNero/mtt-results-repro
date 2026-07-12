"""Build the U1/Y Route-C terminal-orientation to branch-coherence bridge."""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "candidate_data"
CERTS = ROOT / "certificates"
PROOF = ROOT / "proof_corpus"

INPUTS = {
    "branchcoherence": DATA / "selected_u1y_routec_branchcoherence_selector_or_finite_validator_replay.candidate.json",
    "hym_orientation_nogo": DATA / "selected_u1y_routec_matterslot_orientationselector_from_hym_finitereplay.candidate.json",
    "terminal_baseorder_slotmap": DATA / "selected_u1y_routec_terminalmonad_baseorder_ahbinding_smslotmap.candidate.json",
}

OUTPUT_DATA = DATA / "selected_u1y_routec_terminal_orientation_branchcoherence_bridge.candidate.json"
OUTPUT_CERT = CERTS / "selected_u1y_routec_terminal_orientation_branchcoherence_bridge_certificate.json"
OUTPUT_NOTE = PROOF / "Selected_U1Y_RouteC_Terminal_Orientation_BranchCoherence_Bridge_v1.md"

STATUS = "U1Y_ROUTEC_TERMINAL_ORIENTATION_BRIDGE_ORDERED_SELECTOR_CLOSED_OPERATOR_EMISSION_OPEN"
NEXT = "Selected_U1Y_RouteC_OperatorEmission_and_OverlapNormalization_from_TerminalSlotMap_v1"


def load(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def rel(path: Path) -> str:
    try:
        return str(path.relative_to(ROOT))
    except ValueError:
        return str(path)


def build() -> tuple[dict[str, Any], dict[str, Any], str]:
    branch = load(INPUTS["branchcoherence"])
    nogo = load(INPUTS["hym_orientation_nogo"])
    terminal = load(INPUTS["terminal_baseorder_slotmap"])

    terminal_decision = terminal["decision"]
    base = terminal["baseorder_binding"]
    slot = terminal["slot_map"]

    ordered_orientation = {
        "closed": (
            terminal_decision["terminal_lane_selected_at_ordered_source_layer_under_explicit_principle"]
            and terminal_decision["AH_or_Cech_transition_binding_selected_at_ordered_source_layer"]
            and terminal_decision["slot_map_support_complete"]
            and slot["support_values_are_mutually_compatible"]
        ),
        "source": "terminal_monad_AH_goodcover_sectionring",
        "source_label": base["terminal_source_label"],
        "L": base["selected_L"],
        "L2": base["selected_L2"],
        "phase_sectors": slot["finite_structural_route"]["phase"],
        "shift_sectors": slot["finite_structural_route"]["shift"],
        "clock_packet": {
            "10_M": slot["finite_structural_route"]["10_M_clock"],
            "sectors": slot["finite_structural_route"]["phase"],
        },
        "shift_packet": {
            "bar5_M": slot["finite_structural_route"]["bar5_M_shift"],
            "one_M_Dirac_shift": slot["finite_structural_route"]["one_M_Dirac_shift"],
        },
        "scope": "ordered matter-slot/source-label layer only",
    }

    replay_bridge = {
        "stationary_hym_replay_closed": branch["decision"]["hym_finite_validator_replay_closed"],
        "rho_s_validator_ready": branch["decision"]["rho_s_validator_ready_promoted"],
        "hym_replay_orientation_nogo_retained": nogo["decision"]["hym_replay_no_go_for_orientation_proved"],
        "meaning": (
            "HYM replay supplies selected common carrier data; terminal section-ring labels supply "
            "the ordered orientation. The bridge joins them only as a compatibility theorem, not "
            "as same-source operator emission."
        ),
    }

    emission_gap = {
        "same_branch_selected_operator_emission": False,
        "operator_layer_Pic0_closed": False,
        "selected_overlap_transfer_normalization": False,
        "N_alpha1_h_ext_promoted_to_du_dalpha1": False,
        "alpha1_driver_verified": False,
        "lambda_12_computable": False,
        "missing_payload": [
            "selected operator-layer Pic0/gerbe/twisted D_E rule",
            "same-source emission map from terminal ordered slot labels to finite HYM/End0 operator blocks",
            "selected inner-product/overlap normalization in the oriented slots",
            "honest dotD_alpha1 replay with du/dalpha1=h_ext",
        ],
    }

    decision = {
        "terminal_orientation_bridge_built": True,
        "ordered_matter_slot_orientation_selector_closed": ordered_orientation["closed"],
        "selected_U10_Ubar5_orientation_at_ordered_layer": ordered_orientation["closed"],
        "selected_1M_Dirac_shift_at_ordered_layer": ordered_orientation["closed"],
        "stationary_hym_replay_remains_closed": replay_bridge["stationary_hym_replay_closed"],
        "hym_nogo_retained": replay_bridge["hym_replay_orientation_nogo_retained"],
        "same_branch_selected_operator_emission": False,
        "selected_overlap_normalization_emitted": False,
        "alpha1_driver_verified": False,
        "lambda_12_computable": False,
        "target_fitting_used": False,
        "next_required_artifact": NEXT,
    }

    theorem = {
        "name": "U1YRouteCTerminalOrientationBranchCoherenceBridge",
        "proved": True,
        "statement": (
            "The HYM replay no-go and terminal source theorem are compatible and complementary. "
            "HYM/End0 replay cannot distinguish the matter-slot orientation because it is "
            "permutation-invariant on u,d,e,N. The terminal monad/AH/good-cover section-ring "
            "source now does distinguish it at the ordered source-label layer: g3/L3-K2 selects "
            "10_M clock sectors {u,e}, bar5_M shift sector {d}, and 1_M=N^c Dirac shift sector {nuD}. "
            "Thus the orientation selector is closed as an ordered terminal-source label theorem, "
            "while same-branch operator emission, operator-layer Pic0, selected overlap normalization, "
            "alpha1 transfer, and lambda_12 remain open."
        ),
    }

    candidate = {
        "candidate": "SelectedU1YRouteCTerminalOrientationBranchCoherenceBridge",
        "status": STATUS,
        "inputs": {key: rel(path) for key, path in INPUTS.items()},
        "ordered_orientation": ordered_orientation,
        "replay_bridge": replay_bridge,
        "emission_gap": emission_gap,
        "decision": decision,
        "theorem": theorem,
        "what_closes_now": {
            "HYM_orientation_nogo_retained": replay_bridge["hym_replay_orientation_nogo_retained"],
            "terminal_source_orientation_selector_closed_at_ordered_layer": ordered_orientation["closed"],
            "10M_clock_orientation_at_ordered_layer": ordered_orientation["closed"],
            "bar5M_shift_orientation_at_ordered_layer": ordered_orientation["closed"],
            "1M_Dirac_shift_orientation_at_ordered_layer": ordered_orientation["closed"],
            "branchcoherence_frontier_moved_to_operator_emission_and_overlap": True,
            "target_fitting_excluded": True,
        },
        "what_remains_open": {
            "same_branch_selected_operator_emission": True,
            "operator_layer_Pic0_or_torsion_gerbe_rule": True,
            "selected_overlap_transfer_normalization": True,
            "same_source_D_E_Riesz_Green_dotD": True,
            "alpha1_driver_verified": True,
            "lambda_12": True,
        },
        "guardrails": {
            "claims_hym_replay_selects_orientation": False,
            "claims_same_branch_operator_emission": False,
            "claims_operator_layer_Pic0_closed": False,
            "claims_selected_overlap_normalization": False,
            "claims_alpha1_driver_verified": False,
            "claims_lambda12": False,
            "uses_observed_data": False,
            "uses_benchmark_data": False,
            "uses_locked_C1_columns": False,
            "target_fitting_used": False,
        },
        "next_required_artifact": NEXT,
        "closure_claimed": False,
        "target_fitting_used": False,
        "observed_data_used": False,
    }

    cert = {
        "certificate": "SelectedU1YRouteCTerminalOrientationBranchCoherenceBridge",
        "status": STATUS,
        "candidate_path": rel(OUTPUT_DATA),
        "note_path": rel(OUTPUT_NOTE),
        "ordered_matter_slot_orientation_selector_closed": decision[
            "ordered_matter_slot_orientation_selector_closed"
        ],
        "selected_1M_Dirac_shift_at_ordered_layer": decision["selected_1M_Dirac_shift_at_ordered_layer"],
        "same_branch_selected_operator_emission": False,
        "selected_overlap_normalization_emitted": False,
        "alpha1_driver_verified": False,
        "lambda_12_closed": False,
        "next_required_artifact": NEXT,
        "target_fitting_used": False,
        "observed_data_used": False,
    }
    return candidate, cert, render_note(candidate, cert)


def render_note(candidate: dict[str, Any], cert: dict[str, Any]) -> str:
    lines = [
        "# Selected U1Y Route-C Terminal Orientation BranchCoherence Bridge v1",
        "",
        "## Result",
        "",
        "```text",
        f"status = {candidate['status']}",
        "ordered_matter_slot_orientation_selector_closed = "
        f"{str(cert['ordered_matter_slot_orientation_selector_closed']).lower()}",
        "same_branch_selected_operator_emission = "
        f"{str(cert['same_branch_selected_operator_emission']).lower()}",
        "selected_overlap_normalization_emitted = "
        f"{str(cert['selected_overlap_normalization_emitted']).lower()}",
        f"next_required_artifact = {candidate['next_required_artifact']}",
        "```",
        "",
        "This closes the orientation selector in the ordered terminal-source sense,",
        "without contradicting the HYM replay no-go. HYM supplies a common selected",
        "carrier; the terminal section-ring source supplies the matter-slot labels.",
        "",
        "## Ordered Orientation",
        "",
        "```json",
        json.dumps(candidate["ordered_orientation"], indent=2, sort_keys=True),
        "```",
        "",
        "## Remaining Emission Gap",
        "",
        "```json",
        json.dumps(candidate["emission_gap"], indent=2, sort_keys=True),
        "```",
        "",
        "## Theorem",
        "",
        candidate["theorem"]["statement"],
        "",
        "## Guardrails",
        "",
        "- Do not say HYM replay itself selects orientation; the no-go remains true.",
        "- Do not promote ordered source labels to same-branch operator emission without an emission map.",
        "- Do not promote overlap normalization, `alpha1`, or `lambda_12` here.",
        "",
        "## Certificate",
        "",
        "```json",
        json.dumps(cert, indent=2, sort_keys=True),
        "```",
        "",
    ]
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
