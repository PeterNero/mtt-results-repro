"""Audit CONST-HIGGS-01 H7B1E binding retirement and Omega route."""

from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SLUG = "const_higgs_01_h7b1e_binding_retirement_and_omega_route"
SCRIPT = ROOT / "scripts" / f"build_{SLUG}.py"
DATA = ROOT / "candidate_data" / f"{SLUG}.candidate.json"
BASE = ROOT / "candidate_data" / SLUG
BINDING_AUDIT = BASE / "diagonal_binding_retirement.packet.json"
OMEGA_ROUTE = BASE / "nonsplit_omega_route_status.packet.json"
EXTERNAL_GUARDRAIL = BASE / "external_and_corpus_guardrail.packet.json"
NEXT_WORK = BASE / "next_labeled_workorder.packet.json"
CERT = ROOT / "certificates" / f"{SLUG}_certificate.json"
NOTE = ROOT / "proof_corpus" / "MTT_CONST_HIGGS_01_H7B1E_BindingRetirementAndOmegaRoute_v1.md"

STATUS = "MTT_CONST_HIGGS_01_H7B1E_DIAGONAL_BINDING_RETIRED_NONSPLIT_OMEGA_ROUTE_OPEN"


def load(path: Path) -> dict[str, object]:
    return json.loads(path.read_text(encoding="utf-8"))


def require(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)


def clean(packet: dict[str, object], name: str) -> None:
    require(packet["observed_data_used_as_selector"] is False, f"{name} observed selector")
    require(packet["target_fitting_used"] is False, f"{name} target fitting")
    require(packet["closure_claimed"] is False, f"{name} closure overclaim")


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
    binding = load(BINDING_AUDIT)
    omega = load(OMEGA_ROUTE)
    guardrail = load(EXTERNAL_GUARDRAIL)
    next_work = load(NEXT_WORK)
    cert = load(CERT)
    note = NOTE.read_text(encoding="utf-8")

    for name, item in [
        ("candidate", candidate),
        ("binding", binding),
        ("omega", omega),
        ("guardrail", guardrail),
    ]:
        clean(item, name)

    require(candidate["status"] == STATUS, "candidate status")
    require(candidate["theorem"]["proved"] is True, "candidate theorem")
    require(candidate["diagonal_binding_retired_as_strict_route"] is True, "diagonal retired")
    require(candidate["diagonal_support_preserved_conditionally"] is True, "support preserved")
    require(candidate["nonsplit_valpha_route_selected_as_primary"] is True, "nonsplit primary")
    require(candidate["rank2_valpha_model_selected"] is True, "rank2 selected")
    require(candidate["terminal_L_L2_source_closed"] is True, "terminal source")
    require(candidate["nonzero_ext_class_selected"] is True, "nonzero ext")
    for key in [
        "selected_Huv_basis_binding_found",
        "selected_finite_Huv_reduction_found",
        "selected_offdiagonal_Omega_found",
        "selected_Huu_Hud_Hdd_found",
        "selected_Delta_Omega_found",
        "selected_s_beta_value_found",
        "selected_EW_boundary_RG_packet_closed",
        "numeric_lambda_H_derived",
        "strict_no_knob_Higgs_closure",
    ]:
        require(candidate[key] is False, f"candidate overclosed {key}")
    require(candidate["new_Higgs_specific_parameters"] == 0, "new params")

    require(binding["status"] == "DIAGONAL_HYM_TO_HUV_BINDING_RETIRED_AS_STRICT_ROUTE", "binding status")
    support = binding["positive_support_kept"]
    require(support["diagonal_rank2_metric_found"] is True, "diag support")
    require(support["diagonal_nonzero_strain_found"] is True, "diag strain")
    require(support["conditional_readout_if_later_bound"] == "Omega=0, s_beta=1", "conditional preserved")
    reasons = binding["retirement_reasons"]
    require(len(reasons) == 4, "retirement reason count")
    require(reasons[0]["evidence"] == "VISIBLE_SPLIT_LINE_HYM_SOURCE_NO_GO_NONABELIAN_OR_ROUTE_C_REQUIRED", "split no-go evidence")
    decision = binding["decision"]
    require(decision["diagonal_binding_promoted"] is False, "binding promoted")
    require(decision["diagonal_binding_retired_as_strict_route"] is True, "binding retired")

    closed = omega["closed_support_fields"]
    require(closed["rank2_valpha_model_selected"] is True, "omega rank2")
    require(closed["terminal_monad_difference_L3_minus_K2_selector_closed"] is True, "omega terminal")
    require(closed["ordered_source_validator_passes"] is True, "omega validator")
    require(closed["selected_L"] == [1, -2, 0], "selected L")
    require(closed["selected_L2"] == [2, -4, 0], "selected L2")
    require(closed["h1_L2"] == 8, "h1")
    require(closed["nonzero_ext_class_selected"] is True, "nonzero ext route")
    require(closed["c2_valpha"] == [4, 0, 0], "c2")
    open_fields = omega["open_source_fields_before_Omega_or_Huv"]
    for key in [
        "pic0_selected_or_quotiented",
        "non_split_stability_or_hym_proved",
        "orientation_selection_justified_by_source",
        "typed_transition_or_rhoE_data_emitted",
        "hym_strominger_or_routec_residual_pass",
        "sector_D_E_packets_pass",
        "reduced_green_packets_pass",
        "dotD_packets_pass",
        "primitive_C1_or_Yukawa_contractions",
        "same_source_Chern_Weil_row_derived",
        "selected_RouteC_residual_DE_values_emitted",
    ]:
        require(open_fields[key] is False, f"omega route overclosed {key}")
    implication = omega["Huv_implication"]
    require(implication["offdiagonal_Omega_source_found"] is False, "Omega overfound")
    require(implication["finite_Huv_packet_found"] is False, "Huv overfound")
    require("non-split V_alpha/Route-C" in implication["minimal_next_source_object"], "minimal source")

    require(guardrail["status"] == "GUARDRAIL_SUPPORTS_SEPARATING_HYM_BUNDLE_METRIC_FROM_HIGGS_DOUBLET_SELECTION", "guardrail status")
    require(len(guardrail["external_method_guardrails"]) == 2, "external count")
    for item in guardrail["external_method_guardrails"]:
        require(item["used_as_selector"] is False, "external selector")
    result = guardrail["result"]
    require(result["diagonal_metric_lines_may_not_be_identified_with_Higgs_slots_without_source_theorem"] is True, "guardrail result")
    require(result["external_sources_used_as_numeric_or_physical_selector"] is False, "guardrail selector result")

    require("H7B1F-NONSPLIT-VALPHA-TO-HUV-OMEGA-PACKET" in next_work["primary_next"]["label"], "next primary")
    require("H7B2-SELECTED-EW-BOUNDARY-RG-PACKET" in next_work["parallel_next"]["label"], "next parallel")
    require(cert["status"] == STATUS, "cert status")
    require(cert["diagonal_binding_retired_as_strict_route"] is True, "cert retired")
    require(cert["nonsplit_valpha_route_selected_as_primary"] is True, "cert primary")
    require(cert["selected_offdiagonal_Omega_found"] is False, "cert Omega")
    require(cert["numeric_lambda_H_derived"] is False, "cert lambda")
    require(cert["strict_no_knob_Higgs_closure"] is False, "cert closure")
    require("diagonal HYM binding retired as strict route" in note, "note retired")
    require("non-split rank-two" in note, "note route")
    require("no `Omega`, no finite `H_uv`, and no `lambda_H` yet" in note, "note guardrail")

    print("CONST-HIGGS-01 H7B1E binding retirement and Omega route audit: PASS")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
