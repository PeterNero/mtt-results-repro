"""Audit tau EW/QED running policy or R_theta mass-scheme rows artifact."""

from __future__ import annotations

import json
import math
import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SLUG = "selected_tauewrunningpolicy_or_rthetamassschemerows"
DATA = ROOT / "candidate_data" / f"{SLUG}.candidate.json"
PACKET_DIR = ROOT / "candidate_data" / SLUG
TABLE_IMPORT = PACKET_DIR / "huang_zhou_tau_mz_table_import.packet.json"
CONVENTION = PACKET_DIR / "tau_mz_convention_alignment_decision.packet.json"
TAU_ROW = PACKET_DIR / "tau_external_mass_scheme_row.packet.json"
CUTSET = PACKET_DIR / "next_cutset_after_tau_policy.packet.json"
CERT = ROOT / "certificates" / f"{SLUG}_certificate.json"
NOTE = ROOT / "proof_corpus" / "MTT_Selected_TauEWRunningPolicy_or_RThetaMassSchemeRows_v1.md"
BUILDER = ROOT / "scripts" / f"build_{SLUG}.py"

STATUS = (
    "MTT_SELECTED_TAUEWRUNNINGPOLICY_OR_RTHETAMASSSCHEMEROWS_"
    "BUILT_TAU_EFT_TABLE_ROW_FULLSM_RTHETA_OPEN"
)
NEXT = "MTT_Selected_AllBCTExternalRows_or_FullSMConventionReconciliation_v1"


