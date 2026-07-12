"""Audit CONST-HIGGS-01 H2 selected Higgs projector/quartic-kernel source packet."""

from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SLUG = "const_higgs_01_h2_selected_higgs_projector_and_quartic_kernel_source_packet"
SCRIPT = ROOT / "scripts" / f"build_{SLUG}.py"
DATA = ROOT / "candidate_data" / f"{SLUG}.candidate.json"
BASE = ROOT / "candidate_data" / SLUG
GAP_LAYER = BASE / "selected_gap_layer_promotion.packet.json"
PROJECTOR_PACKET = BASE / "higgs_projector_source_packet.packet.json"
HEAT_RESPONSE = BASE / "finite_heat_spectrum_response_import.packet.json"
QUARTIC_GATE = BASE / "quartic_kernel_reduction.packet.json"
BOUNDARY = BASE / "h2_boundary.packet.json"
NEXT_WORK = BASE / "next_labeled_workorder.packet.json"
CERT = ROOT / "certificates" / f"{SLUG}_certificate.json"
NOTE = ROOT / "proof_corpus" / "MTT_CONST_HIGGS_01_H2_SelectedHiggsProjectorAndQuarticKernelSourcePacket_v1.md"

STATUS = "MTT_CONST_HIGGS_01_H2_SELECTED_PROJECTOR_SOURCE_PROMOTED_QUARTIC_KERNEL_OPEN"


def load(path: Path) -> dict[str, object]:
    return json.loads(path.read_text(encoding="utf-8"))


def require(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)


def clean(packet: dict[str, object], name: str) -> None:
    require(packet["observed_data_used_as_selector"] is False, f"{name} observed selector")
    require(packet["target_fitting_used"] is False, f"{name} target fitting")
    require(packet["closure_claimed"] is False, f"{name} closure overclaim")


