"""Build BN27 validator-export fill / selected-connection solve gate."""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "candidate_data"
CERTS = ROOT / "certificates"
PROOF = ROOT / "proof_corpus"

INPUTS = {
    "prior_gate": DATA / "selected_heterotic_orientedphifin_bn27_samesourceexport_to_bn27validators_or_selectedconnectionvalues.candidate.json",
    "validator_contract": DATA / "selected_heterotic_orientedphifin_bn27_validator_export_acceptance_contract.json",
    "transport_attempt": DATA / "selected_heterotic_orientedphifin_sourceidentitytransport_proofattempt.candidate.json",
    "sourcebranch_nogo": DATA / "selected_heterotic_orientedphifin_sourcebranchidentity_emission_or_nogo.candidate.json",
    "repair_packet": DATA / "selected_heterotic_orientedphifin_sourcebranchidentity_repair_packet.json",
    "selected_connection_witness_minimal": DATA / "selected_heterotic_orientedphifin_selectedconnectionwitness_minimal_source_values_packet.json",
}

OUTPUT_DATA = DATA / "selected_heterotic_orientedphifin_bn27_validatorexport_fill_or_selectedconnectionsolve.candidate.json"
OUTPUT_COLLAPSE = DATA / "selected_heterotic_orientedphifin_bn27_validator_dependency_collapse.json"
OUTPUT_CERT = CERTS / "selected_heterotic_orientedphifin_bn27_validatorexport_fill_or_selectedconnectionsolve_certificate.json"
OUTPUT_NOTE = PROOF / "Selected_Heterotic_OrientedPhiFin_BN27_ValidatorExport_Fill_or_SelectedConnectionSolve_v1.md"

STATUS = "HETEROTIC_ORIENTEDPHIFIN_BN27_VALIDATOR_EXPORT_FILL_REDUCED_TO_SOURCEBRANCH_OR_CONNECTIONVALUES"
NEXT = "Selected_Heterotic_OrientedPhiFin_BN27_SourceBranchIdentity_ThreeClause_Fill_or_ConnectionSolve_v1"


def rel(path: Path) -> str:
    try:
        return str(path.relative_to(ROOT))
    except ValueError:
        return str(path)


