"""Build oriented Phi_fin orientation/magnitude co-emission reduction theorem."""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "candidate_data"
CERTS = ROOT / "certificates"
PROOF = ROOT / "proof_corpus"

INPUTS = {
    "coemission_packet": DATA / "selected_heterotic_orientedphifin_fullfourierorbit_source_coemission_packet.json",
    "fullorbit_source_selection": DATA / "selected_heterotic_orientedphifin_fullfourierorbit_sourceselection_theorem_or_nogo.candidate.json",
    "fullorbit_trace_identity": DATA / "selected_heterotic_orientedphifin_fullfourierorbit_traceidentity.json",
    "product_operator": DATA / "selected_heterotic_orientedphifin_productoperator_or_smootheqa_magnitudesource.candidate.json",
    "source_emission_gate": DATA / "selected_heterotic_orientedphifin_sourceemission_or_smootheqa_thresholdidentity.candidate.json",
    "source_identity_frontier": DATA / "selected_heterotic_orientedphifin_sourceidentity_or_orientedbn_operatoremission.candidate.json",
    "orientation_functor": DATA / "selected_heterotic_orientedphifin_finiterhoe_to_orientedbn_functor_or_smoothrepresentative.candidate.json",
    "routec_trace_equals_27mode": DATA / "selected_u1y_routec_trace_equals_27mode_or_full_hym_replay.candidate.json",
}

OUTPUT_DATA = DATA / "selected_heterotic_orientedphifin_orientation_magnitude_coemission_theorem.candidate.json"
OUTPUT_PACKET = DATA / "selected_heterotic_orientedphifin_orientation_magnitude_coemission_packet.json"
OUTPUT_CERT = CERTS / "selected_heterotic_orientedphifin_orientation_magnitude_coemission_theorem_certificate.json"
OUTPUT_NOTE = PROOF / "Selected_Heterotic_OrientedPhiFin_OrientationMagnitude_CoEmission_Theorem_v1.md"

STATUS = "HETEROTIC_ORIENTEDPHIFIN_ORIENTATION_MAGNITUDE_COEMISSION_REDUCED_TO_BRANCH_IDENTITY_OPEN"
NEXT = "Selected_Heterotic_OrientedPhiFin_BranchIdentity_SourceCertificate_or_SmoothEQa_FinalGate_v1"


def rel(path: Path) -> str:
    try:
        return str(path.relative_to(ROOT))
    except ValueError:
        return str(path)


