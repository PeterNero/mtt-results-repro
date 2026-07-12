"""Build the heterotic projective rho_E source-selection/direct-identity frontier."""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "candidate_data"
CERTS = ROOT / "certificates"
PROOF = ROOT / "proof_corpus"

INPUTS = {
    "source_selection_contract": DATA / "selected_heterotic_projectiverhoe_source_selection_theorem_contract.json",
    "previous_reduction": DATA / "selected_heterotic_projectiverhoe_smoothsourcetheorem_or_directfiniteoperatorclosure.candidate.json",
    "gr_internal_separation": DATA / "gr_surface_internal_quantum_separation_theorem.candidate.json",
    "chi_qa": DATA / "selected_response_functional_chi_qa.candidate.json",
    "bundle_direct_gate": DATA / "selected_heterotic_bundle_curvature_trace_or_direct_operator_gate.candidate.json",
}

OUTPUT_DATA = DATA / "selected_heterotic_projectiverhoe_sourceselection_theorem_or_directoperatoridentity.candidate.json"
OUTPUT_CERT = CERTS / "selected_heterotic_projectiverhoe_sourceselection_theorem_or_directoperatoridentity_certificate.json"
OUTPUT_NOTE = PROOF / "Selected_Heterotic_ProjectiveRhoE_SourceSelectionTheorem_or_DirectOperatorIdentity_v1.md"
OUTPUT_MISSING = DATA / "selected_heterotic_projectiverhoe_sourceselection_remaining_obligations.json"

STATUS = "HETEROTIC_PROJECTIVERHOE_SOURCE_SELECTION_OR_DIRECT_OPERATOR_IDENTITY_ATTEMPT_OPEN"
NEXT = "Selected_Heterotic_ProjectiveRhoE_FinitePhysicalQuotient_SourceTheorem_v1"


def rel(path: Path) -> str:
    try:
        return str(path.relative_to(ROOT))
    except ValueError:
        return str(path)


