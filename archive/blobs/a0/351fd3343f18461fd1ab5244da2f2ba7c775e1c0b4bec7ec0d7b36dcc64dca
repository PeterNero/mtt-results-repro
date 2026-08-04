"""Attempt selected bundle A/smooth transition or direct BN27 source emission."""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "candidate_data"
CERTS = ROOT / "certificates"
PROOF = ROOT / "proof_corpus"

INPUTS = {
    "frontier_matrix": DATA / "selected_heterotic_orientedphifin_directbn27source_or_smootheqa_frontier_matrix.candidate.json",
    "payload_contract": DATA / "selected_heterotic_orientedphifin_directbn27source_or_smootheqa_payload_contract.json",
    "projective_lift_nogo": DATA / "selected_heterotic_orientedphifin_projectiverhoe_bn27lift_or_directsource_theorem.candidate.json",
    "sourceleaf_discovery": DATA / "selected_heterotic_orientedphifin_sourceleaf_corpus_discovery_report.json",
    "phifin_gate": DATA / "selected_heterotic_phifin_sourceidentity_or_bundleconnection_solve_gate.candidate.json",
    "bundle_valuesolve": DATA / "selected_heterotic_bundleconnection_valuesolve_or_phifin_sourceidentity_proof.candidate.json",
    "rplus_payload": DATA / "selected_heterotic_rplus_curvature_payload_fill.candidate.json",
    "bundle_curvature_gate": DATA / "selected_heterotic_bundle_curvature_trace_or_direct_operator_gate.candidate.json",
}

OUTPUT_DATA = DATA / "selected_heterotic_orientedphifin_selectedbundleA_or_directbn27_sourceemission.candidate.json"
OUTPUT_REQUEST = DATA / "selected_heterotic_orientedphifin_selectedbundleA_or_directbn27_sourceemission_request.json"
OUTPUT_CERT = CERTS / "selected_heterotic_orientedphifin_selectedbundleA_or_directbn27_sourceemission_certificate.json"
OUTPUT_NOTE = PROOF / "Selected_Heterotic_OrientedPhiFin_SelectedBundleA_or_DirectBN27_SourceEmission_v1.md"

STATUS = "HETEROTIC_ORIENTEDPHIFIN_SELECTEDBUNDLEA_OR_DIRECTBN27_EMISSION_ATTEMPT_REJECTS_UNSELECTED_SUBSTITUTES"
NEXT = "Selected_Heterotic_OrientedPhiFin_BundleA_SourceSelector_or_BN27_SourceDeclaration_v1"


def rel(path: Path) -> str:
    try:
        return str(path.relative_to(ROOT))
    except ValueError:
        return str(path)


