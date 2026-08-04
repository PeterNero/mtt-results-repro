"""Build Route-A physical action identity proof or Route-B independent row-source table attempt."""

from __future__ import annotations

import json
import subprocess
import sys
from collections import Counter
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "candidate_data"
CERTS = ROOT / "certificates"
CORPUS = ROOT / "proof_corpus"

SLUG = "selected_routea_physicalactionidentityproof_or_routeb_independentrowsourcetable"
PACKET_DIR = DATA / SLUG
OUTPUT = DATA / f"{SLUG}.candidate.json"
CURRENT_TABLE = PACKET_DIR / "route_b_current_110_row_source_table_attempt.packet.json"
PROVENANCE_AUDIT = PACKET_DIR / "route_b_row_provenance_audit.packet.json"
REPLACEMENT_SCHEMA = PACKET_DIR / "independent_row_source_table_required_schema.packet.json"
TWO_EXIT_ATTEMPT = PACKET_DIR / "two_exit_current_after_table_attempt.packet.json"
VALIDATION = PACKET_DIR / "two_exit_current_after_table_validator_result.packet.json"
DECISION = PACKET_DIR / "routea_or_routeb_next_decision.packet.json"
CERT = CERTS / f"{SLUG}_certificate.json"
NOTE = CORPUS / "MTT_Selected_RouteA_PhysicalActionIdentityProof_or_RouteB_IndependentRowSourceTable_v1.md"

PREVIOUS = DATA / "selected_physicalphifinc1actionidentity_or_independentrowsourceexport.candidate.json"
EXPORT_CONTRACT = (
    DATA
    / "selected_physicalphifinc1actionidentity_or_independentrowsourceexport"
    / "source_export_acceptance_contract.packet.json"
)
ROUTEB_ROWS = (
    DATA
    / "selected_routeb_bestcurrentpayloadfill_or_independentsourcegap"
    / "routeb_best_current_payload_fill_attempt.packet.json"
)
ROUTEB_GAP = (
    DATA
    / "selected_routeb_bestcurrentpayloadfill_or_independentsourcegap"
    / "routeb_independent_source_gap.packet.json"
)
NORMAL_FORM = (
    DATA
    / "selected_routeb_rowkernelsource_normalform_or_sourceobjectcontract"
    / "primitive_row_kernel_source_normal_form.packet.json"
)
ACTION_EQUIV = (
    DATA
    / "selected_physicalc1actionidentity_or_samesourcebselectedemission"
    / "physical_action_identity_to_source_emission.packet.json"
)
VALIDATOR = ROOT / "scripts" / "validate_selected_physicalphifinc1_action_or_independent_rowkernel_source.py"

STATUS = "MTT_SELECTED_ROUTEA_ACTIONIDENTITY_OR_ROUTEB_ROWSOURCETABLE_BUILT_TABLE_PROVENANCE_OPEN"
NEXT = "MTT_Selected_IndependentC1RowKernelSourceIds_or_PhysicalPhiFinC1ActionProof_v1"


def rel(path: Path) -> str:
    try:
        return str(path.relative_to(ROOT)).replace("\\", "/")
    except ValueError:
        return str(path)


