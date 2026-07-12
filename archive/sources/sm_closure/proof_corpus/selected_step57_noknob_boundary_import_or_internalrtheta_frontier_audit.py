"""Audit Step57 no-knob boundary import / internal Rtheta frontier."""

from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SLUG = "selected_step57_noknob_boundary_import_or_internalrtheta_frontier"
DATA = ROOT / "candidate_data" / f"{SLUG}.candidate.json"
PACKET_DIR = ROOT / "candidate_data" / SLUG
BOUNDARY_IMPORT = PACKET_DIR / "step57_noknob_boundary_import.packet.json"
POLICY_RECHECK = PACKET_DIR / "step57_minimal_policy_recheck.packet.json"
CUTSET = PACKET_DIR / "step57_internal_rtheta_frontier.packet.json"
CERT = ROOT / "certificates" / f"{SLUG}_certificate.json"
NOTE = ROOT / "proof_corpus" / "MTT_Selected_Step57_NoKnobBoundaryImport_or_InternalRThetaFrontier_v1.md"
BUILDER = ROOT / "scripts" / f"build_{SLUG}.py"

STATUS = "MTT_SELECTED_STEP57_NOKNOB_BOUNDARY_IMPORTED_INTERNAL_RTHETA_FRONTIER_OPEN"
NEXT = "MTT_Selected_InternalRThetaValueDerivation_or_MinimalUniversalParameterSelection_v1"


def load(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def require(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)


def main() -> int:
    subprocess.run([sys.executable, str(BUILDER)], cwd=ROOT, check=True)

    data = load(DATA)
    boundary = load(BOUNDARY_IMPORT)
    policy = load(POLICY_RECHECK)
    cutset = load(CUTSET)
    cert = load(CERT)
    note = NOTE.read_text(encoding="utf-8")

    require(data["status"] == STATUS, "candidate status mismatch")
    require(cert["status"] == STATUS, "certificate status mismatch")
    require(data["next_required_artifact"] == NEXT, "candidate next mismatch")
    require(cert["next_required_artifact"] == NEXT, "certificate next mismatch")
    require(data["theorem"]["proved"] is True, "Step57 theorem not proved")
    require(cert["theorem_proved"] is True, "certificate theorem missing")

    for packet in [data, boundary, policy, cutset, cert]:
        require(packet.get("observed_data_used_as_selector") is False, "observed selector violation")
        require(packet.get("target_fitting_used") is False, "target fitting violation")

    require(boundary["post_pi_external_replay_ready"] is True, "external replay boundary not ready")
    require(boundary["SM_parity_external_replay_boundary_declared"] is True, "SM-parity boundary missing")
    require(boundary["Rtheta_readiness_present_count"] == 8, "boundary readiness present mismatch")
    require(boundary["Rtheta_readiness_requirement_count"] == 9, "boundary readiness requirement mismatch")
    require(boundary["only_remaining_readiness_blocker"] == "no_knob_value_derivation", "wrong blocker")
    require(boundary["selected_internal_value_emission_count"] == 0, "internal emissions overclaimed")
    require(boundary["accepted_coefficient_value_count"] == 0, "coefficient rows overclaimed")
    require(boundary["no_knob_value_derivation_closed"] is False, "no-knob overclosed")
    require(boundary["true_SM_equivalence_closed"] is False, "true SM overclosed")
    require(boundary["full_no_knob_closed"] is False, "full no-knob overclosed")
    require(boundary["closure_claimed"] is False, "boundary packet overclaimed")

    require(policy["selected_universal_parameter_count"] == 0, "universal parameter overselected")
    require(policy["maximum_live_universal_parameters"] == 3, "max universal count mismatch")
    require(policy["minimal_universal_parameter_selection_closed"] is False, "minimal policy overclosed")
    require(policy["candidate_specific_source_theorem_present"] is False, "source theorem overclaimed")
    require(policy["external_replay_policy_ready"] is True, "external replay policy not ready")
    require(policy["external_replay_policy_is_no_knob"] is False, "external replay treated as no-knob")
    require(policy["closure_claimed"] is False, "policy packet overclaimed")

    require(cutset["status"] == "FINAL_NUMBERED_FRONTIER_INTERNAL_RTHETA_OR_MINIMAL_SOURCE_ANCHOR", "cutset status mismatch")
    for key in [
        "post_pi_final_no_knob_recheck",
        "SM_parity_external_replay_boundary_declared",
        "minimal_universal_parameter_policy_matrix_built",
        "Rtheta_readiness_fixed_at_8_of_9",
        "basis_vs_coefficient_distinction_preserved",
        "post_pi_external_replay_boundary_imported_into_numbered_plan",
        "minimal_policy_matrix_imported_into_numbered_plan",
    ]:
        require(cutset["closed_now"][key] is True, f"cutset closure missing: {key}")
    for key in [
        "no_knob_value_derivation",
        "selected_internal_Rtheta_threshold_mass_derivation",
        "selected_threshold_response_functional_instantiated",
        "numeric_Rtheta_coefficient_values",
        "lambda_H_value_execution",
        "Yukawa_mass_mixing_value_closure",
        "minimal_universal_parameter_selection",
        "candidate_specific_universal_source_theorem",
        "true_SM_equivalence",
        "full_no_knob",
    ]:
        require(cutset["still_open"][key] is True, f"cutset overclosed: {key}")
    require(cutset["recommended_next"]["artifact"] == NEXT, "cutset next mismatch")
    require(cutset["closure_claimed"] is False, "cutset overclaimed")

    decision = data["closure_decision"]
    for key in [
        "post_pi_external_replay_ready",
        "SM_parity_external_replay_boundary_declared",
    ]:
        require(decision[key] is True, f"candidate closure missing: {key}")
        require(cert[key] is True, f"certificate closure missing: {key}")
    require(decision["Rtheta_readiness_present_count"] == 8, "candidate readiness present mismatch")
    require(decision["Rtheta_readiness_requirement_count"] == 9, "candidate readiness requirement mismatch")
    require(decision["only_remaining_readiness_blocker"] == "no_knob_value_derivation", "candidate blocker mismatch")
    for key in [
        "selected_internal_value_emission_count",
        "accepted_internal_Rtheta_coefficient_row_count",
        "accepted_internal_scalar_row_count",
        "selected_universal_parameter_count",
    ]:
        require(decision[key] == 0, f"candidate count overclaimed: {key}")
        require(cert[key] == 0, f"certificate count overclaimed: {key}")
    for key in [
        "minimal_universal_parameter_selection_closed",
        "candidate_specific_universal_source_theorem_present",
        "no_knob_value_derivation_closed",
        "selected_threshold_response_functional_instantiated",
        "accepted_lambda_H_value",
        "Yukawa_mass_mixing_value_closure",
        "true_SM_equivalence_closed",
        "full_no_knob_closed",
    ]:
        require(decision[key] is False, f"candidate overclosed: {key}")
        require(cert[key] is False, f"certificate overclosed: {key}")
    require(data["minimal_parameter_closure_claimed"] is False, "minimal closure overclaimed")
    require(data["true_SM_equivalence_claimed"] is False, "true SM overclaimed")
    require(data["full_no_knob_closure_claimed"] is False, "full no-knob overclaimed")

    for phrase in [
        "post-Pi external replay ready          : true",
        "Rtheta readiness                       : 8/9",
        "only remaining readiness blocker       : no_knob_value_derivation",
        "selected internal no-knob rows         : 0",
        "selected universal parameters          : 0",
        NEXT,
    ]:
        require(phrase in note, f"note missing phrase: {phrase}")

    print(f"PASS {DATA.name}: {STATUS}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
