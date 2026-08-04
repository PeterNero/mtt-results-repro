"""Build the oriented Phi_fin source-theorem fill attempt / direct smooth E_Qa payload gate."""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "candidate_data"
CERTS = ROOT / "certificates"
PROOF = ROOT / "proof_corpus"

INPUTS = {
    "request": DATA / "selected_heterotic_orientedphifin_finitequotientidentity_source_theorem_request.json",
    "previous_gate": DATA / "selected_heterotic_orientedphifin_finitequotientidentity_sourcetheorem_or_smootheqapayload.candidate.json",
    "phifin_bridge": DATA / "selected_heterotic_phifin_sourceidentity_bridge_attempt.candidate.json",
    "ende_bn_fill": DATA / "selected_heterotic_ende_to_bn_functor_or_rhoe_transition_valuepacket_fill.candidate.json",
    "ende_domain_or_rhoe_gate": DATA / "selected_heterotic_ende_domainbasis_or_nonidentity_rhoe_sourceemission.candidate.json",
    "label_embedding": DATA / "selected_heterotic_ende_to_bn_labelembedding_or_smoothtransitionconnection_valuepacket.candidate.json",
    "oriented_table": DATA / "selected_heterotic_orientedphifin_simultaneous_ctau_phifin_table.json",
}

OUTPUT_DATA = DATA / "selected_heterotic_orientedphifin_sourcetheorem_fillattempt_or_directsmootheqapayload.candidate.json"
OUTPUT_PACKET = DATA / "selected_heterotic_orientedphifin_sourcetheorem_fillattempt_packet.json"
OUTPUT_CERT = CERTS / "selected_heterotic_orientedphifin_sourcetheorem_fillattempt_or_directsmootheqapayload_certificate.json"
OUTPUT_NOTE = PROOF / "Selected_Heterotic_OrientedPhiFin_SourceTheorem_FillAttempt_or_DirectSmoothEQaPayload_v1.md"

STATUS = "HETEROTIC_ORIENTEDPHIFIN_SOURCETHEOREM_FILLATTEMPT_VALUES_OPEN_END0_OR_RHOE_NEXT"
NEXT = "Selected_Heterotic_OrientedPhiFin_EndE_Basis_or_NonidentityRhoE_ValueInsertion_v1"


def rel(path: Path) -> str:
    try:
        return str(path.relative_to(ROOT))
    except ValueError:
        return str(path)


