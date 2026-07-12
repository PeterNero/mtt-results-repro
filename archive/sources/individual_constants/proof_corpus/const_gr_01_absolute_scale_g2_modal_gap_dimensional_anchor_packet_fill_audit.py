"""Audit CONST-GR-01 G2 modal-gap dimensional-anchor packet fill attempt."""

from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SLUG = "const_gr_01_absolute_scale_g2_modal_gap_dimensional_anchor_packet_fill"
SCRIPT = ROOT / "scripts" / f"build_{SLUG}.py"
DATA = ROOT / "candidate_data" / f"{SLUG}.candidate.json"
BASE = ROOT / "candidate_data" / SLUG
PACKET_ATTEMPT = BASE / "selected_dimensional_anchor_packet_fill_attempt.packet.json"
ROUTE_MATRIX = BASE / "dimensional_anchor_route_matrix.packet.json"
TAU_BRIDGE = BASE / "same_branch_tau_rod_clock_bridge.packet.json"
OMEGA_REDUCTION = BASE / "omega0_source_reduction.packet.json"
BOUNDARY = BASE / "g2_boundary.packet.json"
NEXT_WORK = BASE / "next_labeled_workorder.packet.json"
CERT = ROOT / "certificates" / f"{SLUG}_certificate.json"
NOTE = ROOT / "proof_corpus" / "MTT_CONST_GR_01_AbsoluteScale_G2_ModalGapDimensionalAnchorPacketFill_v1.md"

