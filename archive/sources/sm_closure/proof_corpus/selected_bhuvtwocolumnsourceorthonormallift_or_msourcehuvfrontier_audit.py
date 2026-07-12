"""Audit selected B_Huv two-column lift frontier closure."""

from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SLUG = "selected_bhuvtwocolumnsourceorthonormallift_or_msourcehuvfrontier"
DATA = ROOT / "candidate_data" / f"{SLUG}.candidate.json"
PACKET_DIR = ROOT / "candidate_data" / SLUG
BHUV_LIFT = PACKET_DIR / "bhuv_two_column_source_orthonormal_lift.packet.json"
BHUV_REQUEST = PACKET_DIR / "h7b1g_bhuv_request_recheck_after_c4.packet.json"
DIRECT_RECHECK = PACKET_DIR / "direct_huv_functor_recheck_after_bhuv_lift.packet.json"
MSOURCE_FRONTIER = PACKET_DIR / "msource_huv_frontier_after_bhuv_lift.packet.json"
HK_GATE = PACKET_DIR / "hk_threshold_gate_after_bhuv_lift.packet.json"
CUTSET = PACKET_DIR / "next_cutset_after_bhuv_lift.packet.json"
CERT = ROOT / "certificates" / f"{SLUG}_certificate.json"
NOTE = ROOT / "proof_corpus" / "MTT_Selected_BHuvTwoColumnSourceOrthonormalLift_or_MSourceHuvFrontier_v1.md"
BUILDER = ROOT / "scripts" / f"build_{SLUG}.py"

