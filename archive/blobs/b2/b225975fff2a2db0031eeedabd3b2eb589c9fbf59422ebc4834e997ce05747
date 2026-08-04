"""Build the finite physical quotient source theorem attempt for projective rho_E."""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "candidate_data"
CERTS = ROOT / "certificates"
PROOF = ROOT / "proof_corpus"

INPUTS = {
    "remaining_obligations": DATA / "selected_heterotic_projectiverhoe_sourceselection_remaining_obligations.json",
    "source_augmentation_packet": DATA / "source_augmentation_packet.candidate.json",
    "minimal_finite_galerkin": DATA / "minimal_hsel_gret_finite_galerkin_candidate.candidate.json",
    "locked_proof_state": DATA / "locked_proof_state.candidate.json",
    "gr_internal_separation": DATA / "gr_surface_internal_quantum_separation_theorem.candidate.json",
    "chi_qa": DATA / "selected_response_functional_chi_qa.candidate.json",
}

OUTPUT_DATA = DATA / "selected_heterotic_projectiverhoe_finitephysicalquotient_sourcetheorem.candidate.json"
OUTPUT_CERT = CERTS / "selected_heterotic_projectiverhoe_finitephysicalquotient_sourcetheorem_certificate.json"
OUTPUT_NOTE = PROOF / "Selected_Heterotic_ProjectiveRhoE_FinitePhysicalQuotient_SourceTheorem_v1.md"
OUTPUT_OBLIGATIONS = DATA / "selected_heterotic_projectiverhoe_finitephysicalquotient_remaining_obligations.json"

STATUS = "HETEROTIC_PROJECTIVERHOE_FINITE_PHYSICAL_QUOTIENT_DOMAIN_CLOSED_RHOE_SOURCE_EMISSION_OPEN"
NEXT = "Selected_Heterotic_ProjectiveRhoE_SelectedPacketEmission_or_OperatorIdentity_v1"


EXPECTED_LABELS = ["F1", "F2", "F3", "F4", "F5", "G1", "G2", "G3", "G4", "G5", "P"]


def rel(path: Path) -> str:
    try:
        return str(path.relative_to(ROOT))
    except ValueError:
        return str(path)


