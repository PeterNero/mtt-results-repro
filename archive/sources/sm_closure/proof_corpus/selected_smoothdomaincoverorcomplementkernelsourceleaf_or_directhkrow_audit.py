"""Audit smooth-domain cover/complement-kernel source leaf or direct H K-row packet."""

from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SLUG = "selected_smoothdomaincoverorcomplementkernelsourceleaf_or_directhkrow"
DATA = ROOT / "candidate_data" / f"{SLUG}.candidate.json"
PACKET_DIR = ROOT / "candidate_data" / SLUG
S1_EQUATIONS = PACKET_DIR / "s1_chartatlas_localfield_equation_reduction.packet.json"
INTERNAL_BOUNDARY = PACKET_DIR / "direct_operator_internal_boundary_and_physical_request.packet.json"
ORIENTED_SUPPORT = PACKET_DIR / "oriented_phifin_smootheqa_support_import.packet.json"
NEXT_CUTSET = PACKET_DIR / "next_cutset_after_s1_source_leaf.packet.json"
CERT = ROOT / "certificates" / f"{SLUG}_certificate.json"
NOTE = ROOT / "proof_corpus" / "MTT_Selected_SmoothDomainCoverOrComplementKernelSourceLeaf_or_DirectHKRow_v1.md"
BUILDER = ROOT / "scripts" / f"build_{SLUG}.py"

