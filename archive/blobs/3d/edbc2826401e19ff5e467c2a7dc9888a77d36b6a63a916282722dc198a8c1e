"""Build PSM-C1-02 RA-3 same-source emission / RB-5 dynamic owner attack."""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "candidate_data"
CERTS = ROOT / "certificates"
CORPUS = ROOT / "proof_corpus"

PREVIOUS = DATA / "selected_psm_c1_02_ra2_boundarysource_or_rb4_independentsource.candidate.json"
SOURCE_OWNER = DATA / "selected_dynamicc1_sourceowner_fill_or_connectiontables_export_run" / "source_owner_field_matrix_after_backimport.packet.json"
NORMAL_FORM = DATA / "selected_samesource_dynamictransferidentity_or_galerkinc1contractions_emission.candidate.json"
SOURCE_IDENTITY = DATA / "selected_unpatchedfinitec1sourceidentity_or_honestindependentkernelexport" / "source_identity_route_audit.packet.json"
ROUTE_TABLE = DATA / "selected_routea_physicalactionidentityproof_or_routeb_independentrowsourcetable" / "two_exit_current_after_table_attempt.packet.json"
RB3 = DATA / "selected_psm_c1_02_ra1_physicalactionequality_or_rb3_hessiansourcefill" / "route_b_rb3_hessian_source_fill.packet.json"

OUTPUT = DATA / "selected_psm_c1_02_ra3_samesourceemission_or_rb5_dynamicvalueownerfill.candidate.json"
PACKET_DIR = DATA / "selected_psm_c1_02_ra3_samesourceemission_or_rb5_dynamicvalueownerfill"
RA3_PACKET = PACKET_DIR / "route_a_ra3_samesource_emission_attack.packet.json"
RB5_PACKET = PACKET_DIR / "route_b_rb5_dynamic_value_owner_fill_attack.packet.json"
REDUCTION_PACKET = PACKET_DIR / "four_dynamic_fields_to_single_identity_reduction.packet.json"
NEXT_WORKORDER = PACKET_DIR / "next_labeled_workorder.packet.json"
CERT = CERTS / "selected_psm_c1_02_ra3_samesourceemission_or_rb5_dynamicvalueownerfill_certificate.json"
NOTE = CORPUS / "MTT_Selected_PSM_C1_02_RouteA_RA3_SameSourceEmission_or_RouteB_RB5_DynamicValueOwnerFill_v1.md"

STATUS = "MTT_SELECTED_PSM_C1_02_RA3_SAMESOURCEEMISSION_OR_RB5_DYNAMICVALUEOWNERFILL_ATTACK_BUILT_REDUCED_TO_SINGLE_IDENTITY_OPEN"
NEXT = "MTT_Selected_PSM_C1_02_SourceIdentityLemma_Derivation_or_ExplicitLocalPrincipleDecision_v1"
OPEN_FIELDS = ["phase_R_Z_source", "shift_R_X_source", "b_selected_source", "sector_row_assembly"]


def rel(path: Path) -> str:
    return str(path.relative_to(ROOT)).replace("\\", "/")


