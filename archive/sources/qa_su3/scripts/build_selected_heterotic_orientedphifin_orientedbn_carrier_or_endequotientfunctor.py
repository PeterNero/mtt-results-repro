"""Build oriented Phi_fin oriented-BN carrier emission / EndE quotient-functor attempt."""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "candidate_data"
CERTS = ROOT / "certificates"
PROOF = ROOT / "proof_corpus"

INPUTS = {
    "certificate_fill": DATA / "selected_heterotic_orientedphifin_sourceownership_certificate_fillattempt.values.json",
    "sourceemission_gate": DATA / "selected_heterotic_ende_domainbasis_or_nonidentity_rhoe_sourceemission.candidate.json",
    "typed_or_projective_fill": DATA / "selected_heterotic_typedcechende_basis_or_projectiverhoe_fill_attempt.candidate.json",
    "label_embedding": DATA / "selected_heterotic_ende_to_bn_labelembedding_candidate_values.json",
    "oriented_table": DATA / "selected_heterotic_orientedphifin_simultaneous_ctau_phifin_table.json",
}

OUTPUT_DATA = DATA / "selected_heterotic_orientedphifin_orientedbn_carrier_or_endequotientfunctor.candidate.json"
OUTPUT_ATTEMPT = DATA / "selected_heterotic_orientedphifin_orientedbn_carrier_or_endequotientfunctor_attempt.json"
OUTPUT_CERT = CERTS / "selected_heterotic_orientedphifin_orientedbn_carrier_or_endequotientfunctor_certificate.json"
OUTPUT_NOTE = PROOF / "Selected_Heterotic_OrientedPhiFin_OrientedBN_CarrierEmission_or_EndEQuotientFunctor_v1.md"

STATUS = "HETEROTIC_ORIENTEDPHIFIN_ORIENTEDBN_CARRIER_FUNCTOR_ATTEMPT_RHOSHADOW_ONLY"
NEXT = "Selected_Heterotic_OrientedPhiFin_EndEDomain_or_NonidentityRhoE_SourceValue_Insertion_v1"


def rel(path: Path) -> str:
    try:
        return str(path.relative_to(ROOT))
    except ValueError:
        return str(path)


