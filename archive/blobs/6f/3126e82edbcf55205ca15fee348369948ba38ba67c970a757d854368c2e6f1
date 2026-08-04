"""Build oriented Phi_fin source-ownership certificate fill attempt."""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "candidate_data"
CERTS = ROOT / "certificates"
PROOF = ROOT / "proof_corpus"

INPUTS = {
    "request": DATA / "selected_heterotic_orientedphifin_sourceownership_minimal_certificate_request.json",
    "sourceownership_gate": DATA / "selected_heterotic_orientedphifin_sourceownership_or_smootheqa_quotient.candidate.json",
    "ende_bn_fill": DATA / "selected_heterotic_ende_to_bn_functor_or_rhoe_transition_valuepacket_fill.candidate.json",
    "label_embedding_values": DATA / "selected_heterotic_ende_to_bn_labelembedding_candidate_values.json",
    "direct_fill_packet": DATA / "selected_heterotic_orientedphifin_directfiniteresponse_fillattempt_packet.json",
}

OUTPUT_DATA = DATA / "selected_heterotic_orientedphifin_sourceownership_certificate_fillattempt.candidate.json"
OUTPUT_FILLED = DATA / "selected_heterotic_orientedphifin_sourceownership_certificate_fillattempt.values.json"
OUTPUT_CERT = CERTS / "selected_heterotic_orientedphifin_sourceownership_certificate_fillattempt_certificate.json"
OUTPUT_NOTE = PROOF / "Selected_Heterotic_OrientedPhiFin_SourceOwnership_Certificate_FillAttempt_v1.md"

STATUS = "HETEROTIC_ORIENTEDPHIFIN_SOURCEOWNERSHIP_CERTIFICATE_FILL_PARTIAL_BRANCHCERT_ONLY"
NEXT = "Selected_Heterotic_OrientedPhiFin_OrientedBN_CarrierEmission_or_EndEQuotientFunctor_v1"


def rel(path: Path) -> str:
    try:
        return str(path.relative_to(ROOT))
    except ValueError:
        return str(path)


