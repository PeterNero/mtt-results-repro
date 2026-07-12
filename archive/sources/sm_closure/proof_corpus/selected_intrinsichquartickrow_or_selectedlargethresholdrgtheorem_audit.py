"""Audit the intrinsic-H K row vs large-threshold/RG burden packet."""

from __future__ import annotations

import json
import math
import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SLUG = "selected_intrinsichquartickrow_or_selectedlargethresholdrgtheorem"
DATA = ROOT / "candidate_data" / f"{SLUG}.candidate.json"
PACKET_DIR = ROOT / "candidate_data" / SLUG
ROUTE_A = PACKET_DIR / "route_a_intrinsic_k4_current_underdetermination_import.packet.json"
ROUTE_B = PACKET_DIR / "route_b_large_threshold_rg_burden.packet.json"
THETA_TEST = PACKET_DIR / "theta_inverse_large_threshold_shortcut_test.packet.json"
ACCEPTANCE = PACKET_DIR / "selected_large_threshold_rg_acceptance_contract.packet.json"
HK_GATE = PACKET_DIR / "hk_threshold_gate_after_route_ab_burden.packet.json"
CUTSET = PACKET_DIR / "next_cutset_after_route_ab_burden.packet.json"
CERT = ROOT / "certificates" / f"{SLUG}_certificate.json"
NOTE = ROOT / "proof_corpus" / "MTT_Selected_IntrinsicHQuarticKRow_or_SelectedLargeThresholdRGTheorem_v1.md"
BUILDER = ROOT / "scripts" / f"build_{SLUG}.py"

