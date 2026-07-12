"""Audit W/Z/H electroweak rows or selected Rtheta mass-scheme derivation artifact."""

from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SLUG = "selected_wzhelectroweakrows_or_selectedrthetamassschemederivation"
DATA = ROOT / "candidate_data" / f"{SLUG}.candidate.json"
PACKET_DIR = ROOT / "candidate_data" / SLUG
INVENTORY = PACKET_DIR / "wzh_electroweak_row_inventory.packet.json"
ACCEPTANCE = PACKET_DIR / "wzh_external_benchmark_row_acceptance.packet.json"
RTHETA_GAP = PACKET_DIR / "selected_rtheta_mass_scheme_gap_after_wzh_rows.packet.json"
HIGGS_EW = PACKET_DIR / "higgs_decay_electroweak_boundary_reconciliation.packet.json"
CUTSET = PACKET_DIR / "next_cutset_after_wzh_external_rows.packet.json"
CERT = ROOT / "certificates" / f"{SLUG}_certificate.json"
NOTE = ROOT / "proof_corpus" / "MTT_Selected_WZHElectroweakRows_or_SelectedRThetaMassSchemeDerivation_v1.md"
BUILDER = ROOT / "scripts" / f"build_{SLUG}.py"

STATUS = (
    "MTT_SELECTED_WZHELECTROWEAKROWS_OR_SELECTEDRTHETAMASSSCHEMEDERIVATION_"
    "BUILT_EXTERNAL_BENCHMARK_ROWS_CLOSED_COVARIANCE_RTHETA_OPEN"
)
NEXT = "MTT_Selected_FullCovarianceProfile_or_SelectedRThetaSourceRows_v1"


