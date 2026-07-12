"""Audit typed Cech/HYM/projective connection witness value gate packet."""

from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SLUG = "selected_typedcechhymprojectiveconnectionwitnessvalues_or_directhkrow"
DATA = ROOT / "candidate_data" / f"{SLUG}.candidate.json"
PACKET_DIR = ROOT / "candidate_data" / SLUG
TYPED_GATE = PACKET_DIR / "typed_cech_gaplayer_not_connection_values.packet.json"
HYM_GATE = PACKET_DIR / "direct_hym_galerkin_nonpromotion_gate.packet.json"
ROUTEC_GATE = PACKET_DIR / "routec_projective_extraction_open_gate.packet.json"
NEXT_CONTRACT = PACKET_DIR / "next_same_source_connection_table_or_direct_hkrow_contract.packet.json"
CERT = ROOT / "certificates" / f"{SLUG}_certificate.json"
NOTE = ROOT / "proof_corpus" / "MTT_Selected_TypedCechHYMProjectiveConnectionWitnessValues_or_DirectHKRow_v1.md"
BUILDER = ROOT / "scripts" / f"build_{SLUG}.py"

STATUS = (
    "MTT_SELECTED_TYPEDCECH_HYM_PROJECTIVE_CONNECTIONWITNESSVALUES_"
    "OLD_SUPPORT_REJECTED_SAME_SOURCE_VALUE_TABLE_OPEN"
)
NEXT = "MTT_Selected_SameSourceConnectionValueTable_or_DirectHKRow_v1"


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
    typed = load(TYPED_GATE)
    hym = load(HYM_GATE)
    routec = load(ROUTEC_GATE)
    contract = load(NEXT_CONTRACT)
    cert = load(CERT)
    note = NOTE.read_text(encoding="utf-8")

    for label, packet in [
        ("candidate", data),
        ("typed", typed),
        ("hym", hym),
        ("routec", routec),
        ("contract", contract),
        ("certificate", cert),
    ]:
        guard(packet, label)

    require(data["status"] == STATUS, "candidate status")
    require(cert["status"] == STATUS, "certificate status")
    require(data["next_required_artifact"] == NEXT, "candidate next")
    require(cert["next_required_artifact"] == NEXT, "certificate next")
    require(data["theorem"]["proved"] is True, "candidate theorem")
    require(cert["theorem_proved"] is True, "certificate theorem")
    require(data["full_no_knob_closure_claimed"] is False, "candidate no-knob")
    require(data["true_SM_equivalence_claimed"] is False, "candidate true SM")

    require(typed["transition_rhoE_or_Cech_Dolbeault_DE_data_closed"] is True, "typed gap support")
    require(typed["finite_determinant_heat_spectrum_or_torsion_response_closed"] is False, "typed torsion overclosed")
    require(typed["actual_dynamic_QaSU3_operator_packet_closed"] is False, "typed dynamic overclosed")
    require(typed["accepted_as_connection_witness_values"] is False, "typed overaccepted")

    require(hym["diagonal_hym_green_subsource_closed"] is True, "HYM support")
    require(hym["honest_galerkin_input_readiness_closed"] is True, "Galerkin readiness")
    for key in [
        "selected_HYM_projector_values_promoted",
        "selected_sector_transfer_values_emitted",
        "selected_retarded_overlap_derivative_rows_emitted",
        "selected_threshold_scheme_rows_emitted",
        "lambda_H_value_row_emitted",
        "accepted_as_connection_witness_values",
    ]:
        require(hym[key] is False, f"HYM overclosed {key}")
    require(hym["accepted_rowlocal_source_row_count"] == 0, "HYM overaccepted rows")

    require(routec["finite_operator_extraction_contract_active"] is True, "Route-C contract")
    for key in [
        "visible_operator_payload_emitted",
        "routec_hym_residual_promoted",
        "actual_QaSU3_packet_promoted",
        "accepted_as_connection_witness_values",
    ]:
        require(routec[key] is False, f"Route-C overclosed {key}")

    require(
        contract["status"] == "SAME_SOURCE_CONNECTION_VALUE_TABLE_OR_DIRECT_HKROW_REQUIRED",
        "contract status",
    )
    require(len(contract["required_same_source_connection_table_fields"]) == 8, "field count")
    require(contract["strict_K_threshold_count"] == {"accepted": 9, "required": 10}, "K count")
    for phrase in [
        "gap-layer Cech/trace payload as connection values",
        "model-active diagonal HYM Galerkin data as selected HYM projector values",
        "lifted Route-C flags as honest same-source operator values",
        "controlled HRG/radial calibration as no-knob H K row",
    ]:
        require(phrase in contract["forbidden_reuse"], f"forbidden reuse missing {phrase}")

    decision = data["closure_decision"]
    for key in [
        "typed_cech_gaplayer_support_closed",
        "direct_hym_diagonal_support_closed",
        "routec_projective_extraction_contract_active",
        "all_three_legal_routes_rechecked",
        "old_support_rejected_as_final_values",
    ]:
        require(decision[key] is True, f"decision missing {key}")
        require(cert[key] is True, f"certificate missing {key}")
    for key in [
        "typed_cech_connection_values_emitted",
        "direct_hym_selected_projector_values_promoted",
        "direct_hym_connection_values_emitted",
        "routec_same_source_values_emitted",
        "same_source_connection_value_table_emitted",
        "selected_K_threshold_Omega_H_lambda",
        "strict_H_K_threshold_row_emitted",
        "full_no_knob_closed",
        "true_SM_equivalence_closed",
    ]:
        require(decision[key] is False, f"decision overclosed {key}")
    require(decision["payload_missing_leaf_count"] == 29, "missing leaves")
    require(decision["accepted_selected_K_source_row_count"] == 9, "K accepted")
    require(decision["selected_K_threshold_row_count_required"] == 10, "K required")

    for phrase in [
        "TypedCechHYMSupportNonPromotionTheorem",
        "Gap-layer Cech/trace data cannot fill the `8` connection-value fields",
        "Model-active HYM/Galerkin data cannot be promoted",
        "Lifted Route-C flags cannot be promoted",
        "The `29` missing U1/Y connection-witness leaves",
        "`9/10`",
        NEXT,
    ]:
        require(phrase in note, f"note missing {phrase}")

    print(
        "AUDIT_PASS: old Cech/HYM/Route-C support rejected as final selected connection values."
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
