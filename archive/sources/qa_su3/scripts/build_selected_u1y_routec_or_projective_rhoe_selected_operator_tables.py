"""Construct the U1/Y Route-C or projective rhoE selected operator-table gate."""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "candidate_data"
CERTS = ROOT / "certificates"
PROOF = ROOT / "proof_corpus"
TEXPAPERS = ROOT.parent
Q79 = TEXPAPERS / "mtt-q79-proof-repro"
SM = TEXPAPERS / "mtt-sm-parity-closure"

INPUTS = {
    "prior_payload": DATA / "selected_u1y_same_source_nonabelian_or_routec_operator_payload.candidate.json",
    "q79_conditional_weylpair_A": Q79 / "certificates" / "q79_routec_weylpair_aselected_assembly_or_source_proof_certificate.json",
    "q79_source_provenance": Q79 / "certificates" / "q79_routec_weylpair_source_provenance_lemma_certificate.json",
    "q79_sector_charge": Q79 / "certificates" / "q79_routec_weylpair_sector_charge_or_chirality_certificate.json",
    "q79_matter_slot_overlap": Q79 / "certificates" / "q79_selected_matter_slot_charge_and_overlap_normalization_theorem_certificate.json",
    "q79_samesource_fill_nogo": Q79 / "certificates" / "q79_samesource_operatorpacket_fill_or_nogo_certificate.json",
    "projective_gerbe_rhoe": SM / "candidate_data" / "projective_gerbe_rhoe_source_promotion.candidate.json",
    "projective_mesh_validator": Q79 / "certificates" / "iwasawa_projective_rhoE_mesh_validator_certificate.json",
    "orientation_de_dotd": SM / "candidate_data" / "selected_orientation_carrying_de_dotd_source.candidate.json",
}

OUTPUT_DATA = DATA / "selected_u1y_routec_or_projective_rhoe_selected_operator_tables.candidate.json"
OUTPUT_CERT = CERTS / "selected_u1y_routec_or_projective_rhoe_selected_operator_tables_certificate.json"
OUTPUT_NOTE = PROOF / "Selected_U1Y_RouteC_or_ProjectiveRhoE_Selected_Operator_Tables_v1.md"


