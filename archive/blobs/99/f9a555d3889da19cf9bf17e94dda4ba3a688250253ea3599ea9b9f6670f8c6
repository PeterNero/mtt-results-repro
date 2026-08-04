"""Audit E_H^UV C1 variation operators or ambient Hessian restriction rows packet."""

from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SLUG = "selected_ehuvc1variationoperators_or_ambienthessianrestrictionrows"
BASE = ROOT / "candidate_data" / SLUG
CANDIDATE = ROOT / "candidate_data" / f"{SLUG}.candidate.json"
CERT = ROOT / "certificates" / f"{SLUG}_certificate.json"
NOTE = ROOT / "proof_corpus" / "MTT_Selected_EHUvC1VariationOperators_or_AmbientHessianRestrictionRows_v1.md"
BUILD = ROOT / "scripts" / f"build_{SLUG}.py"

C1_IMPORT = BASE / "active_c1_source_to_higgs_frontier_import.packet.json"
H7B1M_IMPORT = BASE / "h7b1m_projection_route_supersession.packet.json"
EVALUATION_ATTEMPT = BASE / "ehuv_operator_evaluation_attempt.packet.json"
RESTRICTION_ATTEMPT = BASE / "ambient_hessian_restriction_rows_attempt.packet.json"
CUTSET = BASE / "next_cutset_after_ehuv_c1_operator_attempt.packet.json"

