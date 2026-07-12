"""Audit Higgs HYM bridge C2 finite quotient-basis closure."""

from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SLUG = "selected_higgshymsectionringquadraturebridge_or_directhuvpayload"
DATA = ROOT / "candidate_data" / f"{SLUG}.candidate.json"
PACKET_DIR = ROOT / "candidate_data" / SLUG
FINITE_BASIS = PACKET_DIR / "c2_ehuv_finite_quotient_basis_exactness.packet.json"
BRIDGE_UPDATE = PACKET_DIR / "bridge_validator_c2_update.packet.json"
DIRECT_RECHECK = PACKET_DIR / "direct_herm2_huv_payload_recheck_after_c2.packet.json"
HK_GATE = PACKET_DIR / "hk_threshold_gate_after_c2_basis.packet.json"
CUTSET = PACKET_DIR / "next_cutset_after_c2_basis.packet.json"
CERT = ROOT / "certificates" / f"{SLUG}_certificate.json"
NOTE = ROOT / "proof_corpus" / "MTT_Selected_HiggsHYMSectionRingQuadratureBridge_or_DirectHuvPayload_v1.md"
BUILDER = ROOT / "scripts" / f"build_{SLUG}.py"

STATUS = (
    "MTT_SELECTED_HIGGSHYMSECTIONRINGQUADRATUREBRIDGE_OR_DIRECTHUVPAYLOAD_"
    "C2_FINITE_QUOTIENT_BASIS_CLOSED_C3_C6_OPEN"
)
NEXT = "MTT_Selected_EHUvHYMMetricConnectionFixedPoint_or_DirectHuvPayload_v1"


