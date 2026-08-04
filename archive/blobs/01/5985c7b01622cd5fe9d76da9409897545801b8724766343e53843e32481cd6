"""Audit the EW-boundary/RG factor gate for the selected Higgs D-term route."""

from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SLUG = "selected_ewboundaryrgfactorforhiggsdterm_or_directtenkclosure"
DATA = ROOT / "candidate_data" / f"{SLUG}.candidate.json"
PACKET_DIR = ROOT / "candidate_data" / SLUG
TIER_GATE = PACKET_DIR / "aew_source_tier_gate.packet.json"
DIAGNOSTIC = PACKET_DIR / "external_aew_dterm_diagnostic_postcheck.packet.json"
ROUTE_DECISION = PACKET_DIR / "dterm_route_decision_after_aew_recheck.packet.json"
HK_GATE = PACKET_DIR / "hk_threshold_gate_after_aew_recheck.packet.json"
CUTSET = PACKET_DIR / "next_cutset_after_aew_recheck.packet.json"
CERT = ROOT / "certificates" / f"{SLUG}_certificate.json"
NOTE = (
    ROOT
    / "proof_corpus"
    / "MTT_Selected_EWBoundaryRGFactorForHiggsDTerm_or_DirectTenKClosure_v1.md"
)
BUILDER = ROOT / "scripts" / f"build_{SLUG}.py"

