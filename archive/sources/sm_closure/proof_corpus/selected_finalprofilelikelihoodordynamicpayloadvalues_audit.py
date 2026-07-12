"""Audit final profile-likelihood or dynamic-payload values frontier."""

from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
SLUG = "selected_finalprofilelikelihoodordynamicpayloadvalues"
BUILDER = ROOT / "scripts" / f"build_{SLUG}.py"
CANDIDATE = ROOT / "candidate_data" / f"{SLUG}.candidate.json"
PACKET_DIR = ROOT / "candidate_data" / SLUG
PROFILE = PACKET_DIR / "profile_likelihood_route_status.packet.json"
DYNAMIC = PACKET_DIR / "dynamic_payload_value_readiness.packet.json"
EXIT = PACKET_DIR / "final_dynamic_payload_theorem_exit.packet.json"
CERT = ROOT / "certificates" / f"{SLUG}_certificate.json"
NOTE = ROOT / "proof_corpus" / "MTT_Selected_FinalProfileLikelihoodOrDynamicPayloadValues_v1.md"

STATUS = (
    "MTT_SELECTED_FINALPROFILELIKELIHOODORDYNAMICPAYLOADVALUES_"
    "PROFILE_ROUTE_OPEN_DYNAMIC_PAYLOAD_REDUCED_TO_TWO_THEOREMS"
)
NEXT_ARTIFACT = "MTT_Selected_PhiFinC1SourceEmissionOrFiniteRowIndependenceTheorem_v1"


def require(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)


