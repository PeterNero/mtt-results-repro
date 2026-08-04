"""Audit residual-cause decision after selected Pi_CKM weight rows."""

from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SLUG = "selected_pickmweightrows_ckmresidualdecision_or_higherorderclosure"
BUILDER = ROOT / "scripts" / f"build_{SLUG}.py"
CANDIDATE = ROOT / "candidate_data" / f"{SLUG}.candidate.json"
PACKET_DIR = ROOT / "candidate_data" / SLUG
FINGERPRINT = PACKET_DIR / "selected_pickm_ckm_residual_fingerprint.packet.json"
CAUSE = PACKET_DIR / "selected_pickm_ckm_residual_cause_decision.packet.json"
TEMPLATE = PACKET_DIR / "higher_order_or_profile_residual_template.packet.json"
CERT = ROOT / "certificates" / f"{SLUG}_certificate.json"
NOTE = ROOT / "proof_corpus" / "MTT_Selected_PiCKMWeightRows_CKMResidualDecision_or_HigherOrderClosure_v1.md"

STATUS = "MTT_SELECTED_PICKM_WEIGHT_ROWS_RESIDUAL_CAUSE_AUDITED_HIGHERORDER_OR_PROFILE_OPEN"
NEXT = "MTT_Selected_CKMCovarianceProfileOrHigherOrderResidualClosure_v1"


def require(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)


def load(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def main() -> int:
    subprocess.run([sys.executable, str(BUILDER)], cwd=ROOT, check=True)

    data = load(CANDIDATE)
    fingerprint = load(FINGERPRINT)
    cause = load(CAUSE)
    template = load(TEMPLATE)
    cert = load(CERT)
    note = NOTE.read_text(encoding="utf-8")

    require(data["status"] == STATUS, "candidate status mismatch")
    require(cert["status"] == STATUS, "certificate status mismatch")
    require(data["next_required_artifact"] == NEXT, "candidate next mismatch")
    require(cert["next_required_artifact"] == NEXT, "certificate next mismatch")
    require(data["theorem"]["name"] == "PiCKMWeightRowsResidualCauseAuditTheorem", "theorem name")
    require(data["theorem"]["proved"] is True, "theorem not proved")
    require(cert["theorem_proved"] is True, "certificate theorem not proved")

    closure = data["closure_decision"]
    require(closure["residual_cause_audited"] is True, "residual not audited")
    require(closure["selected_Pi_CKM_row_certificates"] == 3, "row certs not retained")
    require(closure["accepted_weight_rows"] == 3, "weight rows not retained")
    require(closure["accepted_exact_ckm_correction_rows"] == 0, "exact correction overaccepted")
    require(closure["accepted_no_knob_CKM_angle_rows"] == 0, "no-knob angle rows overaccepted")
    require(closure["exact_ckm_angle_magnitudes_closed"] is False, "exact CKM overclosed")
    require(closure["true_SM_equivalence_closed"] is False, "true SM overclosed")
    require(closure["full_no_knob_closure_closed"] is False, "no-knob overclosed")

    require(fingerprint["status"] == "RESIDUAL_FINGERPRINT_COMPUTED", "fingerprint status")
    require(fingerprint["roundoff_scale_rejected"] is True, "roundoff not rejected")
    require(fingerprint["observed_data_used_as_selector"] is False, "fingerprint observed selector")
    require(fingerprint["observed_data_used_for_postcheck"] is True, "fingerprint postcheck flag")
    require(fingerprint["target_fitting_used"] is False, "fingerprint target fitting")
    require(set(fingerprint["weight_residuals"]) == {"W12", "W23", "W13"}, "residual row set")
    require(fingerprint["weight_residuals"]["W12"]["required_minus_selected_weight"] > 0, "W12 sign")
    require(fingerprint["weight_residuals"]["W23"]["required_minus_selected_weight"] < 0, "W23 sign")
    require(fingerprint["weight_residuals"]["W13"]["required_minus_selected_weight"] < 0, "W13 sign")
    q_eff = fingerprint["effective_q_if_each_row_forced_to_replay"]
    require(q_eff["W12"]["delta_from_79"] > 0, "W12 q delta sign")
    require(q_eff["W23"]["delta_from_79"] > 0, "W23 q delta sign")
    require(q_eff["W13"]["delta_from_79"] < 0, "W13 q delta sign")
    require(abs(q_eff["W12"]["delta_from_79"] - q_eff["W13"]["delta_from_79"]) > 0.01, "q relabel not row-specific")
    z_scores = fingerprint["z_scores_against_frozen_ckm_inputs"]
    for angle, payload in z_scores.items():
        require(payload["absolute_residual_over_estimated_sigma"] < 1.0e-3, f"{angle} too large vs uncertainty")

    require(cause["status"] == "RESIDUAL_CAUSE_AUDITED_NO_EXACT_CLOSURE", "cause status")
    for key, value in cause["ruled_out_causes"].items():
        require(value is True, f"cause not ruled out: {key}")
    findings = cause["positive_findings"]
    require(findings["selected_rows_are_source_owned"] is True, "source ownership missing")
    require(findings["exact_central_replay_residual_is_nonzero"] is True, "nonzero residual missing")
    require(findings["residual_is_far_below_current_diagonal_ckm_uncertainty_estimate"] is True, "uncertainty finding missing")
    require(findings["largest_central_residual_row"] == "s13/W13", "largest row mismatch")
    require(cause["accepted_weight_rows"] == 3, "cause weight row count")
    require(cause["accepted_exact_ckm_correction_rows"] == 0, "cause exact overaccepted")
    require(cause["accepted_no_knob_ckm_angle_rows"] == 0, "cause no-knob overaccepted")
    require(cause["exact_ckm_angle_magnitudes_closed"] is False, "cause exact CKM overclosed")
    require(cause["true_SM_equivalence_closed"] is False, "cause true SM overclosed")

    require(template["status"] == "HIGHER_ORDER_OR_PROFILE_RESIDUAL_TARGETS_DEFINED_NO_ROWS_ACCEPTED", "template status")
    require(template["accepted_residual_correction_rows"] == 0, "template residual rows overaccepted")
    require(template["next_required_artifact"] == NEXT, "template next")
    require(len(template["candidate_legal_exits"]) == 3, "legal exits count")
    require(len(template["forbidden_exits"]) == 4, "forbidden exits count")

    nums = data["key_numbers"]
    require(nums["accepted_residual_correction_rows"] == 0, "key residual rows")
    require(nums["max_abs_residual_sigma_score_no_covariance"] < 1.0e-3, "key sigma score")
    require(data["closure_claimed"] is False, "candidate closure overclaimed")
    require(data["observed_data_used_as_selector"] is False, "candidate observed selector")
    require(data["observed_data_used_for_postcheck"] is True, "candidate postcheck flag")
    require(data["target_fitting_used"] is False, "candidate target fitting")

    require(cert["residual_cause_audited"] is True, "cert residual audit")
    require(cert["accepted_weight_rows"] == 3, "cert weight rows")
    require(cert["accepted_residual_correction_rows"] == 0, "cert residual rows")
    require(cert["exact_ckm_angle_magnitudes_closed"] is False, "cert exact CKM")
    require(cert["closure_claimed"] is False, "cert closure")

    for phrase in [
        "Ruled out:",
        "one q/phase relabel",
        "far below one",
        "Next legal exits:",
        NEXT,
    ]:
        require(phrase in note, f"note missing {phrase}")

    print(f"PASS {CANDIDATE.name}: {STATUS}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
