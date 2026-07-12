"""Build the next exact request for typed maps or projective rho_E tables."""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "candidate_data"
CERTS = ROOT / "certificates"
PROOF = ROOT / "proof_corpus"

INPUT_FILL = DATA / "selected_heterotic_typedcechende_basis_or_projectiverhoe_fill_attempt.candidate.json"
INPUT_SOURCE_AUG = DATA / "source_augmentation_iwasawa_monad_maps_fill_attempt.candidate.json"
INPUT_TWISTED = DATA / "twisted_source_promotion_packet_fill_attempt.candidate.json"
INPUT_CENTRAL = DATA / "central_cocycle_map_source_search_or_derivation.candidate.json"

OUTPUT_DATA = DATA / "selected_heterotic_sourceaugmented_typedmaps_or_projectiverhoe_tables_request.candidate.json"
OUTPUT_CERT = CERTS / "selected_heterotic_sourceaugmented_typedmaps_or_projectiverhoe_tables_request_certificate.json"
OUTPUT_NOTE = PROOF / "Selected_Heterotic_SourceAugmented_TypedMaps_or_ProjectiveRhoE_Tables_Request_v1.md"

STATUS = "HETEROTIC_SOURCEAUGMENTED_TYPEDMAPS_OR_PROJECTIVERHOE_TABLES_REQUEST_BUILT_VALUES_OPEN"
NEXT = "Selected_Heterotic_TypedMapTables_or_ProjectiveRhoETables_SourceFill_v1"


def rel(path: Path) -> str:
    try:
        return str(path.relative_to(ROOT))
    except ValueError:
        return str(path)


