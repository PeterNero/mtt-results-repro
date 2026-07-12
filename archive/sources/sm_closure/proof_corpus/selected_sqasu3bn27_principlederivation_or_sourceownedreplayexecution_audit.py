"""Audit BN27 strict-principle derivation and premised replay execution."""

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
BUILDER = ROOT / "scripts" / "build_selected_sqasu3bn27_principlederivation_or_sourceownedreplayexecution.py"

SLUG = "selected_sqasu3bn27_principlederivation_or_sourceownedreplayexecution"
PACKET_DIR = DATA / SLUG
CANDIDATE = DATA / f"{SLUG}.candidate.json"
CERT = CERTS / f"{SLUG}_certificate.json"
NOTE = CORPUS / "MTT_Selected_SQaSU3BN27_PrincipleDerivation_or_SourceOwnedReplayExecution_v1.md"
ROUTE_A = PACKET_DIR / "route_a_strict_principle_derivation_attempt.packet.json"
ROUTE_B = PACKET_DIR / "route_b_premised_source_owned_replay_execution.packet.json"
DUAL_DECISION = PACKET_DIR / "dual_path_decision_and_next_cutset.packet.json"

STATUS = (
    "MTT_SELECTED_SQASU3BN27_PRINCIPLEDERIVATION_OR_SOURCEOWNEDREPLAYEXECUTION_"
    "ROUTEA_ZERO_STRICT_ROUTEB_PREMISED_REPLAY_EXECUTED"
)
NEXT = "MTT_Selected_SQaSU3BN27_StrictPrincipleSourceTheorem_or_DirectConnectionTables_v1"


