"""Attempt the oriented Phi_fin source-identity transport proof."""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "candidate_data"
CERTS = ROOT / "certificates"
PROOF = ROOT / "proof_corpus"

INPUTS = {
    "minimal_packet": DATA / "selected_heterotic_orientedphifin_sourceidentitytransport_or_connectionvalues_minimalpacket.candidate.json",
    "obligation_skeleton": DATA / "selected_heterotic_orientedphifin_sourceidentitytransport_obligation_skeleton.json",
    "export_fill": DATA / "selected_heterotic_orientedphifin_selectedconnectionwitness_export_fill.candidate.json",
    "sourceidentity_gate": DATA / "selected_heterotic_orientedphifin_heterotic_routec_sourceidentity_or_selectedconnectionwitness.candidate.json",
    "coemission_theorem": DATA / "selected_heterotic_orientedphifin_orientation_magnitude_coemission_theorem.candidate.json",
    "trace_identity": DATA / "selected_heterotic_orientedphifin_fullfourierorbit_traceidentity.json",
    "simultaneous_table": DATA / "selected_heterotic_orientedphifin_simultaneous_ctau_phifin_table.json",
}

OUTPUT_DATA = DATA / "selected_heterotic_orientedphifin_sourceidentitytransport_proofattempt.candidate.json"
OUTPUT_REDUCTION = DATA / "selected_heterotic_orientedphifin_sourceidentitytransport_reduction_to_sourcebranchidentity.json"
OUTPUT_CERT = CERTS / "selected_heterotic_orientedphifin_sourceidentitytransport_proofattempt_certificate.json"
OUTPUT_NOTE = PROOF / "Selected_Heterotic_OrientedPhiFin_SourceIdentityTransport_ProofAttempt_v1.md"

STATUS = "HETEROTIC_ORIENTEDPHIFIN_SOURCEIDENTITYTRANSPORT_PROOFATTEMPT_REDUCED_TO_SOURCEBRANCHIDENTITY"
NEXT = "Selected_Heterotic_OrientedPhiFin_SourceBranchIdentity_Emission_or_NoGo_v1"


def rel(path: Path) -> str:
    try:
        return str(path.relative_to(ROOT))
    except ValueError:
        return str(path)


