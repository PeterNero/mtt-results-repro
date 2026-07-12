"""Audit S_QaSU3^BN27 selected-source theorem attempt."""

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
BUILDER = ROOT / "scripts" / "build_selected_sqasu3bn27_selectedsourceemissiontheorem_or_fullconnectiontables.py"

SLUG = "selected_sqasu3bn27_selectedsourceemissiontheorem_or_fullconnectiontables"
PACKET_DIR = DATA / SLUG
CANDIDATE = DATA / f"{SLUG}.candidate.json"
CERT = CERTS / f"{SLUG}_certificate.json"
NOTE = CORPUS / "MTT_Selected_SQaSU3BN27_SelectedSourceEmissionTheorem_or_FullConnectionTables_v1.md"
THEOREM_ATTEMPT = PACKET_DIR / "direct_source_theorem_attempt.packet.json"
CONDITIONAL_REPLAY = PACKET_DIR / "conditional_replay_dag_import.packet.json"
NEXT_CONTRACT = PACKET_DIR / "next_source_emission_principle_or_connection_tables_contract.packet.json"

STATUS = (
    "MTT_SELECTED_SQASU3BN27_SELECTEDSOURCEEMISSIONTHEOREM_OR_FULLCONNECTIONTABLES_"
    "BUILT_CONDITIONAL_REPLAY_READY_SOURCE_PRINCIPLE_OPEN"
)
NEXT = "MTT_Selected_SQaSU3BN27_SourceEmissionPrinciple_or_ConnectionTableFill_v1"


def load(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def require(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)


def main() -> int:
    subprocess.run([sys.executable, str(BUILDER)], cwd=ROOT, check=True)

    candidate = load(CANDIDATE)
    cert = load(CERT)
    attempt = load(THEOREM_ATTEMPT)
    replay = load(CONDITIONAL_REPLAY)
    next_contract = load(NEXT_CONTRACT)
    note = NOTE.read_text(encoding="utf-8")

    require(candidate["status"] == STATUS, "candidate status mismatch")
    require(cert["status"] == STATUS, "certificate status mismatch")
    require(candidate["next_required_artifact"] == NEXT, "candidate next mismatch")
    require(cert["next_required_artifact"] == NEXT, "certificate next mismatch")
    require(next_contract["next_required_artifact"] == NEXT, "next contract mismatch")
    require(candidate["theorem"]["proved"] is True, "theorem not proved")
    require(cert["theorem_proved"] is True, "certificate theorem flag missing")

    for payload in [candidate, cert, attempt, replay, next_contract]:
        require(payload["closure_claimed"] is True, "closure boundary missing")
        require(payload["observed_data_used_as_selector"] is False, "observed selector used")
        require(payload["target_fitting_used"] is False, "target fitting used")

    decision = candidate["closure_decision"]
    require(decision["direct_source_theorem_attempted"] is True, "direct theorem not attempted")
    require(decision["source_statement_support_count"] == 6, "support count mismatch")
    require(decision["source_statement_required_count"] == 6, "required count mismatch")
    require(decision["source_statement_emitted_count"] == 0, "source statements overemitted")
    require(decision["source_object_fields_filled"] == 0, "source fields overfilled")
    require(decision["source_object_fields_required"] == 11, "source fields required mismatch")
    require(decision["connection_fields_filled"] == 0, "connection fields overfilled")
    require(decision["connection_fields_required"] == 8, "connection fields required mismatch")
    require(decision["conditional_replay_ready"] is True, "conditional replay not ready")
    for key in [
        "unconditional_replay_allowed",
        "direct_source_theorem_closed",
        "connection_tables_closed",
        "oriented_logdet_promoted",
        "direct_H_K_row_emitted",
        "full_no_knob_closed",
        "true_SM_equivalence_closed",
    ]:
        require(decision[key] is False, f"overclosed: {key}")
    require(decision["source_emission_principle_required"] is True, "source principle not required")

    require(attempt["status"] == "SIX_STATEMENTS_SUPPORTED_ZERO_SOURCE_EMITTED", "attempt status mismatch")
    require(attempt["statement_count"] == 6, "attempt statement count mismatch")
    require(attempt["support_count"] == 6, "attempt support count mismatch")
    require(attempt["emitted_source_statement_count"] == 0, "attempt overemitted")
    require(attempt["source_object_fields_filled"] == 0, "attempt source fields overfilled")
    require(attempt["source_object_fields_required"] == 11, "attempt required fields mismatch")
    require(attempt["direct_source_theorem_closed"] is False, "direct theorem overclosed")
    for row in attempt["rows"]:
        require(row["support_present"] is True, "row support missing")
        require(row["emitted_as_source_owned"] is False, "row overemitted")

    require(replay["status"] == "CONDITIONAL_REPLAY_READY_UNCONDITIONAL_SOURCE_OPEN", "replay status mismatch")
    require(replay["conditional_replay_ready"] is True, "conditional replay missing")
    require(replay["unconditional_replay_allowed"] is False, "unconditional replay overallowed")
    require(replay["source_emission_closed_now"] is False, "source emission overclosed")
    require(replay["oriented_logdet_promoted"] is False, "logdet overpromoted")
    require(replay["direct_declaration_support"]["basis_dimension"] == 27, "basis dimension mismatch")
    require(replay["direct_declaration_support"]["deck_action_materialized"] is True, "deck support missing")
    require(replay["direct_declaration_support"]["source_owned"] is False, "source ownership overclosed")

    require(
        next_contract["status"] == "NEXT_IS_SOURCE_EMISSION_PRINCIPLE_OR_EIGHT_CONNECTION_TABLES",
        "next status mismatch",
    )
    require(next_contract["primary_route"] == "source-emission principle", "primary route mismatch")
    require(len(next_contract["primary_must_prove"]) == 6, "primary proof clauses mismatch")
    require(len(next_contract["fallback_must_emit"]) == 8, "fallback table count mismatch")
    require(next_contract["direct_exit"] == "K_threshold.Omega_H.lambda", "direct exit mismatch")

    require("Source-owned emitted statements: `0/6`" in note, "note missing emitted count")
    require(NEXT in note, "note missing next artifact")

    print("S_QaSU3^BN27 selected-source theorem audit passed")
    print(json.dumps({"candidate": str(CANDIDATE.relative_to(ROOT)), "status": STATUS}, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
