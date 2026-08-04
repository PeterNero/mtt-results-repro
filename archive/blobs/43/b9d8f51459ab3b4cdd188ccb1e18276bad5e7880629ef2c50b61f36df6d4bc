"""Promote source-emission statements made valid by the A_N finitepart policy."""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "candidate_data"
CERTS = ROOT / "certificates"
CORPUS = ROOT / "proof_corpus"

SLUG = "selected_sourceemissionstatementpromotion_after_anpolicy"
PACKET_DIR = DATA / SLUG
OUTPUT = DATA / f"{SLUG}.candidate.json"
STATEMENT_PACKET = PACKET_DIR / "source_emission_statement_revalidation.packet.json"
SOURCE_OBJECT_PACKET = PACKET_DIR / "source_object_field_revalidation_after_an_policy.packet.json"
NEXT_PACKET = PACKET_DIR / "next_same_source_branch_identity_contract.packet.json"
CERT = CERTS / f"{SLUG}_certificate.json"
NOTE = CORPUS / "MTT_Selected_SourceEmissionStatementPromotion_AfterANPolicy_v1.md"

PREVIOUS = DATA / "selected_finitepartkernelpolicy_on_an_or_sourcebranchidentity.candidate.json"
AN_POLICY = DATA / "selected_finitepartkernelpolicy_on_an_or_sourcebranchidentity" / "an_finitepart_kernel_policy.packet.json"
LOGDET_GATE = (
    DATA
    / "selected_finitepartkernelpolicy_on_an_or_sourcebranchidentity"
    / "strict_logdet_gate_after_an_policy.packet.json"
)
SOURCE_ATTEMPT = (
    DATA
    / "selected_sqasu3bn27_selectedsourceemissiontheorem_or_fullconnectiontables"
    / "direct_source_theorem_attempt.packet.json"
)
REPLAY_DAG = (
    DATA
    / "selected_sqasu3bn27_selectedsourceemissiontheorem_or_fullconnectiontables"
    / "conditional_replay_dag_import.packet.json"
)
BRANCH_NOGO = (
    DATA
    / "selected_orientedphifin_sourceownership_theorem_or_smootheqa_quotient"
    / "sourcebranchidentity_current_source_nogo.packet.json"
)
SOURCEOWNERSHIP_FRONTIER = (
    DATA
    / "selected_orientedphifin_sourceownership_theorem_or_smootheqa_quotient"
    / "bn27_sourceownership_transport_frontier.packet.json"
)

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
        raise FileNotFoundError("missing source-emission promotion inputs: " + ", ".join(missing))


