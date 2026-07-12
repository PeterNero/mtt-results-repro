"""Audit covariance sidecar fill or Rtheta source-row derivation artifact."""

from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SLUG = "selected_covariancesidecarfill_or_rthetasourcerowderivation"
DATA = ROOT / "candidate_data" / f"{SLUG}.candidate.json"
PACKET_DIR = ROOT / "candidate_data" / SLUG
SIDECARS = PACKET_DIR / "wzh_gauge_and_lambda_covariance_sidecars.packet.json"
LADDER = PACKET_DIR / "interim_covariance_ladder_after_sidecar_fill.packet.json"
RTHETA = PACKET_DIR / "rtheta_source_row_derivation_recheck_after_sidecar_fill.packet.json"
CUTSET = PACKET_DIR / "next_cutset_after_covariance_sidecar_fill.packet.json"
CERT = ROOT / "certificates" / f"{SLUG}_certificate.json"
NOTE = ROOT / "proof_corpus" / "MTT_Selected_CovarianceSidecarFill_or_RThetaSourceRowDerivation_v1.md"
BUILDER = ROOT / "scripts" / f"build_{SLUG}.py"

STATUS = (
    "MTT_SELECTED_COVARIANCESIDECARFILL_OR_RTHETASOURCEROWDERIVATION_"
    "BUILT_WZH_SIDECARS_INTERIM_LADDER_RTHETA_OPEN"
)
NEXT = "MTT_Selected_CrossBlockCovariance_or_RThetaCoefficientValueFill_v1"


