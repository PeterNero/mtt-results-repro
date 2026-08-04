"""Audit E_H^UV section-source identity or direct Herm(2) Huv row emission."""

from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SLUG = "selected_ehuvsectionsourceidentity_or_directherm2huvrowemission"
DATA = ROOT / "candidate_data" / f"{SLUG}.candidate.json"
PACKET_DIR = ROOT / "candidate_data" / SLUG
CONST_IMPORT = PACKET_DIR / "late_h7b1_sequence_import.packet.json"
ORDERED_SCAFFOLD = PACKET_DIR / "ehuv_ordered_quotient_scaffold_clause.packet.json"
BRIDGE_REDUCTION = PACKET_DIR / "sectionring_quadrature_bridge_reduction.packet.json"
DIRECT_RECHECK = PACKET_DIR / "direct_herm2_huv_payload_recheck.packet.json"
HK_GATE = PACKET_DIR / "hk_threshold_gate_after_section_source_attempt.packet.json"
CUTSET = PACKET_DIR / "next_cutset_after_section_source_attempt.packet.json"
CERT = ROOT / "certificates" / f"{SLUG}_certificate.json"
NOTE = ROOT / "proof_corpus" / "MTT_Selected_EHUvSectionSourceIdentity_or_DirectHerm2HuvRowEmission_v1.md"
BUILDER = ROOT / "scripts" / f"build_{SLUG}.py"

STATUS = (
    "MTT_SELECTED_EHUVSECTIONSOURCEIDENTITY_OR_DIRECTHERM2HUVROWEMISSION_"
    "IMPORTED_ORDERED_SCAFFOLD_BRIDGE_C2_C6_OPEN"
)
NEXT = "MTT_Selected_HiggsHYMSectionRingQuadratureBridgeTheorem_or_DirectHuvPayload_v1"


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
    require(packet.get("closure_claimed") is True, f"{label} should close its local import/reduction")


