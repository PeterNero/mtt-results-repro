"""Build BN27 minimal missing source-value theorem / connection-tables gate."""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "candidate_data"
CERTS = ROOT / "certificates"
PROOF = ROOT / "proof_corpus"

INPUTS = {
    "missing_theorem": DATA / "selected_heterotic_orientedphifin_bn27_minimal_missing_source_value_theorem.json",
    "support_probe": DATA / "selected_heterotic_orientedphifin_bn27_sourceobject_or_connectionvaluepayload_support_probe.json",
    "fill_attempt": DATA / "selected_heterotic_orientedphifin_bn27_sourceobject_or_connectionvaluepayload_fillattempt.candidate.json",
    "direct_declaration_fill": DATA / "selected_heterotic_orientedphifin_bn27_direct_source_declaration.fill_attempt.json",
    "external_connection_request": DATA / "selected_heterotic_orientedphifin_bn27_connectionvalues_externalconstruction_request.json",
}

OUTPUT_DATA = DATA / "selected_heterotic_orientedphifin_bn27_minimalmissingsourcevaluetheorem_or_connectiontables.candidate.json"
OUTPUT_DIRECT = DATA / "selected_heterotic_orientedphifin_bn27_selectedsourceemission_theorem_skeleton.json"
OUTPUT_TABLES = DATA / "selected_heterotic_orientedphifin_bn27_selectedconnectiontables_schema.json"
OUTPUT_CERT = CERTS / "selected_heterotic_orientedphifin_bn27_minimalmissingsourcevaluetheorem_or_connectiontables_certificate.json"
OUTPUT_NOTE = PROOF / "Selected_Heterotic_OrientedPhiFin_BN27_MinimalMissingSourceValueTheorem_or_ConnectionTables_v1.md"

STATUS = "HETEROTIC_ORIENTEDPHIFIN_BN27_MINIMAL_MISSING_THEOREM_OR_TABLES_BUILT_VALUES_STILL_OPEN"
NEXT = "Selected_Heterotic_OrientedPhiFin_BN27_SelectedSourceEmission_or_ConnectionTables_ConstructiveAttempt_v1"


def rel(path: Path) -> str:
    try:
        return str(path.relative_to(ROOT))
    except ValueError:
        return str(path)


