"""Audit Step73 honest row-local HYM/Galerkin execution attempt."""

from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SLUG = "selected_step73_honestrowlocalhymgalerkin_or_selectedprefactorsourcerows"
DATA = ROOT / "candidate_data" / f"{SLUG}.candidate.json"
PACKET_DIR = ROOT / "candidate_data" / SLUG
INPUTS_PACKET = PACKET_DIR / "step73_honest_rowlocal_galerkin_input_readiness.packet.json"
SUBSOURCE_PACKET = PACKET_DIR / "step73_diagonal_hym_green_subsource_import.packet.json"
ROW_ATTEMPT_PACKET = PACKET_DIR / "step73_ten_rowlocal_prefactor_execution_attempt.packet.json"
OBSTRUCTION_PACKET = PACKET_DIR / "step73_sector_transfer_and_projector_obstruction.packet.json"
CUTSET_PACKET = PACKET_DIR / "step73_next_selected_sector_transfer_or_overlap_derivative_cutset.packet.json"
CERT = ROOT / "certificates" / f"{SLUG}_certificate.json"
NOTE = ROOT / "proof_corpus" / "MTT_Selected_Step73_HonestRowLocalHYMGalerkin_or_SelectedPrefactorSourceRows_v1.md"
BUILDER = ROOT / "scripts" / f"build_{SLUG}.py"

STATUS = "MTT_SELECTED_STEP73_HONEST_ROWLOCAL_HYM_GALERKIN_BUILT_DIAGONAL_SUBSOURCE_SECTOR_TRANSFER_OPEN"
NEXT = "MTT_Selected_SelectedSectorTransferOverlapDerivative_or_RowLocalPrefactorEmission_v1"


