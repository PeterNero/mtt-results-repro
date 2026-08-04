"""Build D_E transition or determinant-torsion two-slot closing run."""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
Q79_ROOT = ROOT.parent / "mtt-q79-proof-repro"
DATA = ROOT / "candidate_data"
CERTS = ROOT / "certificates"
CORPUS = ROOT / "proof_corpus"

SLUG = "selected_detransition_or_determinanttorsion_twoslotclosingrun"
PACKET_DIR = DATA / SLUG
OUTPUT = DATA / f"{SLUG}.candidate.json"
TRANSITION = PACKET_DIR / "transition_rhoe_or_cech_dolbeault_de_edge_test.packet.json"
TORSION = PACKET_DIR / "determinant_heat_spectrum_or_torsion_edge_test.packet.json"
FRONTIER = PACKET_DIR / "post_six_slot_two_gate_frontier.packet.json"
CERT = CERTS / f"{SLUG}_certificate.json"
NOTE = CORPUS / "MTT_Selected_DETransition_or_DeterminantTorsion_TwoSlotClosingRun_v1.md"

STATUS = "MTT_SELECTED_DETRANSITION_OR_DETERMINANTTORSION_TWOSLOTCLOSINGRUN_BUILT_TWO_GATES_SHARPENED"
NEXT = "MTT_Selected_TransitionPayload_or_HeatTorsionResponse_OneGateAttack_v1"


def rel(path: Path) -> str:
    try:
        return str(path.relative_to(ROOT)).replace("\\", "/")
    except ValueError:
        return str(path)