def load(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def main() -> dict[str, Any]:
    missing = load(INPUTS["missing_theorem"])
    probe = load(INPUTS["support_probe"])
    fill = load(INPUTS["fill_attempt"])
    declaration = load(INPUTS["direct_declaration_fill"])
    external = load(INPUTS["external_connection_request"])

    direct_skeleton = {
        "schema": "SelectedHeterotic.OrientedPhiFin.BN27.SelectedSourceEmissionTheoremSkeleton.v1",
        "status": "THEOREM_SKELETON_BUILT_SOURCE_STATEMENTS_OPEN",
        "theorem_name": missing["minimal_direct_theorem"]["name"],
        "statements": {
            "S_QaSU3_BN27_is_selected_threshold_source": {
                "required": True,
                "current_truth_value": False,
                "current_support": declaration["source_certificate"]["source_name"],
                "blocker": declaration["source_certificate"]["why_open"],
            },
            "full_F3xF3_carrier_emitted_before_finite_comparison": {
                "required": True,
                "current_truth_value": False,
                "current_support": {
                    "basis_dimension": declaration["domain"]["basis_dimension"],
                    "basis_id": declaration["domain"]["basis_id"],
                    "deck_action_materialized": declaration["domain"]["F3xF3_rank_slot_deck_action_materialized"],
                },
                "blocker": "carrier is materialized but deck/domain ownership is false",
            },
            "C_tau_and_PhiFin_DE_coemitted_by_source": {
                "required": True,
                "current_truth_value": False,
                "current_support": declaration["operators"]["C_tau_and_PhiFin_DE_commute"],
                "blocker": "source_emits_C_tau and source_emits_PhiFin_DE are false",
            },
            "RouteC_row_internal_not_external": {
                "required": True,
                "current_truth_value": declaration["source_certificate"]["not_routec_or_benchmark_import"],
                "current_support": "Route-C support and audit replay exist",
                "blocker": "not_routec_or_benchmark_import is false",
            },
            "kernel_and_trace_policies_source_owned": {
                "required": True,
                "current_truth_value": declaration["finitepart"]["kernel_trace_policy_source_owned"],
                "current_support": {
                    "kernel_policy": declaration["domain"]["kernel_shared_circle_no_double_count_policy"],
                    "finitepart_relative_to_full_orbit_source": declaration["finitepart"]["finitepart_trace_identity_relative_to_full_orbit_source"],
                },
                "blocker": "kernel_trace_policy_source_owned is false",
            },
            "no_lift_replay_audit_from_emitted_fields": {
                "required": True,
                "current_truth_value": declaration["audit_replay"]["closure_replay_allowed"],
                "current_support": declaration["audit_replay"]["support_replay_ready"],
                "blocker": "closure replay is blocked by open source leaves",
            },
        },
        "would_fill_source_fields": missing["minimal_direct_theorem"]["would_fill_source_fields"],
        "target_fitting_used": False,
    }
    direct_skeleton["closed_now"] = all(item["current_truth_value"] is True for item in direct_skeleton["statements"].values())
    OUTPUT_DIRECT.write_text(json.dumps(direct_skeleton, indent=2, sort_keys=True) + "\n", encoding="utf-8")

    connection_schema = {
        "schema": "SelectedHeterotic.OrientedPhiFin.BN27.SelectedConnectionTablesSchema.v1",
        "status": "CONNECTION_TABLE_SCHEMA_BUILT_TABLES_ABSENT",
        "theorem_name": missing["minimal_constructive_alternative"]["name"],
        "required_tables": {
            "typed_f_sections": {
                "required": True,
                "current_truth_value": False,
                "shape": "five typed f_i section representatives in selected Cech/gerbe frame",
            },
            "typed_g_sections": {
                "required": True,
                "current_truth_value": False,
                "shape": "five typed g_i section representatives in selected Cech/gerbe frame",
            },
            "cech_transition_cocycles": {
                "required": True,
                "current_truth_value": False,
                "shape": "transition/cocycle tables for the selected cover and BN27 export",
            },
            "g_after_f_zero_exactness_certificate": {
                "required": True,
                "current_truth_value": False,
                "shape": "machine-checkable g o f = 0 plus exactness/local-freeness certificate",
            },
            "selected_connection_coefficients": {
                "required": True,
                "current_truth_value": False,
                "shape": "selected HYM/Strominger/projective connection coefficients with residual or exact equations",
            },
            "BN27_operator_export": {
                "required": True,
                "current_truth_value": False,
                "shape": "BN27 D_E/Riesz/Green/kernel/trace export from emitted values, not imported support",
                "support_present": external["external_connection_values_route"]["acceptance_fields"]["BN27_operator_export_to_DE_Riesz_Green_kernel_trace"] is not None,
            },
            "finitepart_logdet_from_values": {
                "required": True,
                "current_truth_value": False,
                "shape": "log(92160000) finitepart identity derived from emitted connection tables",
            },
            "no_lift_replay": {
                "required": True,
                "current_truth_value": False,
                "shape": "audit replay from emitted values without lifted selected flags",
            },
        },
        "would_fill_connection_fields": missing["minimal_constructive_alternative"]["would_fill_connection_fields"],
        "target_fitting_used": False,
    }
    connection_schema["closed_now"] = all(item["current_truth_value"] is True for item in connection_schema["required_tables"].values())
    OUTPUT_TABLES.write_text(json.dumps(connection_schema, indent=2, sort_keys=True) + "\n", encoding="utf-8")

    direct_closed = direct_skeleton["closed_now"]
    tables_closed = connection_schema["closed_now"]
    direct_open_count = sum(1 for item in direct_skeleton["statements"].values() if item["current_truth_value"] is not True)
    table_open_count = sum(1 for item in connection_schema["required_tables"].values() if item["current_truth_value"] is not True)

    decision = {
        "attempt_executed": True,
        "direct_theorem_skeleton_built": True,
        "connection_tables_schema_built": True,
        "direct_theorem_closed": direct_closed,
        "connection_tables_closed": tables_closed,
        "direct_open_statement_count": direct_open_count,
        "connection_open_table_count": table_open_count,
        "source_branch_identity_closed": False,
        "same_source_export_to_BN27_validators": False,
        "oriented_logdet_promoted": False,
        "direct_skeleton_path": rel(OUTPUT_DIRECT),
        "connection_tables_schema_path": rel(OUTPUT_TABLES),
        "next_required_artifact": NEXT,
        "closure_claimed": False,
        "target_fitting_used": False,
    }

    candidate = {
        "candidate": "SelectedHeteroticOrientedPhiFinBN27MinimalMissingSourceValueTheoremOrConnectionTables",
        "status": STATUS,
        "inputs": {key: rel(path) for key, path in INPUTS.items()},
        "parent_statuses": {
            "missing_theorem": missing["status"],
            "support_probe": probe["status"],
            "fill_attempt": fill["status"],
            "direct_declaration_fill": declaration["status"],
            "external_connection_request": external["status"],
        },
        "decision": decision,
        "theorem": {
            "name": "BN27MinimalMissingSourceValueTheoremOrTablesGate",
            "proved": True,
            "statement": (
                "The two legal closure forms are now executable schemas. The direct theorem has six required "
                "source-emission statements and all six remain open in the current source record. The constructive "
                "route has eight required connection-table families and all eight remain absent. Therefore the "
                "next legal construction must either prove the selected source-emission theorem or emit the selected "
                "connection tables; no new arithmetic target is needed."
            ),
        },
        "guardrails": {
            "does_not_count_support_as_theorem_statement": True,
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
        "direct_skeleton_path": rel(OUTPUT_DIRECT),
        "connection_tables_schema_path": rel(OUTPUT_TABLES),
        "note_path": rel(OUTPUT_NOTE),
        "direct_theorem_closed": direct_closed,
        "connection_tables_closed": tables_closed,
        "direct_open_statement_count": direct_open_count,
        "connection_open_table_count": table_open_count,
        "source_branch_identity_closed": False,
        "oriented_logdet_promoted": False,
        "closure_claimed": False,
        "target_fitting_used": False,
        "next_required_artifact": NEXT,
    }
    OUTPUT_CERT.write_text(json.dumps(cert, indent=2, sort_keys=True) + "\n", encoding="utf-8")

    note = f"""# Selected Heterotic OrientedPhiFin BN27 MinimalMissingSourceValueTheorem or ConnectionTables v1

## Result

```text
status = {STATUS}
direct_open_statement_count = {direct_open_count}
connection_open_table_count = {table_open_count}
direct_theorem_closed = false
connection_tables_closed = false
oriented_logdet_promoted = false
next_required_artifact = {NEXT}
```

## Theorem

{candidate["theorem"]["statement"]}

## Schemas

```text
{rel(OUTPUT_DIRECT)}
{rel(OUTPUT_TABLES)}
```
"""
    OUTPUT_NOTE.write_text(note, encoding="utf-8")
    return candidate


if __name__ == "__main__":
    result = main()
    print(f"wrote {rel(OUTPUT_DATA)}")
    print(f"wrote {rel(OUTPUT_DIRECT)}")
    print(f"wrote {rel(OUTPUT_TABLES)}")
    print(f"wrote {rel(OUTPUT_CERT)}")
    print(f"wrote {rel(OUTPUT_NOTE)}")
    print(result["status"])
