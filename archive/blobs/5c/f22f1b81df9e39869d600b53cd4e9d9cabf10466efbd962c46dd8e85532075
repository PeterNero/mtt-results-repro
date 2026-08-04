"""Audit qutrit-27 matrix minimal closure / strict PEW upgrade packet."""

from __future__ import annotations

import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "candidate_data"
CERTS = ROOT / "certificates"
CORPUS = ROOT / "proof_corpus"
SLUG = "selected_qutrit27matrixminimalclosure_or_strictpewupgrade"

CANDIDATE = DATA / f"{SLUG}.candidate.json"
CERT = CERTS / f"{SLUG}_certificate.json"
MATRIX_LEDGER = DATA / SLUG / "qutrit27_matrix_closure_ledger.packet.json"
TEN_ROW = DATA / SLUG / "ten_row_minimal_kthreshold_completion.packet.json"
STRICT_CUTSET = DATA / SLUG / "strict_pew_upgrade_cutset.packet.json"
NEXT_PACKET = DATA / SLUG / "next_27matrix_true_equivalence_contract.packet.json"
NOTE = CORPUS / "MTT_Selected_Qutrit27MatrixMinimalClosure_or_StrictPEWUpgrade_v1.md"

STATUS = (
    "MTT_SELECTED_QUTRIT27MATRIXMINIMALCLOSURE_OR_STRICTPEWUPGRADE_"
    "TEN_ROW_MINIMAL_LEDGER_CLOSED_STRICT_PEW_OPEN"
)
NEXT = "MTT_Selected_27MatrixStrictPEWSourceUpgrade_or_TrueSMEquivalenceAudit_v1"


def load(path: Path) -> dict:
    assert path.exists(), f"missing {path.relative_to(ROOT)}"
    return json.loads(path.read_text(encoding="utf-8"))


def main() -> int:
    candidate = load(CANDIDATE)
    cert = load(CERT)
    matrix = load(MATRIX_LEDGER)
    ten = load(TEN_ROW)
    cutset = load(STRICT_CUTSET)
    next_packet = load(NEXT_PACKET)
    note = NOTE.read_text(encoding="utf-8")

    assert candidate["status"] == STATUS
    assert candidate["next_required_artifact"] == NEXT
    assert candidate["theorem"]["name"] == "Qutrit27MatrixMinimalClosureOrStrictPEWUpgradeTheorem"
    assert candidate["theorem"]["proved"] is True
    assert candidate["minimal_parameter_27_matrix_ledger_closed"] is True
    assert candidate["strict_no_knob_27_matrix_ledger_closed"] is False
    assert candidate["measured_primitive_input_used"] is True
    assert candidate["observed_data_used_as_selector"] is False
    assert candidate["target_fitting_used"] is False

    decision = candidate["closure_decision"]
    assert decision["finite_27x27_qutrit_spectral_package_closed"] is True
    assert decision["left_right_weyl_layer_closed"] is True
    assert decision["charged_2_1_1_profile_operator_realized"] is True
    assert decision["strict_charged_K_row_count"] == 9
    assert decision["strict_H_lambda_K_row_count"] == 0
    assert decision["minimal_parameter_K_row_count"] == 10
    assert decision["H_specific_parameter_count"] == 0
    assert decision["declared_shared_physical_primitive_count"] == 1
    assert decision["accepted_strict_P_EW_source_rows"] == 0
    assert decision["accepted_direct_K_threshold_Omega_H_lambda_rows"] == 0
    assert decision["accepted_strict_source_payload_fields"] == 0
    assert decision["full_no_knob_closed"] is False
    assert decision["true_SM_equivalence_closed"] is False

    assert matrix["carrier_dimension"] == 27
    assert matrix["left_action_rank"] == 27
    assert matrix["left_right_weyl_layer_closed"] is True
    assert matrix["charged_2_1_1_profile_operator_realized"] is True
    assert matrix["strict_charged_row_count"] == 9
    assert matrix["minimal_parameter_ten_row_ledger_closed"] is True
    assert matrix["strict_no_knob_ten_row_ledger_closed"] is False

    assert ten["row_count"] == 10
    assert ten["strict_no_knob_row_count"] == 9
    assert ten["minimal_parameter_row_count"] == 10
    assert ten["charged_strict_rows"] == 9
    assert ten["H_lambda_minimal_one_primitive_rows"] == 1
    assert ten["declared_shared_physical_primitive_count"] == 1
    assert ten["H_specific_parameter_count"] == 0
    assert ten["lambda_H_calibrated_from_lambda_H"] is False
    assert ten["lambda_H_conditional_prediction_from_non_Higgs_prefactor"] is True
    h_rows = [row for row in ten["rows"] if row["row_id"] == "selected_overlap_kernel.Omega_H.lambda"]
    assert len(h_rows) == 1
    assert h_rows[0]["accepted_as_minimal_parameter_kthreshold_row"] is True
    assert h_rows[0]["accepted_as_strict_no_knob_kthreshold_row"] is False
    assert h_rows[0]["measured_primitive_input_used"] is True
    assert abs(h_rows[0]["lambda_H_minimal_one_primitive_value"] - 0.1260399999999988) < 1e-14

    assert cutset["open_strict_upgrade_rows"]["accepted_strict_P_EW_source_rows"] == 0
    assert cutset["open_strict_upgrade_rows"]["accepted_direct_K_threshold_Omega_H_lambda_rows"] == 0
    assert cutset["open_strict_upgrade_rows"]["accepted_strict_source_payload_fields"] == 0
    assert cutset["best_current_internal_target"]["formula"] == "8*Delta_G12/pi^2"
    assert cutset["best_current_internal_target"]["accepted_as_source"] is False
    assert cutset["minimal_ledger_already_closed_so_upgrade_reduces_parameter_count_by_one"] is True

    assert next_packet["next_required_artifact"] == NEXT
    assert "ten-row matrix-facing K ledger in the minimal one-shared-primitive lane" in next_packet["what_is_closed_now"]
    assert cert["status"] == STATUS
    assert cert["minimal_parameter_27_matrix_ledger_closed"] is True
    assert cert["strict_no_knob_27_matrix_ledger_closed"] is False
    assert cert["minimal_parameter_K_row_count"] == 10
    assert cert["accepted_strict_P_EW_source_rows"] == 0
    assert cert["accepted_direct_K_threshold_Omega_H_lambda_rows"] == 0

    assert "minimal one-primitive 27-matrix ledger closure" in note
    assert "Strict `P_EW` rows remain `0`" in note
    assert NEXT in note
    print("qutrit-27 matrix minimal closure / strict PEW upgrade audit passed")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