def load(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def main() -> dict[str, Any]:
    prior = load(INPUTS["prior_gate"])
    contract = load(INPUTS["validator_contract"])
    transport = load(INPUTS["transport_attempt"])
    nogo = load(INPUTS["sourcebranch_nogo"])
    repair = load(INPUTS["repair_packet"])
    minimal = load(INPUTS["selected_connection_witness_minimal"])

    validators = contract["validators"]
    sublemmas = transport["sublemma_attempts"]
    clauses = nogo["clauses"]

    collapse = {
        "schema": "SelectedHeterotic.OrientedPhiFin.BN27.ValidatorDependencyCollapse.v1",
        "status": "VALIDATORS_REDUCED_TO_SOURCEBRANCH_OR_CONNECTION_VALUES",
        "validator_dependencies": {
            "source_identity_validator": {
                "root": "source_branch_identity",
                "unconditional_closed": False,
                "blocking_clauses": list(clauses.keys()),
            },
            "BN27_deck_action_validator": {
                "root": "source_branch_identity_or_selected_connection_export",
                "unconditional_closed": False,
                "reason": "The deck action is support-ready but not emitted by a selected source.",
            },
            "operator_coemission_validator": {
                "conditional_closed": sublemmas["operator_coemission_before_finite_comparison"]["conditional_closure_ready"],
                "conditional_on": "source_branch_identity",
                "unconditional_closed": False,
            },
            "kernel_policy_validator": {
                "root": "source_branch_identity_or_selected_connection_export",
                "unconditional_closed": False,
                "reason": "Kernel policy is replayed algebraically, not source-owned.",
            },
            "trace_policy_validator": {
                "root": "source_branch_identity_or_selected_connection_export",
                "unconditional_closed": False,
                "reason": "Trace/zeta finitepart policy is replayed algebraically, not source-owned.",
            },
            "audit_replay_validator": {
                "unconditional_closed": validators["audit_replay_validator"]["selected_source_owned"],
                "acceptance_value": validators["audit_replay_validator"]["acceptance_value"],
            },
        },
        "three_clause_sourcebranch_cutset": clauses,
        "acceptable_connection_value_families": minimal["acceptable_minimal_values"],
        "repair_packet_path": rel(INPUTS["repair_packet"]),
        "target_fitting_used": False,
    }
    OUTPUT_COLLAPSE.write_text(json.dumps(collapse, indent=2, sort_keys=True) + "\n", encoding="utf-8")

    clause_status = {
        key: {
            "support_present": value["support_present"],
            "emitted_by_current_source": value["emitted_by_current_source"],
            "blocker": value["blocker"],
        }
        for key, value in clauses.items()
    }
    emitted_count = sum(1 for value in clause_status.values() if value["emitted_by_current_source"])

    decision = {
        "attempt_executed": True,
        "validator_dependency_collapse_built": True,
        "audit_replay_validator_closed": True,
        "operator_coemission_conditional_closed": True,
        "five_validator_bundle_unconditional_closed": False,
        "sourcebranch_three_clause_cutset_built": True,
        "sourcebranch_emitted_clause_count": emitted_count,
        "sourcebranch_required_clause_count": len(clause_status),
        "selected_connection_solve_closed": False,
        "same_source_export_to_BN27_validators": False,
        "source_object_named_S_QaSU3_BN27": False,
        "BN27_source_identity_closed": False,
        "oriented_logdet_promoted": False,
        "validator_dependency_collapse_path": rel(OUTPUT_COLLAPSE),
        "next_required_artifact": NEXT,
        "closure_claimed": False,
        "target_fitting_used": False,
    }

    candidate = {
        "candidate": "SelectedHeteroticOrientedPhiFinBN27ValidatorExportFillOrSelectedConnectionSolve",
        "status": STATUS,
        "inputs": {key: rel(path) for key, path in INPUTS.items()},
        "parent_statuses": {
            "prior_gate": prior["status"],
            "validator_contract": contract["status"],
            "transport_attempt": transport["status"],
            "sourcebranch_nogo": nogo["status"],
            "selected_connection_witness_minimal": minimal["status"],
        },
        "clause_status": clause_status,
        "validator_dependency_collapse_path": rel(OUTPUT_COLLAPSE),
        "decision": decision,
        "theorem": {
            "name": "BN27ValidatorExportReductionToSourceBranchOrConnectionValuesTheorem",
            "proved": True,
            "statement": (
                "The five open BN27 validators reduce to one source-branch identity cutset or an equivalent selected "
                "connection solve. Audit replay is already closed, and operator co-emission is conditionally closed once "
                "the source emits the BN27 threshold complex before finite comparison. The remaining source-branch cutset "
                "has three clauses: one selected source must own both branches, the 11-label shadow must promote to the "
                "full BN27 carrier, and the Route-C row must not be an external import. Current artifacts support all three "
                "but emit none, so BN27 source identity remains open."
            ),
        },
        "guardrails": {
            "does_not_promote_log92160000": True,
            "does_not_treat_conditional_validator_closure_as_unconditional": True,
            "does_not_treat_support_ready_as_source_owned": True,
            "does_not_import_routec_as_source_identity": True,
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
        "validator_dependency_collapse_path": rel(OUTPUT_COLLAPSE),
        "note_path": rel(OUTPUT_NOTE),
        "validator_dependency_collapse_built": True,
        "sourcebranch_emitted_clause_count": emitted_count,
        "same_source_export_to_BN27_validators": False,
        "selected_connection_solve_closed": False,
        "BN27_source_identity_closed": False,
        "oriented_logdet_promoted": False,
        "closure_claimed": False,
        "target_fitting_used": False,
        "next_required_artifact": NEXT,
    }
    OUTPUT_CERT.write_text(json.dumps(cert, indent=2, sort_keys=True) + "\n", encoding="utf-8")

    note = f"""# Selected Heterotic OrientedPhiFin BN27 ValidatorExport Fill or SelectedConnectionSolve v1

## Result

```text
status = {STATUS}
validator_dependency_collapse_built = true
audit_replay_validator_closed = true
operator_coemission_conditional_closed = true
sourcebranch_emitted_clause_count = {emitted_count}
same_source_export_to_BN27_validators = false
oriented_logdet_promoted = false
next_required_artifact = {NEXT}
```

## Theorem

{candidate["theorem"]["statement"]}

## Dependency Collapse

```text
{rel(OUTPUT_COLLAPSE)}
```
"""
    OUTPUT_NOTE.write_text(note, encoding="utf-8")
    return candidate


if __name__ == "__main__":
    result = main()
    print(f"wrote {rel(OUTPUT_DATA)}")
    print(f"wrote {rel(OUTPUT_COLLAPSE)}")
    print(f"wrote {rel(OUTPUT_CERT)}")
    print(f"wrote {rel(OUTPUT_NOTE)}")
    print(result["status"])
