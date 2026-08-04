"""Audit common-carrier co-emission after split ownership."""

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
BUILDER = ROOT / "scripts" / "build_selected_commoncarriercoemission_after_splitownership_or_selectedsourceobject.py"

SLUG = "selected_commoncarriercoemission_after_splitownership_or_selectedsourceobject"
PACKET_DIR = DATA / SLUG
CANDIDATE = DATA / f"{SLUG}.candidate.json"
CERT = CERTS / f"{SLUG}_certificate.json"
NOTE = CORPUS / "MTT_Selected_CommonCarrierCoEmission_AfterSplitOwnership_or_SelectedSourceObject_v1.md"
SUPPORT_PACKET = PACKET_DIR / "common_carrier_operator_coemission_support.packet.json"
STATEMENT_PACKET = PACKET_DIR / "source_emission_statement_revalidation_after_commoncarrier.packet.json"
FIELD_PACKET = PACKET_DIR / "source_object_field_revalidation_after_commoncarrier.packet.json"
BRANCH_PACKET = PACKET_DIR / "same_branch_source_theorem_gate_after_commoncarrier.packet.json"
NEXT_PACKET = PACKET_DIR / "next_selectedsourceobject_or_cechhym_contract.packet.json"

STATUS = (
    "MTT_SELECTED_COMMONCARRIERCOEMISSION_AFTER_SPLITOWNERSHIP_"
    "OPERATORS_FIELD_PROMOTED_SOURCE_THEOREM_OPEN"
)
NEXT = "MTT_Selected_SelectedSourceObjectSQaSU3BN27_or_CechHYMConnectionValues_v1"
PROMOTED_FIELD = "operators_coemitted_before_finite_comparison"
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
REMAINING_FIELDS = [
    "eleven_label_rho_tau_shadow_embeds_but_is_not_threshold_domain",
    "no_lifted_flags_full_replay_audit",
    "selected_source_object_S_QaSU3_BN27",
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
    support = load(SUPPORT_PACKET)
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

    for payload in [candidate, cert, support, statements, fields, branch, next_packet]:
        require(payload["closure_claimed"] is True, "closure boundary missing")
        require(payload["observed_data_used_as_selector"] is False, "observed selector used")
        require(payload["target_fitting_used"] is False, "target fitting used")

    require(support["promotes_source_object_field"] == PROMOTED_FIELD, "support field mismatch")
    require(support["does_not_promote_source_statement"] == "C_tau_and_PhiFin_DE_coemitted_by_source", "support statement guard")
    require(support["basis_dimension"] == 27, "basis dimension")
    require(support["same_basis"] is True, "same basis not closed")
    require(support["commutator_zero"] is True, "commutator not zero")
    require(support["simultaneous_functional_calculus_closed"] is True, "simultaneous calculus missing")
    require(support["C_tau_orientation_owned_on_split_branch"] is True, "C_tau split owner")
    require(support["PhiFin_DE_magnitude_owned_on_split_branch"] is True, "PhiFin split owner")
    for key in [
        "same_source_owns_both",
        "source_branch_identity_closed",
        "selected_source_object_closed",
        "no_lift_replay_allowed",
    ]:
        require(support[key] is False, f"support overclaim: {key}")

    require(statements["previous_emitted_source_statement_count"] == 3, "previous statement count")
    require(statements["emitted_source_statement_count"] == 3, "statement count changed")
    require(statements["required_source_statement_count"] == 6, "required statements")
    require(statements["accepted_statements"] == ACCEPTED_STATEMENTS, "accepted statements")
    require(statements["remaining_statements"] == REMAINING_STATEMENTS, "remaining statements")
    for statement in ACCEPTED_STATEMENTS:
        require(statements["rows"][statement]["emitted_as_source_owned"] is True, f"statement not retained: {statement}")
    for statement in REMAINING_STATEMENTS:
        require(statements["rows"][statement]["emitted_as_source_owned"] is False, f"statement overpromoted: {statement}")
    require(statements["rows"]["C_tau_and_PhiFin_DE_coemitted_by_source"]["common_carrier_support_closed"] is True, "support not attached")
    require(statements["common_carrier_support_closed"] is True, "statement support flag")
    for key in ["same_branch_coemission_closed", "direct_source_theorem_closed", "selected_source_object_closed"]:
        require(statements[key] is False, f"statement overclaim: {key}")

    require(fields["previous_promoted_source_object_field_count"] == 7, "previous field count")
    require(fields["promoted_source_object_field_count"] == 8, "field count")
    require(fields["required_source_object_field_count"] == 11, "required field count")
    require(fields["newly_promoted_source_object_fields"] == [PROMOTED_FIELD], "new field mismatch")
    require(fields["fields"][PROMOTED_FIELD]["source_owned"] is True, "operator field not promoted")
    require(fields["fields"][PROMOTED_FIELD]["scope"] == "common_carrier_support_not_same_source_theorem", "field scope guard")
    require(fields["remaining_source_object_fields"] == REMAINING_FIELDS, "remaining fields")
    for field in REMAINING_FIELDS:
        require(fields["fields"][field]["source_owned"] is False, f"field overpromoted: {field}")
    split = fields["split_ownership"]
    require(split["operators_coemitted_before_finite_comparison"] is True, "operator coemission not closed")
    require(split["same_source_owns_both"] is False, "same source overclosed")
    require(fields["common_carrier_support_closed"] is True, "field support flag")
    require(fields["oriented_logdet_promoted"] is False, "logdet overpromoted")
    require(fields["unconditional_replay_allowed"] is False, "replay overpromoted")

    require(branch["common_carrier_operator_coemission_closed"] is True, "branch common carrier")
    for key in [
        "source_branch_identity_closed",
        "selected_source_object_S_QaSU3_BN27_closed",
        "same_source_owns_both_branches",
    ]:
        require(branch[key] is False, f"branch overclaim: {key}")
    require("selected_source_object_S_QaSU3_BN27" in branch["remaining_root_clauses"], "selected source root missing")

    decision = candidate["closure_decision"]
    require(decision["source_emission_statement_count"] == 3, "decision statement count")
    require(decision["source_object_field_count"] == 8, "decision field count")
    require(decision["newly_promoted_source_object_fields"] == [PROMOTED_FIELD], "decision field")
    require(decision["operators_coemitted_before_finite_comparison"] is True, "decision operator field")
    require(decision["common_carrier_operator_coemission_closed"] is True, "decision common carrier")
    for key in [
        "C_tau_and_PhiFin_DE_coemitted_by_source",
        "same_source_owns_both_branches",
        "selected_source_object_S_QaSU3_BN27",
        "source_branch_identity_closed",
        "oriented_logdet_promoted",
        "no_lifted_flags_connection_replay_promoted",
        "strict_no_knob_closed",
        "true_SM_equivalence_closed",
    ]:
        require(decision[key] is False, f"decision overclaim: {key}")
        require(cert[key] is False, f"cert overclaim: {key}")
    require(decision["final_connection_tables_accepted"] == 4, "decision final table count")
    require(cert["final_connection_tables_accepted"] == 4, "cert final table count")

    require(next_packet["source_emission_statement_count"] == "3/6", "next statement count")
    require(next_packet["source_object_field_count"] == "8/11", "next field count")
    require(next_packet["final_connection_table_count"] == "4/8", "next table count")
    require("`7/11` to `8/11`" in note, "note missing 8/11 move")
    require("remains `3/6`" in note, "note missing statement guard")
    require(NEXT in note, "note missing next")

    print("Common-carrier co-emission after split ownership audit passed")
    print(json.dumps({"candidate": str(CANDIDATE.relative_to(ROOT)), "status": STATUS}, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
