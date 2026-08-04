"""Audit C1-to-BHuv projection tensor or F_Huv rows packet."""

from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SLUG = "selected_c1tobhuvprojectiontensor_or_fhuvrows"
BASE = ROOT / "candidate_data" / SLUG
CANDIDATE = ROOT / "candidate_data" / f"{SLUG}.candidate.json"
CERT = ROOT / "certificates" / f"{SLUG}_certificate.json"
NOTE = ROOT / "proof_corpus" / "MTT_Selected_C1ToBHuvProjectionTensor_or_FHuvRows_v1.md"
BUILD = ROOT / "scripts" / f"build_{SLUG}.py"

CONTRACT = BASE / "c1_to_bhuv_projection_tensor_contract.packet.json"
INVENTORY = BASE / "c1_variation_vs_higgs_slot_inventory.packet.json"
ATTEMPT = BASE / "projection_tensor_emission_attempt.packet.json"
CUTSET = BASE / "next_cutset_after_c1_to_bhuv_tensor_attempt.packet.json"

STATUS = (
    "MTT_SELECTED_C1TOBHUVPROJECTIONTENSOR_OR_FHUVROWS_"
    "CONTRACT_CLOSED_HIGGS_SLOT_TENSOR_OPEN"
)
NEXT = "MTT_Selected_HiggsC1VariationSlotExtension_or_AmbientHessianRows_v1"
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
    inventory = load(INVENTORY)
    attempt = load(ATTEMPT)
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
        "projection_tensor_contract_closed",
        "inventory_executed",
        "projection_tensor_emission_attempted",
        "C1_matter_slot_routing_available",
        "Higgs_E_H_UV_source_ids_available",
    ]:
        require(decision[key] is True, f"decision true {key}")
    for key in [
        "source_owned_C1_to_BHuv_tensor_emitted",
        "ambient_27_by_27_Hessian_matrix_emitted",
        "selected_Higgs_C1_variation_slots_emitted",
        "selected_F_Huv_rows_emitted",
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
    require(nums["C1_72_slot_row_count"] == 72, "row count")
    require(nums["C1_phase_R_Z_rows"] == 36, "phase rows")
    require(nums["C1_shift_R_X_rows"] == 36, "shift rows")
    require(nums["C1_higgs_slot_rows_found"] == 0, "Higgs rows")
    require(nums["Huv_source_column_count"] == 2, "Huv columns")
    require(nums["accepted_F_Huv_row_count"] == 0, "F rows")
    require(nums["accepted_certificate_count"] == 0, "cert rows")

    require(cert["status"] == STATUS, "cert status")
    require(cert["next_required_artifact"] == NEXT, "cert next")
    require(cert["theorem_proved"] is True, "cert theorem")
    for key in [
        "projection_tensor_contract_closed",
        "inventory_executed",
        "projection_tensor_emission_attempted",
        "C1_matter_slot_routing_available",
        "Higgs_E_H_UV_source_ids_available",
    ]:
        require(cert[key] is True, f"cert true {key}")
    for key in [
        "source_owned_C1_to_BHuv_tensor_emitted",
        "ambient_27_by_27_Hessian_matrix_emitted",
        "selected_Higgs_C1_variation_slots_emitted",
        "selected_F_Huv_rows_emitted",
        "direct_Herm2_row_payload_emitted",
        "lambda_H_predicted",
        "true_SM_equivalence_claimed",
        "full_no_knob_closure_claimed",
        "observed_data_used_as_selector",
        "target_fitting_used",
    ]:
        require(cert[key] is False, f"cert false {key}")

    require(contract["status"] == "C1_TO_BHUV_PROJECTION_TENSOR_CONTRACT_CLOSED", "contract status")
    req = contract["required_tensor"]
    require(req["name"] == "T_C1<-Huv", "tensor name")
    require("B_Huv" in req["domain"], "domain")
    require("C1 variation" in req["codomain"], "codomain")
    require("M_Huv = T_C1<-Huv^* (A^T A)_C1 T_C1<-Huv" in req["acceptance_formula"], "formula")
    for forbidden in [
        "matter-sector C1 slot routing without Higgs slots",
        "diagonal HYM metric/connection on E_H^UV alone",
        "compressed A^T A normal matrix without T_C1<-Huv",
        "observed Higgs beta/lambda/mass values",
    ]:
        require(forbidden in contract["forbidden_substitutes"], f"forbidden {forbidden}")
    for key in ["projection_tensor_contract_closed", "accepted_source_routes_named", "forbidden_substitutes_retired"]:
        require(contract["decision"][key] is True, f"contract decision {key}")
    require_no_selector(contract, "contract")

    require(inventory["status"] == "C1_VARIATION_AND_HIGGS_SLOT_INVENTORY_EXECUTED_NO_TENSOR", "inventory status")
    routing = inventory["c1_variation_routing"]
    require(routing["row_count"] == 72, "inventory row count")
    require(routing["phase_R_Z_rows"] == 36, "inventory phase")
    require(routing["shift_R_X_rows"] == 36, "inventory shift")
    require(routing["routed_sectors"] == ["d", "e", "nuD", "u"], "routed sectors")
    require(routing["sector_routing"]["phase_R_Z"] == ["u", "e"], "phase routing")
    require(routing["sector_routing"]["shift_R_X"] == ["d", "nuD"], "shift routing")
    require(routing["higgs_slot_rows_found"] == 0, "inventory Higgs rows")
    higgs = inventory["higgs_slot_data"]
    require(higgs["ordered_E_H_UV_basis_labels"] == ["H_u", "H_d^dagger"], "H labels")
    require(higgs["single_low_energy_quotient_closed"] is True, "quotient")
    require(higgs["T3_eigenline_binding_closed"] is True, "T3")
    require(higgs["B_Huv_symbolic_exact_payload_emitted"] is True, "B payload")
    result = inventory["intersection_result"]
    require(result["matter_variation_sectors_intersect_Huv_labels"] is False, "intersection")
    require(result["Huv_labels_present_in_72_slot_routing"] is False, "H labels in C1")
    require(result["source_owned_C1_to_BHuv_tensor_emitted"] is False, "tensor emitted")
    require(inventory["decision"]["inventory_executed"] is True, "inventory executed")
    require(inventory["decision"]["C1_to_BHuv_projection_tensor_emitted"] is False, "inventory tensor")
    require_no_selector(inventory, "inventory")

    require(attempt["status"] == "PROJECTION_TENSOR_EMISSION_ATTEMPTED_ZERO_FHUV_ROWS", "attempt status")
    payload = attempt["available_strict_payload"]
    require(payload["compressed_C1_payload_imported"] is True, "payload imported")
    require(payload["selected_b_selected_available"] is True, "b available")
    require(payload["A_transpose_A"] == [[12.0, 0.0], [0.0, 12.0]], "ATA")
    tested = attempt["candidate_routes_tested"]
    for route in [
        "use_72_slot_routing_as_T_C1_Huv",
        "use_E_H_UV_C2_basis_as_T_C1_Huv",
        "use_C3_diagonal_HYM_T3_as_T_C1_Huv",
        "use_A_transpose_A_as_direct_Huv",
    ]:
        require(tested[route]["accepted"] is False, f"route accepted {route}")
        require(tested[route]["reason"], f"route reason {route}")
    require(attempt["emitted_tensor"] is None, "tensor not none")
    for value in attempt["emitted_rows"].values():
        require(value is None, "row emitted")
    for value in attempt["emitted_certificates"].values():
        require(value is None, "cert emitted")
    adec = attempt["decision"]
    require(adec["projection_tensor_emission_attempted"] is True, "attempted")
    for key in [
        "source_owned_C1_to_BHuv_tensor_emitted",
        "ambient_27_by_27_Hessian_matrix_emitted",
        "selected_F_Huv_rows_emitted",
        "direct_Herm2_row_payload_emitted",
    ]:
        require(adec[key] is False, f"attempt false {key}")
    require(adec["accepted_F_Huv_row_count"] == 0, "attempt F rows")
    require(adec["accepted_certificate_count"] == 0, "attempt certs")
    require_no_selector(attempt, "attempt")

    require(cutset["status"] == "NEXT_FRONTIER_HIGGS_C1_VARIATION_SLOT_EXTENSION_OR_AMBIENT_HESSIAN_ROWS", "cutset status")
    require(cutset["next_required_artifact"] == NEXT, "cutset next")
    for phrase in [
        "C1-to-BHuv projection tensor acceptance contract",
        "inventory comparing C1 72-slot routing with H_u/H_d^dagger source IDs",
        "proof that existing C1 routing is matter-sector routing, not a Higgs tensor",
    ]:
        require(phrase in cutset["closed_here"], f"closed {phrase}")
    for phrase in [
        "selected Higgs C1 variation slots extending the 72-slot table",
        "or ambient 27x27 Hess(F_C1)_selected rows on E_H^UV",
        "source-owned T_C1<-Huv tensor values",
    ]:
        require(phrase in cutset["still_open"], f"open {phrase}")
    require_no_selector(cutset, "cutset")

    for phrase in [
        "T_C1<-Huv",
        "Higgs rows inside the C1 72-slot routing: `0`",
        "Accepted `F_Huv` rows: `0`",
        NEXT,
    ]:
        require(phrase in note, f"note missing {phrase}")

    print(
        "AUDIT_PASS: C1-to-BHuv tensor contract is closed; existing C1 routing "
        "has zero Higgs slots and emits zero F_Huv rows."
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
