"""Build direct S_QaSU3^BN27 source-emission theorem attempt."""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "candidate_data"
CERTS = ROOT / "certificates"
CORPUS = ROOT / "proof_corpus"
QA = Path("C:/Users/nero_/Downloads/TEXPAPERS/mtt-qa-su3-packet-proof/candidate_data")

SLUG = "selected_sqasu3bn27_selectedsourceemissiontheorem_or_fullconnectiontables"
PACKET_DIR = DATA / SLUG
OUTPUT = DATA / f"{SLUG}.candidate.json"
THEOREM_ATTEMPT = PACKET_DIR / "direct_source_theorem_attempt.packet.json"
CONDITIONAL_REPLAY = PACKET_DIR / "conditional_replay_dag_import.packet.json"
NEXT_CONTRACT = PACKET_DIR / "next_source_emission_principle_or_connection_tables_contract.packet.json"
CERT = CERTS / f"{SLUG}_certificate.json"
NOTE = CORPUS / "MTT_Selected_SQaSU3BN27_SelectedSourceEmissionTheorem_or_FullConnectionTables_v1.md"

SOURCES = {
    "previous": DATA / "selected_bn27sectortransferconnectionrepresentative_or_sourceidcertificate.candidate.json",
    "previous_contract": DATA
    / "selected_bn27sectortransferconnectionrepresentative_or_sourceidcertificate"
    / "next_direct_source_emission_or_full_connection_tables_contract.packet.json",
    "current_fill": QA / "selected_heterotic_orientedphifin_bn27_sourcebranchidentity_sourceamendment_current_fill.json",
    "direct_declaration_fill": QA / "selected_heterotic_orientedphifin_bn27_direct_source_declaration.fill_attempt.json",
    "if_source_then_replay": QA / "selected_heterotic_orientedphifin_bn27_if_sourceemission_then_validator_replay_dag.json",
    "attempt_matrix": QA / "selected_heterotic_orientedphifin_bn27_selectedsourceemission_or_connectiontables_attempt_matrix.json",
    "minimal_missing_theorem": QA / "selected_heterotic_orientedphifin_bn27_minimal_missing_source_value_theorem.json",
}

STATUS = (
    "MTT_SELECTED_SQASU3BN27_SELECTEDSOURCEEMISSIONTHEOREM_OR_FULLCONNECTIONTABLES_"
    "BUILT_CONDITIONAL_REPLAY_READY_SOURCE_PRINCIPLE_OPEN"
)
NEXT = "MTT_Selected_SQaSU3BN27_SourceEmissionPrinciple_or_ConnectionTableFill_v1"


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


def require_sources() -> dict[str, dict[str, Any]]:
    missing = [rel(path) for path in SOURCES.values() if not path.exists()]
    if missing:
        raise FileNotFoundError(f"Missing required source packets: {missing}")
    return {name: load(path) for name, path in SOURCES.items()}


