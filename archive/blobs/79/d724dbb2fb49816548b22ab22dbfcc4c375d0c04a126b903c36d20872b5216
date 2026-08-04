"""Audit finite rhoE-to-oriented-BN or smooth EQa representative frontier packet."""

from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SLUG = "selected_finiterhoetoorientedbnfunctor_or_smootheqarepresentative_or_directhkrow"
DATA = ROOT / "candidate_data" / f"{SLUG}.candidate.json"
PACKET_DIR = ROOT / "candidate_data" / SLUG
FUNCTOR_GATE = PACKET_DIR / "finite_rhoe_to_oriented_bn_functor_gate.packet.json"
LOGDET_GATE = PACKET_DIR / "bn27_sourceowned_logdet_gate.packet.json"
VALIDATOR_GATE = PACKET_DIR / "bn27_validator_export_transport_gate.packet.json"
NEXT_CONTRACT = PACKET_DIR / "next_source_amendment_or_connection_values_contract.packet.json"
CERT = ROOT / "certificates" / f"{SLUG}_certificate.json"
NOTE = ROOT / "proof_corpus" / "MTT_Selected_FiniteRhoEToOrientedBNFunctor_or_SmoothEQaRepresentative_or_DirectHKRow_v1.md"
BUILDER = ROOT / "scripts" / f"build_{SLUG}.py"

