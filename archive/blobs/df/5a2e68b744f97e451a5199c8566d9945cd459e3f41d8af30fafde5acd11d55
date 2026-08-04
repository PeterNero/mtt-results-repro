"""Audit selected F_Huv second-variation source or direct Herm(2) row payload."""

from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SLUG = "selected_fhuvsecondvariationsource_or_directherm2rowpayload"
BASE = ROOT / "candidate_data" / SLUG
CANDIDATE = ROOT / "candidate_data" / f"{SLUG}.candidate.json"
CERT = ROOT / "certificates" / f"{SLUG}_certificate.json"
NOTE = ROOT / "proof_corpus" / "MTT_Selected_FHuvSecondVariationSource_or_DirectHerm2RowPayload_v1.md"
BUILD = ROOT / "scripts" / f"build_{SLUG}.py"

RESTRICTION = BASE / "fhuv_second_variation_restriction_criterion.packet.json"
LOCAL_BRIDGE = BASE / "local_principle_to_fhuv_bridge_status.packet.json"
EXECUTION = BASE / "fhuv_restriction_matrix_row_execution.packet.json"
CUTSET = BASE / "next_cutset_after_fhuv_restriction_criterion.packet.json"

STATUS = (
    "MTT_SELECTED_FHUVSECONDVARIATIONSOURCE_OR_DIRECTHERM2ROWPAYLOAD_"
    "RESTRICTION_CRITERION_CLOSED_ROWS_OPEN"
)
NEXT = "MTT_Selected_FHuvRestrictionMatrixRows_or_BSelectedProjectionExecution_v1"
S_BETA = 0.004701083905943647


def load(path: Path):
    return json.loads(path.read_text(encoding="utf-8"))


def require(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)


def require_no_selector(packet: dict, label: str) -> None:
    require(packet.get("observed_data_used_as_selector") is False, f"{label}: observed selector")
    require(packet.get("target_fitting_used") is False, f"{label}: target fitting")


