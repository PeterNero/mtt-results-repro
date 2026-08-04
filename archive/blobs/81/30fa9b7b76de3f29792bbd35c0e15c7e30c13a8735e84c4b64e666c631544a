"""Build the selected finite neutral Gamma channel-row successor."""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
SLUG = "selected_neutralfinitegammarowsoractioncostsource"
OUT_DIR = ROOT / "candidate_data" / SLUG
OUT_PACKET = OUT_DIR / "neutral_finite_gamma_channel_rows.packet.json"
OUT_CANDIDATE = ROOT / "candidate_data" / f"{SLUG}.candidate.json"
OUT_CERT = ROOT / "certificates" / f"{SLUG}_certificate.json"
OUT_NOTE = ROOT / "proof_corpus" / "MTT_Selected_NeutralFiniteGammaRowsOrActionCostSource_v1.md"

STATUS = "MTT_SELECTED_NEUTRAL_FINITE_GAMMA_CHANNEL_ROWS_CLOSED_ACTION_WEIGHTS_OPEN"
NEXT = "MTT_Selected_NeutralActionCostPrefactorOrDiracMajoranaCompletion_v1"


def load(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def dump(path: Path, payload: dict[str, Any]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(payload, indent=2, sort_keys=True) + "\n", encoding="utf-8")


def matmul(a: list[list[float]], b: list[list[float]]) -> list[list[float]]:
    return [[sum(a[i][k] * b[k][j] for k in range(3)) for j in range(3)] for i in range(3)]


def main() -> int:
    predecessor = load(
        ROOT
        / "candidate_data"
        / "selected_neutralgammanuactionrowsordiraccompleteness"
        / "neutral_gamma_nu_structural_channel.packet.json"
    )
    dynamic = load(
        ROOT
        / "candidate_data"
        / "selected_samesourcedynamicmatteroverlapoperatorpacket_or_primitivec1valueclosure"
        / "selected_non_scalar_dynamic_overlap_values.packet.json"
    )
    promotion = load(
        ROOT
        / "candidate_data"
        / "selected_samesourcedynamicmatteroverlapoperatorpacket_or_primitivec1valueclosure"
        / "dynamic_transfer_backpromotion_theorem.packet.json"
    )

    identity = [[1.0, 0.0, 0.0], [0.0, 1.0, 0.0], [0.0, 0.0, 1.0]]
    shift = [[0.0, 1.0, 0.0], [0.0, 0.0, 1.0], [1.0, 0.0, 0.0]]
    i_plus_x = [[identity[i][j] + shift[i][j] for j in range(3)] for i in range(3)]
    emitted = dynamic["dynamic_transfer_tensor"]["sector_response_columns"]["shift_packet"]["matrices"]["nuD"]

    source_gate = all(
        [
            predecessor["what_closes_here"]["selected_typed_L_Nc_Hu_trilinear_channel_skeleton"],
            dynamic["selected_by_MTT"],
            dynamic["closure_claimed"],
            promotion["backpromotion_allowed"],
            promotion["new_prerequisites_after_source_and_postsource_replay"]["selected_source_to_C1_transfer_map_emitted"],
            promotion["new_prerequisites_after_source_and_postsource_replay"]["selected_sector_routing_dynamic_map_emitted"],
            promotion["new_prerequisites_after_source_and_postsource_replay"]["selected_Hessian_blocks_emitted"],
            promotion["new_prerequisites_after_source_and_postsource_replay"]["selected_b_selected_emitted"],
            emitted == i_plus_x,
            matmul(matmul(shift, shift), shift) == identity,
        ]
    )

    rows = []
    for i in range(3):
        for j in range(3):
            channels = []
            if identity[i][j] == 1.0:
                channels.append("identity_I3")
            if shift[i][j] == 1.0:
                channels.append("active_circle_shift_X3")
            rows.append(
                {
                    "cell": f"Gamma_nu[{i},{j}]",
                    "finite_channel_set": channels,
                    "channel_multiplicity": emitted[i][j],
                    "active_channel": bool(channels),
                    "selected_emitted": source_gate,
                    "theorem_derived": source_gate,
                    "finite_exactness": "X3^3=I3 and exact finite matrix equality",
                    "source_operator": "Gamma_nu^chan=I3+X3",
                    "source_packet": "selected same-source dynamic matter overlap first response",
                    "physical_amplitude_emitted": False,
                    "action_cost_S_gamma_emitted": False,
                    "prefactor_A_gamma_emitted": False,
                    "retarded_sign_emitted": False,
                }
            )

    readiness = dict(predecessor["readiness_subfields"])
    readiness["Gamma_nu_ij_channel_sets"] = source_gate
    ok_gates = dict(predecessor["neutral_overlap_OK_gate_acceptance"])
    ok_gates["OK5_finite_neutral_overlap_channel_sets"] = source_gate

    packet = {
        "schema": "MTTSelectedNeutralFiniteGammaRowsOrActionCostSource.v1",
        "status": STATUS,
        "predecessor": "MTT_Selected_NeutralGammaNuActionRowsOrDiracCompleteness_v1",
        "theorem": {
            "name": "SelectedNeutralFiniteGammaChannelSetTheorem",
            "proved": source_gate,
            "statement": "On the selected q79/F,m=1 finite qutrit-Weyl branch, the selected Dirac-neutral first-response channel operator is Gamma_nu^chan=I3+X3, where X3 is the order-three active circle shift. It emits all nine finite channel rows, with six active multiplicity-one cells and three exact zero cells, before any physical action weight or observed neutrino datum is supplied.",
        },
        "source_provenance": {
            "typed_L_Nc_Hu_carrier_closed": predecessor["what_closes_here"]["selected_typed_L_Nc_Hu_trilinear_channel_skeleton"],
            "dynamic_packet_selected_by_MTT": dynamic["selected_by_MTT"],
            "same_source_backpromotion_theorem": promotion["backpromotion_allowed"],
            "source_to_C1_transfer_emitted": promotion["new_prerequisites_after_source_and_postsource_replay"]["selected_source_to_C1_transfer_map_emitted"],
            "dynamic_sector_routing_emitted": promotion["new_prerequisites_after_source_and_postsource_replay"]["selected_sector_routing_dynamic_map_emitted"],
            "same_source_Hessian_and_b_selected_emitted": (
                promotion["new_prerequisites_after_source_and_postsource_replay"]["selected_Hessian_blocks_emitted"]
                and promotion["new_prerequisites_after_source_and_postsource_replay"]["selected_b_selected_emitted"]
            ),
            "observed_data_used_as_selector": False,
            "target_fitting_used": False,
        },
        "finite_operator": {
            "I3": identity,
            "X3": shift,
            "Gamma_nu_channel_matrix_I3_plus_X3": emitted,
            "X3_cubed_equals_I3": matmul(matmul(shift, shift), shift) == identity,
            "exact_selected_packet_match": emitted == i_plus_x,
            "operator_rank": 3,
            "determinant": 2.0,
            "active_cell_count": sum(row["active_channel"] for row in rows),
            "zero_cell_count": sum(not row["active_channel"] for row in rows),
        },
        "Gamma_nu_finite_channel_rows": rows,
        "finite_Gamma_nu_row_count": len(rows),
        "finite_Gamma_nu_rows_selected": sum(row["selected_emitted"] for row in rows),
        "what_closes_here": {
            "finite_Gamma_nu_ij_channel_sets": source_gate,
            "nine_dimensionless_channel_multiplicity_rows": source_gate and len(rows) == 9,
            "finite_channel_exactness": source_gate,
            "neutral_action_cost_rows_S_gamma": False,
            "neutral_prefactors_A_gamma": False,
            "neutral_retarded_sign_rows": False,
            "physical_Gamma_nu_amplitudes": False,
            "Dirac_only_action_completeness": False,
        },
        "readiness_subfields": readiness,
        "readiness_subfields_closed": sum(bool(value) for value in readiness.values()),
        "readiness_subfields_total": len(readiness),
        "neutral_overlap_OK_gate_acceptance": ok_gates,
        "neutral_overlap_OK_gates_closed": sum(bool(value) for value in ok_gates.values()),
        "neutral_overlap_OK_gates_total": len(ok_gates),
        "new_dimensionless_channel_rows_closed_here": 9,
        "new_absolute_value_fields_closed_here": 0,
        "accepted_route_exit_count": 0,
        "route_exit_count": 3,
        "dimensionful_M_D_3x3_closed": False,
        "dimensionful_M_L_3x3_closed": False,
        "dimensionful_M_R_3x3_closed": False,
        "absolute_normalization_and_scheme_closed": False,
        "selected_neutral_operator_accepted": False,
        "U5_closed": False,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "remaining_value_blockers": [
            "selected action costs S_gamma and prefactors A_gamma that turn channel multiplicities into overlap amplitudes",
            "selected retarded sign/character weight for the neutral channel",
            "Dirac-only action-completeness theorem or selected Majorana M_L/M_R rows",
            "same-scheme physical unit and absolute normalization",
        ],
        "next_required_artifact": NEXT,
    }

    cert = {
        "certificate": "MTT_Selected_NeutralFiniteGammaRowsOrActionCostSource_v1",
        "candidate": f"candidate_data/{SLUG}.candidate.json",
        "status": STATUS,
        "theorem_proved": source_gate,
        "finite_Gamma_nu_ij_channel_sets_closed": source_gate,
        "finite_Gamma_nu_rows_selected": packet["finite_Gamma_nu_rows_selected"],
        "active_channel_count": packet["finite_operator"]["active_cell_count"],
        "exact_zero_channel_count": packet["finite_operator"]["zero_cell_count"],
        "channel_operator": "I3+X3",
        "X3_cubed_equals_I3": packet["finite_operator"]["X3_cubed_equals_I3"],
        "neutral_action_cost_rows_S_gamma_closed": False,
        "neutral_prefactors_A_gamma_closed": False,
        "neutral_retarded_sign_rows_closed": False,
        "physical_Gamma_nu_amplitudes_closed": False,
        "Dirac_only_action_completeness_closed": False,
        "neutral_overlap_OK_gates_closed": packet["neutral_overlap_OK_gates_closed"],
        "neutral_overlap_OK_gates_total": packet["neutral_overlap_OK_gates_total"],
        "readiness_subfields_closed": packet["readiness_subfields_closed"],
        "readiness_subfields_total": packet["readiness_subfields_total"],
        "new_dimensionless_channel_rows_closed_here": 9,
        "new_absolute_value_fields_closed_here": 0,
        "accepted_route_exit_count": 0,
        "route_exit_count": 3,
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

    note = f"""# MTT Selected Neutral Finite Gamma Rows or Action Cost Source v1

## Result

The selected same-source dynamic matter theorem supplies the finite neutral
first-response channel operator

```text
Gamma_nu^chan = I3 + X3
               [1 1 0]
             = [0 1 1]
               [1 0 1],       X3^3 = I3.
```

Together with the already selected `L_i x N^c_j x H_u` carrier, this emits all
nine finite `Gamma_nu[i,j]` channel rows. Six cells contain one selected finite
channel and three cells are exact zeros. These are channel multiplicities, not
measured neutrino Yukawa couplings or masses. No observed neutrino value is
used as a selector.

This closes OK5. Neutral overlap gates advance to
`{packet['neutral_overlap_OK_gates_closed']}/{packet['neutral_overlap_OK_gates_total']}`
and readiness advances to
`{packet['readiness_subfields_closed']}/{packet['readiness_subfields_total']}`.

## Boundary

The physical amplitude still has the schematic form
`A_gamma * exp(-S_gamma) * sign_ret * Gamma_nu^chan`. The selected action costs,
prefactors, retarded signs/character weights, physical unit, and absolute
normalization are not emitted here. Nor does this theorem exclude the lawful
Majorana self-characters `0` and `672`. Therefore no dimensionful `M_D`, `M_L`,
or `M_R` matrix is claimed and U5 remains partial.

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
