"""Audit BN27 sector-transfer/source-id certificate frontier."""

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
BUILDER = ROOT / "scripts" / "build_selected_bn27sectortransferconnectionrepresentative_or_sourceidcertificate.py"

SLUG = "selected_bn27sectortransferconnectionrepresentative_or_sourceidcertificate"
PACKET_DIR = DATA / SLUG
CANDIDATE = DATA / f"{SLUG}.candidate.json"
CERT = CERTS / f"{SLUG}_certificate.json"
NOTE = CORPUS / "MTT_Selected_BN27SectorTransferConnectionRepresentative_or_SourceIDCertificate_v1.md"
TRANSFER_SPLIT = PACKET_DIR / "stationary_vs_bn27_transfer_split.packet.json"
SOURCEID_GATE = PACKET_DIR / "sourceid_certificate_gate.packet.json"
NEXT_CONTRACT = PACKET_DIR / "next_direct_source_emission_or_full_connection_tables_contract.packet.json"

STATUS = (
    "MTT_SELECTED_BN27SECTORTRANSFERCONNECTIONREPRESENTATIVE_OR_SOURCEIDCERTIFICATE_"
    "BUILT_DIRECT_SOURCE_THEOREM_SHORTEST_CONNECTION_VALUES_OPEN"
)
NEXT = "MTT_Selected_SQaSU3BN27_SelectedSourceEmissionTheorem_or_FullConnectionTables_v1"


def load(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def require(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)


def main() -> int:
    subprocess.run([sys.executable, str(BUILDER)], cwd=ROOT, check=True)

    candidate = load(CANDIDATE)
    cert = load(CERT)
    transfer = load(TRANSFER_SPLIT)
    sourceid = load(SOURCEID_GATE)
    next_contract = load(NEXT_CONTRACT)
    note = NOTE.read_text(encoding="utf-8")

    require(candidate["status"] == STATUS, "candidate status mismatch")
    require(cert["status"] == STATUS, "certificate status mismatch")
    require(candidate["next_required_artifact"] == NEXT, "candidate next mismatch")
    require(cert["next_required_artifact"] == NEXT, "certificate next mismatch")
    require(next_contract["next_required_artifact"] == NEXT, "next contract mismatch")
    require(candidate["theorem"]["proved"] is True, "theorem not proved")
    require(cert["theorem_proved"] is True, "certificate theorem flag missing")

    for payload in [candidate, cert, transfer, sourceid, next_contract]:
        require(payload["closure_claimed"] is True, "closure boundary missing")
        require(payload["observed_data_used_as_selector"] is False, "observed selector used")
        require(payload["target_fitting_used"] is False, "target fitting used")

    decision = candidate["closure_decision"]
    require(decision["stationary_Rtheta_transfer_imported_as_support"] is True, "stationary support missing")
    require(decision["Rtheta_Pi_domain_closed"] is True, "Rtheta Pi closure lost")
    require(decision["direct_source_theorem_ranked_first"] is True, "direct route not ranked first")
    require(decision["direct_source_theorem_support_count"] == 6, "direct support count mismatch")
    require(decision["direct_source_theorem_required_count"] == 6, "direct required count mismatch")
    require(decision["direct_source_theorem_open_count"] == 6, "direct open count mismatch")
    require(decision["connection_table_support_count"] == 0, "connection table support overcounted")
    require(decision["connection_table_required_count"] == 8, "connection table required count mismatch")
    for key in [
        "BN27_operator_transfer_closed",
        "End0_functor_values_extracted",
        "rank2_to_sector_transfer_closed",
        "actual_QaSU3_operator_packet_promoted",
        "source_id_certificate_closed",
        "connection_tables_closed",
        "transition_or_connection_representative_emitted",
        "direct_H_K_row_emitted",
        "full_no_knob_closed",
        "true_SM_equivalence_closed",
    ]:
        require(decision[key] is False, f"overclosed: {key}")

    require(
        transfer["status"] == "STATIONARY_RTHETA_TRANSFER_CLOSED_BN27_OPERATOR_TRANSFER_OPEN",
        "transfer status mismatch",
    )
    require(transfer["stationary_transfer_closed"] is True, "stationary transfer not imported")
    require(transfer["bn27_operator_transfer_closed"] is False, "BN27 operator transfer overclosed")
    require(transfer["end0_functor_values_extracted"] is False, "End0 values overextracted")
    require(transfer["rank2_to_sector_transfer_closed"] is False, "rank2 transfer overclosed")
    require(transfer["actual_QaSU3_operator_packet_promoted"] is False, "Qa/SU3 overpromoted")
    require("operator-level rhoE/DE/Riesz/Green/dotD" in transfer["decision"], "operator distinction missing")

    require(
        sourceid["status"] == "DIRECT_SOURCE_THEOREM_RANKED_FIRST_SUPPORT6_OPEN6",
        "sourceid status mismatch",
    )
    require(sourceid["source_id_certificate_closed"] is False, "source-id certificate overclosed")
    require(sourceid["direct_source_theorem_closed"] is False, "direct theorem overclosed")
    require(sourceid["connection_tables_closed"] is False, "connection tables overclosed")
    direct = sourceid["direct_source_emission_route"]
    connection = sourceid["connection_tables_route"]
    require(direct["support_statement_count"] == direct["required_statement_count"] == 6, "direct count mismatch")
    require(direct["open_statement_count"] == 6, "direct open count mismatch")
    require(connection["support_table_count"] == 0, "connection support overcounted")
    require(connection["required_table_count"] == 8, "connection required count mismatch")
    require(sourceid["minimal_direct_theorem"]["name"] == "S_QaSU3_BN27_SelectedSourceEmissionTheorem", "direct theorem name mismatch")

    require(
        next_contract["status"] == "NEXT_IS_DIRECT_SOURCE_EMISSION_OR_FULL_CONNECTION_TABLES",
        "next status mismatch",
    )
    require(next_contract["primary_route"] == "S_QaSU3_BN27_SelectedSourceEmissionTheorem", "primary route mismatch")
    require(len(next_contract["primary_must_state"]) == 6, "primary statements mismatch")
    require(len(next_contract["fallback_must_emit"]) == 8, "fallback emits mismatch")
    for guard in [
        "stationary R_theta transfer as BN27 operator transfer",
        "A_diag=du*T3 as full BN27 connection table row",
        "branch certificate alone as source ownership",
    ]:
        require(guard in next_contract["must_not_use"], f"missing guard: {guard}")

    require("BN27 operator transfer closed: `false`" in note, "note missing BN27 transfer state")
    require(NEXT in note, "note missing next artifact")

    print("BN27 sector-transfer/source-id audit passed")
    print(json.dumps({"candidate": str(CANDIDATE.relative_to(ROOT)), "status": STATUS}, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
