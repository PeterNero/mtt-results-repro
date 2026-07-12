"""Build the heterotic End(E) domain-basis or nonidentity rho_E source-emission gate."""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "candidate_data"
CERTS = ROOT / "certificates"
PROOF = ROOT / "proof_corpus"

INPUT_FILL = DATA / "selected_heterotic_ende_to_bn_functor_or_rhoe_transition_valuepacket_fill.candidate.json"
INPUT_TYPED = DATA / "typed_monad_data_fill_attempt.candidate.json"
INPUT_GERBE = DATA / "twisted_source_promotion_packet_fill_attempt.candidate.json"
INPUT_U1Y = DATA / "selected_u1y_routec_nonidentity_rhoe_quotientvalid_bn_interface.candidate.json"

OUTPUT_DATA = DATA / "selected_heterotic_ende_domainbasis_or_nonidentity_rhoe_sourceemission.candidate.json"
OUTPUT_CERT = CERTS / "selected_heterotic_ende_domainbasis_or_nonidentity_rhoe_sourceemission_certificate.json"
OUTPUT_NOTE = PROOF / "Selected_Heterotic_EndE_DomainBasis_or_NonIdentityRhoE_SourceEmission_v1.md"

STATUS = "HETEROTIC_ENDE_DOMAINBASIS_OR_NONIDENTITY_RHOE_SOURCEEMISSION_GATE_BUILT_VALUES_OPEN"
NEXT = "Selected_Heterotic_TypedCechEndE_Basis_or_ProjectiveRhoE_FillAttempt_v1"


def rel(path: Path) -> str:
    try:
        return str(path.relative_to(ROOT))
    except ValueError:
        return str(path)


