"""Audit the Higgs second-variation source gate."""

from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SLUG = "selected_higgssecondvariationfunctionalsource_or_herm2rowvalues"
DATA = ROOT / "candidate_data" / f"{SLUG}.candidate.json"
PACKET_DIR = ROOT / "candidate_data" / SLUG
SOURCE_GATE = PACKET_DIR / "source_functional_acceptance_gate.packet.json"
METRIC_NOGO = PACKET_DIR / "kinematic_metric_as_hessian_nogo.packet.json"
STRAIN_SPEC = PACKET_DIR / "dynamic_strain_kernel_payload_spec.packet.json"
VALUE_RECHECK = PACKET_DIR / "herm2_row_value_recheck_after_metric_nogo.packet.json"
HK_GATE = PACKET_DIR / "hk_threshold_gate_after_second_variation_source_gate.packet.json"
CUTSET = PACKET_DIR / "next_cutset_after_second_variation_source_gate.packet.json"
CERT = ROOT / "certificates" / f"{SLUG}_certificate.json"
NOTE = ROOT / "proof_corpus" / "MTT_Selected_HiggsSecondVariationFunctionalSource_or_Herm2RowValues_v1.md"
BUILDER = ROOT / "scripts" / f"build_{SLUG}.py"

STATUS = (
    "MTT_SELECTED_HIGGSSECONDVARIATIONFUNCTIONALSOURCE_OR_HERM2ROWVALUES_"
    "METRIC_ONLY_NOGO_CLOSED_DYNAMIC_SOURCE_ROWS_OPEN"
)
NEXT = "MTT_Selected_HiggsDynamicStrainKernel_or_C5bC6ProjectionNoBoundaryProof_v1"


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
    source_gate = load(SOURCE_GATE)
    metric = load(METRIC_NOGO)
    strain = load(STRAIN_SPEC)
    values = load(VALUE_RECHECK)
    hk_gate = load(HK_GATE)
    cutset = load(CUTSET)
    cert = load(CERT)
    note = NOTE.read_text(encoding="utf-8")

    for label, packet in [
        ("candidate", data),
        ("source gate", source_gate),
        ("metric no-go", metric),
        ("strain spec", strain),
        ("value recheck", values),
        ("H K gate", hk_gate),
        ("cutset", cutset),
        ("certificate", cert),
    ]:
        guard(packet, label)

    require(data["status"] == STATUS, "candidate status")
    require(cert["status"] == STATUS, "certificate status")
    require(data["next_required_artifact"] == NEXT, "candidate next")
    require(cert["next_required_artifact"] == NEXT, "certificate next")
    require(data["theorem"]["proved"] is True, "theorem not proved")
    require(cert["theorem_proved"] is True, "cert theorem")
    require(data["true_SM_equivalence_claimed"] is False, "true SM overclaim")
    require(data["full_no_knob_closure_claimed"] is False, "no-knob overclaim")

    decision = data["closure_decision"]
    for key in [
        "B_Huv_domain_closed",
        "R_H_kinematic_restriction_closed",
        "Herm2_row_extraction_law_closed",
        "second_variation_source_gate_closed",
        "kinematic_metric_as_hessian_nogo_closed",
        "dynamic_strain_kernel_payload_spec_emitted",
        "herm2_value_rows_rechecked_after_metric_nogo",
    ]:
        require(decision[key] is True, f"decision should close {key}")
    for key in [
        "G_Q_metric_promoted_as_M_H",
        "selected_dynamic_strain_kernel_emitted",
        "selected_F_H_second_variation_emitted",
        "selected_dynamic_H_response_emitted",
        "selected_Hermitian_M_source_emitted",
        "selected_Hermitian_M_H_values_emitted",
        "direct_Herm2_Huv_payload_emitted",
        "selected_Delta_row_emitted",
        "selected_Re_Omega_row_emitted",
        "selected_Im_Omega_row_emitted",
        "selected_s_beta_value_found",
        "C5b_projection_measure_equality_emitted",
        "C6_no_extra_boundary_source_term_emitted",
        "K_threshold_Omega_H_lambda_emitted",
        "ten_K_antecedent_satisfied",
        "strict_Omega_lambda_scalar_execution_closed",
        "true_SM_equivalence_closed",
        "full_no_knob_closed",
    ]:
        require(decision[key] is False, f"decision overclosed {key}")
    require(decision["accepted_selected_K_source_row_count"] == 9, "selected K count")
    require(decision["selected_K_threshold_row_count_required"] == 10, "required K count")
    require(decision["accepted_internal_scalar_value_row_count"] == 0, "scalar rows")

    require(
        source_gate["status"] == "SECOND_VARIATION_SOURCE_GATE_CLOSED_VALUES_OPEN",
        "source gate status",
    )
    closed_inputs = source_gate["closed_inputs"]
    for key in [
        "B_Huv_domain_closed",
        "R_H_restriction_closed",
        "P_H_projector_closed",
        "Herm2_row_extractors_closed",
        "C5a_trace_grid_identity_closed",
        "C4_finite_trace_attached",
    ]:
        require(closed_inputs[key] is True, f"closed input missing {key}")
    routes = source_gate["accepted_value_sources"]
    require(routes["full_H_response_route"]["R_H_closed_now"] is True, "R_H route not updated")
    for key in [
        "direct_F_H_second_variation",
        "full_H_response_route",
        "direct_Herm2_rows",
        "C5b_C6_projection_bridge",
    ]:
        require(routes[key]["emitted_now"] is False, f"route overemitted {key}")
    require("G_Q or B_Huv^*G_QB_Huv as the Higgs mass/strain Hessian" in source_gate["forbidden_promotions_retired_by_this_gate"], "G_Q guard missing")

    require(
        metric["status"] == "KINEMATIC_GQ_METRIC_AS_HESSIAN_REJECTED_TRACEFREE_ZERO",
        "metric status",
    )
    require(metric["theorem"]["proved"] is True, "metric theorem")
    require(metric["candidate_functional"]["Hessian_on_BHuv"] == "B_Huv^* G_Q B_Huv = I_2", "metric formula")
    trace_free = metric["computed_trace_free_part"]
    require(trace_free["M_metric"] == [[1, 0], [0, 1]], "metric identity")
    require(trace_free["M_metric_trace_free"] == [[0, 0], [0, 0]], "trace-free not zero")
    require(trace_free["rows_if_wrongly_promoted"]["Delta"] == 0, "Delta zero")
    require(trace_free["rows_if_wrongly_promoted"]["Re_Omega"] == 0, "Re Omega zero")
    require(trace_free["rows_if_wrongly_promoted"]["Im_Omega"] == 0, "Im Omega zero")
    require(trace_free["non_scalar_test_passes"] is False, "non-scalar overpassed")
    require(trace_free["light_line_defined"] is False, "light line overdefined")
    require(metric["decision"]["G_Q_metric_promoted_as_M_H"] is False, "G_Q promoted")
    require(metric["decision"]["metric_only_route_closed_as_no_go"] is True, "metric no-go not closed")
    require(metric["decision"]["requires_dynamic_strain_or_response_term"] is True, "dynamic term missing")

    require(
        strain["status"] == "DYNAMIC_STRAIN_KERNEL_PAYLOAD_SPEC_EMITTED_VALUES_OPEN",
        "strain status",
    )
    require(strain["payload_name"] == "SelectedHiggsDynamicStrainKernel", "payload name")
    must = strain["must_emit"]
    for key in [
        "source_functional_id",
        "same_branch_source_owner_certificate",
        "finite_action_or_response_formula",
        "Hermitian_second_variation_M_H",
        "nondegeneracy_certificate",
        "light_line_not_kernel_certificate",
        "finite_exactness_or_residual_bound",
    ]:
        require(must[key] is None, f"strain overfilled {key}")
    rows = must["trace_free_rows"]
    for key in ["Delta", "Re_Omega", "Im_Omega"]:
        require(rows[key] is None, f"strain row overfilled {key}")
    nearest = strain["nearest_support_not_enough"]
    require(nearest["C3_metric_connection_bound_to_E_H_UV"] is True, "C3 support missing")
    require(nearest["C5a_trace_grid_identity_closed"] is True, "C5a missing")
    require(nearest["C5b_projection_measure_equality_open"] is True, "C5b should be open")
    require(nearest["C6_no_boundary_open"] is True, "C6 should be open")
    require(nearest["full_H_response_absent"] is True, "H response should be absent")
    require(nearest["direct_rows_absent"] is True, "direct rows should be absent")

    require(
        values["status"] == "HERM2_ROW_VALUES_RECHECKED_STILL_ABSENT_AFTER_METRIC_NOGO",
        "value recheck status",
    )
    rechecked = values["value_sources_rechecked"]
    require(rechecked["direct_attempts_emit_values"] is False, "direct attempts emitted")
    require(rechecked["strict_table_rows_all_null"] is True, "strict rows not null")
    require(rechecked["inventory_rows_all_null"] is True, "inventory rows not null")
    require(rechecked["selected_H_response_emitted"] is False, "H response overemitted")
    require(rechecked["selected_F_H_second_variation_emitted"] is False, "F_H overemitted")
    require(rechecked["C5b_projection_measure_equality_emitted"] is False, "C5b overemitted")
    require(rechecked["C6_no_extra_boundary_source_term_emitted"] is False, "C6 overemitted")
    require(values["accepted_source_row_count"] == 0, "source rows found")
    require(values["metric_only_candidate_rejected"] is True, "metric not rejected")
    for key, value in values["current_required_table"].items():
        require(value is None, f"value table overfilled {key}")
    for key, value in values["current_inventory_rows"].items():
        require(value is None, f"inventory overfilled {key}")

    require(
        hk_gate["status"]
        == "H_K_THRESHOLD_GATE_SECOND_VARIATION_SOURCE_GATE_CLOSED_VALUES_OPEN_9_OF_10",
        "H K status",
    )
    require(hk_gate["accepted_selected_K_source_row_count"] == 9, "H K selected")
    require(hk_gate["selected_K_threshold_row_count_required"] == 10, "H K required")
    h_row = hk_gate["H_row"]
    for key in [
        "second_variation_source_gate_closed",
        "kinematic_metric_as_hessian_nogo_closed",
        "dynamic_strain_kernel_payload_spec_emitted",
    ]:
        require(h_row[key] is True, f"H row should close {key}")
    for key in [
        "G_Q_metric_promoted_as_M_H",
        "selected_dynamic_strain_kernel_emitted",
        "selected_F_H_second_variation_emitted",
        "selected_Hermitian_M_H_values_emitted",
        "selected_Delta_row_emitted",
        "selected_Re_Omega_row_emitted",
        "selected_Im_Omega_row_emitted",
        "C5b_projection_measure_equality_emitted",
        "C6_no_extra_boundary_source_term_emitted",
        "K_threshold_Omega_H_lambda_emitted",
    ]:
        require(h_row[key] is False, f"H row overclosed {key}")
    require(hk_gate["conditional_consequent_current"]["ten_K_antecedent_satisfied"] is False, "ten-K overclosed")
    require(
        hk_gate["conditional_consequent_current"]["strict_Omega_lambda_scalar_execution_closed"]
        is False,
        "Omega/lambda overclosed",
    )

    require(
        cutset["status"] == "NEXT_FRONTIER_DYNAMIC_STRAIN_KERNEL_OR_C5B_C6_PROJECTION_BRIDGE",
        "cutset status",
    )
    require(cutset["next_required_artifact"] == NEXT, "cutset next")
    for phrase in [
        "Higgs second-variation source acceptance gate fixed",
        "kinematic G_Q metric tested and rejected as Hessian because trace-free part is zero on B_Huv",
        "dynamic strain kernel payload spec emitted",
        "H K-threshold gate remains 9/10",
    ]:
        require(phrase in cutset["closed_here"], f"cutset closed missing {phrase}")
    for phrase in [
        "selected dynamic strain/response functional F_H with nonzero Herm(2) trace-free part",
        "or direct Huu,Hud,Hdd rows with source/exactness certificates",
        "or C5b projection-measure equality plus C6 no-extra-boundary/source theorem",
        "K_threshold.Omega_H.lambda source row",
    ]:
        require(phrase in cutset["still_open"], f"cutset open missing {phrase}")

    for phrase in [
        "cannot be promoted to `M_H`",
        "`B_Huv^* G_Q B_Huv = I_2`",
        "`Delta=Re(Omega)=Im(Omega)=0`",
        "dynamic strain/response source",
        NEXT,
    ]:
        require(phrase in note, f"note missing {phrase}")

    print(
        "AUDIT_PASS: Higgs second-variation source gate closed; "
        "metric-only Hessian no-go proved; dynamic Herm(2) values remain open."
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