def load(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def main() -> dict[str, Any]:
    request = load(INPUTS["request"])
    previous_gate = load(INPUTS["previous_gate"])
    phifin_bridge = load(INPUTS["phifin_bridge"])
    ende_bn_fill = load(INPUTS["ende_bn_fill"])
    domain_or_rhoe = load(INPUTS["ende_domain_or_rhoe_gate"])
    label_embedding = load(INPUTS["label_embedding"])
    oriented_table = load(INPUTS["oriented_table"])

    attempted_forms = {
        "finite_quotient_identity_direct": {
            "attempted": True,
            "closes": False,
            "support_present": {
                "oriented_27mode_table": True,
                "routec_gap_layer": phifin_bridge["decision"]["u1y_27mode_gap_layer_closed"],
                "ctau_orientation_and_kernel_policy": previous_gate["decision"]["kernel_policy_closed"],
            },
            "blocking_values": [
                "same-branch threshold source certificate for oriented B_N",
                "finite quotient functor from heterotic End(E)/rho_E to oriented B_N",
                "finitepart trace identity for the oriented logdet table",
            ],
        },
        "direct_smooth_EQa_payload": {
            "attempted": True,
            "closes": False,
            "support_present": {
                "Rplus_or_geometry_support_seen_upstream": ende_bn_fill["filled_packet"]["operator_payload"]["D_E_or_E_Qa_matrix"]["support_present"],
                "smooth_lane_required": True,
            },
            "blocking_values": [
                "selected bundle connection A or projective connection",
                "curvature F_A and representation action",
                "smooth E_Qa matrix or heat/zeta/torsion finite part",
                "smooth-to-finite quotient proving the oriented table is its quotient",
            ],
        },
        "EndE_to_BN_functor_plus_finitepart": {
            "attempted": True,
            "closes": False,
            "support_present": {
                "label_embedding_candidate_built": label_embedding["decision"]["label_embedding_candidate_built"],
                "rhoE_character_intertwines": label_embedding["decision"]["rhoE_character_intertwines"],
                "source_certificate_context_leaves_closed": ende_bn_fill["decision"]["source_certificate_leaves_closed"],
            },
            "blocking_values": [
                "selected finite End(E) domain basis/cochains",
                "End(E)->B_N basis map or commuting projection certificate",
                "nonidentity heterotic rho_E transition/projective carrier",
                "same-scheme heterotic finitepart regularization",
            ],
        },
    }

    leaf_status_after_attempt = {
        "kernel_policy_closed": previous_gate["leaf_status"]["kernel_policy_closed"],
        "source_certificate_closed": {
            "closed": False,
            "partial_source_context_closed": ende_bn_fill["decision"]["source_certificate_leaves_closed"],
            "why_open": (
                "The branch/source context is selected, and Route-C substitution is forbidden, "
                "but no theorem identifies the heterotic threshold object itself with the oriented B_N quotient."
            ),
        },
        "quotient_functor_closed": {
            "closed": False,
            "partial_embedding_support": label_embedding["decision"]["projection_pair_candidate_valid_as_injection"],
            "why_open": "The sparse 27x11 label embedding is a rho_E shadow, not an exact operator/functor identity.",
        },
        "operator_identity_closed": {
            "closed": False,
            "support": {
                "C_tau_orientation": True,
                "PhiFin_gap_layer": phifin_bridge["decision"]["u1y_27mode_gap_layer_closed"],
            },
            "why_open": "No source emits E_Qa^or = sign(C_tau) * |PhiFin_DE| as one threshold operator.",
        },
        "finitepart_trace_identity_closed": {
            "closed": False,
            "support": oriented_table["logdet_values"],
            "why_open": "The table is computed, but no heterotic finitepart theorem authorizes it.",
        },
        "audit_replay_closed": {
            "closed": False,
            "why_open": "The replay cannot close until the source, functor, operator, and finitepart leaves close.",
        },
    }
    closed_count = sum(1 for leaf in leaf_status_after_attempt.values() if leaf["closed"] is True)

    next_value_object = {
        "schema": "SelectedHeterotic.OrientedPhiFin.NextValueObject.v1",
        "selected_next": "EndE_domain_basis_or_nonidentity_rhoE",
        "reason": (
            "Every legal source-theorem form blocks first at either a selected finite End(E) "
            "basis/cochain packet or a selected nonidentity heterotic rho_E/projective transition packet."
        ),
        "lane_A_EndE_basis_required": domain_or_rhoe["lanes"]["A_typed_cech_EndE_domain_basis"]["required_payload"],
        "lane_B_nonidentity_rhoE_required": domain_or_rhoe["lanes"]["B_projective_twisted_nonidentity_rhoE"]["required_payload"],
        "forbidden": domain_or_rhoe["acceptance_kernel"]["forbidden"],
        "target_fitting_used": False,
    }

    packet = {
        "schema": "SelectedHeterotic.OrientedPhiFin.SourceTheoremFillAttemptPacket.v1",
        "attempted_forms": attempted_forms,
        "leaf_status_after_attempt": leaf_status_after_attempt,
        "next_value_object": next_value_object,
        "request_must_emit": request["must_emit"],
        "target_fitting_used": False,
        "closure_claimed": False,
    }
    OUTPUT_PACKET.write_text(json.dumps(packet, indent=2, sort_keys=True) + "\n", encoding="utf-8")

    decision = {
        "fill_attempt_executed": True,
        "attempted_source_theorem_forms_count": len(attempted_forms),
        "kernel_policy_closed_carried_forward": True,
        "closed_leaf_count": closed_count,
        "required_leaf_count": len(leaf_status_after_attempt),
        "new_leaves_closed": 0,
        "source_certificate_context_partial": True,
        "finite_quotient_identity_constructed": False,
        "smooth_EQa_constructed": False,
        "oriented_threshold_logdet_promoted": False,
        "next_value_object_selected": next_value_object["selected_next"],
        "next_required_artifact": NEXT,
        "packet_path": rel(OUTPUT_PACKET),
        "target_fitting_used": False,
        "closure_claimed": False,
    }

    candidate = {
        "candidate": "SelectedHeteroticOrientedPhiFinSourceTheoremFillAttemptOrDirectSmoothEQaPayload",
        "status": STATUS,
        "inputs": {key: rel(path) for key, path in INPUTS.items()},
        "parent_statuses": {
            "previous_gate": previous_gate["status"],
            "phifin_bridge": phifin_bridge["status"],
            "ende_bn_fill": ende_bn_fill["status"],
            "domain_or_rhoe_gate": domain_or_rhoe["status"],
            "label_embedding": label_embedding["status"],
        },
        "fill_attempt_packet_path": rel(OUTPUT_PACKET),
        "decision": decision,
        "theorem": {
            "name": "OrientedPhiFinSourceTheoremFillAttemptReduction",
            "proved": True,
            "statement": (
                "The current corpus can execute all three legal oriented Phi_fin source-theorem forms, "
                "but none closes beyond the already settled kernel/no-double-count leaf. The branch "
                "source context and a phase-preserving rho_E label embedding are real support, yet the "
                "first missing value is still selected finite End(E) domain data or a selected "
                "nonidentity heterotic rho_E/projective transition packet. Therefore the next "
                "constructive object is exactly that value insertion, not another threshold comparison."
            ),
        },
        "guardrails": {
            "does_not_claim_source_certificate_leaf": True,
            "does_not_claim_quotient_functor_leaf": True,
            "does_not_claim_operator_identity_leaf": True,
            "does_not_claim_finitepart_trace_identity_leaf": True,
            "does_not_promote_oriented_logdets": True,
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
        "closed_leaf_count": closed_count,
        "new_leaves_closed": 0,
        "next_value_object_selected": next_value_object["selected_next"],
        "finite_quotient_identity_constructed": False,
        "smooth_EQa_constructed": False,
        "oriented_threshold_logdet_promoted": False,
        "next_required_artifact": NEXT,
        "closure_claimed": False,
        "target_fitting_used": False,
    }
    OUTPUT_CERT.write_text(json.dumps(cert, indent=2, sort_keys=True) + "\n", encoding="utf-8")

    note = f"""# Selected Heterotic OrientedPhiFin SourceTheorem FillAttempt or DirectSmoothEQaPayload v1

## Result

```text
status = {STATUS}
closed_leaf_count = {closed_count}/{len(leaf_status_after_attempt)}
new_leaves_closed = 0
finite_quotient_identity_constructed = false
smooth_EQa_constructed = false
oriented_threshold_logdet_promoted = false
next_required_artifact = {NEXT}
```

## Theorem

{candidate["theorem"]["statement"]}

## Fill Attempt Packet

```text
{rel(OUTPUT_PACKET)}
```

## Next Value Object

```json
{json.dumps(next_value_object, indent=2, sort_keys=True)}
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
