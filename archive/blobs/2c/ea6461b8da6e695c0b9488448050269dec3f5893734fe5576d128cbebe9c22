"""Audit E_H^UV binding/trace identity or direct Huv rows to H K-threshold emission."""

from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SLUG = "selected_ehuvbindingtraceidentity_or_directhuvrows_to_hkthresholdemission"
DATA = ROOT / "candidate_data" / f"{SLUG}.candidate.json"
PACKET_DIR = ROOT / "candidate_data" / SLUG
TRACE_ANALOGY = PACKET_DIR / "finite_trace_analogy_assessment.packet.json"
BINDING_ATTEMPT = PACKET_DIR / "ehuv_binding_trace_identity_attempt.packet.json"
DIRECT_ATTEMPT = PACKET_DIR / "direct_huv_row_emission_attempt.packet.json"
HK_GATE = PACKET_DIR / "hk_threshold_gate_after_ehuv_attempt.packet.json"
CUTSET = PACKET_DIR / "next_cutset_after_ehuv_binding_attempt.packet.json"
CERT = ROOT / "certificates" / f"{SLUG}_certificate.json"
NOTE = ROOT / "proof_corpus" / "MTT_Selected_EHUvBindingTraceIdentityOrDirectHuvRows_to_HKThresholdEmission_v1.md"
BUILDER = ROOT / "scripts" / f"build_{SLUG}.py"

STATUS = (
    "MTT_SELECTED_EHUVBINDINGTRACEIDENTITY_OR_DIRECTHUVROWS_TO_HKTHRESHOLDEMISSION_"
    "BUILT_TRACE_ANALOGY_BINDING_OPEN"
)
NEXT = "MTT_Selected_EHUvSectionSourceIdentity_or_DirectHerm2HuvRowEmission_v1"


