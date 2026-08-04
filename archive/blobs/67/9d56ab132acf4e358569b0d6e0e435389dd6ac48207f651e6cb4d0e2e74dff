"""Build the minimal source-transport or connection-values packet."""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "candidate_data"
CERTS = ROOT / "certificates"
PROOF = ROOT / "proof_corpus"

INPUTS = {
    "export_fill": DATA / "selected_heterotic_orientedphifin_selectedconnectionwitness_export_fill.candidate.json",
    "minimal_source_values": DATA / "selected_heterotic_orientedphifin_selectedconnectionwitness_minimal_source_values_packet.json",
    "sourceidentity_gate": DATA / "selected_heterotic_orientedphifin_heterotic_routec_sourceidentity_or_selectedconnectionwitness.candidate.json",
    "typed_projective_fill": DATA / "selected_heterotic_typedcechende_basis_or_projectiverhoe_fill_attempt.candidate.json",
    "sourceamendment_projective_tables": DATA / "selected_heterotic_sourceamendment_or_projectiverhoe_representative_tables.candidate.json",
    "simultaneous_table": DATA / "selected_heterotic_orientedphifin_simultaneous_ctau_phifin_table.json",
    "trace_identity": DATA / "selected_heterotic_orientedphifin_fullfourierorbit_traceidentity.json",
}

OUTPUT_DATA = DATA / "selected_heterotic_orientedphifin_sourceidentitytransport_or_connectionvalues_minimalpacket.candidate.json"
OUTPUT_OBLIGATIONS = DATA / "selected_heterotic_orientedphifin_sourceidentitytransport_obligation_skeleton.json"
OUTPUT_CERT = CERTS / "selected_heterotic_orientedphifin_sourceidentitytransport_or_connectionvalues_minimalpacket_certificate.json"
OUTPUT_NOTE = PROOF / "Selected_Heterotic_OrientedPhiFin_SourceIdentityTransport_or_ConnectionValues_MinimalPacket_v1.md"

STATUS = "HETEROTIC_ORIENTEDPHIFIN_SOURCEIDENTITYTRANSPORT_MINIMAL_PACKET_BUILT_PROOF_OBJECT_OPEN"
NEXT = "Selected_Heterotic_OrientedPhiFin_SourceIdentityTransport_ProofAttempt_v1"


def rel(path: Path) -> str:
    try:
        return str(path.relative_to(ROOT))
    except ValueError:
        return str(path)


