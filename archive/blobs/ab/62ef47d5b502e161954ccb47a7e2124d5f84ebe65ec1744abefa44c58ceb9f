"""Audit selected sector-transfer / overlap-derivative reconciliation packet."""

from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SLUG = "selected_selectedsectortransferoverlapderivative_or_rowlocalprefactoremission"
DATA = ROOT / "candidate_data" / f"{SLUG}.candidate.json"
PACKET_DIR = ROOT / "candidate_data" / SLUG
STEP73_IMPORT = PACKET_DIR / "step73_supersession_import.packet.json"
READINESS = PACKET_DIR / "sector_transfer_overlap_derivative_readiness.packet.json"
REEXECUTION = PACKET_DIR / "rowlocal_prefactor_reexecution_after_import.packet.json"
MINIMAL_OBJECT = PACKET_DIR / "minimal_remaining_prefactor_source_object.packet.json"
CUTSET = PACKET_DIR / "next_cutset_after_selected_transfer_derivative_reconciliation.packet.json"
CERT = ROOT / "certificates" / f"{SLUG}_certificate.json"
NOTE = ROOT / "proof_corpus" / "MTT_Selected_SelectedSectorTransferOverlapDerivative_or_RowLocalPrefactorEmission_v1.md"
BUILDER = ROOT / "scripts" / f"build_{SLUG}.py"

STATUS = (
    "MTT_SELECTED_SECTORTRANSFER_OVERLAPDERIVATIVE_RECONCILED_"
    "ROWLOCAL_SCALAR_VALUES_OPEN"
)
NEXT = "MTT_Selected_RowwiseScalarRetardedOverlapQuadratureValues_or_TSchemeLambdaHExecution_v1"


