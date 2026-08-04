"""Audit the selected H-sector restriction from B_Huv."""

from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SLUG = "selected_hsectorrestrictionfrombhuv_or_dynamichiggsresponsehessian"
DATA = ROOT / "candidate_data" / f"{SLUG}.candidate.json"
PACKET_DIR = ROOT / "candidate_data" / SLUG
RH_PACKET = PACKET_DIR / "hsector_restriction_from_bhuv.packet.json"
ROUTE_REDUCTION = PACKET_DIR / "full_route_reduction_after_rh_closure.packet.json"
DYNAMIC_GATE = PACKET_DIR / "dynamic_higgs_response_hessian_gate.packet.json"
H7B1J_RECHECK = PACKET_DIR / "h7b1j_after_rh_closure_recheck.packet.json"
HK_GATE = PACKET_DIR / "hk_threshold_gate_after_rh_closure.packet.json"
CUTSET = PACKET_DIR / "next_cutset_after_rh_closure.packet.json"
CERT = ROOT / "certificates" / f"{SLUG}_certificate.json"
NOTE = ROOT / "proof_corpus" / "MTT_Selected_HSectorRestrictionFromBHuv_or_DynamicHiggsResponseHessian_v1.md"
BUILDER = ROOT / "scripts" / f"build_{SLUG}.py"

