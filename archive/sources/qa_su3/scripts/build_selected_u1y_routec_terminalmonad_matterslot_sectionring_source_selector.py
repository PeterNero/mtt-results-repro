"""Build the U1/Y Route-C terminal-monad matter-slot section-ring source selector gate."""

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
    "orientation_selector": DATA / "selected_u1y_routec_matterslot_orientationselector_from_hym_finitereplay.candidate.json",
    "sm_terminal_selector": SM / "candidate_data" / "selected_terminalmonad_matterslot_sectionring_source_selector.candidate.json",
    "sm_terminal_selector_certificate": SM / "certificates" / "selected_terminalmonad_matterslot_sectionring_source_selector_certificate.json",
    "sm_terminal_pic0_gate": SM / "candidate_data" / "selected_terminal_monad_lane_pic0_quotient_source.candidate.json",
    "sm_grading_readout": SM / "candidate_data" / "selected_matterslot_grading_or_sectionring_readout.candidate.json",
}

OUTPUT_DATA = DATA / "selected_u1y_routec_terminalmonad_matterslot_sectionring_source_selector.candidate.json"
OUTPUT_CERT = CERTS / "selected_u1y_routec_terminalmonad_matterslot_sectionring_source_selector_certificate.json"
OUTPUT_NOTE = PROOF / "Selected_U1Y_RouteC_TerminalMonad_MatterSlot_SectionRing_SourceSelector_v1.md"

STATUS = "U1Y_ROUTEC_TERMINALMONAD_MATTERSLOT_SELECTOR_REDUCED_BASEORDER_AHBINDING_SLOTMAP_OPEN"
NEXT = "Selected_U1Y_RouteC_TerminalMonad_BaseOrder_AHBinding_SMSlotMap_v1"


