"""Audit selected H-sector quartic/threshold payload or strict ten-K closure."""

from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SLUG = "selected_hsectorquarticthresholdpayload_or_stricttenkclosure"
DATA = ROOT / "candidate_data" / f"{SLUG}.candidate.json"
PACKET_DIR = ROOT / "candidate_data" / SLUG
EQUATION = PACKET_DIR / "h_sector_payload_source_equation.packet.json"
TRIALS = PACKET_DIR / "h_sector_payload_candidate_trials.packet.json"
TEN_K_GATE = PACKET_DIR / "strict_ten_k_gate_after_h_payload_attempt.packet.json"
WORKORDER = PACKET_DIR / "h_sector_payload_execution_workorder.packet.json"
CUTSET = PACKET_DIR / "next_cutset_after_h_sector_payload_gate.packet.json"
CERT = ROOT / "certificates" / f"{SLUG}_certificate.json"
NOTE = ROOT / "proof_corpus" / "MTT_Selected_HSectorQuarticThresholdPayload_or_StrictTenKClosure_v1.md"
BUILDER = ROOT / "scripts" / f"build_{SLUG}.py"

STATUS = (
    "MTT_SELECTED_HSECTORQUARTICTHRESHOLDPAYLOAD_OR_STRICTTENKCLOSURE_"
    "BUILT_H_SOURCE_EQUATION_PAYLOAD_ROW_OPEN"
)
NEXT = "MTT_Selected_DirectHThresholdKRowEmission_or_HQuarticFunctionalTheorem_v1"


