"""Audit F_Huv restriction matrix rows or B-selected projection execution."""

from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SLUG = "selected_fhuvrestrictionmatrixrows_or_bselectedprojectionexecution"
BASE = ROOT / "candidate_data" / SLUG
CANDIDATE = ROOT / "candidate_data" / f"{SLUG}.candidate.json"
CERT = ROOT / "certificates" / f"{SLUG}_certificate.json"
NOTE = ROOT / "proof_corpus" / "MTT_Selected_FHuvRestrictionMatrixRows_or_BSelectedProjectionExecution_v1.md"
BUILD = ROOT / "scripts" / f"build_{SLUG}.py"

IMPORT = BASE / "selected_c1_hessian_payload_import.packet.json"
SHAPE = BASE / "bhuv_projection_shape_compatibility.packet.json"
EXECUTION = BASE / "bselected_projection_execution_attempt.packet.json"
CUTSET = BASE / "next_cutset_after_fhuv_projection_attempt.packet.json"

STATUS = (
    "MTT_SELECTED_FHUVRESTRICTIONMATRIXROWS_OR_BSELECTEDPROJECTIONEXECUTION_"
    "C1_PAYLOAD_IMPORTED_PROJECTION_TENSOR_OPEN"
)
NEXT = "MTT_Selected_C1ToBHuvProjectionTensor_or_FHuvRows_v1"
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
    imported = load(IMPORT)
    shape = load(SHAPE)
    execution = load(EXECUTION)
    cutset = load(CUTSET)
    note = NOTE.read_text(encoding="utf-8")

    require(candidate["status"] == STATUS, "candidate status")
    require(candidate["next_required_artifact"] == NEXT, "candidate next")
    require(candidate["closure_claimed"] is True, "candidate closure")
    require(candidate["theorem"]["proved"] is True, "candidate theorem")
    require(candidate["true_SM_equivalence_claimed"] is False, "true SM overclaim")
    require(candidate["full_no_knob_closure_claimed"] is False, "no-knob overclaim")
    require_no_selector(candidate, "candidate")

    decision = candidate["closure_decision"]
    for key in [
        "strict_dynamic_C1_payload_imported",
        "compressed_C1_Hessian_rows_available",
        "selected_b_selected_available",
        "B_selected_projection_execution_attempted",
        "shape_compatibility_checked",
        "naive_scalar_C1_normal_matrix_rejected_as_Huv",
    ]:
        require(decision[key] is True, f"decision true {key}")
    for key in [
        "ambient_27_mode_Hessian_matrix_emitted",
        "C1_to_BHuv_projection_tensor_emitted",
        "B_Huv_projection_execution_emitted",
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
    require(nums["compressed_C1_rank"] == 2, "rank")
    require(nums["A_transpose_A_trace"] == 24.0, "trace")
    require(nums["A_transpose_A_trace_free_norm"] == 0.0, "tf norm")
    require(nums["accepted_F_Huv_row_count"] == 0, "F rows")
    require(nums["accepted_certificate_count"] == 0, "cert rows")

    require(cert["status"] == STATUS, "cert status")
    require(cert["next_required_artifact"] == NEXT, "cert next")
    require(cert["theorem_proved"] is True, "cert theorem")
    for key in [
        "strict_dynamic_C1_payload_imported",
        "compressed_C1_Hessian_rows_available",
        "selected_b_selected_available",
        "B_selected_projection_execution_attempted",
        "shape_compatibility_checked",
        "naive_scalar_C1_normal_matrix_rejected_as_Huv",
    ]:
        require(cert[key] is True, f"cert true {key}")
    for key in [
        "ambient_27_mode_Hessian_matrix_emitted",
        "C1_to_BHuv_projection_tensor_emitted",
        "B_Huv_projection_execution_emitted",
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
    require(cert["accepted_certificate_count"] == 0, "cert certs")

    require(imported["status"] == "STRICT_DYNAMIC_C1_PAYLOAD_IMPORTED_COMPRESSED_COORDINATES_ONLY", "import status")
    src = imported["source_rule"]
    for key in [
        "source_rule_premise_free",
        "selected_dynamic_phi_fin_c1_payload_emitted",
        "b_selected_promoted_strict",
        "A_selected_promoted_strict",
        "deltaTheta_C1_promoted_strict",
        "unpatched_source_rule_proved_by_backimport",
    ]:
        require(src[key] is True, f"source rule {key}")
    compressed = imported["compressed_payload"]
    require(compressed["rank"] == 2, "compressed rank")
    require(compressed["A_transpose_A"] == [[12.0, 0.0], [0.0, 12.0]], "ATA")
    require(compressed["A_transpose_b"] == [12.0, 12.0], "ATb")
    require(compressed["hessian_b_source_rows"] == 2, "hessian rows")
    for key in [
        "ambient_27_by_27_Hess_F_C1_matrix",
        "B_Huv_restriction_tensor",
        "Higgs_specific_non_diagonal_Huv_block",
        "direct_Herm2_row_payload",
    ]:
        require(imported["not_imported_as"][key] is False, f"not imported {key}")
    idec = imported["decision"]
    for key in [
        "strict_dynamic_C1_payload_imported",
        "compressed_C1_Hessian_rows_available",
        "selected_b_selected_available",
    ]:
        require(idec[key] is True, f"import decision true {key}")
    for key in ["ambient_27_mode_Hessian_matrix_emitted", "B_Huv_projection_tensor_emitted"]:
        require(idec[key] is False, f"import decision false {key}")
    require_no_selector(imported, "import")

    require(shape["status"] == "BHUV_PROJECTION_SHAPE_CHECK_EXECUTED_TENSOR_OPEN", "shape status")
    domains = shape["available_domains"]
    require(domains["compressed_C1_variation_space_dimension"] == 2, "shape C1 dim")
    require(domains["B_Huv_column_count"] == 2, "shape Huv columns")
    require(domains["ambient_selected_source_dimension"] == 27, "shape ambient")
    require(domains["B_Huv_symbolic_exact_payload_emitted"] is True, "shape B")
    require(domains["R_H_symbolic_exact_payload_emitted"] is True, "shape R")
    need = shape["needed_for_F_Huv_rows"]
    require("T_C1<-Huv" in need["projection_tensor"], "projection tensor")
    require(need["or_full_matrix"] == "ambient 27x27 Hess(F_C1)_selected with B_Huv columns", "full matrix")
    obstruction = shape["shape_obstruction"]
    require(obstruction["A_transpose_A_shape"] == "2x2 compressed C1 normal matrix", "ATA shape")
    require(obstruction["B_Huv_shape"] == "27x2 symbolic source columns", "B shape")
    require("cannot be reinterpreted" in obstruction["why_A_transpose_A_is_not_enough"], "obstruction reason")
    sdec = shape["decision"]
    require(sdec["shape_compatibility_checked"] is True, "shape checked")
    require(sdec["dimension_counts_match_for_possible_2x2_restriction"] is True, "dim counts")
    require(sdec["projection_tensor_required"] is True, "tensor required")
    require(sdec["projection_tensor_emitted"] is False, "tensor emitted")
    require(sdec["ambient_27_by_27_Hessian_matrix_emitted"] is False, "ambient emitted")
    require_no_selector(shape, "shape")

    require(execution["status"] == "BSELECTED_PROJECTION_EXECUTION_ATTEMPTED_ZERO_HUV_ROWS", "execution status")
    available = execution["strict_available_payload"]
    require(available["A_transpose_A"] == [[12.0, 0.0], [0.0, 12.0]], "exec ATA")
    require(available["A_transpose_b"] == [12.0, 12.0], "exec ATb")
    guard = execution["naive_identification_guard"]
    require(guard["trace_free_part"] == [[0.0, 0.0], [0.0, 0.0]], "tf part")
    require(guard["trace_free_norm"] == 0.0, "tf norm exec")
    require(guard["would_emit_non_diagonal_Huv"] is False, "non diagonal")
    require("forbidden naive identification" in guard["decision"], "naive guard")
    legal = execution["legal_execution"]
    require(legal["M_Huv_formula"] == "M_Huv = B_Huv^* Hess(F_C1)_selected B_Huv", "legal formula")
    for key in [
        "ambient_matrix_available",
        "projection_tensor_available",
        "B_Huv_projection_execution_emitted",
        "direct_Herm2_rows_emitted",
    ]:
        require(legal[key] is False, f"legal false {key}")
    for value in execution["emitted_rows"].values():
        require(value is None, "row unexpectedly emitted")
    for value in execution["emitted_certificates"].values():
        require(value is None, "cert unexpectedly emitted")
    edec = execution["decision"]
    for key in [
        "B_selected_projection_execution_attempted",
        "selected_C1_Hessian_payload_imported",
        "naive_scalar_C1_normal_matrix_rejected_as_Huv",
    ]:
        require(edec[key] is True, f"execution true {key}")
    for key in ["selected_F_Huv_second_variation_emitted", "direct_Herm2_row_payload_emitted"]:
        require(edec[key] is False, f"execution false {key}")
    require(edec["accepted_F_Huv_row_count"] == 0, "execution F rows")
    require(edec["accepted_certificate_count"] == 0, "execution certs")
    require_no_selector(execution, "execution")

    require(cutset["status"] == "NEXT_FRONTIER_C1_TO_BHUV_PROJECTION_TENSOR_OR_FHUV_ROWS", "cutset status")
    require(cutset["next_required_artifact"] == NEXT, "cutset next")
    for phrase in [
        "strict dynamic C1 Hessian/b_selected payload imported into Huv frontier",
        "compressed C1 normal matrix separated from ambient 27x27 Hessian",
        "naive A^T A -> Huv promotion rejected as scalar and non-diagonal-zero",
    ]:
        require(phrase in cutset["closed_here"], f"cutset closed {phrase}")
    for phrase in [
        "source-owned C1 variation coordinate map for B_Huv columns",
        "or ambient 27x27 Hess(F_C1)_selected matrix entries",
        "C1-to-BHuv projection tensor certificate",
    ]:
        require(phrase in cutset["still_open"], f"cutset open {phrase}")
    require_no_selector(cutset, "cutset")

    for phrase in [
        "A^T A = [[12.0, 0.0], [0.0, 12.0]]",
        "scalar `12 I_2`, trace-free norm `0.0`",
        "Accepted `F_Huv` rows: `0`",
        NEXT,
    ]:
        require(phrase in note, f"note missing {phrase}")

    print(
        "AUDIT_PASS: strict C1 Hessian/b payload is imported; compressed A^T A "
        "is rejected as Huv and the C1-to-BHuv projection tensor remains open."
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
