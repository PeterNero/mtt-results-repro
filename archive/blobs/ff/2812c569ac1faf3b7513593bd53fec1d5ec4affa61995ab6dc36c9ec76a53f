"""Audit the H-sector quartic threshold gate after selected projection reduction."""

from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SLUG = "selected_hsectorquarticthresholdfromprojectionreduction_or_dynamicherm2rows"
DATA = ROOT / "candidate_data" / f"{SLUG}.candidate.json"
PACKET_DIR = ROOT / "candidate_data" / SLUG
QUARTIC_GATE = PACKET_DIR / "projection_reduction_to_h_quartic_gate.packet.json"
HERM2_NOGO = PACKET_DIR / "sbeta_to_dynamic_herm2_rows_nogo.packet.json"
PAYLOAD_CONTRACT = PACKET_DIR / "h_quartic_threshold_payload_contract.packet.json"
TRIALS = PACKET_DIR / "current_h_payload_trials_after_sbeta.packet.json"
HK_GATE = PACKET_DIR / "hk_threshold_gate_after_sbeta_quartic_attempt.packet.json"
CUTSET = PACKET_DIR / "next_cutset_after_sbeta_quartic_attempt.packet.json"
CERT = ROOT / "certificates" / f"{SLUG}_certificate.json"
NOTE = (
    ROOT
    / "proof_corpus"
    / "MTT_Selected_HSectorQuarticThresholdFromProjectionReduction_or_DynamicHerm2Rows_v1.md"
)
BUILDER = ROOT / "scripts" / f"build_{SLUG}.py"

STATUS = (
    "MTT_SELECTED_HSECTORQUARTICTHRESHOLDFROMPROJECTIONREDUCTION_OR_DYNAMICHERM2ROWS_"
    "SBETA_FACTOR_CLOSED_PAYLOAD_ROWS_OPEN"
)
NEXT = "MTT_Selected_DirectHQuarticThresholdFunctional_or_DynamicHerm2ValueRows_v1"
SBETA_VALUE = 0.004701083905943647