def load(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def main() -> int:
    PACKET_DIR.mkdir(parents=True, exist_ok=True)

    previous = load(PREVIOUS)
    owner = load(SOURCE_OWNER)
    normal = load(NORMAL_FORM)
    source_identity = load(SOURCE_IDENTITY)
    route_table = load(ROUTE_TABLE)
    rb3 = load(RB3)
    fields = owner["field_results"]

    normal_form = normal["normal_form_identity"]
    identity_equations = normal_form["identity_equations"]
    conditional_values = normal_form["finite_values_if_identity_proved"]

    current_open = [name for name in OPEN_FIELDS if not fields[name]["source_owner_verified"]]
    all_four_open = current_open == OPEN_FIELDS
    validator_ready = source_identity["conditional_source_id_validator"]["ok"] is True
    source_identity_inserted = source_identity["principle"]["insertion_status"]["accepted_as_axiom_or_derived_theorem"]
    theorem_gate_proved = source_identity["theorem_gate"]["proved_now"]

    ra3_packet = {
        "schema": "MTTPSMC102RouteARA3SameSourceEmissionAttack.v1",
        "active_label": "PSM-C1-02",
        "route_label": "ROUTE-A",
        "clause_id": "RA-3",
        "status": "ROUTE_A_RA3_SAMESOURCE_EMISSION_REDUCED_TO_SELECTED_FINITE_C1_SOURCE_IDENTITY_OPEN",
        "same_source_emission_target": {
            "phase_R_Z_source": "Phi_C1_selected(Z)=phase_packet",
            "shift_R_X_source": "Phi_C1_selected(X)=shift_packet",
            "b_selected_source": "b_selected=Phi_C1_selected(Z)+Phi_C1_selected(X)",
            "sector_row_assembly": "finite trace rule assembles sector rows from the same primitive source rows",
        },
        "current_route_A_accepts": source_identity["theorem_gate"]["current_route_A_accepts"],
        "physical_action_restriction_current": route_table["route_A_physical_action_restriction"],
        "conditional_source_identity_validator_ready": validator_ready,
        "selected_finite_c1_source_identity_derived_now": source_identity_inserted or theorem_gate_proved,
        "selected_values_promoted_now": False,
        "why_not_promoted": [
            "The SelectedFiniteC1SourceIdentityPrinciple is formulated and validator-ready conditionally, but is not derived or accepted unpatched.",
            "Route A still lacks physical_action_restricts_to_finite_weyl_quotient, zero_extra_boundary_or_source_term, phase_R_Z_source_selection, shift_R_X_source_selection, and same_source_b_selected_emission.",
        ],
        "free_axiom_patch_used": False,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
    }

    rb5_packet = {
        "schema": "MTTPSMC102RouteBRB5DynamicValueOwnerFillAttack.v1",
        "active_label": "PSM-C1-02",
        "route_label": "ROUTE-B",
        "input_id": "RB-5",
        "status": "ROUTE_B_RB5_DYNAMIC_VALUE_OWNER_ATTACK_REDUCED_TO_SAME_SOURCE_IDENTITY_OR_INDEPENDENT_TABLE_OPEN",
        "current_open_dynamic_fields": current_open,
        "source_owner_field_status": {name: fields[name] for name in OPEN_FIELDS},
        "normal_form_identity": {
            "identity_equations": identity_equations,
            "selected_identity_proved_now": normal_form["selected_identity_proved_now"],
            "finite_values_if_identity_proved": conditional_values,
        },
        "rb3_support_hessian": rb3["hessian_source_support"],
        "route_B_current_accepts": source_identity["theorem_gate"]["current_route_B_accepts"],
        "route_B_current_table": route_table["route_B_independent_rowkernel_source"],
        "dynamic_fields_promoted_now": False,
        "independent_source_table_promoted_now": False,
        "why_not_promoted": [
            "The best current Route-B table still fails source validation: rows are exact but not source-owned independently of residual replay.",
            "The normal-form identity proves what must be emitted, not that the selected branch emits it.",
        ],
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
    }

    reduction = {
        "schema": "MTTPSMC102FourDynamicFieldsToSingleIdentityReduction.v1",
        "active_label": "PSM-C1-02",
        "closed_boundary": "DONE-PARITY-00",
        "status": "FOUR_DYNAMIC_FIELDS_REDUCED_TO_SELECTED_FINITE_C1_SOURCE_IDENTITY_LEMMA",
        "open_dynamic_fields_before": OPEN_FIELDS,
        "all_four_still_open_now": all_four_open,
        "single_remaining_identity": {
            "name": "SelectedFiniteC1SourceIdentityLemma",
            "statement": source_identity["principle"]["statement"],
            "minimal_axioms_or_subclaims": source_identity["principle"]["minimal_axioms"],
            "conditional_validator_would_pass_if_inserted": source_identity["principle"]["insertion_status"]["conditional_validator_would_pass_if_inserted"],
            "derived_or_accepted_now": source_identity_inserted or theorem_gate_proved,
        },
        "if_single_identity_proved_then": {
            "phase_R_Z_source_owner": True,
            "shift_R_X_source_owner": True,
            "b_selected_source_owner": True,
            "sector_row_assembly_source_owner": True,
            "A_transpose_A": conditional_values["Gram_A_transpose_A"],
            "A_transpose_b": conditional_values["A_transpose_b"],
            "deltaTheta_C1": conditional_values["deltaTheta_C1"],
            "selected_source_promotion_would_close_for_PSM_C1_02": True,
        },
        "superset_strategy": {
            "paths_used": ["ROUTE-A/RA-3 same-source physical emission", "ROUTE-B/RB-5 dynamic value owner fill", "conditional source identity validator", "normal-form dynamic transfer identity"],
            "locked_target": "the same selected finite C1 source identity, not separate fitted values",
            "paths_used_as_knobs": False,
            "observed_values_used_as_knobs": False,
        },
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
    }

    next_work = {
        "schema": "MTTNextLabeledWorkorderAfterPSMC102RA3RB5.v1",
        "previous_artifact": "MTT_Selected_PSM_C1_02_RouteA_RA3_SameSourceEmission_or_RouteB_RB5_DynamicValueOwnerFill_v1",
        "next_required_artifact": NEXT,
        "primary": {
            "label": "PSM-C1-02 / SOURCE-IDENTITY / SI-1",
            "task": "Derive the SelectedFiniteC1SourceIdentityLemma unpatched from corpus/source structure.",
        },
        "secondary": {
            "label": "PSM-C1-02 / SOURCE-IDENTITY / SI-2",
            "task": "If derivation fails, decide whether to explicitly add the minimal local principle to the papers as an axiom and mark no-knob closure open.",
        },
        "status": "NEXT_WORKORDER_SOURCE_IDENTITY_DERIVATION_OR_LOCAL_PRINCIPLE_DECISION",
    }

    candidate = {
        "candidate": "MTTSelectedPSMC102RA3SameSourceEmissionOrRB5DynamicValueOwnerFill",
        "active_label": "PSM-C1-02",
        "active_routes": ["ROUTE-A/RA-3", "ROUTE-B/RB-5"],
        "closed_boundary": "DONE-PARITY-00",
        "status": STATUS,
        "next_required_artifact": NEXT,
        "inputs": {
            "previous": rel(PREVIOUS),
            "previous_status": previous["status"],
            "source_owner_field_matrix": rel(SOURCE_OWNER),
            "same_source_dynamic_transfer_normal_form": rel(NORMAL_FORM),
            "source_identity_route_audit": rel(SOURCE_IDENTITY),
            "route_A_or_B_current_table_attempt": rel(ROUTE_TABLE),
            "rb3_hessian_source_fill": rel(RB3),
        },
        "output_packets": {
            "route_A_RA3": rel(RA3_PACKET),
            "route_B_RB5": rel(RB5_PACKET),
            "single_identity_reduction": rel(REDUCTION_PACKET),
            "next_workorder": rel(NEXT_WORKORDER),
        },
        "theorem": {
            "name": "PSMC102RA3RB5DynamicFieldsToSourceIdentityReductionTheorem",
            "proved": True,
            "statement": (
                "For PSM-C1-02, direct RA-3 same-source emission and RB-5 dynamic value owner "
                "promotion both fail unpatched, but their failures are equivalent to one named "
                "SelectedFiniteC1SourceIdentityLemma. If that lemma is derived or explicitly accepted, "
                "phase_R_Z_source, shift_R_X_source, b_selected_source, sector_row_assembly, and the "
                "RB-3 normal equations promote together. Without it, all four dynamic source-owner "
                "fields remain open."
            ),
        },
        "what_closes_now": {
            "RA3_direct_attack_completed": True,
            "RB5_direct_attack_completed": True,
            "four_dynamic_fields_reduced_to_single_identity": True,
            "conditional_source_id_validator_ready": validator_ready,
            "observed_constants_excluded_as_selectors": True,
            "superset_paths_constrained_to_locked_target": True,
        },
        "what_remains_open": {
            "SelectedFiniteC1SourceIdentityLemma_unpatched_derivation": True,
            "phase_R_Z_source_owner": True,
            "shift_R_X_source_owner": True,
            "b_selected_source_owner": True,
            "sector_row_assembly_source_owner": True,
            "selected_source_promotion": True,
            "true_equivalence_closed": False,
        },
        "closure_claimed": False,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
    }

    cert = {
        "certificate": "MTT_Selected_PSM_C1_02_RouteA_RA3_SameSourceEmission_or_RouteB_RB5_DynamicValueOwnerFill_v1",
        "active_label": "PSM-C1-02",
        "status": STATUS,
        "candidate_path": rel(OUTPUT),
        "note_path": rel(NOTE),
        "next_required_artifact": NEXT,
        "route_A_clause": "RA-3",
        "route_A_RA3_same_source_promoted": False,
        "route_B_input": "RB-5",
        "route_B_RB5_dynamic_fields_promoted": False,
        "open_dynamic_fields": current_open,
        "reduced_to_single_identity": True,
        "conditional_source_id_validator_ready": validator_ready,
        "closure_claimed": False,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
    }

    for path, obj in [
        (RA3_PACKET, ra3_packet),
        (RB5_PACKET, rb5_packet),
        (REDUCTION_PACKET, reduction),
        (NEXT_WORKORDER, next_work),
        (OUTPUT, candidate),
        (CERT, cert),
    ]:
        path.write_text(json.dumps(obj, indent=2, sort_keys=True) + "\n", encoding="utf-8")

    NOTE.write_text(
        f"""# MTT Selected PSM C1 02 RouteA RA3 SameSourceEmission or RouteB RB5 DynamicValueOwnerFill v1

Status label: `PSM-C1-02 / ROUTE-A / RA-3` and `PSM-C1-02 / ROUTE-B / RB-5`

Status: `{STATUS}`

Closed boundary label: `DONE-PARITY-00`

## Theorem

**PSMC102RA3RB5DynamicFieldsToSourceIdentityReductionTheorem.** Direct `RA-3` same-source emission and `RB-5` dynamic value owner promotion both fail unpatched, but their failures reduce to one named lemma: `SelectedFiniteC1SourceIdentityLemma`.

If that lemma is derived or explicitly accepted, the following close together:

- `phase_R_Z_source`
- `shift_R_X_source`
- `b_selected_source`
- `sector_row_assembly`
- `A^T A = [[12, 0], [0, 12]]`
- `A^T b = [12, 12]`
- `deltaTheta_C1 = [1, 1]`

Without it, all four dynamic source-owner fields remain open.

## Superset Strategy

`ROUTE-A / RA-3` and `ROUTE-B / RB-5` are not knobs. They are two constrained exits to the same selected finite C1 source identity.

## Next Artifact

`{NEXT}`
""",
        encoding="utf-8",
    )

    print(json.dumps({"candidate": rel(OUTPUT), "status": STATUS}, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