def load(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def null_tree(value: Any) -> bool:
    if value is None:
        return True
    if isinstance(value, dict):
        return all(null_tree(item) for item in value.values())
    if isinstance(value, list):
        return all(null_tree(item) for item in value)
    return False


def main() -> dict[str, Any]:
    fill = load(INPUT_FILL)
    source_aug = load(INPUT_SOURCE_AUG)
    twisted = load(INPUT_TWISTED)
    central = load(INPUT_CENTRAL)

    monad_spaces = source_aug["partial_packet"]["section_spaces"]["spaces"]
    monad_hard_blockers = source_aug["hard_blockers"]
    twisted_partial = twisted["partial_packet"]

    typed_payload = {
        "lane": "source_augmented_typed_monad_Cech_EndE",
        "purpose": "Emit a machine-checkable selected End(E) domain basis from the same heterotic Iwasawa SU(3) monad source.",
        "source_branch": fill["decision"]["next_required_artifact"],
        "required_tables": {
            "cover_or_finite_domain": None,
            "lattice_generators_and_complex_coordinate_action": {
                "lattice_generators": monad_hard_blockers["lattice_generators"],
                "complex_coordinate_action": monad_hard_blockers["complex_coordinate_action"],
            },
            "factor_of_automorphy": {
                "charge_to_factor_map": monad_hard_blockers["charge_to_factor_map"],
                "cocycle_checked": monad_hard_blockers["cocycle_checked"],
                "c1_charge_realization_checked": monad_hard_blockers["c1_charge_realization_checked"],
            },
            "section_spaces": [
                {
                    "id": space["id"],
                    "charge": space["charge"],
                    "dimension": monad_hard_blockers["section_dimensions"][space["id"]],
                    "basis": monad_hard_blockers["section_bases"][space["id"]],
                }
                for space in monad_spaces
            ],
            "product_constants": monad_hard_blockers["product_constants"],
            "f_coefficients": monad_hard_blockers["f_coefficients"],
            "g_coefficients": monad_hard_blockers["g_coefficients"],
            "g_f_zero_machine_check": None,
            "exactness_or_local_freeness_certificate": None,
            "EndE_cochain_or_harmonic_basis": None,
            "trace_inner_product_and_shared_line_policy": None,
            "finite_operator_exit": monad_hard_blockers["operator_exit"],
        },
        "acceptance_equations": [
            "a_{q+r}(gamma,z) = a_q(gamma,z) a_r(gamma,z) for all printed charges q,r used in products",
            "s_i(gamma.z) = a_{q_i}(gamma,z) s_i(z) for every section basis element",
            "g o f = sum_i g_i f_i = 0 in the printed P section basis",
            "the chosen f,g define a locally free rank-three monad bundle E",
            "End(E) basis/cochains are computed from the same f,g packet",
            "the trace pairing and shared-line quotient policy are fixed before any electroweak comparison",
        ],
        "filled_now": False,
    }

    projective_payload = {
        "lane": "source_augmented_projective_rhoE_tables",
        "purpose": "Emit selected nonidentity projective rho_E transition tables from the same heterotic gerbe/twisted source.",
        "required_tables": {
            "selected_Deligne_Cech_or_B_field_representative": twisted_partial["source_evidence"]["Deligne_Cech_or_B_field_representative"],
            "period_denominator_or_smooth_unit": twisted_partial["source_evidence"]["period_denominator_or_smooth_unit"],
            "representative_to_central_cocycle_map": twisted_partial["source_evidence"]["map_to_central_cocycle_verified"],
            "rho_E_generator_or_boundary_matrices": twisted_partial["projective_rhoE"]["projective_mesh_tables"],
            "central_corner_cocycle": twisted_partial["projective_rhoE"]["central_corner_cocycle"],
            "nontrivial_central_twist": twisted_partial["projective_rhoE"]["nontrivial_central_twist"],
            "metric_or_unitarity_compatibility": twisted_partial["projective_rhoE"]["metric_compatibility"],
            "sector_or_QaSU3_domain_maps": twisted_partial["projective_rhoE"]["sector_maps"],
            "Freed_Witten_and_Bianchi_checks": {
                "Freed_Witten_verified": twisted_partial["admissibility"]["Freed_Witten_verified"],
                "Green_Schwarz_Bianchi_verified": twisted_partial["admissibility"]["Green_Schwarz_Bianchi_verified"],
                "twisted_projector_retains_sector": twisted_partial["admissibility"]["twisted_projector_retains_sector"],
            },
            "finite_response": twisted_partial["operator_response"],
        },
        "acceptance_equations": [
            "rho_E(gamma) rho_E(delta) = zeta^{tau(gamma,delta)} rho_E(gamma delta)",
            "tau is extracted from the selected representative, not imported from q79/S3",
            "rho_E is nonidentity and not simultaneously pure gauge on the retained sector",
            "metric/unitarity, Bianchi, Freed-Witten, and projector checks use the same tau",
            "D_E, dotD, Riesz/Green, heat/zeta, or torsion finite response is computed from the same rho_E packet",
        ],
        "filled_now": False,
    }

    request = {
        "candidate": "SelectedHeteroticSourceAugmentedTypedMapsOrProjectiveRhoETablesRequest",
        "status": STATUS,
        "inputs": {
            "typed_or_projective_fill_attempt": rel(INPUT_FILL),
            "source_augmentation_iwasawa_monad_maps_fill_attempt": rel(INPUT_SOURCE_AUG),
            "twisted_source_promotion_packet_fill_attempt": rel(INPUT_TWISTED),
            "central_cocycle_map_source_search_or_derivation": rel(INPUT_CENTRAL),
        },
        "input_statuses": {
            "typed_or_projective_fill_attempt": fill["status"],
            "source_augmentation": source_aug["status"],
            "twisted_source": twisted["status"],
            "central_cocycle": central["status"],
        },
        "typed_payload": typed_payload,
        "projective_payload": projective_payload,
        "current_source_audit": {
            "typed_required_null_or_open": null_tree(typed_payload["required_tables"]),
            "projective_required_null_or_open": null_tree(
                {
                    key: value
                    for key, value in projective_payload["required_tables"].items()
                    if key != "central_corner_cocycle"
                }
            ),
            "q79_guardrail_only": central["source_search_result"]["q79_guardrail_packet_found"],
            "same_branch_hessian_language_found": central["source_search_result"]["same_branch_hessian_language_found"],
            "selected_Qa_SU3_source_packet_found": central["source_search_result"]["selected_Qa_SU3_source_packet_found"],
            "response_payload_found": central["source_search_result"]["response_payload_found"],
        },
        "decision": {
            "request_built": True,
            "typed_tables_emitted": False,
            "projective_rhoE_tables_emitted": False,
            "legal_next_artifact": NEXT,
            "closure_claimed": False,
            "E_Qa_computed": False,
            "threshold_value_computed": False,
            "target_fitting_used": False,
        },
        "guardrails": {
            "no_observed_electroweak_inputs": True,
            "no_q79_value_import": True,
            "no_identity_rhoE": True,
            "no_generic_existence_promotion": True,
            "no_topology_as_operator_basis": True,
            "no_validator_as_source": True,
        },
        "theorem": {
            "name": "HeteroticSourceAugmentedFirstValueRequestCompleteness",
            "proved": True,
            "statement": (
                "For the current source record, any legal next closure must emit either "
                "the typed monad/Cech tables listed in typed_payload or the selected "
                "projective rho_E tables listed in projective_payload. No downstream "
                "End(E)->B_N, E_Qa, or electroweak threshold value may be promoted until "
                "one lane supplies those tables from the same selected source."
            ),
        },
    }

    OUTPUT_DATA.write_text(json.dumps(request, indent=2, sort_keys=True) + "\n", encoding="utf-8")

    cert = {
        "certificate": request["candidate"],
        "status": STATUS,
        "candidate_path": rel(OUTPUT_DATA),
        "note_path": rel(OUTPUT_NOTE),
        "typed_tables_emitted": False,
        "projective_rhoE_tables_emitted": False,
        "closure_claimed": False,
        "legal_next_artifact": NEXT,
        "target_fitting_used": False,
    }
    OUTPUT_CERT.write_text(json.dumps(cert, indent=2, sort_keys=True) + "\n", encoding="utf-8")

    note = f"""# Selected Heterotic SourceAugmented TypedMaps or ProjectiveRhoE Tables Request v1

## Result

```text
status = {STATUS}
typed_tables_emitted = false
projective_rhoE_tables_emitted = false
E_Qa_computed = false
threshold_value_computed = false
legal_next_artifact = {NEXT}
```

## The Exact Fork

The previous fill attempt is now turned into a concrete source request. There
are only two legal first-value lanes:

1. source-augmented typed monad/Cech tables for the selected `End(E)` domain;
2. selected nonidentity projective `rho_E` tables with the representative-to-
   central-cocycle map and same-source finite response.

## Typed/Cech Payload

```json
{json.dumps(typed_payload, indent=2, sort_keys=True)}
```

## Projective rhoE Payload

```json
{json.dumps(projective_payload, indent=2, sort_keys=True)}
```

## Guardrail Theorem

For the current source record, no `End(E)->B_N`, `E_Qa`, or electroweak
threshold value may promote until one of these two payloads is source-filled.
Topology, generic map existence, q79/S3 validator data, and identity `rho_E`
remain non-values for this branch.
"""
    OUTPUT_NOTE.write_text(note, encoding="utf-8")
    return request


if __name__ == "__main__":
    result = main()
    print(f"wrote {rel(OUTPUT_DATA)}")
    print(f"wrote {rel(OUTPUT_CERT)}")
    print(f"wrote {rel(OUTPUT_NOTE)}")
    print(result["status"])
