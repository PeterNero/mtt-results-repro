"""Audit dynamic Phi_fin/C1 payload rows or higher-response execution artifact."""

from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "candidate_data"
CERTS = ROOT / "certificates"
CORPUS = ROOT / "proof_corpus"
BUILDER = ROOT / "scripts" / "build_selected_dynamicphifinc1payloadrows_or_higherresponseexecution.py"

SLUG = "selected_dynamicphifinc1payloadrows_or_higherresponseexecution"
PACKET_DIR = DATA / SLUG
CANDIDATE = DATA / f"{SLUG}.candidate.json"
CERT = CERTS / f"{SLUG}_certificate.json"
NOTE = CORPUS / "MTT_Selected_DynamicPhiFinC1PayloadRows_or_HigherResponseExecution_v1.md"

INVENTORY = PACKET_DIR / "dynamic_phifin_c1_payload_row_inventory.packet.json"
RECONCILIATION = PACKET_DIR / "support_vs_selected_payload_reconciliation.packet.json"
EXECUTION = PACKET_DIR / "higher_response_execution_attempt_after_payload_inventory.packet.json"
CUTSET = PACKET_DIR / "next_cutset_after_payload_row_inventory.packet.json"

STATUS = (
    "MTT_SELECTED_DYNAMICPHIFINC1PAYLOADROWS_OR_HIGHERRESPONSEEXECUTION_"
    "BUILT_ROW_LEDGER_EXECUTION_OPEN"
)
NEXT = "MTT_Selected_HYMProjectorZeroModeBasisValueEmission_or_PrimitiveRowFormulaExecution_v1"


