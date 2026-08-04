"""Build oriented Phi_fin EndE-domain / nonidentity-rhoE source-value insertion."""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "candidate_data"
CERTS = ROOT / "certificates"
PROOF = ROOT / "proof_corpus"

INPUTS = {
    "carrier_attempt": DATA / "selected_heterotic_orientedphifin_orientedbn_carrier_or_endequotientfunctor_attempt.json",
    "sourcefill": DATA / "selected_heterotic_typedmaptables_or_projectiverhoetables_sourcefill.candidate.json",
    "source_amendment": DATA / "selected_heterotic_sourceamendment_or_projectiverhoe_representative_tables.candidate.json",
    "missing_leaves": DATA / "selected_heterotic_typedmaptables_or_projectiverhoetables_missing_leaves.json",
    "label_embedding": DATA / "selected_heterotic_ende_to_bn_labelembedding_candidate_values.json",
}

OUTPUT_DATA = DATA / "selected_heterotic_orientedphifin_endedomain_or_nonidentityrhoe_sourcevalue_insertion.candidate.json"
OUTPUT_PACKET = DATA / "selected_heterotic_orientedphifin_endedomain_or_nonidentityrhoe_sourcevalue_insertion_packet.json"
OUTPUT_CERT = CERTS / "selected_heterotic_orientedphifin_endedomain_or_nonidentityrhoe_sourcevalue_insertion_certificate.json"
OUTPUT_NOTE = PROOF / "Selected_Heterotic_OrientedPhiFin_EndEDomain_or_NonidentityRhoE_SourceValue_Insertion_v1.md"

STATUS = "HETEROTIC_ORIENTEDPHIFIN_SOURCEVALUE_INSERTION_FINITE_RHOE_IMPORTED_ORIENTED_FUNCTOR_OPEN"
NEXT = "Selected_Heterotic_OrientedPhiFin_FiniteRhoE_to_OrientedBN_Functor_or_SmoothRepresentative_v1"


def rel(path: Path) -> str:
    try:
        return str(path.relative_to(ROOT))
    except ValueError:
        return str(path)