def load(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def require(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)


def require_close(value: float, expected: float, message: str) -> None:
    require(abs(float(value) - expected) < 1e-12, message)


def guard(packet: dict, label: str) -> None:
    require(packet.get("observed_data_used_as_selector") is False, f"{label} observed selector violation")
    require(packet.get("target_fitting_used") is False, f"{label} target fitting violation")
    require(packet.get("closure_claimed") is True, f"{label} should close its local route split")


def main() -> int:
    subprocess.run([sys.executable, str(BUILDER)], cwd=ROOT, check=True)

    data = load(DATA)
    cert = load(CERT)
    trace_analogy = load(TRACE_ANALOGY)
    binding_attempt = load(BINDING_ATTEMPT)
    direct_attempt = load(DIRECT_ATTEMPT)
    hk_gate = load(HK_GATE)
    cutset = load(CUTSET)
    note = NOTE.read_text(encoding="utf-8")

    for label, packet in [
        ("candidate", data),
        ("certificate", cert),
        ("finite trace analogy", trace_analogy),
        ("E_H^UV binding attempt", binding_attempt),
        ("direct Huv attempt", direct_attempt),
        ("H K gate", hk_gate),
        ("cutset", cutset),
    ]:
        guard(packet, label)

    require(data["status"] == STATUS, "candidate status mismatch")
    require(cert["status"] == STATUS, "certificate status mismatch")
    require(data["next_required_artifact"] == NEXT, "candidate next mismatch")
    require(cert["next_required_artifact"] == NEXT, "certificate next mismatch")
    require(data["theorem"]["proved"] is True, "candidate theorem missing")
    require(cert["theorem_proved"] is True, "certificate theorem missing")
    require(data["true_SM_equivalence_claimed"] is False, "true SM overclaim")
    require(data["full_no_knob_closure_claimed"] is False, "full no-knob overclaim")
    require(cert["true_SM_equivalence_claimed"] is False, "cert true SM overclaim")
    require(cert["full_no_knob_closure_claimed"] is False, "cert full no-knob overclaim")

    decision = data["closure_decision"]
    require(decision["H7B1ZA_route_split_executed"] is True, "H7B1ZA split missing")
    require(decision["finite_trace_analogy_imported"] is True, "finite trace analogy missing")
    require(
        decision["finite_trace_analogy_proves_E_H_UV_binding"] is False,
        "finite trace analogy overpromoted",
    )
    require(decision["source_HYM_grid_payload_emitted"] is True, "HYM grid support missing")
    require(decision["computational_uniform_quadrature_emitted"] is True, "uniform quadrature support missing")
    require(decision["selected_E_H_UV_section_basis_emitted"] is False, "section basis overemitted")
    require(
        decision["selected_HYM_metric_or_connection_on_E_H_UV_emitted"] is False,
        "E_H^UV HYM metric overemitted",
    )
    require(decision["projection_measure_equality_emitted"] is False, "projection equality overemitted")
    require(decision["trace_to_H7B1U_grid_identity_emitted"] is False, "trace identity overemitted")
    require(
        decision["no_extra_boundary_source_term_for_Higgs_projection"] is False,
        "boundary/source theorem overemitted",
    )
    require(decision["direct_Herm2_Huv_payload_emitted"] is False, "direct Huv payload overemitted")
    require(decision["selected_s_beta_value_found"] is False, "s_beta overselected")
    require(decision["K_threshold_Omega_H_lambda_emitted"] is False, "H K row overemitted")
    require(decision["accepted_selected_K_source_row_count"] == 9, "selected K count mismatch")
    require(decision["selected_K_threshold_row_count_required"] == 10, "required K count mismatch")
    require(decision["ten_K_antecedent_satisfied"] is False, "ten-K antecedent overclosed")
    require(decision["strict_Omega_lambda_scalar_execution_closed"] is False, "Omega/lambda overclosed")
    require(decision["accepted_internal_scalar_value_row_count"] == 0, "scalar rows overaccepted")
    require(decision["true_SM_equivalence_closed"] is False, "true SM closure overclaimed")
    require(decision["full_no_knob_closed"] is False, "full no-knob closure overclaimed")

    require(
        trace_analogy["status"] == "FINITE_TRACE_ANALOGY_IMPORTED_NOT_A_BINDING_THEOREM",
        "finite trace analogy status",
    )
    imported = trace_analogy["imported_finite_weyl_trace_theorem"]
    require(imported["measure_normalization_derived"] is True, "finite trace measure not imported")
    require(imported["remaining_physical_boundary_source_open"] is True, "boundary open flag missing")
    promotion = trace_analogy["conditional_promotion_template"]
    require(promotion["promoted_now"] is False, "finite Galerkin promotion overclaimed")
    require(
        promotion["physical_measure_equals_finite_trace_quadrature"] is False,
        "physical measure antecedent overclaimed",
    )
    require(
        promotion["no_extra_physical_boundary_or_source_term"] is False,
        "no-extra-boundary antecedent overclaimed",
    )
    applicability = trace_analogy["applicability_to_E_H_UV"]
    require(applicability["supports_uniform_trace_choice"] is True, "uniform trace support missing")
    require(applicability["proves_E_H_UV_binding"] is False, "E_H^UV binding overproved")
    require("C1 qutrit Weyl response algebra" in applicability["reason"], "trace analogy reason too vague")

    require(binding_attempt["status"] == "EHUV_BINDING_TRACE_IDENTITY_ATTEMPT_OPEN", "binding status")
    require(binding_attempt["route_id"] == "H7B1ZA-A", "binding route")
    require(binding_attempt["accepted_as_H_K_source_row"] is False, "binding route overaccepted")
    support = binding_attempt["closed_support"]
    require(support["same_branch_with_H7B1U_grid"] is True, "same branch support missing")
    require(
        support["selected_source_branch"] == "q79/F,m=1 eta_00 rank-2 V_alpha diagonal T3 HYM lane",
        "selected branch mismatch",
    )
    require(support["ordered_Hu_Hd_labels_closed"] is True, "H labels not closed")
    require(support["coordinate_scaffold"]["basis_labels"] == ["H_u", "H_d^dagger"], "basis labels mismatch")
    require(support["coordinate_scaffold"]["kernel_vector"] == [1, -1], "kernel vector mismatch")
    require(support["coordinate_scaffold"]["quotient_row"] == [1, 1], "quotient row mismatch")
    require(support["source_HYM_grid_payload_emitted"] is True, "HYM payload support missing")
    require(support["computational_uniform_quadrature_emitted"] is True, "quadrature support missing")
    require(support["node_count"] == 331776, "node count mismatch")
    require(support["uniform_weight_rational"] == "1/331776", "uniform weight mismatch")
    require(support["source_independent_of_target_replay"] is True, "source independence missing")
    require_close(support["residual_l2"], 8.208178923714022e-13, "HYM residual mismatch")
    require("diag(exp(u), exp(-u))" in support["Gram_matrix_formula"], "Gram formula mismatch")
    require("A_diag = d u * T3" in support["connection_formula"], "connection formula mismatch")

    missing = binding_attempt["missing_binding_fields"]
    require(missing["selected_E_H_UV_section_basis_emitted"] is False, "section basis overclosed")
    require(missing["finite_section_basis_source_ids"] is None, "section source ids should be absent")
    require(missing["section_basis_exactness_certificate"] is None, "section exactness should be absent")
    require(
        missing["selected_HYM_metric_or_connection_on_E_H_UV"] is False,
        "E_H^UV metric overclosed",
    )
    require(missing["accepted_as_metric_on_E_H_UV"] is False, "metric accepted too early")
    require(missing["projection_measure_equality"] is False, "projection equality overclosed")
    require(missing["trace_to_H7B1U_grid_identity"] is False, "trace identity overclosed")
    require(missing["no_extra_boundary_source_term"] is False, "boundary theorem overclosed")
    diagnostic = binding_attempt["diagnostic_replay_only"]
    require(diagnostic["conditional_local_formula"] == "tanh(2u)^2", "diagnostic formula")
    require_close(diagnostic["uniform_candidate_s_beta"], 0.004701083905943647, "diagnostic s_beta")
    require(diagnostic["selected_s_beta_promoted"] is False, "diagnostic s_beta promoted")
    require(
        diagnostic["accepted_as_physical_Higgs_projection_measure"] is False,
        "diagnostic projection measure accepted",
    )
    require("not a source section basis" in binding_attempt["reason_not_closed"], "binding rejection reason")

    require(
        direct_attempt["status"] == "DIRECT_HERM2_HUV_ROW_EMISSION_ATTEMPT_VALUES_ABSENT",
        "direct Huv status",
    )
    require(direct_attempt["route_id"] == "H7B1ZA-B", "direct route")
    require(direct_attempt["accepted_as_H_K_source_row"] is False, "direct route overaccepted")
    for key in [
        "B_Huv",
        "M_source",
        "G_source_or_whitening_map",
        "Huu",
        "Hud",
        "Hdd",
        "Delta",
        "Omega",
        "P_L",
        "s_beta",
    ]:
        require(direct_attempt["attempted_outputs"][key] is None, f"direct output overemitted {key}")
    direct_decision = direct_attempt["decision"]
    for key in [
        "B_Huv_emitted",
        "Herm2_payload_complete",
        "M_source_emitted",
        "direct_Huu_Hud_Hdd_emitted",
        "numeric_lambda_H_derived",
        "selected_s_beta_promoted",
    ]:
        require(direct_decision[key] is False, f"direct decision overclosed {key}")
    require(
        "No same-source M_source or direct Huu,Hud,Hdd values are emitted by the imported packets."
        in direct_attempt["why_no_direct_fill"],
        "direct reason",
    )

    require(hk_gate["status"] == "H_K_THRESHOLD_GATE_RECHECKED_EHUV_BINDING_OPEN", "H K gate status")
    require(hk_gate["required_output"] == "K_threshold.Omega_H.lambda", "H K output mismatch")
    require(
        hk_gate["source_equation"]["split_K_row"]
        == "K_threshold.Omega_H.lambda = L_rowlocal.Omega_H.lambda * T_scheme.Omega_H.lambda",
        "H K split mismatch",
    )
    require(hk_gate["accepted_selected_K_source_row_count"] == 9, "gate selected K count")
    require(hk_gate["selected_K_threshold_row_count_required"] == 10, "gate required K count")
    for key, value in hk_gate["H_row"].items():
        require(value is False, f"H row gate overclosed {key}")
    current = hk_gate["conditional_consequent_current"]
    require(current["ten_K_antecedent_satisfied"] is False, "gate ten-K overclosed")
    require(current["strict_Omega_lambda_scalar_execution_closed"] is False, "gate scalar execution overclosed")
    require(current["accepted_internal_scalar_value_row_count"] == 0, "gate scalar count")

    require(
        cutset["status"] == "NEXT_FRONTIER_EHUV_SECTION_SOURCE_IDENTITY_OR_DIRECT_HERM2_ROWS",
        "cutset status",
    )
    require(cutset["next_required_artifact"] == NEXT, "cutset next mismatch")
    for phrase in [
        "H7B1ZA route split executed locally",
        "finite Weyl trace uniqueness imported as analogy/support only",
        "uniform trace support retained without promoting it to physical Higgs measure",
        "E_H^UV binding/trace identity attempted and left open on exact fields",
        "direct Herm2 Huv route attempted and found all values absent",
        "H K-threshold gate rechecked at 9/10",
    ]:
        require(phrase in cutset["closed_here"], f"cutset closed missing {phrase}")
    for phrase in [
        "selected E_H^UV finite section source ids",
        "section basis exactness certificate",
        "binding diagonal End0 HYM metric/connection to E_H^UV",
        "projection-measure equality",
        "trace-to-H7B1U grid identity as physical projection measure",
        "no-extra-boundary/source theorem for Higgs projection",
        "direct B_Huv+M_source or Huu,Hud,Hdd rows",
        "selected s_beta or equivalent H quartic/threshold functional",
        "K_threshold.Omega_H.lambda source row",
        "strict Omega/lambda_H scalar execution",
    ]:
        require(phrase in cutset["still_open"], f"cutset open missing {phrase}")

    for phrase in [
        "executed the H7B1ZA route split locally",
        "finite Weyl trace uniqueness as support",
        "attempted `E_H^UV` binding/trace identity: `false`",
        "attempted direct Herm(2) Huv row emission: `false`",
        "H K-threshold gate remains: `9/10`",
        "selected `E_H^UV` finite section source ids",
        "selected `K_threshold.Omega_H.lambda`: `false`",
        NEXT,
    ]:
        require(phrase in note, f"note missing {phrase}")

    print(f"PASS {DATA.name}: {STATUS}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
