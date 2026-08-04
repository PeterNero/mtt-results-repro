"""Audit common-scale Jacobian or Rtheta threshold response execution artifact."""

from __future__ import annotations

import json
import math
import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SLUG = "selected_commonscalejacobian_or_rthetathresholdresponseexecution"
DATA = ROOT / "candidate_data" / f"{SLUG}.candidate.json"
PACKET_DIR = ROOT / "candidate_data" / SLUG
ALGEBRAIC = PACKET_DIR / "bct_mz_mass_to_yukawa_v_jacobian.packet.json"
MZMT_GAP = PACKET_DIR / "mz_to_mt_common_scale_jacobian_gap.packet.json"
RTHETA = PACKET_DIR / "rtheta_threshold_response_execution_gate.packet.json"
CUTSET = PACKET_DIR / "next_cutset_after_common_scale_jacobian.packet.json"
CERT = ROOT / "certificates" / f"{SLUG}_certificate.json"
NOTE = ROOT / "proof_corpus" / "MTT_Selected_CommonScaleJacobian_or_RThetaThresholdResponseExecution_v1.md"
BUILDER = ROOT / "scripts" / f"build_{SLUG}.py"

STATUS = (
    "MTT_SELECTED_COMMONSCALEJACOBIAN_OR_RTHETATHRESHOLDRESPONSEEXECUTION_"
    "BUILT_BCT_YUKAWA_JACOBIAN_MZMT_RTHETA_OPEN"
)
NEXT = "MTT_Selected_MZtoMtJacobianExecution_or_SelectedThresholdResponseFunctionalFill_v1"


def load(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def require(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)


def main() -> int:
    subprocess.run([sys.executable, str(BUILDER)], cwd=ROOT, check=True)

    data = load(DATA)
    cert = load(CERT)
    algebraic = load(ALGEBRAIC)
    gap = load(MZMT_GAP)
    rtheta = load(RTHETA)
    cutset = load(CUTSET)
    note = NOTE.read_text(encoding="utf-8")

    require(data["status"] == STATUS, "candidate status mismatch")
    require(cert["status"] == STATUS, "certificate status mismatch")
    require(data["next_required_artifact"] == NEXT, "candidate next mismatch")
    require(cert["next_required_artifact"] == NEXT, "certificate next mismatch")
    for key in ["closure_claimed", "unpatched_theorem_closure_claimed", "observed_data_used_as_selector", "target_fitting_used"]:
        require(data[key] is False, f"candidate guardrail overclaimed: {key}")

    require(algebraic["status"] == "BCT_MZ_MASS_TO_YUKAWA_V_JACOBIAN_BUILT_MZ_TO_MT_OPEN", "algebraic status mismatch")
    require(algebraic["closes_common_scale_algebraic_yukawa_map"] is True, "algebraic map not closed")
    require(algebraic["closes_MZ_to_Mt_RG_transport_jacobian"] is False, "MZ->Mt overclosed")
    require(algebraic["matrix_shape"] == [3, 4], "Jacobian shape mismatch")
    require(len(algebraic["row_jacobians"]) == 3, "wrong row count")
    for row in algebraic["row_jacobians"]:
        expected_y = math.sqrt(2.0) * row["mass_MZ_GeV"] / row["v_GeV"]
        expected_dm = math.sqrt(2.0) / row["v_GeV"]
        expected_dv = -math.sqrt(2.0) * row["mass_MZ_GeV"] / (row["v_GeV"] ** 2)
        require(abs(row["yukawa_MZ"] - expected_y) <= 1e-18, f"y formula mismatch: {row['id']}")
        require(abs(row["dy_dm"] - expected_dm) <= 1e-18, f"dy/dm mismatch: {row['id']}")
        require(abs(row["dy_dv"] - expected_dv) <= 1e-18, f"dy/dv mismatch: {row['id']}")
        require(row["accepted_as_algebraic_common_scale_jacobian_row"] is True, f"algebraic row not accepted: {row['id']}")
        require(row["accepted_as_MZ_to_Mt_RG_jacobian_row"] is False, f"MZ->Mt row overclosed: {row['id']}")
        require(row["accepted_as_Rtheta_source_row"] is False, f"Rtheta row overclosed: {row['id']}")
    require(algebraic["closure_claimed"] is True, "algebraic packet should close locally")

    require(gap["closes_common_scale_MZ_to_Mt_jacobian"] is False, "gap MZ->Mt overclosed")
    require(gap["closes_common_scale_convention_map"] is False, "gap convention overclosed")
    require(gap["accepted_common_scale_values_for_profile_input"] is True, "common scale profile input not accepted")
    require(gap["accepted_for_true_precision_equivalence"] is False, "true precision overaccepted")
    require(len(gap["why_MZ_to_Mt_jacobian_still_open"]) == 4, "gap reason count changed")
    require(gap["closure_claimed"] is False, "gap overclosed")

    require(rtheta["contract_emitted"] is True, "Rtheta contract missing")
    require(rtheta["algebraic_jacobian_can_validate_future_Rtheta"] is True, "validation relation missing")
    require(rtheta["algebraic_jacobian_selects_Rtheta"] is False, "algebraic Jacobian selects Rtheta")
    require(rtheta["Rtheta_coefficient_values_closed"] is False, "Rtheta coefficients overclosed")
    require(rtheta["selected_threshold_response_functional_instantiated"] is False, "threshold response overclosed")
    require(rtheta["selected_Rtheta_source_rows_closed"] is False, "source rows overclosed")
    require(rtheta["accepted_Rtheta_source_row_count"] == 0, "Rtheta row count mismatch")
    require(rtheta["closure_claimed"] is False, "Rtheta gate overclosed")

    for key in ["BCT_MZ_mass_to_yukawa_v_jacobian", "common_scale_algebraic_yukawa_map", "Rtheta_threshold_response_contract_rechecked"]:
        require(cutset["closed_now"][key] is True, f"cutset closed flag missing: {key}")
    for key in [
        "MZ_to_Mt_common_scale_RG_jacobian",
        "common_scale_convention_map_for_precision",
        "numeric_cross_block_covariance_values",
        "Rtheta_coefficient_values",
        "selected_threshold_response_functional",
        "selected_Rtheta_source_rows",
        "full_covariance_profile_likelihood",
        "true_SM_equivalence",
        "full_no_knob",
    ]:
        require(cutset["still_open"][key] is True, f"cutset open flag missing: {key}")
    require(cutset["recommended_next"]["artifact"] == NEXT, "cutset next mismatch")

    closure = data["closure_decision"]
    require(closure["BCT_MZ_mass_to_yukawa_v_jacobian_closed"] is True, "candidate algebraic Jacobian not closed")
    for key in [
        "MZ_to_Mt_common_scale_RG_jacobian_closed",
        "numeric_cross_block_covariance_values_closed",
        "Rtheta_coefficient_values_closed",
        "selected_threshold_response_functional_closed",
        "selected_Rtheta_source_rows_closed",
        "full_covariance_profile_likelihood_closed",
        "true_SM_equivalence_closed",
        "full_no_knob_closed",
    ]:
        require(closure[key] is False, f"candidate overclosed: {key}")
    require(cert["BCT_MZ_mass_to_yukawa_v_jacobian_closed"] is True, "certificate algebraic closure missing")
    require("BCT M_Z mass-to-yukawa Jacobian : true" in note, "note missing algebraic closure")
    require("M_Z -> M_t RG Jacobian           : false" in note, "note missing MZ->Mt guard")

    print(f"PASS {DATA.name}: {STATUS}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
