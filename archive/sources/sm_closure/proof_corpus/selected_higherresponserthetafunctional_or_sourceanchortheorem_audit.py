"""Audit higher-response Rtheta functional / source-anchor theorem artifact."""

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
BUILDER = ROOT / "scripts" / "build_selected_higherresponserthetafunctional_or_sourceanchortheorem.py"

SLUG = "selected_higherresponserthetafunctional_or_sourceanchortheorem"
PACKET_DIR = DATA / SLUG
CANDIDATE = DATA / f"{SLUG}.candidate.json"
CERT = CERTS / f"{SLUG}_certificate.json"
NOTE = CORPUS / "MTT_Selected_HigherResponseRThetaFunctional_or_SourceAnchorTheorem_v1.md"

PAYLOAD_GAP = PACKET_DIR / "higher_response_source_payload_gap.packet.json"
CONTRACT = PACKET_DIR / "rtheta_higher_response_functional_contract.packet.json"
ANCHOR_RECHECK = PACKET_DIR / "source_anchor_theorem_recheck.packet.json"
DECISION = PACKET_DIR / "higher_response_or_source_anchor_decision.packet.json"
CUTSET = PACKET_DIR / "next_cutset_after_higher_response_contract.packet.json"

STATUS = (
    "MTT_SELECTED_HIGHERRESPONSERTHETAFUNCTIONAL_OR_SOURCEANCHORTHEOREM_"
    "BUILT_PAYLOAD_SPEC_SOURCE_ANCHOR_OPEN"
)
NEXT = "MTT_Selected_DynamicPhiFinC1PayloadRows_or_HigherResponseExecution_v1"


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
    payload_gap = load(PAYLOAD_GAP)
    contract = load(CONTRACT)
    anchor = load(ANCHOR_RECHECK)
    decision = load(DECISION)
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
        ("payload_gap", payload_gap),
        ("contract", contract),
        ("anchor", anchor),
        ("decision", decision),
        ("cutset", cutset),
    ]:
        guard(packet, errors, label)

    expect(
        payload_gap.get("status")
        == "DYNAMIC_PHIFIN_C1_PAYLOAD_ROWS_MISSING_HIGHER_RESPONSE_NOT_EXECUTABLE",
        "payload gap status mismatch",
        errors,
    )
    expect(payload_gap.get("current_layer_no_go_proved") is True, "current no-go missing", errors)
    expect(payload_gap.get("current_values_available") is False, "current values overclaimed", errors)
    expect(payload_gap.get("open_payload_flag_count") == 9, "open payload flag count mismatch", errors)
    for key in [
        "primitive_C1_contractions",
        "sector_response_matrices_M_u_M_d_M_e_M_nuD",
        "selected_deltaTheta_C1",
        "selected_dotD_alpha1",
        "source_flags_not_lifted",
        "zero_mode_bases",
    ]:
        expect(payload_gap.get("required_full_response_outputs", {}).get(key) is True, f"required output missing: {key}", errors)
    expect(payload_gap.get("typed_bn_retarded_derivative_closed") is False, "typed BN overclosed", errors)
    expect(payload_gap.get("phi_fin_dynamic_c1_payload_closed") is False, "dynamic payload overclosed", errors)
    expect(payload_gap.get("primitive_fiber_class_quotient_selected") is True, "primitive quotient missing", errors)
    expect(payload_gap.get("absolute_matrix_representative_selected") is False, "absolute matrix representative overselected", errors)
    expect(payload_gap.get("selected_higher_response_payload_rows_emitted") is False, "payload rows overemitted", errors)

    expect(
        contract.get("status") == "HIGHER_RESPONSE_RTHETA_FUNCTIONAL_CONTRACT_BUILT_EXECUTION_OPEN",
        "contract status mismatch",
        errors,
    )
    expect(contract.get("contract_closed") is True, "contract not closed", errors)
    expect(len(contract.get("domain_requirements", [])) == 7, "domain requirement count mismatch", errors)
    expect(contract.get("codomain_scalar_row_count") == 10, "codomain scalar count mismatch", errors)
    expect(contract.get("codomain_scalar_rows", [])[-1] == "lambda_H", "lambda_H row missing", errors)
    for key in ["mass_hierarchy", "CKM", "PMNS", "CP", "lambda_H", "no_target_selector"]:
        expect(key in contract.get("acceptance_tests_after_execution", {}), f"acceptance test missing: {key}", errors)
    expect(contract.get("execution_inputs_available_now") is False, "execution inputs overclaimed", errors)
    expect(contract.get("selected_functional_executed") is False, "functional overexecuted", errors)
    expect(contract.get("accepted_scalar_row_count_now") == 0, "accepted scalar rows overclaimed", errors)

    expect(anchor.get("status") == "SOURCE_ANCHOR_THEOREM_NOT_SELECTED", "anchor status mismatch", errors)
    expect(anchor.get("selected_universal_parameter_count") == 0, "universal parameter overselected", errors)
    expect(anchor.get("maximum_live_universal_parameters") == 3, "max universal parameter mismatch", errors)
    expect(anchor.get("candidate_specific_source_theorem_present") is False, "source theorem overclaimed", errors)
    expect(anchor.get("typed_retarded_derivative_emitted") is False, "typed derivative overemitted", errors)
    expect(anchor.get("selected_primitive_response_emitted") is False, "primitive response overemitted", errors)
    expect(anchor.get("retarded_source_selector_selected") is False, "retarded selector overselected", errors)
    expect(anchor.get("source_anchor_theorem_closed") is False, "source anchor overclosed", errors)

    expect(decision.get("status") == "CONTRACT_BUILT_EXECUTION_AND_SOURCE_ANCHOR_OPEN", "decision status mismatch", errors)
    expect(decision.get("higher_response_contract_closed") is True, "decision missing contract", errors)
    expect(decision.get("higher_response_payload_rows_emitted") is False, "decision overemitted payload", errors)
    expect(decision.get("selected_higher_response_Rtheta_functional_executed") is False, "decision overexecuted functional", errors)
    expect(decision.get("source_anchor_theorem_closed") is False, "decision source anchor overclosed", errors)
    expect(decision.get("selected_universal_parameter_count") == 0, "decision universal parameter overselected", errors)
    expect(decision.get("first_response_only_route_rejected") is True, "decision lost first-response no-go", errors)
    expect(decision.get("dynamic_first_response_rank") == 2, "decision rank mismatch", errors)
    expect(decision.get("scalar_target_slot_count") == 10, "decision scalar slot mismatch", errors)
    for key in ["no_knob_value_derivation_closed", "true_SM_equivalence_closed", "full_no_knob_closed"]:
        expect(decision.get(key) is False, f"decision overclosed: {key}", errors)

    expect(
        cutset.get("status") == "NEXT_ATTACK_DYNAMIC_PHIFIN_C1_PAYLOAD_ROWS_OR_HIGHER_RESPONSE_EXECUTION",
        "cutset status mismatch",
        errors,
    )
    closed = cutset.get("closed_now", {})
    for key in [
        "higher_response_payload_gap_imported",
        "higher_response_Rtheta_functional_contract_built",
        "source_anchor_rechecked_not_selected",
        "ten_scalar_row_target_fixed",
        "first_response_no_go_preserved",
    ]:
        expect(closed.get(key) is True, f"cutset closure missing: {key}", errors)
    still = cutset.get("still_open", {})
    for key in [
        "selected_dynamic_PhiFin_C1_payload_rows",
        "selected_zero_mode_bases",
        "selected_Hermitian_metric_and_Riesz_Green",
        "selected_finite_Hessian_C1_source_blocks",
        "selected_rho_E_transition_data",
        "selected_sector_projectors",
        "selected_dotD_alpha1_and_deltaTheta_C1",
        "primitive_C1_contractions",
        "sector_response_matrices",
        "higher_response_Rtheta_execution",
        "candidate_specific_universal_source_anchor_theorem",
        "Yukawa_mass_mixing_value_closure",
        "true_SM_equivalence",
        "full_no_knob",
    ]:
        expect(still.get(key) is True, f"cutset overclosed: {key}", errors)
    expect(cutset.get("recommended_next", {}).get("artifact") == NEXT, "cutset next mismatch", errors)

    closure = candidate.get("closure_decision", {})
    expect(closure.get("higher_response_Rtheta_functional_contract_closed") is True, "candidate contract missing", errors)
    expect(closure.get("codomain_scalar_row_count") == 10, "candidate scalar row count mismatch", errors)
    expect(closure.get("selected_universal_parameter_count") == 0, "candidate universal parameter overselected", errors)
    expect(closure.get("accepted_scalar_row_count_now") == 0, "candidate scalar rows overaccepted", errors)
    for key in [
        "higher_response_payload_rows_emitted",
        "selected_higher_response_Rtheta_functional_executed",
        "source_anchor_theorem_closed",
        "no_knob_value_derivation_closed",
        "true_SM_equivalence_closed",
        "full_no_knob_closed",
    ]:
        expect(closure.get(key) is False, f"candidate overclosed: {key}", errors)
        expect(cert.get(key) is False, f"certificate overclosed: {key}", errors)

    expect("higher-response contract closed        : true" in note, "note missing contract", errors)
    expect("scalar output rows                     : 10" in note, "note missing row count", errors)
    expect("dynamic Phi_fin/C1 payload emitted     : false" in note, "note missing payload guard", errors)
    expect("source-anchor theorem closed           : false" in note, "note missing source anchor guard", errors)
    expect("selected universal parameters          : 0" in note, "note missing universal parameter count", errors)
    expect("no-knob value derivation closed        : false" in note, "note missing no-knob guard", errors)
    expect("true SM equivalence                    : false" in note, "note missing true SM guard", errors)

    if errors:
        print("Higher-response/source-anchor audit FAILED")
        for error in errors:
            print(f"- {error}")
        return 1

    print("Higher-response/source-anchor audit passed")
    print(json.dumps({"candidate": str(CANDIDATE.relative_to(ROOT)), "status": STATUS}, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