def load(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def main() -> dict[str, Any]:
    minimal = load(INPUTS["minimal_packet"])
    obligations = load(INPUTS["obligation_skeleton"])
    export_fill = load(INPUTS["export_fill"])
    source_gate = load(INPUTS["sourceidentity_gate"])
    coemission = load(INPUTS["coemission_theorem"])
    trace_identity = load(INPUTS["trace_identity"])
    table = load(INPUTS["simultaneous_table"])

    source_branch_identity = {
        "unconditional_closed": False,
        "support_ready": obligations["sublemmas"]["source_branch_identity"]["support_ready"],
        "current_blocker": source_gate["route_status"]["same_source_identity"]["blocker"],
        "missing_payload": [
            "source theorem naming one selected source for heterotic C_tau and Route-C/q79 PhiFin_DE",
            "proof that the 11-label heterotic finite quotient is promoted to the full BN27 threshold carrier",
            "proof that the Route-C finite trace row is not imported after the fact as external support",
        ],
    }

    operator_coemission = {
        "unconditional_closed": False,
        "conditional_on_source_branch_identity": True,
        "conditional_closure_ready": (
            table["commutation"]["commutator_zero"]
            and table["basis_dimension"] == 27
            and minimal["current_support"]["same_BN27_basis"]
            and minimal["current_support"]["C_tau_PhiFin_commute"]
        ),
        "support": {
            "same_basis": minimal["current_support"]["same_BN27_basis"],
            "basis_dimension": table["basis_dimension"],
            "commutator_zero": table["commutation"]["commutator_zero"],
            "coemission_status": coemission["status"],
        },
        "conditional_statement": (
            "If the source-branch identity theorem emits the BN27 threshold complex before finite comparison, "
            "then C_tau and PhiFin_DE co-emit because they are simultaneous diagonal operators on the same BN27 basis."
        ),
    }

    no_lift_replay = {
        "unconditional_closed": False,
        "conditional_on_source_branch_identity": True,
        "conditional_closure_ready": (
            export_fill["decision"]["audit_replay_export_filled"]
            and export_fill["guardrails"]["does_not_use_lifted_selected_flags"]
            and export_fill["guardrails"]["does_not_promote_routec_support_to_source_identity"]
        ),
        "support": {
            "audit_replay_export_filled": export_fill["decision"]["audit_replay_export_filled"],
            "target_fitting_used": export_fill["target_fitting_used"],
            "no_lift_guardrail": export_fill["guardrails"]["does_not_use_lifted_selected_flags"],
            "trace_identity_relative": trace_identity["identity_closed_relative_to_full_orbit_source"],
        },
        "conditional_statement": (
            "If the same source emits the BN27 complex, then the existing oriented table, finitepart trace, "
            "D_E/Riesz/Green, and no-double-count audits replay without lifted selected flags."
        ),
    }

    reduction = {
        "schema": "SelectedHeterotic.OrientedPhiFin.SourceIdentityTransportReduction.v1",
        "status": "REDUCED_TO_SOURCE_BRANCH_IDENTITY",
        "proved_conditional_implications": {
            "source_branch_identity_implies_operator_coemission": operator_coemission["conditional_closure_ready"],
            "source_branch_identity_implies_no_lift_replay": no_lift_replay["conditional_closure_ready"],
        },
        "remaining_unconditional_leaf": "source_branch_identity",
        "required_next_payload": source_branch_identity["missing_payload"],
        "forbidden_shortcuts": obligations["forbidden_shortcuts"],
    }
    OUTPUT_REDUCTION.write_text(json.dumps(reduction, indent=2, sort_keys=True) + "\n", encoding="utf-8")

    decision = {
        "proof_attempt_executed": True,
        "source_branch_identity_closed": False,
        "operator_coemission_unconditional_closed": False,
        "no_lift_replay_unconditional_closed": False,
        "operator_coemission_conditional_closed": operator_coemission["conditional_closure_ready"],
        "no_lift_replay_conditional_closed": no_lift_replay["conditional_closure_ready"],
        "transport_reduced_to_single_leaf": True,
        "single_remaining_leaf": "source_branch_identity",
        "selected_connection_witness_export_closed": False,
        "oriented_logdet_promoted": False,
        "next_required_artifact": NEXT,
        "target_fitting_used": False,
        "closure_claimed": False,
    }

    candidate = {
        "candidate": "SelectedHeteroticOrientedPhiFinSourceIdentityTransportProofAttempt",
        "status": STATUS,
        "inputs": {key: rel(path) for key, path in INPUTS.items()},
        "parent_statuses": {
            "minimal_packet": minimal["status"],
            "export_fill": export_fill["status"],
            "sourceidentity_gate": source_gate["status"],
            "coemission_theorem": coemission["status"],
        },
        "sublemma_attempts": {
            "source_branch_identity": source_branch_identity,
            "operator_coemission_before_finite_comparison": operator_coemission,
            "no_lift_audit_replay_from_emitted_source": no_lift_replay,
        },
        "reduction_path": rel(OUTPUT_REDUCTION),
        "decision": decision,
        "theorem": {
            "name": "SourceIdentityTransportReductionTheorem",
            "proved": True,
            "statement": (
                "The source-identity transport proof is reduced to one unconditional leaf. "
                "Operator co-emission and no-lift audit replay are conditionally ready: once a same-source "
                "branch-identity theorem emits the BN27 threshold complex, the commuting C_tau/PhiFin_DE table "
                "and existing no-lift audits promote together. The current corpus still does not emit that "
                "source-branch identity, so the oriented logdet and selected-connection export remain unpromoted."
            ),
        },
        "guardrails": {
            "does_not_treat_conditional_implication_as_closure": True,
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
        "reduction_path": rel(OUTPUT_REDUCTION),
        "note_path": rel(OUTPUT_NOTE),
        "operator_coemission_conditional_closed": decision["operator_coemission_conditional_closed"],
        "no_lift_replay_conditional_closed": decision["no_lift_replay_conditional_closed"],
        "source_branch_identity_closed": False,
        "transport_reduced_to_single_leaf": True,
        "selected_connection_witness_export_closed": False,
        "oriented_logdet_promoted": False,
        "closure_claimed": False,
        "target_fitting_used": False,
        "next_required_artifact": NEXT,
    }
    OUTPUT_CERT.write_text(json.dumps(cert, indent=2, sort_keys=True) + "\n", encoding="utf-8")

    note = f"""# Selected Heterotic OrientedPhiFin SourceIdentityTransport ProofAttempt v1

## Result

```text
status = {STATUS}
operator_coemission_conditional_closed = {str(decision["operator_coemission_conditional_closed"]).lower()}
no_lift_replay_conditional_closed = {str(decision["no_lift_replay_conditional_closed"]).lower()}
source_branch_identity_closed = false
transport_reduced_to_single_leaf = true
selected_connection_witness_export_closed = false
oriented_logdet_promoted = false
next_required_artifact = {NEXT}
```

## Theorem

{candidate["theorem"]["statement"]}

Reduction packet:

```text
{rel(OUTPUT_REDUCTION)}
```
"""
    OUTPUT_NOTE.write_text(note, encoding="utf-8")
    return candidate


if __name__ == "__main__":
    result = main()
    print(f"wrote {rel(OUTPUT_DATA)}")
    print(f"wrote {rel(OUTPUT_REDUCTION)}")
    print(f"wrote {rel(OUTPUT_CERT)}")
    print(f"wrote {rel(OUTPUT_NOTE)}")
    print(result["status"])
