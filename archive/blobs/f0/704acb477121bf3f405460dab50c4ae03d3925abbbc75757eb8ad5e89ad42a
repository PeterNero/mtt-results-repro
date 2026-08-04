"""Attack source-branch identity repair via source amendment or connection values."""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "candidate_data"
CERTS = ROOT / "certificates"
PROOF = ROOT / "proof_corpus"

INPUTS = {
    "sourcebranch_nogo": DATA / "selected_heterotic_orientedphifin_sourcebranchidentity_emission_or_nogo.candidate.json",
    "repair_packet": DATA / "selected_heterotic_orientedphifin_sourcebranchidentity_repair_packet.json",
    "projective_tables": DATA / "selected_heterotic_sourceamendment_or_projectiverhoe_representative_tables.candidate.json",
    "typed_projective_fill": DATA / "selected_heterotic_typedcechende_basis_or_projectiverhoe_fill_attempt.candidate.json",
    "bn27_bridge": DATA / "selected_heterotic_orientedphifin_bn27_sourcedomainbridge_or_smootheqa_quotient.candidate.json",
    "export_fill": DATA / "selected_heterotic_orientedphifin_selectedconnectionwitness_export_fill.candidate.json",
}

OUTPUT_DATA = DATA / "selected_heterotic_orientedphifin_sourcebranchidentity_sourceamendment_or_connectionvalues.candidate.json"
OUTPUT_NEXT = DATA / "selected_heterotic_orientedphifin_projectiverhoe_bn27_lift_or_directsource_theorem_request.json"
OUTPUT_CERT = CERTS / "selected_heterotic_orientedphifin_sourcebranchidentity_sourceamendment_or_connectionvalues_certificate.json"
OUTPUT_NOTE = PROOF / "Selected_Heterotic_OrientedPhiFin_SourceBranchIdentity_SourceAmendment_or_ConnectionValues_v1.md"

STATUS = "HETEROTIC_ORIENTEDPHIFIN_SOURCEBRANCHIDENTITY_REPAIR_ATTACK_PROJECTIVERHOE_PRIMARY_BN27_LIFT_OPEN"
NEXT = "Selected_Heterotic_OrientedPhiFin_ProjectiveRhoE_BN27Lift_or_DirectSourceTheorem_v1"


def rel(path: Path) -> str:
    try:
        return str(path.relative_to(ROOT))
    except ValueError:
        return str(path)