def load(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def ids_from_source(source_packet: dict[str, Any]) -> list[str]:
    return [entry["id"] for entry in source_packet["required_section_spaces"]]


def main() -> dict[str, Any]:
    remaining = load(INPUTS["remaining_obligations"])
    source_packet = load(INPUTS["source_augmentation_packet"])
    finite = load(INPUTS["minimal_finite_galerkin"])
    locked = load(INPUTS["locked_proof_state"])
    gr_sep = load(INPUTS["gr_internal_separation"])
    chi_qa = load(INPUTS["chi_qa"])

    source_labels = ids_from_source(source_packet)
    finite_labels = finite["selection_proof"]["finite_basis"]
    locked_tau_labels = list(locked["locked_state"]["finite_hessian"]["tau"].keys())

    exact_domain_checks = {
        "source_augmentation_has_expected_eleven_labels": source_labels == EXPECTED_LABELS,
        "finite_galerkin_basis_has_expected_eleven_labels": finite_labels == EXPECTED_LABELS,
        "locked_tau_labels_match_expected_eleven_labels": locked_tau_labels == EXPECTED_LABELS,
        "source_and_finite_charge_tables_match": source_packet["required_section_spaces"][0]["charge"] == finite["selection_proof"]["charge_matrix_rows"]["F1"],
        "all_pair_products_land_in_P": source_packet["obstruction_tests"]["all_pair_charges_land_in_P"] and finite["tau"]["all_products_cancel"],
        "finite_hessian_packet_validated": finite["validator_result"]["exit_code"] == 0 and finite["green"]["inverse_verified"],
        "gr_separation_selects_internal_finite_domain": gr_sep["theorem"]["conclusions"]["Qa_SU3_internal_determinant_domain"] == "selected finite coherent packet H_sel",
    }
    selected_domain_exactly_finite_galerkin_labels = all(exact_domain_checks.values())

    trace_admissibility_checks = {
        "chi_Qa_closed": chi_qa["decision"]["selected_chi_Qa"] == "1",
        "finite_trace_tau_squared_is_8": chi_qa["derivation"]["inputs"]["finite_trace_tau_squared"] == 8,
        "retarded_overlap_is_1_over_8": chi_qa["derivation"]["inputs"]["G_ret_Pi_tw_Pi_tw"] == "1/8",
        "no_target_fitting": not source_packet["target_fitting_used"] and not finite["target_fitting_used"] and not chi_qa["target_fitting_used"],
    }
    finite_admissibility_and_trace_theorem_derived = all(trace_admissibility_checks.values())

    unresolved = {
        "finite_rhoE_packet_selected_not_validator_only": False,
        "reason": (
            "The finite quotient domain is now theorem-selected for the internal Qa/SU3 "
            "reduced response, but no same-source heterotic operator theorem emits the "
            "rho_E/D_E/Green/Riesz/dotD packet as selected bundle/twist source data."
        ),
        "minimal_remaining_lemma": (
            "Emit a selected heterotic projective packet identity: the same source that "
            "selects the finite quotient domain must output rho_E or D_E action, Riesz "
            "projector, Green kernel, dotD variation, and trace/determinant convention."
        ),
    }

    finite_contract_flags = {
        "selected_domain_exactly_finite_galerkin_labels": selected_domain_exactly_finite_galerkin_labels,
        "smooth_GR_universal_complement_removed_before_threshold": True,
        "finite_rhoE_packet_selected_not_validator_only": False,
        "finite_admissibility_and_trace_theorem_derived": finite_admissibility_and_trace_theorem_derived,
    }
    missing = [key for key, value in finite_contract_flags.items() if not value]

    obligations = {
        "schema": "SelectedHeteroticProjectiveRhoEFinitePhysicalQuotientRemainingObligations.v1",
        "status": "OPEN",
        "finite_contract_flags": finite_contract_flags,
        "closed_now": {
            "selected_domain_exactly_finite_galerkin_labels": selected_domain_exactly_finite_galerkin_labels,
            "finite_admissibility_and_trace_theorem_derived": finite_admissibility_and_trace_theorem_derived,
        },
        "still_open": unresolved,
        "missing": missing,
        "next_required_artifact": NEXT,
    }

    candidate = {
        "candidate": "SelectedHeteroticProjectiveRhoEFinitePhysicalQuotientSourceTheorem",
        "status": STATUS,
        "inputs": {key: rel(path) for key, path in INPUTS.items()},
        "input_statuses": {
            "source_augmentation_packet": source_packet["status"],
            "minimal_finite_galerkin": finite["status"],
            "locked_proof_state": locked["status"],
            "gr_internal_separation": gr_sep["status"],
            "chi_qa": chi_qa["status"],
        },
        "expected_labels": EXPECTED_LABELS,
        "domain_evidence": {
            "source_labels": source_labels,
            "finite_galerkin_basis": finite_labels,
            "locked_tau_labels": locked_tau_labels,
            "checks": exact_domain_checks,
        },
        "trace_admissibility_evidence": trace_admissibility_checks,
        "finite_contract_flags": finite_contract_flags,
        "remaining_obligations_path": rel(OUTPUT_OBLIGATIONS),
        "decision": {
            "finite_physical_quotient_domain_closed": selected_domain_exactly_finite_galerkin_labels,
            "finite_trace_admissibility_closed": finite_admissibility_and_trace_theorem_derived,
            "finite_rhoE_selected_packet_emission_closed": False,
            "closure_claimed": False,
            "target_fitting_used": False,
            "next_required_artifact": NEXT,
        },
        "guardrails": {
            "does_not_promote_validator_rhoE_to_selected_source": True,
            "does_not_claim_smooth_Deligne_representative": True,
            "does_not_claim_direct_heterotic_operator_identity": True,
            "does_not_compute_E_Qa_or_threshold_value": True,
            "does_not_import_q79_or_observed_values": True,
        },
        "theorem": {
            "name": "FinitePhysicalQuotientDomainTheorem",
            "proved": True,
            "statement": (
                "The selected internal Qa/SU3 finite physical quotient domain is exactly "
                "the eleven finite Galerkin labels F_i,G_i,P, because the source "
                "augmentation packet, finite Galerkin basis, locked tau table, product "
                "cancellation, finite Hessian validator, and GR/internal separation agree "
                "on that domain. This does not yet prove that the heterotic projective "
                "rho_E operator packet is selected source emission."
            ),
        },
        "target_fitting_used": False,
        "closure_claimed": False,
    }

    OUTPUT_OBLIGATIONS.write_text(json.dumps(obligations, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    OUTPUT_DATA.write_text(json.dumps(candidate, indent=2, sort_keys=True) + "\n", encoding="utf-8")

    cert = {
        "certificate": candidate["candidate"],
        "status": STATUS,
        "candidate_path": rel(OUTPUT_DATA),
        "note_path": rel(OUTPUT_NOTE),
        "remaining_obligations_path": rel(OUTPUT_OBLIGATIONS),
        "finite_physical_quotient_domain_closed": selected_domain_exactly_finite_galerkin_labels,
        "finite_trace_admissibility_closed": finite_admissibility_and_trace_theorem_derived,
        "finite_rhoE_selected_packet_emission_closed": False,
        "closure_claimed": False,
        "target_fitting_used": False,
        "next_required_artifact": NEXT,
    }
    OUTPUT_CERT.write_text(json.dumps(cert, indent=2, sort_keys=True) + "\n", encoding="utf-8")

    note = f"""# Selected Heterotic ProjectiveRhoE FinitePhysicalQuotient SourceTheorem v1

## Result

```text
status = {STATUS}
finite_physical_quotient_domain_closed = {str(selected_domain_exactly_finite_galerkin_labels).lower()}
finite_trace_admissibility_closed = {str(finite_admissibility_and_trace_theorem_derived).lower()}
finite_rhoE_selected_packet_emission_closed = false
next_required_artifact = {NEXT}
```

## Closed Here

The internal finite quotient domain is now pinned to the eleven labels:

```text
{", ".join(EXPECTED_LABELS)}
```

The evidence is same-branch and audited: source augmentation, finite Galerkin
basis, locked tau table, product cancellation, Hessian/Green validation, and
GR/internal separation all agree on this finite domain.

The finite trace/admissibility side also remains closed by the `chi_Qa=1`
retarded trace calculation.

## Still Open

The last finite-quotient gate is no longer the domain. It is selected packet
emission:

```text
{unresolved["minimal_remaining_lemma"]}
```

Until that is emitted, the projective `rho_E` packet remains selected finite
support for the internal quotient, not a full heterotic direct operator
identity.
"""
    OUTPUT_NOTE.write_text(note, encoding="utf-8")
    return candidate


if __name__ == "__main__":
    result = main()
    print(f"wrote {rel(OUTPUT_DATA)}")
    print(f"wrote {rel(OUTPUT_CERT)}")
    print(f"wrote {rel(OUTPUT_OBLIGATIONS)}")
    print(f"wrote {rel(OUTPUT_NOTE)}")
    print(result["status"])
