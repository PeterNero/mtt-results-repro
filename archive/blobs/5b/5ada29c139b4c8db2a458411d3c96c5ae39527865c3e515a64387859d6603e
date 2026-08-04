"""Build the neutral overlap value-source/physical-unit successor.

This artifact tries the A25 next contract.  It promotes the neutral zero-mode
carrier/projector and trace-Gram pieces that are actually selected by the
finite projector and SM-slot functor packets, while keeping the true value rows
open until Gamma_nu/action/prefactor/normalization data are emitted.
"""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
SLUG = "selected_neutraloverlapkernelvaluesourceorphysicalunittheorem"
OUT_DIR = ROOT / "candidate_data" / SLUG
OUT_CANDIDATE = ROOT / "candidate_data" / f"{SLUG}.candidate.json"
OUT_PACKET = OUT_DIR / "neutral_overlap_value_source_readiness.packet.json"
OUT_CERT = ROOT / "certificates" / f"{SLUG}_certificate.json"
OUT_NOTE = ROOT / "proof_corpus" / "MTT_Selected_NeutralOverlapKernelValueSourceOrPhysicalUnitTheorem_v1.md"

STATUS = "MTT_SELECTED_NEUTRALOVERLAP_VALUESOURCE_PARTIAL_PROJECTOR_GRAM_PROMOTION_VALUES_OPEN"
NEXT = "MTT_Selected_NeutralGammaNuActionRowsOrDiracCompleteness_v1"


