"""Audit CONST-HIGGS-01 H7B1G B_Huv or M_source fill attempt."""

from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SLUG = "const_higgs_01_h7b1g_fill_bhuv_or_msource"
SCRIPT = ROOT / "scripts" / f"build_{SLUG}.py"
DATA = ROOT / "candidate_data" / f"{SLUG}.candidate.json"
BASE = ROOT / "candidate_data" / SLUG
SUPPORT_SPLIT = BASE / "support_split_theorem.packet.json"
CURRENT_FILL = BASE / "current_fill_attempt.packet.json"
BHUV_REQUEST = BASE / "bhuv_minimal_lift_payload_request.packet.json"
MSOURCE_REQUEST = BASE / "msource_minimal_operator_payload_request.packet.json"
NO_CURRENT_SOURCE = BASE / "no_current_source_value_emission.packet.json"
NEXT_WORK = BASE / "next_labeled_workorder.packet.json"
CERT = ROOT / "certificates" / f"{SLUG}_certificate.json"
NOTE = ROOT / "proof_corpus" / "MTT_CONST_HIGGS_01_H7B1G_FillBHuvOrMSource_v1.md"

STATUS = "MTT_CONST_HIGGS_01_H7B1G_FILL_ATTEMPT_SUPPORT_SPLIT_VALUES_OPEN"


def load(path: Path) -> dict[str, object]:
    return json.loads(path.read_text(encoding="utf-8"))


def require(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)


def clean(packet: dict[str, object], name: str) -> None:
    require(packet["observed_data_used_as_selector"] is False, f"{name} observed selector")
    require(packet["target_fitting_used"] is False, f"{name} target fitting")
    require(packet["closure_claimed"] is False, f"{name} closure overclaim")


def require_all_false(packet: dict[str, object], keys: list[str], name: str) -> None:
    for key in keys:
        require(packet[key] is False, f"{name} overclosed {key}")


