"""Build heterotic/Route-C same-source identity or selected connection witness gate."""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "candidate_data"
CERTS = ROOT / "certificates"
PROOF = ROOT / "proof_corpus"

INPUTS = {
    "bn27_orbitclosure_fill": DATA / "selected_heterotic_orientedphifin_bn27_orbitclosure_sourcefill.candidate.json",
    "bn27_orbitclosure_report": DATA / "selected_heterotic_orientedphifin_bn27_orbitclosure_sourcefill_report.json",
    "u1y_source_certificate_gate": DATA / "selected_u1y_routec_selected_source_certificate_or_typed_de_construction.candidate.json",
    "u1y_connection_witness_contract": DATA / "selected_u1y_routec_typed_monad_cech_or_hym_connection_witness.candidate.json",
    "u1y_finite_hym_partial": DATA / "selected_u1y_routec_finite_hym_connection_solve_or_typed_cech_payload.candidate.json",
    "heterotic_phifin_bridge": DATA / "selected_heterotic_phifin_sourceidentity_bridge_attempt.candidate.json",
    "heterotic_bundle_gate": DATA / "selected_heterotic_bundleconnection_valuesolve_or_phifin_sourceidentity_proof.candidate.json",
}

OUTPUT_DATA = DATA / "selected_heterotic_orientedphifin_heterotic_routec_sourceidentity_or_selectedconnectionwitness.candidate.json"
OUTPUT_REQUEST = DATA / "selected_heterotic_orientedphifin_selectedconnectionwitness_export_request.json"
OUTPUT_CERT = CERTS / "selected_heterotic_orientedphifin_heterotic_routec_sourceidentity_or_selectedconnectionwitness_certificate.json"
OUTPUT_NOTE = PROOF / "Selected_Heterotic_OrientedPhiFin_HeteroticRouteC_SourceIdentity_or_SelectedConnectionWitness_v1.md"

STATUS = "HETEROTIC_ORIENTEDPHIFIN_HETEROTIC_ROUTEC_SOURCEIDENTITY_OPEN_CONNECTION_WITNESS_REQUEST_BUILT"
NEXT = "Selected_Heterotic_OrientedPhiFin_SelectedConnectionWitness_Export_Fill_v1"


def rel(path: Path) -> str:
    try:
        return str(path.relative_to(ROOT))
    except ValueError:
        return str(path)


