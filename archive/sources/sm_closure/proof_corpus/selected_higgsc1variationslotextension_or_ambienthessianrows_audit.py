"""Audit Higgs C1 variation-slot extension or ambient Hessian rows packet."""

from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SLUG = "selected_higgsc1variationslotextension_or_ambienthessianrows"
BASE = ROOT / "candidate_data" / SLUG
CANDIDATE = ROOT / "candidate_data" / f"{SLUG}.candidate.json"
CERT = ROOT / "certificates" / f"{SLUG}_certificate.json"
NOTE = ROOT / "proof_corpus" / "MTT_Selected_HiggsC1VariationSlotExtension_or_AmbientHessianRows_v1.md"
BUILD = ROOT / "scripts" / f"build_{SLUG}.py"

SLOT_CONTRACT = BASE / "higgs_c1_variation_slot_extension_contract.packet.json"
HESSIAN_CONTRACT = BASE / "ambient_hessian_restriction_row_contract.packet.json"
SLOT_ATTEMPT = BASE / "higgs_c1_slot_extension_execution_attempt.packet.json"
HESSIAN_ATTEMPT = BASE / "ambient_hessian_restriction_execution_attempt.packet.json"
CUTSET = BASE / "next_cutset_after_higgs_c1_extension_attempt.packet.json"