def load(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def lane_status(flags: dict[str, bool]) -> str:
    if all(flags.values()):
        return "CLOSED"
    if any(flags.values()):
        return "PARTIAL"
    return "OPEN"


def main() -> dict[str, Any]:
    contract = load(INPUTS["source_selection_contract"])
    previous = load(INPUTS["previous_reduction"])
    gr_sep = load(INPUTS["gr_internal_separation"])
    chi_qa = load(INPUTS["chi_qa"])
    direct_gate = load(INPUTS["bundle_direct_gate"])

    finite_values = contract["finite_values_available"]

    finite_flags = {
        "selected_domain_exactly_finite_galerkin_labels": False,
        "smooth_GR_universal_complement_removed_before_threshold": (
            gr_sep["decision"]["GR_smooth_surface_response"] == "ROUTED_TO_GR_PROTOSPINOR_SECTOR"
            and gr_sep["decision"]["internal_reduced_Qa_SU3_determinant"] == "CLOSED_LOG_2008"
        ),
        "finite_rhoE_packet_selected_not_validator_only": False,
        "finite_admissibility_and_trace_theorem_derived": (
            chi_qa["decision"]["selected_chi_Qa"] == "1"
            and finite_values["finite_part"]["finite_trace_tau_squared"] == 8
            and finite_values["finite_part"]["finite_trace_projector"] == 1
        ),
    }

    smooth_flags = {
        "selected_Deligne_Cech_B_field_local_data_emitted": False,
        "DD_tau_class_maps_to_finite_tau_table": False,
        "rhoE_transition_boundary_matrices_metric_compatibility_emitted": False,
        "mapped_FreedWitten_GreenSchwarz_projector_retention_verified": False,
    }

    direct_support = direct_gate["routes"]["B_direct_finite_operator"]["support"]
    direct_flags = {
        "selected_source_certificate_for_bundle_twist_emitted": direct_support["source_certificate_found"],
        "direct_finite_operator_packet_with_rhoE_or_DE_emitted": direct_support["direct_operator_emission_found"],
        "Riesz_Green_dotD_zero_order_block_emitted": False,
        "finite_heat_zeta_torsion_trace_convention_emitted": False,
    }

    finite_missing = [key for key, value in finite_flags.items() if not value]
    smooth_missing = [key for key, value in smooth_flags.items() if not value]
    direct_missing = [key for key, value in direct_flags.items() if not value]

    obligation_map = {
        "schema": "SelectedHeteroticProjectiveRhoESourceSelectionRemainingObligations.v1",
        "status": "OPEN",
        "strongest_lane": "finite_physical_quotient_selection",
        "finite_physical_quotient_selection": {
            "contract": contract["must_prove_one_of"]["finite_physical_quotient_selection"],
            "flags": finite_flags,
            "missing": finite_missing,
            "minimal_remaining_lemma": (
                "Prove that the selected heterotic Qa/SU3 projective threshold source "
                "is exactly the finite Galerkin quotient with labels F_i,G_i,P, and that "
                "the audited tau/rho_E/D_E/Green/Riesz/dotD packet is emitted by that source."
            ),
        },
        "smooth_representative_map": {
            "contract": contract["must_prove_one_of"]["smooth_representative_map"],
            "flags": smooth_flags,
            "missing": smooth_missing,
        },
        "direct_operator_identity": {
            "contract": contract["must_prove_one_of"]["direct_operator_identity"],
            "flags": direct_flags,
            "missing": direct_missing,
        },
        "forbidden_shortcuts": contract["forbidden_shortcuts"],
    }

    lane_evaluation = {
        "finite_physical_quotient_selection": {
            "status": lane_status(finite_flags),
            "closed": all(finite_flags.values()),
            "support_count": sum(finite_flags.values()),
            "required_count": len(finite_flags),
            "flags": finite_flags,
            "missing": finite_missing,
            "why_strongest": [
                "it reuses the accepted GR/internal separation instead of constructing new smooth local data",
                "it reuses chi_Qa=1 as finite response normalization without treating it as source identity",
                "all needed finite tau/rho_E/D_E/Green/Riesz/dotD values are already audited and replayable",
            ],
        },
        "smooth_representative_map": {
            "status": lane_status(smooth_flags),
            "closed": all(smooth_flags.values()),
            "support_count": sum(smooth_flags.values()),
            "required_count": len(smooth_flags),
            "flags": smooth_flags,
            "missing": smooth_missing,
        },
        "direct_operator_identity": {
            "status": lane_status(direct_flags),
            "closed": all(direct_flags.values()),
            "support_count": sum(direct_flags.values()),
            "required_count": len(direct_flags),
            "flags": direct_flags,
            "missing": direct_missing,
        },
    }

    decision = {
        "contract_replayed": True,
        "all_three_lanes_evaluated": True,
        "strongest_lane": "finite_physical_quotient_selection",
        "finite_physical_quotient_source_theorem_proved": False,
        "smooth_representative_map_proved": False,
        "direct_operator_identity_proved": False,
        "closure_claimed": False,
        "target_fitting_used": False,
        "next_required_artifact": NEXT,
        "minimal_remaining_lemma": obligation_map["finite_physical_quotient_selection"]["minimal_remaining_lemma"],
    }

    candidate = {
        "candidate": "SelectedHeteroticProjectiveRhoESourceSelectionTheoremOrDirectOperatorIdentity",
        "status": STATUS,
        "inputs": {key: rel(path) for key, path in INPUTS.items()},
        "input_statuses": {
            "previous_reduction": previous["status"],
            "gr_internal_separation": gr_sep["status"],
            "chi_qa": chi_qa["status"],
            "bundle_direct_gate": direct_gate["status"],
        },
        "finite_values_carried_forward": finite_values,
        "lane_evaluation": lane_evaluation,
        "remaining_obligations_path": rel(OUTPUT_MISSING),
        "decision": decision,
        "guardrails": {
            "does_not_treat_finite_candidate_as_selected_source": True,
            "does_not_treat_chi_Qa_as_heterotic_rhoE_identity": True,
            "does_not_treat_GR_separation_as_bundle_operator_identity": True,
            "does_not_import_q79_or_observed_values": True,
            "does_not_compute_E_Qa_or_threshold_value": True,
            "does_not_close_full_SM_or_electroweak_matching": True,
        },
        "theorem": {
            "name": "HeteroticProjectiveRhoESourceSelectionFrontierReduction",
            "proved": True,
            "statement": (
                "The source-selection/direct-identity contract reduces to one strongest "
                "finite-physical-quotient lemma: the same selected heterotic Qa/SU3 "
                "threshold source must name the finite Galerkin quotient F_i,G_i,P and "
                "emit the existing tau/rho_E/D_E/Green/Riesz/dotD packet as selected "
                "operator data. Existing artifacts support complement removal and finite "
                "trace normalization, but do not yet prove source identity."
            ),
        },
        "target_fitting_used": False,
        "closure_claimed": False,
    }

    OUTPUT_MISSING.write_text(json.dumps(obligation_map, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    OUTPUT_DATA.write_text(json.dumps(candidate, indent=2, sort_keys=True) + "\n", encoding="utf-8")

    cert = {
        "certificate": candidate["candidate"],
        "status": STATUS,
        "candidate_path": rel(OUTPUT_DATA),
        "note_path": rel(OUTPUT_NOTE),
        "remaining_obligations_path": rel(OUTPUT_MISSING),
        "contract_replayed": True,
        "all_three_lanes_evaluated": True,
        "strongest_lane": "finite_physical_quotient_selection",
        "finite_support_count": lane_evaluation["finite_physical_quotient_selection"]["support_count"],
        "finite_required_count": lane_evaluation["finite_physical_quotient_selection"]["required_count"],
        "finite_physical_quotient_source_theorem_proved": False,
        "smooth_representative_map_proved": False,
        "direct_operator_identity_proved": False,
        "closure_claimed": False,
        "target_fitting_used": False,
        "next_required_artifact": NEXT,
    }
    OUTPUT_CERT.write_text(json.dumps(cert, indent=2, sort_keys=True) + "\n", encoding="utf-8")

    note = f"""# Selected Heterotic ProjectiveRhoE SourceSelectionTheorem or DirectOperatorIdentity v1

## Result

```text
status = {STATUS}
strongest_lane = finite_physical_quotient_selection
finite_physical_quotient_source_theorem_proved = false
smooth_representative_map_proved = false
direct_operator_identity_proved = false
next_required_artifact = {NEXT}
```

## What this proves

This closes the meta-step around the previous contract: all three legal routes
were replayed against the current audited packets, and the strongest route is
now the finite physical quotient source theorem.

The finite route already has two real supports:

- GR/protospinor separation removes the smooth elastic complement from the
  internal Qa/SU3 determinant lane.
- `chi_Qa=1` supplies the finite retarded trace normalization.

It still does not prove the two source-identity clauses:

- the selected heterotic Qa/SU3 projective threshold source is exactly the
  finite Galerkin quotient on `F_i,G_i,P`;
- the existing `tau/rho_E/D_E/Green/Riesz/dotD` packet is emitted as selected
  heterotic source data, not merely as a validator candidate.

## Frontier

The next theorem should prove:

```text
{decision["minimal_remaining_lemma"]}
```

The machine-readable remaining-obligation packet is:

```text
{rel(OUTPUT_MISSING)}
```
"""
    OUTPUT_NOTE.write_text(note, encoding="utf-8")

    return candidate


if __name__ == "__main__":
    result = main()
    print(f"wrote {rel(OUTPUT_DATA)}")
    print(f"wrote {rel(OUTPUT_CERT)}")
    print(f"wrote {rel(OUTPUT_MISSING)}")
    print(f"wrote {rel(OUTPUT_NOTE)}")
    print(result["status"])