def load(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def require(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)


def require_close(value: float, expected: float, message: str) -> None:
    require(abs(float(value) - expected) < 1e-12, message)


def guard(packet: dict, label: str) -> None:
    require(packet.get("observed_data_used_as_selector") is False, f"{label} observed selector violation")
    require(packet.get("target_fitting_used") is False, f"{label} target fitting violation")
    require(packet.get("closure_claimed") is True, f"{label} should close its local theorem/gate")


def trial_by_id(trials: dict, trial_id: str) -> dict:
    for trial in trials["trials"]:
        if trial["trial_id"] == trial_id:
            return trial
    raise AssertionError(f"missing trial {trial_id}")


def route_by_id(workorder: dict, route_id: str) -> dict:
    for route in workorder["allowed_routes"]:
        if route["route_id"] == route_id:
            return route
    raise AssertionError(f"missing route {route_id}")


def main() -> int:
    subprocess.run([sys.executable, str(BUILDER)], cwd=ROOT, check=True)

    data = load(DATA)
    cert = load(CERT)
    equation = load(EQUATION)
    trials = load(TRIALS)
    ten_k_gate = load(TEN_K_GATE)
    workorder = load(WORKORDER)
    cutset = load(CUTSET)
    note = NOTE.read_text(encoding="utf-8")

    for label, packet in [
        ("candidate", data),
        ("certificate", cert),
        ("source equation", equation),
        ("candidate trials", trials),
        ("ten-K gate", ten_k_gate),
        ("workorder", workorder),
        ("cutset", cutset),
    ]:
        guard(packet, label)

    require(data["status"] == STATUS, "candidate status mismatch")
    require(cert["status"] == STATUS, "certificate status mismatch")
    require(data["next_required_artifact"] == NEXT, "candidate next mismatch")
    require(cert["next_required_artifact"] == NEXT, "certificate next mismatch")
    require(data["theorem"]["proved"] is True, "candidate theorem missing")
    require(cert["theorem_proved"] is True, "certificate theorem missing")
    require(data["true_SM_equivalence_claimed"] is False, "true SM overclaim")
    require(data["full_no_knob_closure_claimed"] is False, "full no-knob overclaim")
    require(cert["true_SM_equivalence_claimed"] is False, "cert true SM overclaim")
    require(cert["full_no_knob_closure_claimed"] is False, "cert full no-knob overclaim")

    decision = data["closure_decision"]
    require(decision["H_payload_source_equation_closed"] is True, "H equation not closed")
    require(decision["accepted_H_payload_candidate_count"] == 0, "H candidates overaccepted")
    require(decision["selected_H_quartic_functional_emitted"] is False, "H quartic overemitted")
    require(decision["selected_H_threshold_scheme_emitted"] is False, "H threshold overemitted")
    require(decision["selected_H_K_threshold_row_emitted"] is False, "H K overemitted")
    require(decision["accepted_selected_K_source_row_count"] == 9, "selected K count mismatch")
    require(decision["selected_K_threshold_row_count_required"] == 10, "required K count mismatch")
    require(decision["ten_K_antecedent_satisfied"] is False, "ten-K antecedent overclosed")
    require(decision["strict_Omega_lambda_scalar_execution_closed"] is False, "Omega/lambda overclosed")
    require(decision["accepted_internal_scalar_value_row_count"] == 0, "scalar rows overaccepted")
    require(decision["true_SM_equivalence_closed"] is False, "true SM closure overclaimed")
    require(decision["full_no_knob_closed"] is False, "full no-knob closure overclaimed")

    require(equation["status"] == "H_SECTOR_SOURCE_EQUATION_CLOSED_VALUE_ROW_OPEN", "equation status")
    require(equation["omega_id"] == "Omega_H.lambda", "equation omega mismatch")
    require(equation["combined_kernel_row_id"] == "K_threshold.Omega_H.lambda", "equation K id")
    source_eq = equation["selected_source_equation"]
    require(
        source_eq["omega_value"]
        == "Omega_H.lambda.value = D_fin.H * K_threshold.Omega_H.lambda * epsilon_Theta^(1/3)",
        "omega source equation mismatch",
    )
    require(source_eq["direct_K_row"] == "K_threshold.Omega_H.lambda", "direct K row mismatch")
    require(
        source_eq["split_K_row"]
        == "K_threshold.Omega_H.lambda = L_rowlocal.Omega_H.lambda * T_scheme.Omega_H.lambda",
        "split K row mismatch",
    )
    require(
        source_eq["prefactor_factorization"]
        == "C_HYMthr.H.lambda = D_fin.H * L_rowlocal.Omega_H.lambda * T_scheme.Omega_H.lambda",
        "prefactor factorization mismatch",
    )
    closed = equation["closed_inputs"]
    require(closed["selected_H_projector_carrier"] is True, "H carrier not closed")
    require(closed["H_projector_rank"] == 1, "H rank mismatch")
    require(closed["H_transport_identity"] is True, "H identity transport lost")
    require(closed["D_fin_H_subfactor_closed"] is True, "D_fin.H not closed")
    require(closed["D_fin_H_subfactor_id"] == "D_fin.H", "D_fin.H id mismatch")
    require(closed["shared_circle_theta_exponent_closed"] is True, "shared-circle exponent not closed")
    require(closed["theta_exponent"] == "1/3", "theta exponent mismatch")
    require_close(closed["theta_weight"], 0.12314471107013315, "theta weight mismatch")
    require(closed["ten_K_conditional_theorem_closed"] is True, "conditional theorem missing")
    for key, value in equation["open_source_terms"].items():
        require(value is False, f"open source term overclosed: {key}")
    diagnostic = equation["diagnostic_postcheck_only"]
    require(diagnostic["rowlocal_composite_target_symbolic"] == "(1.193869931683266) / D_fin.H", "diagnostic expression")
    require_close(diagnostic["diagnostic_prefactor_numerator"], 1.193869931683266, "diagnostic numerator")
    require(diagnostic["accepted_as_source_row"] is False, "diagnostic row overaccepted")
    require(diagnostic["source_value_tier"] == "diagnostic_replay_postcheck_only", "diagnostic tier mismatch")

    require(trials["status"] == "CURRENT_H_PAYLOAD_CANDIDATES_TESTED_ZERO_ACCEPTED", "trials status")
    require(trials["accepted_H_payload_candidate_count"] == 0, "trial H count")
    require(trials["accepted_direct_H_K_row_count"] == 0, "trial direct H K count")
    require(len(trials["trials"]) == 4, "trial count mismatch")
    for trial in trials["trials"]:
        require(trial["accepted"] is False, f"{trial['trial_id']} overaccepted")
    rank_trial = trial_by_id(trials, "direct_H_quartic_from_rank_one_projector")
    require(rank_trial["closed_support"]["rank"] == 1, "rank trial rank")
    require(rank_trial["closed_support"]["selected_H_projector_carrier"] is True, "rank trial carrier")
    require(rank_trial["closed_support"]["transport_identity"] is True, "rank trial transport")
    require("do not define a quartic functional" in rank_trial["reason"], "rank trial reason")
    heat_trial = trial_by_id(trials, "D_fin_H_times_shared_circle_theta")
    require(heat_trial["closed_support"]["D_fin_H_subfactor"] == "D_fin.H", "heat trial D_fin")
    require(heat_trial["closed_support"]["theta_exponent"] == "1/3", "heat trial theta")
    require("leaves K_threshold.Omega_H.lambda open" in heat_trial["reason"], "heat trial reason")
    inversion_trial = trial_by_id(trials, "postcheck_inversion_for_K_H")
    require(inversion_trial["uses_replay_postcheck"] is True, "inversion trial replay flag")
    require(inversion_trial["diagnostic_expression"] == "(1.193869931683266) / D_fin.H", "inversion expression")
    require_close(inversion_trial["diagnostic_prefactor_numerator"], 1.193869931683266, "inversion numerator")
    require("cannot select the source row" in inversion_trial["reason"], "inversion reason")
    step73_trial = trial_by_id(trials, "step73_honest_galerkin_current_H_row")
    require(step73_trial["closed_support"]["diagonal_hym_connection_available"] is True, "Step73 HYM missing")
    require(step73_trial["closed_support"]["diagonal_green_available"] is True, "Step73 Green missing")
    require(step73_trial["closed_support"]["model_active_zero_mode_basis_available"] is True, "Step73 basis missing")
    require("emits no selected retarded overlap derivative" in step73_trial["reason"], "Step73 reason")
    for phrase in [
        "use H rank one as L_rowlocal.Omega_H.lambda=1",
        "use the postcheck inversion as a source row",
        "treat D_fin.H * epsilon_Theta^(1/3) as Omega_H.lambda without K_threshold.Omega_H.lambda",
        "claim ten-K closure with the H row absent",
    ]:
        require(phrase in trials["forbidden_promotions"], f"forbidden promotion missing {phrase}")

    require(ten_k_gate["status"] == "STRICT_TEN_K_GATE_RECHECKED_H_ROW_STILL_OPEN", "ten-K gate status")
    require(ten_k_gate["accepted_selected_K_source_row_count"] == 9, "ten-K selected count")
    require(ten_k_gate["selected_K_threshold_row_count_required"] == 10, "ten-K required count")
    require(ten_k_gate["ten_K_antecedent_satisfied"] is False, "ten-K antecedent overclosed")
    h_row = ten_k_gate["H_row"]
    require(h_row["omega_id"] == "Omega_H.lambda", "H row omega")
    require(h_row["combined_kernel_row_id"] == "K_threshold.Omega_H.lambda", "H row K")
    require(h_row["selected_H_payload_equation_closed"] is True, "H source equation not marked closed")
    for key in [
        "selected_H_quartic_functional_emitted",
        "selected_H_threshold_scheme_emitted",
        "selected_L_rowlocal_Omega_H_lambda",
        "selected_T_scheme_Omega_H_lambda",
        "selected_direct_K_threshold_Omega_H_lambda",
    ]:
        require(h_row[key] is False, f"H row overclosed {key}")
    current = ten_k_gate["conditional_consequent_current"]
    require(current["strict_Omega_rows_executable"] is False, "strict Omega overclosed")
    require(current["lambda_H_row_executable"] is False, "lambda_H overclosed")
    require(current["accepted_internal_scalar_value_row_count"] == 0, "scalar count overaccepted")

    require(workorder["status"] == "DIRECT_H_K_ROW_OR_H_QUARTIC_FUNCTIONAL_WORKORDER_EMITTED", "workorder status")
    for route_id in [
        "direct_H_K_row_from_selected_galerkin",
        "split_H_quartic_and_threshold_payload",
        "source_selected_H_universal_anchor",
    ]:
        route_by_id(workorder, route_id)
    for phrase in [
        "do not read sm_parity_projected_abs_value before source row emission",
        "prove q=79/F/m=1 same-branch provenance for the H row",
        "emit K_threshold.Omega_H.lambda or both split factors before strict Omega execution",
        "then use the existing conditional ten-K theorem as the scalar execution trigger",
    ]:
        require(phrase in workorder["acceptance_tests"], f"acceptance test missing {phrase}")

    require(cutset["status"] == "NEXT_FRONTIER_DIRECT_H_K_ROW_OR_H_QUARTIC_FUNCTIONAL", "cutset status")
    require(cutset["next_required_artifact"] == NEXT, "cutset next mismatch")
    for phrase in [
        "H-sector source equation closed",
        "current H candidate trials tested with zero accepted source rows",
        "postcheck inversion quarantined as replay-only",
        "strict ten-K gate rechecked at 9/10",
        "direct H K row workorder emitted",
    ]:
        require(phrase in cutset["closed_here"], f"cutset closed missing {phrase}")
    for phrase in [
        "selected H-sector quartic/overlap functional",
        "selected H-sector threshold/scheme functional",
        "selected K_threshold.Omega_H.lambda source row",
        "strict Omega/lambda_H scalar execution",
        "selected matrix-level mixing extension and true SM equivalence",
    ]:
        require(phrase in cutset["still_open"], f"cutset open missing {phrase}")

    for phrase in [
        "H-sector source equation",
        "Omega_H.lambda = D_fin.H * K_threshold.Omega_H.lambda * epsilon_Theta^(1/3)",
        "K_threshold.Omega_H.lambda = L_rowlocal.Omega_H.lambda * T_scheme.Omega_H.lambda",
        "current H candidate trials tested: `0` accepted",
        "ten-K gate remains: `9/10`",
        "selected H quartic/overlap functional: `false`",
        "selected direct `K_threshold.Omega_H.lambda`: `false`",
        NEXT,
    ]:
        require(phrase in note, f"note missing {phrase}")

    print(f"PASS {DATA.name}: {STATUS}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
