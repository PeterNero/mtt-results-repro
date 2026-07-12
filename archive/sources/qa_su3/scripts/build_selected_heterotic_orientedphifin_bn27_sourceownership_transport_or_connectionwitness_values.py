"""Build the BN27 source-ownership transport/connection-witness value gate."""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "candidate_data"
CERTS = ROOT / "certificates"
PROOF = ROOT / "proof_corpus"

INPUTS = {
    "sourceowned_certificate": DATA / "selected_heterotic_orientedphifin_sourceowned_bn27_certificate_or_bundleA_selector.candidate.json",
    "refined_certificate": DATA / "selected_heterotic_orientedphifin_bn27_source_owned_certificate.refined.json",
    "connection_export_fill": DATA / "selected_heterotic_orientedphifin_selectedconnectionwitness_export_fill.candidate.json",
    "minimal_source_values_packet": DATA / "selected_heterotic_orientedphifin_selectedconnectionwitness_minimal_source_values_packet.json",
    "sourceidentity_minimal_packet": DATA / "selected_heterotic_orientedphifin_sourceidentitytransport_or_connectionvalues_minimalpacket.candidate.json",
    "sourceidentity_proofattempt": DATA / "selected_heterotic_orientedphifin_sourceidentitytransport_proofattempt.candidate.json",
    "projective_rhoe_lift_nogo": DATA / "selected_heterotic_orientedphifin_projectiverhoe_bn27lift_or_directsource_theorem.candidate.json",
    "direct_bn27_declaration_fill": DATA / "selected_heterotic_orientedphifin_directbn27_sourcedeclaration_fill_or_bundleA_selector.candidate.json",
}

OUTPUT_DATA = DATA / "selected_heterotic_orientedphifin_bn27_sourceownership_transport_or_connectionwitness_values.candidate.json"
OUTPUT_TEMPLATE = DATA / "selected_heterotic_orientedphifin_bn27_sourceownership_transport_witness.template.json"
OUTPUT_CERT = CERTS / "selected_heterotic_orientedphifin_bn27_sourceownership_transport_or_connectionwitness_values_certificate.json"
OUTPUT_NOTE = PROOF / "Selected_Heterotic_OrientedPhiFin_BN27_SourceOwnership_Transport_or_ConnectionWitness_Values_v1.md"

STATUS = "HETEROTIC_ORIENTEDPHIFIN_BN27_SOURCEOWNERSHIP_TRANSPORT_VALUES_BRANCHCERT_CLOSED_TRANSPORT_OPEN"
NEXT = "Selected_Heterotic_OrientedPhiFin_DirectBN27_SourceIdentityTransport_Fill_or_TypedConnectionWitnessValues_v1"


def rel(path: Path) -> str:
    try:
        return str(path.relative_to(ROOT))
    except ValueError:
        return str(path)


