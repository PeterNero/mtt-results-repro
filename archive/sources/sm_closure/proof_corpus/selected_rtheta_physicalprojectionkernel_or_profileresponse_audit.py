"""Audit R_theta physical projection kernel / profile response gate."""

from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SLUG = "selected_rtheta_physicalprojectionkernel_or_profileresponse"
DATA = ROOT / "candidate_data" / f"{SLUG}.candidate.json"
PACKET_DIR = ROOT / "candidate_data" / SLUG
INPUT_RECONCILIATION = PACKET_DIR / "projection_input_reconciliation.packet.json"
KERNEL_ATTEMPT = PACKET_DIR / "pi_rtheta_kernel_attempt.packet.json"
PROFILE_GATE = PACKET_DIR / "profile_response_recheck.packet.json"
DECISION = PACKET_DIR / "physical_projection_kernel_decision.packet.json"
CUTSET = PACKET_DIR / "next_cutset_after_projection_kernel_attempt.packet.json"
CERT = ROOT / "certificates" / f"{SLUG}_certificate.json"
NOTE = ROOT / "proof_corpus" / "MTT_Selected_RThetaPhysicalProjectionKernel_or_ProfileResponse_v1.md"
BUILDER = ROOT / "scripts" / f"build_{SLUG}.py"

STATUS = (
    "MTT_SELECTED_RTHETAPHYSICALPROJECTIONKERNEL_OR_PROFILERESPONSE_"
    "BUILT_INPUTS_RECONCILED_SELECTED_SOLVE_OPEN"
)
NEXT = "MTT_Selected_RThetaSelectedRouteCGalerkinSolve_or_DiagonalProfileTheorem_v1"


