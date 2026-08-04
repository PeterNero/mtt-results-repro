"""Audit the H radial-threshold scalar / D-term ten-K route packet."""

from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SLUG = "selected_hradialthresholdscalarsource_or_tenkclosure"
DATA = ROOT / "candidate_data" / f"{SLUG}.candidate.json"
PACKET_DIR = ROOT / "candidate_data" / SLUG
DTERM_IMPORT = PACKET_DIR / "dterm_route_after_selected_sbeta_import.packet.json"
FORMULA = PACKET_DIR / "conditional_h_k_from_ew_boundary_formula.packet.json"
EW_RECHECK = PACKET_DIR / "ew_boundary_rg_recheck_for_h_dterm.packet.json"
HK_GATE = PACKET_DIR / "hk_threshold_gate_after_dterm_route.packet.json"
CUTSET = PACKET_DIR / "next_cutset_after_h_radial_threshold_attempt.packet.json"
CERT = ROOT / "certificates" / f"{SLUG}_certificate.json"
NOTE = ROOT / "proof_corpus" / "MTT_Selected_HRadialThresholdScalarSource_or_TenKClosure_v1.md"
BUILDER = ROOT / "scripts" / f"build_{SLUG}.py"

STATUS = (
    "MTT_SELECTED_HRADIALTHRESHOLDSCALARSOURCE_OR_TENKCLOSURE_"
    "DTERM_ROUTE_REDUCED_EW_BOUNDARY_OPEN"
)
NEXT = "MTT_Selected_EWBoundaryRGFactorForHiggsDTerm_or_DirectTenKClosure_v1"
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
    dterm = load(DTERM_IMPORT)
    formula = load(FORMULA)
    ew = load(EW_RECHECK)
    hk_gate = load(HK_GATE)
    cutset = load(CUTSET)
    cert = load(CERT)
    note = NOTE.read_text(encoding="utf-8")

    for label, packet in [
        ("candidate", data),
        ("D-term import", dterm),
        ("formula", formula),
        ("EW recheck", ew),
        ("H K gate", hk_gate),
        ("cutset", cutset),
        ("certificate", cert),
    ]:
        guard(packet, label)

    require(data["status"] == STATUS, "candidate status")
    require(cert["status"] == STATUS, "certificate status")
    require(data["next_required_artifact"] == NEXT, "candidate next")
    require(cert["next_required_artifact"] == NEXT, "certificate next")
    require(data["theorem"]["proved"] is True, "candidate theorem")
    require(cert["theorem_proved"] is True, "certificate theorem")
    require(data["true_SM_equivalence_claimed"] is False, "true SM overclaim")
    require(data["full_no_knob_closure_claimed"] is False, "no-knob overclaim")

    decision = data["closure_decision"]
    for key in [
        "Dterm_route_imported",
        "selected_s_beta_input_for_Dterm_closed",
        "conditional_lambda_H_mu_match_formula_closed",
        "conditional_K_threshold_formula_closed",
    ]:
        require(decision[key] is True, f"decision should close {key}")
    require(abs(decision["selected_s_beta_value"] - SBETA_VALUE) < 1e-18, "decision s_beta")
    for key in [
        "selected_A_EW_emitted",
        "selected_EW_boundary_RG_packet_closed",
        "selected_matching_scale_mu_match_closed",
        "selected_threshold_RG_transport_closed",
        "lambda_H_mu_match_emitted",
        "K_threshold_Omega_H_lambda_emitted",
        "ten_K_antecedent_satisfied",
        "strict_Omega_lambda_scalar_execution_closed",
        "true_SM_equivalence_closed",
        "full_no_knob_closed",
    ]:
        require(decision[key] is False, f"decision overclosed {key}")
    require(decision["accepted_selected_K_source_row_count"] == 9, "selected K count")
    require(decision["selected_K_threshold_row_count_required"] == 10, "required K count")
    require(decision["accepted_internal_scalar_value_row_count"] == 0, "scalar rows")

    require(
        dterm["status"] == "DTERM_ROUTE_IMPORTED_SELECTED_SBETA_INPUT_CLOSED_EW_BOUNDARY_OPEN",
        "D-term status",
    )
    require(dterm["theorem"]["proved"] is True, "D-term theorem")
    previous_missing = dterm["previous_constants_repo_missing_fields"]
    require(previous_missing["H7B_selected_Dterm_projection_invariant_s_beta_found"] is False, "H7B old s_beta")
    require(previous_missing["H7B_selected_EW_boundary_RG_packet_closed"] is False, "H7B old EW")
    filled = dterm["filled_now_in_current_repo"]
    require(filled["selected_s_beta_value_found"] is True, "s_beta filled")
    require(abs(filled["selected_s_beta_value"] - SBETA_VALUE) < 1e-18, "filled s_beta")
    require(filled["observed_higgs_or_beta_used"] is False, "observed beta")
    require(filled["P_L_projector_emitted"] is False, "P_L overclaim")
    still = dterm["still_open_for_Dterm_value"]
    for key in [
        "selected_EW_boundary_pair_g2_gY",
        "selected_matching_scale_mu_match",
        "selected_threshold_RG_transport",
        "selected_A_EW",
        "numeric_lambda_H_derived",
    ]:
        require(still[key] is False, f"D-term overclosed {key}")

    require(
        formula["status"] == "CONDITIONAL_H_K_FORMULA_FROM_SELECTED_SBETA_AND_AEW_BUILT",
        "formula status",
    )
    require(formula["Dterm_boundary"]["A_EW"] == "(g_2(mu_match)^2 + g_Y(mu_match)^2) / 8", "A_EW")
    require(formula["Dterm_boundary"]["lambda_H_mu_match"] == "A_EW(mu_match) * s_beta", "lambda formula")
    require(abs(formula["selected_s_beta"]["value"] - SBETA_VALUE) < 1e-18, "formula s_beta")
    k_formula = formula["K_threshold_formula_if_same_scheme"]
    require(k_formula["direct_K_row"] == "K_threshold.Omega_H.lambda", "direct K")
    require("A_EW(mu_match) * s_beta" in k_formula["conditional_formula"], "conditional K")
    require(k_formula["requires_selected_A_EW"] is True, "requires A_EW")
    require(k_formula["requires_selected_RG_transport_to_Omega_scheme"] is True, "requires RG")
    for key, value in formula["numeric_status"].items():
        require(value is False, f"formula numeric overclosed {key}")

    require(ew["status"] == "EW_BOUNDARY_RG_RECHECK_VALUES_OPEN", "EW status")
    remaining = ew["remaining_EW_inputs"]
    for key in [
        "K_phys_or_f_ab_closed",
        "physical_alpha_or_metrology_anchor_closed",
        "source_selected_mu_match_closed",
        "source_selected_threshold_vector_closed",
        "precision_RG_threshold_values_closed",
    ]:
        require(remaining[key] is False, f"EW overclosed {key}")
    require(
        "one universal metrological primitive" in ew["allowed_future_routes"]["one_primitive_tier"],
        "one primitive route",
    )

    require(
        hk_gate["status"] == "H_K_THRESHOLD_GATE_DTERM_ROUTE_REDUCED_EW_BOUNDARY_OPEN_9_OF_10",
        "H K status",
    )
    require(hk_gate["accepted_selected_K_source_row_count"] == 9, "H K count")
    require(hk_gate["selected_K_threshold_row_count_required"] == 10, "H K required")
    h_row = hk_gate["H_row"]
    require(h_row["Dterm_route_imported"] is True, "H row D-term")
    require(h_row["selected_s_beta_input_for_Dterm_closed"] is True, "H row s_beta")
    for key in [
        "selected_A_EW_emitted",
        "selected_EW_boundary_RG_packet_closed",
        "lambda_H_mu_match_emitted",
        "direct_K_threshold_Omega_H_lambda_emitted",
    ]:
        require(h_row[key] is False, f"H row overclosed {key}")
    cons = hk_gate["conditional_consequent_current"]
    require(cons["ten_K_antecedent_satisfied"] is False, "ten K")
    require(cons["strict_Omega_lambda_scalar_execution_closed"] is False, "strict scalar")
    require(cons["lambda_H_row_executable"] is False, "lambda executable")
    require(cons["accepted_internal_scalar_value_row_count"] == 0, "internal scalar")

    require(
        cutset["status"] == "NEXT_FRONTIER_EW_BOUNDARY_RG_FACTOR_FOR_HIGGS_DTERM_OR_DIRECT_TEN_K",
        "cutset status",
    )
    require(cutset["next_required_artifact"] == NEXT, "cutset next")
    for phrase in [
        "imported H7B/H7B1 D-term route after selected s_beta",
        "selected H projection invariant input for Route B is now closed in this repo",
        "derived conditional lambda_H(mu_match)=A_EW*s_beta",
        "derived conditional K_threshold.Omega_H.lambda formula in the Omega scheme",
    ]:
        require(phrase in cutset["closed_here"], f"cutset closed missing {phrase}")
    for phrase in [
        "selected EW boundary pair g_2 and g_Y at mu_match",
        "selected A_EW=(g_2^2+g_Y^2)/8",
        "selected matching scale mu_match",
        "selected threshold/RG transport into the Omega/lambda_H scheme",
        "or direct intrinsic H quartic K_threshold.Omega_H.lambda row",
    ]:
        require(phrase in cutset["still_open"], f"cutset open missing {phrase}")

    for phrase in [
        f"`s_beta={SBETA_VALUE}`",
        "`lambda_H(mu_match)=A_EW*s_beta`",
        "`A_EW=(g_2^2+g_Y^2)/8`",
        "`K_threshold.Omega_H.lambda=(A_EW*s_beta)/(D_fin.H*epsilon_Theta^(1/3))`",
        NEXT,
    ]:
        require(phrase in note, f"note missing {phrase}")

    print(
        "AUDIT_PASS: selected s_beta activates the D-term route; "
        "selected A_EW/RG transport and tenth H K row remain open."
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