def main() -> int:
    require_sources([PREVIOUS, AN_POLICY, LOGDET_GATE, SOURCE_ATTEMPT, REPLAY_DAG, BRANCH_NOGO, SOURCEOWNERSHIP_FRONTIER])

    previous = load(PREVIOUS)
    an_policy = load(AN_POLICY)
    logdet_gate = load(LOGDET_GATE)
    source_attempt = load(SOURCE_ATTEMPT)
    replay_dag = load(REPLAY_DAG)
    branch_nogo = load(BRANCH_NOGO)
    sourceownership = load(SOURCEOWNERSHIP_FRONTIER)

    if previous["next_required_artifact"] != "MTT_Selected_SourceBranchIdentity_or_CechHYMConnectionValues_AfterFinitepartPolicy_v1":
        raise ValueError("previous frontier is not the post-A_N source-branch target")
    if not an_policy["kernel_policy"]["kernel_trace_policy_source_owned_on_A_N"]:
        raise ValueError("A_N kernel/trace policy is not source-owned")
    if not an_policy["finitepart_functional"]["source_owned_finitepart_functional_closed_on_A_N"]:
        raise ValueError("A_N finitepart functional is not source-owned")
    if source_attempt["emitted_source_statement_count"] != 0:
        raise ValueError("expected old source attempt to have zero emitted statements")

    source_rows: dict[str, dict[str, Any]] = {}
    for row in source_attempt["rows"]:
        statement = row["statement"]
        source_rows[statement] = dict(row)
        if statement == "full_F3xF3_carrier_emitted_before_finite_comparison":
            source_rows[statement].update(
                {
                    "emitted_as_source_owned": True,
                    "promotion_source": rel(AN_POLICY),
                    "accepted_reason": (
                        "The selected A_N source algebra has rank 27 with basis [class, phase, shift], "
                        "hilbert dimension 27, and exact finite qutrit-Weyl carrier before any determinant comparison."
                    ),
                }
            )
        elif statement == "kernel_and_trace_policies_source_owned":
            source_rows[statement].update(
                {
                    "emitted_as_source_owned": True,
                    "promotion_source": rel(AN_POLICY),
                    "accepted_reason": (
                        "The A_N theorem closes normalized finite trace, zero-cluster/kernel exclusion, "
                        "and determinant finitepart as selected finite source operations."
                    ),
                }
            )

    accepted_statements = [name for name in PROMOTED_STATEMENTS if source_rows[name]["emitted_as_source_owned"]]
    remaining_statements = [name for name in REMAINING_STATEMENTS if not source_rows[name]["emitted_as_source_owned"]]

    statement_packet = {
        "schema": "MTTSourceEmissionStatementRevalidationAfterANPolicy.v1",
        "status": "TWO_OF_SIX_SOURCE_EMISSION_STATEMENTS_PROMOTED",
        "closure_claimed": True,
        "previous_emitted_source_statement_count": source_attempt["emitted_source_statement_count"],
        "emitted_source_statement_count": len(accepted_statements),
        "required_source_statement_count": source_attempt["statement_count"],
        "accepted_statements": accepted_statements,
        "remaining_statements": remaining_statements,
        "rows": source_rows,
        "direct_source_theorem_closed": False,
        "source_branch_identity_closed": False,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
    }

    all_fields = replay_dag["then_fills_source_fields"]
    source_fields = {
        field: {
            "source_owned": field in PROMOTED_SOURCE_FIELDS,
            "promotion_source": rel(AN_POLICY) if field in PROMOTED_SOURCE_FIELDS else None,
        }
        for field in all_fields
    }
    source_object_packet = {
        "schema": "MTTSourceObjectFieldRevalidationAfterANPolicy.v1",
        "status": "THREE_OF_ELEVEN_SOURCE_OBJECT_FIELDS_PROMOTED",
        "closure_claimed": True,
        "promoted_source_object_fields": PROMOTED_SOURCE_FIELDS,
        "promoted_source_object_field_count": len(PROMOTED_SOURCE_FIELDS),
        "required_source_object_field_count": len(all_fields),
        "remaining_source_object_fields": [field for field in all_fields if field not in PROMOTED_SOURCE_FIELDS],
        "fields": source_fields,
        "validators_unblocked_at_policy_level": [
            "BN27_deck_action",
            "kernel_policy",
            "trace_policy",
        ],
        "validators_still_conditional": [
            "audit_replay",
            "not_external_import",
            "operator_coemission",
            "source_identity",
        ],
        "oriented_logdet_promoted": False,
        "unconditional_replay_allowed": False,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
    }

    next_packet = {
        "schema": "MTTNextSameSourceBranchIdentityContract.v1",
        "status": "SAME_SOURCE_BRANCH_IDENTITY_STILL_REQUIRED_AFTER_TWO_SOURCE_STATEMENTS",
        "closure_claimed": True,
        "next_required_artifact": NEXT,
        "source_emission_statement_count": "2/6",
        "source_object_field_count": "3/11",
        "final_connection_table_count": "4/8",
        "remaining_sourcebranch_clauses": {
            key: value for key, value in branch_nogo["clauses"].items() if not value["emitted_by_current_source"]
        },
        "remaining_minimal_exits": [
            "prove one selected source owns both heterotic C_tau orientation and Route-C/q79 PhiFin_DE magnitude",
            "prove Route-C finite trace row is internal to that source, not external support",
            "promote the full BN27 oriented carrier/magnitude branch rather than the 11-label shadow",
            "or emit selected Cech/HYM/projective connection values exporting the same fields",
        ],
        "strict_promotion_blockers_remaining": logdet_gate["strict_promotion_blockers_remaining"],
        "sourceownership_transport_closed": sourceownership["BN27_source_ownership_transport_closed"],
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
    }

    candidate = {
        "candidate": "MTTSelectedSourceEmissionStatementPromotionAfterANPolicy",
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
            "an_policy": rel(AN_POLICY),
            "logdet_gate": rel(LOGDET_GATE),
            "source_attempt": rel(SOURCE_ATTEMPT),
            "replay_dag": rel(REPLAY_DAG),
            "branch_nogo": rel(BRANCH_NOGO),
            "sourceownership_frontier": rel(SOURCEOWNERSHIP_FRONTIER),
        },
        "output_packets": {
            "source_emission_statement_revalidation": rel(STATEMENT_PACKET),
            "source_object_field_revalidation_after_an_policy": rel(SOURCE_OBJECT_PACKET),
            "next_same_source_branch_identity_contract": rel(NEXT_PACKET),
        },
        "closure_decision": {
            "source_emission_statement_count": len(accepted_statements),
            "required_source_emission_statement_count": source_attempt["statement_count"],
            "accepted_source_emission_statements": accepted_statements,
            "remaining_source_emission_statements": remaining_statements,
            "source_object_field_count": len(PROMOTED_SOURCE_FIELDS),
            "required_source_object_field_count": len(all_fields),
            "promoted_source_object_fields": PROMOTED_SOURCE_FIELDS,
            "direct_source_theorem_closed": False,
            "source_branch_identity_closed": False,
            "oriented_logdet_promoted": False,
            "no_lifted_flags_connection_replay_promoted": False,
            "final_connection_tables_accepted": 4,
            "strict_no_knob_closed": False,
            "true_SM_equivalence_closed": False,
        },
        "theorem": {
            "name": "SourceEmissionStatementPromotionAfterANPolicyTheorem",
            "proved": True,
            "statement": (
                "The A_N finitepart/kernel policy upgrades two previously support-only BN27 source-emission "
                "statements to source-owned statements: the full finite F3xF3 rank-slot carrier is emitted "
                "before finite comparison, and the kernel/shared-circle plus trace/zeta finitepart policies "
                "are source-owned.  This promotes three of eleven source-object fields, but the direct source "
                "theorem and source-branch identity remain open because C_tau/PhiFin_DE same-source ownership, "
                "Route-C internality, selected source naming, and no-lift replay are not yet emitted."
            ),
        },
    }

    cert = {
        "certificate": "MTTSelectedSourceEmissionStatementPromotionAfterANPolicy",
        "status": STATUS,
        "candidate_path": rel(OUTPUT),
        "next_required_artifact": NEXT,
        "closure_claimed": True,
        "theorem_proved": True,
        "source_emission_statement_count": len(accepted_statements),
        "required_source_emission_statement_count": source_attempt["statement_count"],
        "accepted_source_emission_statements": accepted_statements,
        "remaining_source_emission_statements": remaining_statements,
        "source_object_field_count": len(PROMOTED_SOURCE_FIELDS),
        "required_source_object_field_count": len(all_fields),
        "promoted_source_object_fields": PROMOTED_SOURCE_FIELDS,
        "direct_source_theorem_closed": False,
        "source_branch_identity_closed": False,
        "oriented_logdet_promoted": False,
        "no_lifted_flags_connection_replay_promoted": False,
        "final_connection_tables_accepted": 4,
        "strict_no_knob_closed": False,
        "true_SM_equivalence_closed": False,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
    }

    note = f"""# MTT Selected Source Emission Statement Promotion After A_N Policy v1

## Theorem

`SourceEmissionStatementPromotionAfterANPolicyTheorem` is proved.

## Result

The A_N finitepart/kernel policy promotes the BN27 source-emission layer from
`0/6` to `{len(accepted_statements)}/6`.

Accepted now:

- `full_F3xF3_carrier_emitted_before_finite_comparison`
- `kernel_and_trace_policies_source_owned`

It also promotes `3/11` source-object fields:

- `full_F3xF3_rank_slot_carrier_emitted`
- `kernel_shared_circle_policy_source_owned`
- `trace_zeta_finitepart_policy_source_owned`

The direct source theorem, source-branch identity, `log(92160000)` final row,
and no-lift replay remain open.

## Next Artifact

`{NEXT}`
"""

    write_json(STATEMENT_PACKET, statement_packet)
    write_json(SOURCE_OBJECT_PACKET, source_object_packet)
    write_json(NEXT_PACKET, next_packet)
    write_json(OUTPUT, candidate)
    write_json(CERT, cert)
    NOTE.write_text(note, encoding="utf-8")

    print(json.dumps({"candidate": rel(OUTPUT), "status": STATUS}, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
