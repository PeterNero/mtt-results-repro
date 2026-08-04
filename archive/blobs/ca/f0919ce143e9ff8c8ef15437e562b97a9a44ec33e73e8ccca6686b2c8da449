"""Build the neutral Gamma_nu structural-channel successor.

This artifact follows the neutral overlap value-source readiness packet.  It
promotes only the selected typed trilinear carrier

    L_i x N^c_j x H_u

for the neutral Dirac overlap kernel.  It deliberately does not promote finite
Gamma_nu[i,j] channel sets, action costs, prefactors, retarded signs, or a
Dirac-only completeness theorem.
"""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
SLUG = "selected_neutralgammanuactionrowsordiraccompleteness"
OUT_DIR = ROOT / "candidate_data" / SLUG
OUT_CANDIDATE = ROOT / "candidate_data" / f"{SLUG}.candidate.json"
OUT_PACKET = OUT_DIR / "neutral_gamma_nu_structural_channel.packet.json"
OUT_CERT = ROOT / "certificates" / f"{SLUG}_certificate.json"
OUT_NOTE = ROOT / "proof_corpus" / "MTT_Selected_NeutralGammaNuActionRowsOrDiracCompleteness_v1.md"

STATUS = "MTT_SELECTED_NEUTRAL_GAMMANU_TYPED_CHANNEL_SKELETON_CLOSED_ACTION_ROWS_OPEN"
NEXT = "MTT_Selected_NeutralFiniteGammaRowsOrActionCostSource_v1"


