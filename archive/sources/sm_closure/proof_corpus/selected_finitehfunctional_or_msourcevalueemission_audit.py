"""Audit finite H functional or M_source value emission packet."""

from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SLUG = "selected_finitehfunctional_or_msourcevalueemission"
BASE = ROOT / "candidate_data" / SLUG
CANDIDATE = ROOT / "candidate_data" / f"{SLUG}.candidate.json"
CERT = ROOT / "certificates" / f"{SLUG}_certificate.json"
NOTE = ROOT / "proof_corpus" / "MTT_Selected_FiniteHFunctionalOrMSourceValueEmission_v1.md"
BUILD = ROOT / "scripts" / f"build_{SLUG}.py"

INVENTORY = BASE / "finiteh_msource_kh_source_inventory.packet.json"
POLAR = BASE / "polar_reduced_value_executor.packet.json"
EXECUTION = BASE / "finiteh_msource_kh_value_execution_attempt.packet.json"
CUTSET = BASE / "next_cutset_after_finiteh_msource_execution.packet.json"

STATUS = (
    "MTT_SELECTED_FINITEHFUNCTIONAL_OR_MSOURCEVALUEEMISSION_"
    "EXECUTED_ZERO_ROWS_POLAR_SOURCE_FIELDS_OPEN"
)
NEXT = "MTT_Selected_HRadialPhaseTraceSource_or_FiniteHActionEmission_v1"


def load(path: Path):
    return json.loads(path.read_text(encoding="utf-8"))


def require(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)


def require_no_selector(packet: dict, label: str) -> None:
    require(packet.get("observed_data_used_as_selector") is False, f"{label}: observed selector")
    require(packet.get("target_fitting_used") is False, f"{label}: target fitting")


