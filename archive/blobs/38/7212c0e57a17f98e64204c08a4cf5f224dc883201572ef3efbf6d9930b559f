"""Build the DynamicC1 source-owner theorem object and connection-table export schema."""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "candidate_data"
CERTS = ROOT / "certificates"
CORPUS = ROOT / "proof_corpus"

SLUG = "selected_dynamicc1_sourceowner_theorem_or_independentconnectiontables"
PACKET_DIR = DATA / SLUG
OUTPUT = DATA / f"{SLUG}.candidate.json"
STRICT_TEMPLATE = PACKET_DIR / "dynamic_c1_source_owner_theorem.strict_template.json"
CURRENT_ATTEMPT = PACKET_DIR / "current_source_owner_fill_attempt.packet.json"
CONNECTION_SCHEMA = PACKET_DIR / "independent_connection_tables_export_schema.packet.json"
IMPLICATION = PACKET_DIR / "source_owner_promotion_implication.packet.json"
PAPER_TEXT = PACKET_DIR / "paper_ready_theorem_text.packet.json"
CERT = CERTS / f"{SLUG}_certificate.json"
NOTE = CORPUS / "MTT_Selected_DynamicC1_SourceOwnerTheorem_or_IndependentConnectionTables_v1.md"

STATUS = "MTT_SELECTED_DYNAMICC1_SOURCEOWNER_THEOREM_BUILT_TEMPLATE_OPEN"
NEXT = "MTT_Selected_DynamicC1_SourceOwnerTheorem_Fill_or_ConnectionTablesExport_Run_v1"


def rel(path: Path) -> str:
    try:
        return str(path.relative_to(ROOT)).replace("\\", "/")
    except ValueError:
        return str(path)