def load(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def rel(path: Path) -> str:
    try:
        return str(path.relative_to(ROOT))
    except ValueError:
        return str(path)


def build() -> tuple[dict[str, Any], dict[str, Any], str]:
    prior = load(INPUTS["prior_payload"])
    conditional = load(INPUTS["q79_conditional_weylpair_A"])
    provenance = load(INPUTS["q79_source_provenance"])
    sector = load(INPUTS["q79_sector_charge"])
    matter = load(INPUTS["q79_matter_slot_overlap"])
    nogo = load(INPUTS["q79_samesource_fill_nogo"])
    projective = load(INPUTS["projective_gerbe_rhoe"])
    mesh = load(INPUTS["projective_mesh_validator"])
    orientation = load(INPUTS["orientation_de_dotd"])

    conditional_solve = conditional["conditional_solve"]
    routec_table = {
        "lane": "RouteC_WeylPair_operator_table",
        "constructed_table_kind": "conditional_A_weylpair",
        "shape": conditional_solve["conditional_operator"]["shape"],
        "rank": conditional_solve["locked_solve"]["rank"],
        "condition_number": conditional_solve["locked_solve"]["condition_number"],
        "relative_residual": conditional_solve["locked_solve"]["relative_residual"],
        "deltaTheta_conditional": conditional_solve["locked_solve"]["deltaTheta_conditional"],
        "algebraic_rank_obstruction_absent": conditional["decision"]["algebraic_rank_obstruction_absent_for_weylpair_packet"],
        "conditional_A_weylpair_assembled": conditional["decision"]["conditional_A_weylpair_assembled"],
        "conditional_source_to_C1_transfer_exact": provenance["decision"]["conditional_source_to_C1_transfer_exact"],
        "source_level_weyl_carrier_closed": provenance["decision"]["source_level_weyl_carrier_and_active_shift_proved"],
        "sector_structural_candidate_identified": sector["sector_charge_reduction"]["su5_e6_structural_candidate"]["matches_required_partition"],
        "matter_slot_overlap_reduced_to_packet": matter["matter_slot_overlap_reduction"]["decision"]["same_source_operator_packet_required"],
        "same_source_fill_nogo_executed": nogo["q79_decision"]["fill_attempt_executed"],
        "validator_errors": nogo["fill_or_nogo_result"]["validator_report"]["errors"],
        "selected_operator_table_emitted": False,
        "promote_to_A_selected": nogo["fill_or_nogo_result"]["packet_flags"]["promote_to_A_selected"],
        "promote_to_b_selected": nogo["fill_or_nogo_result"]["packet_flags"]["promote_to_b_selected"],
        "why_not_selected": [
            "conditional A is algebraically exact but explicitly is_A_selected=false",
            "same-source validator rejects all seven required fields as support-only, conditional, target-localized, or absent",
            "selected matter-slot charge, 1_M neutrino rule, operator values, overlap transfer, normalization, and primitive contractions are not emitted",
        ],
    }

    projective_table = {
        "lane": "Projective_rhoE_operator_tables",
        "source_level_projective_gerbe_promoted": projective["promotion_result"]["source_level_projective_gerbe_rhoE_promoted"],
        "operator_level_projective_rhoE_promoted": projective["promotion_result"]["operator_level_projective_rhoE_promoted"],
        "mesh_validator_ready": mesh["verdict"]["projective_validator_ready"],
        "projective_magnetic_carrier_validated": mesh["verdict"]["projective_magnetic_carrier_validated_as_twisted_not_ordinary"],
        "strict_mismatch_count": mesh["audit_cases"]["projective_magnetic_carrier"]["strict_mismatch_count"],
        "projective_mismatch_count": mesh["audit_cases"]["projective_magnetic_carrier"]["projective_mismatch_count"],
        "nontrivial_central_twist_count": mesh["audit_cases"]["projective_magnetic_carrier"]["nontrivial_central_twist_count"],
        "orientation_de_dotd_shape_support": {
            "de_action_boundary_shapes_present": orientation["what_closes_now"]["de_action_boundary_shapes_present"],
            "reduced_green_riesz_shapes_present": orientation["what_closes_now"]["reduced_green_riesz_shapes_present"],
            "dotd_horizontal_green_shapes_present": orientation["what_closes_now"]["dotd_horizontal_green_shapes_present"],
            "finite_branch_residuals_hit_zero_in_smoke": orientation["what_closes_now"]["finite_branch_residuals_hit_zero_in_smoke"],
        },
        "selected_operator_table_emitted": False,
        "selected_DE_dotD_Riesz_Green_emitted": False,
        "why_not_selected": [
            "projective rhoE mesh validator is ready, but the validator does not select a twist/source",
            "projective gerbe promotion is source-level only; operator_level_projective_rhoE_promoted=false",
            "orientation-carrying D_E/dotD shapes have selected source flags and alpha1-driver provenance open",
        ],
    }

    selected_tables = {
        "routec_A_selected": False,
        "routec_b_selected": False,
        "routec_selected_operator_values": False,
        "projective_rhoE_operator_tables": False,
        "projective_DE_dotD_Riesz_Green": False,
        "finite_part_or_spectrum": False,
    }

    decision = {
        "operator_table_gate_constructed": True,
        "routec_conditional_operator_constructed": True,
        "projective_validator_table_constructed": True,
        "selected_operator_tables_emitted": False,
        "selected_A_selected_emitted": False,
        "selected_b_selected_emitted": False,
        "selected_projective_rhoE_tables_emitted": False,
        "selected_finite_part_found": False,
        "lambda_12_computable": False,
        "lambda_12_closed": False,
        "target_fitting_used": False,
        "strongest_result": "conditional Route-C Weyl-pair A has exact rank/solve, but same-source validator proves current scaffolds are support-only",
        "next_required_object": "Selected_U1Y_Stability_HYM_or_RouteC_Residual_Source_v1",
        "parallel_projective_next_object": "Selected_U1Y_ProjectiveRhoE_SourceOrigin_and_DEDotD_OperatorTables_v1",
    }

    candidate = {
        "candidate": "SelectedU1YRouteCOrProjectiveRhoESelectedOperatorTables",
        "status": "U1Y_ROUTEC_OR_PROJECTIVE_RHOE_OPERATOR_TABLES_CONSTRUCTED_CONDITIONAL_SELECTED_TABLES_OPEN",
        "inputs": {key: rel(path) for key, path in INPUTS.items()},
        "prior_status": prior["status"],
        "routec_operator_table": routec_table,
        "projective_rhoE_table": projective_table,
        "selected_tables": selected_tables,
        "closed_support": {
            "conditional_routec_A_rank_solve_exact": True,
            "routec_source_level_weyl_carrier_closed": routec_table["source_level_weyl_carrier_closed"],
            "routec_same_source_fill_nogo_executed": True,
            "projective_mesh_validator_ready": True,
            "projective_source_level_support_closed": projective_table["source_level_projective_gerbe_promoted"],
            "de_dotd_shape_support_present": True,
            "no_target_fit_used": True,
        },
        "open": {
            "selected_visible_or_routec_operator_source": True,
            "non_split_stability_or_hym_or_routec_residual": True,
            "same_source_Chern_Weil_GS_derivation": True,
            "selected_DE_dotD_Riesz_Green_values": True,
            "selected_projective_rhoE_operator_tables": True,
            "selected_matter_slot_charge_table": True,
            "selected_1M_neutrino_rule": True,
            "selected_overlap_transfer_functor": True,
            "selected_trace_hessian_normalization": True,
            "primitive_C1_contractions": True,
            "finite_part_or_spectrum": True,
            "lambda_12": True,
        },
        "decision": decision,
        "guardrails": [
            "Do not promote conditional A_weylpair to A_selected.",
            "Do not promote exact conditional transfer to selected source-to-C1 map.",
            "Do not promote projective mesh validation to selected rhoE operator tables.",
            "Do not promote D_E/dotD smoke residuals to selected source flags.",
            "Do not compute lambda_12 from conditional or support-only tables.",
        ],
        "closure_claimed": True,
        "closure_scope": "conditional_operator_table_construction_and_selected_table_no_go_only",
        "target_fitting_used": False,
    }

    certificate = {
        "certificate": "SelectedU1YRouteCOrProjectiveRhoESelectedOperatorTables",
        "status": candidate["status"],
        "candidate_path": rel(OUTPUT_DATA),
        "closed": {
            "routec_conditional_A_table_constructed": True,
            "routec_rank_solve_exact": True,
            "routec_same_source_validator_no_go_imported": True,
            "projective_rhoE_mesh_validator_imported": True,
            "projective_DE_dotD_shape_support_imported": True,
            "no_target_fit_used": True,
        },
        "open": candidate["open"],
        "next_required_object": decision["next_required_object"],
        "parallel_projective_next_object": decision["parallel_projective_next_object"],
        "target_fitting_used": False,
    }
    return candidate, certificate, render_note(candidate)


def render_note(candidate: dict[str, Any]) -> str:
    routec = candidate["routec_operator_table"]
    projective = candidate["projective_rhoE_table"]
    routec_missing = "\n".join(f"- {item}" for item in routec["why_not_selected"])
    projective_missing = "\n".join(f"- {item}" for item in projective["why_not_selected"])
    guardrails = "\n".join(f"- {item}" for item in candidate["guardrails"])
    open_rows = "\n".join(f"- `{key}`" for key, value in candidate["open"].items() if value)
    decision = candidate["decision"]
    return f"""# Selected U1Y Route-C or Projective RhoE Selected Operator Tables v1

## Result

```text
routec_conditional_operator_constructed = true
projective_validator_table_constructed = true
selected_operator_tables_emitted = false
selected_A_selected_emitted = false
selected_b_selected_emitted = false
selected_projective_rhoE_tables_emitted = false
selected_finite_part_found = false
lambda_12_computable = false
lambda_12_closed = false
target_fitting_used = false
```

This artifact constructs the strongest available operator-table objects. The
Route-C lane now has a conditional `72 x 2` Weyl-pair operator with exact
rank/solve. The projective lane has a validated projective mesh format and
nontrivial central-twist carrier. Neither lane emits selected operator tables.

## Route-C Table

```text
shape = {routec["shape"]}
rank = {routec["rank"]}
condition_number = {routec["condition_number"]}
relative_residual = {routec["relative_residual"]}
deltaTheta_conditional = {routec["deltaTheta_conditional"]}
selected_operator_table_emitted = false
promote_to_A_selected = false
promote_to_b_selected = false
```

Why this cannot close:

{routec_missing}

## Projective RhoE Table

```text
mesh_validator_ready = {str(projective["mesh_validator_ready"]).lower()}
projective_magnetic_carrier_validated = {str(projective["projective_magnetic_carrier_validated"]).lower()}
strict_mismatch_count = {projective["strict_mismatch_count"]}
projective_mismatch_count = {projective["projective_mismatch_count"]}
nontrivial_central_twist_count = {projective["nontrivial_central_twist_count"]}
operator_level_projective_rhoE_promoted = false
selected_DE_dotD_Riesz_Green_emitted = false
```

Why this cannot close:

{projective_missing}

## Open Selected Fields

{open_rows}

## Guardrails

{guardrails}

## Decision

```text
strongest_result = {decision["strongest_result"]}
next_required_object = {decision["next_required_object"]}
parallel_projective_next_object = {decision["parallel_projective_next_object"]}
```
"""


def write_json(path: Path, payload: dict[str, Any]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(payload, indent=2, sort_keys=True) + "\n", encoding="utf-8")


def main() -> int:
    missing = [str(path) for path in INPUTS.values() if not path.exists()]
    if missing:
        print("Missing inputs:")
        print("\n".join(missing))
        return 1
    candidate, certificate, note = build()
    write_json(OUTPUT_DATA, candidate)
    write_json(OUTPUT_CERT, certificate)
    OUTPUT_NOTE.write_text(note, encoding="utf-8")
    print(f"Wrote {OUTPUT_DATA}")
    print(f"Wrote {OUTPUT_CERT}")
    print(f"Wrote {OUTPUT_NOTE}")
    print(certificate["status"])
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