def main() -> int:
    proc = subprocess.run([sys.executable, str(BUILD)], cwd=ROOT, text=True, capture_output=True)
    if proc.returncode:
        print(proc.stdout)
        print(proc.stderr)
        return proc.returncode

    candidate = load(CANDIDATE)
    cert = load(CERT)
    inventory = load(INVENTORY)
    polar = load(POLAR)
    execution = load(EXECUTION)
    cutset = load(CUTSET)
    note = NOTE.read_text(encoding="utf-8")

    require(candidate["status"] == STATUS, "candidate status")
    require(candidate["next_required_artifact"] == NEXT, "candidate next")
    require(candidate["closure_claimed"] is True, "candidate closure")
    require(candidate["theorem"]["proved"] is True, "candidate theorem")
    require(candidate["true_SM_equivalence_claimed"] is False, "true SM overclaim")
    require(candidate["full_no_knob_closure_claimed"] is False, "no-knob overclaim")
    require_no_selector(candidate, "candidate")

    decision = candidate["closure_decision"]
    for key in [
        "strict_F_H_M_source_K_H_inventory_executed",
        "polar_reduction_executed",
        "controlled_lane_separated",
        "selected_s_beta_polar_angle_closed",
    ]:
        require(decision[key] is True, f"decision true {key}")
    for key in [
        "selected_F_H_functional_emitted",
        "selected_M_source_value_emitted",
        "selected_K_H_emitted",
        "strict_radial_scale_source_emitted",
        "selected_Delta_sign_emitted",
        "selected_Omega_phase_emitted",
        "trace_center_source_or_normalization_emitted",
        "selected_H_response_value_rows_emitted",
        "true_SM_equivalence_closed",
        "full_no_knob_closed",
    ]:
        require(decision[key] is False, f"decision false {key}")

    nums = candidate["key_numbers"]
    require(nums["accepted_strict_source_route_count"] == 0, "accepted route count")
    require(nums["accepted_value_row_count"] == 0, "accepted row count")
    require(nums["accepted_final_certificate_count"] == 0, "accepted cert count")
    require(nums["selected_s_beta_value"] == 0.004701083905943647, "s_beta")
    require(nums["strict_unknown_scalar_source_fields"] == 4, "unknown field count")

    require(cert["status"] == STATUS, "cert status")
    require(cert["next_required_artifact"] == NEXT, "cert next")
    require(cert["theorem_proved"] is True, "cert theorem")
    for key in [
        "true_SM_equivalence_claimed",
        "full_no_knob_closure_claimed",
        "observed_data_used_as_selector",
        "target_fitting_used",
        "selected_F_H_functional_emitted",
        "selected_M_source_value_emitted",
        "selected_K_H_emitted",
        "selected_H_response_value_rows_emitted",
    ]:
        require(cert[key] is False, f"cert false {key}")

    require(inventory["status"] == "FINITE_H_MSOURCE_KH_SOURCE_INVENTORY_EXECUTED_ZERO_ACCEPTED", "inventory status")
    strict = inventory["strict_routes"]
    require(set(strict) == {"finite_H_functional_F_H", "same_source_M_source", "primitive_H_response_kernel_K_H"}, "strict route set")
    for route in strict.values():
        require(route["accepted"] is False, "strict route accepted")
    require(inventory["controlled_lane_not_strict"]["available"] is True, "controlled lane")
    require(inventory["controlled_lane_not_strict"]["accepted_as_no_knob_source"] is False, "controlled promoted")
    require(inventory["decision"]["accepted_strict_source_route_count"] == 0, "inventory accepted")
    require_no_selector(inventory, "inventory")

    require(polar["status"] == "POLAR_VALUE_EXECUTOR_REDUCED_TO_SELECTED_SCALAR_FIELDS", "polar status")
    pdata = polar["selected_angle_data"]
    require(pdata["selected_s_beta_polar_angle_closed"] is True, "polar angle")
    require(pdata["s_beta"] == 0.004701083905943647, "polar s_beta")
    unknown = polar["strict_unknown_source_fields"]
    for key in ["r_H", "sigma_D", "phi_Omega", "m0", "certificates"]:
        require(key in unknown, f"unknown {key}")
    pdec = polar["decision"]
    require(pdec["polar_reduction_executed"] is True, "polar executed")
    for key in [
        "strict_radial_scale_source_emitted",
        "selected_Delta_sign_emitted",
        "selected_Omega_phase_emitted",
        "trace_center_source_or_normalization_emitted",
        "full_H_response_rows_executable",
        "tracefree_threshold_block_executable",
    ]:
        require(pdec[key] is False, f"polar false {key}")
    require_no_selector(polar, "polar")

    require(execution["status"] == "FINITE_H_MSOURCE_KH_VALUE_EXECUTION_ZERO_ROWS", "execution status")
    edec = execution["decision"]
    require(edec["execution_attempted"] is True, "execution attempted")
    require(edec["accepted_value_row_count"] == 0, "execution rows")
    require(edec["accepted_final_certificate_count"] == 0, "execution certs")
    require(edec["accepted_strict_source_route_count"] == 0, "execution routes")
    require(edec["strict_no_knob_H_closure"] is False, "strict closure")
    for value in execution["emitted_rows"].values():
        require(value is None, "row emitted")
    require_no_selector(execution, "execution")

    require(
        cutset["status"] == "NEXT_FRONTIER_H_RADIAL_PHASE_TRACE_SOURCE_OR_FINITE_H_ACTION_EMISSION",
        "cutset status",
    )
    require(cutset["next_required_artifact"] == NEXT, "cutset next")
    for phrase in [
        "strict F_H/M_source/K_H route inventory executed",
        "selected s_beta polar reduction imported into Huv row executor",
        "controlled HRG radial calibration separated from strict no-knob source",
        "remaining row fields reduced to r_H, sigma_D, phi_Omega, m0/quotient trace, and certificates",
    ]:
        require(phrase in cutset["closed_here"], f"closed {phrase}")
    for phrase in [
        "selected finite H action/functional F_H emitting the Herm(2) Hessian",
        "or selected same-source Hermitian M_source values",
        "or selected primitive H-response kernel K_H",
        "or selected polar source fields r_H, sigma_D, phi_Omega, and m0/trace theorem",
    ]:
        require(phrase in cutset["still_open"], f"open {phrase}")
    require_no_selector(cutset, "cutset")

    for phrase in [
        "selected finite H functional `F_H`: `0` accepted",
        "selected same-source Hermitian `M_source`: `0` accepted",
        "selected primitive H-response kernel `K_H`: `0` accepted",
        "s_beta = 0.004701083905943647",
        "r_H",
        "phi_Omega",
        NEXT,
    ]:
        require(phrase in note, f"note missing {phrase}")

    print(
        "AUDIT_PASS: F_H/M_source/K_H inventory executed; selected s_beta reduces "
        "rows to radial/sign/phase/trace fields, but zero strict rows emit."
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