def main() -> int:
    subprocess.run([sys.executable, str(BUILDER)], cwd=ROOT, check=True)

    data = load(DATA)
    cert = load(CERT)
    const_import = load(CONST_IMPORT)
    ordered = load(ORDERED_SCAFFOLD)
    bridge = load(BRIDGE_REDUCTION)
    direct = load(DIRECT_RECHECK)
    hk_gate = load(HK_GATE)
    cutset = load(CUTSET)
    note = NOTE.read_text(encoding="utf-8")

    for label, packet in [
        ("candidate", data),
        ("certificate", cert),
        ("constants import", const_import),
        ("ordered scaffold", ordered),
        ("bridge reduction", bridge),
        ("direct recheck", direct),
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
    require(decision["late_H7B1_sequence_imported"] is True, "late H7B1 sequence missing")
    require(decision["ordered_E_H_UV_quotient_scaffold_closed"] is True, "ordered scaffold not closed")
    require(decision["bridge_validator_C1_closed"] is True, "C1 not closed")
    for key in [
        "bridge_validator_C2_closed",
        "bridge_validator_C3_closed",
        "bridge_validator_C4_closed",
        "bridge_validator_C5_closed",
        "bridge_validator_C6_closed",
        "finite_section_source_ids_emitted",
        "section_basis_exactness_certificate_emitted",
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
    require(decision["accepted_selected_K_source_row_count"] == 9, "selected K count mismatch")
    require(decision["selected_K_threshold_row_count_required"] == 10, "required K count mismatch")
    require(decision["accepted_internal_scalar_value_row_count"] == 0, "scalar rows overaccepted")

    require(
        const_import["status"] == "LATE_H7B1_SEQUENCE_IMPORTED_NO_HUV_PAYLOAD",
        "constants import status",
    )
    imported = const_import["imported_sequence"]
    require(imported["H7B1S"]["minimal_missing_theorem_built"] is True, "H7B1S theorem missing")
    require(imported["H7B1S"]["UV_Higgs_plane_binding_closed"] is False, "H7B1S overclosed")
    require(imported["H7B1T"]["formal_UV_exact_sequence_scaffold_closed"] is True, "H7B1T sequence")
    require(imported["H7B1T"]["conditional_G_minimal_lift_formula_proved"] is True, "H7B1T lift")
    require(imported["H7B1T"]["source_metric_bound_to_E_H_UV"] is False, "H7B1T binding overclosed")
    require(imported["H7B1U"]["conditional_finite_reduction_executable"] is True, "H7B1U reduction")
    require(imported["H7B1U"]["source_metric_bound_to_E_H_UV"] is False, "H7B1U binding overclosed")
    require(imported["H7B1V"]["finite_Weyl_trace_measure_derived"] is True, "H7B1V trace")
    require(
        imported["H7B1V"]["uniform_reduction_best_current_source_aligned_candidate"] is True,
        "H7B1V uniform support",
    )
    require(imported["H7B1V"]["trace_to_HYM_grid_binding_closed"] is False, "H7B1V binding")
    require(
        imported["H7B1W"]["selected_Higgs_HYM_quadrature_bridge_criterion_emitted"] is True,
        "H7B1W criterion",
    )
    require(imported["H7B1W"]["finite_trace_HYM_binding_closed"] is False, "H7B1W binding")
    require(imported["H7B1W"]["direct_Herm2_Huv_payload_emitted"] is False, "H7B1W direct")
    require(imported["H7B1X"]["E_H_UV_exact_sequence_scaffold_closed"] is True, "H7B1X scaffold")
    require(imported["H7B1X"]["ordered_Hu_Hd_channel_scaffold_closed"] is True, "H7B1X labels")
    require(imported["H7B1X"]["bridge_validator_first_clause_filled"] is True, "H7B1X C1")
    require(imported["H7B1X"]["selected_E_H_UV_section_basis_emitted"] is False, "H7B1X basis")
    import_decision = const_import["decision"]
    require(import_decision["ordered_scaffold_closure_imported"] is True, "ordered import")
    require(import_decision["bridge_criterion_imported"] is True, "criterion import")
    require(import_decision["direct_Huv_payload_imported"] is False, "direct import overclosed")
    require(import_decision["selected_s_beta_imported"] is False, "s_beta import overclosed")
    require(import_decision["K_threshold_Omega_H_lambda_emitted"] is False, "K import overclosed")

    require(
        ordered["status"] == "EHUV_ORDERED_QUOTIENT_SCAFFOLD_IMPORTED_C1_CLOSED_C2_OPEN",
        "ordered status",
    )
    require(ordered["validator_clause"] == "C1_branch_and_ordered_channel_labels", "ordered clause")
    require(ordered["validator_clause_closed"] is True, "ordered C1 not closed")
    require(
        ordered["ordered_label_ids_emitted"]
        == ["H7B1X:E_H_UV:ordered_label:H_u", "H7B1X:E_H_UV:ordered_label:H_d^dagger"],
        "ordered label ids mismatch",
    )
    scaffold = ordered["formal_quotient_scaffold"]
    require(scaffold["basis_labels"] == ["H_u", "H_d^dagger"], "basis label mismatch")
    require(scaffold["quotient"]["kernel"] == "span(H_u-H_d^dagger)", "kernel mismatch")
    require(scaffold["quotient"]["q_Hu"] == "H", "q_Hu mismatch")
    require(scaffold["quotient"]["q_Hd_dagger"] == "H", "q_Hd mismatch")
    not_promoted = ordered["not_promoted_to_section_basis"]
    require(not_promoted["selected_E_H_UV_section_basis_emitted"] is False, "basis overemitted")
    require(not_promoted["finite_section_source_ids_emitted"] is False, "section source ids overemitted")
    require(
        not_promoted["section_basis_exactness_certificate_emitted"] is False,
        "section exactness overemitted",
    )
    require("forbids treating ordered Hu/Hd labels as finite basis vectors" in not_promoted["reason"], "reason")

    require(
        bridge["status"] == "SECTIONRING_QUADRATURE_BRIDGE_REDUCED_TO_C2_C6",
        "bridge status",
    )
    require(
        bridge["bridge_validator_name"] == "SelectedHiggsHYMSectionRingQuadratureBridgeValidator",
        "bridge name",
    )
    require(bridge["h7b1w_bridge_criterion"]["criterion_emitted"] is True, "criterion not emitted")
    require(
        bridge["h7b1w_bridge_criterion"]["name"] == "SelectedHiggsHYMSectionRingQuadratureBridgeTheorem",
        "criterion name",
    )
    clauses = bridge["clause_status"]
    require(clauses["C1_branch_and_ordered_channel_labels"] is True, "C1 not closed in bridge")
    for key in [
        "C2_typed_E_H_UV_section_basis_or_finite_quotient",
        "C3_selected_HYM_metric_or_connection_fixed_point",
        "C4_quadrature_weights_and_trace_normalization",
        "C5_trace_to_H7B1U_grid_and_projection_measure_identity",
        "C6_no_extra_boundary_or_source_term",
    ]:
        require(clauses[key] is False, f"bridge clause overclosed {key}")
    reduction = bridge["conditional_reduction_executed_not_selected"]
    require(reduction["formula"] == "tanh(2u)^2", "reduction formula")
    values = reduction["values"]
    require_close(values["uniform_mean"], 0.004701083905943647, "uniform mean")
    require_close(values["rho_weighted_mean"], 0.01175427147946371, "rho mean")
    require_close(values["exp_density_weighted_mean"], 0.012349317823559027, "exp mean")
    require(reduction["replay_certificate"]["matches_stored_replay"] is True, "replay mismatch")
    require_close(reduction["replay_certificate"]["residual_l2"], 8.208178923714022e-13, "residual")
    require(reduction["selected_finite_reduction_policy_promoted"] is False, "reduction promoted")
    require(reduction["selected_s_beta_promoted"] is False, "s_beta promoted")
    bridge_decision = bridge["decision"]
    require(bridge_decision["bridge_validator_complete"] is False, "bridge overcomplete")
    require(bridge_decision["uniform_mean_can_be_promoted_now"] is False, "uniform overpromoted")
    require(bridge_decision["selected_s_beta_promoted"] is False, "bridge s_beta overpromoted")
    require(bridge_decision["finite_trace_HYM_binding_closed"] is False, "finite trace binding overclosed")
    for key, value in bridge["h7b1w_missing_payload"].items():
        require(value is True, f"H7B1W missing payload flag lost {key}")
    for key, value in bridge["request_must_emit_next"].items():
        require(value is None, f"request field should be open {key}")
    for phrase in [
        "do not treat ordered Hu/Hd labels as finite basis vectors",
        "do not treat QA/SU3 ordered source-layer support as operator-layer metric data",
        "do not treat the H7B1U uniform mean as selected s_beta without C2-C6",
        "do not use measured Higgs mass, v, tan beta, or lambda_H as selectors",
    ]:
        require(phrase in bridge["forbidden_promotions"], f"forbidden promotion missing {phrase}")

    require(direct["status"] == "DIRECT_HERM2_HUV_PAYLOAD_RECHECKED_VALUES_ABSENT", "direct status")
    for key in ["B_Huv", "M_source", "Huu", "Hud", "Hdd", "Delta", "Omega", "P_L", "s_beta", "lambda_H"]:
        require(direct["actual_outputs"][key] is None, f"direct output overemitted {key}")
    direct_decision = direct["decision"]
    for key in [
        "B_Huv_value_emitted",
        "M_source_value_emitted",
        "direct_Herm2_Huv_payload_emitted",
        "direct_Huu_Hud_Hdd_emitted",
        "numeric_lambda_H_derived",
        "selected_s_beta_promoted",
    ]:
        require(direct_decision[key] is False, f"direct decision overclosed {key}")
    require(direct["accepted_as_H_K_source_row"] is False, "direct accepted too early")

    require(hk_gate["status"] == "H_K_THRESHOLD_GATE_RECHECKED_SECTION_SOURCE_OPEN", "HK status")
    require(hk_gate["required_output"] == "K_threshold.Omega_H.lambda", "HK output")
    require(hk_gate["accepted_selected_K_source_row_count"] == 9, "HK selected count")
    require(hk_gate["selected_K_threshold_row_count_required"] == 10, "HK required count")
    h_row = hk_gate["H_row"]
    require(h_row["ordered_quotient_scaffold_closed"] is True, "H row lost scaffold closure")
    for key in [
        "finite_section_source_ids_emitted",
        "section_basis_exactness_certificate_emitted",
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
    current = hk_gate["conditional_consequent_current"]
    require(current["ten_K_antecedent_satisfied"] is False, "ten-K overclosed")
    require(current["strict_Omega_lambda_scalar_execution_closed"] is False, "strict scalar overclosed")
    require(current["accepted_internal_scalar_value_row_count"] == 0, "scalar count")

    require(
        cutset["status"] == "NEXT_FRONTIER_HIGGS_HYM_SECTIONRING_BRIDGE_OR_DIRECT_HUV_PAYLOAD",
        "cutset status",
    )
    require(cutset["next_required_artifact"] == NEXT, "cutset next")
    for phrase in [
        "late constants H7B1S/T/U/V/W/X sequence imported",
        "ordered E_H^UV label and quotient scaffold imported",
        "bridge validator C1 clause closed in the active SM H-row ledger",
        "H7B1W bridge criterion imported as the exact C2-C6 acceptance contract",
        "conditional finite reductions replayed only as diagnostics",
        "direct Herm2 Huv payload route rechecked with all values absent",
        "H K-threshold gate rechecked at 9/10",
    ]:
        require(phrase in cutset["closed_here"], f"cutset closed missing {phrase}")
    for phrase in [
        "C2 typed E_H^UV section basis or finite quotient basis",
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
        "closed the ordered `E_H^UV=span(H_u,H_d^dagger)` label/quotient scaffold",
        "closed bridge-validator C1",
        "exact C2-C6 acceptance contract",
        "rechecked direct Herm(2) Huv payload: `false`",
        "H K-threshold gate remains: `9/10`",
        "C2 typed `E_H^UV` section basis or finite quotient basis",
        "selected `K_threshold.Omega_H.lambda`: `false`",
        NEXT,
    ]:
        require(phrase in note, f"note missing {phrase}")

    print(f"PASS {DATA.name}: {STATUS}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