def load(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def rel(path: Path) -> str:
    try:
        return str(path.relative_to(ROOT))
    except ValueError:
        return str(path)


def build() -> tuple[dict[str, Any], dict[str, Any], str]:
    orientation = load(INPUTS["orientation_selector"])
    sm_selector = load(INPUTS["sm_terminal_selector"])
    sm_cert = load(INPUTS["sm_terminal_selector_certificate"])
    sm_pic0 = load(INPUTS["sm_terminal_pic0_gate"])
    sm_grading = load(INPUTS["sm_grading_readout"])

    source_switch = sm_selector["source_switch_contract"]
    slot_map = sm_selector["matter_slot_map_contract"]
    pic0 = sm_selector["pic0_accounting"]
    switches = sm_selector["two_switch_reduction"]
    terminal_pic0 = sm_pic0["terminal_lane_audit"]

    imported_terminal_candidate = {
        "forced_label": source_switch["central_neutral_member"]["forced_label"],
        "forced_value": source_switch["central_neutral_member"]["forced_value"],
        "forced_double": source_switch["central_neutral_member"]["forced_double"],
        "ordered_pair": source_switch["central_neutral_member"]["ordered_pair"],
        "closed_as_unique_candidate": source_switch["central_neutral_member"]["closed"]
        and terminal_pic0["conditional_unique_target_inside_lane"],
        "selected_by_mtt": source_switch["terminal_monad_lane_selection"]["closed"],
    }

    ordered_layer_pic0_result = {
        "ordered_layer_pic0_removed_as_blocker": pic0["ordered_layer_pic0_closed"]
        and pic0["ordered_layer_validator_after_quotient"]["pic0_items_absent"],
        "scope": pic0["ordered_layer_scope"],
        "operator_layer_pic0_closed": pic0["operator_layer_pic0_closed"],
        "operator_layer_reopen_condition": pic0["operator_layer_reopen_condition"],
        "switch_table_imported": switches["switch_table_imported"],
        "source_and_pic0_passes_ordered_validator": switches["source_and_pic0_passes_ordered_validator"],
    }

    source_selector_obligations = {
        "terminal_monad_lane_selected_by_MTT": {
            "closed": source_switch["terminal_monad_lane_selection"]["closed"],
            "must_emit": source_switch["terminal_monad_lane_selection"]["must_emit"],
        },
        "standard_lattice_or_equivalent_selected": {
            "closed": source_switch["standard_lattice_or_equivalent"]["closed"],
            "must_emit": source_switch["standard_lattice_or_equivalent"]["must_emit"],
        },
        "base_factor_order_selected": {
            "closed": source_switch["base_factor_order"]["closed"],
            "must_emit": source_switch["base_factor_order"]["must_emit"],
        },
        "AH_or_Cech_transition_binding_selected": {
            "closed": source_switch["AH_or_Cech_binding"]["closed"],
            "support_closed": source_switch["AH_or_Cech_binding"]["support_closed"],
            "must_emit": source_switch["AH_or_Cech_binding"]["must_emit"],
        },
        "operator_layer_Pic0_or_torsion_gerbe_rule": {
            "closed": pic0["operator_layer_pic0_closed"],
            "must_emit": "operator-layer Pic0 selection, physical quotient theorem, or same-source gerbe/twisted D_E replacement",
        },
        "section_ring_to_SU5_E6_slot_map": {
            "closed": slot_map["closed"],
            "must_emit": slot_map["must_emit"],
            "must_map_without_locked_C1_columns": slot_map["must_map_without_locked_C1_columns"],
        },
    }
    closed_obligations = sum(1 for row in source_selector_obligations.values() if row["closed"] is True)

    slot_map_contract = {
        "closed": slot_map["closed"],
        "must_map_without_locked_C1_columns": slot_map["must_map_without_locked_C1_columns"],
        "must_preserve_q79_polarization": slot_map["must_preserve_q79_polarization"],
        "promotes_if_closed": [
            "selected_matter_slot_orientation_emitted",
            "selected_U10_Ubar5_polarization_emitted",
            "selected_1M_Dirac_source_emitted",
            "selected_overlap_normalization_emitted",
            "N_alpha1_h_ext_promoted_to_du_dalpha1",
            "alpha1_driver_verified",
        ],
    }

    routec_bypass = {
        "retained": sm_selector["routec_bypass"]["retained"],
        "reason": sm_selector["routec_bypass"]["reason"],
        "minimum_required": sm_selector["routec_bypass"]["minimum_required"],
    }

    decision = {
        "terminal_selector_gate_built": True,
        "L3_K2_unique_terminal_candidate_imported": imported_terminal_candidate["closed_as_unique_candidate"],
        "terminal_monad_lane_selected_by_MTT": False,
        "ordered_layer_Pic0_removed_as_ordered_source_blocker": ordered_layer_pic0_result[
            "ordered_layer_pic0_removed_as_blocker"
        ],
        "operator_layer_Pic0_closed": False,
        "matter_slot_map_closed": False,
        "selected_matter_slot_orientation_emitted": False,
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
        "name": "U1YRouteCTerminalMonadMatterSlotSectionRingSelectorReduction",
        "proved": True,
        "statement": (
            "The U1/Y Route-C matter-slot orientation problem is reduced to the "
            "terminal monad/Cech/section-ring source packet. The imported SM parity "
            "selector fixes L3-K2=(1,-2,0), double (2,-4,0), as the unique central-neutral "
            "terminal candidate and removes Pic0 as an ordered Chern/H1/ordinary-curvature "
            "blocker. It does not yet select the terminal lane by MTT, the standard lattice "
            "or base factor order, the AH/Cech representative, operator-layer Pic0/torsion "
            "discipline, or the section-ring-to-SU5/E6 matter-slot map. Thus orientation "
            "still remains open, but the missing packet is now explicit and target-free."
        ),
    }

    candidate = {
        "candidate": "SelectedU1YRouteCTerminalMonadMatterSlotSectionRingSourceSelector",
        "status": STATUS,
        "inputs": {key: rel(path) for key, path in INPUTS.items()},
        "parent_status": orientation["status"],
        "imported_terminal_candidate": imported_terminal_candidate,
        "ordered_layer_pic0_result": ordered_layer_pic0_result,
        "source_selector_obligations": source_selector_obligations,
        "closed_obligations": closed_obligations,
        "slot_map_contract": slot_map_contract,
        "routec_bypass": routec_bypass,
        "decision": decision,
        "theorem": theorem,
        "what_closes_now": {
            "L3_K2_unique_terminal_candidate": imported_terminal_candidate["closed_as_unique_candidate"],
            "ordered_layer_Pic0_removed_as_ordered_source_blocker": ordered_layer_pic0_result[
                "ordered_layer_pic0_removed_as_blocker"
            ],
            "matter_slot_map_contract_imported": True,
            "terminal_selector_reduced_to_baseorder_AHbinding_slotmap": True,
            "routec_bypass_preserved": routec_bypass["retained"],
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
            "lambda_12": True,
        },
        "next_required_artifact": NEXT,
        "closure_claimed": False,
        "target_fitting_used": False,
        "observed_data_used": False,
        "guardrails": {
            "claims_selected_matter_slot_orientation": False,
            "claims_selected_U10_Ubar5": False,
            "claims_selected_1M_Dirac_source": False,
            "claims_selected_overlap_normalization": False,
            "claims_operator_layer_Pic0_closed": False,
            "claims_alpha1_driver_verified": False,
            "claims_lambda12": False,
            "uses_observed_data": False,
            "uses_benchmark_data": False,
            "uses_locked_C1_columns": False,
            "target_fitting_used": False,
        },
        "source_certificate_import": {
            "status": sm_cert["status"],
            "theorem_proved": sm_cert["theorem_proved"],
            "closure_claimed": sm_cert["closure_claimed"],
            "next_required_artifact": sm_cert["next_required_artifact"],
        },
        "grading_parent_status": sm_grading["status"],
    }

    cert = {
        "certificate": "SelectedU1YRouteCTerminalMonadMatterSlotSectionRingSourceSelector",
        "status": STATUS,
        "candidate_path": rel(OUTPUT_DATA),
        "note_path": rel(OUTPUT_NOTE),
        "L3_K2_unique_terminal_candidate": imported_terminal_candidate["closed_as_unique_candidate"],
        "ordered_layer_Pic0_removed_as_ordered_source_blocker": ordered_layer_pic0_result[
            "ordered_layer_pic0_removed_as_blocker"
        ],
        "closed_obligations": closed_obligations,
        "required_obligations": len(source_selector_obligations),
        "selected_matter_slot_orientation_emitted": False,
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
        "# Selected U1Y Route-C TerminalMonad MatterSlot SectionRing SourceSelector v1",
        "",
        "## Result",
        "",
        "```text",
        f"status = {candidate['status']}",
        f"L3_K2_unique_terminal_candidate = {str(cert['L3_K2_unique_terminal_candidate']).lower()}",
        f"ordered_layer_Pic0_removed_as_ordered_source_blocker = {str(cert['ordered_layer_Pic0_removed_as_ordered_source_blocker']).lower()}",
        f"closed_obligations = {cert['closed_obligations']} / {cert['required_obligations']}",
        f"selected_matter_slot_orientation_emitted = {str(cert['selected_matter_slot_orientation_emitted']).lower()}",
        f"next_required_artifact = {candidate['next_required_artifact']}",
        "```",
        "",
        "The terminal-monad route now has a sharper source packet. `L3-K2=(1,-2,0)`",
        "with double `(2,-4,0)` is the unique central-neutral terminal candidate,",
        "and Pic0 is removed at the ordered Chern/H1/ordinary-curvature layer. The",
        "operator layer still has to recheck Pic0 or replace it by a selected",
        "gerbe/twisted source.",
        "",
        "## Open Obligations",
        "",
        "| Obligation | Closed | Must Emit |",
        "| --- | --- | --- |",
    ]
    for key, row in candidate["source_selector_obligations"].items():
        lines.append(f"| `{key}` | `{str(row['closed']).lower()}` | `{row['must_emit']}` |")
    lines.extend(
        [
            "",
            "## Slot Map Contract",
            "",
            "```json",
            json.dumps(candidate["slot_map_contract"]["must_map_without_locked_C1_columns"], indent=2, sort_keys=True),
            "```",
            "",
            "## Theorem",
            "",
            candidate["theorem"]["statement"],
            "",
            "## Guardrails",
            "",
            "- Do not treat the unique `L3-K2` candidate as MTT-selected lane emission yet.",
            "- Do not inherit ordered-layer Pic0 quotient into the operator layer.",
            "- Do not use locked C1 splitter columns, observed masses, CKM/PMNS, or benchmark flavor matrices.",
            "- Do not promote orientation, `alpha1_driver_verified`, or `lambda_12` here.",
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
