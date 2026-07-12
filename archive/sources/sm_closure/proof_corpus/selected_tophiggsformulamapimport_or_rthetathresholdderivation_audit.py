"""Audit top/Higgs formula map import or R_theta threshold derivation artifact."""

from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SLUG = "selected_tophiggsformulamapimport_or_rthetathresholdderivation"
DATA = ROOT / "candidate_data" / f"{SLUG}.candidate.json"
PACKET_DIR = ROOT / "candidate_data" / SLUG
FORMULA_IMPORT = PACKET_DIR / "top_higgs_formula_map_import_replay.packet.json"
ACCEPTANCE = PACKET_DIR / "top_higgs_external_formula_map_acceptance.packet.json"
RTHETA_GAP = PACKET_DIR / "rtheta_threshold_map_derivation_gap.packet.json"
CUTSET = PACKET_DIR / "next_cutset_after_top_higgs_formula_import.packet.json"
CERT = ROOT / "certificates" / f"{SLUG}_certificate.json"
NOTE = ROOT / "proof_corpus" / "MTT_Selected_TopHiggsFormulaMapImport_or_RThetaThresholdDerivation_v1.md"
BUILDER = ROOT / "scripts" / f"build_{SLUG}.py"

STATUS = (
    "MTT_SELECTED_TOPHIGGSFORMULAMAPIMPORT_OR_RTHETATHRESHOLDDERIVATION_"
    "BUILT_EXTERNAL_FORMULA_MAP_ROWS_CLOSED_RTHETA_OPEN"
)
NEXT = "MTT_Selected_BottomCharmTauMaps_or_RThetaThresholdDerivation_v1"


