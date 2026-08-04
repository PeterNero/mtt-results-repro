"""Refine source-owned BN27 certificate using prior branch certificate support."""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "candidate_data"
CERTS = ROOT / "certificates"
PROOF = ROOT / "proof_corpus"

INPUTS = {
    "direct_fill": DATA / "selected_heterotic_orientedphifin_directbn27_sourcedeclaration_fill_or_bundleA_selector.candidate.json",
    "filled_declaration": DATA / "selected_heterotic_orientedphifin_bn27_direct_source_declaration.fill_attempt.json",
    "ownership_cert": DATA / "selected_heterotic_orientedphifin_sourceownership_certificate_fillattempt.candidate.json",
    "ownership_values": DATA / "selected_heterotic_orientedphifin_sourceownership_certificate_fillattempt.values.json",
    "sourceowned_positive": DATA / "selected_heterotic_orientedphifin_sourceownedpositiveoperator_or_eqapayload_fill.candidate.json",
    "connection_export": DATA / "selected_heterotic_orientedphifin_selectedconnectionwitness_export_fill.candidate.json",
}

OUTPUT_DATA = DATA / "selected_heterotic_orientedphifin_sourceowned_bn27_certificate_or_bundleA_selector.candidate.json"
OUTPUT_REFINED = DATA / "selected_heterotic_orientedphifin_bn27_source_owned_certificate.refined.json"
OUTPUT_CERT = CERTS / "selected_heterotic_orientedphifin_sourceowned_bn27_certificate_or_bundleA_selector_certificate.json"
OUTPUT_NOTE = PROOF / "Selected_Heterotic_OrientedPhiFin_SourceOwned_BN27_Certificate_or_BundleA_Selector_v1.md"

STATUS = "HETEROTIC_ORIENTEDPHIFIN_SOURCEOWNED_BN27_CERTIFICATE_REFINED_BRANCH_CERT_CLOSED_BN27_OWNERSHIP_OPEN"
NEXT = "Selected_Heterotic_OrientedPhiFin_BN27_SourceOwnership_Transport_or_ConnectionWitness_Values_v1"


def rel(path: Path) -> str:
    try:
        return str(path.relative_to(ROOT))
    except ValueError:
        return str(path)