def load(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def main() -> dict[str, Any]:
    frontier = load(INPUTS["frontier_matrix"])
    contract = load(INPUTS["payload_contract"])
    projective = load(INPUTS["projective_lift_nogo"])
    sourceleaf = load(INPUTS["sourceleaf_discovery"])
    phifin_gate = load(INPUTS["phifin_gate"])
    bundle = load(INPUTS["bundle_valuesolve"])
    rplus = load(INPUTS["rplus_payload"])
    curvature_gate = load(INPUTS["bundle_curvature_gate"])

    standard_embedding = curvature_gate["routes"]["A_conditional_standard_embedding"]
    rplus_summary = rplus["rplus_payload"]["R_plus_summary"]

    emission_attempts = {
        "direct_BN27_source_declaration": {
            "tested": True,
            "closes": False,
            "candidate_available": sourceleaf["classification"]["direct_selected_carrier_packet_found"],
            "reason": "No current artifact emits S_QaSU3^BN27 as a selected heterotic source.",
            "missing_contract_fields": list(contract["direct_BN27_source_payload"].keys()),
        },
        "standard_embedding_A_equals_GammaPlus": {
            "tested": True,
            "closes": False,
            "geometric_values_available": True,
            "R_plus_summary": rplus_summary,
            "why_rejected": standard_embedding["why_not_promoted"],
            "reason": "A=GammaPlus would fill a connection-shaped object, but the current source does not select the tangent-bundle standard embedding as the visible Qa/SU3 threshold bundle.",
        },
        "finite_projective_rhoE_as_smooth_transition": {
            "tested": True,
            "closes": False,
            "orientation_shadow_available": projective["lift_tests"]["domain_lift"]["orientation_shadow_passes"],
            "threshold_lift_available": projective["decision"]["projective_rhoE_BN27_lift_closed"],
            "reason": "Finite rho_E remains valid at internal 11-label scope and as orientation shadow, but it is not smooth A/F_A data and failed the BN27 threshold lift.",
        },
    }

    request = {
        "schema": "SelectedHeterotic.OrientedPhiFin.BundleA_or_DirectBN27.SourceEmissionRequest.v1",
        "status": "OPEN_SOURCE_SELECTOR_REQUIRED",
        "minimal_selector_options": {
            "smooth_bundle_A_selector": [
                "same-source theorem selecting the visible Qa/SU3 bundle or projective transition representative",
                "explicit A components or transition functions in the selected frame",
                "F_A and HYM/Strominger residual certificate",
                "representation action on u(E)-valued one-forms",
                "trace normalization and quotient/kernel policy",
                "E_Qa or heat/zeta/torsion finitepart operator",
            ],
            "direct_BN27_source_declaration": [
                "source certificate declaring S_QaSU3^BN27",
                "source-owned F3xF3 rank-slot deck action",
                "source-emitted C_tau and PhiFin_DE tables",
                "kernel/trace policy and finitepart identity",
            ],
        },
        "explicitly_rejected_substitutes": list(emission_attempts.keys()),
        "forbidden": [
            "do not use A=GammaPlus unless a same-source standard-embedding selector is proved",
            "do not reuse finite projective rho_E as smooth A/F_A",
            "do not promote Route-C BN27 values as heterotic ownership",
            "do not promote log(92160000) before source-owned kernel/trace identity",
            "do not use observed electroweak constants or residual scans",
        ],
    }
    OUTPUT_REQUEST.write_text(json.dumps(request, indent=2, sort_keys=True) + "\n", encoding="utf-8")

    decision = {
        "attempt_executed": True,
        "direct_BN27_source_emitted": False,
        "selected_bundle_A_emitted": False,
        "standard_embedding_promoted": False,
        "finite_projective_rhoE_promoted_to_smooth_A": False,
        "smooth_EQa_quotient_closed": False,
        "oriented_threshold_closed": False,
        "request_path": rel(OUTPUT_REQUEST),
        "next_required_artifact": NEXT,
        "closure_claimed": False,
        "target_fitting_used": False,
    }

    candidate = {
        "candidate": "SelectedHeteroticOrientedPhiFinSelectedBundleAOrDirectBN27SourceEmission",
        "status": STATUS,
        "inputs": {key: rel(path) for key, path in INPUTS.items()},
        "parent_statuses": {
            "frontier_matrix": frontier["status"],
            "projective_lift_nogo": projective["status"],
            "phifin_gate": phifin_gate["status"],
            "bundle_valuesolve": bundle["status"],
            "rplus_payload": rplus["status"],
            "bundle_curvature_gate": curvature_gate["status"],
        },
        "emission_attempts": emission_attempts,
        "decision": decision,
        "source_emission_request_path": rel(OUTPUT_REQUEST),
        "theorem": {
            "name": "SelectedBundleAOrDirectBN27EmissionCurrentSourceNoGoTheorem",
            "proved": True,
            "statement": (
                "The first source leaf cannot be filled from current artifacts. Direct BN27 source emission is absent. "
                "The standard-embedding substitute A=GammaPlus has real R+ geometry but no same-source selector for the "
                "visible Qa/SU3 threshold bundle. The finite projective rho_E packet remains internal 11-label data and "
                "cannot serve as smooth A/F_A after its BN27 lift failed. Therefore the next object must prove a bundle-A "
                "source selector or directly declare and emit S_QaSU3^BN27."
            ),
        },
        "guardrails": {
            "does_not_promote_standard_embedding": True,
            "does_not_promote_finite_rhoE_to_smooth_A": True,
            "does_not_promote_routec_BN27_support": True,
            "does_not_promote_log92160000": True,
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
        "direct_BN27_source_emitted": False,
        "selected_bundle_A_emitted": False,
        "standard_embedding_promoted": False,
        "finite_projective_rhoE_promoted_to_smooth_A": False,
        "closure_claimed": False,
        "target_fitting_used": False,
        "next_required_artifact": NEXT,
    }
    OUTPUT_CERT.write_text(json.dumps(cert, indent=2, sort_keys=True) + "\n", encoding="utf-8")

    note = f"""# Selected Heterotic OrientedPhiFin SelectedBundleA or DirectBN27 SourceEmission v1

## Result

```text
status = {STATUS}
direct_BN27_source_emitted = false
selected_bundle_A_emitted = false
standard_embedding_promoted = false
finite_projective_rhoE_promoted_to_smooth_A = false
next_required_artifact = {NEXT}
```

## Theorem

{candidate["theorem"]["statement"]}

## Source Request

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
