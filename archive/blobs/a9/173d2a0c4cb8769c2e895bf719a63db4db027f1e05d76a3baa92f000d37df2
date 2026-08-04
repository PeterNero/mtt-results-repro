"""Adopt the BN27 source-object principle as one explicit premise.

The strict lane remains unchanged: the current proof has 9/11 source-object
fields, 3/6 source-emission statements, and 4/8 final connection tables.  This
builder adds a separate counted-premise lane.  In that lane the already audited
SelectedBN27ThresholdSourceEmissionPrinciple is adopted as one explicit source
premise, which closes the two remaining BN27 source-object fields and the two
provenance connection rows.  The two geometric Cech/HYM rows remain open.
"""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "candidate_data"
CERTS = ROOT / "certificates"
CORPUS = ROOT / "proof_corpus"

SLUG = "selected_bn27_onepremise_sourceobject_adoption_or_strictcechhym"
PACKET_DIR = DATA / SLUG
OUTPUT = DATA / f"{SLUG}.candidate.json"
SOURCE_PACKET = PACKET_DIR / "strict_vs_onepremise_sourceobject_gate.packet.json"
STATEMENT_PACKET = PACKET_DIR / "strict_vs_onepremise_source_statement_gate.packet.json"
CONNECTION_PACKET = PACKET_DIR / "strict_vs_onepremise_connection_row_gate.packet.json"
NEXT_PACKET = PACKET_DIR / "next_strictsource_or_geometric_cechhym_contract.packet.json"
CERT = CERTS / f"{SLUG}_certificate.json"
NOTE = CORPUS / "MTT_Selected_BN27_OnePremise_SourceObjectAdoption_or_StrictCechHYM_v1.md"

CURRENT = DATA / "selected_rhotau_shadowguard_after_commoncarrier_or_selectedsourceobject.candidate.json"
CURRENT_FIELDS = (
    DATA
    / "selected_rhotau_shadowguard_after_commoncarrier_or_selectedsourceobject"
    / "source_object_field_revalidation_after_shadowguard.packet.json"
)
CURRENT_STATEMENTS = (
    DATA
    / "selected_rhotau_shadowguard_after_commoncarrier_or_selectedsourceobject"
    / "source_emission_statement_revalidation_after_shadowguard.packet.json"
)
CURRENT_NEXT = (
    DATA
    / "selected_rhotau_shadowguard_after_commoncarrier_or_selectedsourceobject"
    / "next_selectedsourceobject_or_nolift_or_cechhym_contract.packet.json"
)
PRINCIPLE = (
    DATA
    / "selected_sqasu3bn27_sourceemissionprinciple_or_connectiontablefill"
    / "source_emission_principle_premise.packet.json"
)
PREMISED_REPLAY = (
    DATA
    / "selected_sqasu3bn27_sourceemissionprinciple_or_connectiontablefill"
    / "premised_source_owned_replay.packet.json"
)
ROUTE_A = (
    DATA
    / "selected_sqasu3bn27_principlederivation_or_sourceownedreplayexecution"
    / "route_a_strict_principle_derivation_attempt.packet.json"
)
ROUTE_B = (
    DATA
    / "selected_sqasu3bn27_principlederivation_or_sourceownedreplayexecution"
    / "route_b_premised_source_owned_replay_execution.packet.json"
)
CONNECTION_ROWS = (
    DATA
    / "selected_derieszgreenkerneltraceexport_promotion_or_remainingconnectiontables"
    / "eight_table_revalidation_after_de_export.packet.json"
)
POSTDE_GATE = (
    DATA
    / "selected_postdeexport_remainingdependencycut_or_sourceownedfinitepart"
    / "logdet_no_lift_strict_gate_after_4of8.packet.json"
)

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


def rel(path: Path) -> str:
    try:
        return str(path.relative_to(ROOT)).replace("\\", "/")
    except ValueError:
        return str(path).replace("\\", "/")


