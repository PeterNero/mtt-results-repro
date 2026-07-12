"""Audit final E_CKM weight row certificate attempt."""

from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SLUG = "selected_eckmweightrowcertificates_or_ckmangleclosuredecision"
BUILDER = ROOT / "scripts" / f"build_{SLUG}.py"
CANDIDATE = ROOT / "candidate_data" / f"{SLUG}.candidate.json"
PACKET_DIR = ROOT / "candidate_data" / SLUG
SCAN = PACKET_DIR / "available_eckm_trace_invariant_scan.packet.json"
GATE = PACKET_DIR / "kckm_trace_assembly_rule_gate.packet.json"
DECISION = PACKET_DIR / "ckm_angle_closure_decision_after_eckm_attempt.packet.json"
CERT = ROOT / "certificates" / f"{SLUG}_certificate.json"
NOTE = ROOT / "proof_corpus" / "MTT_Selected_ECKMWeightRowCertificates_or_CKMAngleClosureDecision_v1.md"

STATUS = "MTT_SELECTED_ECKM_WEIGHT_ROW_CERTIFICATE_ATTEMPT_EXECUTED_KCKM_RULE_OPEN"
NEXT = "MTT_Selected_KCKMTraceAssemblyRule_or_OnePrincipleCKMClosure_v1"


def load(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def require(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)


def main() -> int:
    subprocess.run([sys.executable, str(BUILDER)], cwd=ROOT, check=True)

    data = load(CANDIDATE)
    scan = load(SCAN)
    gate = load(GATE)
    decision = load(DECISION)
    cert = load(CERT)
    note = NOTE.read_text(encoding="utf-8")

    require(data["status"] == STATUS, "candidate status mismatch")
    require(cert["status"] == STATUS, "cert status mismatch")
    require(data["next_required_artifact"] == NEXT, "candidate next mismatch")
    require(cert["next_required_artifact"] == NEXT, "cert next mismatch")
    require(data["theorem"]["proved"] is True, "theorem not proved")
    require(data["theorem"]["name"] == "ECKMWeightRowCertificateAttemptTheorem", "theorem name")
    require(cert["theorem_proved"] is True, "cert theorem")

    closure = data["closure_decision"]
    require(closure["available_eckm_trace_invariant_scan_executed"] is True, "scan not executed")
    require(closure["selected_K_CKM_rule_emitted"] is False, "K rule overemitted")
    require(closure["accepted_weight_rows"] == 0, "accepted weights")
    require(closure["accepted_exact_ckm_correction_rows"] == 0, "accepted corrections")
    require(closure["accepted_no_knob_CKM_angle_rows"] == 0, "accepted CKM rows")
    for key in [
        "CKM_angle_magnitudes_derived_exact",
        "Jarlskog_source_derived_without_measured_angles",
        "true_SM_equivalence_closed",
        "full_no_knob_closure_closed",
    ]:
        require(closure[key] is False, f"overclaim: {key}")

    require(scan["status"] == "AVAILABLE_ECKM_TRACE_INVARIANT_SCAN_EXECUTED_NO_ACCEPTED_ROWS", "scan status")
    require(scan["candidate_count"] > 1000, "scan too small")
    require(scan["accepted_weight_rows"] == 0, "scan accepted weights")
    for row in ["W12", "W23", "W13"]:
        require(scan["best_by_weight_row"][row]["accepted"] is False, f"scan accepted {row}")
        require(scan["best_by_weight_row"][row]["relative_residual"] >= 0.0, f"scan residual {row}")
    require(scan["observed_data_used_as_selector"] is False, "scan observed selector")
    require(scan["target_fitting_used"] is False, "scan target fit")

    require(gate["status"] == "KCKM_TRACE_ASSEMBLY_RULE_REQUIRED_FOR_WEIGHT_CERTIFICATES", "gate status")
    require(gate["all_domain_inputs_ready"] is True, "domain inputs")
    require(gate["selected_K_CKM_rule_emitted"] is False, "gate K rule")
    require(gate["selected_Pi_CKM_row_certificates"] == 0, "gate row certs")
    require("selected K_CKM trace assembly rule" in gate["missing_rule"], "missing rule text")
    require("near-hit invariant expressions are not row certificates" in gate["why_scan_not_enough"], "near-hit guard")
    require(gate["observed_data_used_as_selector"] is False, "gate observed selector")
    require(gate["target_fitting_used"] is False, "gate target fit")

    require(decision["status"] == "ECKM_DOMAIN_7_OF_8_FINAL_WEIGHT_CERTIFICATES_OPEN", "decision status")
    require(decision["domain_readiness"] == "7/8", "domain readiness")
    require(decision["available_eckm_trace_invariant_scan_executed"] is True, "decision scan")
    require(decision["selected_K_CKM_rule_emitted"] is False, "decision K rule")
    require(decision["accepted_weight_rows"] == 0, "decision weights")
    require(decision["next_required_artifact"] == NEXT, "decision next")
    for key in [
        "CKM_angle_magnitudes_derived_exact",
        "Jarlskog_source_derived_without_measured_angles",
        "true_SM_equivalence_closed",
        "full_no_knob_closure_closed",
        "observed_data_used_as_selector",
        "target_fitting_used",
    ]:
        require(decision[key] is False, f"decision overclaim: {key}")

    nums = data["key_numbers"]
    require(nums["domain_readiness"] == "7/8", "key readiness")
    require(nums["accepted_eckm_weight_rows"] == 0, "key accepted")
    require(abs(nums["required_q448_weights"]["W12"] - 1.41236734693301) < 1e-12, "W12")

    require(data["closure_claimed"] is False, "closure overclaimed")
    require(data["observed_data_used_as_selector"] is False, "observed selector")
    require(data["observed_data_used_for_postcheck"] is True, "postcheck")
    require(data["target_fitting_used"] is False, "target fitting")
    require(cert["selected_K_CKM_rule_emitted"] is False, "cert K rule")
    require(cert["accepted_weight_rows"] == 0, "cert weights")
    require(cert["closure_claimed"] is False, "cert closure")
    require("domain readiness = 7/8" in note, "note readiness")
    require("accepted W rows  = 0/3" in note, "note weights")
    require(NEXT in note, "note next")

    print(f"PASS {CANDIDATE.name}: {STATUS}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