def load(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def main() -> dict[str, Any]:
    sourceowned = load(INPUTS["sourceowned_certificate"])
    refined = load(INPUTS["refined_certificate"])
    export = load(INPUTS["connection_export_fill"])
    minimal = load(INPUTS["sourceidentity_minimal_packet"])
    proofattempt = load(INPUTS["sourceidentity_proofattempt"])
    projective = load(INPUTS["projective_rhoe_lift_nogo"])
    direct = load(INPUTS["direct_bn27_declaration_fill"])
    minimal_source_values = load(INPUTS["minimal_source_values_packet"])

    bn27_fields = refined["BN27_source_ownership_fields"]
    branch_closed = refined["source_certificate"]["heterotic_QaSU3_branch_certificate_closed"]
    export_decision = export["decision"]
    support = refined["support_values"]

    template = {
        "schema": "SelectedHeterotic.OrientedPhiFin.BN27.SourceOwnershipTransportWitness.Template.v1",
        "purpose": "Minimal values/theorems required to export the certified heterotic Qa/SU3 branch to the full oriented BN27 threshold packet without Route-C import or target fitting.",
        "required_closed_payload": {
            "source_identity_transport_theorem": None,
            "S_QaSU3_BN27_declaration": None,
            "EndE_or_rhoE_to_BN27_carrier_functor": None,
            "BN27_deck_action_export": None,
            "operator_coemission_export": None,
            "kernel_policy_export": None,
            "trace_policy_export": None,
            "finitepart_identity_export": None,
            "not_routec_import_proof": None,
        },
        "connection_values_family": {
            "typed_cech_monad_values": {
                "status": "open",
                "required": [
                    "typed f_i/g_i section representatives",
                    "Cech transition tables",
                    "g o f = 0 certificate",
                    "finite BN27 operator export",
                ],
            },
            "direct_hym_connection_values": {
                "status": "open",
                "required": [
                    "selected A/F_A coefficients",
                    "HYM residual certificate",
                    "BN27 threshold trace export",
                ],
            },
            "smooth_EQa_quotient_values": {
                "status": "open",
                "required": [
                    "selected smooth bundle connection",
                    "representation trace producing E_Qa",
                    "quotient map to oriented BN27",
                ],
            },
            "direct_BN27_source_theorem_values": {
                "status": "open",
                "required": [
                    "same-branch source theorem naming BN27 as selected source",
                    "full F3xF3 rank-slot carrier emission before finite comparison",
                    "no-Route-C-import provenance proof",
                ],
            },
        },
        "forbidden_shortcuts": [
            "treating branch certificate closure as BN27 source ownership",
            "promoting log(92160000) from support-only finite trace",
            "reopening projective rho_E as a full BN27 threshold lift",
            "using observed electroweak data or benchmark values",
        ],
        "target_fitting_used": False,
    }
    OUTPUT_TEMPLATE.write_text(json.dumps(template, indent=2, sort_keys=True) + "\n", encoding="utf-8")

    route_ranking = {
        "rank_1_source_identity_transport_or_direct_BN27_source": {
            "closed_now": False,
            "why_ranked_first": "The proofattempt already reduces transport to one unconditional source-branch identity leaf; the improved certificate supplies branch provenance but not S_QaSU3^BN27.",
            "remaining_missing": proofattempt["sublemma_attempts"]["source_branch_identity"]["missing_payload"],
            "new_values_needed": template["connection_values_family"]["direct_BN27_source_theorem_values"]["required"],
        },
        "rank_2_selected_connection_witness_values": {
            "closed_now": False,
            "why_ranked_second": "All six export fields are support-ready, but only audit replay is source-filled; actual selected connection values would own the deck/operator/kernel/trace exports directly.",
            "support_ready_count": export_decision["support_ready_count"],
            "export_filled_count": export_decision["export_filled_count"],
            "export_required_count": export_decision["export_required_count"],
            "family_fill": export["family_fill"],
        },
        "rank_3_projective_rhoE_BN27_lift": {
            "closed_now": False,
            "retired_as_threshold_proof_source": True,
            "why_retired": projective["lift_tests"]["domain_lift"]["reason"],
            "orientation_shadow_still_valid": projective["lift_tests"]["domain_lift"]["orientation_shadow_passes"],
            "missing_positive_oriented_rows": projective["lift_tests"]["domain_lift"]["missing_positive_oriented_rows"],
        },
        "rank_4_smooth_bundle_A_or_EQa_quotient": {
            "closed_now": False,
            "why_larger": "This remains legal, but it requires smooth connection/quotient data before it can own the finite BN27 packet.",
            "direct_fill_open_source_leaves": direct["filled_support_summary"]["open_source_leaves"],
        },
    }

    decision = {
        "branch_certificate_closed": branch_closed,
        "S_QaSU3_BN27_declared_as_selected_source": False,
        "transport_witness_values_found": False,
        "BN27_source_ownership_transport_closed": False,
        "selected_connection_witness_values_closed": False,
        "projective_rhoE_lift_reopened": False,
        "direct_BN27_source_declaration_closed": False,
        "oriented_logdet_promoted": False,
        "template_path": rel(OUTPUT_TEMPLATE),
        "next_required_artifact": NEXT,
        "closure_claimed": False,
        "target_fitting_used": False,
    }

    candidate = {
        "candidate": "SelectedHeteroticOrientedPhiFinBN27SourceOwnershipTransportOrConnectionWitnessValues",
        "status": STATUS,
        "inputs": {key: rel(path) for key, path in INPUTS.items()},
        "parent_statuses": {
            "sourceowned_certificate": sourceowned["status"],
            "connection_export_fill": export["status"],
            "sourceidentity_minimal_packet": minimal["status"],
            "sourceidentity_proofattempt": proofattempt["status"],
            "projective_rhoe_lift_nogo": projective["status"],
            "direct_bn27_declaration_fill": direct["status"],
        },
        "support_now_locked": {
            "heterotic_branch_value": refined["source_certificate"]["heterotic_QaSU3_branch_value"],
            "basis_dimension": support["basis_dimension"],
            "oriented_nonzero_count": support["oriented_nonzero_count"],
            "oriented_abs_sector_product": support["oriented_abs_sector_product"],
            "oriented_abs_sector_logdet_exact": support["oriented_abs_sector_logdet_exact"],
            "C_tau_orientation_bound": refined["support_owned_or_replayed"]["C_tau_orientation_bound_to_same_threshold_complex"],
            "kernel_zero_mode_shared_circle_policy_replayed": refined["support_owned_or_replayed"]["kernel_zero_mode_shared_circle_policy_replayed"],
            "audit_replay_export_filled": refined["support_owned_or_replayed"]["audit_replay_export_filled"],
            "minimal_source_values_packet_keys": sorted(minimal_source_values.keys()),
        },
        "BN27_source_ownership_fields": bn27_fields,
        "route_ranking": route_ranking,
        "transport_witness_template_path": rel(OUTPUT_TEMPLATE),
        "decision": decision,
        "theorem": {
            "name": "BN27SourceOwnershipTransportValuesFrontierTheorem",
            "proved": True,
            "statement": (
                "After the heterotic Qa/SU3 branch certificate is closed, the BN27 source-ownership problem is reduced "
                "to a transport/connection-witness value problem. The branch certificate improves provenance but does not "
                "declare S_QaSU3^BN27. The shortest rigorous closure remains a direct source-identity transport theorem; "
                "a selected connection witness is the constructive alternative; the projective rho_E lift stays retired as "
                "a full BN27 threshold proof source."
            ),
        },
        "guardrails": {
            "does_not_treat_branch_certificate_as_BN27_source_ownership": True,
            "does_not_promote_log92160000": True,
            "does_not_promote_routec_import": True,
            "does_not_reopen_projective_rhoE_lift": True,
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
        "template_path": rel(OUTPUT_TEMPLATE),
        "note_path": rel(OUTPUT_NOTE),
        "branch_certificate_closed": branch_closed,
        "BN27_source_ownership_transport_closed": False,
        "selected_connection_witness_values_closed": False,
        "projective_rhoE_lift_reopened": False,
        "oriented_logdet_promoted": False,
        "closure_claimed": False,
        "target_fitting_used": False,
        "next_required_artifact": NEXT,
    }
    OUTPUT_CERT.write_text(json.dumps(cert, indent=2, sort_keys=True) + "\n", encoding="utf-8")

    note = f"""# Selected Heterotic OrientedPhiFin BN27 SourceOwnership Transport or ConnectionWitness Values v1

## Result

```text
status = {STATUS}
branch_certificate_closed = true
S_QaSU3_BN27_declared_as_selected_source = false
transport_witness_values_found = false
BN27_source_ownership_transport_closed = false
selected_connection_witness_values_closed = false
projective_rhoE_lift_reopened = false
oriented_logdet_promoted = false
next_required_artifact = {NEXT}
```

## Theorem

{candidate["theorem"]["statement"]}

## Ranking

1. Source-identity transport / direct BN27 source theorem remains shortest.
2. Selected connection witness values are constructive but still require actual source-owned deck/operator/kernel/trace exports.
3. Projective rho_E remains an orientation shadow only and is retired as a full BN27 threshold proof source.
4. Smooth BundleA/E_Qa quotient remains legal but larger.

## Witness Template

```text
{rel(OUTPUT_TEMPLATE)}
```
"""
    OUTPUT_NOTE.write_text(note, encoding="utf-8")
    return candidate


if __name__ == "__main__":
    result = main()
    print(f"wrote {rel(OUTPUT_DATA)}")
    print(f"wrote {rel(OUTPUT_TEMPLATE)}")
    print(f"wrote {rel(OUTPUT_CERT)}")
    print(f"wrote {rel(OUTPUT_NOTE)}")
    print(result["status"])
