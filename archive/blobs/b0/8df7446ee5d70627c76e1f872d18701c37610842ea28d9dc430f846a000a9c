"""Audit R_H^RG determinant/index candidate or external validation target packet."""

from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SLUG = "selected_rhrgdeterminantindexcandidate_or_externalvalidationtarget"
BASE = ROOT / "candidate_data" / SLUG
CANDIDATE = ROOT / "candidate_data" / f"{SLUG}.candidate.json"
CERT = ROOT / "certificates" / f"{SLUG}_certificate.json"
NOTE = ROOT / "proof_corpus" / "MTT_Selected_RHRGDeterminantIndexCandidate_or_ExternalValidationTarget_v1.md"
BUILD = ROOT / "scripts" / f"build_{SLUG}.py"

DET_MATRIX = BASE / "rhrg_determinant_index_candidate_matrix.packet.json"
HIGGS_BINDING = BASE / "higgs_projection_binding_to_rhrg_contract.packet.json"
VALIDATION_TARGET = BASE / "external_validation_target_manifest.packet.json"
CUTSET = BASE / "next_cutset_after_rhrg_candidate_matrix.packet.json"

STATUS = (
    "MTT_SELECTED_RHRGDETERMINANTINDEXCANDIDATE_OR_EXTERNALVALIDATIONTARGET_"
    "MATRIX_BUILT_ZERO_ACCEPTED_CANDIDATES"
)
NEXT = "MTT_Selected_HSectorDeterminantRGOperatorDefinition_or_TargetIndependentValidationRun_v1"
HRG = 391.39140285811936
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
    det = load(DET_MATRIX)
    binding = load(HIGGS_BINDING)
    validation = load(VALIDATION_TARGET)
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
    require(decision["higgs_projection_binding_closed"] is True, "binding not closed")
    require(decision["selected_s_beta_available"] is True, "s_beta unavailable")
    for key in [
        "determinant_index_candidate_accepted",
        "threshold_RG_R_H_RG_selected",
        "external_validation_target_imported",
        "strict_R_H_RG_source_constructed",
        "lambda_H_predicted",
        "true_SM_equivalence_closed",
        "full_no_knob_closed",
    ]:
        require(decision[key] is False, f"decision false {key}")
    require(decision["accepted_R_H_RG_candidate_count"] == 0, "accepted R_H count")

    nums = candidate["key_numbers"]
    require(abs(nums["UP_RET_OVERLAP_HRG"] - HRG) < 1e-12, "HRG")
    require(abs(nums["selected_s_beta_value"] - S_BETA) < 1e-18, "s_beta")
    require(nums["tested_determinant_index_candidate_count"] == 3, "tested count")
    require(nums["accepted_R_H_RG_candidate_count"] == 0, "accepted count")
    require(nums["accepted_external_validation_target_count"] == 0, "external count")
    require(nums["accepted_selected_K_source_row_count"] == 9, "K count")
    require(nums["selected_K_threshold_row_count_required"] == 10, "K required")

    require(cert["status"] == STATUS, "cert status")
    require(cert["next_required_artifact"] == NEXT, "cert next")
    require(cert["theorem_proved"] is True, "cert theorem")
    require(cert["higgs_projection_binding_closed"] is True, "cert binding")
    require(cert["selected_s_beta_available"] is True, "cert s_beta")
    for key in [
        "determinant_index_candidate_accepted",
        "threshold_RG_R_H_RG_selected",
        "external_validation_target_imported",
        "strict_R_H_RG_source_constructed",
        "lambda_H_predicted",
        "true_SM_equivalence_claimed",
        "full_no_knob_closure_claimed",
        "observed_data_used_as_selector",
        "target_fitting_used",
    ]:
        require(cert[key] is False, f"cert false {key}")
    require(cert["accepted_R_H_RG_candidate_count"] == 0, "cert accepted")

    require(det["status"] == "RHRG_DETERMINANT_INDEX_CANDIDATES_TESTED_ZERO_ACCEPTED", "det status")
    require(det["decision"]["tested_candidate_count"] == 3, "det count")
    require(det["decision"]["accepted_R_H_RG_candidate_count"] == 0, "det accepted")
    require(det["decision"]["determinant_index_candidate_accepted"] is False, "det accepted bool")
    require(det["decision"]["external_validation_target_imported"] is False, "det external")
    require(det["decision"]["strict_R_H_RG_source_constructed"] is False, "det strict")
    for row in det["candidate_rows"]:
        require(row["accepted_for_R_H_RG"] is False, f"det row accepted {row['candidate']}")
    require_no_selector(det, "det")

    require(
        binding["status"] == "HIGGS_PROJECTION_DATA_BOUND_TO_RHRG_CONTRACT_BUT_RG_OPERATOR_OPEN",
        "binding status",
    )
    require(binding["closed_higgs_inputs"]["C5b_projection_measure_equality_closed"] is True, "C5b")
    require(binding["closed_higgs_inputs"]["C6_no_boundary_closed"] is True, "C6")
    require(binding["closed_higgs_inputs"]["selected_s_beta_value_found"] is True, "s_beta found")
    require(abs(binding["closed_higgs_inputs"]["selected_s_beta_value"] - S_BETA) < 1e-18, "binding s_beta")
    require(binding["name_collision_guard"]["kinematic_R_H_is_selected_or_partly_selected"] is True, "kinematic R_H")
    require(binding["name_collision_guard"]["threshold_RG_R_H_RG_selected"] is False, "threshold R_H")
    require(binding["name_collision_guard"]["may_identify_R_H_with_R_H_RG"] is False, "name collision")
    for value in binding["still_open_for_R_H_RG"].values():
        require(value is False, "binding overclosed")
    require_no_selector(binding, "binding")

    require(validation["status"] == "EXTERNAL_VALIDATION_TARGETS_DECLARED_NONE_IMPORTED", "validation status")
    require(validation["accepted_external_validation_target_count"] == 0, "validation count")
    require("lambda_H(M_t)" in validation["forbidden_as_selector"], "lambda guard")
    require_no_selector(validation, "validation")

    require(
        cutset["status"]
        == "NEXT_FRONTIER_HSECTOR_DETERMINANT_RG_OPERATOR_DEFINITION_OR_TARGET_INDEPENDENT_VALIDATION_RUN",
        "cutset status",
    )
    require(cutset["next_required_artifact"] == NEXT, "cutset next")
    require("determinant/torsion candidates tested against the R_H^RG acceptance contract" in cutset["closed_here"], "cutset closed")
    require("define selected H-sector determinant/RG operator whose zeta determinant, torsion, or index emits R_H^RG" in cutset["still_open"], "cutset open")
    require_no_selector(cutset, "cutset")

    for phrase in [
        "accepted `R_H^RG` candidates: `0`",
        "selected `s_beta` available: `true`",
        "kinematic H-sector `R_H` kept distinct",
        NEXT,
    ]:
        require(phrase in note, f"note missing {phrase}")

    print(
        "AUDIT_PASS: R_H^RG determinant/index candidates tested; Higgs projection binding is useful, "
        "but zero strict candidates or external validation targets are accepted."
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
