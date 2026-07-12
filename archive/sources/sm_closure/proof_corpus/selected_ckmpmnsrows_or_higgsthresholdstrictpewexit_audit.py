"""Audit CKM/PMNS rows versus Higgs/threshold/strict-PEW exit reduction."""

from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SLUG = "selected_ckmpmnsrows_or_higgsthresholdstrictpewexit"
BUILDER = ROOT / "scripts" / f"build_{SLUG}.py"
CANDIDATE = ROOT / "candidate_data" / f"{SLUG}.candidate.json"
PACKET_DIR = ROOT / "candidate_data" / SLUG
CKM_STATUS = PACKET_DIR / "ckm_weightrow_status_after_pickm_residual_audit.packet.json"
PMNS_STATUS = PACKET_DIR / "pmns_runningratio_status_after_flavor_bridge.packet.json"
DECISION = PACKET_DIR / "ckmpmns_higgs_pew_exit_decision.packet.json"
CERT = ROOT / "certificates" / f"{SLUG}_certificate.json"
NOTE = ROOT / "proof_corpus" / "MTT_Selected_CKMPMNSRows_or_HiggsThresholdStrictPEWExit_v1.md"

STATUS = (
    "MTT_SELECTED_CKMPMNSROWS_OR_HIGGSTHRESHOLDSTRICTPEWEXIT_"
    "BUILT_CKM_WEIGHTROWS_CLOSED_PMNS_HIGGS_PEW_OPEN"
)
NEXT = "MTT_Selected_CKMCovarianceProfileOrHigherOrderResidualClosure_or_PMNSHiggsPEWRows_v1"


def require(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)