def main() -> int:
    proc = subprocess.run(
        [sys.executable, str(SCRIPT)],
        cwd=ROOT,
        text=True,
        stdout=subprocess.PIPE,
        stderr=subprocess.STDOUT,
        check=True,
    )
    computed = json.loads(proc.stdout)
    require(computed["status"] == STATUS, "builder status mismatch")

    candidate = load(DATA)
    gap_layer = load(GAP_LAYER)
    projector_packet = load(PROJECTOR_PACKET)
    heat_response = load(HEAT_RESPONSE)
    quartic_gate = load(QUARTIC_GATE)
    boundary = load(BOUNDARY)
    next_work = load(NEXT_WORK)
    cert = load(CERT)
    note = NOTE.read_text(encoding="utf-8")

    for name, item in [
        ("candidate", candidate),
        ("gap_layer", gap_layer),
        ("projector_packet", projector_packet),
        ("heat_response", heat_response),
        ("quartic_gate", quartic_gate),
        ("boundary", boundary),
    ]:
        clean(item, name)

    require(candidate["status"] == STATUS, "candidate status")
    require(candidate["theorem"]["proved"] is True, "candidate theorem")
    require(candidate["G4_one_metrology_primitive_reused"] is True, "G4 reuse")
    require(candidate["new_Higgs_specific_parameters"] == 0, "Higgs params")
    require(candidate["selected_PhiFin_provenance_closed_for_DE_gap_layer"] is True, "Phi_fin gap")
    require(candidate["selected_DE_gap_Riesz_Green_layer_closed"] is True, "gap layer")
    require(candidate["selected_eta_N"] == 1.0, "eta")
    require(candidate["H_sector_rank_two_zero_cluster_shift_source_closed"] is True, "H shift")
    require(candidate["finite_heat_spectrum_response_slot_closed"] is True, "heat")
    require(candidate["selected_Higgs_quartic_threshold_kernel_emitted"] is False, "quartic overemitted")
    require(candidate["Higgs_quartic_numeric_value_derived"] is False, "lambda overderived")
    require(candidate["strict_no_knob_Higgs_closure"] is False, "strict overclosed")

    promotion = gap_layer["promotion"]
    require(promotion["selected_trace_equality_proved"] is True, "trace equality")
    require(promotion["D_E_source_flags_theorem_derived"] is True, "D_E flags")
    require(promotion["D_E_honest_replay_passes_after_theorem_derived_source_flags"] is True, "D_E replay")
    require(promotion["Riesz_Green_layer_closes"] is True, "Riesz/Green")
    require(promotion["selected_eta_N"] == 1.0, "gap eta")
    require(promotion["eta_threshold"] == 2.1932454224643014, "threshold")
    require(promotion["selected_gap_lower_bound"] == 2.386490844928603, "gap lower")
    require(promotion["selected_green_norm_bound"] == 0.4190252822989217, "green bound")
    require(gap_layer["still_separate"]["dotD_alpha1_C1_response"] is True, "dotD separate")
    require(gap_layer["still_separate"]["A_selected_and_b_selected"] is True, "A/b separate")

    h_sector = projector_packet["H_sector_selected_gap_layer"]
    require(h_sector["H_rank_two_shift_source_proved"] is True, "H rank-two")
    require(h_sector["canonical_metric_connection_source_proved"] is True, "metric")
    require(h_sector["projective_flat_connection_to_DE_source_proved"] is True, "connection")
    require(h_sector["H_shift_indices"] == [13, 14], "H shift indices")
    boundary_projector = projector_packet["projector_boundary"]
    require(boundary_projector["selected_DE_gap_layer_closed_now"] is True, "projector DE")
    require(boundary_projector["full_selected_zero_mode_basis_packet"] is False, "zero-mode overclosed")
    require(boundary_projector["full_selected_dotD_C1_response"] is False, "dotD overclosed")

    imported = heat_response["imported_response"]
    require(imported["finite_determinant_heat_spectrum_or_torsion_response_closed"] is True, "finite heat")
    require(imported["selected_finite_heat_trace_emitted"] is True, "heat trace")
    require(imported["selected_positive_complement_pseudodeterminant_emitted"] is True, "pseudodet")
    require(imported["operator_source_slots_closed_total"] == 8, "source slots")
    require(imported["operator_source_slots_remaining"] == 0, "slot remaining")
    require(heat_response["open_from_import"]["actual_dynamic_QaSU3_operator_packet"] is True, "dynamic open")
    require(heat_response["open_from_import"]["primitive_C1_response"] is True, "C1 open")

    require(quartic_gate["what_changed_from_H1"]["selected_gap_Riesz_Green_layer"] is True, "changed")
    not_quartic = quartic_gate["still_not_a_quartic_derivation"]
    require(not_quartic["selected_Higgs_quartic_threshold_kernel_emitted"] is False, "quartic gate")
    require(not_quartic["Higgs_quartic_numeric_value_derived"] is False, "numeric gate")
    require(not_quartic["dotD_alpha1_C1_response_closed"] is False, "dotD gate")
    require("lambda_H = m_H^2/(2 v^2) as a source selector" in quartic_gate["strict_H3_acceptance"]["must_forbid"], "Higgs selector guard")

    closed = boundary["closed_or_promoted_now"]
    require(closed["selected_PhiFin_finite_trace_morphism_for_DE_gap_layer"] is True, "boundary morphism")
    require(closed["selected_trace_equality_for_27mode_DE"] is True, "boundary trace")
    require(closed["selected_eta_N_promoted"] is True, "boundary eta")
    require(closed["finite_heat_spectrum_response_slot"] is True, "boundary heat")
    open_ = boundary["still_open"]
    require(open_["selected_Higgs_quartic_threshold_kernel"] is True, "boundary quartic open")
    require(open_["dotD_alpha1_C1_response"] is True, "boundary dotD open")
    require(open_["strict_no_knob_Higgs_closure"] is True, "boundary strict open")
    require("not treating D_E/gap-layer closure as Higgs quartic closure" in boundary["anti_cycle_delta_from_H1"]["not_repeated"], "anti-cycle")

    require(next_work["primary"]["label"] == "CONST-HIGGS-01 / HIGGS-QUARTIC-THRESHOLD / H3-SELECTED-HIGGS-QUARTIC-SECOND-VARIATION-KERNEL", "primary")
    require(next_work["parallel"]["label"] == "CONST-HIGGS-01 / HIGGS-QUARTIC-THRESHOLD / H3B-DYNAMIC-C1-RETARDED-OVERLAP-RESPONSE", "parallel")

    require(cert["status"] == STATUS, "cert status")
    require(cert["selected_PhiFin_provenance_closed_for_DE_gap_layer"] is True, "cert gap")
    require(cert["selected_Higgs_quartic_threshold_kernel_emitted"] is False, "cert quartic")
    require(cert["Higgs_quartic_numeric_value_derived"] is False, "cert numeric")
    require("H2-SELECTED-HIGGS-PROJECTOR" in note and "H3-SELECTED-HIGGS-QUARTIC" in note, "note")

    print("CONST-HIGGS-01 H2 selected projector/quartic-kernel source packet audit: PASS")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