STATUS = (
    "MTT_SELECTED_INTRINSICHQUARTICKROW_OR_SELECTEDLARGETHRESHOLDRGTHEOREM_"
    "ROUTE_A_PARKED_LARGE_THRESHOLD_BURDEN_CLOSED"
)
NEXT = "MTT_Selected_HThresholdRGOperatorOrUniversalPrimitivePolicy_v1"


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
    route_a = load(ROUTE_A)
    route_b = load(ROUTE_B)
    theta_test = load(THETA_TEST)
    acceptance = load(ACCEPTANCE)
    hk_gate = load(HK_GATE)
    cutset = load(CUTSET)
    cert = load(CERT)
    note = NOTE.read_text(encoding="utf-8")

    for label, packet in [
        ("candidate", data),
        ("route A", route_a),
        ("route B", route_b),
        ("theta test", theta_test),
        ("acceptance", acceptance),
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
        "route_A_current_material_underdetermined",
        "route_A_parked_pending_new_zero_mode_potential_theorem",
        "route_B_large_threshold_burden_computed",
        "minimal_no_additional_threshold_replay_rejected_for_H_postcheck",
        "theta_inverse_shortcut_rejected_as_selected_operator",
        "selected_large_threshold_RG_acceptance_contract_built",
    ]:
        require(decision[key] is True, f"decision should close {key}")
    for key in [
        "selected_A_EW_emitted",
        "selected_mu_match_emitted",
        "selected_H_threshold_RG_operator_emitted",
        "selected_large_threshold_RG_theorem_emitted",
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

    nums = data["diagnostic_numbers_not_source"]
    require(nums["required_R_H_RG_for_external_Mt_lambda_postcheck"] > 100, "required R too small")
    require(nums["log_required_R_H_RG"] > 5, "log R too small")
    require(nums["epsilon_theta_inverse"] > nums["required_R_H_RG_for_external_Mt_lambda_postcheck"], "theta inverse ordering")
    require(0 < nums["required_over_epsilon_theta_inverse"] < 1, "theta ratio")
    require(nums["lambda_if_R_equals_1"] < nums["external_lambda_Mt_coordinate"], "R=1 should fail")
    require(nums["lambda_if_R_equals_epsilon_theta_inverse"] > nums["external_lambda_Mt_coordinate"], "theta inverse diagnostic should overshoot")

    require(
        route_a["status"] == "ROUTE_A_CURRENT_INTRINSIC_K4_PARKED_PENDING_NEW_ZERO_MODE_POTENTIAL",
        "route A status",
    )
    under = route_a["underdetermination"]
    require(under["same_closed_data_different_K4"] is True, "route A countermodel")
    require(under["K4_unique_from_current_closed_data"] is False, "route A uniqueness")
    require(under["requires_extra_selected_source_rule"] is True, "route A extra source")
    require(
        under["does_not_deny_future_zero_mode_potential_theorem"] is True,
        "route A future theorem guard",
    )
    route_a_status = route_a["route_A_status_after_import"]
    require(route_a_status["intrinsic_K4_row_address_ready"] is True, "route A address")
    require(route_a_status["current_K4_derivation_underdetermined"] is True, "route A underdet")
    require(route_a_status["selected_analytic_zero_mode_potential_found"] is False, "route A potential")
    require(route_a_status["direct_intrinsic_H_quartic_K_row_emitted"] is False, "route A overclose")
    require(route_a["decision"]["park_current_route_A_as_proof_source"] is True, "route A parked")

    require(
        route_b["status"] == "ROUTE_B_SELECTED_LARGE_THRESHOLD_RG_BURDEN_EXACTLY_COMPUTED_NOT_SOURCE",
        "route B status",
    )
    post = route_b["external_postcheck_not_source"]
    require(
        math.isclose(
            post["required_threshold_multiplier_R_H_RG_to_match_external_lambda_Mt"],
            nums["required_R_H_RG_for_external_Mt_lambda_postcheck"],
            rel_tol=0,
            abs_tol=1e-12,
        ),
        "route B required R mismatch",
    )
    strict = route_b["strict_threshold_status_import"]
    require(strict["current_source_nogo_for_strict_vector"] is True, "strict vector no-go")
    require(strict["strict_threshold_vector_source_emitted"] is False, "strict vector overclose")
    require(strict["mathematical_impossibility_claimed"] is False, "strict vector impossible overclaim")
    minimal = route_b["minimal_threshold_policy_recheck"]
    require(minimal["minimal_threshold_replay_policy_closed"] is True, "minimal replay")
    require(minimal["allowed_as_strict_source_vector"] is False, "minimal strict overclose")
    require(minimal["multiplier_if_no_additional_H_threshold"] == 1.0, "minimal multiplier")
    require(minimal["passes_H_lambda_external_postcheck"] is False, "minimal should fail")
    decomp = route_b["threshold_vector_decomposition_import"]
    require(decomp["internal_weaksplit_prefix_closed"] is True, "internal prefix")
    require(decomp["flat_FP_extra_threshold_closed_zero"] is True, "flat FP")
    require(decomp["full_physical_threshold_vector_closed"] is False, "full vector overclose")
    require(route_b["selected_large_threshold_RG_theorem_emitted"] is False, "large threshold overclose")
    require(route_b["accepted_as_K_threshold_Omega_H_lambda_source"] is False, "K row overclose")

    require(
        theta_test["status"] == "THETA_INVERSE_LARGE_THRESHOLD_SHORTCUT_TESTED_NOT_SELECTED",
        "theta test status",
    )
    theta_decision = theta_test["decision"]
    require(theta_decision["theta_inverse_equals_required_multiplier"] is False, "theta equality")
    require(theta_decision["theta_inverse_promoted_as_H_threshold_RG_operator"] is False, "theta promoted")
    require(
        math.isclose(
            theta_test["diagnostic_comparison_not_source"]["required_threshold_multiplier"],
            nums["required_R_H_RG_for_external_Mt_lambda_postcheck"],
            rel_tol=0,
            abs_tol=1e-12,
        ),
        "theta required R mismatch",
    )

    require(
        acceptance["status"] == "SELECTED_H_THRESHOLD_RG_OPERATOR_ACCEPTANCE_CONTRACT_BUILT",
        "acceptance status",
    )
    required_equations = acceptance["required_equations"]
    require("lambda_H(mu_match)=A_EW(mu_match)*s_beta" in required_equations["boundary"], "boundary eq")
    require("R_H^RG" in required_equations["transported_postcheck"], "transport eq")
    require("K_threshold.Omega_H.lambda" in required_equations["omega_scheme"], "omega eq")
    current = acceptance["accepted_current_source_rows"]
    for key in [
        "selected_A_EW",
        "selected_mu_match",
        "selected_R_H_RG",
        "selected_K_threshold_Omega_H_lambda",
    ]:
        require(current[key] is False, f"acceptance overclosed {key}")

    require(
        hk_gate["status"] == "H_K_THRESHOLD_GATE_ROUTE_A_PARKED_ROUTE_B_OPERATOR_OPEN_9_OF_10",
        "H K status",
    )
    require(hk_gate["accepted_selected_K_source_row_count"] == 9, "H K count")
    require(hk_gate["selected_K_threshold_row_count_required"] == 10, "H K required")
    h_row = hk_gate["H_row"]
    for key in [
        "route_A_current_intrinsic_K4_derivation_underdetermined",
        "route_A_parked_pending_zero_mode_potential_theorem",
        "route_B_large_threshold_RG_burden_computed",
    ]:
        require(h_row[key] is True, f"H row should close {key}")
    for key in [
        "selected_large_threshold_RG_theorem_emitted",
        "selected_H_threshold_RG_operator_emitted",
        "theta_inverse_shortcut_promoted",
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
        cutset["status"] == "NEXT_FRONTIER_SELECTED_H_THRESHOLD_RG_OPERATOR_OR_EXPLICIT_PRIMITIVE_POLICY",
        "cutset status",
    )
    require(cutset["next_required_artifact"] == NEXT, "cutset next")
    for phrase in [
        "Route A current-material K4 underdetermination imported from constants H7A3",
        "Route B large-threshold/RG burden computed as an exact postcheck requirement",
        "theta inverse large-threshold shortcut tested and rejected as selected operator",
        "selected large-threshold/RG acceptance contract built",
    ]:
        require(phrase in cutset["closed_here"], f"cutset closed missing {phrase}")
    for phrase in [
        "selected H-sector threshold/RG operator R_H^RG",
        "selected A_EW or explicit admitted physical primitive tier",
        "selected K_threshold.Omega_H.lambda",
    ]:
        require(phrase in cutset["still_open"], f"cutset open missing {phrase}")

    for phrase in [
        "required `R_H^RG=",
        "selected `R_H^RG(mu_match -> M_t)`",
        "epsilon_Theta^-1",
        NEXT,
    ]:
        require(phrase in note, f"note missing {phrase}")

    print(
        "AUDIT_PASS: Route A current K4 source is parked by H7A3; "
        "Route B large-threshold/RG burden and acceptance contract are closed."
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