def load(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def require(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)


def assert_guarded(payload: dict, name: str) -> None:
    require(payload["observed_data_used_as_selector"] is False, f"{name} observed selector")
    require(payload["target_fitting_used"] is False, f"{name} target fitting")


def main() -> int:
    subprocess.run([sys.executable, str(BUILDER)], cwd=ROOT, check=True)

    data = load(DATA)
    step73_import = load(STEP73_IMPORT)
    readiness = load(READINESS)
    reexecution = load(REEXECUTION)
    minimal = load(MINIMAL_OBJECT)
    cutset = load(CUTSET)
    cert = load(CERT)
    note = NOTE.read_text(encoding="utf-8")

    require(data["status"] == STATUS, "candidate status mismatch")
    require(cert["status"] == STATUS, "certificate status mismatch")
    require(data["next_required_artifact"] == NEXT, "candidate next mismatch")
    require(cert["next_required_artifact"] == NEXT, "certificate next mismatch")
    require(data["theorem"]["proved"] is True, "candidate theorem missing")
    require(cert["theorem_proved"] is True, "certificate theorem missing")
    require(data["full_no_knob_closure_claimed"] is False, "candidate overclaims no-knob")
    require(data["true_SM_equivalence_claimed"] is False, "candidate overclaims true SM")

    for name, payload in [
        ("candidate", data),
        ("step73_import", step73_import),
        ("readiness", readiness),
        ("reexecution", reexecution),
        ("minimal", minimal),
        ("cutset", cutset),
        ("cert", cert),
    ]:
        assert_guarded(payload, name)

    require(
        step73_import["status"] == "STEP73_TRANSFER_DOTD_BLOCKERS_PARTLY_SUPERSEDED",
        "step73 import status",
    )
    superseded = step73_import["superseded_for_current_k_attempt"]
    require(
        superseded["selected_rank2_to_sector_transfer_or_stationary_sector_transfer"] is True,
        "sector transfer not superseded",
    )
    require(superseded["selected_physical_dotD_alpha1_payload"] is True, "dotD not superseded")
    require(superseded["dynamic_first_response_support"] is True, "dynamic support not imported")
    not_superseded = step73_import["not_superseded"]
    require(not_superseded["rowwise_scalar_retarded_overlap_derivative_values"] is True, "rowwise values overclosed")
    require(not_superseded["selected_T_scheme_rows"] is True, "T_scheme overclosed")
    require(not_superseded["selected_lambda_H_payload"] is True, "lambda_H overclosed")
    require(not_superseded["strict_omega_acceptance"] is True, "strict Omega overclosed")

    require(readiness["status"] == "SECTOR_TRANSFER_DOTD_READY_ROWLOCAL_SCALAR_VALUES_OPEN", "readiness status")
    require(readiness["stationary_sector_transfer_imported"] is True, "stationary transfer missing")
    require(readiness["stationary_sector_rho_s_imported"] is True, "rho_s missing")
    require(readiness["physical_dotD_alpha1_imported"] is True, "physical dotD missing")
    require(readiness["dynamic_first_response_support_imported"] is True, "dynamic support missing")
    require(readiness["rtheta_stationary_sector_transfer_closed"] is True, "Rtheta transfer missing")
    require(readiness["rtheta_dotD_alpha1_transport_subgate_closed"] is True, "Rtheta dotD missing")
    require(readiness["model_active_projector_values_emitted"] is True, "model projectors missing")
    require(readiness["selected_HYM_projector_values_promoted"] is False, "HYM projectors overpromoted")
    require(readiness["step68_exponent_rows_closed"] is True, "Step68 exponents not imported")
    require(readiness["step69_formula_rows_constructed"] == 10, "Step69 formula count mismatch")
    require(len(readiness["row_readiness"]) == 10, "readiness row count")
    for row in readiness["row_readiness"]:
        require(row["stationary_sector_projector_available"] is True, f"stationary projector missing {row['omega_id']}")
        require(row["stationary_rho_s_available"] is True, f"rho_s missing {row['omega_id']}")
        require(row["physical_dotD_alpha1_available"] is True, f"dotD missing {row['omega_id']}")
        require(row["selected_retarded_overlap_derivative_row_emitted"] is False, f"retarded row overemitted {row['omega_id']}")
        require(row["selected_threshold_scheme_row_emitted"] is False, f"threshold row overemitted {row['omega_id']}")
        require(row["selected_K_threshold_row_emitted"] is False, f"K row overemitted {row['omega_id']}")
        require(row["accepted_as_no_knob_source_row"] is False, f"no-knob row overaccepted {row['omega_id']}")

    require(
        reexecution["status"] == "TEN_ROWLOCAL_ROWS_REEXECUTED_ZERO_SCALAR_VALUES_EMITTED",
        "reexecution status",
    )
    require(reexecution["row_count"] == 10, "reexecution count")
    for key in [
        "accepted_rowwise_scalar_quadrature_value_count",
        "accepted_selected_retarded_derivative_row_count",
        "accepted_T_scheme_row_count",
        "accepted_K_threshold_source_row_count",
        "accepted_rowlocal_prefactor_source_row_count",
        "accepted_omega_source_row_count",
    ]:
        require(reexecution[key] == 0, f"reexecution overaccepted {key}")
    require(reexecution["lambda_H_value_row_emitted"] is False, "lambda_H emitted")
    for row in reexecution["attempt_rows"]:
        require(row["stationary_sector_transfer_available"] is True, f"transfer missing {row['omega_id']}")
        require(row["physical_dotD_alpha1_available"] is True, f"dotD missing {row['omega_id']}")
        require(row["selected_rowwise_scalar_quadrature_evaluator_emitted"] is False, f"scalar evaluator overemitted {row['omega_id']}")
        require(row["selected_retarded_overlap_derivative_row_emitted"] is False, f"retarded row overemitted {row['omega_id']}")
        require(row["selected_T_scheme_row_emitted"] is False, f"T_scheme overemitted {row['omega_id']}")
        require(row["selected_K_threshold_row_emitted"] is False, f"K row overemitted {row['omega_id']}")
        require(row["accepted_as_no_knob_source_row"] is False, f"no-knob overaccepted {row['omega_id']}")
        require(row["accepted_as_rowlocal_prefactor_source_row"] is False, f"prefactor overaccepted {row['omega_id']}")
        require(row["accepted_as_omega_source_row"] is False, f"Omega overaccepted {row['omega_id']}")
        require(
            "rowwise scalar quadrature value is not emitted"
            in row["blocking_reasons_after_reconciliation"],
            f"missing scalar blocker {row['omega_id']}",
        )
        require(
            "selected T_scheme row is not instantiated"
            in row["blocking_reasons_after_reconciliation"],
            f"missing scheme blocker {row['omega_id']}",
        )
    h_row = next(row for row in reexecution["attempt_rows"] if row["omega_id"] == "Omega_H.lambda")
    require(
        "selected lambda_H H-sector payload is not emitted"
        in h_row["blocking_reasons_after_reconciliation"],
        "H lambda blocker missing",
    )

    require(minimal["status"] == "MINIMAL_REMAINING_OBJECT_ROWLOCAL_SCALAR_EVALUATOR_AND_TSCHEME", "minimal status")
    closed = minimal["closed_now"]
    require(closed["step73_stale_sector_transfer_blocker_retired"] is True, "stale sector blocker not retired")
    require(closed["step73_stale_physical_dotD_blocker_retired"] is True, "stale dotD blocker not retired")
    require(closed["generation_resolved_theta_exponent_rows"] is True, "theta exponents missing")
    require(closed["prefactor_formula_contract"] is True, "prefactor formula missing")
    for phrase in [
        "selected rowwise scalar retarded-overlap quadrature values L_rowlocal.Omega_*",
        "selected threshold/scale/scheme rows T_scheme.Omega_*",
        "selected lambda_H H-sector payload",
        "strict Omega/K_threshold acceptance after row emission",
    ]:
        require(phrase in minimal["still_open"], f"minimal open missing {phrase}")
    for phrase in [
        "ten L_rowlocal.Omega_* scalar quadrature rows",
        "ten T_scheme.Omega_* rows or a source-selected universal scheme rule",
        "lambda_H payload for Omega_H.lambda",
        "row-level certificates before admitted replay values enter",
    ]:
        require(phrase in minimal["minimal_source_object"]["must_emit"], f"must emit missing {phrase}")

    require(cutset["next_required_artifact"] == NEXT, "cutset next")
    require(
        "selected rank2-to-sector transfer values for the current K attempt"
        in cutset["resolved_open_labels_from_step73"],
        "resolved transfer label missing",
    )
    require(
        "selected physical dotD_alpha1 support for the current K attempt"
        in cutset["resolved_open_labels_from_step73"],
        "resolved dotD label missing",
    )

    decision = data["closure_decision"]
    for key in [
        "step73_transfer_dotd_blocker_superseded_for_current_k_attempt",
        "stationary_sector_transfer_imported",
        "physical_dotD_alpha1_imported",
        "dynamic_first_response_support_imported",
    ]:
        require(decision[key] is True, f"decision did not close {key}")
        require(cert[key] is True, f"certificate did not close {key}")
    for key in [
        "selected_HYM_projector_values_promoted",
        "rowwise_scalar_retarded_overlap_values_emitted",
        "selected_T_scheme_rows_emitted",
        "selected_lambda_H_payload_emitted",
        "strict_omega_acceptance_closed",
        "true_SM_equivalence_closed",
        "full_no_knob_closed",
    ]:
        require(decision[key] is False, f"decision overclosed {key}")
        require(cert[key] is False, f"certificate overclosed {key}")
    for key in [
        "accepted_rowlocal_prefactor_source_row_count",
        "accepted_selected_retarded_derivative_row_count",
        "accepted_K_threshold_source_row_count",
        "accepted_omega_source_row_count",
        "accepted_internal_scalar_value_row_count",
    ]:
        require(decision[key] == 0, f"decision count overaccepted {key}")
        require(cert[key] == 0, f"certificate count overaccepted {key}")

    for phrase in [
        "Step73 transfer/dotD blocker superseded",
        "rowwise scalar retarded-overlap values emitted: false",
        "accepted row-local prefactor source rows      : 0",
        "SelectedRowwiseScalarRetardedOverlapAndSchemeValueRows",
        NEXT,
    ]:
        require(phrase in note, f"note missing {phrase}")

    print(
        "AUDIT_PASS: Step73 transfer/dotD blockers reconciled; rowwise scalar "
        "values and T_scheme/lambda_H remain the active wall."
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
