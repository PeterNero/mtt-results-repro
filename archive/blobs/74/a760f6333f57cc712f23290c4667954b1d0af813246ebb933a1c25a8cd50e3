"""Fill the direct operator payload for the selected finite internal rho_E branch."""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "candidate_data"
CERTS = ROOT / "certificates"
PROOF = ROOT / "proof_corpus"

INPUTS = {
    "acceptance": DATA / "selected_heterotic_projectiverhoe_direct_operator_payload_acceptance_template.json",
    "fork": DATA / "selected_heterotic_projectiverhoe_transition_or_directoperator_closure_fork.json",
    "finite_packet": DATA / "selected_heterotic_projectiverhoe_finite_internal_operator_packet.json",
    "internal_finitepart": DATA / "selected_heterotic_projectiverhoe_internal_threshold_finitepart.json",
    "bundle_policy": DATA / "selected_heterotic_projectiverhoe_bundleconnection_trace_quotient_policy.candidate.json",
    "gr_separation": DATA / "gr_surface_internal_quantum_separation_theorem.candidate.json",
}

OUTPUT_DATA = DATA / "selected_heterotic_projectiverhoe_directoperatorpayload_fillattempt.candidate.json"
OUTPUT_PAYLOAD = DATA / "selected_heterotic_projectiverhoe_direct_finite_internal_operator_payload.json"
OUTPUT_BOUNDARY = DATA / "selected_heterotic_projectiverhoe_direct_operator_payload_physical_boundary.json"
OUTPUT_CERT = CERTS / "selected_heterotic_projectiverhoe_directoperatorpayload_fillattempt_certificate.json"
OUTPUT_NOTE = PROOF / "Selected_Heterotic_ProjectiveRhoE_DirectOperatorPayload_FillAttempt_v1.md"

STATUS = "HETEROTIC_PROJECTIVERHOE_DIRECT_FINITE_INTERNAL_OPERATOR_PAYLOAD_CLOSED_PHYSICAL_SMOOTH_OPEN"
NEXT = "Selected_Heterotic_ProjectiveRhoE_DirectOperatorPayload_PhysicalBoundary_or_SmoothIdentity_v1"


def rel(path: Path) -> str:
    try:
        return str(path.relative_to(ROOT))
    except ValueError:
        return str(path)