def load(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def require(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)


def main() -> int:
    subprocess.run([sys.executable, str(BUILDER)], cwd=ROOT, check=True)

    data = load(DATA)
    cert = load(CERT)
    sidecars = load(SIDECARS)
    ladder = load(LADDER)
    rtheta = load(RTHETA)
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
        sidecars["status"] == "WZH_INTERIM_COVARIANCE_SIDECARS_FILLED_FULL_COVARIANCE_OPEN",
        "sidecar status mismatch",
    )
    require(sidecars["accepted_as_interim_covariance_sidecars"] is True, "interim sidecars not accepted")
    require(sidecars["accepted_as_full_covariance_profile"] is False, "full covariance overclaimed")
    require(sidecars["accepted_as_selected_Rtheta_source_rows"] is False, "Rtheta source rows overclaimed")
    require(sidecars["fills_previous_missing_object"].startswith("gauge-row uncertainty"), "wrong filled object")
    require(sidecars["independent_covariance_basis"] == ["v_from_G_F_tree_reference", "g_Y_Mt", "g_2_Mt", "lambda_Mt"], "basis changed")
    require(sidecars["alias_basis"]["g_1_GUT_Mt"]["must_not_be_double_counted_in_covariance"] is True, "g1 alias guard missing")
    require(len(sidecars["row_sidecars"]) == 5, "wrong sidecar row count")
    for row in sidecars["row_sidecars"]:
        require(row["total_interim_sigma"] > 0.0, f"nonpositive sigma: {row['id']}")
        require(row["variance"] > 0.0, f"nonpositive variance: {row['id']}")
        require(row["accepted_as_interim_covariance_sidecar"] is True, f"row sidecar not accepted: {row['id']}")
        require(row["accepted_as_full_covariance_sidecar"] is False, f"row full sidecar overclaimed: {row['id']}")
        require(row["accepted_as_selected_Rtheta_source_row"] is False, f"row Rtheta overclaimed: {row['id']}")
    require(len(sidecars["diagonal_covariance_matrix"]) == 4, "covariance dimension mismatch")
    for i, row in enumerate(sidecars["diagonal_covariance_matrix"]):
        require(len(row) == 4, "covariance row dimension mismatch")
        for j, value in enumerate(row):
            if i == j:
                require(value > 0.0, "diagonal covariance not positive")
            else:
                require(value == 0.0, "interim WZH covariance should be diagonal")
    require(sidecars["closure_claimed"] is True, "sidecar packet should close locally")

    require(
        ladder["status"] == "INTERIM_COVARIANCE_LADDER_ADVANCED_CROSS_BLOCK_PROFILE_OPEN",
        "ladder status mismatch",
    )
    require(ladder["advanced_now"]["WZH_interim_sidecars"] is True, "ladder did not advance WZH sidecars")
    require(ladder["advanced_now"]["gauge_alias_handling_for_g1GUT"] is True, "alias handling not advanced")
    require(ladder["can_build_interim_block_diagonal_profile"] is True, "interim block diagonal profile unavailable")
    require(ladder["can_claim_full_correlated_profile"] is False, "full correlated profile overclaimed")
    require(
        all(not item.startswith("gauge-row uncertainty") for item in ladder["missing_covariance_objects_after_sidecar_fill"]),
        "gauge sidecar gap still listed after fill",
    )
    require(
        "cross-block covariance linking W/Z/H, top/Higgs, BCT, and Higgs-decay replay rows"
        in ladder["missing_covariance_objects_after_sidecar_fill"],
        "cross-block covariance gap missing",
    )
    require(ladder["closure_claimed"] is False, "ladder overclosed")

    require(
        rtheta["status"] == "RTHETA_SOURCE_ROW_DERIVATION_RECHECKED_STILL_OPEN",
        "Rtheta recheck status mismatch",
    )
    require(rtheta["source_owner_candidate_matrix_closed"] is True, "Rtheta source-owner matrix should be closed")
    require(rtheta["row_coefficient_slot_manifest_closed"] is True, "Rtheta slot manifest should be closed")
    require(rtheta["row_coefficients_filled"] is False, "Rtheta coefficients overfilled")
    require(rtheta["selected_threshold_response_functional_instantiated"] is False, "threshold functional overclosed")
    require(rtheta["selected_Rtheta_source_rows_closed"] is False, "selected Rtheta rows overclosed")
    require(rtheta["accepted_Rtheta_source_row_count"] == 0, "Rtheta row count mismatch")
    require(rtheta["closure_claimed"] is False, "Rtheta recheck overclosed")

    require(
        cutset["status"] == "NEXT_ATTACK_CROSS_BLOCK_COVARIANCE_OR_RTHETA_COEFFICIENT_VALUES",
        "cutset status mismatch",
    )
    for key in [
        "WZH_interim_covariance_sidecars",
        "gauge_alias_handling_for_covariance",
        "interim_covariance_ladder_advanced",
        "Rtheta_derivation_rechecked_after_sidecar_fill",
    ]:
        require(cutset["closed_now"][key] is True, f"cutset closed flag missing: {key}")
    for key in [
        "cross_block_covariance",
        "full_covariance_profile_likelihood",
        "Rtheta_row_coefficients",
        "selected_threshold_response_functional",
        "selected_Rtheta_source_rows",
        "common_scale_convention_map",
        "EW_formula_kernels_for_WW_ZZ_Zgamma",
        "true_SM_equivalence",
        "full_no_knob",
    ]:
        require(cutset["still_open"][key] is True, f"cutset open flag missing: {key}")
    require(cutset["recommended_next"]["artifact"] == NEXT, "cutset next mismatch")
    require(cutset["closure_claimed"] is False, "cutset overclosed")

    closure = data["closure_decision"]
    require(closure["WZH_interim_covariance_sidecars_closed"] is True, "candidate sidecars not closed")
    require(closure["interim_block_diagonal_profile_available"] is True, "candidate interim profile unavailable")
    for key in [
        "full_covariance_profile_likelihood_closed",
        "selected_Rtheta_source_rows_closed",
        "true_SM_equivalence_closed",
        "full_no_knob_closed",
    ]:
        require(closure[key] is False, f"candidate overclosed: {key}")
    require(cert["WZH_interim_covariance_sidecars_closed"] is True, "certificate sidecar closure missing")
    require(cert["selected_Rtheta_source_rows_closed"] is False, "certificate Rtheta overclosed")
    require("W/Z/H interim sidecars closed       : true" in note, "note missing sidecar status")
    require("cross-block covariance closed       : false" in note, "note missing covariance guard")

    print(f"PASS {DATA.name}: {STATUS}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
