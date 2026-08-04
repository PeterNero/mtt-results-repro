"""Audit BN27 connection-source values / physical determinant frontier packet."""

from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SLUG = "selected_bn27connectionsourcevalues_or_physicalalphaactionunitdeterminanttable_or_directhkrow"
DATA = ROOT / "candidate_data" / f"{SLUG}.candidate.json"
PACKET_DIR = ROOT / "candidate_data" / SLUG
BN27_LANE = PACKET_DIR / "bn27_source_transport_or_connection_values_lane.packet.json"
DETERMINANT_LANE = PACKET_DIR / "physical_determinant_finitepart_or_action_unit_lane.packet.json"
NEXT_CUTSET = PACKET_DIR / "next_cutset_after_bn27_values_physical_determinant.packet.json"
CERT = ROOT / "certificates" / f"{SLUG}_certificate.json"
NOTE = ROOT / "proof_corpus" / "MTT_Selected_BN27ConnectionSourceValues_or_PhysicalAlphaActionUnitDeterminantTable_or_DirectHKRow_v1.md"
BUILDER = ROOT / "scripts" / f"build_{SLUG}.py"

STATUS = (
    "MTT_SELECTED_BN27CONNECTIONSOURCEVALUES_OR_PHYSICALALPHAACTIONUNITDETERMINANTTABLE_"
    "CONTRACTED_TO_SOURCEIDENTITY_FINITEPARTPOLICY_OR_DIRECTHKROW"
)
NEXT = "MTT_Selected_SourceIdentityTransportProofAttempt_or_FinitePartPolicyIndexScaleSourceTheorem_or_DirectHKRow_v1"


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
    bn27 = load(BN27_LANE)
    determinant = load(DETERMINANT_LANE)
    cutset = load(NEXT_CUTSET)
    cert = load(CERT)
    note = NOTE.read_text(encoding="utf-8")

    for label, packet in [
        ("candidate", data),
        ("BN27 lane", bn27),
        ("determinant lane", determinant),
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
        "BN27_minimal_source_identity_transport_packet_built",
        "finite_projected_hessian_log2008_closed_as_support",
        "u1y_quotient_determinant_lemma_proved",
        "factorized_threshold_operator_constructed",
        "minimal_finitepart_payload_partially_filled",
        "direct_HK_exit_still_allowed",
    ]:
        require(decision[key] is True, f"decision support missing {key}")
    require(decision["BN27_source_fields_probed"] == 11, "source fields probed")
    require(decision["BN27_connection_fields_probed"] == 8, "connection fields probed")
    require(decision["BN27_source_fields_filled"] == 0, "source fields filled")
    require(decision["BN27_connection_fields_filled"] == 0, "connection fields filled")
    require(decision["accepted_selected_K_source_row_count"] == 9, "K row count")
    require(decision["selected_K_threshold_row_count_required"] == 10, "required K rows")
    for key in [
        "BN27_source_identity_transport_closed",
        "S_QaSU3_BN27_declared_as_selected_source",
        "selected_connection_values_closed",
        "factorized_threshold_operator_selected_as_source",
        "regularization_finite_part_selected",
        "index_weights_promoted_to_determinant_weights",
        "determinant_scale_selected",
        "selected_p_a_promoted",
        "lambda_12_closed",
        "physical_alpha_action_unit_or_Omega0_closed",
        "selected_R_H_RG_emitted",
        "selected_K_threshold_Omega_H_lambda",
        "strict_H_K_threshold_row_emitted",
        "full_no_knob_closed",
        "true_SM_equivalence_closed",
    ]:
        require(decision[key] is False, f"decision overclosed {key}")

    minimal = bn27["minimal_source_identity_transport"]
    require(minimal["minimal_packet_built"] is True, "minimal packet")
    require(minimal["support_prefilter_passes"] is True, "support prefilter")
    require(minimal["primary_route_selected"] == "source_identity_transport", "primary route")
    for key in [
        "proof_object_emitted",
        "source_identity_transport_closed",
        "typed_connection_values_closed",
        "direct_connection_values_closed",
        "selected_connection_witness_export_closed",
    ]:
        require(minimal[key] is False, f"minimal transport overclosed {key}")
    repair = bn27["sourcebranch_repair"]
    require(repair["repair_attack_executed"] is True, "repair executed")
    require(repair["projective_rhoE_primary"] is True, "projective primary")
    require(repair["projective_finite_candidate_available"] is True, "finite candidate")
    for key in [
        "projective_BN27_lift_closed",
        "BN27_domain_emission_closed",
        "source_branch_identity_closed",
        "source_identity_transport_closed",
        "selected_connection_witness_export_closed",
    ]:
        require(repair[key] is False, f"repair overclosed {key}")
    template = bn27["source_or_connection_template"]
    require(template["template_built"] is True, "template built")
    require(template["current_fill_built"] is True, "current fill")
    require(template["source_object_required_field_count"] == 11, "source required")
    require(template["source_object_filled_field_count"] == 0, "source filled")
    require(template["connection_values_required_field_count"] == 8, "connection required")
    require(template["connection_values_filled_field_count"] == 0, "connection filled")
    require(template["source_amendment_closed"] is False, "source amendment")
    require(template["connection_values_closed"] is False, "connection values")
    probe = bn27["field_probe"]
    require(probe["attempt_executed"] is True, "probe executed")
    require(probe["source_support_fields_probed"] == 11, "source probe")
    require(probe["connection_support_fields_probed"] == 8, "connection probe")
    require(probe["source_object_filled_field_count"] == 0, "probe source filled")
    require(probe["connection_values_filled_field_count"] == 0, "probe connection filled")
    require(probe["minimal_missing_theorem_built"] is True, "missing theorem")
    require(probe["source_object_payload_closed"] is False, "source payload")
    require(probe["connection_value_payload_closed"] is False, "connection payload")
    boundary = bn27["u1y_import_and_transport_boundary"]
    require(boundary["u1y_routec_support_imported_for_compatibility"] is True, "U1Y support")
    require(boundary["branch_certificate_closed"] is True, "branch cert")
    for key in [
        "finite_routec_solve_export_to_BN27_closed",
        "same_source_export_to_BN27_validators",
        "source_object_named_S_QaSU3_BN27",
        "projective_rhoE_lift_reopened",
        "BN27_source_ownership_transport_closed",
        "transport_witness_values_found",
        "S_QaSU3_BN27_declared_as_selected_source",
    ]:
        require(boundary[key] is False, f"boundary overclosed {key}")

    finite = determinant["finite_support"]
    require(finite["finite_projected_hessian_zeta_determinant"] == "CLOSED_LOG_2008", "log2008")
    require(
        finite["orbit_democracy_weight_source_selection"]
        == "CLOSED_FOR_FINITE_GALERKIN_TRACE_BRANCH",
        "orbit democracy",
    )
    require(finite["finite_response_payload"] == "CLOSED_TRACE_PROJECTOR_AND_TAU_SQUARED", "finite response")
    require(finite["smooth_threshold_spectral_table"] == "OPEN", "smooth spectrum")
    require(finite["smooth_source_operator"] == "OPEN", "smooth operator")
    require(finite["smooth_threshold_determinant_operator"] == "OPEN", "smooth det")
    q = determinant["quotient_and_factorized_operator"]
    require(q["algebraic_quotient_determinant_lemma_proved"] is True, "quotient lemma")
    require(q["quotient_positive_spectrum_computed"] is True, "positive spectrum")
    require(q["matches_previous_Pperp_weighted_value"] is True, "Pperp match")
    require(q["quotient_logdet"] == 29.201650332199108, "quotient logdet")
    require(q["factorized_operator_matrix_constructed"] is True, "factorized matrix")
    require(q["quotient_operator_matrix_constructed"] is True, "quotient matrix")
    require(q["factorization_matches_27mode_spectrum"] is True, "factorization match")
    require(q["selected_source_emission_closed"] is False, "selected source")
    require(q["hypercharge_index_Dynkin_weights_closed"] is False, "weights")
    require(q["typed_convention_map_closed"] is False, "convention")
    m = determinant["minimal_finitepart_payload"]
    for key in [
        "source_identity_for_DE_gap_layer_filled",
        "V_mod_s_positive_table_computed_conditionally",
        "H_zero_cluster_currently_logdet_neutral",
        "kernel_policy_partially_filled",
    ]:
        require(m[key] is True, f"minimal finitepart support {key}")
    for key in [
        "regularization_finite_part_selected",
        "index_weights_promoted_to_determinant_weights",
        "determinant_scale_selected",
        "selected_p_a_promoted",
    ]:
        require(m[key] is False, f"minimal finitepart overclosed {key}")
    gate = determinant["source_theorem_gate"]
    for key in [
        "route_a_selected_abase_emission_closed",
        "route_b_direct_bn_functional_closed",
        "conditional_quotient_logdet_promoted",
        "Qa_stack_route_promoted",
        "direct_pY_route_promoted",
        "selected_Qa_or_pY_source_payload_found",
        "selected_U1Y_determinant_functional_closed",
        "determinant_functional_source_theorem_found",
        "Pperp_weighting_promoted",
        "u1_hypercharge_spectrum_closed",
        "Pperp_quotient_identity_promoted",
    ]:
        require(gate[key] is False, f"gate overclosed {key}")
    require(gate["conditional_quotient_logdet_carried"] == 29.201650332199108, "carried logdet")
    boundary = determinant["lambda_and_physical_boundary"]
    for key in [
        "lambda_12_closed",
        "measured_electroweak_closure",
        "full_Qa_SU3_threshold_closure_now",
        "physical_action_unit_or_alpha_closed",
    ]:
        require(boundary[key] is False, f"physical boundary overclosed {key}")

    require(
        cutset["status"] == "NEXT_FRONTIER_SOURCEIDENTITY_TRANSPORT_OR_FINITEPART_POLICY_OR_DIRECT_HK_ROW",
        "cutset status",
    )
    require(cutset["next_required_artifact"] == NEXT, "cutset next")
    for phrase in [
        "BN27 support probe covers 11 source fields and 8 connection fields",
        "U1/Y quotient determinant lemma computes logdet 29.201650332199108",
        "concrete factorized A_base tensor I_3 quotient operator constructed",
    ]:
        require(phrase in cutset["closed_here"], f"closed phrase missing {phrase}")
    for phrase in [
        "source-identity transport proof object with three sublemmas",
        "selected connection-value payload filling 8 fields",
        "regularization finite part selected as electroweak finite part",
        "direct source-native K_threshold.Omega_H.lambda",
    ]:
        require(phrase in cutset["still_open"], f"open phrase missing {phrase}")

    for phrase in [
        "BN27ConnectionValuesOrFinitePartPolicyReductionTheorem",
        "`11` direct source fields",
        "`8` fields",
        NEXT,
    ]:
        require(phrase in note, f"note missing {phrase}")

    print(
        "AUDIT_PASS: BN27 source-value fields and determinant finitepart policy frontier contracted; H row open."
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