def load(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def require(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)


def main() -> int:
    subprocess.run([sys.executable, str(BUILDER)], cwd=ROOT, check=True)

    data = load(DATA)
    cert = load(CERT)
    inputs = load(INPUT_RECONCILIATION)
    kernel = load(KERNEL_ATTEMPT)
    profile = load(PROFILE_GATE)
    decision = load(DECISION)
    cutset = load(CUTSET)
    note = NOTE.read_text(encoding="utf-8")

    require(data["status"] == STATUS, "candidate status mismatch")
    require(cert["status"] == STATUS, "certificate status mismatch")
    require(data["next_required_artifact"] == NEXT, "candidate next mismatch")
    require(cert["next_required_artifact"] == NEXT, "certificate next mismatch")
    for key in [
        "closure_claimed",
        "unpatched_theorem_closure_claimed",
        "observed_data_used_as_selector",
        "target_fitting_used",
    ]:
        require(data[key] is False, f"candidate guardrail overclaimed: {key}")

    require(
        inputs["status"] == "PROJECTION_INPUTS_RECONCILED_SELECTED_SOLVE_STILL_OPEN",
        "input reconciliation status mismatch",
    )
    for key in [
        "q79_polarization_A4",
        "block_family_Higgs_projector_retention",
        "stationary_projector_source_verified",
        "sector_projectors_on_27_mode_BN_emitted",
        "projectors_idempotent_and_hermitian",
    ]:
        require(inputs["closed_inputs"][key] is True, f"closed input missing: {key}")
    require(inputs["closed_inputs"]["U10_Ubar5_outputs"]["U_10"] == "I_3", "U10 mismatch")
    require(inputs["closed_inputs"]["U10_Ubar5_outputs"]["U_bar5"] == "F", "Ubar5 mismatch")
    require(
        inputs["not_closed_inputs"]["selected_RouteC_Strominger_Galerkin_residual_solve"]
        is True,
        "selected solve overclosed",
    )
    require(
        inputs["not_closed_inputs"]["coherent_spectral_projector_retention"] is False,
        "coherent spectral projector unexpectedly closed",
    )
    require(inputs["not_closed_inputs"]["selected_DE_Riesz_Green_dotD_values"] is False, "DE/Riesz/Green/dotD overclosed")
    require(inputs["not_closed_inputs"]["honest_sector_projector_dotD_replay"] is False, "honest replay overclosed")
    require(inputs["input_reconciliation_closed"] is True, "input reconciliation not closed")
    require(inputs["closure_claimed"] is False, "input reconciliation overclaimed")

    require(
        kernel["status"] == "PI_RTHETA_KERNEL_ATTEMPTED_SELECTED_SOLVE_REQUIRED",
        "kernel status mismatch",
    )
    tests = kernel["component_tests"]
    for key in [
        "static_block_projectors_available",
        "q79_polarization_available",
        "sector_projector_matrices_available",
        "stationary_projector_source_verified",
    ]:
        require(tests[key] is True, f"kernel positive component missing: {key}")
    for key in [
        "coherent_spectral_projectors_available",
        "selected_routec_solve_available",
        "honest_sector_projector_dotd_replay",
    ]:
        require(tests[key] is False, f"kernel blocker overclosed: {key}")
    require(kernel["slot_count"] == 10, "wrong Pi slot count")
    require(kernel["closed_slot_count"] == 0, "Pi slots overclosed")
    require(kernel["Pi_Rtheta_closed"] is False, "Pi_Rtheta overclosed")
    require(
        kernel["minimal_internal_missing_object"] == "SelectedRouteCStromingerGalerkinResidualSolve",
        "wrong minimal missing object",
    )
    for row in kernel["slot_rows"]:
        require(row["physical_projection_kernel_closed_for_slot"] is False, f"slot overclosed: {row['slot_id']}")
        require("selected Route-C/Strominger Galerkin residual solve is not emitted" in row["why_not_closed"], f"slot missing solve reason: {row['slot_id']}")
    require(kernel["closure_claimed"] is False, "kernel overclaimed")

    require(
        profile["status"] == "PROFILE_RESPONSE_RECHECKED_FULL_WORKSPACE_OR_DIAGONAL_THEOREM_OPEN",
        "profile status mismatch",
    )
    require(profile["external_profile_workspace_imported"] is False, "external profile overimported")
    require(profile["accepted_diagonal_limitation_theorem_present"] is False, "diagonal theorem overaccepted")
    require(profile["profile_response_closed"] is False, "profile response overclosed")
    require(profile["closure_claimed"] is False, "profile overclaimed")

    require(
        decision["status"] == "PROJECTION_INPUTS_CLOSED_PI_RTHETA_AND_PROFILE_RESPONSE_OPEN",
        "decision status mismatch",
    )
    require(decision["projection_input_reconciliation_closed"] is True, "decision input reconciliation not closed")
    for key in [
        "Pi_Rtheta_closed",
        "profile_response_closed",
        "rtheta_packet_constructed",
        "selected_threshold_response_functional_instantiated",
        "true_SM_equivalence_closed",
        "full_no_knob_closed",
    ]:
        require(decision[key] is False, f"decision overclosed: {key}")
    require(len(decision["active_frontier"]) == 3, "decision frontier should have three obligations")
    require(decision["closure_claimed"] is False, "decision overclaimed")

    require(cutset["recommended_next"]["artifact"] == NEXT, "cutset next mismatch")
    require(cutset["closed_now"]["projection_input_reconciliation"] is True, "cutset missing input closure")
    require(cutset["closed_now"]["Pi_Rtheta_attempt_without_overclaim"] is True, "cutset missing Pi attempt")
    require(len(cutset["still_open"]) == 3, "cutset frontier should have three obligations")
    require(cutset["closure_claimed"] is False, "cutset overclaimed")

    final = data["closure_decision"]
    require(final["projection_input_reconciliation_closed"] is True, "candidate final input reconciliation not closed")
    for key in [
        "Pi_Rtheta_closed",
        "profile_response_closed",
        "selected_threshold_response_functional_instantiated",
        "true_SM_equivalence_closed",
        "full_no_knob_closed",
    ]:
        require(final[key] is False, f"candidate final overclosed: {key}")
    require(data["theorem"]["proved"] is True, "theorem not proved")
    require(cert["theorem_proved"] is True, "certificate theorem missing")
    require(cert["projection_input_reconciliation_closed"] is True, "certificate input closure missing")
    require(cert["Pi_Rtheta_closed"] is False, "certificate Pi overclosed")
    require(cert["profile_response_closed"] is False, "certificate profile overclosed")
    require("Pi_Rtheta closed             : false" in note, "note missing Pi false guard")
    require("closed projection slots      : 0/10" in note, "note missing slot guard")

    print(f"PASS {DATA.name}: {STATUS}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
