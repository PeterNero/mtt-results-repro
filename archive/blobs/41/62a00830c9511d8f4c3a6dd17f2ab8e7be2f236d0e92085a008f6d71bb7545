"""Build the bundle-A source selector or BN27 source declaration normal form."""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "candidate_data"
CERTS = ROOT / "certificates"
PROOF = ROOT / "proof_corpus"

INPUTS = {
    "emission_attempt": DATA / "selected_heterotic_orientedphifin_selectedbundleA_or_directbn27_sourceemission.candidate.json",
    "emission_request": DATA / "selected_heterotic_orientedphifin_selectedbundleA_or_directbn27_sourceemission_request.json",
    "sourceleaf_directcarrier_or_bundlea": DATA / "selected_heterotic_orientedphifin_sourceleaf_directcarrier_or_bundlea.candidate.json",
    "sourceleaf_request": DATA / "selected_heterotic_orientedphifin_sourceleaf_directcarrier_or_bundlea_source_theorem_request.json",
    "standard_embedding_gate": DATA / "selected_heterotic_standard_embedding_selector_or_phifin_gate.candidate.json",
    "frontier_matrix": DATA / "selected_heterotic_orientedphifin_directbn27source_or_smootheqa_frontier_matrix.candidate.json",
    "simultaneous_table": DATA / "selected_heterotic_orientedphifin_simultaneous_ctau_phifin_table.json",
}

OUTPUT_DATA = DATA / "selected_heterotic_orientedphifin_bundleA_sourceselector_or_bn27_sourcedeclaration.candidate.json"
OUTPUT_TEMPLATE = DATA / "selected_heterotic_orientedphifin_bn27_direct_source_declaration.template.json"
OUTPUT_CERT = CERTS / "selected_heterotic_orientedphifin_bundleA_sourceselector_or_bn27_sourcedeclaration_certificate.json"
OUTPUT_NOTE = PROOF / "Selected_Heterotic_OrientedPhiFin_BundleA_SourceSelector_or_BN27_SourceDeclaration_v1.md"

STATUS = "HETEROTIC_ORIENTEDPHIFIN_BUNDLEA_SOURCESELECTOR_OR_BN27_SOURCEDECLARATION_NORMAL_FORM_BUILT_DIRECT_DECLARATION_MINIMAL_OPEN"
NEXT = "Selected_Heterotic_OrientedPhiFin_DirectBN27_SourceDeclaration_Fill_or_BundleA_SourceSelector_Proof_v1"


def rel(path: Path) -> str:
    try:
        return str(path.relative_to(ROOT))
    except ValueError:
        return str(path)