def load(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def require(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)


def main() -> int:
    subprocess.run([sys.executable, str(BUILDER)], cwd=ROOT, check=True)

    data = load(DATA)
    cert = load(CERT)
    formula = load(FORMULA_IMPORT)
    acceptance = load(ACCEPTANCE)
    gap = load(RTHETA_GAP)
    cutset = load(CUTSET)
    note = NOTE.read_text(encoding="utf-8")

    require(data["status"] == STATUS, "candidate status mismatch")
    require(cert["status"] == STATUS, "certificate status mismatch")
    require(data["next_required_artifact"] == NEXT, "candidate next mismatch")
    require(cert["next_required_artifact"] == NEXT, "certificate next mismatch")
    for key in [
        "closure_claimed",
        "unpatched_theorem_closure_claimed",
        "observed_data_used_as_selector",
        "target_fitting_used",
    ]:
        require(data[key] is False, f"candidate guardrail overclaimed: {key}")
    require(data["theorem"]["proved"] is True, "candidate theorem not proved")
    require(cert["theorem_proved"] is True, "certificate theorem missing")

    require(
        formula["status"] == "TOP_HIGGS_BUTTAZZO_FORMULA_MAPS_IMPORTED_FOR_EXTERNAL_VALIDATION",
        "formula import status mismatch",
    )
    require(formula["source"]["arxiv"] == "1307.3536", "formula source mismatch")
    require(len(formula["formula_rows"]) == 2, "wrong formula row count")
    row_ids = {row["id"] for row in formula["formula_rows"]}
    require(row_ids == {"lambda_Mt", "y_t_Mt"}, "wrong formula rows")
    require(formula["formulas_replay_encoded_literature_values"] is True, "formula replay not exact")
    require(formula["diagonal_sensitivity_sidecars_present"] is True, "diagonal sidecars missing")
    require(formula["accepted_as_external_formula_map_import"] is True, "formula import not accepted")
    require(formula["accepted_as_same_branch_Rtheta_derivation"] is False, "Rtheta derivation overclosed")
    require(formula["accepted_as_full_profile_likelihood"] is False, "full profile overclosed")
    for row in formula["central_replay_rows"]:
        require(row["absolute_delta"] < 1e-14, f"central replay delta too large: {row['id']}")
    require(formula["closure_claimed"] is True, "formula import should close locally")

    require(
        acceptance["status"] == "TWO_EXTERNAL_TOP_HIGGS_FORMULA_MAP_ROWS_ACCEPTED_RTHETA_OPEN",
        "acceptance status mismatch",
    )
    require(acceptance["accepted_external_formula_map_row_count"] == 2, "wrong accepted formula count")
    require(acceptance["accepted_Rtheta_source_row_count"] == 0, "Rtheta row overaccepted")
    require(acceptance["accepted_full_profile_row_count"] == 0, "full profile row overaccepted")
    require(acceptance["old_accepted_top_higgs_threshold_map_row_count"] == 0, "old rows should be zero")
    for row in acceptance["accepted_rows"]:
        require(row["accepted_as_external_top_higgs_formula_map_row"] is True, f"external row not accepted: {row['id']}")
        require(row["accepted_as_Rtheta_source_row"] is False, f"Rtheta row overaccepted: {row['id']}")
        require(row["accepted_as_full_profile_row"] is False, f"profile row overaccepted: {row['id']}")
    require(acceptance["residuals_are_requirements_not_fitted_corrections"] is True, "residual guard missing")
    require(acceptance["closure_claimed"] is True, "acceptance should close locally")

    require(
        gap["status"] == "EXTERNAL_FORMULA_MAP_ROWS_ACCEPTED_SELECTED_RTHETA_DERIVATION_OPEN",
        "Rtheta gap status mismatch",
    )
    require(gap["same_branch_convention_source_theorem_closed"] is False, "same-branch convention overclosed")
    require(gap["formula_values_are_literature_replay_not_MTT_source"] is True, "formula source guard missing")
    require(gap["current_input_variant_is_not_selected_prediction"] is True, "current input guard missing")
    require(len(gap["what_Rtheta_must_still_derive"]) == 4, "Rtheta obligation count changed")
    require(gap["accepted_external_formula_rows_may_validate_Rtheta"] is True, "validation relation missing")
    require(gap["accepted_external_formula_rows_select_Rtheta"] is False, "formula rows select Rtheta")
    require(gap["closure_claimed"] is False, "Rtheta gap overclosed")

    require(
        cutset["status"] == "NEXT_ATTACK_BOTTOM_CHARM_TAU_MAPS_OR_RTHETA_THRESHOLD_DERIVATION",
        "cutset status mismatch",
    )
    for key in [
        "top_higgs_external_formula_map_import",
        "lambda_Mt_external_formula_map_row",
        "y_t_Mt_external_formula_map_row",
        "diagonal_sensitivity_sidecars",
        "Rtheta_nonselector_gap_recorded",
    ]:
        require(cutset["closed_now"][key] is True, f"cutset closed flag missing: {key}")
    for key in [
        "same_branch_Rtheta_threshold_derivation",
        "full_covariance_profile_likelihood",
        "bottom_charm_native_MSbar_scale_transport_maps",
        "tau_pole_rest_to_running_lepton_map",
        "W_Z_H_electroweak_matching_rows",
        "true_SM_equivalence",
        "full_no_knob",
    ]:
        require(cutset["still_open"][key] is True, f"cutset open flag missing: {key}")
    require(cutset["recommended_next"]["artifact"] == NEXT, "cutset next mismatch")
    require(cutset["closure_claimed"] is False, "cutset overclosed")

    closure = data["closure_decision"]
    for key in [
        "top_higgs_external_formula_map_import_closed",
        "lambda_Mt_external_formula_map_row_closed",
        "y_t_Mt_external_formula_map_row_closed",
    ]:
        require(closure[key] is True, f"candidate closed flag missing: {key}")
    require(closure["accepted_external_formula_map_row_count"] == 2, "candidate formula count mismatch")
    for key in [
        "same_branch_Rtheta_threshold_derivation_closed",
        "full_covariance_profile_likelihood_closed",
        "bottom_charm_tau_mass_scheme_maps_closed",
        "W_Z_H_electroweak_matching_rows_closed",
        "true_SM_equivalence_closed",
        "full_no_knob_closed",
    ]:
        require(closure[key] is False, f"candidate overclosed: {key}")
    require(cert["accepted_external_formula_map_row_count"] == 2, "certificate count mismatch")
    require("accepted external formula-map rows : 2" in note, "note missing formula count")
    require("same-branch R_theta derivation     : false" in note, "note missing Rtheta guard")

    print(f"PASS {DATA.name}: {STATUS}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
