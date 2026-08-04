"""Audit CONST-HIGGS-01 H6C H-sector row or boundary-route discriminator."""

from __future__ import annotations

import json
import math
import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SLUG = "const_higgs_01_h6c_hsector_row_or_boundary_route_discriminator"
SCRIPT = ROOT / "scripts" / f"build_{SLUG}.py"
DATA = ROOT / "candidate_data" / f"{SLUG}.candidate.json"
BASE = ROOT / "candidate_data" / SLUG
ROW_SEARCH = BASE / "actual_hsector_fourth_row_search.packet.json"
BOUNDARY_IMPORT = BASE / "susy_dterm_boundary_route_import.packet.json"
ROUTE_DECISION = BASE / "route_discriminator_decision.packet.json"
NEXT_WORK = BASE / "next_labeled_workorder.packet.json"
CERT = ROOT / "certificates" / f"{SLUG}_certificate.json"
NOTE = ROOT / "proof_corpus" / "MTT_CONST_HIGGS_01_H6C_HSectorRowOrBoundaryRouteDiscriminator_v1.md"

STATUS = "MTT_CONST_HIGGS_01_H6C_ROW_ABSENT_BOUNDARY_ROUTE_IDENTIFIED"


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
    row_search = load(ROW_SEARCH)
    boundary_import = load(BOUNDARY_IMPORT)
    route_decision = load(ROUTE_DECISION)
    next_work = load(NEXT_WORK)
    cert = load(CERT)
    note = NOTE.read_text(encoding="utf-8")

    for name, item in [
        ("candidate", candidate),
        ("row_search", row_search),
        ("boundary_import", boundary_import),
        ("route_decision", route_decision),
    ]:
        clean(item, name)

    require(candidate["status"] == STATUS, "candidate status")
    require(candidate["theorem"]["proved"] is True, "candidate theorem")
    require(candidate["actual_H_sector_fourth_variation_row_found"] is False, "H row overfound")
    require(candidate["boundary_route_identified"] is True, "boundary route")
    require(candidate["standard_Dterm_boundary_formula_factor"] == "1/8", "boundary factor")
    require(candidate["old_factor_overhigh_by_two_under_standard_convention"] is True, "factor of two")
    require(candidate["selected_beta_or_tan_beta_source_found"] is False, "beta overselected")
    require(candidate["DTerm_boundary_numeric_value_derived"] is False, "D-term numeric overderived")
    require(candidate["Higgs_quartic_numeric_value_derived"] is False, "lambda overderived")
    require(candidate["strict_no_knob_Higgs_closure"] is False, "strict no-knob overclosed")
    require(candidate["new_Higgs_specific_parameters"] == 0, "Higgs params")

    target_row = row_search["target_row"]
    require(target_row["coordinate_index"] == 12, "row coordinate")
    require(target_row["quartic_row_address"] == [12, 12, 12, 12], "row address")
    require(target_row["row_owner_source_local_tier"] is True, "row owner")
    negative = row_search["negative_result"]
    require(negative["actual_H_sector_fourth_variation_row_found"] is False, "negative actual row")
    require(negative["exact_multilinear_formula_found"] is False, "negative formula")
    require(negative["row_exactness_certificate_found"] is False, "negative exactness")
    require(negative["lambda_H_coefficient_convention_from_source_row_found"] is False, "negative lambda convention")
    require(negative["no_knob_Higgs_value_found"] is False, "negative no-knob")
    non_promotions = row_search["non_promotions_reconfirmed"]
    require(non_promotions["H3_quadratic_K2_to_K4"] is False, "K2 to K4 promotion")
    require(non_promotions["H5B_row_address_to_row_value"] is False, "address promotion")
    require(non_promotions["H6_SI1c_source_rows_to_H_sector_fourth_row"] is False, "SI1c promotion")
    require(non_promotions["SM_parity_measured_lambda_to_source"] is False, "SM replay promotion")

    finding = boundary_import["corpus_finding"]
    require(finding["old_execution_formula_factor"] == "1/4", "old factor")
    require(finding["standard_SM_normalized_MSSM_tree_formula_factor"] == "1/8", "standard factor")
    require(finding["old_factor_overhigh_by_two_under_standard_convention"] is True, "standard factor check")
    require(finding["representative_tan_beta_in_old_text"] == 10, "tan beta example")
    require(finding["representative_tan_beta_selected_by_MTT"] is False, "tan beta selected")
    diagnostic = boundary_import["diagnostic_replay_not_source"]
    require(diagnostic["diagnostic_values_used_as_selector"] is False, "diagnostic selector")
    require(diagnostic["cos2beta_sq_exact_rational"] == "9801/10201", "cos2beta rational")
    require(math.isclose(diagnostic["cos2beta_sq_float"], 9801 / 10201), "cos2beta float")
    require(math.isclose(diagnostic["corrected_lambda_over_8_same_gauge_diagnostic"], diagnostic["legacy_lambda_over_4_diagnostic"] / 2), "factor half")
    requirements = boundary_import["route_requirements_for_source_use"]
    for key in [
        "selected_gauge_couplings_or_selected_EW_boundary_packet",
        "selected_beta_or_two_Higgs_projection_angle",
        "matching_scale_and_threshold_policy",
        "RG_transport_to_observable_scale",
        "no_use_of_measured_Higgs_mass_or_lambda_as_selector",
    ]:
        require(requirements[key] is True, f"boundary requirement {key}")
    does_not = boundary_import["what_this_route_does_not_close"]
    require(does_not["selected_beta_or_tan_beta"] is True, "beta open")
    require(does_not["physical_gauge_coupling_normalization"] is True, "gauge open")
    require(does_not["threshold_RG_precision"] is True, "RG open")
    require(does_not["strict_no_knob_Higgs_quartic"] is True, "no-knob open")

    route_a = route_decision["route_A_finite_H_row"]
    route_b = route_decision["route_B_boundary_matching"]
    require(route_a["current_status"] == "OPEN", "route A status")
    require("K_H^(4)[12,12,12,12]" in route_a["next_missing_object"], "route A object")
    require(route_b["current_status"] == "FORMULA_IDENTIFIED_SOURCE_INPUTS_OPEN", "route B status")
    require(route_b["formula"] == "lambda = (g^2 + g'^2) * cos^2(2 beta) / 8", "route B formula")
    require("selected beta" in route_b["next_missing_object"], "route B beta")
    superset = route_decision["superset_strategy"]
    require(superset["paths_combined_as_free_parameters"] is False, "superset free params")
    require("declared as an explicit universal or Higgs-sector primitive" in superset["allowed_future_parameter_note"], "parameter note")
    require("H6D-SELECTED-DTERM-BOUNDARY-OR-BETA-SOURCE" in next_work["primary"]["label"], "next H6D")

    require(cert["status"] == STATUS, "cert status")
    require(cert["actual_H_sector_fourth_variation_row_found"] is False, "cert row")
    require(cert["boundary_route_identified"] is True, "cert boundary")
    require(cert["standard_Dterm_boundary_formula_factor"] == "1/8", "cert factor")
    require(cert["selected_beta_or_tan_beta_source_found"] is False, "cert beta")
    require(cert["Higgs_quartic_numeric_value_derived"] is False, "cert numeric")
    require(cert["strict_no_knob_Higgs_closure"] is False, "cert no-knob")
    require("H6C-HSECTOR-ROW-OR-BOUNDARY" in note and "H6D-SELECTED-DTERM" in note, "note")

    print("CONST-HIGGS-01 H6C H-sector row/boundary-route discriminator audit: PASS")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
