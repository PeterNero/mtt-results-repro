"""Audit CKM correction-functional domain closure."""

from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SLUG = "selected_ckmanglecorrectionfunctional_or_exactflavorobservableclosure"
BUILDER = ROOT / "scripts" / f"build_{SLUG}.py"
CANDIDATE = ROOT / "candidate_data" / f"{SLUG}.candidate.json"
PACKET_DIR = ROOT / "candidate_data" / SLUG
DOMAIN = PACKET_DIR / "dynamic_c1_correction_domain.packet.json"
REQUIREMENT = PACKET_DIR / "ckm_correction_factor_requirement.packet.json"
SCAN = PACKET_DIR / "source_native_correction_candidate_scan.packet.json"
DECISION = PACKET_DIR / "exact_correction_acceptance_decision.packet.json"
CERT = ROOT / "certificates" / f"{SLUG}_certificate.json"
NOTE = ROOT / "proof_corpus" / "MTT_Selected_CKMAngleCorrectionFunctional_or_ExactFlavorObservableClosure_v1.md"

STATUS = "MTT_SELECTED_CKMANGLECORRECTIONFUNCTIONAL_DYNAMICC1_DOMAIN_CLOSED_EXACT_ROWS_OPEN"
NEXT = "MTT_Selected_CKMSectorPairProjectionRows_or_HonestFlavorGalerkinExecution_v1"


