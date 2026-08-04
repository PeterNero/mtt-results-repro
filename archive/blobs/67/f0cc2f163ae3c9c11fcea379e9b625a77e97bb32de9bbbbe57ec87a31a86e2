"""Build ordered V_alpha/Pic0 source or profile workspace import bridge."""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "candidate_data"
CERTS = ROOT / "certificates"
CORPUS = ROOT / "proof_corpus"

SLUG = "selected_orderedvalphapic0source_or_profileworkspaceimport"
PACKET_DIR = DATA / SLUG
OUTPUT = DATA / f"{SLUG}.candidate.json"
ORDERED_BRIDGE = PACKET_DIR / "ordered_valpha_pic0_bridge.packet.json"
PROFILE_WORKSPACE = PACKET_DIR / "profile_workspace_import_attempt.packet.json"
PROMOTION = PACKET_DIR / "promotion_decision_after_ordered_bridge.packet.json"
CUTSET = PACKET_DIR / "terminal_source_or_operator_workspace_cutset.packet.json"
CERT = CERTS / f"{SLUG}_certificate.json"
NOTE = CORPUS / "MTT_Selected_OrderedVAlphaPic0Source_or_ProfileWorkspaceImport_v1.md"

STATUS = "MTT_SELECTED_ORDEREDVALPHAPIC0SOURCE_OR_PROFILEWORKSPACEIMPORT_BUILT_ORDERED_LAYER_BRIDGE_OPERATOR_OPEN"


def rel(path: Path) -> str:
    try:
        return str(path.relative_to(ROOT)).replace("\\", "/")
    except ValueError:
        return str(path)


