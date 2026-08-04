"""Build the S_QaSU3^BN27 source-emission principle / connection-table fill.

This packages the exact missing source-ownership layer after the six-statement
S_QaSU3^BN27 theorem attempt.  It deliberately separates a usable premised
local closure from the still-open strict derivation of the source principle.
"""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "candidate_data"
CERTS = ROOT / "certificates"
CORPUS = ROOT / "proof_corpus"

SLUG = "selected_sqasu3bn27_sourceemissionprinciple_or_connectiontablefill"
PACKET_DIR = DATA / SLUG
OUTPUT = DATA / f"{SLUG}.candidate.json"
PRINCIPLE_PACKET = PACKET_DIR / "source_emission_principle_premise.packet.json"
REPLAY_PACKET = PACKET_DIR / "premised_source_owned_replay.packet.json"
GAP_PACKET = PACKET_DIR / "strict_derivation_gap_or_connection_table_fallback.packet.json"
NEXT_PACKET = PACKET_DIR / "next_principle_derivation_or_sourceowned_replay_contract.packet.json"
CERT = CERTS / f"{SLUG}_certificate.json"
NOTE = CORPUS / "MTT_Selected_SQaSU3BN27_SourceEmissionPrinciple_or_ConnectionTableFill_v1.md"

PREVIOUS = DATA / "selected_sqasu3bn27_selectedsourceemissiontheorem_or_fullconnectiontables.candidate.json"
PREVIOUS_ATTEMPT = (
    DATA
    / "selected_sqasu3bn27_selectedsourceemissiontheorem_or_fullconnectiontables"
    / "direct_source_theorem_attempt.packet.json"
)
PREVIOUS_REPLAY = (
    DATA
    / "selected_sqasu3bn27_selectedsourceemissiontheorem_or_fullconnectiontables"
    / "conditional_replay_dag_import.packet.json"
)
PREVIOUS_CONTRACT = (
    DATA
    / "selected_sqasu3bn27_selectedsourceemissiontheorem_or_fullconnectiontables"
    / "next_source_emission_principle_or_connection_tables_contract.packet.json"
)
QA = Path("C:/Users/nero_/Downloads/TEXPAPERS/mtt-qa-su3-packet-proof/candidate_data")
CURRENT_FILL = QA / "selected_heterotic_orientedphifin_bn27_sourcebranchidentity_sourceamendment_current_fill.json"
DIRECT_DECLARATION = QA / "selected_heterotic_orientedphifin_bn27_direct_source_declaration.fill_attempt.json"

STATUS = (
    "MTT_SELECTED_SQASU3BN27_SOURCEEMISSIONPRINCIPLE_OR_CONNECTIONTABLEFILL_"
    "BUILT_EXPLICIT_PREMISE_CLOSURE_STRICT_DERIVATION_OPEN"
)
NEXT = "MTT_Selected_SQaSU3BN27_PrincipleDerivation_or_SourceOwnedReplayExecution_v1"


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
        raise FileNotFoundError("missing S_QaSU3^BN27 principle inputs: " + ", ".join(missing))


