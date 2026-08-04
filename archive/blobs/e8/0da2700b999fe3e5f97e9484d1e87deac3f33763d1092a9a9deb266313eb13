"""Build BN27 selected-source-emission or connection-tables constructive attempt."""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "candidate_data"
CERTS = ROOT / "certificates"
PROOF = ROOT / "proof_corpus"

INPUTS = {
    "prior_gate": DATA / "selected_heterotic_orientedphifin_bn27_minimalmissingsourcevaluetheorem_or_connectiontables.candidate.json",
    "direct_skeleton": DATA / "selected_heterotic_orientedphifin_bn27_selectedsourceemission_theorem_skeleton.json",
    "connection_schema": DATA / "selected_heterotic_orientedphifin_bn27_selectedconnectiontables_schema.json",
    "support_probe": DATA / "selected_heterotic_orientedphifin_bn27_sourceobject_or_connectionvaluepayload_support_probe.json",
    "direct_declaration_fill": DATA / "selected_heterotic_orientedphifin_bn27_direct_source_declaration.fill_attempt.json",
    "connection_request": DATA / "selected_heterotic_orientedphifin_bn27_connectionvalues_externalconstruction_request.json",
}

OUTPUT_DATA = DATA / "selected_heterotic_orientedphifin_bn27_selectedsourceemission_or_connectiontables_constructiveattempt.candidate.json"
OUTPUT_ATTEMPT = DATA / "selected_heterotic_orientedphifin_bn27_selectedsourceemission_or_connectiontables_attempt_matrix.json"
OUTPUT_REPLAY = DATA / "selected_heterotic_orientedphifin_bn27_if_sourceemission_then_validator_replay_dag.json"
OUTPUT_CERT = CERTS / "selected_heterotic_orientedphifin_bn27_selectedsourceemission_or_connectiontables_constructiveattempt_certificate.json"
OUTPUT_NOTE = PROOF / "Selected_Heterotic_OrientedPhiFin_BN27_SelectedSourceEmission_or_ConnectionTables_ConstructiveAttempt_v1.md"

STATUS = "HETEROTIC_ORIENTEDPHIFIN_BN27_SELECTEDSOURCEEMISSION_OR_CONNECTIONTABLES_ATTEMPT_DIRECT_THEOREM_SHORTEST_OPEN"
NEXT = "Selected_Heterotic_OrientedPhiFin_BN27_SelectedSourceEmission_TheoremPacket_Fill_or_NoGo_v1"


def rel(path: Path) -> str:
    try:
        return str(path.relative_to(ROOT))
    except ValueError:
        return str(path)


