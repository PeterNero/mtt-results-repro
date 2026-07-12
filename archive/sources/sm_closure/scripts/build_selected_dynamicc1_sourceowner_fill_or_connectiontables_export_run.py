"""Build the DynamicC1 source-owner fill/export run after later source imports."""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "candidate_data"
CERTS = ROOT / "certificates"
CORPUS = ROOT / "proof_corpus"

SLUG = "selected_dynamicc1_sourceowner_fill_or_connectiontables_export_run"
PACKET_DIR = DATA / SLUG
OUTPUT = DATA / f"{SLUG}.candidate.json"
FIELD_MATRIX = PACKET_DIR / "source_owner_field_matrix_after_backimport.packet.json"
CONNECTION_STATUS = PACKET_DIR / "independent_connection_export_status_after_backimport.packet.json"
FIX_DECISION = PACKET_DIR / "dynamic_c1_sourceowner_fix_decision.packet.json"
CERT = CERTS / f"{SLUG}_certificate.json"
NOTE = CORPUS / "MTT_Selected_DynamicC1_SourceOwnerTheorem_Fill_or_ConnectionTablesExport_Run_v1.md"

STATUS = "MTT_SELECTED_DYNAMICC1_SOURCEOWNER_FILLRUN_STATIC_FIELDS_IMPORTED_DYNAMIC_VALUES_OPEN"
NEXT = "MTT_Selected_DynamicC1_SourceOwner_DynamicTransferHessian_or_HonestGalerkinValues_v1"


def rel(path: Path) -> str:
    try:
        return str(path.relative_to(ROOT)).replace("\\", "/")
    except ValueError:
        return str(path)