def load(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def require(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)


def guard(packet: dict, label: str) -> None:
    require(packet.get("closure_claimed") is True, f"{label} closure flag")
    require(packet.get("observed_data_used_as_selector") is False, f"{label} observed selector")
    require(packet.get("target_fitting_used") is False, f"{label} target fitting")


def main() -> int:
    subprocess.run([sys.executable, str(BUILDER)], cwd=ROOT, check=True)

    data = load(DATA)
    quartic = load(QUARTIC_GATE)
    herm2 = load(HERM2_NOGO)
    contract = load(PAYLOAD_CONTRACT)
    trials = load(TRIALS)
    hk_gate = load(HK_GATE)
    cutset = load(CUTSET)
    cert = load(CERT)
    note = NOTE.read_text(encoding="utf-8")

    for label, packet in [
        ("candidate", data),
        ("quartic gate", quartic),
        ("Herm2 no-go", herm2),
        ("payload contract", contract),
        ("trials", trials),
        ("H K gate", hk_gate),
        ("cutset", cutset),
        ("certificate", cert),
    ]:
        guard(packet, label)

    require(data["status"] == STATUS, "candidate status")
    require(cert["status"] == STATUS, "certificate status")
    require(data["next_required_artifact"] == NEXT, "candidate next")
    require(cert["next_required_artifact"] == NEXT, "cert next")
    require(data["theorem"]["proved"] is True, "candidate theorem")
    require(cert["theorem_proved"] is True, "cert theorem")
    require(data["true_SM_equivalence_claimed"] is False, "true SM overclaim")
    require(data["full_no_knob_closure_claimed"] is False, "no-knob overclaim")

    decision = data["closure_decision"]
    for key in [
        "selected_H_angular_projection_factor_s_beta_closed",
        "selected_s_beta_value_found",
        "sbeta_to_dynamic_Herm2_rows_nogo_closed",
        "H_quartic_threshold_payload_contract_closed",
    ]:
        require(decision[key] is True, f"decision should close {key}")
    require(abs(decision["selected_s_beta_value"] - SBETA_VALUE) < 1e-18, "decision s_beta")
    for key in [
        "selected_H_quartic_functional_emitted",
        "selected_H_threshold_scheme_functional_emitted",
        "selected_L_rowlocal_Omega_H_lambda",
        "selected_T_scheme_Omega_H_lambda",
        "K_threshold_Omega_H_lambda_emitted",
        "selected_dynamic_strain_kernel_emitted",
        "selected_F_H_second_variation_emitted",
        "selected_H_response_table_emitted",
        "selected_Hermitian_M_H_values_emitted",
        "direct_Herm2_Huv_payload_emitted",
        "selected_Delta_row_emitted",
        "selected_Re_Omega_row_emitted",
        "selected_Im_Omega_row_emitted",
        "mass_light_line_projector_P_L_emitted",
        "ten_K_antecedent_satisfied",
        "strict_Omega_lambda_scalar_execution_closed",
        "true_SM_equivalence_closed",
        "full_no_knob_closed",
    ]:
        require(decision[key] is False, f"decision overclosed {key}")
    require(decision["accepted_selected_K_source_row_count"] == 9, "selected K count")
    require(decision["selected_K_threshold_row_count_required"] == 10, "required K count")
    require(decision["accepted_internal_scalar_value_row_count"] == 0, "internal scalar rows")

    require(
        quartic["status"] == "SELECTED_SBETA_ANGULAR_FACTOR_CLOSED_H_QUARTIC_NORMALIZATION_OPEN",
        "quartic status",
    )
    require(quartic["theorem"]["proved"] is True, "quartic theorem")
    closed = quartic["closed_projection_factor"]
    require(closed["selected_s_beta_promoted"] is True, "s_beta promoted")
    require(abs(closed["selected_s_beta_value"] - SBETA_VALUE) < 1e-18, "quartic s_beta")
    require(closed["projection_measure_equality"] is True, "projection equality")
    require(closed["no_extra_boundary_source_term"] is True, "no boundary")
    require(closed["observed_higgs_or_beta_used"] is False, "observed beta")
    required = quartic["required_for_H_quartic_threshold"]
    for key, value in required.items():
        require(value is None, f"quartic requirement overfilled {key}")
    for key in [
        "selected_H_angular_projection_factor_closed",
        "selected_H_quartic_functional_emitted",
        "selected_H_threshold_scheme_functional_emitted",
        "K_threshold_Omega_H_lambda_emitted",
        "lambda_H_value_row_emitted",
    ]:
        if key == "selected_H_angular_projection_factor_closed":
            require(quartic["decision"][key] is True, f"quartic decision {key}")
        else:
            require(quartic["decision"][key] is False, f"quartic overclosed {key}")

    require(
        herm2["status"] == "SBETA_DOES_NOT_DETERMINE_DYNAMIC_HERM2_ROWS",
        "Herm2 no-go status",
    )
    require(herm2["theorem"]["proved"] is True, "Herm2 theorem")
    require(herm2["accepted_Herm2_relation"] == "Delta^2/(Delta^2+|Omega|^2)", "relation")
    family = herm2["same_s_beta_witness_family"]
    require(abs(family["s_beta_value"] - SBETA_VALUE) < 1e-18, "family s_beta")
    require(len(family["witness_rows"]) == 2, "witness count")
    witness_1, witness_2 = family["witness_rows"]
    require(witness_1["Delta"] != witness_2["Delta"], "witness Delta differs")
    require(witness_1["Re_Omega"] != witness_2["Re_Omega"], "witness Re differs")
    require(witness_1["Im_Omega"] != witness_2["Im_Omega"], "witness Im differs")
    for key, value in herm2["not_emitted"].items():
        require(value is None, f"Herm2 no-go overfilled {key}")
    previous_dynamic = herm2["previous_dynamic_route_recheck"]
    for key in [
        "selected_dynamic_strain_kernel_emitted",
        "selected_F_H_second_variation_emitted",
        "selected_H_response_table_emitted",
        "selected_Hermitian_M_H_values_emitted",
        "direct_Herm2_Huv_payload_emitted",
        "selected_Delta_row_emitted",
        "selected_Re_Omega_row_emitted",
        "selected_Im_Omega_row_emitted",
    ]:
        require(previous_dynamic[key] is False, f"previous dynamic overclosed {key}")

    require(
        contract["status"] == "H_QUARTIC_THRESHOLD_PAYLOAD_CONTRACT_CLOSED_VALUES_OPEN",
        "contract status",
    )
    require(contract["payload_name"] == "SelectedHQuarticThresholdPayload", "contract name")
    must = contract["must_emit"]
    require(must["selected_H_angular_factor_s_beta"] == SBETA_VALUE, "contract s_beta")
    require(must["no_observed_lambda_or_higgs_replay_selector"] is True, "contract guard")
    for key in [
        "source_functional_id",
        "same_branch_source_owner_certificate",
        "quartic_or_threshold_functional_formula",
        "normalization_or_coupling_row",
        "selected_H_threshold_scheme_factor",
        "selected_L_rowlocal_Omega_H_lambda",
        "selected_T_scheme_Omega_H_lambda",
        "direct_K_threshold_Omega_H_lambda",
        "finite_exactness_or_residual_bound",
    ]:
        require(must[key] is None, f"contract overfilled {key}")
    sub = contract["already_closed_subfields"]
    require(sub["selected_s_beta"] is True, "closed s_beta")
    require(sub["D_fin_H_closed"] is True, "D_fin.H")
    require(sub["theta_exponent_1_over_3_closed"] is True, "theta")
    require(sub["conditional_ten_K_scalar_closure_theorem"] is True, "conditional K")

    require(
        trials["status"] == "CURRENT_H_PAYLOAD_TRIALS_AFTER_SBETA_ZERO_K_ROWS_ACCEPTED",
        "trials status",
    )
    require(trials["accepted_H_K_source_row_count"] == 0, "trial accepted K")
    require(len(trials["trials"]) == 4, "trial count")
    for trial in trials["trials"]:
        require(trial["accepted_as_K_threshold_Omega_H_lambda"] is False, f"trial accepted {trial['route_id']}")

    require(
        hk_gate["status"] == "H_K_THRESHOLD_GATE_SBETA_FACTOR_CLOSED_H_PAYLOAD_OPEN_9_OF_10",
        "H K status",
    )
    require(hk_gate["accepted_selected_K_source_row_count"] == 9, "H K count")
    require(hk_gate["selected_K_threshold_row_count_required"] == 10, "H K required")
    h_row = hk_gate["H_row"]
    require(h_row["selected_H_angular_projection_factor_s_beta_closed"] is True, "H row s_beta")
    require(abs(h_row["selected_s_beta_value"] - SBETA_VALUE) < 1e-18, "H row value")
    for key in [
        "s_beta_promoted_as_K_threshold",
        "selected_H_quartic_functional_emitted",
        "selected_H_threshold_scheme_functional_emitted",
        "selected_L_rowlocal_Omega_H_lambda",
        "selected_T_scheme_Omega_H_lambda",
        "selected_dynamic_strain_kernel_emitted",
        "selected_F_H_second_variation_emitted",
        "selected_Hermitian_M_H_values_emitted",
        "selected_Delta_row_emitted",
        "selected_Re_Omega_row_emitted",
        "selected_Im_Omega_row_emitted",
        "K_threshold_Omega_H_lambda_emitted",
    ]:
        require(h_row[key] is False, f"H row overclosed {key}")
    cons = hk_gate["conditional_consequent_current"]
    require(cons["ten_K_antecedent_satisfied"] is False, "ten K")
    require(cons["strict_Omega_lambda_scalar_execution_closed"] is False, "strict scalar")
    require(cons["lambda_H_row_executable"] is False, "lambda executable")
    require(cons["accepted_internal_scalar_value_row_count"] == 0, "scalar rows")

    require(
        cutset["status"]
        == "NEXT_FRONTIER_DIRECT_H_QUARTIC_THRESHOLD_FUNCTIONAL_OR_DYNAMIC_HERM2_VALUE_ROWS",
        "cutset status",
    )
    require(cutset["next_required_artifact"] == NEXT, "cutset next")
    for phrase in [
        "selected s_beta promoted from projection reduction to H angular factor",
        "proved s_beta does not determine dynamic Herm(2) rows",
        "H quartic/threshold payload contract emitted",
        "current s_beta/D_fin/theta/empirical/Galerkin shortcuts rejected as H K source rows",
        "H K-threshold gate remains 9/10",
    ]:
        require(phrase in cutset["closed_here"], f"cutset closed missing {phrase}")
    for phrase in [
        "selected H-sector quartic normalization functional",
        "selected H-sector threshold/scheme functional",
        "selected L_rowlocal.Omega_H.lambda and T_scheme.Omega_H.lambda, or direct K_threshold.Omega_H.lambda",
        "selected dynamic strain/response functional F_H with nonzero Herm(2) trace-free part",
        "Delta/Re(Omega)/Im(Omega) dynamic mass-strain rows",
        "strict Omega/lambda_H scalar execution",
    ]:
        require(phrase in cutset["still_open"], f"cutset open missing {phrase}")

    for phrase in [
        f"`s_beta={SBETA_VALUE}`",
        "does not determine `Delta/Re(Omega)/Im(Omega)`",
        "`SelectedHQuarticThresholdPayload`",
        "insufficient for the H K row",
        NEXT,
    ]:
        require(phrase in note, f"note missing {phrase}")

    print(
        "AUDIT_PASS: selected s_beta promoted only as H angular factor; "
        "Herm(2) and H K-threshold payload rows remain open."
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