def load(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def require(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)


def main() -> int:
    subprocess.run([sys.executable, str(BUILDER)], cwd=ROOT, check=True)
    data = load(DATA)
    inputs = load(INPUTS_PACKET)
    subsource = load(SUBSOURCE_PACKET)
    row_attempt = load(ROW_ATTEMPT_PACKET)
    obstruction = load(OBSTRUCTION_PACKET)
    cutset = load(CUTSET_PACKET)
    cert = load(CERT)
    note = NOTE.read_text(encoding="utf-8")

    require(data["status"] == STATUS, "candidate status mismatch")
    require(cert["status"] == STATUS, "certificate status mismatch")
    require(data["next_required_artifact"] == NEXT, "candidate next mismatch")
    require(cert["next_required_artifact"] == NEXT, "certificate next mismatch")
    require(data["theorem"]["proved"] is True, "candidate theorem missing")
    require(cert["theorem_proved"] is True, "certificate theorem missing")

    for item in [data, inputs, subsource, row_attempt, obstruction, cutset, cert]:
        require(item.get("observed_data_used_as_selector") is False, "observed selector violation")
        require(item.get("target_fitting_used") is False, "target fitting violation")

    require(inputs["ready_source_subgate_count"] == 2, "expected exactly two ready source subgates")
    require(inputs["rowlocal_blocking_requirement_count"] >= 5, "blocking requirements missing")
    readiness = {row["requirement"]: row for row in inputs["readiness_rows"]}
    require(
        readiness["selected q79/F/m=1 finite HYM/Strominger operator"][
            "accepted_for_rowlocal_prefactor_source"
        ] is True,
        "HYM operator subgate not accepted",
    )
    require(
        readiness["diagonal End0 Riesz/Green normalization"][
            "accepted_for_rowlocal_prefactor_source"
        ] is True,
        "diagonal Green subgate not accepted",
    )
    for key in [
        "ordered zero-mode bases for every Omega slot",
        "sector transfer from rank-2/End0 lane to u,d,e,H Omega slots",
        "retarded overlap kernel derivative on the same branch",
        "threshold/scale/scheme convention selected before replay",
        "lambda_H H-sector source value payload",
    ]:
        require(readiness[key]["accepted_for_rowlocal_prefactor_source"] is False, f"overaccepted {key}")

    require(subsource["diagonal_hym_subsource_closed"] is True, "HYM subsource not closed")
    require(subsource["diagonal_green_subsource_closed"] is True, "Green subsource not closed")
    require(subsource["accepted_as_full_rowlocal_prefactor_source"] is False, "subsource overpromoted")
    require(subsource["accepted_rowlocal_source_row_count"] == 0, "subsource row count overaccepted")
    require(subsource["source_descriptors"]["final_residual_l2"] < 1e-10, "HYM residual too large")
    require(subsource["source_descriptors"]["T1T2_green_operator_norm_bound"] > 0.0, "Green norm missing")
    for phrase in [
        "selected sector B_N basis/quadrature/error contract",
        "rank2-to-sector transfer values",
        "ten L_rowlocal.* values",
        "ten T_scheme.* values",
        "lambda_H value row",
    ]:
        require(phrase in subsource["does_not_emit"], f"subsource guard missing {phrase}")

    rows = row_attempt["attempt_rows"]
    require(row_attempt["attempt_row_count"] == 10, "row attempt count mismatch")
    require(row_attempt["accepted_rowlocal_source_row_count"] == 0, "rowlocal rows overaccepted")
    require(row_attempt["accepted_prefactor_source_row_count"] == 0, "prefactors overaccepted")
    require(row_attempt["accepted_omega_source_row_count"] == 0, "Omega rows overaccepted")
    require(row_attempt["accepted_internal_scalar_value_row_count"] == 0, "scalar rows overaccepted")
    for row in rows:
        require(row["diagonal_hym_connection_available"] is True, f"HYM missing for {row['omega_id']}")
        require(row["diagonal_green_available"] is True, f"Green missing for {row['omega_id']}")
        require(row["model_active_zero_mode_basis_available"] is True, f"basis missing for {row['omega_id']}")
        require(row["selected_zero_mode_projector_promoted"] is False, f"projector overpromoted {row['omega_id']}")
        require(row["selected_sector_transfer_available"] is False, f"sector transfer overclosed {row['omega_id']}")
        require(row["selected_retarded_overlap_derivative_available"] is False, f"overlap derivative overclosed {row['omega_id']}")
        require(row["selected_threshold_scheme_available"] is False, f"threshold scheme overclosed {row['omega_id']}")
        require(row["emitted_L_rowlocal_value"] is None, f"L row emitted early {row['omega_id']}")
        require(row["emitted_T_scheme_value"] is None, f"T row emitted early {row['omega_id']}")
        require(row["accepted_as_rowlocal_source_row"] is False, f"rowlocal overaccepted {row['omega_id']}")
        require(row["accepted_as_prefactor_source_row"] is False, f"prefactor overaccepted {row['omega_id']}")
        require(row["accepted_as_omega_source_row"] is False, f"Omega overaccepted {row['omega_id']}")
        for phrase in [
            "selected HYM projector source promotion is false",
            "rank2-to-sector transfer values are not emitted",
            "threshold/scale/scheme row T_scheme.* is not selected",
        ]:
            require(phrase in row["blocking_reasons"], f"row blocker missing {phrase}")
    h_row = next(row for row in rows if row["omega_id"] == "Omega_H.lambda")
    require("lambda_H H-sector value payload is not emitted" in h_row["blocking_reasons"], "lambda_H blocker missing")

    require(
        obstruction["projector_status"]["finite_model_active_projector_values_emitted"] is True,
        "model-active projectors missing",
    )
    require(
        obstruction["projector_status"]["selected_HYM_projector_values_promoted"] is False,
        "projectors overpromoted",
    )
    require(
        obstruction["sector_transfer_status"]["selected_values_open"]["rank2_to_sector_transfer_values"] is True,
        "sector transfer should remain open",
    )
    require(
        obstruction["overlap_status"]["transition_overlap_table_closed"] is True,
        "overlap support missing",
    )
    require(
        obstruction["overlap_status"]["physical_dotD_alpha1_payload_extracted"] is False,
        "dotD alpha1 overextracted",
    )

    for phrase in [
        "selected HYM projector source promotion for the zero-mode bases",
        "selected rank2-to-sector transfer values for u,d,e,H Omega slots",
        "selected retarded overlap kernel derivative / physical dotD_alpha1 payload",
        "selected threshold/scale/scheme rows T_scheme.*",
        "lambda_H H-sector source value payload",
    ]:
        require(phrase in cutset["still_missing"], f"cutset missing {phrase}")
    for phrase in [
        "use Step72 postcheck target numbers to choose L_rowlocal.*",
        "promote model-active zero-mode projectors as selected HYM projectors",
        "treat diagonal End0 Green as sector-ready u,d,e,H row-local data",
    ]:
        require(phrase in cutset["forbidden_routes"], f"forbidden route missing {phrase}")

    decision = data["closure_decision"]
    for key in [
        "diagonal_hym_green_subsource_closed",
        "honest_galerkin_input_readiness_closed",
        "ten_rowlocal_execution_attempt_closed",
        "projector_sector_transfer_obstruction_closed",
    ]:
        require(decision[key] is True, f"decision did not close {key}")
        require(cert[key] is True, f"certificate did not close {key}")
    for key in [
        "selected_HYM_projector_values_promoted",
        "selected_sector_transfer_values_emitted",
        "selected_retarded_overlap_derivative_rows_emitted",
        "selected_threshold_scheme_rows_emitted",
        "lambda_H_value_row_emitted",
        "strict_omega_acceptance_closed",
        "scalar_value_execution_closed",
        "true_SM_equivalence_closed",
        "full_no_knob_closed",
    ]:
        require(decision[key] is False, f"decision overclosed {key}")
        require(cert[key] is False, f"certificate overclosed {key}")
    for key in [
        "accepted_rowlocal_source_row_count",
        "accepted_prefactor_source_row_count",
        "accepted_omega_source_row_count",
        "accepted_internal_scalar_value_row_count",
    ]:
        require(decision[key] == 0, f"decision overaccepted {key}")
        require(cert[key] == 0, f"certificate overaccepted {key}")

    for phrase in [
        "imports the already computed",
        "accepted row-local source rows  : 0",
        "selected HYM projector values promoted",
        "rank2-to-sector transfer values emitted",
        "Next artifact",
        NEXT,
    ]:
        require(phrase in note, f"note missing {phrase}")

    print(f"PASS {DATA.name}: {STATUS}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
