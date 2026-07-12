"""Audit S_QaSU3^BN27 source-emission principle / connection-table fill."""

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
BUILDER = ROOT / "scripts" / "build_selected_sqasu3bn27_sourceemissionprinciple_or_connectiontablefill.py"

SLUG = "selected_sqasu3bn27_sourceemissionprinciple_or_connectiontablefill"
PACKET_DIR = DATA / SLUG
CANDIDATE = DATA / f"{SLUG}.candidate.json"
CERT = CERTS / f"{SLUG}_certificate.json"
NOTE = CORPUS / "MTT_Selected_SQaSU3BN27_SourceEmissionPrinciple_or_ConnectionTableFill_v1.md"

PRINCIPLE_PACKET = PACKET_DIR / "source_emission_principle_premise.packet.json"
REPLAY_PACKET = PACKET_DIR / "premised_source_owned_replay.packet.json"
GAP_PACKET = PACKET_DIR / "strict_derivation_gap_or_connection_table_fallback.packet.json"
NEXT_PACKET = PACKET_DIR / "next_principle_derivation_or_sourceowned_replay_contract.packet.json"

STATUS = (
    "MTT_SELECTED_SQASU3BN27_SOURCEEMISSIONPRINCIPLE_OR_CONNECTIONTABLEFILL_"
    "BUILT_EXPLICIT_PREMISE_CLOSURE_STRICT_DERIVATION_OPEN"
)
NEXT = "MTT_Selected_SQaSU3BN27_PrincipleDerivation_or_SourceOwnedReplayExecution_v1"