def load(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def guard(packet: dict[str, Any], label: str) -> None:
    require(packet.get("closure_claimed") is True, f"{label} closure")
    require(packet.get("observed_data_used_as_selector") is False, f"{label} observed selector")
    require(packet.get("target_fitting_used") is False, f"{label} target fitting")


def main() -> int:
    subprocess.run([sys.executable, str(BUILDER)], cwd=ROOT, check=True)

    candidate = load(CANDIDATE)
    profile = load(PROFILE)
    dynamic = load(DYNAMIC)
    exit_packet = load(EXIT)
    cert = load(CERT)
    note = NOTE.read_text(encoding="utf-8")

    for label, packet in [
        ("candidate", candidate),
        ("profile", profile),
        ("dynamic", dynamic),
        ("exit", exit_packet),
        ("cert", cert),
    ]:
        guard(packet, label)

    require(candidate["status"] == STATUS, "candidate status")
    require(cert["status"] == STATUS, "cert status")
    require(candidate["theorem"]["proved"] is True, "candidate theorem")
    require(candidate["theorem"]["name"] == "FinalProfileLikelihoodOrDynamicPayloadValuesTheorem", "theorem name")
    require(cert["theorem_proved"] is True, "cert theorem")
    require(candidate["next_required_artifact"] == NEXT_ARTIFACT, "candidate next")
    require(exit_packet["next_required_artifact"] == NEXT_ARTIFACT, "exit next")
    require(cert["next_required_artifact"] == NEXT_ARTIFACT, "cert next")

    require(profile["status"] == "PROFILE_ROUTE_SUPPORT_PRESENT_FULL_LIKELIHOOD_OPEN", "profile status")
    require(profile["imported_profile_replay_closed"] is True, "profile replay")
    require(profile["accepted_as_SM_parity_covariance_replay"] is True, "parity replay")
    require(profile["surrogate_profile_matrix_reconstructed"] is True, "surrogate profile")
    require(profile["accepted_as_official_LHCHXSWG_likelihood"] is False, "official likelihood overclaim")
    require(profile["accepted_as_full_profile"] is False, "full profile overclaim")
    require(profile["actual_QaSU3_packet_found"] is False, "QaSU3 packet found overclaim")

    require(dynamic["status"] == "DYNAMIC_VALUES_READY_SOURCE_RULE_OR_EXPORT_OPEN", "dynamic status")
    require(dynamic["dynamic_values_ready"] is True, "dynamic values")
    require(dynamic["conditional_hessian_values_attached"] is True, "conditional Hessian")
    require(dynamic["exact_phase_R_Z_candidate_table_emitted"] is True, "R_Z table")
    require(dynamic["exact_shift_R_X_candidate_table_emitted"] is True, "R_X table")
    require(dynamic["source_rule_or_galerkin_export_is_only_remaining_dynamic_gate"] is True, "remaining dynamic gate")
    require(dynamic["source_rule_proved"] is False, "source rule overclaim")
    require(dynamic["honest_galerkin_table_exported"] is False, "Galerkin export overclaim")
    require(dynamic["value_slots_manifest_built"] is True, "value manifest")
    require(dynamic["route_a_values_emitted"] is False, "route A values overemitted")
    require(dynamic["route_b_rows_executed"] is False, "route B rows overexecuted")
    require(dynamic["first_primitive_seed_value_exact"] is True, "primitive seed")
    require(dynamic["primitive_exactness_backimported"] is True, "primitive backimport")
    require(dynamic["first_value_row_promoted_to_selected_dynamic_source"] is False, "first row overpromoted")

    require(exit_packet["status"] == "DYNAMIC_PAYLOAD_REDUCED_TO_TWO_UNPATCHED_THEOREMS", "exit status")
    require(exit_packet["route_A_actual_attempt_rejected"] is True, "route A rejection")
    require(exit_packet["route_B_actual_attempt_rejected"] is True, "route B rejection")
    require(exit_packet["local_principle_route_A_validates"] is True, "local principle")
    require(exit_packet["final_two_unpatched_theorem_targets_named"] is True, "two theorem targets")
    require(exit_packet["remaining_theorem_targets"] == [
        "SelectedPhiFinC1PhysicalSourceEmissionTheorem",
        "SelectedFiniteC1RowSourceIndependenceTheorem",
    ], "remaining theorem targets")
    require(exit_packet["independent_Galerkin_value_requirements_are_exact"] is True, "Galerkin reqs exact")
    require(exit_packet["minimal_orthogonal_completion_principle_is_sufficient_if_derived"] is True, "orth completion")
    require(exit_packet["unpatched_PSM_C1_02_closed"] is False, "unpatched overclosed")
    require(exit_packet["true_SM_equivalence_closed"] is False, "true SM overclosed")

    decision = candidate["closure_decision"]
    require(decision["final_profile_or_dynamic_payload_frontier_executed"] is True, "decision executed")
    require(decision["profile_route_support_present"] is True, "decision profile support")
    require(decision["dynamic_values_ready"] is True, "decision dynamic")
    require(decision["conditional_hessian_values_attached"] is True, "decision Hessian")
    require(decision["first_primitive_seed_value_exact"] is True, "decision seed")
    require(decision["primitive_exactness_backimported"] is True, "decision primitive")
    require(decision["source_rule_or_galerkin_export_is_only_remaining_dynamic_gate"] is True, "decision gate")
    require(decision["route_A_actual_attempt_rejected"] is True, "decision route A reject")
    require(decision["route_B_actual_attempt_rejected"] is True, "decision route B reject")
    require(decision["final_two_unpatched_theorem_targets_named"] is True, "decision theorem targets")
    for key in [
        "full_profile_likelihood_closed",
        "accepted_as_official_LHCHXSWG_likelihood",
        "source_rule_proved",
        "honest_galerkin_table_exported",
        "selected_PhiFinC1_physical_source_emission_theorem_closed",
        "selected_finite_C1_row_source_independence_theorem_closed",
        "actual_dynamic_QaSU3_payload_values_closed",
        "true_SM_equivalence_closed",
        "full_no_knob_closed",
    ]:
        require(decision[key] is False, f"{key} overclosed")

    for phrase in [
        "profile replay support present                    true",
        "accepted full profile likelihood                  false",
        "dynamic values ready                              true",
        "source rule proved                                false",
        "final two theorem targets named                   true",
        "SelectedPhiFinC1PhysicalSourceEmissionTheorem",
        "SelectedFiniteC1RowSourceIndependenceTheorem",
        NEXT_ARTIFACT,
    ]:
        require(phrase in note, f"note missing {phrase}")

    print(f"PASS {CANDIDATE.name}: {STATUS}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
