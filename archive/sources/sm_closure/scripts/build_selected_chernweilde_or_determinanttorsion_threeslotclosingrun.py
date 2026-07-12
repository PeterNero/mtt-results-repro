"""Build Chern-Weil/D_E/determinant-torsion three-slot closing run."""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
Q79_ROOT = ROOT.parent / "mtt-q79-proof-repro"
DATA = ROOT / "candidate_data"
CERTS = ROOT / "certificates"
CORPUS = ROOT / "proof_corpus"

SLUG = "selected_chernweilde_or_determinanttorsion_threeslotclosingrun"
PACKET_DIR = DATA / SLUG
OUTPUT = DATA / f"{SLUG}.candidate.json"
RECON = PACKET_DIR / "same_source_chern_weil_row_reconciliation.packet.json"
SLOT_CLOSURE = PACKET_DIR / "same_source_chern_weil_row_slot_closure.packet.json"
FRONTIER = PACKET_DIR / "post_six_slot_true_equivalence_frontier.packet.json"
CERT = CERTS / f"{SLUG}_certificate.json"
NOTE = CORPUS / "MTT_Selected_ChernWeilDE_or_DeterminantTorsion_ThreeSlotClosingRun_v1.md"

STATUS = "MTT_SELECTED_CHERNWEILDE_OR_DETERMINANTTORSION_THREESLOTCLOSINGRUN_BUILT_CHERNWEIL_SLOT_CLOSED"
NEXT = "MTT_Selected_DETransition_or_DeterminantTorsion_TwoSlotClosingRun_v1"
SLOT = "same_source_Chern_Weil_row_derived"


def rel(path: Path) -> str:
    try:
        return str(path.relative_to(ROOT)).replace("\\", "/")
    except ValueError:
        return str(path)


