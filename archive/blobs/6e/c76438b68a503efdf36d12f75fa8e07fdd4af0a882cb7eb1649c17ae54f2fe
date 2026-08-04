"""Audit first same-source connection-field emission attempt."""

from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "candidate_data"
CERTS = ROOT / "certificates"
CORPUS = ROOT / "proof_corpus"
BUILDER = ROOT / "scripts" / "build_selected_firstsamesourceconnectionfieldemission_or_directhkrow.py"

SLUG = "selected_firstsamesourceconnectionfieldemission_or_directhkrow"
PACKET_DIR = DATA / SLUG
CANDIDATE = DATA / f"{SLUG}.candidate.json"
CERT = CERTS / f"{SLUG}_certificate.json"
NOTE = CORPUS / "MTT_Selected_FirstSameSourceConnectionFieldEmission_or_DirectHKRow_v1.md"
FIELD_SCAN = PACKET_DIR / "first_field_candidate_scan.packet.json"
VALIDATOR = PACKET_DIR / "first_field_validator.packet.json"
NEXT_CONTRACT = PACKET_DIR / "next_bn27_sector_transfer_or_sourceid_certificate_contract.packet.json"

STATUS = (
    "MTT_SELECTED_FIRSTSAMESOURCECONNECTIONFIELDEMISSION_OR_DIRECTHKROW_"
    "BUILT_RTHETA_HYM_CLUE_REJECTED_BN27_FIELD_OPEN"
)
NEXT = "MTT_Selected_BN27SectorTransferConnectionRepresentative_or_SourceIDCertificate_v1"


def load(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def require(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)


def main() -> int:
    subprocess.run([sys.executable, str(BUILDER)], cwd=ROOT, check=True)

    candidate = load(CANDIDATE)
    cert = load(CERT)
    scan = load(FIELD_SCAN)
    validator = load(VALIDATOR)
    next_contract = load(NEXT_CONTRACT)
    note = NOTE.read_text(encoding="utf-8")

    require(candidate["status"] == STATUS, "candidate status mismatch")
    require(cert["status"] == STATUS, "certificate status mismatch")
    require(candidate["next_required_artifact"] == NEXT, "candidate next mismatch")
    require(cert["next_required_artifact"] == NEXT, "certificate next mismatch")
    require(next_contract["next_required_artifact"] == NEXT, "next contract mismatch")
    require(candidate["theorem"]["proved"] is True, "theorem not proved")
    require(cert["theorem_proved"] is True, "certificate theorem flag missing")

    for payload in [candidate, cert, scan, validator, next_contract]:
        require(payload["closure_claimed"] is True, "closure boundary missing")
        require(payload["observed_data_used_as_selector"] is False, "observed selector used")
        require(payload["target_fitting_used"] is False, "target fitting used")

    decision = candidate["closure_decision"]
    require(decision["first_field_attempted"] is True, "first field not attempted")
    require(decision["rtheta_diagonal_HYM_clue_found"] is True, "HYM clue missing")
    require(decision["rtheta_diagonal_HYM_accepted_for_rtheta_subgate"] is True, "Rtheta clue not accepted")
    require(decision["accepted_first_field_count"] == 0, "first field overaccepted")
    require(decision["accepted_same_source_connection_value_count_after_attempt"] == 0, "table values overaccepted")
    for key in [
        "rtheta_diagonal_HYM_promoted_to_BN27_field",
        "transition_or_connection_representative_emitted",
        "rank2_to_sector_transfer_closed",
        "actual_QaSU3_operator_packet_promoted",
        "direct_H_K_row_emitted",
        "full_no_knob_closed",
        "true_SM_equivalence_closed",
    ]:
        require(decision[key] is False, f"overclosed: {key}")
    require(decision["selected_connection_witness_values_absent"] is True, "connection witness absence not preserved")

    require(
        scan["status"] == "RTHETA_DIAGONAL_HYM_CLUE_FOUND_BN27_FIELD_NOT_ACCEPTED",
        "scan status mismatch",
    )
    require(scan["target_field"] == "transition_or_connection_representative", "target field mismatch")
    require(scan["accepted_transition_or_connection_representative"] is False, "field overaccepted")
    rtheta = scan["candidate_sources"]["rtheta_diagonal_hym_representative"]
    require(rtheta["value"] == "A_diag = d u * T3 in the selected diagonal End0 lane", "HYM value mismatch")
    require(rtheta["selected_for_rtheta_pi_subgate"] is True, "Rtheta subgate clue missing")
    require(rtheta["accepted_for_bn27_transition_field"] is False, "Rtheta clue overpromoted")
    require(
        scan["candidate_sources"]["hym_first_solve"]["rank2_to_sector_transfer_closed"] is False,
        "rank2 transfer overclosed",
    )
    require(
        scan["candidate_sources"]["u1y_connection_witness"]["selected_connection_witness_values_absent"] is True,
        "U1/Y witness absence lost",
    )

    require(validator["status"] == "VALIDATOR_EXECUTED_FIRST_FIELD_ACCEPTED0", "validator status mismatch")
    require(validator["accepted_first_field_count"] == 0, "validator overaccepted")
    require(validator["support_clues_promoted_to_table_values"] == 0, "support clues promoted")
    require(validator["rtheta_diagonal_HYM_clue_recorded"] is True, "clue not recorded")
    require(validator["direct_H_K_row_emitted"] is False, "direct H K overemitted")
    for reason in [
        "rank2-to-sector transfer closed false",
        "actual Qa/SU3 operator packet promoted false",
        "selected connection witness values absent in U1/Y Route-C packet",
    ]:
        require(reason in validator["why_rtheta_clue_not_promoted"], f"missing reason: {reason}")

    require(
        next_contract["status"] == "NEXT_IS_BN27_TRANSFERRED_CONNECTION_REPRESENTATIVE_OR_SOURCEID_CERTIFICATE",
        "next contract status mismatch",
    )
    require(any("rank2-to-sector transfer" in item for item in next_contract["must_emit"]), "rank2 transfer target missing")
    require(any("BN27 transition/connection representative" in item for item in next_contract["must_emit"]), "BN27 field target missing")
    require(next_contract["direct_exit"] == "K_threshold.Omega_H.lambda", "direct exit mismatch")

    require("Accepted first-field rows: `0`" in note, "note missing first-field count")
    require(NEXT in note, "note missing next artifact")

    print("First same-source connection-field audit passed")
    print(json.dumps({"candidate": str(CANDIDATE.relative_to(ROOT)), "status": STATUS}, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
