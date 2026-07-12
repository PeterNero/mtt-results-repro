"""Audit flat-torsion / BN27 source-values / physical-Omega0 frontier packet."""

from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SLUG = "selected_flattorsionsmoothpromotion_or_selectedbundleabn27source_or_physicalomega0"
DATA = ROOT / "candidate_data" / f"{SLUG}.candidate.json"
PACKET_DIR = ROOT / "candidate_data" / SLUG
FLAT_LANE = PACKET_DIR / "flat_torsion_smooth_promotion_lane.packet.json"
BN27_LANE = PACKET_DIR / "bn27_source_values_or_connection_tables_lane.packet.json"
PHYSICAL_LANE = PACKET_DIR / "physical_omega0_alpha_determinant_lane.packet.json"
NEXT_CUTSET = PACKET_DIR / "next_cutset_after_flat_bn27_physicalomega0.packet.json"
CERT = ROOT / "certificates" / f"{SLUG}_certificate.json"
NOTE = ROOT / "proof_corpus" / "MTT_Selected_FlatTorsionSmoothPromotion_or_SelectedBundleAOrBN27Source_or_PhysicalOmega0_or_DirectHKRow_v1.md"
BUILDER = ROOT / "scripts" / f"build_{SLUG}.py"

STATUS = (
    "MTT_SELECTED_FLATTORSIONSMOOTHPROMOTION_OR_SELECTEDBUNDLEABN27SOURCE_OR_"
    "PHYSICALOMEGA0_REDUCED_TO_SOURCEVALUES_ALPHA_OR_DIRECTHKROW"
)
NEXT = "MTT_Selected_BN27ConnectionSourceValues_or_PhysicalAlphaActionUnitDeterminantTable_or_DirectHKRow_v1"


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
    flat = load(FLAT_LANE)
    bn27 = load(BN27_LANE)
    physical = load(PHYSICAL_LANE)
    cutset = load(NEXT_CUTSET)
    cert = load(CERT)
    note = NOTE.read_text(encoding="utf-8")

    for label, packet in [
        ("candidate", data),
        ("flat lane", flat),
        ("BN27 lane", bn27),
        ("physical lane", physical),
        ("next cutset", cutset),
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
        "flat_torsion_validators_closed",
        "direct_finite_internal_operator_payload_closed",
        "BN27_validator_dependency_collapse_built",
        "central_rank_operator_intertwiner_support_closed",
        "finite_DE_Riesz_Green_gap_layer_promoted_as_support",
        "physical_alpha_action_unit_reduction_built",
        "direct_HK_exit_still_allowed",
    ]:
        require(decision[key] is True, f"decision support missing {key}")
    for key in [
        "smooth_flat_torsion_source_promoted",
        "selected_bundle_A_emitted",
        "direct_BN27_source_emitted",
        "BN27_source_branch_identity_closed",
        "BN27_source_emission_theorem_closed",
        "selected_connection_tables_closed",
        "selected_connection_witness_constructed",
        "central_rank_operator_source_selected",
        "full_finite_HYM_connection_solve_closed",
        "A_selected_or_b_selected_emitted",
        "lambda_12_closed_or_computable",
        "physical_Omega0_closed",
        "selected_local_determinant_table_closed",
        "full_physical_electroweak_closure",
        "selected_R_H_RG_emitted",
        "selected_K_threshold_Omega_H_lambda",
        "strict_H_K_threshold_row_emitted",
        "full_no_knob_closed",
        "true_SM_equivalence_closed",
    ]:
        require(decision[key] is False, f"decision overclosed {key}")
    require(decision["accepted_selected_K_source_row_count"] == 9, "K row count")
    require(decision["selected_K_threshold_row_count_required"] == 10, "required K rows")

    validators = flat["formal_transition_validators"]
    for key in [
        "symbolic_smooth_transition_template_built",
        "exact_B_plus_flat_torsion_split_consistent",
        "formal_cocycle_law_passes",
        "formal_products_cancel_to_P",
        "formal_unitarity_passes_for_scalar_U1_phases",
    ]:
        require(validators[key] is True, f"flat validator missing {key}")
    require(validators["smooth_source_promoted"] is False, "flat source overpromoted")
    require(
        validators["smooth_transition_tables_source_selected"] is False,
        "transition tables overselected",
    )
    sourcegap = flat["sourcegap_fork"]
    require(sourcegap["lane_A_current_source_nogo"] is True, "sourcegap no-go")
    require(sourcegap["lane_A_formal_validators_pass"] is True, "sourcegap validators")
    require(sourcegap["lane_B_direct_operator_acceptance_template_built"] is True, "template")
    require(sourcegap["lane_A_smooth_source_closed"] is False, "smooth lane overclosed")
    require(sourcegap["direct_operator_payload_closed"] is False, "fork overclosed")
    internal = flat["direct_finite_internal_payload"]
    require(internal["direct_finite_internal_operator_payload_closed"] is True, "finite payload")
    require(
        internal["all_acceptance_fields_filled_at_finite_internal_scope"] is True,
        "finite fields",
    )
    require(internal["selected_internal_logdet_retained"] is True, "internal logdet")
    require(internal["smooth_operator_identity_closed"] is False, "smooth identity")
    require(internal["physical_threshold_normalization_closed"] is False, "physical norm")

    first = bn27["first_leaf_attempt"]
    require(first["attempt_executed"] is True, "first leaf")
    for key in [
        "direct_BN27_source_emitted",
        "selected_bundle_A_emitted",
        "finite_projective_rhoE_promoted_to_smooth_A",
        "standard_embedding_promoted",
        "smooth_EQa_quotient_closed",
    ]:
        require(first[key] is False, f"first leaf overclosed {key}")
    orbit = bn27["orbitclosure_and_export"]
    require(orbit["compatibility_closed"] is True, "orbit compatibility")
    require(orbit["audit_replay_closed"] is True, "orbit replay")
    require(orbit["filled_count"] == 2, "orbit filled count")
    require(orbit["required_count"] == 7, "orbit required count")
    require(orbit["BN27_orbitclosure_source_bridge_closed"] is False, "orbit bridge")
    require(orbit["open_validator_count"] == 5, "open validators")
    require(orbit["support_ready_count"] == 6, "support validators")
    require(orbit["same_source_export_to_BN27_validators"] is False, "export overclosed")
    require(orbit["selected_connection_values_closed"] is False, "connection values")
    collapse = bn27["validator_dependency_collapse"]
    require(collapse["audit_replay_validator_closed"] is True, "audit validator")
    require(collapse["operator_coemission_conditional_closed"] is True, "operator conditional")
    require(collapse["sourcebranch_three_clause_cutset_built"] is True, "three-clause")
    require(collapse["sourcebranch_emitted_clause_count"] == 0, "emitted clauses")
    require(collapse["sourcebranch_required_clause_count"] == 3, "required clauses")
    require(
        collapse["five_validator_bundle_unconditional_closed"] is False,
        "validator bundle overclosed",
    )
    three = bn27["sourcebranch_three_clause"]
    require(three["source_amendment_packet_built"] is True, "source amendment")
    require(three["support_count"] == 3, "support count")
    require(three["required_clause_count"] == 3, "required clause count")
    require(three["emitted_count"] == 0, "emitted count")
    for key in [
        "one_source_owns_both_branches",
        "full_BN27_carrier_emitted",
        "routec_internalized",
        "selected_connection_solve_closed",
    ]:
        require(three[key] is False, f"three-clause overclosed {key}")
    root = bn27["root_cutset"]
    require(root["root_cutset_built"] is True, "root cutset")
    for key in [
        "all_minimal_roots_closed",
        "selected_trace_equality_proved",
        "full_selected_operator_formula_proved",
        "theorem_derived_selected_source_flags",
        "source_object_named_S_QaSU3_BN27",
        "connection_values_external_construction_closed",
    ]:
        require(root[key] is False, f"root overclosed {key}")
    legal = bn27["minimal_legal_closure_forms"]
    require(legal["direct_theorem_skeleton_built"] is True, "direct skeleton")
    require(legal["direct_open_statement_count"] == 6, "direct statement count")
    require(legal["connection_tables_schema_built"] is True, "schema")
    require(legal["connection_open_table_count"] == 8, "table count")
    require(legal["conditional_replay_ready"] is True, "conditional replay")
    require(legal["direct_theorem_closed"] is False, "direct theorem")
    require(legal["connection_tables_closed"] is False, "tables")
    require(legal["same_source_export_to_BN27_validators"] is False, "same-source")
    conn = bn27["connection_witness_and_bundle_lanes"]
    require(conn["DE_gap_Riesz_Green_export_support_closed"] is True, "DE export support")
    require(conn["audit_replay_export_filled"] is True, "audit export")
    require(conn["export_filled_count"] == 1, "export filled")
    require(conn["export_required_count"] == 6, "export required")
    require(conn["finite_internal_projective_packet_promoted_for_internal_scope"] is True, "internal promote")
    require(conn["rhoE_character_intertwines"] is True, "rhoE character")
    require(conn["central_rank_operator_candidate_intertwines"] is True, "central rank")
    for key in [
        "direct_source_identity_transport_closed",
        "selected_connection_witness_export_closed",
        "same_source_identity_proved",
        "explicit_bundle_connection_solved",
        "same_source_PhiFin_identity_proved",
        "smooth_operator_identity_closed",
        "D_E_or_EQa_intertwines",
        "central_rank_operator_source_selected",
    ]:
        require(conn[key] is False, f"connection lane overclosed {key}")
    u1 = bn27["u1y_routec_connection_support"]
    require(u1["accepts_three_equivalent_witness_routes"] is True, "witness routes")
    require(u1["payload_missing_leaf_count"] == 29, "missing leaves")
    require(u1["finite_DE_gap_layer_promoted"] is True, "finite DE promoted")
    require(u1["DE_action_closed_for_gap_layer"] is True, "DE action")
    require(u1["Riesz_Green_gap_layer_closed"] is True, "Riesz/Green")
    for key in [
        "selected_connection_witness_constructed",
        "full_finite_HYM_connection_solve_closed",
        "A_selected_or_b_selected_emitted",
        "lambda_12_computable",
        "dotD_alpha1_source_closed",
    ]:
        require(u1[key] is False, f"U1 support overclosed {key}")

    pprev = physical["previous_physical_anchor_gate"]
    for key in [
        "physical_anchor_closed",
        "threshold_vector_closed",
        "physical_electroweak_matching_closed",
        "convention_reconciliation_closed",
    ]:
        require(pprev[key] is False, f"physical previous overclosed {key}")
    dual = physical["dual_attack"]
    require(dual["lane_A_reduced_to_selected_spectral_table"] is True, "lambda table reduction")
    require(dual["lane_B_reduced_to_alpha_phys_only"] is True, "Omega alpha reduction")
    require(dual["lane_A_lambda12_closed"] is False, "lambda12")
    require(dual["lane_B_Omega0_closed"] is False, "Omega0")
    require(dual["full_physical_electroweak_closure"] is False, "EW closure")
    for obj in [
        "Selected_Gauge_Factor_Spectral_Table_v1",
        "Selected_Physical_Alpha_or_Action_Unit_Theorem_v1",
        "Typed_Electroweak_Convention_Map_and_RG_Scheme_v1",
    ]:
        require(obj in dual["next_required_objects"], f"missing physical object {obj}")
    qa = physical["qastack_support_boundary"]
    require(qa["nonidentity_rhoE_BN_prefix_imported"] is True, "rhoE prefix")
    require(qa["prefix_can_host_threshold_operator"] is True, "prefix host")
    require(qa["selected_DE_gap_trace_equality_closed"] is True, "trace equality support")
    require(qa["DE_gap_Riesz_Green_layer_closed"] is True, "DE gap support")
    for key in [
        "threshold_operator_identity_closed",
        "quotient_functor_closed",
        "A_base_tensor_I3_identity_closed",
        "Qa_stack_weights_and_scale_policy_closed",
        "full_threshold_operator_formula_closed",
        "lambda_12_closed",
    ]:
        require(qa[key] is False, f"Qa-stack overclosed {key}")

    require(
        cutset["status"] == "NEXT_FRONTIER_BN27_SOURCE_VALUES_ALPHA_ACTION_UNIT_OR_DIRECT_HK_ROW",
        "cutset status",
    )
    require(cutset["next_required_artifact"] == NEXT, "cutset next")
    for phrase in [
        "direct finite internal projective rhoE operator payload closed at finite internal scope",
        "BN27 validator dependency collapsed to source-branch identity or selected connection values",
        "physical Omega0 lane reduced to alpha_phys/action-unit plus local determinant spectral table",
    ]:
        require(phrase in cutset["closed_here"], f"closed phrase missing {phrase}")
    for phrase in [
        "direct source object S_QaSU3^BN27 with full carrier/operator/provenance ownership",
        "six direct BN27 source-emission statements or eight selected connection-table families",
        "physical alpha/action-unit theorem or Omega0/K_phys anchor",
        "direct source-native K_threshold.Omega_H.lambda",
    ]:
        require(phrase in cutset["still_open"], f"open phrase missing {phrase}")

    for phrase in [
        "FlatTorsionBN27SourceValuesOrPhysicalOmega0ReductionTheorem",
        "six source-emission statements",
        "eight selected connection-table families",
        NEXT,
    ]:
        require(phrase in note, f"note missing {phrase}")

    print(
        "AUDIT_PASS: flat torsion, BN27 source, and physical Omega0 lanes reduced to source values/action-unit/table cutset; H row open."
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
