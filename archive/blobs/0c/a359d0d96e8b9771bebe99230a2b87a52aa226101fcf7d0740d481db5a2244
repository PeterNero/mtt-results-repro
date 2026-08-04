"""Audit Route-C internality and split ownership promotion."""

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
BUILDER = ROOT / "scripts" / "build_selected_routecinternality_splitownership_or_samebranchidentity.py"

SLUG = "selected_routecinternality_splitownership_or_samebranchidentity"
PACKET_DIR = DATA / SLUG
CANDIDATE = DATA / f"{SLUG}.candidate.json"
CERT = CERTS / f"{SLUG}_certificate.json"
NOTE = CORPUS / "MTT_Selected_RouteCInternality_SplitOwnership_or_SameBranchIdentity_v1.md"
STATEMENT_PACKET = PACKET_DIR / "source_emission_statement_revalidation_after_routec.packet.json"
FIELD_PACKET = PACKET_DIR / "source_object_field_revalidation_after_splitownership.packet.json"
BRANCH_PACKET = PACKET_DIR / "same_branch_identity_remaining_gate.packet.json"
NEXT_PACKET = PACKET_DIR / "next_samebranch_or_cechhym_contract.packet.json"

STATUS = (
    "MTT_SELECTED_ROUTECINTERNALITY_SPLITOWNERSHIP_OR_SAMEBRANCHIDENTITY_"
    "THREE_OF_SIX_SOURCE_STATEMENTS_SEVEN_OF_ELEVEN_FIELDS_PROMOTED_SAMEBRANCH_OPEN"
)
NEXT = "MTT_Selected_CTauPhiFinSameBranchCoEmission_or_CechHYMConnectionValues_v1"
ACCEPTED_STATEMENTS = [
    "full_F3xF3_carrier_emitted_before_finite_comparison",
    "kernel_and_trace_policies_source_owned",
    "RouteC_row_internal_not_external",
]
REMAINING_STATEMENTS = [
    "C_tau_and_PhiFin_DE_coemitted_by_source",
    "S_QaSU3_BN27_is_selected_threshold_source",
    "no_lift_replay_audit_from_emitted_fields",
]
NEW_FIELDS = [
    "RouteC_row_internal_theorem_not_external_import",
    "one_selected_source_owns_RouteC_PhiFin_DE_magnitude",
    "one_selected_source_owns_heterotic_C_tau_orientation",
    "sixteen_nonzero_oriented_positive_rows_retained",
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
    fields = load(FIELD_PACKET)
    branch = load(BRANCH_PACKET)
    next_packet = load(NEXT_PACKET)
    note = NOTE.read_text(encoding="utf-8")

    require(candidate["status"] == STATUS, "candidate status mismatch")
    require(cert["status"] == STATUS, "certificate status mismatch")
    require(candidate["next_required_artifact"] == NEXT, "candidate next mismatch")
    require(cert["next_required_artifact"] == NEXT, "certificate next mismatch")
    require(next_packet["next_required_artifact"] == NEXT, "next packet mismatch")
    require(candidate["theorem"]["proved"] is True, "theorem not proved")
    require(cert["theorem_proved"] is True, "certificate theorem not proved")

    for payload in [candidate, cert, statements, fields, branch, next_packet]:
        require(payload["closure_claimed"] is True, "closure boundary missing")
        require(payload["observed_data_used_as_selector"] is False, "observed selector used")
        require(payload["target_fitting_used"] is False, "target fitting used")

    require(statements["previous_emitted_source_statement_count"] == 2, "previous statement count")
    require(statements["emitted_source_statement_count"] == 3, "statement count")
    require(statements["required_source_statement_count"] == 6, "required statements")
    require(statements["accepted_statements"] == ACCEPTED_STATEMENTS, "accepted statements")
    require(statements["remaining_statements"] == REMAINING_STATEMENTS, "remaining statements")
    for statement in ACCEPTED_STATEMENTS:
        require(statements["rows"][statement]["emitted_as_source_owned"] is True, f"statement not promoted: {statement}")
    for statement in REMAINING_STATEMENTS:
        require(statements["rows"][statement]["emitted_as_source_owned"] is False, f"statement overpromoted: {statement}")
    require(statements["direct_source_theorem_closed"] is False, "direct theorem overclosed")
    require(statements["same_branch_coemission_closed"] is False, "same branch overclosed")

    require(fields["promoted_source_object_field_count"] == 7, "field count")
    require(fields["required_source_object_field_count"] == 11, "required field count")
    require(fields["newly_promoted_source_object_fields"] == NEW_FIELDS, "new fields")
    for field in NEW_FIELDS:
        require(fields["fields"][field]["source_owned"] is True, f"field not promoted: {field}")
    split = fields["split_ownership"]
    require(split["RouteC_PhiFin_DE_magnitude_owned_by_A_N_source"] is True, "PhiFin split owner")
    require(split["heterotic_C_tau_orientation_owned_by_C_tau_source"] is True, "C_tau split owner")
    require(split["same_source_owns_both"] is False, "same source overclosed")
    require(split["operators_coemitted_before_finite_comparison"] is False, "coemission overclosed")
    require(fields["oriented_logdet_promoted"] is False, "logdet overpromoted")
    require(fields["unconditional_replay_allowed"] is False, "replay overpromoted")

    require(branch["routec_row_not_external_import_closed"] is True, "routec clause not closed")
    require(branch["source_branch_identity_closed"] is False, "source branch overclosed")
    require(branch["transport_closed"] is False, "transport overclosed")
    require("routec_row_not_external_import" in branch["closed_sourcebranch_clauses"], "routec closed clause missing")
    require("one_selected_source_names_both_branches" in branch["remaining_sourcebranch_clauses"], "same source clause missing")
    require("eleven_label_to_full_BN27_threshold_carrier" in branch["remaining_sourcebranch_clauses"], "carrier clause missing")

    decision = candidate["closure_decision"]
    require(decision["source_emission_statement_count"] == 3, "decision statement count")
    require(decision["source_object_field_count"] == 7, "decision field count")
    require(decision["accepted_source_emission_statements"] == ACCEPTED_STATEMENTS, "decision accepted")
    require(decision["remaining_source_emission_statements"] == REMAINING_STATEMENTS, "decision remaining")
    require(decision["newly_promoted_source_object_fields"] == NEW_FIELDS, "decision fields")
    require(decision["routec_row_internal_not_external_closed"] is True, "decision routec")
    require(decision["split_Ctau_orientation_owned"] is True, "decision ctau")
    require(decision["split_PhiFin_DE_magnitude_owned"] is True, "decision phifin")
    for key in [
        "same_source_owns_both_branches",
        "direct_source_theorem_closed",
        "source_branch_identity_closed",
        "oriented_logdet_promoted",
        "no_lifted_flags_connection_replay_promoted",
        "strict_no_knob_closed",
        "true_SM_equivalence_closed",
    ]:
        require(decision[key] is False, f"decision overclaim: {key}")
        require(cert[key] is False, f"cert overclaim: {key}")

    require(next_packet["source_emission_statement_count"] == "3/6", "next statement count")
    require(next_packet["source_object_field_count"] == "7/11", "next field count")
    require(next_packet["final_connection_table_count"] == "4/8", "next table count")
    require("`2/6` to `3/6`" in note, "note missing count")
    require(NEXT in note, "note missing next")

    print("Route-C internality and split ownership audit passed")
    print(json.dumps({"candidate": str(CANDIDATE.relative_to(ROOT)), "status": STATUS}, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
