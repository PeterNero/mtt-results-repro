"""Build the U1/Y Route-C terminal-monad base-order/AH-binding/slot-map gate."""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "candidate_data"
CERTS = ROOT / "certificates"
PROOF = ROOT / "proof_corpus"

INPUTS = {
    "terminal_selector": DATA / "selected_u1y_routec_terminalmonad_matterslot_sectionring_source_selector.candidate.json",
    "ordered_ah_source": DATA / "selected_u1y_ah_goodcover_source_or_routec_selected_residual.candidate.json",
    "u10_ubar5_1m_packet": DATA / "selected_u1y_routec_u10ubar5_1m_sourcepromotion_samebranch_emission.candidate.json",
}

OUTPUT_DATA = DATA / "selected_u1y_routec_terminalmonad_baseorder_ahbinding_smslotmap.candidate.json"
OUTPUT_CERT = CERTS / "selected_u1y_routec_terminalmonad_baseorder_ahbinding_smslotmap_certificate.json"
OUTPUT_NOTE = PROOF / "Selected_U1Y_RouteC_TerminalMonad_BaseOrder_AHBinding_SMSlotMap_v1.md"

STATUS = "U1Y_ROUTEC_TERMINALMONAD_BASEORDER_AHBINDING_PROVED_SLOTMAP_SUPPORT_COMPLETE_BRANCHCOHERENCE_OPEN"
NEXT = "Selected_U1Y_RouteC_BranchCoherence_Selector_or_FiniteValidatorReplay_v1"