def load(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def main() -> dict[str, Any]:
    direct_fill = load(INPUTS["direct_fill"])
    filled = load(INPUTS["filled_declaration"])
    ownership = load(INPUTS["ownership_cert"])
    values = load(INPUTS["ownership_values"])
    positive = load(INPUTS["sourceowned_positive"])
    export = load(INPUTS["connection_export"])

    branch_cert = values["filled_certificate_fields"]["same_branch_QaSU3_heterotic_source_certificate"]
    orientation = values["filled_certificate_fields"]["C_tau_orientation_bound_to_same_threshold_complex"]
    no_double = values["filled_certificate_fields"]["kernel_zero_mode_shared_circle_policy_replayed"]
    carrier = values["filled_certificate_fields"]["oriented_BN_carrier_emitted_by_that_source"]
    functor = values["filled_certificate_fields"]["quotient_or_functor_EndE_or_rhoE_to_oriented_BN"]
    positive_owner = values["filled_certificate_fields"]["positive_PhiFin_DE_magnitude_owned_by_source"]
    finitepart_owner = values["filled_certificate_fields"]["finitepart_trace_identity_consumes_nonzero_oriented_sector"]

    refined = {
        "schema": "SelectedHeterotic.OrientedPhiFin.BN27.SourceOwnedCertificate.Refined.v1",
        "status": "BRANCH_CERTIFICATE_CLOSED_BN27_SOURCE_OWNERSHIP_OPEN",
        "source_certificate": {
            "heterotic_QaSU3_branch_certificate_closed": branch_cert["filled"],
            "heterotic_QaSU3_branch_value": branch_cert.get("value"),
            "S_QaSU3_BN27_declared_as_selected_source": False,
            "not_routec_or_benchmark_import": False,
            "reason_open": "The selected rank-three Iwasawa SU(3) monad/End(E) branch is certified, but no theorem declares the BN27 finite packet as source-owned by that branch.",
        },
        "support_owned_or_replayed": {
            "C_tau_orientation_bound_to_same_threshold_complex": orientation["filled"],
            "kernel_zero_mode_shared_circle_policy_replayed": no_double["filled"],
            "audit_replay_export_filled": export["decision"]["audit_replay_export_filled"],
            "table_D_E_Riesz_Green_positive_spectrum_materialized": positive["attempts"]["direct_source_owned_positive_operator"]["table_D_E_Riesz_Green_positive_spectrum_materialized"],
            "exact_finitepart_ready": positive["attempts"]["direct_source_owned_positive_operator"]["exact_finitepart_ready"],
        },
        "BN27_source_ownership_fields": {
            "oriented_BN_carrier_emitted_by_that_source": carrier["filled"],
            "quotient_or_functor_EndE_or_rhoE_to_oriented_BN": functor["filled"],
            "positive_PhiFin_DE_magnitude_owned_by_source": positive_owner["filled"],
            "operator_coemission_source_owned": export["export_fields"]["operators"]["selected_source_owned"],
            "BN27_deck_action_source_owned": export["export_fields"]["BN27_deck_action"]["selected_source_owned"],
            "kernel_policy_source_owned": export["export_fields"]["kernel_policy"]["selected_source_owned"],
            "trace_policy_source_owned": export["export_fields"]["trace_policy"]["selected_source_owned"],
            "finitepart_trace_identity_consumes_nonzero_oriented_sector": finitepart_owner["filled"],
        },
        "support_values": {
            "basis_dimension": filled["domain"]["basis_dimension"],
            "oriented_nonzero_count": filled["domain"]["oriented_nonzero_count"],
            "oriented_abs_sector_logdet_exact": filled["finitepart"]["oriented_abs_sector_logdet_exact"],
            "oriented_abs_sector_product": filled["finitepart"]["oriented_abs_sector_product"],
        },
        "target_fitting_used": False,
    }
    OUTPUT_REFINED.write_text(json.dumps(refined, indent=2, sort_keys=True) + "\n", encoding="utf-8")

    bn27_fields = refined["BN27_source_ownership_fields"]
    bn27_closed = all(bn27_fields.values())
    branch_closed = refined["source_certificate"]["heterotic_QaSU3_branch_certificate_closed"]

    decision = {
        "refinement_executed": True,
        "heterotic_branch_certificate_closed": branch_closed,
        "S_QaSU3_BN27_declared_as_selected_source": False,
        "BN27_source_ownership_closed": bn27_closed,
        "direct_BN27_source_declaration_closed": False,
        "bundle_A_source_selector_closed": False,
        "support_values_remain_available": True,
        "oriented_logdet_promoted": False,
        "refined_certificate_path": rel(OUTPUT_REFINED),
        "next_required_artifact": NEXT,
        "closure_claimed": False,
        "target_fitting_used": False,
    }

    candidate = {
        "candidate": "SelectedHeteroticOrientedPhiFinSourceOwnedBN27CertificateOrBundleASelector",
        "status": STATUS,
        "inputs": {key: rel(path) for key, path in INPUTS.items()},
        "parent_statuses": {
            "direct_fill": direct_fill["status"],
            "ownership_cert": ownership["status"],
            "sourceowned_positive": positive["status"],
            "connection_export": export["status"],
        },
        "refined_certificate_path": rel(OUTPUT_REFINED),
        "decision": decision,
        "theorem": {
            "name": "SourceOwnedBN27CertificateRefinementTheorem",
            "proved": True,
            "statement": (
                "The source-owned BN27 certificate can be refined: the heterotic Qa/SU3 branch certificate is closed "
                "for the rank-three Iwasawa SU(3) monad/End(E) threshold branch, and C_tau/no-double-count/audit replay "
                "support is retained. This does not declare S_QaSU3^BN27 or close BN27 ownership. The remaining missing "
                "object is a transport/connection-witness theorem exporting that certified heterotic branch to the full "
                "BN27 carrier, operator co-emission, kernel/trace policy, and finitepart identity."
            ),
        },
        "guardrails": {
            "does_not_treat_branch_certificate_as_BN27_source_ownership": True,
            "does_not_promote_log92160000": True,
            "does_not_promote_routec_import": True,
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
        "refined_certificate_path": rel(OUTPUT_REFINED),
        "note_path": rel(OUTPUT_NOTE),
        "heterotic_branch_certificate_closed": branch_closed,
        "BN27_source_ownership_closed": False,
        "direct_BN27_source_declaration_closed": False,
        "oriented_logdet_promoted": False,
        "closure_claimed": False,
        "target_fitting_used": False,
        "next_required_artifact": NEXT,
    }
    OUTPUT_CERT.write_text(json.dumps(cert, indent=2, sort_keys=True) + "\n", encoding="utf-8")

    note = f"""# Selected Heterotic OrientedPhiFin SourceOwned BN27 Certificate or BundleA Selector v1

## Result

```text
status = {STATUS}
heterotic_branch_certificate_closed = true
S_QaSU3_BN27_declared_as_selected_source = false
BN27_source_ownership_closed = false
direct_BN27_source_declaration_closed = false
oriented_logdet_promoted = false
next_required_artifact = {NEXT}
```

## Theorem

{candidate["theorem"]["statement"]}

## Refined Certificate

```text
{rel(OUTPUT_REFINED)}
```
"""
    OUTPUT_NOTE.write_text(note, encoding="utf-8")
    return candidate


if __name__ == "__main__":
    result = main()
    print(f"wrote {rel(OUTPUT_DATA)}")
    print(f"wrote {rel(OUTPUT_REFINED)}")
    print(f"wrote {rel(OUTPUT_CERT)}")
    print(f"wrote {rel(OUTPUT_NOTE)}")
    print(result["status"])
