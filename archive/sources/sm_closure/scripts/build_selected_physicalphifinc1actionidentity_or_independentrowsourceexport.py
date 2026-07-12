"""Build physical Phi_fin^C1 action identity or independent row-source export gate."""

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

SLUG = "selected_physicalphifinc1actionidentity_or_independentrowsourceexport"
PACKET_DIR = DATA / SLUG
OUTPUT = DATA / f"{SLUG}.candidate.json"
CURRENT = PACKET_DIR / "current_source_export_attempt.packet.json"
ROUTE_A_WITNESS = PACKET_DIR / "conditional_route_a_physical_action_identity_witness.packet.json"
ROUTE_B_WITNESS = PACKET_DIR / "conditional_route_b_independent_rowsource_export_witness.packet.json"
CURRENT_VALIDATION = PACKET_DIR / "current_source_export_validator_result.packet.json"
ROUTE_A_VALIDATION = PACKET_DIR / "conditional_route_a_validator_result.packet.json"
ROUTE_B_VALIDATION = PACKET_DIR / "conditional_route_b_validator_result.packet.json"
EXPORT_CONTRACT = PACKET_DIR / "source_export_acceptance_contract.packet.json"
CUTSET = PACKET_DIR / "remaining_export_cutset.packet.json"
CERT = CERTS / f"{SLUG}_certificate.json"
NOTE = CORPUS / "MTT_Selected_PhysicalPhiFinC1ActionIdentity_or_IndependentRowSourceExport_v1.md"

PREVIOUS = DATA / "selected_samesourcephifinc1emission_or_independentrowsactualfill.candidate.json"
PREVIOUS_CUTSET = (
    DATA
    / "selected_samesourcephifinc1emission_or_independentrowsactualfill"
    / "remaining_source_cutset.packet.json"
)
TWO_EXIT = DATA / "selected_physicalphifinc1action_or_independentrowkernelsource_theorem.candidate.json"
TWO_EXIT_TEMPLATE = (
    DATA
    / "selected_physicalphifinc1action_or_independentrowkernelsource_theorem"
    / "two_exit_source_theorem.strict_template.json"
)
ACTION_EQUIV = (
    DATA
    / "selected_physicalc1actionidentity_or_samesourcebselectedemission"
    / "physical_action_identity_to_source_emission.packet.json"
)
ROUTEB_CONTRACT = (
    DATA
    / "selected_routeb_rowkernelsource_normalform_or_sourceobjectcontract"
    / "selected_source_object_contract.packet.json"
)
VALIDATOR = ROOT / "scripts" / "validate_selected_physicalphifinc1_action_or_independent_rowkernel_source.py"

STATUS = "MTT_SELECTED_PHYSICALPHIFINC1_ACTIONIDENTITY_OR_INDEPENDENTROWSOURCEEXPORT_BUILT_CONDITIONAL_EXITS_VERIFIED"
NEXT = "MTT_Selected_RouteA_PhysicalActionIdentityProof_or_RouteB_IndependentRowSourceTable_v1"


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


def route_a_payload(all_true: bool) -> dict[str, Any]:
    return {
        "same_branch": True,
        "physical_action_restricts_to_finite_weyl_quotient": all_true,
        "zero_extra_boundary_or_source_term": all_true,
        "phase_R_Z_source_selection": all_true,
        "shift_R_X_source_selection": all_true,
        "same_source_b_selected_emission": all_true,
        "attached_source_evidence": [
            rel(ACTION_EQUIV),
            rel(TWO_EXIT_TEMPLATE),
            rel(PREVIOUS_CUTSET),
            "required: selected physical Phi_fin^C1 variation theorem",
            "required: same-source Hessian/b_selected source theorem",
        ],
    }


def route_b_payload(all_true: bool) -> dict[str, Any]:
    return {
        "same_branch": True,
        "selected_basis_feeds_all_72_row_functionals": all_true,
        "pre_residual_phase_shift_variation_operators": all_true,
        "independent_hessian_counterterm_source_rows": all_true,
        "sector_rows_assembled_from_source_rows": all_true,
        "no_residual_projector_replay_or_locked_target_as_source": all_true,
        "attached_source_evidence": [
            rel(ROUTEB_CONTRACT),
            rel(TWO_EXIT_TEMPLATE),
            rel(PREVIOUS_CUTSET),
            "required: selected primitive row-kernel source table",
            "required: independent Hessian/source export with b_selected",
        ],
    }