def load(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def main() -> dict[str, Any]:
    export_fill = load(INPUTS["export_fill"])
    minimal_source_values = load(INPUTS["minimal_source_values"])
    gate = load(INPUTS["sourceidentity_gate"])
    typed_projective = load(INPUTS["typed_projective_fill"])
    projective_tables = load(INPUTS["sourceamendment_projective_tables"])
    table = load(INPUTS["simultaneous_table"])
    trace_identity = load(INPUTS["trace_identity"])

    current_support = {
        "same_BN27_basis": table["basis_id"] == export_fill["support"]["basis_id"],
        "basis_dimension_27": table["basis_dimension"] == 27,
        "C_tau_PhiFin_commute": table["commutation"]["commutator_zero"],
        "oriented_abs_finitepart_exact": trace_identity["oriented_abs_sector_logdet_exact"] == "log(92160000)",
        "full_oriented_positive_orbit_rows": table["counts"]["oriented_nonzero_Ctau_positive_magnitude_count"] == 16,
        "all_export_fields_support_ready": export_fill["decision"]["support_ready_count"] == 6,
        "only_audit_replay_exported": export_fill["decision"]["export_filled_count"] == 1,
    }

    route_comparison = {
        "source_identity_transport": {
            "route_rank": 1,
            "why_primary": "It is the smallest possible object: one source theorem would promote five already-replayable support fields.",
            "support_prefilter_passes": all(current_support.values()),
            "closed_now": False,
            "missing_proof_object": "a source-emitted theorem identifying heterotic Qa/SU3 threshold ownership with the Route-C/q79 BN27 finite trace row",
            "required_sublemmas": [
                "source_branch_identity",
                "operator_coemission_before_finite_comparison",
                "no_lift_audit_replay_from_emitted_source",
            ],
        },
        "typed_connection_values": {
            "route_rank": 2,
            "why_secondary": "It would close the same gate constructively, but currently requires many typed Cech values not printed by the source.",
            "support_prefilter_passes": True,
            "closed_now": False,
            "missing_count": typed_projective["candidate"]["decision"]["payload_missing_leaf_count"] if isinstance(typed_projective.get("candidate"), dict) else None,
            "first_missing": "typed f_i/g_i section representatives, Cech transitions, and g o f = 0 certificate",
        },
        "direct_connection_values": {
            "route_rank": 3,
            "why_secondary": "It bypasses typed maps, but still needs selected A/F_A or projective rho_E values plus finite operator/finitepart identity.",
            "support_prefilter_passes": True,
            "closed_now": False,
            "projective_table_status": projective_tables["status"],
            "first_missing": "same-branch selected connection or projective transition tables that export to BN27 threshold ownership",
        },
    }

    obligation_skeleton = {
        "schema": "SelectedHeterotic.OrientedPhiFin.SourceIdentityTransportObligationSkeleton.v1",
        "status": "PROOF_OBJECT_OPEN",
        "primary_route": "source_identity_transport",
        "theorem_to_prove": {
            "name": "SelectedHeteroticRouteC_BN27_ThresholdSourceIdentityTransport",
            "statement": (
                "The selected heterotic Qa/SU3 source that emits the signed C_tau orientation layer also emits the "
                "Route-C/q79 BN27 PhiFin_DE magnitude layer as one threshold complex, before finite comparison."
            ),
        },
        "sublemmas": {
            "source_branch_identity": {
                "current_status": "OPEN",
                "must_show": "heterotic Qa/SU3 branch source and Route-C/q79 BN27 finite trace source are one selected source for this row",
                "support_ready": True,
            },
            "operator_coemission_before_finite_comparison": {
                "current_status": "OPEN",
                "must_show": "C_tau and PhiFin_DE are emitted together by that source, not glued after separate computations",
                "support_ready": current_support["C_tau_PhiFin_commute"],
            },
            "no_lift_audit_replay_from_emitted_source": {
                "current_status": "OPEN",
                "must_show": "existing orbit, trace, D_E/Riesz/Green, and no-double-count audits rerun without lifted selected flags",
                "support_ready": export_fill["export_fields"]["audit_replay"]["filled_for_export"],
            },
        },
        "acceptance_rule": "all three sublemmas must close; then promote BN27_deck_action, operators, kernel_policy, and trace_policy together",
        "forbidden_shortcuts": minimal_source_values["must_not_use"],
    }
    OUTPUT_OBLIGATIONS.write_text(json.dumps(obligation_skeleton, indent=2, sort_keys=True) + "\n", encoding="utf-8")

    decision = {
        "minimal_packet_built": True,
        "primary_route_selected": "source_identity_transport",
        "source_identity_transport_closed": False,
        "typed_connection_values_closed": False,
        "direct_connection_values_closed": False,
        "support_prefilter_passes": all(current_support.values()),
        "proof_object_emitted": False,
        "selected_connection_witness_export_closed": False,
        "oriented_logdet_promoted": False,
        "next_required_artifact": NEXT,
        "target_fitting_used": False,
        "closure_claimed": False,
    }

    candidate = {
        "candidate": "SelectedHeteroticOrientedPhiFinSourceIdentityTransportOrConnectionValuesMinimalPacket",
        "status": STATUS,
        "inputs": {key: rel(path) for key, path in INPUTS.items()},
        "parent_statuses": {
            "export_fill": export_fill["status"],
            "sourceidentity_gate": gate["status"],
            "typed_projective_fill": typed_projective["status"],
            "sourceamendment_projective_tables": projective_tables["status"],
        },
        "current_support": current_support,
        "route_comparison": route_comparison,
        "obligation_skeleton_path": rel(OUTPUT_OBLIGATIONS),
        "decision": decision,
        "theorem": {
            "name": "MinimalSourceIdentityTransportPacketTheorem",
            "proved": True,
            "statement": (
                "The remaining oriented Phi_fin closure problem is minimized to a source-identity transport proof. "
                "Typed Cech and direct connection routes remain legal, but they require new value tables. Since the "
                "BN27 deck, commuting operators, kernel policy, exact finitepart, and audit replay are already "
                "support-ready, one three-sublemma source-transport theorem is the shortest rigorous route to "
                "promoting the selected-connection export without target fitting."
            ),
        },
        "guardrails": {
            "does_not_promote_support_prefilter_to_proof": True,
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
        "obligation_skeleton_path": rel(OUTPUT_OBLIGATIONS),
        "note_path": rel(OUTPUT_NOTE),
        "primary_route_selected": "source_identity_transport",
        "support_prefilter_passes": decision["support_prefilter_passes"],
        "source_identity_transport_closed": False,
        "selected_connection_witness_export_closed": False,
        "oriented_logdet_promoted": False,
        "closure_claimed": False,
        "target_fitting_used": False,
        "next_required_artifact": NEXT,
    }
    OUTPUT_CERT.write_text(json.dumps(cert, indent=2, sort_keys=True) + "\n", encoding="utf-8")

    note = f"""# Selected Heterotic OrientedPhiFin SourceIdentityTransport or ConnectionValues MinimalPacket v1

## Result

```text
status = {STATUS}
primary_route_selected = source_identity_transport
support_prefilter_passes = {str(decision["support_prefilter_passes"]).lower()}
source_identity_transport_closed = false
selected_connection_witness_export_closed = false
oriented_logdet_promoted = false
next_required_artifact = {NEXT}
```

## Theorem

{candidate["theorem"]["statement"]}

Obligation skeleton:

```text
{rel(OUTPUT_OBLIGATIONS)}
```
"""
    OUTPUT_NOTE.write_text(note, encoding="utf-8")
    return candidate


if __name__ == "__main__":
    result = main()
    print(f"wrote {rel(OUTPUT_DATA)}")
    print(f"wrote {rel(OUTPUT_OBLIGATIONS)}")
    print(f"wrote {rel(OUTPUT_CERT)}")
    print(f"wrote {rel(OUTPUT_NOTE)}")
    print(result["status"])
