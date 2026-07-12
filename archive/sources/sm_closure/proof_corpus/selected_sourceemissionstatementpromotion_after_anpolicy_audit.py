"""Audit source-emission statement promotion after A_N policy closure."""

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
BUILDER = ROOT / "scripts" / "build_selected_sourceemissionstatementpromotion_after_anpolicy.py"

SLUG = "selected_sourceemissionstatementpromotion_after_anpolicy"
PACKET_DIR = DATA / SLUG
CANDIDATE = DATA / f"{SLUG}.candidate.json"
CERT = CERTS / f"{SLUG}_certificate.json"
NOTE = CORPUS / "MTT_Selected_SourceEmissionStatementPromotion_AfterANPolicy_v1.md"
STATEMENT_PACKET = PACKET_DIR / "source_emission_statement_revalidation.packet.json"
SOURCE_OBJECT_PACKET = PACKET_DIR / "source_object_field_revalidation_after_an_policy.packet.json"
NEXT_PACKET = PACKET_DIR / "next_same_source_branch_identity_contract.packet.json"

STATUS = (
    "MTT_SELECTED_SOURCEEMISSIONSTATEMENTPROMOTION_AFTER_ANPOLICY_"
    "TWO_OF_SIX_SOURCE_STATEMENTS_PROMOTED_SOURCEBRANCH_OPEN"
)
NEXT = "MTT_Selected_CTauPhiFinSameSourceBranchIdentity_or_CechHYMConnectionValues_v1"
PROMOTED_STATEMENTS = [
    "full_F3xF3_carrier_emitted_before_finite_comparison",
    "kernel_and_trace_policies_source_owned",
]
REMAINING_STATEMENTS = [
    "C_tau_and_PhiFin_DE_coemitted_by_source",
    "RouteC_row_internal_not_external",
    "S_QaSU3_BN27_is_selected_threshold_source",
    "no_lift_replay_audit_from_emitted_fields",
]
PROMOTED_SOURCE_FIELDS = [
    "full_F3xF3_rank_slot_carrier_emitted",
    "kernel_shared_circle_policy_source_owned",
    "trace_zeta_finitepart_policy_source_owned",
]


def load(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def require(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)


def main() -> int:
    subprocess.run([sys.executable, str(BUILDER)], cwd=ROOT, check=True)

    candidate = load(CANDIDATE)
    cert = load(CERT)
    statements = load(STATEMENT_PACKET)
    source_fields = load(SOURCE_OBJECT_PACKET)
    next_packet = load(NEXT_PACKET)
    note = NOTE.read_text(encoding="utf-8")

    require(candidate["status"] == STATUS, "candidate status mismatch")
    require(cert["status"] == STATUS, "certificate status mismatch")
    require(candidate["next_required_artifact"] == NEXT, "candidate next mismatch")
    require(cert["next_required_artifact"] == NEXT, "certificate next mismatch")
    require(next_packet["next_required_artifact"] == NEXT, "next packet mismatch")
    require(candidate["theorem"]["proved"] is True, "theorem not proved")
    require(cert["theorem_proved"] is True, "certificate theorem not proved")

    for payload in [candidate, cert, statements, source_fields, next_packet]:
        require(payload["closure_claimed"] is True, "closure boundary missing")
        require(payload["observed_data_used_as_selector"] is False, "observed selector used")
        require(payload["target_fitting_used"] is False, "target fitting used")

    require(statements["previous_emitted_source_statement_count"] == 0, "previous count should be zero")
    require(statements["emitted_source_statement_count"] == 2, "statement count mismatch")
    require(statements["required_source_statement_count"] == 6, "required statement count")
    require(statements["accepted_statements"] == PROMOTED_STATEMENTS, "accepted statements")
    require(statements["remaining_statements"] == REMAINING_STATEMENTS, "remaining statements")
    for statement in PROMOTED_STATEMENTS:
        require(statements["rows"][statement]["emitted_as_source_owned"] is True, f"statement not promoted: {statement}")
    for statement in REMAINING_STATEMENTS:
        require(statements["rows"][statement]["emitted_as_source_owned"] is False, f"statement overpromoted: {statement}")
    require(statements["direct_source_theorem_closed"] is False, "direct source theorem overclosed")
    require(statements["source_branch_identity_closed"] is False, "source branch overclosed")

    require(source_fields["promoted_source_object_fields"] == PROMOTED_SOURCE_FIELDS, "source fields")
    require(source_fields["promoted_source_object_field_count"] == 3, "source field count")
    require(source_fields["required_source_object_field_count"] == 11, "source field required")
    for field in PROMOTED_SOURCE_FIELDS:
        require(source_fields["fields"][field]["source_owned"] is True, f"field not source-owned: {field}")
    for field in source_fields["remaining_source_object_fields"]:
        require(source_fields["fields"][field]["source_owned"] is False, f"field overpromoted: {field}")
    require(source_fields["oriented_logdet_promoted"] is False, "oriented logdet overpromoted")
    require(source_fields["unconditional_replay_allowed"] is False, "unconditional replay overpromoted")

    decision = candidate["closure_decision"]
    require(decision["source_emission_statement_count"] == 2, "decision statement count")
    require(decision["required_source_emission_statement_count"] == 6, "decision required statements")
    require(decision["accepted_source_emission_statements"] == PROMOTED_STATEMENTS, "decision accepted")
    require(decision["remaining_source_emission_statements"] == REMAINING_STATEMENTS, "decision remaining")
    require(decision["source_object_field_count"] == 3, "decision field count")
    require(decision["required_source_object_field_count"] == 11, "decision required fields")
    require(decision["promoted_source_object_fields"] == PROMOTED_SOURCE_FIELDS, "decision fields")
    require(decision["final_connection_tables_accepted"] == 4, "decision table count")
    for key in [
        "direct_source_theorem_closed",
        "source_branch_identity_closed",
        "oriented_logdet_promoted",
        "no_lifted_flags_connection_replay_promoted",
        "strict_no_knob_closed",
        "true_SM_equivalence_closed",
    ]:
        require(decision[key] is False, f"decision overclaim: {key}")
        require(cert[key] is False, f"cert overclaim: {key}")

    require(next_packet["source_emission_statement_count"] == "2/6", "next source count")
    require(next_packet["source_object_field_count"] == "3/11", "next field count")
    require(next_packet["final_connection_table_count"] == "4/8", "next table count")
    require(next_packet["sourceownership_transport_closed"] is False, "transport overclosed")
    require("`0/6` to `2/6`" in note, "note missing source count")
    require(NEXT in note, "note missing next")

    print("Source-emission statement promotion after A_N policy audit passed")
    print(json.dumps({"candidate": str(CANDIDATE.relative_to(ROOT)), "status": STATUS}, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