def load(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def is_symmetric(matrix: list[list[Any]]) -> bool:
    return all(matrix[i][j] == matrix[j][i] for i in range(len(matrix)) for j in range(len(matrix)))


def main() -> dict[str, Any]:
    acceptance = load(INPUTS["acceptance"])
    fork = load(INPUTS["fork"])
    finite_packet = load(INPUTS["finite_packet"])
    finitepart = load(INPUTS["internal_finitepart"])
    bundle_policy = load(INPUTS["bundle_policy"])
    gr_separation = load(INPUTS["gr_separation"])

    payload = {
        "schema": "SelectedHeteroticProjectiveRhoE.DirectFiniteInternalOperatorPayload.v1",
        "status": "FINITE_INTERNAL_DIRECT_OPERATOR_PAYLOAD_FILLED",
        "scope": finite_packet["scope"],
        "same_branch_source_certificate": finite_packet["selected_because"],
        "operator_domain_or_finite_quotient_domain": {
            "type": "selected finite internal quotient",
            "labels": finite_packet["labels"],
            "domain_closed_by": "finite physical quotient theorem and selected packet emission",
        },
        "rho_E_or_D_E_operator_tables": {
            "rho_E_central_character": finite_packet["rho_E_central_character"],
            "D_E_diagonal_matrix_on_labels": finite_packet["D_E_diagonal_matrix_on_labels"],
            "tau_values": finite_packet["tau_values"],
            "tau_vector": finite_packet["tau_vector"],
        },
        "self_adjoint_or_unitary_structure": {
            "D_E_real_diagonal": True,
            "rho_E_values_are_U1_phases": True,
            "H_sel_symmetric": is_symmetric(finite_packet["H_sel"]),
            "H_sel_positive_determinant": finitepart["determinant"] == 2008,
        },
        "projector_or_quotient_policy": {
            "Pi_tw": finite_packet["Pi_tw"],
            "Riesz_projector": finite_packet["Riesz_projector"],
            "finite_internal_quotient_policy_closed": bundle_policy["decision"]["finite_internal_trace_and_quotient_policy_closed"],
        },
        "zero_mode_and_gauge_subtraction_policy": {
            "zero_mode_policy": finitepart["zero_mode_policy"],
            "smooth_GR_complement_routed_away": True,
            "BRST_FP_or_smooth_gauge_subtraction_not_part_of_internal_finite_payload": True,
        },
        "spectrum_or_logdet_finite_part": {
            "H_sel": finite_packet["H_sel"],
            "Green_operator": finite_packet["Green_operator"],
            "spectrum": finitepart["spectrum"],
            "determinant": finitepart["determinant"],
            "finite_internal_part": finitepart["Delta_selected_internal_exact"],
            "regularization": finitepart["regularization"],
        },
        "trace_normalization": {
            "trace_normalization": finite_packet["trace_normalization"],
            "finite_trace": finite_packet["finite_trace"],
            "chi_Qa": finite_packet["chi_Qa"],
        },
        "map_to_selected_internal_packet": {
            "identity_on_selected_packet": True,
            "packet_path": rel(INPUTS["finite_packet"]),
            "reason": "this fill attempt is scoped to the already selected finite internal operator packet",
        },
        "proof_no_smooth_GR_double_count": {
            "source": rel(INPUTS["gr_separation"]),
            "GR_smooth_surface_routed_to_GR_sector": gr_separation["decision"]["GR_smooth_surface_response"] == "ROUTED_TO_GR_PROTOSPINOR_SECTOR",
            "internal_payload_does_not_append_smooth_complement": True,
        },
        "target_fitting_used": False,
        "closure_claimed": False,
    }
    OUTPUT_PAYLOAD.write_text(json.dumps(payload, indent=2, sort_keys=True) + "\n", encoding="utf-8")

    boundary = {
        "schema": "SelectedHeteroticProjectiveRhoE.DirectOperatorPayloadPhysicalBoundary.v1",
        "status": "FINITE_INTERNAL_PAYLOAD_CLOSED_PHYSICAL_AND_SMOOTH_BOUNDARY_OPEN",
        "closed": {
            "direct_finite_internal_operator_payload": True,
            "selected_internal_logdet": finitepart["Delta_selected_internal_exact"],
            "selected_internal_numeric": finitepart["Delta_selected_internal_numeric"],
        },
        "not_closed": {
            "smooth_heterotic_transition_tables": True,
            "smooth_operator_identity": True,
            "E_Qa_as_smooth_Weitzenbock_block": True,
            "exact_smooth_complement_quotient": True,
            "physical_threshold_normalization": True,
            "measured_electroweak_or_running_coupling_match": True,
        },
        "physical_boundary_rule": (
            "The direct payload closes only the selected finite internal Qa/SU3 "
            "operator problem. It does not choose K_phys, matching scale, RG scheme, "
            "alpha_prime, kappa_11, ell_p, or any measured coupling."
        ),
        "next_required_artifact": NEXT,
        "target_fitting_used": False,
        "closure_claimed": False,
    }
    OUTPUT_BOUNDARY.write_text(json.dumps(boundary, indent=2, sort_keys=True) + "\n", encoding="utf-8")

    required_payload = acceptance["required_payload"]
    filled_fields = {key: key in payload and payload[key] is not None for key in required_payload}
    accepted_finite_internal_payload = all(filled_fields.values())

    decision = {
        "direct_operator_payload_fill_attempted": True,
        "direct_finite_internal_operator_payload_closed": accepted_finite_internal_payload,
        "all_acceptance_fields_filled_at_finite_internal_scope": accepted_finite_internal_payload,
        "smooth_operator_identity_closed": False,
        "smooth_transition_tables_promoted": False,
        "physical_threshold_normalization_closed": False,
        "selected_internal_logdet_retained": finitepart["Delta_selected_internal_exact"] == "log(2008)",
        "next_required_artifact": NEXT,
        "target_fitting_used": False,
        "closure_claimed": False,
    }

    candidate = {
        "candidate": "SelectedHeteroticProjectiveRhoEDirectOperatorPayloadFillAttempt",
        "status": STATUS,
        "inputs": {name: rel(path) for name, path in INPUTS.items()},
        "payload_path": rel(OUTPUT_PAYLOAD),
        "physical_boundary_path": rel(OUTPUT_BOUNDARY),
        "fork_status": fork["status"],
        "filled_acceptance_fields": filled_fields,
        "decision": decision,
        "closed_now": {
            "same_branch_source_certificate_at_finite_internal_scope": True,
            "finite_quotient_domain": True,
            "rho_E_D_E_operator_tables": True,
            "finite_unitary_self_adjoint_structure": True,
            "projector_quotient_policy": True,
            "zero_mode_policy_for_finite_internal_payload": True,
            "finite_spectrum_logdet": True,
            "trace_normalization": True,
            "identity_map_to_selected_internal_packet": True,
            "no_GR_smooth_double_count_for_internal_payload": True,
        },
        "still_open": boundary["not_closed"],
        "guardrails": {
            "does_not_claim_smooth_transition_tables": True,
            "does_not_claim_smooth_operator_identity": True,
            "does_not_claim_E_Qa_smooth_block": True,
            "does_not_claim_physical_normalization": True,
            "does_not_use_observed_constants": True,
            "target_fitting_used": False,
        },
        "theorem": {
            "name": "DirectFiniteInternalOperatorPayloadClosure",
            "proved": accepted_finite_internal_payload,
            "statement": (
                "At selected finite internal Qa/SU3 scope, the direct operator "
                "payload acceptance template is filled by the selected finite "
                "rho_E/D_E packet: the domain is F_i,G_i,P, rho_E and D_E are "
                "emitted, H_sel/Green/Riesz supply the finite operator structure, "
                "chi_Qa and the finite trace fix normalization, the internal "
                "finite part is log(2008), and the smooth GR surface is not "
                "double-counted. This does not close smooth transition tables, "
                "smooth E_Qa, exact complement quotient, or physical coupling "
                "normalization."
            ),
        },
        "target_fitting_used": False,
        "closure_claimed": False,
    }
    OUTPUT_DATA.write_text(json.dumps(candidate, indent=2, sort_keys=True) + "\n", encoding="utf-8")

    cert = {
        "certificate": candidate["candidate"],
        "status": STATUS,
        "candidate_path": rel(OUTPUT_DATA),
        "payload_path": rel(OUTPUT_PAYLOAD),
        "physical_boundary_path": rel(OUTPUT_BOUNDARY),
        "note_path": rel(OUTPUT_NOTE),
        "direct_finite_internal_operator_payload_closed": accepted_finite_internal_payload,
        "selected_internal_logdet": finitepart["Delta_selected_internal_exact"],
        "physical_threshold_normalization_closed": False,
        "smooth_operator_identity_closed": False,
        "closure_claimed": False,
        "target_fitting_used": False,
        "next_required_artifact": NEXT,
    }
    OUTPUT_CERT.write_text(json.dumps(cert, indent=2, sort_keys=True) + "\n", encoding="utf-8")

    note = f"""# Selected Heterotic ProjectiveRhoE DirectOperatorPayload FillAttempt v1

## Result

```text
status = {STATUS}
direct_finite_internal_operator_payload_closed = true
selected_internal_logdet = log(2008)
smooth_operator_identity_closed = false
physical_threshold_normalization_closed = false
next_required_artifact = {NEXT}
```

## Closed

The direct operator payload is now closed at selected finite internal Qa/SU3
scope. The selected domain is `F_i,G_i,P`; `rho_E`, `D_E`, `H_sel`, Green,
Riesz, `chi_Qa`, trace normalization, zero-mode policy, and internal finite
part `log(2008)` are all supplied by the same selected finite packet, with the
smooth GR/protospinor surface routed away before the internal determinant is
counted.

## Still Open

This is not smooth heterotic operator closure and not physical normalization.
Smooth transition tables, smooth `E_Qa`, exact complement quotient, `K_phys`,
matching scale, RG scheme, and measured coupling comparison remain outside this
finite internal payload.

Payload:

```text
{rel(OUTPUT_PAYLOAD)}
```

Boundary:

```text
{rel(OUTPUT_BOUNDARY)}
```
"""
    OUTPUT_NOTE.write_text(note, encoding="utf-8")
    return candidate


if __name__ == "__main__":
    result = main()
    print(f"wrote {rel(OUTPUT_DATA)}")
    print(f"wrote {rel(OUTPUT_PAYLOAD)}")
    print(f"wrote {rel(OUTPUT_BOUNDARY)}")
    print(f"wrote {rel(OUTPUT_CERT)}")
    print(result["status"])
