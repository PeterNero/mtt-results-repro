"""Audit final DynamicC1 source-owner value gate."""

from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SLUG = "selected_dynamicc1_sourceowner_dynamictransferhessian_or_honestgalerkinvalues"
DATA = ROOT / "candidate_data" / f"{SLUG}.candidate.json"
PACKET_DIR = ROOT / "candidate_data" / SLUG
READY_TABLE = PACKET_DIR / "ready_to_promote_dynamic_value_table.packet.json"
LANE_A = PACKET_DIR / "lane_a_residual_projector_source_rule_attempt.packet.json"
LANE_B = PACKET_DIR / "lane_b_honest_galerkin_export_attempt.packet.json"
FINAL_GATE = PACKET_DIR / "final_dynamic_value_gate.packet.json"
CERT = ROOT / "certificates" / f"{SLUG}_certificate.json"
NOTE = ROOT / "proof_corpus" / "MTT_Selected_DynamicC1_SourceOwner_DynamicTransferHessian_or_HonestGalerkinValues_v1.md"
BUILDER = ROOT / "scripts" / f"build_{SLUG}.py"

STATUS = "MTT_SELECTED_DYNAMICC1_SOURCEOWNER_DYNAMICVALUE_GATE_BUILT_VALUES_READY_SOURCE_RULE_OPEN"
NEXT = "MTT_Selected_DifferentiatedPhiFinC1_SourceRule_or_HonestGalerkinC1Table_Proof_v1"


def load(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def require(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)


def main() -> int:
    subprocess.run([sys.executable, str(BUILDER)], cwd=ROOT, check=True)

    data = load(DATA)
    ready = load(READY_TABLE)
    lane_a = load(LANE_A)
    lane_b = load(LANE_B)
    gate = load(FINAL_GATE)
    cert = load(CERT)
    note = NOTE.read_text(encoding="utf-8")

    require(data["status"] == STATUS, "candidate status mismatch")
    require(cert["status"] == STATUS, "certificate status mismatch")
    require(data["next_required_artifact"] == NEXT, "next artifact mismatch")
    require(cert["next_required_artifact"] == NEXT, "certificate next artifact mismatch")
    require(data["theorem"]["proved"] is True, "theorem flag missing")

    phase = ready["dynamic_operator_candidates"]["phase_R_Z"]
    shift = ready["dynamic_operator_candidates"]["shift_R_X"]
    require(phase["residual_norm_sq"] == 4.0, "phase residual norm mismatch")
    require(shift["residual_norm_sq"] == 2.0, "shift residual norm mismatch")
    require(phase["target_norm_sq"] == 6.0, "phase target norm mismatch")
    require(shift["target_norm_sq"] == 6.0, "shift target norm mismatch")
    require(phase["orthogonal_to_fixed_fiber_span"] is True, "phase orthogonality missing")
    require(shift["orthogonal_to_fixed_fiber_span"] is True, "shift orthogonality missing")
    require(phase["selected_now"] is False, "phase selected too early")
    require(shift["selected_now"] is False, "shift selected too early")

    hessian = ready["conditional_hessian_values"]
    require(hessian["A_transpose_A"] == [[12.0, 0.0], [0.0, 12.0]], "A^T A mismatch")
    require(hessian["A_transpose_b"] == [12.0, 12.0], "A^T b mismatch")
    require(hessian["deltaTheta_C1"] == [1.0, 1.0], "delta mismatch")
    require(hessian["rank"] == 2, "rank mismatch")
    for key, value in ready["promotion_status"].items():
        require(value is False, f"{key} promoted too early")

    require(lane_a["passes_now"] is False, "Lane A passed unexpectedly")
    require(lane_a["required_source_rule"]["would_select_phase_R_Z"] is True, "Lane A phase consequence missing")
    require(lane_a["required_source_rule"]["would_select_shift_R_X"] is True, "Lane A shift consequence missing")
    require(lane_a["required_source_rule"]["would_emit_b_selected"] is True, "Lane A b consequence missing")
    require(lane_a["required_source_rule"]["would_emit_sector_response_matrices"] is True, "Lane A sector consequence missing")
    require(len(lane_a["why_not_proved_now"]) >= 4, "Lane A blockers not recorded")

    require(lane_b["passes_now"] is False, "Lane B passed unexpectedly")
    require(lane_b["selected_source_verified"] is False, "Lane B source verified too early")
    require(lane_b["strict_coordinate_target"]["total_real_coordinates"] == 72, "Lane B coordinate mismatch")
    require(len(lane_b["missing_outputs"]) == 4, "Lane B missing outputs mismatch")

    require(gate["status"] == "FINAL_DYNAMIC_VALUE_GATE_SHARP_VALUES_READY_PROOF_OPEN", "gate status mismatch")
    require(gate["exact_values_ready"]["phase_R_Z_matrix_emitted_as_candidate"] is True, "phase table missing")
    require(gate["exact_values_ready"]["shift_R_X_matrix_emitted_as_candidate"] is True, "shift table missing")
    require(gate["exact_values_ready"]["A_transpose_b"] == [12.0, 12.0], "gate b mismatch")
    require(gate["legal_exits"]["lane_A_differentiated_PhiFinC1_source_rule"]["would_close_dynamic_source_owner"] is True, "Lane A exit missing")
    require(gate["legal_exits"]["lane_B_honest_selected_Galerkin_C1_table_export"]["would_close_dynamic_source_owner"] is True, "Lane B exit missing")
    require(gate["legal_exits"]["lane_A_differentiated_PhiFinC1_source_rule"]["passes_now"] is False, "Lane A overaccepted")
    require(gate["legal_exits"]["lane_B_honest_selected_Galerkin_C1_table_export"]["passes_now"] is False, "Lane B overaccepted")

    closure = gate["closure_decision"]
    require(closure["dynamic_values_ready"] is True, "dynamic values not ready")
    require(closure["source_rule_proved"] is False, "source rule overproved")
    require(closure["honest_galerkin_table_exported"] is False, "Galerkin export overclaimed")
    require(closure["dynamic_C1_source_owner_closed"] is False, "dynamic source owner overclosed")
    require(closure["true_SM_equivalence_closed"] is False, "true equivalence overclosed")
    require(closure["no_knob_closed"] is False, "no-knob overclosed")

    require(data["what_closes_now"]["exact_phase_R_Z_candidate_table_emitted"] is True, "phase emission missing")
    require(data["what_closes_now"]["exact_shift_R_X_candidate_table_emitted"] is True, "shift emission missing")
    require(data["what_closes_now"]["final_two_exit_dynamic_value_gate_built"] is True, "two-exit gate missing")
    require(data["closure_claimed"] is False, "closure claimed")
    require(data["superset_strategy"]["paths_used_as_knobs"] is False, "superset paths used as knobs")

    require("not a closure claim" in note, "note missing non-closure guardrail")
    require("A^T A = 12 I_2" in note, "note missing exact values")

    for packet in [data, ready, lane_a, lane_b, gate, cert]:
        require(packet.get("observed_data_used_as_selector") is False, "observed selector violation")
        require(packet.get("target_fitting_used") is False, "target fitting violation")

    print(json.dumps({"candidate": str(DATA.relative_to(ROOT)), "status": STATUS}, indent=2))
    print(f"PASS {DATA.name}: {STATUS}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