def load(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def write_json(path: Path, payload: dict[str, Any]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(payload, indent=2, sort_keys=True) + "\n", encoding="utf-8")


def run_validator(path: Path) -> dict[str, Any]:
    proc = subprocess.run(
        [sys.executable, str(VALIDATOR), str(path)],
        cwd=ROOT,
        text=True,
        capture_output=True,
        check=False,
    )
    return {
        "path": rel(path),
        "exit_code": proc.returncode,
        "ok": proc.returncode == 0,
        "stdout": proc.stdout.strip().splitlines(),
        "stderr": proc.stderr.strip().splitlines(),
    }


def main() -> int:
    PACKET_DIR.mkdir(parents=True, exist_ok=True)

    previous = load(PREVIOUS)
    contract = load(EXPORT_CONTRACT)
    rows_packet = load(ROUTEB_ROWS)
    routeb_gap = load(ROUTEB_GAP)
    normal_form = load(NORMAL_FORM)
    action_equiv = load(ACTION_EQUIV)
    rows = rows_packet["rows"]

    stage_counts = Counter(row["stage"] for row in rows)
    replay_dependency_count = sum(1 for row in rows if row.get("residual_replay_dependency") is True)
    independent_source_count = sum(1 for row in rows if row.get("independent_source_emitted") is True)
    missing_quadrature_count = sum(
        1 for row in rows if row.get("quadrature_rule_id") == "missing_selected_independent_quadrature_rule"
    )
    hessian_rows = [row for row in rows if row["stage"] == "hessian_source"]
    selected_b_rows = [row for row in hessian_rows if row.get("selected_b_vector_source")]

    current_table = {
        "schema": "MTTRouteBCurrent110RowSourceTableAttempt.v1",
        "status": "ALL_ROWS_PRESENT_BUT_REPLAY_BACKED_NOT_INDEPENDENT",
        "source": rel(ROUTEB_ROWS),
        "row_count": len(rows),
        "stage_counts": dict(sorted(stage_counts.items())),
        "all_rows_present": len(rows) == 110,
        "independent_source_emitted_count": independent_source_count,
        "residual_replay_dependency_count": replay_dependency_count,
        "missing_quadrature_rule_count": missing_quadrature_count,
        "hessian_source_row_count": len(hessian_rows),
        "selected_b_vector_source_row_count": len(selected_b_rows),
        "locked_target_values_used_as_source": rows_packet["locked_target_values_used_as_source"],
        "observed_data_used_as_selector": rows_packet["observed_data_used_as_selector"],
        "target_fitting_used": False,
        "closure_claimed": False,
    }
    write_json(CURRENT_TABLE, current_table)

    provenance_audit = {
        "schema": "MTTRouteBRowProvenanceAudit.v1",
        "status": "PROVENANCE_FAILS_INDEPENDENT_SOURCE_REQUIREMENT",
        "passes_independent_source_requirement": False,
        "failures": {
            "rows_still_residual_replay_backed": replay_dependency_count,
            "rows_without_independent_source_emission": len(rows) - independent_source_count,
            "rows_without_selected_independent_quadrature_rule": missing_quadrature_count,
            "hessian_rows_without_selected_b_vector_source": len(hessian_rows) - len(selected_b_rows),
            "packet_marks_locked_target_values_used_as_source": rows_packet["locked_target_values_used_as_source"],
        },
        "why_not_enough": (
            "The table is valuable as a complete 110-row postcheck, but it cannot serve as Route B "
            "source export because its kernel source ids and quadrature rule ids are replay markers."
        ),
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "closure_claimed": False,
    }
    write_json(PROVENANCE_AUDIT, provenance_audit)

    replacement_schema = {
        "schema": "MTTIndependentC1RowSourceTableRequiredSchema.v1",
        "status": "REPLACEMENT_SCHEMA_READY_VALUES_TO_EXPORT",
        "required_row_count": 110,
        "row_families": {
            "primitive_contractions": {
                "required_count": 72,
                "required_fields_per_row": [
                    "row_id",
                    "sector",
                    "variation_id",
                    "matrix_coordinate",
                    "selected_kernel_source_id",
                    "selected_measure_pairing_id",
                    "selected_quadrature_rule_id",
                    "integral_formula",
                    "value_or_interval",
                    "exactness_or_error_certificate",
                    "residual_projector_replay_dependency=false",
                    "locked_target_dependency=false",
                    "theorem_derived=true",
                ],
            },
            "hessian_source": {
                "required_count": 2,
                "required_fields_per_row": [
                    "variation_id",
                    "same_source_hessian_counterterm_id",
                    "selected_b_component_formula",
                    "selected_b_component_value_or_interval",
                    "not_copied_from_A_transpose_b_target",
                    "theorem_derived=true",
                ],
            },
            "sector_response": {
                "required_count": 36,
                "required_fields_per_row": [
                    "sector",
                    "matrix_coordinate",
                    "assembled_from_primitive_source_rows",
                    "selected_sector_functor_id",
                    "theorem_derived=true",
                ],
            },
        },
        "normal_form_formula": normal_form["acceptance_formula"],
        "forbidden_sources": [
            "canonical residual-projector replay",
            "locked A^T b, deltaTheta, or target residual values",
            "observed SM masses/mixings/constants",
            "benchmark matrices",
        ],
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
    }
    write_json(REPLACEMENT_SCHEMA, replacement_schema)

    two_exit_attempt = {
        "schema": "MTTRouteAOrRouteBCurrentAfterTableAttempt.v1",
        "status": "CURRENT_TABLE_IMPORTED_ROUTE_B_STILL_FAILS_SOURCE_VALIDATOR",
        "route_A_physical_action_restriction": {
            "same_branch": True,
            "physical_action_restricts_to_finite_weyl_quotient": False,
            "zero_extra_boundary_or_source_term": False,
            "phase_R_Z_source_selection": False,
            "shift_R_X_source_selection": False,
            "same_source_b_selected_emission": False,
            "attached_source_evidence": [
                rel(ACTION_EQUIV),
                rel(EXPORT_CONTRACT),
                "physical action identity equivalence support only",
                "finite boundary support only",
                "same-source b_selected still open",
            ],
        },
        "route_B_independent_rowkernel_source": {
            "same_branch": True,
            "selected_basis_feeds_all_72_row_functionals": True,
            "pre_residual_phase_shift_variation_operators": False,
            "independent_hessian_counterterm_source_rows": False,
            "sector_rows_assembled_from_source_rows": False,
            "no_residual_projector_replay_or_locked_target_as_source": False,
            "attached_source_evidence": [
                rel(CURRENT_TABLE),
                rel(PROVENANCE_AUDIT),
                rel(REPLACEMENT_SCHEMA),
                rel(NORMAL_FORM),
                rel(ROUTEB_GAP),
            ],
        },
        "locked_target_values_used_as_source": False,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "closure_claimed": False,
    }
    write_json(TWO_EXIT_ATTEMPT, two_exit_attempt)
    validation = run_validator(TWO_EXIT_ATTEMPT)
    write_json(VALIDATION, validation)

    decision = {
        "schema": "MTTRouteAOrRouteBNextDecision.v1",
        "status": "ROUTE_B_TABLE_SHAPE_FILLED_PROVENANCE_OPEN_ROUTE_A_STILL_PARALLEL",
        "route_B_table_shape_ready": current_table["all_rows_present"],
        "route_B_table_independent": False,
        "route_A_conditional_acceptance_known": contract["route_A_acceptance"]["validates_when_all_fields_supplied"],
        "route_B_conditional_acceptance_known": contract["route_B_acceptance"]["validates_when_all_fields_supplied"],
        "strict_validator_ok": validation["ok"],
        "next_minimal_payload": {
            "route_B_primary": [
                "replace replay kernel_source_id markers with selected row-kernel source ids",
                "emit selected independent quadrature/measure rule",
                "emit independent Hessian/source rows with b_selected not copied from target",
                "assemble sector rows from those source rows",
            ],
            "route_A_parallel": [
                "derive physical Phi_fin^C1 action restriction",
                "prove no extra physical boundary/source term",
                "emit same-source R_Z/R_X/b_selected",
            ],
        },
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "closure_claimed": False,
    }
    write_json(DECISION, decision)

    candidate = {
        "candidate": "MTTSelectedRouteAPhysicalActionIdentityProofOrRouteBIndependentRowSourceTable",
        "status": STATUS,
        "inputs": {
            "previous": rel(PREVIOUS),
            "source_export_contract": rel(EXPORT_CONTRACT),
            "routeb_best_current_rows": rel(ROUTEB_ROWS),
            "routeb_source_gap": rel(ROUTEB_GAP),
            "normal_form": rel(NORMAL_FORM),
            "action_equivalence": rel(ACTION_EQUIV),
        },
        "output_packets": {
            "route_b_current_110_row_source_table_attempt": rel(CURRENT_TABLE),
            "route_b_row_provenance_audit": rel(PROVENANCE_AUDIT),
            "independent_row_source_table_required_schema": rel(REPLACEMENT_SCHEMA),
            "two_exit_current_after_table_attempt": rel(TWO_EXIT_ATTEMPT),
            "two_exit_current_after_table_validator_result": rel(VALIDATION),
            "routea_or_routeb_next_decision": rel(DECISION),
        },
        "theorem": {
            "name": "RouteBRowTableProvenanceNoGoAndReplacementSchemaTheorem",
            "proved": True,
            "statement": (
                "The current Route-B 110-row table is complete as a value/postcheck table but fails as an independent "
                "source table because every row remains replay-backed and lacks selected independent row-kernel/quadrature "
                "source ids; the two Hessian rows also lack independent b_selected source emission. A replacement "
                "schema for the required independent source table is emitted, while Route A "
                "physical action identity remains the parallel legal exit."
            ),
        },
        "what_closes_now": {
            "route_B_current_table_shape_audited": True,
            "route_B_provenance_failure_counted": True,
            "independent_row_source_table_schema_emitted": True,
            "two_exit_validator_rerun": True,
        },
        "what_remains_open": {
            "route_A_physical_action_identity_proof": True,
            "route_B_independent_row_kernel_source_ids": True,
            "route_B_independent_hessian_b_source": True,
            "route_B_residual_replay_exclusion_certificate": True,
        },
        "closure_claimed": False,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "next_required_artifact": NEXT,
    }

    cert = {
        "certificate": "MTT_Selected_RouteA_PhysicalActionIdentityProof_or_RouteB_IndependentRowSourceTable_v1",
        "status": STATUS,
        "candidate_path": rel(OUTPUT),
        "note_path": rel(NOTE),
        "row_count": len(rows),
        "independent_source_emitted_count": independent_source_count,
        "residual_replay_dependency_count": replay_dependency_count,
        "strict_validator_ok": validation["ok"],
        "closure_claimed": False,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
    }

    NOTE.write_text(
        "# MTT Selected RouteA PhysicalActionIdentityProof or RouteB IndependentRowSourceTable v1\n\n"
        f"Status: `{STATUS}`.\n\n"
        "This artifact tries the concrete Route-B table path first. The current `110`-row "
        "table is complete as a postcheck object, but the provenance audit rejects it as an "
        "independent source table: the primitive and sector rows still carry replay/kernel "
        "placeholders, and the two Hessian rows still lack an independent `b_selected` export.\n\n"
        "The emitted replacement schema is the next constructive target. Route A remains the "
        "parallel legal path through a same-source physical `Phi_fin^C1` action identity.\n\n"
        f"Next artifact: `{NEXT}`.\n",
        encoding="utf-8",
    )
    write_json(OUTPUT, candidate)
    write_json(CERT, cert)

    print(json.dumps({"candidate": rel(OUTPUT), "status": STATUS}, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