def load(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def require(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)


def close(actual: float, expected: float, tol: float = 1e-15) -> bool:
    return math.isclose(actual, expected, rel_tol=0.0, abs_tol=tol)


def main() -> int:
    subprocess.run([sys.executable, str(BUILDER)], cwd=ROOT, check=True)

    data = load(DATA)
    cert = load(CERT)
    table = load(TABLE_IMPORT)
    convention = load(CONVENTION)
    tau = load(TAU_ROW)
    cutset = load(CUTSET)
    note = NOTE.read_text(encoding="utf-8")

    require(data["status"] == STATUS, "candidate status mismatch")
    require(cert["status"] == STATUS, "certificate status mismatch")
    require(data["next_required_artifact"] == NEXT, "candidate next mismatch")
    require(cert["next_required_artifact"] == NEXT, "certificate next mismatch")
    require(data["theorem"]["proved"] is True, "candidate theorem missing")
    require(cert["theorem_proved"] is True, "certificate theorem missing")
    for key in [
        "closure_claimed",
        "unpatched_theorem_closure_claimed",
        "observed_data_used_as_selector",
        "target_fitting_used",
    ]:
        require(data[key] is False, f"candidate guardrail overclaimed: {key}")
        require(cert[key] is False, f"certificate guardrail overclaimed: {key}")

    require(
        table["status"] == "HUANG_ZHOU_TAU_MZ_EFT_AND_FULLSM_TABLE_VALUES_IMPORTED",
        "table status mismatch",
    )
    require(table["table_values_imported"] is True, "table values not imported")
    require(table["single_convention_selected_by_table_alone"] is False, "table alone selects convention")
    require(table["closure_claimed"] is True, "table import should close locally")
    eft = table["table_rows"]["EFT_QCDxQED_5q3l_MZ"]
    full = table["table_rows"]["FullSM_6q3l_MZ"]
    require(close(eft["mass_GeV"], 1.74743), "EFT tau mass changed")
    require(close(eft["uncertainty_GeV"], 0.00012), "EFT tau uncertainty changed")
    require(close(eft["yukawa_from_repo_vev"], 0.010036726570212717), "EFT tau Yukawa changed")
    require(close(full["mass_GeV"], 1.72856), "full-SM tau mass changed")
    require(close(full["uncertainty_GeV"], 0.00028), "full-SM tau uncertainty changed")
    require(close(full["yukawa_from_repo_vev"], 0.00992834281213376), "full-SM tau Yukawa changed")

    require(
        convention["status"] == "TAU_EFT_MZ_CONVENTION_ACCEPTED_AS_EXTERNAL_MAP_ROW_FULLSM_CONVERSION_OPEN",
        "convention status mismatch",
    )
    require(convention["selected_external_tau_row_convention"] == "EFT_QCDxQED_5q3l_MZ", "wrong tau convention")
    require(convention["full_SM_tau_row_reserved_for_later_reconciliation"] is True, "full-SM row not reserved")
    require(convention["selected_Rtheta_mass_scheme_derivation_closed"] is False, "Rtheta overclosed")
    require(convention["closure_claimed"] is True, "convention should close locally")
    cross = convention["b_c_table_crosscheck"]
    require(abs(cross["bottom_absolute_delta_GeV"]) < 0.001, "bottom/table crosscheck changed")
    require(cross["charm_absolute_delta_GeV"] > 0.05, "charm mismatch guard changed")
    require("mismatch" in cross["crosscheck_interpretation"], "charm mismatch interpretation missing")

    require(
        tau["status"] == "TAU_EFT_MZ_EXTERNAL_MASS_SCHEME_ROW_ACCEPTED_RTHETA_OPEN",
        "tau row status mismatch",
    )
    row = tau["accepted_external_map_row"]
    require(row["id"] == "tau_pole_rest_to_running_lepton", "wrong tau row id")
    require(row["target_convention"] == "EFT_QCDxQED_5q3l_MZ", "wrong row convention")
    require(close(row["huang_zhou_running_mass_MZ_GeV"], 1.74743), "tau row mass changed")
    require(close(row["huang_zhou_yukawa_MZ_from_repo_vev"], 0.010036726570212717), "tau row Yukawa changed")
    require(row["accepted_as_external_map_row"] is True, "tau row not accepted external")
    require(row["accepted_as_Rtheta_source_row"] is False, "tau row accepted as Rtheta")
    require(row["multiplicative_factor_vs_native_inventory"] < 1.0, "tau/native factor unexpected")
    require(row["multiplicative_factor_vs_legacy_firstpass"] < 1.0, "tau/legacy factor unexpected")
    for source, sidecar in row["diagonal_sensitivity_sidecar"].items():
        require(source in {"m_tau_MZ_EFT", "vev"}, f"unexpected tau sidecar: {source}")
        for key in ["central_value", "minus_value", "plus_value", "symmetric_half_width"]:
            require(math.isfinite(float(sidecar[key])), f"nonfinite tau sidecar {source} {key}")
        require(sidecar["symmetric_half_width"] >= 0.0, f"negative tau sidecar {source}")
    require(tau["reserved_fullSM_alternative"]["target_convention"] == "FullSM_6q3l_MZ", "full-SM alternative missing")
    require(tau["tau_external_row_closed"] is True, "tau external row not closed")
    require(tau["selected_Rtheta_mass_scheme_derivation_closed"] is False, "Rtheta overclosed in tau row")
    require(tau["closure_claimed"] is True, "tau row should close locally")

    require(
        cutset["status"] == "NEXT_RECONCILE_ALL_BCT_EXTERNAL_ROWS_WITH_FULLSM_CONVENTION_AND_RTHETA",
        "cutset status mismatch",
    )
    for key in [
        "tau_EFT_MZ_table_values_imported",
        "tau_pole_rest_to_running_lepton_external_row",
        "all_three_bct_external_mass_scheme_rows_available",
    ]:
        require(cutset["closed_now"][key] is True, f"cutset closed flag missing: {key}")
    for key in [
        "fullSM_tau_conversion_or_profile_reconciliation",
        "charm_CRunDec_vs_HuangZhou_table_reconciliation",
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
    require(closure["tau_pole_rest_to_running_lepton_external_row_closed"] is True, "candidate tau row not closed")
    require(closure["accepted_bottom_charm_tau_map_row_count"] == 3, "candidate b/c/tau count mismatch")
    require(closure["all_three_bct_external_mass_scheme_rows_available"] is True, "all-three flag missing")
    for key in [
        "fullSM_tau_conversion_or_profile_reconciliation_closed",
        "charm_CRunDec_vs_HuangZhou_table_reconciliation_closed",
        "selected_Rtheta_mass_scheme_derivation_closed",
        "W_Z_H_electroweak_matching_rows_closed",
        "full_covariance_profile_likelihood_closed",
        "true_SM_equivalence_closed",
        "full_no_knob_closed",
    ]:
        require(closure[key] is False, f"candidate overclosed: {key}")

    require("accepted b/c/tau external rows: 3" in note, "note missing row count")
    require("full-SM tau convention closed : false" in note, "note missing full-SM guard")
    require(NEXT in note, "note missing next artifact")
    print(json.dumps({"audit": SLUG, "status": "ok"}, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
