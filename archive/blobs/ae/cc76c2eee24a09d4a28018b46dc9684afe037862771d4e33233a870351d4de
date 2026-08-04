"""Audit the full M_source + R_H route attempt."""

from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SLUG = "selected_fullmsourcehsectorrestriction_or_hresponsehuvtable"
DATA = ROOT / "candidate_data" / f"{SLUG}.candidate.json"
PACKET_DIR = ROOT / "candidate_data" / SLUG
FULL_ROUTE = PACKET_DIR / "full_msource_rh_route_instantiation.packet.json"
SOURCE_GATE = PACKET_DIR / "selected_source_object_value_gate.packet.json"
H7B1J_RECHECK = PACKET_DIR / "h7b1j_after_bhuv_lift_recheck.packet.json"
DIRECT_TABLE = PACKET_DIR / "direct_hresponse_huv_table_after_full_route.packet.json"
HK_GATE = PACKET_DIR / "hk_threshold_gate_after_full_msource_route.packet.json"
CUTSET = PACKET_DIR / "next_cutset_after_full_msource_route.packet.json"
CERT = ROOT / "certificates" / f"{SLUG}_certificate.json"
NOTE = ROOT / "proof_corpus" / "MTT_Selected_FullMSourceHSectorRestriction_or_HResponseHuvTable_v1.md"
BUILDER = ROOT / "scripts" / f"build_{SLUG}.py"

