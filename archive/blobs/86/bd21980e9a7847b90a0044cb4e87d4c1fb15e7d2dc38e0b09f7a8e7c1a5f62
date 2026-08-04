"""Build the oriented Phi_fin finite-quotient identity source-theorem gate."""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "candidate_data"
CERTS = ROOT / "certificates"
PROOF = ROOT / "proof_corpus"

INPUTS = {
    "minimal_contract": DATA / "selected_heterotic_orientedphifin_minimal_finitequotientidentity_contract.json",
    "minimal_gate": DATA / "selected_heterotic_orientedphifin_minimal_leaf_fill_or_finitequotientidentity.candidate.json",
    "source_gate": DATA / "selected_heterotic_orientedphifin_sourceemission_or_smootheqa_thresholdidentity.candidate.json",
    "sourcefill_packet": DATA / "selected_heterotic_orientedphifin_thresholdidentity_sourcefill_packet.json",
    "oriented_table": DATA / "selected_heterotic_orientedphifin_simultaneous_ctau_phifin_table.json",
    "ctau_dirac": DATA / "selected_heterotic_ctau_positivefinitepart_or_smoothdiracconvention_sourcetheorem.candidate.json",
    "ctau_operator": DATA / "selected_heterotic_bn_centralrankoperator_or_smootheqa_sourceemission.candidate.json",
    "routec_trace": DATA / "selected_u1y_routec_trace_equals_27mode_or_full_hym_replay.candidate.json",
}

OUTPUT_DATA = DATA / "selected_heterotic_orientedphifin_finitequotientidentity_sourcetheorem_or_smootheqapayload.candidate.json"
OUTPUT_REQUEST = DATA / "selected_heterotic_orientedphifin_finitequotientidentity_source_theorem_request.json"
OUTPUT_CERT = CERTS / "selected_heterotic_orientedphifin_finitequotientidentity_sourcetheorem_or_smootheqapayload_certificate.json"
OUTPUT_NOTE = PROOF / "Selected_Heterotic_OrientedPhiFin_FiniteQuotientIdentity_SourceTheorem_or_SmoothEQaPayload_v1.md"

STATUS = "HETEROTIC_ORIENTEDPHIFIN_FINITEQUOTIENT_SOURCE_THEOREM_REQUEST_BUILT_KERNEL_POLICY_CLOSED"
NEXT = "Selected_Heterotic_OrientedPhiFin_SourceTheorem_FillAttempt_or_DirectSmoothEQaPayload_v1"


def rel(path: Path) -> str:
    try:
        return str(path.relative_to(ROOT))
    except ValueError:
        return str(path)