def main() -> int:
    proc = subprocess.run([sys.executable, str(BUILD)], cwd=ROOT, text=True, capture_output=True)
    if proc.returncode:
        print(proc.stdout)
        print(proc.stderr)
        return proc.returncode

    candidate = load(CANDIDATE)
    cert = load(CERT)
    restriction = load(RESTRICTION)
    local_bridge = load(LOCAL_BRIDGE)
    execution = load(EXECUTION)
    cutset = load(CUTSET)
    note = NOTE.read_text(encoding="utf-8")

    require(candidate["status"] == STATUS, "candidate status")
    require(candidate["next_required_artifact"] == NEXT, "candidate next")
    require(candidate["closure_claimed"] is True, "candidate closure")
    require(candidate["theorem"]["proved"] is True, "candidate theorem")
    require(candidate["minimal_parameter_tier_claimed"] is True, "minimal tier")
    require(candidate["true_SM_equivalence_claimed"] is False, "true SM overclaim")
    require(candidate["full_no_knob_closure_claimed"] is False, "no-knob overclaim")
    require_no_selector(candidate, "candidate")

    decision = candidate["closure_decision"]
    for key in [
        "F_Huv_restriction_criterion_closed",
        "B_Huv_R_H_domain_available",
        "Herm2_extraction_law_available",
        "local_premise_conditional_F_Huv_source_bridge_ready",
    ]:
        require(decision[key] is True, f"decision true {key}")
    for key in [
        "strict_unpatched_F_Huv_source_bridge_closed",
        "independent_quadrature_F_Huv_source_bridge_closed",
        "selected_C1_Hessian_matrix_rows_emitted",
        "B_selected_projection_execution_emitted",
        "selected_F_Huv_second_variation_emitted",
        "direct_Herm2_row_payload_emitted",
        "selected_H_response_table_emitted",
        "R_H_RG_value_emitted",
        "lambda_H_predicted",
        "true_SM_equivalence_closed",
        "full_no_knob_closed",
    ]:
        require(decision[key] is False, f"decision false {key}")

    nums = candidate["key_numbers"]
    require(abs(nums["selected_s_beta_value"] - S_BETA) < 1e-15, "s_beta")
    require(nums["ambient_selected_source_dimension"] == 27, "ambient dim")
    require(nums["Huv_restricted_dimension"] == 2, "restricted dim")
    require(nums["accepted_F_Huv_row_count"] == 0, "F rows")
    require(nums["accepted_direct_Herm2_row_count"] == 0, "direct rows")
    require(nums["accepted_certificate_count"] == 0, "cert rows")
    require(nums["accepted_non_diagonal_Huv_Hessian_source_count"] == 0, "Huv rows")

    require(cert["status"] == STATUS, "cert status")
    require(cert["next_required_artifact"] == NEXT, "cert next")
    require(cert["theorem_proved"] is True, "cert theorem")
    for key in [
        "F_Huv_restriction_criterion_closed",
        "B_Huv_R_H_domain_available",
        "Herm2_extraction_law_available",
        "local_premise_conditional_F_Huv_source_bridge_ready",
    ]:
        require(cert[key] is True, f"cert true {key}")
    for key in [
        "strict_unpatched_F_Huv_source_bridge_closed",
        "independent_quadrature_F_Huv_source_bridge_closed",
        "selected_C1_Hessian_matrix_rows_emitted",
        "B_selected_projection_execution_emitted",
        "selected_F_Huv_second_variation_emitted",
        "direct_Herm2_row_payload_emitted",
        "lambda_H_predicted",
        "true_SM_equivalence_claimed",
        "full_no_knob_closure_claimed",
        "observed_data_used_as_selector",
        "target_fitting_used",
    ]:
        require(cert[key] is False, f"cert false {key}")
    require(cert["accepted_F_Huv_row_count"] == 0, "cert F rows")
    require(cert["accepted_direct_Herm2_row_count"] == 0, "cert direct")
    require(cert["accepted_certificate_count"] == 0, "cert certs")

    require(restriction["status"] == "FHUV_RESTRICTION_CRITERION_CLOSED_MATRIX_ROWS_OPEN", "restriction status")
    domain = restriction["selected_domain"]
    require(domain["source_basis_dimension"] == 27, "domain dim")
    require(domain["B_Huv_symbolic_exact_payload_emitted"] is True, "B payload")
    require(domain["B_Huv_orthonormality"] == "B_Huv^* G_Q B_Huv = I_2", "orthonormality")
    require(domain["R_H_B_Huv_equals_I2"] is True, "RHB")
    source_def = restriction["source_functional_definition"]
    require(source_def["name"] == "F_Huv", "source name")
    require("F_Huv(z) = F_C1(B_Huv z)" in source_def["definition"], "definition")
    require("M_Huv = B_Huv^* Hess(F_C1)_selected B_Huv" in source_def["second_variation_rule"], "rule")
    require(source_def["trace_free_projection"] == "M_Huv^tf = M_Huv - (Tr M_Huv / 2) I_2", "trace-free")
    for req in [
        "selected finite C1/H-sector Hessian matrix or b_selected row source emitted before residual replay",
        "matrix restriction B_Huv^* Hess(F_C1)_selected B_Huv executed",
        "same-source exactness/error certificate attached",
    ]:
        require(req in restriction["strict_acceptance_requirements"], f"requirement {req}")
    rdec = restriction["decision"]
    for key in [
        "F_Huv_restriction_criterion_closed",
        "B_Huv_R_H_domain_available",
        "Herm2_extraction_law_available",
    ]:
        require(rdec[key] is True, f"restriction true {key}")
    for key in [
        "selected_C1_Hessian_matrix_rows_emitted",
        "B_selected_projection_execution_emitted",
        "selected_F_Huv_second_variation_emitted",
    ]:
        require(rdec[key] is False, f"restriction false {key}")
    require_no_selector(restriction, "restriction")

    require(local_bridge["status"] == "LOCAL_PRINCIPLE_CONDITIONAL_BRIDGE_READY_STRICT_SOURCE_OPEN", "local status")
    lp = local_bridge["local_principle"]
    require(lp["principle_name"] == "SelectedWeylVariationActionPrinciple", "principle")
    require(lp["local_pre_residual_kernel_closed"] is True, "local kernel")
    require(lp["unpatched_principle_derived_now"] is False, "unpatched")
    require(lp["independent_kernel_execution_supplied"] is False, "independent")
    guard = local_bridge["strict_no_knob_guard"]
    require(guard["minimal_action_theorem_proved_here"] is False, "minimal action proved")
    require(guard["minimal_action_must_not_be_used_as_free_patch"] is True, "free patch")
    require(guard["finite_c1_source_identity_inserted"] is False, "identity inserted")
    require(guard["conditional_validator_would_pass_if_inserted"] is True, "conditional")
    bdec = local_bridge["bridge_decision"]
    require(bdec["local_premise_conditional_F_Huv_source_bridge_ready"] is True, "local bridge")
    require(bdec["strict_unpatched_F_Huv_source_bridge_closed"] is False, "strict bridge")
    require(bdec["independent_quadrature_F_Huv_source_bridge_closed"] is False, "quad bridge")
    require(bdec["may_use_for_SM_parity_local_spine"] is True, "parity use")
    require(bdec["may_use_for_full_no_knob_closure"] is False, "no-knob use")
    require_no_selector(local_bridge, "local bridge")

    require(execution["status"] == "FHUV_RESTRICTION_MATRIX_EXECUTED_ZERO_ROWS", "execution status")
    requested = execution["requested_matrix"]
    require(requested["ambient_matrix"] == "Hess(F_C1)_selected on the 27-mode selected source basis", "ambient")
    require(requested["restriction"] == "M_Huv = B_Huv^* Hess(F_C1)_selected B_Huv", "restriction formula")
    for row in ["Huu", "Hud_re", "Hud_im", "Hdd", "Delta", "Re_Omega", "Im_Omega"]:
        require(row in requested["required_output_rows"], f"required output {row}")
        require(execution["emitted_rows"][row] is None, f"emitted row {row}")
    for cert_key in [
        "source_ownership_certificate",
        "same_source_exactness_or_error_certificate",
        "quotient_admissibility_certificate",
        "Hdu_equals_conj_Hud_certificate",
    ]:
        require(cert_key in requested["required_certificates"], f"required cert {cert_key}")
        require(execution["emitted_certificates"][cert_key] is None, f"emitted cert {cert_key}")
    current = execution["current_inputs"]
    require(current["B_Huv_symbolic_exact_payload_emitted"] is True, "current B")
    require(current["R_H_symbolic_exact_payload_emitted"] is True, "current R")
    for key in [
        "selected_C1_Hessian_or_b_selected_source_rows_emitted",
        "direct_Herm2_rows_emitted",
        "selected_H_response_table_emitted",
    ]:
        require(current[key] is False, f"current false {key}")
    edec = execution["decision"]
    require(edec["F_Huv_restriction_matrix_row_execution_attempted"] is True, "execution attempted")
    for key in ["selected_F_Huv_second_variation_emitted", "direct_Herm2_row_payload_emitted"]:
        require(edec[key] is False, f"execution false {key}")
    require(edec["accepted_F_Huv_row_count"] == 0, "execution F rows")
    require(edec["accepted_direct_Herm2_row_count"] == 0, "execution direct rows")
    require(edec["accepted_certificate_count"] == 0, "execution certs")
    require_no_selector(execution, "execution")

    require(cutset["status"] == "NEXT_FRONTIER_FHUV_RESTRICTION_MATRIX_ROWS_OR_BSELECTED_PROJECTION_EXECUTION", "cutset status")
    require(cutset["next_required_artifact"] == NEXT, "cutset next")
    for phrase in [
        "F_Huv as restriction of selected finite C1/Weyl second variation to B_Huv",
        "matrix formula M_Huv = B_Huv^* Hess(F_C1)_selected B_Huv",
        "local-premise bridge separated from strict no-knob bridge",
    ]:
        require(phrase in cutset["closed_here"], f"cutset closed {phrase}")
    for phrase in [
        "actual 27-mode selected Hess(F_C1) or b_selected row source entries",
        "B_Huv projection execution producing Huu,Hud,Hdd",
        "unpatched derivation or independent quadrature source for no-knob closure",
    ]:
        require(phrase in cutset["still_open"], f"cutset open {phrase}")
    require_no_selector(cutset, "cutset")

    for phrase in [
        "M_Huv = B_Huv^* Hess(F_C1)_selected B_Huv",
        "Accepted `F_Huv` rows: `0`",
        f"Selected `s_beta` retained as projection support: `{S_BETA}`",
        NEXT,
    ]:
        require(phrase in note, f"note missing {phrase}")

    print(
        "AUDIT_PASS: F_Huv restriction criterion is closed; local premise is "
        "separated from no-knob closure and zero F_Huv/direct Herm(2) rows are emitted."
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