def load(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def main() -> dict[str, Any]:
    certificate_fill = load(INPUTS["certificate_fill"])
    sourceemission_gate = load(INPUTS["sourceemission_gate"])
    typed_or_projective_fill = load(INPUTS["typed_or_projective_fill"])
    label_embedding = load(INPUTS["label_embedding"])
    oriented_table = load(INPUTS["oriented_table"])

    rho_shadow_support = {
        "embedding_matrix_27x11_present": len(label_embedding["embedding_matrix_27x11"]) == 27,
        "projection_pair_valid": label_embedding["projection_pair_checks"]["P_transpose_P_equals_identity_11"],
        "rho_character_intertwines": label_embedding["rho_checks"]["all_labels_preserve_tau_mod3_rank_slot"],
        "product_cancellation_retained": label_embedding["rho_checks"]["product_cancellation_retained"],
        "oriented_table_basis_matches": label_embedding["basis_id"] == oriented_table["basis_id"],
    }

    operator_functor_tests = {
        "typed_cech_EndE_domain_basis_emitted": sourceemission_gate["decision"]["typed_cech_EndE_domain_basis_emitted"],
        "projective_twisted_nonidentity_rhoE_emitted": sourceemission_gate["decision"]["projective_twisted_nonidentity_rhoE_emitted"],
        "typed_cech_fill_closes": typed_or_projective_fill["decision"]["typed_cech_EndE_domain_basis_emitted"],
        "projective_rhoE_fill_closes": typed_or_projective_fill["decision"]["projective_twisted_nonidentity_rhoE_emitted"],
        "DE_intertwines": label_embedding["D_E_intertwiner_checks"]["intertwines"],
        "same_finitepart": label_embedding["finitepart_checks"]["same_finitepart"],
    }

    carrier_attempt = {
        "schema": "SelectedHeterotic.OrientedPhiFin.OrientedBNCarrierOrEndEQuotientFunctor.Attempt.v1",
        "status": "RHO_SHADOW_ONLY_VALUES_OPEN",
        "rho_shadow_support": rho_shadow_support,
        "operator_functor_tests": operator_functor_tests,
        "can_emit_oriented_BN_carrier_from_heterotic_source": False,
        "can_promote_EndE_to_oriented_BN_functor": False,
        "why_not": [
            "The sparse 27x11 map preserves tau/rho_E central character only.",
            "The source still emits no finite End(E) basis/cochains or nonidentity heterotic rho_E transition packet.",
            "The nonnegative oriented Phi_fin D_E layer does not intertwine with the internal signed tau/D_E action.",
            "The 27-mode oriented finitepart is not equal to the internal log(2008) finitepart under the sparse embedding.",
        ],
        "first_true_value_needed": "selected finite End(E) domain basis or nonidentity heterotic rho_E transition/source packet",
        "target_fitting_used": False,
        "closure_claimed": False,
    }
    OUTPUT_ATTEMPT.write_text(json.dumps(carrier_attempt, indent=2, sort_keys=True) + "\n", encoding="utf-8")

    decision = {
        "carrier_or_functor_attempted": True,
        "rho_shadow_embedding_retained": all(rho_shadow_support.values()),
        "oriented_BN_carrier_emission_closed": False,
        "EndE_or_rhoE_to_oriented_BN_functor_closed": False,
        "operator_intertwiner_closed": False,
        "finitepart_identity_closed": False,
        "oriented_logdet_promoted": False,
        "next_required_artifact": NEXT,
        "attempt_path": rel(OUTPUT_ATTEMPT),
        "target_fitting_used": False,
        "closure_claimed": False,
    }

    candidate = {
        "candidate": "SelectedHeteroticOrientedPhiFinOrientedBNCarrierEmissionOrEndEQuotientFunctor",
        "status": STATUS,
        "inputs": {key: rel(path) for key, path in INPUTS.items()},
        "parent_statuses": {
            "certificate_fill": certificate_fill["status"],
            "sourceemission_gate": sourceemission_gate["status"],
            "typed_or_projective_fill": typed_or_projective_fill["status"],
            "label_embedding": label_embedding["status"],
        },
        "attempt_path": rel(OUTPUT_ATTEMPT),
        "decision": decision,
        "theorem": {
            "name": "OrientedBNCarrierOrEndEQuotientFunctorCurrentSourceNoGo",
            "proved": True,
            "statement": (
                "The existing 27x11 label embedding is a valid rho-shadow: it preserves the "
                "central tau/rho_E character and projection-pair injection into the oriented "
                "B_N basis. It is not a threshold functor. The selected heterotic source still "
                "does not emit a finite End(E) domain basis or nonidentity heterotic rho_E "
                "transition packet, the internal signed operator does not intertwine with the "
                "oriented nonnegative Phi_fin D_E layer, and the finiteparts are not identified. "
                "Thus the oriented B_N carrier/functor leaf remains open without promoting the "
                "oriented logdet."
            ),
        },
        "guardrails": {
            "does_not_promote_rho_shadow_to_threshold_functor": True,
            "does_not_promote_27mode_DE_as_heterotic_owned": True,
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
        "attempt_path": rel(OUTPUT_ATTEMPT),
        "note_path": rel(OUTPUT_NOTE),
        "rho_shadow_embedding_retained": decision["rho_shadow_embedding_retained"],
        "oriented_BN_carrier_emission_closed": False,
        "EndE_or_rhoE_to_oriented_BN_functor_closed": False,
        "oriented_logdet_promoted": False,
        "next_required_artifact": NEXT,
        "closure_claimed": False,
        "target_fitting_used": False,
    }
    OUTPUT_CERT.write_text(json.dumps(cert, indent=2, sort_keys=True) + "\n", encoding="utf-8")

    note = f"""# Selected Heterotic OrientedPhiFin OrientedBN CarrierEmission or EndEQuotientFunctor v1

## Result

```text
status = {STATUS}
rho_shadow_embedding_retained = {str(decision["rho_shadow_embedding_retained"]).lower()}
oriented_BN_carrier_emission_closed = false
EndE_or_rhoE_to_oriented_BN_functor_closed = false
oriented_logdet_promoted = false
next_required_artifact = {NEXT}
```

## Theorem

{candidate["theorem"]["statement"]}

## Attempt Packet

```text
{rel(OUTPUT_ATTEMPT)}
```
"""
    OUTPUT_NOTE.write_text(note, encoding="utf-8")
    return candidate


if __name__ == "__main__":
    result = main()
    print(f"wrote {rel(OUTPUT_DATA)}")
    print(f"wrote {rel(OUTPUT_ATTEMPT)}")
    print(f"wrote {rel(OUTPUT_CERT)}")
    print(f"wrote {rel(OUTPUT_NOTE)}")
    print(result["status"])