def load(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def require(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)


def main() -> int:
    subprocess.run([sys.executable, str(BUILDER)], cwd=ROOT, check=True)

    data = load(DATA)
    cert = load(CERT)
    inventory = load(INVENTORY)
    acceptance = load(ACCEPTANCE)
    gap = load(RTHETA_GAP)
    higgs_ew = load(HIGGS_EW)
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
        inventory["status"] == "WZH_ELECTROWEAK_COORDINATE_ROWS_INVENTORIED",
        "inventory status mismatch",
    )
    rows = inventory["accepted_wzh_coordinate_rows"]
    require(len(rows) == 5, "wrong WZH row count")
    row_ids = {row["id"] for row in rows}
    require(
        row_ids == {"v_from_G_F_tree_reference", "g_Y_Mt", "g_1_GUT_Mt", "g_2_Mt", "lambda_Mt"},
        "wrong WZH row ids",
    )
    require(inventory["row_inventory_summary"]["g_1_GUT_is_normalization_alias_of_g_Y"] is True, "g1 alias guard missing")
    require(inventory["row_inventory_summary"]["v_row_is_tree_reference_anchor_not_MSbar_threshold_match"] is True, "v guard missing")
    require(inventory["row_inventory_summary"]["all_wzh_coordinate_rows_available"] is True, "WZH rows unavailable")
    for row in rows:
        require(row["accepted_as_external_WZH_coordinate_row"] is True, f"external WZH row not accepted: {row['id']}")
        require(row["accepted_as_selected_Rtheta_source_row"] is False, f"Rtheta row overaccepted: {row['id']}")
        require(row["used_as_source_selector"] is False, f"selector guard failed: {row['id']}")
    require(inventory["closure_claimed"] is True, "inventory should close locally")

    require(
        acceptance["status"] == "WZH_EXTERNAL_BENCHMARK_COORDINATE_ROWS_ACCEPTED_SOURCE_RTHETA_OPEN",
        "acceptance status mismatch",
    )
    require(acceptance["accepted_external_wzh_coordinate_row_count"] == 5, "accepted WZH row count mismatch")
    require(acceptance["accepted_selected_Rtheta_source_row_count"] == 0, "Rtheta rows overaccepted")
    require(acceptance["accepted_full_covariance_profile_row_count"] == 0, "profile rows overaccepted")
    require(acceptance["row_coordinate_closure_claimed"] is True, "coordinate layer not closed")
    require(acceptance["full_precision_threshold_match_claimed"] is False, "precision threshold overclaimed")
    require(acceptance["full_covariance_profile_likelihood_claimed"] is False, "profile likelihood overclaimed")
    require(acceptance["gauge_bridge_policy_validation"]["passes_coarse_gauge_bridge"] is True, "gauge bridge did not pass")
    require(
        acceptance["gauge_bridge_policy_validation"]["accepted_as_precision_threshold_match"] is False,
        "gauge bridge precision overclaimed",
    )
    require(acceptance["covariance_boundary"]["lambda_Mt_has_diagonal_sidecar"] is True, "lambda sidecar missing")
    require(
        acceptance["covariance_boundary"]["gauge_rows_have_full_uncertainty_or_correlation_sidecars"] is False,
        "gauge covariance overclaimed",
    )
    require(acceptance["covariance_boundary"]["full_covariance_required_before_profile_likelihood"] is True, "covariance guard missing")
    require(acceptance["closure_claimed"] is True, "acceptance should close locally")

    require(
        gap["status"] == "WZH_EXTERNAL_ROWS_ACCEPTED_SELECTED_RTHETA_MASS_SCHEME_STILL_OPEN",
        "Rtheta gap status mismatch",
    )
    require(gap["selected_Rtheta_mass_scheme_derivation_closed"] is False, "Rtheta mass scheme overclosed")
    require(gap["same_branch_Rtheta_threshold_derivation_closed"] is False, "same-branch threshold overclosed")
    require(gap["accepted_external_rows_may_validate_Rtheta"] is True, "validation relation missing")
    require(gap["accepted_external_rows_select_Rtheta"] is False, "external rows select Rtheta")
    require(len(gap["minimal_internal_missing_objects"]) == 4, "Rtheta obligation count changed")
    require(gap["closure_claimed"] is False, "Rtheta gap overclosed")

    require(
        higgs_ew["status"] == "HIGGS_DECAY_EW_ROWS_REMAIN_BENCHMARK_REPLAY_NOT_WZH_MATCHING_SOURCE",
        "Higgs EW boundary status mismatch",
    )
    require(higgs_ew["higgs_ten_channel_replay_completed"] is True, "Higgs ten-channel replay not preserved")
    require(higgs_ew["higgs_uniform_formula_rows_fully_closed"] is False, "Higgs EW formulas overclosed")
    require(len(higgs_ew["remaining_higgs_ew_benchmark_rows"]) == 3, "wrong remaining Higgs EW count")
    for row in higgs_ew["remaining_higgs_ew_benchmark_rows"]:
        require(row["accepted_as_downstream_benchmark_replay_row"] is True, f"Higgs replay row missing: {row['channel']}")
        require(row["accepted_as_executable_formula_kernel"] is False, f"Higgs formula kernel overclosed: {row['channel']}")
        require(row["accepted_as_precision_formula_row"] is False, f"Higgs precision row overclosed: {row['channel']}")
    require(higgs_ew["closure_claimed"] is False, "Higgs EW boundary overclosed")

    require(
        cutset["status"] == "NEXT_ATTACK_FULL_COVARIANCE_PROFILE_OR_SELECTED_RTHETA_SOURCE_ROWS",
        "cutset status mismatch",
    )
    for key in [
        "W_Z_H_external_benchmark_coordinate_rows",
        "v_from_G_F_reference_coordinate_row",
        "gY_g1_g2_Mt_external_benchmark_rows",
        "lambda_Mt_external_benchmark_row_integrated",
        "Higgs_decay_EW_boundary_reconciled",
    ]:
        require(cutset["closed_now"][key] is True, f"cutset closed flag missing: {key}")
    for key in [
        "selected_Rtheta_mass_scheme_derivation",
        "same_branch_Rtheta_threshold_derivation",
        "gauge_row_uncertainty_and_correlation_sidecars",
        "full_covariance_profile_likelihood",
        "EW_formula_kernels_for_WW_ZZ_Zgamma",
        "BCT_source_or_no_knob_profile_closure",
        "selected_CRunDec_charm_input_policy",
        "true_SM_equivalence",
        "full_no_knob",
    ]:
        require(cutset["still_open"][key] is True, f"cutset open flag missing: {key}")
    require(cutset["recommended_next"]["artifact"] == NEXT, "cutset next mismatch")
    require(cutset["closure_claimed"] is False, "cutset overclosed")

    closure = data["closure_decision"]
    require(closure["W_Z_H_electroweak_matching_rows_closed_at_external_coordinate_layer"] is True, "candidate WZH layer not closed")
    require(closure["accepted_external_wzh_coordinate_row_count"] == 5, "candidate WZH row count mismatch")
    require(closure["accepted_selected_Rtheta_source_row_count"] == 0, "candidate Rtheta count mismatch")
    for key in [
        "selected_Rtheta_mass_scheme_derivation_closed",
        "same_branch_Rtheta_threshold_derivation_closed",
        "full_precision_threshold_match_closed",
        "full_covariance_profile_likelihood_closed",
        "true_SM_equivalence_closed",
        "full_no_knob_closed",
    ]:
        require(closure[key] is False, f"candidate overclosed: {key}")
    require(cert["W_Z_H_external_coordinate_layer_closed"] is True, "certificate WZH closure missing")
    require(cert["selected_Rtheta_mass_scheme_derivation_closed"] is False, "certificate Rtheta overclosed")
    require("accepted W/Z/H coordinate rows : 5" in note, "note missing WZH count")
    require("selected R_theta rows closed    : false" in note, "note missing Rtheta guard")

    print(f"PASS {DATA.name}: {STATUS}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
