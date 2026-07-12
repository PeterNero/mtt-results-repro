"""Audit all b/c/tau external rows or full-SM convention reconciliation artifact."""

from __future__ import annotations

import json
import math
import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SLUG = "selected_allbctexternalrows_or_fullsmconventionreconciliation"
DATA = ROOT / "candidate_data" / f"{SLUG}.candidate.json"
PACKET_DIR = ROOT / "candidate_data" / SLUG
ROW_ASSEMBLY = PACKET_DIR / "all_bct_external_rows_assembly.packet.json"
HZ_MATRIX = PACKET_DIR / "huang_zhou_eft_fullsm_reconciliation_matrix.packet.json"
PROFILE_GATE = PACKET_DIR / "fullsm_profile_reconciliation_gate.packet.json"
CUTSET = PACKET_DIR / "next_cutset_after_all_bct_external_rows.packet.json"
CERT = ROOT / "certificates" / f"{SLUG}_certificate.json"
NOTE = ROOT / "proof_corpus" / "MTT_Selected_AllBCTExternalRows_or_FullSMConventionReconciliation_v1.md"
BUILDER = ROOT / "scripts" / f"build_{SLUG}.py"

STATUS = (
    "MTT_SELECTED_ALLBCTEXTERNALROWS_OR_FULLSMCONVENTIONRECONCILIATION_"
    "BUILT_THREE_ROWS_FULLSM_PROFILE_OPEN"
)
NEXT = "MTT_Selected_BCTProfileReconciliation_or_RThetaMassSchemeDerivation_v1"


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
    assembly = load(ROW_ASSEMBLY)
    matrix = load(HZ_MATRIX)
    gate = load(PROFILE_GATE)
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

    require(assembly["status"] == "ALL_THREE_BCT_EXTERNAL_MASS_SCHEME_ROWS_ASSEMBLED", "assembly status mismatch")
    require(assembly["accepted_external_map_row_count"] == 3, "accepted external count mismatch")
    require(assembly["accepted_Rtheta_source_row_count"] == 0, "Rtheta source rows overaccepted")
    require(assembly["all_three_bct_external_mass_scheme_rows_available"] is True, "all-three flag missing")
    rows = {row["id"]: row for row in assembly["rows"]}
    require(set(rows) == {
        "bottom_MSbar_native_scale_transport",
        "charm_MSbar_native_scale_transport",
        "tau_pole_rest_to_running_lepton",
    }, "wrong assembled row ids")
    require(close(rows["bottom_MSbar_native_scale_transport"]["running_mass_MZ_GeV"], 2.8653031219496135), "bottom value changed")
    require(close(rows["charm_MSbar_native_scale_transport"]["running_mass_MZ_GeV"], 0.6792260486838773), "charm value changed")
    require(close(rows["tau_pole_rest_to_running_lepton"]["running_mass_MZ_GeV"], 1.74743), "tau value changed")
    for row in rows.values():
        require(row["accepted_as_external_map_row"] is True, f"row not external: {row['id']}")
        require(row["accepted_as_Rtheta_source_row"] is False, f"row is Rtheta source: {row['id']}")
    require(assembly["closure_claimed"] is True, "assembly should close locally")

    require(
        matrix["status"] == "BCT_EXTERNAL_ROWS_COMPARED_TO_EFT_AND_FULLSM_TABLES_PROFILE_OPEN",
        "matrix status mismatch",
    )
    summary = matrix["summary"]
    require(summary["all_rows_within_3sigma_EFT_table_band"] is True, "EFT 3sigma summary changed")
    require(summary["all_rows_within_3sigma_FullSM_table_band"] is False, "full-SM summary changed")
    require(summary["bottom_EFT_alignment_good"] is True, "bottom EFT alignment changed")
    require(summary["charm_EFT_alignment_borderline"] is True, "charm EFT guard changed")
    require(summary["tau_EFT_alignment_exact_table_import"] is True, "tau EFT alignment changed")
    require(summary["tau_FullSM_split_large"] is True, "tau full-SM split guard changed")

    mrows = matrix["matrix_rows"]
    require(
        close(
            mrows["bottom_MSbar_native_scale_transport"]["EFT_QCDxQED_5q3l_MZ"]["z_delta_using_table_sigma"],
            -0.026803001937948125,
        ),
        "bottom EFT z changed",
    )
    require(
        close(
            mrows["charm_MSbar_native_scale_transport"]["EFT_QCDxQED_5q3l_MZ"]["z_delta_using_table_sigma"],
            2.8458915935487368,
        ),
        "charm EFT z changed",
    )
    require(
        close(
            mrows["tau_pole_rest_to_running_lepton"]["FullSM_6q3l_MZ"]["z_delta_using_table_sigma"],
            67.39285714285694,
        ),
        "tau full-SM z changed",
    )
    require(matrix["closure_claimed"] is True, "matrix should close locally")

    require(gate["status"] == "EXTERNAL_BCT_ROWS_AVAILABLE_FULLSM_PROFILE_RECONCILIATION_OPEN", "gate status mismatch")
    for key in [
        "three_external_bct_mass_scheme_rows_available",
        "EFT_vs_fullSM_reconciliation_matrix_built",
        "tau_EFT_external_row_policy_explicit",
    ]:
        require(gate["closed_now"][key] is True, f"gate closed flag missing: {key}")
    for key in [
        "single_fullSM_profile_convention_for_bct_rows",
        "charm_table_reconciliation",
        "selected_Rtheta_mass_scheme_derivation",
        "profile_covariance_with_correlations",
    ]:
        require(gate["not_closed"][key] is True, f"gate open flag missing: {key}")
    require(gate["minimal_next_object"] == "BCTProfileReconciliationMatrixWithCovarianceOrSelectedRThetaRows", "wrong next object")
    require(gate["closure_claimed"] is False, "gate overclosed")

    require(
        cutset["status"] == "NEXT_ATTACK_BCT_PROFILE_RECONCILIATION_OR_SELECTED_RTHETA_DERIVATION",
        "cutset status mismatch",
    )
    for key in [
        "all_three_bct_external_mass_scheme_rows_available",
        "bct_EFT_fullSM_reconciliation_matrix",
        "fullSM_profile_gate_sharpened",
    ]:
        require(cutset["closed_now"][key] is True, f"cutset closed flag missing: {key}")
    for key in [
        "BCT_profile_reconciliation_matrix_with_covariance",
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
    require(closure["accepted_bottom_charm_tau_map_row_count"] == 3, "candidate row count mismatch")
    require(closure["all_three_bct_external_mass_scheme_rows_available"] is True, "candidate all-three missing")
    require(closure["bct_EFT_fullSM_reconciliation_matrix_built"] is True, "candidate matrix missing")
    for key in [
        "single_fullSM_profile_convention_for_bct_rows_closed",
        "BCT_profile_reconciliation_matrix_with_covariance_closed",
        "selected_Rtheta_mass_scheme_derivation_closed",
        "W_Z_H_electroweak_matching_rows_closed",
        "full_covariance_profile_likelihood_closed",
        "true_SM_equivalence_closed",
        "full_no_knob_closed",
    ]:
        require(closure[key] is False, f"candidate overclosed: {key}")

    require("accepted b/c/tau external rows : 3" in note, "note missing row count")
    require("full-SM profile closed          : false" in note, "note missing full-SM guard")
    require(NEXT in note, "note missing next artifact")
    print(json.dumps({"audit": SLUG, "status": "ok"}, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
