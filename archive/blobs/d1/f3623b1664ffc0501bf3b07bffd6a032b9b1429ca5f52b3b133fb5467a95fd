"""Audit B45/G4 primitive-portfolio comparison packet."""

from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SLUG = "selected_b45portfolioprimitivecomparison_or_constgr01sharedprimitivesourcetest"
BASE = ROOT / "candidate_data" / SLUG
CANDIDATE = ROOT / "candidate_data" / f"{SLUG}.candidate.json"
CERT = ROOT / "certificates" / f"{SLUG}_certificate.json"
NOTE = ROOT / "proof_corpus" / "MTT_Selected_B45PortfolioPrimitiveComparison_or_CONSTGR01SharedPrimitiveSourceTest_v1.md"
BUILD = ROOT / "scripts" / f"build_{SLUG}.py"

G4_IMPORT = BASE / "frontier_import_g4_latest.packet.json"
SEPARATION = BASE / "primitive_class_separation.packet.json"
PORTFOLIO = BASE / "portfolio_budget_after_separation.packet.json"
HIGGS_HANDOFF = BASE / "higgs_handoff_status.packet.json"
CUTSET = BASE / "next_cutset_after_b45_g4_comparison.packet.json"

STATUS = (
    "MTT_SELECTED_B45PORTFOLIOPRIMITIVECOMPARISON_OR_CONSTGR01SHAREDPRIMITIVESOURCETEST_"
    "G4_IMPORTED_HRG_SEPARATED_METROLOGY_OPEN"
)
NEXT = "MTT_Selected_HiggsSharedMetrologyPrimitiveHandoff_or_HRGSourceTheoremReentry_v1"
HRG = 391.39140285811936
LOG_HRG = 5.969708089616292
SIN2 = 0.2315309482915084
TAU_INT = 0.40698621549433234
OMEGA_OVER_SQRT_ALPHA = 1.5675093859261626
GR_GEFF_L0_COEFF = 0.29759362932431804


def load(path: Path):
    return json.loads(path.read_text(encoding="utf-8"))


def require(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)