STATUS = (
    "MTT_SELECTED_HSECTORRESTRICTIONFROMBHUV_OR_DYNAMICHIGGSRESPONSEHESSIAN_"
    "RH_KINEMATIC_RESTRICTION_CLOSED_DYNAMIC_MH_OPEN"
)
NEXT = "MTT_Selected_DynamicHiggsResponseHessianOnBHuv_or_DirectMHValueEmission_v1"


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
    rh_packet = load(RH_PACKET)
    route = load(ROUTE_REDUCTION)
    dynamic_gate = load(DYNAMIC_GATE)
    h7b1j = load(H7B1J_RECHECK)
    hk_gate = load(HK_GATE)
    cutset = load(CUTSET)
    cert = load(CERT)
    note = NOTE.read_text(encoding="utf-8")

    for label, packet in [
        ("candidate", data),
        ("R_H packet", rh_packet),
        ("route reduction", route),
        ("dynamic gate", dynamic_gate),
        ("H7B1J recheck", h7b1j),
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
        "B_Huv_two_column_uv_lift_emitted",
        "B_Huv_source_orthonormality_certified",
        "selected_H_sector_restriction_R_H_emitted",
        "selected_H_projector_P_H_emitted",
        "R_H_B_Huv_equals_I2_certified",
        "P_H_idempotent_and_G_self_adjoint_certified",
        "old_H7B1J_R_H_gap_retired",
        "full_route_reduced_to_dynamic_H_response_or_direct_M_H",
    ]:
        require(decision[key] is True, f"decision should close {key}")
    for key in [
        "selected_dynamic_H_response_emitted",
        "selected_Hermitian_M_source_emitted",
        "direct_Herm2_Huv_payload_emitted",
        "selected_H_response_table_emitted",
        "selected_Delta_row_emitted",
        "selected_Re_Omega_row_emitted",
        "selected_Im_Omega_row_emitted",
        "selected_s_beta_value_found",
        "K_threshold_Omega_H_lambda_emitted",
        "ten_K_antecedent_satisfied",
        "strict_Omega_lambda_scalar_execution_closed",
        "true_SM_equivalence_closed",
        "full_no_knob_closed",
    ]:
        require(decision[key] is False, f"decision overclosed {key}")
    require(decision["accepted_selected_K_source_row_count"] == 9, "selected K count")
    require(decision["selected_K_threshold_row_count_required"] == 10, "required K count")
    require(decision["accepted_internal_scalar_value_row_count"] == 0, "scalar row count")

    require(rh_packet["status"] == "RH_KINEMATIC_RESTRICTION_FROM_BHUV_CLOSED", "R_H status")
    require(rh_packet["restriction_kind"] == "kinematic_two_Higgs_source_restriction", "restriction kind")
    require(rh_packet["selected_source_space"]["basis_dimension"] == 27, "source dimension")
    require(rh_packet["selected_source_space"]["branch"]["q"] == 79, "source q")
    require(rh_packet["selected_source_space"]["branch"]["orientation"] == "F", "source orientation")
    require(rh_packet["selected_source_space"]["branch"]["torsion_label_m"] == 1, "source m")
    subspace = rh_packet["selected_two_higgs_subspace"]
    require(subspace["basis_order"] == ["H_u", "H_d^dagger"], "basis order")
    require("span(B_Huv" in subspace["definition"], "subspace definition")
    require(subspace["quadrature_rule_id"] == "Q_sel^U:E_H_UV:HYM_grid:Z24^4:normalized_uniform_trace", "quadrature")
    canonical = rh_packet["canonical_restriction"]
    require(canonical["R_H"] == "R_H(x) = B_Huv^* G_Q x", "R_H formula")
    require(canonical["P_H"] == "P_H = B_Huv R_H = B_Huv B_Huv^* G_Q", "P_H formula")
    require(canonical["R_H_symbolic_exact_payload_emitted"] is True, "R_H not emitted")
    require(canonical["selected_H_sector_restriction_R_H_emitted"] is True, "R_H flag")
    require(canonical["selected_H_projector_P_H_emitted"] is True, "P_H flag")
    require(canonical["R_H_numeric_27x2_entries_evaluated"] is False, "numeric overclaim")
    identities = rh_packet["proof_identities"]
    for key in [
        "R_H_B_Huv_equals_I2",
        "P_H_squared_equals_P_H",
        "P_H_is_G_Q_self_adjoint",
        "image_P_H_equals_span_B_Huv",
        "kernel_R_H_equals_G_Q_orthogonal_complement_of_span_B_Huv",
    ]:
        require(identities[key] is True, f"identity missing {key}")
    for key, value in rh_packet["not_claimed"].items():
        require(value is False, f"R_H packet overclaimed {key}")

    require(route["status"] == "FULL_ROUTE_REDUCED_TO_DYNAMIC_HRESPONSE_OR_DIRECT_MH", "route status")
    closed_inputs = route["closed_route_inputs"]
    for key in [
        "same_q79_F_m1_source_space",
        "B_Huv_source_orthonormal",
        "R_H_kinematic_restriction_from_B_Huv",
        "Pauli_Riesz_three_row_extractors",
        "C5a_trace_grid_identity",
        "no_observed_selector",
    ]:
        require(closed_inputs[key] is True, f"closed route input missing {key}")
    remaining = route["remaining_value_objects"]
    require(remaining["dynamic_H_response_absent"] is True, "dynamic H_response absence")
    require(remaining["M_source_absent"] is True, "M_source absence")
    require(remaining["Huv_absent"] is True, "Huv absence")
    for key in [
        "selected_dynamic_H_response_emitted",
        "selected_Hermitian_M_source_emitted",
        "direct_Herm2_M_H_on_BHuv_emitted",
        "selected_H_response_table_emitted",
    ]:
        require(remaining[key] is False, f"route overclosed {key}")

    require(
        dynamic_gate["status"] == "DYNAMIC_HIGGS_RESPONSE_HESSIAN_ON_BHUV_DOMAIN_OPEN",
        "dynamic gate status",
    )
    required = dynamic_gate["required_object"]
    require(required["codomain"] == "Herm(2) on span(B_Huv)", "dynamic codomain")
    require(required["minimal_rows"] == ["Huu", "Hud_re", "Hud_im", "Hdd"], "minimal rows")
    require(required["trace_free_rows"] == ["Delta", "Re_Omega", "Im_Omega"], "trace-free rows")
    for key, value in dynamic_gate["current_table"].items():
        require(value is None, f"dynamic table overfilled {key}")
    for key, value in dynamic_gate["current_values"].items():
        require(value is None, f"dynamic value overfilled {key}")
    rejected = dynamic_gate["rejected_current_support_as_values"]
    require(rejected["H7B1J_dynamic_hessian_export"]["H_response_exported"] is False, "H7B1J H_response overclaim")
    require(rejected["H7B1L_dynamic_C1_directly_emits_Huv"] is False, "H7B1L Huv overclaim")
    require(rejected["static_or_compact_H_slot_promoted"] is False, "compact H promotion")
    require(rejected["observed_Higgs_or_beta_selector_used"] is False, "observed selector")

    require(
        h7b1j["status"] == "H7B1J_RH_KINEMATIC_GAP_RETIRED_DYNAMIC_HESSIAN_STILL_OPEN",
        "H7B1J status",
    )
    require(h7b1j["old_R_H_exported"] is False, "old R_H expected false")
    require(h7b1j["new_R_H_exported_from_B_Huv"] is True, "new R_H expected true")
    strict = h7b1j["strict_gate_after_R_H_update"]
    for key in [
        "same_q79_F_m1_branch",
        "B_Huv_two_column_lift_source_owned",
        "H_sector_restriction_map_source_owned",
        "no_observed_selector",
    ]:
        require(strict[key] is True, f"strict field should close {key}")
    for key in [
        "dynamic_hessian_or_mass_strain_source_owned",
        "finite_exactness_or_error_certificate_for_values",
        "strict_M_source_gate_passes",
    ]:
        require(strict[key] is False, f"strict field overclosed {key}")
    require(h7b1j["why_still_fails"]["H_response_exported"] is False, "H_response overexport")
    require(h7b1j["why_still_fails"]["M_source_dynamic_part_exported"] is False, "M_source dynamic overexport")

    require(hk_gate["status"] == "H_K_THRESHOLD_GATE_RH_CLOSED_DYNAMIC_MH_OPEN_9_OF_10", "H K status")
    require(hk_gate["accepted_selected_K_source_row_count"] == 9, "H K selected count")
    require(hk_gate["selected_K_threshold_row_count_required"] == 10, "H K required count")
    h_row = hk_gate["H_row"]
    for key in [
        "selected_H_sector_restriction_R_H_emitted",
        "selected_H_projector_P_H_emitted",
        "full_route_reduced_to_dynamic_H_response_or_direct_M_H",
    ]:
        require(h_row[key] is True, f"H row should close {key}")
    for key in [
        "selected_dynamic_H_response_emitted",
        "selected_Hermitian_M_source_emitted",
        "M_source_plus_R_H_values_emitted",
        "direct_Herm2_Huv_payload_emitted",
        "selected_s_beta_value_found",
        "K_threshold_Omega_H_lambda_emitted",
    ]:
        require(h_row[key] is False, f"H row overclosed {key}")
    require(hk_gate["conditional_consequent_current"]["ten_K_antecedent_satisfied"] is False, "ten-K overclaim")
    require(
        hk_gate["conditional_consequent_current"]["strict_Omega_lambda_scalar_execution_closed"]
        is False,
        "Omega/lambda overclaim",
    )

    require(
        cutset["status"] == "NEXT_FRONTIER_DYNAMIC_HIGGS_RESPONSE_HESSIAN_ON_BHUV_OR_DIRECT_MH_VALUE",
        "cutset status",
    )
    require(cutset["next_required_artifact"] == NEXT, "cutset next")
    for phrase in [
        "selected kinematic H-sector restriction R_H=B_Huv^*G_Q emitted",
        "selected H-sector projector P_H=B_HuvB_Huv^*G_Q emitted",
        "full M_source route reduced to selected dynamic H_response or direct Herm(2) M_H",
        "H K-threshold gate remains 9/10",
    ]:
        require(phrase in cutset["closed_here"], f"cutset closed missing {phrase}")
    for phrase in [
        "selected dynamic Higgs response Hessian/mass-strain functional F_H on B_Huv",
        "selected Herm(2) M_H entries Huu,Hud,Hdd or equivalent H_response table",
        "finite exactness/error and source-ownership certificate for M_H values",
        "K_threshold.Omega_H.lambda source row",
    ]:
        require(phrase in cutset["still_open"], f"cutset open missing {phrase}")

    for phrase in [
        "`R_H(x)=B_Huv^* G_Q x`",
        "`P_H=B_Huv R_H`",
        "`R_H B_Huv=I_2`",
        "reduced the full `M_source+R_H` route",
        "selected dynamic Higgs response Hessian",
        NEXT,
    ]:
        require(phrase in note, f"note missing {phrase}")

    print(
        "AUDIT_PASS: canonical R_H from B_Huv is closed; dynamic Higgs "
        "Herm(2) response values remain open."
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