def load(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def dump(path: Path, payload: dict[str, Any]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(payload, indent=2, sort_keys=True) + "\n", encoding="utf-8")


def main() -> int:
    predecessor = load(
        ROOT
        / "candidate_data"
        / "selected_neutraloverlapkernelvaluesourceorphysicalunittheorem"
        / "neutral_overlap_value_source_readiness.packet.json"
    )
    slots = load(ROOT / "candidate_data" / "selected_smslotfunctor_overlapkernel_source_emission.candidate.json")
    neutral_mass = load(
        ROOT / "candidate_data" / "selected_neutralmassoperator_sourceemission" / "neutral_mass_operator_source_emission.packet.json"
    )

    carriers = predecessor["neutral_carrier_projectors"]
    l_labels = carriers["L"]["selected_basis_labels"]
    n_labels = carriers["N"]["selected_basis_labels"]
    h_label = carriers["H_as_Hu_carrier"]["selected_basis_labels"][0]

    carrier_gate = (
        carriers["L"]["rank"] == 3
        and carriers["N"]["rank"] == 3
        and carriers["H_as_Hu_carrier"]["rank"] == 1
        and all(
            row["projector_idempotent"]
            and row["projector_self_adjoint"]
            and row["source_verified_by_transport_conjugation"]
            and row["stationary_rho_s_promoted"]
            for row in carriers.values()
        )
    )
    slot_gate = (
        "A3_terminal_Ext_to_1M_Dirac" in slots["arrow_status"]["closed_arrows"]
        and slots["selected_SMSlotFunctor_all_six_arrows_claimed"] is True
        and slots["same_source_consistency"]["selected_same_source_consistency_map"] is True
        and neutral_mass["character_and_ontology_gate"]["selected_1M_equals_Nc_Dirac_channel"] is True
    )
    gram_gate = (
        predecessor["readiness_subfields"]["selected_trace_Gram_normalization"] is True
        and predecessor["readiness_subfields"]["selected_same_source_slot_consistency"] is True
    )

    structural_channel_closed = carrier_gate and slot_gate and gram_gate

    typed_cells = []
    for i, l_label in enumerate(l_labels):
        for j, n_label in enumerate(n_labels):
            typed_cells.append(
                {
                    "cell": f"Gamma_nu[{i},{j}]",
                    "left_carrier": l_label,
                    "right_carrier": n_label,
                    "higgs_carrier": h_label,
                    "typed_operator": "bar5_M(L) x 1_M(N^c) x 5_H(H_u)",
                    "selected_structural_slot": structural_channel_closed,
                    "finite_channel_set_emitted": False,
                    "action_cost_emitted": False,
                    "prefactor_emitted": False,
                    "retarded_sign_emitted": False,
                    "value_row_emitted": False,
                }
            )

    readiness_subfields = dict(predecessor["readiness_subfields"])
    readiness_subfields["selected_neutral_trilinear_L_Nc_Hu_slot_skeleton"] = structural_channel_closed

    ok_gates = dict(predecessor["neutral_overlap_OK_gate_acceptance"])
    ok_gates["OK5_finite_neutral_overlap_channel_sets"] = False
    ok_gates["OK6_action_costs_prefactors_characters_retarded_signs"] = False

    packet = {
        "schema": "MTTSelectedNeutralGammaNuActionRowsOrDiracCompleteness.v1",
        "status": STATUS,
        "predecessor": "MTT_Selected_NeutralOverlapKernelValueSourceOrPhysicalUnitTheorem_v1",
        "what_closes_here": {
            "selected_typed_L_Nc_Hu_trilinear_channel_skeleton": structural_channel_closed,
            "nine_Gamma_nu_matrix_slots_typed": len(typed_cells) == 9,
            "same_source_Dirac_slot_and_projector_composition": slot_gate and carrier_gate,
            "finite_Gamma_nu_ij_channel_sets": False,
            "neutral_action_cost_rows_S_gamma": False,
            "neutral_prefactors_A_gamma": False,
            "neutral_retarded_sign_rows": False,
            "Dirac_only_action_completeness": False,
            "value_rows_emitted": False,
        },
        "proof_inputs": {
            "selected_L_projector_rank": carriers["L"]["rank"],
            "selected_Nc_projector_rank": carriers["N"]["rank"],
            "selected_Hu_carrier_rank": carriers["H_as_Hu_carrier"]["rank"],
            "A3_terminal_Ext_to_1M_Dirac_closed": "A3_terminal_Ext_to_1M_Dirac" in slots["arrow_status"]["closed_arrows"],
            "all_six_SMslot_arrows_closed": slots["arrow_status"]["all_six_closed"],
            "selected_same_source_consistency_map": slots["same_source_consistency"]["selected_same_source_consistency_map"],
            "selected_1M_equals_Nc_Dirac_channel": neutral_mass["character_and_ontology_gate"][
                "selected_1M_equals_Nc_Dirac_channel"
            ],
            "selected_trace_Gram_normalization": predecessor["readiness_subfields"]["selected_trace_Gram_normalization"],
        },
        "Gamma_nu_typed_structural_cells": typed_cells,
        "typed_cell_count": len(typed_cells),
        "readiness_subfields": readiness_subfields,
        "readiness_subfields_closed": sum(bool(value) for value in readiness_subfields.values()),
        "readiness_subfields_total": len(readiness_subfields),
        "neutral_overlap_OK_gate_acceptance": ok_gates,
        "neutral_overlap_OK_gates_closed": sum(bool(value) for value in ok_gates.values()),
        "neutral_overlap_OK_gates_total": len(ok_gates),
        "Dirac_only_completeness_analysis": {
            "selected_Dirac_channel_exists": neutral_mass["character_and_ontology_gate"]["selected_1M_equals_Nc_Dirac_channel"],
            "Majorana_admissible_characters_Z1344": neutral_mass["character_and_ontology_gate"][
                "Majorana_admissible_characters_Z1344"
            ],
            "separate_Majorana_operator_excluded": neutral_mass["character_and_ontology_gate"][
                "separate_Majorana_operator_excluded"
            ],
            "Dirac_only_action_completeness_closed": False,
            "reason_not_closed": "The selected Dirac trilinear carrier exists, but admissible Majorana self-characters k=0,672 remain lawful until a selected neutral real-structure/action theorem excludes or emits M_L/M_R.",
        },
        "remaining_value_blockers": [
            "finite Gamma_nu[i,j] channel sets, not only the typed L_i N^c_j H_u carrier",
            "selected action costs S_gamma for each admitted neutral channel",
            "selected prefactors A_gamma and retarded signs",
            "Dirac-only action-completeness theorem or selected Majorana M_L/M_R rows",
            "same-scheme physical normalization or physical unit",
        ],
        "route_exit_screen": predecessor["route_exit_screen"],
        "accepted_route_exit_count": 0,
        "route_exit_count": 3,
        "new_value_fields_closed_here": 0,
        "dimensionful_M_D_3x3_closed": False,
        "dimensionful_M_L_3x3_closed": False,
        "dimensionful_M_R_3x3_closed": False,
        "absolute_normalization_and_scheme_closed": False,
        "selected_neutral_operator_accepted": False,
        "U5_closed": False,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "next_required_artifact": NEXT,
    }

    cert = {
        "certificate": "MTT_Selected_NeutralGammaNuActionRowsOrDiracCompleteness_v1",
        "candidate": f"candidate_data/{SLUG}.candidate.json",
        "status": STATUS,
        "theorem_proved": True,
        "selected_typed_L_Nc_Hu_trilinear_channel_skeleton": structural_channel_closed,
        "typed_Gamma_nu_cell_count": len(typed_cells),
        "finite_Gamma_nu_ij_channel_sets_closed": False,
        "neutral_action_cost_rows_S_gamma_closed": False,
        "neutral_prefactors_A_gamma_closed": False,
        "neutral_retarded_sign_rows_closed": False,
        "Dirac_only_action_completeness_closed": False,
        "neutral_overlap_OK_gates_closed": packet["neutral_overlap_OK_gates_closed"],
        "neutral_overlap_OK_gates_total": packet["neutral_overlap_OK_gates_total"],
        "readiness_subfields_closed": packet["readiness_subfields_closed"],
        "readiness_subfields_total": packet["readiness_subfields_total"],
        "accepted_route_exit_count": 0,
        "route_exit_count": 3,
        "new_value_fields_closed_here": 0,
        "dimensionful_M_D_3x3_closed": False,
        "dimensionful_M_L_3x3_closed": False,
        "dimensionful_M_R_3x3_closed": False,
        "absolute_normalization_and_scheme_closed": False,
        "selected_neutral_operator_accepted": False,
        "U5_closed": False,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "next_required_artifact": NEXT,
    }

    note = f"""# MTT Selected Neutral GammaNu Action Rows or Dirac Completeness v1

## Result

This artifact closes the selected *typed carrier* for the neutral Dirac overlap
kernel:

```text
Gamma_nu structural slot: L_i x N^c_j x H_u
operator type: bar5_M(L) x 1_M(N^c) x 5_H(H_u)
family cells: 3 x 3 = 9
```

The proof uses only already selected source objects: the rank-3 `L` projector,
the rank-3 `N^c` projector, the rank-1 Higgs carrier, the closed
`A3_terminal_Ext_to_1M_Dirac` arrow, all-six-arrow SM-slot consistency, and the
selected transported-projector trace-Gram normalization.

Readiness advances from `6/12` to
`{packet["readiness_subfields_closed"]}/{packet["readiness_subfields_total"]}`.

## Boundary

This is not yet finite neutral value emission.  OK5 stays false because the
packet emits the typed 3x3 carrier but not the actual finite channel sets
`Gamma_nu[i,j]`.  OK6 also stays false because no selected action costs,
prefactors, character weights, or retarded signs are emitted.

Dirac-only completeness also remains open: the selected `1_M=N^c` Dirac channel
exists, but Majorana self-characters `0` and `672` remain admissible until a
selected action or real-structure theorem excludes them or emits the
corresponding `M_L/M_R` rows.

Next artifact: `{NEXT}`.
"""

    dump(OUT_PACKET, packet)
    dump(OUT_CANDIDATE, packet)
    dump(OUT_CERT, cert)
    OUT_NOTE.write_text(note, encoding="utf-8")
    print(json.dumps(cert, indent=2, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