def load(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def write_json(path: Path, payload: dict[str, Any]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(payload, indent=2, sort_keys=True) + "\n", encoding="utf-8")


def require_sources(paths: list[Path]) -> None:
    missing = [rel(path) for path in paths if not path.exists()]
    if missing:
        raise FileNotFoundError("missing BN27 one-premise inputs: " + ", ".join(missing))


def main() -> int:
    require_sources(
        [
            CURRENT,
            CURRENT_FIELDS,
            CURRENT_STATEMENTS,
            CURRENT_NEXT,
            PRINCIPLE,
            PREMISED_REPLAY,
            ROUTE_A,
            ROUTE_B,
            CONNECTION_ROWS,
            POSTDE_GATE,
        ]
    )

    current = load(CURRENT)
    current_fields = load(CURRENT_FIELDS)
    current_statements = load(CURRENT_STATEMENTS)
    current_next = load(CURRENT_NEXT)
    principle = load(PRINCIPLE)
    premised_replay = load(PREMISED_REPLAY)
    route_a = load(ROUTE_A)
    route_b = load(ROUTE_B)
    connection_rows = load(CONNECTION_ROWS)
    postde_gate = load(POSTDE_GATE)

    if current_fields["promoted_source_object_field_count"] != 9:
        raise ValueError("expected strict source-object fields 9/11")
    if current_statements["emitted_source_statement_count"] != 3:
        raise ValueError("expected strict source statements 3/6")
    if connection_rows["accepted_final_same_source_connection_tables"] != 4:
        raise ValueError("expected strict connection rows 4/8")
    if principle["premise_status"] != "EXPLICIT_LOCAL_PREMISE_NOT_STRICT_DERIVATION":
        raise ValueError("BN27 principle is not marked as explicit local premise")
    if principle["principle_name"] != PREMISE_NAME:
        raise ValueError("unexpected principle name")
    if route_a["strict_derived_clause_count"] != 0:
        raise ValueError("strict source theorem unexpectedly derived")
    if route_b["accepted_as"] != "explicit local premise, not unpatched theorem":
        raise ValueError("Route B premise boundary missing")

    source_fields = premised_replay["source_object_field_fill"]
    source_statements = premised_replay["source_statement_emission"]
    if len(source_fields) != 11 or not all(row["value"] for row in source_fields.values()):
        raise ValueError("premised source-object replay does not fill 11/11")
    if len(source_statements) != 6 or not all(row["emitted_as_source_owned_under_premise"] for row in source_statements.values()):
        raise ValueError("premised source-statement replay does not emit 6/6")

    finitepart_support = connection_rows["rows"]["finitepart_log92160000_identity_from_values"]["support_available"]
    nolift_support = connection_rows["rows"]["no_lifted_flags_connection_replay"]["support_available"]
    if not finitepart_support["source_owned_under_premise"]:
        raise ValueError("finitepart row is not source-owned under premise")
    if not nolift_support["premised_no_lift_replay_available"]:
        raise ValueError("no-lift row is not available under premise")
    if postde_gate["sourceowned_logdet_gate"]["source_owned_logdet_closed"]:
        raise ValueError("strict logdet gate should still be open")
    if postde_gate["no_lift_gate"]["same_source_export_to_BN27_validators"]:
        raise ValueError("strict no-lift validator should still be open")

    premised_accepted_rows = STRICT_ACCEPTED_ROWS + PREMISED_PROVENANCE_ROWS

    source_packet = {
        "schema": "MTTStrictVsOnePremiseBN27SourceObjectGate.v1",
        "status": "STRICT_9_OF_11_ONE_PREMISE_11_OF_11",
        "closure_claimed": True,
        "premise_name": PREMISE_NAME,
        "premise_count": 1,
        "premise_status": principle["premise_status"],
        "strict_source_object_field_count": "9/11",
        "strict_remaining_source_object_fields": STRICT_REMAINING_FIELDS,
        "one_premise_source_object_field_count": "11/11",
        "one_premise_newly_closed_fields": STRICT_REMAINING_FIELDS,
        "one_premise_field_owner": PREMISE_NAME,
        "strict_source_emission_principle_derived": False,
        "downstream_use_allowed_as_premised_local_source": True,
        "downstream_use_allowed_as_strict_unconditional_source": False,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
    }

    statement_packet = {
        "schema": "MTTStrictVsOnePremiseBN27SourceStatementGate.v1",
        "status": "STRICT_3_OF_6_ONE_PREMISE_6_OF_6",
        "closure_claimed": True,
        "premise_name": PREMISE_NAME,
        "premise_count": 1,
        "strict_source_statement_count": "3/6",
        "strict_remaining_source_emission_statements": STRICT_REMAINING_STATEMENTS,
        "one_premise_source_statement_count": "6/6",
        "one_premise_newly_closed_statements": STRICT_REMAINING_STATEMENTS,
        "one_premise_statement_owner": PREMISE_NAME,
        "strict_source_emission_principle_derived": False,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
    }

    connection_packet = {
        "schema": "MTTStrictVsOnePremiseBN27ConnectionRowGate.v1",
        "status": "STRICT_4_OF_8_ONE_PREMISE_6_OF_8_GEOMETRIC_CECHHYM_OPEN",
        "closure_claimed": True,
        "premise_name": PREMISE_NAME,
        "premise_count": 1,
        "strict_final_connection_table_count": "4/8",
        "strict_accepted_rows": STRICT_ACCEPTED_ROWS,
        "strict_remaining_rows": connection_rows["remaining_rows"],
        "one_premise_final_connection_table_count": "6/8",
        "one_premise_accepted_rows": premised_accepted_rows,
        "one_premise_newly_promoted_provenance_rows": PREMISED_PROVENANCE_ROWS,
        "one_premise_remaining_geometric_rows": GEOMETRIC_REMAINING_ROWS,
        "finitepart_log92160000_source_owned_under_premise": True,
        "no_lift_replay_available_under_premise": True,
        "strict_connection_tables_closed": False,
        "strict_source_emission_principle_derived": False,
        "selected_cech_hym_geometric_values_closed": False,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
    }

    next_packet = {
        "schema": "MTTNextStrictSourceOrGeometricCechHYMContract.v1",
        "status": "NEXT_IS_STRICT_SOURCE_THEOREM_OR_GEOMETRIC_CECHHYM_VALUES",
        "closure_claimed": True,
        "next_required_artifact": NEXT,
        "strict_lane": {
            "source_emission_statement_count": "3/6",
            "source_object_field_count": "9/11",
            "final_connection_table_count": "4/8",
            "remaining_minimal_exits": [
                "derive SelectedBN27ThresholdSourceEmissionPrinciple without the explicit premise",
                "emit selected Cech/HYM connection values directly",
            ],
        },
        "one_premise_lane": {
            "premise_count": 1,
            "premise_name": PREMISE_NAME,
            "source_emission_statement_count": "6/6",
            "source_object_field_count": "11/11",
            "final_connection_table_count": "6/8",
            "remaining_minimal_exits": [
                "emit selected good-cover Cech transition cocycles",
                "emit selected HYM/projective connection coefficients or equivalent End(E) operator values",
            ],
        },
        "forbidden_overclaims": [
            "do not report the one-premise lane as strict no-knob closure",
            "do not report the explicit local premise as an unpatched derivation",
            "do not claim final 8/8 connection tables until Cech/HYM geometric rows are emitted",
        ],
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
    }

    candidate = {
        "candidate": "MTTSelectedBN27OnePremiseSourceObjectAdoptionOrStrictCechHYM",
        "status": STATUS,
        "previous_status": current["status"],
        "next_required_artifact": NEXT,
        "closure_claimed": True,
        "full_no_knob_closure_claimed": False,
        "true_SM_equivalence_claimed": False,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "inputs": {
            "current": rel(CURRENT),
            "current_fields": rel(CURRENT_FIELDS),
            "current_statements": rel(CURRENT_STATEMENTS),
            "current_next": rel(CURRENT_NEXT),
            "principle": rel(PRINCIPLE),
            "premised_replay": rel(PREMISED_REPLAY),
            "route_a": rel(ROUTE_A),
            "route_b": rel(ROUTE_B),
            "connection_rows": rel(CONNECTION_ROWS),
            "postde_gate": rel(POSTDE_GATE),
        },
        "output_packets": {
            "strict_vs_onepremise_sourceobject_gate": rel(SOURCE_PACKET),
            "strict_vs_onepremise_source_statement_gate": rel(STATEMENT_PACKET),
            "strict_vs_onepremise_connection_row_gate": rel(CONNECTION_PACKET),
            "next_strictsource_or_geometric_cechhym_contract": rel(NEXT_PACKET),
        },
        "closure_decision": {
            "premise_name": PREMISE_NAME,
            "premise_count": 1,
            "premise_status": principle["premise_status"],
            "strict_source_object_field_count": 9,
            "one_premise_source_object_field_count": 11,
            "strict_source_statement_count": 3,
            "one_premise_source_statement_count": 6,
            "strict_final_connection_tables_accepted": 4,
            "one_premise_final_connection_tables_accepted": 6,
            "one_premise_newly_promoted_source_object_fields": STRICT_REMAINING_FIELDS,
            "one_premise_newly_promoted_source_statements": STRICT_REMAINING_STATEMENTS,
            "one_premise_newly_promoted_connection_rows": PREMISED_PROVENANCE_ROWS,
            "remaining_geometric_connection_rows": GEOMETRIC_REMAINING_ROWS,
            "strict_source_emission_principle_derived": False,
            "downstream_use_allowed_as_premised_local_source": True,
            "downstream_use_allowed_as_strict_unconditional_source": False,
            "strict_connection_tables_closed": False,
            "strict_no_knob_closed": False,
            "true_SM_equivalence_closed": False,
        },
        "theorem": {
            "name": "BN27OnePremiseSourceObjectAdoptionTheorem",
            "proved": True,
            "statement": (
                "The already audited SelectedBN27ThresholdSourceEmissionPrinciple may be adopted as exactly "
                "one explicit local source premise.  Under that counted premise, the BN27 source-object layer "
                "closes 11/11, the source-emission statements close 6/6, and the finitepart log(92160000) plus "
                "no-lift replay provenance rows close, giving a one-premise 6/8 connection-row lane.  The strict "
                "unconditional lane remains 9/11, 3/6, and 4/8; the two geometric Cech/HYM rows still require "
                "selected good-cover cocycles and selected HYM/projective coefficients or equivalent End(E) values."
            ),
        },
    }

    cert = {
        "certificate": "MTTSelectedBN27OnePremiseSourceObjectAdoptionOrStrictCechHYM",
        "status": STATUS,
        "candidate_path": rel(OUTPUT),
        "next_required_artifact": NEXT,
        "closure_claimed": True,
        "theorem_proved": True,
        "premise_name": PREMISE_NAME,
        "premise_count": 1,
        "strict_source_object_field_count": 9,
        "one_premise_source_object_field_count": 11,
        "strict_source_statement_count": 3,
        "one_premise_source_statement_count": 6,
        "strict_final_connection_tables_accepted": 4,
        "one_premise_final_connection_tables_accepted": 6,
        "one_premise_newly_promoted_connection_rows": PREMISED_PROVENANCE_ROWS,
        "remaining_geometric_connection_rows": GEOMETRIC_REMAINING_ROWS,
        "strict_source_emission_principle_derived": False,
        "downstream_use_allowed_as_premised_local_source": True,
        "downstream_use_allowed_as_strict_unconditional_source": False,
        "strict_connection_tables_closed": False,
        "strict_no_knob_closed": False,
        "true_SM_equivalence_closed": False,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
    }

    note = f"""# MTT Selected BN27 One-Premise Source-Object Adoption v1

## Theorem

`BN27OnePremiseSourceObjectAdoptionTheorem` is proved.

## Result

Strict lane remains:

- source statements: `3/6`
- source-object fields: `9/11`
- final connection tables: `4/8`

One-counted-premise lane adopts `{PREMISE_NAME}` as an explicit local source
premise:

- source statements: `6/6`
- source-object fields: `11/11`
- final connection tables: `6/8`

The two newly promoted connection rows in the one-premise lane are
`finitepart_log92160000_identity_from_values` and
`no_lifted_flags_connection_replay`.

The remaining rows, even in the one-premise lane, are geometric:

- `cech_transition_cocycles`
- `selected_HYM_or_projective_connection_coefficients`

This is not strict no-knob closure and not true SM equivalence.

## Next Artifact

`{NEXT}`
"""

    write_json(SOURCE_PACKET, source_packet)
    write_json(STATEMENT_PACKET, statement_packet)
    write_json(CONNECTION_PACKET, connection_packet)
    write_json(NEXT_PACKET, next_packet)
    write_json(OUTPUT, candidate)
    write_json(CERT, cert)
    NOTE.write_text(note, encoding="utf-8")

    print(json.dumps({"candidate": rel(OUTPUT), "status": STATUS}, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
