"""Audit Pi_CKM denominator provenance reduction."""

from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SLUG = "selected_pickmsourcederivationclauses_or_ckmpredictionupgrade"
BUILDER = ROOT / "scripts" / f"build_{SLUG}.py"
CANDIDATE = ROOT / "candidate_data" / f"{SLUG}.candidate.json"
PACKET_DIR = ROOT / "candidate_data" / SLUG
DENOMS = PACKET_DIR / "pickm_denominator_provenance_clauses.packet.json"
NUMERATORS = PACKET_DIR / "pickm_numerator_projector_weight_clauses.packet.json"
GATE = PACKET_DIR / "ckm_prediction_upgrade_after_denominator_closure.packet.json"
CERT = ROOT / "certificates" / f"{SLUG}_certificate.json"
NOTE = ROOT / "proof_corpus" / "MTT_Selected_PiCKMSourceDerivationClauses_or_CKMPredictionUpgrade_v1.md"

STATUS = "MTT_SELECTED_PICKM_SOURCE_DERIVATION_DENOMINATORS_CLOSED_NUMERATOR_PROJECTORS_OPEN"
NEXT = "MTT_Selected_PiCKMProjectorNumeratorRule_or_CKMWeightRowCertificates_v1"


def load(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def require(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)


def main() -> int:
    subprocess.run([sys.executable, str(BUILDER)], cwd=ROOT, check=True)

    data = load(CANDIDATE)
    denoms = load(DENOMS)
    numerators = load(NUMERATORS)
    gate = load(GATE)
    cert = load(CERT)
    note = NOTE.read_text(encoding="utf-8")

    require(data["status"] == STATUS, "candidate status mismatch")
    require(cert["status"] == STATUS, "cert status mismatch")
    require(data["next_required_artifact"] == NEXT, "candidate next mismatch")
    require(cert["next_required_artifact"] == NEXT, "cert next mismatch")
    require(data["theorem"]["proved"] is True, "theorem not proved")
    require(data["theorem"]["name"] == "PiCKMDenominatorProvenanceReductionTheorem", "theorem name")
    require(cert["theorem_proved"] is True, "cert theorem")

    require(denoms["status"] == "PICKM_DENOMINATOR_PROVENANCE_CLAUSES_CLOSED", "denom status")
    require(denoms["all_denominator_clauses_closed"] is True, "denoms not closed")
    clauses = denoms["clauses"]
    require(clauses["D12_six_arrow_normalization"]["denominator"] == 6, "D12 denom")
    require(clauses["D23_eight_slot_normalization"]["denominator"] == 8, "D23 denom")
    require(clauses["D13_eighteen_pure_weyl_normalization"]["denominator"] == 18, "D13 denom")
    for clause in clauses.values():
        require(clause["closed"] is True, "denom clause not closed")

    require(numerators["status"] == "PICKM_NUMERATOR_PROJECTOR_WEIGHT_RULE_OPEN", "numerator status")
    require(numerators["accepted_weight_rows"] == 0, "numerator weights")
    require(len(numerators["open_clauses"]) == 3, "open numerator clauses")
    for clause in numerators["open_clauses"].values():
        require(clause["closed"] is False, "numerator overclosed")

    require(gate["status"] == "CKM_PREDICTION_UPGRADE_REDUCED_TO_PROJECTOR_NUMERATOR_RULE", "gate status")
    require(gate["denominator_provenance_closed"] is True, "gate denom")
    require(gate["numerator_projector_rule_closed"] is False, "gate numerator")
    require(gate["accepted_weight_rows"] == 0, "gate weights")
    require(gate["accepted_exact_ckm_correction_rows"] == 0, "gate corrections")
    require(gate["accepted_no_knob_ckm_angle_rows"] == 0, "gate CKM")
    require(gate["next_required_artifact"] == NEXT, "gate next")

    closure = data["closure_decision"]
    require(closure["Pi_CKM_denominator_provenance_closed"] is True, "closure denom")
    require(closure["Pi_CKM_numerator_projector_rule_closed"] is False, "closure numerator")
    require(closure["selected_Pi_CKM_row_certificates"] == 0, "closure Pi certs")
    require(closure["accepted_weight_rows"] == 0, "closure weights")
    require(closure["accepted_exact_ckm_correction_rows"] == 0, "closure corrections")
    require(closure["accepted_no_knob_CKM_angle_rows"] == 0, "closure CKM")
    require(closure["true_SM_equivalence_closed"] is False, "true SM overclaim")
    require(closure["full_no_knob_closure_closed"] is False, "no-knob overclaim")

    nums = data["key_numbers"]
    require(nums["closed_denominators"] == {"W12": 6, "W23": 8, "W13": 18}, "closed denom map")
    require(nums["closed_denominator_clauses"] == 3, "closed denom count")
    require(nums["open_numerator_projector_clauses"] == 3, "open numerator count")
    require(nums["accepted_eckm_weight_rows"] == 0, "key accepted")
    require(data["closure_claimed"] is False, "closure claimed")
    require(data["observed_data_used_as_selector"] is False, "observed selector")
    require(data["target_fitting_used"] is False, "target fitting")
    require(cert["Pi_CKM_denominator_provenance_closed"] is True, "cert denom")
    require(cert["Pi_CKM_numerator_projector_rule_closed"] is False, "cert numerator")
    require(cert["selected_Pi_CKM_row_certificates"] == 0, "cert Pi certs")
    require(cert["closure_claimed"] is False, "cert closure")
    require("W12 denominator 6" in note, "note W12")
    require("W23 denominator 8" in note, "note W23")
    require("W13 denominator 18" in note, "note W13")
    require(NEXT in note, "note next")

    print(f"PASS {CANDIDATE.name}: {STATUS}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