def load(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def require(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)


def main() -> int:
    subprocess.run([sys.executable, str(BUILDER)], cwd=ROOT, check=True)

    candidate = load(CANDIDATE)
    cert = load(CERT)
    route_a = load(ROUTE_A)
    route_b = load(ROUTE_B)
    decision_packet = load(DUAL_DECISION)
    note = NOTE.read_text(encoding="utf-8")

    require(candidate["status"] == STATUS, "candidate status mismatch")
    require(cert["status"] == STATUS, "certificate status mismatch")
    require(candidate["next_required_artifact"] == NEXT, "candidate next mismatch")
    require(cert["next_required_artifact"] == NEXT, "certificate next mismatch")
    require(decision_packet["next_required_artifact"] == NEXT, "decision next mismatch")
    require(candidate["theorem"]["proved"] is True, "theorem not proved")
    require(cert["theorem_proved"] is True, "certificate theorem flag missing")

    for payload in [candidate, cert, route_a, route_b, decision_packet]:
        require(payload["closure_claimed"] is True, "closure boundary missing")
        require(payload["observed_data_used_as_selector"] is False, "observed selector used")
        require(payload["target_fitting_used"] is False, "target fitting used")

    decision = candidate["closure_decision"]
    require(decision["route_A_strict_principle_derivation_attempted"] is True, "Route A not attempted")
    require(decision["route_A_support_clause_count"] == 6, "Route A support count mismatch")
    require(decision["route_A_required_clause_count"] == 6, "Route A required count mismatch")
    require(decision["route_A_strict_derived_clause_count"] == 0, "Route A overderived clauses")
    require(decision["route_A_strict_principle_derived"] is False, "Route A principle overderived")
    require(decision["route_B_premised_replay_executed"] is True, "Route B not executed")
    require(decision["route_B_source_statement_rows_executed"] == 6, "Route B statement count mismatch")
    require(decision["route_B_source_object_fields_executed"] == 11, "Route B source field count mismatch")
    require(decision["route_B_downstream_use_allowed_as_premised_local_source"] is True, "Route B premised use missing")
    require(decision["route_B_downstream_use_allowed_as_strict_unconditional_source"] is False, "Route B overpromoted")
    require(decision["connection_tables_filled"] == 0, "connection tables overfilled")
    require(decision["connection_tables_required"] == 8, "connection table required count mismatch")
    for key in [
        "strict_source_emission_principle_derived",
        "strict_unconditional_replay_allowed",
        "strict_no_knob_closed",
        "true_SM_equivalence_closed",
        "direct_H_K_row_emitted",
    ]:
        require(decision[key] is False, f"overclosed: {key}")

    require(
        route_a["status"] == "ROUTE_A_TESTED_SUPPORT_PRESENT_ZERO_STRICT_DERIVED_CLAUSES",
        "Route A status mismatch",
    )
    require(route_a["strict_derivation_attempted"] is True, "Route A attempt flag missing")
    require(route_a["clause_count"] == 6, "Route A clause count mismatch")
    require(route_a["support_clause_count"] == 6, "Route A support mismatch")
    require(route_a["strict_derived_clause_count"] == 0, "Route A overderived")
    require(route_a["accepted_as_strict_source_emission_theorem"] is False, "Route A accepted incorrectly")
    for row in route_a["rows"]:
        require(row["support_present"] is True, "Route A support missing")
        require(row["strict_derivation_from_current_unpatched_geometry"] is False, "Route A row overderived")

    require(
        route_b["status"] == "ROUTE_B_EXECUTED_PREMISED_LOCAL_SOURCE_OWNED_REPLAY",
        "Route B status mismatch",
    )
    require(route_b["accepted_as"] == "explicit local premise, not unpatched theorem", "Route B boundary missing")
    require(route_b["source_name"] == "S_QaSU3^BN27", "Route B source mismatch")
    require(route_b["basis_dimension"] == 27, "Route B basis mismatch")
    require(route_b["source_statement_rows_executed"] == 6, "Route B statement mismatch")
    require(route_b["source_object_fields_executed"] == 11, "Route B field mismatch")
    require(route_b["source_owned_values_under_premise"]["positive_spectrum_count"] == 16, "positive spectrum mismatch")
    require(route_b["source_owned_values_under_premise"]["oriented_abs_sector_product"] == 92160000, "product mismatch")
    require(route_b["source_owned_values_under_premise"]["oriented_abs_sector_logdet_exact"] == "log(92160000)", "logdet mismatch")
    require(route_b["downstream_use_allowed_as_premised_local_source"] is True, "Route B premised downstream use missing")
    require(route_b["downstream_use_allowed_as_strict_unconditional_source"] is False, "Route B strict use overallowed")
    require(route_b["strict_source_emission_principle_derived"] is False, "Route B overderived")
    require(route_b["strict_no_knob_closed"] is False, "Route B no-knob overclosed")
    require(route_b["true_SM_equivalence_closed"] is False, "Route B true-SM overclosed")

    require(
        decision_packet["status"] == "ROUTE_A_REMAINS_STRICT_WALL_ROUTE_B_IS_USABLE_PREMISED_SPINE",
        "decision packet status mismatch",
    )
    require(decision_packet["route_A_result"]["strict_principle_derived"] is False, "decision Route A overderived")
    require(decision_packet["route_A_result"]["strict_derived_clause_count"] == 0, "decision Route A count mismatch")
    require(decision_packet["route_B_result"]["premised_local_replay_executed"] is True, "decision Route B missing")
    require(decision_packet["route_B_result"]["premised_source_statement_rows"] == 6, "decision Route B statements mismatch")
    require(decision_packet["route_B_result"]["premised_source_object_fields"] == 11, "decision Route B fields mismatch")
    require(decision_packet["route_C_fallback"]["connection_table_fields_filled"] == 0, "decision connection overfilled")
    require(decision_packet["route_C_fallback"]["connection_table_fields_required"] == 8, "decision connection required mismatch")

    require("Strictly derived clauses from current unpatched geometry: `0/6`" in note, "note missing Route A result")
    require("Downstream use allowed: `premised/local source`" in note, "note missing Route B boundary")
    require(NEXT in note, "note missing next artifact")

    print("S_QaSU3^BN27 dual-path audit passed")
    print(json.dumps({"candidate": str(CANDIDATE.relative_to(ROOT)), "status": STATUS}, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