def main() -> int:
    proc = subprocess.run(
        [sys.executable, str(SCRIPT)],
        cwd=ROOT,
        text=True,
        stdout=subprocess.PIPE,
        stderr=subprocess.STDOUT,
        check=True,
    )
    computed = json.loads(proc.stdout)
    require(computed["status"] == STATUS, "builder status mismatch")

    candidate = load(DATA)
    support_split = load(SUPPORT_SPLIT)
    current_fill = load(CURRENT_FILL)
    bhuv_request = load(BHUV_REQUEST)
    msource_request = load(MSOURCE_REQUEST)
    no_current_source = load(NO_CURRENT_SOURCE)
    next_work = load(NEXT_WORK)
    cert = load(CERT)
    note = NOTE.read_text(encoding="utf-8")

    for name, packet in [
        ("candidate", candidate),
        ("support_split", support_split),
        ("current_fill", current_fill),
        ("bhuv_request", bhuv_request),
        ("msource_request", msource_request),
        ("no_current_source", no_current_source),
        ("cert", cert),
    ]:
        clean(packet, name)

    require(candidate["status"] == STATUS, "candidate status")
    require(candidate["theorem"]["proved"] is True, "theorem not proved")
    require(candidate["H7B1F_reduction_contract_imported"] is True, "H7B1F contract not imported")
    require(candidate["support_split_theorem_proved"] is True, "support split")
    require(candidate["B_Huv_support_present"] is True, "B_Huv support")
    require(candidate["M_source_support_present"] is True, "M_source support")
    require(candidate["both_payloads_required_for_Huv"] is True, "both payloads rule")
    require(candidate["new_Higgs_specific_parameters"] == 0, "new Higgs parameters")
    require_all_false(
        candidate,
        [
            "B_Huv_value_emitted",
            "M_source_value_emitted",
            "selected_Huv_basis_binding_found",
            "selected_Higgs_lift_B_Huv_found",
            "selected_Hermitian_M_source_found",
            "selected_finite_Huv_reduction_found",
            "selected_offdiagonal_Omega_found",
            "selected_Huu_Hud_Hdd_found",
            "selected_Delta_Omega_found",
            "selected_s_beta_value_found",
            "numeric_lambda_H_derived",
            "strict_no_knob_Higgs_closure",
        ],
        "candidate",
    )

    require(support_split["status"] == "BHUV_AND_MSOURCE_SUPPORT_SPLIT_PROVED_VALUES_OPEN", "split status")
    require(support_split["theorem"]["proved"] is True, "split theorem")
    require(len(support_split["proof_steps"]) == 4, "split proof steps")
    bhuv_support = support_split["bhuv_support"]
    msource_support = support_split["msource_support"]
    require(bhuv_support["value_emitted"] is False, "B_Huv emitted")
    require(msource_support["value_emitted"] is False, "M_source emitted")
    require(bhuv_support["support_closed"]["E6_representation_bridge"] is True, "E6 bridge")
    require(bhuv_support["support_closed"]["SM_slot_functor_all_six_arrows"] is True, "SM slot arrows")
    require(bhuv_support["support_closed"]["static_SM_slot_tier"] is True, "static tier")
    require(bhuv_support["support_closed"]["single_Higgs_quotient_imported"] is True, "single quotient")
    require(bhuv_support["support_closed"]["quotient_to_projector_underdetermined"] is True, "underdetermination")
    for key in [
        "physical_light_higgs_doublet_selection",
        "color_triplet_projection_or_decoupling",
        "channel_weights",
        "family_or_Higgs_kinetic_metrics",
        "selected_metric_on_two_Higgs_plane",
        "selected_rank_one_light_projector",
        "selected_splitting_source",
        "two_column_source_orthonormal_lift_B_Huv",
    ]:
        require(bhuv_support["still_missing_for_B_Huv"][key] is True, f"B missing {key}")

    require(msource_support["support_closed"]["rank2_valpha_model_selected"] is True, "rank2")
    require(msource_support["support_closed"]["terminal_L_L2_source_closed"] is True, "terminal L")
    require(msource_support["support_closed"]["nonzero_ext_class_selected"] is True, "nonzero Ext")
    require(msource_support["support_closed"]["finite_operator_extraction_contract_built"] is True, "contract")
    require(msource_support["support_closed"]["rhoE_mesh_shape_passes"] is True, "rhoE mesh")
    require(msource_support["support_closed"]["rhoE_metric_shape_passes"] is True, "rhoE metric")
    require(msource_support["support_closed"]["sector_maps_shape_passes"] is True, "sector maps")
    require(msource_support["support_closed"]["primitive_vertex_source_selector_promoted"] is True, "selector")
    for key in [
        "selected_source_identity",
        "source_certificate",
        "pic0_selected_or_quotiented",
        "non_split_stability_or_hym_proved",
        "route_c_residual_selected_source_verified",
        "selected_operator_values_closed",
        "actual_extraction_theorem_supplied",
        "actual_visible_operator_payload_emitted",
        "honest_operator_pipeline_pass",
        "sector_D_E_packets_pass",
        "reduced_green_packets_pass",
        "dotD_packets_pass",
        "primitive_C1_or_Yukawa_contractions",
        "selected_Hermitian_mass_strain_operator",
    ]:
        require(msource_support["still_missing_for_M_source"][key] is True, f"M missing {key}")

    require(bhuv_request["status"] == "BHUV_MINIMAL_LIFT_PAYLOAD_REQUESTED_NOT_EMITTED", "B request status")
    require(bhuv_request["same_source_branch"] == "q79/F,m=1", "B branch")
    require(len(bhuv_request["must_emit"]) == 7, "B must emit count")
    require("two finite source-space column vectors" in bhuv_request["must_emit"][1], "B columns")
    require(bhuv_request["acceptance_tests"]["same_source_with_M_source_required_for_Huv"] is True, "B same source")
    require(bhuv_request["acceptance_tests"]["current_payload_emitted"] is False, "B current emitted")
    require("tan_beta backsolve" in bhuv_request["acceptance_tests"]["forbid_observed_selectors"], "B forbids beta")

    require(msource_request["status"] == "MSOURCE_MINIMAL_OPERATOR_PAYLOAD_REQUESTED_NOT_EMITTED", "M request status")
    require(msource_request["same_source_branch"] == "q79/F,m=1", "M branch")
    require(len(msource_request["must_emit"]) == 7, "M must emit count")
    require("Hermitian mass/strain" in msource_request["must_emit"][3], "M Hermitian")
    require(msource_request["acceptance_tests"]["same_source_with_B_Huv_required_for_Huv"] is True, "M same source")
    require(msource_request["acceptance_tests"]["Hermiticity_required"] is True, "M Hermiticity")
    require(msource_request["acceptance_tests"]["current_payload_emitted"] is False, "M current emitted")
    require("benchmark Yukawa or CKM entries" in msource_request["acceptance_tests"]["forbid_observed_selectors"], "M forbids benchmark")

    values = no_current_source["value_emission_matrix"]
    for key in ["B_Huv", "M_source", "H_uv", "Omega", "s_beta", "lambda_H"]:
        require(values[key]["value_emitted"] is False, f"value emitted {key}")
    require(values["H_uv"]["reason"] == "H_uv requires both B_Huv and M_source from the same source", "Huv reason")

    for route in current_fill["attempted_routes"].values():
        require(route["support_closed"] is True, "route support")
        require(route["value_emitted"] is False, "route value")
        require(len(route["blocked_by"]) == 4, "blocked-by shape")
    for key in ["Huv", "Delta", "Omega", "s_beta", "lambda_H"]:
        require(current_fill["computed_values"][key] is None, f"computed {key}")
    require(current_fill["new_Higgs_specific_parameters"] == 0, "current new params")

    require(next_work["status"] == "NEXT_WORKORDER_H7B1H_SOURCE_EXPORT_FIRST_ACTUAL_PAYLOAD", "next status")
    require("H7B1H-SOURCE-EXPORT-FIRST-ACTUAL-PAYLOAD" in next_work["primary_next"]["label"], "next label")
    require(len(next_work["recommended_order"]) == 3, "next order")

    require(cert["status"] == STATUS, "cert status")
    require(cert["support_split_theorem_proved"] is True, "cert split")
    require(cert["B_Huv_support_present"] is True, "cert B support")
    require(cert["M_source_support_present"] is True, "cert M support")
    require(cert["B_Huv_value_emitted"] is False, "cert B emitted")
    require(cert["M_source_value_emitted"] is False, "cert M emitted")
    require(cert["numeric_lambda_H_derived"] is False, "cert lambda")
    require("H_uv = B_Huv^* M_source B_Huv" in note, "note formula")
    require("No observed Higgs mass" in note, "note guardrail")

    print("CONST-HIGGS-01 H7B1G B_Huv or M_source fill attempt audit: PASS")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