def load(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def require(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)


def main() -> int:
    subprocess.run([sys.executable, str(BUILDER)], cwd=ROOT, check=True)

    candidate = load(CANDIDATE)
    cert = load(CERT)
    principle = load(PRINCIPLE_PACKET)
    replay = load(REPLAY_PACKET)
    gap = load(GAP_PACKET)
    next_packet = load(NEXT_PACKET)
    note = NOTE.read_text(encoding="utf-8")

    require(candidate["status"] == STATUS, "candidate status mismatch")
    require(cert["status"] == STATUS, "certificate status mismatch")
    require(candidate["next_required_artifact"] == NEXT, "candidate next mismatch")
    require(cert["next_required_artifact"] == NEXT, "certificate next mismatch")
    require(next_packet["next_required_artifact"] == NEXT, "next packet mismatch")
    require(candidate["theorem"]["proved"] is True, "theorem flag missing")
    require(cert["theorem_proved"] is True, "certificate theorem flag missing")

    for payload in [candidate, cert, principle, replay, gap, next_packet]:
        require(payload["closure_claimed"] is True, "closure boundary missing")
        require(payload["observed_data_used_as_selector"] is False, "observed selector used")
        require(payload["target_fitting_used"] is False, "target fitting used")

    decision = candidate["closure_decision"]
    require(decision["source_emission_principle_constructed"] is True, "principle not constructed")
    require(decision["explicit_local_premise_inserted"] is True, "explicit premise missing")
    require(decision["premised_source_ownership_closed"] is True, "premised closure missing")
    require(decision["premised_source_statement_emitted_count"] == 6, "premised statement count mismatch")
    require(decision["premised_source_statement_required_count"] == 6, "required statement count mismatch")
    require(decision["premised_source_object_fields_filled"] == 11, "premised source field count mismatch")
    require(decision["premised_source_object_fields_required"] == 11, "required source field count mismatch")
    require(decision["premised_validator_replay_allowed"] is True, "premised replay not allowed")
    require(decision["premised_oriented_logdet_source_owned"] is True, "premised logdet not owned")
    require(decision["strict_source_emission_principle_derived"] is False, "strict principle overderived")
    require(decision["strict_unconditional_replay_allowed"] is False, "strict replay overallowed")
    require(decision["connection_tables_filled"] == 0, "connection tables overfilled")
    require(decision["connection_tables_required"] == 8, "connection table required count mismatch")
    for key in ["strict_no_knob_closed", "true_SM_equivalence_closed", "direct_H_K_row_emitted"]:
        require(decision[key] is False, f"overclosed: {key}")

    require(
        principle["status"] == "EXPLICIT_LOCAL_SOURCE_EMISSION_PREMISE_CONSTRUCTED",
        "principle status mismatch",
    )
    require(
        principle["premise_status"] == "EXPLICIT_LOCAL_PREMISE_NOT_STRICT_DERIVATION",
        "principle premise boundary mismatch",
    )
    require(principle["source_name"] == "S_QaSU3^BN27", "source name mismatch")
    require(principle["basis_dimension"] == 27, "basis dimension mismatch")
    require(len(principle["premise_clauses"]) == 6, "principle clause count mismatch")
    require(principle["guardrails"]["strict_source_emission_principle_derived"] is False, "principle overderived")
    require(principle["guardrails"]["strict_no_knob_closed"] is False, "principle no-knob overclosed")
    require(principle["guardrails"]["true_SM_equivalence_closed"] is False, "principle true-SM overclosed")

    require(
        replay["status"] == "PREMISED_SOURCE_OWNED_REPLAY_CLOSES_CONDITIONAL_DAG",
        "replay status mismatch",
    )
    require(len(replay["source_statement_emission"]) == 6, "replay statement count mismatch")
    require(len(replay["source_object_field_fill"]) == 11, "replay source field count mismatch")
    require(replay["premised_source_owned_positive_spectrum_count"] == 16, "positive spectrum mismatch")
    require(replay["premised_oriented_abs_sector_product"] == 92160000, "oriented product mismatch")
    require(replay["premised_oriented_abs_sector_logdet_exact"] == "log(92160000)", "oriented logdet mismatch")
    require(replay["premised_validator_replay_allowed"] is True, "replay not allowed under premise")
    require(replay["unconditional_validator_replay_allowed"] is False, "unconditional replay overallowed")
    require(replay["strict_source_emission_principle_derived"] is False, "replay overderived")
    for row in replay["source_statement_emission"].values():
        require(row["emitted_as_source_owned_under_premise"] is True, "statement not emitted under premise")
    for row in replay["source_object_field_fill"].values():
        require(row["value"] is True, "field not filled under premise")

    require(
        gap["status"] == "STRICT_DERIVATION_OPEN_CONNECTION_TABLE_FALLBACK_OPEN",
        "gap status mismatch",
    )
    require(gap["strict_source_emission_principle_derived"] is False, "gap overderived")
    require(gap["strict_unconditional_replay_allowed"] is False, "gap replay overallowed")
    require(gap["connection_table_fields_filled"] == 0, "gap connection fields overfilled")
    require(gap["connection_table_fields_required"] == 8, "gap connection required mismatch")
    require(len(gap["connection_table_fields_remaining"]) == 8, "remaining connection fields mismatch")
    require(gap["strict_no_knob_closed"] is False, "gap no-knob overclosed")
    require(gap["true_SM_equivalence_closed"] is False, "gap true-SM overclosed")

    require(
        next_packet["status"] == "NEXT_IS_DERIVE_PRINCIPLE_OR_EXECUTE_PREMISED_REPLAY_WITH_GUARD",
        "next status mismatch",
    )
    require(next_packet["route_A_strict_derivation_target"] == "SelectedBN27ThresholdSourceEmissionPrinciple", "route A mismatch")
    require(len(next_packet["route_A_must_turn_into_theorem"]) == 6, "route A clauses mismatch")
    require(len(next_packet["route_C_fallback_connection_tables"]) == 8, "route C tables mismatch")
    require("premised/local" in next_packet["claim_boundary_required"], "claim boundary missing")

    require("premised/local closure" in note, "note missing premised/local boundary")
    require("Strict source-emission principle derived: `false`" in note, "note missing strict guard")
    require(NEXT in note, "note missing next artifact")

    print("S_QaSU3^BN27 source-emission principle audit passed")
    print(json.dumps({"candidate": str(CANDIDATE.relative_to(ROOT)), "status": STATUS}, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
