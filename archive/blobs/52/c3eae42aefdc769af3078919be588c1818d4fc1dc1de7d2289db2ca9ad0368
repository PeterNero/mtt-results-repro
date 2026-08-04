"""Build oriented Phi_fin source-ownership / smooth-EQa quotient attempt."""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "candidate_data"
CERTS = ROOT / "certificates"
PROOF = ROOT / "proof_corpus"

INPUTS = {
    "single_frontier": DATA / "selected_heterotic_orientedphifin_sourceidentity_single_frontier.json",
    "sourceidentity_gate": DATA / "selected_heterotic_orientedphifin_sourceidentity_or_orientedbn_operatoremission.candidate.json",
    "source_lift": DATA / "selected_heterotic_finiteinternalrhoe_to_phifin_or_smoothbundleconnection_sourcelift.candidate.json",
    "bundle_connection_gate": DATA / "selected_heterotic_bundleconnection_valuesolve_or_phifin_sourceidentity_proof.candidate.json",
    "smooth_trace_lift": DATA / "selected_heterotic_projectiverhoe_smoothtracelift_or_eqafinitepart.candidate.json",
    "physical_or_smooth_fill": DATA / "selected_heterotic_projectiverhoe_physicalanchor_or_smootheqa_sourcefillattempt.candidate.json",
    "direct_fill_packet": DATA / "selected_heterotic_orientedphifin_directfiniteresponse_fillattempt_packet.json",
}

OUTPUT_DATA = DATA / "selected_heterotic_orientedphifin_sourceownership_or_smootheqa_quotient.candidate.json"
OUTPUT_REQUEST = DATA / "selected_heterotic_orientedphifin_sourceownership_minimal_certificate_request.json"
OUTPUT_CERT = CERTS / "selected_heterotic_orientedphifin_sourceownership_or_smootheqa_quotient_certificate.json"
OUTPUT_NOTE = PROOF / "Selected_Heterotic_OrientedPhiFin_SourceOwnership_Theorem_or_SmoothEQa_Quotient_v1.md"

STATUS = "HETEROTIC_ORIENTEDPHIFIN_SOURCEOWNERSHIP_ATTEMPT_CURRENT_SOURCE_NOGO_CERTIFICATE_REQUEST_BUILT"
NEXT = "Selected_Heterotic_OrientedPhiFin_SourceOwnership_Certificate_FillAttempt_v1"


def rel(path: Path) -> str:
    try:
        return str(path.relative_to(ROOT))
    except ValueError:
        return str(path)


