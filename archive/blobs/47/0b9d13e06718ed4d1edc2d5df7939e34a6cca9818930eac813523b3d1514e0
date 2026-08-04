"""Audit qutrit27 H functional search / radial source frontier."""

from __future__ import annotations

import json
import math
import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SLUG = "selected_qutrit27hfunctionalsearch_or_radialsourcefrontier"
DATA = ROOT / "candidate_data" / f"{SLUG}.candidate.json"
PACKET_DIR = ROOT / "candidate_data" / SLUG
SCALAR = PACKET_DIR / "profile_matrix_scalar_functional_inventory.packet.json"
H_PACKET = PACKET_DIR / "controlled_herm2_matrix_invariants.packet.json"
GATE = PACKET_DIR / "strict_h_acceptance_gate_after_matrix_functional_search.packet.json"
CERT = ROOT / "certificates" / f"{SLUG}_certificate.json"
NOTE = ROOT / "proof_corpus" / "MTT_Selected_Qutrit27HFunctionalSearch_or_RadialSourceFrontier_v1.md"
BUILDER = ROOT / "scripts" / f"build_{SLUG}.py"

STATUS = (
    "MTT_SELECTED_QUTRIT27HFUNCTIONALSEARCH_OR_RADIALSOURCEFRONTIER_"
    "MATRIX_FUNCTIONALS_REJECTED_CONTROLLED_H_READY_RADIAL_OPEN"
)
NEXT = "MTT_Selected_HRadialValueSource_or_NonHiggsHRGPrediction_v1"


def load(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def require(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)


def guard(packet: dict, label: str) -> None:
    require(packet.get("closure_claimed") is True, f"{label} closure")
    require(packet.get("observed_data_used_as_selector") is False, f"{label} observed selector")
    require(packet.get("target_fitting_used") is False, f"{label} target fitting")


def main() -> int:
    subprocess.run([sys.executable, str(BUILDER)], cwd=ROOT, check=True)

    data = load(DATA)
    scalar = load(SCALAR)
    h_packet = load(H_PACKET)
    gate = load(GATE)
    cert = load(CERT)
    note = NOTE.read_text(encoding="utf-8")

    for label, packet in [
        ("candidate", data),
        ("scalar", scalar),
        ("h_packet", h_packet),
        ("gate", gate),
        ("certificate", cert),
    ]:
        guard(packet, label)

    require(data["status"] == STATUS, "candidate status")
    require(cert["status"] == STATUS, "certificate status")
    require(data["next_required_artifact"] == NEXT, "candidate next")
    require(cert["next_required_artifact"] == NEXT, "certificate next")
    require(data["theorem"]["proved"] is True, "theorem")
    require(data["full_no_knob_closure_claimed"] is False, "no-knob overclaim")
    require(data["true_SM_equivalence_claimed"] is False, "true SM overclaim")

    require(scalar["accepted_strict_H_radial_functional_count"] == 0, "scalar strict count")
    require(scalar["accepted_K_threshold_Omega_H_lambda_count"] == 0, "scalar K count")
    require(len(scalar["functionals"]) >= 10, "functional inventory")
    require(all(not item["accepted_as_K_threshold_Omega_H_lambda"] for item in scalar["functionals"]), "K overaccept")

    domain = h_packet["domain_readiness"]
    for key in [
        "B_Huv_domain_closed",
        "P_H_projector_closed",
        "R_H_restriction_closed",
        "Herm2_codomain_closed",
        "left_right_End9_control_closed",
    ]:
        require(domain[key] is True, f"domain {key}")
    invariants = h_packet["invariants"]
    require(invariants["Hermitian_error_frobenius"] < 1e-12, "Hermitian error")
    require(abs(invariants["trace_real"]) < 1e-12, "trace real")
    require(abs(invariants["trace_imag"]) < 1e-12, "trace imag")
    require(math.isclose(invariants["r_H_from_sqrt_Tr_H_squared_over_2"], 391.39140285811936, rel_tol=0, abs_tol=1e-9), "r_H")
    require(math.isclose(invariants["s_beta_recovered"], 0.004701083905943647, rel_tol=0, abs_tol=1e-15), "s_beta")
    require(h_packet["controlled_one_parameter_matrix_H_ready"] is True, "controlled H ready")
    require(h_packet["strict_selected_radial_source_emitted"] is False, "strict radial overclaim")

    require(gate["matrix_functional_search_completed"] is True, "gate search")
    require(gate["accepted_profile_matrix_H_radial_sources"] == 0, "gate accepted scalar")
    require(gate["strict_phi_Omega_promoted"] is True, "phase not promoted")
    require(gate["strict_r_H_promoted"] is False, "radial overpromoted")
    require(gate["strict_H_source_row_emitted"] is False, "strict H overclaim")
    require(gate["direct_K_threshold_Omega_H_lambda_emitted"] is False, "direct K overclaim")
    require(gate["minimal_one_parameter_H_parameter_count"] == 1, "parameter count")

    decision = data["closure_decision"]
    require(decision["profile_matrix_scalar_functionals_tested"] == len(scalar["functionals"]), "decision count")
    require(decision["accepted_profile_matrix_H_radial_sources"] == 0, "decision accepted")
    require(decision["controlled_Herm2_numerics_verified"] is True, "decision H numerics")
    require(decision["controlled_one_parameter_matrix_H_ready"] is True, "decision one-param")
    require(decision["strict_phi_Omega_promoted"] is True, "decision phase")
    require(decision["strict_r_H_promoted"] is False, "decision radial")
    require(decision["strict_no_knob_H_closed"] is False, "decision strict")

    for phrase in [
        "Qutrit27HFunctionalSearchAndRadialFrontierTheorem",
        "Accepted as strict H radial sources: `0`",
        "strict_phi_Omega_promoted = True",
        "selected r_H / direct N_H / non-Higgs UP-RET-OVERLAP.HRG prediction",
        NEXT,
    ]:
        require(phrase in note, f"note missing {phrase}")

    print("AUDIT_PASS: qutrit27 H functional search rejects matrix scalars; controlled H ready; radial source open.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