def load(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def require(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)


def main() -> int:
    subprocess.run([sys.executable, str(BUILDER)], cwd=ROOT, check=True)

    data = load(CANDIDATE)
    domain = load(DOMAIN)
    requirement = load(REQUIREMENT)
    scan = load(SCAN)
    decision = load(DECISION)
    cert = load(CERT)
    note = NOTE.read_text(encoding="utf-8")

    require(data["status"] == STATUS, "candidate status mismatch")
    require(cert["status"] == STATUS, "cert status mismatch")
    require(data["next_required_artifact"] == NEXT, "candidate next mismatch")
    require(cert["next_required_artifact"] == NEXT, "cert next mismatch")
    require(data["theorem"]["proved"] is True, "theorem not proved")
    require(data["theorem"]["name"] == "CKMAngleCorrectionFunctionalDynamicC1DomainTheorem", "theorem name")
    require(cert["theorem_proved"] is True, "cert theorem not proved")

    closure = data["closure_decision"]
    for key in [
        "dynamic_c1_correction_domain_closed",
        "Step10_route_A_source_rule_imported",
        "VSD01_primitive_rows_imported",
        "required_correction_factors_identified",
        "source_native_near_hit_scan_executed",
    ]:
        require(closure[key] is True, f"missing closed/imported flag: {key}")
    require(closure["selected_sector_pair_projection_rows"] == 0, "sector-pair rows overaccepted")
    require(closure["accepted_exact_correction_rows"] == 0, "exact corrections overaccepted")
    require(closure["accepted_no_knob_CKM_angle_rows"] == 0, "no-knob angle rows overaccepted")
    for key in [
        "CKM_angle_magnitudes_derived_exact",
        "Jarlskog_source_derived_without_measured_angles",
        "true_SM_equivalence_closed",
        "full_no_knob_closure_closed",
    ]:
        require(closure[key] is False, f"overclaim: {key}")

    nums = data["key_numbers"]
    require(nums["A_transpose_A"] == [[12.0, 0.0], [0.0, 12.0]], "A^T A mismatch")
    require(nums["A_transpose_b"] == [12.0, 12.0], "A^T b mismatch")
    require(nums["deltaTheta_C1"] == [1.0, 1.0], "deltaTheta mismatch")
    require(abs(nums["phase_R_Z_frobenius_norm_sq"] - 4.0) < 1e-12, "phase norm mismatch")
    require(abs(nums["shift_R_X_frobenius_norm_sq"] - 2.0) < 1e-12, "shift norm mismatch")
    require(nums["dynamic_rank"] == 2, "dynamic rank mismatch")

    require(domain["status"] == "DYNAMIC_C1_CORRECTION_DOMAIN_CLOSED", "domain status")
    require(domain["source_owner"] == "PhysicalPhiFinC1ActionSource", "domain owner")
    require(domain["same_branch"] is True, "domain same branch")
    require(domain["route_a_source_rule_closed"] is True, "Route A not closed")
    require(domain["dynamic_phi_fin_c1_payload_emitted"] is True, "dynamic payload missing")
    require(domain["primitive_rows_exact"] is True, "primitive rows not exact")
    require(domain["formal_110_rows_executed"] is True, "formal rows not executed")
    require(domain["rank"] == 2, "domain rank")
    require(domain["row_counts"]["primitive_kernel_rows"] == 72, "primitive count")
    require(domain["row_counts"]["formal_110_total_rows"] == 110, "formal count")
    require("sector-pair projection functional Pi_CKM^12" in domain["missing_for_exact_CKM_corrections"], "missing Pi12 gap")
    require(domain["target_fitting_used"] is False, "domain target fit")
    require(domain["observed_data_used_as_selector"] is False, "domain observed selector")

    required = requirement["required_if_matching_measured_replay"]
    require(requirement["status"] == "THREE_UNEQUAL_CORRECTION_FACTORS_IDENTIFIED_FOR_EXACT_REPLAY", "requirement status")
    require(requirement["all_three_factors_distinct"] is True, "corrections should be distinct")
    require(abs(required["s12"] - 1.0031526056851183) < 1e-15, "C12 mismatch")
    require(abs(required["s23"] - 1.0152451887355003) < 1e-15, "C23 mismatch")
    require(abs(required["s13"] - 1.0515803740935308) < 1e-15, "C13 mismatch")
    require("multiplicative corrections backsolved from measured CKM angles" in requirement["forbidden_source_interpretation"], "forbidden source missing")

    require(scan["status"] == "DIAGNOSTIC_NEAR_HIT_SCAN_EXECUTED_NO_ACCEPTED_ROWS", "scan status")
    require(scan["candidate_count"] > 100, "scan too small")
    require(scan["accepted_exact_correction_rows"] == 0, "scan overaccepted rows")
    for row in ["s12", "s23", "s13"]:
        require(scan["best_by_ckm_row"][row]["accepted"] is False, f"scan accepted {row}")
        require(scan["best_by_ckm_row"][row]["relative_residual"] >= 0.0, f"scan residual {row}")
    require(scan["target_fitting_used"] is False, "scan target fit")
    require(scan["observed_data_used_as_selector"] is False, "scan observed selector")

    require(decision["status"] == "DOMAIN_CLOSED_EXACT_CORRECTION_ROWS_REJECTED_UNTIL_SECTOR_PAIR_EVALUATORS", "decision status")
    require(decision["dynamic_c1_correction_domain_closed"] is True, "decision domain")
    require(decision["required_correction_factors_identified"] is True, "decision requirement")
    require(decision["source_native_scan_executed"] is True, "decision scan")
    require(decision["accepted_exact_correction_rows"] == 0, "decision exact rows")
    require(decision["selected_sector_pair_projection_rows"] == 0, "decision projection rows")
    require(decision["next_required_artifact"] == NEXT, "decision next")
    for key in [
        "CKM_angle_magnitudes_derived_exact",
        "Jarlskog_source_derived_without_measured_angles",
        "true_SM_equivalence_closed",
        "full_no_knob_closure_closed",
        "target_fitting_used",
        "observed_data_used_as_selector",
    ]:
        require(decision[key] is False, f"decision overclaim: {key}")

    require(data["closure_claimed"] is False, "closure overclaimed")
    require(data["observed_data_used_as_selector"] is False, "observed selector used")
    require(data["observed_data_used_for_postcheck"] is True, "postcheck flag missing")
    require(data["target_fitting_used"] is False, "target fitting used")
    require(cert["dynamic_c1_correction_domain_closed"] is True, "cert domain")
    require(cert["accepted_exact_correction_rows"] == 0, "cert exact rows")
    require(cert["selected_sector_pair_projection_rows"] == 0, "cert projection rows")
    require(cert["closure_claimed"] is False, "cert closure overclaimed")
    require("Accepted exact CKM correction rows: `0`" in note, "note boundary")
    require(NEXT in note, "note next")

    print(f"PASS {CANDIDATE.name}: {STATUS}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