STATUS = "MTT_CONST_GR_01_G2_MODAL_GAP_DIMENSIONAL_ANCHOR_PACKET_FILL_BUILT"


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
    packet_attempt = load(PACKET_ATTEMPT)
    route_matrix = load(ROUTE_MATRIX)
    tau_bridge = load(TAU_BRIDGE)
    omega_reduction = load(OMEGA_REDUCTION)
    boundary = load(BOUNDARY)
    next_work = load(NEXT_WORK)
    cert = load(CERT)
    note = NOTE.read_text(encoding="utf-8")

    for name, item in [
        ("candidate", candidate),
        ("packet_attempt", packet_attempt),
        ("route_matrix", route_matrix),
        ("tau_bridge", tau_bridge),
        ("omega_reduction", omega_reduction),
        ("boundary", boundary),
    ]:
        clean(item, name)

    require(candidate["status"] == STATUS, "candidate status")
    require(candidate["theorem"]["proved"] is True, "candidate theorem")
    require(candidate["structural_packet_fill_attempted"] is True, "structural fill")
    require(candidate["packet_promotes_to_closed_anchor"] is False, "packet promoted too early")
    require(candidate["same_branch_tau_role_closed"] is True, "tau role")
    require(candidate["absolute_physical_value_closed"] is False, "absolute value")
    require(candidate["next_gate_reduced_to_CUV_Qtau_Omega0"] is True, "next reduction")
    require(candidate["measured_Newton_or_Planck_derived"] is False, "Newton overclosed")
    require(candidate["strict_no_knob_absolute_scale_closure"] is False, "strict overclosed")

    require(packet_attempt["packet"] == "SelectedDimensionalAnchorPacket", "packet schema")
    require(packet_attempt["status"] == "ATTEMPTED_STRUCTURAL_FILL_VALUE_OPEN", "packet status")
    require(packet_attempt["dimensionful_quantity"]["value"] is None, "dimensionful value should be null")
    require(packet_attempt["source_certification"]["same_branch_as_rho_uv_and_z448"] is True, "same branch")
    require(packet_attempt["source_certification"]["structural_role_found"] is True, "structural role")
    require(packet_attempt["source_certification"]["absolute_value_found"] is False, "absolute found")
    require(packet_attempt["source_certification"]["selected_by_mtt"] is False, "selected by MTT")
    require(packet_attempt["source_certification"]["computed_before_target_comparison"] is False, "computed before target")
    require(packet_attempt["map_to_alpha_phys"]["alpha_phys_value"] is None, "alpha value")
    require(packet_attempt["promotion"]["packet_promotes_to_closed_anchor"] is False, "promotion")
    require("dimensionful_quantity.value" in packet_attempt["promotion"]["blocking_fields"], "blocking field")

    require(route_matrix["status"] == "ALL_CURRENT_ROUTES_CLASSIFIED_NO_PROMOTION", "route status")
    require(route_matrix["best_current_route"]["id"] == "m_theory_modal_gap_to_ellp", "best route")
    require(route_matrix["best_current_route"]["classification"] == "BEST_STRUCTURAL_ROUTE_PHYSICAL_GAP_VALUE_OPEN", "best classification")
    require(route_matrix["best_unconventional_auxiliary"]["id"] == "same_branch_tau_rod_clock_bridge", "aux route")
    require("flux_bianchi_alpha_prime" in route_matrix["routes"], "flux route")
    require("central_circle_spectral_gap" in route_matrix["routes"], "central circle route")

    require(tau_bridge["status"] == "SAME_BRANCH_TAU_ROLE_CLOSED_ABSOLUTE_VALUE_OPEN", "tau status")
    require(tau_bridge["source_identification"]["tau_role"] == "physical proper-time/coherent-length squared object", "tau role")
    require(tau_bridge["relative_values"]["tau_int"] == 0.40698621549433234, "tau int")
    require(tau_bridge["absolute_values"]["alpha_phys"] is None, "tau alpha")
    require(tau_bridge["verdict"]["same_branch_physical_clock_or_length_source_found"] is True, "source found")
    require(tau_bridge["verdict"]["absolute_physical_value_closed"] is False, "tau absolute")
    require(tau_bridge["metrology_no_go"]["applies_here"] is True, "metrology")

    require(omega_reduction["status"] == "OMEGA0_REDUCED_TO_CUV_QTAU_AND_PHYSICAL_UNIT", "omega status")
    require(omega_reduction["closed_internal_data"]["rho_UV"] == 0.164530397543639, "rho")
    require(omega_reduction["closed_internal_data"]["s_star_from_rho"] == 1.464646774701829, "s star")
    require(omega_reduction["closed_internal_data"]["lambda_internal_exact"] == 15.0, "lambda")
    require(omega_reduction["closed_internal_data"]["kappa"] == 1.0, "kappa")
    require(omega_reduction["open_gates"]["selected_higher_order_correction_functional_evaluated"] is False, "C_UV overclosed")
    require(omega_reduction["open_gates"]["selected_finite_memory_covariance_Q_tau_derived"] is False, "Q_tau overclosed")
    require(omega_reduction["open_gates"]["physical_Omega_0_selected"] is False, "Omega0 overclosed")
    require("C_UV" in omega_reduction["primitive_source_objects"], "C_UV object")
    require("Q_tau" in omega_reduction["primitive_source_objects"], "Q_tau object")
    require("Omega_0" in omega_reduction["primitive_source_objects"], "Omega0 object")

    closed = boundary["closed_or_tightened_now"]
    open_ = boundary["still_open"]
    require(closed["SelectedDimensionalAnchorPacket_structural_fill"] is True, "boundary fill")
    require(closed["omega_gap_source_data_reduced_to_CUV_Qtau_Omega0"] is True, "boundary source reduction")
    require(open_["dimensionful_quantity_value"] is True, "dimensionful open")
    require(open_["C_UV_source_certified_value"] is True, "C_UV open")
    require(open_["Q_tau_or_d_Q_source_certified_value"] is True, "Q_tau open")
    require(open_["physical_Omega0_source"] is True, "Omega0 open")
    require("not treating tau role as tau value" in boundary["anti_cycle_delta_from_G1"]["not_repeated"], "anti-cycle")

    require(next_work["primary"]["label"] == "CONST-GR-01 / ABSOLUTE-SCALE-GN / G3-CUV-QTAU-OMEGA0-SOURCE-DATA", "primary")
    require(next_work["secondary"]["label"] == "CONST-GR-01 / ABSOLUTE-SCALE-GN / G3B-DECLARE-ONE-METROLOGY-PRIMITIVE-TIER", "secondary")

    require(cert["status"] == STATUS, "cert status")
    require(cert["packet_promotes_to_closed_anchor"] is False, "cert promotion")
    require(cert["next_gate_reduced_to_CUV_Qtau_Omega0"] is True, "cert next")
    require("G2-MODAL-GAP-DIMENSIONAL-ANCHOR-PACKET-FILL" in note and "G3-CUV-QTAU-OMEGA0" in note, "note")

    print("CONST-GR-01 G2 modal-gap dimensional-anchor packet fill audit: PASS")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