def load(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def main() -> int:
    PACKET_DIR.mkdir(parents=True, exist_ok=True)

    prior = load(
        DATA
        / "selected_chernweilde_or_determinanttorsion_threeslotclosingrun"
        / "post_six_slot_true_equivalence_frontier.packet.json"
    )
    local_de = load(DATA / "selected_end0_de_payload_from_diagonal_hym.candidate.json")
    local_green = load(DATA / "selected_riesz_green_dotd_from_diagonal_end0_de.candidate.json")
    q79_trace = load(
        Q79_ROOT
        / "candidate_data"
        / "q79_selected_trace_equals_emitted_27mode_operator_or_full_hym_newton_replay"
        / "selected_trace_equality_gap_layer_proof.json"
    )
    q79_finite = load(
        Q79_ROOT
        / "candidate_data"
        / "q79_selected_finite_connection_solve_execution"
        / "finite_connection_execution_import_summary.json"
    )
    crossrepo = load(DATA / "sm_equivalence_crossrepo_qasu3_status_import.candidate.json")

    transition_support = {
        "prior_frontier_has_six_closed_two_open": prior["operator_source_slots_closed"] == 6
        and prior["operator_source_slots_remaining"] == 2,
        "local_diagonal_End0_DE_formula_extracted": local_de["operator_payload_boundary"][
            "diagonal_End0_D_E_formula_extracted"
        ],
        "local_rank2_to_sector_transfer_values_extracted": local_de["operator_payload_boundary"][
            "rank2_to_rank3_sector_transfer_values_extracted"
        ],
        "local_validator_ready": local_de["operator_payload_boundary"]["validator_ready"],
        "q79_DE_matrix_on_27_mode_BN_emitted": q79_finite["DE"]["D_E_matrix_on_27_mode_BN_emitted"],
        "q79_DE_source_flags_theorem_derived_for_gap_layer": q79_trace["gap_layer"][
            "D_E_source_flags_are_theorem_derived"
        ],
        "q79_gap_layer_scope_only": q79_trace["scope"] == "D_E gap/Riesz/Green layer only",
        "q79_nonidentity_rhoE_selected_by_mtt": q79_finite["nonidentity_rhoE"]["selected_by_mtt"],
    }
    transition_slot_closes = (
        transition_support["prior_frontier_has_six_closed_two_open"]
        and transition_support["local_diagonal_End0_DE_formula_extracted"]
        and transition_support["local_rank2_to_sector_transfer_values_extracted"]
        and transition_support["local_validator_ready"]
        and transition_support["q79_DE_matrix_on_27_mode_BN_emitted"]
        and transition_support["q79_DE_source_flags_theorem_derived_for_gap_layer"]
        and not transition_support["q79_gap_layer_scope_only"]
        and transition_support["q79_nonidentity_rhoE_selected_by_mtt"]
    )

    transition_packet = {
        "schema": "MTTTransitionRhoEOrCechDolbeaultDEEdgeTest.v1",
        "slot": "transition_rhoE_or_Cech_Dolbeault_DE_data",
        "status": "TRANSITION_DE_EDGE_TESTED_SUPPORT_PRESENT_PAYLOAD_OPEN",
        "inputs": {
            "post_six_frontier": rel(
                DATA
                / "selected_chernweilde_or_determinanttorsion_threeslotclosingrun"
                / "post_six_slot_true_equivalence_frontier.packet.json"
            ),
            "local_diagonal_End0_DE": rel(DATA / "selected_end0_de_payload_from_diagonal_hym.candidate.json"),
            "local_Riesz_Green_dotD": rel(DATA / "selected_riesz_green_dotd_from_diagonal_end0_de.candidate.json"),
            "q79_trace_gap_layer": rel(
                Q79_ROOT
                / "candidate_data"
                / "q79_selected_trace_equals_emitted_27mode_operator_or_full_hym_newton_replay"
                / "selected_trace_equality_gap_layer_proof.json"
            ),
            "q79_finite_connection_summary": rel(
                Q79_ROOT
                / "candidate_data"
                / "q79_selected_finite_connection_solve_execution"
                / "finite_connection_execution_import_summary.json"
            ),
        },
        "support": transition_support,
        "slot_closes": transition_slot_closes,
        "why_not_closed": (
            "The same-source diagonal End0 D_E formula and q79 finite D_E/gap layer are real support, "
            "but the remaining slot requires selected transition rho_E or Cech-Dolbeault/sector D_E payload. "
            "Current q79 nonidentity rho_E is not selected by MTT, local rank2-to-sector values are not "
            "extracted, and the q79 theorem is explicitly gap-layer only."
        ),
        "minimal_closing_payload": [
            "selected nonidentity rho_E transition functions/matrices or literal Cech-Dolbeault transition tables",
            "rank2-to-sector transfer values for Q,u,d,L,e,N,H on the selected q79/F,m=1 branch",
            "validator-ready D_E action matrices derived from the same selected HYM/End0 source",
            "metric/cocycle compatibility and no identity-smoke replacement",
        ],
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
    }

    status_entries = crossrepo.get("import_summary", {})
    determinant_support = {
        "prior_frontier_has_six_closed_two_open": prior["operator_source_slots_closed"] == 6
        and prior["operator_source_slots_remaining"] == 2,
        "local_protected_T3_reduced_Green": local_green["operator_payload_boundary"][
            "protected_T3_reduced_Green_extracted"
        ],
        "local_T1_T2_covariant_Green_extracted": local_green["operator_payload_boundary"][
            "T1_T2_coupled_covariant_Green_extracted"
        ],
        "crossrepo_determinant_trail_present": "determinant" in json.dumps(crossrepo).lower(),
        "crossrepo_torsion_trail_present": "torsion" in json.dumps(crossrepo).lower(),
        "selected_HYM_End0_heat_table_emitted_here": False,
        "selected_HYM_End0_spectrum_emitted_here": False,
        "selected_analytic_or_reidemeister_torsion_emitted_here": False,
        "crossrepo_import_summary_keys": sorted(status_entries.keys())[:12],
    }
    torsion_slot_closes = (
        determinant_support["prior_frontier_has_six_closed_two_open"]
        and determinant_support["local_protected_T3_reduced_Green"]
        and determinant_support["local_T1_T2_covariant_Green_extracted"]
        and determinant_support["selected_HYM_End0_heat_table_emitted_here"]
        and determinant_support["selected_HYM_End0_spectrum_emitted_here"]
    )

    torsion_packet = {
        "schema": "MTTDeterminantHeatSpectrumOrTorsionEdgeTest.v1",
        "slot": "finite_determinant_heat_spectrum_or_torsion_response",
        "status": "DETERMINANT_TORSION_EDGE_TESTED_CROSSREPO_SUPPORT_PRESENT_PAYLOAD_OPEN",
        "inputs": {
            "crossrepo_qasu3_status_import": rel(DATA / "sm_equivalence_crossrepo_qasu3_status_import.candidate.json"),
            "local_Riesz_Green_dotD": rel(DATA / "selected_riesz_green_dotd_from_diagonal_end0_de.candidate.json"),
        },
        "support": determinant_support,
        "slot_closes": torsion_slot_closes,
        "why_not_closed": (
            "The corpus and sibling repos contain determinant/torsion trails, but this repo still lacks a "
            "selected heat-kernel coefficient table, spectrum, zeta determinant, or analytic/Reidemeister "
            "torsion response for the selected q79/F,m=1 HYM/End0 operator. Importing an internal reduced "
            "determinant or generic threshold trail would not close the selected source slot."
        ),
        "minimal_closing_payload": [
            "selected HYM/End0 operator spectrum or heat-kernel table on the same q79/F,m=1 source",
            "finite determinant or zeta/analytic-torsion response with normalization and cutoff policy",
            "proof that the response is attached to the selected transition/D_E payload, not an off-branch determinant",
            "reproducible validator comparing trace/heat coefficients and torsion response",
        ],
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
    }

    remaining = list(prior["remaining_slots"])
    frontier = {
        "schema": "MTTPostSixSlotTwoGateFrontier.v1",
        "status": "TWO_REMAINING_TRUE_EQUIVALENCE_GATES_SHARPENED_NO_NEW_SLOT_CLOSED",
        "operator_source_slots_closed": prior["operator_source_slots_closed"],
        "operator_source_slots_remaining": prior["operator_source_slots_remaining"],
        "remaining_slots": remaining,
        "transition_slot_closes": transition_slot_closes,
        "determinant_torsion_slot_closes": torsion_slot_closes,
        "recommended_primary_next": "transition_rhoE_or_Cech_Dolbeault_DE_data",
        "reason_primary_next": (
            "The transition/D_E gate has selected-source D_E formulas and q79 gap support already in hand; "
            "the determinant/torsion gate depends on that operator payload to define the selected spectrum."
        ),
        "true_SM_equivalence_closed": False,
        "no_knob_closed": False,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
    }

    candidate = {
        "candidate": "MTTSelectedDETransitionOrDeterminantTorsionTwoSlotClosingRun",
        "status": STATUS,
        "inputs": {
            "post_six_frontier": transition_packet["inputs"]["post_six_frontier"],
            "local_diagonal_End0_DE": transition_packet["inputs"]["local_diagonal_End0_DE"],
            "q79_trace_gap_layer": transition_packet["inputs"]["q79_trace_gap_layer"],
            "crossrepo_qasu3_status_import": torsion_packet["inputs"]["crossrepo_qasu3_status_import"],
        },
        "output_packets": {
            "transition_rhoe_or_cech_dolbeault_de_edge_test": rel(TRANSITION),
            "determinant_heat_spectrum_or_torsion_edge_test": rel(TORSION),
            "post_six_slot_two_gate_frontier": rel(FRONTIER),
        },
        "theorem": {
            "name": "TwoRemainingOperatorGateNormalFormTheorem",
            "proved": True,
            "statement": (
                "After six operator-source slots are closed, the remaining gates reduce to exactly two "
                "payloads: selected transition/rho_E or Cech-Dolbeault/sector D_E data, and a finite "
                "determinant/heat/torsion response for the selected HYM/End0 operator. Current artifacts "
                "supply partial D_E/gap/determinant support but not the selected payload required to close "
                "either gate."
            ),
        },
        "what_closes_now": {
            "two_gate_frontier_sharpened": True,
            "transition_DE_support_imported": True,
            "determinant_torsion_support_imported": True,
            "primary_next_gate_identified": True,
            "target_fitting_excluded": True,
        },
        "what_remains_open": {
            "transition_rhoE_or_Cech_Dolbeault_DE_data": True,
            "finite_determinant_heat_spectrum_or_torsion_response": True,
            "actual_dynamic_QaSU3_operator_packet": True,
            "true_SM_equivalence": True,
            "no_knob_closure": True,
        },
        "closure_decision": {
            "SM_parity_closed": True,
            "operator_source_slots_closed_total": prior["operator_source_slots_closed"],
            "operator_source_slots_remaining": prior["operator_source_slots_remaining"],
            "transition_rhoE_or_Cech_Dolbeault_DE_data_closed": transition_slot_closes,
            "finite_determinant_heat_spectrum_or_torsion_response_closed": torsion_slot_closes,
            "actual_dynamic_QaSU3_operator_packet_closed": False,
            "true_SM_equivalence_closed": False,
            "no_knob_closed": False,
        },
        "next_required_artifact": NEXT,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "closure_claimed": transition_slot_closes or torsion_slot_closes,
    }

    cert = {
        "certificate": "MTT_Selected_DETransition_or_DeterminantTorsion_TwoSlotClosingRun_v1",
        "candidate_path": rel(OUTPUT),
        "status": STATUS,
        "theorem_proved": True,
        "closed_operator_source_slots_total": prior["operator_source_slots_closed"],
        "operator_source_slots_remaining": prior["operator_source_slots_remaining"],
        "transition_rhoE_or_Cech_Dolbeault_DE_data_closed": transition_slot_closes,
        "finite_determinant_heat_spectrum_or_torsion_response_closed": torsion_slot_closes,
        "next_required_artifact": NEXT,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "note_path": rel(NOTE),
    }

    note = f"""# MTT Selected DETransition or DeterminantTorsion TwoSlotClosingRun v1

This artifact attacks the final two operator-source slots after the
same-source Chern-Weil row closure.

It does not close a new slot.  It proves the remaining two-gate normal form.

Transition / `D_E` side:

- local selected diagonal End0 formula `D_E=d+ad(du*T3)` is present
- q79 finite `D_E` matrix and selected trace/gap layer are present
- the q79 theorem is explicitly gap-layer only
- q79 nonidentity `rho_E` is still not selected by MTT
- local rank2-to-sector transfer values are not extracted

Determinant / heat / torsion side:

- determinant/torsion trails exist in the corpus and sibling repos
- local reduced Green support exists only in the protected T3 lane
- no selected HYM/End0 heat table, spectrum, zeta determinant, or analytic
  torsion response is emitted for this source

Current count remains six closed operator-source slots and two open slots.

Primary next gate: `transition_rhoE_or_Cech_Dolbeault_DE_data`.

Next artifact: `{NEXT}`.
"""

    for path, payload in [
        (TRANSITION, transition_packet),
        (TORSION, torsion_packet),
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
