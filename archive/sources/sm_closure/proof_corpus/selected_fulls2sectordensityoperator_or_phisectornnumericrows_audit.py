"""Audit full-S2 sector density operator / Phi_sector_N numeric rows gate."""

from __future__ import annotations

import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "candidate_data"
CERTS = ROOT / "certificates"
CORPUS = ROOT / "proof_corpus"
SLUG = "selected_fulls2sectordensityoperator_or_phisectornnumericrows"

CANDIDATE = DATA / f"{SLUG}.candidate.json"
CERT = CERTS / f"{SLUG}_certificate.json"
DENSITY = DATA / SLUG / "fulls2_density_operator_contract.packet.json"
RESIDUAL = DATA / SLUG / "phisectorn_residual_obligation_after_c1.packet.json"
REDUCTION = DATA / SLUG / "minimal_pattern_reduction_tests.packet.json"
SOURCE = DATA / SLUG / "phisectorn_numeric_row_source_decision.packet.json"
NEXT_PACKET = DATA / SLUG / "next_cutset_after_fulls2_density_contract.packet.json"
NOTE = CORPUS / "MTT_Selected_FullS2SectorDensityOperator_or_PhiSectorNNumericRows_v1.md"

STATUS = (
    "MTT_SELECTED_FULLS2SECTORDENSITYOPERATOR_OR_PHISECTORNNUMERICROWS_"
    "DENSITY_CONTRACT_CLOSED_NUMERIC_ROWS_OPEN"
)
NEXT = "MTT_Selected_DeltaS2DensityCorrectionSource_or_StrictCSKRows_v1"


def load(path: Path) -> dict:
    assert path.exists(), f"missing {path.relative_to(ROOT)}"
    return json.loads(path.read_text(encoding="utf-8"))