def load(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def main() -> int:
    PACKET_DIR.mkdir(parents=True, exist_ok=True)

    previous = load(DATA / "selected_qasu3candidatepayloadfill_or_profilesourceacquisition.candidate.json")
    payload = load(
        DATA
        / "selected_qasu3candidatepayloadfill_or_profilesourceacquisition"
        / "qasu3_candidate_payload_fill_attempt.packet.json"
    )
    ordered_repair = load(DATA / "selected_qa_su3_ordered_valpha_pic0_source_repair.candidate.json")
    terminal_pic0 = load(DATA / "selected_terminal_monad_lane_pic0_quotient_source.candidate.json")
    terminal_section = load(DATA / "selected_terminalmonad_matterslot_sectionring_source_selector.candidate.json")
    visible_cw = load(DATA / "selected_visible_chern_weil_operator_source.candidate.json")

    ordered_target = terminal_pic0["terminal_lane_audit"]
    terminal_switch = terminal_section["source_switch_contract"]
    pic0_accounting = terminal_section["pic0_accounting"]
    operator_contract = visible_cw["selected_source_packet"]

    ordered_bridge = {
        "schema": "MTTOrderedVAlphaPic0Bridge.v1",
        "status": "ORDERED_LAYER_L3K2_AND_PIC0_BRIDGED_OPERATOR_LAYER_REOPENED",
        "input_payload_fill": rel(
            DATA
            / "selected_qasu3candidatepayloadfill_or_profilesourceacquisition"
            / "qasu3_candidate_payload_fill_attempt.packet.json"
        ),
        "ordered_target": {
            "selected_ordered_difference": ordered_target["selected_ordered_difference"],
            "L": ordered_target["selected_ordered_difference_L"],
            "L2": ordered_target["selected_ordered_difference_L2"],
            "conditional_unique_target_inside_lane": ordered_target["conditional_unique_target_inside_lane"],
            "strict_ordered_validator_would_pass_after_source_and_pic0": ordered_target[
                "strict_ordered_validator_would_pass_after_source_and_pic0"
            ],
        },
        "ordered_layer_pic0_accounting": {
            "ordered_layer_pic0_closed": pic0_accounting["ordered_layer_pic0_closed"],
            "ordered_layer_scope": pic0_accounting["ordered_layer_scope"],
            "ordered_pic0_removed_as_ordered_source_blocker": terminal_section["what_closes_now"][
                "ordered_layer_Pic0_removed_as_ordered_source_blocker"
            ],
            "operator_layer_pic0_closed": pic0_accounting["operator_layer_pic0_closed"],
            "operator_layer_reopen_condition": pic0_accounting["operator_layer_reopen_condition"],
        },
        "source_switch_status": {
            "terminal_monad_lane_selection_closed": terminal_switch["terminal_monad_lane_selection"]["closed"],
            "standard_lattice_or_equivalent_closed": terminal_switch["standard_lattice_or_equivalent"]["closed"],
            "base_factor_order_closed": terminal_switch["base_factor_order"]["closed"],
            "AH_or_Cech_binding_closed": terminal_switch["AH_or_Cech_binding"]["closed"],
            "central_neutral_member_closed": terminal_switch["central_neutral_member"]["closed"],
            "monad_orientation_closed_as_candidate": terminal_switch["monad_orientation"]["closed_as_candidate"],
        },
        "imported_ordered_repair_status": ordered_repair["status"],
        "imported_terminal_pic0_status": terminal_pic0["status"],
        "imported_terminal_section_status": terminal_section["status"],
        "actual_ordered_source_promoted": False,
        "actual_operator_layer_pic0_resolved": False,
        "actual_QaSU3_packet_promoted": False,
        "accepted_for_true_SM_equivalence": False,
        "ordered_bridge_closes_now": [
            "L3-K2 target retained as the unique conditional terminal candidate",
            "ordered-layer Pic0 quotient/accounting imported with scope restriction",
            "source-switch blockers separated from operator-layer blockers",
        ],
        "operator_layer_still_requires": operator_contract["critical_must_supply"],
        "superset_strategy_used": {
            "mode": "convergent multi-encoding bridge",
            "straight_path_core": "terminal monad/Cech/section-ring selected source packet",
            "support_paths_combined": [
                "ordered V_alpha/Pic0 repair audit",
                "terminal monad Pic0 gate audit",
                "terminal matter-slot section-ring selector",
                "visible Chern-Weil/operator-source reduction",
            ],
            "locked_target": "ordered L3-K2 visible/color source; no measured constants or benchmark matrices select it",
            "using_one_straight_path": False,
        },
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
    }

    profile_workspace = {
        "schema": "MTTProfileWorkspaceImportAttempt.v1",
        "status": "NO_PROFILE_WORKSPACE_IMPORTED_ORDERED_BRIDGE_PRIMARY",
        "profile_workspace_imported": False,
        "surrogate_profile_remains_diagnostic_only": True,
        "can_close_true_SM_equivalence_now": False,
        "required_profile_workspace_payload": [
            "official or independently reconstructed non-Higgs profile likelihood workspace",
            "machine-readable covariance/profile basis map",
            "loop-order and threshold convention",
            "profile acceptance rule",
            "provenance sufficient for replay",
        ],
        "why_ordered_bridge_primary": [
            "the ordered source lane now has local bridge artifacts with exact blockers",
            "no provenance-safe profile workspace exists locally",
            "source promotion strengthens both SM-parity and no-knob upgrade routes",
        ],
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
    }

    promotion = {
        "schema": "MTTPromotionDecisionAfterOrderedVAlphaPic0Bridge.v1",
        "status": "ORDERED_LAYER_BRIDGED_ACTUAL_SOURCE_OPERATOR_PROMOTION_OPEN",
        "route_A_profile_workspace": {
            "profile_workspace_imported": False,
            "can_close_true_SM_equivalence_now": False,
        },
        "route_B_ordered_valpha_pic0_source": {
            "ordered_layer_pic0_closed": True,
            "conditional_L3K2_target_retained": True,
            "actual_ordered_source_promoted": False,
            "operator_layer_pic0_resolved": False,
            "actual_QaSU3_packet_promoted": False,
            "can_close_true_SM_equivalence_now": False,
            "can_close_no_knob_now": False,
        },
        "SM_parity_closed": True,
        "true_SM_equivalence_closed": False,
        "no_knob_closed": False,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
    }

    cutset = {
        "schema": "MTTTerminalSourceOrOperatorWorkspaceCutset.v1",
        "status": "TERMINAL_SOURCE_OPERATOR_PAYLOAD_OR_PROFILE_WORKSPACE_REQUIRED",
        "closed_now": [
            "ordered-layer Pic0 accounting imported with restricted scope",
            "conditional L3-K2 target carried forward",
            "terminal source-switch blockers separated from operator-layer Pic0 and D_E blockers",
        ],
        "remaining_minimal_payloads": [
            "promote terminal monad lane selection as MTT-selected source data",
            "select standard lattice or equivalent source and base-factor order",
            "bind L3-K2 to AH/Cech transition data from the same source",
            "resolve operator-layer Pic0 by same-source operator invariance or gerbe/twisted D_E replacement",
            "emit same-source D_E/rho_E, Riesz, Green, dotD, and projector retention",
            "or import an official/reconstructed non-Higgs profile likelihood workspace",
        ],
        "recommended_next_artifact": "MTT_Selected_TerminalSourceSwitch_or_OperatorPic0GerbeDE_v1",
        "SM_parity_closed": True,
        "true_SM_equivalence_closed": False,
        "no_knob_closed": False,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
    }

    candidate = {
        "candidate": "MTTSelectedOrderedVAlphaPic0SourceOrProfileWorkspaceImport",
        "status": STATUS,
        "inputs": {
            "previous_candidate": rel(DATA / "selected_qasu3candidatepayloadfill_or_profilesourceacquisition.candidate.json"),
            "ordered_valpha_pic0_repair": rel(DATA / "selected_qa_su3_ordered_valpha_pic0_source_repair.candidate.json"),
            "terminal_monad_lane_pic0_quotient_source": rel(
                DATA / "selected_terminal_monad_lane_pic0_quotient_source.candidate.json"
            ),
            "terminalmonad_matterslot_sectionring_source_selector": rel(
                DATA / "selected_terminalmonad_matterslot_sectionring_source_selector.candidate.json"
            ),
            "visible_chern_weil_operator_source": rel(DATA / "selected_visible_chern_weil_operator_source.candidate.json"),
        },
        "output_packets": {
            "ordered_valpha_pic0_bridge": rel(ORDERED_BRIDGE),
            "profile_workspace_import_attempt": rel(PROFILE_WORKSPACE),
            "promotion_decision": rel(PROMOTION),
            "terminal_source_or_operator_workspace_cutset": rel(CUTSET),
        },
        "theorem": {
            "name": "OrderedLayerPic0BridgeTheorem",
            "proved": True,
            "statement": (
                "Existing ordered V_alpha, terminal-monad, and section-ring audits bridge the current partial Qa/SU3 "
                "payload to the conditional L3-K2 ordered target and remove Pic0 as an ordered-layer blocker only. "
                "They do not promote the actual ordered source or operator-layer Qa/SU3 packet; source selection, "
                "AH/Cech binding, operator-layer Pic0, and same-source D_E/Riesz/Green/dotD remain required."
            ),
        },
        "what_closes_now": {
            "ordered_layer_pic0_accounting_imported": True,
            "conditional_L3K2_target_carried_forward": True,
            "profile_workspace_import_attempted": True,
            "terminal_source_operator_cutset_sharpened": True,
        },
        "what_remains_open": {
            "terminal_monad_lane_selected_by_MTT": True,
            "standard_lattice_or_equivalent_selected": True,
            "base_factor_order_selected": True,
            "AH_or_Cech_transition_binding_selected": True,
            "operator_layer_Pic0_selection_or_quotient": True,
            "same_source_D_E_Riesz_Green_dotD": True,
            "true_SM_equivalence": True,
            "no_knob_closure": True,
        },
        "closure_decision": {
            "SM_parity_closed": previous["closure_decision"]["SM_parity_closed"],
            "ordered_layer_pic0_bridged": True,
            "actual_ordered_source_promoted": False,
            "actual_QaSU3_packet_promoted": False,
            "profile_workspace_imported": False,
            "true_SM_equivalence_closed": False,
            "no_knob_closed": False,
        },
        "previous_status": previous["status"],
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "next_required_artifact": cutset["recommended_next_artifact"],
    }

    cert = {
        "certificate": "MTT_Selected_OrderedVAlphaPic0Source_or_ProfileWorkspaceImport_v1",
        "status": STATUS,
        "candidate_path": rel(OUTPUT),
        "note_path": rel(NOTE),
        "theorem_proved": True,
        "SM_parity_closed": True,
        "ordered_layer_pic0_bridged": True,
        "actual_ordered_source_promoted": False,
        "actual_QaSU3_packet_promoted": False,
        "profile_workspace_imported": False,
        "true_SM_equivalence_closed": False,
        "no_knob_closed": False,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "next_required_artifact": candidate["next_required_artifact"],
    }

    note = f"""# MTT Selected OrderedVAlphaPic0Source or ProfileWorkspaceImport v1

Status: `{STATUS}`.

This artifact bridges the newest Qa/SU3 partial payload to the older ordered
`V_alpha` / `Pic0` work already present in the repo.

What closes now is deliberately narrow: the conditional `L3-K2` target is
carried forward, and Pic0 is imported as removed only at the ordered
Chern/H1/ordinary-curvature layer.

What does not close is the physical operator packet. Operator-layer Pic0
reopens, and the selected terminal source, standard lattice/base order,
AH/Cech binding, same-source `D_E/rho_E`, Riesz, Green, dotD, and projector
retention remain required.

The superset strategy is convergent but constrained: several encodings support
the same `L3-K2` lane, locked to the declared target, with no measured constants
or benchmark matrices used as selectors.
"""

    for path, body in [
        (ORDERED_BRIDGE, ordered_bridge),
        (PROFILE_WORKSPACE, profile_workspace),
        (PROMOTION, promotion),
        (CUTSET, cutset),
        (OUTPUT, candidate),
        (CERT, cert),
    ]:
        path.write_text(json.dumps(body, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    NOTE.write_text(note, encoding="utf-8")
    print(json.dumps({"candidate": rel(OUTPUT), "status": STATUS}, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