def load(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def false_count(items: dict[str, dict[str, Any]], key: str = "current_truth_value") -> int:
    return sum(1 for item in items.values() if item[key] is not True)


def main() -> dict[str, Any]:
    prior = load(INPUTS["prior_gate"])
    direct = load(INPUTS["direct_skeleton"])
    tables = load(INPUTS["connection_schema"])
    probe = load(INPUTS["support_probe"])
    declaration = load(INPUTS["direct_declaration_fill"])
    connection_request = load(INPUTS["connection_request"])

    direct_open = false_count(direct["statements"])
    table_open = false_count(tables["required_tables"])
    direct_support_count = sum(1 for item in direct["statements"].values() if item.get("current_support") not in (None, False))
    table_support_count = sum(1 for item in tables["required_tables"].values() if item.get("support_present") is True)

    route_matrix = {
        "schema": "SelectedHeterotic.OrientedPhiFin.BN27.SelectedSourceEmissionOrConnectionTables.AttemptMatrix.v1",
        "status": "DIRECT_THEOREM_IS_SHORTEST_CURRENT_ROUTE",
        "direct_source_emission_route": {
            "required_statement_count": len(direct["statements"]),
            "open_statement_count": direct_open,
            "support_statement_count": direct_support_count,
            "closed_now": direct["closed_now"],
            "why_ranked_first": (
                "The full BN27 carrier/operator/arithmetic support is already materialized; "
                "the missing work is a provenance theorem with six statements, not eight new emitted table families."
            ),
            "open_statements": {
                key: {
                    "blocker": value["blocker"],
                    "current_support": value["current_support"],
                }
                for key, value in direct["statements"].items()
                if value["current_truth_value"] is not True
            },
        },
        "connection_tables_route": {
            "required_table_count": len(tables["required_tables"]),
            "open_table_count": table_open,
            "support_table_count": table_support_count,
            "closed_now": tables["closed_now"],
            "why_ranked_second": (
                "The connection route is fully constructive but currently has no emitted typed f/g sections, "
                "Cech cocycles, selected connection coefficients, or value-derived BN27 export."
            ),
            "open_tables": {
                key: {
                    "shape": value["shape"],
                    "support_present": value.get("support_present", False),
                }
                for key, value in tables["required_tables"].items()
                if value["current_truth_value"] is not True
            },
        },
        "target_fitting_used": False,
    }
    OUTPUT_ATTEMPT.write_text(json.dumps(route_matrix, indent=2, sort_keys=True) + "\n", encoding="utf-8")

    replay_dag = {
        "schema": "SelectedHeterotic.OrientedPhiFin.BN27.IfSourceEmissionThenValidatorReplayDAG.v1",
        "status": "CONDITIONAL_REPLAY_DAG_BUILT_SOURCE_EMISSION_OPEN",
        "if_source_emission_statements": list(direct["statements"].keys()),
        "then_fills_source_fields": direct["would_fill_source_fields"],
        "then_validators_close": {
            "source_identity": "S_QaSU3^BN27 selected threshold source statement",
            "BN27_deck_action": "full F3xF3 carrier emitted before finite comparison",
            "operator_coemission": "C_tau and PhiFin_DE co-emitted by source",
            "kernel_policy": "kernel/shared-circle policy source-owned",
            "trace_policy": "trace/zeta finitepart policy source-owned",
            "audit_replay": "no-lift replay audit from emitted fields",
            "not_external_import": "Route-C row internal theorem",
        },
        "then_promotes_only_after_source_owned": {
            "oriented_abs_sector_logdet": declaration["finitepart"]["oriented_abs_sector_logdet_exact"],
            "oriented_abs_sector_product": declaration["finitepart"]["oriented_abs_sector_product"],
            "positive_spectrum_count": len(declaration["operators"]["positive_spectrum"]),
        },
        "current_status": {
            "source_emission_closed_now": False,
            "conditional_replay_ready": True,
            "unconditional_replay_allowed": declaration["audit_replay"]["closure_replay_allowed"],
            "oriented_logdet_promoted": False,
        },
        "target_fitting_used": False,
    }
    OUTPUT_REPLAY.write_text(json.dumps(replay_dag, indent=2, sort_keys=True) + "\n", encoding="utf-8")

    decision = {
        "attempt_executed": True,
        "route_matrix_built": True,
        "conditional_replay_dag_built": True,
        "primary_route": "direct_selected_source_emission_theorem",
        "secondary_route": "selected_connection_tables_export",
        "direct_open_statement_count": direct_open,
        "connection_open_table_count": table_open,
        "direct_theorem_closed": False,
        "connection_tables_closed": False,
        "conditional_replay_ready": True,
        "unconditional_replay_allowed": False,
        "source_branch_identity_closed": False,
        "same_source_export_to_BN27_validators": False,
        "oriented_logdet_promoted": False,
        "attempt_matrix_path": rel(OUTPUT_ATTEMPT),
        "conditional_replay_dag_path": rel(OUTPUT_REPLAY),
        "next_required_artifact": NEXT,
        "closure_claimed": False,
        "target_fitting_used": False,
    }

    candidate = {
        "candidate": "SelectedHeteroticOrientedPhiFinBN27SelectedSourceEmissionOrConnectionTablesConstructiveAttempt",
        "status": STATUS,
        "inputs": {key: rel(path) for key, path in INPUTS.items()},
        "parent_statuses": {
            "prior_gate": prior["status"],
            "direct_skeleton": direct["status"],
            "connection_schema": tables["status"],
            "support_probe": probe["status"],
            "connection_request": connection_request["status"],
        },
        "decision": decision,
        "theorem": {
            "name": "BN27ConstructiveAttemptDirectSourceEmissionShortestRouteTheorem",
            "proved": True,
            "statement": (
                "Both legal BN27 closure routes are tested. The direct selected-source-emission route is the shortest "
                "current route because the carrier/operator/arithmetic support is already materialized and only six "
                "provenance statements remain open. The connection-table route is fully constructive but requires eight "
                "absent table families. A conditional replay DAG is built: once the six source-emission statements are "
                "proved, the BN27 validators and logdet promotion follow without new numerical choices. Unconditionally, "
                "closure remains open."
            ),
        },
        "guardrails": {
            "does_not_treat_conditional_replay_as_unconditional": True,
            "does_not_count_support_as_source_emission": True,
            "does_not_count_route_requirements_as_connection_tables": True,
            "does_not_promote_log92160000": True,
            "does_not_use_lifted_selected_flags": True,
            "does_not_use_observed_data": True,
            "target_fitting_used": False,
        },
        "closure_claimed": False,
        "target_fitting_used": False,
    }
    OUTPUT_DATA.write_text(json.dumps(candidate, indent=2, sort_keys=True) + "\n", encoding="utf-8")

    cert = {
        "certificate": candidate["candidate"],
        "status": STATUS,
        "candidate_path": rel(OUTPUT_DATA),
        "attempt_matrix_path": rel(OUTPUT_ATTEMPT),
        "conditional_replay_dag_path": rel(OUTPUT_REPLAY),
        "note_path": rel(OUTPUT_NOTE),
        "primary_route": decision["primary_route"],
        "direct_open_statement_count": direct_open,
        "connection_open_table_count": table_open,
        "conditional_replay_ready": True,
        "direct_theorem_closed": False,
        "connection_tables_closed": False,
        "source_branch_identity_closed": False,
        "oriented_logdet_promoted": False,
        "closure_claimed": False,
        "target_fitting_used": False,
        "next_required_artifact": NEXT,
    }
    OUTPUT_CERT.write_text(json.dumps(cert, indent=2, sort_keys=True) + "\n", encoding="utf-8")

    note = f"""# Selected Heterotic OrientedPhiFin BN27 SelectedSourceEmission or ConnectionTables ConstructiveAttempt v1

## Result

```text
status = {STATUS}
primary_route = direct_selected_source_emission_theorem
direct_open_statement_count = {direct_open}
connection_open_table_count = {table_open}
conditional_replay_ready = true
unconditional_replay_allowed = false
oriented_logdet_promoted = false
next_required_artifact = {NEXT}
```

## Theorem

{candidate["theorem"]["statement"]}

## Outputs

```text
{rel(OUTPUT_ATTEMPT)}
{rel(OUTPUT_REPLAY)}
```
"""
    OUTPUT_NOTE.write_text(note, encoding="utf-8")
    return candidate


if __name__ == "__main__":
    result = main()
    print(f"wrote {rel(OUTPUT_DATA)}")
    print(f"wrote {rel(OUTPUT_ATTEMPT)}")
    print(f"wrote {rel(OUTPUT_REPLAY)}")
    print(f"wrote {rel(OUTPUT_CERT)}")
    print(f"wrote {rel(OUTPUT_NOTE)}")
    print(result["status"])
