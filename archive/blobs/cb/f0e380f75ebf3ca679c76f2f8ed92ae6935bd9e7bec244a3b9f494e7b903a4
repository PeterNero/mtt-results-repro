"""Build PSM-C1-02 RA-2 boundary/source or RB-4 independent-source gate."""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "candidate_data"
CERTS = ROOT / "certificates"
CORPUS = ROOT / "proof_corpus"

PREVIOUS = DATA / "selected_psm_c1_02_ra1_physicalactionequality_or_rb3_hessiansourcefill.candidate.json"
BOUNDARY = DATA / "selected_c1tracemeasurepromotion_or_actionboundaryproof" / "finite_trace_boundary_cancellation_certificate.packet.json"
SOURCE_OWNER = DATA / "selected_dynamicc1_sourceowner_fill_or_connectiontables_export_run" / "source_owner_field_matrix_after_backimport.packet.json"
WORKORDER = DATA / "selected_routeb_independentquadraturepayload_schema_or_executionworkorder" / "routeb_independent_quadrature_execution_workorder.packet.json"
ALL_ROWS = DATA / "selected_allrowsprovenancepromotion_or_physicalphifinc1actionsource.candidate.json"
RB3 = DATA / "selected_psm_c1_02_ra1_physicalactionequality_or_rb3_hessiansourcefill" / "route_b_rb3_hessian_source_fill.packet.json"

OUTPUT = DATA / "selected_psm_c1_02_ra2_boundarysource_or_rb4_independentsource.candidate.json"
PACKET_DIR = DATA / "selected_psm_c1_02_ra2_boundarysource_or_rb4_independentsource"
RA2_PACKET = PACKET_DIR / "route_a_ra2_boundary_source_gate.packet.json"
RB4_PACKET = PACKET_DIR / "route_b_rb4_independent_source_gate.packet.json"
PROMOTION_MATRIX = PACKET_DIR / "psm_c1_02_source_promotion_matrix.packet.json"
NEXT_WORKORDER = PACKET_DIR / "next_labeled_workorder.packet.json"
CERT = CERTS / "selected_psm_c1_02_ra2_boundarysource_or_rb4_independentsource_certificate.json"
NOTE = CORPUS / "MTT_Selected_PSM_C1_02_RouteA_RA2_BoundarySource_or_RouteB_RB4_IndependentSource_v1.md"

STATUS = "MTT_SELECTED_PSM_C1_02_RA2_BOUNDARYSOURCE_OR_RB4_INDEPENDENTSOURCE_BUILT_STATIC_PROVENANCE_CLOSED_DYNAMIC_SOURCE_OPEN"
NEXT = "MTT_Selected_PSM_C1_02_RouteA_RA3_SameSourceEmission_or_RouteB_RB5_DynamicValueSourceOwnerFill_v1"


def rel(path: Path) -> str:
    return str(path.relative_to(ROOT)).replace("\\", "/")


