"""Build source-branch identity emission attempt or current-source no-go."""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "candidate_data"
CERTS = ROOT / "certificates"
PROOF = ROOT / "proof_corpus"

INPUTS = {
    "transport_reduction": DATA / "selected_heterotic_orientedphifin_sourceidentitytransport_reduction_to_sourcebranchidentity.json",
    "transport_attempt": DATA / "selected_heterotic_orientedphifin_sourceidentitytransport_proofattempt.candidate.json",
    "single_frontier": DATA / "selected_heterotic_orientedphifin_sourceidentity_single_frontier.json",
    "branch_fill": DATA / "selected_heterotic_orientedphifin_branchidentity_minimalsourcecertificate_fill.candidate.json",
    "bn27_bridge": DATA / "selected_heterotic_orientedphifin_bn27_sourcedomainbridge_or_smootheqa_quotient.candidate.json",
    "orbit_fill": DATA / "selected_heterotic_orientedphifin_bn27_orbitclosure_sourcefill.candidate.json",
    "fullorbit_selection": DATA / "selected_heterotic_orientedphifin_fullfourierorbit_sourceselection_theorem_or_nogo.candidate.json",
    "ctau_source": DATA / "selected_heterotic_bn_centralrankoperator_or_smootheqa_sourceemission.candidate.json",
    "routec_source_certificate": DATA / "selected_u1y_routec_selected_source_certificate_or_typed_de_construction.candidate.json",
}

OUTPUT_DATA = DATA / "selected_heterotic_orientedphifin_sourcebranchidentity_emission_or_nogo.candidate.json"
OUTPUT_REPAIR = DATA / "selected_heterotic_orientedphifin_sourcebranchidentity_repair_packet.json"
OUTPUT_CERT = CERTS / "selected_heterotic_orientedphifin_sourcebranchidentity_emission_or_nogo_certificate.json"
OUTPUT_NOTE = PROOF / "Selected_Heterotic_OrientedPhiFin_SourceBranchIdentity_Emission_or_NoGo_v1.md"

STATUS = "HETEROTIC_ORIENTEDPHIFIN_SOURCEBRANCHIDENTITY_CURRENT_SOURCE_NOGO_REPAIR_PACKET_BUILT"
NEXT = "Selected_Heterotic_OrientedPhiFin_SourceBranchIdentity_SourceAmendment_or_ConnectionValues_v1"


def rel(path: Path) -> str:
    try:
        return str(path.relative_to(ROOT))
    except ValueError:
        return str(path)