def main() -> int:
    candidate = load(CANDIDATE)
    cert = load(CERT)
    density = load(DENSITY)
    residual = load(RESIDUAL)
    reduction = load(REDUCTION)
    source = load(SOURCE)
    next_packet = load(NEXT_PACKET)
    note = NOTE.read_text(encoding="utf-8")

    assert candidate["status"] == STATUS
    assert candidate["next_required_artifact"] == NEXT
    assert candidate["theorem"]["name"] == "FullS2DensityCorrectionContractTheorem"
    assert candidate["theorem"]["proved"] is True
    assert candidate["closure_claimed"] is True
    assert candidate["full_s2_density_contract_claimed"] is True
    assert candidate["strict_phi_sector_n_values_claimed"] is False
    assert candidate["strict_csk_source_theorem_claimed"] is False
    assert candidate["full_no_knob_closure_claimed"] is False
    assert candidate["true_SM_equivalence_claimed"] is False
    assert candidate["observed_data_used_as_selector"] is False
    assert candidate["target_fitting_used"] is False

    decision = candidate["closure_decision"]
    assert decision["full_s2_density_operator_contract_closed"] is True
    assert decision["selected_c1_support_embedded"] is True
    assert decision["delta_s2_row_dual_slots_defined"] is True
    assert decision["diagnostic_delta_s2_obligation_computed"] is True
    assert decision["delta_s2_diagnostic_rank"] == 3
    assert decision["delta_s2_numeric_source_values_emitted"] is False
    assert decision["accepted_delta_s2_source_row_count"] == 0
    assert decision["accepted_phi_sector_n_numeric_row_count"] == 0
    assert decision["accepted_strict_csk_source_row_count"] == 0
    assert decision["low_parameter_pattern_reduction_closed"] is False
    assert decision["full_s2_value_execution_allowed_now"] is False
    assert decision["full_s2_accepted_scalar_row_count_now"] == 0
    assert decision["policy_replay_rows_accepted_as_source"] is False

    nums = candidate["key_numbers"]
    assert nums["delta_s2_diagnostic_rank"] == 3
    assert abs(nums["delta_s2_diagnostic_determinant"]) > 1e-6
    assert nums["delta_s2_rms"] > 1.0
    assert nums["delta_s2_max_abs"] > 1.0
    assert nums["additive_model_rms_residual"] > 0.0
    assert nums["additive_model_max_abs_residual"] > 0.0

    assert density["status"] == "FULL_S2_DENSITY_OPERATOR_CONTRACT_CLOSED_VALUES_OPEN"
    assert density["source_form"] == "Phi_sector_N = Phi_C1_lanes + Delta_S2"
    assert density["closed_inputs"]["H_cen_and_trace_basis_closed"] is True
    assert density["closed_inputs"]["c1_dynamic_support_imported"] is True
    assert density["closed_inputs"]["c1_lane_commoncircle_trace_executed"] is True
    assert density["value_boundary"]["delta_s2_numeric_source_values_emitted"] is False
    assert density["value_boundary"]["policy_replay_values_define_delta_s2"] is False
    assert density["value_boundary"]["accepted_phi_sector_n_numeric_rows"] == 0

    assert residual["status"] == "DELTA_S2_RESIDUAL_OBLIGATION_COMPUTED_DIAGNOSTIC_ONLY"
    assert residual["policy_values_used_only_as_diagnostic_target"] is True
    assert residual["matrix_diagnostics"]["delta_s2_diagnostic_rank"] == 3
    assert len(residual["rows"]) == 9
    assert all(row["source_value_emitted"] is False for row in residual["rows"])
    assert all(row["accepted_as_phi_sector_n_numeric_row"] is False for row in residual["rows"])
    assert all(row["accepted_as_csk_source_row"] is False for row in residual["rows"])

    assert reduction["status"] == "LOW_PARAMETER_PATTERN_REDUCTION_REJECTED_FOR_CURRENT_SUPPORT"
    assert reduction["diagnostic_matrix_rank_full"] is True
    assert reduction["ordinary_sector_knobs_rejected_by_policy"] is True
    assert reduction["minimal_universal_parameter_lane_selected_now"] is False
    assert reduction["selected_parameter_count_now"] == 0
    assert reduction["tests"]["sector_only"]["exact"] is False
    assert reduction["tests"]["coefficient_only"]["exact"] is False
    assert reduction["tests"]["additive_sector_plus_coefficient"]["exact"] is False
    assert reduction["tests"]["rank_less_than_three_exact"]["exact"] is False
    assert reduction["accepted_reduced_source_theorem_now"] is False
    assert reduction["accepted_delta_s2_source_rows_now"] == 0

    assert source["status"] == "PHI_SECTOR_N_NUMERIC_ROWS_NOT_EMITTED_BY_CURRENT_FULL_S2_SUPPORT"
    assert source["full_s2_execution_gate"]["execution_allowed_now"] is False
    assert source["full_s2_execution_gate"]["accepted_scalar_row_count_now"] == 0
    assert source["accepted_phi_sector_n_numeric_row_count"] == 0
    assert source["accepted_delta_s2_source_row_count"] == 0
    assert source["accepted_strict_csk_source_row_count"] == 0
    assert "sector_projectors_dotD_alpha1" in source["payload_support_summary"]["selected_now"]
    assert "HYM_projector_zero_mode_basis_values" in source["payload_support_summary"]["support_only_rows"]

    assert next_packet["next_required_artifact"] == NEXT
    assert "full-S2 density operator contract constructed" in next_packet["closed_now"]
    assert "selected Delta_S2 density correction source" in next_packet["still_open"]

    assert cert["status"] == STATUS
    assert cert["full_s2_density_operator_contract_closed"] is True
    assert cert["selected_c1_support_embedded"] is True
    assert cert["delta_s2_row_dual_slots_defined"] is True
    assert cert["diagnostic_delta_s2_obligation_computed"] is True
    assert cert["delta_s2_diagnostic_rank"] == 3
    assert cert["delta_s2_numeric_source_values_emitted"] is False
    assert cert["accepted_delta_s2_source_row_count"] == 0
    assert cert["accepted_phi_sector_n_numeric_row_count"] == 0
    assert cert["accepted_strict_csk_source_row_count"] == 0
    assert cert["next_required_artifact"] == NEXT

    assert "FullS2DensityCorrectionContractTheorem" in note
    assert "accepted strict `Delta_S2` source rows: `0`" in note
    assert NEXT in note
    print("full-S2 sector density operator / Phi_sector_N numeric rows audit passed")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