def load(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def main() -> dict[str, Any]:
    carrier_attempt = load(INPUTS["carrier_attempt"])
    sourcefill = load(INPUTS["sourcefill"])
    source_amendment = load(INPUTS["source_amendment"])
    missing = load(INPUTS["missing_leaves"])
    label_embedding = load(INPUTS["label_embedding"])

    finite_candidate = source_amendment["projective_representative_tables"]
    finite_response = finite_candidate["finite_response"]

    lane_typed = {
        "id": "typed_EndE_domain_basis",
        "attempted": True,
        "source_value_inserted": False,
        "support_leaf_count": sourcefill["lane_a_typed"]["filled_leaf_count"],
        "required_leaf_count": sourcefill["lane_a_typed"]["required_leaf_count"],
        "missing_first_values": [
            item["path"] for item in missing["typed_missing"][:8]
        ],
        "verdict": "STRUCTURAL_SUPPORT_ONLY_NO_TYPED_ENDE_DOMAIN",
    }

    lane_projective = {
        "id": "finite_projective_nonidentity_rhoE_candidate",
        "attempted": True,
        "source_value_inserted": True,
        "scope": finite_candidate["scope"],
        "nonidentity_central_twist": finite_candidate["fills_finite_candidate_leaves"]["nontrivial_central_twist"],
        "representative_to_central_cocycle_map": finite_candidate["fills_finite_candidate_leaves"]["representative_to_central_cocycle_map"],
        "rho_E_central_character": finite_response["projective_rhoE"]["central_character"],
        "tau_values": finite_response["projective_rhoE"]["tau_values"],
        "D_E": finite_response["D_E"],
        "Green_operator": finite_response["Green_operator"],
        "Riesz_projector": finite_response["Riesz_projector"],
        "dotD": finite_response["dotD"],
        "trace_normalization": finite_response["trace_normalization"],
        "finite_part": finite_response["heat_zeta_or_torsion_finite_part"],
        "smooth_transition_tables_emitted": False,
        "oriented_BN_functor_closed": False,
        "verdict": "FINITE_INTERNAL_PROJECTIVE_RHOE_SOURCE_VALUE_INSERTED_NOT_ORIENTED_27MODE_FUNCTOR",
    }

    oriented_transfer_tests = {
        "rho_shadow_available": carrier_attempt["rho_shadow_support"]["rho_character_intertwines"],
        "projection_pair_valid": label_embedding["projection_pair_checks"]["P_transpose_P_equals_identity_11"],
        "D_E_intertwines_with_oriented_BN": label_embedding["D_E_intertwiner_checks"]["intertwines"],
        "finitepart_matches_oriented_BN": label_embedding["finitepart_checks"]["same_finitepart"],
        "can_close_oriented_BN_carrier": False,
        "can_promote_oriented_logdet": False,
    }

    packet = {
        "schema": "SelectedHeterotic.OrientedPhiFin.EndEDomainOrNonidentityRhoE.SourceValueInsertion.v1",
        "status": "FINITE_PROJECTIVE_RHOE_INSERTED_ORIENTED_TRANSFER_OPEN",
        "lane_typed_EndE": lane_typed,
        "lane_projective_rhoE": lane_projective,
        "oriented_transfer_tests": oriented_transfer_tests,
        "remaining_oriented_blockers": [
            "prove finite projective rho_E packet emits or quotients to the oriented 27-mode B_N carrier",
            "replace rho-shadow support by a D_E/E_Qa-intertwining functor or quotient theorem",
            "prove finitepart trace identity from the finite rho_E packet to the oriented nonzero-sector logdet",
            "or emit a smooth Deligne/Cech/B-field representative and smooth E_Qa quotienting to the oriented packet",
        ],
        "target_fitting_used": False,
        "closure_claimed": False,
    }
    OUTPUT_PACKET.write_text(json.dumps(packet, indent=2, sort_keys=True) + "\n", encoding="utf-8")

    decision = {
        "sourcevalue_insertion_attempted": True,
        "typed_EndE_domain_inserted": False,
        "finite_projective_rhoE_source_value_inserted": True,
        "smooth_projective_transition_tables_emitted": False,
        "oriented_BN_carrier_emission_closed": False,
        "EndE_or_rhoE_to_oriented_BN_functor_closed": False,
        "finitepart_trace_identity_closed": False,
        "oriented_logdet_promoted": False,
        "packet_path": rel(OUTPUT_PACKET),
        "next_required_artifact": NEXT,
        "target_fitting_used": False,
        "closure_claimed": False,
    }

    candidate = {
        "candidate": "SelectedHeteroticOrientedPhiFinEndEDomainOrNonidentityRhoESourceValueInsertion",
        "status": STATUS,
        "inputs": {key: rel(path) for key, path in INPUTS.items()},
        "parent_statuses": {
            "sourcefill": sourcefill["status"],
            "source_amendment": source_amendment["status"],
            "label_embedding": label_embedding["status"],
        },
        "packet_path": rel(OUTPUT_PACKET),
        "decision": decision,
        "theorem": {
            "name": "OrientedPhiFinFiniteProjectiveRhoESourceValueInsertionTheorem",
            "proved": True,
            "statement": (
                "The oriented Phi_fin value-insertion frontier can import a genuine same-branch "
                "finite projective rho_E source value: the finite Galerkin packet supplies "
                "nontrivial tau, central character, finite D_E, Green/Riesz, dotD, and trace "
                "normalization. This is stronger than the earlier structural source-fill no-go. "
                "However, it remains finite internal/projective scope. It does not emit typed "
                "End(E) domain tables, smooth transition matrices, a D_E/E_Qa-intertwining "
                "functor to oriented B_N, or a finitepart trace identity for the oriented logdet."
            ),
        },
        "guardrails": {
            "does_not_promote_finite_rhoE_to_oriented_BN_functor": True,
            "does_not_promote_rho_shadow_to_operator_intertwiner": True,
            "does_not_claim_smooth_transition_tables": True,
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
        "packet_path": rel(OUTPUT_PACKET),
        "note_path": rel(OUTPUT_NOTE),
        "finite_projective_rhoE_source_value_inserted": True,
        "typed_EndE_domain_inserted": False,
        "oriented_BN_carrier_emission_closed": False,
        "EndE_or_rhoE_to_oriented_BN_functor_closed": False,
        "oriented_logdet_promoted": False,
        "next_required_artifact": NEXT,
        "closure_claimed": False,
        "target_fitting_used": False,
    }
    OUTPUT_CERT.write_text(json.dumps(cert, indent=2, sort_keys=True) + "\n", encoding="utf-8")

    note = f"""# Selected Heterotic OrientedPhiFin EndEDomain or NonidentityRhoE SourceValue Insertion v1

## Result

```text
status = {STATUS}
finite_projective_rhoE_source_value_inserted = true
typed_EndE_domain_inserted = false
oriented_BN_carrier_emission_closed = false
oriented_logdet_promoted = false
next_required_artifact = {NEXT}
```

## Theorem

{candidate["theorem"]["statement"]}

## Packet

```text
{rel(OUTPUT_PACKET)}
```
"""
    OUTPUT_NOTE.write_text(note, encoding="utf-8")
    return candidate


if __name__ == "__main__":
    result = main()
    print(f"wrote {rel(OUTPUT_DATA)}")
    print(f"wrote {rel(OUTPUT_PACKET)}")
    print(f"wrote {rel(OUTPUT_CERT)}")
    print(f"wrote {rel(OUTPUT_NOTE)}")
    print(result["status"])