STATUS = (
    "MTT_SELECTED_EWBOUNDARYRGFACTORFORHIGGSDTERM_OR_DIRECTTENKCLOSURE_"
    "AEW_TIER_GATE_CLOSED_VALUES_OPEN"
)
NEXT = "MTT_Selected_IntrinsicHQuarticKRow_or_SelectedLargeThresholdRGTheorem_v1"


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
    tier = load(TIER_GATE)
    diagnostic = load(DIAGNOSTIC)
    route = load(ROUTE_DECISION)
    hk_gate = load(HK_GATE)
    cutset = load(CUTSET)
    cert = load(CERT)
    note = NOTE.read_text(encoding="utf-8")

    for label, packet in [
        ("candidate", data),
        ("tier gate", tier),
        ("diagnostic", diagnostic),
        ("route decision", route),
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
        "A_EW_source_tier_gate_closed",
        "external_AEW_diagnostic_postcheck_built",
        "one_universal_primitive_extension_ready",
    ]:
        require(decision[key] is True, f"decision should close {key}")
    for key in [
        "plain_external_Dterm_postcheck_success",
        "selected_A_EW_emitted",
        "selected_matching_scale_mu_match_closed",
        "selected_threshold_RG_transport_closed",
        "selected_large_threshold_RG_theorem_emitted",
        "one_universal_primitive_selected_now",
        "direct_intrinsic_H_quartic_K_row_emitted",
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

    diag_nums = data["diagnostic_numbers_not_source"]
    require(diag_nums["A_EW_Mt_external"] > 0, "A_EW positive")
    require(diag_nums["lambda_Dterm_Mt_external_AEW_times_selected_sbeta"] > 0, "lambda dterm positive")
    require(diag_nums["lambda_Mt_external_coordinate"] > 0, "lambda external positive")
    require(diag_nums["underprediction_factor_lambda_ext_over_Dterm"] > 100, "underprediction not large")
    require(diag_nums["required_A_EW_to_match_external_lambda_Mt"] > 1, "required A_EW not large")
    require(diag_nums["required_effective_sqrt_g2sq_plus_gYsq"] > 10, "required geff not large")

    require(tier["status"] == "AEW_SOURCE_TIER_GATE_CLOSED_VALUES_OPEN", "tier status")
    require(tier["theorem"]["proved"] is True, "tier theorem")
    strict = tier["strict_no_knob_tier"]
    require(strict["current_corpus_no_go"] is True, "strict no-go")
    require(strict["B41_K_phys_or_f_ab_closed"] is False, "K_phys overclosed")
    require(strict["B41_source_selected_mu_match_closed"] is False, "mu_match overclosed")
    require(strict["selected_A_EW_emitted"] is False, "A_EW overclosed")
    one = tier["one_universal_primitive_tier"]
    require(one["extension_ready"] is True, "one primitive ready")
    require(one["primitive_selected_now"] is False, "one primitive selected")
    require(one["selected_A_EW_emitted"] is False, "one primitive A_EW")
    external = tier["admitted_external_replay_tier"]
    require(external["WZH_external_coordinate_rows_closed"] is True, "WZH rows")
    require(external["accepted_selected_Rtheta_source_row_count"] == 0, "external source rows")
    require(external["accepted_as_no_knob_A_EW"] is False, "external A_EW overaccepted")

    require(
        diagnostic["status"] == "EXTERNAL_AEW_DTERM_POSTCHECK_BUILT_NOT_SOURCE",
        "diagnostic status",
    )
    interp = diagnostic["interpretation"]
    require(interp["accepted_as_source_row"] is False, "diagnostic source")
    require(interp["plain_external_weak_coupling_Dterm_closes_H_row"] is False, "diagnostic closes")
    require(interp["large_threshold_or_direct_H_row_required_for_external_lambda_postcheck"] is True, "large/direct")
    require(diagnostic["diagnostic_values"] == diag_nums, "diagnostic numbers mismatch")

    require(
        route["status"] == "DTERM_ROUTE_CONDITIONAL_LARGE_THRESHOLD_OR_DIRECT_H_ROW_REQUIRED",
        "route status",
    )
    route_status = route["route_status"]
    require(route_status["selected_s_beta_input_closed"] is True, "route s_beta")
    for key in [
        "selected_A_EW_closed",
        "selected_RG_threshold_transport_closed",
        "plain_external_Dterm_postcheck_success",
        "direct_intrinsic_H_quartic_K_row_emitted",
        "large_selected_threshold_RG_theorem_emitted",
    ]:
        require(route_status[key] is False, f"route overclosed {key}")
    for phrase in [
        "promote external g_2/g_Y rows as no-knob A_EW",
        "use selected s_beta alone as the Higgs quartic value",
        "hide a large Higgs threshold correction without a source theorem",
    ]:
        require(phrase in route["retired_shortcuts"], f"missing retired {phrase}")

    require(
        hk_gate["status"]
        == "H_K_THRESHOLD_GATE_AEW_VALUES_OPEN_DIRECT_OR_LARGE_THRESHOLD_REQUIRED_9_OF_10",
        "H K status",
    )
    require(hk_gate["accepted_selected_K_source_row_count"] == 9, "H K count")
    require(hk_gate["selected_K_threshold_row_count_required"] == 10, "H K required")
    h_row = hk_gate["H_row"]
    require(h_row["A_EW_source_tier_gate_closed"] is True, "H row tier")
    require(h_row["external_AEW_diagnostic_postcheck_built"] is True, "H row diagnostic")
    for key in [
        "selected_A_EW_emitted",
        "selected_large_threshold_RG_theorem_emitted",
        "direct_intrinsic_H_quartic_K_row_emitted",
        "K_threshold_Omega_H_lambda_emitted",
    ]:
        require(h_row[key] is False, f"H row overclosed {key}")
    cons = hk_gate["conditional_consequent_current"]
    require(cons["ten_K_antecedent_satisfied"] is False, "ten K")
    require(cons["strict_Omega_lambda_scalar_execution_closed"] is False, "strict scalar")
    require(cons["lambda_H_row_executable"] is False, "lambda executable")
    require(cons["accepted_internal_scalar_value_row_count"] == 0, "internal scalar")

    require(
        cutset["status"]
        == "NEXT_FRONTIER_INTRINSIC_H_QUARTIC_K_ROW_OR_SELECTED_LARGE_THRESHOLD_RG_THEOREM",
        "cutset status",
    )
    require(cutset["next_required_artifact"] == NEXT, "cutset next")
    for phrase in [
        "A_EW source-tier separation theorem",
        "strict no-knob A_EW current-corpus no-go imported from A10/B41",
        "one-universal-primitive extension classified as ready but not selected",
        "external A_EW D-term diagnostic postcheck computed and quarantined as non-source",
        "plain external weak-coupling D-term replay rejected as H K closure",
    ]:
        require(phrase in cutset["closed_here"], f"cutset closed missing {phrase}")
    for phrase in [
        "selected A_EW=(g_2^2+g_Y^2)/8",
        "selected matching scale mu_match",
        "selected threshold/RG transport large enough for the Higgs lambda postcheck",
        "or direct intrinsic H quartic K_threshold.Omega_H.lambda row",
    ]:
        require(phrase in cutset["still_open"], f"cutset open missing {phrase}")

    for phrase in [
        "`A_EW=(g_2^2+g_Y^2)/8`",
        "`A_EW(M_t)=",
        "`A_EW(M_t)*s_beta=",
        "underprediction factor",
        NEXT,
    ]:
        require(phrase in note, f"note missing {phrase}")

    print(
        "AUDIT_PASS: A_EW tier gate closed; external D-term diagnostic rejects "
        "plain weak-coupling replay; direct H row or selected large threshold remains."
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
