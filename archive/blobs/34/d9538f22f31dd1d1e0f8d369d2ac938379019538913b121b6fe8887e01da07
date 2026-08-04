"""Audit CKM sector-pair projection-row contract."""

from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SLUG = "selected_ckmsectorpairprojectionrows_or_honestflavorgalerkinexecution"
BUILDER = ROOT / "scripts" / f"build_{SLUG}.py"
CANDIDATE = ROOT / "candidate_data" / f"{SLUG}.candidate.json"
PACKET_DIR = ROOT / "candidate_data" / SLUG
CONTRACT = PACKET_DIR / "sector_pair_projection_contract.packet.json"
WEIGHTS = PACKET_DIR / "required_q448_sector_pair_weights.packet.json"
BASIS = PACKET_DIR / "finite_source_basis_projection_attempt.packet.json"
DECISION = PACKET_DIR / "sector_pair_projection_acceptance_decision.packet.json"
CERT = ROOT / "certificates" / f"{SLUG}_certificate.json"
NOTE = ROOT / "proof_corpus" / "MTT_Selected_CKMSectorPairProjectionRows_or_HonestFlavorGalerkinExecution_v1.md"

STATUS = "MTT_SELECTED_CKMSECTORPAIR_PROJECTION_CONTRACT_CLOSED_WEIGHT_SOURCE_ROWS_OPEN"
NEXT = "MTT_Selected_CKMSectorPairWeightSourceTheorem_or_FullFlavorGalerkinRun_v1"


def load(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def require(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)


def main() -> int:
    subprocess.run([sys.executable, str(BUILDER)], cwd=ROOT, check=True)

    data = load(CANDIDATE)
    contract = load(CONTRACT)
    weights = load(WEIGHTS)
    basis = load(BASIS)
    decision = load(DECISION)
    cert = load(CERT)
    note = NOTE.read_text(encoding="utf-8")

    require(data["status"] == STATUS, "candidate status mismatch")
    require(cert["status"] == STATUS, "cert status mismatch")
    require(data["next_required_artifact"] == NEXT, "candidate next mismatch")
    require(cert["next_required_artifact"] == NEXT, "cert next mismatch")
    require(data["theorem"]["proved"] is True, "theorem not proved")
    require(data["theorem"]["name"] == "CKMSectorPairProjectionRowContractTheorem", "theorem name")
    require(cert["theorem_proved"] is True, "cert theorem")

    closure = data["closure_decision"]
    for key in [
        "q448_sector_pair_projection_contract_closed",
        "required_weight_obligation_identified",
        "finite_source_basis_projection_attempt_executed",
    ]:
        require(closure[key] is True, f"missing closed flag: {key}")
    require(closure["selected_weight_rows"] == 0, "selected weight rows overaccepted")
    require(closure["accepted_exact_ckm_correction_rows"] == 0, "exact CKM rows overaccepted")
    require(closure["accepted_no_knob_CKM_angle_rows"] == 0, "no-knob rows overaccepted")
    for key in [
        "CKM_angle_magnitudes_derived_exact",
        "Jarlskog_source_derived_without_measured_angles",
        "true_SM_equivalence_closed",
        "full_no_knob_closure_closed",
    ]:
        require(closure[key] is False, f"overclaim: {key}")

    require(contract["status"] == "Q448_SECTOR_PAIR_PROJECTION_CONTRACT_CLOSED", "contract status")
    require(contract["normalization"] == "C_ij = 1 + W_ij/448", "normalization mismatch")
    require(contract["selected_inputs_already_available"]["selected_Delta_v"] is True, "Delta_v missing")
    require(contract["selected_inputs_already_available"]["dynamic_C1_domain"] is True, "dynamic domain missing")
    require(contract["sector_pair_rows"]["s12"]["projection_row"] == "Pi_CKM^12", "Pi12")
    require(contract["sector_pair_rows"]["s23"]["projection_row"] == "Pi_CKM^23", "Pi23")
    require(contract["sector_pair_rows"]["s13"]["projection_row"] == "Pi_CKM^13", "Pi13")
    require(contract["contract_does_not_close"] == "the selected numeric source values W12,W23,W13", "contract boundary")
    require(contract["observed_data_used_as_selector"] is False, "contract observed selector")
    require(contract["target_fitting_used"] is False, "contract target fit")

    require(weights["status"] == "REQUIRED_WEIGHT_OBLIGATION_IDENTIFIED_NOT_SOURCE_VALUES", "weights status")
    q448 = weights["q448_weights_if_matching_measured_replay"]
    require(abs(q448["W12"] - 1.41236734693301) < 1e-12, "W12 mismatch")
    require(abs(q448["W23"] - 6.829844553504131) < 1e-12, "W23 mismatch")
    require(abs(q448["W13"] - 23.10800759390179) < 1e-12, "W13 mismatch")
    require(weights["all_three_weights_distinct"] is True, "weights not distinct")
    require(weights["observed_data_used_as_selector"] is False, "weights observed selector")
    require(weights["observed_data_used_for_postcheck"] is True, "weights postcheck")

    require(basis["status"] == "FINITE_SOURCE_BASIS_ATTEMPT_EXECUTED_NO_ACCEPTED_WEIGHT_ROWS", "basis status")
    require(basis["candidate_count"] > 1000, "basis attempt too small")
    require(basis["accepted_weight_rows"] == 0, "basis accepted weights")
    require(basis["accepted_exact_ckm_correction_rows"] == 0, "basis accepted corrections")
    for row in ["W12", "W23", "W13"]:
        require(basis["best_by_sector_pair"][row]["accepted"] is False, f"basis accepted {row}")
        require(basis["best_by_sector_pair"][row]["relative_residual"] >= 0.0, f"basis residual {row}")
    require(basis["observed_data_used_as_selector"] is False, "basis observed selector")
    require(basis["target_fitting_used"] is False, "basis target fit")

    require(decision["status"] == "PROJECTION_CONTRACT_CLOSED_SELECTED_WEIGHT_ROWS_REMAIN_OPEN", "decision status")
    require(decision["q448_sector_pair_projection_contract_closed"] is True, "decision contract")
    require(decision["required_weight_obligation_identified"] is True, "decision weights")
    require(decision["finite_source_basis_projection_attempt_executed"] is True, "decision basis")
    require(decision["selected_weight_rows"] == 0, "decision selected weights")
    require(decision["accepted_exact_ckm_correction_rows"] == 0, "decision corrections")
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

    require(data["closure_claimed"] is False, "closure overclaimed")
    require(data["observed_data_used_as_selector"] is False, "observed selector")
    require(data["observed_data_used_for_postcheck"] is True, "postcheck missing")
    require(data["target_fitting_used"] is False, "target fitting")
    require(cert["q448_sector_pair_projection_contract_closed"] is True, "cert contract")
    require(cert["selected_weight_rows"] == 0, "cert selected weights")
    require(cert["accepted_exact_ckm_correction_rows"] == 0, "cert corrections")
    require(cert["closure_claimed"] is False, "cert closure")
    require("Accepted selected weight rows: `0/3`" in note, "note boundary")
    require(NEXT in note, "note next")

    print(f"PASS {CANDIDATE.name}: {STATUS}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