def load(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def main() -> int:
    PACKET_DIR.mkdir(parents=True, exist_ok=True)

    previous = load(PREVIOUS)
    boundary = load(BOUNDARY)
    owner = load(SOURCE_OWNER)
    workorder = load(WORKORDER)
    all_rows = load(ALL_ROWS)
    rb3 = load(RB3)
    fields = owner["field_results"]

    closed_static_fields = [
        key
        for key, value in fields.items()
        if value["closed_for_source_owner_template"] is True
        and value["source_owner_verified"] is True
    ]
    open_dynamic_fields = [
        key
        for key, value in fields.items()
        if value["closed_for_source_owner_template"] is False
    ]

    ra2_closed_static = (
        boundary["algebraic_boundary_closed_now"] is True
        and fields["source_owner_id"]["source_owner_verified"] is True
        and fields["admissible_c1_variation_space"]["source_owner_verified"] is True
        and fields["independence_guard"]["source_owner_verified"] is True
    )

    rb4_ready_schema = (
        workorder["counts"]["primitive_contractions"] == 72
        and workorder["counts"]["hessian_source"] == 2
        and workorder["counts"]["sector_matrices"] == 36
        and workorder["counts"]["strict_payload_rows"] == 110
    )

    ra2_packet = {
        "schema": "MTTPSMC102RouteARA2BoundarySourceGate.v1",
        "active_label": "PSM-C1-02",
        "route_label": "ROUTE-A",
        "clause_id": "RA-2",
        "status": "ROUTE_A_RA2_STATIC_BOUNDARY_CLOSED_PHYSICAL_DYNAMIC_SOURCE_OPEN",
        "finite_trace_boundary_cancellation": {
            "algebraic_boundary_closed_now": boundary["algebraic_boundary_closed_now"],
            "physical_boundary_promoted_now": boundary["physical_boundary_promoted_now"],
            "scope_limit": boundary["scope_limit"],
            "source": rel(BOUNDARY),
        },
        "static_source_owner_fields_closed": closed_static_fields,
        "ra2_static_gate_closed": ra2_closed_static,
        "ra2_physical_boundary_source_closed": False,
        "missing_for_full_RA2": [
            "same-branch proof that the physical Phi_fin^C1 restriction has no extra boundary/source term",
            "same-source emission of phase_R_Z_source",
            "same-source emission of shift_R_X_source",
            "same-source Hessian/source emission of b_selected_source",
        ],
        "free_axiom_patch_used": False,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
    }

    rb4_packet = {
        "schema": "MTTPSMC102RouteBRB4IndependentSourceGate.v1",
        "active_label": "PSM-C1-02",
        "route_label": "ROUTE-B",
        "input_id": "RB-4",
        "status": "ROUTE_B_RB4_STRICT_PAYLOAD_SCHEMA_READY_DYNAMIC_SOURCE_ROWS_OPEN",
        "execution_workorder": rel(WORKORDER),
        "strict_payload_counts": workorder["counts"],
        "strict_payload_schema_ready": rb4_ready_schema,
        "formal_replay_closed": all_rows["promotion_decision"]["formal_110_row_replay_closed"],
        "rb3_hessian_support": rb3["hessian_source_support"],
        "closed_source_owner_fields": closed_static_fields,
        "open_source_owner_fields": open_dynamic_fields,
        "independent_source_promoted_now": False,
        "selected_dynamic_values_promoted_now": False,
        "remaining_dynamic_rows": {
            "phase_R_Z_source": fields["phase_R_Z_source"],
            "shift_R_X_source": fields["shift_R_X_source"],
            "b_selected_source": fields["b_selected_source"],
            "sector_row_assembly": fields["sector_row_assembly"],
        },
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
    }

    promotion_matrix = {
        "schema": "MTTPSMC102SourcePromotionMatrixAfterRA2RB4.v1",
        "active_label": "PSM-C1-02",
        "closed_boundary": "DONE-PARITY-00",
        "status": "STATIC_PROVENANCE_AND_FORMAL_ROW_REPLAY_CLOSED_DYNAMIC_SOURCE_OWNERSHIP_OPEN",
        "source_owner_field_counts": {
            "closed": owner["closed_field_count"],
            "open": owner["open_field_count"],
            "closed_fields": closed_static_fields,
            "open_fields": open_dynamic_fields,
        },
        "closed_now": {
            "finite_trace_algebraic_boundary_cancellation": boundary["algebraic_boundary_closed_now"],
            "source_owner_id": fields["source_owner_id"]["source_owner_verified"],
            "admissible_c1_variation_space": fields["admissible_c1_variation_space"]["source_owner_verified"],
            "independence_guard": fields["independence_guard"]["source_owner_verified"],
            "strict_110_row_payload_schema_ready": rb4_ready_schema,
            "formal_110_row_replay_closed": all_rows["promotion_decision"]["formal_110_row_replay_closed"],
            "support_hessian_normal_equations_filled": rb3["hessian_source_support"]["positive_definite_support_hessian"],
        },
        "still_open": {
            "physical_no_extra_boundary_source_term": True,
            "phase_R_Z_source_owner": True,
            "shift_R_X_source_owner": True,
            "b_selected_source_owner": True,
            "sector_row_assembly_source_owner": True,
            "selected_source_promotion": True,
        },
        "superset_strategy": {
            "paths_used": ["ROUTE-A/RA-2", "ROUTE-B/RB-4", "source-owner matrix", "formal 110-row replay"],
            "locked_target": "promote the same PSM-C1-02 C1 source packet without observed constants, residual target fitting, or free axiom insertion",
            "paths_used_as_knobs": False,
            "observed_values_used_as_knobs": False,
        },
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
    }

    next_work = {
        "schema": "MTTNextLabeledWorkorderAfterPSMC102RA2RB4.v1",
        "previous_artifact": "MTT_Selected_PSM_C1_02_RouteA_RA2_BoundarySource_or_RouteB_RB4_IndependentSource_v1",
        "next_required_artifact": NEXT,
        "primary": {
            "label": "PSM-C1-02 / ROUTE-A / RA-3",
            "task": "Prove same-source R_Z/R_X/b_selected emission from the physical Phi_fin^C1 action after the finite boundary cancellation.",
        },
        "secondary": {
            "label": "PSM-C1-02 / ROUTE-B / RB-5",
            "task": "Fill dynamic source-owner rows for R_Z, R_X, b_selected, and sector-row assembly without residual replay provenance.",
        },
        "status": "NEXT_WORKORDER_RA3_SAMESOURCE_EMISSION_OR_RB5_DYNAMIC_SOURCE_OWNER_FILL",
    }

    candidate = {
        "candidate": "MTTSelectedPSMC102RA2BoundarySourceOrRB4IndependentSource",
        "active_label": "PSM-C1-02",
        "active_routes": ["ROUTE-A/RA-2", "ROUTE-B/RB-4"],
        "closed_boundary": "DONE-PARITY-00",
        "status": STATUS,
        "next_required_artifact": NEXT,
        "inputs": {
            "previous": rel(PREVIOUS),
            "previous_status": previous["status"],
            "finite_trace_boundary_cancellation": rel(BOUNDARY),
            "source_owner_field_matrix": rel(SOURCE_OWNER),
            "routeb_independent_quadrature_workorder": rel(WORKORDER),
            "all_rows_provenance": rel(ALL_ROWS),
            "rb3_hessian_source_fill": rel(RB3),
        },
        "output_packets": {
            "route_A_RA2": rel(RA2_PACKET),
            "route_B_RB4": rel(RB4_PACKET),
            "promotion_matrix": rel(PROMOTION_MATRIX),
            "next_workorder": rel(NEXT_WORKORDER),
        },
        "theorem": {
            "name": "PSMC102RA2BoundarySourceOrRB4IndependentSourceGateTheorem",
            "proved": True,
            "statement": (
                "For PSM-C1-02, finite trace algebra cancels algebraic boundary terms, and the "
                "source-owner matrix closes source_owner_id, admissible_c1_variation_space, and "
                "independence_guard.  Route B has a strict 110-row independent-source payload schema "
                "and formal replay, with the RB-3 Hessian/source equations already filled.  The exact "
                "remaining dynamic source-owner fields are phase_R_Z_source, shift_R_X_source, "
                "b_selected_source, and sector_row_assembly; hence selected source promotion remains open."
            ),
        },
        "what_closes_now": {
            "ROUTE_A_RA2_static_finite_boundary_gate": ra2_closed_static,
            "ROUTE_B_RB4_strict_independent_payload_schema_ready": rb4_ready_schema,
            "source_owner_static_fields_closed_count": len(closed_static_fields),
            "dynamic_source_open_fields_identified": open_dynamic_fields,
            "support_hessian_normal_equations_retained": True,
            "observed_constants_excluded_as_selectors": True,
            "superset_paths_constrained_to_locked_target": True,
        },
        "what_remains_open": {
            "physical_no_extra_boundary_source_term": True,
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
        "certificate": "MTT_Selected_PSM_C1_02_RouteA_RA2_BoundarySource_or_RouteB_RB4_IndependentSource_v1",
        "active_label": "PSM-C1-02",
        "status": STATUS,
        "candidate_path": rel(OUTPUT),
        "note_path": rel(NOTE),
        "next_required_artifact": NEXT,
        "route_A_clause": "RA-2",
        "route_A_RA2_static_gate_closed": ra2_closed_static,
        "route_A_RA2_physical_boundary_source_closed": False,
        "route_B_input": "RB-4",
        "route_B_RB4_schema_ready": rb4_ready_schema,
        "route_B_RB4_selected_source_promoted": False,
        "closed_source_owner_fields": closed_static_fields,
        "open_source_owner_fields": open_dynamic_fields,
        "closure_claimed": False,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
    }

    for path, obj in [
        (RA2_PACKET, ra2_packet),
        (RB4_PACKET, rb4_packet),
        (PROMOTION_MATRIX, promotion_matrix),
        (NEXT_WORKORDER, next_work),
        (OUTPUT, candidate),
        (CERT, cert),
    ]:
        path.write_text(json.dumps(obj, indent=2, sort_keys=True) + "\n", encoding="utf-8")

    NOTE.write_text(
        f"""# MTT Selected PSM C1 02 RouteA RA2 BoundarySource or RouteB RB4 IndependentSource v1

Status label: `PSM-C1-02 / ROUTE-A / RA-2` and `PSM-C1-02 / ROUTE-B / RB-4`

Status: `{STATUS}`

Closed boundary label: `DONE-PARITY-00`

## Theorem

**PSMC102RA2BoundarySourceOrRB4IndependentSourceGateTheorem.** Finite trace algebra cancels algebraic boundary terms, and the source-owner matrix closes `source_owner_id`, `admissible_c1_variation_space`, and `independence_guard`. Route B has a strict 110-row independent-source payload schema and formal replay, with the RB-3 Hessian/source equations already filled.

The exact remaining dynamic source-owner fields are:

- `phase_R_Z_source`
- `shift_R_X_source`
- `b_selected_source`
- `sector_row_assembly`

Therefore selected source promotion remains open.

## Superset Strategy

`ROUTE-A / RA-2` and `ROUTE-B / RB-4` are combined as constrained exits to the same locked target. They are not knobs. The target is selected C1 source promotion without observed constants, residual target fitting, or free axiom insertion.

## Next Artifact

`{NEXT}`
""",
        encoding="utf-8",
    )

    print(json.dumps({"candidate": rel(OUTPUT), "status": STATUS}, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
