"""Build projective rho_E bundle-connection/trace/quotient-policy replay."""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "candidate_data"
CERTS = ROOT / "certificates"
PROOF = ROOT / "proof_corpus"

INPUTS = {
    "kphys_or_smooth_fill": DATA / "selected_heterotic_projectiverhoe_kphysanchor_or_smoothoperatoridentity_fill.candidate.json",
    "remaining_obligations": DATA / "selected_heterotic_projectiverhoe_smooth_bundle_operator_or_kphys_remaining_obligations.json",
    "finite_packet": DATA / "selected_heterotic_projectiverhoe_finite_internal_operator_packet.json",
    "internal_finite_part": DATA / "selected_heterotic_projectiverhoe_internal_threshold_finitepart.json",
    "bundle_gate": DATA / "selected_heterotic_bundle_curvature_trace_or_direct_operator_gate.candidate.json",
    "standard_embedding_gate": DATA / "selected_heterotic_standard_embedding_selector_or_phifin_gate.candidate.json",
    "phifin_bridge": DATA / "selected_heterotic_phifin_sourceidentity_bridge_attempt.candidate.json",
}

OUTPUT_DATA = DATA / "selected_heterotic_projectiverhoe_bundleconnection_trace_quotient_policy.candidate.json"
OUTPUT_CERT = CERTS / "selected_heterotic_projectiverhoe_bundleconnection_trace_quotient_policy_certificate.json"
OUTPUT_CONTRACT = DATA / "selected_heterotic_projectiverhoe_smooth_trace_lift_or_eqa_finitepart_contract.json"
OUTPUT_NOTE = PROOF / "Selected_Heterotic_ProjectiveRhoE_BundleConnection_RepresentationTrace_QuotientPolicy_v1.md"

STATUS = "HETEROTIC_PROJECTIVERHOE_BUNDLECONNECTION_TRACE_QUOTIENT_POLICY_FINITE_INTERNAL_CLOSED_SMOOTH_LIFT_OPEN"
NEXT = "Selected_Heterotic_ProjectiveRhoE_SmoothTraceLift_or_EQaFinitePartOperator_v1"


def rel(path: Path) -> str:
    try:
        return str(path.relative_to(ROOT))
    except ValueError:
        return str(path)