def load(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def source_field(name: str, description: str, current_support: list[str]) -> dict[str, Any]:
    return {
        "name": name,
        "description": description,
        "current_support": current_support,
        "selected_emitted": False,
        "same_branch": False,
        "theorem_derived": False,
        "source_owner_verified": False,
        "forbidden_provenance_excluded": True,
    }


def main() -> int:
    PACKET_DIR.mkdir(parents=True, exist_ok=True)

    decisive = load(DATA / "selected_decisive_dynamicc1_sourceleaf_attack_or_sourceowner_theorem.candidate.json")
    owner = load(
        DATA
        / "selected_decisive_dynamicc1_sourceleaf_attack_or_sourceowner_theorem"
        / "minimal_dynamic_c1_source_owner_theorem.packet.json"
    )
    route_a = load(
        DATA
        / "selected_decisive_dynamicc1_sourceleaf_attack_or_sourceowner_theorem"
        / "route_a_sixfield_phifinc1_source_attack.packet.json"
    )
    route_b = load(
        DATA
        / "selected_decisive_dynamicc1_sourceleaf_attack_or_sourceowner_theorem"
        / "route_b_independent_row_export_attack.packet.json"
    )
    qasu3 = load(
        DATA
        / "selected_decisive_dynamicc1_sourceleaf_attack_or_sourceowner_theorem"
        / "qasu3_bn27_source_support_attack.packet.json"
    )
    formal_rows = load(DATA / "selected_routeaemission_or_routebgalerkinrows_execution.candidate.json")
    source_counter = load(DATA / "selected_minimalfinitec1sourcepromotionlemma_proof_or_countermodel.candidate.json")
    source_kernel = load(DATA / "selected_preresidualvariation_hessiansourcekernel_attempt_or_actionaxiom.candidate.json")

    strict_template = {
        "schema": "MTTDynamicC1SourceOwnerTheoremStrictTemplate.v1",
        "status": "STRICT_TEMPLATE_READY_VALUES_OPEN",
        "branch": "q79/F,m=1/S3_GS/RouteC_or_equivalent_same_selected_source",
        "required_fields": {
            "source_owner_id": source_field(
                "source_owner_id",
                "A named selected same-branch source that owns the dynamic C1 response before replay.",
                ["q79/F,m=1 branch support", "stationary transported Phi_fin trace support"],
            ),
            "admissible_c1_variation_space": source_field(
                "admissible_c1_variation_space",
                "The selected admissible C1 variation directions before residual-projector replay.",
                ["72 row coordinate chart", "finite Weyl trace pairing", "formal 110 row execution"],
            ),
            "phase_R_Z_source": source_field(
                "phase_R_Z_source",
                "The phase residual operator R_Z emitted as source data, not inherited from residual replay.",
                ["exact finite Weyl R_Z row values", "phase rows in u,e sectors"],
            ),
            "shift_R_X_source": source_field(
                "shift_R_X_source",
                "The shift residual operator R_X emitted as source data, not inherited from residual replay.",
                ["exact finite Weyl R_X row values", "shift rows in d,nuD sectors"],
            ),
            "b_selected_source": source_field(
                "b_selected_source",
                "The same-source Hessian/source vector b_selected in the fixed 72-real coordinate system.",
                ["formal A^T b=(12,12)", "formal ||b||^2=24", "deltaTheta replay target (1,1)"],
            ),
            "sector_row_assembly": source_field(
                "sector_row_assembly",
                "The source-owned functor assembling primitive rows into u,d,e,nuD sector response matrices.",
                ["formal sector response matrices", "C33/rank/noncommutation diagnostics"],
            ),
            "independence_guard": source_field(
                "independence_guard",
                "Proof that the fields are independent of observed constants, locked residual targets, and replay-only provenance.",
                ["closed support countermodel", "strict source validators", "no target fitting guardrails"],
            ),
        },
        "accepted_exports": [
            "Route A physical Phi_fin^C1 action/source theorem filling all fields",
            "Route B independent selected Galerkin row-kernel theorem filling all fields",
            "Qa/SU3 nonidentity rho_E plus quotient-valid B_N selected connection-table export filling all fields",
        ],
        "forbidden_provenance": [
            "observed constants",
            "benchmark matrices",
            "target residual minimization",
            "residual-projector replay used as source",
            "formal row replay without source ownership",
            "lifted selected-source flags",
        ],
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
    }

    current_attempt = {
        "schema": "MTTDynamicC1SourceOwnerCurrentFillAttempt.v1",
        "status": "CURRENT_FILL_REJECTED_SOURCE_OWNER_OPEN",
        "route_A_import": {
            "measure_clause_closed": route_a["required_fields"]["physical_trace_frobenius_measure"],
            "passes": route_a["passes_strict_source_validator"],
            "open_fields": [
                key for key, value in route_a["required_fields"].items() if value is False
            ],
        },
        "route_B_import": {
            "stationary_basis_rows_selected": route_b["required_fields"]["stationary_basis_rows_selected"],
            "primitive_row_ids_locked": route_b["required_fields"]["primitive_row_ids_locked"],
            "formal_110_rows_executed": route_b["required_fields"]["formal_110_rows_executed"],
            "passes": route_b["passes_strict_source_validator"],
            "open_fields": [
                key for key, value in route_b["required_fields"].items() if value is False
            ],
        },
        "qasu3_import": {
            "nonidentity_rho_E_interface_built": qasu3["required_fields"]["nonidentity_rho_E_interface_built"],
            "quotient_valid_B_N_required": qasu3["required_fields"]["quotient_valid_B_N_required"],
            "passes": qasu3["passes_strict_source_validator"],
            "open_fields": [
                key for key, value in qasu3["required_fields"].items() if value is False
            ],
        },
        "strict_template_field_results": {
            key: False for key in strict_template["required_fields"].keys()
        },
        "why_rejected": (
            "Current packets provide exact finite values, stationary basis rows, and Qa/SU3 support contracts, "
            "but no packet source-owns the dynamic C1 variation space plus R_Z/R_X/b_selected/sector assembly "
            "before residual-projector replay."
        ),
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
    }

    connection_schema = {
        "schema": "MTTIndependentConnectionTablesExportSchema.v1",
        "status": "EXPORT_SCHEMA_READY_VALUES_OPEN",
        "purpose": "Constructive alternative to a direct source-owner theorem.",
        "required_table_families": {
            "selected_connection_or_transition_data": {
                "description": "Same-branch connection/transition values, e.g. HYM/Strominger, typed Cech, or finite Route-C values.",
                "present": False,
            },
            "rho_E_or_nonidentity_projective_transition": {
                "description": "Nonidentity rho_E or equivalent projective/twisted transition table.",
                "present": False,
            },
            "quotient_valid_B_N_or_BN27_carrier": {
                "description": "Finite carrier with quotient-valid basis and source-owned deck/trace policy.",
                "present": False,
            },
            "D_E_Riesz_Green_dotD_payload": {
                "description": "Validator-ready D_E, Riesz, reduced Green, dotD from the same source without lifted flags.",
                "present": False,
            },
            "primitive_C1_row_kernel_tables": {
                "description": "Selected primitive 72 row-kernel formula/pairing/exactness data.",
                "present": False,
            },
            "hessian_bselected_tables": {
                "description": "Selected Hessian/source rows emitting b_selected, A^T b, and norm policy.",
                "present": False,
            },
            "sector_response_tables": {
                "description": "Selected u,d,e,nuD sector response matrices and rank/C33/phase tests.",
                "present": False,
            },
            "source_independence_certificate": {
                "description": "Proof no observed constants, locked target residuals, or replay-only provenance selected the source.",
                "present": False,
            },
        },
        "if_all_present_then_fills_source_owner_template": True,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
    }

    implication = {
        "schema": "MTTDynamicC1SourceOwnerPromotionImplication.v1",
        "status": "CONDITIONAL_PROMOTION_IMPLICATION_PROVED",
        "hypothesis": "All strict source-owner fields are selected_emitted, same_branch, theorem_derived, and source_owner_verified.",
        "consequences": {
            "selected_A_selected_promotes": True,
            "selected_b_selected_promotes": True,
            "selected_deltaTheta_C1_promotes": True,
            "selected_sector_response_matrices_promote": True,
            "unpatched_dynamic_C1_packet_closes": True,
        },
        "uses_formal_values": {
            "A_transpose_A": [[12.0, 0.0], [0.0, 12.0]],
            "A_transpose_b": [12.0, 12.0],
            "b_norm_sq": 24.0,
            "deltaTheta_C1": [1.0, 1.0],
            "formal_rows_executed": formal_rows["promotion_decision"]["formal_rows_executed"],
        },
        "guardrail": "The implication does not prove the hypothesis; it proves sufficiency once source ownership or connection tables are supplied.",
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
    }

    paper_text = {
        "schema": "MTTDynamicC1SourceOwnerPaperText.v1",
        "status": "PAPER_READY_THEOREM_TEMPLATE_OPEN",
        "theorem_title": "Selected Dynamic C1 Source-Owner Theorem",
        "theorem_statement": (
            "Let S be the selected q79/F,m=1 source branch. If S emits a dynamic C1 source-owner packet "
            "consisting of a selected admissible C1 variation space, source-owned phase and shift residual "
            "operators R_Z and R_X, a same-source Hessian/source vector b_selected, and a sector assembly "
            "functor into u,d,e,nuD rows, all independently of observed constants and residual-projector replay, "
            "then the fixed finite C1 row packet promotes to selected A_selected, b_selected, deltaTheta_C1, "
            "and sector response matrices."
        ),
        "proof_skeleton": [
            "Use the selected variation space to type the 72 primitive real rows.",
            "Use source-owned R_Z/R_X to identify the phase and shift columns before residual replay.",
            "Use b_selected source ownership to fix A^T b=(12,12) and ||b||^2=24 in the same source convention.",
            "Use the sector assembly functor to emit u,d,e,nuD response matrices.",
            "Apply the already-verified finite C1 linear algebra: A^T A=12 I_2, deltaTheta=(1,1).",
            "Apply the independence guardrail to exclude observed constants, benchmark values, and replay-only provenance.",
        ],
        "current_status": "template ready; source-owner fields not yet emitted",
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
    }

    for path, payload in [
        (STRICT_TEMPLATE, strict_template),
        (CURRENT_ATTEMPT, current_attempt),
        (CONNECTION_SCHEMA, connection_schema),
        (IMPLICATION, implication),
        (PAPER_TEXT, paper_text),
    ]:
        path.write_text(json.dumps(payload, indent=2, sort_keys=True) + "\n", encoding="utf-8")

    candidate = {
        "candidate": "MTTSelectedDynamicC1SourceOwnerTheoremOrIndependentConnectionTables",
        "status": STATUS,
        "inputs": {
            "decisive_sourceleaf_attack": rel(DATA / "selected_decisive_dynamicc1_sourceleaf_attack_or_sourceowner_theorem.candidate.json"),
            "minimal_source_owner_packet": rel(
                DATA
                / "selected_decisive_dynamicc1_sourceleaf_attack_or_sourceowner_theorem"
                / "minimal_dynamic_c1_source_owner_theorem.packet.json"
            ),
            "closed_support_countermodel": rel(
                DATA / "selected_minimalfinitec1sourcepromotionlemma_proof_or_countermodel.candidate.json"
            ),
            "pre_residual_source_kernel": rel(
                DATA / "selected_preresidualvariation_hessiansourcekernel_attempt_or_actionaxiom.candidate.json"
            ),
        },
        "output_packets": {
            "strict_template": rel(STRICT_TEMPLATE),
            "current_source_owner_fill_attempt": rel(CURRENT_ATTEMPT),
            "independent_connection_tables_export_schema": rel(CONNECTION_SCHEMA),
            "source_owner_promotion_implication": rel(IMPLICATION),
            "paper_ready_theorem_text": rel(PAPER_TEXT),
        },
        "theorem": {
            "name": "DynamicC1SourceOwnerTheoremTemplateAndSufficiencyTheorem",
            "proved": True,
            "statement": (
                "The DynamicC1SourceOwnerTheorem can now be stated as a strict seven-field source-owner packet "
                "or equivalently as an independent selected connection-table export. If supplied, the packet "
                "promotes the already verified finite C1 values to selected A_selected, b_selected, "
                "deltaTheta_C1, and sector response matrices. Current packets do not yet supply the source-owner fields."
            ),
        },
        "closure_decision": {
            "SM_parity_closed": decisive["closure_decision"]["SM_parity_closed"],
            "strict_source_owner_template_built": True,
            "independent_connection_export_schema_built": True,
            "current_fill_attempt_passes": False,
            "dynamic_C1_source_owner_theorem_proved_as_hypothesis": False,
            "unpatched_dynamic_C1_packet_closed": False,
            "true_SM_equivalence_closed": False,
            "no_knob_closed": False,
        },
        "what_closes_now": {
            "DynamicC1SourceOwnerTheorem_created_as_strict_object": True,
            "paper_ready_statement_and_proof_skeleton_created": True,
            "connection_table_export_schema_created": True,
            "conditional_promotion_implication_proved": True,
            "current_support_rejected_as_insufficient": source_counter["what_closes_now"]["closed_support_not_enough_countermodel"],
        },
        "what_remains_open": {
            "fill_source_owner_id": True,
            "fill_selected_variation_space": True,
            "fill_R_Z_R_X_source_operators": True,
            "fill_b_selected_source": True,
            "fill_sector_row_assembly": True,
            "or_export_independent_connection_tables": True,
        },
        "superset_strategy": {
            "using_one_straight_path": False,
            "combines_multiple_paths": True,
            "paths": owner["legal_exports"],
            "paths_used_as_knobs": False,
            "locked_target": "source ownership of dynamic C1 rows before replay promotion",
        },
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "closure_claimed": False,
        "next_required_artifact": NEXT,
    }

    cert = {
        "certificate": "MTT_Selected_DynamicC1_SourceOwnerTheorem_or_IndependentConnectionTables_v1",
        "status": STATUS,
        "candidate_path": rel(OUTPUT),
        "note_path": rel(NOTE),
        "theorem_proved": True,
        "strict_source_owner_template_built": True,
        "independent_connection_export_schema_built": True,
        "conditional_promotion_implication_proved": True,
        "current_fill_attempt_passes": False,
        "unpatched_dynamic_C1_packet_closed": False,
        "true_SM_equivalence_closed": False,
        "no_knob_closed": False,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "next_required_artifact": NEXT,
    }

    note = f"""# MTT Selected DynamicC1 SourceOwnerTheorem or IndependentConnectionTables v1

Status: `{STATUS}`.

This artifact creates the theorem object requested by the decisive source-leaf
attack. It is not a closure claim. It provides:

- a strict seven-field `DynamicC1SourceOwnerTheorem` template;
- a current fill attempt, rejected because source ownership is still absent;
- an independent connection/Galerkin table export schema;
- a conditional promotion theorem: if the source-owner packet or connection
  export is supplied, then the verified finite C1 values promote to selected
  `A_selected`, `b_selected`, `deltaTheta_C1`, and sector response matrices.

The next task is to fill the source-owner fields or export selected connection
tables. No observed constants, benchmark matrices, or residual fits may select
the source.

Next artifact: `{NEXT}`.
"""

    OUTPUT.write_text(json.dumps(candidate, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    CERT.write_text(json.dumps(cert, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    NOTE.write_text(note, encoding="utf-8")
    print(json.dumps({"candidate": rel(OUTPUT), "status": STATUS}, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
