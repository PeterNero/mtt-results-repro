"""Audit residual-completion source-promotion or honest Galerkin C1 emission gate."""

from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "candidate_data" / "selected_residualcompletion_sourcepromotion_or_honestgalerkinc1_emission.candidate.json"
SOURCE_PACKET = (
    ROOT
    / "candidate_data"
    / "selected_residualcompletion_sourcepromotion_or_honestgalerkinc1_emission"
    / "minimal_residual_source_packet.template.json"
)
PARITY_GATE = (
    ROOT
    / "candidate_data"
    / "selected_residualcompletion_sourcepromotion_or_honestgalerkinc1_emission"
    / "sm_parity_vs_no_knob_acceptance_gate.packet.json"
)
CERT = ROOT / "certificates" / "selected_residualcompletion_sourcepromotion_or_honestgalerkinc1_emission_certificate.json"
NOTE = ROOT / "proof_corpus" / "MTT_Selected_ResidualCompletion_SourcePromotion_or_HonestGalerkinC1_Emission_v1.md"
BUILDER = ROOT / "scripts" / "build_selected_residualcompletion_sourcepromotion_or_honestgalerkinc1_emission.py"

STATUS = (
    "MTT_SELECTED_RESIDUALCOMPLETION_SOURCEPROMOTION_OR_HONESTGALERKINC1_EMISSION_"
    "BUILT_PROMOTION_GATE_OPEN"
)
NEXT = "MTT_Selected_ResidualSourceTheorem_or_GalerkinC1Run_ValueFill_v1"


def require(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)