def load(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def main() -> dict[str, Any]:
    request = load(INPUTS["request"])
    sourceownership_gate = load(INPUTS["sourceownership_gate"])
    ende_bn_fill = load(INPUTS["ende_bn_fill"])
    label_embedding = load(INPUTS["label_embedding_values"])
    direct_packet = load(INPUTS["direct_fill_packet"])

    source_certificate = ende_bn_fill["filled_packet"]["source_certificate"]
    same_branch_cert_closed = (
        ende_bn_fill["decision"]["source_certificate_leaves_closed"]
        and source_certificate["selected_branch_id"]["same_branch_selected"]
        and source_certificate["selected_branch_id"]["source_emitted"]
        and source_certificate["no_imported_routec_substitution"]["value"] is True
    )

    filled = {
        "schema": "SelectedHeterotic.OrientedPhiFin.SourceOwnership.CertificateFillAttempt.v1",
        "status": "PARTIAL_BRANCH_CERTIFICATE_ONLY",
        "filled_certificate_fields": {
            "same_branch_QaSU3_heterotic_source_certificate": {
                "filled": same_branch_cert_closed,
                "value": source_certificate["selected_branch_id"]["value"],
                "reason": source_certificate["selected_branch_id"]["reason"],
            },
            "oriented_BN_carrier_emitted_by_that_source": {
                "filled": False,
                "reason": "The heterotic branch is selected, but its source packet does not emit the 27-mode oriented B_N carrier.",
            },
            "quotient_or_functor_EndE_or_rhoE_to_oriented_BN": {
                "filled": False,
                "support": {
                    "rho_character_embedding_candidate": label_embedding["rho_checks"]["all_labels_preserve_tau_mod3_rank_slot"],
                    "projection_pair_valid": label_embedding["projection_pair_checks"]["P_transpose_P_equals_identity_11"],
                },
                "reason": "The sparse 27x11 embedding is a rho_E shadow only; D_E and finitepart checks do not intertwine.",
            },
            "positive_PhiFin_DE_magnitude_owned_by_source": {
                "filled": False,
                "support": "Route-C owns the selected 27-mode D_E gap layer; heterotic ownership remains unproved.",
                "reason": "No same-branch theorem transfers positive Phi_fin D_E magnitude from Route-C support to heterotic Qa/SU3 ownership.",
            },
            "C_tau_orientation_bound_to_same_threshold_complex": {
                "filled": request["required_certificate_fields"]["C_tau_orientation_bound_to_same_threshold_complex"],
                "reason": "C_tau is source-selected as signed central-rank orientation support, retained from prior theorem.",
            },
            "smooth_EQa_or_finite_threshold_complex_quotients_to_packet": {
                "filled": False,
                "reason": "No selected smooth E_Qa, bundle A/F_A, or finite threshold complex quotienting to the oriented packet is emitted.",
            },
            "finitepart_trace_identity_consumes_nonzero_oriented_sector": {
                "filled": False,
                "waiting_values": direct_packet["finitepart_candidates"],
                "reason": "The logdet candidates are computed, but no trace identity lets them be consumed as heterotic threshold finitepart.",
            },
            "kernel_zero_mode_shared_circle_policy_replayed": {
                "filled": request["required_certificate_fields"]["kernel_zero_mode_shared_circle_policy_replayed"],
                "reason": "Existing no-double-count policy is retained.",
            },
            "no_observed_data_or_residual_selector": {
                "filled": request["required_certificate_fields"]["no_observed_data_or_residual_selector"],
                "reason": "No observed constants, residuals, or target data enter the fill.",
            },
        },
        "diagnostics": {
            "label_embedding_status": label_embedding["status"],
            "rho_shadow_intertwines": label_embedding["rho_checks"]["all_labels_preserve_tau_mod3_rank_slot"],
            "DE_intertwines": label_embedding["D_E_intertwiner_checks"]["intertwines"],
            "same_finitepart": label_embedding["finitepart_checks"]["same_finitepart"],
            "first_true_value_blocker": ende_bn_fill["blockers"]["first_true_value_blocker"],
        },
        "target_fitting_used": False,
        "closure_claimed": False,
    }
    OUTPUT_FILLED.write_text(json.dumps(filled, indent=2, sort_keys=True) + "\n", encoding="utf-8")

    closed_fields = [key for key, value in filled["filled_certificate_fields"].items() if value["filled"] is True]
    open_fields = [key for key, value in filled["filled_certificate_fields"].items() if value["filled"] is False]

    decision = {
        "certificate_fill_attempted": True,
        "same_branch_source_certificate_closed": same_branch_cert_closed,
        "support_policy_fields_retained": True,
        "oriented_BN_carrier_emission_closed": False,
        "EndE_or_rhoE_to_oriented_BN_functor_closed": False,
        "positive_PhiFin_DE_source_ownership_closed": False,
        "finitepart_trace_identity_closed": False,
        "oriented_logdet_promoted": False,
        "closed_fields": closed_fields,
        "open_fields": open_fields,
        "next_required_artifact": NEXT,
        "filled_path": rel(OUTPUT_FILLED),
        "target_fitting_used": False,
        "closure_claimed": False,
    }

    candidate = {
        "candidate": "SelectedHeteroticOrientedPhiFinSourceOwnershipCertificateFillAttempt",
        "status": STATUS,
        "inputs": {key: rel(path) for key, path in INPUTS.items()},
        "parent_statuses": {
            "sourceownership_gate": sourceownership_gate["status"],
            "ende_bn_fill": ende_bn_fill["status"],
            "label_embedding": label_embedding["status"],
        },
        "filled_path": rel(OUTPUT_FILLED),
        "decision": decision,
        "theorem": {
            "name": "OrientedPhiFinSourceOwnershipCertificatePartialFillTheorem",
            "proved": True,
            "statement": (
                "The minimal source-ownership certificate can now be partially filled: the "
                "same heterotic Qa/SU3 branch certificate and no-imported-Route-C-substitution "
                "guardrail are source-emitted, and the C_tau/no-double-count support fields "
                "remain closed. However, the true value fields remain open: the source does "
                "not emit the oriented 27-mode B_N carrier, no End(E)/rho_E to oriented B_N "
                "functor or quotient is proved, positive Phi_fin D_E ownership remains "
                "Route-C-scoped support, and the finitepart trace identity is absent."
            ),
        },
        "guardrails": {
            "does_not_promote_rho_shadow_to_operator_functor": True,
            "does_not_promote_routec_DE_to_heterotic_ownership": True,
            "does_not_promote_oriented_logdet": True,
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
        "filled_path": rel(OUTPUT_FILLED),
        "note_path": rel(OUTPUT_NOTE),
        "same_branch_source_certificate_closed": same_branch_cert_closed,
        "oriented_BN_carrier_emission_closed": False,
        "EndE_or_rhoE_to_oriented_BN_functor_closed": False,
        "oriented_logdet_promoted": False,
        "next_required_artifact": NEXT,
        "closure_claimed": False,
        "target_fitting_used": False,
    }
    OUTPUT_CERT.write_text(json.dumps(cert, indent=2, sort_keys=True) + "\n", encoding="utf-8")

    note = f"""# Selected Heterotic OrientedPhiFin SourceOwnership Certificate FillAttempt v1

## Result

```text
status = {STATUS}
same_branch_source_certificate_closed = {str(same_branch_cert_closed).lower()}
oriented_BN_carrier_emission_closed = false
EndE_or_rhoE_to_oriented_BN_functor_closed = false
oriented_logdet_promoted = false
next_required_artifact = {NEXT}
```

## Theorem

{candidate["theorem"]["statement"]}

## Filled Certificate Attempt

```text
{rel(OUTPUT_FILLED)}
```
"""
    OUTPUT_NOTE.write_text(note, encoding="utf-8")
    return candidate


if __name__ == "__main__":
    result = main()
    print(f"wrote {rel(OUTPUT_DATA)}")
    print(f"wrote {rel(OUTPUT_FILLED)}")
    print(f"wrote {rel(OUTPUT_CERT)}")
    print(f"wrote {rel(OUTPUT_NOTE)}")
    print(result["status"])
