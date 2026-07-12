"""Audit bottom/charm/tau maps or R_theta threshold derivation artifact."""

from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SLUG = "selected_bottomcharmtaumaps_or_rthetathresholdderivation"
DATA = ROOT / "candidate_data" / f"{SLUG}.candidate.json"
PACKET_DIR = ROOT / "candidate_data" / SLUG
INVENTORY = PACKET_DIR / "bottom_charm_tau_native_residual_inventory.packet.json"
FILL_ATTEMPT = PACKET_DIR / "bottom_charm_tau_map_row_fill_attempt.packet.json"
RTHETA_RECHECK = PACKET_DIR / "rtheta_bottom_charm_tau_projection_recheck.packet.json"
IMPORT_CONTRACT = PACKET_DIR / "bottom_charm_tau_external_map_import_contract.packet.json"
CUTSET = PACKET_DIR / "next_cutset_after_bottom_charm_tau_attempt.packet.json"
CERT = ROOT / "certificates" / f"{SLUG}_certificate.json"
NOTE = ROOT / "proof_corpus" / "MTT_Selected_BottomCharmTauMaps_or_RThetaThresholdDerivation_v1.md"
BUILDER = ROOT / "scripts" / f"build_{SLUG}.py"

STATUS = (
    "MTT_SELECTED_BOTTOMCHARMTAUMAPS_OR_RTHETATHRESHOLDDERIVATION_"
    "BUILT_NATIVE_RESIDUAL_INVENTORY_MAPS_OPEN"
)
NEXT = "MTT_Selected_BottomCharmTauFormulaImport_or_RThetaMassSchemeDerivation_v1"


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
    fill = load(FILL_ATTEMPT)
    rtheta = load(RTHETA_RECHECK)
    contract = load(IMPORT_CONTRACT)
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
        inventory["status"] == "BOTTOM_CHARM_TAU_NATIVE_AND_RESIDUAL_ROWS_INVENTORIED",
        "inventory status mismatch",
    )
    require(inventory["inventory_closed"] is True, "inventory not closed")
    require(len(inventory["residual_rows"]) == 3, "wrong residual row count")
    residual_ids = {row["id"] for row in inventory["residual_rows"]}
    require(
        residual_ids
        == {
            "Y_d_b_native_to_firstpass_MZ",
            "Y_u_c_native_to_firstpass_MZ",
            "Y_e_tau_native_to_firstpass_MZ",
        },
        "wrong residual rows",
    )
    for row in inventory["residual_rows"]:
        require(row["finite"] is True, f"nonfinite residual row: {row['id']}")
        require(row["accepted_as_map_row"] is False, f"residual overaccepted: {row['id']}")
    require(inventory["accepted_as_external_map_rows"] is False, "inventory overaccepted external rows")
    require(inventory["accepted_as_Rtheta_source_rows"] is False, "inventory overaccepted Rtheta rows")
    require(inventory["closure_claimed"] is True, "inventory should close locally")

    require(
        fill["status"] == "BOTTOM_CHARM_TAU_MAP_FILL_ATTEMPTED_NO_MAP_ROWS_ACCEPTED",
        "fill status mismatch",
    )
    require(fill["accepted_bottom_charm_tau_map_rows"] == [], "map rows overaccepted")
    require(fill["accepted_bottom_charm_tau_map_row_count"] == 0, "map row count overclaimed")
    require(fill["top_higgs_external_formula_map_row_count"] == 2, "top/Higgs accepted row count changed")
    require(fill["accepted_threshold_mass_scheme_source_rows_present"] is False, "source rows unexpectedly present")
    require(fill["residual_rows_are_source_rows"] is False, "residual rows treated as source")
    for row in fill["required_maps"]:
        require(row["accepted_now"] is False, f"required map overaccepted: {row['id']}")
        require(row["blocking_reason"], f"missing blocking reason: {row['id']}")
    require(fill["closure_claimed"] is False, "fill overclosed")

    require(
        rtheta["status"] == "RTHETA_BOTTOM_CHARM_TAU_SKELETON_PRESENT_SELECTED_SOLVE_OPEN",
        "Rtheta status mismatch",
    )
    require(rtheta["Pi_Rtheta_closed"] is False, "Pi_Rtheta overclosed in old packet")
    require(rtheta["minimal_internal_missing_object"] == "SelectedRouteCStromingerGalerkinResidualSolve", "wrong missing object")
    require(rtheta["precoefficient_skeletons_present"] is True, "Rtheta skeletons missing")
    require(rtheta["selected_Rtheta_mass_scheme_derivation_closed"] is False, "Rtheta derivation overclosed")
    require(rtheta["accepted_external_maps_may_validate_Rtheta"] is True, "validation relation missing")
    require(rtheta["accepted_external_maps_select_Rtheta"] is False, "external maps select Rtheta")
    require(rtheta["closure_claimed"] is False, "Rtheta recheck overclosed")

    require(
        contract["status"] == "BOTTOM_CHARM_TAU_EXTERNAL_IMPORT_CONTRACT_BUILT_ROWS_OPEN",
        "contract status mismatch",
    )
    require(len(contract["required_for_acceptance"]) == 7, "contract requirements changed")
    require(contract["current_support"]["native_values_present"] is True, "native values support missing")
    require(contract["current_support"]["finite_residual_rows_present"] is True, "residual support missing")
    require(contract["current_support"]["rtheta_precoefficient_skeletons_present"] is True, "Rtheta skeleton support missing")
    require(contract["current_support"]["accepted_external_formula_rows_present_for_top_higgs"] == 2, "top/Higgs support count changed")
    require(contract["accepted_external_bottom_charm_tau_table_now"] is False, "external table overaccepted")
    require(contract["closure_claimed"] is True, "contract should close locally")

    require(
        cutset["status"] == "NEXT_ATTACK_FORMULA_IMPORT_OR_RTHETA_MASS_SCHEME_DERIVATION",
        "cutset status mismatch",
    )
    for key in [
        "bottom_charm_tau_native_residual_inventory",
        "bottom_charm_tau_map_fill_attempt",
        "rtheta_bottom_charm_tau_projection_recheck",
        "bottom_charm_tau_external_import_contract",
    ]:
        require(cutset["closed_now"][key] is True, f"cutset closed flag missing: {key}")
    for key in [
        "accepted_bottom_charm_tau_map_rows",
        "accepted_external_bottom_charm_tau_table",
        "selected_Rtheta_mass_scheme_derivation",
        "W_Z_H_electroweak_matching_rows",
        "full_covariance_profile_likelihood",
        "true_SM_equivalence",
        "full_no_knob",
    ]:
        require(cutset["still_open"][key] is True, f"cutset open flag missing: {key}")
    require(cutset["recommended_next"]["artifact"] == NEXT, "cutset next mismatch")
    require(cutset["closure_claimed"] is False, "cutset overclosed")

    closure = data["closure_decision"]
    require(closure["bottom_charm_tau_native_residual_inventory_closed"] is True, "candidate inventory not closed")
    require(closure["bottom_charm_tau_external_import_contract_closed"] is True, "candidate contract not closed")
    require(closure["accepted_bottom_charm_tau_map_row_count"] == 0, "candidate map rows overaccepted")
    for key in [
        "accepted_bottom_charm_tau_map_rows_closed",
        "accepted_external_bottom_charm_tau_table_closed",
        "selected_Rtheta_mass_scheme_derivation_closed",
        "W_Z_H_electroweak_matching_rows_closed",
        "full_covariance_profile_likelihood_closed",
        "true_SM_equivalence_closed",
        "full_no_knob_closed",
    ]:
        require(closure[key] is False, f"candidate overclosed: {key}")
    require("accepted b/c/tau map rows              : 0" in note, "note missing zero map row")
    require("Rtheta precoefficient skeletons present: true" in note, "note missing Rtheta skeleton line")

    print(f"PASS {DATA.name}: {STATUS}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