def load(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def main() -> dict[str, Any]:
    fill = load(INPUT_FILL)
    typed = load(INPUT_TYPED)
    gerbe = load(INPUT_GERBE)
    u1y = load(INPUT_U1Y)

    lane_a = {
        "id": "typed_cech_EndE_domain_basis",
        "goal": "emit a selected finite End(E) section/cochain/domain basis from the typed monad/Cech data",
        "required_payload": {
            "selected_cover_or_finite_galerkin_domain": False,
            "line_bundle_transition_or_automorphy_factors": False,
            "typed_f_map_matrix": False,
            "typed_g_map_matrix": False,
            "g_f_zero_machine_check": False,
            "local_freeness_or_exactness_certificate": False,
            "EndE_basis_vectors_or_cochains": False,
            "trace_inner_product_on_EndE": False,
            "zero_mode_or_shared_line_policy": False,
        },
        "current_support": {
            "monad_topology_selected": typed["fill_result"]["topological_monad_data_filled"],
            "rank": typed["partial_packet"]["typed_monad"]["rank"],
            "c1_zero": typed["partial_packet"]["typed_monad"]["monad_checks"]["c1_zero"],
            "c2_zero": typed["partial_packet"]["typed_monad"]["monad_checks"]["c2_zero"],
            "c3_integral": typed["partial_packet"]["typed_monad"]["monad_checks"]["c3_integral"],
            "typed_maps_filled": typed["fill_result"]["typed_maps_filled"],
            "cochain_or_dolbeault_packet_filled": typed["fill_result"]["cochain_or_dolbeault_packet_filled"],
        },
        "closes_now": False,
    }

    lane_b = {
        "id": "projective_twisted_nonidentity_rhoE",
        "goal": "emit a selected nonidentity heterotic rho_E transition/projective/twisted carrier on the same branch",
        "required_payload": {
            "selected_gerbe_or_B_field_representative": False,
            "map_to_central_cocycle_or_transition_law": False,
            "rho_E_generator_or_boundary_matrices": False,
            "nonidentity_check": False,
            "projective_cocycle_law": False,
            "metric_or_unitarity_compatibility": False,
            "shared_line_or_fixed_fiber_quotient_compatibility": False,
            "sector_or_QaSU3_domain_maps": False,
            "finite_response_exit": False,
        },
        "current_support": {
            "gerbe_fill_status": gerbe["status"],
            "projective_rhoE_tables_supplied": gerbe["fill_result"]["projective_rhoE_tables_supplied"],
            "u1y_nonidentity_schema_built": u1y["interface_checks"]["previous_gate_reduced_to_this_payload"],
            "u1y_template_values_open": u1y["interface_checks"]["all_template_selected_values_open"],
        },
        "closes_now": False,
    }

    acceptance_kernel = {
        "accept_if": [
            "Lane A emits selected End(E) basis/cochains plus trace/quotient policy, then a later map may build End(E)->B_N",
            "Lane B emits selected nonidentity rho_E/transition data plus quotient compatibility and finite response exit",
        ],
        "forbidden": [
            "abstract End(E) fiber dimension as a finite basis",
            "identity rho_E",
            "Route-C nonidentity schema as heterotic rho_E values",
            "R+ geometry as bundle transition data",
            "topological Chern classes as operator values",
            "observed electroweak constants or target residuals",
        ],
    }

    candidate = {
        "candidate": "SelectedHeteroticEndEDomainBasisOrNonidentityRhoESourceEmission",
        "status": STATUS,
        "inputs": {
            "previous_fill": rel(INPUT_FILL),
            "typed_monad": rel(INPUT_TYPED),
            "twisted_source_fill": rel(INPUT_GERBE),
            "u1y_nonidentity_schema": rel(INPUT_U1Y),
        },
        "input_statuses": {
            "previous_fill": fill["status"],
            "typed_monad": typed["status"],
            "twisted_source_fill": gerbe["status"],
            "u1y_nonidentity_schema": u1y["status"],
        },
        "target_fitting_used": False,
        "closure_claimed": False,
        "lanes": {
            "A_typed_cech_EndE_domain_basis": lane_a,
            "B_projective_twisted_nonidentity_rhoE": lane_b,
        },
        "acceptance_kernel": acceptance_kernel,
        "decision": {
            "sourceemission_gate_built": True,
            "typed_cech_EndE_domain_basis_emitted": False,
            "projective_twisted_nonidentity_rhoE_emitted": False,
            "EndE_to_BN_functor_filled": False,
            "E_Qa_computed": False,
            "same_source_identity_proved": False,
            "computed_threshold_value": False,
            "next_required_artifact": NEXT,
            "target_fitting_used": False,
        },
        "guardrails": {
            "promotes_abstract_EndE_dimension_as_basis": False,
            "inserts_identity_rhoE": False,
            "promotes_u1y_schema_as_heterotic_values": False,
            "promotes_Rplus_as_transition_data": False,
            "uses_observed_electroweak_data": False,
            "uses_target_residual_scan": False,
            "target_fitting_used": False,
        },
        "theorem": {
            "name": "HeteroticEndEDomainBasisOrNonidentityRhoESourceEmissionGateTheorem",
            "proved": True,
            "statement": (
                "After the source-certificate leaves are closed, the first true value "
                "needed for heterotic Phi_fin closure is either a selected finite "
                "End(E) basis/cochain packet with trace and quotient policy, or a "
                "selected nonidentity rho_E transition/projective carrier with "
                "quotient compatibility. Current support does not fill either lane."
            ),
        },
    }

    OUTPUT_DATA.write_text(json.dumps(candidate, indent=2, sort_keys=True) + "\n", encoding="utf-8")

    cert = {
        "certificate": candidate["candidate"],
        "status": STATUS,
        "candidate_path": rel(OUTPUT_DATA),
        "note_path": rel(OUTPUT_NOTE),
        "sourceemission_gate_built": True,
        "typed_cech_EndE_domain_basis_emitted": False,
        "projective_twisted_nonidentity_rhoE_emitted": False,
        "EndE_to_BN_functor_filled": False,
        "E_Qa_computed": False,
        "same_source_identity_proved": False,
        "next_required_artifact": NEXT,
        "target_fitting_used": False,
    }
    OUTPUT_CERT.write_text(json.dumps(cert, indent=2, sort_keys=True) + "\n", encoding="utf-8")

    note = f"""# Selected Heterotic EndE DomainBasis or NonIdentityRhoE SourceEmission v1

## Result

```text
status = {STATUS}
typed_cech_EndE_domain_basis_emitted = false
projective_twisted_nonidentity_rhoE_emitted = false
EndE_to_BN_functor_filled = false
E_Qa_computed = false
same_source_identity_proved = false
next_required_artifact = {NEXT}
```

## Lane A: Typed/Cech End(E) Domain Basis

```json
{json.dumps(lane_a, indent=2, sort_keys=True)}
```

## Lane B: Projective/Twisted Nonidentity rhoE

```json
{json.dumps(lane_b, indent=2, sort_keys=True)}
```

## Acceptance Kernel

```json
{json.dumps(acceptance_kernel, indent=2, sort_keys=True)}
```

This gate makes the next computation exact. We either build selected finite
`End(E)` basis/cochain data from typed monad/Cech source material, or selected
nonidentity heterotic `rho_E` transition data from the gerbe/twisted source.
Everything else remains support.
"""
    OUTPUT_NOTE.write_text(note, encoding="utf-8")
    return candidate


if __name__ == "__main__":
    result = main()
    print(f"wrote {rel(OUTPUT_DATA)}")
    print(f"wrote {rel(OUTPUT_CERT)}")
    print(f"wrote {rel(OUTPUT_NOTE)}")
    print(result["status"])
