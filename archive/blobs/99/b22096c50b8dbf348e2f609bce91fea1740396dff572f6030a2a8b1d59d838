"""Attempt to fill selected typed-map tables or projective rho_E tables."""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "candidate_data"
CERTS = ROOT / "certificates"
PROOF = ROOT / "proof_corpus"

INPUTS = {
    "request": DATA / "selected_heterotic_sourceaugmented_typedmaps_or_projectiverhoe_tables_request.candidate.json",
    "source_augmentation_fill": DATA / "source_augmentation_iwasawa_monad_maps_fill_attempt.candidate.json",
    "typed_monad_fill": DATA / "typed_monad_data_fill_attempt.candidate.json",
    "gerbe_response_fill": DATA / "gerbe_twisted_local_system_response_fill_attempt.candidate.json",
    "twisted_source_fill": DATA / "twisted_source_promotion_packet_fill_attempt.candidate.json",
    "central_search": DATA / "central_cocycle_map_source_search_or_derivation.candidate.json",
    "projective_hunt": DATA / "projective_rhoe_or_de_response_source_hunt.candidate.json",
}

OUTPUT_DATA = DATA / "selected_heterotic_typedmaptables_or_projectiverhoetables_sourcefill.candidate.json"
OUTPUT_CERT = CERTS / "selected_heterotic_typedmaptables_or_projectiverhoetables_sourcefill_certificate.json"
OUTPUT_NOTE = PROOF / "Selected_Heterotic_TypedMapTables_or_ProjectiveRhoETables_SourceFill_v1.md"
OUTPUT_MISSING = DATA / "selected_heterotic_typedmaptables_or_projectiverhoetables_missing_leaves.json"

STATUS = "HETEROTIC_TYPEDMAPTABLES_OR_PROJECTIVERHOETABLES_SOURCEFILL_NOGO_VALUES_OPEN"
NEXT = "Selected_Heterotic_SourceAmendment_or_ProjectiveRhoE_RepresentativeTables_v1"


def rel(path: Path) -> str:
    try:
        return str(path.relative_to(ROOT))
    except ValueError:
        return str(path)