def main() -> int:
    proc = subprocess.run([sys.executable, str(BUILD)], cwd=ROOT, text=True, capture_output=True)
    if proc.returncode:
        print(proc.stdout)
        print(proc.stderr)
        return proc.returncode

    candidate = load(CANDIDATE)
    cert = load(CERT)
    g4_import = load(G4_IMPORT)
    separation = load(SEPARATION)
    portfolio = load(PORTFOLIO)
    higgs_handoff = load(HIGGS_HANDOFF)
    cutset = load(CUTSET)
    note = NOTE.read_text(encoding="utf-8")

    require(candidate["status"] == STATUS, "candidate status")
    require(candidate["next_required_artifact"] == NEXT, "candidate next")
    require(candidate["closure_claimed"] is True, "candidate closure")
    require(candidate["true_SM_equivalence_claimed"] is False, "true SM overclaim")
    require(candidate["full_no_knob_closure_claimed"] is False, "no-knob overclaim")
    require(candidate["observed_data_used_as_selector"] is False, "observed selector")
    require(candidate["target_fitting_used"] is False, "target fitting")
    require(candidate["theorem"]["proved"] is True, "theorem proved")
    require(
        candidate["theorem"]["name"]
        == "B45PortfolioPrimitiveComparisonOrCONSTGR01SharedPrimitiveSourceTestTheorem",
        "theorem name",
    )

    decision = candidate["closure_decision"]
    for key in [
        "B45_latest_weak_mixing_frontier_imported",
        "CONST_GR_01_G4_latest_imported",
        "G4_relative_physical_scale_solution_closed",
        "G4_one_metrology_primitive_tier_defined",
        "HRG_and_metrology_primitives_typed_separate_now",
        "minimal_portfolio_requires_two_distinct_open_primitives_if_HRG_retained",
    ]:
        require(decision[key] is True, f"decision true {key}")
    for key in [
        "G4_strict_same_branch_Omega0_E0_L0_derived",
        "G4_selected_metrology_primitive_value",
        "G4_Newton_or_Planck_prediction",
        "HRG_equals_E0_L0_or_Omega0_now",
        "UP_RET_OVERLAP_HRG_universal_admitted",
        "silent_HRG_as_metrology_merge_allowed",
        "deeper_identity_theorem_excluded",
        "true_SM_equivalence_closed",
        "full_no_knob_closed",
    ]:
        require(decision[key] is False, f"decision false {key}")

    nums = candidate["key_numbers"]
    require(abs(nums["UP_RET_OVERLAP_HRG"] - HRG) < 1e-12, "HRG")
    require(abs(nums["log_UP_RET_OVERLAP_HRG"] - LOG_HRG) < 1e-12, "log HRG")
    require(abs(nums["B44_conditional_minimal_threshold_sin2"] - SIN2) < 1e-15, "sin2")
    require(nums["B45_selected_numeric_primitive_values_now"] == 0, "B45 selected values")
    require(abs(nums["tau_int"] - TAU_INT) < 1e-15, "tau int")
    require(abs(nums["Omega0_over_sqrt_alpha_phys"] - OMEGA_OVER_SQRT_ALPHA) < 1e-15, "Omega/alpha")
    require(abs(nums["GR_G_eff_L0_coeff"] - GR_GEFF_L0_COEFF) < 1e-15, "GR coeff")
    require(nums["selected_numeric_metrology_values_now"] == 0, "metrology values")
    require(nums["selected_HRG_source_value_now"] == 0, "HRG source values")
    require(nums["strict_H_K_rows"] == 9, "strict H rows")
    require(nums["required_H_K_rows"] == 10, "required H rows")

    require(cert["status"] == STATUS, "cert status")
    require(cert["next_required_artifact"] == NEXT, "cert next")
    for key in [
        "B45_latest_weak_mixing_frontier_imported",
        "CONST_GR_01_G4_latest_imported",
        "G4_relative_physical_scale_solution_closed",
        "G4_one_metrology_primitive_tier_defined",
        "HRG_and_metrology_primitives_typed_separate_now",
        "minimal_portfolio_requires_two_distinct_open_primitives_if_HRG_retained",
    ]:
        require(cert[key] is True, f"cert true {key}")
    for key in [
        "G4_strict_same_branch_Omega0_E0_L0_derived",
        "G4_selected_metrology_primitive_value",
        "G4_Newton_or_Planck_prediction",
        "HRG_equals_E0_L0_or_Omega0_now",
        "UP_RET_OVERLAP_HRG_universal_admitted",
        "silent_HRG_as_metrology_merge_allowed",
        "deeper_identity_theorem_excluded",
        "true_SM_equivalence_claimed",
        "full_no_knob_closure_claimed",
        "observed_data_used_as_selector",
        "target_fitting_used",
    ]:
        require(cert[key] is False, f"cert false {key}")

    require(g4_import["status"] == "G4_LATEST_CONST_GR_01_FRONTIER_IMPORTED", "G4 import status")
    require(g4_import["closure_claimed"] is True, "G4 import closure")
    require(g4_import["observed_data_used_as_selector"] is False, "G4 import observed")
    require(g4_import["target_fitting_used"] is False, "G4 import target")
    require(g4_import["b45_import"]["weak_mixing_down_to_one_shared_primitive_tier"] is True, "B45 one primitive")
    require(g4_import["b45_import"]["selected_next_constant"] == "CONST-GR-01 / ABSOLUTE-SCALE-GN", "B45 next")
    require(g4_import["b45_import"]["selected_numeric_primitive_values_now"] == 0, "B45 numeric")
    require(abs(g4_import["b45_import"]["conditional_profile_replay_sin2"] - SIN2) < 1e-15, "B45 sin2")
    require(g4_import["const_gr_01_chain"]["G4"] == "MTT_CONST_GR_01_G4_OMEGA0_OR_ONE_METROLOGY_PRIMITIVE_BUILT", "G4 status")
    g4_decision = g4_import["decision"]
    for key in [
        "B45_latest_weak_mixing_frontier_imported",
        "CONST_GR_01_G4_latest_imported",
        "G4_relative_physical_scale_solution_closed",
        "G4_one_metrology_primitive_tier_defined",
        "G4_recommends_Higgs_shared_metrology_next",
    ]:
        require(g4_decision[key] is True, f"G4 decision true {key}")
    for key in [
        "G4_strict_same_branch_Omega0_E0_L0_derived",
        "G4_selected_metrology_primitive_value",
        "G4_Newton_or_Planck_prediction",
    ]:
        require(g4_decision[key] is False, f"G4 decision false {key}")
    g4_result = g4_import["g4_result"]
    require(g4_result["boundary_status"] == "G4_METROLOGY_TIER_FROZEN_STRICT_SOURCE_OPEN", "G4 boundary")
    require(g4_result["closed_or_decided_now"]["one_universal_metrology_primitive_contract_defined"] is True, "G4 contract")
    require(g4_result["still_open"]["selected_physical_E0_or_L0_value"] is True, "G4 E0/L0 open")
    require(g4_result["parameter_budget"]["new_universal_metrology_primitives"] == 1, "G4 primitive count")
    require(g4_result["parameter_budget"]["strict_no_knob_primitives"] == 0, "G4 no knob count")
    require(abs(g4_result["shared_formulae"]["tau_int"] - TAU_INT) < 1e-15, "G4 tau")
    require(
        abs(g4_result["shared_formulae"]["Omega0_over_sqrt_alpha_phys"] - OMEGA_OVER_SQRT_ALPHA) < 1e-15,
        "G4 Omega",
    )
    require(g4_result["physical_predictions_now"]["Newton_or_Planck_numeric"] is False, "G4 Newton")

    require(separation["status"] == "PRIMITIVE_CLASS_SEPARATION_ESTABLISHED_FOR_CURRENT_LEDGER", "separation")
    require(separation["closure_claimed"] is True, "separation closure")
    abs_scale = separation["primitive_classes"]["UP_ABS_SCALE"]
    hrg = separation["primitive_classes"]["UP_RET_OVERLAP_HRG"]
    require(abs_scale["id"] == "UP-ABS-SCALE", "abs id")
    require(abs_scale["selected_value_now"] is False, "abs value")
    require(abs_scale["strict_no_knob_now"] is False, "abs no knob")
    require("Omega0" in abs_scale["symbols"], "abs symbols")
    require(hrg["id"] == "UP-RET-OVERLAP.HRG", "hrg id")
    require(abs(hrg["value_if_empirically_calibrated"] - HRG) < 1e-12, "hrg value")
    require(hrg["strict_source_selected_now"] is False, "hrg strict")
    require(hrg["universal_admitted_now"] is False, "hrg universal")
    require(hrg["empirical_layer_admitted_now"] is True, "hrg empirical")
    require(hrg["lambda_H_calibrated"] is True, "lambda calibrated")
    require(hrg["lambda_H_predicted"] is False, "lambda predicted")
    require(len(separation["separation_tests"]) == 4, "separation tests")
    for row in separation["separation_tests"]:
        require(row["accepted_identity_now"] is False, f"separation test {row['test']}")
    identity = separation["identity_route_status"]
    for key in [
        "typed_identity_theorem_found_now",
        "HRG_equals_E0_or_L0_or_Omega0_now",
        "HRG_promoted_by_B45_now",
        "HRG_promoted_by_G4_now",
        "deeper_identity_theorem_excluded",
    ]:
        require(identity[key] is False, f"identity false {key}")
    sep_decision = separation["decision"]
    require(sep_decision["HRG_and_metrology_primitives_typed_separate_now"] is True, "sep true")
    require(sep_decision["current_ledger_must_not_merge_HRG_with_UP_ABS_SCALE"] is True, "sep merge")

    require(
        portfolio["status"] == "PORTFOLIO_AFTER_SEPARATION_TWO_OPEN_PRIMITIVE_CLASSES_IF_HRG_RETAINED",
        "portfolio",
    )
    current = portfolio["current_minimal_portfolio_if_HRG_retained"]
    require(current["candidate_primitive_class_count"] == 2, "portfolio count")
    require(current["strict_no_knob_primitive_count"] == 0, "portfolio no knob")
    require(current["selected_numeric_primitive_value_count"] == 0, "portfolio values")
    require(current["ordinary_fitted_sector_knobs"] == 0, "portfolio knobs")
    require(current["conditional_empirical_calibrations_now"] == 1, "portfolio empirical")
    guards = portfolio["policy_guardrails"]
    require(guards["credible_minimal_parameter_path_exists"] is True, "guard credible")
    require(guards["ordinary_H_only_knob_allowed"] is False, "guard H knob")
    require(guards["selected_existing_physical_unit_primitive_now"] is False, "guard abs")
    require(guards["selected_H_threshold_primitive_now"] is False, "guard H")
    require(guards["calibrating_H_lambda_makes_H_lambda_a_prediction"] is False, "guard prediction")
    port_decision = portfolio["decision"]
    require(port_decision["minimal_one_primitive_solves_everything_now"] is False, "port one")
    require(port_decision["minimal_two_class_portfolio_is_current_legal_if_HRG_retained"] is True, "port two")
    require(port_decision["HRG_requires_source_theorem_or_admission_before_prediction_credit"] is True, "port source")
    require(port_decision["true_SM_equivalence_closed"] is False, "port SM")
    require(port_decision["full_no_knob_closed"] is False, "port no knob")

    require(
        higgs_handoff["status"] == "HIGGS_HANDOFF_REFINED_TO_SHARED_METROLOGY_OR_HRG_SOURCE_REENTRY",
        "higgs handoff",
    )
    hdec = higgs_handoff["local_h_threshold_decision"]
    require(hdec["strict_K_rows"] == 9, "h strict rows")
    require(hdec["required_K_rows"] == 10, "h required rows")
    require(hdec["controlled_empirical_conditional_K_rows"] == 10, "h empirical rows")
    require(hdec["UP_RET_OVERLAP_HRG_admitted_empirical_layer"] is True, "h empirical")
    require(hdec["UP_RET_OVERLAP_HRG_selected_strict_source"] is False, "h source")
    require(hdec["crossuse_prediction_audit_passed"] is False, "h crossuse")
    routes = {row["route"]: row for row in higgs_handoff["refined_next_routes"]}
    require(routes["shared_metrology_handoff"]["allowed_now"] is True, "route metrology")
    require(routes["HRG_source_theorem_reentry"]["allowed_now"] is True, "route HRG")
    require(routes["silent_identity_with_metrology"]["allowed_now"] is False, "route silent")

    require(cutset["status"] == "NEXT_FRONTIER_HIGGS_SHARED_METROLOGY_OR_HRG_SOURCE_REENTRY", "cutset")
    require(cutset["next_required_artifact"] == NEXT, "cutset next")
    for phrase in [
        "B45 latest weak-mixing one-shared-primitive handoff imported",
        "CONST-GR-01 G1-G4 chain imported as the latest absolute-scale shared primitive test",
        "UP-ABS-SCALE and UP-RET-OVERLAP.HRG separated for the current typed ledger",
        "silent HRG-as-metrology merge rejected until a selected typed identity theorem exists",
    ]:
        require(phrase in cutset["closed_here"], f"closed missing {phrase}")
    for phrase in [
        "selected physical E0/L0/Omega0 value or strict same-branch physical unit theorem",
        "strict source theorem for UP-RET-OVERLAP.HRG",
        "universal admission and non-Higgs cross-use prediction for UP-RET-OVERLAP.HRG",
        "true SM/no-knob equivalence",
    ]:
        require(phrase in cutset["still_open"], f"open missing {phrase}")

    for phrase in [
        "G4 closes the relative physical-scale solution",
        "`UP-ABS-SCALE` and `UP-RET-OVERLAP.HRG` are not the same object",
        "No selected typed identity theorem currently maps the HRG value",
        "The silent one-primitive-does-everything route is rejected",
        NEXT,
    ]:
        require(phrase in note, f"note missing {phrase}")

    print(
        "AUDIT_PASS: B45/G4 imported; UP-ABS-SCALE and UP-RET-OVERLAP.HRG "
        "are separated in the current ledger; portfolio remains value-open."
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
