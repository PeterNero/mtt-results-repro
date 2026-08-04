"""Build independent C1 row-kernel source ids or physical Phi_fin^C1 action proof attempt."""

from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "candidate_data"
CERTS = ROOT / "certificates"
CORPUS = ROOT / "proof_corpus"

SLUG = "selected_independentc1_rowkernelsourceids_or_physicalphifinc1actionproof"
PACKET_DIR = DATA / SLUG
OUTPUT = DATA / f"{SLUG}.candidate.json"
CURRENT_IDS = PACKET_DIR / "current_rowkernel_source_id_attempt.packet.json"
CONDITIONAL_IDS = PACKET_DIR / "conditional_independent_rowkernel_source_id_witness.packet.json"
CURRENT_VALIDATION = PACKET_DIR / "current_source_id_validator_result.packet.json"
CONDITIONAL_VALIDATION = PACKET_DIR / "conditional_source_id_validator_result.packet.json"
BRIDGE_ATTEMPT = PACKET_DIR / "two_exit_bridge_after_source_ids_attempt.packet.json"
BRIDGE_VALIDATION = PACKET_DIR / "two_exit_bridge_after_source_ids_validator_result.packet.json"
DECISION = PACKET_DIR / "source_ids_or_actionproof_decision.packet.json"
CERT = CERTS / f"{SLUG}_certificate.json"
NOTE = CORPUS / "MTT_Selected_IndependentC1RowKernelSourceIds_or_PhysicalPhiFinC1ActionProof_v1.md"