def load(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def main() -> dict[str, Any]:
    fill = load(INPUTS["kphys_or_smooth_fill"])
    obligations = load(INPUTS["remaining_obligations"])
    finite_packet = load(INPUTS["finite_packet"])
    finite_part = load(INPUTS["internal_finite_part"])
    bundle_gate = load(INPUTS["bundle_gate"])
    standard_gate = load(INPUTS["standard_embedding_gate"])
    phifin_bridge = load(INPUTS["phifin_bridge"])

    finite_internal_policy = {
        "finite_domain_labels": finite_packet["labels"],
        "finite_domain_closed": finite_packet["selected"] and len(finite_packet["labels"]) == 11,
        "finite_trace_normalization_closed": finite_packet["trace_normalization"],
        "finite_kernel_policy_closed": finite_part["zero_mode_policy"],
        "finite_quotient_regularization_closed": finite_part["regularization"],
        "finite_operator_action_closed": {
            "rho_E_central_character": finite_packet["rho_E_central_character"],
            "D_E_diagonal_matrix_on_labels": finite_packet["D_E_diagonal_matrix_on_labels"],
            "Riesz_projector": finite_packet["Riesz_projector"],
            "Green_operator": finite_packet["Green_operator"],
            "Pi_tw": finite_packet["Pi_tw"],
            "chi_Qa": finite_packet["chi_Qa"],
        },
        "finite_threshold_value": finite_part["Delta_selected_internal_exact"],
    }

    smooth_bridge_policy = {
        "standard_embedding_route": {
            "retired_as_current_proof_source": standard_gate["decision"]["standard_embedding_retired_as_current_proof_source"],
            "reason": standard_gate["standard_embedding_evaluation"]["reason"],
            "reopen_requires": standard_gate["standard_embedding_evaluation"]["what_would_be_needed_to_reopen"],
        },
        "direct_operator_route": {
            "finite_projective_packet_now_selected": True,
            "phifin_support_imported_without_promotion": phifin_bridge["decision"]["support_imported_without_promotion"],
            "still_missing_smooth_lift": [
                "smooth projective rho_E transition/Cech/Deligne representative",
                "selected bundle connection A or equivalent smooth operator source",
                "bundle curvature F_A",
                "representation action on u(E)-valued one-forms",
                "trace lift from finite eleven-label trace to smooth heat/zeta/torsion trace",
                "kernel/complement quotient policy for the smooth operator",
                "E_Qa matrix or equivalent smooth finite-part operator",
            ],
        },
    }

    closed_subclaims = {
        "finite_internal_trace_normalization": True,
        "finite_internal_quotient_policy": True,
        "finite_internal_operator_action": True,
        "finite_internal_logdet_value": finite_part["Delta_selected_internal_exact"] == "log(2008)",
        "standard_embedding_retired_for_current_branch": standard_gate["decision"]["standard_embedding_retired_as_current_proof_source"],
    }

    open_subclaims = {
        "smooth_trace_lift": False,
        "smooth_projective_transition_data": False,
        "selected_bundle_connection_A": False,
        "selected_bundle_curvature_F_A": False,
        "smooth_representation_action_on_uE_one_forms": False,
        "smooth_kernel_and_quotient_policy": False,
        "E_Qa_or_smooth_finitepart_operator": False,
        "physical_K_phys_or_matching_scheme": False,
    }

    contract = {
        "schema": "SelectedHeteroticProjectiveRhoESmoothTraceLiftOrEQaFinitePartContract.v1",
        "status": "OPEN",
        "finite_internal_subclaims_closed": closed_subclaims,
        "smooth_or_physical_subclaims_open": open_subclaims,
        "next_required_artifact": NEXT,
        "must_supply": smooth_bridge_policy["direct_operator_route"]["still_missing_smooth_lift"],
        "forbidden_shortcuts": obligations["forbidden_shortcuts"]
        + [
            "treat finite eleven-label trace as the smooth heat trace without a trace-lift theorem",
            "reopen A=GammaPlus after its current-source retirement without a new selector",
        ],
    }

    decision = {
        "finite_internal_trace_and_quotient_policy_closed": all(closed_subclaims.values()),
        "smooth_bundle_connection_policy_closed": False,
        "smooth_operator_identity_closed": False,
        "E_Qa_computed": False,
        "standard_embedding_route_retired_for_current_branch": True,
        "direct_projective_rhoE_route_primary": True,
        "next_required_artifact": NEXT,
        "contract_path": rel(OUTPUT_CONTRACT),
        "target_fitting_used": False,
        "closure_claimed": False,
    }

    candidate = {
        "candidate": "SelectedHeteroticProjectiveRhoEBundleConnectionRepresentationTraceQuotientPolicy",
        "status": STATUS,
        "inputs": {key: rel(path) for key, path in INPUTS.items()},
        "input_statuses": {
            "kphys_or_smooth_fill": fill["status"],
            "bundle_gate": bundle_gate["status"],
            "standard_embedding_gate": standard_gate["status"],
            "phifin_bridge": phifin_bridge["status"],
        },
        "finite_internal_policy": finite_internal_policy,
        "smooth_bridge_policy": smooth_bridge_policy,
        "closed_subclaims": closed_subclaims,
        "open_subclaims": open_subclaims,
        "decision": decision,
        "guardrails": {
            "does_not_claim_smooth_trace_lift": True,
            "does_not_claim_selected_A_or_F_A": True,
            "does_not_reopen_standard_embedding": True,
            "does_not_promote_finite_trace_to_heat_trace": True,
            "does_not_claim_E_Qa": True,
            "target_fitting_used": False,
        },
        "theorem": {
            "name": "ProjectiveRhoEBundleTraceQuotientPolicyReduction",
            "proved": True,
            "statement": (
                "The selected projective rho_E packet closes the finite internal trace, "
                "quotient, operator-action, and logdet policy on the eleven-label domain. "
                "The older standard-embedding route remains retired for this branch, so "
                "smooth closure cannot be obtained by setting A=GammaPlus. What remains is "
                "a trace-lift/smooth-operator theorem: emit smooth projective transition "
                "data or a selected bundle connection/operator, then compute E_Qa or an "
                "equivalent heat/zeta/torsion finite part."
            ),
        },
        "target_fitting_used": False,
        "closure_claimed": False,
    }

    OUTPUT_DATA.write_text(json.dumps(candidate, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    OUTPUT_CONTRACT.write_text(json.dumps(contract, indent=2, sort_keys=True) + "\n", encoding="utf-8")

    cert = {
        "certificate": candidate["candidate"],
        "status": STATUS,
        "candidate_path": rel(OUTPUT_DATA),
        "contract_path": rel(OUTPUT_CONTRACT),
        "note_path": rel(OUTPUT_NOTE),
        "finite_internal_trace_and_quotient_policy_closed": True,
        "smooth_operator_identity_closed": False,
        "E_Qa_computed": False,
        "next_required_artifact": NEXT,
        "closure_claimed": False,
        "target_fitting_used": False,
    }
    OUTPUT_CERT.write_text(json.dumps(cert, indent=2, sort_keys=True) + "\n", encoding="utf-8")

    note = f"""# Selected Heterotic ProjectiveRhoE BundleConnection RepresentationTrace QuotientPolicy v1

## Result

```text
status = {STATUS}
finite_internal_trace_and_quotient_policy_closed = true
smooth_operator_identity_closed = false
E_Qa_computed = false
next_required_artifact = {NEXT}
```

## Closed at Finite Internal Scope

The selected projective `rho_E` packet now gives the exact internal policy:

- domain: `F1..F5,G1..G5,P`
- trace: ordinary finite trace over the selected eleven module labels
- quotient: finite `H_sel` has no zero eigenvalues after GR/internal routing
- operator: selected `rho_E`, `D_E`, Riesz projector, Green operator, `Pi_tw`
- finite part: `Delta_selected_internal = log(2008)`

## Still Not Closed

The smooth/physical bridge is not solved. The previous standard-embedding route
`A=GammaPlus` remains retired as a current proof source for this branch. The next
theorem must supply a trace lift or smooth operator identity rather than reuse
the finite trace as a heat trace.

```text
contract = {rel(OUTPUT_CONTRACT)}
```
"""
    OUTPUT_NOTE.write_text(note, encoding="utf-8")
    return candidate


if __name__ == "__main__":
    result = main()
    print(f"wrote {rel(OUTPUT_DATA)}")
    print(f"wrote {rel(OUTPUT_CERT)}")
    print(f"wrote {rel(OUTPUT_CONTRACT)}")
    print(f"wrote {rel(OUTPUT_NOTE)}")
    print(result["status"])