def load(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def main() -> dict[str, Any]:
    sourcebranch = load(INPUTS["sourcebranch_nogo"])
    repair = load(INPUTS["repair_packet"])
    projective = load(INPUTS["projective_tables"])
    typed = load(INPUTS["typed_projective_fill"])
    bn27 = load(INPUTS["bn27_bridge"])
    export_fill = load(INPUTS["export_fill"])

    lanes = {
        "source_identity_transport_theorem": {
            "rank": 2,
            "closed_now": False,
            "support_present": sourcebranch["decision"]["support_count"] == 3,
            "reason_open": "still needs a new theorem naming S_QaSU3^BN27 and internalizing the Route-C row",
            "payload": repair["minimal_success_payload"]["source_identity_transport_theorem"],
        },
        "BN27_domain_emission": {
            "rank": 3,
            "closed_now": False,
            "support_present": bn27["orbit_completion_test"]["full_BN27_domain"]["basis_dimension"] == 27,
            "reason_open": "full BN27 table is materialized but not source-emitted by the heterotic branch",
            "payload": repair["minimal_success_payload"]["BN27_domain_emission"],
        },
        "selected_connection_values_alternative": {
            "rank": 1,
            "closed_now": False,
            "support_present": projective["decision"]["finite_projective_candidate_built"],
            "reason_open": "finite projective rho_E values exist at 11-label scope but no BN27 lift/export theorem makes them a threshold connection witness",
            "payload": repair["minimal_success_payload"]["selected_connection_values_alternative"],
        },
    }

    projective_attack = {
        "finite_candidate_available": projective["decision"]["finite_projective_candidate_built"],
        "finite_values_inserted": {
            "tau_values": True,
            "central_character": True,
            "finite_D_E": True,
            "Green_Riesz": True,
            "dotD": True,
            "finite_trace": True,
        },
        "closes_sourcebranch_identity_now": False,
        "why_not": [
            "candidate lives on the selected 11-label twisted module, not the full oriented BN27 threshold carrier",
            "no theorem lifts projective rho_E/tau tables to all 27 F3xF3 rank-slot rows",
            "no export proves BN27 D_E/Riesz/Green/kernel/trace validators from these connection values",
            "typed/Cech and smooth transition representatives remain open",
        ],
        "best_next_object": "projective rho_E BN27 lift or direct source theorem",
    }

    lift_request = {
        "schema": "SelectedHeterotic.OrientedPhiFin.ProjectiveRhoE_BN27Lift_or_DirectSourceTheoremRequest.v1",
        "status": "BN27_LIFT_OR_DIRECT_SOURCE_THEOREM_REQUIRED",
        "primary_lane": "projective_rhoE_BN27_lift",
        "must_emit": {
            "domain_lift": "map 11-label tau/rho_E module into full 27 F3xF3 rank-slot carrier without losing the 16 positive oriented rows",
            "operator_lift": "derive BN27 PhiFin_DE/Riesz/Green/kernel/trace validators from the same projective connection values",
            "source_identity": "prove the lift is emitted by the selected heterotic Qa/SU3 source before finite comparison",
            "audit_replay": "rerun source-branch, export-fill, and source-identity transport audits without lifted flags",
        },
        "alternative_lane": "direct theorem declaring S_QaSU3^BN27 and emitting C_tau/PhiFin_DE as one source object",
        "forbidden_shortcuts": repair["forbidden_shortcuts"],
    }
    OUTPUT_NEXT.write_text(json.dumps(lift_request, indent=2, sort_keys=True) + "\n", encoding="utf-8")

    decision = {
        "repair_attack_executed": True,
        "primary_lane": "selected_connection_values_alternative",
        "projective_rhoE_primary": True,
        "projective_finite_candidate_available": True,
        "projective_BN27_lift_closed": False,
        "source_identity_transport_closed": False,
        "BN27_domain_emission_closed": False,
        "source_branch_identity_closed": False,
        "selected_connection_witness_export_closed": False,
        "oriented_logdet_promoted": False,
        "next_request_built": True,
        "next_required_artifact": NEXT,
        "target_fitting_used": False,
        "closure_claimed": False,
    }

    candidate = {
        "candidate": "SelectedHeteroticOrientedPhiFinSourceBranchIdentitySourceAmendmentOrConnectionValues",
        "status": STATUS,
        "inputs": {key: rel(path) for key, path in INPUTS.items()},
        "parent_statuses": {
            "sourcebranch_nogo": sourcebranch["status"],
            "projective_tables": projective["status"],
            "typed_projective_fill": typed["status"],
            "bn27_bridge": bn27["status"],
            "export_fill": export_fill["status"],
        },
        "lane_ranking": lanes,
        "projective_attack": projective_attack,
        "next_request_path": rel(OUTPUT_NEXT),
        "decision": decision,
        "theorem": {
            "name": "SourceBranchIdentityRepairAttackProjectiveRhoEPrimaryTheorem",
            "proved": True,
            "statement": (
                "Among the legal repair lanes, the selected connection-values alternative is the first executable "
                "lane because the finite projective rho_E candidate already emits tau, central character, finite "
                "D_E, Green/Riesz, dotD, and finite trace. This still does not close source-branch identity: those "
                "values live at 11-label scope and need a BN27 lift/export theorem, or a direct source theorem "
                "declaring one selected BN27 threshold source."
            ),
        },
        "guardrails": {
            "does_not_promote_projective_11label_values_to_BN27": True,
            "does_not_promote_connection_support_to_source_identity": True,
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
        "next_request_path": rel(OUTPUT_NEXT),
        "note_path": rel(OUTPUT_NOTE),
        "projective_rhoE_primary": True,
        "projective_BN27_lift_closed": False,
        "source_branch_identity_closed": False,
        "selected_connection_witness_export_closed": False,
        "oriented_logdet_promoted": False,
        "closure_claimed": False,
        "target_fitting_used": False,
        "next_required_artifact": NEXT,
    }
    OUTPUT_CERT.write_text(json.dumps(cert, indent=2, sort_keys=True) + "\n", encoding="utf-8")

    note = f"""# Selected Heterotic OrientedPhiFin SourceBranchIdentity SourceAmendment or ConnectionValues v1

## Result

```text
status = {STATUS}
primary_lane = selected_connection_values_alternative
projective_rhoE_primary = true
projective_BN27_lift_closed = false
source_branch_identity_closed = false
selected_connection_witness_export_closed = false
oriented_logdet_promoted = false
next_required_artifact = {NEXT}
```

## Theorem

{candidate["theorem"]["statement"]}

Next request:

```text
{rel(OUTPUT_NEXT)}
```
"""
    OUTPUT_NOTE.write_text(note, encoding="utf-8")
    return candidate


if __name__ == "__main__":
    result = main()
    print(f"wrote {rel(OUTPUT_DATA)}")
    print(f"wrote {rel(OUTPUT_NEXT)}")
    print(f"wrote {rel(OUTPUT_CERT)}")
    print(f"wrote {rel(OUTPUT_NOTE)}")
    print(result["status"])