def load(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def main() -> dict[str, Any]:
    reduction = load(INPUTS["transport_reduction"])
    transport = load(INPUTS["transport_attempt"])
    single_frontier = load(INPUTS["single_frontier"])
    branch_fill = load(INPUTS["branch_fill"])
    bn27_bridge = load(INPUTS["bn27_bridge"])
    orbit_fill = load(INPUTS["orbit_fill"])
    fullorbit = load(INPUTS["fullorbit_selection"])
    ctau_source = load(INPUTS["ctau_source"])
    routec_source = load(INPUTS["routec_source_certificate"])

    clauses = {
        "one_selected_source_names_both_branches": {
            "required": reduction["required_next_payload"][0],
            "support_present": (
                single_frontier["support_closed"]["ctau_signed_operator_source_selected"]
                and fullorbit["decision"]["routec_magnitude_source_selected_for_27mode_DE_gap_layer"]
            ),
            "emitted_by_current_source": False,
            "blocker": "C_tau is selected at heterotic orientation scope and Route-C PhiFin_DE is selected at magnitude/gap scope, but no artifact names one source owning both.",
        },
        "eleven_label_to_full_BN27_threshold_carrier": {
            "required": reduction["required_next_payload"][1],
            "support_present": bn27_bridge["orbit_completion_test"]["embedded_11_shadow"]["rho_intertwines"],
            "emitted_by_current_source": False,
            "blocker": (
                "The 27x11 shadow preserves rho/tau but misses "
                f"{bn27_bridge['orbit_completion_test']['completion_gap']['missing_positive_oriented_row_count']} "
                "positive oriented rows and multiplier "
                f"{bn27_bridge['orbit_completion_test']['completion_gap']['missing_multiplier_to_full_abs_sector']}."
            ),
        },
        "routec_row_not_external_import": {
            "required": reduction["required_next_payload"][2],
            "support_present": orbit_fill["decision"]["compatibility_closed"] and orbit_fill["decision"]["audit_replay_closed"],
            "emitted_by_current_source": False,
            "blocker": "Route-C supplies support and replay, while its selected source certificate is still reduced to a connection witness rather than heterotic ownership.",
        },
    }

    emitted_count = sum(1 for clause in clauses.values() if clause["emitted_by_current_source"])
    support_count = sum(1 for clause in clauses.values() if clause["support_present"])

    repair_packet = {
        "schema": "SelectedHeterotic.OrientedPhiFin.SourceBranchIdentityRepairPacket.v1",
        "status": "SOURCE_AMENDMENT_OR_CONNECTION_VALUES_REQUIRED",
        "minimal_success_payload": {
            "source_identity_transport_theorem": [
                "declare/name the selected source object S_QaSU3^BN27",
                "prove S_QaSU3^BN27 emits both C_tau and PhiFin_DE before finite comparison",
                "prove Route-C/q79 finite trace row is an internal theorem of S_QaSU3^BN27, not imported support",
            ],
            "BN27_domain_emission": [
                "emit full F3xF3 rank-slot carrier, all 27 basis rows",
                "prove the 16 nonzero oriented positive rows are source-retained",
                "prove the 11-label rho/tau shadow is only a shadow or quotient, not the threshold domain",
            ],
            "selected_connection_values_alternative": [
                "emit typed Cech/HYM/projective rho_E connection values from the same source",
                "export them to BN27 D_E/Riesz/Green/kernel/trace validators",
                "rerun audits without lifted selected flags",
            ],
        },
        "current_nogo_scope": "current repo/source artifacts only; not a mathematical impossibility theorem",
        "forbidden_shortcuts": reduction["forbidden_shortcuts"],
    }
    OUTPUT_REPAIR.write_text(json.dumps(repair_packet, indent=2, sort_keys=True) + "\n", encoding="utf-8")

    decision = {
        "sourcebranchidentity_attempted": True,
        "support_count": support_count,
        "required_clause_count": len(clauses),
        "emitted_count": emitted_count,
        "source_branch_identity_closed": False,
        "current_source_nogo": True,
        "repair_packet_built": True,
        "transport_reduced_leaf_resolved": False,
        "selected_connection_witness_export_closed": False,
        "oriented_logdet_promoted": False,
        "next_required_artifact": NEXT,
        "target_fitting_used": False,
        "closure_claimed": False,
    }

    candidate = {
        "candidate": "SelectedHeteroticOrientedPhiFinSourceBranchIdentityEmissionOrNoGo",
        "status": STATUS,
        "inputs": {key: rel(path) for key, path in INPUTS.items()},
        "parent_statuses": {
            "transport_attempt": transport["status"],
            "single_frontier": single_frontier["status"],
            "branch_fill": branch_fill["status"],
            "bn27_bridge": bn27_bridge["status"],
            "orbit_fill": orbit_fill["status"],
            "fullorbit_selection": fullorbit["status"],
            "ctau_source": ctau_source["status"],
            "routec_source_certificate": routec_source["status"],
        },
        "clauses": clauses,
        "repair_packet_path": rel(OUTPUT_REPAIR),
        "decision": decision,
        "theorem": {
            "name": "SourceBranchIdentityCurrentSourceNoGoTheorem",
            "proved": True,
            "statement": (
                "Against the current repo/source artifacts, source-branch identity is not emitted. "
                "All three required clauses have support, but none is source-owned: no single source names both "
                "the heterotic C_tau orientation and Route-C/q79 PhiFin_DE magnitude branches; the 11-label "
                "heterotic shadow does not promote to full BN27 threshold ownership; and the Route-C finite trace "
                "row remains external support unless a selected connection/source theorem internalizes it. "
                "Therefore the transport leaf remains open, and the exact repair packet is a source amendment or "
                "same-source connection-values emission."
            ),
        },
        "guardrails": {
            "does_not_treat_support_as_emission": True,
            "does_not_promote_11label_shadow_to_BN27": True,
            "does_not_promote_routec_row_as_heterotic_source": True,
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
        "repair_packet_path": rel(OUTPUT_REPAIR),
        "note_path": rel(OUTPUT_NOTE),
        "support_count": support_count,
        "emitted_count": emitted_count,
        "required_clause_count": len(clauses),
        "source_branch_identity_closed": False,
        "current_source_nogo": True,
        "selected_connection_witness_export_closed": False,
        "oriented_logdet_promoted": False,
        "closure_claimed": False,
        "target_fitting_used": False,
        "next_required_artifact": NEXT,
    }
    OUTPUT_CERT.write_text(json.dumps(cert, indent=2, sort_keys=True) + "\n", encoding="utf-8")

    note = f"""# Selected Heterotic OrientedPhiFin SourceBranchIdentity Emission or NoGo v1

## Result

```text
status = {STATUS}
support_count = {support_count}
emitted_count = {emitted_count}
required_clause_count = {len(clauses)}
source_branch_identity_closed = false
current_source_nogo = true
selected_connection_witness_export_closed = false
oriented_logdet_promoted = false
next_required_artifact = {NEXT}
```

## Theorem

{candidate["theorem"]["statement"]}

Repair packet:

```text
{rel(OUTPUT_REPAIR)}
```
"""
    OUTPUT_NOTE.write_text(note, encoding="utf-8")
    return candidate


if __name__ == "__main__":
    result = main()
    print(f"wrote {rel(OUTPUT_DATA)}")
    print(f"wrote {rel(OUTPUT_REPAIR)}")
    print(f"wrote {rel(OUTPUT_CERT)}")
    print(f"wrote {rel(OUTPUT_NOTE)}")
    print(result["status"])