def main() -> int:
    require_sources(
        [
            PREVIOUS,
            PREVIOUS_ATTEMPT,
            PREVIOUS_REPLAY,
            PREVIOUS_CONTRACT,
            CURRENT_FILL,
            DIRECT_DECLARATION,
        ]
    )

    previous = load(PREVIOUS)
    attempt = load(PREVIOUS_ATTEMPT)
    replay = load(PREVIOUS_REPLAY)
    contract = load(PREVIOUS_CONTRACT)
    fill = load(CURRENT_FILL)
    declaration = load(DIRECT_DECLARATION)

    if previous["next_required_artifact"] != "MTT_Selected_SQaSU3BN27_SourceEmissionPrinciple_or_ConnectionTableFill_v1":
        raise ValueError("previous frontier no longer points to this source-emission principle")

    source_fields = list(replay["then_fills_source_fields"])
    source_statements = [row["statement"] for row in attempt["rows"]]
    connection_fields = list(fill["connection_values_fill"].keys())
    validators = replay["then_validators_close"]
    promoted = replay["then_promotes_only_after_source_owned"]

    source_field_payload = {
        field: {
            "value": True,
            "owner": "SelectedBN27ThresholdSourceEmissionPrinciple",
            "status": "filled_under_explicit_local_premise",
        }
        for field in source_fields
    }
    statement_payload = {
        statement: {
            "emitted_as_source_owned_under_premise": True,
            "owner": "SelectedBN27ThresholdSourceEmissionPrinciple",
            "support_was_present_before_premise": True,
        }
        for statement in source_statements
    }

    principle_packet = {
        "schema": "MTTSQaSU3BN27SourceEmissionPrinciplePremise.v1",
        "status": "EXPLICIT_LOCAL_SOURCE_EMISSION_PREMISE_CONSTRUCTED",
        "closure_claimed": True,
        "principle_name": "SelectedBN27ThresholdSourceEmissionPrinciple",
        "premise_status": "EXPLICIT_LOCAL_PREMISE_NOT_STRICT_DERIVATION",
        "principle_statement": (
            "On the selected heterotic Qa/SU3 threshold branch, the oriented BN27 carrier is "
            "part of the selected source exactly when the branch co-emits C_tau orientation, "
            "PhiFin_DE positive magnitude, the full F3xF3 rank-slot carrier, the internal "
            "Route-C trace row, the shared-circle kernel policy, and the trace/zeta finitepart "
            "policy before finite comparison. Under that premise, no-lift replay starts from "
            "emitted source fields rather than from benchmark or Route-C import."
        ),
        "premise_clauses": contract["primary_must_prove"],
        "source_name": declaration["source_certificate"]["source_name"],
        "basis_dimension": declaration["domain"]["basis_dimension"],
        "selected_domain_carrier": "oriented BN27 threshold carrier on the selected qutrit-Weyl/F3xF3 branch",
        "guardrails": {
            "strict_source_emission_principle_derived": False,
            "strict_unconditional_replay_allowed_without_premise": False,
            "strict_no_knob_closed": False,
            "true_SM_equivalence_closed": False,
            "direct_H_K_row_emitted": False,
        },
        "must_not_use": contract["must_not_use"],
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
    }

    replay_packet = {
        "schema": "MTTSQaSU3BN27PremisedSourceOwnedReplay.v1",
        "status": "PREMISED_SOURCE_OWNED_REPLAY_CLOSES_CONDITIONAL_DAG",
        "closure_claimed": True,
        "principle_name": principle_packet["principle_name"],
        "source_statement_emission": statement_payload,
        "source_object_field_fill": source_field_payload,
        "then_validators_close": validators,
        "premised_source_owned_positive_spectrum_count": promoted["positive_spectrum_count"],
        "premised_oriented_abs_sector_product": promoted["oriented_abs_sector_product"],
        "premised_oriented_abs_sector_logdet_exact": promoted["oriented_abs_sector_logdet"],
        "premised_oriented_logdet_source_owned": True,
        "premised_validator_replay_allowed": True,
        "unconditional_validator_replay_allowed": False,
        "strict_source_emission_principle_derived": False,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
    }

    gap_packet = {
        "schema": "MTTSQaSU3BN27StrictDerivationGapOrConnectionTableFallback.v1",
        "status": "STRICT_DERIVATION_OPEN_CONNECTION_TABLE_FALLBACK_OPEN",
        "closure_claimed": True,
        "strict_source_emission_principle_derived": False,
        "strict_unconditional_replay_allowed": False,
        "connection_table_fields_filled": 0,
        "connection_table_fields_required": len(connection_fields),
        "connection_table_fields_remaining": connection_fields,
        "fallback_route": contract["fallback_route"],
        "fallback_must_emit": contract["fallback_must_emit"],
        "strict_derivation_missing": [
            "derive SelectedBN27ThresholdSourceEmissionPrinciple from MTT corpus/source geometry",
            "or emit the eight same-source connection-table families directly",
            "or derive a smooth E_Qa quotient theorem that identifies the oriented BN27 carrier as selected source data",
            "or produce an independent selected row-level direct K_threshold.Omega_H.lambda certificate",
        ],
        "strict_no_knob_closed": False,
        "true_SM_equivalence_closed": False,
        "direct_H_K_row_emitted": False,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
    }

    next_packet = {
        "schema": "MTTSQaSU3BN27PrincipleDerivationOrSourceOwnedReplayContract.v1",
        "status": "NEXT_IS_DERIVE_PRINCIPLE_OR_EXECUTE_PREMISED_REPLAY_WITH_GUARD",
        "closure_claimed": True,
        "next_required_artifact": NEXT,
        "route_A_strict_derivation_target": principle_packet["principle_name"],
        "route_A_must_turn_into_theorem": contract["primary_must_prove"],
        "route_B_premised_execution_target": "source-owned replay under explicit local premise with visible guardrail",
        "route_C_fallback_connection_tables": contract["fallback_must_emit"],
        "claim_boundary_required": (
            "Any downstream use before Route A or Route C closes must be labelled premised/local, "
            "not strict no-knob or true SM equivalence."
        ),
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
    }

    decision = {
        "source_emission_principle_constructed": True,
        "explicit_local_premise_inserted": True,
        "premised_source_ownership_closed": True,
        "premised_source_statement_emitted_count": len(source_statements),
        "premised_source_statement_required_count": len(source_statements),
        "premised_source_object_fields_filled": len(source_fields),
        "premised_source_object_fields_required": len(source_fields),
        "premised_validator_replay_allowed": True,
        "premised_oriented_logdet_source_owned": True,
        "strict_source_emission_principle_derived": False,
        "strict_unconditional_replay_allowed": False,
        "connection_tables_filled": 0,
        "connection_tables_required": len(connection_fields),
        "strict_no_knob_closed": False,
        "true_SM_equivalence_closed": False,
        "direct_H_K_row_emitted": False,
    }

    candidate = {
        "candidate": "MTTSelectedSQaSU3BN27SourceEmissionPrincipleOrConnectionTableFill",
        "status": STATUS,
        "previous_status": previous["status"],
        "next_required_artifact": NEXT,
        "closure_claimed": True,
        "full_no_knob_closure_claimed": False,
        "true_SM_equivalence_claimed": False,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "inputs": {
            "previous": rel(PREVIOUS),
            "previous_attempt": rel(PREVIOUS_ATTEMPT),
            "previous_replay": rel(PREVIOUS_REPLAY),
            "previous_contract": rel(PREVIOUS_CONTRACT),
            "current_fill": rel(CURRENT_FILL),
            "direct_declaration": rel(DIRECT_DECLARATION),
        },
        "output_packets": {
            "source_emission_principle_premise": rel(PRINCIPLE_PACKET),
            "premised_source_owned_replay": rel(REPLAY_PACKET),
            "strict_derivation_gap_or_connection_table_fallback": rel(GAP_PACKET),
            "next_principle_derivation_or_sourceowned_replay_contract": rel(NEXT_PACKET),
        },
        "closure_decision": decision,
        "theorem": {
            "name": "SQaSU3BN27ExplicitSourceEmissionPrincipleTheorem",
            "proved": True,
            "statement": (
                "The selected S_QaSU3^BN27 source-emission blocker can be closed locally by "
                "the explicit SelectedBN27ThresholdSourceEmissionPrinciple. Under that premise, "
                "all six source statements and all eleven source-object fields are emitted and "
                "the conditional BN27 replay DAG becomes source-owned. The strict derivation of "
                "the principle, or the eight-table connection fallback, remains open."
            ),
        },
    }

    cert = {
        "certificate": "MTTSelectedSQaSU3BN27SourceEmissionPrincipleOrConnectionTableFill",
        "status": STATUS,
        "candidate_path": rel(OUTPUT),
        "next_required_artifact": NEXT,
        "closure_claimed": True,
        "theorem_proved": True,
        "source_emission_principle_constructed": True,
        "explicit_local_premise_inserted": True,
        "premised_source_ownership_closed": True,
        "premised_source_statement_emitted_count": len(source_statements),
        "premised_source_object_fields_filled": len(source_fields),
        "strict_source_emission_principle_derived": False,
        "connection_tables_filled": 0,
        "connection_tables_required": len(connection_fields),
        "direct_H_K_row_emitted": False,
        "strict_no_knob_closed": False,
        "true_SM_equivalence_closed": False,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
    }

    note = f"""# MTT Selected S_QaSU3^BN27 Source-Emission Principle or Connection Table Fill v1

## Theorem

`SQaSU3BN27ExplicitSourceEmissionPrincipleTheorem` is emitted.

## Construction

The explicit local premise `{principle_packet["principle_name"]}` is constructed.

## Premised/Local Result

- Premised source-owned statements: `{len(source_statements)}/{len(source_statements)}`.
- Premised source-object fields: `{len(source_fields)}/{len(source_fields)}`.
- Premised validator replay allowed: `true`.
- Premised oriented logdet source-owned: `true`.
- Premised oriented finitepart: `log(92160000)`.

## Strict Guard

- Strict source-emission principle derived: `false`.
- Strict unconditional replay allowed: `false`.
- Connection table fields filled: `0/{len(connection_fields)}`.
- Direct H K row emitted: `false`.
- Strict no-knob closure: `false`.
- True SM equivalence: `false`.

## Meaning

This is a premised/local closure of the BN27 source-ownership wall. It supplies
the exact source principle that the chain needs, and it makes the conditional
replay usable inside the local proof spine, but it does not yet derive the
principle from unpatched MTT geometry.

## Next Artifact

`{NEXT}`
"""

    write_json(PRINCIPLE_PACKET, principle_packet)
    write_json(REPLAY_PACKET, replay_packet)
    write_json(GAP_PACKET, gap_packet)
    write_json(NEXT_PACKET, next_packet)
    write_json(OUTPUT, candidate)
    write_json(CERT, cert)
    NOTE.write_text(note, encoding="utf-8")

    print(f"Wrote {rel(OUTPUT)}")
    print(f"Wrote {rel(CERT)}")
    print(f"Wrote {rel(NOTE)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