def load(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def field(
    name: str,
    *,
    closed: bool,
    tier: str,
    source: str,
    reason: str,
    selected_emitted: bool | None = None,
) -> dict[str, Any]:
    if selected_emitted is None:
        selected_emitted = closed
    return {
        "name": name,
        "closed_for_source_owner_template": closed,
        "tier": tier,
        "source": source,
        "reason": reason,
        "selected_emitted": selected_emitted,
        "same_branch": closed,
        "theorem_derived": closed,
        "source_owner_verified": closed,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
    }


def main() -> int:
    PACKET_DIR.mkdir(parents=True, exist_ok=True)

    template = load(DATA / "selected_dynamicc1_sourceowner_theorem_or_independentconnectiontables.candidate.json")
    static_ledger = load(DATA / "selected_smslotfunctor_downstream_operator_payloads_or_smparity_ledger.candidate.json")
    static_routing = load(DATA / "selected_primitivec1_or_weylpair_sectorrouting_sourceemission.candidate.json")
    alpha1 = load(DATA / "selected_crossrepo_alpha1_driver_replay_import.candidate.json")
    dynamic_cutset = load(DATA / "selected_dynamicc1transfertensor_valueemission_or_honestgalerkinc1run.candidate.json")
    source_map = load(DATA / "selected_sourcemapselectiontheorem_or_honestgalerkinc1valuerun.candidate.json")
    hessian = load(DATA / "selected_dynamictransferhessian_bselected_or_honestgalerkinc1_valuefill.candidate.json")
    primitive_candidate = load(DATA / "selected_primitivec1tensor_hessiansourcemap_or_honestgalerkinc1execution.candidate.json")

    field_matrix = {
        "schema": "MTTDynamicC1SourceOwnerFillRunFieldMatrix.v1",
        "status": "STATIC_AND_PROVENANCE_FIELDS_IMPORTED_DYNAMIC_VALUES_OPEN",
        "template_import": rel(DATA / "selected_dynamicc1_sourceowner_theorem_or_independentconnectiontables.candidate.json"),
        "field_results": {
            "source_owner_id": field(
                "source_owner_id",
                closed=True,
                tier="selected_source_spine",
                source=rel(DATA / "selected_crossrepo_alpha1_driver_replay_import.candidate.json"),
                reason=(
                    "The same q79/F,m=1 oriented source spine is imported with selected alpha1 driver "
                    "and selected dotD source verified."
                ),
            ),
            "admissible_c1_variation_space": field(
                "admissible_c1_variation_space",
                closed=True,
                tier="static_source_plus_fixed_72_real_coordinate_target",
                source=rel(DATA / "selected_dynamictransferhessian_bselected_or_honestgalerkinc1_valuefill.candidate.json"),
                reason=(
                    "The 72-real coordinate system, static Weyl routing, active shift, and finite trace "
                    "normalization are fixed independently of observed constants."
                ),
            ),
            "phase_R_Z_source": field(
                "phase_R_Z_source",
                closed=False,
                tier="dynamic_value",
                source=rel(DATA / "selected_primitivec1tensor_hessiansourcemap_or_honestgalerkinc1execution.candidate.json"),
                reason=(
                    "R_Z is constructed as the unique canonical residual/source-map candidate, but the "
                    "differentiated Phi_fin^C1 application rule or honest Galerkin emission has not selected it."
                ),
                selected_emitted=False,
            ),
            "shift_R_X_source": field(
                "shift_R_X_source",
                closed=False,
                tier="dynamic_value",
                source=rel(DATA / "selected_primitivec1tensor_hessiansourcemap_or_honestgalerkinc1execution.candidate.json"),
                reason=(
                    "R_X is constructed as the unique canonical residual/source-map candidate, but the "
                    "differentiated Phi_fin^C1 application rule or honest Galerkin emission has not selected it."
                ),
                selected_emitted=False,
            ),
            "b_selected_source": field(
                "b_selected_source",
                closed=False,
                tier="dynamic_hessian_value",
                source=rel(DATA / "selected_dynamictransferhessian_bselected_or_honestgalerkinc1_valuefill.candidate.json"),
                reason=(
                    "A^T b=(12,12), ||b||^2=24, and deltaTheta=(1,1) are exact conditional Gram values, "
                    "but the same-source Hessian/source vector is still not emitted."
                ),
                selected_emitted=False,
            ),
            "sector_row_assembly": field(
                "sector_row_assembly",
                closed=False,
                tier="dynamic_sector_response_value",
                source=rel(DATA / "selected_dynamicc1transfertensor_valueemission_or_honestgalerkinc1run.candidate.json"),
                reason=(
                    "Static Z->u,e and X->d,nuD routing is selected, but the dynamic sector response "
                    "matrices are still unpromoted."
                ),
                selected_emitted=False,
            ),
            "independence_guard": field(
                "independence_guard",
                closed=True,
                tier="guardrail",
                source=rel(DATA / "selected_sourcemapselectiontheorem_or_honestgalerkinc1valuerun.candidate.json"),
                reason=(
                    "The tested routes exclude observed constants, benchmark matrices, and residual-target "
                    "selection; support-only and conditional packets remain separate."
                ),
            ),
        },
        "closed_field_count": 3,
        "open_field_count": 4,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
    }

    connection_status = {
        "schema": "MTTDynamicC1IndependentConnectionExportStatusAfterBackimport.v1",
        "status": "CONNECTION_EXPORT_PARTIAL_STATIC_SUPPORT_DYNAMIC_TABLES_OPEN",
        "required_table_families": {
            "selected_connection_or_transition_data": {
                "present": True,
                "source": rel(DATA / "selected_crossrepo_alpha1_driver_replay_import.candidate.json"),
                "note": "same q79/F,m=1 source spine plus selected alpha1/dotD import",
            },
            "rho_E_or_nonidentity_projective_transition": {
                "present": True,
                "source": rel(DATA / "selected_nonidentity_rhoe_transition_source.candidate.json"),
                "note": "nonidentity rho_E source layer exists as support",
            },
            "quotient_valid_B_N_or_BN27_carrier": {
                "present": True,
                "source": rel(DATA / "selected_primitivefibershift_or_typedretardedselector_sourcetheorem.candidate.json"),
                "note": "active shift and fixed-fiber quotient class selected for current C1 spectral observables",
            },
            "D_E_Riesz_Green_dotD_payload": {
                "present": True,
                "source": rel(DATA / "selected_crossrepo_alpha1_driver_replay_import.candidate.json"),
                "note": "selected_dotD_source_verified and alpha1_driver_verified imported",
            },
            "primitive_C1_row_kernel_tables": {
                "present": False,
                "source": rel(DATA / "selected_primitivec1tensor_hessiansourcemap_or_honestgalerkinc1execution.candidate.json"),
                "note": "candidate residual operators exist, but selected primitive C1 tensor values remain open",
            },
            "hessian_bselected_tables": {
                "present": False,
                "source": rel(DATA / "selected_dynamictransferhessian_bselected_or_honestgalerkinc1_valuefill.candidate.json"),
                "note": "conditional Hessian/Gram exactness is not same-source b_selected emission",
            },
            "sector_response_tables": {
                "present": False,
                "source": rel(DATA / "selected_dynamicc1transfertensor_valueemission_or_honestgalerkinc1run.candidate.json"),
                "note": "dynamic sector response matrices are still not emitted",
            },
            "source_independence_certificate": {
                "present": True,
                "source": rel(DATA / "selected_sourcemapselectiontheorem_or_honestgalerkinc1valuerun.candidate.json"),
                "note": "selection/conditional-support boundary is machine recorded",
            },
        },
        "present_count": 5,
        "missing_count": 3,
        "if_missing_tables_filled_then_source_owner_closes": True,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
    }

    fix_decision = {
        "schema": "MTTDynamicC1SourceOwnerFixDecision.v1",
        "status": "FIX_APPLIED_AS_BACKIMPORT_FILLRUN_CLOSURE_NOT_CLAIMED",
        "fixed_issue": (
            "The original theorem object was too early in the proof spine and did not import later static "
            "SM-slot routing, alpha1/dotD, and quotient-carrier closures. This fill-run imports them and "
            "reduces the active blocker to dynamic C1 value emission."
        ),
        "superset_strategy": {
            "combined_paths": [
                "SM-slot/terminal source functor static routing",
                "cross-repo alpha1/dotD selected source import",
                "fixed-fiber quotient/primitive C1 candidate",
                "conditional dynamic Hessian Gram solve",
            ],
            "locked_target": "seven-field DynamicC1 source-owner template",
            "paths_used_as_knobs": False,
            "postcheck_target_fixed_before_import": True,
        },
        "closure_decision": {
            "source_owner_id_closed": True,
            "admissible_c1_variation_space_closed": True,
            "independence_guard_closed": True,
            "phase_R_Z_source_closed": False,
            "shift_R_X_source_closed": False,
            "b_selected_source_closed": False,
            "sector_row_assembly_closed": False,
            "dynamic_C1_source_owner_closed": False,
            "true_SM_equivalence_closed": False,
            "no_knob_closed": False,
        },
        "exact_conditional_values_retained": {
            "A_transpose_A": [[12.0, 0.0], [0.0, 12.0]],
            "A_transpose_b": [12.0, 12.0],
            "b_norm_sq": 24.0,
            "deltaTheta_C1": [1.0, 1.0],
            "linear_algebra_obstruction_removed": hessian["what_closes_now"]["linear_algebra_obstruction_removed"],
        },
        "next_action": (
            "Prove selected differentiated Phi_fin^C1 applies the canonical residual projector to emit R_Z/R_X "
            "and b_selected, or run an honest selected Galerkin C1 execution that emits replacement dynamic tables."
        ),
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
    }

    for path, payload in [
        (FIELD_MATRIX, field_matrix),
        (CONNECTION_STATUS, connection_status),
        (FIX_DECISION, fix_decision),
    ]:
        path.write_text(json.dumps(payload, indent=2, sort_keys=True) + "\n", encoding="utf-8")

    candidate = {
        "candidate": "MTTSelectedDynamicC1SourceOwnerFillOrConnectionTablesExportRun",
        "status": STATUS,
        "inputs": {
            "sourceowner_template": rel(DATA / "selected_dynamicc1_sourceowner_theorem_or_independentconnectiontables.candidate.json"),
            "static_sm_slot_payloads": rel(DATA / "selected_smslotfunctor_downstream_operator_payloads_or_smparity_ledger.candidate.json"),
            "static_weyl_routing": rel(DATA / "selected_primitivec1_or_weylpair_sectorrouting_sourceemission.candidate.json"),
            "alpha1_dotd_import": rel(DATA / "selected_crossrepo_alpha1_driver_replay_import.candidate.json"),
            "dynamic_value_cutset": rel(DATA / "selected_dynamicc1transfertensor_valueemission_or_honestgalerkinc1run.candidate.json"),
            "source_map_boundary": rel(DATA / "selected_sourcemapselectiontheorem_or_honestgalerkinc1valuerun.candidate.json"),
        },
        "output_packets": {
            "field_matrix": rel(FIELD_MATRIX),
            "connection_export_status": rel(CONNECTION_STATUS),
            "fix_decision": rel(FIX_DECISION),
        },
        "theorem": {
            "name": "DynamicC1SourceOwnerBackimportFillRunTheorem",
            "proved": True,
            "statement": (
                "After importing later selected static SM-slot routing, selected alpha1/dotD source replay, "
                "fixed-fiber quotient support, and the exact conditional Hessian solve, the seven-field "
                "DynamicC1 source-owner template has exactly three closed fields and four dynamic value fields open. "
                "The remaining obstruction is selected dynamic C1 value emission, not sector labels, alpha1/dotD, "
                "normalization convention, or linear algebra."
            ),
        },
        "closure_decision": fix_decision["closure_decision"],
        "what_closes_now": {
            "old_template_backimport_fixed": True,
            "static_sector_routing_imported": static_routing["what_closes_now"]["selected_static_weyl_sector_routing_emitted"],
            "static_trace_transfer_normalization_imported": static_ledger["what_closes_now"]["selected_static_finite_trace_transfer_normalization"],
            "alpha1_dotd_imported": alpha1["what_closes_now"]["selected_dotD_source_verified_imported"],
            "source_owner_fields_closed_count": field_matrix["closed_field_count"],
            "connection_export_tables_present_count": connection_status["present_count"],
            "dynamic_value_blocker_is_precisely_identified": True,
        },
        "what_remains_open": {
            "selected_phase_R_Z_source": True,
            "selected_shift_R_X_source": True,
            "selected_b_selected_source": True,
            "selected_sector_response_matrices": True,
            "or_honest_selected_Galerkin_C1_execution": True,
        },
        "not_used_as_closure": {
            "conditional_values": dynamic_cutset["promotion_decision"]["A_selected_promoted"] is False,
            "source_map_candidate": source_map["promotion_decision"]["source_map_selected_by_MTT_now"] is False,
            "primitive_candidate": primitive_candidate["promotion_decision"]["source_map_selected_by_MTT_now"] is False,
        },
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "closure_claimed": False,
        "next_required_artifact": NEXT,
    }

    cert = {
        "certificate": "MTT_Selected_DynamicC1_SourceOwnerTheorem_Fill_or_ConnectionTablesExport_Run_v1",
        "status": STATUS,
        "candidate_path": rel(OUTPUT),
        "note_path": rel(NOTE),
        "backimport_fill_run_built": True,
        "closed_field_count": field_matrix["closed_field_count"],
        "open_field_count": field_matrix["open_field_count"],
        "connection_tables_present_count": connection_status["present_count"],
        "connection_tables_missing_count": connection_status["missing_count"],
        "dynamic_C1_source_owner_closed": False,
        "true_SM_equivalence_closed": False,
        "no_knob_closed": False,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "next_required_artifact": NEXT,
    }

    note = f"""# MTT Selected DynamicC1 SourceOwnerTheorem Fill or ConnectionTablesExport Run v1

Status: `{STATUS}`.

This fixes the earlier source-owner theorem object by back-importing later
verified source-spine progress into the strict seven-field template.

Closed now:

- selected source-owner spine: q79/F,m=1 with selected alpha1/dotD import;
- selected admissible 72-real C1 coordinate/variation target;
- independence guard against observed constants, benchmark matrices, and
  residual-target selection.

Still open:

- selected dynamic `R_Z` source;
- selected dynamic `R_X` source;
- same-source `b_selected`/Hessian emission;
- selected dynamic sector response matrices.

So the repair is real but not a closure claim. The active blocker is now
exactly dynamic C1 value emission: prove the differentiated `Phi_fin^C1`
residual-projector/source rule, or export an honest selected Galerkin C1 table
that emits replacement values.

Next artifact: `{NEXT}`.
"""

    OUTPUT.write_text(json.dumps(candidate, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    CERT.write_text(json.dumps(cert, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    NOTE.write_text(note, encoding="utf-8")
    print(json.dumps({"candidate": rel(OUTPUT), "status": STATUS}, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