STATUS = (
    "MTT_SELECTED_HIGGSC1VARIATIONSLOTEXTENSION_OR_AMBIENTHESSIANROWS_"
    "CONTRACTS_CLOSED_ROWS_OPEN"
)
NEXT = "MTT_Selected_EHuvC1VariationOperators_or_AmbientHessianRestrictionRows_v1"


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
    slot_contract = load(SLOT_CONTRACT)
    hessian_contract = load(HESSIAN_CONTRACT)
    slot_attempt = load(SLOT_ATTEMPT)
    hessian_attempt = load(HESSIAN_ATTEMPT)
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
        "higgs_c1_slot_extension_contract_closed",
        "ambient_hessian_row_contract_closed",
        "current_higgs_slot_extension_execution_attempted",
        "current_ambient_hessian_row_execution_attempted",
        "future_execution_formula_M_Huv_equals_12_TstarT_closed",
        "C1_matter_slot_routing_available",
        "Higgs_E_H_UV_source_ids_available",
    ]:
        require(decision[key] is True, f"decision true {key}")
    for key in [
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
    require(nums["C1_72_slot_row_count"] == 72, "row count")
    require(nums["C1_phase_R_Z_rows"] == 36, "phase rows")
    require(nums["C1_shift_R_X_rows"] == 36, "shift rows")
    require(nums["C1_routed_sector_count"] == 4, "sector count")
    require(nums["C1_higgs_slot_rows_found"] == 0, "Higgs rows")
    require(nums["required_minimum_Higgs_C1_variation_slot_count"] == 4, "required Higgs slots")
    require(nums["selected_Higgs_C1_variation_slot_count"] == 0, "selected Higgs slots")
    require(nums["ambient_Hessian_matrix_shape"] == [27, 27], "ambient shape")
    require(nums["restricted_Huv_matrix_shape"] == [2, 2], "restricted shape")
    require(nums["accepted_F_Huv_row_count"] == 0, "F rows")
    require(nums["accepted_certificate_count"] == 0, "cert rows")

    require(cert["status"] == STATUS, "cert status")
    require(cert["next_required_artifact"] == NEXT, "cert next")
    require(cert["theorem_proved"] is True, "cert theorem")
    for key in [
        "higgs_c1_slot_extension_contract_closed",
        "ambient_hessian_row_contract_closed",
        "current_higgs_slot_extension_execution_attempted",
        "current_ambient_hessian_row_execution_attempted",
        "future_execution_formula_M_Huv_equals_12_TstarT_closed",
    ]:
        require(cert[key] is True, f"cert true {key}")
    for key in [
        "true_SM_equivalence_claimed",
        "full_no_knob_closure_claimed",
        "observed_data_used_as_selector",
        "target_fitting_used",
        "selected_Higgs_C1_variation_slots_emitted",
        "ambient_27_by_27_Hessian_matrix_emitted",
        "ambient_Hessian_restriction_rows_emitted",
        "selected_F_Huv_rows_emitted",
        "direct_Herm2_row_payload_emitted",
    ]:
        require(cert[key] is False, f"cert false {key}")
    require(cert["accepted_F_Huv_row_count"] == 0, "cert F rows")
    require(cert["accepted_certificate_count"] == 0, "cert rows")

    require(
        slot_contract["status"] == "HIGGS_C1_VARIATION_SLOT_EXTENSION_CONTRACT_CLOSED",
        "slot contract status",
    )
    obj = slot_contract["object"]
    require(obj["name"] == "T_C1<-E_H^UV", "slot object name")
    require(obj["minimum_symbolic_slot_count"] == 4, "slot count")
    require(obj["matrix_shape_if_emitted"] == [2, 2], "slot shape")
    require(obj["matrix_rows"] == ["phase_R_Z", "shift_R_X"], "slot rows")
    require(obj["matrix_columns"] == ["H_u", "H_d^dagger"], "slot columns")
    require(len(obj["required_slots"]) == 4, "required slot list")
    for slot in [
        "H_u.phase_R_Z",
        "H_u.shift_R_X",
        "H_d_dagger.phase_R_Z",
        "H_d_dagger.shift_R_X",
    ]:
        require(any(item["slot"] == slot for item in obj["required_slots"]), f"slot {slot}")
    formula = slot_contract["execution_formula_after_slot_emission"]
    require(formula["compressed_dynamic_C1_normal_matrix"] == [[12.0, 0.0], [0.0, 12.0]], "slot ATA")
    require("M_Huv = 12 T^* T" in formula["current_simplification"], "slot execution")
    require("not a source for T" in formula["important_guard"], "slot guard")
    for key in [
        "higgs_c1_slot_extension_contract_closed",
        "minimum_slot_schema_closed",
        "formula_for_future_execution_closed",
    ]:
        require(slot_contract["decision"][key] is True, f"slot decision {key}")
    require_no_selector(slot_contract, "slot contract")

    require(
        hessian_contract["status"] == "AMBIENT_HESSIAN_RESTRICTION_ROW_CONTRACT_CLOSED",
        "hessian contract status",
    )
    full_route = hessian_contract["accepted_routes"]["full_ambient_route"]
    restricted_route = hessian_contract["accepted_routes"]["restricted_row_route"]
    require(full_route["matrix_shape"] == [27, 27], "full route shape")
    require("B_Huv^* Hess(F_C1)_selected B_Huv" in full_route["restriction"], "restriction")
    require(restricted_route["matrix_shape"] == [2, 2], "restricted route shape")
    require(restricted_route["required_rows"] == ["Huu", "Hud_re", "Hud_im", "Hdd"], "restricted rows")
    for forbidden in [
        "compressed A^T A normal matrix without ambient or Higgs-slot map",
        "diagonal E_H^UV HYM metric/connection alone",
        "low-energy quotient q(H_u)=q(H_d^dagger)=H alone",
        "observed Higgs beta/lambda/mass values",
    ]:
        require(forbidden in hessian_contract["forbidden_substitutes"], f"forbidden {forbidden}")
    for key in [
        "ambient_hessian_row_contract_closed",
        "restriction_row_contract_closed",
        "forbidden_substitutes_retired",
    ]:
        require(hessian_contract["decision"][key] is True, f"hessian decision {key}")
    require_no_selector(hessian_contract, "hessian contract")

    require(slot_attempt["status"] == "HIGGS_C1_SLOT_EXTENSION_EXECUTED_ZERO_SELECTED_SLOTS", "slot attempt")
    routing = slot_attempt["current_c1_routing_inventory"]
    require(routing["row_count"] == 72, "attempt rows")
    require(routing["phase_R_Z_rows"] == 36, "attempt phase")
    require(routing["shift_R_X_rows"] == 36, "attempt shift")
    require(routing["routed_sectors"] == ["d", "e", "nuD", "u"], "attempt sectors")
    require(routing["operator_selected_as_source_now_true_count"] == 0, "source flags")
    require(routing["hessian_counterterm_sourced_true_count"] == 0, "hessian flags")
    require(slot_attempt["higgs_source_inventory"]["ordered_E_H_UV_basis_labels"] == ["H_u", "H_d^dagger"], "H labels")
    require(slot_attempt["higgs_source_inventory"]["T3_eigenline_binding_closed"] is True, "T3")
    require(
        slot_attempt["higgs_source_inventory"]["B_Huv_source_orthonormal_lift_emitted"] is True,
        "B lift",
    )
    require(slot_attempt["matched_selected_higgs_slots"] == [], "matched slots")
    require(slot_attempt["missing_selected_higgs_slots"] == [item["slot"] for item in obj["required_slots"]], "missing slots")
    sdec = slot_attempt["decision"]
    require(sdec["current_higgs_slot_extension_execution_attempted"] is True, "slot attempted")
    require(sdec["selected_Higgs_C1_variation_slots_emitted"] is False, "slot emitted")
    require(sdec["selected_Higgs_C1_variation_slot_count"] == 0, "slot count emitted")
    require(sdec["required_minimum_Higgs_C1_variation_slot_count"] == 4, "slot count required")
    require_no_selector(slot_attempt, "slot attempt")

    require(hessian_attempt["status"] == "AMBIENT_HESSIAN_RESTRICTION_EXECUTED_ZERO_ROWS", "hessian attempt")
    payload = hessian_attempt["available_dynamic_C1_payload"]
    require(payload["strict_dynamic_C1_payload_imported"] is True, "payload imported")
    require(payload["A_transpose_A"] == [[12.0, 0.0], [0.0, 12.0]], "payload ATA")
    require(payload["A_transpose_b"] == [12.0, 12.0], "payload ATb")
    require(payload["selected_b_selected_available"] is True, "payload b")
    guard = hessian_attempt["current_naive_projection_guard"]
    require(guard["attempted"] is True, "guard attempted")
    require(guard["accepted"] is False, "guard accepted")
    require("zero trace-free" in guard["reason"], "guard reason")
    for value in hessian_attempt["ambient_rows"].values():
        require(value is None, "ambient row emitted")
    for value in hessian_attempt["restricted_rows"].values():
        require(value is None, "restricted row emitted")
    hdec = hessian_attempt["decision"]
    require(hdec["current_ambient_hessian_row_execution_attempted"] is True, "hessian attempted")
    for key in [
        "ambient_27_by_27_Hessian_matrix_emitted",
        "ambient_Hessian_restriction_rows_emitted",
        "selected_F_Huv_rows_emitted",
        "direct_Herm2_row_payload_emitted",
    ]:
        require(hdec[key] is False, f"hessian false {key}")
    require(hdec["accepted_F_Huv_row_count"] == 0, "hessian F rows")
    require(hdec["accepted_certificate_count"] == 0, "hessian certs")
    require_no_selector(hessian_attempt, "hessian attempt")

    require(
        cutset["status"] == "NEXT_FRONTIER_EHUV_C1_VARIATION_OPERATORS_OR_AMBIENT_HESSIAN_RESTRICTION_ROWS",
        "cutset status",
    )
    require(cutset["next_required_artifact"] == NEXT, "cutset next")
    for phrase in [
        "Higgs C1 variation-slot extension contract",
        "minimum four-slot T_C1<-E_H^UV schema",
        "ambient 27x27 Hess(F_C1) or direct 2x2 restriction-row acceptance contract",
        "future execution formula M_Huv=12 T^*T after T is selected",
    ]:
        require(phrase in cutset["closed_here"], f"closed {phrase}")
    for phrase in [
        "selected E_H^UV C1 variation operator rows for H_u and H_d^dagger",
        "or selected ambient Hess(F_C1) rows/restriction rows on the 27-mode carrier",
        "source-owned T_C1<-E_H^UV numeric/symbolic entries",
    ]:
        require(phrase in cutset["still_open"], f"open {phrase}")
    require_no_selector(cutset, "cutset")

    for phrase in [
        "T_C1<-E_H^UV",
        "M_Huv = 12 T^* T",
        "Higgs C1 slots found in current routing: `0`",
        "Required minimum Higgs C1 slots: `4`",
        NEXT,
    ]:
        require(phrase in note, f"note missing {phrase}")

    print(
        "AUDIT_PASS: Higgs C1 slot and ambient Hessian row contracts are closed; "
        "current corpus emits zero selected Higgs slots and zero F_Huv rows."
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
