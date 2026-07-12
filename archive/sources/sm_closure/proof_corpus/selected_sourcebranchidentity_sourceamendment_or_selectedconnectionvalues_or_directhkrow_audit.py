"""Audit source-branch amendment or selected connection values frontier packet."""

from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SLUG = "selected_sourcebranchidentity_sourceamendment_or_selectedconnectionvalues_or_directhkrow"
DATA = ROOT / "candidate_data" / f"{SLUG}.candidate.json"
PACKET_DIR = ROOT / "candidate_data" / SLUG
AMENDMENT_GATE = PACKET_DIR / "source_amendment_or_connection_values_gate.packet.json"
TRANSPORT_GATE = PACKET_DIR / "bn27_sourceownership_transport_gate.packet.json"
CONNECTION_GATE = PACKET_DIR / "typed_connection_witness_gate.packet.json"
NEXT_CONTRACT = PACKET_DIR / "next_connection_witness_value_payload_contract.packet.json"
CERT = ROOT / "certificates" / f"{SLUG}_certificate.json"
NOTE = ROOT / "proof_corpus" / "MTT_Selected_SourceBranchIdentity_SourceAmendment_or_SelectedConnectionValues_or_DirectHKRow_v1.md"
BUILDER = ROOT / "scripts" / f"build_{SLUG}.py"

STATUS = (
    "MTT_SELECTED_SOURCEBRANCHIDENTITY_SOURCEAMENDMENT_OR_SELECTEDCONNECTIONVALUES_"
    "BRANCHCERT_CLOSED_CONNECTION_WITNESS_VALUES_OPEN"
)
NEXT = "MTT_Selected_TypedCechHYMProjectiveConnectionWitnessValues_or_DirectHKRow_v1"


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
    amendment = load(AMENDMENT_GATE)
    transport = load(TRANSPORT_GATE)
    connection = load(CONNECTION_GATE)
    contract = load(NEXT_CONTRACT)
    cert = load(CERT)
    note = NOTE.read_text(encoding="utf-8")

    for label, packet in [
        ("candidate", data),
        ("amendment", amendment),
        ("transport", transport),
        ("connection", connection),
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

    decision = data["closure_decision"]
    for key in [
        "branch_certificate_closed",
        "source_amendment_template_built",
        "DE_gap_Riesz_Green_export_support_closed",
        "selected_trace_equality_for_27mode_DE_gap_layer_closed",
        "electroweak_internal_finitepart_policy_closed",
        "quotient_finitepart_support_imported",
        "connection_witness_contract_built",
        "accepts_three_equivalent_witness_routes",
    ]:
        require(decision[key] is True, f"decision support missing {key}")
    require(decision["source_object_filled_field_count"] == 0, "source fields filled")
    require(decision["source_object_required_field_count"] == 11, "source fields required")
    require(decision["connection_values_filled_field_count"] == 0, "connection fields filled")
    require(decision["connection_values_required_field_count"] == 8, "connection fields required")
    require(decision["payload_missing_leaf_count"] == 29, "payload missing leaves")
    require(decision["accepted_selected_K_source_row_count"] == 9, "K count")
    require(decision["selected_K_threshold_row_count_required"] == 10, "K required")
    for key in [
        "source_amendment_closed",
        "connection_values_closed",
        "S_QaSU3_BN27_declared_as_selected_source",
        "BN27_source_ownership_transport_closed",
        "selected_connection_witness_values_closed",
        "full_selected_operator_formula_closed",
        "theorem_derived_selected_source_flags",
        "typed_monad_cech_values_present",
        "direct_hym_values_present",
        "finite_routec_solve_values_present",
        "same_source_certificate_present",
        "selected_connection_witness_constructed",
        "oriented_logdet_promoted",
        "selected_K_threshold_Omega_H_lambda",
        "strict_H_K_threshold_row_emitted",
        "full_no_knob_closed",
        "true_SM_equivalence_closed",
    ]:
        require(decision[key] is False, f"decision overclosed {key}")

    repair = amendment["repair_attack"]
    require(repair["primary_lane"] == "selected_connection_values_alternative", "primary lane")
    require(repair["projective_rhoE_primary"] is True, "projective primary")
    require(repair["projective_BN27_lift_closed"] is False, "projective lift")
    template = amendment["source_amendment_template"]
    require(template["source_object_required_field_count"] == 11, "template source required")
    require(template["connection_values_required_field_count"] == 8, "template connection required")
    require(template["source_object_filled_field_count"] == 0, "template source filled")
    require(template["connection_values_filled_field_count"] == 0, "template connection filled")

    ownership = transport["sourceownership_transport"]
    require(ownership["branch_certificate_closed"] is True, "branch certificate")
    require(ownership["S_QaSU3_BN27_declared_as_selected_source"] is False, "S not declared")
    require(ownership["projective_rhoE_lift_reopened"] is False, "rhoe not reopened")
    direct = transport["direct_bn27_fill"]
    require(direct["DE_gap_Riesz_Green_export_support_closed"] is True, "DE export")
    require(direct["typed_connection_witness_values_found"] is False, "typed witness values")
    root = transport["root_cutset"]
    require(root["root_cutset_built"] is True, "root cutset")
    require(root["all_minimal_roots_closed"] is False, "root open")

    trace = connection["trace_root"]
    require(trace["selected_trace_equality_for_27mode_DE_gap_layer_closed"] is True, "trace scoped")
    require(trace["full_selected_operator_formula_closed"] is False, "full formula")
    boundary = connection["full_operator_boundary"]
    require(boundary["electroweak_internal_finitepart_policy_closed"] is True, "EW finitepart")
    require(boundary["quotient_finitepart_support_imported"] is True, "quotient support")
    witness = connection["u1y_connection_witness_contract"]
    require(witness["contract_built"] is True, "witness contract")
    require(witness["accepts_three_equivalent_witness_routes"] is True, "three routes")
    require(witness["payload_missing_leaf_count"] == 29, "witness missing count")
    require(witness["typed_monad_cech_values_present"] is False, "typed absent")
    require(witness["direct_hym_values_present"] is False, "hym absent")
    require(witness["finite_routec_solve_values_present"] is False, "routec absent")
    require(connection["minimal_source_values_packet"]["status"] == "MINIMAL_SOURCE_VALUES_REQUIRED", "minimal packet")
    require(
        connection["external_construction_request"]["status"]
        == "OPEN_EXTERNAL_CONSTRUCTION_VALUES_REQUIRED",
        "external request",
    )

    require(
        contract["status"] == "TYPED_CECH_HYM_PROJECTIVE_CONNECTION_WITNESS_VALUES_REQUIRED",
        "contract status",
    )
    require(contract["strict_K_threshold_count"] == {"accepted": 9, "required": 10}, "contract count")
    for phrase in [
        "heterotic Qa/SU3 branch certificate closed",
        "connection-witness contract built with three equivalent witness routes",
    ]:
        require(phrase in contract["closed_now"], f"closed phrase missing {phrase}")
    for phrase in [
        "S_QaSU3^BN27 declared and source-owned",
        "typed monad/Cech values",
        "direct K_threshold.Omega_H.lambda source row",
    ]:
        require(any(phrase in item for item in contract["still_open"]), f"open phrase missing {phrase}")

    for phrase in [
        "SourceBranchAmendmentOrConnectionWitnessFrontierTheorem",
        "`11` source-object fields",
        "`8` value fields",
        "`29` missing leaves",
        "`9/10`",
        NEXT,
    ]:
        require(phrase in note, f"note missing {phrase}")

    print(
        "AUDIT_PASS: branch certificate closed; source amendment and connection witness values remain the exact frontier."
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