def load(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def main() -> int:
    subprocess.run([sys.executable, str(BUILDER)], cwd=ROOT, check=True)

    data = load(DATA)
    source_packet = load(SOURCE_PACKET)
    parity_gate = load(PARITY_GATE)
    cert = load(CERT)
    note = NOTE.read_text(encoding="utf-8")

    require(data["status"] == STATUS, "candidate status mismatch")
    require(cert["status"] == STATUS, "certificate status mismatch")
    require(data["next_required_artifact"] == NEXT, "candidate next mismatch")
    require(cert["next_required_artifact"] == NEXT, "certificate next mismatch")
    require(NEXT in note, "note missing next artifact")

    require(source_packet["status"] == "TEMPLATE_EMITTED_SOURCE_THEOREM_OPEN", "source packet status mismatch")
    require(source_packet["same_branch_source_required"] is True, "same branch source not required")
    require(source_packet["observed_data_forbidden"] is True, "observed data not forbidden")
    require(source_packet["target_fitting_forbidden"] is True, "target fitting not forbidden")
    require(source_packet["selected_source_selector_attached"] is True, "source selector not attached")
    require(source_packet["active_shift"] == [1, 1], "active shift mismatch")
    require(source_packet["fixed_fiber_class"] == [0, 1, 2], "fixed fiber class mismatch")

    phase = source_packet["required_source_emissions"]["phase_residual_operator_R_Z"]
    shift = source_packet["required_source_emissions"]["shift_residual_operator_R_X"]
    require(phase["shape"]["residual_norm_sq"] == 4.0, "phase residual norm mismatch")
    require(shift["shape"]["residual_norm_sq"] == 2.0, "shift residual norm mismatch")
    require(phase["shape"]["orthogonal_to_fixed_fiber_span"] is True, "phase residual not orthogonal")
    require(shift["shape"]["orthogonal_to_fixed_fiber_span"] is True, "shift residual not orthogonal")
    require(phase["selected_by_MTT_now"] is False, "phase residual overselected")
    require(shift["selected_by_MTT_now"] is False, "shift residual overselected")

    implied = source_packet["if_emitted_then"]
    require(implied["projection_plus_residual_reconstructs_conditional_packet"] is True, "reconstruction missing")
    require(implied["A_transpose_A"] == [[12.0, 0.0], [0.0, 12.0]], "A^T A mismatch")
    require(implied["A_transpose_b"] == [12.0, 12.0], "A^T b mismatch")
    require(implied["deltaTheta_C1"] == [1.0, 1.0], "deltaTheta mismatch")
    require(implied["rank"] == 2, "rank mismatch")

    require(parity_gate["this_repo_view"] == "SM_PARITY_FIRST", "SM parity lens missing")
    require(parity_gate["sibling_repo_default_view"] == "NO_KNOB_RESEARCH", "sibling no-knob lens missing")
    require(parity_gate["current_decision"] == "OPEN_FOR_SM_PARITY_BECAUSE_NO_TYPED_SELECTED_DYNAMIC_PACKET_IS_EMITTED_YET", "parity decision mismatch")
    require(parity_gate["measured_constants_used_as_selector"] is False, "measured selector misuse")
    require("deriving observed Yukawa magnitudes" in parity_gate["SM_parity_does_not_require_here"], "parity/no-knob split missing")

    lane_a, lane_b = data["lane_results"]
    require(lane_a["status"] == "OPEN_SOURCE_THEOREM_MISSING", "Lane A overclosed")
    require(lane_b["status"] == "OPEN_RUN_VALUES_MISSING", "Lane B overclosed")
    require(lane_a["closes_SM_parity_dynamic_packet_if_source_theorem_supplied"] is True, "Lane A parity implication missing")
    require(lane_a["closes_no_knob_flavor_constants_if_source_theorem_supplied"] is False, "Lane A no-knob overclaim")
    require(lane_b["closes_SM_parity_dynamic_packet_if_selected_run_emits_values"] is True, "Lane B parity implication missing")
    require(lane_b["selected_source_verified"] is False, "Lane B source oververified")

    decision = data["promotion_decision"]
    for key in [
        "lane_A_promoted",
        "lane_B_promoted",
        "selected_residual_source_packet_promoted",
        "honest_Galerkin_C1_emission_promoted",
        "A_selected_promoted",
        "b_selected_promoted",
        "deltaTheta_C1_promoted",
        "SM_parity_dynamic_packet_closed",
        "no_knob_flavor_constants_closed",
    ]:
        require(decision[key] is False, f"promotion overclaimed: {key}")

    closes = data["what_closes_now"]
    for key in [
        "minimal_residual_source_packet_template_emitted",
        "two_lane_source_promotion_gate_built",
        "SM_parity_vs_no_knob_acceptance_separated",
        "exact_post_promotion_linear_algebra_fixed",
        "observed_constants_excluded_as_selectors",
    ]:
        require(closes[key] is True, f"close flag missing: {key}")

    remains = data["what_remains_open"]
    for key in [
        "same_branch_residual_source_theorem",
        "honest_selected_Galerkin_C1_value_run",
        "selected_A_selected",
        "selected_b_selected",
        "selected_deltaTheta_C1",
        "SM_parity_dynamic_packet_closure",
        "true_SM_equivalence_closure",
        "full_no_knob_flavor_closure",
    ]:
        require(remains[key] is True, f"remaining gate missing: {key}")

    require(data["closure_claimed"] is False, "closure overclaimed")
    require(data["SM_parity_dynamic_packet_closure_claimed"] is False, "SM parity dynamic overclaimed")
    require(data["true_SM_equivalence_claimed"] is False, "true equivalence overclaimed")
    require(data["no_knob_closure_claimed"] is False, "no-knob overclaimed")
    require(data["observed_data_used"] is False, "observed data used")
    require(data["target_fitting_used"] is False, "target fitting used")
    require(data["theorem"]["proved"] is True, "theorem not proved")
    require(cert["theorem_proved"] is True, "certificate theorem missing")
    require("SM-Parity View" in note, "note missing SM-parity view")
    require("Lane A" in note and "Lane B" in note, "note missing lanes")

    print(f"PASS {DATA.name}: {STATUS}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