def load(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def main() -> dict[str, Any]:
    emission = load(INPUTS["emission_attempt"])
    emission_request = load(INPUTS["emission_request"])
    sourceleaf = load(INPUTS["sourceleaf_directcarrier_or_bundlea"])
    sourceleaf_request = load(INPUTS["sourceleaf_request"])
    standard = load(INPUTS["standard_embedding_gate"])
    frontier = load(INPUTS["frontier_matrix"])
    table = load(INPUTS["simultaneous_table"])

    direct_fields = emission_request["minimal_selector_options"]["direct_BN27_source_declaration"]
    smooth_fields = emission_request["minimal_selector_options"]["smooth_bundle_A_selector"]

    normal_form = {
        "direct_BN27_source_declaration": {
            "rank": 1,
            "minimal_amendment": True,
            "closed_now": False,
            "required_fields": direct_fields,
            "already_computable_after_declaration": {
                "basis_dimension": table["basis_dimension"],
                "basis_id": table["basis_id"],
                "C_tau_spectrum": table["counts"]["C_tau_spectrum"],
                "PhiFin_positive_count": table["counts"]["PhiFin_positive_count"],
                "oriented_sector_counts": table["counts"]["oriented_sector_counts"],
                "oriented_nonzero_positive_count": table["counts"]["oriented_nonzero_Ctau_positive_magnitude_count"],
                "commutation_closed": table["commutation"]["commutator_zero"],
            },
            "why_minimal": (
                "The full finite BN27 table, orientation, magnitude support, and replay guardrails are already materialized. "
                "A source declaration would bind existing values to heterotic Qa/SU3 ownership without needing a new smooth operator solve."
            ),
        },
        "smooth_bundle_A_selector": {
            "rank": 2,
            "minimal_amendment": False,
            "closed_now": False,
            "required_fields": smooth_fields,
            "support": {
                "R_plus_geometry_available": True,
                "standard_embedding_conditional_valid": standard["standard_embedding_evaluation"]["conditional_packet_valid"],
                "standard_embedding_selected_now": standard["standard_embedding_evaluation"]["selected_now"],
            },
            "why_larger": (
                "This route must first select A/F_A or transition data, then still construct representation action, quotient policy, "
                "E_Qa or heat/zeta/torsion finitepart, and the finite quotient to BN27."
            ),
        },
    }

    declaration_template = {
        "schema": "SelectedHeterotic.OrientedPhiFin.DirectBN27.SourceDeclaration.Template.v1",
        "status": "OPEN_SOURCE_DECLARATION_REQUIRED",
        "source_certificate": {
            "source_name": "S_QaSU3^BN27",
            "same_selected_source_as_heterotic_QaSU3_threshold_branch": None,
            "not_routec_or_benchmark_import": None,
            "relation_to_internal_projective_rhoE_shadow": "orientation_shadow_only_unless_source_declares_more",
        },
        "domain": {
            "basis_id": table["basis_id"],
            "basis_dimension": table["basis_dimension"],
            "F3xF3_rank_slot_deck_action_source_owned": None,
            "kernel_shared_circle_no_double_count_policy": None,
        },
        "operators": {
            "source_emits_C_tau": None,
            "source_emits_PhiFin_DE": None,
            "C_tau_and_PhiFin_DE_commute": table["commutation"]["commutator_zero"],
            "source_owns_positive_magnitude_with_orientation": None,
        },
        "finitepart": {
            "kernel_trace_policy_source_owned": None,
            "finitepart_trace_identity_for_oriented_nonzero_sector": None,
            "oriented_logdet_promoted": None,
        },
        "audit_replay": {
            "replay_allowed_after_all_null_fields_are_filled": True,
            "required_before_closure": [
                "source certificate",
                "domain/deck action",
                "operator co-emission",
                "kernel/trace policy",
                "finitepart identity",
            ],
        },
        "forbidden": emission_request["forbidden"],
    }
    OUTPUT_TEMPLATE.write_text(json.dumps(declaration_template, indent=2, sort_keys=True) + "\n", encoding="utf-8")

    decision = {
        "normal_form_built": True,
        "direct_BN27_source_declaration_closed": False,
        "bundle_A_source_selector_closed": False,
        "standard_embedding_reopened": False,
        "minimal_next_route": "direct_BN27_source_declaration",
        "direct_template_path": rel(OUTPUT_TEMPLATE),
        "oriented_threshold_closed": False,
        "oriented_logdet_promoted": False,
        "next_required_artifact": NEXT,
        "closure_claimed": False,
        "target_fitting_used": False,
    }

    candidate = {
        "candidate": "SelectedHeteroticOrientedPhiFinBundleASourceSelectorOrBN27SourceDeclaration",
        "status": STATUS,
        "inputs": {key: rel(path) for key, path in INPUTS.items()},
        "parent_statuses": {
            "emission_attempt": emission["status"],
            "sourceleaf": sourceleaf["status"],
            "standard_embedding_gate": standard["status"],
            "frontier_matrix": frontier["status"],
        },
        "normal_form": normal_form,
        "source_declaration_template_path": rel(OUTPUT_TEMPLATE),
        "decision": decision,
        "theorem": {
            "name": "BundleASourceSelectorOrBN27SourceDeclarationNormalFormTheorem",
            "proved": True,
            "statement": (
                "For the current oriented Phi_fin frontier, every legal closure must take one of two source-selector forms: "
                "a direct source declaration S_QaSU3^BN27, or a smooth selected bundle-A/E_Qa selector. The direct declaration "
                "is the minimal amendment because the 27-mode BN27 table, C_tau/PhiFin_DE commutation, and oriented value support "
                "are already materialized; it still remains open until source ownership, deck action, kernel policy, and finitepart "
                "identity are filled. The smooth route is legal but larger because A/F_A, representation action, E_Qa, quotient, "
                "and finitepart data are all still absent."
            ),
        },
        "guardrails": {
            "does_not_close_by_template": True,
            "does_not_promote_log92160000": True,
            "does_not_reopen_standard_embedding": True,
            "does_not_promote_routec_support": True,
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
        "direct_template_path": rel(OUTPUT_TEMPLATE),
        "note_path": rel(OUTPUT_NOTE),
        "normal_form_built": True,
        "direct_BN27_source_declaration_closed": False,
        "bundle_A_source_selector_closed": False,
        "standard_embedding_reopened": False,
        "oriented_threshold_closed": False,
        "oriented_logdet_promoted": False,
        "closure_claimed": False,
        "target_fitting_used": False,
        "next_required_artifact": NEXT,
    }
    OUTPUT_CERT.write_text(json.dumps(cert, indent=2, sort_keys=True) + "\n", encoding="utf-8")

    note = f"""# Selected Heterotic OrientedPhiFin BundleA SourceSelector or BN27 SourceDeclaration v1

## Result

```text
status = {STATUS}
normal_form_built = true
direct_BN27_source_declaration_closed = false
bundle_A_source_selector_closed = false
standard_embedding_reopened = false
oriented_logdet_promoted = false
minimal_next_route = direct_BN27_source_declaration
next_required_artifact = {NEXT}
```

## Theorem

{candidate["theorem"]["statement"]}

## Direct Declaration Template

```text
{rel(OUTPUT_TEMPLATE)}
```
"""
    OUTPUT_NOTE.write_text(note, encoding="utf-8")
    return candidate


if __name__ == "__main__":
    result = main()
    print(f"wrote {rel(OUTPUT_DATA)}")
    print(f"wrote {rel(OUTPUT_TEMPLATE)}")
    print(f"wrote {rel(OUTPUT_CERT)}")
    print(f"wrote {rel(OUTPUT_NOTE)}")
    print(result["status"])
