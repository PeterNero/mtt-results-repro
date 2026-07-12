"""Audit Pi_CKM numerator/projector corpus clue scan."""

from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
BUILDER = ROOT / "scripts" / "build_selected_pickmprojectornumeratorrule_or_ckmweightrowcertificates.py"
CANDIDATE = ROOT / "candidate_data" / "selected_pickmprojectornumeratorrule_or_ckmweightrowcertificates.candidate.json"
SCAN = (
    ROOT
    / "candidate_data"
    / "selected_pickmprojectornumeratorrule_or_ckmweightrowcertificates"
    / "pickm_numerator_corpus_clue_scan.packet.json"
)
GATE = (
    ROOT
    / "candidate_data"
    / "selected_pickmprojectornumeratorrule_or_ckmweightrowcertificates"
    / "pickm_branch_retention_principle_gate.packet.json"
)
CERT = ROOT / "certificates" / "selected_pickmprojectornumeratorrule_or_ckmweightrowcertificates_certificate.json"
NOTE = ROOT / "proof_corpus" / "MTT_Selected_PiCKMProjectorNumeratorRule_or_CKMWeightRowCertificates_v1.md"

STATUS = "MTT_SELECTED_PICKM_NUMERATOR_CORPUS_CLUE_SCAN_EXECUTED_BRANCH_RULE_OPEN"
NEXT = "MTT_Selected_PiCKMNumeratorBranchRetentionPrinciple_or_WeightRows_v1"


def require(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)


def load(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def main() -> int:
    subprocess.run([sys.executable, str(BUILDER)], cwd=ROOT, check=True)

    candidate = load(CANDIDATE)
    scan = load(SCAN)
    gate = load(GATE)
    cert = load(CERT)
    note = NOTE.read_text(encoding="utf-8")

    require(candidate["status"] == STATUS, "candidate status mismatch")
    require(candidate["next_required_artifact"] == NEXT, "candidate next artifact mismatch")
    require(candidate["theorem"]["name"] == "PiCKMNumeratorCorpusClueScanTheorem", "theorem name mismatch")
    require(candidate["theorem"]["proved"] is True, "scan theorem not proved")
    require(candidate["closure_claimed"] is False, "candidate overclaims closure")
    require(candidate["observed_data_used_as_selector"] is False, "observed selector used")
    require(candidate["target_fitting_used"] is False, "target fitting used")

    closure = candidate["closure_decision"]
    require(closure["Pi_CKM_numerator_corpus_scan_executed"] is True, "scan not executed")
    require(closure["branch_retention_principle_defined"] is True, "branch gate not defined")
    require(closure["branch_retention_principle_proved"] is False, "branch principle overproved")
    require(closure["selected_Pi_CKM_row_certificates"] == 0, "row certificates overemitted")
    require(closure["accepted_weight_rows"] == 0, "weight rows overaccepted")
    require(closure["true_SM_equivalence_closed"] is False, "true SM overclosed")

    key_numbers = candidate["key_numbers"]
    require(key_numbers["strong_or_medium_numerator_clue_groups"] == 3, "clue group count mismatch")
    require(key_numbers["accepted_eckm_weight_rows"] == 0, "accepted E_CKM rows mismatch")
    require(key_numbers["remaining_branch_retention_clauses"] == 3, "remaining branch clauses mismatch")

    require(scan["status"] == "PICKM_NUMERATOR_CORPUS_CLUE_SCAN_EXECUTED_NO_ROW_CERTIFICATES", "scan status mismatch")
    require(all(scan["marker_checks"].values()), "one or more corpus markers missing")
    require(scan["accepted_weight_rows"] == 0, "scan overaccepted weight rows")
    require(scan["accepted_exact_ckm_correction_rows"] == 0, "scan overaccepted CKM correction rows")
    require(scan["accepted_no_knob_ckm_angle_rows"] == 0, "scan overaccepted no-knob CKM rows")

    terms = scan["candidate_terms"]
    require(set(terms) == {
        "N12_five_sine_branches",
        "N23_three_qcos_branches",
        "N13_five_q_plus_three_modulus_branches",
    }, "candidate term set mismatch")
    require(terms["N12_five_sine_branches"]["support_level"].startswith("strong"), "N12 support level mismatch")
    require(terms["N23_three_qcos_branches"]["support_level"].startswith("medium"), "N23 support level mismatch")
    require(terms["N13_five_q_plus_three_modulus_branches"]["support_level"].startswith("strong"), "N13 support level mismatch")
    for name, term in terms.items():
        require(term["accepted"] is False, f"{name} overaccepted")
        require("why_not_closed" in term and term["why_not_closed"], f"{name} missing closure boundary")

    proto = scan["paper_corpus_support"]["protospinor_closure_cost_geometry"]
    require(proto["available"] is True, "protospinor closure-cost support missing")
    require("not the numeric branch counts" in proto["role"], "protospinor role overclaimed")

    require(gate["status"] == "PICKM_BRANCH_RETENTION_PRINCIPLE_REQUIRED", "gate status mismatch")
    require(gate["corpus_clues_are_sufficient_to_define_attempt"] is True, "gate attempt not defined")
    require(gate["corpus_clues_are_sufficient_to_accept_rows"] is False, "gate overaccepts rows")
    require(gate["accepted_weight_rows"] == 0, "gate overaccepted weights")
    require(gate["next_required_artifact"] == NEXT, "gate next artifact mismatch")
    require(len(gate["must_prove"]) == 3, "must_prove clause count mismatch")
    require("five Route-B" in gate["must_prove"][0], "five-branch clause missing")
    require("family/S3" in gate["must_prove"][1], "threefold clause missing")
    require("five dyadic carry rows" in gate["must_prove"][2], "long-bridge clause missing")

    require(cert["status"] == STATUS, "certificate status mismatch")
    require(cert["next_required_artifact"] == NEXT, "certificate next artifact mismatch")
    require(cert["theorem_proved"] is True, "certificate theorem mismatch")
    require(cert["branch_retention_principle_proved"] is False, "certificate overproved branch theorem")
    require(cert["accepted_weight_rows"] == 0, "certificate overaccepted weights")
    require(cert["true_SM_equivalence_closed"] is False, "certificate overclosed true SM")

    for phrase in [
        "Route-B five-slot",
        "family/S3 qutrit",
        "Fu-Yau/Mukai Z7",
        "Accepted CKM weight rows remain `0/3`",
        NEXT,
    ]:
        require(phrase in note, f"note missing {phrase}")

    print(
        json.dumps(
            {
                "audit": "selected_pickmprojectornumeratorrule_or_ckmweightrowcertificates",
                "status": STATUS,
                "accepted_weight_rows": 0,
                "next_required_artifact": NEXT,
            },
            indent=2,
        )
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