STATUS = (
    "MTT_SELECTED_FINITERHOETOORIENTEDBNFUNCTOR_OR_SMOOTHEQAREPRESENTATIVE_"
    "OR_DIRECTHKROW_REDUCED_TO_SOURCE_AMENDMENT_OR_CONNECTION_VALUES"
)
NEXT = "MTT_Selected_SourceBranchIdentity_SourceAmendment_or_SelectedConnectionValues_or_DirectHKRow_v1"


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
    functor = load(FUNCTOR_GATE)
    logdet = load(LOGDET_GATE)
    validator = load(VALIDATOR_GATE)
    contract = load(NEXT_CONTRACT)
    cert = load(CERT)
    note = NOTE.read_text(encoding="utf-8")

    for label, packet in [
        ("candidate", data),
        ("functor gate", functor),
        ("logdet gate", logdet),
        ("validator gate", validator),
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
        "finite_rhoE_to_oriented_BN_orientation_functor_closed",
        "direct_finitepart_arithmetic_log92160000_closed",
        "conditional_implication_theorem_closed",
        "bare_source_name_rejected_as_closure",
        "validator_export_acceptance_contract_built",
        "validator_dependency_collapse_built",
        "sourcebranch_three_clause_cutset_built",
        "sourceidentity_transport_reduced_to_single_leaf",
        "sourcebranch_current_source_nogo",
    ]:
        require(decision[key] is True, f"decision support missing {key}")
    require(decision["single_remaining_leaf"] == "source_branch_identity", "single leaf")
    require(decision["validator_support_ready_count"] == 6, "support validators")
    require(decision["validator_selected_export_owned_count"] == 1, "owned validators")
    require(decision["validator_open_count"] == 5, "open validators")
    require(decision["sourcebranch_support_count"] == 3, "sourcebranch support")
    require(decision["sourcebranch_required_clause_count"] == 3, "sourcebranch required")
    require(decision["sourcebranch_emitted_count"] == 0, "sourcebranch emitted")
    require(decision["accepted_selected_K_source_row_count"] == 9, "K count")
    require(decision["selected_K_threshold_row_count_required"] == 10, "K required")
    for key in [
        "threshold_magnitude_functor_closed",
        "smooth_representative_emitted",
        "source_owned_logdet_closed",
        "source_object_named_S_QaSU3_BN27",
        "source_branch_identity_closed",
        "selected_connection_values_closed",
        "selected_connection_witness_export_closed",
        "oriented_logdet_promoted",
        "selected_K_threshold_Omega_H_lambda",
        "strict_H_K_threshold_row_emitted",
        "full_no_knob_closed",
        "true_SM_equivalence_closed",
    ]:
        require(decision[key] is False, f"decision overclosed {key}")

    orientation = functor["orientation_functor"]
    require(orientation["finite_rhoE_to_oriented_BN_orientation_functor_closed"] is True, "orientation functor")
    require(orientation["threshold_magnitude_functor_closed"] is False, "magnitude functor")
    require(orientation["finitepart_trace_identity_closed"] is False, "finitepart functor")
    shadow = functor["rho_shadow_functor"]
    require(shadow["rho_shadow_embedding_retained"] is True, "rho shadow")
    require(shadow["operator_intertwiner_closed"] is False, "operator no")
    smooth = functor["smooth_representative"]
    require(smooth["finite_candidate_values_replayed"] is True, "finite replay")
    require(smooth["smooth_heterotic_representative_emitted"] is False, "smooth no")

    arithmetic = logdet["direct_finitepart_arithmetic"]
    require(arithmetic["direct_finitepart_arithmetic_closed"] is True, "arithmetic")
    require(arithmetic["source_owned_finitepart_functional_closed"] is False, "source owned functional")
    owned = logdet["sourceowned_logdet"]
    require(owned["sourceowned_logdet_minimal_packet_built"] is True, "minimal logdet packet")
    require(owned["source_owned_logdet_closed"] is False, "owned logdet")
    fill = logdet["minimal_emission_fill"]
    require(fill["conditional_implication_theorem_closed"] is True, "conditional implication")
    require(fill["source_amendment_template_built"] is True, "source amendment")

    source_decl = validator["source_object_declaration"]
    require(source_decl["source_object_declaration_interface_built"] is True, "decl interface")
    require(source_decl["bare_source_name_rejected_as_closure"] is True, "bare rejected")
    require(source_decl["direct_source_object_declaration_closed"] is False, "decl no")
    decl_fill = validator["declaration_fill"]
    require(decl_fill["u1y_routec_support_imported_for_compatibility"] is True, "U1Y support")
    export = validator["validator_export"]
    require(export["support_ready_count"] == 6, "support ready")
    require(export["selected_export_owned_count"] == 1, "owned export")
    require(export["open_validator_count"] == 5, "open export")
    reduction = validator["validator_reduction"]
    require(reduction["audit_replay_validator_closed"] is True, "audit replay validator")
    require(reduction["operator_coemission_conditional_closed"] is True, "operator conditional")
    require(reduction["sourcebranch_emitted_clause_count"] == 0, "sourcebranch emitted")
    require(reduction["sourcebranch_required_clause_count"] == 3, "sourcebranch required")
    conn = validator["connection_witness_fill"]
    require(conn["audit_replay_export_filled"] is True, "audit replay export")
    require(conn["export_filled_count"] == 1, "export filled")
    require(conn["export_required_count"] == 6, "export required")
    transport = validator["source_identity_transport"]
    require(transport["minimal_packet_built"] is True, "minimal packet")
    require(transport["primary_route_selected"] == "source_identity_transport", "primary route")
    require(transport["transport_reduced_to_single_leaf"] is True, "transport reduced")
    require(transport["single_remaining_leaf"] == "source_branch_identity", "leaf")
    require(transport["operator_coemission_conditional_closed"] is True, "operator conditional transport")
    require(transport["no_lift_replay_conditional_closed"] is True, "no lift conditional")
    direct = validator["direct_bn27_fill"]
    require(direct["DE_gap_Riesz_Green_export_support_closed"] is True, "DE support")
    require(direct["typed_connection_witness_values_found"] is False, "typed values not found")
    branch = validator["sourcebranch_nogo"]
    require(branch["sourcebranchidentity_attempted"] is True, "sourcebranch attempted")
    require(branch["current_source_nogo"] is True, "sourcebranch no-go")
    require(branch["support_count"] == 3, "sourcebranch support")
    require(branch["emitted_count"] == 0, "sourcebranch emitted no")
    require(branch["repair_packet_built"] is True, "repair packet")

    require(contract["status"] == "SOURCE_AMENDMENT_OR_SELECTED_CONNECTION_VALUES_REQUIRED", "contract status")
    require(contract["strict_K_threshold_count"] == {"accepted": 9, "required": 10}, "contract count")
    for phrase in [
        "finite rhoE to oriented BN orientation functor closed",
        "source identity transport proof reduced to source_branch_identity",
        "current-source no-go for source_branch_identity proved with exact repair packet",
    ]:
        require(phrase in contract["closed_now"], f"closed phrase missing {phrase}")
    for phrase in [
        "source amendment naming and owning S_QaSU3^BN27",
        "selected connection values exporting the same BN27 validator fields",
        "direct K_threshold.Omega_H.lambda source row",
    ]:
        require(any(phrase in item for item in contract["still_open"]), f"open phrase missing {phrase}")

    for phrase in [
        "FiniteRhoEToOrientedBNOrSmoothEQaReductionTheorem",
        "`log(92160000)`",
        "`source_branch_identity`",
        "`9/10`",
        NEXT,
    ]:
        require(phrase in note, f"note missing {phrase}")

    print(
        "AUDIT_PASS: finite rhoE orientation and BN27 arithmetic closed; source-branch no-go reduces frontier to source amendment or connection values."
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