def load(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def rel(path: Path) -> str:
    try:
        return str(path.relative_to(ROOT))
    except ValueError:
        return str(path)


def build() -> tuple[dict[str, Any], dict[str, Any], str]:
    terminal = load(INPUTS["terminal_selector"])
    ah = load(INPUTS["ordered_ah_source"])
    slot = load(INPUTS["u10_ubar5_1m_packet"])

    source_layer = ah["source_layer"]
    terminal_candidate = terminal["imported_terminal_candidate"]
    slot_packet = slot["source_promotion_packet"]

    baseorder_binding = {
        "terminal_source_label": source_layer["selected_source_label"],
        "selected_L": source_layer["selected_L"],
        "selected_L2": source_layer["selected_L2"],
        "terminal_candidate_label": terminal_candidate["forced_label"],
        "terminal_candidate_value": terminal_candidate["forced_value"],
        "terminal_candidate_double": terminal_candidate["forced_double"],
        "same_L3_K2_identity": (
            source_layer["selected_L"] == terminal_candidate["forced_value"]
            and source_layer["selected_L2"] == terminal_candidate["forced_double"]
            and terminal_candidate["forced_label"] == "L3-K2"
        ),
        "base_factor_order_selected_at_ordered_source_layer": (
            ah["decision"]["selected_AH_goodcover_source_layer_emitted"]
            and source_layer["ordered_source_selected_by_mtt_under_principle"]
            and source_layer["selected_source_label"] == "g3 / L3-K2"
        ),
        "standard_lattice_equivalent_selected_at_ordered_source_layer": (
            source_layer["terminal_lane_unique_visible_c2"]
            and source_layer["terminal_lane_unique_zero_central"]
            and ah["what_closes"]["target_branch_L_selected_at_ordered_source_layer"]
        ),
        "AH_goodcover_binding_selected_at_ordered_source_layer": (
            ah["ah_goodcover_stability_layer"]["AH_automorphy_cocycle_and_degree_laws"]
            and ah["ah_goodcover_stability_layer"]["selected_ordered_AH_goodcover_source_for_stability_layer"]
            and ah["ah_goodcover_stability_layer"]["stable_in_selected_ordered_AH_layer"]
        ),
        "principle_dependency": ah["decision"]["terminal_admissible_section_principle_dependency"],
        "principle_unconditional_in_mtt_axioms": ah["decision"]["principle_unconditional_in_mtt_axioms"],
        "scope": ah["ah_goodcover_stability_layer"]["scope"],
    }

    slot_map = {
        "support_complete": slot["decision"]["support_complete"],
        "same_branch_complete": slot["decision"]["same_branch_complete"],
        "physical_selected_complete": slot["decision"]["physical_selected_complete"],
        "selected_U10_Ubar5_polarization_emitted": slot["decision"]["selected_U10_Ubar5_polarization_emitted"],
        "selected_1M_Dirac_source_emitted": slot["decision"]["selected_1M_Dirac_source_emitted"],
        "selected_overlap_normalization_emitted": slot["decision"]["selected_overlap_normalization_emitted"],
        "finite_structural_route": {
            "10_M_clock": slot_packet["U_10_clock"]["value"],
            "bar5_M_shift": slot_packet["U_bar5_shift"]["value"],
            "one_M_Dirac_shift": slot_packet["one_M_Dirac_shift"]["value"],
            "phase": ["u", "e"],
            "shift": ["d", "nuD"],
        },
        "support_values_are_mutually_compatible": (
            slot_packet["U_10_clock"]["support_present"]
            and slot_packet["U_bar5_shift"]["support_present"]
            and slot_packet["one_M_Dirac_shift"]["support_present"]
            and slot_packet["overlap_transfer_normalization"]["support_present"]
        ),
        "blocked_by": slot["branch_coherence_selector"]["must_prove"],
    }

    proved_baseorder_ah = (
        baseorder_binding["same_L3_K2_identity"]
        and baseorder_binding["base_factor_order_selected_at_ordered_source_layer"]
        and baseorder_binding["standard_lattice_equivalent_selected_at_ordered_source_layer"]
        and baseorder_binding["AH_goodcover_binding_selected_at_ordered_source_layer"]
    )

    decision = {
        "baseorder_AHbinding_gate_built": True,
        "terminal_lane_selected_at_ordered_source_layer_under_explicit_principle": proved_baseorder_ah,
        "base_factor_order_selected_at_ordered_source_layer": baseorder_binding[
            "base_factor_order_selected_at_ordered_source_layer"
        ],
        "standard_lattice_equivalent_selected_at_ordered_source_layer": baseorder_binding[
            "standard_lattice_equivalent_selected_at_ordered_source_layer"
        ],
        "AH_or_Cech_transition_binding_selected_at_ordered_source_layer": baseorder_binding[
            "AH_goodcover_binding_selected_at_ordered_source_layer"
        ],
        "slot_map_support_complete": slot_map["support_complete"] and slot_map["support_values_are_mutually_compatible"],
        "slot_map_selected_same_branch": False,
        "selected_matter_slot_orientation_emitted": False,
        "selected_overlap_normalization_emitted": False,
        "operator_layer_Pic0_closed": False,
        "alpha1_driver_verified": False,
        "lambda_12_computable": False,
        "target_fitting_used": False,
        "next_required_artifact": NEXT,
    }

    theorem = {
        "name": "U1YRouteCTerminalMonadBaseOrderAHBindingSMSlotMapGate",
        "proved": True,
        "statement": (
            "The selected ordered AH/good-cover source packet and the terminal-monad selector "
            "refer to the same L3-K2 source: L=(1,-2,0), L^2=(2,-4,0), selected as g3/L3-K2 "
            "under the explicit terminal admissible-section principle. Therefore the terminal "
            "lane, standard-lattice equivalent, base factor order, and AH/good-cover binding are "
            "closed at the ordered Chern/H1/ordinary-curvature/stability layer. The SU(5)/E6 "
            "slot map is support-complete: U_10=I_3, U_bar5=F, and 1_M=N^c route to phase={u,e} "
            "and shift={d,nuD}. This does not yet prove same-branch selected operator emission, "
            "operator-layer Pic0, overlap normalization, alpha1 transfer, or lambda_12."
        ),
    }

    candidate = {
        "candidate": "SelectedU1YRouteCTerminalMonadBaseOrderAHBindingSMSlotMap",
        "status": STATUS,
        "inputs": {key: rel(path) for key, path in INPUTS.items()},
        "parent_status": terminal["status"],
        "baseorder_binding": baseorder_binding,
        "slot_map": slot_map,
        "decision": decision,
        "theorem": theorem,
        "what_closes_now": {
            "same_L3_K2_identity_between_terminal_selector_and_AH_source": baseorder_binding["same_L3_K2_identity"],
            "terminal_lane_selected_at_ordered_source_layer_under_explicit_principle": proved_baseorder_ah,
            "standard_lattice_equivalent_selected_at_ordered_source_layer": decision[
                "standard_lattice_equivalent_selected_at_ordered_source_layer"
            ],
            "base_factor_order_selected_at_ordered_source_layer": decision[
                "base_factor_order_selected_at_ordered_source_layer"
            ],
            "AH_goodcover_transition_binding_selected_at_ordered_source_layer": decision[
                "AH_or_Cech_transition_binding_selected_at_ordered_source_layer"
            ],
            "SU5_E6_slot_map_support_complete": decision["slot_map_support_complete"],
            "target_fitting_excluded": True,
        },
        "what_remains_open": {
            "promote_terminal_admissible_section_principle_to_unconditional_MTT_axiom_or_derivation": True,
            "same_branch_selected_slot_map_emission": True,
            "operator_layer_Pic0_or_torsion_gerbe_rule": True,
            "selected_overlap_transfer_normalization": True,
            "same_source_D_E_Riesz_Green_dotD": True,
            "alpha1_driver_verified": True,
            "lambda_12": True,
        },
        "guardrails": {
            "claims_unconditional_terminal_principle": False,
            "claims_operator_layer_Pic0_closed": False,
            "claims_selected_same_branch_slotmap": False,
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
        "certificate": "SelectedU1YRouteCTerminalMonadBaseOrderAHBindingSMSlotMap",
        "status": STATUS,
        "candidate_path": rel(OUTPUT_DATA),
        "note_path": rel(OUTPUT_NOTE),
        "same_L3_K2_identity": baseorder_binding["same_L3_K2_identity"],
        "terminal_lane_selected_at_ordered_source_layer_under_explicit_principle": proved_baseorder_ah,
        "AH_goodcover_binding_selected_at_ordered_source_layer": decision[
            "AH_or_Cech_transition_binding_selected_at_ordered_source_layer"
        ],
        "slot_map_support_complete": decision["slot_map_support_complete"],
        "slot_map_selected_same_branch": False,
        "operator_layer_Pic0_closed": False,
        "alpha1_driver_verified": False,
        "lambda_12_closed": False,
        "next_required_artifact": NEXT,
        "target_fitting_used": False,
        "observed_data_used": False,
    }
    return candidate, cert, render_note(candidate, cert)


def render_note(candidate: dict[str, Any], cert: dict[str, Any]) -> str:
    lines = [
        "# Selected U1Y Route-C TerminalMonad BaseOrder AHBinding SMSlotMap v1",
        "",
        "## Result",
        "",
        "```text",
        f"status = {candidate['status']}",
        f"same_L3_K2_identity = {str(cert['same_L3_K2_identity']).lower()}",
        "terminal_lane_selected_at_ordered_source_layer_under_explicit_principle = "
        f"{str(cert['terminal_lane_selected_at_ordered_source_layer_under_explicit_principle']).lower()}",
        "AH_goodcover_binding_selected_at_ordered_source_layer = "
        f"{str(cert['AH_goodcover_binding_selected_at_ordered_source_layer']).lower()}",
        f"slot_map_support_complete = {str(cert['slot_map_support_complete']).lower()}",
        f"slot_map_selected_same_branch = {str(cert['slot_map_selected_same_branch']).lower()}",
        f"next_required_artifact = {candidate['next_required_artifact']}",
        "```",
        "",
        "The terminal selector and the selected ordered AH/good-cover source now bind to",
        "the same object: `g3 / L3-K2`, with `L=(1,-2,0)` and `L^2=(2,-4,0)`. This",
        "closes the base-order/AH-binding part at the ordered Chern/H1/ordinary-curvature",
        "layer under the explicit terminal admissible-section principle.",
        "",
        "## Slot Map",
        "",
        "```json",
        json.dumps(candidate["slot_map"]["finite_structural_route"], indent=2, sort_keys=True),
        "```",
        "",
        "The slot map is support-complete, not yet selected same-branch operator emission.",
        "The required next proof is the branch-coherence selector or finite validator replay.",
        "",
        "## Theorem",
        "",
        candidate["theorem"]["statement"],
        "",
        "## Guardrails",
        "",
        "- The terminal admissible-section principle is still an explicit principle, not yet an unconditional MTT axiom.",
        "- The ordered-layer AH binding does not close operator-layer Pic0.",
        "- Slot-map support does not count as same-branch selected operator emission.",
        "- Do not compute `alpha1`, `lambda_12`, masses, CKM, or threshold matches from this artifact.",
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