def load(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def main() -> int:
    subprocess.run([sys.executable, str(BUILDER)], cwd=ROOT, check=True)

    data = load(CANDIDATE)
    ckm = load(CKM_STATUS)
    pmns = load(PMNS_STATUS)
    decision = load(DECISION)
    cert = load(CERT)
    note = NOTE.read_text(encoding="utf-8")

    require(data["status"] == STATUS, "candidate status")
    require(cert["status"] == STATUS, "cert status")
    require(data["next_required_artifact"] == NEXT, "candidate next")
    require(cert["next_required_artifact"] == NEXT, "cert next")
    require(data["closure_claimed"] is False, "candidate overclosed")
    require(data["observed_data_used_as_selector"] is False, "candidate observed selector")
    require(data["target_fitting_used"] is False, "candidate target fitting")
    require(data["observed_data_used_for_postcheck"] is True, "postcheck flag")

    require(ckm["status"] == "CKM_PICKM_WEIGHT_ROWS_CLOSED_EXACT_CENTRAL_RESIDUAL_OPEN", "CKM status")
    require(ckm["observed_data_used_as_selector"] is False, "CKM observed selector")
    require(ckm["target_fitting_used"] is False, "CKM target fitting")
    require(ckm["observed_data_used_for_postcheck"] is True, "CKM postcheck")
    require(ckm["accepted_selected_Pi_CKM_weight_rows"] == 3, "CKM rows")
    require(ckm["selected_Pi_CKM_row_certificates"] == 3, "CKM certs")
    require(set(ckm["selected_weights"]) == {"W12", "W13", "W23"}, "weights")
    require(ckm["q79_CKM_CP_phase_contact_imported"] is True, "q79 phase")
    require(ckm["residual_cause_audited"] is True, "residual audit")
    require(ckm["accepted_exact_ckm_correction_rows"] == 0, "exact CKM rows")
    require(ckm["accepted_no_knob_CKM_angle_rows"] == 0, "no-knob CKM rows")
    require(ckm["exact_ckm_angle_magnitudes_closed"] is False, "CKM overclosed")

    require(pmns["status"] == "PMNS_AND_RUNNING_RATIO_SOURCE_ROWS_OPEN", "PMNS status")
    require(pmns["observed_data_used_as_selector"] is False, "PMNS observed selector")
    require(pmns["target_fitting_used"] is False, "PMNS target fitting")
    require(pmns["CKM_PMNS_orientation_bridge_executable"] is True, "bridge executable")
    require(pmns["policy_csk_source_value_row_count"] == 9, "policy csk")
    require(pmns["strict_selected_csk_source_row_count"] == 0, "strict csk")
    require(pmns["selected_CKM_PMNS_orientation_source_closed"] is False, "orientation overclosed")
    require(pmns["selected_CKM_PMNS_values_derived"] is False, "values overclosed")
    require(pmns["selected_orientation_source_theorem_closed"] is False, "source theorem overclosed")
    require(pmns["running_mass_ratio_rows_closed"] is False, "running ratio overclosed")
    require(pmns["PMNS_angle_phase_rows_closed"] is False, "PMNS overclosed")

    require(
        decision["status"] == "CKM_WEIGHT_SUBLAYER_CLOSED_FULL_CKMPMNS_HIGGS_PEW_OPEN",
        "decision status",
    )
    require(len(decision["closed_now"]) == 4, "closed count")
    require(len(decision["not_closed"]) == 3, "not closed count")
    counts = decision["source_row_counts"]
    require(counts["accepted_selected_Pi_CKM_weight_rows"] == 3, "decision CKM rows")
    require(counts["selected_Pi_CKM_row_certificates"] == 3, "decision CKM certs")
    require(counts["accepted_exact_ckm_correction_rows"] == 0, "decision exact CKM")
    require(counts["accepted_no_knob_CKM_angle_rows"] == 0, "decision no-knob CKM")
    require(counts["strict_selected_csk_source_row_count"] == 0, "decision strict csk")
    require(counts["PMNS_angle_phase_rows"] == 0, "decision PMNS")
    require(counts["running_mass_ratio_rows"] == 0, "decision running ratios")
    acceptance = decision["acceptance"]
    require(acceptance["ckm_Pi_weight_rows_closed"] is True, "accept CKM rows")
    require(acceptance["ckm_exact_central_residual_closed"] is False, "accept CKM residual")
    require(acceptance["ckm_covariance_or_higher_order_profile_closed"] is False, "profile overclosed")
    require(acceptance["PMNS_rows_closed"] is False, "PMNS overclosed")
    require(acceptance["running_mass_ratio_rows_closed"] is False, "running overclosed")
    require(acceptance["higgs_threshold_rows_closed"] is False, "Higgs overclosed")
    require(acceptance["strict_PEW_directK_values_closed"] is False, "PEW overclosed")
    require(acceptance["fullS2_obligation_rows_closed_after_previous_update"] == 2, "fullS2 count")
    require(acceptance["fullS2_no_proxy_rows_closed"] is False, "fullS2 overclosed")
    require(acceptance["global_true_SM_no_knob_closure"] is False, "global overclosed")
    require(acceptance["true_SM_equivalence_closed"] is False, "true SM overclosed")
    require(decision["next_exact_target"] == NEXT, "decision next")

    require(data["theorem"]["name"] == "CKMPMNSRowsOrHiggsThresholdStrictPEWExitReductionTheorem", "theorem")
    require(data["theorem"]["proved"] is True, "theorem proved")
    key = data["key_numbers"]
    require(key["accepted_selected_Pi_CKM_weight_rows"] == 3, "key CKM")
    require(key["accepted_exact_ckm_correction_rows"] == 0, "key exact")
    require(key["accepted_no_knob_CKM_angle_rows"] == 0, "key no-knob")
    require(key["PMNS_angle_phase_rows"] == 0, "key PMNS")
    require(key["running_mass_ratio_rows"] == 0, "key running")

    require(cert["ckm_Pi_weight_rows_closed"] is True, "cert CKM")
    require(cert["accepted_selected_Pi_CKM_weight_rows"] == 3, "cert row count")
    require(cert["ckm_exact_central_residual_closed"] is False, "cert exact")
    require(cert["PMNS_rows_closed"] is False, "cert PMNS")
    require(cert["running_mass_ratio_rows_closed"] is False, "cert running")
    require(cert["higgs_threshold_rows_closed"] is False, "cert Higgs")
    require(cert["strict_PEW_directK_values_closed"] is False, "cert PEW")
    require(cert["fullS2_no_proxy_rows_closed"] is False, "cert fullS2")
    require(cert["global_true_SM_no_knob_closure"] is False, "cert global")
    require(cert["true_SM_equivalence_closed"] is False, "cert true SM")

    for phrase in [
        "selected `Pi_CKM` weight rows: `3/3`",
        "exact/no-knob CKM correction rows: `0`",
        "PMNS rows: `0`",
        "strict `P_EW` / direct-K normalization values: open",
        NEXT,
    ]:
        require(phrase in note, f"note missing {phrase}")

    print(f"PASS {CANDIDATE.name}: {STATUS}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