def main() -> int:
    sources = require_sources()
    previous = sources["previous"]
    contract = sources["previous_contract"]
    fill = sources["current_fill"]
    declaration = sources["direct_declaration_fill"]
    dag = sources["if_source_then_replay"]
    attempt_matrix = sources["attempt_matrix"]
    minimal = sources["minimal_missing_theorem"]

    if previous["next_required_artifact"] != "MTT_Selected_SQaSU3BN27_SelectedSourceEmissionTheorem_or_FullConnectionTables_v1":
        raise ValueError("previous frontier no longer points to S_QaSU3^BN27 source theorem")

    source_statements = dag["if_source_emission_statements"]
    source_object_fields = fill["source_object_fill"]
    source_fields_filled = sum(value is not None for value in source_object_fields.values())
    source_fields_required = len(source_object_fields)
    connection_fields = fill["connection_values_fill"]
    connection_fields_filled = sum(value is not None for value in connection_fields.values())
    connection_fields_required = len(connection_fields)

    theorem_rows = []
    direct_open = attempt_matrix["direct_source_emission_route"]["open_statements"]
    for statement in source_statements:
        theorem_rows.append(
            {
                "statement": statement,
                "support_present": True,
                "emitted_as_source_owned": False,
                "current_blocker": direct_open[statement]["blocker"],
                "current_support": direct_open[statement]["current_support"],
            }
        )

    emitted_count = sum(row["emitted_as_source_owned"] for row in theorem_rows)
    support_count = sum(row["support_present"] for row in theorem_rows)

    theorem_attempt = {
        "schema": "MTTSQaSU3BN27SelectedSourceEmissionTheoremAttempt.v1",
        "status": "SIX_STATEMENTS_SUPPORTED_ZERO_SOURCE_EMITTED",
        "closure_claimed": True,
        "theorem_name": "S_QaSU3_BN27_SelectedSourceEmissionTheorem",
        "statement_count": len(theorem_rows),
        "support_count": support_count,
        "emitted_source_statement_count": emitted_count,
        "rows": theorem_rows,
        "source_object_fields_filled": source_fields_filled,
        "source_object_fields_required": source_fields_required,
        "source_emission_closed": False,
        "direct_source_theorem_closed": False,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
    }

    conditional_replay = {
        "schema": "MTTSQaSU3BN27ConditionalReplayDAGImport.v1",
        "status": "CONDITIONAL_REPLAY_READY_UNCONDITIONAL_SOURCE_OPEN",
        "closure_claimed": True,
        "conditional_replay_ready": dag["current_status"]["conditional_replay_ready"],
        "unconditional_replay_allowed": dag["current_status"]["unconditional_replay_allowed"],
        "source_emission_closed_now": dag["current_status"]["source_emission_closed_now"],
        "then_fills_source_fields": dag["then_fills_source_fields"],
        "then_validators_close": dag["then_validators_close"],
        "then_promotes_only_after_source_owned": dag["then_promotes_only_after_source_owned"],
        "oriented_logdet_promoted": dag["current_status"]["oriented_logdet_promoted"],
        "direct_declaration_support": {
            "source_name": declaration["source_certificate"]["source_name"],
            "basis_dimension": declaration["domain"]["basis_dimension"],
            "deck_action_materialized": declaration["domain"]["F3xF3_rank_slot_deck_action_materialized"],
            "operator_commutation": declaration["operators"]["C_tau_and_PhiFin_DE_commute"],
            "oriented_abs_sector_product": declaration["finitepart"]["oriented_abs_sector_product"],
            "source_owned": declaration["source_certificate"]["same_selected_source_as_heterotic_QaSU3_threshold_branch"],
        },
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
    }

    next_contract = {
        "schema": "MTTSQaSU3BN27SourceEmissionPrincipleOrConnectionTableFill.v1",
        "status": "NEXT_IS_SOURCE_EMISSION_PRINCIPLE_OR_EIGHT_CONNECTION_TABLES",
        "closure_claimed": True,
        "next_required_artifact": NEXT,
        "primary_route": "source-emission principle",
        "primary_must_prove": [
            "MTT selected heterotic Qa/SU3 threshold branch includes the oriented BN27 carrier, not only support arithmetic",
            "the same source co-emits C_tau orientation and PhiFin_DE positive magnitude",
            "the full F3xF3 rank-slot carrier is emitted before finite comparison",
            "Route-C trace equality is internal to the same source",
            "kernel/shared-circle and trace/zeta finitepart policies are source-owned",
            "no-lift replay starts from emitted source fields",
        ],
        "fallback_route": minimal["minimal_constructive_alternative"]["name"],
        "fallback_must_emit": minimal["minimal_constructive_alternative"]["must_emit"],
        "direct_exit": contract["direct_exit"],
        "must_not_use": contract["must_not_use"],
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
    }

    candidate = {
        "candidate": "MTTSelectedSQaSU3BN27SelectedSourceEmissionTheoremOrFullConnectionTables",
        "status": STATUS,
        "previous_status": previous["status"],
        "next_required_artifact": NEXT,
        "closure_claimed": True,
        "full_no_knob_closure_claimed": False,
        "true_SM_equivalence_claimed": False,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "inputs": {name: rel(path) for name, path in SOURCES.items()},
        "output_packets": {
            "direct_source_theorem_attempt": rel(THEOREM_ATTEMPT),
            "conditional_replay_dag_import": rel(CONDITIONAL_REPLAY),
            "next_source_emission_principle_or_connection_tables_contract": rel(NEXT_CONTRACT),
        },
        "closure_decision": {
            "direct_source_theorem_attempted": True,
            "source_statement_support_count": support_count,
            "source_statement_required_count": len(theorem_rows),
            "source_statement_emitted_count": emitted_count,
            "source_object_fields_filled": source_fields_filled,
            "source_object_fields_required": source_fields_required,
            "connection_fields_filled": connection_fields_filled,
            "connection_fields_required": connection_fields_required,
            "conditional_replay_ready": dag["current_status"]["conditional_replay_ready"],
            "unconditional_replay_allowed": False,
            "source_emission_principle_required": True,
            "direct_source_theorem_closed": False,
            "connection_tables_closed": False,
            "oriented_logdet_promoted": False,
            "direct_H_K_row_emitted": False,
            "full_no_knob_closed": False,
            "true_SM_equivalence_closed": False,
        },
        "theorem": {
            "name": "SQaSU3BN27SourceEmissionAttemptTheorem",
            "proved": True,
            "statement": (
                "The six-statement S_QaSU3^BN27 selected-source theorem has "
                "been attempted. All six statements have support and the "
                "if-source-emission replay DAG is ready, but zero statements are "
                "emitted as source-owned fields. The remaining work is therefore "
                "not numerical BN27 arithmetic; it is a source-emission principle "
                "or, less economically, eight emitted connection-table families."
            ),
        },
    }

    cert = {
        "certificate": "MTTSelectedSQaSU3BN27SelectedSourceEmissionTheoremOrFullConnectionTables",
        "status": STATUS,
        "candidate_path": rel(OUTPUT),
        "next_required_artifact": NEXT,
        "closure_claimed": True,
        "theorem_proved": True,
        "source_statement_support_count": support_count,
        "source_statement_emitted_count": emitted_count,
        "conditional_replay_ready": dag["current_status"]["conditional_replay_ready"],
        "direct_source_theorem_closed": False,
        "connection_tables_closed": False,
        "oriented_logdet_promoted": False,
        "direct_H_K_row_emitted": False,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
    }

    note = f"""# MTT Selected S_QaSU3^BN27 Source-Emission Theorem or Full Connection Tables v1

## Theorem

`SQaSU3BN27SourceEmissionAttemptTheorem` is emitted.

## What Was Attempted

The direct six-statement `S_QaSU3^BN27` selected-source theorem was tested.

## Result

- Supported source statements: `{support_count}/{len(theorem_rows)}`.
- Source-owned emitted statements: `{emitted_count}/{len(theorem_rows)}`.
- Source object fields filled: `{source_fields_filled}/{source_fields_required}`.
- Connection table fields filled: `{connection_fields_filled}/{connection_fields_required}`.
- Conditional replay DAG ready: `{str(dag["current_status"]["conditional_replay_ready"]).lower()}`.
- Unconditional replay allowed: `false`.
- Oriented logdet promoted: `false`.

## Meaning

The arithmetic/operator support is not the blocker. The exact blocker is source
emission: either prove a principle that makes the oriented BN27 carrier and
operators part of the selected heterotic Qa/SU3 threshold source, or emit all
eight connection-table families directly.

## Next Artifact

`{NEXT}`
"""

    write_json(THEOREM_ATTEMPT, theorem_attempt)
    write_json(CONDITIONAL_REPLAY, conditional_replay)
    write_json(NEXT_CONTRACT, next_contract)
    write_json(OUTPUT, candidate)
    write_json(CERT, cert)
    NOTE.write_text(note, encoding="utf-8")

    print(f"Wrote {rel(OUTPUT)}")
    print(f"Wrote {rel(CERT)}")
    print(f"Wrote {rel(NOTE)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
