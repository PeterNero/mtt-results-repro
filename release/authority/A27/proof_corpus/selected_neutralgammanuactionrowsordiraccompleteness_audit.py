from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SLUG = "selected_neutralgammanuactionrowsordiraccompleteness"
BUILDER = ROOT / "scripts" / f"build_{SLUG}.py"
PACKET = ROOT / "candidate_data" / SLUG / "neutral_gamma_nu_structural_channel.packet.json"
CANDIDATE = ROOT / "candidate_data" / f"{SLUG}.candidate.json"
CERT = ROOT / "certificates" / f"{SLUG}_certificate.json"
NOTE = ROOT / "proof_corpus" / "MTT_Selected_NeutralGammaNuActionRowsOrDiracCompleteness_v1.md"

STATUS = "MTT_SELECTED_NEUTRAL_GAMMANU_TYPED_CHANNEL_SKELETON_CLOSED_ACTION_ROWS_OPEN"
NEXT = "MTT_Selected_NeutralFiniteGammaRowsOrActionCostSource_v1"


def load(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def require(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)


def main() -> int:
    subprocess.run([sys.executable, str(BUILDER)], cwd=ROOT, check=True)
    packet = load(PACKET)
    candidate = load(CANDIDATE)
    cert = load(CERT)
    note = NOTE.read_text(encoding="utf-8")

    require(packet == candidate, "candidate/packet mismatch")
    require(packet["status"] == STATUS, "packet status changed")
    require(cert["status"] == STATUS, "certificate status changed")
    require(packet["next_required_artifact"] == NEXT, "next artifact changed")
    require(cert["next_required_artifact"] == NEXT, "cert next changed")
    require(packet["observed_data_used_as_selector"] is False, "observed selector used")
    require(packet["target_fitting_used"] is False, "target fitting used")

    closes = packet["what_closes_here"]
    require(closes["selected_typed_L_Nc_Hu_trilinear_channel_skeleton"] is True, "typed neutral channel not closed")
    require(closes["nine_Gamma_nu_matrix_slots_typed"] is True, "nine typed cells not closed")
    require(closes["same_source_Dirac_slot_and_projector_composition"] is True, "same-source composition not closed")
    for key in [
        "finite_Gamma_nu_ij_channel_sets",
        "neutral_action_cost_rows_S_gamma",
        "neutral_prefactors_A_gamma",
        "neutral_retarded_sign_rows",
        "Dirac_only_action_completeness",
        "value_rows_emitted",
    ]:
        require(closes[key] is False, f"overclosed: {key}")

    inputs = packet["proof_inputs"]
    require(inputs["selected_L_projector_rank"] == 3, "L rank changed")
    require(inputs["selected_Nc_projector_rank"] == 3, "N rank changed")
    require(inputs["selected_Hu_carrier_rank"] == 1, "H rank changed")
    require(inputs["A3_terminal_Ext_to_1M_Dirac_closed"] is True, "A3 Dirac arrow not closed")
    require(inputs["all_six_SMslot_arrows_closed"] is True, "SM slot arrows not closed")
    require(inputs["selected_same_source_consistency_map"] is True, "same source missing")
    require(inputs["selected_1M_equals_Nc_Dirac_channel"] is True, "Dirac channel missing")
    require(inputs["selected_trace_Gram_normalization"] is True, "trace Gram missing")

    cells = packet["Gamma_nu_typed_structural_cells"]
    require(packet["typed_cell_count"] == 9, "typed cell count changed")
    require(cert["typed_Gamma_nu_cell_count"] == 9, "cert typed cell count changed")
    require(len(cells) == 9, "cell list count changed")
    require({cell["cell"] for cell in cells} == {f"Gamma_nu[{i},{j}]" for i in range(3) for j in range(3)}, "cell IDs changed")
    for cell in cells:
        require(cell["selected_structural_slot"] is True, f"structural slot false: {cell['cell']}")
        require(cell["typed_operator"] == "bar5_M(L) x 1_M(N^c) x 5_H(H_u)", f"operator type changed: {cell['cell']}")
        for key in [
            "finite_channel_set_emitted",
            "action_cost_emitted",
            "prefactor_emitted",
            "retarded_sign_emitted",
            "value_row_emitted",
        ]:
            require(cell[key] is False, f"cell overemitted {key}: {cell['cell']}")

    sub = packet["readiness_subfields"]
    require(packet["readiness_subfields_closed"] == 7, "readiness count changed")
    require(packet["readiness_subfields_total"] == 13, "readiness total changed")
    require(sub["selected_neutral_trilinear_L_Nc_Hu_slot_skeleton"] is True, "new skeleton subfield not closed")
    require(sub["Gamma_nu_ij_channel_sets"] is False, "finite Gamma_nu rows overclosed")
    require(sub["neutral_action_cost_rows_S_gamma"] is False, "action rows overclosed")
    require(sub["neutral_prefactors_A_gamma"] is False, "prefactors overclosed")
    require(sub["neutral_retarded_sign_rows"] is False, "retarded signs overclosed")
    require(sub["Dirac_only_action_completeness"] is False, "Dirac-only completeness overclosed")
    require(sub["same_scheme_physical_normalization"] is False, "physical normalization overclosed")

    ok = packet["neutral_overlap_OK_gate_acceptance"]
    require(packet["neutral_overlap_OK_gates_closed"] == 5, "OK count changed")
    require(packet["neutral_overlap_OK_gates_total"] == 9, "OK total changed")
    require(ok["OK5_finite_neutral_overlap_channel_sets"] is False, "OK5 overclosed")
    require(ok["OK6_action_costs_prefactors_characters_retarded_signs"] is False, "OK6 overclosed")

    dirac = packet["Dirac_only_completeness_analysis"]
    require(dirac["selected_Dirac_channel_exists"] is True, "Dirac channel missing in analysis")
    require(dirac["Majorana_admissible_characters_Z1344"] == [0, 672], "Majorana character set changed")
    require(dirac["separate_Majorana_operator_excluded"] is False, "Majorana overexcluded")
    require(dirac["Dirac_only_action_completeness_closed"] is False, "Dirac-only overclosed")

    require(packet["accepted_route_exit_count"] == 0, "route overaccepted")
    require(packet["new_value_fields_closed_here"] == 0, "value fields overclosed")
    for field in [
        "dimensionful_M_D_3x3_closed",
        "dimensionful_M_L_3x3_closed",
        "dimensionful_M_R_3x3_closed",
        "absolute_normalization_and_scheme_closed",
        "selected_neutral_operator_accepted",
        "U5_closed",
    ]:
        require(packet[field] is False, f"packet overclosed: {field}")
        require(cert[field] is False, f"cert overclosed: {field}")

    for field in [
        "finite_Gamma_nu_ij_channel_sets_closed",
        "neutral_action_cost_rows_S_gamma_closed",
        "neutral_prefactors_A_gamma_closed",
        "neutral_retarded_sign_rows_closed",
        "Dirac_only_action_completeness_closed",
    ]:
        require(cert[field] is False, f"cert overclosed: {field}")

    for phrase in [
        "Gamma_nu structural slot",
        "`7/13`",
        "OK5 stays false",
        "Majorana self-characters `0` and `672` remain admissible",
        NEXT,
    ]:
        require(phrase in note, f"note missing phrase: {phrase}")

    print(json.dumps({
        "neutral_OK_gates": "5/9",
        "readiness": "7/13",
        "typed_Gamma_nu_cells": 9,
        "accepted_routes": 0,
        "new_value_fields_closed": 0,
        "next": NEXT,
    }, indent=2))
    print("selected neutral Gamma_nu action rows / Dirac completeness audit passed")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