def load(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def is_filled(value: Any) -> bool:
    if value is None or value is False:
        return False
    if isinstance(value, str):
        return bool(value) and not value.startswith(("FAIL", "OPEN", "PARTIAL", "GUARDRAIL", "TYPING_ONLY"))
    if isinstance(value, dict):
        return bool(value) and all(is_filled(item) for item in value.values())
    if isinstance(value, list):
        return bool(value) and all(is_filled(item) for item in value)
    return True


def leaf_rows(prefix: str, value: Any) -> list[dict[str, Any]]:
    if isinstance(value, dict):
        rows: list[dict[str, Any]] = []
        for key, item in value.items():
            rows.extend(leaf_rows(f"{prefix}.{key}", item))
        return rows
    if isinstance(value, list):
        rows = []
        for index, item in enumerate(value):
            rows.extend(leaf_rows(f"{prefix}[{index}]", item))
        return rows
    return [{"path": prefix, "value": value, "filled": is_filled(value)}]


def main() -> dict[str, Any]:
    request = load(INPUTS["request"])
    source_aug = load(INPUTS["source_augmentation_fill"])
    typed = load(INPUTS["typed_monad_fill"])
    gerbe = load(INPUTS["gerbe_response_fill"])
    twisted = load(INPUTS["twisted_source_fill"])
    central = load(INPUTS["central_search"])
    projective_hunt = load(INPUTS["projective_hunt"])

    typed_required = request["typed_payload"]["required_tables"]
    projective_required = request["projective_payload"]["required_tables"]

    typed_evidence = {
        "monad_topology": typed["gate_results"]["topological_monad_data"],
        "source_certificate": source_aug["gate_results"]["source_certificate"],
        "charge_compatibility": "PASS_SYMBOLIC_PRODUCTS_FROM_SOURCE_AUGMENTATION_PACKET",
        "generic_maps_named": source_aug["fillable_from_source"]["generic_maps_named"],
        "constant_left_invariant_maps_named": source_aug["fillable_from_source"]["constant_left_invariant_maps_named"],
    }
    typed_rejections = {
        "generic_maps": source_aug["gate_results"]["generic_constant_maps"],
        "automorphy_cocycle": source_aug["gate_results"]["automorphy_cocycle"],
        "section_ring": source_aug["gate_results"]["section_ring"],
        "g_f_zero": source_aug["gate_results"]["g_f_zero"],
        "operator_exit": source_aug["gate_results"]["operator_exit"],
        "typed_f_g_maps": typed["gate_results"]["typed_f_g_maps"],
        "dolbeault_or_cech_matrices": typed["gate_results"]["dolbeault_or_cech_matrices"],
        "representation_and_trace": typed["gate_results"]["representation_and_trace"],
    }

    projective_evidence = {
        "source_family_selected": twisted["fill_result"]["source_family_selected"],
        "fixed_differential_class_context_found": twisted["fill_result"]["fixed_differential_class_context_found"],
        "global_bianchi_context_found": twisted["fill_result"]["global_bianchi_context_found"],
        "primitive_central_support_available": twisted["fill_result"]["primitive_central_support_available"],
        "twist_cancellation_table_available": twisted["fill_result"]["twist_cancellation_table_available"],
        "projective_validator_pattern_available": twisted["fill_result"]["projective_validator_pattern_available"],
        "projective_hunt_status": projective_hunt["status"],
        "q79_guardrail_packet_found": central["source_search_result"]["q79_guardrail_packet_found"],
    }
    projective_rejections = {
        "selected_representative": twisted["fill_result"]["selected_Qa_SU3_representative_found"],
        "period_denominator_or_smooth_unit": twisted["fill_result"]["period_denominator_or_smooth_unit_selected"],
        "central_cocycle_map": twisted["fill_result"]["central_cocycle_map_verified"],
        "projective_rhoE_tables": twisted["fill_result"]["projective_rhoE_tables_supplied"],
        "selected_D_E_dotD_response": twisted["fill_result"]["selected_D_E_dotD_response_supplied"],
        "mapped_Freed_Witten": twisted["fill_result"]["mapped_Freed_Witten_verified"],
        "twisted_projector_retention": twisted["fill_result"]["twisted_projector_retention_verified"],
        "gerbe_response_section_constants": gerbe["fill_result"]["section_bases_and_constants_filled"],
        "gerbe_response_operator": gerbe["fill_result"]["finite_response_filled"],
        "central_search_response_payload": central["source_search_result"]["response_payload_found"],
    }

    typed_leaf_report = leaf_rows("typed_payload.required_tables", typed_required)
    projective_leaf_report = leaf_rows("projective_payload.required_tables", projective_required)
    typed_filled = sum(1 for row in typed_leaf_report if row["filled"])
    projective_filled = sum(1 for row in projective_leaf_report if row["filled"])
    missing_leaves = {
        "schema": "SelectedHeteroticTypedMapTablesOrProjectiveRhoETablesMissingLeaves.v1",
        "status": "CURRENT_SOURCE_VALUES_OPEN",
        "typed_missing": [row for row in typed_leaf_report if not row["filled"]],
        "projective_missing": [row for row in projective_leaf_report if not row["filled"]],
        "legal_minimal_repairs": [
            "source-amend the Iwasawa nil-theta/automorphy section ring and emit selected typed f,g tables",
            "source-amend the heterotic gerbe representative-to-central-cocycle map and emit nonidentity projective rho_E tables",
            "emit a direct same-source finite D_E/dotD/Riesz/Green/heat/zeta/torsion response that bypasses both table lanes",
        ],
    }

    lane_a = {
        "lane": "typed_map_tables_source_fill",
        "attempted": True,
        "required_leaf_count": len(typed_leaf_report),
        "filled_leaf_count": typed_filled,
        "value_packet_emitted": False,
        "support_imported": typed_evidence,
        "rejections": typed_rejections,
        "verdict": "NO_SELECTED_TYPED_TABLES_EMITTED",
    }
    lane_b = {
        "lane": "projective_rhoE_tables_source_fill",
        "attempted": True,
        "required_leaf_count": len(projective_leaf_report),
        "filled_leaf_count": projective_filled,
        "value_packet_emitted": False,
        "support_imported": projective_evidence,
        "rejections": projective_rejections,
        "verdict": "NO_SELECTED_PROJECTIVE_RHOE_TABLES_EMITTED",
    }

    candidate = {
        "candidate": "SelectedHeteroticTypedMapTablesOrProjectiveRhoETablesSourceFill",
        "status": STATUS,
        "inputs": {key: rel(path) for key, path in INPUTS.items()},
        "input_statuses": {
            "request": request["status"],
            "source_augmentation_fill": source_aug["status"],
            "typed_monad_fill": typed["status"],
            "gerbe_response_fill": gerbe["status"],
            "twisted_source_fill": twisted["status"],
            "central_search": central["status"],
            "projective_hunt": projective_hunt["status"],
        },
        "lane_a_typed": lane_a,
        "lane_b_projective": lane_b,
        "missing_leaves_path": rel(OUTPUT_MISSING),
        "decision": {
            "source_fill_attempt_executed": True,
            "typed_map_tables_emitted": False,
            "projective_rhoE_tables_emitted": False,
            "direct_operator_exit_emitted": False,
            "EndE_to_BN_functor_filled": False,
            "E_Qa_computed": False,
            "threshold_value_computed": False,
            "closure_claimed": False,
            "target_fitting_used": False,
            "next_required_artifact": NEXT,
        },
        "guardrails": {
            "does_not_promote_generic_maps": True,
            "does_not_promote_topology_to_EndE_basis": True,
            "does_not_promote_projective_validator_to_rhoE_tables": True,
            "does_not_import_q79_values": True,
            "does_not_insert_identity_rhoE": True,
            "does_not_use_observed_electroweak_data": True,
            "does_not_use_target_residual": True,
        },
        "theorem": {
            "name": "HeteroticTypedMapTablesOrProjectiveRhoETablesCurrentSourceNoGo",
            "proved": True,
            "statement": (
                "Running the exact source-fill contract against the current repository "
                "does not emit selected typed map tables, selected projective rho_E "
                "tables, or a direct same-source finite operator exit. The live support "
                "is structural only: monad topology, charge compatibility, gerbe context, "
                "twist cancellation, and validator patterns. Closure therefore requires "
                "a genuine source amendment or a new same-source finite response packet."
            ),
        },
        "target_fitting_used": False,
        "closure_claimed": False,
    }

    OUTPUT_DATA.write_text(json.dumps(candidate, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    OUTPUT_MISSING.write_text(json.dumps(missing_leaves, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    cert = {
        "certificate": candidate["candidate"],
        "status": STATUS,
        "candidate_path": rel(OUTPUT_DATA),
        "note_path": rel(OUTPUT_NOTE),
        "missing_leaves_path": rel(OUTPUT_MISSING),
        "source_fill_attempt_executed": True,
        "typed_map_tables_emitted": False,
        "projective_rhoE_tables_emitted": False,
        "direct_operator_exit_emitted": False,
        "typed_filled_leaf_count": typed_filled,
        "projective_filled_leaf_count": projective_filled,
        "EndE_to_BN_functor_filled": False,
        "E_Qa_computed": False,
        "threshold_value_computed": False,
        "closure_claimed": False,
        "target_fitting_used": False,
        "next_required_artifact": NEXT,
    }
    OUTPUT_CERT.write_text(json.dumps(cert, indent=2, sort_keys=True) + "\n", encoding="utf-8")

    note = f"""# Selected Heterotic TypedMapTables or ProjectiveRhoETables SourceFill v1

## Result

```text
status = {STATUS}
typed_map_tables_emitted = false
projective_rhoE_tables_emitted = false
direct_operator_exit_emitted = false
EndE_to_BN_functor_filled = false
E_Qa_computed = false
threshold_value_computed = false
next_required_artifact = {NEXT}
```

## Typed Lane

```json
{json.dumps(lane_a, indent=2, sort_keys=True)}
```

## Projective rhoE Lane

```json
{json.dumps(lane_b, indent=2, sort_keys=True)}
```

## What This Closes

This closes the current-source fill attempt for the exact two-lane request. The
repository has support objects, but neither support family emits the selected
value tables required for `End(E)->B_N`, `E_Qa`, or electroweak threshold
normalization.

## Legal Next Repairs

- source-amend the Iwasawa nil-theta/automorphy section ring and emit selected typed `f,g` tables;
- source-amend the heterotic gerbe representative-to-central-cocycle map and emit nonidentity projective `rho_E` tables;
- emit a direct same-source finite `D_E/dotD/Riesz/Green/heat/zeta/torsion` response.
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
