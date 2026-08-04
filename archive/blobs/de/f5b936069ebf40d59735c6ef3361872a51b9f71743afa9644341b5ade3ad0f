"""Audit BN27 one-premise source-object adoption."""

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
BUILDER = ROOT / "scripts" / "build_selected_bn27_onepremise_sourceobject_adoption_or_strictcechhym.py"

SLUG = "selected_bn27_onepremise_sourceobject_adoption_or_strictcechhym"
PACKET_DIR = DATA / SLUG
CANDIDATE = DATA / f"{SLUG}.candidate.json"
CERT = CERTS / f"{SLUG}_certificate.json"
NOTE = CORPUS / "MTT_Selected_BN27_OnePremise_SourceObjectAdoption_or_StrictCechHYM_v1.md"
SOURCE_PACKET = PACKET_DIR / "strict_vs_onepremise_sourceobject_gate.packet.json"
STATEMENT_PACKET = PACKET_DIR / "strict_vs_onepremise_source_statement_gate.packet.json"
CONNECTION_PACKET = PACKET_DIR / "strict_vs_onepremise_connection_row_gate.packet.json"
NEXT_PACKET = PACKET_DIR / "next_strictsource_or_geometric_cechhym_contract.packet.json"

STATUS = (
    "MTT_SELECTED_BN27_ONEPREMISE_SOURCEOBJECTADOPTION_OR_STRICTCECHHYM_"
    "ONE_PREMISE_CLOSES_SOURCEOBJECT_PROVENANCE_STRICT_OPEN"
)
NEXT = "MTT_Selected_StrictBN27SourceTheorem_or_GeometricCechHYMConnectionValues_v1"
PREMISE_NAME = "SelectedBN27ThresholdSourceEmissionPrinciple"
STRICT_REMAINING_FIELDS = [
    "no_lifted_flags_full_replay_audit",
    "selected_source_object_S_QaSU3_BN27",
]
STRICT_REMAINING_STATEMENTS = [
    "C_tau_and_PhiFin_DE_coemitted_by_source",
    "S_QaSU3_BN27_is_selected_threshold_source",
    "no_lift_replay_audit_from_emitted_fields",
]
PREMISED_PROVENANCE_ROWS = [
    "finitepart_log92160000_identity_from_values",
    "no_lifted_flags_connection_replay",
]
STRICT_ACCEPTED_ROWS = [
    "typed_f_sections",
    "typed_g_sections",
    "g_after_f_zero_exactness_certificate",
    "BN27_DE_Riesz_Green_kernel_trace_export",
]
GEOMETRIC_REMAINING_ROWS = [
    "cech_transition_cocycles",
    "selected_HYM_or_projective_connection_coefficients",
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
    source = load(SOURCE_PACKET)
    statements = load(STATEMENT_PACKET)
    connection = load(CONNECTION_PACKET)
    next_packet = load(NEXT_PACKET)
    note = NOTE.read_text(encoding="utf-8")

    require(candidate["status"] == STATUS, "candidate status mismatch")
    require(cert["status"] == STATUS, "certificate status mismatch")
    require(candidate["next_required_artifact"] == NEXT, "candidate next mismatch")
    require(cert["next_required_artifact"] == NEXT, "certificate next mismatch")
    require(next_packet["next_required_artifact"] == NEXT, "next packet mismatch")
    require(candidate["theorem"]["proved"] is True, "theorem not proved")
    require(cert["theorem_proved"] is True, "certificate theorem not proved")

    for payload in [candidate, cert, source, statements, connection, next_packet]:
        require(payload["closure_claimed"] is True, "closure boundary missing")
        require(payload["observed_data_used_as_selector"] is False, "observed selector used")
        require(payload["target_fitting_used"] is False, "target fitting used")

    require(source["premise_name"] == PREMISE_NAME, "source premise name")
    require(source["premise_count"] == 1, "source premise count")
    require(source["premise_status"] == "EXPLICIT_LOCAL_PREMISE_NOT_STRICT_DERIVATION", "source premise status")
    require(source["strict_source_object_field_count"] == "9/11", "strict source fields")
    require(source["strict_remaining_source_object_fields"] == STRICT_REMAINING_FIELDS, "strict remaining fields")
    require(source["one_premise_source_object_field_count"] == "11/11", "premised source fields")
    require(source["one_premise_newly_closed_fields"] == STRICT_REMAINING_FIELDS, "premised new fields")
    require(source["strict_source_emission_principle_derived"] is False, "strict principle overclosed")
    require(source["downstream_use_allowed_as_premised_local_source"] is True, "premised downstream missing")
    require(source["downstream_use_allowed_as_strict_unconditional_source"] is False, "strict downstream overclaim")

    require(statements["premise_name"] == PREMISE_NAME, "statement premise name")
    require(statements["premise_count"] == 1, "statement premise count")
    require(statements["strict_source_statement_count"] == "3/6", "strict statements")
    require(statements["strict_remaining_source_emission_statements"] == STRICT_REMAINING_STATEMENTS, "strict remaining statements")
    require(statements["one_premise_source_statement_count"] == "6/6", "premised statements")
    require(statements["one_premise_newly_closed_statements"] == STRICT_REMAINING_STATEMENTS, "premised new statements")
    require(statements["strict_source_emission_principle_derived"] is False, "statement strict overclaim")

    require(connection["premise_name"] == PREMISE_NAME, "connection premise name")
    require(connection["premise_count"] == 1, "connection premise count")
    require(connection["strict_final_connection_table_count"] == "4/8", "strict table count")
    require(connection["strict_accepted_rows"] == STRICT_ACCEPTED_ROWS, "strict accepted rows")
    require(connection["one_premise_final_connection_table_count"] == "6/8", "premised table count")
    require(connection["one_premise_newly_promoted_provenance_rows"] == PREMISED_PROVENANCE_ROWS, "premised provenance rows")
    require(connection["one_premise_remaining_geometric_rows"] == GEOMETRIC_REMAINING_ROWS, "premised remaining rows")
    require(connection["finitepart_log92160000_source_owned_under_premise"] is True, "finitepart premise missing")
    require(connection["no_lift_replay_available_under_premise"] is True, "no-lift premise missing")
    for key in [
        "strict_connection_tables_closed",
        "strict_source_emission_principle_derived",
        "selected_cech_hym_geometric_values_closed",
    ]:
        require(connection[key] is False, f"connection overclaim: {key}")

    decision = candidate["closure_decision"]
    require(decision["premise_name"] == PREMISE_NAME, "decision premise")
    require(decision["premise_count"] == 1, "decision premise count")
    require(decision["strict_source_object_field_count"] == 9, "decision strict fields")
    require(decision["one_premise_source_object_field_count"] == 11, "decision premised fields")
    require(decision["strict_source_statement_count"] == 3, "decision strict statements")
    require(decision["one_premise_source_statement_count"] == 6, "decision premised statements")
    require(decision["strict_final_connection_tables_accepted"] == 4, "decision strict tables")
    require(decision["one_premise_final_connection_tables_accepted"] == 6, "decision premised tables")
    require(decision["one_premise_newly_promoted_source_object_fields"] == STRICT_REMAINING_FIELDS, "decision new fields")
    require(decision["one_premise_newly_promoted_source_statements"] == STRICT_REMAINING_STATEMENTS, "decision new statements")
    require(decision["one_premise_newly_promoted_connection_rows"] == PREMISED_PROVENANCE_ROWS, "decision new rows")
    require(decision["remaining_geometric_connection_rows"] == GEOMETRIC_REMAINING_ROWS, "decision remaining geometric")
    for key in [
        "strict_source_emission_principle_derived",
        "downstream_use_allowed_as_strict_unconditional_source",
        "strict_connection_tables_closed",
        "strict_no_knob_closed",
        "true_SM_equivalence_closed",
    ]:
        require(decision[key] is False, f"decision overclaim: {key}")
        require(cert[key] is False, f"cert overclaim: {key}")
    require(decision["downstream_use_allowed_as_premised_local_source"] is True, "decision premise downstream")

    require(next_packet["strict_lane"]["source_emission_statement_count"] == "3/6", "next strict statement count")
    require(next_packet["strict_lane"]["source_object_field_count"] == "9/11", "next strict field count")
    require(next_packet["strict_lane"]["final_connection_table_count"] == "4/8", "next strict table count")
    require(next_packet["one_premise_lane"]["premise_count"] == 1, "next premise count")
    require(next_packet["one_premise_lane"]["source_emission_statement_count"] == "6/6", "next premised statements")
    require(next_packet["one_premise_lane"]["source_object_field_count"] == "11/11", "next premised fields")
    require(next_packet["one_premise_lane"]["final_connection_table_count"] == "6/8", "next premised tables")
    require(any("not report the one-premise lane as strict" in item for item in next_packet["forbidden_overclaims"]), "forbidden overclaim")

    require("Strict lane remains" in note, "note strict lane")
    require("One-counted-premise lane" in note, "note premised lane")
    require("final connection tables: `6/8`" in note, "note 6/8")
    require(NEXT in note, "note next")

    print("BN27 one-premise source-object adoption audit passed")
    print(json.dumps({"candidate": str(CANDIDATE.relative_to(ROOT)), "status": STATUS}, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