def load(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def main() -> dict[str, Any]:
    frontier = load(INPUTS["single_frontier"])
    sourceidentity = load(INPUTS["sourceidentity_gate"])
    source_lift = load(INPUTS["source_lift"])
    bundle_gate = load(INPUTS["bundle_connection_gate"])
    smooth_trace = load(INPUTS["smooth_trace_lift"])
    physical_or_smooth = load(INPUTS["physical_or_smooth_fill"])
    packet = load(INPUTS["direct_fill_packet"])

    lane_a_source_ownership = {
        "id": "A_source_ownership_theorem",
        "attempted": True,
        "closes_now": False,
        "support": {
            "operator_payload_ready": frontier["operator_payload_ready"],
            "ctau_source_selected": frontier["support_closed"]["ctau_signed_operator_source_selected"],
            "routec_27mode_DE_trace_layer_selected": frontier["support_closed"]["routec_27mode_DE_trace_layer_selected"],
            "oriented_values_materialized": packet["operator_values_materialized"]["minimum_positive_eigenvalue"] > 0,
            "finite_internal_packet_closed": source_lift["decision"]["finite_internal_packet_remains_closed"],
        },
        "blocking_facts": {
            "dimension_mismatch_11_to_27_without_functor": source_lift["dimension_comparison"]["dimension_match"] is False,
            "finite_internal_to_PhiFin_functor_constructed": source_lift["decision"]["finite_internal_to_PhiFin_functor_constructed"],
            "commuting_projection_proved": source_lift["decision"]["commuting_projection_proved"],
            "same_source_PhiFin_identity_proved": bundle_gate["decision"]["same_source_PhiFin_identity_proved"],
            "heterotic_source_owns_positive_BN_gap_layer": False,
        },
        "verdict": "OPEN_SOURCE_OWNERSHIP_NOT_PROVED",
    }

    lane_b_smooth_eqa_quotient = {
        "id": "B_smooth_EQa_quotient_theorem",
        "attempted": True,
        "closes_now": False,
        "support": {
            "Bismut_Rplus_geometry_support_present": physical_or_smooth["decision"]["smooth_geometry_support_present"],
            "smooth_EQa_lane_recognized": physical_or_smooth["decision"]["smooth_EQa_still_open"],
            "smooth_trace_lift_current_source_nogo": smooth_trace["decision"]["current_source_no_go_for_trace_lift"],
        },
        "blocking_facts": {
            "selected_bundle_A_and_F_A": not physical_or_smooth["still_open"]["selected_bundle_A_and_F_A"],
            "smooth_projective_transition_or_Deligne_Cech_values": not physical_or_smooth["still_open"]["smooth_projective_transition_or_Deligne_Cech_values"],
            "smooth_EQa_or_heat_zeta_torsion_finite_part": not physical_or_smooth["still_open"]["smooth_E_Qa_or_heat_zeta_torsion_finite_part"],
            "smooth_trace_lift_proved": smooth_trace["decision"]["smooth_trace_lift_proved"],
        },
        "verdict": "OPEN_SMOOTH_EQA_QUOTIENT_NOT_EMITTED",
    }

    request = {
        "schema": "SelectedHeterotic.OrientedPhiFin.SourceOwnership.CertificateRequest.v1",
        "status": "VALUES_REQUIRED",
        "required_certificate_fields": {
            "same_branch_QaSU3_heterotic_source_certificate": False,
            "oriented_BN_carrier_emitted_by_that_source": False,
            "quotient_or_functor_EndE_or_rhoE_to_oriented_BN": False,
            "positive_PhiFin_DE_magnitude_owned_by_source": False,
            "C_tau_orientation_bound_to_same_threshold_complex": frontier["support_closed"]["ctau_signed_operator_source_selected"],
            "smooth_EQa_or_finite_threshold_complex_quotients_to_packet": False,
            "finitepart_trace_identity_consumes_nonzero_oriented_sector": False,
            "kernel_zero_mode_shared_circle_policy_replayed": frontier["support_closed"]["kernel_policy_and_no_double_count"],
            "no_observed_data_or_residual_selector": True,
        },
        "acceptance_tests": [
            "all currently false certificate fields must be true before oriented logdet promotion",
            "dimension mismatch between 11-label internal packet and 27-mode BN must be resolved by an emitted functor or quotient",
            "Route-C source ownership cannot stand in for heterotic Qa/SU3 source ownership without a bridge theorem",
            "smooth EQa lane must emit A/F_A or equivalent operator values, not only Rplus geometry support",
            "full verify must pass with target_fitting_used=false",
        ],
        "candidate_finitepart_values_waiting_for_certificate": packet["finitepart_candidates"],
        "target_fitting_used": False,
        "closure_claimed": False,
    }
    OUTPUT_REQUEST.write_text(json.dumps(request, indent=2, sort_keys=True) + "\n", encoding="utf-8")

    decision = {
        "sourceownership_attempted": True,
        "operator_payload_ready_retained": frontier["operator_payload_ready"],
        "source_ownership_closed": False,
        "smooth_EQa_quotient_closed": False,
        "finitepart_trace_identity_closed": False,
        "oriented_logdet_promoted": False,
        "minimal_certificate_request_built": True,
        "next_required_artifact": NEXT,
        "request_path": rel(OUTPUT_REQUEST),
        "target_fitting_used": False,
        "closure_claimed": False,
    }

    candidate = {
        "candidate": "SelectedHeteroticOrientedPhiFinSourceOwnershipTheoremOrSmoothEQaQuotient",
        "status": STATUS,
        "inputs": {key: rel(path) for key, path in INPUTS.items()},
        "parent_statuses": {
            "sourceidentity_gate": sourceidentity["status"],
            "source_lift": source_lift["status"],
            "bundle_connection_gate": bundle_gate["status"],
            "smooth_trace_lift": smooth_trace["status"],
            "physical_or_smooth_fill": physical_or_smooth["status"],
        },
        "lanes": {
            "source_ownership_theorem": lane_a_source_ownership,
            "smooth_EQa_quotient_theorem": lane_b_smooth_eqa_quotient,
        },
        "request_path": rel(OUTPUT_REQUEST),
        "decision": decision,
        "theorem": {
            "name": "OrientedPhiFinSourceOwnershipCurrentSourceNoGo",
            "proved": True,
            "statement": (
                "The oriented B_N operator payload is ready, but the current source record "
                "still does not prove ownership by the heterotic Qa/SU3 branch. The direct "
                "source-ownership lane is blocked by the unresolved 11-label to 27-mode "
                "functor/commuting projection and by the absence of a same-source Phi_fin "
                "identity theorem. The smooth E_Qa quotient lane is blocked by the absence "
                "of selected bundle A/F_A or equivalent E_Qa/heat-zeta-torsion values. "
                "Therefore the next object is a minimal source-ownership certificate; no "
                "oriented logdet or threshold value is promoted."
            ),
        },
        "guardrails": {
            "does_not_promote_11label_internal_packet_to_27mode": True,
            "does_not_promote_routec_source_ownership": True,
            "does_not_promote_Rplus_geometry_to_EQa": True,
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
        "request_path": rel(OUTPUT_REQUEST),
        "note_path": rel(OUTPUT_NOTE),
        "operator_payload_ready_retained": True,
        "source_ownership_closed": False,
        "smooth_EQa_quotient_closed": False,
        "oriented_logdet_promoted": False,
        "next_required_artifact": NEXT,
        "closure_claimed": False,
        "target_fitting_used": False,
    }
    OUTPUT_CERT.write_text(json.dumps(cert, indent=2, sort_keys=True) + "\n", encoding="utf-8")

    note = f"""# Selected Heterotic OrientedPhiFin SourceOwnership Theorem or SmoothEQa Quotient v1

## Result

```text
status = {STATUS}
operator_payload_ready_retained = true
source_ownership_closed = false
smooth_EQa_quotient_closed = false
oriented_logdet_promoted = false
next_required_artifact = {NEXT}
```

## Theorem

{candidate["theorem"]["statement"]}

## Minimal Certificate Request

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