STATUS = (
    "MTT_SELECTED_BHUVTWOCOLUMNSOURCEORTHONORMALLIFT_OR_MSOURCEHUVFRONTIER_"
    "BHUV_LIFT_CLOSED_MSOURCE_HUV_OPEN"
)
NEXT = "MTT_Selected_MSourceHermitianMassStrainOperator_or_C5C6HiggsProjectionBridge_v1"


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
    bhuv = load(BHUV_LIFT)
    request = load(BHUV_REQUEST)
    direct = load(DIRECT_RECHECK)
    msource = load(MSOURCE_FRONTIER)
    hk_gate = load(HK_GATE)
    cutset = load(CUTSET)
    cert = load(CERT)
    note = NOTE.read_text(encoding="utf-8")

    for label, packet in [
        ("candidate", data),
        ("B_Huv lift", bhuv),
        ("B_Huv request recheck", request),
        ("direct Huv recheck", direct),
        ("M_source frontier", msource),
        ("H K gate", hk_gate),
        ("cutset", cutset),
        ("certificate", cert),
    ]:
        guard(packet, label)

    require(data["status"] == STATUS, "candidate status")
    require(cert["status"] == STATUS, "certificate status")
    require(data["next_required_artifact"] == NEXT, "candidate next")
    require(cert["next_required_artifact"] == NEXT, "certificate next")
    require(data["theorem"]["proved"] is True, "theorem flag")
    require(cert["theorem_proved"] is True, "certificate theorem flag")
    require(data["true_SM_equivalence_claimed"] is False, "true SM overclaim")
    require(data["full_no_knob_closure_claimed"] is False, "no-knob overclaim")

    decision = data["closure_decision"]
    for key in [
        "bridge_validator_C1_closed",
        "bridge_validator_C2_closed",
        "bridge_validator_C3_closed",
        "bridge_validator_C4_closed",
        "B_Huv_two_column_uv_lift_emitted",
        "B_Huv_source_orthonormality_certified",
    ]:
        require(decision[key] is True, f"decision should close {key}")
    for key in [
        "B_Huv_numeric_entries_evaluated",
        "selected_Hermitian_M_source_emitted",
        "direct_Herm2_Huv_payload_emitted",
        "direct_Huu_Hud_Hdd_emitted",
        "selected_rank_one_light_projector_emitted",
        "selected_s_beta_value_found",
        "K_threshold_Omega_H_lambda_emitted",
        "ten_K_antecedent_satisfied",
        "strict_Omega_lambda_scalar_execution_closed",
        "true_SM_equivalence_closed",
        "full_no_knob_closed",
    ]:
        require(decision[key] is False, f"decision overclosed {key}")
    require(decision["accepted_selected_K_source_row_count"] == 9, "K selected count")
    require(decision["selected_K_threshold_row_count_required"] == 10, "K required count")
    require(decision["accepted_internal_scalar_value_row_count"] == 0, "scalar count")

    require(bhuv["status"] == "BHUV_TWO_COLUMN_SOURCE_ORTHONORMAL_LIFT_EMITTED_MSOURCE_OPEN", "B_Huv status")
    source_space = bhuv["ordered_two_column_source_space"]
    require(source_space["basis"] == ["H_u", "H_d^dagger"], "ordered basis")
    require(
        source_space["ordered_E_H_UV_source_ids"]["H_u"]
        == "Q_sel^U:E_H_UV:H_u:phi_(0,0)_e0",
        "H_u source id",
    )
    require(
        source_space["ordered_E_H_UV_source_ids"]["H_d_dagger"]
        == "Q_sel^U:E_H_UV:H_d_dagger:phi_(0,0)_e0",
        "H_d source id",
    )
    require(source_space["pre_whitening_column_vectors"]["H_u"]["coordinate_vector"] == [1, 0], "H_u vector")
    require(
        source_space["pre_whitening_column_vectors"]["H_d_dagger"]["coordinate_vector"] == [0, 1],
        "H_d vector",
    )

    inner = bhuv["source_hermitian_inner_product"]
    require(inner["quadrature_rule_id"] == "Q_sel^U:E_H_UV:HYM_grid:Z24^4:normalized_uniform_trace", "trace id")
    require(inner["node_count"] == 331776, "node count")
    require(inner["uniform_weight_rational"] == "1/331776", "weight rational")
    require(inner["G_HYM_on_ordered_basis"] == "diag(exp(u), exp(-u))", "G formula")
    require(inner["Gram_matrix_before_whitening"][0][0] == "Tr_Q_sel^U,ZHYM(exp(u))", "N_u")
    require(inner["Gram_matrix_before_whitening"][1][1] == "Tr_Q_sel^U,ZHYM(exp(-u))", "N_d")
    require(inner["Gram_matrix_before_whitening"][0][1] == "0", "offdiag 01")
    require(inner["Gram_matrix_before_whitening"][1][0] == "0", "offdiag 10")
    require(inner["positivity_certificate"]["N_u_positive"] is True, "N_u positive")
    require(inner["positivity_certificate"]["N_d_positive"] is True, "N_d positive")

    lift = bhuv["whitening_map_and_lift"]
    require(lift["B_Huv_symbolic_exact_payload_emitted"] is True, "B_Huv symbolic emitted")
    require(lift["B_Huv_numeric_entries_evaluated"] is False, "numeric norm overclaim")
    require(lift["source_orthonormality_certificate"]["equation"] == "B_Huv^* G_Q B_Huv = I_2", "orth equation")
    require(lift["source_orthonormality_certificate"]["matrix"] == [["1", "0"], ["0", "1"]], "orth matrix")

    tests = bhuv["minimal_lift_request_tests"]
    for key in [
        "source_id_matching_selected_branch",
        "two_finite_source_space_column_vectors_emitted",
        "source_Hermitian_inner_product_or_Gram_matrix_emitted",
        "color_triplet_projection_or_decoupling_certificate",
        "basis_phase_covariance_rule_emitted",
        "finite_exactness_or_truncation_certificate_attached",
        "source_orthonormality_required_by_H7B1G_satisfied",
    ]:
        require(tests[key] is True, f"B_Huv test {key}")
    require(tests["doublet_slot_certificate"]["scope"].endswith("not a selected rank-one light projector"), "doublet scope")
    quotient = tests["quotient_admissibility_certificate"]
    for key in [
        "q_Hu_equals_q_Hd_dagger",
        "q_times_kernel_is_zero",
        "kernel_is_span_Hu_minus_Hd_dagger",
        "q_restricted_to_each_B_Huv_column_nonzero",
    ]:
        require(quotient[key] is True, f"quotient {key}")

    not_claimed = bhuv["not_claimed"]
    for key in [
        "selected_rank_one_light_projector_P_L",
        "selected_minimal_lift_sigma_G_of_low_energy_H",
        "selected_s_beta",
        "M_source",
        "direct_Huu_Hud_Hdd",
        "Huv_values",
        "K_threshold_Omega_H_lambda",
    ]:
        require(not_claimed[key] is False, f"B_Huv overclaimed {key}")

    after = request["after_C2_C3_C4"]
    for key in [
        "channel_weights",
        "color_triplet_projection_or_decoupling",
        "family_or_Higgs_kinetic_metrics",
        "physical_Higgs_doublet_slot_selection",
        "selected_metric_on_two_Higgs_plane",
        "two_column_source_orthonormal_lift_B_Huv",
    ]:
        require(after[key] is True, f"request should close {key}")
    for key in [
        "selected_rank_one_light_projector",
        "selected_minimal_lift_sigma_G",
        "selected_s_beta_value",
    ]:
        require(after[key] is False, f"request overclosed {key}")
    req_decision = request["decision"]
    require(req_decision["B_Huv_two_column_uv_lift_emitted"] is True, "request B emitted")
    require(req_decision["B_Huv_can_now_feed_H7B1F_functor"] is True, "functor feed")
    require(req_decision["rank_one_projector_contract_closed"] is False, "projector overclosed")
    require(req_decision["H7B1A_quotient_to_projector_underdetermination_retained"] is True, "H7B1A retained")

    fields = direct["direct_schema_fields_after_lift"]
    require(fields["B_Huv"][0].startswith("Tr_Q_sel^U,ZHYM(exp(u))^(-1/2)"), "direct B H_u")
    require(fields["B_Huv"][1].startswith("Tr_Q_sel^U,ZHYM(exp(-u))^(-1/2)"), "direct B H_d")
    require(fields["G_source_or_whitening_map"].startswith("G_Q=Tr_Q"), "direct G")
    require(fields["quotient_admissibility_certificate"] is True, "direct quotient")
    require(fields["same_source_exactness_or_residual_bound"] is True, "direct exactness")
    for key in [
        "M_source",
        "Huu",
        "Hud",
        "Hdd",
        "Hdu_equals_conj_Hud_certificate",
        "Delta_equals_Huu_minus_Hdd_over_2",
        "Omega_equals_Hud",
        "P_L_light_projector",
        "s_beta_equals_Delta2_over_Delta2_plus_absOmega2",
    ]:
        require(fields[key] is None, f"direct overemitted {key}")
    booleans = direct["acceptance_booleans_after_lift"]
    require(booleans["B_Huv_emitted"] is True, "direct B boolean")
    for key in [
        "M_source_emitted",
        "Herm2_payload_complete",
        "direct_Huu_Hud_Hdd_emitted",
        "selected_s_beta_promoted",
        "numeric_lambda_H_derived",
    ]:
        require(booleans[key] is False, f"direct boolean overclosed {key}")
    require(direct["decision"]["direct_Herm2_Huv_payload_emitted"] is False, "direct overclosed")

    require(msource["same_source_with_B_Huv_now_available"] is True, "M_source same source")
    for phrase in [
        "Hermitian mass/strain or Hessian operator M_source on the same finite source space used by B_Huv",
        "H-sector restriction map proving that B_Huv^* M_source B_Huv is the accepted two-Higgs Hessian block",
        "Hermiticity check M_source^*=M_source and finite residual/error certificate",
    ]:
        require(phrase in msource["must_emit_next"], f"M_source request missing {phrase}")
    for key in [
        "selected_Hermitian_M_source",
        "selected_operator_payload_for_Huv",
        "H_sector_restriction_map",
        "direct_Huu_Hud_Hdd",
        "selected_s_beta",
        "K_threshold_Omega_H_lambda",
    ]:
        require(msource["still_open"][key] is True, f"M_source frontier should keep {key}")

    h_row = hk_gate["H_row"]
    require(h_row["B_Huv_two_column_source_orthonormal_lift_emitted"] is True, "H gate B")
    require(hk_gate["accepted_selected_K_source_row_count"] == 9, "H gate count")
    require(hk_gate["selected_K_threshold_row_count_required"] == 10, "H gate required")
    route = hk_gate["direct_route_state"]
    require(route["B_Huv_two_column_lift_emitted"] is True, "route B")
    for key in [
        "M_source_emitted",
        "direct_Herm2_Huv_payload_emitted",
        "K_threshold_Omega_H_lambda_emitted",
    ]:
        require(route[key] is False, f"H gate overclosed {key}")
    require(hk_gate["conditional_consequent_current"]["ten_K_antecedent_satisfied"] is False, "ten K")
    require(hk_gate["conditional_consequent_current"]["accepted_internal_scalar_value_row_count"] == 0, "scalar rows")

    for phrase in [
        "same-source B_Huv two-column UV lift emitted",
        "source Gram/inner product G_Q=Tr_Q(diag(exp(u),exp(-u))) emitted",
        "whitening map W=diag(N_u^-1/2,N_d^-1/2) emitted",
        "B_Huv^* G_Q B_Huv = I_2 certified",
        "H K-threshold gate remains 9/10",
    ]:
        require(phrase in cutset["closed_here"], f"cutset closed missing {phrase}")
    for phrase in [
        "same-source Hermitian mass/strain operator M_source",
        "direct Huu,Hud,Hdd rows",
        "C5 trace-to-H7B1U/projection-measure identity",
        "C6 no-extra-boundary/source theorem",
        "selected rank-one light projector P_L or selected s_beta equivalent",
        "K_threshold.Omega_H.lambda source row",
        "strict Omega/lambda_H scalar execution",
    ]:
        require(phrase in cutset["still_open"], f"cutset open missing {phrase}")

    for key in [
        "B_Huv_two_column_uv_lift_emitted",
        "B_Huv_source_orthonormality_certified",
    ]:
        require(cert[key] is True, f"cert should close {key}")
    for key in [
        "selected_Hermitian_M_source_emitted",
        "direct_Herm2_Huv_payload_emitted",
        "direct_Huu_Hud_Hdd_emitted",
        "selected_rank_one_light_projector_emitted",
        "selected_s_beta_value_found",
        "K_threshold_Omega_H_lambda_emitted",
        "ten_K_antecedent_satisfied",
        "strict_Omega_lambda_scalar_execution_closed",
        "full_no_knob_closure_claimed",
        "true_SM_equivalence_claimed",
    ]:
        require(cert[key] is False, f"cert overclosed {key}")

    for phrase in [
        "emitted the same-source two-column UV lift `B_Huv`",
        "certified `B_Huv^* G_Q B_Huv = I_2`",
        "rechecked H7B1F: `B_Huv=true`, `M_source=false`",
        "H K-threshold gate remains `9/10`",
        "same-source Hermitian mass/strain operator `M_source`",
        NEXT,
    ]:
        require(phrase in note, f"note missing {phrase}")

    print(f"PASS {DATA.name}: {STATUS}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