STATUS = (
    "MTT_SELECTED_EHUVC1VARIATIONOPERATORS_OR_AMBIENTHESSIANRESTRICTIONROWS_"
    "C1_SOURCE_IMPORTED_HSECTOR_EXTENSION_OPEN"
)
NEXT = "MTT_Selected_HSectorDynamicC1Extension_or_DirectHuvRows_v1"


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
    c1_import = load(C1_IMPORT)
    h7b1m_import = load(H7B1M_IMPORT)
    evaluation = load(EVALUATION_ATTEMPT)
    restriction = load(RESTRICTION_ATTEMPT)
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
        "active_C1_source_imported",
        "stale_C1_source_promotion_blocker_retired",
        "plain_matter_C1_to_Huv_projection_retired",
        "E_HUV_C1_operator_evaluation_attempted",
        "ambient_Hessian_restriction_rows_attempted",
    ]:
        require(decision[key] is True, f"decision true {key}")
    for key in [
        "selected_E_HUV_C1_variation_operator_rows_emitted",
        "source_owned_T_C1_EHuv_emitted",
        "selected_Higgs_C1_variation_slots_emitted",
        "ambient_27_by_27_Hessian_matrix_emitted",
        "ambient_Hessian_restriction_rows_emitted",
        "selected_F_Huv_rows_emitted",
        "direct_Herm2_row_payload_emitted",
        "true_SM_equivalence_closed",
        "full_no_knob_closed",
    ]:
        require(decision[key] is False, f"decision false {key}")

    nums = candidate["key_numbers"]
    require(nums["C1_target_row_count"] == 72, "row count")
    require(nums["C1_target_sector_count"] == 4, "sector count")
    require(nums["C1_higgs_slot_rows_found"] == 0, "Higgs rows")
    require(nums["phase_R_Z_matrix_shape"] == [3, 3], "phase shape")
    require(nums["shift_R_X_matrix_shape"] == [3, 3], "shift shape")
    require(nums["A_transpose_A"] == [[12.0, 0.0], [0.0, 12.0]], "ATA")
    require(nums["required_minimum_Higgs_C1_variation_slot_count"] == 4, "required slots")
    require(nums["selected_Higgs_C1_variation_slot_count"] == 0, "selected slots")
    require(nums["accepted_F_Huv_row_count"] == 0, "F rows")
    require(nums["accepted_certificate_count"] == 0, "cert rows")

    require(cert["status"] == STATUS, "cert status")
    require(cert["next_required_artifact"] == NEXT, "cert next")
    require(cert["theorem_proved"] is True, "cert theorem")
    for key in [
        "active_C1_source_imported",
        "stale_C1_source_promotion_blocker_retired",
        "plain_matter_C1_to_Huv_projection_retired",
        "E_HUV_C1_operator_evaluation_attempted",
        "ambient_Hessian_restriction_rows_attempted",
    ]:
        require(cert[key] is True, f"cert true {key}")
    for key in [
        "true_SM_equivalence_claimed",
        "full_no_knob_closure_claimed",
        "observed_data_used_as_selector",
        "target_fitting_used",
        "selected_E_HUV_C1_variation_operator_rows_emitted",
        "source_owned_T_C1_EHuv_emitted",
        "selected_Higgs_C1_variation_slots_emitted",
        "ambient_27_by_27_Hessian_matrix_emitted",
        "ambient_Hessian_restriction_rows_emitted",
        "selected_F_Huv_rows_emitted",
        "direct_Herm2_row_payload_emitted",
    ]:
        require(cert[key] is False, f"cert false {key}")

    require(c1_import["status"] == "ACTIVE_DYNAMIC_C1_SOURCE_IMPORTED_FOR_HIGGS_FRONTIER", "c1 import")
    closed = c1_import["what_is_now_closed"]
    for key in [
        "strict_unpatched_dynamic_C1_closed",
        "selected_dynamic_phi_fin_c1_payload_emitted",
        "A_selected_promoted_strict",
        "b_selected_promoted_strict",
        "deltaTheta_C1_promoted_strict",
        "sector_response_matrices_promoted_strict",
        "source_rule_premise_free",
        "emitted_before_residual_replay",
    ]:
        require(closed[key] is True, f"c1 closed {key}")
    exact = c1_import["exact_dynamic_C1_values"]
    require(exact["phase_R_Z_shape"] == [3, 3], "c1 phase")
    require(exact["shift_R_X_shape"] == [3, 3], "c1 shift")
    require(exact["A_transpose_A"] == [[12.0, 0.0], [0.0, 12.0]], "c1 ATA")
    require(c1_import["higgs_relevance"]["C1_source_ownership_is_no_longer_the_Huv_blocker"] is True, "c1 relevance")
    require(c1_import["decision"]["active_C1_source_imported"] is True, "c1 active")
    require(c1_import["decision"]["stale_dynamic_C1_source_open_gate_retired"] is True, "c1 stale")
    require_no_selector(c1_import, "c1 import")

    require(
        h7b1m_import["status"] == "H7B1M_ROUTE_IMPORTED_DYNAMIC_SOURCE_UPDATED_TARGET_MISMATCH_STILL_LIVE",
        "h7b1m status",
    )
    route = h7b1m_import["imported_route_decision"]
    require(route["plain_C1_to_Huv_projection_route_passes"] is False, "plain route")
    require(route["plain_C1_to_Huv_projection_route_retired_current_target"] is True, "route retired")
    require(route["H_sector_dynamic_C1_extension_required"] is True, "H extension")
    require(route["honest_Huv_row_export_still_live"] is True, "direct Huv live")
    require(route["current_C1_target_sector_set"] == ["d", "e", "nuD", "u"], "sector set")
    require(route["current_C1_target_contains_H_sector"] is False, "H sector")
    superseded = h7b1m_import["superseded_h7b1m_clause"]
    require(superseded["superseded_by_active_ledger"] is True, "superseded")
    require("target has no H-sector codomain" in superseded["replacement"], "replacement")
    require(h7b1m_import["decision"]["plain_matter_C1_to_Huv_projection_retired"] is True, "plain retired")
    require_no_selector(h7b1m_import, "h7b1m")

    require(evaluation["status"] == "EHUV_C1_OPERATOR_EVALUATION_ATTEMPTED_ZERO_SELECTED_VALUES", "eval status")
    available = evaluation["available_inputs"]
    require(available["selected_phase_R_Z_matrix_shape"] == [3, 3], "eval phase")
    require(available["selected_shift_R_X_matrix_shape"] == [3, 3], "eval shift")
    require(available["higgs_source_labels"] == ["H_u", "H_d^dagger"], "eval labels")
    require(available["B_Huv_symbolic_exact_payload_emitted"] is True, "eval B")
    require(available["C1_target_sectors"] == ["d", "e", "nuD", "u"], "eval sectors")
    require(available["C1_higgs_slot_rows_found"] == 0, "eval H rows")
    req = evaluation["required_map"]
    require(req["name"] == "Eval_EHuv_C1", "eval map name")
    require("T_C1<-E_H^UV" in req["if_emitted"], "eval T")
    require(req["then_execute"] == "M_Huv = 12 T^*T", "eval formula")
    for route_name, data in evaluation["candidate_evaluations_rejected"].items():
        require(data["accepted"] is False, f"eval rejected {route_name}")
        require(data["reason"], f"eval reason {route_name}")
    require(evaluation["emitted_T_C1_EHuv"] is None, "eval T emitted")
    for value in evaluation["emitted_slot_values"].values():
        require(value is None, "eval slot emitted")
    edec = evaluation["decision"]
    require(edec["E_HUV_C1_operator_evaluation_attempted"] is True, "eval attempted")
    require(edec["selected_E_HUV_C1_variation_operator_rows_emitted"] is False, "eval rows")
    require(edec["source_owned_T_C1_EHuv_emitted"] is False, "eval T false")
    require(edec["selected_Higgs_C1_variation_slot_count"] == 0, "eval slot count")
    require_no_selector(evaluation, "evaluation")

    require(
        restriction["status"] == "AMBIENT_HESSIAN_RESTRICTION_ROWS_ATTEMPTED_ZERO_ROWS_AFTER_C1_IMPORT",
        "restriction status",
    )
    support = restriction["available_support"]
    require(support["active_C1_normal_matrix"] == [[12.0, 0.0], [0.0, 12.0]], "restriction ATA")
    require(support["H7B1L_gap_status"] == "HUV_PROJECTION_RESTRICTION_FUNCTOR_NOT_EMITTED", "restriction gap")
    require(restriction["emitted_ambient_rows"] is None, "ambient emitted")
    for value in restriction["emitted_restriction_rows"].values():
        require(value is None, "restriction row emitted")
    rdec = restriction["decision"]
    require(rdec["ambient_Hessian_restriction_rows_attempted"] is True, "restriction attempted")
    for key in [
        "ambient_27_by_27_Hessian_matrix_emitted",
        "ambient_Hessian_restriction_rows_emitted",
        "selected_F_Huv_rows_emitted",
        "direct_Herm2_row_payload_emitted",
    ]:
        require(rdec[key] is False, f"restriction false {key}")
    require(rdec["accepted_F_Huv_row_count"] == 0, "restriction F rows")
    require(rdec["accepted_certificate_count"] == 0, "restriction certs")
    require_no_selector(restriction, "restriction")

    require(cutset["status"] == "NEXT_FRONTIER_HSECTOR_DYNAMIC_C1_EXTENSION_OR_DIRECT_HUV_ROWS", "cutset status")
    require(cutset["next_required_artifact"] == NEXT, "cutset next")
    for phrase in [
        "active strict dynamic Phi_fin/C1 source import into the Higgs frontier",
        "retirement of stale C1 source-promotion/Galerkin blocker for this branch",
        "proof that the missing object is Eval_EHuv_C1 or direct Huv rows",
    ]:
        require(phrase in cutset["closed_here"], f"closed {phrase}")
    for phrase in [
        "selected H-sector dynamic C1 extension containing H/H_u/H_d^dagger coordinates",
        "selected Eval_EHuv_C1 map from H_u,H_d^dagger to phase_R_Z/shift_R_X",
        "or direct source-owned Huu,Hud,Hdd rows on B_Huv",
    ]:
        require(phrase in cutset["still_open"], f"open {phrase}")
    require_no_selector(cutset, "cutset")

    for phrase in [
        "phase_R_Z shape = [3, 3]",
        "M_Huv = 12 T^*T",
        "Current C1 H/Huv rows: `0`",
        "Selected `T_C1<-E_H^UV` rows emitted: `0`",
        NEXT,
    ]:
        require(phrase in note, f"note missing {phrase}")

    print(
        "AUDIT_PASS: active C1 source rows are imported; Huv now requires "
        "Eval_EHuv_C1/H-sector extension or direct Huv rows."
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
