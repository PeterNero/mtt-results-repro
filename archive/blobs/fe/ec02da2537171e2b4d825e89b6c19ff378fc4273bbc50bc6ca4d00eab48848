"""Audit CONST-HIGGS-01 H6D selected D-term boundary or beta-source gate."""

from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SLUG = "const_higgs_01_h6d_selected_dterm_boundary_or_beta_source"
SCRIPT = ROOT / "scripts" / f"build_{SLUG}.py"
DATA = ROOT / "candidate_data" / f"{SLUG}.candidate.json"
BASE = ROOT / "candidate_data" / SLUG
SINGLE_HIGGS_IMPORT = BASE / "single_higgs_projection_import.packet.json"
BETA_SOURCE_TEST = BASE / "beta_or_projection_angle_source_test.packet.json"
DTERM_CONTRACT = BASE / "dterm_boundary_acceptance_contract.packet.json"
NEXT_WORK = BASE / "next_labeled_workorder.packet.json"
CERT = ROOT / "certificates" / f"{SLUG}_certificate.json"
NOTE = ROOT / "proof_corpus" / "MTT_CONST_HIGGS_01_H6D_SelectedDTermBoundaryOrBetaSource_v1.md"

STATUS = "MTT_CONST_HIGGS_01_H6D_DTERM_BOUNDARY_CONTRACT_BUILT_BETA_SOURCE_OPEN"


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
    single_higgs = load(SINGLE_HIGGS_IMPORT)
    beta_test = load(BETA_SOURCE_TEST)
    dterm = load(DTERM_CONTRACT)
    next_work = load(NEXT_WORK)
    cert = load(CERT)
    note = NOTE.read_text(encoding="utf-8")

    for name, item in [
        ("candidate", candidate),
        ("single_higgs", single_higgs),
        ("beta_test", beta_test),
        ("dterm", dterm),
    ]:
        clean(item, name)

    require(candidate["status"] == STATUS, "candidate status")
    require(candidate["theorem"]["proved"] is True, "candidate theorem")
    require(candidate["low_energy_single_Higgs_projection_imported"] is True, "single Higgs import")
    require(candidate["Dterm_boundary_formula_ready"] is True, "formula ready")
    require(candidate["standard_Dterm_boundary_formula_factor"] == "1/8", "formula factor")
    require(candidate["selected_beta_or_tan_beta_source_found"] is False, "beta overselected")
    require(candidate["selected_two_Higgs_projection_angle_found"] is False, "angle overselected")
    require(candidate["representative_tan_beta_10_promoted"] is False, "tan beta promoted")
    require(candidate["selected_Dterm_boundary_packet_closed"] is False, "D-term packet overclosed")
    require(candidate["DTerm_boundary_numeric_value_derived"] is False, "D-term numeric overderived")
    require(candidate["Higgs_quartic_numeric_value_derived"] is False, "lambda overderived")
    require(candidate["strict_no_knob_Higgs_closure"] is False, "strict no-knob")
    require(candidate["new_Higgs_specific_parameters"] == 0, "Higgs params")

    projection = single_higgs["imported_projection"]
    require(projection["physical_doublet"] == "H", "physical doublet")
    require(projection["hypercharge"] == "+1/2", "hypercharge")
    require(projection["H_u"] == "H", "H_u")
    require(projection["H_d"] == "H^dagger", "H_d")
    require(projection["single_higgs_channel_projection"] is True, "projection closed")
    require(projection["two_independent_low_energy_higgs_alignment_references"] is False, "two Higgs low energy")
    closes = single_higgs["what_this_closes_for_H6D"]
    require(closes["which_low_energy_Higgs_doublet"] is True, "which doublet")
    require(closes["H_u_H_d_channel_conjugation"] is True, "channel conjugation")
    require(closes["no_second_low_energy_alignment_mode_as_flavor_knob"] is True, "no second mode")
    open_ = single_higgs["what_this_does_not_close_for_H6D"]
    require(open_["UV_two_Higgs_VEV_ratio"] is True, "UV ratio open")
    require(open_["selected_beta_or_tan_beta"] is True, "beta open")
    require(open_["selected_Dterm_projection_angle"] is True, "angle open")
    require(open_["RG_threshold_matching"] is True, "RG open")

    candidates = {item["id"]: item for item in beta_test["candidate_sources"]}
    require(candidates["theta_execution_tan_beta_10"]["accepted_as_source"] is False, "theta tan beta accepted")
    require(candidates["theta_execution_tan_beta_10"]["candidate_value"] == 10, "theta tan beta value")
    require(candidates["theta_execution_tan_beta_10"]["would_add_Higgs_specific_parameter_if_used_now"] is True, "theta parameter")
    require(candidates["q79_single_higgs_projection"]["accepted_as_source"] is False, "single Higgs beta")
    require(candidates["q79_single_higgs_projection"]["would_add_Higgs_specific_parameter_if_used_now"] is False, "single Higgs param")
    require(candidates["single_universal_or_Higgs_primitive_beta"]["classification"] == "ALLOWED_ONLY_AS_EXPLICIT_NON_NO_KNOB_EXTENSION", "primitive classification")
    negative = beta_test["negative_result"]
    require(negative["selected_beta_or_tan_beta_source_found"] is False, "negative beta")
    require(negative["selected_two_Higgs_projection_angle_found"] is False, "negative angle")
    require(negative["representative_tan_beta_10_promoted"] is False, "negative representative")
    require(negative["single_higgs_projection_promoted_to_beta"] is False, "negative projection")
    require(negative["observed_Higgs_or_lambda_backsolve_used"] is False, "negative backsolve")
    require(beta_test["superset_strategy"]["paths_combined_as_free_parameters"] is False, "superset params")

    boundary = dterm["boundary_formula"]
    require(boundary["potential_convention"] == "V(H)=-m^2 |H|^2 + lambda |H|^4", "potential convention")
    require(boundary["formula"] == "lambda = (g^2 + g'^2) * cos^2(2 beta) / 8", "formula")
    require(boundary["standard_factor"] == "1/8", "boundary factor")
    require(boundary["old_factor_overhigh_by_two_under_standard_convention"] is True, "factor warning")
    filled = dterm["current_filled_fields"]
    require(filled["correct_formula_factor"] is True, "filled factor")
    require(filled["low_energy_single_Higgs_projection"] is True, "filled single Higgs")
    require(filled["selector_guardrail"] is True, "filled selector")
    required = dterm["required_before_numeric_boundary_value"]
    for key in [
        "selected_gauge_boundary_values",
        "selected_beta_or_two_Higgs_projection_angle",
        "matching_scale_policy",
        "threshold_RG_transport",
        "one_universal_metrology_or_action_primitive_if_needed",
    ]:
        require(required[key]["filled"] is False, f"{key} overfilled")
    acceptance = dterm["acceptance_after_H6D"]
    require(acceptance["Dterm_formula_ready"] is True, "acceptance formula")
    require(acceptance["low_energy_Higgs_channel_ready"] is True, "acceptance single Higgs")
    require(acceptance["selected_Dterm_boundary_packet_closed"] is False, "acceptance packet")
    require(acceptance["DTerm_boundary_numeric_value_derived"] is False, "acceptance numeric")
    require(acceptance["Higgs_quartic_numeric_value_derived"] is False, "acceptance lambda")
    require(acceptance["strict_no_knob_Higgs_closure"] is False, "acceptance no-knob")
    require("representative tan_beta=10 -> selected beta" in dterm["forbidden_promotions"], "forbidden tan beta")
    require("single-Higgs projection -> UV tan_beta value" in dterm["forbidden_promotions"], "forbidden projection")

    require("H6E-UV-TWO-HIGGS-PROJECTION-ANGLE-SOURCE" in next_work["primary"]["label"], "next primary")
    require("H6E-PRIMITIVE-BETA-POLICY" in next_work["secondary"]["label"], "next secondary")
    require(cert["status"] == STATUS, "cert status")
    require(cert["low_energy_single_Higgs_projection_imported"] is True, "cert single Higgs")
    require(cert["Dterm_boundary_formula_ready"] is True, "cert formula")
    require(cert["selected_beta_or_tan_beta_source_found"] is False, "cert beta")
    require(cert["selected_two_Higgs_projection_angle_found"] is False, "cert angle")
    require(cert["DTerm_boundary_numeric_value_derived"] is False, "cert D-term")
    require(cert["Higgs_quartic_numeric_value_derived"] is False, "cert lambda")
    require(cert["strict_no_knob_Higgs_closure"] is False, "cert no-knob")
    require("H6D-SELECTED-DTERM" in note and "H6E-UV-TWO-HIGGS" in note, "note")

    print("CONST-HIGGS-01 H6D selected D-term boundary / beta-source audit: PASS")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