def load(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def main() -> dict[str, Any]:
    contract = load(INPUTS["minimal_contract"])
    minimal_gate = load(INPUTS["minimal_gate"])
    source_gate = load(INPUTS["source_gate"])
    fill_packet = load(INPUTS["sourcefill_packet"])
    oriented_table = load(INPUTS["oriented_table"])
    ctau_dirac = load(INPUTS["ctau_dirac"])
    ctau_operator = load(INPUTS["ctau_operator"])
    routec_trace = load(INPUTS["routec_trace"])

    leaf_status = {
        "source_certificate_closed": {
            "closed": False,
            "support": {
                "ctau_source_selected_as_BN_operator": ctau_operator["decision"]["C_tau_source_selected_as_BN_operator"],
                "routec_27mode_DE_gap_layer_closed": routec_trace["decision"]["DE_gap_Riesz_Green_layer_closed"],
                "oriented_table_built": source_gate["closed_support"]["oriented_table_built"],
            },
            "missing": "same-branch theorem that the heterotic Qa/SU3 threshold object is exactly the oriented 27-mode B_N quotient",
        },
        "quotient_functor_closed": {
            "closed": False,
            "support": {
                "selected_internal_packet_reused": fill_packet["source_certificate"]["finite_internal_projective_packet_selected"],
                "same_BN_domain": source_gate["closed_support"]["same_BN_domain"],
            },
            "missing": "exact functor from selected internal rho_E packet / End(E) labels to the oriented B_N threshold complex, not merely an embedding",
        },
        "operator_identity_closed": {
            "closed": False,
            "support": {
                "ctau_orientation_operator_closed": ctau_dirac["decision"]["ctau_supplies_orientation"],
                "phifin_positive_gap_layer_available": ctau_dirac["decision"]["phifin_positive_gap_layer_available"],
                "same_domain_commutation_table_complete": source_gate["decision"]["same_domain_commutation_table_complete"],
            },
            "missing": "source-emitted product/threshold identity E_Qa^or = sign(C_tau) * |PhiFin_DE|",
        },
        "finitepart_trace_identity_closed": {
            "closed": False,
            "support": {
                "oriented_logdet_values": oriented_table["logdet_values"],
                "finite_positive_policy_available": source_gate["closed_support"]["finite_positive_policy_available"],
            },
            "missing": "source permission to use the oriented table logdet values as heterotic threshold finite part",
        },
        "kernel_policy_closed": {
            "closed": True,
            "support": {
                "kernel_policy_algebraic": source_gate["closed_support"]["kernel_policy_algebraic"],
                "no_double_counting_algebraic": source_gate["closed_support"]["no_double_counting_algebraic"],
                "PhiFin_kernel_count": oriented_table["counts"]["PhiFin_kernel_count"],
                "C_tau_kernel_count": oriented_table["counts"]["C_tau_spectrum"]["0"],
                "shared_circle_policy": "kernel/projector subtraction is algebraic only; no GR/protospinor smooth surface is counted in the internal threshold",
            },
            "closed_scope": "finite B_N algebraic kernel, zero-mode, and no-double-count policy only",
        },
        "audit_replay_closed": {
            "closed": False,
            "support": {
                "oriented_table_replayed": fill_packet["audit_replay"]["oriented_table_replayed"],
                "target_fitting_used": False,
            },
            "missing": "identity theorem replay cannot close until source_certificate, quotient_functor, operator_identity, and finitepart_trace_identity close",
        },
    }
    closed_count = sum(1 for leaf in leaf_status.values() if leaf["closed"] is True)

    request = {
        "schema": "SelectedHeterotic.OrientedPhiFin.FiniteQuotientIdentity.SourceTheoremRequest.v1",
        "status": "SOURCE_THEOREM_REQUIRED",
        "already_closed": ["kernel_policy_closed"],
        "must_emit": {
            "source_certificate": leaf_status["source_certificate_closed"]["missing"],
            "quotient_functor": leaf_status["quotient_functor_closed"]["missing"],
            "operator_identity": leaf_status["operator_identity_closed"]["missing"],
            "finitepart_trace_identity": leaf_status["finitepart_trace_identity_closed"]["missing"],
            "audit_replay": leaf_status["audit_replay_closed"]["missing"],
        },
        "allowed_source_theorem_forms": [
            "finite quotient identity theorem selecting the oriented 27-mode B_N threshold complex directly",
            "direct smooth E_Qa payload whose finite quotient is the oriented table",
            "End(E)->B_N functor plus determinant finitepart theorem proving the oriented table is the selected threshold quotient",
        ],
        "forbidden_shortcuts": contract["must_not_use"]
        + [
            "treating Route-C D_E gap closure as full heterotic Phi_fin closure",
            "multiplying C_tau and Phi_fin as an operator identity without source emission",
            "using the kernel policy leaf as a threshold magnitude theorem",
        ],
        "target_fitting_used": False,
        "closure_claimed": False,
    }
    OUTPUT_REQUEST.write_text(json.dumps(request, indent=2, sort_keys=True) + "\n", encoding="utf-8")

    decision = {
        "source_theorem_request_built": True,
        "finite_quotient_identity_constructed": False,
        "smooth_EQa_constructed": False,
        "kernel_policy_closed": True,
        "closed_leaf_count": closed_count,
        "required_leaf_count": len(leaf_status),
        "remaining_open_leaf_count": len(leaf_status) - closed_count,
        "heterotic_threshold_magnitude_promoted": False,
        "current_source_nogo": True,
        "mathematical_impossibility_claimed": False,
        "next_required_artifact": NEXT,
        "request_path": rel(OUTPUT_REQUEST),
        "target_fitting_used": False,
        "closure_claimed": False,
    }

    candidate = {
        "candidate": "SelectedHeteroticOrientedPhiFinFiniteQuotientIdentitySourceTheoremOrSmoothEQaPayload",
        "status": STATUS,
        "inputs": {key: rel(path) for key, path in INPUTS.items()},
        "parent_statuses": {
            "minimal_gate": minimal_gate["status"],
            "source_gate": source_gate["status"],
            "ctau_dirac": ctau_dirac["status"],
            "ctau_operator": ctau_operator["status"],
            "routec_trace": routec_trace["status"],
        },
        "leaf_status": leaf_status,
        "request_path": rel(OUTPUT_REQUEST),
        "decision": decision,
        "theorem": {
            "name": "OrientedPhiFinFiniteQuotientIdentityKernelPolicyLeafTheorem",
            "proved": True,
            "statement": (
                "The oriented Phi_fin finite-quotient identity gate closes exactly one "
                "minimal leaf with current sources: the finite B_N kernel, zero-mode, "
                "and no-double-count policy. The signed C_tau source and Route-C "
                "Phi_fin gap layer give strong support for the remaining leaves, but "
                "they do not by themselves emit the heterotic threshold source "
                "certificate, quotient functor, product operator identity, or "
                "finitepart trace identity. Therefore a source theorem is still "
                "required before the oriented logdet values can be promoted."
            ),
        },
        "guardrails": {
            "does_not_claim_finite_quotient_identity": True,
            "does_not_claim_smooth_EQa": True,
            "does_not_promote_oriented_values": True,
            "does_not_promote_routec_gap_to_heterotic_threshold": True,
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
        "request_path": rel(OUTPUT_REQUEST),
        "note_path": rel(OUTPUT_NOTE),
        "kernel_policy_closed": True,
        "closed_leaf_count": closed_count,
        "finite_quotient_identity_constructed": False,
        "smooth_EQa_constructed": False,
        "heterotic_threshold_magnitude_promoted": False,
        "current_source_nogo": True,
        "next_required_artifact": NEXT,
        "closure_claimed": False,
        "target_fitting_used": False,
    }
    OUTPUT_CERT.write_text(json.dumps(cert, indent=2, sort_keys=True) + "\n", encoding="utf-8")

    note = f"""# Selected Heterotic OrientedPhiFin FiniteQuotientIdentity SourceTheorem or SmoothEQaPayload v1

## Result

```text
status = {STATUS}
closed_leaf_count = {closed_count}/{len(leaf_status)}
kernel_policy_closed = true
finite_quotient_identity_constructed = false
smooth_EQa_constructed = false
heterotic_threshold_magnitude_promoted = false
next_required_artifact = {NEXT}
```

## Theorem

{candidate["theorem"]["statement"]}

## Source-Theorem Request

```text
{rel(OUTPUT_REQUEST)}
```

## Leaf Status

```json
{json.dumps(leaf_status, indent=2, sort_keys=True)}
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