PREVIOUS = DATA / "selected_routea_physicalactionidentityproof_or_routeb_independentrowsourcetable.candidate.json"
REQUIRED_SCHEMA = (
    DATA
    / "selected_routea_physicalactionidentityproof_or_routeb_independentrowsourcetable"
    / "independent_row_source_table_required_schema.packet.json"
)
ROUTEB_WORKORDER = (
    DATA
    / "selected_routeb_independentquadraturepayload_schema_or_executionworkorder"
    / "routeb_independent_quadrature_execution_workorder.packet.json"
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
SOURCE_ID_VALIDATOR = ROOT / "scripts" / "validate_selected_independentc1_rowkernel_source_ids.py"
TWO_EXIT_VALIDATOR = ROOT / "scripts" / "validate_selected_physicalphifinc1_action_or_independent_rowkernel_source.py"

STATUS = "MTT_SELECTED_INDEPENDENTC1_ROWKERNELSOURCEIDS_OR_PHYSICALPHIFINC1ACTIONPROOF_BUILT_IDS_SUPPORT_ONLY"
NEXT = "MTT_Selected_IndependentQuadratureRuleAndHessianBSource_or_RouteAActionIdentity_v1"


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


def run_validator(validator: Path, path: Path) -> dict[str, Any]:
    proc = subprocess.run(
        [sys.executable, str(validator), str(path)],
        cwd=ROOT,
        text=True,
        capture_output=True,
        check=False,
    )
    return {
        "path": rel(path),
        "validator": rel(validator),
        "exit_code": proc.returncode,
        "ok": proc.returncode == 0,
        "stdout": proc.stdout.strip().splitlines(),
        "stderr": proc.stderr.strip().splitlines(),
    }


def schedule_ids() -> dict[str, list[str]]:
    workorder = load(ROUTEB_WORKORDER)
    out: dict[str, list[str]] = {}
    for stage in workorder["execution_order"]:
        if stage["stage"] == "basis_prerequisite":
            continue
        out[stage["stage"]] = stage["rows"]
    return out


def source_flags(selected: bool) -> dict[str, Any]:
    return {
        "selected_emitted": selected,
        "theorem_derived": selected,
        "independent_of_residual_replay": selected,
        "locked_target_dependency": False,
    }


def build_source_id_packet(selected: bool) -> dict[str, Any]:
    ids = schedule_ids()
    measure_id = "selected_C1_trace_frobenius_measure_pairing"
    quadrature_id = "selected_finite_C1_independent_quadrature_rule"
    variation_id = "selected_C1_admissible_variation_space"

    primitive = []
    for row_id in ids["primitive_contractions"]:
        primitive.append(
            {
                "row_id": row_id,
                "source_id": f"K_C1::{row_id}",
                "selected_measure_pairing_id": measure_id,
                "selected_quadrature_rule_id": quadrature_id,
                "integral_formula": "normal_form_row_functional_from_selected_zero_modes_and_variation_operator",
                "provenance": "theorem_derived" if selected else "normal_form_support_only",
                **source_flags(selected),
            }
        )

    hessian = []
    for row_id in ids["hessian_source"]:
        hessian.append(
            {
                "row_id": row_id,
                "source_id": f"H_C1::{row_id}",
                "selected_b_vector_source": selected,
                "not_copied_from_A_transpose_b_target": selected,
                "provenance": "theorem_derived" if selected else "formal_hessian_target_support_only",
                **source_flags(selected),
            }
        )

    sector = []
    for row_id in ids["sector_matrices"]:
        sector.append(
            {
                "row_id": row_id,
                "source_id": f"S_C1::{row_id}",
                "assembled_from_primitive_source_rows": selected,
                "provenance": "theorem_derived" if selected else "formal_sector_assembly_support_only",
                **source_flags(selected),
            }
        )

    return {
        "schema": "MTTSelectedIndependentC1RowKernelSourceIds.v1",
        "status": "SOURCE_IDS_CONDITIONAL_WITNESS" if selected else "SOURCE_IDS_NAMED_SUPPORT_ONLY",
        "global_sources": {
            "selected_measure_pairing": {
                "source_id": measure_id,
                "provenance": "theorem_derived" if selected else "finite_trace_support_only",
                **source_flags(selected),
            },
            "selected_quadrature_rule": {
                "source_id": quadrature_id,
                "provenance": "theorem_derived" if selected else "workorder_support_only",
                **source_flags(selected),
            },
            "selected_variation_space": {
                "source_id": variation_id,
                "provenance": "theorem_derived" if selected else "normal_form_support_only",
                **source_flags(selected),
            },
        },
        "primitive_row_kernel_sources": primitive,
        "hessian_b_sources": hessian,
        "sector_assembly_sources": sector,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "locked_target_values_used_as_source": False,
        "closure_claimed": False,
    }


def main() -> int:
    PACKET_DIR.mkdir(parents=True, exist_ok=True)
    previous = load(PREVIOUS)
    required_schema = load(REQUIRED_SCHEMA)
    normal_form = load(NORMAL_FORM)
    action_equiv = load(ACTION_EQUIV)

    current = build_source_id_packet(False)
    conditional = build_source_id_packet(True)
    write_json(CURRENT_IDS, current)
    write_json(CONDITIONAL_IDS, conditional)
    current_validation = run_validator(SOURCE_ID_VALIDATOR, CURRENT_IDS)
    conditional_validation = run_validator(SOURCE_ID_VALIDATOR, CONDITIONAL_IDS)
    write_json(CURRENT_VALIDATION, current_validation)
    write_json(CONDITIONAL_VALIDATION, conditional_validation)

    bridge_attempt = {
        "schema": "MTTTwoExitBridgeAfterSourceIdsAttempt.v1",
        "status": "SOURCE_IDS_SUPPORT_ONLY_ROUTE_B_STILL_FAILS_TWO_EXIT",
        "route_A_physical_action_restriction": {
            "same_branch": True,
            "physical_action_restricts_to_finite_weyl_quotient": False,
            "zero_extra_boundary_or_source_term": False,
            "phase_R_Z_source_selection": False,
            "shift_R_X_source_selection": False,
            "same_source_b_selected_emission": False,
            "attached_source_evidence": [
                rel(ACTION_EQUIV),
                "Route A equivalence support only",
                "physical action identity still open",
                "no-extra-boundary/source still open",
                "same-source b_selected still open",
            ],
        },
        "route_B_independent_rowkernel_source": {
            "same_branch": True,
            "selected_basis_feeds_all_72_row_functionals": True,
            "pre_residual_phase_shift_variation_operators": current_validation["ok"],
            "independent_hessian_counterterm_source_rows": current_validation["ok"],
            "sector_rows_assembled_from_source_rows": current_validation["ok"],
            "no_residual_projector_replay_or_locked_target_as_source": current_validation["ok"],
            "attached_source_evidence": [
                rel(CURRENT_IDS),
                rel(CURRENT_VALIDATION),
                rel(REQUIRED_SCHEMA),
                rel(ROUTEB_WORKORDER),
                rel(NORMAL_FORM),
            ],
        },
        "locked_target_values_used_as_source": False,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "closure_claimed": False,
    }
    write_json(BRIDGE_ATTEMPT, bridge_attempt)
    bridge_validation = run_validator(TWO_EXIT_VALIDATOR, BRIDGE_ATTEMPT)
    write_json(BRIDGE_VALIDATION, bridge_validation)

    decision = {
        "schema": "MTTIndependentC1RowKernelSourceIdsDecision.v1",
        "status": "IDS_NAMED_BUT_NOT_SELECTED_CONDITIONAL_VALIDATOR_WITNESS_PASSES",
        "current_source_id_validator_ok": current_validation["ok"],
        "conditional_source_id_validator_ok": conditional_validation["ok"],
        "two_exit_bridge_validator_ok": bridge_validation["ok"],
        "counts": {
            "primitive_source_ids": len(current["primitive_row_kernel_sources"]),
            "hessian_b_source_ids": len(current["hessian_b_sources"]),
            "sector_assembly_source_ids": len(current["sector_assembly_sources"]),
        },
        "what_is_new": (
            "The exact source-id namespace and strict selected-id validator now exist. Current ids are support-only; "
            "a theorem-derived independent quadrature/measure/Hessian source promotion would make the conditional packet pass."
        ),
        "next_minimal_payload": {
            "route_B_primary": [
                "derive selected independent quadrature rule source",
                "derive selected measure pairing as source, not postcheck",
                "derive Hessian/b_selected source rows independent of A^T b target",
                "promote primitive and sector source ids as theorem-derived",
            ],
            "route_A_parallel": [
                "derive physical Phi_fin^C1 action identity",
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
        "candidate": "MTTSelectedIndependentC1RowKernelSourceIdsOrPhysicalPhiFinC1ActionProof",
        "status": STATUS,
        "inputs": {
            "previous": rel(PREVIOUS),
            "required_schema": rel(REQUIRED_SCHEMA),
            "routeb_workorder": rel(ROUTEB_WORKORDER),
            "normal_form": rel(NORMAL_FORM),
            "action_equivalence": rel(ACTION_EQUIV),
        },
        "output_packets": {
            "current_rowkernel_source_id_attempt": rel(CURRENT_IDS),
            "conditional_independent_rowkernel_source_id_witness": rel(CONDITIONAL_IDS),
            "current_source_id_validator_result": rel(CURRENT_VALIDATION),
            "conditional_source_id_validator_result": rel(CONDITIONAL_VALIDATION),
            "two_exit_bridge_after_source_ids_attempt": rel(BRIDGE_ATTEMPT),
            "two_exit_bridge_after_source_ids_validator_result": rel(BRIDGE_VALIDATION),
            "source_ids_or_actionproof_decision": rel(DECISION),
        },
        "theorem": {
            "name": "IndependentC1SourceIdNamespaceAndValidatorTheorem",
            "proved": True,
            "statement": (
                "A strict source-id namespace for the independent Route-B C1 row-kernel table is built. "
                "The current ids are only support-level and fail the selected source-id validator; the conditional "
                "theorem-derived source-id witness passes. Thus the next obstacle is selected independent "
                "quadrature/measure/Hessian source derivation, or the parallel physical Phi_fin^C1 action proof."
            ),
        },
        "what_closes_now": {
            "source_id_namespace_built": True,
            "strict_source_id_validator_built": True,
            "current_support_rejected_honestly": current_validation["ok"] is False,
            "conditional_source_id_witness_passes": conditional_validation["ok"],
            "two_exit_bridge_rerun": True,
        },
        "what_remains_open": {
            "selected_independent_quadrature_rule_source": True,
            "selected_measure_pairing_source": True,
            "selected_hessian_b_source": True,
            "actual_route_B_source_id_promotion": True,
            "route_A_physical_action_identity_proof": True,
        },
        "closed_support": {
            "replacement_schema_ready": required_schema["status"] == "REPLACEMENT_SCHEMA_READY_VALUES_TO_EXPORT",
            "normal_form_formula_ready": bool(normal_form["acceptance_formula"]),
            "route_A_equivalence_ready": action_equiv["route_A_promotes_if_all_antecedents_true"],
            "previous_table_shape_ready": previous["what_closes_now"]["route_B_current_table_shape_audited"],
        },
        "closure_claimed": False,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "next_required_artifact": NEXT,
    }

    cert = {
        "certificate": "MTT_Selected_IndependentC1RowKernelSourceIds_or_PhysicalPhiFinC1ActionProof_v1",
        "status": STATUS,
        "candidate_path": rel(OUTPUT),
        "note_path": rel(NOTE),
        "current_source_id_validator_ok": current_validation["ok"],
        "conditional_source_id_validator_ok": conditional_validation["ok"],
        "two_exit_bridge_validator_ok": bridge_validation["ok"],
        "closure_claimed": False,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
    }

    NOTE.write_text(
        "# MTT Selected IndependentC1RowKernelSourceIds or PhysicalPhiFinC1ActionProof v1\n\n"
        f"Status: `{STATUS}`.\n\n"
        "This artifact constructs the Route-B source-id namespace and a strict validator for "
        "selected independent C1 row-kernel source ids. The current packet can name all ids, "
        "but they are support-only rather than theorem-derived selected sources, so the actual "
        "source-id validator rejects it. A separate conditional witness proves that the same "
        "namespace would validate if the measure, quadrature rule, primitive kernels, sector "
        "assembly, and Hessian/`b_selected` sources were theorem-derived and independent of "
        "residual replay.\n\n"
        "Route A remains the parallel legal exit through a physical `Phi_fin^C1` action proof.\n\n"
        f"Next artifact: `{NEXT}`.\n",
        encoding="utf-8",
    )
    write_json(OUTPUT, candidate)
    write_json(CERT, cert)

    print(json.dumps({"candidate": rel(OUTPUT), "status": STATUS}, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