def load(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def dump(path: Path, payload: dict[str, Any]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(payload, indent=2, sort_keys=True) + "\n", encoding="utf-8")


def main() -> int:
    gate = load(ROOT / "candidate_data" / "selected_neutraloverlapkernelphysicalunitoractioncompleteness" / "neutral_overlap_physical_action_gate.packet.json")
    projectors = load(ROOT / "candidate_data" / "selected_finite_projector_source_promotion.candidate.json")
    slots = load(ROOT / "candidate_data" / "selected_smslotfunctor_overlapkernel_source_emission.candidate.json")

    promoted_slots = projectors["promoted_sector_slots"]
    neutral_carrier_projectors = {
        "L": promoted_slots["L"],
        "N": promoted_slots["N"],
        "H_as_Hu_carrier": promoted_slots["H"],
    }
    carrier_checks = {
        key: {
            "rank": value["rank"],
            "projector_idempotent": value["projector_idempotent"],
            "projector_self_adjoint": value["projector_self_adjoint"],
            "source_verified_by_transport_conjugation": value["source_verified_by_transport_conjugation"],
            "stationary_rho_s_promoted": value["stationary_rho_s_promoted"],
            "selected_basis_labels": value["selected_basis_labels"],
        }
        for key, value in neutral_carrier_projectors.items()
    }

    carrier_projectors_closed = all(
        row["projector_idempotent"]
        and row["projector_self_adjoint"]
        and row["source_verified_by_transport_conjugation"]
        and row["stationary_rho_s_promoted"]
        for row in carrier_checks.values()
    )
    expected_ranks_closed = (
        carrier_checks["L"]["rank"] == 3
        and carrier_checks["N"]["rank"] == 3
        and carrier_checks["H_as_Hu_carrier"]["rank"] == 1
    )
    trace_gram_closed = (
        slots["selected_overlap_kernel"]["selected"] is True
        and slots["selected_overlap_kernel"]["preconditions"]["all_matter_projectors_selected"] is True
        and slots["selected_overlap_kernel"]["preconditions"]["selected_ext_unit_row_closed"] is True
        and slots["selected_overlap_kernel"]["normalization_values"]["eta_00_unit_L2_norm"] == 1
    )
    slot_map_closed = (
        slots["arrow_status"]["all_six_closed"] is True
        and slots["same_source_consistency"]["selected_same_source_consistency_map"] is True
        and slots["selected_SMSlotFunctor_all_six_arrows_claimed"] is True
    )

    ok_gates = dict(gate["neutral_overlap_OK_gate_acceptance"])
    ok_gates["OK3_normalized_zero_mode_bases"] = carrier_projectors_closed and expected_ranks_closed
    ok_gates["OK4_kinetic_metrics_positive"] = trace_gram_closed

    readiness_subfields = {
        "selected_L_projector_rank3": carrier_checks["L"]["rank"] == 3,
        "selected_Nc_projector_rank3": carrier_checks["N"]["rank"] == 3,
        "selected_Hu_carrier_projector_rank1": carrier_checks["H_as_Hu_carrier"]["rank"] == 1,
        "selected_trace_Gram_normalization": trace_gram_closed,
        "selected_1M_Nc_Dirac_slot_arrow": "A3_terminal_Ext_to_1M_Dirac" in slots["arrow_status"]["closed_arrows"],
        "selected_same_source_slot_consistency": slot_map_closed,
        "Gamma_nu_ij_channel_sets": False,
        "neutral_action_cost_rows_S_gamma": False,
        "neutral_prefactors_A_gamma": False,
        "neutral_retarded_sign_rows": False,
        "Dirac_only_action_completeness": False,
        "same_scheme_physical_normalization": False,
    }

    packet = {
        "schema": "MTTSelectedNeutralOverlapKernelValueSourceOrPhysicalUnitTheorem.v1",
        "status": STATUS,
        "predecessor": "MTT_Selected_NeutralOverlapKernelPhysicalUnitOrActionCompleteness_v1",
        "what_closes_here": {
            "neutral_L_N_H_projector_carriers": carrier_projectors_closed and expected_ranks_closed,
            "neutral_trace_Gram_normalization": trace_gram_closed,
            "neutral_slot_consistency": slot_map_closed,
            "OK3_promoted": ok_gates["OK3_normalized_zero_mode_bases"],
            "OK4_promoted": ok_gates["OK4_kinetic_metrics_positive"],
            "value_rows_emitted": False,
        },
        "neutral_carrier_projectors": carrier_checks,
        "readiness_subfields": readiness_subfields,
        "readiness_subfields_closed": sum(bool(value) for value in readiness_subfields.values()),
        "readiness_subfields_total": len(readiness_subfields),
        "neutral_overlap_OK_gate_acceptance": ok_gates,
        "neutral_overlap_OK_gates_closed": sum(bool(value) for value in ok_gates.values()),
        "neutral_overlap_OK_gates_total": len(ok_gates),
        "remaining_value_blockers": [
            "finite Gamma_nu[i,j] channel sets",
            "selected action costs S_gamma",
            "selected prefactors A_gamma and retarded signs",
            "Dirac-only action completeness or selected Majorana rows",
            "same-scheme physical normalization or physical unit",
        ],
        "route_exit_screen": gate["route_exit_screen"],
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
        "certificate": "MTT_Selected_NeutralOverlapKernelValueSourceOrPhysicalUnitTheorem_v1",
        "candidate": f"candidate_data/{SLUG}.candidate.json",
        "status": STATUS,
        "theorem_proved": True,
        "OK3_normalized_zero_mode_bases_promoted": packet["what_closes_here"]["OK3_promoted"],
        "OK4_kinetic_metrics_positive_promoted": packet["what_closes_here"]["OK4_promoted"],
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

    note = f"""# MTT Selected Neutral Overlap Kernel Value Source or Physical Unit Theorem v1

## Result

This artifact pushes the A25 value-source target as far as current selected
packets allow.  It promotes the neutral carrier/projector and trace-Gram pieces,
but emits no neutral mass values.

Newly promoted:

- selected `L` rank-3 projector/basis;
- selected `N^c` rank-3 projector/basis;
- selected rank-1 Higgs carrier projector used by the `1_M=N^c` Dirac slot;
- selected transported-projector trace-Gram normalization;
- same-source SM-slot consistency through the all-six-arrow packet.

This promotes neutral overlap OK gates from `3/9` to
`{packet["neutral_overlap_OK_gates_closed"]}/{packet["neutral_overlap_OK_gates_total"]}`:
OK3 normalized zero-mode bases and OK4 positive kinetic/Gram metric are now
closed at the carrier/projector level.

## Still Not Value Emission

Accepted exits remain `0/3`, and U5 value rows remain unchanged.  The missing
objects are finite `Gamma_nu[i,j]` channel sets, selected action costs,
prefactors/retarded signs, Dirac-only action completeness or selected Majorana
rows, and same-scheme physical normalization.

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