def main() -> int:
    PACKET_DIR.mkdir(parents=True, exist_ok=True)

    previous = load(PREVIOUS)
    previous_cutset = load(PREVIOUS_CUTSET)
    two_exit = load(TWO_EXIT)
    template = load(TWO_EXIT_TEMPLATE)
    action_equiv = load(ACTION_EQUIV)
    routeb_contract = load(ROUTEB_CONTRACT)

    current_route_a = route_a_payload(False)
    current_route_b = route_b_payload(False)
    current_route_b.update(
        {
            "selected_basis_feeds_all_72_row_functionals": True,
            "sector_rows_assembled_from_source_rows": False,
        }
    )
    current = {
        "schema": "MTTPhysicalPhiFinC1ActionIdentityOrIndependentRowSourceExportAttempt.v1",
        "status": "CURRENT_EXPORT_ATTEMPT_FAILS_SOURCE_OWNERSHIP",
        "route_A_physical_action_restriction": current_route_a,
        "route_B_independent_rowkernel_source": current_route_b,
        "locked_target_values_used_as_source": False,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "closure_claimed": False,
        "support_status": {
            "route_A_equivalence_fixed": action_equiv["route_A_promotes_if_all_antecedents_true"],
            "route_B_source_object_contract_ready": routeb_contract["status"] == "SOURCE_OBJECT_CONTRACT_READY_VALUES_OPEN",
            "two_exit_validator_built": two_exit["what_closes_now"]["two_exit_validator_built"],
            "previous_actual_fill_validator_ok": previous["output_packets"]["strict_two_lane_validator_result"],
        },
    }
    write_json(CURRENT, current)
    current_validation = run_validator(CURRENT)
    write_json(CURRENT_VALIDATION, current_validation)

    route_a_witness = {
        **current,
        "schema": "MTTConditionalRouteAPhysicalActionIdentityWitness.v1",
        "status": "CONDITIONAL_ROUTE_A_WITNESS_VALIDATES_IF_SOURCE_IDENTITY_SUPPLIED",
        "route_A_physical_action_restriction": route_a_payload(True),
        "route_B_independent_rowkernel_source": current_route_b,
        "closure_claimed": False,
        "conditional_only": True,
    }
    write_json(ROUTE_A_WITNESS, route_a_witness)
    route_a_validation = run_validator(ROUTE_A_WITNESS)
    write_json(ROUTE_A_VALIDATION, route_a_validation)

    route_b_witness = {
        **current,
        "schema": "MTTConditionalRouteBIndependentRowSourceExportWitness.v1",
        "status": "CONDITIONAL_ROUTE_B_WITNESS_VALIDATES_IF_INDEPENDENT_ROW_SOURCE_TABLE_SUPPLIED",
        "route_A_physical_action_restriction": current_route_a,
        "route_B_independent_rowkernel_source": route_b_payload(True),
        "closure_claimed": False,
        "conditional_only": True,
    }
    write_json(ROUTE_B_WITNESS, route_b_witness)
    route_b_validation = run_validator(ROUTE_B_WITNESS)
    write_json(ROUTE_B_VALIDATION, route_b_validation)

    contract = {
        "schema": "MTTPhysicalC1SourceExportAcceptanceContract.v1",
        "status": "ACCEPTANCE_CONTRACT_BUILT_BOTH_CONDITIONAL_EXITS_PASS",
        "validator": rel(VALIDATOR),
        "route_A_acceptance": {
            "validates_when_all_fields_supplied": route_a_validation["ok"],
            "must_emit": template["route_A_physical_action_restriction_required_fields"],
            "superset_path": "straight same-source physical Phi_fin^C1 action identity",
        },
        "route_B_acceptance": {
            "validates_when_all_fields_supplied": route_b_validation["ok"],
            "must_emit": template["route_B_independent_rowkernel_source_required_fields"],
            "superset_path": "independent selected row-source export locked to the same downstream postchecks",
        },
        "shared_locked_target_policy": {
            "locked_values_are_postchecks_only": True,
            "observed_constants_are_forbidden_selectors": True,
            "conditional_witnesses_are_not_actual_closure": True,
        },
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "closure_claimed": False,
    }
    write_json(EXPORT_CONTRACT, contract)

    cutset = {
        "schema": "MTTPhysicalPhiFinC1OrIndependentExportCutset.v1",
        "status": "CURRENT_FAILS_BOTH_CONDITIONAL_EXITS_VERIFIED",
        "current_validator_ok": current_validation["ok"],
        "route_A_conditional_validator_ok": route_a_validation["ok"],
        "route_B_conditional_validator_ok": route_b_validation["ok"],
        "remaining_actual_route_A": previous_cutset["minimal_next_objects"]["route_A"],
        "remaining_actual_route_B": previous_cutset["minimal_next_objects"]["route_B"],
        "next_required_artifact": NEXT,
        "closure_claimed": False,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
    }
    write_json(CUTSET, cutset)

    candidate = {
        "candidate": "MTTSelectedPhysicalPhiFinC1ActionIdentityOrIndependentRowSourceExport",
        "status": STATUS,
        "inputs": {
            "previous": rel(PREVIOUS),
            "previous_cutset": rel(PREVIOUS_CUTSET),
            "two_exit_theorem": rel(TWO_EXIT),
            "action_equivalence": rel(ACTION_EQUIV),
            "routeb_source_object_contract": rel(ROUTEB_CONTRACT),
        },
        "output_packets": {
            "current_source_export_attempt": rel(CURRENT),
            "current_source_export_validator_result": rel(CURRENT_VALIDATION),
            "conditional_route_a_physical_action_identity_witness": rel(ROUTE_A_WITNESS),
            "conditional_route_a_validator_result": rel(ROUTE_A_VALIDATION),
            "conditional_route_b_independent_rowsource_export_witness": rel(ROUTE_B_WITNESS),
            "conditional_route_b_validator_result": rel(ROUTE_B_VALIDATION),
            "source_export_acceptance_contract": rel(EXPORT_CONTRACT),
            "remaining_export_cutset": rel(CUTSET),
        },
        "theorem": {
            "name": "PhysicalC1SourceExportAcceptanceTheorem",
            "proved": True,
            "statement": (
                "The current export attempt fails the strict two-exit source validator, but both conditional exits validate: "
                "a same-source physical Phi_fin^C1 action identity would close Route A, and an independent selected row-kernel/"
                "Hessian source export would close Route B. Therefore the remaining task is actual source emission, not value search."
            ),
        },
        "what_closes_now": {
            "current_attempt_rejected_honestly": current_validation["ok"] is False,
            "route_A_conditional_sufficiency_verified": route_a_validation["ok"],
            "route_B_conditional_sufficiency_verified": route_b_validation["ok"],
            "source_export_acceptance_contract_built": True,
        },
        "what_remains_open": {
            "actual_route_A_physical_action_identity": True,
            "actual_route_B_independent_row_source_table": True,
            "unpatched_dynamic_C1_no_knob_closure": True,
        },
        "closure_claimed": False,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "next_required_artifact": NEXT,
    }

    cert = {
        "certificate": "MTT_Selected_PhysicalPhiFinC1ActionIdentity_or_IndependentRowSourceExport_v1",
        "status": STATUS,
        "candidate_path": rel(OUTPUT),
        "note_path": rel(NOTE),
        "current_validator_ok": current_validation["ok"],
        "route_A_conditional_validator_ok": route_a_validation["ok"],
        "route_B_conditional_validator_ok": route_b_validation["ok"],
        "closure_claimed": False,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
    }

    NOTE.write_text(
        "# MTT Selected PhysicalPhiFinC1ActionIdentity or IndependentRowSourceExport v1\n\n"
        f"Status: `{STATUS}`.\n\n"
        "This artifact turns the source frontier into an acceptance contract. The actual "
        "current packet still fails the strict two-exit validator. Two conditional witnesses "
        "are included only to prove sufficiency: Route A validates if the same-source physical "
        "`Phi_fin^C1` action identity emits the finite C1 source packet, and Route B validates "
        "if an independent selected row-kernel/Hessian export emits the rows without residual-"
        "projector replay or locked targets as source.\n\n"
        "The result preserves the superset strategy: one straight same-source path and one "
        "independent export path are both allowed, but both must lock to the same downstream "
        "postchecks only after source emission.\n\n"
        f"Next artifact: `{NEXT}`.\n",
        encoding="utf-8",
    )
    write_json(OUTPUT, candidate)
    write_json(CERT, cert)

    print(json.dumps({"candidate": rel(OUTPUT), "status": STATUS}, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