def load(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def main() -> dict[str, Any]:
    bn27 = load(INPUTS["bn27_orbitclosure_fill"])
    bn27_report = load(INPUTS["bn27_orbitclosure_report"])
    source_gate = load(INPUTS["u1y_source_certificate_gate"])
    witness = load(INPUTS["u1y_connection_witness_contract"])
    finite_hym = load(INPUTS["u1y_finite_hym_partial"])
    phifin_bridge = load(INPUTS["heterotic_phifin_bridge"])
    bundle_gate = load(INPUTS["heterotic_bundle_gate"])

    route_status = {
        "same_source_identity": {
            "closed": False,
            "support": {
                "heterotic_branch_has_monad_topology": True,
                "routec_BN27_gap_layer_closed": finite_hym["decision"]["DE_action_closed_for_gap_layer"],
                "bn27_compatibility_closed": bn27["decision"]["compatibility_closed"],
                "bn27_audit_replay_closed": bn27["decision"]["audit_replay_closed"],
            },
            "blocker": "no theorem identifies heterotic Qa/SU3 source ownership with the Route-C/q79 finite trace source for this threshold row",
        },
        "typed_monad_cech_witness": {
            "closed": witness["decision"]["typed_monad_cech_values_present"],
            "missing_count": witness["payload_counts"]["typed_monad_cech_missing"],
            "blocker": "typed global f_i/g_i sections, Cech transitions, g o f, exactness, and selected Hermitian/B_N export are absent",
        },
        "direct_hym_witness": {
            "closed": witness["decision"]["direct_hym_values_present"],
            "missing_count": witness["payload_counts"]["direct_hym_missing"],
            "blocker": "selected HYM/Strominger connection coefficients, gauge fixing, finite residual, and gap certificate are absent",
        },
        "finite_routec_solve_witness": {
            "closed": witness["decision"]["finite_routec_solve_values_present"],
            "missing_count": witness["payload_counts"]["finite_routec_solve_missing"],
            "blocker": "finite Route-C solve has 27-mode D_E gap support, but not selected source provenance/export for the full witness",
        },
        "smooth_bundle_EQa_witness": {
            "closed": False,
            "support": {
                "heterotic_bundle_gate_status": bundle_gate["status"],
                "phifin_bridge_status": phifin_bridge["status"],
            },
            "blocker": "selected A/F_A, representation action, smooth E_Qa, and quotient-to-BN27 trace theorem are absent",
        },
    }

    export_request = {
        "schema": "SelectedHeterotic.OrientedPhiFin.SelectedConnectionWitnessExportRequest.v1",
        "status": "SELECTED_CONNECTION_WITNESS_EXPORT_REQUIRED",
        "purpose": "Export the selected BN27 deck action into heterotic oriented Phi_fin threshold ownership.",
        "acceptable_witness_families": {
            "typed_monad_cech": witness["witness_routes"]["typed_monad_cech"],
            "direct_hym": witness["witness_routes"]["direct_hym"],
            "finite_routec_solve": witness["witness_routes"]["finite_routec_solve"],
            "smooth_EQa_quotient": [
                "selected A/F_A or equivalent smooth bundle connection",
                "representation action and trace pairing",
                "finite quotient functor to full BN27",
                "heat/zeta/torsion finitepart reducing to log(92160000)",
            ],
        },
        "must_export_to_oriented_phifin": {
            "source_identity": "same source owns heterotic Qa/SU3 branch and Route-C/q79 BN27 finite trace row",
            "BN27_deck_action": "uniform F3xF3 Fourier deck with rank slots r=0,1,2",
            "operators": "C_tau orientation and PhiFin_DE magnitude emitted in one source algebra",
            "kernel_policy": "C_tau=0 rank and PhiFin zero cluster policy selected before finitepart",
            "trace_policy": "uniform BN27 trace weights/source-owned zeta finitepart",
            "audit_replay": "rerun oriented table, coemission, BN27 orbit closure, and log(92160000) without lifted flags",
        },
        "forbidden_shortcuts": [
            "treat Route-C support as heterotic source identity",
            "treat selected trace equality for D_E gap layer as full selected connection witness",
            "use typed/HYM abstract existence without emitted values",
            "use lifted selected flags or smoke residuals",
            "promote log(92160000) before witness export",
        ],
    }
    OUTPUT_REQUEST.write_text(json.dumps(export_request, indent=2, sort_keys=True) + "\n", encoding="utf-8")

    decision = {
        "gate_executed": True,
        "same_source_identity_closed": False,
        "selected_connection_witness_export_closed": False,
        "typed_monad_cech_witness_closed": False,
        "direct_hym_witness_closed": False,
        "finite_routec_solve_witness_closed": False,
        "smooth_EQa_quotient_witness_closed": False,
        "connection_witness_export_request_built": True,
        "BN27_orbitclosure_source_bridge_closed": False,
        "branch_identity_closed": False,
        "oriented_logdet_promoted": False,
        "minimal_next_leaf": "selected_connection_witness_export_to_BN27_oriented_PhiFin",
        "next_required_artifact": NEXT,
        "target_fitting_used": False,
        "closure_claimed": False,
    }

    candidate = {
        "candidate": "SelectedHeteroticOrientedPhiFinHeteroticRouteCSourceIdentityOrSelectedConnectionWitness",
        "status": STATUS,
        "inputs": {key: rel(path) for key, path in INPUTS.items()},
        "parent_statuses": {
            "bn27_orbitclosure_fill": bn27["status"],
            "bn27_orbitclosure_report": bn27_report["status"],
            "u1y_source_certificate_gate": source_gate["status"],
            "u1y_connection_witness_contract": witness["status"],
            "u1y_finite_hym_partial": finite_hym["status"],
            "heterotic_phifin_bridge": phifin_bridge["status"],
            "heterotic_bundle_gate": bundle_gate["status"],
        },
        "route_status": route_status,
        "connection_witness_export_request_path": rel(OUTPUT_REQUEST),
        "decision": decision,
        "theorem": {
            "name": "HeteroticRouteCSourceIdentityOrSelectedConnectionWitnessGateTheorem",
            "proved": True,
            "statement": (
                "The BN27 orbit-closure cutset cannot be closed by existing Route-C support "
                "alone. Current artifacts close the 27-mode D_E gap/Riesz/Green layer and "
                "provide a machine-readable connection-witness contract, but they explicitly "
                "leave selected source provenance, typed Cech/HYM/finite connection values, "
                "and smooth E_Qa quotient data open. Therefore the oriented Phi_fin branch "
                "requires one selected connection witness export, or an explicit theorem that "
                "the heterotic Qa/SU3 source and Route-C/q79 finite trace source are the same "
                "source for this BN27 threshold row."
            ),
        },
        "guardrails": {
            "does_not_promote_routec_support_to_source_identity": True,
            "does_not_promote_abstract_hym_existence": True,
            "does_not_use_lifted_selected_flags": True,
            "does_not_promote_log92160000": True,
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
        "connection_witness_export_request_path": rel(OUTPUT_REQUEST),
        "note_path": rel(OUTPUT_NOTE),
        "same_source_identity_closed": False,
        "selected_connection_witness_export_closed": False,
        "BN27_orbitclosure_source_bridge_closed": False,
        "branch_identity_closed": False,
        "oriented_logdet_promoted": False,
        "closure_claimed": False,
        "target_fitting_used": False,
        "next_required_artifact": NEXT,
    }
    OUTPUT_CERT.write_text(json.dumps(cert, indent=2, sort_keys=True) + "\n", encoding="utf-8")

    note = f"""# Selected Heterotic OrientedPhiFin HeteroticRouteC SourceIdentity or SelectedConnectionWitness v1

## Result

```text
status = {STATUS}
same_source_identity_closed = false
selected_connection_witness_export_closed = false
BN27_orbitclosure_source_bridge_closed = false
branch_identity_closed = false
oriented_logdet_promoted = false
next_required_artifact = {NEXT}
```

## Theorem

{candidate["theorem"]["statement"]}

Request:

```text
{rel(OUTPUT_REQUEST)}
```
"""
    OUTPUT_NOTE.write_text(note, encoding="utf-8")
    return candidate


if __name__ == "__main__":
    result = main()
    print(f"wrote {rel(OUTPUT_DATA)}")
    print(f"wrote {rel(OUTPUT_REQUEST)}")
    print(f"wrote {rel(OUTPUT_CERT)}")
    print(f"wrote {rel(OUTPUT_NOTE)}")
    print(result["status"])