STATUS = (
    "MTT_SELECTED_FULLMSOURCEHSECTORRESTRICTION_OR_HRESPONSEHUVTABLE_"
    "FORMULA_INSTANTIATED_DYNAMIC_RH_VALUES_OPEN"
)
NEXT = "MTT_Selected_DynamicHiggsResponseHessian_or_HSectorRestrictionExport_v1"


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
    full_route = load(FULL_ROUTE)
    source_gate = load(SOURCE_GATE)
    h7b1j = load(H7B1J_RECHECK)
    direct = load(DIRECT_TABLE)
    hk_gate = load(HK_GATE)
    cutset = load(CUTSET)
    cert = load(CERT)
    note = NOTE.read_text(encoding="utf-8")

    for label, packet in [
        ("candidate", data),
        ("full route", full_route),
        ("source gate", source_gate),
        ("H7B1J recheck", h7b1j),
        ("direct table", direct),
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
    require(cert["true_SM_equivalence_claimed"] is False, "cert true SM overclaim")
    require(cert["full_no_knob_closure_claimed"] is False, "cert no-knob overclaim")

    decision = data["closure_decision"]
    for key in [
        "full_M_source_R_H_formula_instantiated",
        "same_q79_F_m1_source_space_verified",
        "B_Huv_two_column_uv_lift_emitted",
        "same_source_functional_alpha1_dotD_side_closed",
        "Pauli_Riesz_three_row_source_functional_contract_closed",
        "C5a_trace_grid_identity_closed",
        "old_H7B1J_B_Huv_gap_retired",
    ]:
        require(decision[key] is True, f"decision should close {key}")
    for key in [
        "selected_dynamic_H_response_emitted",
        "selected_H_sector_restriction_R_H_emitted",
        "selected_Hermitian_M_source_emitted",
        "M_source_plus_R_H_values_emitted",
        "selected_H_response_table_emitted",
        "direct_Herm2_Huv_payload_emitted",
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

    require(full_route["status"] == "FULL_MSOURCE_RH_FORMULA_INSTANTIATED_VALUES_OPEN", "full route status")
    require(full_route["source_space"]["basis_dimension"] == 27, "source dimension")
    require(full_route["source_space"]["branch"]["q"] == 79, "source q")
    require(full_route["source_space"]["branch"]["orientation"] == "F", "source orientation")
    require(full_route["source_space"]["branch"]["torsion_label_m"] == 1, "source m")
    require(
        full_route["formula"]["expanded"]
        == "H_uv = B_Huv^* Herm(R_H^* H_response R_H) B_Huv",
        "expanded formula",
    )
    route_inputs = full_route["route_inputs_now_closed"]
    for key in [
        "same_q79_F_m1_branch",
        "finite_source_space_dimension_27",
        "B_Huv_two_column_source_orthonormal_lift",
        "B_Huv_symbolic_exact_payload",
        "Pauli_Riesz_three_row_source_functional_contract",
        "same_source_functional_alpha1_dotD_side",
        "C5a_trace_grid_identity",
        "no_observed_selector",
    ]:
        require(route_inputs[key] is True, f"route input missing {key}")
    value_eval = full_route["value_evaluation"]
    require(value_eval["possible_now"] is False, "value evaluation overclosed")
    require(value_eval["M_source_value_emitted"] is False, "M_source value overemitted")
    require(value_eval["Huv_value_emitted"] is False, "Huv value overemitted")
    for key, value in value_eval["computed_values"].items():
        require(value is None, f"computed value overfilled {key}")
    require(full_route["equivalent_direct_exit"]["direct_M_H_emitted_now"] is False, "direct M_H overemitted")

    require(
        source_gate["status"] == "SELECTED_HRESPONSE_AND_RH_SOURCE_OBJECTS_STILL_OPEN",
        "source gate status",
    )
    required = source_gate["required_selected_source_objects"]
    require(required["H_response"]["required"] is True, "H_response not required")
    require(required["H_response"]["emitted"] is False, "H_response overemitted")
    require(required["H_response"]["current_value"] is None, "H_response value overfilled")
    require(required["H_response"]["strict_export_passes"] is False, "H_response strict pass overclaim")
    require(required["R_H"]["required"] is True, "R_H not required")
    require(required["R_H"]["emitted"] is False, "R_H overemitted")
    require(required["R_H"]["current_value"] is None, "R_H value overfilled")
    require(required["R_H"]["old_B_Huv_gap_retired_by_this_repo"] is True, "B_Huv gap not retired")
    require(required["R_H"]["strict_export_passes"] is False, "R_H strict pass overclaim")
    absent = source_gate["derived_objects_currently_absent"]
    for key in [
        "H_response_absent",
        "R_H_absent",
        "M_source_absent",
        "Huv_absent",
        "Delta_Omega_s_beta_absent",
        "lambda_H_absent",
    ]:
        require(absent[key] is True, f"absence guard failed {key}")
    require(source_gate["static_prefix_nonimplication"]["obstruction_theorem_proved"] is True, "obstruction not imported")
    scope = source_gate["matter_functional_scope_guard"]
    require(scope["same_source_functional_side_closed"] is True, "same-source side not closed")
    require(scope["contains_Huv"] is False, "matter scope overclaims Huv")
    require(scope["contains_H_u"] is False, "matter scope overclaims Hu")
    require(scope["contains_H_d_dagger"] is False, "matter scope overclaims Hd dagger")

    require(
        h7b1j["status"] == "H7B1J_RECHECK_BHUV_GAP_RETIRED_RH_DYNAMIC_VALUES_STILL_OPEN",
        "H7B1J status",
    )
    updated = h7b1j["updated_required_fields"]
    require(updated["B_Huv_two_column_lift_source_owned"] is True, "B_Huv not updated")
    for key in [
        "H_sector_restriction_map_source_owned",
        "dynamic_hessian_or_mass_strain_source_owned",
        "finite_exactness_or_error_certificate_for_values",
    ]:
        require(updated[key] is False, f"H7B1J overclosed {key}")
    require(h7b1j["what_changed"]["old_H7B1J_B_Huv_or_two_column_lift_exported"] is False, "old B_Huv should be false")
    require(h7b1j["what_changed"]["current_repo_B_Huv_two_column_lift_exported"] is True, "new B_Huv should be true")
    remains = h7b1j["what_remains_open"]
    for key in [
        "H_response_exported",
        "M_source_dynamic_part_exported",
        "H_sector_restriction_map_exported",
        "R_H_exported",
        "strict_gate_passes",
    ]:
        require(remains[key] is False, f"H7B1J remains overclosed {key}")
    require(h7b1j["decision"]["strict_M_source_gate_passes_after_B_Huv_update"] is False, "strict gate pass overclaim")

    require(
        direct["status"] == "HRESPONSE_HUV_TABLE_STILL_VALUES_OPEN_AFTER_FULL_ROUTE_ATTEMPT",
        "direct status",
    )
    require(direct["full_route_formula_instantiated"] is True, "direct formula not instantiated")
    for key in [
        "M_source_plus_R_H_values_emitted",
        "selected_H_response_table_emitted",
        "direct_Herm2_Huv_payload_emitted",
    ]:
        require(direct[key] is False, f"direct table overclosed {key}")
    for key, value in direct["required_table"].items():
        require(value is None, f"required table overfilled {key}")
    for key, value in direct["values_emitted_now"].items():
        require(value is None, f"value overfilled {key}")

    require(
        hk_gate["status"] == "H_K_THRESHOLD_GATE_FULL_MSOURCE_RH_TRIED_VALUES_OPEN_9_OF_10",
        "H K status",
    )
    require(hk_gate["accepted_selected_K_source_row_count"] == 9, "H K selected count")
    require(hk_gate["selected_K_threshold_row_count_required"] == 10, "H K required count")
    h_row = hk_gate["H_row"]
    require(h_row["full_M_source_R_H_formula_instantiated"] is True, "H row formula")
    for key in [
        "selected_dynamic_H_response_emitted",
        "selected_H_sector_restriction_R_H_emitted",
        "selected_Hermitian_M_source_emitted",
        "M_source_plus_R_H_values_emitted",
        "selected_H_response_table_emitted",
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
    require(hk_gate["conditional_consequent_current"]["accepted_internal_scalar_value_row_count"] == 0, "scalar rows")

    require(
        cutset["status"]
        == "NEXT_FRONTIER_DYNAMIC_HIGGS_RESPONSE_HESSIAN_OR_HSECTOR_RESTRICTION_EXPORT",
        "cutset status",
    )
    require(cutset["next_required_artifact"] == NEXT, "cutset next")
    for phrase in [
        "full M_source+R_H route formula instantiated on the same q79/F,m=1 finite source space",
        "old H7B1J B_Huv gap retired while R_H and dynamic H_response remain open",
        "H K-threshold gate remains 9/10",
    ]:
        require(phrase in cutset["closed_here"], f"cutset closed missing {phrase}")
    for phrase in [
        "selected dynamic Higgs response Hessian or mass/strain block H_response",
        "selected H-sector restriction map R_H from the 27-mode source to the two-Higgs response subspace",
        "Hermitian M_source entries and exactness/error certificate",
        "direct H_response/Huv table values Huu,Hud,Hdd as an equivalent shortcut",
        "K_threshold.Omega_H.lambda source row",
        "C5b physical Higgs projection-measure equality and C6 no-extra-boundary/source theorem",
    ]:
        require(phrase in cutset["still_open"], f"cutset open missing {phrase}")

    for phrase in [
        "instantiated the full route",
        "`M_source = Herm(R_H^* H_response R_H)`",
        "`Huv = B_Huv^* M_source B_Huv`",
        "retired the old H7B1J `B_Huv` gap",
        "selected dynamic Higgs response Hessian",
        "selected H-sector restriction map `R_H`",
        NEXT,
    ]:
        require(phrase in note, f"note missing {phrase}")

    print(
        "AUDIT_PASS: full M_source+R_H route is instantiated; selected "
        "H_response/R_H values remain the live blocker."
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