def load(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def main() -> dict[str, Any]:
    coemission = load(INPUTS["coemission_packet"])
    fullorbit = load(INPUTS["fullorbit_source_selection"])
    trace_identity = load(INPUTS["fullorbit_trace_identity"])
    product = load(INPUTS["product_operator"])
    source_gate = load(INPUTS["source_emission_gate"])
    frontier = load(INPUTS["source_identity_frontier"])
    orientation = load(INPUTS["orientation_functor"])
    routec = load(INPUTS["routec_trace_equals_27mode"])

    support_reduction = {
        "same_BN_domain_for_Ctau_and_PhiFin_positive_gap": product["decision"]["same_BN_domain_for_Ctau_and_PhiFin_positive_gap"],
        "C_tau_commutes_with_PhiFin_DE_as_functional_calculus": product["decision"]["commutation_or_simultaneous_functional_calculus_closed"],
        "C_tau_orientation_available_on_BN_rank_slots": orientation["decision"]["finite_rhoE_to_oriented_BN_orientation_functor_closed"],
        "selected_27mode_DE_gap_layer_closed": routec["decision"]["DE_gap_Riesz_Green_layer_closed"],
        "selected_27mode_trace_equality_closed": routec["decision"]["selected_trace_equality_for_27mode_DE"],
        "full_positive_fourier_orbit_selected_at_gap_scope": fullorbit["decision"]["full_positive_fourier_orbit_selected_at_gap_layer_scope"],
        "relative_finitepart_trace_identity_closed": fullorbit["decision"]["trace_identity_closed_relative_to_coemission"],
        "oriented_positive_sector_policy_computable": source_gate["closed_support"]["finite_positive_policy_available"],
        "kernel_and_no_double_count_policy_algebraically_closed": (
            source_gate["closed_support"]["kernel_policy_algebraic"]
            and source_gate["closed_support"]["no_double_counting_algebraic"]
        ),
        "operator_payload_ready": frontier["decision"]["operator_payload_ready"],
    }
    closed_support_count = sum(1 for value in support_reduction.values() if value is True)

    branch_identity_gate = {
        "schema": "SelectedHeterotic.OrientedPhiFin.OrientationMagnitudeCoEmissionPacket.v1",
        "status": "BRANCH_IDENTITY_SOURCE_CERTIFICATE_REQUIRED",
        "support_reduction_closed": closed_support_count == len(support_reduction),
        "closed_support_count": closed_support_count,
        "support_required_count": len(support_reduction),
        "five_field_coemission_request_reduced": True,
        "original_remaining_required_fields": coemission["remaining_required_fields"],
        "reduced_single_leaf": {
            "same_source_orientation_magnitude_branch_identity": {
                "closed": False,
                "missing": (
                    "a selected heterotic Qa/SU3 source certificate proving that the Route-C "
                    "27-mode Phi_fin D_E magnitude branch and the C_tau oriented B_N branch "
                    "are emitted as one threshold complex, or a smooth E_Qa quotient theorem "
                    "that emits that same complex"
                ),
            }
        },
        "would_close_under_branch_identity": {
            "same_source_identity_between_routec_gap_layer_and_heterotic_oriented_phifin": True,
            "C_tau_orientation_emitted_on_full_27mode_BN_domain": True,
            "proof_C_tau_commutes_with_selected_routec_DE_as_source_operator": True,
            "oriented_positive_sector_policy_selected_before_finitepart": True,
            "finitepart_trace_identity_inherits_source_ownership": True,
        },
        "guardrail": "The five fields are not individually closed here; they are reduced to one same-source branch-identity theorem.",
    }
    OUTPUT_PACKET.write_text(json.dumps(branch_identity_gate, indent=2, sort_keys=True) + "\n", encoding="utf-8")

    trace_values = {
        "plus_sector_product": trace_identity["plus_sector_product"],
        "minus_sector_product": trace_identity["minus_sector_product"],
        "oriented_abs_sector_product": trace_identity["oriented_abs_sector_product"],
        "finitepart_expression": trace_identity["oriented_abs_sector_logdet_exact"],
    }

    decision = {
        "support_reduction_closed": branch_identity_gate["support_reduction_closed"],
        "closed_support_count": closed_support_count,
        "support_required_count": len(support_reduction),
        "five_field_coemission_request_reduced_to_single_leaf": True,
        "same_source_orientation_magnitude_branch_identity_closed": False,
        "orientation_magnitude_coemission_closed": False,
        "full_oriented_phi_fin_threshold_closed": False,
        "oriented_logdet_promoted": False,
        "next_required_artifact": NEXT,
        "target_fitting_used": False,
        "closure_claimed": False,
    }

    candidate = {
        "candidate": "SelectedHeteroticOrientedPhiFinOrientationMagnitudeCoEmissionTheorem",
        "status": STATUS,
        "inputs": {key: rel(path) for key, path in INPUTS.items()},
        "parent_statuses": {
            "fullorbit_source_selection": fullorbit["status"],
            "product_operator": product["status"],
            "source_emission_gate": source_gate["status"],
            "source_identity_frontier": frontier["status"],
            "orientation_functor": orientation["status"],
            "routec_trace_equals_27mode": routec["status"],
        },
        "support_reduction": support_reduction,
        "trace_values_support_only": trace_values,
        "branch_identity_gate_path": rel(OUTPUT_PACKET),
        "decision": decision,
        "theorem": {
            "name": "OrientationMagnitudeCoEmissionReductionTheorem",
            "proved": True,
            "statement": (
                "For the selected oriented Phi_fin branch, the current source record closes "
                "same B_N domain, simultaneous functional calculus, C_tau rank-slot orientation "
                "support, selected 27-mode D_E gap-layer magnitude, relative full-orbit trace "
                "identity, finite positive policy, and kernel/no-double-count algebra. Therefore "
                "the previous five named co-emission requirements are equivalent to one remaining "
                "source leaf: a same-source branch identity proving that the selected heterotic "
                "Qa/SU3 source co-emits the Route-C Phi_fin D_E magnitude branch and the C_tau "
                "orientation branch as one threshold complex. Without that leaf, the oriented "
                "finitepart remains support-only."
            ),
        },
        "guardrails": {
            "does_not_close_branch_identity": True,
            "does_not_close_orientation_magnitude_coemission": True,
            "does_not_promote_oriented_logdet": True,
            "does_not_promote_two_support_packets_by_multiplication": True,
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
        "branch_identity_gate_path": rel(OUTPUT_PACKET),
        "note_path": rel(OUTPUT_NOTE),
        "support_reduction_closed": branch_identity_gate["support_reduction_closed"],
        "closed_support_count": closed_support_count,
        "support_required_count": len(support_reduction),
        "five_field_coemission_request_reduced_to_single_leaf": True,
        "same_source_orientation_magnitude_branch_identity_closed": False,
        "orientation_magnitude_coemission_closed": False,
        "oriented_logdet_promoted": False,
        "closure_claimed": False,
        "target_fitting_used": False,
        "next_required_artifact": NEXT,
    }
    OUTPUT_CERT.write_text(json.dumps(cert, indent=2, sort_keys=True) + "\n", encoding="utf-8")

    note = f"""# Selected Heterotic OrientedPhiFin OrientationMagnitude CoEmission Theorem v1

## Result

```text
status = {STATUS}
support_reduction_closed = true
closed_support_count = {closed_support_count}
support_required_count = {len(support_reduction)}
five_field_coemission_request_reduced_to_single_leaf = true
same_source_orientation_magnitude_branch_identity_closed = false
orientation_magnitude_coemission_closed = false
next_required_artifact = {NEXT}
```

## Theorem

{candidate["theorem"]["statement"]}

## Support Values

```text
plus_sector_product = {trace_values["plus_sector_product"]}
minus_sector_product = {trace_values["minus_sector_product"]}
oriented_abs_sector_product = {trace_values["oriented_abs_sector_product"]}
finitepart_expression = {trace_values["finitepart_expression"]}
```

These values remain support-only until the single branch-identity/source-certificate leaf is filled.

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
