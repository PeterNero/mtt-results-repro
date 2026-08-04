"""Audit sector response density source theorem / no-knob csk row emission gate."""

from __future__ import annotations

import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "candidate_data"
CERTS = ROOT / "certificates"
CORPUS = ROOT / "proof_corpus"
SLUG = "selected_sectorresponsedensitysource_or_noknobcskrowemission"

CANDIDATE = DATA / f"{SLUG}.candidate.json"
CERT = CERTS / f"{SLUG}_certificate.json"
IMPORT = DATA / SLUG / "step10_c1_sector_matrix_import.packet.json"
TRACE_EXEC = DATA / SLUG / "c1_lane_commoncircle_trace_execution.packet.json"
OBSTRUCTION = DATA / SLUG / "sector_density_codomain_obstruction.packet.json"
NEXT_PACKET = DATA / SLUG / "next_cutset_after_c1_density_bridge.packet.json"
NOTE = CORPUS / "MTT_Selected_SectorResponseDensitySourceTheorem_or_NoKnobCSKRowEmission_v1.md"

STATUS = (
    "MTT_SELECTED_SECTORRESPONSEDENSITYSOURCE_OR_NOKNOBCSKROWEMISSION_"
    "C1_MATRICES_BRIDGED_FULL_DENSITY_OPEN"
)
NEXT = "MTT_Selected_FullS2SectorDensityOperator_or_PhiSectorNNumericRows_v1"


def load(path: Path) -> dict:
    assert path.exists(), f"missing {path.relative_to(ROOT)}"
    return json.loads(path.read_text(encoding="utf-8"))


def main() -> int:
    candidate = load(CANDIDATE)
    cert = load(CERT)
    import_packet = load(IMPORT)
    trace_exec = load(TRACE_EXEC)
    obstruction = load(OBSTRUCTION)
    next_packet = load(NEXT_PACKET)
    note = NOTE.read_text(encoding="utf-8")

    assert candidate["status"] == STATUS
    assert candidate["next_required_artifact"] == NEXT
    assert candidate["theorem"]["name"] == "C1SectorMatrixBridgeObstructionTheorem"
    assert candidate["theorem"]["proved"] is True
    assert candidate["closure_claimed"] is True
    assert candidate["strict_phi_sector_n_values_claimed"] is False
    assert candidate["strict_csk_source_theorem_claimed"] is False
    assert candidate["full_no_knob_closure_claimed"] is False
    assert candidate["true_SM_equivalence_claimed"] is False
    assert candidate["observed_data_used_as_selector"] is False
    assert candidate["target_fitting_used"] is False

    decision = candidate["closure_decision"]
    assert decision["step10_c1_sector_matrices_imported"] is True
    assert decision["selected_dynamic_phi_fin_c1_payload_emitted"] is True
    assert decision["sector_response_matrices_promoted_strict"] is True
    assert decision["c1_lane_commoncircle_traces_executed"] is True
    assert decision["c1_lane_trace_row_count"] == 9
    assert decision["required_phi_sector_n_value_count"] == 9
    assert decision["accepted_phi_sector_n_value_count"] == 0
    assert decision["accepted_strict_csk_source_row_count"] == 0
    assert decision["full_S2_value_rows_closed"] is False
    assert decision["Yukawa_magnitude_rows_closed"] is False
    assert decision["policy_replay_rows_accepted_as_source"] is False
    assert decision["strict_csk_source_theorem_closed"] is False

    nums = candidate["key_numbers"]
    assert nums["u_e_c1_duplicate_residual"] == 0.0
    assert nums["u_e_policy_difference_norm"] > 0.0
    assert nums["imaginary_projected_row_count"] > 0
    assert nums["max_abs_real_part_minus_policy"] > 1.0
    assert nums["rms_real_part_minus_policy"] > 1.0

    imported = import_packet["imported_closure"]
    assert imported["route_A_selected_physical_PhiFinC1_source_rule_closed"] is True
    assert imported["selected_dynamic_phi_fin_c1_payload_emitted"] is True
    assert imported["A_selected_promoted_strict"] is True
    assert imported["b_selected_promoted_strict"] is True
    assert imported["deltaTheta_C1_promoted_strict"] is True
    assert imported["sector_response_matrices_promoted_strict"] is True
    assert imported["full_S2_value_rows_closed"] is False
    assert imported["Yukawa_CKM_PMNS_Higgs_mass_value_rows_without_proxy_fitting_closed"] is False

    assert trace_exec["formal_trace_row_count"] == 9
    assert trace_exec["accepted_phi_sector_n_value_count"] == 0
    assert trace_exec["accepted_csk_source_row_count"] == 0
    assert set(trace_exec["lane_trace_rows"].keys()) == {"phase_Z", "shift_X"}
    assert trace_exec["sector_lane_map_tested"] == {"u": "phase_Z", "e": "phase_Z", "d": "shift_X"}
    assert len(trace_exec["projected_rows"]) == 9
    assert all(row["accepted_as_phi_sector_n_value"] is False for row in trace_exec["projected_rows"])
    assert all(row["accepted_as_csk_source_row"] is False for row in trace_exec["projected_rows"])

    fields = obstruction["obstruction_fields"]
    assert fields["c1_lane_count"] == 2
    assert fields["required_charged_sector_count"] == 3
    assert fields["required_phi_sector_n_row_count"] == 9
    assert fields["accepted_phi_sector_n_row_count"] == 0
    assert fields["accepted_csk_source_row_count"] == 0
    assert fields["u_and_e_share_same_phase_lane"] is True
    assert fields["u_e_c1_duplicate_residual"] == 0.0
    assert fields["u_e_policy_difference_norm"] > 0.0
    assert fields["d_shift_lane_has_complex_commoncircle_rows"] is True
    assert fields["full_S2_value_rows_closed"] is False
    assert fields["accepted_Yukawa_magnitudes_closed"] is False

    assert next_packet["next_required_artifact"] == NEXT
    assert "the potential Step10-already-closes-csk shortcut rejected by calculation" in next_packet["closed_now"]
    assert "full S2 sector density operator Phi_sector_N" in next_packet["still_open"]

    assert cert["status"] == STATUS
    assert cert["step10_c1_sector_matrices_imported"] is True
    assert cert["selected_dynamic_phi_fin_c1_payload_emitted"] is True
    assert cert["sector_response_matrices_promoted_strict"] is True
    assert cert["c1_lane_commoncircle_traces_executed"] is True
    assert cert["accepted_phi_sector_n_value_count"] == 0
    assert cert["accepted_strict_csk_source_row_count"] == 0
    assert cert["u_e_c1_duplicate_residual"] == 0.0
    assert cert["u_e_policy_difference_norm"] > 0.0
    assert cert["full_S2_value_rows_closed"] is False
    assert cert["next_required_artifact"] == NEXT

    assert "C1SectorMatrixBridgeObstructionTheorem" in note
    assert "accepted strict `Phi_sector_N` rows: `0`" in note
    assert NEXT in note
    print("sector response density source / no-knob csk row emission audit passed")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