def load(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def expect(condition: bool, message: str, errors: list[str]) -> None:
    if not condition:
        errors.append(message)


def guard(packet: dict[str, Any], errors: list[str], label: str) -> None:
    expect(packet.get("observed_data_used_as_selector") is False, f"{label} observed selector violation", errors)
    expect(packet.get("target_fitting_used") is False, f"{label} target fitting violation", errors)
    expect(packet.get("closure_claimed") is False, f"{label} overclaimed closure", errors)


def main() -> int:
    subprocess.run([sys.executable, str(BUILDER)], cwd=ROOT, check=True)

    candidate = load(CANDIDATE)
    cert = load(CERT)
    inventory = load(INVENTORY)
    reconciliation = load(RECONCILIATION)
    execution = load(EXECUTION)
    cutset = load(CUTSET)
    note = NOTE.read_text(encoding="utf-8")

    errors: list[str] = []

    expect(candidate.get("status") == STATUS, "candidate status mismatch", errors)
    expect(cert.get("status") == STATUS, "certificate status mismatch", errors)
    expect(candidate.get("next_required_artifact") == NEXT, "candidate next mismatch", errors)
    expect(cert.get("next_required_artifact") == NEXT, "certificate next mismatch", errors)
    expect(candidate.get("theorem", {}).get("proved") is True, "candidate theorem missing", errors)
    expect(cert.get("theorem_proved") is True, "certificate theorem missing", errors)

    for label, packet in [
        ("candidate", candidate),
        ("certificate", cert),
        ("inventory", inventory),
        ("reconciliation", reconciliation),
        ("execution", execution),
        ("cutset", cutset),
    ]:
        guard(packet, errors, label)

    expect(
        inventory.get("status") == "PAYLOAD_ROW_INVENTORY_BUILT_NO_DYNAMIC_ROWS_ACCEPTED",
        "inventory status mismatch",
        errors,
    )
    expect(inventory.get("row_count") == 9, "inventory row count mismatch", errors)
    expect(inventory.get("support_candidate_present_count") == 9, "support count mismatch", errors)
    expect(inventory.get("stationary_source_slot_closed_count") == 3, "stationary slot count mismatch", errors)
    expect(inventory.get("accepted_dynamic_payload_row_count") == 0, "dynamic payload rows overaccepted", errors)
    expect(inventory.get("all_support_shapes_present") is True, "support shapes not present", errors)
    expect(inventory.get("all_selected_values_emitted") is False, "selected values overemitted", errors)
    expect(inventory.get("higher_response_execution_inputs_available") is False, "execution inputs overclaimed", errors)
    rows = {row["row_id"]: row for row in inventory.get("rows", [])}
    for row_id in [
        "D_E_action",
        "Hermitian_metric",
        "Riesz_Green",
        "dotD_alpha1",
        "finite_Hessian_C1_source",
        "primitive_C1_contractions",
        "rho_E_transition_data",
        "sector_projectors",
        "zero_mode_bases",
    ]:
        expect(row_id in rows, f"payload row missing: {row_id}", errors)
        expect(rows[row_id]["support_candidate_present"] is True, f"support missing: {row_id}", errors)
        expect(rows[row_id]["selected_payload_flag"] is False, f"selected payload overclaimed: {row_id}", errors)
        expect(rows[row_id]["accepted_as_dynamic_phifin_c1_payload_row"] is False, f"payload accepted: {row_id}", errors)
    for row_id in ["Riesz_Green", "dotD_alpha1", "sector_projectors"]:
        expect(rows[row_id].get("stationary_source_slot_closed") is True, f"stationary slot missing: {row_id}", errors)
        expect(rows[row_id].get("dynamic_C1_scope_excluded_by_source") is True, f"dynamic scope not excluded: {row_id}", errors)
    expect(rows["sector_projectors"].get("finite_projector_matrices_emitted") is True, "projector matrices not emitted", errors)
    expect(rows["sector_projectors"].get("honest_validator_promotes") is False, "projector honest promotion overclaimed", errors)
    expect(rows["zero_mode_bases"].get("zero_mode_bridge_theorem_closed") is True, "zero-mode bridge missing", errors)
    expect(rows["zero_mode_bases"].get("selected_zero_mode_bases_emitted") is False, "zero-mode bases overemitted", errors)
    for row_id in ["finite_Hessian_C1_source", "primitive_C1_contractions"]:
        expect(rows[row_id].get("primitive_row_formula_contract_built") is True, f"primitive contract missing: {row_id}", errors)
        expect(rows[row_id].get("primitive_row_formula_executed") is False, f"primitive formula overexecuted: {row_id}", errors)

    expect(
        reconciliation.get("status") == "SUPPORT_ROWS_RECONCILED_WITH_SELECTED_PAYLOAD_GAP",
        "reconciliation status mismatch",
        errors,
    )
    expect(reconciliation.get("stationary_riesz_green_dotd_slot_closed") is True, "stationary slot not closed", errors)
    expect(reconciliation.get("stationary_source_value_emitted") is True, "stationary source not emitted", errors)
    expect(reconciliation.get("dynamic_C1_scope_excluded") is True, "dynamic scope guard missing", errors)
    expect(reconciliation.get("sector_projectors_emitted_as_matrices") is True, "sector projectors missing", errors)
    expect(reconciliation.get("sector_projectors_honest_validator_promotes") is False, "sector projectors overpromoted", errors)
    expect(reconciliation.get("dynamic_trace_binding_reconciled") is True, "dynamic trace binding not reconciled", errors)
    expect(reconciliation.get("primitive_row_formula_contract_built") is True, "primitive row contract missing", errors)
    expect(reconciliation.get("primitive_row_formula_executed") is False, "primitive row formula overexecuted", errors)
    expect(reconciliation.get("same_source_route_test_closed") is True, "same-source route test missing", errors)
    expect(reconciliation.get("same_source_dynamic_payload_closed") is False, "same-source dynamic payload overclosed", errors)

    expect(
        execution.get("status") == "HIGHER_RESPONSE_EXECUTION_BLOCKED_BY_DYNAMIC_PAYLOAD_ROWS",
        "execution status mismatch",
        errors,
    )
    expect(execution.get("codomain_scalar_row_count") == 10, "scalar row count mismatch", errors)
    expect(execution.get("payload_row_count") == 9, "payload row count mismatch", errors)
    expect(execution.get("accepted_dynamic_payload_row_count") == 0, "payload rows overaccepted in execution", errors)
    expect(execution.get("execution_inputs_available_now") is False, "execution inputs overclaimed", errors)
    expect(execution.get("selected_functional_executed") is False, "functional overexecuted", errors)
    expect(execution.get("accepted_scalar_row_count_now") == 0, "scalar rows overaccepted", errors)
    for key in ["mass_hierarchy_test_executed", "CKM_test_executed", "PMNS_test_executed", "CP_test_executed", "lambda_H_row_emitted"]:
        expect(execution.get(key) is False, f"execution overclaimed: {key}", errors)
    expect(len(execution.get("why_blocked", [])) >= 5, "execution blocker list incomplete", errors)

    expect(
        cutset.get("status") == "NEXT_ATTACK_HYM_PROJECTOR_ZEROMODE_VALUES_OR_PRIMITIVE_ROW_FORMULA",
        "cutset status mismatch",
        errors,
    )
    closed = cutset.get("closed_now", {})
    for key in [
        "dynamic_payload_row_inventory_built",
        "support_vs_selected_payload_reconciled",
        "stationary_slot_not_confused_with_dynamic_payload",
        "higher_response_execution_attempted_and_blocked",
        "next_executable_subgates_identified",
    ]:
        expect(closed.get(key) is True, f"cutset closure missing: {key}", errors)
    still = cutset.get("still_open", {})
    for key in [
        "selected_HYM_projector_zero_mode_basis_values",
        "selected_D_E_operator_values",
        "selected_rho_E_transition_data",
        "selected_finite_Hessian_C1_source_blocks",
        "selected_deltaTheta_C1",
        "primitive_C1_contractions",
        "sector_response_matrices",
        "higher_response_Rtheta_execution",
        "Yukawa_mass_mixing_value_closure",
        "true_SM_equivalence",
        "full_no_knob",
    ]:
        expect(still.get(key) is True, f"cutset overclosed: {key}", errors)
    expect(cutset.get("recommended_next", {}).get("artifact") == NEXT, "cutset next mismatch", errors)

    closure = candidate.get("closure_decision", {})
    expect(closure.get("dynamic_payload_row_inventory_built") is True, "candidate inventory missing", errors)
    expect(closure.get("dynamic_payload_row_count") == 9, "candidate payload count mismatch", errors)
    expect(closure.get("support_candidate_present_count") == 9, "candidate support count mismatch", errors)
    expect(closure.get("accepted_dynamic_payload_row_count") == 0, "candidate payload rows overaccepted", errors)
    expect(closure.get("stationary_source_slot_closed_count") == 3, "candidate stationary count mismatch", errors)
    expect(closure.get("higher_response_execution_inputs_available") is False, "candidate execution inputs overclaimed", errors)
    expect(closure.get("higher_response_Rtheta_executed") is False, "candidate Rtheta overexecuted", errors)
    expect(closure.get("accepted_scalar_row_count_now") == 0, "candidate scalar rows overaccepted", errors)
    for key in ["no_knob_value_derivation_closed", "true_SM_equivalence_closed", "full_no_knob_closed"]:
        expect(closure.get(key) is False, f"candidate overclosed: {key}", errors)
        expect(cert.get(key) is False, f"certificate overclosed: {key}", errors)

    expect("dynamic payload slots                  : 9" in note, "note missing payload row count", errors)
    expect("support shapes present                 : 9" in note, "note missing support count", errors)
    expect("accepted dynamic payload rows          : 0" in note, "note missing accepted dynamic rows", errors)
    expect("stationary source slots closed         : 3" in note, "note missing stationary count", errors)
    expect("higher-response Rtheta executed        : false" in note, "note missing execution guard", errors)
    expect("full no-knob closure                   : false" in note, "note missing no-knob guard", errors)
    expect("true SM equivalence                    : false" in note, "note missing true SM guard", errors)

    if errors:
        print("Dynamic Phi_fin/C1 payload audit FAILED")
        for error in errors:
            print(f"- {error}")
        return 1

    print("Dynamic Phi_fin/C1 payload audit passed")
    print(json.dumps({"candidate": str(CANDIDATE.relative_to(ROOT)), "status": STATUS}, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