def load(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def require(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)


def guard(packet: dict, label: str) -> None:
    require(packet.get("observed_data_used_as_selector") is False, f"{label} observed selector")
    require(packet.get("target_fitting_used") is False, f"{label} target fitting")
    require(packet.get("closure_claimed") is True, f"{label} closure flag")


def main() -> int:
    subprocess.run([sys.executable, str(BUILDER)], cwd=ROOT, check=True)

    data = load(DATA)
    finite = load(FINITE_BASIS)
    bridge = load(BRIDGE_UPDATE)
    direct = load(DIRECT_RECHECK)
    hk_gate = load(HK_GATE)
    cutset = load(CUTSET)
    cert = load(CERT)
    note = NOTE.read_text(encoding="utf-8")

    for label, packet in [
        ("candidate", data),
        ("finite basis", finite),
        ("bridge update", bridge),
        ("direct recheck", direct),
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
    require(data["full_no_knob_closure_claimed"] is False, "full no-knob overclaim")
    require(cert["true_SM_equivalence_claimed"] is False, "cert true SM overclaim")
    require(cert["full_no_knob_closure_claimed"] is False, "cert no-knob overclaim")

    decision = data["closure_decision"]
    for key in [
        "bridge_validator_C1_closed",
        "bridge_validator_C2_closed",
        "finite_E_H_UV_quotient_basis_emitted",
        "finite_section_source_ids_emitted",
        "section_basis_exactness_certificate_emitted",
    ]:
        require(decision[key] is True, f"decision should close {key}")
    for key in [
        "bridge_validator_C3_closed",
        "bridge_validator_C4_closed",
        "bridge_validator_C5_closed",
        "bridge_validator_C6_closed",
        "literal_continuum_section_basis_emitted",
        "selected_HYM_metric_or_connection_on_E_H_UV_emitted",
        "quadrature_weights_and_trace_normalization_emitted",
        "trace_to_H7B1U_grid_identity_emitted",
        "projection_measure_equality_emitted",
        "no_extra_boundary_source_term_for_Higgs_projection",
        "direct_Herm2_Huv_payload_emitted",
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

    require(finite["status"] == "C2_EHUV_FINITE_QUOTIENT_BASIS_EXACTNESS_CLOSED", "finite status")
    require(finite["bridge_clause_closed"] is True, "C2 not closed in finite packet")
    basis = finite["finite_quotient_basis"]
    require(basis["selected_finite_quotient"] == "Q_sel^U", "quotient name")
    require(basis["base_finite_rank"] == 27, "base rank")
    require(basis["base_basis_id"] == "F3xF3_gerbe_twisted_fourier_N1_rank3", "basis id")
    require(basis["finite_H_line_basis"]["id"] == "Q_sel^U:H:phi_(0,0)_e0", "H id")
    require(basis["finite_H_line_basis"]["dimension"] == 1, "H dimension")
    require(
        [entry["id"] for entry in basis["uv_lift_basis"]]
        == [
            "Q_sel^U:E_H_UV:H_u:phi_(0,0)_e0",
            "Q_sel^U:E_H_UV:H_d_dagger:phi_(0,0)_e0",
        ],
        "UV source ids",
    )
    require(all(entry["source_id_emitted"] is True for entry in basis["uv_lift_basis"]), "source ids")
    require(
        basis["kernel_basis"][0]["id"]
        == "Q_sel^U:ker_E_H_UV_to_H:H_u_minus_H_d_dagger:phi_(0,0)_e0",
        "kernel id",
    )
    require(basis["kernel_basis"][0]["formal_vector"] == [1, -1], "kernel vector")

    exact = finite["exactness_certificate"]
    require(exact["quotient_map_matrix_over_Z"] == [[1, 1]], "quotient matrix")
    require(exact["kernel_inclusion_matrix_over_Z"] == [[1], [-1]], "kernel matrix")
    require(exact["quotient_times_kernel"] == [[0]], "q times kernel")
    for key in [
        "q_times_kernel_is_zero",
        "rank_nullity_holds",
        "q_Hu_equals_q_Hd_dagger",
        "kernel_is_span_Hu_minus_Hd_dagger",
        "exact_at_kernel",
        "exact_at_E_H_UV",
        "exact_at_H",
    ]:
        require(exact[key] is True, f"exactness missing {key}")
    require(exact["E_H_UV_rank"] == 2, "E rank")
    require(exact["kernel_rank"] == 1, "kernel rank")
    require(exact["quotient_H_rank"] == 1, "H rank")
    require(exact["rank_quotient_map"] == 1, "q rank")
    require(exact["rank_kernel_inclusion"] == 1, "kernel inclusion rank")

    typing = finite["typing_checks"]
    require(typing["ordered_E_H_UV_basis_labels"] == ["H_u", "H_d^dagger"], "labels")
    require(typing["low_energy_projection"]["H_u"] == "H", "H_u projection")
    require(typing["low_energy_projection"]["H_d"] == "H^dagger", "H_d projection")
    require(typing["quotient"]["kernel"] == "span(H_u-H_d^dagger)", "kernel text")
    require(typing["single_higgs_projection_closed"] is True, "single Higgs projection")
    require(typing["low_energy_higgs_doublet_embedding_closed"] is True, "low energy embedding")
    require(typing["two_independent_low_energy_higgs_alignment_references"] is False, "two Higgs overclaim")
    require(typing["H_sector_coordinate_label_is_used_only_as_finite_basis_label"] is True, "H coordinate guard")
    require(typing["model_active_H_projector_promoted_to_metric_or_Huv_value"] is False, "projector overpromoted")

    finite_guard = finite["guardrails"]
    for key in [
        "finite_quotient_basis_emitted",
        "finite_section_source_ids_emitted",
        "section_basis_exactness_certificate_emitted",
    ]:
        require(finite_guard[key] is True, f"finite guard should close {key}")
    for key in [
        "literal_continuum_section_basis_emitted",
        "selected_HYM_metric_or_connection_on_E_H_UV_emitted",
        "quadrature_weights_and_trace_normalization_emitted",
        "trace_to_H7B1U_grid_identity_emitted",
        "projection_measure_equality_emitted",
        "same_source_no_extra_boundary_source_proof_emitted",
        "selected_s_beta_promoted",
        "direct_Herm2_Huv_payload_emitted",
        "K_threshold_Omega_H_lambda_emitted",
    ]:
        require(finite_guard[key] is False, f"finite guard overclosed {key}")

    clauses = bridge["clause_status"]
    require(clauses["C1_branch_and_ordered_channel_labels"] is True, "C1")
    require(clauses["C2_typed_E_H_UV_section_basis_or_finite_quotient"] is True, "C2")
    for key in [
        "C3_selected_HYM_metric_or_connection_fixed_point",
        "C4_quadrature_weights_and_trace_normalization",
        "C5_trace_to_H7B1U_grid_and_projection_measure_identity",
        "C6_no_extra_boundary_or_source_term",
        "B_direct_Herm2_Huv_rows",
    ]:
        require(clauses[key] is False, f"bridge overclosed {key}")
    c2_clause = bridge["clauses"]["C2_typed_E_H_UV_section_basis_or_finite_quotient"]
    require(c2_clause["closed"] is True, "C2 clause closed")
    for phrase in [
        "continuum analytic section basis",
        "HYM or balanced metric on E_H^UV",
        "quadrature weights or trace-to-H7B1U measure identity",
        "direct Herm(2) Huv values",
    ]:
        require(phrase in c2_clause["what_is_not_claimed"], f"C2 guard missing {phrase}")
    bridge_decision = bridge["decision"]
    require(bridge_decision["C2_closed_by_finite_quotient_basis"] is True, "C2 decision")
    require(bridge_decision["C3_to_C6_remain_required"] is True, "C3-C6 requirement")
    for key in [
        "bridge_validator_complete",
        "direct_Herm2_Huv_payload_emitted",
        "selected_s_beta_promoted",
        "uniform_mean_can_be_promoted_now",
    ]:
        require(bridge_decision[key] is False, f"bridge decision overclosed {key}")

    for key in ["B_Huv", "M_source", "Huu", "Hud", "Hdd", "Delta", "Omega", "P_L", "s_beta", "lambda_H"]:
        require(direct["actual_outputs"][key] is None, f"direct output overemitted {key}")
    require(direct["C2_basis_changes_direct_Huv_status"] is False, "direct status changed")
    require(direct["accepted_as_H_K_source_row"] is False, "direct accepted")

    h_row = hk_gate["H_row"]
    for key in [
        "ordered_quotient_scaffold_closed",
        "finite_section_source_ids_emitted",
        "section_basis_exactness_certificate_emitted",
        "bridge_validator_C2_closed",
    ]:
        require(h_row[key] is True, f"H row should close {key}")
    for key in [
        "selected_HYM_metric_or_connection_on_E_H_UV",
        "quadrature_weights_and_trace_normalization_emitted",
        "trace_to_H7B1U_grid_identity_emitted",
        "projection_measure_equality_emitted",
        "no_extra_boundary_source_term_emitted",
        "direct_Herm2_Huv_payload_emitted",
        "selected_s_beta_value_found",
        "K_threshold_Omega_H_lambda_emitted",
    ]:
        require(h_row[key] is False, f"H row overclosed {key}")
    require(hk_gate["accepted_selected_K_source_row_count"] == 9, "HK count")
    require(hk_gate["selected_K_threshold_row_count_required"] == 10, "HK required")
    current = hk_gate["conditional_consequent_current"]
    require(current["ten_K_antecedent_satisfied"] is False, "ten K overclosed")
    require(current["strict_Omega_lambda_scalar_execution_closed"] is False, "strict scalar overclosed")
    require(current["accepted_internal_scalar_value_row_count"] == 0, "scalar row overclosed")

    for phrase in [
        "C2 finite E_H^UV quotient basis emitted over Q_sel^U",
        "quotient map q(H_u)=q(H_d^dagger)=H certified",
        "kernel span(H_u-H_d^dagger) certified by exact integer rank/nullity",
        "H K-threshold gate rechecked at 9/10",
    ]:
        require(phrase in cutset["closed_here"], f"cutset closed missing {phrase}")
    for phrase in [
        "C3 selected HYM or balanced metric/connection fixed point on E_H^UV",
        "C4 finite quadrature weights and trace normalization on that basis",
        "C5 trace-to-H7B1U grid identity and Higgs projection-measure equality",
        "C6 same-source no-extra-boundary/source theorem",
        "direct B_Huv+M_source or Huu,Hud,Hdd rows",
        "selected s_beta or equivalent H quartic/threshold functional",
        "K_threshold.Omega_H.lambda source row",
        "strict Omega/lambda_H scalar execution",
    ]:
        require(phrase in cutset["still_open"], f"cutset open missing {phrase}")

    for phrase in [
        "closed C2 by emitting a typed finite `E_H^UV` quotient basis over `Q_sel^U`",
        "certified the quotient map `q(H_u)=q(H_d^dagger)=H`",
        "certified the kernel `span(H_u-H_d^dagger)`",
        "H K-threshold gate remains: `9/10`",
        "C3 selected HYM/balanced metric or connection fixed point on `E_H^UV`",
        "selected `K_threshold.Omega_H.lambda`: `false`",
        NEXT,
    ]:
        require(phrase in note, f"note missing {phrase}")

    print(f"PASS {DATA.name}: {STATUS}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