STATUS = (
    "MTT_SELECTED_SMOOTHDOMAINCOVERORCOMPLEMENTKERNELSOURCELEAF_OR_DIRECTHKROW_"
    "S1_EQUATIONS_DH_AND_INTERNAL_BOUNDARY_CLOSED_SOURCE_VALUES_OPEN"
)
NEXT = "MTT_Selected_CoverHomotopyOrSmoothEQaSourceCertificate_or_PhysicalGaugeAnchor_or_DirectHKRow_v1"


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
    s1 = load(S1_EQUATIONS)
    boundary = load(INTERNAL_BOUNDARY)
    oriented = load(ORIENTED_SUPPORT)
    cutset = load(NEXT_CUTSET)
    cert = load(CERT)
    note = NOTE.read_text(encoding="utf-8")

    for label, packet in [
        ("candidate", data),
        ("S1 equations", s1),
        ("internal boundary", boundary),
        ("oriented support", oriented),
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
        "S1_equation_packet_built",
        "dH_zero_and_conditional_local_potentials_closed",
        "internal_complement_quotient_policy_closed",
        "physical_or_smooth_source_request_built",
        "typed_EW_convention_and_weak_split_imported",
        "oriented_PhiFin_exact_table_support_imported",
        "BN_signed_operator_identity_support_imported",
        "direct_HK_exit_still_allowed",
    ]:
        require(decision[key] is True, f"decision missing support {key}")
    for key in [
        "selected_smooth_cover_or_homotopy_emitted",
        "local_Deligne_Cech_values_emitted",
        "smooth_EQa_or_trace_identity_closed",
        "positive_finitepart_source_identity_closed",
        "physical_Kphys_or_normalization_closed",
        "selected_R_H_RG_emitted",
        "selected_K_threshold_Omega_H_lambda",
        "strict_H_K_threshold_row_emitted",
        "full_no_knob_closed",
        "true_SM_equivalence_closed",
    ]:
        require(decision[key] is False, f"decision overclosed {key}")
    require(decision["accepted_selected_K_source_row_count"] == 9, "K row count")
    require(decision["selected_K_threshold_row_count_required"] == 10, "required K rows")

    chart = s1["chartatlas_equation_packet"]
    require(chart["equation_packet_built"] is True, "equation packet")
    require(chart["geometry_anchor_promoted_to_known_support"] is True, "geometry support")
    for key in [
        "selected_chart_atlas_emitted",
        "smooth_cover_contractibility_proved",
        "local_field_values_emitted",
        "smooth_tau_shadow_derived",
    ]:
        require(chart[key] is False, f"chart overclosed {key}")
    local = s1["localfield_solve"]
    for key in [
        "dH_computed",
        "dH_closed",
        "conditional_local_potential_lane_live",
        "invariant_dH_zero_check",
        "conditional_poincare_local_potential_existence_theorem",
    ]:
        require(local[key] is True, f"local support missing {key}")
    for key in [
        "selected_cover_emitted",
        "local_B_i_A_ij_g_ijk_values_emitted",
        "smooth_tau_shadow_derived",
        "S1_closed",
    ]:
        require(local[key] is False, f"local overclosed {key}")

    direct = boundary["direct_payload_boundary"]
    require(direct["finite_internal_payload_complete"] is True, "finite payload")
    require(direct["direct_payload_boundary_locked"] is True, "payload boundary")
    require(direct["smooth_identity_lane_selected_next"] is True, "smooth lane selected")
    require(direct["physical_lane_blocked_by_anchor_and_rg"] is True, "physical blocked")
    require(direct["physical_lane_closed"] is False, "physical lane overclosed")
    require(direct["smooth_identity_lane_closed"] is False, "smooth lane overclosed")
    trace = boundary["trace_lift_or_complement"]
    require(trace["internal_complement_quotient_policy_closed"] is True, "internal complement")
    require(trace["selected_internal_logdet_preserved"] is True, "logdet")
    require(trace["trace_lift_current_source_nogo_retained"] is True, "trace nogo")
    for key in [
        "smooth_trace_lift_closed",
        "smooth_EQa_closed",
        "smooth_heat_zeta_torsion_finitepart_computed",
        "physical_normalization_closed",
    ]:
        require(trace[key] is False, f"trace overclosed {key}")
    source = boundary["source_data_request_and_fill"]
    for key in [
        "internal_branch_locked",
        "no_more_internal_computation_required_for_log2008",
        "source_request_built",
        "typed_electroweak_convention_map",
        "internal_weaksplit_threshold_for_physical_lane",
        "Rplus_geometry_support_for_smooth_lane",
        "physical_anchor_still_open",
        "matching_scale_still_open",
        "RG_scheme_still_open",
        "smooth_EQa_still_open",
    ]:
        require(source[key] is True, f"source request state mismatch {key}")
    require(source["preferred_next_lane"] == "physical_gauge_action_anchor_RG_scheme", "preferred lane")

    mag = oriented["oriented_magnitude"]
    require(mag["oriented_table_magnitude_finitepart_computed"] is True, "oriented magnitude")
    require(mag["oriented_abs_sector_logdet_exact"] == "log(92160000)", "abs logdet")
    require(mag["full_positive_logdet_exact"] == "log(884736000000)", "full logdet")
    require(mag["source_owned_positive_PhiFin_magnitude"] is False, "positive source overclosed")
    require(mag["smooth_E_Qa_trace_identity_closed"] is False, "E_Qa trace overclosed")
    threshold = oriented["oriented_threshold_identity"]
    require(threshold["same_domain_commutation_table_complete"] is True, "commutation")
    require(threshold["closed_support_count"] == 7, "support count")
    for key in [
        "source_emission_closed",
        "smooth_E_Qa_threshold_identity_closed",
        "heterotic_threshold_magnitude_promoted",
    ]:
        require(threshold[key] is False, f"threshold overclosed {key}")
    source_fill = oriented["oriented_source_fill"]
    require(source_fill["fill_attempt_executed"] is True, "oriented fill")
    require(source_fill["selected_finite_internal_packet_reused"] is True, "finite reused")
    require(source_fill["oriented_table_reused"] is True, "table reused")
    require(source_fill["required_leaf_count"] == 6, "required leaves")
    require(source_fill["closed_required_leaf_count"] == 0, "closed leaves")
    for key in [
        "source_emission_closed",
        "smooth_EQa_constructed",
        "finite_quotient_identity_constructed",
    ]:
        require(source_fill[key] is False, f"oriented fill overclosed {key}")
    bn = oriented["bn_centralrank"]
    for key in [
        "C_tau_source_selected_as_BN_operator",
        "C_tau_signed_intertwiner_closed",
        "operator_identity_closed_for_signed_layer",
        "chiral_dirac_eta_route_ranked_primary",
    ]:
        require(bn[key] is True, f"BN support missing {key}")
    for key in [
        "operator_identity_closed_for_positive_finitepart_layer",
        "selected_smooth_E_Qa_emitted",
        "positive_finitepart_for_C_tau_closed",
    ]:
        require(bn[key] is False, f"BN overclosed {key}")
    smooth_packet = oriented["smooth_operator_packet_fill"]
    require(smooth_packet["support_context_filled"] is True, "smooth packet support")
    for key in [
        "smooth_operator_source_packet_filled",
        "E_Qa_matrix_filled",
        "projective_rhoE_transition_tables_filled",
        "selected_connection_A_filled",
        "finite_part_value_filled",
    ]:
        require(smooth_packet[key] is False, f"smooth packet overclosed {key}")

    require(
        cutset["status"]
        == "NEXT_FRONTIER_COVER_HOMOTOPY_OR_SMOOTH_EQA_SOURCE_CERTIFICATE_OR_PHYSICAL_GAUGE_ANCHOR",
        "cutset status",
    )
    require(cutset["next_required_artifact"] == NEXT, "cutset next")
    for phrase in [
        "S1 chart-atlas and Deligne/Cech local-field equation packet built",
        "invariant dH=0 check closed",
        "internal complement-quotient policy closed for log(2008)",
        "oriented Phi_fin exact magnitude table imported as support",
        "BN central-rank signed operator identity imported as support",
    ]:
        require(phrase in cutset["closed_here"], f"closed phrase missing {phrase}")
    for phrase in [
        "selected contractible smooth cover and homotopy operator",
        "smooth E_Qa source certificate or equivalent trace identity",
        "physical action unit K_phys or alpha_phys",
        "direct source-native K_threshold.Omega_H.lambda",
    ]:
        require(phrase in cutset["still_open"], f"open phrase missing {phrase}")

    for phrase in [
        "SmoothDomainCoverOrComplementKernelSourceLeafOrDirectHKRowTheorem",
        "Invariant `dH=0` check",
        "BN central-rank signed operator identity",
        NEXT,
    ]:
        require(phrase in note, f"note missing {phrase}")

    print(
        "AUDIT_PASS: S1 equations/dH/internal boundary closed as support; cover, smooth E_Qa, and physical anchor remain open."
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
