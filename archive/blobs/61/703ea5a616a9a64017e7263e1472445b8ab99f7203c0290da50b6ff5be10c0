"""Audit non-diagonal Huv Hessian source or direct Herm(2) rows packet."""

from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SLUG = "selected_nondiagonalhuvhessiansource_or_directherm2rows"
BASE = ROOT / "candidate_data" / SLUG
CANDIDATE = ROOT / "candidate_data" / f"{SLUG}.candidate.json"
CERT = ROOT / "certificates" / f"{SLUG}_certificate.json"
NOTE = ROOT / "proof_corpus" / "MTT_Selected_NonDiagonalHuvHessianSource_or_DirectHerm2Rows_v1.md"
BUILD = ROOT / "scripts" / f"build_{SLUG}.py"

CONTRACT = BASE / "nondiagonal_huv_source_acceptance_contract.packet.json"
REJECTION = BASE / "candidate_source_rejection_matrix.packet.json"
DIRECT_RUN = BASE / "direct_herm2_row_payload_run.packet.json"
CUTSET = BASE / "next_cutset_after_nondiagonal_huv_source_attempt.packet.json"

STATUS = (
    "MTT_SELECTED_NONDIAGONALHUVHESSIANSOURCE_OR_DIRECTHERM2ROWS_"
    "CANDIDATES_REJECTED_SOURCE_FUNCTIONAL_OPEN"
)
NEXT = "MTT_Selected_FHuvSecondVariationSource_or_DirectHerm2RowPayload_v1"
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
    contract = load(CONTRACT)
    rejection = load(REJECTION)
    direct = load(DIRECT_RUN)
    cutset = load(CUTSET)
    note = NOTE.read_text(encoding="utf-8")

    require(candidate["status"] == STATUS, "candidate status")
    require(candidate["next_required_artifact"] == NEXT, "candidate next")
    require(candidate["closure_claimed"] is True, "candidate closure")
    require(candidate["minimal_parameter_tier_claimed"] is True, "minimal tier")
    require(candidate["true_SM_equivalence_claimed"] is False, "true SM overclaim")
    require(candidate["full_no_knob_closure_claimed"] is False, "no-knob overclaim")
    require(candidate["theorem"]["proved"] is True, "candidate theorem")
    require_no_selector(candidate, "candidate")

    decision = candidate["closure_decision"]
    for key in [
        "non_diagonal_Huv_source_acceptance_contract_closed",
        "candidate_source_rejection_matrix_executed",
        "direct_Herm2_row_payload_run_executed",
        "diagonal_metric_retired_as_non_diagonal_Hessian_source",
        "projection_bridge_retired_as_direct_value_route",
        "matter_operator_blocks_retired_as_Huv_value_route",
        "source_promotion_guard_closed",
    ]:
        require(decision[key] is True, f"decision true {key}")
    for key in [
        "selected_non_diagonal_Huv_Hessian_source_emitted",
        "selected_F_H_second_variation_emitted",
        "selected_Hermitian_M_source_emitted",
        "M_source_plus_R_H_values_emitted",
        "direct_Herm2_rows_emitted",
        "selected_H_response_table_emitted",
        "selected_H_response_spectrum_emitted",
        "R_H_RG_value_emitted",
        "lambda_H_predicted",
        "true_SM_equivalence_closed",
        "full_no_knob_closed",
    ]:
        require(decision[key] is False, f"decision false {key}")

    nums = candidate["key_numbers"]
    require(abs(nums["selected_s_beta_value"] - S_BETA) < 1e-15, "s_beta")
    require(nums["accepted_non_diagonal_Huv_Hessian_source_count"] == 0, "accepted Huv")
    require(nums["accepted_direct_Herm2_row_payload_count"] == 0, "accepted direct")
    require(nums["accepted_H_response_source_row_count"] == 0, "accepted H rows")
    require(nums["accepted_R_H_RG_source_count"] == 0, "accepted RHRG")
    require(nums["required_H_response_row_count"] == 7, "required H rows")
    require(nums["emitted_H_response_row_count"] == 0, "emitted H rows")
    require(nums["accepted_selected_K_source_row_count"] == 9, "K rows")
    require(nums["selected_K_threshold_row_count_required"] == 10, "K required")

    require(cert["status"] == STATUS, "cert status")
    require(cert["next_required_artifact"] == NEXT, "cert next")
    require(cert["theorem_proved"] is True, "cert theorem")
    require(cert["minimal_parameter_tier_claimed"] is True, "cert minimal")
    for key in [
        "non_diagonal_Huv_source_acceptance_contract_closed",
        "candidate_source_rejection_matrix_executed",
        "direct_Herm2_row_payload_run_executed",
        "diagonal_metric_retired_as_non_diagonal_Hessian_source",
        "projection_bridge_retired_as_direct_value_route",
        "matter_operator_blocks_retired_as_Huv_value_route",
        "source_promotion_guard_closed",
    ]:
        require(cert[key] is True, f"cert true {key}")
    for key in [
        "selected_non_diagonal_Huv_Hessian_source_emitted",
        "selected_F_H_second_variation_emitted",
        "selected_Hermitian_M_source_emitted",
        "M_source_plus_R_H_values_emitted",
        "direct_Herm2_rows_emitted",
        "R_H_RG_value_emitted",
        "lambda_H_predicted",
        "true_SM_equivalence_claimed",
        "full_no_knob_closure_claimed",
        "observed_data_used_as_selector",
        "target_fitting_used",
    ]:
        require(cert[key] is False, f"cert false {key}")
    require(cert["accepted_non_diagonal_Huv_Hessian_source_count"] == 0, "cert Huv")
    require(cert["accepted_direct_Herm2_row_payload_count"] == 0, "cert direct")

    require(contract["status"] == "NONDIAGONAL_HUV_SOURCE_ACCEPTANCE_CONTRACT_CLOSED", "contract status")
    require(contract["domain"]["orthonormality"] == "B_Huv^* G_Q B_Huv = I_2", "orthonormality")
    require("Omega != 0" in contract["domain"]["non_diagonal_requirement"], "non-diagonal condition")
    routes = contract["accepted_source_routes"]
    require(routes["selected_F_H_second_variation"]["current_emitted"] is False, "F_H emitted")
    require(routes["selected_M_source_plus_R_H"]["current_emitted"] is False, "M route emitted")
    require(routes["direct_Herm2_rows"]["current_emitted"] is False, "direct route emitted")
    for forbidden in [
        "C1-C6 projection bridge alone",
        "diagonal HYM metric or G_Q kinematic metric alone",
        "matter/neutrino operator blocks without a Higgs Huv block",
        "trace-free polar reconstruction law without r_H/sign/phase/source rows",
        "controlled HRG calibration lane as strict no-knob value source",
    ]:
        require(forbidden in contract["forbidden_promotions"], f"forbidden {forbidden}")
    for key in [
        "non_diagonal_Huv_source_acceptance_contract_closed",
        "B_Huv_domain_closed",
        "Herm2_tracefree_row_functional_closed",
        "source_promotion_guard_closed",
    ]:
        require(contract["decision"][key] is True, f"contract decision {key}")
    require_no_selector(contract, "contract")

    require(rejection["status"] == "CANDIDATE_SOURCE_REJECTION_MATRIX_EXECUTED_ZERO_ACCEPTED", "rejection status")
    rows = rejection["rows"]
    require(len(rows) == 6, "rejection row count")
    ids = {row["candidate_id"] for row in rows}
    for expected in [
        "diagonal_HYM_metric_connection_C3",
        "C1_C6_projection_bridge",
        "H7B1Q_matter_same_source_operator_blocks",
        "full_M_source_plus_R_H_route",
        "direct_H_response_rows",
        "tracefree_polar_contract",
    ]:
        require(expected in ids, f"missing rejection row {expected}")
    for row in rows:
        require(row["accepted_as_non_diagonal_Huv_source"] is False, f"row accepted {row['candidate_id']}")
        require(row["rejection_reason"], f"missing reason {row['candidate_id']}")
        require(row["blocker_fields"], f"missing blockers {row['candidate_id']}")
    rdec = rejection["decision"]
    require(rdec["candidate_source_rejection_matrix_executed"] is True, "matrix executed")
    require(rdec["accepted_non_diagonal_Huv_Hessian_source_count"] == 0, "matrix accepted")
    require(rdec["accepted_direct_Herm2_row_payload_count"] == 0, "matrix direct")
    for key in [
        "diagonal_metric_retired_as_non_diagonal_Hessian_source",
        "projection_bridge_retired_as_direct_value_route",
        "matter_operator_blocks_retired_as_Huv_value_route",
        "full_M_source_route_formula_only_values_open",
    ]:
        require(rdec[key] is True, f"matrix decision {key}")
    require_no_selector(rejection, "rejection")

    require(direct["status"] == "DIRECT_HERM2_ROW_PAYLOAD_RUN_EXECUTED_ZERO_ROWS", "direct status")
    for key in [
        "Delta",
        "Re_Omega",
        "Im_Omega",
        "Huu",
        "Hud_re",
        "Hud_im",
        "Hdd",
        "source_ownership_certificate",
        "same_source_exactness_or_error_certificate",
        "quotient_admissibility_certificate",
    ]:
        require(key in direct["required_rows"], f"required row {key}")
        require(direct["required_rows"][key] is None, f"unexpected row {key}")
    for value in direct["prior_required_table"].values():
        require(value is None, "prior required unexpectedly filled")
    for value in direct["prior_values_emitted_now"].values():
        require(value is None, "prior value unexpectedly emitted")
    table = direct["hresponse_table_status"]
    require(table["required_row_count"] == 7, "table required")
    require(table["emitted_row_count"] == 0, "table emitted")
    require(table["accepted_source_row_count"] == 0, "table accepted")
    ddec = direct["decision"]
    require(ddec["direct_Herm2_row_payload_run_executed"] is True, "direct executed")
    for key in [
        "selected_non_diagonal_Huv_Hessian_source_emitted",
        "selected_F_H_second_variation_emitted",
        "selected_Hermitian_M_source_emitted",
        "M_source_plus_R_H_values_emitted",
        "direct_Herm2_rows_emitted",
        "selected_H_response_table_emitted",
        "selected_H_response_spectrum_emitted",
        "R_H_RG_value_emitted",
        "lambda_H_predicted",
    ]:
        require(ddec[key] is False, f"direct false {key}")
    require_no_selector(direct, "direct")

    require(cutset["status"] == "NEXT_FRONTIER_FHUV_SECOND_VARIATION_SOURCE_OR_DIRECT_HERM2_ROW_PAYLOAD", "cutset status")
    require(cutset["next_required_artifact"] == NEXT, "cutset next")
    for phrase in [
        "non-diagonal Huv source acceptance contract",
        "source-promotion guard against diagonal/projection/matter shortcuts",
        "candidate source rejection matrix across current strongest packets",
        "direct Herm(2) row payload run with zero emitted rows",
    ]:
        require(phrase in cutset["closed_here"], f"cutset closed {phrase}")
    for phrase in [
        "selected finite F_Huv second-variation source row",
        "nonzero Omega row or equivalent off-diagonal Huv row",
        "same-source exactness/error certificate for the Huv Hessian",
        "selected M_source+R_H numeric values or direct Huu/Hud/Hdd values",
    ]:
        require(phrase in cutset["still_open"], f"cutset open {phrase}")
    require_no_selector(cutset, "cutset")

    for phrase in [
        "a non-diagonal Higgs",
        "Accepted non-diagonal Huv Hessian sources: `0`",
        f"`s_beta = {S_BETA}`",
        NEXT,
    ]:
        require(phrase in note, f"note missing {phrase}")

    print(
        "AUDIT_PASS: non-diagonal Huv source contract is closed; all current "
        "shortcut candidates are rejected and zero direct Herm(2) rows are emitted."
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