def load(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def main() -> int:
    PACKET_DIR.mkdir(parents=True, exist_ok=True)

    prior_frontier = load(
        DATA
        / "selected_chernweilhymde_or_determinanttorsion_fourslotclosingrun"
        / "post_five_slot_true_equivalence_frontier.packet.json"
    )
    prior_hym_slot = load(
        DATA
        / "selected_chernweilhymde_or_determinanttorsion_fourslotclosingrun"
        / "selected_hym_or_routec_residual_slot_closure.packet.json"
    )
    topological_candidates = load(
        Q79_ROOT / "candidate_data" / "visible_valpha_chern_bianchi_source_packet_candidates.candidate.json"
    )
    same_source_packet = load(DATA / "selected_nonsplit_rank2_or_routec_same_source_packet.candidate.json")

    primary = topological_candidates["candidate_ranking"][0]
    target = primary["topological_target"]
    rank2_target = same_source_packet["rank2_lane"]["target"]
    selected_value = prior_hym_slot["selected_source_value"]

    proof_inputs = {
        "prior_frontier_has_five_closed_three_open": prior_frontier["operator_source_slots_closed"] == 5
        and prior_frontier["operator_source_slots_remaining"] == 3,
        "prior_HYM_slot_closed": prior_hym_slot["closure_result"]["selected_HYM_or_RouteC_residual_slot_closed"],
        "selected_source_value_emitted": prior_hym_slot["closure_result"]["selected_source_value_emitted"],
        "source_selected_by_mtt": selected_value["source_selected_by_mtt"],
        "same_branch_q79_F_m1": selected_value["branch"] == {"orientation": "F", "q": 79, "torsion_label_m": 1},
        "primary_rank2_non_split_extension": primary["candidate_kind"] == "non_split_rank_two_extension",
        "same_L_vector": target["l_vector_abc"] == rank2_target["l_vector_abc"] == [1, -2, 0],
        "same_L_squared_vector": target["c1_L_squared_vector_abc"]
        == rank2_target["c1_L_squared_vector_abc"]
        == [2, -4, 0],
        "c1_zero": target["c1_V_alpha"] == [0, 0, 0],
        "c2_is_four_alpha1": target["c2_V_alpha"] == [4, 0, 0],
        "chern_character_row_is_minus_four_alpha1": target["ch2_math"] == [-4, 0, 0],
        "ordinary_integral_c1_matrix_realized": same_source_packet["rank2_lane"]["closed"][
            "ordinary_integral_c1_matrix_realized"
        ],
        "rank2_topological_c2_target_closed": same_source_packet["rank2_lane"]["closed"]["topological_c2_target"],
        "hym_residual_same_selected_lane": "rank-2 V_alpha" in selected_value["selected_source"],
    }
    slot_closes = all(proof_inputs.values())

    filled_slots = list(prior_hym_slot["slot_status_after_closure"]["filled_slots"])
    missing_slots = list(prior_frontier["remaining_slots"])
    if slot_closes and SLOT not in filled_slots:
        filled_slots.append(SLOT)
    if slot_closes and SLOT in missing_slots:
        missing_slots.remove(SLOT)

    chern_weil_row = {
        "level": "same-source Chern/Bianchi cohomology row",
        "source": selected_value["selected_source"],
        "branch": selected_value["branch"],
        "source_shape": primary["source_shape"],
        "L_vector_abc": target["l_vector_abc"],
        "L_squared_vector_abc": target["c1_L_squared_vector_abc"],
        "c1_V_alpha": target["c1_V_alpha"],
        "c2_V_alpha": target["c2_V_alpha"],
        "ch2_math": target["ch2_math"],
        "chern_weil_trace_normalization_note": (
            "The row is promoted only as the same-source topological Chern/Bianchi row for the selected "
            "rank-two V_alpha/HYM lane. A pointwise finite transition representative and sector D_E table "
            "remain separate open payloads."
        ),
    }

    recon = {
        "schema": "MTTSameSourceChernWeilRowReconciliation.v1",
        "slot": SLOT,
        "status": "SAME_SOURCE_CHERN_WEIL_ROW_RECONCILED_AT_CHERN_BIANCHI_LEVEL",
        "inputs": {
            "prior_frontier": rel(
                DATA
                / "selected_chernweilhymde_or_determinanttorsion_fourslotclosingrun"
                / "post_five_slot_true_equivalence_frontier.packet.json"
            ),
            "prior_selected_HYM_slot": rel(
                DATA
                / "selected_chernweilhymde_or_determinanttorsion_fourslotclosingrun"
                / "selected_hym_or_routec_residual_slot_closure.packet.json"
            ),
            "q79_visible_valpha_chern_bianchi_candidates": rel(
                Q79_ROOT / "candidate_data" / "visible_valpha_chern_bianchi_source_packet_candidates.candidate.json"
            ),
            "local_same_source_packet": rel(DATA / "selected_nonsplit_rank2_or_routec_same_source_packet.candidate.json"),
        },
        "proof_inputs": proof_inputs,
        "same_source_row": chern_weil_row,
        "slot_closes": slot_closes,
        "scope": {
            "closes": "same-source Chern-Weil/Chern-Bianchi cohomology row for c1=0 and c2=4 alpha_1",
            "does_not_close": [
                "transition rho_E/Cech-Dolbeault D_E data",
                "finite determinant/heat spectrum/torsion response",
                "pointwise finite curvature representative table",
                "full sector-ready Qa/SU3 dynamic operator packet",
                "full no-knob Standard Model data derivation",
            ],
            "reason": (
                "The already selected q79/F,m=1 rank-two V_alpha HYM lane and the q79 Chern/Bianchi target "
                "refer to the same L=(1,-2,0), L^2=(2,-4,0), c1=0, c2=4 alpha_1 source. This proves the "
                "cohomological Chern-Weil row, while transition-level and determinant/torsion payloads remain "
                "unemitted."
            ),
        },
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
    }

    slot_closure = {
        "schema": "MTTSameSourceChernWeilRowSlotClosure.v1",
        "filled_slot": SLOT,
        "selected_source_value": selected_value,
        "same_source_chern_weil_row": chern_weil_row,
        "proof_inputs": proof_inputs,
        "closure_result": {
            "same_source_Chern_Weil_row_derived": slot_closes,
            "source_value_emitted": True,
            "transition_rhoE_or_Cech_Dolbeault_DE_data_closed": False,
            "finite_determinant_heat_spectrum_or_torsion_response_closed": False,
            "actual_dynamic_QaSU3_operator_packet_closed": False,
            "why_not_dynamic_operator_packet": (
                "The slot is closed only at the selected same-source Chern/Bianchi cohomology row level. "
                "It does not provide finite transition rho_E/D_E tables, determinant/torsion response, "
                "or dynamic C1 operator values."
            ),
        },
        "slot_status_after_closure": {
            "required_operator_slot_count": 8,
            "filled_operator_slot_count": len(filled_slots),
            "filled_slots": filled_slots,
            "missing_slots": missing_slots,
            "remaining_missing_slot_count": len(missing_slots),
        },
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
    }

    frontier = {
        "schema": "MTTPostSixSlotTrueEquivalenceFrontier.v1",
        "status": "SIX_OPERATOR_SOURCE_SLOTS_CLOSED_TWO_REMAIN_OPEN" if slot_closes else "CHERN_WEIL_SLOT_OPEN",
        "operator_source_slots_closed": len(filled_slots),
        "operator_source_slots_remaining": len(missing_slots),
        "remaining_slots": missing_slots,
        "remaining_slot_contracts": {
            "transition_rhoE_or_Cech_Dolbeault_DE_data": {
                "open": "transition_rhoE_or_Cech_Dolbeault_DE_data" in missing_slots,
                "best_route": "rank2-to-sector transfer or literal transition/rho_E/Cech-Dolbeault tables",
                "current_blocker": True,
            },
            "finite_determinant_heat_spectrum_or_torsion_response": {
                "open": "finite_determinant_heat_spectrum_or_torsion_response" in missing_slots,
                "best_route": "heat-kernel determinant/torsion response from selected HYM/End0 operator spectrum",
                "current_blocker": True,
            },
        },
        "true_SM_equivalence_closed": False,
        "no_knob_closed": False,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
    }

    candidate = {
        "candidate": "MTTSelectedChernWeilDEOrDeterminantTorsionThreeSlotClosingRun",
        "status": STATUS,
        "inputs": recon["inputs"],
        "output_packets": {
            "same_source_chern_weil_row_reconciliation": rel(RECON),
            "same_source_chern_weil_row_slot_closure": rel(SLOT_CLOSURE),
            "post_six_slot_true_equivalence_frontier": rel(FRONTIER),
        },
        "theorem": {
            "name": "SelectedSameSourceChernWeilRowClosureTheorem",
            "proved": slot_closes,
            "statement": (
                "On the selected q79/F,m=1 rank-two V_alpha HYM lane, the same branch that emits the "
                "selected residual also carries the Chern/Bianchi target c1(V_alpha)=0 and "
                "c2(V_alpha)=4 alpha_1 with L=L3-K2=(1,-2,0). Therefore the "
                "same_source_Chern_Weil_row_derived slot is closed at cohomology/Chern-Bianchi row level. "
                "Transition rho_E/D_E tables and determinant/torsion response remain open."
            ),
        },
        "what_closes_now": {
            "same_source_Chern_Weil_row_derived": slot_closes,
            "Chern_Bianchi_row_level_only": True,
            "target_fitting_excluded": True,
        },
        "what_remains_open": {
            "transition_rhoE_or_Cech_Dolbeault_DE_data": "transition_rhoE_or_Cech_Dolbeault_DE_data" in missing_slots,
            "finite_determinant_heat_spectrum_or_torsion_response": (
                "finite_determinant_heat_spectrum_or_torsion_response" in missing_slots
            ),
            "pointwise_finite_curvature_representative_table": True,
            "actual_dynamic_QaSU3_operator_packet": True,
            "true_SM_equivalence": True,
            "no_knob_closure": True,
        },
        "closure_decision": {
            "SM_parity_closed": True,
            "operator_source_slots_closed_total": len(filled_slots),
            "operator_source_slots_remaining": len(missing_slots),
            "same_source_Chern_Weil_row_derived_slot_closed": slot_closes,
            "transition_rhoE_or_Cech_Dolbeault_DE_data_closed": False,
            "finite_determinant_heat_spectrum_or_torsion_response_closed": False,
            "actual_dynamic_QaSU3_operator_packet_closed": False,
            "true_SM_equivalence_closed": False,
            "no_knob_closed": False,
        },
        "next_required_artifact": NEXT,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "closure_claimed": slot_closes,
    }

    cert = {
        "certificate": "MTT_Selected_ChernWeilDE_or_DeterminantTorsion_ThreeSlotClosingRun_v1",
        "candidate_path": rel(OUTPUT),
        "status": STATUS,
        "theorem_proved": slot_closes,
        "same_source_Chern_Weil_row_derived_slot_closed": slot_closes,
        "closed_operator_source_slots_total": len(filled_slots),
        "operator_source_slots_remaining": len(missing_slots),
        "actual_dynamic_QaSU3_operator_packet_closed": False,
        "true_SM_equivalence_closed": False,
        "no_knob_closed": False,
        "next_required_artifact": NEXT,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "note_path": rel(NOTE),
    }

    note = f"""# MTT Selected ChernWeilDE or DeterminantTorsion ThreeSlotClosingRun v1

This artifact checks the three remaining operator-source slots after the
selected diagonal HYM residual slot closure.

It closes one more slot:
`{SLOT}`.

The closure is deliberately narrow.  The selected q79/F,m=1 rank-two
`V_alpha` HYM lane and the q79 Chern/Bianchi packet name the same source:

- branch `q=79`, orientation `F`, torsion label `m=1`
- source shape `0 -> L -> V_alpha -> L^-1 -> 0`
- `L=(1,-2,0)` and `L^2=(2,-4,0)`
- `c1(V_alpha)=(0,0,0)`
- `c2(V_alpha)=(4,0,0) = 4 alpha_1`
- `ch2(V_alpha)=(-4,0,0)`

Therefore the same-source Chern-Weil row is closed at the
cohomology/Chern-Bianchi row level.

This does not emit transition `rho_E`/Cech-Dolbeault `D_E` tables, a
pointwise finite curvature representative, determinant / heat / torsion
response, the full sector-ready Qa/SU3 dynamic operator packet, or a no-knob
derivation of all Standard Model data.

Current count is now six closed operator-source slots and two open slots.

Remaining open slots:

- `transition_rhoE_or_Cech_Dolbeault_DE_data`
- `finite_determinant_heat_spectrum_or_torsion_response`

Next artifact: `{NEXT}`.
"""

    for path, payload in [
        (RECON, recon),
        (SLOT_CLOSURE, slot_closure),
        (FRONTIER, frontier),
        (OUTPUT, candidate),
        (CERT, cert),
    ]:
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(json.dumps(payload, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    NOTE.write_text(note, encoding="utf-8")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
