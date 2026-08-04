"""Build the non-identity rho_E / quotient-valid B_N construction interface."""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "candidate_data"
CERTS = ROOT / "certificates"
PROOF = ROOT / "proof_corpus"

PREVIOUS = DATA / "selected_u1y_routec_selectedcorrection_source_or_fullresponse_emission.candidate.json"
OUTPUT_DATA = DATA / "selected_u1y_routec_nonidentity_rhoe_quotientvalid_bn_interface.candidate.json"
OUTPUT_CERT = CERTS / "selected_u1y_routec_nonidentity_rhoe_quotientvalid_bn_interface_certificate.json"
OUTPUT_TEMPLATE = CERTS / "selected_u1y_routec_nonidentity_rhoe_quotientvalid_bn.template.json"
OUTPUT_NOTE = PROOF / "Selected_U1Y_RouteC_NonIdentity_RhoE_and_QuotientValid_BN_Construction_v1.md"

STATUS = "U1Y_ROUTEC_NONIDENTITY_RHOE_QUOTIENTVALID_BN_INTERFACE_BUILT_VALUES_OPEN"
NEXT = "Selected_U1Y_RouteC_NonIdentity_RhoE_and_QuotientValid_BN_FillAttempt_v1"


def load(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def rel(path: Path) -> str:
    return str(path.relative_to(ROOT))


def template() -> dict[str, Any]:
    return {
        "status": "OPEN_SELECTED_U1Y_ROUTEC_NONIDENTITY_RHOE_QUOTIENTVALID_BN_REQUIRED",
        "schema": "SelectedU1YRouteCNonIdentityRhoEQuotientValidBN.v1",
        "source_evidence": {
            "selected_by_mtt": None,
            "same_branch_q79_F_m1": None,
            "source_kind": None,
            "source_certificate": None,
            "no_observed_or_benchmark_inputs": None,
        },
        "rho_E": {
            "nonidentity": None,
            "projective_or_twisted_transition_tables": None,
            "metric_compatibility": None,
            "sector_maps_u_d_e_nuD": None,
            "trace_normalization": None,
            "fixed_fiber_quotient_compatibility": None,
        },
        "B_N": {
            "quotient_valid": None,
            "noninvariant_basis_vectors": None,
            "zero_mode_basis_order": None,
            "Gram_matrix": None,
            "projector_retention": None,
            "basis_transport_or_holonomy_component": None,
        },
        "operator_replay": {
            "D_E": None,
            "Riesz_projector": None,
            "Green_operator": None,
            "dotD_alpha1": None,
            "alpha1_driver_verified": None,
            "no_lifted_flags": None,
        },
        "correction_emission": {
            "deltaTheta_C1_solution": None,
            "primitive_C1_atom_matrices": None,
            "full_response_matrices": None,
            "A_selected": None,
            "b_selected_or_homogeneous_zero_theorem": None,
        },
        "acceptance_tests": {
            "mass_traceless_splitting_nonzero": None,
            "CKM_or_PMNS_commutator_nonzero": None,
            "CP_odd_invariant_nonzero": None,
            "lambda_12_not_computed_from_diagnostic_values": None,
        },
        "guardrails": {
            "diagnostic_splitter_not_used_as_source": None,
            "formal_lift_not_used_as_proof": None,
            "identity_rhoE_forbidden": None,
            "target_fitting_forbidden": None,
        },
    }


def build() -> tuple[dict[str, Any], dict[str, Any], dict[str, Any], str]:
    previous = load(PREVIOUS)
    tmpl = template()
    candidate = {
        "candidate": "SelectedU1YRouteCNonIdentityRhoEQuotientValidBNInterface",
        "status": STATUS,
        "input_statuses": {
            "selected_correction_emission_gate": previous["status"],
        },
        "template_path": rel(OUTPUT_TEMPLATE),
        "template": tmpl,
        "interface_checks": {
            "previous_gate_reduced_to_this_payload": previous["decision"]["nonidentity_rhoE_and_BN_required"],
            "required_payload_keys_imported": sorted(previous["required_payload"].keys()),
            "all_template_selected_values_open": True,
            "identity_rhoE_explicitly_forbidden": True,
            "diagnostic_splitter_explicitly_forbidden": True,
            "closure_claimed": False,
        },
        "promotion_rule": [
            "selected_by_mtt and same_branch_q79_F_m1 must be true",
            "rho_E must be non-identity and compatible with fixed-fiber quotient",
            "B_N must be quotient-valid and carry the non-invariant basis/holonomy component",
            "D_E/Riesz/Green/dotD replay must pass without lifted flags",
            "deltaTheta_C1 must emit selected correction or full-response matrices",
            "mass, commutator, and CP tests must pass on selected matrices",
        ],
        "what_this_interface_prevents": [
            "using the diagnostic qutrit/Weyl splitter as selected data",
            "using a formal Galerkin lift as proof",
            "using identity rho_E smoke payloads",
            "computing lambda_12 or flavor data before selected A/b emission",
        ],
        "next_required_artifact": NEXT,
        "closure_claimed": False,
        "target_fitting_used": False,
    }
    cert = {
        "certificate": "SelectedU1YRouteCNonIdentityRhoEQuotientValidBNInterface",
        "status": STATUS,
        "candidate_path": rel(OUTPUT_DATA),
        "template_path": rel(OUTPUT_TEMPLATE),
        "note_path": rel(OUTPUT_NOTE),
        "what_closes": {
            "nonidentity_rhoE_BN_payload_schema_built": True,
            "selected_source_requirements_named": True,
            "operator_replay_requirements_named": True,
            "correction_acceptance_tests_named": True,
            "forbidden_shortcuts_named": True,
        },
        "what_remains_open": {
            "selected_source_certificate": True,
            "nonidentity_rho_E_values": True,
            "quotient_valid_B_N_values": True,
            "selected_operator_replay": True,
            "selected_correction_or_full_response_matrices": True,
            "A_selected": True,
            "b_selected": True,
            "lambda_12": True,
            "Yukawa_CKM_PMNS_CP_or_full_SM_closure": True,
        },
        "next_required_artifact": NEXT,
        "closure_claimed": False,
        "target_fitting_used": False,
    }
    note = f"""# Selected U1Y Route-C NonIdentity RhoE and QuotientValid BN Construction v1

This is the strict fill interface for the next selected correction-source gate.

## Required

```text
same q79/F,m=1 source certificate,
non-identity rho_E with fixed-fiber quotient compatibility,
quotient-valid non-invariant B_N,
selected D_E/Riesz/Green/dotD replay without lifted flags,
selected deltaTheta_C1 solve,
selected primitive C1 atom or full-response matrices,
b_selected or a homogeneous-zero theorem,
mass, commutator, and CP tests on selected matrices.
```

## Forbidden

```text
diagnostic splitter as source,
formal lift as proof,
identity rho_E smoke payload,
observed or benchmark flavor values,
diagnostic lambda_12 values.
```

All selected values are open in the template. This file is an executable contract,
not a closure claim.

Next required artifact:

```text
{NEXT}
```

closure claimed: no
target fitting used: no
"""
    return candidate, cert, tmpl, note


def write_json(path: Path, payload: dict[str, Any]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(payload, indent=2, sort_keys=True) + "\n", encoding="utf-8")


def main() -> int:
    candidate, cert, tmpl, note = build()
    write_json(OUTPUT_DATA, candidate)
    write_json(OUTPUT_CERT, cert)
    write_json(OUTPUT_TEMPLATE, tmpl)
    OUTPUT_NOTE.write_text(note, encoding="utf-8")
    for path in [OUTPUT_DATA, OUTPUT_CERT, OUTPUT_TEMPLATE, OUTPUT_NOTE]:
        print(f"wrote {rel(path)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
